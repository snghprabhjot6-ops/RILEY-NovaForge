from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

def test_arith_precedence_001() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 5 + 3 * 2 - 1')], 'en')
    assert reply == 'The answer is 10.'

