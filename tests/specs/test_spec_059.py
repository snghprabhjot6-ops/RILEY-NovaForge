"""Verification spec batch 059: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('sa', 'Riley echo check #5801 [sa]', 'You said: Riley echo check #5801 [sa]'),
    ('en', 'Riley echo check #5802 [en]', 'You said: Riley echo check #5802 [en]'),
    ('hi', 'Riley echo check #5803 [hi]', 'You said: Riley echo check #5803 [hi]'),
    ('fr', 'Riley echo check #5804 [fr]', 'You said: Riley echo check #5804 [fr]'),
    ('es', 'Riley echo check #5805 [es]', 'You said: Riley echo check #5805 [es]'),
    ('bn', 'Riley echo check #5806 [bn]', 'You said: Riley echo check #5806 [bn]'),
    ('sa', 'Riley echo check #5807 [sa]', 'You said: Riley echo check #5807 [sa]'),
    ('en', 'Riley echo check #5808 [en]', 'You said: Riley echo check #5808 [en]'),
    ('hi', 'Riley echo check #5809 [hi]', 'You said: Riley echo check #5809 [hi]'),
    ('fr', 'Riley echo check #5810 [fr]', 'You said: Riley echo check #5810 [fr]'),
    ('es', 'Riley echo check #5811 [es]', 'You said: Riley echo check #5811 [es]'),
    ('bn', 'Riley echo check #5812 [bn]', 'You said: Riley echo check #5812 [bn]'),
    ('sa', 'Riley echo check #5813 [sa]', 'You said: Riley echo check #5813 [sa]'),
    ('en', 'Riley echo check #5814 [en]', 'You said: Riley echo check #5814 [en]'),
    ('hi', 'Riley echo check #5815 [hi]', 'You said: Riley echo check #5815 [hi]'),
    ('fr', 'Riley echo check #5816 [fr]', 'You said: Riley echo check #5816 [fr]'),
    ('es', 'Riley echo check #5817 [es]', 'You said: Riley echo check #5817 [es]'),
    ('bn', 'Riley echo check #5818 [bn]', 'You said: Riley echo check #5818 [bn]'),
    ('sa', 'Riley echo check #5819 [sa]', 'You said: Riley echo check #5819 [sa]'),
    ('en', 'Riley echo check #5820 [en]', 'You said: Riley echo check #5820 [en]'),
    ('hi', 'Riley echo check #5821 [hi]', 'You said: Riley echo check #5821 [hi]'),
    ('fr', 'Riley echo check #5822 [fr]', 'You said: Riley echo check #5822 [fr]'),
    ('es', 'Riley echo check #5823 [es]', 'You said: Riley echo check #5823 [es]'),
    ('bn', 'Riley echo check #5824 [bn]', 'You said: Riley echo check #5824 [bn]'),
    ('sa', 'Riley echo check #5825 [sa]', 'You said: Riley echo check #5825 [sa]'),
    ('en', 'Riley echo check #5826 [en]', 'You said: Riley echo check #5826 [en]'),
    ('hi', 'Riley echo check #5827 [hi]', 'You said: Riley echo check #5827 [hi]'),
]


def test_spec_batch_059() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
