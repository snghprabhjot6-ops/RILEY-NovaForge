from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Sequence

from ..models import Message


class ConversationBackend(ABC):
    """Interface implemented by every Riley conversation backend."""

    @abstractmethod
    def generate(self, messages: Sequence[Message], language: str) -> str:
        """Return an assistant response for the supplied conversation."""
