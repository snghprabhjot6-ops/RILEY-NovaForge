"""Verification spec batch 038: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (30 - 12) * 3?', 'The answer is 54.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(3728 % 16) + 12!', 'The answer is 12.'),
    ('calculate 2 ** 4 + 4', 'The answer is 20.'),
    ('calculate 3712 + 2 * 10?', 'The answer is 3732.'),
    ('what is (35 - 4) * 3.', 'The answer is 93.'),
    ('calc (219 * 6) / 3!', 'The answer is 438.'),
    ('(3733 % 4) + 4', 'The answer is 5.'),
    ('calculate 7 ** 3 + 9?', 'The answer is 352.'),
    ('calculate 3717 + 7 * 4.', 'The answer is 3745.'),
    ('what is (40 - 9) * 3!', 'The answer is 93.'),
    ('calc (224 * 6) / 3', 'The answer is 448.'),
    ('(3738 % 9) + 9?', 'The answer is 12.'),
    ('calculate 4 ** 2 + 14.', 'The answer is 30.'),
    ('calculate 3722 + 12 * 9!', 'The answer is 3830.'),
    ('what is (45 - 14) * 3', 'The answer is 93.'),
    ('calc (229 * 6) / 3?', 'The answer is 458.'),
    ('(3743 % 14) + 14.', 'The answer is 19.'),
    ('calculate 9 ** 4 + 19!', 'The answer is 6580.'),
    ('calculate 3727 + 17 * 3', 'The answer is 3778.'),
    ('what is (50 - 6) * 3?', 'The answer is 132.'),
    ('calc (234 * 6) / 3.', 'The answer is 468.'),
    ('(3748 % 2) + 6!', 'The answer is 6.'),
    ('calculate 6 ** 3 + 24', 'The answer is 240.'),
    ('calculate 3732 + 3 * 8?', 'The answer is 3756.'),
    ('what is (55 - 11) * 3.', 'The answer is 132.'),
    ('calc (239 * 6) / 3!', 'The answer is 478.'),
    ('(3753 % 7) + 11', 'The answer is 12.'),
    ('calculate 3 ** 2 + 29?', 'The answer is 38.'),
    ('calculate 3737 + 8 * 2.', 'The answer is 3753.'),
    ('what is (60 - 3) * 3!', 'The answer is 171.'),
    ('calc (244 * 6) / 3', 'The answer is 488.'),
    ('(3758 % 12) + 3?', 'The answer is 5.'),
    ('calculate 8 ** 4 + 34.', 'The answer is 4130.'),
    ('calculate 3742 + 13 * 7!', 'The answer is 3833.'),
    ('what is (65 - 8) * 3', 'The answer is 171.'),
    ('calc (249 * 6) / 3?', 'The answer is 498.'),
    ('(3763 % 17) + 8.', 'The answer is 14.'),
    ('calculate 5 ** 3 + 39!', 'The answer is 164.'),
    ('calculate 3747 + 18 * 1', 'The answer is 3765.'),
    ('what is (70 - 13) * 3?', 'The answer is 171.'),
    ('calc (254 * 6) / 3.', 'The answer is 508.'),
    ('(3768 % 5) + 13!', 'The answer is 16.'),
]


def test_spec_batch_038() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
