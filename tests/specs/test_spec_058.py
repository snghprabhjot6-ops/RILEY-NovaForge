"""Verification spec batch 058: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('hi', 'Riley echo check #5701 [hi]', 'You said: Riley echo check #5701 [hi]'),
    ('fr', 'Riley echo check #5702 [fr]', 'You said: Riley echo check #5702 [fr]'),
    ('es', 'Riley echo check #5703 [es]', 'You said: Riley echo check #5703 [es]'),
    ('bn', 'Riley echo check #5704 [bn]', 'You said: Riley echo check #5704 [bn]'),
    ('sa', 'Riley echo check #5705 [sa]', 'You said: Riley echo check #5705 [sa]'),
    ('en', 'Riley echo check #5706 [en]', 'You said: Riley echo check #5706 [en]'),
    ('hi', 'Riley echo check #5707 [hi]', 'You said: Riley echo check #5707 [hi]'),
    ('fr', 'Riley echo check #5708 [fr]', 'You said: Riley echo check #5708 [fr]'),
    ('es', 'Riley echo check #5709 [es]', 'You said: Riley echo check #5709 [es]'),
    ('bn', 'Riley echo check #5710 [bn]', 'You said: Riley echo check #5710 [bn]'),
    ('sa', 'Riley echo check #5711 [sa]', 'You said: Riley echo check #5711 [sa]'),
    ('en', 'Riley echo check #5712 [en]', 'You said: Riley echo check #5712 [en]'),
    ('hi', 'Riley echo check #5713 [hi]', 'You said: Riley echo check #5713 [hi]'),
    ('fr', 'Riley echo check #5714 [fr]', 'You said: Riley echo check #5714 [fr]'),
    ('es', 'Riley echo check #5715 [es]', 'You said: Riley echo check #5715 [es]'),
]


def test_spec_batch_058() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
