"""Verification spec batch 065: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('sa', 'Riley echo check #6401 [sa]', 'You said: Riley echo check #6401 [sa]'),
    ('en', 'Riley echo check #6402 [en]', 'You said: Riley echo check #6402 [en]'),
    ('hi', 'Riley echo check #6403 [hi]', 'You said: Riley echo check #6403 [hi]'),
    ('fr', 'Riley echo check #6404 [fr]', 'You said: Riley echo check #6404 [fr]'),
]


def test_spec_batch_065() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
