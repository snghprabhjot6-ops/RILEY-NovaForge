"""Verification spec batch 060: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('es', 'Riley echo check #5901 [es]', 'You said: Riley echo check #5901 [es]'),
    ('bn', 'Riley echo check #5902 [bn]', 'You said: Riley echo check #5902 [bn]'),
    ('sa', 'Riley echo check #5903 [sa]', 'You said: Riley echo check #5903 [sa]'),
    ('en', 'Riley echo check #5904 [en]', 'You said: Riley echo check #5904 [en]'),
    ('hi', 'Riley echo check #5905 [hi]', 'You said: Riley echo check #5905 [hi]'),
    ('fr', 'Riley echo check #5906 [fr]', 'You said: Riley echo check #5906 [fr]'),
    ('es', 'Riley echo check #5907 [es]', 'You said: Riley echo check #5907 [es]'),
    ('bn', 'Riley echo check #5908 [bn]', 'You said: Riley echo check #5908 [bn]'),
    ('sa', 'Riley echo check #5909 [sa]', 'You said: Riley echo check #5909 [sa]'),
    ('en', 'Riley echo check #5910 [en]', 'You said: Riley echo check #5910 [en]'),
]


def test_spec_batch_060() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
