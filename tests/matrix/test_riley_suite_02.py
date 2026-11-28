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

