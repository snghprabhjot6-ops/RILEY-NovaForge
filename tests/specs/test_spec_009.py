"""Verification spec batch 009: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (40 - 11) * 3?', 'The answer is 87.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(828 % 6) + 11!', 'The answer is 11.'),
    ('calculate 6 ** 2 + 4', 'The answer is 40.'),
]


def test_spec_batch_009() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
