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
    ('calculate 1322 + 6 * 7!', 'The answer is 1364.'),
    ('what is (70 - 6) * 3', 'The answer is 192.'),
    ('calc (79 * 6) / 3?', 'The answer is 158.'),
    ('(1343 % 11) + 6.', 'The answer is 7.'),
    ('calculate 9 ** 4 + 19!', 'The answer is 6580.'),
    ('calculate 1327 + 11 * 1', 'The answer is 1338.'),
    ('what is (75 - 11) * 3?', 'The answer is 192.'),
    ('calc (84 * 6) / 3.', 'The answer is 168.'),
    ('(1348 % 16) + 11!', 'The answer is 15.'),
    ('calculate 6 ** 3 + 24', 'The answer is 240.'),
    ('calculate 1332 + 16 * 6?', 'The answer is 1428.'),
    ('what is (80 - 3) * 3.', 'The answer is 231.'),
    ('calc (89 * 6) / 3!', 'The answer is 178.'),
    ('(1353 % 4) + 3', 'The answer is 4.'),
    ('calculate 3 ** 2 + 29?', 'The answer is 38.'),
    ('calculate 1337 + 2 * 11.', 'The answer is 1359.'),
    ('what is (85 - 8) * 3!', 'The answer is 231.'),
    ('calc (94 * 6) / 3', 'The answer is 188.'),
    ('(1358 % 9) + 8?', 'The answer is 16.'),
]


def test_spec_batch_014() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
