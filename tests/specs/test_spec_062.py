"""Verification spec batch 062: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('sa', 'Riley echo check #6101 [sa]', 'You said: Riley echo check #6101 [sa]'),
    ('en', 'Riley echo check #6102 [en]', 'You said: Riley echo check #6102 [en]'),
    ('hi', 'Riley echo check #6103 [hi]', 'You said: Riley echo check #6103 [hi]'),
    ('fr', 'Riley echo check #6104 [fr]', 'You said: Riley echo check #6104 [fr]'),
    ('es', 'Riley echo check #6105 [es]', 'You said: Riley echo check #6105 [es]'),
]


def test_spec_batch_062() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
