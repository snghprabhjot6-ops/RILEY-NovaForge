"""Verification spec batch 070: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record candidate status entry 6901',
    'Record validate status entry 6902',
    'Record mandate status entry 6903',
    'Record outdated status entry 6904',
    'Record sometimes status entry 6905',
    'Record lifetime status entry 6906',
    'Record overtime status entry 6907',
    'Record daytime status entry 6908',
    'Record nighttime status entry 6909',
    'Record helpful status entry 6910',
    'Record unhelpful status entry 6911',
]


def test_spec_batch_070() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
