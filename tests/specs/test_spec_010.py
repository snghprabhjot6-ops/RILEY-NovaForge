"""Verification spec batch 010: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (43 - 7) * 3?', 'The answer is 108.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(928 % 4) + 7!', 'The answer is 7.'),
    ('calculate 2 ** 3 + 4', 'The answer is 12.'),
]


def test_spec_batch_010() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
