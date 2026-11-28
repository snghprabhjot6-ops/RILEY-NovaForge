"""Verification spec batch 068: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record unhelpful status entry 6701',
    'Record thankful status entry 6702',
    'Record thankless status entry 6703',
    'Record maiden status entry 6704',
    'Record braided status entry 6705',
    'Record thorax status entry 6706',
    'Record choral status entry 6707',
    'Record storage status entry 6708',
    'Record shipping status entry 6709',
    'Record whisper status entry 6710',
    'Record archive status entry 6711',
]


def test_spec_batch_068() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
