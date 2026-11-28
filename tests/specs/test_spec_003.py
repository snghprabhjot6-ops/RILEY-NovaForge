"""Verification spec batch 003: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (22 - 9) * 3?', 'The answer is 39.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(228 % 18) + 9!', 'The answer is 21.'),
    ('calculate 6 ** 2 + 4', 'The answer is 40.'),
    ('calculate 212 + 17 * 8?', 'The answer is 348.'),
    ('what is (27 - 14) * 3.', 'The answer is 39.'),
    ('calc (219 * 6) / 3!', 'The answer is 438.'),
    ('(233 % 6) + 14', 'The answer is 19.'),
    ('calculate 3 ** 4 + 9?', 'The answer is 90.'),
    ('calculate 217 + 3 * 2.', 'The answer is 223.'),
    ('what is (32 - 6) * 3!', 'The answer is 78.'),
    ('calc (224 * 6) / 3', 'The answer is 448.'),
    ('(238 % 11) + 6?', 'The answer is 13.'),
    ('calculate 8 ** 3 + 14.', 'The answer is 526.'),
    ('calculate 222 + 8 * 7!', 'The answer is 278.'),
    ('what is (37 - 11) * 3', 'The answer is 78.'),
    ('calc (229 * 6) / 3?', 'The answer is 458.'),
    ('(243 % 16) + 11.', 'The answer is 14.'),
    ('calculate 5 ** 2 + 19!', 'The answer is 44.'),
]


def test_spec_batch_003() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
