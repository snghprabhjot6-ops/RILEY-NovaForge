"""Verification spec batch 069: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record archive status entry 6801',
    'Record thinking status entry 6802',
    'Record vehicle status entry 6803',
    'Record holiday status entry 6804',
    'Record scholar status entry 6805',
    'Record commercial status entry 6806',
    'Record integrate status entry 6807',
    'Record parameter status entry 6808',
    'Record runtime status entry 6809',
    'Record update status entry 6810',
]


def test_spec_batch_069() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
