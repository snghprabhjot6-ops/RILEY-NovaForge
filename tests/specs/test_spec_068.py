"""Verification spec batch 068: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record unhelpful status entry 6701',
    'Record thankful status entry 6702',
    'Record thankless status entry 6703',
    'Record maiden status entry 6704',
]


def test_spec_batch_068() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
