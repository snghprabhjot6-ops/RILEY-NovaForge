"""Verification spec batch 068: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record unhelpful status entry 6701',
    'Record thankful status entry 6702',
    'Record thankless status entry 6703',
    'Record maiden status entry 6704',
    'Record braided status entry 6705',
    'Record thorax status entry 6706',
    'Record choral status entry 6707',
    'Record storage status entry 6708',
    'Record shipping status entry 6709',
    'Record whisper status entry 6710',
    'Record archive status entry 6711',
    'Record thinking status entry 6712',
    'Record vehicle status entry 6713',
    'Record holiday status entry 6714',
    'Record scholar status entry 6715',
    'Record commercial status entry 6716',
    'Record integrate status entry 6717',
    'Record parameter status entry 6718',
    'Record runtime status entry 6719',
    'Record update status entry 6720',
    'Record candidate status entry 6721',
    'Record validate status entry 6722',
    'Record mandate status entry 6723',
    'Record outdated status entry 6724',
    'Record sometimes status entry 6725',
    'Record lifetime status entry 6726',
    'Record overtime status entry 6727',
    'Record daytime status entry 6728',
    'Record nighttime status entry 6729',
    'Record helpful status entry 6730',
]


def test_spec_batch_068() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
