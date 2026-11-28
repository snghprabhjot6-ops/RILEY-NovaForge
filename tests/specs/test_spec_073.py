"""Verification spec batch 073: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record candidate status entry 7201',
    'Record validate status entry 7202',
    'Record mandate status entry 7203',
    'Record outdated status entry 7204',
]


def test_spec_batch_073() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
