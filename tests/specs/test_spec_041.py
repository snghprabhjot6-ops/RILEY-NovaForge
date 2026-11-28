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
]


def test_spec_batch_041() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
