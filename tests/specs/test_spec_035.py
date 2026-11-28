"""Verification spec batch 035: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (21 - 11) * 3?', 'The answer is 30.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(3428 % 5) + 11!', 'The answer is 14.'),
    ('calculate 6 ** 4 + 4', 'The answer is 1300.'),
    ('calculate 3412 + 6 * 7?', 'The answer is 3454.'),
    ('what is (26 - 3) * 3.', 'The answer is 69.'),
    ('calc (169 * 6) / 3!', 'The answer is 338.'),
    ('(3433 % 10) + 3', 'The answer is 6.'),
    ('calculate 3 ** 3 + 9?', 'The answer is 36.'),
    ('calculate 3417 + 11 * 1.', 'The answer is 3428.'),
    ('what is (31 - 8) * 3!', 'The answer is 69.'),
    ('calc (174 * 6) / 3', 'The answer is 348.'),
    ('(3438 % 15) + 8?', 'The answer is 11.'),
    ('calculate 8 ** 2 + 14.', 'The answer is 78.'),
    ('calculate 3422 + 16 * 6!', 'The answer is 3518.'),
    ('what is (36 - 13) * 3', 'The answer is 69.'),
    ('calc (179 * 6) / 3?', 'The answer is 358.'),
    ('(3443 % 3) + 13.', 'The answer is 15.'),
    ('calculate 5 ** 4 + 19!', 'The answer is 644.'),
    ('calculate 3427 + 2 * 11', 'The answer is 3449.'),
    ('what is (41 - 5) * 3?', 'The answer is 108.'),
    ('calc (184 * 6) / 3.', 'The answer is 368.'),
    ('(3448 % 8) + 5!', 'The answer is 5.'),
    ('calculate 2 ** 3 + 24', 'The answer is 32.'),
    ('calculate 3432 + 7 * 5?', 'The answer is 3467.'),
    ('what is (46 - 10) * 3.', 'The answer is 108.'),
    ('calc (189 * 6) / 3!', 'The answer is 378.'),
    ('(3453 % 13) + 10', 'The answer is 18.'),
    ('calculate 7 ** 2 + 29?', 'The answer is 78.'),
    ('calculate 3437 + 12 * 10.', 'The answer is 3557.'),
    ('what is (51 - 15) * 3!', 'The answer is 108.'),
    ('calc (194 * 6) / 3', 'The answer is 388.'),
    ('(3458 % 18) + 15?', 'The answer is 17.'),
    ('calculate 4 ** 4 + 34.', 'The answer is 290.'),
]


def test_spec_batch_035() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
