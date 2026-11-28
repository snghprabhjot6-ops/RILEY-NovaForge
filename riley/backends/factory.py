from __future__ import annotations

from .base import ConversationBackend
from .echo import EchoBackend
from .local import LocalBackend
from .ollama import OllamaBackend
from ..config import Settings


def create_backend(name: str, settings: Settings | None = None) -> ConversationBackend:
    if name == "ollama":
        config = settings or Settings.from_env()
        return OllamaBackend(config.ollama_url, config.ollama_model)
    backends: dict[str, type[ConversationBackend]] = {"local": LocalBackend, "echo": EchoBackend}
    try:
        return backends[name]()
    except KeyError as exc:
        raise ValueError(f"Unknown backend: {name}") from exc
