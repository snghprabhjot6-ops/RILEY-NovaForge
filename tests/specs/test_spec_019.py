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
    ('calculate 5 ** 3 + 19!', 'The answer is 144.'),
    ('calculate 1827 + 17 * 6', 'The answer is 1929.'),
    ('what is (90 - 4) * 3?', 'The answer is 258.'),
    ('calc (84 * 6) / 3.', 'The answer is 168.'),
    ('(1848 % 6) + 4!', 'The answer is 4.'),
    ('calculate 2 ** 2 + 24', 'The answer is 28.'),
    ('calculate 1832 + 3 * 11?', 'The answer is 1865.'),
    ('what is (95 - 9) * 3.', 'The answer is 258.'),
    ('calc (89 * 6) / 3!', 'The answer is 178.'),
    ('(1853 % 11) + 9', 'The answer is 14.'),
    ('calculate 7 ** 4 + 29?', 'The answer is 2430.'),
    ('calculate 1837 + 8 * 5.', 'The answer is 1877.'),
    ('what is (100 - 14) * 3!', 'The answer is 258.'),
    ('calc (94 * 6) / 3', 'The answer is 188.'),
    ('(1858 % 16) + 14?', 'The answer is 16.'),
    ('calculate 4 ** 3 + 34.', 'The answer is 98.'),
    ('calculate 1842 + 13 * 10!', 'The answer is 1972.'),
    ('what is (105 - 6) * 3', 'The answer is 297.'),
    ('calc (99 * 6) / 3?', 'The answer is 198.'),
    ('(1863 % 4) + 6.', 'The answer is 9.'),
]


def test_spec_batch_019() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
