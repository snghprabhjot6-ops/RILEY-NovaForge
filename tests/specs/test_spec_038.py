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
]


def test_spec_batch_038() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
