"""Verification spec batch 076: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record candidate status entry 7501',
    'Record validate status entry 7502',
    'Record mandate status entry 7503',
    'Record outdated status entry 7504',
    'Record sometimes status entry 7505',
    'Record lifetime status entry 7506',
    'Record overtime status entry 7507',
    'Record daytime status entry 7508',
    'Record nighttime status entry 7509',
    'Record helpful status entry 7510',
    'Record unhelpful status entry 7511',
    'Record thankful status entry 7512',
    'Record thankless status entry 7513',
    'Record maiden status entry 7514',
    'Record braided status entry 7515',
]


def test_spec_batch_076() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
