from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class SentenceReview:
    sentence: str = ""
    category: str = ""
    level: str = "info"
    target: str = ""
    comment: str = ""


@dataclass
class PigaiFeedback:
    score: float | None = None
    rank: int | None = None
    total_students: int | None = None
    highest_score: float | None = None
    lowest_score: float | None = None
    dimensions: dict[str, float | None] = field(default_factory=dict)
    overall_comment: str = ""
    word_count: int | None = None
    submission_count: int | None = None
    sentence_reviews: list[SentenceReview] = field(default_factory=list)
    highlights: list[str] = field(default_factory=list)
    suggestions: list[str] = field(default_factory=list)
    page_url: str = ""
    raw_text: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
