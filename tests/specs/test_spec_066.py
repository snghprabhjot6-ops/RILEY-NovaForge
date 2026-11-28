"""Verification spec batch 066: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record archive status entry 6501',
    'Record thinking status entry 6502',
    'Record vehicle status entry 6503',
    'Record holiday status entry 6504',
    'Record scholar status entry 6505',
    'Record commercial status entry 6506',
    'Record integrate status entry 6507',
    'Record parameter status entry 6508',
    'Record runtime status entry 6509',
    'Record update status entry 6510',
    'Record candidate status entry 6511',
    'Record validate status entry 6512',
    'Record mandate status entry 6513',
    'Record outdated status entry 6514',
    'Record sometimes status entry 6515',
    'Record lifetime status entry 6516',
    'Record overtime status entry 6517',
    'Record daytime status entry 6518',
    'Record nighttime status entry 6519',
    'Record helpful status entry 6520',
    'Record unhelpful status entry 6521',
    'Record thankful status entry 6522',
    'Record thankless status entry 6523',
    'Record maiden status entry 6524',
    'Record braided status entry 6525',
    'Record thorax status entry 6526',
    'Record choral status entry 6527',
    'Record storage status entry 6528',
    'Record shipping status entry 6529',
    'Record whisper status entry 6530',
    'Record archive status entry 6531',
    'Record thinking status entry 6532',
    'Record vehicle status entry 6533',
    'Record holiday status entry 6534',
    'Record scholar status entry 6535',
    'Record commercial status entry 6536',
    'Record integrate status entry 6537',
]


def test_spec_batch_066() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
