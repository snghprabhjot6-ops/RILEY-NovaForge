"""Verification spec batch 084: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record archive status entry 8301',
    'Record thinking status entry 8302',
    'Record vehicle status entry 8303',
    'Record holiday status entry 8304',
    'Record scholar status entry 8305',
    'Record commercial status entry 8306',
    'Record integrate status entry 8307',
    'Record parameter status entry 8308',
    'Record runtime status entry 8309',
    'Record update status entry 8310',
    'Record candidate status entry 8311',
    'Record validate status entry 8312',
]


def test_spec_batch_084() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
