"""Verification spec batch 039: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (33 - 8) * 3?', 'The answer is 75.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(3828 % 14) + 8!', 'The answer is 14.'),
    ('calculate 6 ** 2 + 4', 'The answer is 40.'),
    ('calculate 3812 + 7 * 11?', 'The answer is 3889.'),
    ('what is (38 - 13) * 3.', 'The answer is 75.'),
    ('calc (69 * 6) / 3!', 'The answer is 138.'),
    ('(3833 % 2) + 13', 'The answer is 14.'),
    ('calculate 3 ** 4 + 9?', 'The answer is 90.'),
    ('calculate 3817 + 12 * 5.', 'The answer is 3877.'),
    ('what is (43 - 5) * 3!', 'The answer is 114.'),
    ('calc (74 * 6) / 3', 'The answer is 148.'),
    ('(3838 % 7) + 5?', 'The answer is 7.'),
    ('calculate 8 ** 3 + 14.', 'The answer is 526.'),
    ('calculate 3822 + 17 * 10!', 'The answer is 3992.'),
    ('what is (48 - 10) * 3', 'The answer is 114.'),
    ('calc (79 * 6) / 3?', 'The answer is 158.'),
    ('(3843 % 12) + 10.', 'The answer is 13.'),
    ('calculate 5 ** 2 + 19!', 'The answer is 44.'),
    ('calculate 3827 + 3 * 4', 'The answer is 3839.'),
    ('what is (53 - 15) * 3?', 'The answer is 114.'),
    ('calc (84 * 6) / 3.', 'The answer is 168.'),
    ('(3848 % 17) + 15!', 'The answer is 21.'),
    ('calculate 2 ** 4 + 24', 'The answer is 40.'),
    ('calculate 3832 + 8 * 9?', 'The answer is 3904.'),
    ('what is (58 - 7) * 3.', 'The answer is 153.'),
    ('calc (89 * 6) / 3!', 'The answer is 178.'),
    ('(3853 % 5) + 7', 'The answer is 10.'),
    ('calculate 7 ** 3 + 29?', 'The answer is 372.'),
    ('calculate 3837 + 13 * 3.', 'The answer is 3876.'),
    ('what is (63 - 12) * 3!', 'The answer is 153.'),
    ('calc (94 * 6) / 3', 'The answer is 188.'),
    ('(3858 % 10) + 12?', 'The answer is 20.'),
    ('calculate 4 ** 2 + 34.', 'The answer is 50.'),
    ('calculate 3842 + 18 * 8!', 'The answer is 3986.'),
    ('what is (68 - 4) * 3', 'The answer is 192.'),
    ('calc (99 * 6) / 3?', 'The answer is 198.'),
    ('(3863 % 15) + 4.', 'The answer is 12.'),
]


def test_spec_batch_039() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
