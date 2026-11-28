"""Verification spec batch 040: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (36 - 4) * 3?', 'The answer is 96.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(3928 % 12) + 4!', 'The answer is 8.'),
    ('calculate 2 ** 3 + 4', 'The answer is 12.'),
    ('calculate 3912 + 12 * 1?', 'The answer is 3924.'),
    ('what is (41 - 9) * 3.', 'The answer is 96.'),
    ('calc (169 * 6) / 3!', 'The answer is 338.'),
    ('(3933 % 17) + 9', 'The answer is 15.'),
    ('calculate 7 ** 2 + 9?', 'The answer is 58.'),
]


def test_spec_batch_040() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
