"""Verification spec batch 049: multilingual EchoBackend round-trips."""
from riley.backends.echo import EchoBackend
from riley.models import Message

_BACKEND = EchoBackend()

CASES: list[tuple[str, str, str]] = [
    ('hi', 'Riley echo check #4801 [hi]', 'You said: Riley echo check #4801 [hi]'),
]


def test_spec_batch_049() -> None:
    for lang, prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt, lang)], lang) == expected
