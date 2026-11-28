"""Verification spec batch 027: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (94 - 4) * 3?', 'The answer is 270.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(2628 % 4) + 4!', 'The answer is 4.'),
    ('calculate 6 ** 2 + 4', 'The answer is 40.'),
    ('calculate 2612 + 4 * 10?', 'The answer is 2652.'),
    ('what is (99 - 9) * 3.', 'The answer is 270.'),
    ('calc (119 * 6) / 3!', 'The answer is 238.'),
    ('(2633 % 9) + 9', 'The answer is 14.'),
    ('calculate 3 ** 4 + 9?', 'The answer is 90.'),
    ('calculate 2617 + 9 * 4.', 'The answer is 2653.'),
    ('what is (104 - 14) * 3!', 'The answer is 270.'),
    ('calc (124 * 6) / 3', 'The answer is 248.'),
    ('(2638 % 14) + 14?', 'The answer is 20.'),
    ('calculate 8 ** 3 + 14.', 'The answer is 526.'),
    ('calculate 2622 + 14 * 9!', 'The answer is 2748.'),
    ('what is (109 - 6) * 3', 'The answer is 309.'),
    ('calc (129 * 6) / 3?', 'The answer is 258.'),
    ('(2643 % 2) + 6.', 'The answer is 7.'),
    ('calculate 5 ** 2 + 19!', 'The answer is 44.'),
    ('calculate 2627 + 19 * 3', 'The answer is 2684.'),
    ('what is (17 - 11) * 3?', 'The answer is 18.'),
    ('calc (134 * 6) / 3.', 'The answer is 268.'),
    ('(2648 % 7) + 11!', 'The answer is 13.'),
    ('calculate 2 ** 4 + 24', 'The answer is 40.'),
    ('calculate 2632 + 5 * 8?', 'The answer is 2672.'),
    ('what is (22 - 3) * 3.', 'The answer is 57.'),
    ('calc (139 * 6) / 3!', 'The answer is 278.'),
    ('(2653 % 12) + 3', 'The answer is 4.'),
]


def test_spec_batch_027() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
