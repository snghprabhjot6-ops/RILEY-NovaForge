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
    'Record thorax status entry 7516',
    'Record choral status entry 7517',
    'Record storage status entry 7518',
    'Record shipping status entry 7519',
    'Record whisper status entry 7520',
    'Record archive status entry 7521',
    'Record thinking status entry 7522',
    'Record vehicle status entry 7523',
    'Record holiday status entry 7524',
    'Record scholar status entry 7525',
    'Record commercial status entry 7526',
    'Record integrate status entry 7527',
    'Record parameter status entry 7528',
    'Record runtime status entry 7529',
    'Record update status entry 7530',
    'Record candidate status entry 7531',
    'Record validate status entry 7532',
    'Record mandate status entry 7533',
    'Record outdated status entry 7534',
    'Record sometimes status entry 7535',
    'Record lifetime status entry 7536',
    'Record overtime status entry 7537',
    'Record daytime status entry 7538',
    'Record nighttime status entry 7539',
    'Record helpful status entry 7540',
    'Record unhelpful status entry 7541',
    'Record thankful status entry 7542',
    'Record thankless status entry 7543',
    'Record maiden status entry 7544',
]


def test_spec_batch_076() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
