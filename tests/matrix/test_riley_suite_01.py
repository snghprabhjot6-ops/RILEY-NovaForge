from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

def test_arith_precedence_001() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 5 + 3 * 2 - 1')], 'en')
    assert reply == 'The answer is 10.'

def test_arith_precedence_002() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 8 + 4 * 3 - 2')], 'en')
    assert reply == 'The answer is 18.'

def test_arith_precedence_003() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 11 + 5 * 4 - 3')], 'en')
    assert reply == 'The answer is 28.'

def test_arith_precedence_004() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 14 + 6 * 5 - 4')], 'en')
    assert reply == 'The answer is 40.'

def test_arith_precedence_005() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 17 + 7 * 6 - 5')], 'en')
    assert reply == 'The answer is 54.'

def test_arith_precedence_006() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 20 + 8 * 7 - 6')], 'en')
    assert reply == 'The answer is 70.'

def test_arith_precedence_007() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 23 + 9 * 1 - 7')], 'en')
    assert reply == 'The answer is 25.'

def test_arith_precedence_008() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 26 + 10 * 2 - 8')], 'en')
    assert reply == 'The answer is 38.'

