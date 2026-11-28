import pytest
from riley.config import Settings, _as_bool, SUPPORTED_LANGUAGES
from riley.exceptions import ConfigurationError

def test_settings_valid_001() -> None:
    cfg = Settings(backend='echo', ollama_url='http://localhost:11434', ollama_model='model-1', language='en', speech_engine='google', log_level='INFO')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_002() -> None:
    cfg = Settings(backend='ollama', ollama_url='http://[::1]:11434', ollama_model='model-2', language='es', speech_engine='sphinx', log_level='WARNING')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_003() -> None:
    cfg = Settings(backend='local', ollama_url='http://127.0.0.1:8080', ollama_model='model-3', language='fr', speech_engine='google', log_level='ERROR')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_004() -> None:
    cfg = Settings(backend='echo', ollama_url='http://localhost:11435', ollama_model='model-4', language='hi', speech_engine='sphinx', log_level='CRITICAL')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_005() -> None:
    cfg = Settings(backend='ollama', ollama_url='http://127.0.0.1:11434', ollama_model='model-5', language='sa', speech_engine='google', log_level='DEBUG')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_006() -> None:
    cfg = Settings(backend='local', ollama_url='http://localhost:11434', ollama_model='model-6', language='bn', speech_engine='sphinx', log_level='INFO')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_007() -> None:
    cfg = Settings(backend='echo', ollama_url='http://[::1]:11434', ollama_model='model-7', language='en', speech_engine='google', log_level='WARNING')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_008() -> None:
    cfg = Settings(backend='ollama', ollama_url='http://127.0.0.1:8080', ollama_model='model-8', language='es', speech_engine='sphinx', log_level='ERROR')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

