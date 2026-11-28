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
    'Record nighttime status entry 6609',
    'Record helpful status entry 6610',
    'Record unhelpful status entry 6611',
    'Record thankful status entry 6612',
    'Record thankless status entry 6613',
    'Record maiden status entry 6614',
    'Record braided status entry 6615',
    'Record thorax status entry 6616',
    'Record choral status entry 6617',
    'Record storage status entry 6618',
    'Record shipping status entry 6619',
    'Record whisper status entry 6620',
    'Record archive status entry 6621',
    'Record thinking status entry 6622',
    'Record vehicle status entry 6623',
    'Record holiday status entry 6624',
    'Record scholar status entry 6625',
    'Record commercial status entry 6626',
    'Record integrate status entry 6627',
    'Record parameter status entry 6628',
    'Record runtime status entry 6629',
    'Record update status entry 6630',
    'Record candidate status entry 6631',
    'Record validate status entry 6632',
    'Record mandate status entry 6633',
    'Record outdated status entry 6634',
    'Record sometimes status entry 6635',
    'Record lifetime status entry 6636',
    'Record overtime status entry 6637',
    'Record daytime status entry 6638',
    'Record nighttime status entry 6639',
    'Record helpful status entry 6640',
    'Record unhelpful status entry 6641',
    'Record thankful status entry 6642',
    'Record thankless status entry 6643',
    'Record maiden status entry 6644',
    'Record braided status entry 6645',
    'Record thorax status entry 6646',
    'Record choral status entry 6647',
    'Record storage status entry 6648',
    'Record shipping status entry 6649',
    'Record whisper status entry 6650',
    'Record archive status entry 6651',
]


def test_spec_batch_067() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
