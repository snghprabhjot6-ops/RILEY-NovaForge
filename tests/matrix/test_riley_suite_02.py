from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

def test_arith_compound_001() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (10 * 4) / 8')], 'en')
    assert reply == 'The answer is 5.'

def test_arith_compound_002() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (39 % 4) + 2')], 'en')
    assert reply == 'The answer is 5.'

def test_arith_compound_003() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (5 ** 4) + 3')], 'en')
    assert reply == 'The answer is 628.'

def test_arith_compound_004() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (40 * 4) / 8')], 'en')
    assert reply == 'The answer is 20.'

def test_arith_compound_005() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (90 % 7) + 5')], 'en')
    assert reply == 'The answer is 11.'

def test_arith_compound_006() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (8 ** 3) + 6')], 'en')
    assert reply == 'The answer is 518.'

def test_arith_compound_007() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (70 * 4) / 8')], 'en')
    assert reply == 'The answer is 35.'

def test_arith_compound_008() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (141 % 10) + 8')], 'en')
    assert reply == 'The answer is 9.'

def test_arith_compound_009() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (2 ** 2) + 9')], 'en')
    assert reply == 'The answer is 13.'

def test_arith_compound_010() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (100 * 4) / 8')], 'en')
    assert reply == 'The answer is 50.'

def test_arith_compound_011() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (192 % 2) + 11')], 'en')
    assert reply == 'The answer is 11.'

def test_arith_compound_012() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (5 ** 1) + 12')], 'en')
    assert reply == 'The answer is 17.'

def test_arith_compound_013() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (130 * 4) / 8')], 'en')
    assert reply == 'The answer is 65.'

def test_arith_compound_014() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (243 % 5) + 14')], 'en')
    assert reply == 'The answer is 17.'

def test_arith_compound_015() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (8 ** 4) + 15')], 'en')
    assert reply == 'The answer is 4111.'

def test_arith_compound_016() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (160 * 4) / 8')], 'en')
    assert reply == 'The answer is 80.'

def test_arith_compound_017() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (294 % 8) + 17')], 'en')
    assert reply == 'The answer is 23.'

def test_arith_compound_018() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (2 ** 3) + 18')], 'en')
    assert reply == 'The answer is 26.'

def test_arith_compound_019() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (190 * 4) / 8')], 'en')
    assert reply == 'The answer is 95.'

def test_arith_compound_020() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (345 % 11) + 20')], 'en')
    assert reply == 'The answer is 24.'

def test_arith_compound_021() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (5 ** 2) + 21')], 'en')
    assert reply == 'The answer is 46.'

def test_arith_compound_022() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (220 * 4) / 8')], 'en')
    assert reply == 'The answer is 110.'

def test_arith_compound_023() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (396 % 3) + 23')], 'en')
    assert reply == 'The answer is 23.'

def test_arith_compound_024() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (8 ** 1) + 24')], 'en')
    assert reply == 'The answer is 32.'

