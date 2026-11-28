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
    ('calc (74 * 6) / 3', 'The answer is 148.'),
    ('(3338 % 17) + 12?', 'The answer is 18.'),
    ('calculate 4 ** 4 + 14.', 'The answer is 270.'),
    ('calculate 3322 + 11 * 5!', 'The answer is 3377.'),
    ('what is (33 - 4) * 3', 'The answer is 87.'),
    ('calc (79 * 6) / 3?', 'The answer is 158.'),
    ('(3343 % 5) + 4.', 'The answer is 7.'),
    ('calculate 9 ** 3 + 19!', 'The answer is 748.'),
    ('calculate 3327 + 16 * 10', 'The answer is 3487.'),
    ('what is (38 - 9) * 3?', 'The answer is 87.'),
    ('calc (84 * 6) / 3.', 'The answer is 168.'),
    ('(3348 % 10) + 9!', 'The answer is 17.'),
    ('calculate 6 ** 2 + 24', 'The answer is 60.'),
    ('calculate 3332 + 2 * 4?', 'The answer is 3340.'),
    ('what is (43 - 14) * 3.', 'The answer is 87.'),
    ('calc (89 * 6) / 3!', 'The answer is 178.'),
    ('(3353 % 15) + 14', 'The answer is 22.'),
    ('calculate 3 ** 4 + 29?', 'The answer is 110.'),
    ('calculate 3337 + 7 * 9.', 'The answer is 3400.'),
    ('what is (48 - 6) * 3!', 'The answer is 126.'),
    ('calc (94 * 6) / 3', 'The answer is 188.'),
    ('(3358 % 3) + 6?', 'The answer is 7.'),
    ('calculate 8 ** 3 + 34.', 'The answer is 546.'),
    ('calculate 3342 + 12 * 3!', 'The answer is 3378.'),
    ('what is (53 - 11) * 3', 'The answer is 126.'),
    ('calc (99 * 6) / 3?', 'The answer is 198.'),
    ('(3363 % 8) + 11.', 'The answer is 14.'),
    ('calculate 5 ** 2 + 39!', 'The answer is 64.'),
    ('calculate 3347 + 17 * 8', 'The answer is 3483.'),
    ('what is (58 - 3) * 3?', 'The answer is 165.'),
    ('calc (104 * 6) / 3.', 'The answer is 208.'),
    ('(3368 % 13) + 3!', 'The answer is 4.'),
    ('calculate 2 ** 4 + 44', 'The answer is 60.'),
    ('calculate 3352 + 3 * 2?', 'The answer is 3358.'),
    ('what is (63 - 8) * 3.', 'The answer is 165.'),
    ('calc (109 * 6) / 3!', 'The answer is 218.'),
    ('(3373 % 18) + 8', 'The answer is 15.'),
    ('calculate 7 ** 3 + 49?', 'The answer is 392.'),
    ('calculate 3357 + 8 * 7.', 'The answer is 3413.'),
]


def test_spec_batch_034() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
