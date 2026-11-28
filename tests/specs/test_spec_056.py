"""Verification spec batch 056: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('sa', 'Riley echo check #5501 [sa]', 'You said: Riley echo check #5501 [sa]'),
    ('en', 'Riley echo check #5502 [en]', 'You said: Riley echo check #5502 [en]'),
    ('hi', 'Riley echo check #5503 [hi]', 'You said: Riley echo check #5503 [hi]'),
    ('fr', 'Riley echo check #5504 [fr]', 'You said: Riley echo check #5504 [fr]'),
    ('es', 'Riley echo check #5505 [es]', 'You said: Riley echo check #5505 [es]'),
    ('bn', 'Riley echo check #5506 [bn]', 'You said: Riley echo check #5506 [bn]'),
    ('sa', 'Riley echo check #5507 [sa]', 'You said: Riley echo check #5507 [sa]'),
    ('en', 'Riley echo check #5508 [en]', 'You said: Riley echo check #5508 [en]'),
    ('hi', 'Riley echo check #5509 [hi]', 'You said: Riley echo check #5509 [hi]'),
    ('fr', 'Riley echo check #5510 [fr]', 'You said: Riley echo check #5510 [fr]'),
    ('es', 'Riley echo check #5511 [es]', 'You said: Riley echo check #5511 [es]'),
    ('bn', 'Riley echo check #5512 [bn]', 'You said: Riley echo check #5512 [bn]'),
    ('sa', 'Riley echo check #5513 [sa]', 'You said: Riley echo check #5513 [sa]'),
    ('en', 'Riley echo check #5514 [en]', 'You said: Riley echo check #5514 [en]'),
    ('hi', 'Riley echo check #5515 [hi]', 'You said: Riley echo check #5515 [hi]'),
    ('fr', 'Riley echo check #5516 [fr]', 'You said: Riley echo check #5516 [fr]'),
    ('es', 'Riley echo check #5517 [es]', 'You said: Riley echo check #5517 [es]'),
    ('bn', 'Riley echo check #5518 [bn]', 'You said: Riley echo check #5518 [bn]'),
    ('sa', 'Riley echo check #5519 [sa]', 'You said: Riley echo check #5519 [sa]'),
    ('en', 'Riley echo check #5520 [en]', 'You said: Riley echo check #5520 [en]'),
    ('hi', 'Riley echo check #5521 [hi]', 'You said: Riley echo check #5521 [hi]'),
    ('fr', 'Riley echo check #5522 [fr]', 'You said: Riley echo check #5522 [fr]'),
    ('es', 'Riley echo check #5523 [es]', 'You said: Riley echo check #5523 [es]'),
    ('bn', 'Riley echo check #5524 [bn]', 'You said: Riley echo check #5524 [bn]'),
    ('sa', 'Riley echo check #5525 [sa]', 'You said: Riley echo check #5525 [sa]'),
    ('en', 'Riley echo check #5526 [en]', 'You said: Riley echo check #5526 [en]'),
    ('hi', 'Riley echo check #5527 [hi]', 'You said: Riley echo check #5527 [hi]'),
    ('fr', 'Riley echo check #5528 [fr]', 'You said: Riley echo check #5528 [fr]'),
    ('es', 'Riley echo check #5529 [es]', 'You said: Riley echo check #5529 [es]'),
    ('bn', 'Riley echo check #5530 [bn]', 'You said: Riley echo check #5530 [bn]'),
    ('sa', 'Riley echo check #5531 [sa]', 'You said: Riley echo check #5531 [sa]'),
    ('en', 'Riley echo check #5532 [en]', 'You said: Riley echo check #5532 [en]'),
    ('hi', 'Riley echo check #5533 [hi]', 'You said: Riley echo check #5533 [hi]'),
    ('fr', 'Riley echo check #5534 [fr]', 'You said: Riley echo check #5534 [fr]'),
    ('es', 'Riley echo check #5535 [es]', 'You said: Riley echo check #5535 [es]'),
    ('bn', 'Riley echo check #5536 [bn]', 'You said: Riley echo check #5536 [bn]'),
    ('sa', 'Riley echo check #5537 [sa]', 'You said: Riley echo check #5537 [sa]'),
    ('en', 'Riley echo check #5538 [en]', 'You said: Riley echo check #5538 [en]'),
    ('hi', 'Riley echo check #5539 [hi]', 'You said: Riley echo check #5539 [hi]'),
    ('fr', 'Riley echo check #5540 [fr]', 'You said: Riley echo check #5540 [fr]'),
    ('es', 'Riley echo check #5541 [es]', 'You said: Riley echo check #5541 [es]'),
    ('bn', 'Riley echo check #5542 [bn]', 'You said: Riley echo check #5542 [bn]'),
]


def test_spec_batch_056() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
