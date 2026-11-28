"""Verification spec batch 078: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record archive status entry 7701',
    'Record thinking status entry 7702',
    'Record vehicle status entry 7703',
]


def test_spec_batch_078() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
