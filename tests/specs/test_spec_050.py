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
    ('en', 'Riley echo check #4926 [en]', 'You said: Riley echo check #4926 [en]'),
    ('hi', 'Riley echo check #4927 [hi]', 'You said: Riley echo check #4927 [hi]'),
    ('fr', 'Riley echo check #4928 [fr]', 'You said: Riley echo check #4928 [fr]'),
    ('es', 'Riley echo check #4929 [es]', 'You said: Riley echo check #4929 [es]'),
    ('bn', 'Riley echo check #4930 [bn]', 'You said: Riley echo check #4930 [bn]'),
    ('sa', 'Riley echo check #4931 [sa]', 'You said: Riley echo check #4931 [sa]'),
    ('en', 'Riley echo check #4932 [en]', 'You said: Riley echo check #4932 [en]'),
    ('hi', 'Riley echo check #4933 [hi]', 'You said: Riley echo check #4933 [hi]'),
    ('fr', 'Riley echo check #4934 [fr]', 'You said: Riley echo check #4934 [fr]'),
    ('es', 'Riley echo check #4935 [es]', 'You said: Riley echo check #4935 [es]'),
    ('bn', 'Riley echo check #4936 [bn]', 'You said: Riley echo check #4936 [bn]'),
    ('sa', 'Riley echo check #4937 [sa]', 'You said: Riley echo check #4937 [sa]'),
    ('en', 'Riley echo check #4938 [en]', 'You said: Riley echo check #4938 [en]'),
    ('hi', 'Riley echo check #4939 [hi]', 'You said: Riley echo check #4939 [hi]'),
    ('fr', 'Riley echo check #4940 [fr]', 'You said: Riley echo check #4940 [fr]'),
    ('es', 'Riley echo check #4941 [es]', 'You said: Riley echo check #4941 [es]'),
    ('bn', 'Riley echo check #4942 [bn]', 'You said: Riley echo check #4942 [bn]'),
    ('sa', 'Riley echo check #4943 [sa]', 'You said: Riley echo check #4943 [sa]'),
    ('en', 'Riley echo check #4944 [en]', 'You said: Riley echo check #4944 [en]'),
    ('hi', 'Riley echo check #4945 [hi]', 'You said: Riley echo check #4945 [hi]'),
    ('fr', 'Riley echo check #4946 [fr]', 'You said: Riley echo check #4946 [fr]'),
    ('es', 'Riley echo check #4947 [es]', 'You said: Riley echo check #4947 [es]'),
    ('bn', 'Riley echo check #4948 [bn]', 'You said: Riley echo check #4948 [bn]'),
]


def test_spec_batch_050() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
