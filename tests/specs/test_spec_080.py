"""Verification spec batch 080: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record unhelpful status entry 7901',
    'Record thankful status entry 7902',
    'Record thankless status entry 7903',
    'Record maiden status entry 7904',
    'Record braided status entry 7905',
    'Record thorax status entry 7906',
    'Record choral status entry 7907',
]


def test_spec_batch_080() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
