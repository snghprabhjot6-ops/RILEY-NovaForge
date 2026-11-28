"""Verification spec batch 004: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (25 - 5) * 3?', 'The answer is 60.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(328 % 16) + 5!', 'The answer is 13.'),
    ('calculate 2 ** 3 + 4', 'The answer is 12.'),
    ('calculate 312 + 3 * 9?', 'The answer is 339.'),
    ('what is (30 - 10) * 3.', 'The answer is 60.'),
    ('calc (69 * 6) / 3!', 'The answer is 138.'),
    ('(333 % 4) + 10', 'The answer is 11.'),
    ('calculate 7 ** 2 + 9?', 'The answer is 58.'),
    ('calculate 317 + 8 * 3.', 'The answer is 341.'),
    ('what is (35 - 15) * 3!', 'The answer is 60.'),
    ('calc (74 * 6) / 3', 'The answer is 148.'),
]


def test_spec_batch_004() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
