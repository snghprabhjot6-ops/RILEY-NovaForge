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

def test_settings_valid_009() -> None:
    cfg = Settings(backend='local', ollama_url='http://localhost:11435', ollama_model='model-9', language='fr', speech_engine='google', log_level='CRITICAL')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_010() -> None:
    cfg = Settings(backend='echo', ollama_url='http://127.0.0.1:11434', ollama_model='model-10', language='hi', speech_engine='sphinx', log_level='DEBUG')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_011() -> None:
    cfg = Settings(backend='ollama', ollama_url='http://localhost:11434', ollama_model='model-11', language='sa', speech_engine='google', log_level='INFO')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_012() -> None:
    cfg = Settings(backend='local', ollama_url='http://[::1]:11434', ollama_model='model-12', language='bn', speech_engine='sphinx', log_level='WARNING')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_013() -> None:
    cfg = Settings(backend='echo', ollama_url='http://127.0.0.1:8080', ollama_model='model-13', language='en', speech_engine='google', log_level='ERROR')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_014() -> None:
    cfg = Settings(backend='ollama', ollama_url='http://localhost:11435', ollama_model='model-14', language='es', speech_engine='sphinx', log_level='CRITICAL')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_015() -> None:
    cfg = Settings(backend='local', ollama_url='http://127.0.0.1:11434', ollama_model='model-15', language='fr', speech_engine='google', log_level='DEBUG')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_016() -> None:
    cfg = Settings(backend='echo', ollama_url='http://localhost:11434', ollama_model='model-16', language='hi', speech_engine='sphinx', log_level='INFO')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_017() -> None:
    cfg = Settings(backend='ollama', ollama_url='http://[::1]:11434', ollama_model='model-17', language='sa', speech_engine='google', log_level='WARNING')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_018() -> None:
    cfg = Settings(backend='local', ollama_url='http://127.0.0.1:8080', ollama_model='model-18', language='bn', speech_engine='sphinx', log_level='ERROR')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_019() -> None:
    cfg = Settings(backend='echo', ollama_url='http://localhost:11435', ollama_model='model-19', language='en', speech_engine='google', log_level='CRITICAL')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_020() -> None:
    cfg = Settings(backend='ollama', ollama_url='http://127.0.0.1:11434', ollama_model='model-20', language='es', speech_engine='sphinx', log_level='DEBUG')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_021() -> None:
    cfg = Settings(backend='local', ollama_url='http://localhost:11434', ollama_model='model-21', language='fr', speech_engine='google', log_level='INFO')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_022() -> None:
    cfg = Settings(backend='echo', ollama_url='http://[::1]:11434', ollama_model='model-22', language='hi', speech_engine='sphinx', log_level='WARNING')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_023() -> None:
    cfg = Settings(backend='ollama', ollama_url='http://127.0.0.1:8080', ollama_model='model-23', language='sa', speech_engine='google', log_level='ERROR')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_024() -> None:
    cfg = Settings(backend='local', ollama_url='http://localhost:11435', ollama_model='model-24', language='bn', speech_engine='sphinx', log_level='CRITICAL')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

def test_settings_valid_025() -> None:
    cfg = Settings(backend='echo', ollama_url='http://127.0.0.1:11434', ollama_model='model-25', language='en', speech_engine='google', log_level='DEBUG')
    cfg.validate()
    assert cfg.language in SUPPORTED_LANGUAGES

