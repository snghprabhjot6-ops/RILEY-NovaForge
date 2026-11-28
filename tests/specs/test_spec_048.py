"""Verification spec batch 048: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('es', 'Riley echo check #4701 [es]', 'You said: Riley echo check #4701 [es]'),
    ('bn', 'Riley echo check #4702 [bn]', 'You said: Riley echo check #4702 [bn]'),
    ('sa', 'Riley echo check #4703 [sa]', 'You said: Riley echo check #4703 [sa]'),
    ('en', 'Riley echo check #4704 [en]', 'You said: Riley echo check #4704 [en]'),
]


def test_spec_batch_048() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
