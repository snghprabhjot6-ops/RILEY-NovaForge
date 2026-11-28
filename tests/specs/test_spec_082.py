"""Verification spec batch 082: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record candidate status entry 8101',
    'Record validate status entry 8102',
    'Record mandate status entry 8103',
    'Record outdated status entry 8104',
    'Record sometimes status entry 8105',
    'Record lifetime status entry 8106',
    'Record overtime status entry 8107',
    'Record daytime status entry 8108',
    'Record nighttime status entry 8109',
    'Record helpful status entry 8110',
    'Record unhelpful status entry 8111',
    'Record thankful status entry 8112',
]


def test_spec_batch_082() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
