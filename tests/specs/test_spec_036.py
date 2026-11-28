"""Verification spec batch 036: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (24 - 7) * 3?', 'The answer is 51.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(3528 % 3) + 7!', 'The answer is 7.'),
    ('calculate 2 ** 2 + 4', 'The answer is 8.'),
    ('calculate 3512 + 11 * 8?', 'The answer is 3600.'),
    ('what is (29 - 12) * 3.', 'The answer is 51.'),
    ('calc (19 * 6) / 3!', 'The answer is 38.'),
    ('(3533 % 8) + 12', 'The answer is 17.'),
    ('calculate 7 ** 4 + 9?', 'The answer is 2410.'),
    ('calculate 3517 + 16 * 2.', 'The answer is 3549.'),
    ('what is (34 - 4) * 3!', 'The answer is 90.'),
    ('calc (24 * 6) / 3', 'The answer is 48.'),
    ('(3538 % 13) + 4?', 'The answer is 6.'),
    ('calculate 4 ** 3 + 14.', 'The answer is 78.'),
    ('calculate 3522 + 2 * 7!', 'The answer is 3536.'),
    ('what is (39 - 9) * 3', 'The answer is 90.'),
    ('calc (29 * 6) / 3?', 'The answer is 58.'),
    ('(3543 % 18) + 9.', 'The answer is 24.'),
    ('calculate 9 ** 2 + 19!', 'The answer is 100.'),
    ('calculate 3527 + 7 * 1', 'The answer is 3534.'),
    ('what is (44 - 14) * 3?', 'The answer is 90.'),
    ('calc (34 * 6) / 3.', 'The answer is 68.'),
    ('(3548 % 6) + 14!', 'The answer is 16.'),
    ('calculate 6 ** 4 + 24', 'The answer is 1320.'),
    ('calculate 3532 + 12 * 6?', 'The answer is 3604.'),
    ('what is (49 - 6) * 3.', 'The answer is 129.'),
    ('calc (39 * 6) / 3!', 'The answer is 78.'),
    ('(3553 % 11) + 6', 'The answer is 6.'),
    ('calculate 3 ** 3 + 29?', 'The answer is 56.'),
    ('calculate 3537 + 17 * 11.', 'The answer is 3724.'),
    ('what is (54 - 11) * 3!', 'The answer is 129.'),
    ('calc (44 * 6) / 3', 'The answer is 88.'),
    ('(3558 % 16) + 11?', 'The answer is 17.'),
    ('calculate 8 ** 2 + 34.', 'The answer is 98.'),
    ('calculate 3542 + 3 * 5!', 'The answer is 3557.'),
    ('what is (59 - 3) * 3', 'The answer is 168.'),
    ('calc (49 * 6) / 3?', 'The answer is 98.'),
    ('(3563 % 4) + 3.', 'The answer is 6.'),
    ('calculate 5 ** 4 + 39!', 'The answer is 664.'),
    ('calculate 3547 + 8 * 10', 'The answer is 3627.'),
    ('what is (64 - 8) * 3?', 'The answer is 168.'),
    ('calc (54 * 6) / 3.', 'The answer is 108.'),
    ('(3568 % 9) + 8!', 'The answer is 12.'),
    ('calculate 2 ** 3 + 44', 'The answer is 52.'),
    ('calculate 3552 + 13 * 4?', 'The answer is 3604.'),
    ('what is (69 - 13) * 3.', 'The answer is 168.'),
    ('calc (59 * 6) / 3!', 'The answer is 118.'),
    ('(3573 % 14) + 13', 'The answer is 16.'),
    ('calculate 7 ** 2 + 49?', 'The answer is 98.'),
    ('calculate 3557 + 18 * 9.', 'The answer is 3719.'),
    ('what is (74 - 5) * 3!', 'The answer is 207.'),
    ('calc (64 * 6) / 3', 'The answer is 128.'),
    ('(3578 % 2) + 5?', 'The answer is 5.'),
]


def test_spec_batch_036() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
