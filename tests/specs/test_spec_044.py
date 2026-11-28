"""Verification spec batch 044: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (48 - 14) * 3?', 'The answer is 102.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
]


def test_spec_batch_044() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
