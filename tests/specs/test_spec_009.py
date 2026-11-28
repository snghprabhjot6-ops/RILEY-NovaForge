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
    ('(838 % 16) + 8?', 'The answer is 14.'),
    ('calculate 8 ** 3 + 14.', 'The answer is 526.'),
    ('calculate 822 + 19 * 2!', 'The answer is 860.'),
    ('what is (55 - 13) * 3', 'The answer is 126.'),
    ('calc (79 * 6) / 3?', 'The answer is 158.'),
    ('(843 % 4) + 13.', 'The answer is 16.'),
    ('calculate 5 ** 2 + 19!', 'The answer is 44.'),
    ('calculate 827 + 5 * 7', 'The answer is 862.'),
    ('what is (60 - 5) * 3?', 'The answer is 165.'),
    ('calc (84 * 6) / 3.', 'The answer is 168.'),
    ('(848 % 9) + 5!', 'The answer is 7.'),
    ('calculate 2 ** 4 + 24', 'The answer is 40.'),
    ('calculate 832 + 10 * 1?', 'The answer is 842.'),
    ('what is (65 - 10) * 3.', 'The answer is 165.'),
    ('calc (89 * 6) / 3!', 'The answer is 178.'),
    ('(853 % 14) + 10', 'The answer is 23.'),
    ('calculate 7 ** 3 + 29?', 'The answer is 372.'),
    ('calculate 837 + 15 * 6.', 'The answer is 927.'),
    ('what is (70 - 15) * 3!', 'The answer is 165.'),
    ('calc (94 * 6) / 3', 'The answer is 188.'),
    ('(858 % 2) + 15?', 'The answer is 15.'),
]


def test_spec_batch_009() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
