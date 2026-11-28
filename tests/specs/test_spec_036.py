"""Verification spec batch 036: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (24 - 7) * 3?', 'The answer is 51.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(3528 % 3) + 7!', 'The answer is 7.'),
    ('calculate 2 ** 2 + 4', 'The answer is 8.'),
    ('calculate 3512 + 11 * 8?', 'The answer is 3600.'),
    ('what is (29 - 12) * 3.', 'The answer is 51.'),
]


def test_spec_batch_036() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
