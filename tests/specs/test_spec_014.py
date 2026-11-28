"""Verification spec batch 014: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (55 - 4) * 3?', 'The answer is 153.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(1328 % 13) + 4!', 'The answer is 6.'),
]


def test_spec_batch_014() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
