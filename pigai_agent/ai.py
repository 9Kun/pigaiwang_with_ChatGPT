from __future__ import annotations

import json

from openai import OpenAI

from .models import PigaiFeedback


class EssayOptimizer:
    def __init__(self, api_key: str, model: str) -> None:
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def improve(
        self,
        *,
        title: str,
        requirements: str,
        essay: str,
        feedback: PigaiFeedback,
        min_words: int | None = None,
        max_words: int | None = None,
    ) -> str:
        feedback_json = json.dumps(feedback.to_dict(), ensure_ascii=False, indent=2)
        word_rule = ""
        if min_words is not None or max_words is not None:
            word_rule = f"Word-count constraints: min={min_words}, max={max_words}."

        prompt = f"""
You are revising an English essay for learning and practice.

Title:
{title}

Writing requirements:
{requirements}

Current essay:
{essay}

Detailed grader feedback:
{feedback_json}

{word_rule}

Revise the essay to address EVERY concrete grammar, collocation, coherence,
relevance, vocabulary, and sentence-level issue in the grader feedback while
preserving correct high-quality expressions. Improve weak scoring dimensions
without introducing unnatural rare words or changing the topic.

Rules:
1. Obey the title and all writing requirements exactly.
2. Keep strong expressions unless the grader flagged them.
3. Fix every explicit error and suspected error first.
4. Prefer natural advanced English over vocabulary stuffing.
5. Do not mention the grader, score, revision process, or these instructions.
6. Output ONLY the complete revised essay, with its title on the first line.
""".strip()

        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )
        text = (response.output_text or "").strip()
        if not text:
            raise RuntimeError("OpenAI returned an empty revision.")
        return text
