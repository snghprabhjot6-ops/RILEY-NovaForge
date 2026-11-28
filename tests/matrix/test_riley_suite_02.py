from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

def test_arith_compound_001() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (10 * 4) / 8')], 'en')
    assert reply == 'The answer is 5.'

def test_arith_compound_002() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (39 % 4) + 2')], 'en')
    assert reply == 'The answer is 5.'

