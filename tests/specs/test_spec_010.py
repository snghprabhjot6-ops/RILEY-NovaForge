"""Verification spec batch 010: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (43 - 7) * 3?', 'The answer is 108.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(928 % 4) + 7!', 'The answer is 7.'),
    ('calculate 2 ** 3 + 4', 'The answer is 12.'),
    ('calculate 912 + 14 * 4?', 'The answer is 968.'),
    ('what is (48 - 12) * 3.', 'The answer is 108.'),
    ('calc (169 * 6) / 3!', 'The answer is 338.'),
    ('(933 % 9) + 12', 'The answer is 18.'),
    ('calculate 7 ** 2 + 9?', 'The answer is 58.'),
    ('calculate 917 + 19 * 9.', 'The answer is 1088.'),
    ('what is (53 - 4) * 3!', 'The answer is 147.'),
    ('calc (174 * 6) / 3', 'The answer is 348.'),
    ('(938 % 14) + 4?', 'The answer is 4.'),
    ('calculate 4 ** 4 + 14.', 'The answer is 270.'),
    ('calculate 922 + 5 * 3!', 'The answer is 937.'),
    ('what is (58 - 9) * 3', 'The answer is 147.'),
]


def test_spec_batch_010() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
