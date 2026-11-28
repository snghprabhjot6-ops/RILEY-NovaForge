"""Verification spec batch 047: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('sa', 'Riley echo check #4601 [sa]', 'You said: Riley echo check #4601 [sa]'),
    ('en', 'Riley echo check #4602 [en]', 'You said: Riley echo check #4602 [en]'),
    ('hi', 'Riley echo check #4603 [hi]', 'You said: Riley echo check #4603 [hi]'),
    ('fr', 'Riley echo check #4604 [fr]', 'You said: Riley echo check #4604 [fr]'),
    ('es', 'Riley echo check #4605 [es]', 'You said: Riley echo check #4605 [es]'),
    ('bn', 'Riley echo check #4606 [bn]', 'You said: Riley echo check #4606 [bn]'),
    ('sa', 'Riley echo check #4607 [sa]', 'You said: Riley echo check #4607 [sa]'),
    ('en', 'Riley echo check #4608 [en]', 'You said: Riley echo check #4608 [en]'),
    ('hi', 'Riley echo check #4609 [hi]', 'You said: Riley echo check #4609 [hi]'),
    ('fr', 'Riley echo check #4610 [fr]', 'You said: Riley echo check #4610 [fr]'),
    ('es', 'Riley echo check #4611 [es]', 'You said: Riley echo check #4611 [es]'),
    ('bn', 'Riley echo check #4612 [bn]', 'You said: Riley echo check #4612 [bn]'),
    ('sa', 'Riley echo check #4613 [sa]', 'You said: Riley echo check #4613 [sa]'),
    ('en', 'Riley echo check #4614 [en]', 'You said: Riley echo check #4614 [en]'),
    ('hi', 'Riley echo check #4615 [hi]', 'You said: Riley echo check #4615 [hi]'),
    ('fr', 'Riley echo check #4616 [fr]', 'You said: Riley echo check #4616 [fr]'),
    ('es', 'Riley echo check #4617 [es]', 'You said: Riley echo check #4617 [es]'),
    ('bn', 'Riley echo check #4618 [bn]', 'You said: Riley echo check #4618 [bn]'),
    ('sa', 'Riley echo check #4619 [sa]', 'You said: Riley echo check #4619 [sa]'),
    ('en', 'Riley echo check #4620 [en]', 'You said: Riley echo check #4620 [en]'),
    ('hi', 'Riley echo check #4621 [hi]', 'You said: Riley echo check #4621 [hi]'),
    ('fr', 'Riley echo check #4622 [fr]', 'You said: Riley echo check #4622 [fr]'),
    ('es', 'Riley echo check #4623 [es]', 'You said: Riley echo check #4623 [es]'),
    ('bn', 'Riley echo check #4624 [bn]', 'You said: Riley echo check #4624 [bn]'),
    ('sa', 'Riley echo check #4625 [sa]', 'You said: Riley echo check #4625 [sa]'),
    ('en', 'Riley echo check #4626 [en]', 'You said: Riley echo check #4626 [en]'),
    ('hi', 'Riley echo check #4627 [hi]', 'You said: Riley echo check #4627 [hi]'),
    ('fr', 'Riley echo check #4628 [fr]', 'You said: Riley echo check #4628 [fr]'),
    ('es', 'Riley echo check #4629 [es]', 'You said: Riley echo check #4629 [es]'),
    ('bn', 'Riley echo check #4630 [bn]', 'You said: Riley echo check #4630 [bn]'),
    ('sa', 'Riley echo check #4631 [sa]', 'You said: Riley echo check #4631 [sa]'),
    ('en', 'Riley echo check #4632 [en]', 'You said: Riley echo check #4632 [en]'),
    ('hi', 'Riley echo check #4633 [hi]', 'You said: Riley echo check #4633 [hi]'),
    ('fr', 'Riley echo check #4634 [fr]', 'You said: Riley echo check #4634 [fr]'),
]


def test_spec_batch_047() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
