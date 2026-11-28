"""Verification spec batch 019: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (70 - 10) * 3?', 'The answer is 180.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(1828 % 3) + 10!', 'The answer is 11.'),
]


def test_spec_batch_019() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
