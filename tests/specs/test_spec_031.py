"""Verification spec batch 031: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (106 - 14) * 3?', 'The answer is 276.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(3028 % 13) + 14!', 'The answer is 26.'),
    ('calculate 6 ** 3 + 4', 'The answer is 220.'),
    ('calculate 3012 + 5 * 3?', 'The answer is 3027.'),
    ('what is (111 - 6) * 3.', 'The answer is 315.'),
    ('calc (19 * 6) / 3!', 'The answer is 38.'),
    ('(3033 % 18) + 6', 'The answer is 15.'),
    ('calculate 3 ** 2 + 9?', 'The answer is 18.'),
    ('calculate 3017 + 10 * 8.', 'The answer is 3097.'),
    ('what is (19 - 11) * 3!', 'The answer is 24.'),
    ('calc (24 * 6) / 3', 'The answer is 48.'),
    ('(3038 % 6) + 11?', 'The answer is 13.'),
    ('calculate 8 ** 4 + 14.', 'The answer is 4110.'),
    ('calculate 3022 + 15 * 2!', 'The answer is 3052.'),
    ('what is (24 - 3) * 3', 'The answer is 63.'),
    ('calc (29 * 6) / 3?', 'The answer is 58.'),
    ('(3043 % 11) + 3.', 'The answer is 10.'),
    ('calculate 5 ** 3 + 19!', 'The answer is 144.'),
    ('calculate 3027 + 20 * 7', 'The answer is 3167.'),
    ('what is (29 - 8) * 3?', 'The answer is 63.'),
    ('calc (34 * 6) / 3.', 'The answer is 68.'),
    ('(3048 % 16) + 8!', 'The answer is 16.'),
    ('calculate 2 ** 2 + 24', 'The answer is 28.'),
    ('calculate 3032 + 6 * 1?', 'The answer is 3038.'),
    ('what is (34 - 13) * 3.', 'The answer is 63.'),
    ('calc (39 * 6) / 3!', 'The answer is 78.'),
    ('(3053 % 4) + 13', 'The answer is 14.'),
    ('calculate 7 ** 4 + 29?', 'The answer is 2430.'),
    ('calculate 3037 + 11 * 6.', 'The answer is 3103.'),
    ('what is (39 - 5) * 3!', 'The answer is 102.'),
    ('calc (44 * 6) / 3', 'The answer is 88.'),
    ('(3058 % 9) + 5?', 'The answer is 12.'),
    ('calculate 4 ** 3 + 34.', 'The answer is 98.'),
    ('calculate 3042 + 16 * 11!', 'The answer is 3218.'),
    ('what is (44 - 10) * 3', 'The answer is 102.'),
    ('calc (49 * 6) / 3?', 'The answer is 98.'),
    ('(3063 % 14) + 10.', 'The answer is 21.'),
    ('calculate 9 ** 2 + 39!', 'The answer is 120.'),
    ('calculate 3047 + 2 * 5', 'The answer is 3057.'),
    ('what is (49 - 15) * 3?', 'The answer is 102.'),
    ('calc (54 * 6) / 3.', 'The answer is 108.'),
    ('(3068 % 2) + 15!', 'The answer is 15.'),
    ('calculate 6 ** 4 + 44', 'The answer is 1340.'),
]


def test_spec_batch_031() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
