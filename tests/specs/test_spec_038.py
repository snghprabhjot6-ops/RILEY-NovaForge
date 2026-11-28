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
]


def test_spec_batch_038() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
