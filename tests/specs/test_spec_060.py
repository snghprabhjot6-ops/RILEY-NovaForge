"""Verification spec batch 060: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('es', 'Riley echo check #5901 [es]', 'You said: Riley echo check #5901 [es]'),
    ('bn', 'Riley echo check #5902 [bn]', 'You said: Riley echo check #5902 [bn]'),
    ('sa', 'Riley echo check #5903 [sa]', 'You said: Riley echo check #5903 [sa]'),
    ('en', 'Riley echo check #5904 [en]', 'You said: Riley echo check #5904 [en]'),
    ('hi', 'Riley echo check #5905 [hi]', 'You said: Riley echo check #5905 [hi]'),
    ('fr', 'Riley echo check #5906 [fr]', 'You said: Riley echo check #5906 [fr]'),
    ('es', 'Riley echo check #5907 [es]', 'You said: Riley echo check #5907 [es]'),
    ('bn', 'Riley echo check #5908 [bn]', 'You said: Riley echo check #5908 [bn]'),
    ('sa', 'Riley echo check #5909 [sa]', 'You said: Riley echo check #5909 [sa]'),
    ('en', 'Riley echo check #5910 [en]', 'You said: Riley echo check #5910 [en]'),
    ('hi', 'Riley echo check #5911 [hi]', 'You said: Riley echo check #5911 [hi]'),
    ('fr', 'Riley echo check #5912 [fr]', 'You said: Riley echo check #5912 [fr]'),
    ('es', 'Riley echo check #5913 [es]', 'You said: Riley echo check #5913 [es]'),
    ('bn', 'Riley echo check #5914 [bn]', 'You said: Riley echo check #5914 [bn]'),
    ('sa', 'Riley echo check #5915 [sa]', 'You said: Riley echo check #5915 [sa]'),
    ('en', 'Riley echo check #5916 [en]', 'You said: Riley echo check #5916 [en]'),
    ('hi', 'Riley echo check #5917 [hi]', 'You said: Riley echo check #5917 [hi]'),
    ('fr', 'Riley echo check #5918 [fr]', 'You said: Riley echo check #5918 [fr]'),
    ('es', 'Riley echo check #5919 [es]', 'You said: Riley echo check #5919 [es]'),
    ('bn', 'Riley echo check #5920 [bn]', 'You said: Riley echo check #5920 [bn]'),
    ('sa', 'Riley echo check #5921 [sa]', 'You said: Riley echo check #5921 [sa]'),
    ('en', 'Riley echo check #5922 [en]', 'You said: Riley echo check #5922 [en]'),
    ('hi', 'Riley echo check #5923 [hi]', 'You said: Riley echo check #5923 [hi]'),
    ('fr', 'Riley echo check #5924 [fr]', 'You said: Riley echo check #5924 [fr]'),
    ('es', 'Riley echo check #5925 [es]', 'You said: Riley echo check #5925 [es]'),
    ('bn', 'Riley echo check #5926 [bn]', 'You said: Riley echo check #5926 [bn]'),
    ('sa', 'Riley echo check #5927 [sa]', 'You said: Riley echo check #5927 [sa]'),
    ('en', 'Riley echo check #5928 [en]', 'You said: Riley echo check #5928 [en]'),
    ('hi', 'Riley echo check #5929 [hi]', 'You said: Riley echo check #5929 [hi]'),
    ('fr', 'Riley echo check #5930 [fr]', 'You said: Riley echo check #5930 [fr]'),
    ('es', 'Riley echo check #5931 [es]', 'You said: Riley echo check #5931 [es]'),
    ('bn', 'Riley echo check #5932 [bn]', 'You said: Riley echo check #5932 [bn]'),
    ('sa', 'Riley echo check #5933 [sa]', 'You said: Riley echo check #5933 [sa]'),
    ('en', 'Riley echo check #5934 [en]', 'You said: Riley echo check #5934 [en]'),
    ('hi', 'Riley echo check #5935 [hi]', 'You said: Riley echo check #5935 [hi]'),
    ('fr', 'Riley echo check #5936 [fr]', 'You said: Riley echo check #5936 [fr]'),
    ('es', 'Riley echo check #5937 [es]', 'You said: Riley echo check #5937 [es]'),
    ('bn', 'Riley echo check #5938 [bn]', 'You said: Riley echo check #5938 [bn]'),
    ('sa', 'Riley echo check #5939 [sa]', 'You said: Riley echo check #5939 [sa]'),
    ('en', 'Riley echo check #5940 [en]', 'You said: Riley echo check #5940 [en]'),
    ('hi', 'Riley echo check #5941 [hi]', 'You said: Riley echo check #5941 [hi]'),
    ('fr', 'Riley echo check #5942 [fr]', 'You said: Riley echo check #5942 [fr]'),
    ('es', 'Riley echo check #5943 [es]', 'You said: Riley echo check #5943 [es]'),
    ('bn', 'Riley echo check #5944 [bn]', 'You said: Riley echo check #5944 [bn]'),
    ('sa', 'Riley echo check #5945 [sa]', 'You said: Riley echo check #5945 [sa]'),
    ('en', 'Riley echo check #5946 [en]', 'You said: Riley echo check #5946 [en]'),
    ('hi', 'Riley echo check #5947 [hi]', 'You said: Riley echo check #5947 [hi]'),
    ('fr', 'Riley echo check #5948 [fr]', 'You said: Riley echo check #5948 [fr]'),
]


def test_spec_batch_060() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
