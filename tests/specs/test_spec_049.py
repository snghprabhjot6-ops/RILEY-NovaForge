"""Verification spec batch 049: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('hi', 'Riley echo check #4801 [hi]', 'You said: Riley echo check #4801 [hi]'),
    ('fr', 'Riley echo check #4802 [fr]', 'You said: Riley echo check #4802 [fr]'),
    ('es', 'Riley echo check #4803 [es]', 'You said: Riley echo check #4803 [es]'),
    ('bn', 'Riley echo check #4804 [bn]', 'You said: Riley echo check #4804 [bn]'),
    ('sa', 'Riley echo check #4805 [sa]', 'You said: Riley echo check #4805 [sa]'),
    ('en', 'Riley echo check #4806 [en]', 'You said: Riley echo check #4806 [en]'),
    ('hi', 'Riley echo check #4807 [hi]', 'You said: Riley echo check #4807 [hi]'),
    ('fr', 'Riley echo check #4808 [fr]', 'You said: Riley echo check #4808 [fr]'),
    ('es', 'Riley echo check #4809 [es]', 'You said: Riley echo check #4809 [es]'),
    ('bn', 'Riley echo check #4810 [bn]', 'You said: Riley echo check #4810 [bn]'),
    ('sa', 'Riley echo check #4811 [sa]', 'You said: Riley echo check #4811 [sa]'),
    ('en', 'Riley echo check #4812 [en]', 'You said: Riley echo check #4812 [en]'),
    ('hi', 'Riley echo check #4813 [hi]', 'You said: Riley echo check #4813 [hi]'),
    ('fr', 'Riley echo check #4814 [fr]', 'You said: Riley echo check #4814 [fr]'),
    ('es', 'Riley echo check #4815 [es]', 'You said: Riley echo check #4815 [es]'),
    ('bn', 'Riley echo check #4816 [bn]', 'You said: Riley echo check #4816 [bn]'),
    ('sa', 'Riley echo check #4817 [sa]', 'You said: Riley echo check #4817 [sa]'),
    ('en', 'Riley echo check #4818 [en]', 'You said: Riley echo check #4818 [en]'),
    ('hi', 'Riley echo check #4819 [hi]', 'You said: Riley echo check #4819 [hi]'),
    ('fr', 'Riley echo check #4820 [fr]', 'You said: Riley echo check #4820 [fr]'),
    ('es', 'Riley echo check #4821 [es]', 'You said: Riley echo check #4821 [es]'),
    ('bn', 'Riley echo check #4822 [bn]', 'You said: Riley echo check #4822 [bn]'),
    ('sa', 'Riley echo check #4823 [sa]', 'You said: Riley echo check #4823 [sa]'),
    ('en', 'Riley echo check #4824 [en]', 'You said: Riley echo check #4824 [en]'),
    ('hi', 'Riley echo check #4825 [hi]', 'You said: Riley echo check #4825 [hi]'),
    ('fr', 'Riley echo check #4826 [fr]', 'You said: Riley echo check #4826 [fr]'),
    ('es', 'Riley echo check #4827 [es]', 'You said: Riley echo check #4827 [es]'),
    ('bn', 'Riley echo check #4828 [bn]', 'You said: Riley echo check #4828 [bn]'),
    ('sa', 'Riley echo check #4829 [sa]', 'You said: Riley echo check #4829 [sa]'),
    ('en', 'Riley echo check #4830 [en]', 'You said: Riley echo check #4830 [en]'),
    ('hi', 'Riley echo check #4831 [hi]', 'You said: Riley echo check #4831 [hi]'),
    ('fr', 'Riley echo check #4832 [fr]', 'You said: Riley echo check #4832 [fr]'),
    ('es', 'Riley echo check #4833 [es]', 'You said: Riley echo check #4833 [es]'),
    ('bn', 'Riley echo check #4834 [bn]', 'You said: Riley echo check #4834 [bn]'),
    ('sa', 'Riley echo check #4835 [sa]', 'You said: Riley echo check #4835 [sa]'),
    ('en', 'Riley echo check #4836 [en]', 'You said: Riley echo check #4836 [en]'),
    ('hi', 'Riley echo check #4837 [hi]', 'You said: Riley echo check #4837 [hi]'),
    ('fr', 'Riley echo check #4838 [fr]', 'You said: Riley echo check #4838 [fr]'),
]


def test_spec_batch_049() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
