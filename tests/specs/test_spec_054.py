"""Verification spec batch 054: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('es', 'Riley echo check #5301 [es]', 'You said: Riley echo check #5301 [es]'),
    ('bn', 'Riley echo check #5302 [bn]', 'You said: Riley echo check #5302 [bn]'),
    ('sa', 'Riley echo check #5303 [sa]', 'You said: Riley echo check #5303 [sa]'),
    ('en', 'Riley echo check #5304 [en]', 'You said: Riley echo check #5304 [en]'),
    ('hi', 'Riley echo check #5305 [hi]', 'You said: Riley echo check #5305 [hi]'),
    ('fr', 'Riley echo check #5306 [fr]', 'You said: Riley echo check #5306 [fr]'),
    ('es', 'Riley echo check #5307 [es]', 'You said: Riley echo check #5307 [es]'),
    ('bn', 'Riley echo check #5308 [bn]', 'You said: Riley echo check #5308 [bn]'),
    ('sa', 'Riley echo check #5309 [sa]', 'You said: Riley echo check #5309 [sa]'),
    ('en', 'Riley echo check #5310 [en]', 'You said: Riley echo check #5310 [en]'),
    ('hi', 'Riley echo check #5311 [hi]', 'You said: Riley echo check #5311 [hi]'),
    ('fr', 'Riley echo check #5312 [fr]', 'You said: Riley echo check #5312 [fr]'),
    ('es', 'Riley echo check #5313 [es]', 'You said: Riley echo check #5313 [es]'),
    ('bn', 'Riley echo check #5314 [bn]', 'You said: Riley echo check #5314 [bn]'),
    ('sa', 'Riley echo check #5315 [sa]', 'You said: Riley echo check #5315 [sa]'),
    ('en', 'Riley echo check #5316 [en]', 'You said: Riley echo check #5316 [en]'),
    ('hi', 'Riley echo check #5317 [hi]', 'You said: Riley echo check #5317 [hi]'),
    ('fr', 'Riley echo check #5318 [fr]', 'You said: Riley echo check #5318 [fr]'),
    ('es', 'Riley echo check #5319 [es]', 'You said: Riley echo check #5319 [es]'),
    ('bn', 'Riley echo check #5320 [bn]', 'You said: Riley echo check #5320 [bn]'),
    ('sa', 'Riley echo check #5321 [sa]', 'You said: Riley echo check #5321 [sa]'),
    ('en', 'Riley echo check #5322 [en]', 'You said: Riley echo check #5322 [en]'),
    ('hi', 'Riley echo check #5323 [hi]', 'You said: Riley echo check #5323 [hi]'),
    ('fr', 'Riley echo check #5324 [fr]', 'You said: Riley echo check #5324 [fr]'),
    ('es', 'Riley echo check #5325 [es]', 'You said: Riley echo check #5325 [es]'),
    ('bn', 'Riley echo check #5326 [bn]', 'You said: Riley echo check #5326 [bn]'),
    ('sa', 'Riley echo check #5327 [sa]', 'You said: Riley echo check #5327 [sa]'),
    ('en', 'Riley echo check #5328 [en]', 'You said: Riley echo check #5328 [en]'),
    ('hi', 'Riley echo check #5329 [hi]', 'You said: Riley echo check #5329 [hi]'),
    ('fr', 'Riley echo check #5330 [fr]', 'You said: Riley echo check #5330 [fr]'),
    ('es', 'Riley echo check #5331 [es]', 'You said: Riley echo check #5331 [es]'),
]


def test_spec_batch_054() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
