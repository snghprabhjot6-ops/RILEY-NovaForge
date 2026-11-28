"""Verification spec batch 064: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('hi', 'Riley echo check #6301 [hi]', 'You said: Riley echo check #6301 [hi]'),
    ('fr', 'Riley echo check #6302 [fr]', 'You said: Riley echo check #6302 [fr]'),
    ('es', 'Riley echo check #6303 [es]', 'You said: Riley echo check #6303 [es]'),
    ('bn', 'Riley echo check #6304 [bn]', 'You said: Riley echo check #6304 [bn]'),
    ('sa', 'Riley echo check #6305 [sa]', 'You said: Riley echo check #6305 [sa]'),
    ('en', 'Riley echo check #6306 [en]', 'You said: Riley echo check #6306 [en]'),
    ('hi', 'Riley echo check #6307 [hi]', 'You said: Riley echo check #6307 [hi]'),
    ('fr', 'Riley echo check #6308 [fr]', 'You said: Riley echo check #6308 [fr]'),
    ('es', 'Riley echo check #6309 [es]', 'You said: Riley echo check #6309 [es]'),
    ('bn', 'Riley echo check #6310 [bn]', 'You said: Riley echo check #6310 [bn]'),
    ('sa', 'Riley echo check #6311 [sa]', 'You said: Riley echo check #6311 [sa]'),
    ('en', 'Riley echo check #6312 [en]', 'You said: Riley echo check #6312 [en]'),
    ('hi', 'Riley echo check #6313 [hi]', 'You said: Riley echo check #6313 [hi]'),
    ('fr', 'Riley echo check #6314 [fr]', 'You said: Riley echo check #6314 [fr]'),
    ('es', 'Riley echo check #6315 [es]', 'You said: Riley echo check #6315 [es]'),
    ('bn', 'Riley echo check #6316 [bn]', 'You said: Riley echo check #6316 [bn]'),
    ('sa', 'Riley echo check #6317 [sa]', 'You said: Riley echo check #6317 [sa]'),
    ('en', 'Riley echo check #6318 [en]', 'You said: Riley echo check #6318 [en]'),
    ('hi', 'Riley echo check #6319 [hi]', 'You said: Riley echo check #6319 [hi]'),
    ('fr', 'Riley echo check #6320 [fr]', 'You said: Riley echo check #6320 [fr]'),
    ('es', 'Riley echo check #6321 [es]', 'You said: Riley echo check #6321 [es]'),
    ('bn', 'Riley echo check #6322 [bn]', 'You said: Riley echo check #6322 [bn]'),
    ('sa', 'Riley echo check #6323 [sa]', 'You said: Riley echo check #6323 [sa]'),
    ('en', 'Riley echo check #6324 [en]', 'You said: Riley echo check #6324 [en]'),
    ('hi', 'Riley echo check #6325 [hi]', 'You said: Riley echo check #6325 [hi]'),
    ('fr', 'Riley echo check #6326 [fr]', 'You said: Riley echo check #6326 [fr]'),
    ('es', 'Riley echo check #6327 [es]', 'You said: Riley echo check #6327 [es]'),
    ('bn', 'Riley echo check #6328 [bn]', 'You said: Riley echo check #6328 [bn]'),
    ('sa', 'Riley echo check #6329 [sa]', 'You said: Riley echo check #6329 [sa]'),
    ('en', 'Riley echo check #6330 [en]', 'You said: Riley echo check #6330 [en]'),
    ('hi', 'Riley echo check #6331 [hi]', 'You said: Riley echo check #6331 [hi]'),
    ('fr', 'Riley echo check #6332 [fr]', 'You said: Riley echo check #6332 [fr]'),
]


def test_spec_batch_064() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
