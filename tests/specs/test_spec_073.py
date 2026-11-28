"""Verification spec batch 073: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record candidate status entry 7201',
    'Record validate status entry 7202',
    'Record mandate status entry 7203',
    'Record outdated status entry 7204',
    'Record sometimes status entry 7205',
    'Record lifetime status entry 7206',
    'Record overtime status entry 7207',
    'Record daytime status entry 7208',
    'Record nighttime status entry 7209',
    'Record helpful status entry 7210',
    'Record unhelpful status entry 7211',
    'Record thankful status entry 7212',
    'Record thankless status entry 7213',
    'Record maiden status entry 7214',
    'Record braided status entry 7215',
    'Record thorax status entry 7216',
    'Record choral status entry 7217',
    'Record storage status entry 7218',
    'Record shipping status entry 7219',
]


def test_spec_batch_073() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
