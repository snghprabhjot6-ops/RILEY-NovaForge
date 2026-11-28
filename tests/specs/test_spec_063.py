"""Verification spec batch 063: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('es', 'Riley echo check #6201 [es]', 'You said: Riley echo check #6201 [es]'),
    ('bn', 'Riley echo check #6202 [bn]', 'You said: Riley echo check #6202 [bn]'),
    ('sa', 'Riley echo check #6203 [sa]', 'You said: Riley echo check #6203 [sa]'),
]


def test_spec_batch_063() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
