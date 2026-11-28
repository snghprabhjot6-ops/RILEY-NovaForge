"""Verification spec batch 044: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (48 - 14) * 3?', 'The answer is 102.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(4328 % 4) + 14!', 'The answer is 14.'),
    ('calculate 2 ** 4 + 4', 'The answer is 20.'),
    ('calculate 4312 + 13 * 5?', 'The answer is 4377.'),
    ('what is (53 - 6) * 3.', 'The answer is 141.'),
    ('calc (69 * 6) / 3!', 'The answer is 138.'),
    ('(4333 % 9) + 6', 'The answer is 10.'),
    ('calculate 7 ** 3 + 9?', 'The answer is 352.'),
    ('calculate 4317 + 18 * 10.', 'The answer is 4497.'),
    ('what is (58 - 11) * 3!', 'The answer is 141.'),
    ('calc (74 * 6) / 3', 'The answer is 148.'),
    ('(4338 % 14) + 11?', 'The answer is 23.'),
]


def test_spec_batch_044() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
