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

def test_arith_precedence_043() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 131 + 6 * 2 - 43')], 'en')
    assert reply == 'The answer is 100.'

def test_arith_precedence_044() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 134 + 7 * 3 - 44')], 'en')
    assert reply == 'The answer is 111.'

def test_arith_precedence_045() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 137 + 8 * 4 - 45')], 'en')
    assert reply == 'The answer is 124.'

def test_arith_precedence_046() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 140 + 9 * 5 - 46')], 'en')
    assert reply == 'The answer is 139.'

def test_arith_precedence_047() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 143 + 10 * 6 - 47')], 'en')
    assert reply == 'The answer is 156.'

def test_arith_precedence_048() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 146 + 11 * 7 - 48')], 'en')
    assert reply == 'The answer is 175.'

def test_arith_precedence_049() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 149 + 12 * 1 - 49')], 'en')
    assert reply == 'The answer is 112.'

def test_arith_precedence_050() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 152 + 13 * 2 - 50')], 'en')
    assert reply == 'The answer is 128.'

def test_arith_precedence_051() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 155 + 14 * 3 - 51')], 'en')
    assert reply == 'The answer is 146.'

def test_arith_precedence_052() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 158 + 2 * 4 - 52')], 'en')
    assert reply == 'The answer is 114.'

def test_arith_precedence_053() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 161 + 3 * 5 - 53')], 'en')
    assert reply == 'The answer is 123.'

def test_arith_precedence_054() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 164 + 4 * 6 - 54')], 'en')
    assert reply == 'The answer is 134.'

def test_arith_precedence_055() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 167 + 5 * 7 - 55')], 'en')
    assert reply == 'The answer is 147.'

def test_arith_precedence_056() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 170 + 6 * 1 - 56')], 'en')
    assert reply == 'The answer is 120.'

def test_arith_precedence_057() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 173 + 7 * 2 - 57')], 'en')
    assert reply == 'The answer is 130.'

def test_arith_precedence_058() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 176 + 8 * 3 - 58')], 'en')
    assert reply == 'The answer is 142.'

def test_arith_precedence_059() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 179 + 9 * 4 - 59')], 'en')
    assert reply == 'The answer is 156.'

def test_arith_precedence_060() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 182 + 10 * 5 - 60')], 'en')
    assert reply == 'The answer is 172.'

def test_arith_precedence_061() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 185 + 11 * 6 - 61')], 'en')
    assert reply == 'The answer is 190.'

def test_arith_precedence_062() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 188 + 12 * 7 - 62')], 'en')
    assert reply == 'The answer is 210.'

def test_arith_precedence_063() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 191 + 13 * 1 - 63')], 'en')
    assert reply == 'The answer is 141.'

def test_arith_precedence_064() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 194 + 14 * 2 - 64')], 'en')
    assert reply == 'The answer is 158.'

def test_arith_precedence_065() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 197 + 2 * 3 - 65')], 'en')
    assert reply == 'The answer is 138.'

def test_arith_precedence_066() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 200 + 3 * 4 - 66')], 'en')
    assert reply == 'The answer is 146.'

def test_arith_precedence_067() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 203 + 4 * 5 - 67')], 'en')
    assert reply == 'The answer is 156.'

def test_arith_precedence_068() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 206 + 5 * 6 - 68')], 'en')
    assert reply == 'The answer is 168.'

def test_arith_precedence_069() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 209 + 6 * 7 - 69')], 'en')
    assert reply == 'The answer is 182.'

def test_arith_precedence_070() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 212 + 7 * 1 - 70')], 'en')
    assert reply == 'The answer is 149.'

def test_arith_precedence_071() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 215 + 8 * 2 - 71')], 'en')
    assert reply == 'The answer is 160.'

def test_arith_precedence_072() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 218 + 9 * 3 - 72')], 'en')
    assert reply == 'The answer is 173.'

def test_arith_precedence_073() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 221 + 10 * 4 - 73')], 'en')
    assert reply == 'The answer is 188.'

def test_arith_precedence_074() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 224 + 11 * 5 - 74')], 'en')
    assert reply == 'The answer is 205.'

def test_arith_precedence_075() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 227 + 12 * 6 - 75')], 'en')
    assert reply == 'The answer is 224.'

def test_arith_precedence_076() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 230 + 13 * 7 - 76')], 'en')
    assert reply == 'The answer is 245.'

def test_arith_precedence_077() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 233 + 14 * 1 - 77')], 'en')
    assert reply == 'The answer is 170.'

def test_arith_precedence_078() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 236 + 2 * 2 - 78')], 'en')
    assert reply == 'The answer is 162.'

def test_arith_precedence_079() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 239 + 3 * 3 - 79')], 'en')
    assert reply == 'The answer is 169.'

def test_arith_precedence_080() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 242 + 4 * 4 - 80')], 'en')
    assert reply == 'The answer is 178.'

def test_arith_precedence_081() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 245 + 5 * 5 - 81')], 'en')
    assert reply == 'The answer is 189.'

def test_arith_precedence_082() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 248 + 6 * 6 - 82')], 'en')
    assert reply == 'The answer is 202.'

def test_arith_precedence_083() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 251 + 7 * 7 - 83')], 'en')
    assert reply == 'The answer is 217.'

def test_arith_precedence_084() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 254 + 8 * 1 - 84')], 'en')
    assert reply == 'The answer is 178.'

def test_arith_precedence_085() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 257 + 9 * 2 - 85')], 'en')
    assert reply == 'The answer is 190.'

def test_arith_precedence_086() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 260 + 10 * 3 - 86')], 'en')
    assert reply == 'The answer is 204.'

def test_arith_precedence_087() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 263 + 11 * 4 - 87')], 'en')
    assert reply == 'The answer is 220.'

def test_arith_precedence_088() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 266 + 12 * 5 - 88')], 'en')
    assert reply == 'The answer is 238.'

def test_arith_precedence_089() -> None:
    reply = _BACKEND.generate([Message('user', 'calculate 269 + 13 * 6 - 89')], 'en')
    assert reply == 'The answer is 258.'

