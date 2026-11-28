"""Verification spec batch 042: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (42 - 9) * 3?', 'The answer is 99.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(4128 % 8) + 9!', 'The answer is 9.'),
    ('calculate 2 ** 2 + 4', 'The answer is 8.'),
    ('calculate 4112 + 3 * 3?', 'The answer is 4121.'),
    ('what is (47 - 14) * 3.', 'The answer is 99.'),
    ('calc (119 * 6) / 3!', 'The answer is 238.'),
    ('(4133 % 13) + 14', 'The answer is 26.'),
    ('calculate 7 ** 4 + 9?', 'The answer is 2410.'),
    ('calculate 4117 + 8 * 8.', 'The answer is 4181.'),
    ('what is (52 - 6) * 3!', 'The answer is 138.'),
    ('calc (124 * 6) / 3', 'The answer is 248.'),
    ('(4138 % 18) + 6?', 'The answer is 22.'),
    ('calculate 4 ** 3 + 14.', 'The answer is 78.'),
    ('calculate 4122 + 13 * 2!', 'The answer is 4148.'),
    ('what is (57 - 11) * 3', 'The answer is 138.'),
    ('calc (129 * 6) / 3?', 'The answer is 258.'),
    ('(4143 % 6) + 11.', 'The answer is 14.'),
    ('calculate 9 ** 2 + 19!', 'The answer is 100.'),
    ('calculate 4127 + 18 * 7', 'The answer is 4253.'),
    ('what is (62 - 3) * 3?', 'The answer is 177.'),
    ('calc (134 * 6) / 3.', 'The answer is 268.'),
    ('(4148 % 11) + 3!', 'The answer is 4.'),
    ('calculate 6 ** 4 + 24', 'The answer is 1320.'),
    ('calculate 4132 + 4 * 1?', 'The answer is 4136.'),
    ('what is (67 - 8) * 3.', 'The answer is 177.'),
    ('calc (139 * 6) / 3!', 'The answer is 278.'),
    ('(4153 % 16) + 8', 'The answer is 17.'),
    ('calculate 3 ** 3 + 29?', 'The answer is 56.'),
    ('calculate 4137 + 9 * 6.', 'The answer is 4191.'),
    ('what is (72 - 13) * 3!', 'The answer is 177.'),
    ('calc (144 * 6) / 3', 'The answer is 288.'),
    ('(4158 % 4) + 13?', 'The answer is 15.'),
    ('calculate 8 ** 2 + 34.', 'The answer is 98.'),
    ('calculate 4142 + 14 * 11!', 'The answer is 4296.'),
    ('what is (77 - 5) * 3', 'The answer is 216.'),
    ('calc (149 * 6) / 3?', 'The answer is 298.'),
    ('(4163 % 9) + 5.', 'The answer is 10.'),
    ('calculate 5 ** 4 + 39!', 'The answer is 664.'),
    ('calculate 4147 + 19 * 5', 'The answer is 4242.'),
    ('what is (82 - 10) * 3?', 'The answer is 216.'),
    ('calc (154 * 6) / 3.', 'The answer is 308.'),
    ('(4168 % 14) + 10!', 'The answer is 20.'),
    ('calculate 2 ** 3 + 44', 'The answer is 52.'),
    ('calculate 4152 + 5 * 10?', 'The answer is 4202.'),
    ('what is (87 - 15) * 3.', 'The answer is 216.'),
    ('calc (159 * 6) / 3!', 'The answer is 318.'),
]


def test_spec_batch_042() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
