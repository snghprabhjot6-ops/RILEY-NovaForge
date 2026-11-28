"""Verification spec batch 071: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record unhelpful status entry 7001',
    'Record thankful status entry 7002',
]


def test_spec_batch_071() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
