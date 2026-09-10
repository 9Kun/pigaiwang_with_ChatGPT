from __future__ import annotations

import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

from .browser import PigaiClient
from .config import Settings


def _extract_hidden_dimensions(html: str) -> dict[str, float]:
    """Extract Pigai's four hidden bar scores from the result-page HTML."""
    soup = BeautifulSoup(html, "html.parser")
    label_to_key = {
        "词汇": "vocabulary",
        "句子": "sentence",
        "篇章结构": "structure",
        "内容相关": "relevance",
    }
    dimensions: dict[str, float] = {}

    for label_node in soup.select("div.tbL"):
        label = label_node.get_text(" ", strip=True).rstrip(":：").strip()
        key = label_to_key.get(label)
        if not key:
            continue

        row = label_node.find_parent("tr")
        if row is None:
            continue
        score_node = row.find("td", attrs={"title": re.compile(r"^0(?:\.\d+)?$|^1(?:\.0+)?$")})
        if score_node is None:
            continue

        try:
            dimensions[key] = round(float(score_node.get("title")) * 100.0, 4)
        except (TypeError, ValueError):
            continue

    return dimensions


def run() -> None:
    settings = Settings.from_env()
    artifacts = Path("artifacts")
    artifacts.mkdir(exist_ok=True)

    essay_path = Path("essay.txt")
    if not essay_path.exists():
        raise RuntimeError("Missing essay.txt. Put the draft to submit in essay.txt first.")

    essay = essay_path.read_text(encoding="utf-8").strip()
    if not essay:
        raise RuntimeError("essay.txt is empty.")

    with PigaiClient(
        account=settings.pigai_account,
        password=settings.pigai_password,
        headless=settings.headless,
    ) as pigai:
        print("[1/4] Logging in...")
        pigai.login()

        print(f"[2/4] Opening essay #{settings.essay_id}...")
        pigai.open_assignment(settings.essay_id)
        title, requirements = pigai.assignment_info()
        print(f"Title: {title}")
        if requirements:
            print(f"Requirements: {requirements}")

        print("[3/4] Submitting essay.txt for grading...")
        pigai.submit_essay(essay)

        print("[4/4] Parsing feedback...")
        feedback = pigai.parse_feedback()
        result = feedback.to_dict()
        result["dimensions"].update(_extract_hidden_dimensions(pigai.driver.page_source))

        (artifacts / "latest_essay.txt").write_text(essay, encoding="utf-8")
        (artifacts / "latest_feedback.json").write_text(
            json.dumps(result, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        (artifacts / "latest_result.html").write_text(
            pigai.driver.page_source,
            encoding="utf-8",
        )
        pigai.screenshot(artifacts / "latest_result.png")

        if feedback.score is None:
            raw = feedback.raw_text
            if "请勿重复提交" in raw:
                raise RuntimeError(
                    "Pigai rejected this round as a duplicate/insufficiently changed submission. "
                    "Change the essay materially before retrying."
                )
            raise RuntimeError(
                "Submission reached Pigai, but the score could not be parsed. "
                "Inspect artifacts/latest_feedback.json, latest_result.html and latest_result.png."
            )

        print("\n=== Pigai result ===")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        print("\nSaved: artifacts/latest_feedback.json")
        print("Saved: artifacts/latest_result.html")
        print("Saved: artifacts/latest_result.png")
