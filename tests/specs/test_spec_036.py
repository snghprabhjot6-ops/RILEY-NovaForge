"""Verification spec batch 036: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (24 - 7) * 3?', 'The answer is 51.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
]


def test_spec_batch_036() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
