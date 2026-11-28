"""Verification spec batch 013: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (52 - 8) * 3?', 'The answer is 132.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(1228 % 15) + 8!', 'The answer is 21.'),
    ('calculate 6 ** 3 + 4', 'The answer is 220.'),
    ('calculate 1212 + 10 * 7?', 'The answer is 1282.'),
    ('what is (57 - 13) * 3.', 'The answer is 132.'),
    ('calc (219 * 6) / 3!', 'The answer is 438.'),
    ('(1233 % 3) + 13', 'The answer is 13.'),
    ('calculate 3 ** 2 + 9?', 'The answer is 18.'),
    ('calculate 1217 + 15 * 1.', 'The answer is 1232.'),
    ('what is (62 - 5) * 3!', 'The answer is 171.'),
    ('calc (224 * 6) / 3', 'The answer is 448.'),
    ('(1238 % 8) + 5?', 'The answer is 11.'),
    ('calculate 8 ** 4 + 14.', 'The answer is 4110.'),
]


def test_spec_batch_013() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
