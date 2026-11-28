"""Verification spec batch 056: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('sa', 'Riley echo check #5501 [sa]', 'You said: Riley echo check #5501 [sa]'),
    ('en', 'Riley echo check #5502 [en]', 'You said: Riley echo check #5502 [en]'),
    ('hi', 'Riley echo check #5503 [hi]', 'You said: Riley echo check #5503 [hi]'),
    ('fr', 'Riley echo check #5504 [fr]', 'You said: Riley echo check #5504 [fr]'),
]


def test_spec_batch_056() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
