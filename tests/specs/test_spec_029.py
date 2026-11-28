"""Verification spec batch 029: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (100 - 9) * 3?', 'The answer is 273.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(2828 % 17) + 9!', 'The answer is 15.'),
    ('calculate 6 ** 4 + 4', 'The answer is 1300.'),
    ('calculate 2812 + 14 * 1?', 'The answer is 2826.'),
    ('what is (105 - 14) * 3.', 'The answer is 273.'),
    ('calc (69 * 6) / 3!', 'The answer is 138.'),
    ('(2833 % 5) + 14', 'The answer is 17.'),
    ('calculate 3 ** 3 + 9?', 'The answer is 36.'),
    ('calculate 2817 + 19 * 6.', 'The answer is 2931.'),
    ('what is (110 - 6) * 3!', 'The answer is 312.'),
    ('calc (74 * 6) / 3', 'The answer is 148.'),
    ('(2838 % 10) + 6?', 'The answer is 14.'),
    ('calculate 8 ** 2 + 14.', 'The answer is 78.'),
    ('calculate 2822 + 5 * 11!', 'The answer is 2877.'),
    ('what is (18 - 11) * 3', 'The answer is 21.'),
    ('calc (79 * 6) / 3?', 'The answer is 158.'),
    ('(2843 % 15) + 11.', 'The answer is 19.'),
    ('calculate 5 ** 4 + 19!', 'The answer is 644.'),
]


def test_spec_batch_029() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
