"""Verification spec batch 015: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (58 - 13) * 3?', 'The answer is 135.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(1428 % 11) + 13!', 'The answer is 22.'),
    ('calculate 6 ** 2 + 4', 'The answer is 40.'),
    ('calculate 1412 + 20 * 9?', 'The answer is 1592.'),
    ('what is (63 - 5) * 3.', 'The answer is 174.'),
]


def test_spec_batch_015() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
