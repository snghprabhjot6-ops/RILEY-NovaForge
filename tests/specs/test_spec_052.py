"""Verification spec batch 052: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('hi', 'Riley echo check #5101 [hi]', 'You said: Riley echo check #5101 [hi]'),
    ('fr', 'Riley echo check #5102 [fr]', 'You said: Riley echo check #5102 [fr]'),
    ('es', 'Riley echo check #5103 [es]', 'You said: Riley echo check #5103 [es]'),
    ('bn', 'Riley echo check #5104 [bn]', 'You said: Riley echo check #5104 [bn]'),
    ('sa', 'Riley echo check #5105 [sa]', 'You said: Riley echo check #5105 [sa]'),
]


def test_spec_batch_052() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
