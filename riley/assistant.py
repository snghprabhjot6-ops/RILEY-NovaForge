from __future__ import annotations

import logging

from .backends.base import ConversationBackend
from .config import SUPPORTED_LANGUAGES, Settings
from .exceptions import BackendError, VoiceOutputError
from .history import ConversationHistory
from .models import Message
from .speech import SpeechInput
from .voice import VoiceOutput


class RileyAssistant:
    def __init__(
        self,
        settings: Settings,
        backend: ConversationBackend,
        history: ConversationHistory,
        voice: VoiceOutput | None = None,
        speech: SpeechInput | None = None,
    ) -> None:
        self.settings = settings
        self.backend = backend
        self.history = history
        self.voice = voice or VoiceOutput(settings.voice_name)
        self.speech = speech or SpeechInput(settings.speech_engine)
        self.log = logging.getLogger(__name__)

    def start(self) -> None:
        self.history.load()

    def respond(self, prompt: str, *, speak: bool | None = None) -> str:
        clean_prompt = prompt.strip()
        if not clean_prompt:
            raise ValueError("Please enter a message")
        message = Message(role="user", content=clean_prompt, language=self.settings.language)
        try:
            response = self.backend.generate((*self.history.messages, message), self.settings.language).strip()
        except Exception as exc:
            self.log.exception("Conversation backend failed")
            raise BackendError("Riley could not generate a response") from exc
        if not response:
            raise BackendError("The conversation backend returned an empty response")
        self.history.add(message)
        self.history.add(Message(role="assistant", content=response, language=self.settings.language))
        should_speak = self.settings.voice_enabled if speak is None else speak
        if should_speak:
            try:
                self.voice.speak(response)
            except VoiceOutputError as exc:
                self.log.warning("Voice output failed: %s", exc)
        return response

    def listen(self) -> str:
        locale = SUPPORTED_LANGUAGES[self.settings.language]
        return self.speech.listen(locale)
