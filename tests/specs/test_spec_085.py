"""Verification spec batch 085: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record candidate status entry 8401',
    'Record validate status entry 8402',
    'Record mandate status entry 8403',
    'Record outdated status entry 8404',
    'Record sometimes status entry 8405',
]


def test_spec_batch_085() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
