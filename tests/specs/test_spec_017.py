"""Verification spec batch 017: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (64 - 5) * 3?', 'The answer is 177.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(1628 % 7) + 5!', 'The answer is 9.'),
    ('calculate 6 ** 4 + 4', 'The answer is 1300.'),
    ('calculate 1612 + 11 * 11?', 'The answer is 1733.'),
    ('what is (69 - 10) * 3.', 'The answer is 177.'),
]


def test_spec_batch_017() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
