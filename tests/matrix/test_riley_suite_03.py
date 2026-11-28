from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

def test_arith_punct_bare_001() -> None:
    reply = _BACKEND.generate([Message('user', '11 * 4 - 1!')], 'en')
    assert reply == 'The answer is 43.'

def test_arith_punct_bare_002() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (12 + 5) * 2.')], 'en')
    assert reply == 'The answer is 34.'

def test_arith_punct_bare_003() -> None:
    reply = _BACKEND.generate([Message('user', '13 * 6 - 3??')], 'en')
    assert reply == 'The answer is 75.'

def test_arith_punct_bare_004() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (14 + 7) * 2')], 'en')
    assert reply == 'The answer is 42.'

def test_arith_punct_bare_005() -> None:
    reply = _BACKEND.generate([Message('user', '15 * 8 - 5?')], 'en')
    assert reply == 'The answer is 115.'

def test_arith_punct_bare_006() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (16 + 9) * 2!')], 'en')
    assert reply == 'The answer is 50.'

def test_arith_punct_bare_007() -> None:
    reply = _BACKEND.generate([Message('user', '17 * 10 - 7.')], 'en')
    assert reply == 'The answer is 163.'

