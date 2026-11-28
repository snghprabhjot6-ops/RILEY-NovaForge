"""Verification spec batch 017: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (64 - 5) * 3?', 'The answer is 177.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(1628 % 7) + 5!', 'The answer is 9.'),
    ('calculate 6 ** 4 + 4', 'The answer is 1300.'),
    ('calculate 1612 + 11 * 11?', 'The answer is 1733.'),
    ('what is (69 - 10) * 3.', 'The answer is 177.'),
    ('calc (119 * 6) / 3!', 'The answer is 238.'),
    ('(1633 % 12) + 10', 'The answer is 11.'),
    ('calculate 3 ** 3 + 9?', 'The answer is 36.'),
    ('calculate 1617 + 16 * 5.', 'The answer is 1697.'),
    ('what is (74 - 15) * 3!', 'The answer is 177.'),
    ('calc (124 * 6) / 3', 'The answer is 248.'),
    ('(1638 % 17) + 15?', 'The answer is 21.'),
    ('calculate 8 ** 2 + 14.', 'The answer is 78.'),
    ('calculate 1622 + 2 * 10!', 'The answer is 1642.'),
    ('what is (79 - 7) * 3', 'The answer is 216.'),
    ('calc (129 * 6) / 3?', 'The answer is 258.'),
    ('(1643 % 5) + 7.', 'The answer is 10.'),
    ('calculate 5 ** 4 + 19!', 'The answer is 644.'),
    ('calculate 1627 + 7 * 4', 'The answer is 1655.'),
    ('what is (84 - 12) * 3?', 'The answer is 216.'),
    ('calc (134 * 6) / 3.', 'The answer is 268.'),
    ('(1648 % 10) + 12!', 'The answer is 20.'),
    ('calculate 2 ** 3 + 24', 'The answer is 32.'),
    ('calculate 1632 + 12 * 9?', 'The answer is 1740.'),
    ('what is (89 - 4) * 3.', 'The answer is 255.'),
    ('calc (139 * 6) / 3!', 'The answer is 278.'),
    ('(1653 % 15) + 4', 'The answer is 7.'),
    ('calculate 7 ** 2 + 29?', 'The answer is 78.'),
    ('calculate 1637 + 17 * 3.', 'The answer is 1688.'),
    ('what is (94 - 9) * 3!', 'The answer is 255.'),
    ('calc (144 * 6) / 3', 'The answer is 288.'),
    ('(1658 % 3) + 9?', 'The answer is 11.'),
    ('calculate 4 ** 4 + 34.', 'The answer is 290.'),
    ('calculate 1642 + 3 * 8!', 'The answer is 1666.'),
    ('what is (99 - 14) * 3', 'The answer is 255.'),
    ('calc (149 * 6) / 3?', 'The answer is 298.'),
    ('(1663 % 8) + 14.', 'The answer is 21.'),
    ('calculate 9 ** 3 + 39!', 'The answer is 768.'),
    ('calculate 1647 + 8 * 2', 'The answer is 1663.'),
    ('what is (104 - 6) * 3?', 'The answer is 294.'),
    ('calc (154 * 6) / 3.', 'The answer is 308.'),
    ('(1668 % 13) + 6!', 'The answer is 10.'),
    ('calculate 6 ** 2 + 44', 'The answer is 80.'),
    ('calculate 1652 + 13 * 7?', 'The answer is 1743.'),
    ('what is (109 - 11) * 3.', 'The answer is 294.'),
    ('calc (159 * 6) / 3!', 'The answer is 318.'),
    ('(1673 % 18) + 11', 'The answer is 28.'),
    ('calculate 3 ** 4 + 49?', 'The answer is 130.'),
    ('calculate 1657 + 18 * 1.', 'The answer is 1675.'),
    ('what is (17 - 3) * 3!', 'The answer is 42.'),
    ('calc (164 * 6) / 3', 'The answer is 328.'),
    ('(1678 % 6) + 3?', 'The answer is 7.'),
    ('calculate 8 ** 3 + 54.', 'The answer is 566.'),
    ('calculate 1662 + 4 * 6!', 'The answer is 1686.'),
]


def test_spec_batch_017() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
