from __future__ import annotations

from collections.abc import Sequence

from ..models import Message
from .base import ConversationBackend


class EchoBackend(ConversationBackend):
    """Predictable development backend used for testing integrations."""

    def generate(self, messages: Sequence[Message], language: str) -> str:
        latest = next((message.content for message in reversed(messages) if message.role == "user"), "")
        return f"You said: {latest}"
