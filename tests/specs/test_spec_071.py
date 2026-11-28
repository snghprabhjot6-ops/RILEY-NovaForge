"""Verification spec batch 071: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record unhelpful status entry 7001',
    'Record thankful status entry 7002',
    'Record thankless status entry 7003',
    'Record maiden status entry 7004',
    'Record braided status entry 7005',
    'Record thorax status entry 7006',
    'Record choral status entry 7007',
    'Record storage status entry 7008',
    'Record shipping status entry 7009',
    'Record whisper status entry 7010',
    'Record archive status entry 7011',
    'Record thinking status entry 7012',
    'Record vehicle status entry 7013',
    'Record holiday status entry 7014',
    'Record scholar status entry 7015',
    'Record commercial status entry 7016',
    'Record integrate status entry 7017',
    'Record parameter status entry 7018',
    'Record runtime status entry 7019',
    'Record update status entry 7020',
    'Record candidate status entry 7021',
    'Record validate status entry 7022',
    'Record mandate status entry 7023',
    'Record outdated status entry 7024',
    'Record sometimes status entry 7025',
    'Record lifetime status entry 7026',
    'Record overtime status entry 7027',
    'Record daytime status entry 7028',
    'Record nighttime status entry 7029',
    'Record helpful status entry 7030',
    'Record unhelpful status entry 7031',
    'Record thankful status entry 7032',
    'Record thankless status entry 7033',
    'Record maiden status entry 7034',
    'Record braided status entry 7035',
    'Record thorax status entry 7036',
    'Record choral status entry 7037',
    'Record storage status entry 7038',
    'Record shipping status entry 7039',
    'Record whisper status entry 7040',
    'Record archive status entry 7041',
    'Record thinking status entry 7042',
]


def test_spec_batch_071() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
