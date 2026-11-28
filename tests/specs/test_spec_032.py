"""Verification spec batch 032: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (109 - 10) * 3?', 'The answer is 297.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(3128 % 11) + 10!', 'The answer is 14.'),
    ('calculate 2 ** 4 + 4', 'The answer is 20.'),
    ('calculate 3112 + 10 * 4?', 'The answer is 3152.'),
    ('what is (17 - 15) * 3.', 'The answer is 6.'),
    ('calc (119 * 6) / 3!', 'The answer is 238.'),
    ('(3133 % 16) + 15', 'The answer is 28.'),
    ('calculate 7 ** 3 + 9?', 'The answer is 352.'),
    ('calculate 3117 + 15 * 9.', 'The answer is 3252.'),
    ('what is (22 - 7) * 3!', 'The answer is 45.'),
    ('calc (124 * 6) / 3', 'The answer is 248.'),
    ('(3138 % 4) + 7?', 'The answer is 9.'),
    ('calculate 4 ** 2 + 14.', 'The answer is 30.'),
    ('calculate 3122 + 20 * 3!', 'The answer is 3182.'),
    ('what is (27 - 12) * 3', 'The answer is 45.'),
    ('calc (129 * 6) / 3?', 'The answer is 258.'),
    ('(3143 % 9) + 12.', 'The answer is 14.'),
    ('calculate 9 ** 4 + 19!', 'The answer is 6580.'),
    ('calculate 3127 + 6 * 8', 'The answer is 3175.'),
    ('what is (32 - 4) * 3?', 'The answer is 84.'),
    ('calc (134 * 6) / 3.', 'The answer is 268.'),
    ('(3148 % 14) + 4!', 'The answer is 16.'),
    ('calculate 6 ** 3 + 24', 'The answer is 240.'),
    ('calculate 3132 + 11 * 2?', 'The answer is 3154.'),
    ('what is (37 - 9) * 3.', 'The answer is 84.'),
    ('calc (139 * 6) / 3!', 'The answer is 278.'),
    ('(3153 % 2) + 9', 'The answer is 10.'),
    ('calculate 3 ** 2 + 29?', 'The answer is 38.'),
    ('calculate 3137 + 16 * 7.', 'The answer is 3249.'),
    ('what is (42 - 14) * 3!', 'The answer is 84.'),
    ('calc (144 * 6) / 3', 'The answer is 288.'),
    ('(3158 % 7) + 14?', 'The answer is 15.'),
    ('calculate 8 ** 4 + 34.', 'The answer is 4130.'),
    ('calculate 3142 + 2 * 1!', 'The answer is 3144.'),
    ('what is (47 - 6) * 3', 'The answer is 123.'),
    ('calc (149 * 6) / 3?', 'The answer is 298.'),
    ('(3163 % 12) + 6.', 'The answer is 13.'),
    ('calculate 5 ** 3 + 39!', 'The answer is 164.'),
    ('calculate 3147 + 7 * 6', 'The answer is 3189.'),
    ('what is (52 - 11) * 3?', 'The answer is 123.'),
    ('calc (154 * 6) / 3.', 'The answer is 308.'),
    ('(3168 % 17) + 11!', 'The answer is 17.'),
]


def test_spec_batch_032() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
