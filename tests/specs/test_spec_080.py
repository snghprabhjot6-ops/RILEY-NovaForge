"""Verification spec batch 080: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record unhelpful status entry 7901',
    'Record thankful status entry 7902',
    'Record thankless status entry 7903',
    'Record maiden status entry 7904',
    'Record braided status entry 7905',
    'Record thorax status entry 7906',
    'Record choral status entry 7907',
    'Record storage status entry 7908',
    'Record shipping status entry 7909',
    'Record whisper status entry 7910',
    'Record archive status entry 7911',
    'Record thinking status entry 7912',
    'Record vehicle status entry 7913',
    'Record holiday status entry 7914',
    'Record scholar status entry 7915',
    'Record commercial status entry 7916',
    'Record integrate status entry 7917',
    'Record parameter status entry 7918',
    'Record runtime status entry 7919',
    'Record update status entry 7920',
    'Record candidate status entry 7921',
    'Record validate status entry 7922',
    'Record mandate status entry 7923',
    'Record outdated status entry 7924',
    'Record sometimes status entry 7925',
    'Record lifetime status entry 7926',
    'Record overtime status entry 7927',
    'Record daytime status entry 7928',
    'Record nighttime status entry 7929',
    'Record helpful status entry 7930',
    'Record unhelpful status entry 7931',
]


def test_spec_batch_080() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
