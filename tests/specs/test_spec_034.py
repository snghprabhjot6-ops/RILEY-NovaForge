"""Verification spec batch 034: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (18 - 15) * 3?', 'The answer is 9.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(3328 % 7) + 15!', 'The answer is 18.'),
    ('calculate 2 ** 3 + 4', 'The answer is 12.'),
    ('calculate 3312 + 20 * 6?', 'The answer is 3432.'),
]


def test_spec_batch_034() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
