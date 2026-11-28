"""Verification spec batch 055: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('hi', 'Riley echo check #5401 [hi]', 'You said: Riley echo check #5401 [hi]'),
]


def test_spec_batch_055() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
