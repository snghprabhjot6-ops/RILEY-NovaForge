"""Verification spec batch 022: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (79 - 11) * 3?', 'The answer is 204.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(2128 % 14) + 11!', 'The answer is 11.'),
    ('calculate 2 ** 3 + 4', 'The answer is 12.'),
]


def test_spec_batch_022() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
