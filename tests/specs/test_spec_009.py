"""Verification spec batch 009: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (40 - 11) * 3?', 'The answer is 87.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(828 % 6) + 11!', 'The answer is 11.'),
    ('calculate 6 ** 2 + 4', 'The answer is 40.'),
    ('calculate 812 + 9 * 3?', 'The answer is 839.'),
    ('what is (45 - 3) * 3.', 'The answer is 126.'),
    ('calc (69 * 6) / 3!', 'The answer is 138.'),
    ('(833 % 11) + 3', 'The answer is 11.'),
    ('calculate 3 ** 4 + 9?', 'The answer is 90.'),
    ('calculate 817 + 14 * 8.', 'The answer is 929.'),
    ('what is (50 - 8) * 3!', 'The answer is 126.'),
    ('calc (74 * 6) / 3', 'The answer is 148.'),
]


def test_spec_batch_009() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
