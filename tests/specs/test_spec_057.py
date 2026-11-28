"""Verification spec batch 057: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('es', 'Riley echo check #5601 [es]', 'You said: Riley echo check #5601 [es]'),
    ('bn', 'Riley echo check #5602 [bn]', 'You said: Riley echo check #5602 [bn]'),
    ('sa', 'Riley echo check #5603 [sa]', 'You said: Riley echo check #5603 [sa]'),
    ('en', 'Riley echo check #5604 [en]', 'You said: Riley echo check #5604 [en]'),
    ('hi', 'Riley echo check #5605 [hi]', 'You said: Riley echo check #5605 [hi]'),
    ('fr', 'Riley echo check #5606 [fr]', 'You said: Riley echo check #5606 [fr]'),
    ('es', 'Riley echo check #5607 [es]', 'You said: Riley echo check #5607 [es]'),
    ('bn', 'Riley echo check #5608 [bn]', 'You said: Riley echo check #5608 [bn]'),
    ('sa', 'Riley echo check #5609 [sa]', 'You said: Riley echo check #5609 [sa]'),
    ('en', 'Riley echo check #5610 [en]', 'You said: Riley echo check #5610 [en]'),
    ('hi', 'Riley echo check #5611 [hi]', 'You said: Riley echo check #5611 [hi]'),
    ('fr', 'Riley echo check #5612 [fr]', 'You said: Riley echo check #5612 [fr]'),
    ('es', 'Riley echo check #5613 [es]', 'You said: Riley echo check #5613 [es]'),
    ('bn', 'Riley echo check #5614 [bn]', 'You said: Riley echo check #5614 [bn]'),
    ('sa', 'Riley echo check #5615 [sa]', 'You said: Riley echo check #5615 [sa]'),
    ('en', 'Riley echo check #5616 [en]', 'You said: Riley echo check #5616 [en]'),
    ('hi', 'Riley echo check #5617 [hi]', 'You said: Riley echo check #5617 [hi]'),
    ('fr', 'Riley echo check #5618 [fr]', 'You said: Riley echo check #5618 [fr]'),
    ('es', 'Riley echo check #5619 [es]', 'You said: Riley echo check #5619 [es]'),
    ('bn', 'Riley echo check #5620 [bn]', 'You said: Riley echo check #5620 [bn]'),
    ('sa', 'Riley echo check #5621 [sa]', 'You said: Riley echo check #5621 [sa]'),
    ('en', 'Riley echo check #5622 [en]', 'You said: Riley echo check #5622 [en]'),
    ('hi', 'Riley echo check #5623 [hi]', 'You said: Riley echo check #5623 [hi]'),
    ('fr', 'Riley echo check #5624 [fr]', 'You said: Riley echo check #5624 [fr]'),
    ('es', 'Riley echo check #5625 [es]', 'You said: Riley echo check #5625 [es]'),
    ('bn', 'Riley echo check #5626 [bn]', 'You said: Riley echo check #5626 [bn]'),
]


def test_spec_batch_057() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
