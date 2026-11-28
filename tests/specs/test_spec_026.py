"""Verification spec batch 026: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (91 - 8) * 3?', 'The answer is 249.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(2528 % 6) + 8!', 'The answer is 10.'),
    ('calculate 2 ** 4 + 4', 'The answer is 20.'),
    ('calculate 2512 + 18 * 9?', 'The answer is 2674.'),
    ('what is (96 - 13) * 3.', 'The answer is 249.'),
    ('calc (19 * 6) / 3!', 'The answer is 38.'),
    ('(2533 % 11) + 13', 'The answer is 16.'),
    ('calculate 7 ** 3 + 9?', 'The answer is 352.'),
    ('calculate 2517 + 4 * 3.', 'The answer is 2529.'),
    ('what is (101 - 5) * 3!', 'The answer is 288.'),
    ('calc (24 * 6) / 3', 'The answer is 48.'),
    ('(2538 % 16) + 5?', 'The answer is 15.'),
    ('calculate 4 ** 2 + 14.', 'The answer is 30.'),
    ('calculate 2522 + 9 * 8!', 'The answer is 2594.'),
    ('what is (106 - 10) * 3', 'The answer is 288.'),
    ('calc (29 * 6) / 3?', 'The answer is 58.'),
    ('(2543 % 4) + 10.', 'The answer is 13.'),
    ('calculate 9 ** 4 + 19!', 'The answer is 6580.'),
    ('calculate 2527 + 14 * 2', 'The answer is 2555.'),
    ('what is (111 - 15) * 3?', 'The answer is 288.'),
    ('calc (34 * 6) / 3.', 'The answer is 68.'),
    ('(2548 % 9) + 15!', 'The answer is 16.'),
    ('calculate 6 ** 3 + 24', 'The answer is 240.'),
    ('calculate 2532 + 19 * 7?', 'The answer is 2665.'),
    ('what is (19 - 7) * 3.', 'The answer is 36.'),
    ('calc (39 * 6) / 3!', 'The answer is 78.'),
    ('(2553 % 14) + 7', 'The answer is 12.'),
    ('calculate 3 ** 2 + 29?', 'The answer is 38.'),
    ('calculate 2537 + 5 * 1.', 'The answer is 2542.'),
    ('what is (24 - 12) * 3!', 'The answer is 36.'),
    ('calc (44 * 6) / 3', 'The answer is 88.'),
    ('(2558 % 2) + 12?', 'The answer is 12.'),
    ('calculate 8 ** 4 + 34.', 'The answer is 4130.'),
    ('calculate 2542 + 10 * 6!', 'The answer is 2602.'),
    ('what is (29 - 4) * 3', 'The answer is 75.'),
    ('calc (49 * 6) / 3?', 'The answer is 98.'),
    ('(2563 % 7) + 4.', 'The answer is 5.'),
    ('calculate 5 ** 3 + 39!', 'The answer is 164.'),
    ('calculate 2547 + 15 * 11', 'The answer is 2712.'),
    ('what is (34 - 9) * 3?', 'The answer is 75.'),
    ('calc (54 * 6) / 3.', 'The answer is 108.'),
    ('(2568 % 12) + 9!', 'The answer is 9.'),
    ('calculate 2 ** 2 + 44', 'The answer is 48.'),
    ('calculate 2552 + 20 * 5?', 'The answer is 2652.'),
    ('what is (39 - 14) * 3.', 'The answer is 75.'),
    ('calc (59 * 6) / 3!', 'The answer is 118.'),
    ('(2573 % 17) + 14', 'The answer is 20.'),
    ('calculate 7 ** 4 + 49?', 'The answer is 2450.'),
    ('calculate 2557 + 6 * 10.', 'The answer is 2617.'),
    ('what is (44 - 6) * 3!', 'The answer is 114.'),
    ('calc (64 * 6) / 3', 'The answer is 128.'),
    ('(2578 % 5) + 6?', 'The answer is 9.'),
    ('calculate 4 ** 3 + 54.', 'The answer is 118.'),
    ('calculate 2562 + 11 * 4!', 'The answer is 2606.'),
    ('what is (49 - 11) * 3', 'The answer is 114.'),
]


def test_spec_batch_026() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
