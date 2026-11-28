"""Verification spec batch 037: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (27 - 3) * 3?', 'The answer is 72.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(3628 % 18) + 3!', 'The answer is 13.'),
    ('calculate 6 ** 3 + 4', 'The answer is 220.'),
    ('calculate 3612 + 16 * 9?', 'The answer is 3756.'),
    ('what is (32 - 8) * 3.', 'The answer is 72.'),
    ('calc (119 * 6) / 3!', 'The answer is 238.'),
    ('(3633 % 6) + 8', 'The answer is 11.'),
    ('calculate 3 ** 2 + 9?', 'The answer is 18.'),
    ('calculate 3617 + 2 * 3.', 'The answer is 3623.'),
    ('what is (37 - 13) * 3!', 'The answer is 72.'),
    ('calc (124 * 6) / 3', 'The answer is 248.'),
    ('(3638 % 11) + 13?', 'The answer is 21.'),
    ('calculate 8 ** 4 + 14.', 'The answer is 4110.'),
    ('calculate 3622 + 7 * 8!', 'The answer is 3678.'),
    ('what is (42 - 5) * 3', 'The answer is 111.'),
    ('calc (129 * 6) / 3?', 'The answer is 258.'),
    ('(3643 % 16) + 5.', 'The answer is 16.'),
    ('calculate 5 ** 3 + 19!', 'The answer is 144.'),
    ('calculate 3627 + 12 * 2', 'The answer is 3651.'),
    ('what is (47 - 10) * 3?', 'The answer is 111.'),
    ('calc (134 * 6) / 3.', 'The answer is 268.'),
    ('(3648 % 4) + 10!', 'The answer is 10.'),
    ('calculate 2 ** 2 + 24', 'The answer is 28.'),
    ('calculate 3632 + 17 * 7?', 'The answer is 3751.'),
    ('what is (52 - 15) * 3.', 'The answer is 111.'),
    ('calc (139 * 6) / 3!', 'The answer is 278.'),
    ('(3653 % 9) + 15', 'The answer is 23.'),
    ('calculate 7 ** 4 + 29?', 'The answer is 2430.'),
    ('calculate 3637 + 3 * 1.', 'The answer is 3640.'),
    ('what is (57 - 7) * 3!', 'The answer is 150.'),
    ('calc (144 * 6) / 3', 'The answer is 288.'),
    ('(3658 % 14) + 7?', 'The answer is 11.'),
]


def test_spec_batch_037() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
