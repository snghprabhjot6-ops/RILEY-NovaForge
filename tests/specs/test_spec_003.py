"""Verification spec batch 003: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (22 - 9) * 3?', 'The answer is 39.'),
]


def test_spec_batch_003() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
