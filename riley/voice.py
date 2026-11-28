from __future__ import annotations

import platform
import re
import shutil
import subprocess
from dataclasses import dataclass

from .exceptions import VoiceOutputError


FEMININE_VOICE_HINTS = ("samantha", "victoria", "karen", "moira", "tessa", "fiona", "veena", "lekha", "female", "woman")


@dataclass(slots=True)
class VoiceOutput:
    preferred_voice: str = "Samantha"

    def speak(self, text: str) -> None:
        if not text.strip():
            return
        if platform.system() == "Darwin" and shutil.which("say"):
            self._speak_macos(text)
            return
        self._speak_portable(text)

    def _macos_voice_names(self) -> list[str]:
        result = subprocess.run(["say", "-v", "?"], capture_output=True, text=True, check=True, timeout=10)
        names: list[str] = []
        for line in result.stdout.splitlines():
            match = re.match(r"^(.+?)\s{2,}[a-z]{2}[_-][A-Z]{2}\s+#", line)
            if match:
                names.append(match.group(1).strip())
        return names

    def _select_macos_voice(self) -> str | None:
        try:
            voices = self._macos_voice_names()
        except (OSError, subprocess.SubprocessError):
            return None
        preferred = self.preferred_voice.casefold()
        for voice in voices:
            if voice.casefold() == preferred:
                return voice
        return next((voice for voice in voices if any(hint in voice.casefold() for hint in FEMININE_VOICE_HINTS)), None)

    def _speak_macos(self, text: str) -> None:
        command = ["say"]
        voice = self._select_macos_voice()
        if voice:
            command.extend(["-v", voice])
        command.extend(["--", text])
        try:
            subprocess.run(command, check=True, timeout=120)
        except (OSError, subprocess.SubprocessError) as exc:
            raise VoiceOutputError(f"macOS speech output failed: {exc}") from exc

    def _speak_portable(self, text: str) -> None:
        try:
            import pyttsx3

            engine = pyttsx3.init()
            voices = engine.getProperty("voices") or []
            preferred = self.preferred_voice.casefold()
            selected = next(
                (
                    voice.id
                    for voice in voices
                    if preferred in f"{getattr(voice, 'name', '')} {getattr(voice, 'id', '')}".casefold()
                ),
                None,
            )
            if selected is None:
                selected = next(
                    (
                        voice.id
                        for voice in voices
                        if any(
                            hint in f"{getattr(voice, 'name', '')} {getattr(voice, 'id', '')}".casefold()
                            for hint in FEMININE_VOICE_HINTS
                        )
                    ),
                    None,
                )
            if selected:
                engine.setProperty("voice", selected)
            engine.say(text)
            engine.runAndWait()
        except Exception as exc:
            raise VoiceOutputError(f"Portable speech output failed: {exc}") from exc
