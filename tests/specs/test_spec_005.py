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
    ('calc (174 * 6) / 3', 'The answer is 348.'),
    ('(438 % 7) + 11?', 'The answer is 15.'),
    ('calculate 8 ** 2 + 14.', 'The answer is 78.'),
    ('calculate 422 + 18 * 9!', 'The answer is 584.'),
    ('what is (43 - 3) * 3', 'The answer is 120.'),
    ('calc (179 * 6) / 3?', 'The answer is 358.'),
    ('(443 % 12) + 3.', 'The answer is 14.'),
    ('calculate 5 ** 4 + 19!', 'The answer is 644.'),
    ('calculate 427 + 4 * 3', 'The answer is 439.'),
    ('what is (48 - 8) * 3?', 'The answer is 120.'),
    ('calc (184 * 6) / 3.', 'The answer is 368.'),
    ('(448 % 17) + 8!', 'The answer is 14.'),
]


def test_spec_batch_005() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
