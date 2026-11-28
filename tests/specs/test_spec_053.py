"""Verification spec batch 053: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('sa', 'Riley echo check #5201 [sa]', 'You said: Riley echo check #5201 [sa]'),
    ('en', 'Riley echo check #5202 [en]', 'You said: Riley echo check #5202 [en]'),
    ('hi', 'Riley echo check #5203 [hi]', 'You said: Riley echo check #5203 [hi]'),
    ('fr', 'Riley echo check #5204 [fr]', 'You said: Riley echo check #5204 [fr]'),
    ('es', 'Riley echo check #5205 [es]', 'You said: Riley echo check #5205 [es]'),
    ('bn', 'Riley echo check #5206 [bn]', 'You said: Riley echo check #5206 [bn]'),
    ('sa', 'Riley echo check #5207 [sa]', 'You said: Riley echo check #5207 [sa]'),
    ('en', 'Riley echo check #5208 [en]', 'You said: Riley echo check #5208 [en]'),
    ('hi', 'Riley echo check #5209 [hi]', 'You said: Riley echo check #5209 [hi]'),
    ('fr', 'Riley echo check #5210 [fr]', 'You said: Riley echo check #5210 [fr]'),
    ('es', 'Riley echo check #5211 [es]', 'You said: Riley echo check #5211 [es]'),
    ('bn', 'Riley echo check #5212 [bn]', 'You said: Riley echo check #5212 [bn]'),
    ('sa', 'Riley echo check #5213 [sa]', 'You said: Riley echo check #5213 [sa]'),
    ('en', 'Riley echo check #5214 [en]', 'You said: Riley echo check #5214 [en]'),
    ('hi', 'Riley echo check #5215 [hi]', 'You said: Riley echo check #5215 [hi]'),
    ('fr', 'Riley echo check #5216 [fr]', 'You said: Riley echo check #5216 [fr]'),
    ('es', 'Riley echo check #5217 [es]', 'You said: Riley echo check #5217 [es]'),
    ('bn', 'Riley echo check #5218 [bn]', 'You said: Riley echo check #5218 [bn]'),
    ('sa', 'Riley echo check #5219 [sa]', 'You said: Riley echo check #5219 [sa]'),
    ('en', 'Riley echo check #5220 [en]', 'You said: Riley echo check #5220 [en]'),
    ('hi', 'Riley echo check #5221 [hi]', 'You said: Riley echo check #5221 [hi]'),
    ('fr', 'Riley echo check #5222 [fr]', 'You said: Riley echo check #5222 [fr]'),
    ('es', 'Riley echo check #5223 [es]', 'You said: Riley echo check #5223 [es]'),
]


def test_spec_batch_053() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
