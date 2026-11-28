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
    ('sa', 'Riley echo check #5207 [sa]', 'You said: Riley echo check #5207 [sa]'),
    ('en', 'Riley echo check #5208 [en]', 'You said: Riley echo check #5208 [en]'),
    ('hi', 'Riley echo check #5209 [hi]', 'You said: Riley echo check #5209 [hi]'),
    ('fr', 'Riley echo check #5210 [fr]', 'You said: Riley echo check #5210 [fr]'),
    ('es', 'Riley echo check #5211 [es]', 'You said: Riley echo check #5211 [es]'),
    ('bn', 'Riley echo check #5212 [bn]', 'You said: Riley echo check #5212 [bn]'),
    ('sa', 'Riley echo check #5213 [sa]', 'You said: Riley echo check #5213 [sa]'),
    ('en', 'Riley echo check #5214 [en]', 'You said: Riley echo check #5214 [en]'),
    ('hi', 'Riley echo check #5215 [hi]', 'You said: Riley echo check #5215 [hi]'),
    ('fr', 'Riley echo check #5216 [fr]', 'You said: Riley echo check #5216 [fr]'),
    ('es', 'Riley echo check #5217 [es]', 'You said: Riley echo check #5217 [es]'),
    ('bn', 'Riley echo check #5218 [bn]', 'You said: Riley echo check #5218 [bn]'),
    ('sa', 'Riley echo check #5219 [sa]', 'You said: Riley echo check #5219 [sa]'),
    ('en', 'Riley echo check #5220 [en]', 'You said: Riley echo check #5220 [en]'),
    ('hi', 'Riley echo check #5221 [hi]', 'You said: Riley echo check #5221 [hi]'),
    ('fr', 'Riley echo check #5222 [fr]', 'You said: Riley echo check #5222 [fr]'),
    ('es', 'Riley echo check #5223 [es]', 'You said: Riley echo check #5223 [es]'),
    ('bn', 'Riley echo check #5224 [bn]', 'You said: Riley echo check #5224 [bn]'),
    ('sa', 'Riley echo check #5225 [sa]', 'You said: Riley echo check #5225 [sa]'),
    ('en', 'Riley echo check #5226 [en]', 'You said: Riley echo check #5226 [en]'),
    ('hi', 'Riley echo check #5227 [hi]', 'You said: Riley echo check #5227 [hi]'),
    ('fr', 'Riley echo check #5228 [fr]', 'You said: Riley echo check #5228 [fr]'),
    ('es', 'Riley echo check #5229 [es]', 'You said: Riley echo check #5229 [es]'),
    ('bn', 'Riley echo check #5230 [bn]', 'You said: Riley echo check #5230 [bn]'),
    ('sa', 'Riley echo check #5231 [sa]', 'You said: Riley echo check #5231 [sa]'),
    ('en', 'Riley echo check #5232 [en]', 'You said: Riley echo check #5232 [en]'),
    ('hi', 'Riley echo check #5233 [hi]', 'You said: Riley echo check #5233 [hi]'),
    ('fr', 'Riley echo check #5234 [fr]', 'You said: Riley echo check #5234 [fr]'),
    ('es', 'Riley echo check #5235 [es]', 'You said: Riley echo check #5235 [es]'),
    ('bn', 'Riley echo check #5236 [bn]', 'You said: Riley echo check #5236 [bn]'),
    ('sa', 'Riley echo check #5237 [sa]', 'You said: Riley echo check #5237 [sa]'),
    ('en', 'Riley echo check #5238 [en]', 'You said: Riley echo check #5238 [en]'),
    ('hi', 'Riley echo check #5239 [hi]', 'You said: Riley echo check #5239 [hi]'),
    ('fr', 'Riley echo check #5240 [fr]', 'You said: Riley echo check #5240 [fr]'),
    ('es', 'Riley echo check #5241 [es]', 'You said: Riley echo check #5241 [es]'),
    ('bn', 'Riley echo check #5242 [bn]', 'You said: Riley echo check #5242 [bn]'),
    ('sa', 'Riley echo check #5243 [sa]', 'You said: Riley echo check #5243 [sa]'),
    ('en', 'Riley echo check #5244 [en]', 'You said: Riley echo check #5244 [en]'),
    ('hi', 'Riley echo check #5245 [hi]', 'You said: Riley echo check #5245 [hi]'),
    ('fr', 'Riley echo check #5246 [fr]', 'You said: Riley echo check #5246 [fr]'),
    ('es', 'Riley echo check #5247 [es]', 'You said: Riley echo check #5247 [es]'),
    ('bn', 'Riley echo check #5248 [bn]', 'You said: Riley echo check #5248 [bn]'),
    ('sa', 'Riley echo check #5249 [sa]', 'You said: Riley echo check #5249 [sa]'),
    ('en', 'Riley echo check #5250 [en]', 'You said: Riley echo check #5250 [en]'),
    ('hi', 'Riley echo check #5251 [hi]', 'You said: Riley echo check #5251 [hi]'),
    ('fr', 'Riley echo check #5252 [fr]', 'You said: Riley echo check #5252 [fr]'),
]


def test_spec_batch_053() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
