"""Verification spec batch 051: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('es', 'Riley echo check #5001 [es]', 'You said: Riley echo check #5001 [es]'),
    ('bn', 'Riley echo check #5002 [bn]', 'You said: Riley echo check #5002 [bn]'),
    ('sa', 'Riley echo check #5003 [sa]', 'You said: Riley echo check #5003 [sa]'),
    ('en', 'Riley echo check #5004 [en]', 'You said: Riley echo check #5004 [en]'),
    ('hi', 'Riley echo check #5005 [hi]', 'You said: Riley echo check #5005 [hi]'),
    ('fr', 'Riley echo check #5006 [fr]', 'You said: Riley echo check #5006 [fr]'),
    ('es', 'Riley echo check #5007 [es]', 'You said: Riley echo check #5007 [es]'),
    ('bn', 'Riley echo check #5008 [bn]', 'You said: Riley echo check #5008 [bn]'),
    ('sa', 'Riley echo check #5009 [sa]', 'You said: Riley echo check #5009 [sa]'),
    ('en', 'Riley echo check #5010 [en]', 'You said: Riley echo check #5010 [en]'),
    ('hi', 'Riley echo check #5011 [hi]', 'You said: Riley echo check #5011 [hi]'),
    ('fr', 'Riley echo check #5012 [fr]', 'You said: Riley echo check #5012 [fr]'),
    ('es', 'Riley echo check #5013 [es]', 'You said: Riley echo check #5013 [es]'),
    ('bn', 'Riley echo check #5014 [bn]', 'You said: Riley echo check #5014 [bn]'),
    ('sa', 'Riley echo check #5015 [sa]', 'You said: Riley echo check #5015 [sa]'),
    ('en', 'Riley echo check #5016 [en]', 'You said: Riley echo check #5016 [en]'),
    ('hi', 'Riley echo check #5017 [hi]', 'You said: Riley echo check #5017 [hi]'),
    ('fr', 'Riley echo check #5018 [fr]', 'You said: Riley echo check #5018 [fr]'),
    ('es', 'Riley echo check #5019 [es]', 'You said: Riley echo check #5019 [es]'),
    ('bn', 'Riley echo check #5020 [bn]', 'You said: Riley echo check #5020 [bn]'),
    ('sa', 'Riley echo check #5021 [sa]', 'You said: Riley echo check #5021 [sa]'),
    ('en', 'Riley echo check #5022 [en]', 'You said: Riley echo check #5022 [en]'),
    ('hi', 'Riley echo check #5023 [hi]', 'You said: Riley echo check #5023 [hi]'),
    ('fr', 'Riley echo check #5024 [fr]', 'You said: Riley echo check #5024 [fr]'),
    ('es', 'Riley echo check #5025 [es]', 'You said: Riley echo check #5025 [es]'),
    ('bn', 'Riley echo check #5026 [bn]', 'You said: Riley echo check #5026 [bn]'),
    ('sa', 'Riley echo check #5027 [sa]', 'You said: Riley echo check #5027 [sa]'),
    ('en', 'Riley echo check #5028 [en]', 'You said: Riley echo check #5028 [en]'),
    ('hi', 'Riley echo check #5029 [hi]', 'You said: Riley echo check #5029 [hi]'),
    ('fr', 'Riley echo check #5030 [fr]', 'You said: Riley echo check #5030 [fr]'),
    ('es', 'Riley echo check #5031 [es]', 'You said: Riley echo check #5031 [es]'),
    ('bn', 'Riley echo check #5032 [bn]', 'You said: Riley echo check #5032 [bn]'),
    ('sa', 'Riley echo check #5033 [sa]', 'You said: Riley echo check #5033 [sa]'),
    ('en', 'Riley echo check #5034 [en]', 'You said: Riley echo check #5034 [en]'),
    ('hi', 'Riley echo check #5035 [hi]', 'You said: Riley echo check #5035 [hi]'),
    ('fr', 'Riley echo check #5036 [fr]', 'You said: Riley echo check #5036 [fr]'),
    ('es', 'Riley echo check #5037 [es]', 'You said: Riley echo check #5037 [es]'),
    ('bn', 'Riley echo check #5038 [bn]', 'You said: Riley echo check #5038 [bn]'),
    ('sa', 'Riley echo check #5039 [sa]', 'You said: Riley echo check #5039 [sa]'),
    ('en', 'Riley echo check #5040 [en]', 'You said: Riley echo check #5040 [en]'),
    ('hi', 'Riley echo check #5041 [hi]', 'You said: Riley echo check #5041 [hi]'),
]


def test_spec_batch_051() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
