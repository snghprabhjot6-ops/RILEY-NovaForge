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

def test_arith_compound_025() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (250 * 4) / 8')], 'en')
    assert reply == 'The answer is 125.'

def test_arith_compound_026() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (447 % 6) + 26')], 'en')
    assert reply == 'The answer is 29.'

def test_arith_compound_027() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (2 ** 4) + 27')], 'en')
    assert reply == 'The answer is 43.'

def test_arith_compound_028() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (280 * 4) / 8')], 'en')
    assert reply == 'The answer is 140.'

def test_arith_compound_029() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (498 % 9) + 29')], 'en')
    assert reply == 'The answer is 32.'

def test_arith_compound_030() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (5 ** 3) + 30')], 'en')
    assert reply == 'The answer is 155.'

def test_arith_compound_031() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (310 * 4) / 8')], 'en')
    assert reply == 'The answer is 155.'

def test_arith_compound_032() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (549 % 12) + 32')], 'en')
    assert reply == 'The answer is 41.'

def test_arith_compound_033() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (8 ** 2) + 33')], 'en')
    assert reply == 'The answer is 97.'

def test_arith_compound_034() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (340 * 4) / 8')], 'en')
    assert reply == 'The answer is 170.'

def test_arith_compound_035() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (600 % 4) + 35')], 'en')
    assert reply == 'The answer is 35.'

def test_arith_compound_036() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (2 ** 1) + 36')], 'en')
    assert reply == 'The answer is 38.'

def test_arith_compound_037() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (370 * 4) / 8')], 'en')
    assert reply == 'The answer is 185.'

def test_arith_compound_038() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (651 % 7) + 38')], 'en')
    assert reply == 'The answer is 38.'

def test_arith_compound_039() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (5 ** 4) + 39')], 'en')
    assert reply == 'The answer is 664.'

def test_arith_compound_040() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (400 * 4) / 8')], 'en')
    assert reply == 'The answer is 200.'

def test_arith_compound_041() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (702 % 10) + 41')], 'en')
    assert reply == 'The answer is 43.'

def test_arith_compound_042() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (8 ** 3) + 42')], 'en')
    assert reply == 'The answer is 554.'

def test_arith_compound_043() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (430 * 4) / 8')], 'en')
    assert reply == 'The answer is 215.'

def test_arith_compound_044() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (753 % 2) + 44')], 'en')
    assert reply == 'The answer is 45.'

def test_arith_compound_045() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (2 ** 2) + 45')], 'en')
    assert reply == 'The answer is 49.'

def test_arith_compound_046() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (460 * 4) / 8')], 'en')
    assert reply == 'The answer is 230.'

def test_arith_compound_047() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (804 % 5) + 47')], 'en')
    assert reply == 'The answer is 51.'

def test_arith_compound_048() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (5 ** 1) + 48')], 'en')
    assert reply == 'The answer is 53.'

def test_arith_compound_049() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (490 * 4) / 8')], 'en')
    assert reply == 'The answer is 245.'

def test_arith_compound_050() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (855 % 8) + 50')], 'en')
    assert reply == 'The answer is 57.'

def test_arith_compound_051() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (8 ** 4) + 51')], 'en')
    assert reply == 'The answer is 4147.'

def test_arith_compound_052() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (520 * 4) / 8')], 'en')
    assert reply == 'The answer is 260.'

def test_arith_compound_053() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (906 % 11) + 53')], 'en')
    assert reply == 'The answer is 57.'

def test_arith_compound_054() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (2 ** 3) + 54')], 'en')
    assert reply == 'The answer is 62.'

def test_arith_compound_055() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (550 * 4) / 8')], 'en')
    assert reply == 'The answer is 275.'

def test_arith_compound_056() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (957 % 3) + 56')], 'en')
    assert reply == 'The answer is 56.'

def test_arith_compound_057() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (5 ** 2) + 57')], 'en')
    assert reply == 'The answer is 82.'

def test_arith_compound_058() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (580 * 4) / 8')], 'en')
    assert reply == 'The answer is 290.'

def test_arith_compound_059() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (1008 % 6) + 59')], 'en')
    assert reply == 'The answer is 59.'

