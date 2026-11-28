"""Verification spec batch 058: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('hi', 'Riley echo check #5701 [hi]', 'You said: Riley echo check #5701 [hi]'),
    ('fr', 'Riley echo check #5702 [fr]', 'You said: Riley echo check #5702 [fr]'),
    ('es', 'Riley echo check #5703 [es]', 'You said: Riley echo check #5703 [es]'),
    ('bn', 'Riley echo check #5704 [bn]', 'You said: Riley echo check #5704 [bn]'),
    ('sa', 'Riley echo check #5705 [sa]', 'You said: Riley echo check #5705 [sa]'),
    ('en', 'Riley echo check #5706 [en]', 'You said: Riley echo check #5706 [en]'),
    ('hi', 'Riley echo check #5707 [hi]', 'You said: Riley echo check #5707 [hi]'),
    ('fr', 'Riley echo check #5708 [fr]', 'You said: Riley echo check #5708 [fr]'),
    ('es', 'Riley echo check #5709 [es]', 'You said: Riley echo check #5709 [es]'),
    ('bn', 'Riley echo check #5710 [bn]', 'You said: Riley echo check #5710 [bn]'),
    ('sa', 'Riley echo check #5711 [sa]', 'You said: Riley echo check #5711 [sa]'),
    ('en', 'Riley echo check #5712 [en]', 'You said: Riley echo check #5712 [en]'),
    ('hi', 'Riley echo check #5713 [hi]', 'You said: Riley echo check #5713 [hi]'),
    ('fr', 'Riley echo check #5714 [fr]', 'You said: Riley echo check #5714 [fr]'),
    ('es', 'Riley echo check #5715 [es]', 'You said: Riley echo check #5715 [es]'),
    ('bn', 'Riley echo check #5716 [bn]', 'You said: Riley echo check #5716 [bn]'),
    ('sa', 'Riley echo check #5717 [sa]', 'You said: Riley echo check #5717 [sa]'),
    ('en', 'Riley echo check #5718 [en]', 'You said: Riley echo check #5718 [en]'),
    ('hi', 'Riley echo check #5719 [hi]', 'You said: Riley echo check #5719 [hi]'),
    ('fr', 'Riley echo check #5720 [fr]', 'You said: Riley echo check #5720 [fr]'),
    ('es', 'Riley echo check #5721 [es]', 'You said: Riley echo check #5721 [es]'),
    ('bn', 'Riley echo check #5722 [bn]', 'You said: Riley echo check #5722 [bn]'),
    ('sa', 'Riley echo check #5723 [sa]', 'You said: Riley echo check #5723 [sa]'),
    ('en', 'Riley echo check #5724 [en]', 'You said: Riley echo check #5724 [en]'),
    ('hi', 'Riley echo check #5725 [hi]', 'You said: Riley echo check #5725 [hi]'),
    ('fr', 'Riley echo check #5726 [fr]', 'You said: Riley echo check #5726 [fr]'),
    ('es', 'Riley echo check #5727 [es]', 'You said: Riley echo check #5727 [es]'),
    ('bn', 'Riley echo check #5728 [bn]', 'You said: Riley echo check #5728 [bn]'),
    ('sa', 'Riley echo check #5729 [sa]', 'You said: Riley echo check #5729 [sa]'),
    ('en', 'Riley echo check #5730 [en]', 'You said: Riley echo check #5730 [en]'),
    ('hi', 'Riley echo check #5731 [hi]', 'You said: Riley echo check #5731 [hi]'),
    ('fr', 'Riley echo check #5732 [fr]', 'You said: Riley echo check #5732 [fr]'),
    ('es', 'Riley echo check #5733 [es]', 'You said: Riley echo check #5733 [es]'),
    ('bn', 'Riley echo check #5734 [bn]', 'You said: Riley echo check #5734 [bn]'),
    ('sa', 'Riley echo check #5735 [sa]', 'You said: Riley echo check #5735 [sa]'),
    ('en', 'Riley echo check #5736 [en]', 'You said: Riley echo check #5736 [en]'),
    ('hi', 'Riley echo check #5737 [hi]', 'You said: Riley echo check #5737 [hi]'),
    ('fr', 'Riley echo check #5738 [fr]', 'You said: Riley echo check #5738 [fr]'),
    ('es', 'Riley echo check #5739 [es]', 'You said: Riley echo check #5739 [es]'),
]


def test_spec_batch_058() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
