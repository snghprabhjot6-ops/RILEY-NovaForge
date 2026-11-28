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
    ('bn', 'Riley echo check #4906 [bn]', 'You said: Riley echo check #4906 [bn]'),
    ('sa', 'Riley echo check #4907 [sa]', 'You said: Riley echo check #4907 [sa]'),
    ('en', 'Riley echo check #4908 [en]', 'You said: Riley echo check #4908 [en]'),
    ('hi', 'Riley echo check #4909 [hi]', 'You said: Riley echo check #4909 [hi]'),
    ('fr', 'Riley echo check #4910 [fr]', 'You said: Riley echo check #4910 [fr]'),
    ('es', 'Riley echo check #4911 [es]', 'You said: Riley echo check #4911 [es]'),
    ('bn', 'Riley echo check #4912 [bn]', 'You said: Riley echo check #4912 [bn]'),
    ('sa', 'Riley echo check #4913 [sa]', 'You said: Riley echo check #4913 [sa]'),
    ('en', 'Riley echo check #4914 [en]', 'You said: Riley echo check #4914 [en]'),
    ('hi', 'Riley echo check #4915 [hi]', 'You said: Riley echo check #4915 [hi]'),
    ('fr', 'Riley echo check #4916 [fr]', 'You said: Riley echo check #4916 [fr]'),
    ('es', 'Riley echo check #4917 [es]', 'You said: Riley echo check #4917 [es]'),
    ('bn', 'Riley echo check #4918 [bn]', 'You said: Riley echo check #4918 [bn]'),
    ('sa', 'Riley echo check #4919 [sa]', 'You said: Riley echo check #4919 [sa]'),
    ('en', 'Riley echo check #4920 [en]', 'You said: Riley echo check #4920 [en]'),
    ('hi', 'Riley echo check #4921 [hi]', 'You said: Riley echo check #4921 [hi]'),
    ('fr', 'Riley echo check #4922 [fr]', 'You said: Riley echo check #4922 [fr]'),
    ('es', 'Riley echo check #4923 [es]', 'You said: Riley echo check #4923 [es]'),
    ('bn', 'Riley echo check #4924 [bn]', 'You said: Riley echo check #4924 [bn]'),
    ('sa', 'Riley echo check #4925 [sa]', 'You said: Riley echo check #4925 [sa]'),
]


def test_spec_batch_050() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
