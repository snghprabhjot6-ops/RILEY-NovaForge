from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

def test_arith_punct_bare_001() -> None:
    reply = _BACKEND.generate([Message('user', '11 * 4 - 1!')], 'en')
    assert reply == 'The answer is 43.'

