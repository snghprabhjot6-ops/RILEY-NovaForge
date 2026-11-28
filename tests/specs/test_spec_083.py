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
    'Record shipping status entry 8209',
    'Record whisper status entry 8210',
    'Record archive status entry 8211',
    'Record thinking status entry 8212',
    'Record vehicle status entry 8213',
    'Record holiday status entry 8214',
    'Record scholar status entry 8215',
    'Record commercial status entry 8216',
    'Record integrate status entry 8217',
]


def test_spec_batch_083() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
