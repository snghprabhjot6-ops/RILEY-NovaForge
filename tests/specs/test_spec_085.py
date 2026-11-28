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
    'Record braided status entry 8415',
    'Record thorax status entry 8416',
    'Record choral status entry 8417',
    'Record storage status entry 8418',
    'Record shipping status entry 8419',
    'Record whisper status entry 8420',
    'Record archive status entry 8421',
    'Record thinking status entry 8422',
    'Record vehicle status entry 8423',
    'Record holiday status entry 8424',
    'Record scholar status entry 8425',
    'Record commercial status entry 8426',
    'Record integrate status entry 8427',
    'Record parameter status entry 8428',
    'Record runtime status entry 8429',
    'Record update status entry 8430',
    'Record candidate status entry 8431',
    'Record validate status entry 8432',
    'Record mandate status entry 8433',
    'Record outdated status entry 8434',
    'Record sometimes status entry 8435',
    'Record lifetime status entry 8436',
    'Record overtime status entry 8437',
    'Record daytime status entry 8438',
    'Record nighttime status entry 8439',
    'Record helpful status entry 8440',
    'Record unhelpful status entry 8441',
    'Record thankful status entry 8442',
    'Record thankless status entry 8443',
    'Record maiden status entry 8444',
    'Record braided status entry 8445',
    'Record thorax status entry 8446',
    'Record choral status entry 8447',
    'Record storage status entry 8448',
    'Record shipping status entry 8449',
    'Record whisper status entry 8450',
    'Record archive status entry 8451',
    'Record thinking status entry 8452',
    'Record vehicle status entry 8453',
    'Record holiday status entry 8454',
    'Record scholar status entry 8455',
    'Record commercial status entry 8456',
]


def test_spec_batch_085() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
