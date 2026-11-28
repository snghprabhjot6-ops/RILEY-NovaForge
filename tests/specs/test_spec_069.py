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
    'Record candidate status entry 6811',
    'Record validate status entry 6812',
    'Record mandate status entry 6813',
    'Record outdated status entry 6814',
    'Record sometimes status entry 6815',
    'Record lifetime status entry 6816',
    'Record overtime status entry 6817',
    'Record daytime status entry 6818',
    'Record nighttime status entry 6819',
    'Record helpful status entry 6820',
    'Record unhelpful status entry 6821',
    'Record thankful status entry 6822',
    'Record thankless status entry 6823',
    'Record maiden status entry 6824',
    'Record braided status entry 6825',
    'Record thorax status entry 6826',
    'Record choral status entry 6827',
    'Record storage status entry 6828',
    'Record shipping status entry 6829',
    'Record whisper status entry 6830',
    'Record archive status entry 6831',
    'Record thinking status entry 6832',
    'Record vehicle status entry 6833',
    'Record holiday status entry 6834',
    'Record scholar status entry 6835',
    'Record commercial status entry 6836',
    'Record integrate status entry 6837',
    'Record parameter status entry 6838',
    'Record runtime status entry 6839',
    'Record update status entry 6840',
    'Record candidate status entry 6841',
    'Record validate status entry 6842',
    'Record mandate status entry 6843',
    'Record outdated status entry 6844',
    'Record sometimes status entry 6845',
    'Record lifetime status entry 6846',
    'Record overtime status entry 6847',
    'Record daytime status entry 6848',
    'Record nighttime status entry 6849',
    'Record helpful status entry 6850',
    'Record unhelpful status entry 6851',
    'Record thankful status entry 6852',
    'Record thankless status entry 6853',
    'Record maiden status entry 6854',
    'Record braided status entry 6855',
]


def test_spec_batch_069() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
