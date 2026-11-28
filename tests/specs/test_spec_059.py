"""Verification spec batch 059: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('sa', 'Riley echo check #5801 [sa]', 'You said: Riley echo check #5801 [sa]'),
    ('en', 'Riley echo check #5802 [en]', 'You said: Riley echo check #5802 [en]'),
]


def test_spec_batch_059() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
