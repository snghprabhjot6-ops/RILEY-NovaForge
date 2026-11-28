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
]


def test_spec_batch_027() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
