from riley.backends.local import LocalBackend, TEXT
from riley.models import Message

_BACKEND = LocalBackend()

def test_multilingual_en_hello_001() -> None:
    reply = _BACKEND.generate([Message('user', 'hello', language='en')], 'en')
    assert reply == TEXT['en']['hello']

