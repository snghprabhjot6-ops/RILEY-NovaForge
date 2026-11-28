"""Verification spec batch 011: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (46 - 3) * 3?', 'The answer is 129.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(1028 % 2) + 3!', 'The answer is 3.'),
]


def test_spec_batch_011() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
