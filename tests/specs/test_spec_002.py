"""Verification spec batch 002: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (19 - 13) * 3?', 'The answer is 18.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(128 % 3) + 13!', 'The answer is 15.'),
    ('calculate 2 ** 4 + 4', 'The answer is 20.'),
    ('calculate 112 + 12 * 7?', 'The answer is 196.'),
    ('what is (24 - 5) * 3.', 'The answer is 57.'),
    ('calc (119 * 6) / 3!', 'The answer is 238.'),
    ('(133 % 8) + 5', 'The answer is 10.'),
    ('calculate 7 ** 3 + 9?', 'The answer is 352.'),
    ('calculate 117 + 17 * 1.', 'The answer is 134.'),
    ('what is (29 - 10) * 3!', 'The answer is 57.'),
    ('calc (124 * 6) / 3', 'The answer is 248.'),
    ('(138 % 13) + 10?', 'The answer is 18.'),
    ('calculate 4 ** 2 + 14.', 'The answer is 30.'),
    ('calculate 122 + 3 * 6!', 'The answer is 140.'),
    ('what is (34 - 15) * 3', 'The answer is 57.'),
    ('calc (129 * 6) / 3?', 'The answer is 258.'),
    ('(143 % 18) + 15.', 'The answer is 32.'),
    ('calculate 9 ** 4 + 19!', 'The answer is 6580.'),
    ('calculate 127 + 8 * 11', 'The answer is 215.'),
    ('what is (39 - 7) * 3?', 'The answer is 96.'),
    ('calc (134 * 6) / 3.', 'The answer is 268.'),
    ('(148 % 6) + 7!', 'The answer is 11.'),
    ('calculate 6 ** 3 + 24', 'The answer is 240.'),
    ('calculate 132 + 13 * 5?', 'The answer is 197.'),
    ('what is (44 - 12) * 3.', 'The answer is 96.'),
    ('calc (139 * 6) / 3!', 'The answer is 278.'),
    ('(153 % 11) + 12', 'The answer is 22.'),
    ('calculate 3 ** 2 + 29?', 'The answer is 38.'),
    ('calculate 137 + 18 * 10.', 'The answer is 317.'),
    ('what is (49 - 4) * 3!', 'The answer is 135.'),
    ('calc (144 * 6) / 3', 'The answer is 288.'),
    ('(158 % 16) + 4?', 'The answer is 18.'),
    ('calculate 8 ** 4 + 34.', 'The answer is 4130.'),
    ('calculate 142 + 4 * 4!', 'The answer is 158.'),
]


def test_spec_batch_002() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
