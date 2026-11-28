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
    'Record thankful status entry 6912',
    'Record thankless status entry 6913',
    'Record maiden status entry 6914',
    'Record braided status entry 6915',
    'Record thorax status entry 6916',
    'Record choral status entry 6917',
    'Record storage status entry 6918',
    'Record shipping status entry 6919',
    'Record whisper status entry 6920',
    'Record archive status entry 6921',
    'Record thinking status entry 6922',
    'Record vehicle status entry 6923',
    'Record holiday status entry 6924',
    'Record scholar status entry 6925',
    'Record commercial status entry 6926',
    'Record integrate status entry 6927',
    'Record parameter status entry 6928',
    'Record runtime status entry 6929',
    'Record update status entry 6930',
    'Record candidate status entry 6931',
]


def test_spec_batch_070() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
