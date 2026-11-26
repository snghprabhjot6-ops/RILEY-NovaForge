from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

from .exceptions import ConfigurationError


SUPPORTED_LANGUAGES = {
    "en": "en-US",
    "hi": "hi-IN",
    "fr": "fr-FR",
    "bn": "bn-BD",
    "sa": "sa-IN",
    "es": "es-ES",
}


def _as_bool(value: str | None, default: bool) -> bool:
    if value is None:
        return default
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "on"}:
        return True
    if normalized in {"0", "false", "no", "off"}:
        return False
    raise ConfigurationError(f"Expected a boolean value, received: {value!r}")


@dataclass(frozen=True, slots=True)
class Settings:
    backend: str = "local"
    language: str = "en"
    voice_enabled: bool = True
    voice_name: str = "Samantha"
    speech_engine: str = "sphinx"
    history_file: Path = Path(".riley/history.json")
    log_level: str = "INFO"

    @classmethod
    def from_env(cls, env_file: str | Path | None = None) -> "Settings":
        if env_file is not None:
            load_dotenv(dotenv_path=env_file, override=False)
        else:
            load_dotenv(override=False)

        settings = cls(
            backend=os.getenv("RILEY_BACKEND", "local").strip().lower(),
            language=os.getenv("RILEY_LANGUAGE", "en").strip().lower(),
            voice_enabled=_as_bool(os.getenv("RILEY_VOICE_ENABLED"), True),
            voice_name=os.getenv("RILEY_VOICE_NAME", "Samantha").strip(),
            speech_engine=os.getenv("RILEY_SPEECH_ENGINE", "sphinx").strip().lower(),
            history_file=Path(os.getenv("RILEY_HISTORY_FILE", ".riley/history.json")).expanduser(),
            log_level=os.getenv("RILEY_LOG_LEVEL", "INFO").strip().upper(),
        )
        settings.validate()
        return settings

    def validate(self) -> None:
        if self.backend not in {"local", "echo"}:
            raise ConfigurationError("RILEY_BACKEND must be 'local' or 'echo'")
        if self.language not in SUPPORTED_LANGUAGES:
            supported = ", ".join(sorted(SUPPORTED_LANGUAGES))
            raise ConfigurationError(f"Unsupported language {self.language!r}. Choose: {supported}")
        if self.speech_engine not in {"sphinx", "google"}:
            raise ConfigurationError("RILEY_SPEECH_ENGINE must be 'sphinx' or 'google'")
        if self.log_level not in {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}:
            raise ConfigurationError("RILEY_LOG_LEVEL is not valid")
