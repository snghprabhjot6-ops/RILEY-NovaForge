from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

def test_word_boundary_guard_001() -> None:
    reply = _BACKEND.generate([Message('user', 'Please review update item 1')], 'en')
    assert 'learning' in reply

