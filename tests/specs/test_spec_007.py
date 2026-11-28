"""Verification spec batch 007: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (34 - 6) * 3?', 'The answer is 84.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(628 % 10) + 6!', 'The answer is 14.'),
    ('calculate 6 ** 3 + 4', 'The answer is 220.'),
    ('calculate 612 + 18 * 1?', 'The answer is 630.'),
    ('what is (39 - 11) * 3.', 'The answer is 84.'),
    ('calc (119 * 6) / 3!', 'The answer is 238.'),
    ('(633 % 15) + 11', 'The answer is 14.'),
    ('calculate 3 ** 2 + 9?', 'The answer is 18.'),
    ('calculate 617 + 4 * 6.', 'The answer is 641.'),
    ('what is (44 - 3) * 3!', 'The answer is 123.'),
    ('calc (124 * 6) / 3', 'The answer is 248.'),
    ('(638 % 3) + 3?', 'The answer is 5.'),
]


def test_spec_batch_007() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
