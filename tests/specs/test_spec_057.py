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
    ('sa', 'Riley echo check #5627 [sa]', 'You said: Riley echo check #5627 [sa]'),
    ('en', 'Riley echo check #5628 [en]', 'You said: Riley echo check #5628 [en]'),
    ('hi', 'Riley echo check #5629 [hi]', 'You said: Riley echo check #5629 [hi]'),
    ('fr', 'Riley echo check #5630 [fr]', 'You said: Riley echo check #5630 [fr]'),
    ('es', 'Riley echo check #5631 [es]', 'You said: Riley echo check #5631 [es]'),
    ('bn', 'Riley echo check #5632 [bn]', 'You said: Riley echo check #5632 [bn]'),
    ('sa', 'Riley echo check #5633 [sa]', 'You said: Riley echo check #5633 [sa]'),
    ('en', 'Riley echo check #5634 [en]', 'You said: Riley echo check #5634 [en]'),
    ('hi', 'Riley echo check #5635 [hi]', 'You said: Riley echo check #5635 [hi]'),
    ('fr', 'Riley echo check #5636 [fr]', 'You said: Riley echo check #5636 [fr]'),
    ('es', 'Riley echo check #5637 [es]', 'You said: Riley echo check #5637 [es]'),
    ('bn', 'Riley echo check #5638 [bn]', 'You said: Riley echo check #5638 [bn]'),
    ('sa', 'Riley echo check #5639 [sa]', 'You said: Riley echo check #5639 [sa]'),
    ('en', 'Riley echo check #5640 [en]', 'You said: Riley echo check #5640 [en]'),
    ('hi', 'Riley echo check #5641 [hi]', 'You said: Riley echo check #5641 [hi]'),
    ('fr', 'Riley echo check #5642 [fr]', 'You said: Riley echo check #5642 [fr]'),
    ('es', 'Riley echo check #5643 [es]', 'You said: Riley echo check #5643 [es]'),
    ('bn', 'Riley echo check #5644 [bn]', 'You said: Riley echo check #5644 [bn]'),
    ('sa', 'Riley echo check #5645 [sa]', 'You said: Riley echo check #5645 [sa]'),
    ('en', 'Riley echo check #5646 [en]', 'You said: Riley echo check #5646 [en]'),
]


def test_spec_batch_057() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
