"""Verification spec batch 055: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('hi', 'Riley echo check #5401 [hi]', 'You said: Riley echo check #5401 [hi]'),
    ('fr', 'Riley echo check #5402 [fr]', 'You said: Riley echo check #5402 [fr]'),
    ('es', 'Riley echo check #5403 [es]', 'You said: Riley echo check #5403 [es]'),
    ('bn', 'Riley echo check #5404 [bn]', 'You said: Riley echo check #5404 [bn]'),
    ('sa', 'Riley echo check #5405 [sa]', 'You said: Riley echo check #5405 [sa]'),
    ('en', 'Riley echo check #5406 [en]', 'You said: Riley echo check #5406 [en]'),
    ('hi', 'Riley echo check #5407 [hi]', 'You said: Riley echo check #5407 [hi]'),
    ('fr', 'Riley echo check #5408 [fr]', 'You said: Riley echo check #5408 [fr]'),
    ('es', 'Riley echo check #5409 [es]', 'You said: Riley echo check #5409 [es]'),
    ('bn', 'Riley echo check #5410 [bn]', 'You said: Riley echo check #5410 [bn]'),
    ('sa', 'Riley echo check #5411 [sa]', 'You said: Riley echo check #5411 [sa]'),
    ('en', 'Riley echo check #5412 [en]', 'You said: Riley echo check #5412 [en]'),
    ('hi', 'Riley echo check #5413 [hi]', 'You said: Riley echo check #5413 [hi]'),
    ('fr', 'Riley echo check #5414 [fr]', 'You said: Riley echo check #5414 [fr]'),
]


def test_spec_batch_055() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
