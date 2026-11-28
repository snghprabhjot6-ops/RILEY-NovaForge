"""Verification spec batch 063: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('es', 'Riley echo check #6201 [es]', 'You said: Riley echo check #6201 [es]'),
    ('bn', 'Riley echo check #6202 [bn]', 'You said: Riley echo check #6202 [bn]'),
    ('sa', 'Riley echo check #6203 [sa]', 'You said: Riley echo check #6203 [sa]'),
    ('en', 'Riley echo check #6204 [en]', 'You said: Riley echo check #6204 [en]'),
    ('hi', 'Riley echo check #6205 [hi]', 'You said: Riley echo check #6205 [hi]'),
    ('fr', 'Riley echo check #6206 [fr]', 'You said: Riley echo check #6206 [fr]'),
    ('es', 'Riley echo check #6207 [es]', 'You said: Riley echo check #6207 [es]'),
    ('bn', 'Riley echo check #6208 [bn]', 'You said: Riley echo check #6208 [bn]'),
    ('sa', 'Riley echo check #6209 [sa]', 'You said: Riley echo check #6209 [sa]'),
    ('en', 'Riley echo check #6210 [en]', 'You said: Riley echo check #6210 [en]'),
    ('hi', 'Riley echo check #6211 [hi]', 'You said: Riley echo check #6211 [hi]'),
    ('fr', 'Riley echo check #6212 [fr]', 'You said: Riley echo check #6212 [fr]'),
    ('es', 'Riley echo check #6213 [es]', 'You said: Riley echo check #6213 [es]'),
    ('bn', 'Riley echo check #6214 [bn]', 'You said: Riley echo check #6214 [bn]'),
    ('sa', 'Riley echo check #6215 [sa]', 'You said: Riley echo check #6215 [sa]'),
    ('en', 'Riley echo check #6216 [en]', 'You said: Riley echo check #6216 [en]'),
    ('hi', 'Riley echo check #6217 [hi]', 'You said: Riley echo check #6217 [hi]'),
    ('fr', 'Riley echo check #6218 [fr]', 'You said: Riley echo check #6218 [fr]'),
    ('es', 'Riley echo check #6219 [es]', 'You said: Riley echo check #6219 [es]'),
    ('bn', 'Riley echo check #6220 [bn]', 'You said: Riley echo check #6220 [bn]'),
    ('sa', 'Riley echo check #6221 [sa]', 'You said: Riley echo check #6221 [sa]'),
    ('en', 'Riley echo check #6222 [en]', 'You said: Riley echo check #6222 [en]'),
    ('hi', 'Riley echo check #6223 [hi]', 'You said: Riley echo check #6223 [hi]'),
    ('fr', 'Riley echo check #6224 [fr]', 'You said: Riley echo check #6224 [fr]'),
    ('es', 'Riley echo check #6225 [es]', 'You said: Riley echo check #6225 [es]'),
    ('bn', 'Riley echo check #6226 [bn]', 'You said: Riley echo check #6226 [bn]'),
    ('sa', 'Riley echo check #6227 [sa]', 'You said: Riley echo check #6227 [sa]'),
    ('en', 'Riley echo check #6228 [en]', 'You said: Riley echo check #6228 [en]'),
    ('hi', 'Riley echo check #6229 [hi]', 'You said: Riley echo check #6229 [hi]'),
    ('fr', 'Riley echo check #6230 [fr]', 'You said: Riley echo check #6230 [fr]'),
    ('es', 'Riley echo check #6231 [es]', 'You said: Riley echo check #6231 [es]'),
    ('bn', 'Riley echo check #6232 [bn]', 'You said: Riley echo check #6232 [bn]'),
    ('sa', 'Riley echo check #6233 [sa]', 'You said: Riley echo check #6233 [sa]'),
    ('en', 'Riley echo check #6234 [en]', 'You said: Riley echo check #6234 [en]'),
    ('hi', 'Riley echo check #6235 [hi]', 'You said: Riley echo check #6235 [hi]'),
    ('fr', 'Riley echo check #6236 [fr]', 'You said: Riley echo check #6236 [fr]'),
    ('es', 'Riley echo check #6237 [es]', 'You said: Riley echo check #6237 [es]'),
    ('bn', 'Riley echo check #6238 [bn]', 'You said: Riley echo check #6238 [bn]'),
    ('sa', 'Riley echo check #6239 [sa]', 'You said: Riley echo check #6239 [sa]'),
    ('en', 'Riley echo check #6240 [en]', 'You said: Riley echo check #6240 [en]'),
    ('hi', 'Riley echo check #6241 [hi]', 'You said: Riley echo check #6241 [hi]'),
    ('fr', 'Riley echo check #6242 [fr]', 'You said: Riley echo check #6242 [fr]'),
    ('es', 'Riley echo check #6243 [es]', 'You said: Riley echo check #6243 [es]'),
    ('bn', 'Riley echo check #6244 [bn]', 'You said: Riley echo check #6244 [bn]'),
    ('sa', 'Riley echo check #6245 [sa]', 'You said: Riley echo check #6245 [sa]'),
    ('en', 'Riley echo check #6246 [en]', 'You said: Riley echo check #6246 [en]'),
]


def test_spec_batch_063() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
