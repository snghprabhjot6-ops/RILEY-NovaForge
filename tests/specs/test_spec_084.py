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
    'Record mandate status entry 8313',
    'Record outdated status entry 8314',
    'Record sometimes status entry 8315',
    'Record lifetime status entry 8316',
    'Record overtime status entry 8317',
    'Record daytime status entry 8318',
    'Record nighttime status entry 8319',
    'Record helpful status entry 8320',
    'Record unhelpful status entry 8321',
    'Record thankful status entry 8322',
    'Record thankless status entry 8323',
    'Record maiden status entry 8324',
    'Record braided status entry 8325',
    'Record thorax status entry 8326',
    'Record choral status entry 8327',
    'Record storage status entry 8328',
    'Record shipping status entry 8329',
    'Record whisper status entry 8330',
    'Record archive status entry 8331',
    'Record thinking status entry 8332',
    'Record vehicle status entry 8333',
    'Record holiday status entry 8334',
    'Record scholar status entry 8335',
    'Record commercial status entry 8336',
    'Record integrate status entry 8337',
    'Record parameter status entry 8338',
    'Record runtime status entry 8339',
    'Record update status entry 8340',
    'Record candidate status entry 8341',
    'Record validate status entry 8342',
    'Record mandate status entry 8343',
    'Record outdated status entry 8344',
    'Record sometimes status entry 8345',
    'Record lifetime status entry 8346',
    'Record overtime status entry 8347',
    'Record daytime status entry 8348',
    'Record nighttime status entry 8349',
    'Record helpful status entry 8350',
]


def test_spec_batch_084() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
