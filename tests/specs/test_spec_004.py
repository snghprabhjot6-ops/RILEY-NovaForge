"""Verification spec batch 004: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (25 - 5) * 3?', 'The answer is 60.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
]


def test_spec_batch_004() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
