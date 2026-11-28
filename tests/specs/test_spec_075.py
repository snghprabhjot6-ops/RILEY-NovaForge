"""Verification spec batch 075: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record archive status entry 7401',
    'Record thinking status entry 7402',
    'Record vehicle status entry 7403',
    'Record holiday status entry 7404',
    'Record scholar status entry 7405',
    'Record commercial status entry 7406',
    'Record integrate status entry 7407',
    'Record parameter status entry 7408',
    'Record runtime status entry 7409',
    'Record update status entry 7410',
    'Record candidate status entry 7411',
    'Record validate status entry 7412',
    'Record mandate status entry 7413',
    'Record outdated status entry 7414',
]


def test_spec_batch_075() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
