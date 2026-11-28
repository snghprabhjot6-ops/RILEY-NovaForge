"""Verification spec batch 053: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('sa', 'Riley echo check #5201 [sa]', 'You said: Riley echo check #5201 [sa]'),
    ('en', 'Riley echo check #5202 [en]', 'You said: Riley echo check #5202 [en]'),
    ('hi', 'Riley echo check #5203 [hi]', 'You said: Riley echo check #5203 [hi]'),
    ('fr', 'Riley echo check #5204 [fr]', 'You said: Riley echo check #5204 [fr]'),
    ('es', 'Riley echo check #5205 [es]', 'You said: Riley echo check #5205 [es]'),
    ('bn', 'Riley echo check #5206 [bn]', 'You said: Riley echo check #5206 [bn]'),
]


def test_spec_batch_053() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
