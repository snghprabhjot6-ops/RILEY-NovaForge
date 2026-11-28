"""Verification spec batch 052: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('hi', 'Riley echo check #5101 [hi]', 'You said: Riley echo check #5101 [hi]'),
    ('fr', 'Riley echo check #5102 [fr]', 'You said: Riley echo check #5102 [fr]'),
    ('es', 'Riley echo check #5103 [es]', 'You said: Riley echo check #5103 [es]'),
    ('bn', 'Riley echo check #5104 [bn]', 'You said: Riley echo check #5104 [bn]'),
    ('sa', 'Riley echo check #5105 [sa]', 'You said: Riley echo check #5105 [sa]'),
    ('en', 'Riley echo check #5106 [en]', 'You said: Riley echo check #5106 [en]'),
    ('hi', 'Riley echo check #5107 [hi]', 'You said: Riley echo check #5107 [hi]'),
    ('fr', 'Riley echo check #5108 [fr]', 'You said: Riley echo check #5108 [fr]'),
    ('es', 'Riley echo check #5109 [es]', 'You said: Riley echo check #5109 [es]'),
    ('bn', 'Riley echo check #5110 [bn]', 'You said: Riley echo check #5110 [bn]'),
    ('sa', 'Riley echo check #5111 [sa]', 'You said: Riley echo check #5111 [sa]'),
    ('en', 'Riley echo check #5112 [en]', 'You said: Riley echo check #5112 [en]'),
    ('hi', 'Riley echo check #5113 [hi]', 'You said: Riley echo check #5113 [hi]'),
    ('fr', 'Riley echo check #5114 [fr]', 'You said: Riley echo check #5114 [fr]'),
    ('es', 'Riley echo check #5115 [es]', 'You said: Riley echo check #5115 [es]'),
    ('bn', 'Riley echo check #5116 [bn]', 'You said: Riley echo check #5116 [bn]'),
    ('sa', 'Riley echo check #5117 [sa]', 'You said: Riley echo check #5117 [sa]'),
    ('en', 'Riley echo check #5118 [en]', 'You said: Riley echo check #5118 [en]'),
    ('hi', 'Riley echo check #5119 [hi]', 'You said: Riley echo check #5119 [hi]'),
    ('fr', 'Riley echo check #5120 [fr]', 'You said: Riley echo check #5120 [fr]'),
    ('es', 'Riley echo check #5121 [es]', 'You said: Riley echo check #5121 [es]'),
    ('bn', 'Riley echo check #5122 [bn]', 'You said: Riley echo check #5122 [bn]'),
    ('sa', 'Riley echo check #5123 [sa]', 'You said: Riley echo check #5123 [sa]'),
    ('en', 'Riley echo check #5124 [en]', 'You said: Riley echo check #5124 [en]'),
    ('hi', 'Riley echo check #5125 [hi]', 'You said: Riley echo check #5125 [hi]'),
    ('fr', 'Riley echo check #5126 [fr]', 'You said: Riley echo check #5126 [fr]'),
    ('es', 'Riley echo check #5127 [es]', 'You said: Riley echo check #5127 [es]'),
    ('bn', 'Riley echo check #5128 [bn]', 'You said: Riley echo check #5128 [bn]'),
    ('sa', 'Riley echo check #5129 [sa]', 'You said: Riley echo check #5129 [sa]'),
    ('en', 'Riley echo check #5130 [en]', 'You said: Riley echo check #5130 [en]'),
    ('hi', 'Riley echo check #5131 [hi]', 'You said: Riley echo check #5131 [hi]'),
    ('fr', 'Riley echo check #5132 [fr]', 'You said: Riley echo check #5132 [fr]'),
    ('es', 'Riley echo check #5133 [es]', 'You said: Riley echo check #5133 [es]'),
    ('bn', 'Riley echo check #5134 [bn]', 'You said: Riley echo check #5134 [bn]'),
    ('sa', 'Riley echo check #5135 [sa]', 'You said: Riley echo check #5135 [sa]'),
    ('en', 'Riley echo check #5136 [en]', 'You said: Riley echo check #5136 [en]'),
    ('hi', 'Riley echo check #5137 [hi]', 'You said: Riley echo check #5137 [hi]'),
    ('fr', 'Riley echo check #5138 [fr]', 'You said: Riley echo check #5138 [fr]'),
    ('es', 'Riley echo check #5139 [es]', 'You said: Riley echo check #5139 [es]'),
    ('bn', 'Riley echo check #5140 [bn]', 'You said: Riley echo check #5140 [bn]'),
    ('sa', 'Riley echo check #5141 [sa]', 'You said: Riley echo check #5141 [sa]'),
    ('en', 'Riley echo check #5142 [en]', 'You said: Riley echo check #5142 [en]'),
    ('hi', 'Riley echo check #5143 [hi]', 'You said: Riley echo check #5143 [hi]'),
    ('fr', 'Riley echo check #5144 [fr]', 'You said: Riley echo check #5144 [fr]'),
    ('es', 'Riley echo check #5145 [es]', 'You said: Riley echo check #5145 [es]'),
    ('bn', 'Riley echo check #5146 [bn]', 'You said: Riley echo check #5146 [bn]'),
    ('sa', 'Riley echo check #5147 [sa]', 'You said: Riley echo check #5147 [sa]'),
    ('en', 'Riley echo check #5148 [en]', 'You said: Riley echo check #5148 [en]'),
    ('hi', 'Riley echo check #5149 [hi]', 'You said: Riley echo check #5149 [hi]'),
    ('fr', 'Riley echo check #5150 [fr]', 'You said: Riley echo check #5150 [fr]'),
    ('es', 'Riley echo check #5151 [es]', 'You said: Riley echo check #5151 [es]'),
    ('bn', 'Riley echo check #5152 [bn]', 'You said: Riley echo check #5152 [bn]'),
    ('sa', 'Riley echo check #5153 [sa]', 'You said: Riley echo check #5153 [sa]'),
    ('en', 'Riley echo check #5154 [en]', 'You said: Riley echo check #5154 [en]'),
]


def test_spec_batch_052() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
