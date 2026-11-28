import pytest
from riley.config import Settings, _as_bool, SUPPORTED_LANGUAGES
from riley.exceptions import ConfigurationError

def test_settings_valid_001() -> None:
    cfg = Settings(backend='echo', ollama_url='http://localhost:11434', ollama_model='model-1', language='en', speech_engine='google', log_level='INFO')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

