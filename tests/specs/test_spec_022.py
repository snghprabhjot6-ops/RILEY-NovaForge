"""Verification spec batch 022: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (79 - 11) * 3?', 'The answer is 204.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(2128 % 14) + 11!', 'The answer is 11.'),
    ('calculate 2 ** 3 + 4', 'The answer is 12.'),
    ('calculate 2112 + 17 * 5?', 'The answer is 2197.'),
    ('what is (84 - 3) * 3.', 'The answer is 243.'),
    ('calc (119 * 6) / 3!', 'The answer is 238.'),
    ('(2133 % 2) + 3', 'The answer is 4.'),
    ('calculate 7 ** 2 + 9?', 'The answer is 58.'),
    ('calculate 2117 + 3 * 10.', 'The answer is 2147.'),
    ('what is (89 - 8) * 3!', 'The answer is 243.'),
    ('calc (124 * 6) / 3', 'The answer is 248.'),
    ('(2138 % 7) + 8?', 'The answer is 11.'),
    ('calculate 4 ** 4 + 14.', 'The answer is 270.'),
    ('calculate 2122 + 8 * 4!', 'The answer is 2154.'),
    ('what is (94 - 13) * 3', 'The answer is 243.'),
    ('calc (129 * 6) / 3?', 'The answer is 258.'),
    ('(2143 % 12) + 13.', 'The answer is 20.'),
    ('calculate 9 ** 3 + 19!', 'The answer is 748.'),
    ('calculate 2127 + 13 * 9', 'The answer is 2244.'),
    ('what is (99 - 5) * 3?', 'The answer is 282.'),
    ('calc (134 * 6) / 3.', 'The answer is 268.'),
    ('(2148 % 17) + 5!', 'The answer is 11.'),
    ('calculate 6 ** 2 + 24', 'The answer is 60.'),
    ('calculate 2132 + 18 * 3?', 'The answer is 2186.'),
    ('what is (104 - 10) * 3.', 'The answer is 282.'),
    ('calc (139 * 6) / 3!', 'The answer is 278.'),
    ('(2153 % 5) + 10', 'The answer is 13.'),
    ('calculate 3 ** 4 + 29?', 'The answer is 110.'),
    ('calculate 2137 + 4 * 8.', 'The answer is 2169.'),
    ('what is (109 - 15) * 3!', 'The answer is 282.'),
    ('calc (144 * 6) / 3', 'The answer is 288.'),
    ('(2158 % 10) + 15?', 'The answer is 23.'),
    ('calculate 8 ** 3 + 34.', 'The answer is 546.'),
    ('calculate 2142 + 9 * 2!', 'The answer is 2160.'),
    ('what is (17 - 7) * 3', 'The answer is 30.'),
    ('calc (149 * 6) / 3?', 'The answer is 298.'),
    ('(2163 % 15) + 7.', 'The answer is 10.'),
    ('calculate 5 ** 2 + 39!', 'The answer is 64.'),
    ('calculate 2147 + 14 * 7', 'The answer is 2245.'),
    ('what is (22 - 12) * 3?', 'The answer is 30.'),
    ('calc (154 * 6) / 3.', 'The answer is 308.'),
    ('(2168 % 3) + 12!', 'The answer is 14.'),
    ('calculate 2 ** 4 + 44', 'The answer is 60.'),
    ('calculate 2152 + 19 * 1?', 'The answer is 2171.'),
]


def test_spec_batch_022() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
