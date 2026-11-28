"""Verification spec batch 007: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (34 - 6) * 3?', 'The answer is 84.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(628 % 10) + 6!', 'The answer is 14.'),
    ('calculate 6 ** 3 + 4', 'The answer is 220.'),
    ('calculate 612 + 18 * 1?', 'The answer is 630.'),
    ('what is (39 - 11) * 3.', 'The answer is 84.'),
    ('calc (119 * 6) / 3!', 'The answer is 238.'),
    ('(633 % 15) + 11', 'The answer is 14.'),
    ('calculate 3 ** 2 + 9?', 'The answer is 18.'),
    ('calculate 617 + 4 * 6.', 'The answer is 641.'),
    ('what is (44 - 3) * 3!', 'The answer is 123.'),
    ('calc (124 * 6) / 3', 'The answer is 248.'),
    ('(638 % 3) + 3?', 'The answer is 5.'),
    ('calculate 8 ** 4 + 14.', 'The answer is 4110.'),
    ('calculate 622 + 9 * 11!', 'The answer is 721.'),
    ('what is (49 - 8) * 3', 'The answer is 123.'),
    ('calc (129 * 6) / 3?', 'The answer is 258.'),
    ('(643 % 8) + 8.', 'The answer is 11.'),
    ('calculate 5 ** 3 + 19!', 'The answer is 144.'),
    ('calculate 627 + 14 * 5', 'The answer is 697.'),
    ('what is (54 - 13) * 3?', 'The answer is 123.'),
    ('calc (134 * 6) / 3.', 'The answer is 268.'),
    ('(648 % 13) + 13!', 'The answer is 24.'),
    ('calculate 2 ** 2 + 24', 'The answer is 28.'),
    ('calculate 632 + 19 * 10?', 'The answer is 822.'),
    ('what is (59 - 5) * 3.', 'The answer is 162.'),
    ('calc (139 * 6) / 3!', 'The answer is 278.'),
    ('(653 % 18) + 5', 'The answer is 10.'),
    ('calculate 7 ** 4 + 29?', 'The answer is 2430.'),
    ('calculate 637 + 5 * 4.', 'The answer is 657.'),
    ('what is (64 - 10) * 3!', 'The answer is 162.'),
    ('calc (144 * 6) / 3', 'The answer is 288.'),
]


def test_spec_batch_007() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