def test_arith_compound_060() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (8 ** 1) + 60')], 'en')
    assert reply == 'The answer is 68.'

def test_arith_compound_061() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (610 * 4) / 8')], 'en')
    assert reply == 'The answer is 305.'

def test_arith_compound_062() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (1059 % 9) + 62')], 'en')
    assert reply == 'The answer is 68.'

def test_arith_compound_063() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (2 ** 4) + 63')], 'en')
    assert reply == 'The answer is 79.'

def test_arith_compound_064() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (640 * 4) / 8')], 'en')
    assert reply == 'The answer is 320.'

def test_arith_compound_065() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (1110 % 12) + 65')], 'en')
    assert reply == 'The answer is 71.'

def test_arith_compound_066() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (5 ** 3) + 66')], 'en')
    assert reply == 'The answer is 191.'

def test_arith_compound_067() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (670 * 4) / 8')], 'en')
    assert reply == 'The answer is 335.'

def test_arith_compound_068() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (1161 % 4) + 68')], 'en')
    assert reply == 'The answer is 69.'

def test_arith_compound_069() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (8 ** 2) + 69')], 'en')
    assert reply == 'The answer is 133.'

def test_arith_compound_070() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (700 * 4) / 8')], 'en')
    assert reply == 'The answer is 350.'

def test_arith_compound_071() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (1212 % 7) + 71')], 'en')
    assert reply == 'The answer is 72.'

def test_arith_compound_072() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (2 ** 1) + 72')], 'en')
    assert reply == 'The answer is 74.'

def test_arith_compound_073() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (730 * 4) / 8')], 'en')
    assert reply == 'The answer is 365.'

def test_arith_compound_074() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (1263 % 10) + 74')], 'en')
    assert reply == 'The answer is 77.'

def test_arith_compound_075() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (5 ** 4) + 75')], 'en')
    assert reply == 'The answer is 700.'

def test_arith_compound_076() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (760 * 4) / 8')], 'en')
    assert reply == 'The answer is 380.'

def test_arith_compound_077() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (1314 % 2) + 77')], 'en')
    assert reply == 'The answer is 77.'

def test_arith_compound_078() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (8 ** 3) + 78')], 'en')
    assert reply == 'The answer is 590.'

def test_arith_compound_079() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (790 * 4) / 8')], 'en')
    assert reply == 'The answer is 395.'

def test_arith_compound_080() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (1365 % 5) + 80')], 'en')
    assert reply == 'The answer is 80.'

def test_arith_compound_081() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (2 ** 2) + 81')], 'en')
    assert reply == 'The answer is 85.'

def test_arith_compound_082() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (820 * 4) / 8')], 'en')
    assert reply == 'The answer is 410.'

def test_arith_compound_083() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (1416 % 8) + 83')], 'en')
    assert reply == 'The answer is 83.'

def test_arith_compound_084() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (5 ** 1) + 84')], 'en')
    assert reply == 'The answer is 89.'

def test_arith_compound_085() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (850 * 4) / 8')], 'en')
    assert reply == 'The answer is 425.'

def test_arith_compound_086() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (1467 % 11) + 86')], 'en')
    assert reply == 'The answer is 90.'

def test_arith_compound_087() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (8 ** 4) + 87')], 'en')
    assert reply == 'The answer is 4183.'

def test_arith_compound_088() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (880 * 4) / 8')], 'en')
    assert reply == 'The answer is 440.'

def test_arith_compound_089() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (1518 % 3) + 89')], 'en')
    assert reply == 'The answer is 89.'

def test_arith_compound_090() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (2 ** 3) + 90')], 'en')
    assert reply == 'The answer is 98.'

def test_arith_compound_091() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (910 * 4) / 8')], 'en')
    assert reply == 'The answer is 455.'

def test_arith_compound_092() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (1569 % 6) + 92')], 'en')
    assert reply == 'The answer is 95.'

def test_arith_compound_093() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (5 ** 2) + 93')], 'en')
    assert reply == 'The answer is 118.'

def test_arith_compound_094() -> None:
    reply = _BACKEND.generate([Message('user', 'calc (940 * 4) / 8')], 'en')
    assert reply == 'The answer is 470.'

