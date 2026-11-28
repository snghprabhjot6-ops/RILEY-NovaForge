"""Verification spec batch 070: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record candidate status entry 6901',
    'Record validate status entry 6902',
    'Record mandate status entry 6903',
    'Record outdated status entry 6904',
    'Record sometimes status entry 6905',
]


def test_spec_batch_070() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
