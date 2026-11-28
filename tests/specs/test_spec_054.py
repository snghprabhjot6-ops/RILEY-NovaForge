"""Verification spec batch 054: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('es', 'Riley echo check #5301 [es]', 'You said: Riley echo check #5301 [es]'),
    ('bn', 'Riley echo check #5302 [bn]', 'You said: Riley echo check #5302 [bn]'),
    ('sa', 'Riley echo check #5303 [sa]', 'You said: Riley echo check #5303 [sa]'),
    ('en', 'Riley echo check #5304 [en]', 'You said: Riley echo check #5304 [en]'),
    ('hi', 'Riley echo check #5305 [hi]', 'You said: Riley echo check #5305 [hi]'),
]


def test_spec_batch_054() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
