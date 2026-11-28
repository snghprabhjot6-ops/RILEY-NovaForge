"""Verification spec batch 039: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (33 - 8) * 3?', 'The answer is 75.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(3828 % 14) + 8!', 'The answer is 14.'),
    ('calculate 6 ** 2 + 4', 'The answer is 40.'),
    ('calculate 3812 + 7 * 11?', 'The answer is 3889.'),
]


def test_spec_batch_039() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
