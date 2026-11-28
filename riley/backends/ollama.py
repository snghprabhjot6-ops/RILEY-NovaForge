"""Local Ollama chat adapter; no API keys or third-party dependencies."""
from __future__ import annotations

import json
from collections.abc import Sequence
from urllib.error import URLError
from urllib.request import Request, build_opener, ProxyHandler, HTTPRedirectHandler

from .base import ConversationBackend
from ..exceptions import BackendError
from ..models import Message


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class OllamaBackend(ConversationBackend):
    def __init__(self, url: str = "http://127.0.0.1:11434", model: str = "llama3.2") -> None:
        self.url, self.model = url.rstrip("/"), model

    def generate(self, messages: Sequence[Message], language: str) -> str:
        languages = {"en": "English", "hi": "Hindi", "fr": "French", "es": "Spanish", "bn": "Bengali", "sa": "Sanskrit"}
        payload = {"model": self.model, "stream": False, "messages": [
            {"role": "system", "content": f"You are Riley, a warm, helpful personal AI assistant by NovaForge. Respond in {languages.get(language, 'English')}. Be honest about limitations. You cannot access apps, files or the internet or perform actions."},
            *[{"role": m.role, "content": m.content} for m in messages[-40:]],
        ]}
        request = Request(self.url + "/api/chat", data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
        try:
            # Avoid forwarding local conversations through environment proxies or redirects.
            with build_opener(ProxyHandler({}), NoRedirect()).open(request, timeout=120) as response:
                raw = response.read(2_000_001)
                if len(raw) > 2_000_000:
                    raise ValueError("Response is too large")
                result = json.loads(raw)["message"]["content"]
                if not isinstance(result, str) or not result.strip():
                    raise ValueError("Empty response")
                return result.strip()
        except (URLError, OSError, ValueError, KeyError, TypeError) as exc:
            raise BackendError(f"Could not reach Ollama model '{self.model}'. Start Ollama and run: ollama pull {self.model}") from exc
