"""Verification spec batch 041: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (39 - 13) * 3?', 'The answer is 78.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(4028 % 10) + 13!', 'The answer is 21.'),
    ('calculate 6 ** 4 + 4', 'The answer is 1300.'),
    ('calculate 4012 + 17 * 2?', 'The answer is 4046.'),
    ('what is (44 - 5) * 3.', 'The answer is 117.'),
    ('calc (19 * 6) / 3!', 'The answer is 38.'),
    ('(4033 % 15) + 5', 'The answer is 18.'),
    ('calculate 3 ** 3 + 9?', 'The answer is 36.'),
    ('calculate 4017 + 3 * 7.', 'The answer is 4038.'),
    ('what is (49 - 10) * 3!', 'The answer is 117.'),
    ('calc (24 * 6) / 3', 'The answer is 48.'),
    ('(4038 % 3) + 10?', 'The answer is 10.'),
    ('calculate 8 ** 2 + 14.', 'The answer is 78.'),
    ('calculate 4022 + 8 * 1!', 'The answer is 4030.'),
    ('what is (54 - 15) * 3', 'The answer is 117.'),
    ('calc (29 * 6) / 3?', 'The answer is 58.'),
    ('(4043 % 8) + 15.', 'The answer is 18.'),
    ('calculate 5 ** 4 + 19!', 'The answer is 644.'),
    ('calculate 4027 + 13 * 6', 'The answer is 4105.'),
]


def test_spec_batch_041() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
