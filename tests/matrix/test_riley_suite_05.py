from riley.backends.local import LocalBackend, TEXT
from riley.models import Message

_BACKEND = LocalBackend()

def test_multilingual_en_hello_001() -> None:
    reply = _BACKEND.generate([Message('user', 'hello', language='en')], 'en')
    assert reply == TEXT['en']['hello']

def test_multilingual_en_help_002() -> None:
    reply = _BACKEND.generate([Message('user', 'Can you help me?', language='en')], 'en')
    assert reply == TEXT['en']['help']

def test_multilingual_en_thanks_003() -> None:
    reply = _BACKEND.generate([Message('user', 'thanks!', language='en')], 'en')
    assert reply == TEXT['en']['thanks']

def test_multilingual_en_time_004() -> None:
    reply = _BACKEND.generate([Message('user', 'What time is it?', language='en')], 'en')
    assert reply.startswith(TEXT['en']['time'].split('{value}')[0])

