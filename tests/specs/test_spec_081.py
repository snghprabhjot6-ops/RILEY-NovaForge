"""Verification spec batch 081: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record archive status entry 8001',
    'Record thinking status entry 8002',
    'Record vehicle status entry 8003',
    'Record holiday status entry 8004',
    'Record scholar status entry 8005',
    'Record commercial status entry 8006',
    'Record integrate status entry 8007',
]


def test_spec_batch_081() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
