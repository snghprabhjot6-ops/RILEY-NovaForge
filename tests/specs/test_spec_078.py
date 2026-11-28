"""Verification spec batch 078: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record archive status entry 7701',
    'Record thinking status entry 7702',
    'Record vehicle status entry 7703',
    'Record holiday status entry 7704',
    'Record scholar status entry 7705',
    'Record commercial status entry 7706',
    'Record integrate status entry 7707',
    'Record parameter status entry 7708',
    'Record runtime status entry 7709',
    'Record update status entry 7710',
    'Record candidate status entry 7711',
    'Record validate status entry 7712',
    'Record mandate status entry 7713',
    'Record outdated status entry 7714',
    'Record sometimes status entry 7715',
    'Record lifetime status entry 7716',
    'Record overtime status entry 7717',
    'Record daytime status entry 7718',
    'Record nighttime status entry 7719',
    'Record helpful status entry 7720',
    'Record unhelpful status entry 7721',
    'Record thankful status entry 7722',
    'Record thankless status entry 7723',
    'Record maiden status entry 7724',
    'Record braided status entry 7725',
    'Record thorax status entry 7726',
    'Record choral status entry 7727',
]


def test_spec_batch_078() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
