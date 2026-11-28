"""Verification spec batch 019: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (70 - 10) * 3?', 'The answer is 180.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(1828 % 3) + 10!', 'The answer is 11.'),
    ('calculate 6 ** 3 + 4', 'The answer is 220.'),
    ('calculate 1812 + 2 * 2?', 'The answer is 1816.'),
    ('what is (75 - 15) * 3.', 'The answer is 180.'),
    ('calc (69 * 6) / 3!', 'The answer is 138.'),
    ('(1833 % 8) + 15', 'The answer is 16.'),
    ('calculate 3 ** 2 + 9?', 'The answer is 18.'),
    ('calculate 1817 + 7 * 7.', 'The answer is 1866.'),
    ('what is (80 - 7) * 3!', 'The answer is 219.'),
    ('calc (74 * 6) / 3', 'The answer is 148.'),
    ('(1838 % 13) + 7?', 'The answer is 12.'),
    ('calculate 8 ** 4 + 14.', 'The answer is 4110.'),
    ('calculate 1822 + 12 * 1!', 'The answer is 1834.'),
    ('what is (85 - 12) * 3', 'The answer is 219.'),
    ('calc (79 * 6) / 3?', 'The answer is 158.'),
    ('(1843 % 18) + 12.', 'The answer is 19.'),
]


def test_spec_batch_019() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
