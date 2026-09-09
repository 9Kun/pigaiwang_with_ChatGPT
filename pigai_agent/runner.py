from __future__ import annotations

import json
from pathlib import Path

from .browser import PigaiClient
from .config import Settings


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

        (artifacts / "latest_essay.txt").write_text(essay, encoding="utf-8")
        (artifacts / "latest_feedback.json").write_text(
            json.dumps(result, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        pigai.screenshot(artifacts / "latest_result.png")

        if feedback.score is None:
            raise RuntimeError(
                "Submission completed, but the score could not be parsed. "
                "Inspect artifacts/latest_feedback.json and artifacts/latest_result.png."
            )

        print("\n=== Pigai result ===")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        print("\nSaved: artifacts/latest_feedback.json")
        print("Saved: artifacts/latest_result.png")
