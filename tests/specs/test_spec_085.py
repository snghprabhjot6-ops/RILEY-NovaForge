"""Verification spec batch 085: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record candidate status entry 8401',
    'Record validate status entry 8402',
    'Record mandate status entry 8403',
    'Record outdated status entry 8404',
    'Record sometimes status entry 8405',
    'Record lifetime status entry 8406',
    'Record overtime status entry 8407',
    'Record daytime status entry 8408',
    'Record nighttime status entry 8409',
    'Record helpful status entry 8410',
    'Record unhelpful status entry 8411',
    'Record thankful status entry 8412',
    'Record thankless status entry 8413',
    'Record maiden status entry 8414',
]


def test_spec_batch_085() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
