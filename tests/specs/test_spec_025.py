"""Verification spec batch 025: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (88 - 12) * 3?', 'The answer is 228.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(2428 % 8) + 12!', 'The answer is 16.'),
    ('calculate 6 ** 3 + 4', 'The answer is 220.'),
    ('calculate 2412 + 13 * 8?', 'The answer is 2516.'),
    ('what is (93 - 4) * 3.', 'The answer is 267.'),
    ('calc (169 * 6) / 3!', 'The answer is 338.'),
    ('(2433 % 13) + 4', 'The answer is 6.'),
    ('calculate 3 ** 2 + 9?', 'The answer is 18.'),
    ('calculate 2417 + 18 * 2.', 'The answer is 2453.'),
    ('what is (98 - 9) * 3!', 'The answer is 267.'),
    ('calc (174 * 6) / 3', 'The answer is 348.'),
    ('(2438 % 18) + 9?', 'The answer is 17.'),
    ('calculate 8 ** 4 + 14.', 'The answer is 4110.'),
    ('calculate 2422 + 4 * 7!', 'The answer is 2450.'),
    ('what is (103 - 14) * 3', 'The answer is 267.'),
    ('calc (179 * 6) / 3?', 'The answer is 358.'),
    ('(2443 % 6) + 14.', 'The answer is 15.'),
    ('calculate 5 ** 3 + 19!', 'The answer is 144.'),
    ('calculate 2427 + 9 * 1', 'The answer is 2436.'),
    ('what is (108 - 6) * 3?', 'The answer is 306.'),
    ('calc (184 * 6) / 3.', 'The answer is 368.'),
    ('(2448 % 11) + 6!', 'The answer is 12.'),
    ('calculate 2 ** 2 + 24', 'The answer is 28.'),
]


def test_spec_batch_025() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
