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
    headless: bool

    @classmethod
    def from_env(cls) -> "Settings":
        required = {
            "PIGAI_ACCOUNT": os.getenv("PIGAI_ACCOUNT", "").strip(),
            "PIGAI_PASSWORD": os.getenv("PIGAI_PASSWORD", "").strip(),
            "PIGAI_ESSAY_ID": os.getenv("PIGAI_ESSAY_ID", "").strip(),
        }
        missing = [key for key, value in required.items() if not value]
        if missing:
            raise RuntimeError(
                "Missing required environment variables: " + ", ".join(missing)
            )

        return cls(
            pigai_account=required["PIGAI_ACCOUNT"],
            pigai_password=required["PIGAI_PASSWORD"],
            essay_id=required["PIGAI_ESSAY_ID"],
            headless=_as_bool("HEADLESS", False),
        )
