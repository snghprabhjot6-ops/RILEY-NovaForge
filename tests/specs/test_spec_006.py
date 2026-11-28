"""Verification spec batch 006: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (31 - 10) * 3?', 'The answer is 63.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(528 % 12) + 10!', 'The answer is 10.'),
    ('calculate 2 ** 2 + 4', 'The answer is 8.'),
]


def test_spec_batch_006() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
