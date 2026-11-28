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

def test_arith_punct_bare_019() -> None:
    reply = _BACKEND.generate([Message('user', '29 * 4 - 19')], 'en')
    assert reply == 'The answer is 97.'

def test_arith_punct_bare_020() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (30 + 5) * 2?')], 'en')
    assert reply == 'The answer is 70.'

def test_arith_punct_bare_021() -> None:
    reply = _BACKEND.generate([Message('user', '31 * 6 - 21!')], 'en')
    assert reply == 'The answer is 165.'

def test_arith_punct_bare_022() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (32 + 7) * 2.')], 'en')
    assert reply == 'The answer is 78.'

def test_arith_punct_bare_023() -> None:
    reply = _BACKEND.generate([Message('user', '33 * 8 - 23??')], 'en')
    assert reply == 'The answer is 241.'

def test_arith_punct_bare_024() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (34 + 9) * 2')], 'en')
    assert reply == 'The answer is 86.'

def test_arith_punct_bare_025() -> None:
    reply = _BACKEND.generate([Message('user', '35 * 10 - 25?')], 'en')
    assert reply == 'The answer is 325.'

def test_arith_punct_bare_026() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (36 + 11) * 2!')], 'en')
    assert reply == 'The answer is 94.'

def test_arith_punct_bare_027() -> None:
    reply = _BACKEND.generate([Message('user', '37 * 3 - 27.')], 'en')
    assert reply == 'The answer is 84.'

def test_arith_punct_bare_028() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (38 + 4) * 2??')], 'en')
    assert reply == 'The answer is 84.'

def test_arith_punct_bare_029() -> None:
    reply = _BACKEND.generate([Message('user', '39 * 5 - 29')], 'en')
    assert reply == 'The answer is 166.'

def test_arith_punct_bare_030() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (40 + 6) * 2?')], 'en')
    assert reply == 'The answer is 92.'

def test_arith_punct_bare_031() -> None:
    reply = _BACKEND.generate([Message('user', '41 * 7 - 31!')], 'en')
    assert reply == 'The answer is 256.'

def test_arith_punct_bare_032() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (42 + 8) * 2.')], 'en')
    assert reply == 'The answer is 100.'

def test_arith_punct_bare_033() -> None:
    reply = _BACKEND.generate([Message('user', '43 * 9 - 33??')], 'en')
    assert reply == 'The answer is 354.'

def test_arith_punct_bare_034() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (44 + 10) * 2')], 'en')
    assert reply == 'The answer is 108.'

def test_arith_punct_bare_035() -> None:
    reply = _BACKEND.generate([Message('user', '45 * 11 - 35?')], 'en')
    assert reply == 'The answer is 460.'

def test_arith_punct_bare_036() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (46 + 3) * 2!')], 'en')
    assert reply == 'The answer is 98.'

def test_arith_punct_bare_037() -> None:
    reply = _BACKEND.generate([Message('user', '47 * 4 - 37.')], 'en')
    assert reply == 'The answer is 151.'

def test_arith_punct_bare_038() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (48 + 5) * 2??')], 'en')
    assert reply == 'The answer is 106.'

def test_arith_punct_bare_039() -> None:
    reply = _BACKEND.generate([Message('user', '49 * 6 - 39')], 'en')
    assert reply == 'The answer is 255.'

def test_arith_punct_bare_040() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (50 + 7) * 2?')], 'en')
    assert reply == 'The answer is 114.'

def test_arith_punct_bare_041() -> None:
    reply = _BACKEND.generate([Message('user', '51 * 8 - 41!')], 'en')
    assert reply == 'The answer is 367.'

def test_arith_punct_bare_042() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (52 + 9) * 2.')], 'en')
    assert reply == 'The answer is 122.'

def test_arith_punct_bare_043() -> None:
    reply = _BACKEND.generate([Message('user', '53 * 10 - 43??')], 'en')
    assert reply == 'The answer is 487.'

def test_arith_punct_bare_044() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (54 + 11) * 2')], 'en')
    assert reply == 'The answer is 130.'

def test_arith_punct_bare_045() -> None:
    reply = _BACKEND.generate([Message('user', '55 * 3 - 45?')], 'en')
    assert reply == 'The answer is 120.'

def test_arith_punct_bare_046() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (56 + 4) * 2!')], 'en')
    assert reply == 'The answer is 120.'

def test_arith_punct_bare_047() -> None:
    reply = _BACKEND.generate([Message('user', '57 * 5 - 47.')], 'en')
    assert reply == 'The answer is 238.'

def test_arith_punct_bare_048() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (58 + 6) * 2??')], 'en')
    assert reply == 'The answer is 128.'

def test_arith_punct_bare_049() -> None:
    reply = _BACKEND.generate([Message('user', '59 * 7 - 49')], 'en')
    assert reply == 'The answer is 364.'

def test_arith_punct_bare_050() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (60 + 8) * 2?')], 'en')
    assert reply == 'The answer is 136.'

def test_arith_punct_bare_051() -> None:
    reply = _BACKEND.generate([Message('user', '61 * 9 - 51!')], 'en')
    assert reply == 'The answer is 498.'

def test_arith_punct_bare_052() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (62 + 10) * 2.')], 'en')
    assert reply == 'The answer is 144.'

def test_arith_punct_bare_053() -> None:
    reply = _BACKEND.generate([Message('user', '63 * 11 - 53??')], 'en')
    assert reply == 'The answer is 640.'

def test_arith_punct_bare_054() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (64 + 3) * 2')], 'en')
    assert reply == 'The answer is 134.'

def test_arith_punct_bare_055() -> None:
    reply = _BACKEND.generate([Message('user', '65 * 4 - 55?')], 'en')
    assert reply == 'The answer is 205.'

def test_arith_punct_bare_056() -> None:
    reply = _BACKEND.generate([Message('user', 'what is (66 + 5) * 2!')], 'en')
    assert reply == 'The answer is 142.'

def test_arith_punct_bare_057() -> None:
    reply = _BACKEND.generate([Message('user', '67 * 6 - 57.')], 'en')
    assert reply == 'The answer is 345.'

