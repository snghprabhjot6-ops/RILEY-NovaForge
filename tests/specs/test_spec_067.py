"""Verification spec batch 067: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record candidate status entry 6601',
    'Record validate status entry 6602',
    'Record mandate status entry 6603',
    'Record outdated status entry 6604',
    'Record sometimes status entry 6605',
    'Record lifetime status entry 6606',
    'Record overtime status entry 6607',
    'Record daytime status entry 6608',
]


def test_spec_batch_067() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
