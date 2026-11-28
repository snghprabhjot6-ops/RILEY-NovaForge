"""Verification spec batch 001: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (16 - 4) * 3?', 'The answer is 36.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(28 % 5) + 4!', 'The answer is 7.'),
    ('calculate 6 ** 3 + 4', 'The answer is 220.'),
    ('calculate 12 + 7 * 6?', 'The answer is 54.'),
    ('what is (21 - 9) * 3.', 'The answer is 36.'),
    ('calc (19 * 6) / 3!', 'The answer is 38.'),
    ('(33 % 10) + 9', 'The answer is 12.'),
    ('calculate 3 ** 2 + 9?', 'The answer is 18.'),
    ('calculate 17 + 12 * 11.', 'The answer is 149.'),
]


def test_spec_batch_001() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
