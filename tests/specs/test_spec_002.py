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
]


def test_spec_batch_002() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
