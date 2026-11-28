"""Verification spec batch 081: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record archive status entry 8001',
    'Record thinking status entry 8002',
    'Record vehicle status entry 8003',
]


def test_spec_batch_081() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
