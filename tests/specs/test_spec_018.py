"""Verification spec batch 018: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (67 - 14) * 3?', 'The answer is 159.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(1728 % 5) + 14!', 'The answer is 17.'),
    ('calculate 2 ** 2 + 4', 'The answer is 8.'),
    ('calculate 1712 + 16 * 1?', 'The answer is 1728.'),
    ('what is (72 - 6) * 3.', 'The answer is 198.'),
    ('calc (219 * 6) / 3!', 'The answer is 438.'),
    ('(1733 % 10) + 6', 'The answer is 9.'),
    ('calculate 7 ** 4 + 9?', 'The answer is 2410.'),
    ('calculate 1717 + 2 * 6.', 'The answer is 1729.'),
    ('what is (77 - 11) * 3!', 'The answer is 198.'),
    ('calc (224 * 6) / 3', 'The answer is 448.'),
    ('(1738 % 15) + 11?', 'The answer is 24.'),
    ('calculate 4 ** 3 + 14.', 'The answer is 78.'),
    ('calculate 1722 + 7 * 11!', 'The answer is 1799.'),
    ('what is (82 - 3) * 3', 'The answer is 237.'),
    ('calc (229 * 6) / 3?', 'The answer is 458.'),
    ('(1743 % 3) + 3.', 'The answer is 3.'),
    ('calculate 9 ** 2 + 19!', 'The answer is 100.'),
    ('calculate 1727 + 12 * 5', 'The answer is 1787.'),
    ('what is (87 - 8) * 3?', 'The answer is 237.'),
    ('calc (234 * 6) / 3.', 'The answer is 468.'),
    ('(1748 % 8) + 8!', 'The answer is 12.'),
    ('calculate 6 ** 4 + 24', 'The answer is 1320.'),
    ('calculate 1732 + 17 * 10?', 'The answer is 1902.'),
    ('what is (92 - 13) * 3.', 'The answer is 237.'),
    ('calc (239 * 6) / 3!', 'The answer is 478.'),
    ('(1753 % 13) + 13', 'The answer is 24.'),
    ('calculate 3 ** 3 + 29?', 'The answer is 56.'),
]


def test_spec_batch_018() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
