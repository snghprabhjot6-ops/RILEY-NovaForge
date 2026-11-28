"""Verification spec batch 020: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (73 - 6) * 3?', 'The answer is 201.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(1928 % 18) + 6!', 'The answer is 8.'),
]


def test_spec_batch_020() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
