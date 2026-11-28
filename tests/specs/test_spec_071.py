"""Verification spec batch 071: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record unhelpful status entry 7001',
    'Record thankful status entry 7002',
    'Record thankless status entry 7003',
    'Record maiden status entry 7004',
    'Record braided status entry 7005',
    'Record thorax status entry 7006',
    'Record choral status entry 7007',
    'Record storage status entry 7008',
    'Record shipping status entry 7009',
]


def test_spec_batch_071() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
