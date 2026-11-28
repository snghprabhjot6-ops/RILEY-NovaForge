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
]


def test_spec_batch_022() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
