"""Verification spec batch 061: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('hi', 'Riley echo check #6001 [hi]', 'You said: Riley echo check #6001 [hi]'),
    ('fr', 'Riley echo check #6002 [fr]', 'You said: Riley echo check #6002 [fr]'),
    ('es', 'Riley echo check #6003 [es]', 'You said: Riley echo check #6003 [es]'),
    ('bn', 'Riley echo check #6004 [bn]', 'You said: Riley echo check #6004 [bn]'),
    ('sa', 'Riley echo check #6005 [sa]', 'You said: Riley echo check #6005 [sa]'),
    ('en', 'Riley echo check #6006 [en]', 'You said: Riley echo check #6006 [en]'),
    ('hi', 'Riley echo check #6007 [hi]', 'You said: Riley echo check #6007 [hi]'),
    ('fr', 'Riley echo check #6008 [fr]', 'You said: Riley echo check #6008 [fr]'),
    ('es', 'Riley echo check #6009 [es]', 'You said: Riley echo check #6009 [es]'),
    ('bn', 'Riley echo check #6010 [bn]', 'You said: Riley echo check #6010 [bn]'),
    ('sa', 'Riley echo check #6011 [sa]', 'You said: Riley echo check #6011 [sa]'),
    ('en', 'Riley echo check #6012 [en]', 'You said: Riley echo check #6012 [en]'),
]


def test_spec_batch_061() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
