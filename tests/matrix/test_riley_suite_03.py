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

def test_arith_punct_bare_008() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (18 + 11) * 2??')], 'en')
    assert reply == 'The answer is 58.'

def test_arith_punct_bare_009() -> None:
    reply = _BACKEND.generate([Message('user', '19 * 3 - 9')], 'en')
    assert reply == 'The answer is 48.'

def test_arith_punct_bare_010() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (20 + 4) * 2?')], 'en')
    assert reply == 'The answer is 48.'

def test_arith_punct_bare_011() -> None:
    reply = _BACKEND.generate([Message('user', '21 * 5 - 11!')], 'en')
    assert reply == 'The answer is 94.'

def test_arith_punct_bare_012() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (22 + 6) * 2.')], 'en')
    assert reply == 'The answer is 56.'

def test_arith_punct_bare_013() -> None:
    reply = _BACKEND.generate([Message('user', '23 * 7 - 13??')], 'en')
    assert reply == 'The answer is 148.'

def test_arith_punct_bare_014() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (24 + 8) * 2')], 'en')
    assert reply == 'The answer is 64.'

def test_arith_punct_bare_015() -> None:
    reply = _BACKEND.generate([Message('user', '25 * 9 - 15?')], 'en')
    assert reply == 'The answer is 210.'

def test_arith_punct_bare_016() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (26 + 10) * 2!')], 'en')
    assert reply == 'The answer is 72.'

def test_arith_punct_bare_017() -> None:
    reply = _BACKEND.generate([Message('user', '27 * 11 - 17.')], 'en')
    assert reply == 'The answer is 280.'

def test_arith_punct_bare_018() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (28 + 3) * 2??')], 'en')
    assert reply == 'The answer is 62.'

