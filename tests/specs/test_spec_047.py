"""Verification spec batch 047: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('sa', 'Riley echo check #4601 [sa]', 'You said: Riley echo check #4601 [sa]'),
    ('en', 'Riley echo check #4602 [en]', 'You said: Riley echo check #4602 [en]'),
    ('hi', 'Riley echo check #4603 [hi]', 'You said: Riley echo check #4603 [hi]'),
    ('fr', 'Riley echo check #4604 [fr]', 'You said: Riley echo check #4604 [fr]'),
    ('es', 'Riley echo check #4605 [es]', 'You said: Riley echo check #4605 [es]'),
    ('bn', 'Riley echo check #4606 [bn]', 'You said: Riley echo check #4606 [bn]'),
]


def test_spec_batch_047() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
