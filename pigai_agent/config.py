from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


def _as_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    pigai_account: str
    pigai_password: str
    essay_id: str
    openai_api_key: str
    openai_model: str
    target_score: float
    max_rounds: int
    headless: bool

    @classmethod
    def from_env(cls) -> "Settings":
        required = {
            "PIGAI_ACCOUNT": os.getenv("PIGAI_ACCOUNT", "").strip(),
            "PIGAI_PASSWORD": os.getenv("PIGAI_PASSWORD", "").strip(),
            "PIGAI_ESSAY_ID": os.getenv("PIGAI_ESSAY_ID", "").strip(),
            "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", "").strip(),
        }
        missing = [k for k, v in required.items() if not v]
        if missing:
            raise RuntimeError("Missing required environment variables: " + ", ".join(missing))

        return cls(
            pigai_account=required["PIGAI_ACCOUNT"],
            pigai_password=required["PIGAI_PASSWORD"],
            essay_id=required["PIGAI_ESSAY_ID"],
            openai_api_key=required["OPENAI_API_KEY"],
            openai_model=os.getenv("OPENAI_MODEL", "gpt-5.6").strip() or "gpt-5.6",
            target_score=float(os.getenv("TARGET_SCORE", "95")),
            max_rounds=max(1, int(os.getenv("MAX_ROUNDS", "8"))),
            headless=_as_bool("HEADLESS", False),
        )
