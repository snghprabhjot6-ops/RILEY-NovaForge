"""Verification spec batch 083: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record unhelpful status entry 8201',
    'Record thankful status entry 8202',
    'Record thankless status entry 8203',
    'Record maiden status entry 8204',
    'Record braided status entry 8205',
    'Record thorax status entry 8206',
    'Record choral status entry 8207',
    'Record storage status entry 8208',
]


def test_spec_batch_083() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
