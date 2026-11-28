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
    'Record thankless status entry 8113',
    'Record maiden status entry 8114',
    'Record braided status entry 8115',
    'Record thorax status entry 8116',
    'Record choral status entry 8117',
    'Record storage status entry 8118',
    'Record shipping status entry 8119',
    'Record whisper status entry 8120',
    'Record archive status entry 8121',
    'Record thinking status entry 8122',
    'Record vehicle status entry 8123',
    'Record holiday status entry 8124',
    'Record scholar status entry 8125',
    'Record commercial status entry 8126',
    'Record integrate status entry 8127',
    'Record parameter status entry 8128',
    'Record runtime status entry 8129',
    'Record update status entry 8130',
    'Record candidate status entry 8131',
]


def test_spec_batch_082() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
