"""Verification spec batch 064: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('hi', 'Riley echo check #6301 [hi]', 'You said: Riley echo check #6301 [hi]'),
    ('fr', 'Riley echo check #6302 [fr]', 'You said: Riley echo check #6302 [fr]'),
    ('es', 'Riley echo check #6303 [es]', 'You said: Riley echo check #6303 [es]'),
    ('bn', 'Riley echo check #6304 [bn]', 'You said: Riley echo check #6304 [bn]'),
    ('sa', 'Riley echo check #6305 [sa]', 'You said: Riley echo check #6305 [sa]'),
]


def test_spec_batch_064() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
