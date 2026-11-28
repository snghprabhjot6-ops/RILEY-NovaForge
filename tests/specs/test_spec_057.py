"""Verification spec batch 057: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('es', 'Riley echo check #5601 [es]', 'You said: Riley echo check #5601 [es]'),
    ('bn', 'Riley echo check #5602 [bn]', 'You said: Riley echo check #5602 [bn]'),
    ('sa', 'Riley echo check #5603 [sa]', 'You said: Riley echo check #5603 [sa]'),
    ('en', 'Riley echo check #5604 [en]', 'You said: Riley echo check #5604 [en]'),
]


def test_spec_batch_057() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
