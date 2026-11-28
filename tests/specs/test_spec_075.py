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
    'Record sometimes status entry 7415',
    'Record lifetime status entry 7416',
    'Record overtime status entry 7417',
    'Record daytime status entry 7418',
    'Record nighttime status entry 7419',
    'Record helpful status entry 7420',
    'Record unhelpful status entry 7421',
    'Record thankful status entry 7422',
    'Record thankless status entry 7423',
    'Record maiden status entry 7424',
    'Record braided status entry 7425',
    'Record thorax status entry 7426',
    'Record choral status entry 7427',
    'Record storage status entry 7428',
    'Record shipping status entry 7429',
    'Record whisper status entry 7430',
    'Record archive status entry 7431',
    'Record thinking status entry 7432',
    'Record vehicle status entry 7433',
    'Record holiday status entry 7434',
    'Record scholar status entry 7435',
    'Record commercial status entry 7436',
    'Record integrate status entry 7437',
    'Record parameter status entry 7438',
    'Record runtime status entry 7439',
    'Record update status entry 7440',
    'Record candidate status entry 7441',
    'Record validate status entry 7442',
    'Record mandate status entry 7443',
    'Record outdated status entry 7444',
    'Record sometimes status entry 7445',
    'Record lifetime status entry 7446',
    'Record overtime status entry 7447',
    'Record daytime status entry 7448',
    'Record nighttime status entry 7449',
    'Record helpful status entry 7450',
    'Record unhelpful status entry 7451',
    'Record thankful status entry 7452',
]


def test_spec_batch_075() -> None:
    for phrase in CASES:
        assert 'learning' in _BACKEND.generate([Message('user', phrase)], 'en')
