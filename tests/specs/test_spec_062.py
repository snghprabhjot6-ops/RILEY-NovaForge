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
    ('bn', 'Riley echo check #6106 [bn]', 'You said: Riley echo check #6106 [bn]'),
    ('sa', 'Riley echo check #6107 [sa]', 'You said: Riley echo check #6107 [sa]'),
    ('en', 'Riley echo check #6108 [en]', 'You said: Riley echo check #6108 [en]'),
    ('hi', 'Riley echo check #6109 [hi]', 'You said: Riley echo check #6109 [hi]'),
    ('fr', 'Riley echo check #6110 [fr]', 'You said: Riley echo check #6110 [fr]'),
    ('es', 'Riley echo check #6111 [es]', 'You said: Riley echo check #6111 [es]'),
    ('bn', 'Riley echo check #6112 [bn]', 'You said: Riley echo check #6112 [bn]'),
    ('sa', 'Riley echo check #6113 [sa]', 'You said: Riley echo check #6113 [sa]'),
    ('en', 'Riley echo check #6114 [en]', 'You said: Riley echo check #6114 [en]'),
    ('hi', 'Riley echo check #6115 [hi]', 'You said: Riley echo check #6115 [hi]'),
    ('fr', 'Riley echo check #6116 [fr]', 'You said: Riley echo check #6116 [fr]'),
    ('es', 'Riley echo check #6117 [es]', 'You said: Riley echo check #6117 [es]'),
    ('bn', 'Riley echo check #6118 [bn]', 'You said: Riley echo check #6118 [bn]'),
    ('sa', 'Riley echo check #6119 [sa]', 'You said: Riley echo check #6119 [sa]'),
    ('en', 'Riley echo check #6120 [en]', 'You said: Riley echo check #6120 [en]'),
    ('hi', 'Riley echo check #6121 [hi]', 'You said: Riley echo check #6121 [hi]'),
    ('fr', 'Riley echo check #6122 [fr]', 'You said: Riley echo check #6122 [fr]'),
    ('es', 'Riley echo check #6123 [es]', 'You said: Riley echo check #6123 [es]'),
    ('bn', 'Riley echo check #6124 [bn]', 'You said: Riley echo check #6124 [bn]'),
    ('sa', 'Riley echo check #6125 [sa]', 'You said: Riley echo check #6125 [sa]'),
    ('en', 'Riley echo check #6126 [en]', 'You said: Riley echo check #6126 [en]'),
    ('hi', 'Riley echo check #6127 [hi]', 'You said: Riley echo check #6127 [hi]'),
    ('fr', 'Riley echo check #6128 [fr]', 'You said: Riley echo check #6128 [fr]'),
    ('es', 'Riley echo check #6129 [es]', 'You said: Riley echo check #6129 [es]'),
    ('bn', 'Riley echo check #6130 [bn]', 'You said: Riley echo check #6130 [bn]'),
    ('sa', 'Riley echo check #6131 [sa]', 'You said: Riley echo check #6131 [sa]'),
    ('en', 'Riley echo check #6132 [en]', 'You said: Riley echo check #6132 [en]'),
    ('hi', 'Riley echo check #6133 [hi]', 'You said: Riley echo check #6133 [hi]'),
    ('fr', 'Riley echo check #6134 [fr]', 'You said: Riley echo check #6134 [fr]'),
    ('es', 'Riley echo check #6135 [es]', 'You said: Riley echo check #6135 [es]'),
    ('bn', 'Riley echo check #6136 [bn]', 'You said: Riley echo check #6136 [bn]'),
    ('sa', 'Riley echo check #6137 [sa]', 'You said: Riley echo check #6137 [sa]'),
    ('en', 'Riley echo check #6138 [en]', 'You said: Riley echo check #6138 [en]'),
    ('hi', 'Riley echo check #6139 [hi]', 'You said: Riley echo check #6139 [hi]'),
]


def test_spec_batch_062() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
