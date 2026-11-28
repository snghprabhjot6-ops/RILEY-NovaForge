"""Verification spec batch 007: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (34 - 6) * 3?', 'The answer is 84.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(628 % 10) + 6!', 'The answer is 14.'),
]


def test_spec_batch_007() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
