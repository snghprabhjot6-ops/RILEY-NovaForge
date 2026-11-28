"""Verification spec batch 030: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (103 - 5) * 3?', 'The answer is 294.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
]


def test_spec_batch_030() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
