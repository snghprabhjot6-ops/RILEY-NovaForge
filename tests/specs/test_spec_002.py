"""Verification spec batch 002: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (19 - 13) * 3?', 'The answer is 18.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(128 % 3) + 13!', 'The answer is 15.'),
    ('calculate 2 ** 4 + 4', 'The answer is 20.'),
]


def test_spec_batch_002() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
