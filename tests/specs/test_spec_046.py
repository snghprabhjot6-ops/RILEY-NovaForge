"""Verification spec batch 046: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('hi', 'Riley echo check #4501 [hi]', 'You said: Riley echo check #4501 [hi]'),
    ('fr', 'Riley echo check #4502 [fr]', 'You said: Riley echo check #4502 [fr]'),
    ('es', 'Riley echo check #4503 [es]', 'You said: Riley echo check #4503 [es]'),
    ('bn', 'Riley echo check #4504 [bn]', 'You said: Riley echo check #4504 [bn]'),
    ('sa', 'Riley echo check #4505 [sa]', 'You said: Riley echo check #4505 [sa]'),
    ('en', 'Riley echo check #4506 [en]', 'You said: Riley echo check #4506 [en]'),
    ('hi', 'Riley echo check #4507 [hi]', 'You said: Riley echo check #4507 [hi]'),
]


def test_spec_batch_046() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
