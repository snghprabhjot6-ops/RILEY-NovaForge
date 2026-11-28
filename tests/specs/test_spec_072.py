"""Verification spec batch 072: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record archive status entry 7101',
    'Record thinking status entry 7102',
    'Record vehicle status entry 7103',
    'Record holiday status entry 7104',
    'Record scholar status entry 7105',
    'Record commercial status entry 7106',
    'Record integrate status entry 7107',
]


def test_spec_batch_072() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
