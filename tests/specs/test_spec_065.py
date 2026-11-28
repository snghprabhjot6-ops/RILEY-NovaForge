"""Verification spec batch 065: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('sa', 'Riley echo check #6401 [sa]', 'You said: Riley echo check #6401 [sa]'),
    ('en', 'Riley echo check #6402 [en]', 'You said: Riley echo check #6402 [en]'),
    ('hi', 'Riley echo check #6403 [hi]', 'You said: Riley echo check #6403 [hi]'),
    ('fr', 'Riley echo check #6404 [fr]', 'You said: Riley echo check #6404 [fr]'),
    ('es', 'Riley echo check #6405 [es]', 'You said: Riley echo check #6405 [es]'),
    ('bn', 'Riley echo check #6406 [bn]', 'You said: Riley echo check #6406 [bn]'),
    ('sa', 'Riley echo check #6407 [sa]', 'You said: Riley echo check #6407 [sa]'),
    ('en', 'Riley echo check #6408 [en]', 'You said: Riley echo check #6408 [en]'),
    ('hi', 'Riley echo check #6409 [hi]', 'You said: Riley echo check #6409 [hi]'),
    ('fr', 'Riley echo check #6410 [fr]', 'You said: Riley echo check #6410 [fr]'),
    ('es', 'Riley echo check #6411 [es]', 'You said: Riley echo check #6411 [es]'),
    ('bn', 'Riley echo check #6412 [bn]', 'You said: Riley echo check #6412 [bn]'),
    ('sa', 'Riley echo check #6413 [sa]', 'You said: Riley echo check #6413 [sa]'),
    ('en', 'Riley echo check #6414 [en]', 'You said: Riley echo check #6414 [en]'),
    ('hi', 'Riley echo check #6415 [hi]', 'You said: Riley echo check #6415 [hi]'),
    ('fr', 'Riley echo check #6416 [fr]', 'You said: Riley echo check #6416 [fr]'),
    ('es', 'Riley echo check #6417 [es]', 'You said: Riley echo check #6417 [es]'),
    ('bn', 'Riley echo check #6418 [bn]', 'You said: Riley echo check #6418 [bn]'),
    ('sa', 'Riley echo check #6419 [sa]', 'You said: Riley echo check #6419 [sa]'),
    ('en', 'Riley echo check #6420 [en]', 'You said: Riley echo check #6420 [en]'),
    ('hi', 'Riley echo check #6421 [hi]', 'You said: Riley echo check #6421 [hi]'),
    ('fr', 'Riley echo check #6422 [fr]', 'You said: Riley echo check #6422 [fr]'),
    ('es', 'Riley echo check #6423 [es]', 'You said: Riley echo check #6423 [es]'),
    ('bn', 'Riley echo check #6424 [bn]', 'You said: Riley echo check #6424 [bn]'),
]


def test_spec_batch_065() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
