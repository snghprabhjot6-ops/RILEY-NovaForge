"""Verification spec batch 050: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('sa', 'Riley echo check #4901 [sa]', 'You said: Riley echo check #4901 [sa]'),
    ('en', 'Riley echo check #4902 [en]', 'You said: Riley echo check #4902 [en]'),
    ('hi', 'Riley echo check #4903 [hi]', 'You said: Riley echo check #4903 [hi]'),
    ('fr', 'Riley echo check #4904 [fr]', 'You said: Riley echo check #4904 [fr]'),
    ('es', 'Riley echo check #4905 [es]', 'You said: Riley echo check #4905 [es]'),
]


def test_spec_batch_050() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
