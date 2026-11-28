"""Verification spec batch 051: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('es', 'Riley echo check #5001 [es]', 'You said: Riley echo check #5001 [es]'),
    ('bn', 'Riley echo check #5002 [bn]', 'You said: Riley echo check #5002 [bn]'),
    ('sa', 'Riley echo check #5003 [sa]', 'You said: Riley echo check #5003 [sa]'),
    ('en', 'Riley echo check #5004 [en]', 'You said: Riley echo check #5004 [en]'),
    ('hi', 'Riley echo check #5005 [hi]', 'You said: Riley echo check #5005 [hi]'),
    ('fr', 'Riley echo check #5006 [fr]', 'You said: Riley echo check #5006 [fr]'),
    ('es', 'Riley echo check #5007 [es]', 'You said: Riley echo check #5007 [es]'),
    ('bn', 'Riley echo check #5008 [bn]', 'You said: Riley echo check #5008 [bn]'),
]


def test_spec_batch_051() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
