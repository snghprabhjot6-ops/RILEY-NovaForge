"""Verification spec batch 055: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('hi', 'Riley echo check #5401 [hi]', 'You said: Riley echo check #5401 [hi]'),
    ('fr', 'Riley echo check #5402 [fr]', 'You said: Riley echo check #5402 [fr]'),
    ('es', 'Riley echo check #5403 [es]', 'You said: Riley echo check #5403 [es]'),
    ('bn', 'Riley echo check #5404 [bn]', 'You said: Riley echo check #5404 [bn]'),
    ('sa', 'Riley echo check #5405 [sa]', 'You said: Riley echo check #5405 [sa]'),
    ('en', 'Riley echo check #5406 [en]', 'You said: Riley echo check #5406 [en]'),
    ('hi', 'Riley echo check #5407 [hi]', 'You said: Riley echo check #5407 [hi]'),
    ('fr', 'Riley echo check #5408 [fr]', 'You said: Riley echo check #5408 [fr]'),
    ('es', 'Riley echo check #5409 [es]', 'You said: Riley echo check #5409 [es]'),
    ('bn', 'Riley echo check #5410 [bn]', 'You said: Riley echo check #5410 [bn]'),
    ('sa', 'Riley echo check #5411 [sa]', 'You said: Riley echo check #5411 [sa]'),
    ('en', 'Riley echo check #5412 [en]', 'You said: Riley echo check #5412 [en]'),
    ('hi', 'Riley echo check #5413 [hi]', 'You said: Riley echo check #5413 [hi]'),
    ('fr', 'Riley echo check #5414 [fr]', 'You said: Riley echo check #5414 [fr]'),
    ('es', 'Riley echo check #5415 [es]', 'You said: Riley echo check #5415 [es]'),
    ('bn', 'Riley echo check #5416 [bn]', 'You said: Riley echo check #5416 [bn]'),
    ('sa', 'Riley echo check #5417 [sa]', 'You said: Riley echo check #5417 [sa]'),
    ('en', 'Riley echo check #5418 [en]', 'You said: Riley echo check #5418 [en]'),
    ('hi', 'Riley echo check #5419 [hi]', 'You said: Riley echo check #5419 [hi]'),
    ('fr', 'Riley echo check #5420 [fr]', 'You said: Riley echo check #5420 [fr]'),
    ('es', 'Riley echo check #5421 [es]', 'You said: Riley echo check #5421 [es]'),
    ('bn', 'Riley echo check #5422 [bn]', 'You said: Riley echo check #5422 [bn]'),
    ('sa', 'Riley echo check #5423 [sa]', 'You said: Riley echo check #5423 [sa]'),
    ('en', 'Riley echo check #5424 [en]', 'You said: Riley echo check #5424 [en]'),
    ('hi', 'Riley echo check #5425 [hi]', 'You said: Riley echo check #5425 [hi]'),
    ('fr', 'Riley echo check #5426 [fr]', 'You said: Riley echo check #5426 [fr]'),
    ('es', 'Riley echo check #5427 [es]', 'You said: Riley echo check #5427 [es]'),
    ('bn', 'Riley echo check #5428 [bn]', 'You said: Riley echo check #5428 [bn]'),
    ('sa', 'Riley echo check #5429 [sa]', 'You said: Riley echo check #5429 [sa]'),
    ('en', 'Riley echo check #5430 [en]', 'You said: Riley echo check #5430 [en]'),
    ('hi', 'Riley echo check #5431 [hi]', 'You said: Riley echo check #5431 [hi]'),
    ('fr', 'Riley echo check #5432 [fr]', 'You said: Riley echo check #5432 [fr]'),
    ('es', 'Riley echo check #5433 [es]', 'You said: Riley echo check #5433 [es]'),
    ('bn', 'Riley echo check #5434 [bn]', 'You said: Riley echo check #5434 [bn]'),
    ('sa', 'Riley echo check #5435 [sa]', 'You said: Riley echo check #5435 [sa]'),
    ('en', 'Riley echo check #5436 [en]', 'You said: Riley echo check #5436 [en]'),
    ('hi', 'Riley echo check #5437 [hi]', 'You said: Riley echo check #5437 [hi]'),
    ('fr', 'Riley echo check #5438 [fr]', 'You said: Riley echo check #5438 [fr]'),
    ('es', 'Riley echo check #5439 [es]', 'You said: Riley echo check #5439 [es]'),
    ('bn', 'Riley echo check #5440 [bn]', 'You said: Riley echo check #5440 [bn]'),
    ('sa', 'Riley echo check #5441 [sa]', 'You said: Riley echo check #5441 [sa]'),
    ('en', 'Riley echo check #5442 [en]', 'You said: Riley echo check #5442 [en]'),
    ('hi', 'Riley echo check #5443 [hi]', 'You said: Riley echo check #5443 [hi]'),
    ('fr', 'Riley echo check #5444 [fr]', 'You said: Riley echo check #5444 [fr]'),
    ('es', 'Riley echo check #5445 [es]', 'You said: Riley echo check #5445 [es]'),
    ('bn', 'Riley echo check #5446 [bn]', 'You said: Riley echo check #5446 [bn]'),
    ('sa', 'Riley echo check #5447 [sa]', 'You said: Riley echo check #5447 [sa]'),
    ('en', 'Riley echo check #5448 [en]', 'You said: Riley echo check #5448 [en]'),
    ('hi', 'Riley echo check #5449 [hi]', 'You said: Riley echo check #5449 [hi]'),
    ('fr', 'Riley echo check #5450 [fr]', 'You said: Riley echo check #5450 [fr]'),
    ('es', 'Riley echo check #5451 [es]', 'You said: Riley echo check #5451 [es]'),
    ('bn', 'Riley echo check #5452 [bn]', 'You said: Riley echo check #5452 [bn]'),
]


def test_spec_batch_055() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
