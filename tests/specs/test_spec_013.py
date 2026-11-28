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
    ('calculate 1222 + 20 * 6!', 'The answer is 1342.'),
    ('what is (67 - 10) * 3', 'The answer is 171.'),
    ('calc (229 * 6) / 3?', 'The answer is 458.'),
    ('(1243 % 13) + 10.', 'The answer is 18.'),
    ('calculate 5 ** 3 + 19!', 'The answer is 144.'),
    ('calculate 1227 + 6 * 11', 'The answer is 1293.'),
    ('what is (72 - 15) * 3?', 'The answer is 171.'),
    ('calc (234 * 6) / 3.', 'The answer is 468.'),
    ('(1248 % 18) + 15!', 'The answer is 21.'),
    ('calculate 2 ** 2 + 24', 'The answer is 28.'),
    ('calculate 1232 + 11 * 5?', 'The answer is 1287.'),
    ('what is (77 - 7) * 3.', 'The answer is 210.'),
]


def test_spec_batch_013() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
