"""Verification spec batch 077: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record unhelpful status entry 7601',
    'Record thankful status entry 7602',
    'Record thankless status entry 7603',
]


def test_spec_batch_077() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
