"""Verification spec batch 047: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('sa', 'Riley echo check #4601 [sa]', 'You said: Riley echo check #4601 [sa]'),
    ('en', 'Riley echo check #4602 [en]', 'You said: Riley echo check #4602 [en]'),
    ('hi', 'Riley echo check #4603 [hi]', 'You said: Riley echo check #4603 [hi]'),
]


def test_spec_batch_047() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
