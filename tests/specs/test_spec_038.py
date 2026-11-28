"""Verification spec batch 038: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (30 - 12) * 3?', 'The answer is 54.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
]


def test_spec_batch_038() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
