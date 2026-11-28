"""Verification spec batch 035: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (21 - 11) * 3?', 'The answer is 30.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(3428 % 5) + 11!', 'The answer is 14.'),
    ('calculate 6 ** 4 + 4', 'The answer is 1300.'),
    ('calculate 3412 + 6 * 7?', 'The answer is 3454.'),
]


def test_spec_batch_035() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
