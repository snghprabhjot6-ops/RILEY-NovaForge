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
]


def test_spec_batch_025() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
