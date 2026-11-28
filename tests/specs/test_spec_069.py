"""Verification spec batch 069: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record archive status entry 6801',
    'Record thinking status entry 6802',
    'Record vehicle status entry 6803',
]


def test_spec_batch_069() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
