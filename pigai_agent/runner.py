from __future__ import annotations

import json
import re
from pathlib import Path

from .ai import EssayOptimizer
from .browser import PigaiClient
from .config import Settings


def _word_limits(requirements: str) -> tuple[int | None, int | None]:
    min_words = max_words = None
    m = re.search(r"at least\s+(\d+)\s+words?", requirements, re.I)
    if m:
        min_words = int(m.group(1))
    m = re.search(r"(?:no more than|at most)\s+(\d+)\s+words?", requirements, re.I)
    if m:
        max_words = int(m.group(1))
    return min_words, max_words


def run() -> None:
    settings = Settings.from_env()
    artifacts = Path("artifacts")
    artifacts.mkdir(exist_ok=True)

    optimizer = EssayOptimizer(settings.openai_api_key, settings.openai_model)

    with PigaiClient(
        account=settings.pigai_account,
        password=settings.pigai_password,
        headless=settings.headless,
    ) as pigai:
        print("[1/3] Logging in...")
        pigai.login()
        print(f"[2/3] Opening essay #{settings.essay_id}...")
        pigai.open_assignment(settings.essay_id)
        title, requirements = pigai.assignment_info()
        essay = pigai.current_essay()
        if not essay:
            initial = Path("essay.txt")
            if not initial.exists():
                raise RuntimeError(
                    "The editor is empty. Put the first draft in essay.txt, then run again."
                )
            essay = initial.read_text(encoding="utf-8").strip()

        min_words, max_words = _word_limits(requirements)
        print(f"Title: {title}")
        print(f"Target score: {settings.target_score}")
        print(f"Max rounds: {settings.max_rounds}")

        best_score = float("-inf")
        best_essay = essay

        for round_no in range(1, settings.max_rounds + 1):
            essay_path = artifacts / f"round_{round_no:02d}_essay.txt"
            essay_path.write_text(essay, encoding="utf-8")

            print(f"\n=== Round {round_no} ===")
            print(essay)
            print("\nThe next step submits this draft to Pigai for grading.")
            input("Press Enter to submit this round, or Ctrl+C to stop: ")

            pigai.submit_essay(essay)
            feedback = pigai.parse_feedback()
            pigai.screenshot(artifacts / f"round_{round_no:02d}.png")
            (artifacts / f"round_{round_no:02d}_feedback.json").write_text(
                json.dumps(feedback.to_dict(), ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

            if feedback.score is None:
                raise RuntimeError(
                    "Could not parse the score. Inspect the saved screenshot and feedback JSON; "
                    "the site selectors/parser may need updating."
                )

            print(f"Score: {feedback.score}")
            print(f"Overall comment: {feedback.overall_comment or '(not parsed)'}")
            print(f"Sentence feedback items: {len(feedback.sentence_reviews)}")

            if feedback.score > best_score:
                best_score = feedback.score
                best_essay = essay
                (artifacts / "best_essay.txt").write_text(best_essay, encoding="utf-8")
                (artifacts / "best_feedback.json").write_text(
                    json.dumps(feedback.to_dict(), ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )

            if feedback.score >= settings.target_score:
                print(f"Target reached: {feedback.score} >= {settings.target_score}. Stopping.")
                return

            if round_no == settings.max_rounds:
                break

            print("Sending the complete grader feedback to the optimizer...")
            essay = optimizer.improve(
                title=title,
                requirements=requirements,
                essay=essay,
                feedback=feedback,
                min_words=min_words,
                max_words=max_words,
            )

        print(f"Stopped after {settings.max_rounds} rounds. Best score: {best_score}")
        print("Best draft saved to artifacts/best_essay.txt")
