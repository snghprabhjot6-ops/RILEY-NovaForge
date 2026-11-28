"""Verification spec batch 033: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (15 - 6) * 3?', 'The answer is 27.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(3228 % 9) + 6!', 'The answer is 12.'),
    ('calculate 6 ** 2 + 4', 'The answer is 40.'),
    ('calculate 3212 + 15 * 5?', 'The answer is 3287.'),
    ('what is (20 - 11) * 3.', 'The answer is 27.'),
    ('calc (219 * 6) / 3!', 'The answer is 438.'),
    ('(3233 % 14) + 11', 'The answer is 24.'),
    ('calculate 3 ** 4 + 9?', 'The answer is 90.'),
    ('calculate 3217 + 20 * 10.', 'The answer is 3417.'),
    ('what is (25 - 3) * 3!', 'The answer is 66.'),
]


def test_spec_batch_033() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
