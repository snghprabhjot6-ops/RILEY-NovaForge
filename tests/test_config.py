from pathlib import Path

import pytest

from riley.config import Settings
from riley.exceptions import ConfigurationError


def test_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    for key in (
        "RILEY_BACKEND", "RILEY_LANGUAGE", "RILEY_VOICE_ENABLED", "RILEY_VOICE_NAME",
        "RILEY_SPEECH_ENGINE", "RILEY_HISTORY_FILE", "RILEY_LOG_LEVEL",
    ):
        monkeypatch.delenv(key, raising=False)
    settings = Settings.from_env(Path("/definitely/missing/.env"))
    assert settings.backend == "local"
    assert settings.language == "en"
    assert settings.voice_enabled is True
    assert settings.speech_engine == "sphinx"


def test_environment_overrides(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv("RILEY_BACKEND", "echo")
    monkeypatch.setenv("RILEY_LANGUAGE", "fr")
    monkeypatch.setenv("RILEY_VOICE_ENABLED", "false")
    monkeypatch.setenv("RILEY_HISTORY_FILE", str(tmp_path / "history.json"))
    settings = Settings.from_env(Path("/definitely/missing/.env"))
    assert settings.backend == "echo"
    assert settings.language == "fr"
    assert settings.voice_enabled is False
    assert settings.history_file == tmp_path / "history.json"


def test_invalid_language_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("RILEY_LANGUAGE", "xx")
    with pytest.raises(ConfigurationError):
        Settings.from_env(Path("/definitely/missing/.env"))


def test_invalid_ollama_port_and_model_whitespace_rejected() -> None:
    from riley.config import Settings as Cfg
    with pytest.raises(ConfigurationError):
        Cfg(ollama_url="http://127.0.0.1:99999").validate()
    with pytest.raises(ConfigurationError):
        Cfg(ollama_model="bad model").validate()
