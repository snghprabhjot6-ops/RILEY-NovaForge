"""Verification spec batch 014: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (55 - 4) * 3?', 'The answer is 153.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(1328 % 13) + 4!', 'The answer is 6.'),
    ('calculate 2 ** 4 + 4', 'The answer is 20.'),
    ('calculate 1312 + 15 * 8?', 'The answer is 1432.'),
    ('what is (60 - 9) * 3.', 'The answer is 153.'),
    ('calc (69 * 6) / 3!', 'The answer is 138.'),
    ('(1333 % 18) + 9', 'The answer is 10.'),
    ('calculate 7 ** 3 + 9?', 'The answer is 352.'),
    ('calculate 1317 + 20 * 2.', 'The answer is 1357.'),
    ('what is (65 - 14) * 3!', 'The answer is 153.'),
    ('calc (74 * 6) / 3', 'The answer is 148.'),
    ('(1338 % 6) + 14?', 'The answer is 14.'),
    ('calculate 4 ** 2 + 14.', 'The answer is 30.'),
]


def test_spec_batch_014() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
