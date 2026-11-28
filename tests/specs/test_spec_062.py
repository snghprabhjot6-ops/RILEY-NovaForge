"""Verification spec batch 062: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('sa', 'Riley echo check #6101 [sa]', 'You said: Riley echo check #6101 [sa]'),
    ('en', 'Riley echo check #6102 [en]', 'You said: Riley echo check #6102 [en]'),
    ('hi', 'Riley echo check #6103 [hi]', 'You said: Riley echo check #6103 [hi]'),
    ('fr', 'Riley echo check #6104 [fr]', 'You said: Riley echo check #6104 [fr]'),
    ('es', 'Riley echo check #6105 [es]', 'You said: Riley echo check #6105 [es]'),
    ('bn', 'Riley echo check #6106 [bn]', 'You said: Riley echo check #6106 [bn]'),
    ('sa', 'Riley echo check #6107 [sa]', 'You said: Riley echo check #6107 [sa]'),
    ('en', 'Riley echo check #6108 [en]', 'You said: Riley echo check #6108 [en]'),
    ('hi', 'Riley echo check #6109 [hi]', 'You said: Riley echo check #6109 [hi]'),
    ('fr', 'Riley echo check #6110 [fr]', 'You said: Riley echo check #6110 [fr]'),
    ('es', 'Riley echo check #6111 [es]', 'You said: Riley echo check #6111 [es]'),
    ('bn', 'Riley echo check #6112 [bn]', 'You said: Riley echo check #6112 [bn]'),
    ('sa', 'Riley echo check #6113 [sa]', 'You said: Riley echo check #6113 [sa]'),
]


def test_spec_batch_062() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
