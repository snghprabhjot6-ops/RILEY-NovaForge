"""Verification spec batch 074: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record unhelpful status entry 7301',
    'Record thankful status entry 7302',
    'Record thankless status entry 7303',
    'Record maiden status entry 7304',
    'Record braided status entry 7305',
    'Record thorax status entry 7306',
    'Record choral status entry 7307',
    'Record storage status entry 7308',
    'Record shipping status entry 7309',
    'Record whisper status entry 7310',
    'Record archive status entry 7311',
    'Record thinking status entry 7312',
    'Record vehicle status entry 7313',
    'Record holiday status entry 7314',
    'Record scholar status entry 7315',
    'Record commercial status entry 7316',
    'Record integrate status entry 7317',
]


def test_spec_batch_074() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
