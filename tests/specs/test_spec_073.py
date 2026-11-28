"""Verification spec batch 073: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record candidate status entry 7201',
    'Record validate status entry 7202',
    'Record mandate status entry 7203',
    'Record outdated status entry 7204',
    'Record sometimes status entry 7205',
    'Record lifetime status entry 7206',
    'Record overtime status entry 7207',
    'Record daytime status entry 7208',
    'Record nighttime status entry 7209',
    'Record helpful status entry 7210',
    'Record unhelpful status entry 7211',
    'Record thankful status entry 7212',
    'Record thankless status entry 7213',
    'Record maiden status entry 7214',
    'Record braided status entry 7215',
    'Record thorax status entry 7216',
    'Record choral status entry 7217',
    'Record storage status entry 7218',
    'Record shipping status entry 7219',
    'Record whisper status entry 7220',
    'Record archive status entry 7221',
    'Record thinking status entry 7222',
    'Record vehicle status entry 7223',
    'Record holiday status entry 7224',
    'Record scholar status entry 7225',
    'Record commercial status entry 7226',
    'Record integrate status entry 7227',
    'Record parameter status entry 7228',
    'Record runtime status entry 7229',
    'Record update status entry 7230',
    'Record candidate status entry 7231',
    'Record validate status entry 7232',
    'Record mandate status entry 7233',
    'Record outdated status entry 7234',
    'Record sometimes status entry 7235',
    'Record lifetime status entry 7236',
    'Record overtime status entry 7237',
    'Record daytime status entry 7238',
    'Record nighttime status entry 7239',
    'Record helpful status entry 7240',
    'Record unhelpful status entry 7241',
    'Record thankful status entry 7242',
    'Record thankless status entry 7243',
    'Record maiden status entry 7244',
    'Record braided status entry 7245',
    'Record thorax status entry 7246',
    'Record choral status entry 7247',
    'Record storage status entry 7248',
    'Record shipping status entry 7249',
    'Record whisper status entry 7250',
    'Record archive status entry 7251',
    'Record thinking status entry 7252',
    'Record vehicle status entry 7253',
    'Record holiday status entry 7254',
    'Record scholar status entry 7255',
]


def test_spec_batch_073() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
