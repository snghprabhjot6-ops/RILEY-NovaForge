from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Literal


@dataclass(frozen=True, slots=True)
class Message:
    role: Literal["user", "assistant", "system"]
    content: str
    language: str = "en"
    created_at: str = ""

    def __post_init__(self) -> None:
        if not self.created_at:
            object.__setattr__(self, "created_at", datetime.now(timezone.utc).isoformat())
        if not self.content.strip():
            raise ValueError("Message content cannot be empty")

    def to_dict(self) -> dict[str, str]:
        return asdict(self)

    @classmethod
    def from_dict(cls, value: dict[str, str]) -> "Message":
        return cls(
            role=value["role"],
            content=value["content"],
            language=value.get("language", "en"),
            created_at=value.get("created_at", ""),
        )
