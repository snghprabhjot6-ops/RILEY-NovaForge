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
]


def test_spec_batch_025() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
