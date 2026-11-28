"""Verification spec batch 021: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (76 - 15) * 3?', 'The answer is 183.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(2028 % 16) + 15!', 'The answer is 27.'),
    ('calculate 6 ** 2 + 4', 'The answer is 40.'),
    ('calculate 2012 + 12 * 4?', 'The answer is 2060.'),
    ('what is (81 - 7) * 3.', 'The answer is 222.'),
    ('calc (19 * 6) / 3!', 'The answer is 38.'),
    ('(2033 % 4) + 7', 'The answer is 8.'),
    ('calculate 3 ** 4 + 9?', 'The answer is 90.'),
    ('calculate 2017 + 17 * 9.', 'The answer is 2170.'),
    ('what is (86 - 12) * 3!', 'The answer is 222.'),
    ('calc (24 * 6) / 3', 'The answer is 48.'),
    ('(2038 % 9) + 12?', 'The answer is 16.'),
    ('calculate 8 ** 3 + 14.', 'The answer is 526.'),
    ('calculate 2022 + 3 * 3!', 'The answer is 2031.'),
    ('what is (91 - 4) * 3', 'The answer is 261.'),
    ('calc (29 * 6) / 3?', 'The answer is 58.'),
    ('(2043 % 14) + 4.', 'The answer is 17.'),
    ('calculate 5 ** 2 + 19!', 'The answer is 44.'),
    ('calculate 2027 + 8 * 8', 'The answer is 2091.'),
    ('what is (96 - 9) * 3?', 'The answer is 261.'),
    ('calc (34 * 6) / 3.', 'The answer is 68.'),
    ('(2048 % 2) + 9!', 'The answer is 9.'),
    ('calculate 2 ** 4 + 24', 'The answer is 40.'),
    ('calculate 2032 + 13 * 2?', 'The answer is 2058.'),
    ('what is (101 - 14) * 3.', 'The answer is 261.'),
    ('calc (39 * 6) / 3!', 'The answer is 78.'),
    ('(2053 % 7) + 14', 'The answer is 16.'),
    ('calculate 7 ** 3 + 29?', 'The answer is 372.'),
    ('calculate 2037 + 18 * 7.', 'The answer is 2163.'),
    ('what is (106 - 6) * 3!', 'The answer is 300.'),
    ('calc (44 * 6) / 3', 'The answer is 88.'),
    ('(2058 % 12) + 6?', 'The answer is 12.'),
    ('calculate 4 ** 2 + 34.', 'The answer is 50.'),
    ('calculate 2042 + 4 * 1!', 'The answer is 2046.'),
    ('what is (111 - 11) * 3', 'The answer is 300.'),
    ('calc (49 * 6) / 3?', 'The answer is 98.'),
    ('(2063 % 17) + 11.', 'The answer is 17.'),
    ('calculate 9 ** 4 + 39!', 'The answer is 6600.'),
    ('calculate 2047 + 9 * 6', 'The answer is 2101.'),
    ('what is (19 - 3) * 3?', 'The answer is 48.'),
    ('calc (54 * 6) / 3.', 'The answer is 108.'),
    ('(2068 % 5) + 3!', 'The answer is 6.'),
    ('calculate 6 ** 3 + 44', 'The answer is 260.'),
    ('calculate 2052 + 14 * 11?', 'The answer is 2206.'),
    ('what is (24 - 8) * 3.', 'The answer is 48.'),
    ('calc (59 * 6) / 3!', 'The answer is 118.'),
    ('(2073 % 10) + 8', 'The answer is 11.'),
    ('calculate 3 ** 2 + 49?', 'The answer is 58.'),
    ('calculate 2057 + 19 * 5.', 'The answer is 2152.'),
    ('what is (29 - 13) * 3!', 'The answer is 48.'),
    ('calc (64 * 6) / 3', 'The answer is 128.'),
    ('(2078 % 15) + 13?', 'The answer is 21.'),
]


def test_spec_batch_021() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
