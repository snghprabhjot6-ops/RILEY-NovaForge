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

def test_arith_precedence_027() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 83 + 3 * 7 - 27')], 'en')
    assert reply == 'The answer is 77.'

def test_arith_precedence_028() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 86 + 4 * 1 - 28')], 'en')
    assert reply == 'The answer is 62.'

def test_arith_precedence_029() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 89 + 5 * 2 - 29')], 'en')
    assert reply == 'The answer is 70.'

def test_arith_precedence_030() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 92 + 6 * 3 - 30')], 'en')
    assert reply == 'The answer is 80.'

def test_arith_precedence_031() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 95 + 7 * 4 - 31')], 'en')
    assert reply == 'The answer is 92.'

def test_arith_precedence_032() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 98 + 8 * 5 - 32')], 'en')
    assert reply == 'The answer is 106.'

def test_arith_precedence_033() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 101 + 9 * 6 - 33')], 'en')
    assert reply == 'The answer is 122.'

def test_arith_precedence_034() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 104 + 10 * 7 - 34')], 'en')
    assert reply == 'The answer is 140.'

def test_arith_precedence_035() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 107 + 11 * 1 - 35')], 'en')
    assert reply == 'The answer is 83.'

def test_arith_precedence_036() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 110 + 12 * 2 - 36')], 'en')
    assert reply == 'The answer is 98.'

def test_arith_precedence_037() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 113 + 13 * 3 - 37')], 'en')
    assert reply == 'The answer is 115.'

def test_arith_precedence_038() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 116 + 14 * 4 - 38')], 'en')
    assert reply == 'The answer is 134.'

def test_arith_precedence_039() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 119 + 2 * 5 - 39')], 'en')
    assert reply == 'The answer is 90.'

def test_arith_precedence_040() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 122 + 3 * 6 - 40')], 'en')
    assert reply == 'The answer is 100.'

def test_arith_precedence_041() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 125 + 4 * 7 - 41')], 'en')
    assert reply == 'The answer is 112.'

def test_arith_precedence_042() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 128 + 5 * 1 - 42')], 'en')
    assert reply == 'The answer is 91.'

