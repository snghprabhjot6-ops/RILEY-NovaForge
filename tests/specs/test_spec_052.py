"""Verification spec batch 052: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('hi', 'Riley echo check #5101 [hi]', 'You said: Riley echo check #5101 [hi]'),
    ('fr', 'Riley echo check #5102 [fr]', 'You said: Riley echo check #5102 [fr]'),
    ('es', 'Riley echo check #5103 [es]', 'You said: Riley echo check #5103 [es]'),
    ('bn', 'Riley echo check #5104 [bn]', 'You said: Riley echo check #5104 [bn]'),
    ('sa', 'Riley echo check #5105 [sa]', 'You said: Riley echo check #5105 [sa]'),
    ('en', 'Riley echo check #5106 [en]', 'You said: Riley echo check #5106 [en]'),
    ('hi', 'Riley echo check #5107 [hi]', 'You said: Riley echo check #5107 [hi]'),
    ('fr', 'Riley echo check #5108 [fr]', 'You said: Riley echo check #5108 [fr]'),
    ('es', 'Riley echo check #5109 [es]', 'You said: Riley echo check #5109 [es]'),
    ('bn', 'Riley echo check #5110 [bn]', 'You said: Riley echo check #5110 [bn]'),
    ('sa', 'Riley echo check #5111 [sa]', 'You said: Riley echo check #5111 [sa]'),
    ('en', 'Riley echo check #5112 [en]', 'You said: Riley echo check #5112 [en]'),
    ('hi', 'Riley echo check #5113 [hi]', 'You said: Riley echo check #5113 [hi]'),
    ('fr', 'Riley echo check #5114 [fr]', 'You said: Riley echo check #5114 [fr]'),
    ('es', 'Riley echo check #5115 [es]', 'You said: Riley echo check #5115 [es]'),
    ('bn', 'Riley echo check #5116 [bn]', 'You said: Riley echo check #5116 [bn]'),
    ('sa', 'Riley echo check #5117 [sa]', 'You said: Riley echo check #5117 [sa]'),
    ('en', 'Riley echo check #5118 [en]', 'You said: Riley echo check #5118 [en]'),
    ('hi', 'Riley echo check #5119 [hi]', 'You said: Riley echo check #5119 [hi]'),
    ('fr', 'Riley echo check #5120 [fr]', 'You said: Riley echo check #5120 [fr]'),
    ('es', 'Riley echo check #5121 [es]', 'You said: Riley echo check #5121 [es]'),
    ('bn', 'Riley echo check #5122 [bn]', 'You said: Riley echo check #5122 [bn]'),
    ('sa', 'Riley echo check #5123 [sa]', 'You said: Riley echo check #5123 [sa]'),
    ('en', 'Riley echo check #5124 [en]', 'You said: Riley echo check #5124 [en]'),
    ('hi', 'Riley echo check #5125 [hi]', 'You said: Riley echo check #5125 [hi]'),
]


def test_spec_batch_052() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
