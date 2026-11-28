"""Verification spec batch 012: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (49 - 12) * 3?', 'The answer is 111.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(1128 % 17) + 12!', 'The answer is 18.'),
    ('calculate 2 ** 2 + 4', 'The answer is 8.'),
    ('calculate 1112 + 5 * 6?', 'The answer is 1142.'),
    ('what is (54 - 4) * 3.', 'The answer is 150.'),
    ('calc (119 * 6) / 3!', 'The answer is 238.'),
    ('(1133 % 5) + 4', 'The answer is 7.'),
    ('calculate 7 ** 4 + 9?', 'The answer is 2410.'),
    ('calculate 1117 + 10 * 11.', 'The answer is 1227.'),
    ('what is (59 - 9) * 3!', 'The answer is 150.'),
    ('calc (124 * 6) / 3', 'The answer is 248.'),
    ('(1138 % 10) + 9?', 'The answer is 17.'),
    ('calculate 4 ** 3 + 14.', 'The answer is 78.'),
    ('calculate 1122 + 15 * 5!', 'The answer is 1197.'),
    ('what is (64 - 14) * 3', 'The answer is 150.'),
    ('calc (129 * 6) / 3?', 'The answer is 258.'),
    ('(1143 % 15) + 14.', 'The answer is 17.'),
    ('calculate 9 ** 2 + 19!', 'The answer is 100.'),
    ('calculate 1127 + 20 * 10', 'The answer is 1327.'),
    ('what is (69 - 6) * 3?', 'The answer is 189.'),
    ('calc (134 * 6) / 3.', 'The answer is 268.'),
    ('(1148 % 3) + 6!', 'The answer is 8.'),
    ('calculate 6 ** 4 + 24', 'The answer is 1320.'),
    ('calculate 1132 + 6 * 4?', 'The answer is 1156.'),
    ('what is (74 - 11) * 3.', 'The answer is 189.'),
    ('calc (139 * 6) / 3!', 'The answer is 278.'),
    ('(1153 % 8) + 11', 'The answer is 12.'),
    ('calculate 3 ** 3 + 29?', 'The answer is 56.'),
    ('calculate 1137 + 11 * 9.', 'The answer is 1236.'),
    ('what is (79 - 3) * 3!', 'The answer is 228.'),
    ('calc (144 * 6) / 3', 'The answer is 288.'),
    ('(1158 % 13) + 3?', 'The answer is 4.'),
    ('calculate 8 ** 2 + 34.', 'The answer is 98.'),
    ('calculate 1142 + 16 * 3!', 'The answer is 1190.'),
    ('what is (84 - 8) * 3', 'The answer is 228.'),
    ('calc (149 * 6) / 3?', 'The answer is 298.'),
    ('(1163 % 18) + 8.', 'The answer is 19.'),
    ('calculate 5 ** 4 + 39!', 'The answer is 664.'),
    ('calculate 1147 + 2 * 8', 'The answer is 1163.'),
    ('what is (89 - 13) * 3?', 'The answer is 228.'),
    ('calc (154 * 6) / 3.', 'The answer is 308.'),
    ('(1168 % 6) + 13!', 'The answer is 17.'),
    ('calculate 2 ** 3 + 44', 'The answer is 52.'),
    ('calculate 1152 + 7 * 2?', 'The answer is 1166.'),
]


def test_spec_batch_012() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
