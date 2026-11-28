"""Verification spec batch 077: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record unhelpful status entry 7601',
    'Record thankful status entry 7602',
    'Record thankless status entry 7603',
    'Record maiden status entry 7604',
    'Record braided status entry 7605',
    'Record thorax status entry 7606',
    'Record choral status entry 7607',
    'Record storage status entry 7608',
    'Record shipping status entry 7609',
    'Record whisper status entry 7610',
    'Record archive status entry 7611',
    'Record thinking status entry 7612',
    'Record vehicle status entry 7613',
]


def test_spec_batch_077() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
