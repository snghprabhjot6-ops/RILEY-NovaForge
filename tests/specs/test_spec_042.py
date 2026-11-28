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
]


def test_spec_batch_042() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
