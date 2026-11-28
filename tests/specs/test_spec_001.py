"""Verification spec batch 001: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (16 - 4) * 3?', 'The answer is 36.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(28 % 5) + 4!', 'The answer is 7.'),
    ('calculate 6 ** 3 + 4', 'The answer is 220.'),
    ('calculate 12 + 7 * 6?', 'The answer is 54.'),
    ('what is (21 - 9) * 3.', 'The answer is 36.'),
    ('calc (19 * 6) / 3!', 'The answer is 38.'),
    ('(33 % 10) + 9', 'The answer is 12.'),
    ('calculate 3 ** 2 + 9?', 'The answer is 18.'),
    ('calculate 17 + 12 * 11.', 'The answer is 149.'),
    ('what is (26 - 14) * 3!', 'The answer is 36.'),
    ('calc (24 * 6) / 3', 'The answer is 48.'),
    ('(38 % 15) + 14?', 'The answer is 22.'),
    ('calculate 8 ** 4 + 14.', 'The answer is 4110.'),
    ('calculate 22 + 17 * 5!', 'The answer is 107.'),
    ('what is (31 - 6) * 3', 'The answer is 75.'),
    ('calc (29 * 6) / 3?', 'The answer is 58.'),
    ('(43 % 3) + 6.', 'The answer is 7.'),
    ('calculate 5 ** 3 + 19!', 'The answer is 144.'),
    ('calculate 27 + 3 * 10', 'The answer is 57.'),
    ('what is (36 - 11) * 3?', 'The answer is 75.'),
    ('calc (34 * 6) / 3.', 'The answer is 68.'),
    ('(48 % 8) + 11!', 'The answer is 11.'),
    ('calculate 2 ** 2 + 24', 'The answer is 28.'),
    ('calculate 32 + 8 * 4?', 'The answer is 64.'),
    ('what is (41 - 3) * 3.', 'The answer is 114.'),
    ('calc (39 * 6) / 3!', 'The answer is 78.'),
    ('(53 % 13) + 3', 'The answer is 4.'),
    ('calculate 7 ** 4 + 29?', 'The answer is 2430.'),
    ('calculate 37 + 13 * 9.', 'The answer is 154.'),
    ('what is (46 - 8) * 3!', 'The answer is 114.'),
    ('calc (44 * 6) / 3', 'The answer is 88.'),
    ('(58 % 18) + 8?', 'The answer is 12.'),
    ('calculate 4 ** 3 + 34.', 'The answer is 98.'),
    ('calculate 42 + 18 * 3!', 'The answer is 96.'),
    ('what is (51 - 13) * 3', 'The answer is 114.'),
    ('calc (49 * 6) / 3?', 'The answer is 98.'),
    ('(63 % 6) + 13.', 'The answer is 16.'),
    ('calculate 9 ** 2 + 39!', 'The answer is 120.'),
    ('calculate 47 + 4 * 8', 'The answer is 79.'),
    ('what is (56 - 5) * 3?', 'The answer is 153.'),
    ('calc (54 * 6) / 3.', 'The answer is 108.'),
    ('(68 % 11) + 5!', 'The answer is 7.'),
    ('calculate 6 ** 4 + 44', 'The answer is 1340.'),
    ('calculate 52 + 9 * 2?', 'The answer is 70.'),
    ('what is (61 - 10) * 3.', 'The answer is 153.'),
    ('calc (59 * 6) / 3!', 'The answer is 118.'),
    ('(73 % 16) + 10', 'The answer is 19.'),
    ('calculate 3 ** 3 + 49?', 'The answer is 76.'),
    ('calculate 57 + 14 * 7.', 'The answer is 155.'),
    ('what is (66 - 15) * 3!', 'The answer is 153.'),
    ('calc (64 * 6) / 3', 'The answer is 128.'),
    ('(78 % 4) + 15?', 'The answer is 17.'),
    ('calculate 8 ** 2 + 54.', 'The answer is 118.'),
    ('calculate 62 + 19 * 1!', 'The answer is 81.'),
    ('what is (71 - 7) * 3', 'The answer is 192.'),
]


def test_spec_batch_001() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
