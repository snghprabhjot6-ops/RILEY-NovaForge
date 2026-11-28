"""Verification spec batch 017: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (64 - 5) * 3?', 'The answer is 177.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(1628 % 7) + 5!', 'The answer is 9.'),
    ('calculate 6 ** 4 + 4', 'The answer is 1300.'),
    ('calculate 1612 + 11 * 11?', 'The answer is 1733.'),
    ('what is (69 - 10) * 3.', 'The answer is 177.'),
    ('calc (119 * 6) / 3!', 'The answer is 238.'),
    ('(1633 % 12) + 10', 'The answer is 11.'),
    ('calculate 3 ** 3 + 9?', 'The answer is 36.'),
    ('calculate 1617 + 16 * 5.', 'The answer is 1697.'),
    ('what is (74 - 15) * 3!', 'The answer is 177.'),
    ('calc (124 * 6) / 3', 'The answer is 248.'),
    ('(1638 % 17) + 15?', 'The answer is 21.'),
    ('calculate 8 ** 2 + 14.', 'The answer is 78.'),
    ('calculate 1622 + 2 * 10!', 'The answer is 1642.'),
    ('what is (79 - 7) * 3', 'The answer is 216.'),
    ('calc (129 * 6) / 3?', 'The answer is 258.'),
]


def test_spec_batch_017() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
