"""Verification spec batch 084: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record archive status entry 8301',
    'Record thinking status entry 8302',
    'Record vehicle status entry 8303',
]


def test_spec_batch_084() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
