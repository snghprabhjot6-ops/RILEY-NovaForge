"""Verification spec batch 005: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (28 - 14) * 3?', 'The answer is 42.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(428 % 14) + 14!', 'The answer is 22.'),
    ('calculate 6 ** 4 + 4', 'The answer is 1300.'),
    ('calculate 412 + 8 * 10?', 'The answer is 492.'),
    ('what is (33 - 6) * 3.', 'The answer is 81.'),
    ('calc (169 * 6) / 3!', 'The answer is 338.'),
    ('(433 % 2) + 6', 'The answer is 7.'),
    ('calculate 3 ** 3 + 9?', 'The answer is 36.'),
    ('calculate 417 + 13 * 4.', 'The answer is 469.'),
    ('what is (38 - 11) * 3!', 'The answer is 81.'),
]


def test_spec_batch_005() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
