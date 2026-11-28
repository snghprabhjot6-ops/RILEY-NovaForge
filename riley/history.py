from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

from .models import Message


class ConversationHistory:
    """Conversation history with an atomic JSON-file persistence layer."""

    def __init__(self, path: Path, max_messages: int = 200) -> None:
        if max_messages < 1:
            raise ValueError("max_messages must be at least 1")
        self.path = path
        self.max_messages = max_messages
        self._messages: list[Message] = []

    @property
    def messages(self) -> tuple[Message, ...]:
        return tuple(self._messages)

    def add(self, message: Message) -> None:
        self._messages.append(message)
        self._messages = self._messages[-self.max_messages :]
        self.save()

    def clear(self) -> None:
        self._messages.clear()
        self.save()

    def load(self) -> None:
        if not self.path.exists():
            self._messages = []
            return
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
            if not isinstance(raw, list):
                raise ValueError("History must be a list")
            self._messages = [Message.from_dict(item) for item in raw][-self.max_messages :]
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"Could not read conversation history: {exc}") from exc

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = json.dumps([message.to_dict() for message in self._messages], ensure_ascii=False, indent=2)
        temporary_name: str | None = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="w", encoding="utf-8", dir=self.path.parent, prefix=f".{self.path.name}.", delete=False
            ) as temporary:
                temporary.write(payload)
                temporary.flush()
                os.fsync(temporary.fileno())
                temporary_name = temporary.name
            os.replace(temporary_name, self.path)
            try:
                self.path.chmod(0o600)
            except OSError:
                pass
        finally:
            if temporary_name:
                Path(temporary_name).unlink(missing_ok=True)
