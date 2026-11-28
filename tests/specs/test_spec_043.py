"""Verification spec batch 043: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (45 - 5) * 3?', 'The answer is 120.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(4228 % 6) + 5!', 'The answer is 9.'),
    ('calculate 6 ** 3 + 4', 'The answer is 220.'),
    ('calculate 4212 + 8 * 4?', 'The answer is 4244.'),
    ('what is (50 - 10) * 3.', 'The answer is 120.'),
    ('calc (219 * 6) / 3!', 'The answer is 438.'),
    ('(4233 % 11) + 10', 'The answer is 19.'),
    ('calculate 3 ** 2 + 9?', 'The answer is 18.'),
    ('calculate 4217 + 13 * 9.', 'The answer is 4334.'),
    ('what is (55 - 15) * 3!', 'The answer is 120.'),
    ('calc (224 * 6) / 3', 'The answer is 448.'),
    ('(4238 % 16) + 15?', 'The answer is 29.'),
    ('calculate 8 ** 4 + 14.', 'The answer is 4110.'),
    ('calculate 4222 + 18 * 3!', 'The answer is 4276.'),
    ('what is (60 - 7) * 3', 'The answer is 159.'),
    ('calc (229 * 6) / 3?', 'The answer is 458.'),
    ('(4243 % 4) + 7.', 'The answer is 10.'),
    ('calculate 5 ** 3 + 19!', 'The answer is 144.'),
    ('calculate 4227 + 4 * 8', 'The answer is 4259.'),
    ('what is (65 - 12) * 3?', 'The answer is 159.'),
    ('calc (234 * 6) / 3.', 'The answer is 468.'),
    ('(4248 % 9) + 12!', 'The answer is 12.'),
]


def test_spec_batch_043() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
