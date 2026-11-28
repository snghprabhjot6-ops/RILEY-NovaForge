"""Verification spec batch 049: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('hi', 'Riley echo check #4801 [hi]', 'You said: Riley echo check #4801 [hi]'),
    ('fr', 'Riley echo check #4802 [fr]', 'You said: Riley echo check #4802 [fr]'),
    ('es', 'Riley echo check #4803 [es]', 'You said: Riley echo check #4803 [es]'),
    ('bn', 'Riley echo check #4804 [bn]', 'You said: Riley echo check #4804 [bn]'),
    ('sa', 'Riley echo check #4805 [sa]', 'You said: Riley echo check #4805 [sa]'),
    ('en', 'Riley echo check #4806 [en]', 'You said: Riley echo check #4806 [en]'),
    ('hi', 'Riley echo check #4807 [hi]', 'You said: Riley echo check #4807 [hi]'),
    ('fr', 'Riley echo check #4808 [fr]', 'You said: Riley echo check #4808 [fr]'),
    ('es', 'Riley echo check #4809 [es]', 'You said: Riley echo check #4809 [es]'),
    ('bn', 'Riley echo check #4810 [bn]', 'You said: Riley echo check #4810 [bn]'),
    ('sa', 'Riley echo check #4811 [sa]', 'You said: Riley echo check #4811 [sa]'),
    ('en', 'Riley echo check #4812 [en]', 'You said: Riley echo check #4812 [en]'),
    ('hi', 'Riley echo check #4813 [hi]', 'You said: Riley echo check #4813 [hi]'),
    ('fr', 'Riley echo check #4814 [fr]', 'You said: Riley echo check #4814 [fr]'),
    ('es', 'Riley echo check #4815 [es]', 'You said: Riley echo check #4815 [es]'),
]


def test_spec_batch_049() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
