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

def test_arith_precedence_009() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 29 + 11 * 3 - 9')], 'en')
    assert reply == 'The answer is 53.'

def test_arith_precedence_010() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 32 + 12 * 4 - 10')], 'en')
    assert reply == 'The answer is 70.'

def test_arith_precedence_011() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 35 + 13 * 5 - 11')], 'en')
    assert reply == 'The answer is 89.'

def test_arith_precedence_012() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 38 + 14 * 6 - 12')], 'en')
    assert reply == 'The answer is 110.'

def test_arith_precedence_013() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 41 + 2 * 7 - 13')], 'en')
    assert reply == 'The answer is 42.'

def test_arith_precedence_014() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 44 + 3 * 1 - 14')], 'en')
    assert reply == 'The answer is 33.'

def test_arith_precedence_015() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 47 + 4 * 2 - 15')], 'en')
    assert reply == 'The answer is 40.'

def test_arith_precedence_016() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 50 + 5 * 3 - 16')], 'en')
    assert reply == 'The answer is 49.'

def test_arith_precedence_017() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 53 + 6 * 4 - 17')], 'en')
    assert reply == 'The answer is 60.'

def test_arith_precedence_018() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 56 + 7 * 5 - 18')], 'en')
    assert reply == 'The answer is 73.'

def test_arith_precedence_019() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 59 + 8 * 6 - 19')], 'en')
    assert reply == 'The answer is 88.'

def test_arith_precedence_020() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 62 + 9 * 7 - 20')], 'en')
    assert reply == 'The answer is 105.'

def test_arith_precedence_021() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 65 + 10 * 1 - 21')], 'en')
    assert reply == 'The answer is 54.'

def test_arith_precedence_022() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 68 + 11 * 2 - 22')], 'en')
    assert reply == 'The answer is 68.'

def test_arith_precedence_023() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 71 + 12 * 3 - 23')], 'en')
    assert reply == 'The answer is 84.'

def test_arith_precedence_024() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 74 + 13 * 4 - 24')], 'en')
    assert reply == 'The answer is 102.'

def test_arith_precedence_025() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 77 + 14 * 5 - 25')], 'en')
    assert reply == 'The answer is 122.'

def test_arith_precedence_026() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 80 + 2 * 6 - 26')], 'en')
    assert reply == 'The answer is 66.'

