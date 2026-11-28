"""Verification spec batch 079: intent word-boundary isolation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[str] = [
    'Record candidate status entry 7801',
    'Record validate status entry 7802',
    'Record mandate status entry 7803',
    'Record outdated status entry 7804',
    'Record sometimes status entry 7805',
    'Record lifetime status entry 7806',
    'Record overtime status entry 7807',
    'Record daytime status entry 7808',
    'Record nighttime status entry 7809',
    'Record helpful status entry 7810',
    'Record unhelpful status entry 7811',
    'Record thankful status entry 7812',
    'Record thankless status entry 7813',
    'Record maiden status entry 7814',
    'Record braided status entry 7815',
    'Record thorax status entry 7816',
    'Record choral status entry 7817',
    'Record storage status entry 7818',
    'Record shipping status entry 7819',
    'Record whisper status entry 7820',
    'Record archive status entry 7821',
    'Record thinking status entry 7822',
    'Record vehicle status entry 7823',
    'Record holiday status entry 7824',
    'Record scholar status entry 7825',
    'Record commercial status entry 7826',
    'Record integrate status entry 7827',
    'Record parameter status entry 7828',
    'Record runtime status entry 7829',
    'Record update status entry 7830',
    'Record candidate status entry 7831',
    'Record validate status entry 7832',
    'Record mandate status entry 7833',
    'Record outdated status entry 7834',
    'Record sometimes status entry 7835',
    'Record lifetime status entry 7836',
    'Record overtime status entry 7837',
    'Record daytime status entry 7838',
    'Record nighttime status entry 7839',
    'Record helpful status entry 7840',
    'Record unhelpful status entry 7841',
    'Record thankful status entry 7842',
    'Record thankless status entry 7843',
    'Record maiden status entry 7844',
    'Record braided status entry 7845',
    'Record thorax status entry 7846',
    'Record choral status entry 7847',
    'Record storage status entry 7848',
    'Record shipping status entry 7849',
    'Record whisper status entry 7850',
    'Record archive status entry 7851',
    'Record thinking status entry 7852',
]


def test_spec_batch_079() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
