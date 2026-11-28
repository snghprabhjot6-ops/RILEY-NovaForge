"""Verification spec batch 040: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (36 - 4) * 3?', 'The answer is 96.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(3928 % 12) + 4!', 'The answer is 8.'),
]


def test_spec_batch_040() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
