"""Verification spec batch 048: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('es', 'Riley echo check #4701 [es]', 'You said: Riley echo check #4701 [es]'),
    ('bn', 'Riley echo check #4702 [bn]', 'You said: Riley echo check #4702 [bn]'),
    ('sa', 'Riley echo check #4703 [sa]', 'You said: Riley echo check #4703 [sa]'),
    ('en', 'Riley echo check #4704 [en]', 'You said: Riley echo check #4704 [en]'),
    ('hi', 'Riley echo check #4705 [hi]', 'You said: Riley echo check #4705 [hi]'),
    ('fr', 'Riley echo check #4706 [fr]', 'You said: Riley echo check #4706 [fr]'),
    ('es', 'Riley echo check #4707 [es]', 'You said: Riley echo check #4707 [es]'),
    ('bn', 'Riley echo check #4708 [bn]', 'You said: Riley echo check #4708 [bn]'),
    ('sa', 'Riley echo check #4709 [sa]', 'You said: Riley echo check #4709 [sa]'),
    ('en', 'Riley echo check #4710 [en]', 'You said: Riley echo check #4710 [en]'),
    ('hi', 'Riley echo check #4711 [hi]', 'You said: Riley echo check #4711 [hi]'),
    ('fr', 'Riley echo check #4712 [fr]', 'You said: Riley echo check #4712 [fr]'),
    ('es', 'Riley echo check #4713 [es]', 'You said: Riley echo check #4713 [es]'),
    ('bn', 'Riley echo check #4714 [bn]', 'You said: Riley echo check #4714 [bn]'),
    ('sa', 'Riley echo check #4715 [sa]', 'You said: Riley echo check #4715 [sa]'),
    ('en', 'Riley echo check #4716 [en]', 'You said: Riley echo check #4716 [en]'),
    ('hi', 'Riley echo check #4717 [hi]', 'You said: Riley echo check #4717 [hi]'),
    ('fr', 'Riley echo check #4718 [fr]', 'You said: Riley echo check #4718 [fr]'),
    ('es', 'Riley echo check #4719 [es]', 'You said: Riley echo check #4719 [es]'),
    ('bn', 'Riley echo check #4720 [bn]', 'You said: Riley echo check #4720 [bn]'),
    ('sa', 'Riley echo check #4721 [sa]', 'You said: Riley echo check #4721 [sa]'),
    ('en', 'Riley echo check #4722 [en]', 'You said: Riley echo check #4722 [en]'),
    ('hi', 'Riley echo check #4723 [hi]', 'You said: Riley echo check #4723 [hi]'),
    ('fr', 'Riley echo check #4724 [fr]', 'You said: Riley echo check #4724 [fr]'),
    ('es', 'Riley echo check #4725 [es]', 'You said: Riley echo check #4725 [es]'),
    ('bn', 'Riley echo check #4726 [bn]', 'You said: Riley echo check #4726 [bn]'),
    ('sa', 'Riley echo check #4727 [sa]', 'You said: Riley echo check #4727 [sa]'),
    ('en', 'Riley echo check #4728 [en]', 'You said: Riley echo check #4728 [en]'),
    ('hi', 'Riley echo check #4729 [hi]', 'You said: Riley echo check #4729 [hi]'),
    ('fr', 'Riley echo check #4730 [fr]', 'You said: Riley echo check #4730 [fr]'),
    ('es', 'Riley echo check #4731 [es]', 'You said: Riley echo check #4731 [es]'),
    ('bn', 'Riley echo check #4732 [bn]', 'You said: Riley echo check #4732 [bn]'),
    ('sa', 'Riley echo check #4733 [sa]', 'You said: Riley echo check #4733 [sa]'),
    ('en', 'Riley echo check #4734 [en]', 'You said: Riley echo check #4734 [en]'),
    ('hi', 'Riley echo check #4735 [hi]', 'You said: Riley echo check #4735 [hi]'),
    ('fr', 'Riley echo check #4736 [fr]', 'You said: Riley echo check #4736 [fr]'),
    ('es', 'Riley echo check #4737 [es]', 'You said: Riley echo check #4737 [es]'),
    ('bn', 'Riley echo check #4738 [bn]', 'You said: Riley echo check #4738 [bn]'),
    ('sa', 'Riley echo check #4739 [sa]', 'You said: Riley echo check #4739 [sa]'),
    ('en', 'Riley echo check #4740 [en]', 'You said: Riley echo check #4740 [en]'),
    ('hi', 'Riley echo check #4741 [hi]', 'You said: Riley echo check #4741 [hi]'),
    ('fr', 'Riley echo check #4742 [fr]', 'You said: Riley echo check #4742 [fr]'),
    ('es', 'Riley echo check #4743 [es]', 'You said: Riley echo check #4743 [es]'),
    ('bn', 'Riley echo check #4744 [bn]', 'You said: Riley echo check #4744 [bn]'),
    ('sa', 'Riley echo check #4745 [sa]', 'You said: Riley echo check #4745 [sa]'),
    ('en', 'Riley echo check #4746 [en]', 'You said: Riley echo check #4746 [en]'),
    ('hi', 'Riley echo check #4747 [hi]', 'You said: Riley echo check #4747 [hi]'),
    ('fr', 'Riley echo check #4748 [fr]', 'You said: Riley echo check #4748 [fr]'),
    ('es', 'Riley echo check #4749 [es]', 'You said: Riley echo check #4749 [es]'),
    ('bn', 'Riley echo check #4750 [bn]', 'You said: Riley echo check #4750 [bn]'),
    ('sa', 'Riley echo check #4751 [sa]', 'You said: Riley echo check #4751 [sa]'),
    ('en', 'Riley echo check #4752 [en]', 'You said: Riley echo check #4752 [en]'),
    ('hi', 'Riley echo check #4753 [hi]', 'You said: Riley echo check #4753 [hi]'),
    ('fr', 'Riley echo check #4754 [fr]', 'You said: Riley echo check #4754 [fr]'),
    ('es', 'Riley echo check #4755 [es]', 'You said: Riley echo check #4755 [es]'),
]


def test_spec_batch_048() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
