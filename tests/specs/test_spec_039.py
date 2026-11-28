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
]


def test_spec_batch_039() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
