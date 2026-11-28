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
    ('what is (23 - 7) * 3.', 'The answer is 48.'),
    ('calc (69 * 6) / 3!', 'The answer is 138.'),
    ('(3333 % 12) + 7', 'The answer is 16.'),
    ('calculate 7 ** 2 + 9?', 'The answer is 58.'),
    ('calculate 3317 + 6 * 11.', 'The answer is 3383.'),
    ('what is (28 - 12) * 3!', 'The answer is 48.'),
]


def test_spec_batch_034() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
