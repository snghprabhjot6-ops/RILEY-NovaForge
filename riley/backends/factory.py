from __future__ import annotations

from .base import ConversationBackend
from .echo import EchoBackend
from .local import LocalBackend


def create_backend(name: str) -> ConversationBackend:
    backends: dict[str, type[ConversationBackend]] = {"local": LocalBackend, "echo": EchoBackend}
    try:
        return backends[name]()
    except KeyError as exc:
        raise ValueError(f"Unknown backend: {name}") from exc
