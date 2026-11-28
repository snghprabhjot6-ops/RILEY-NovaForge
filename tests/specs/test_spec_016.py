"""Verification spec batch 016: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (61 - 9) * 3?', 'The answer is 156.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(1528 % 9) + 9!', 'The answer is 16.'),
    ('calculate 2 ** 3 + 4', 'The answer is 12.'),
    ('calculate 1512 + 6 * 10?', 'The answer is 1572.'),
    ('what is (66 - 14) * 3.', 'The answer is 156.'),
    ('calc (19 * 6) / 3!', 'The answer is 38.'),
    ('(1533 % 14) + 14', 'The answer is 21.'),
    ('calculate 7 ** 2 + 9?', 'The answer is 58.'),
    ('calculate 1517 + 11 * 4.', 'The answer is 1561.'),
    ('what is (71 - 6) * 3!', 'The answer is 195.'),
    ('calc (24 * 6) / 3', 'The answer is 48.'),
    ('(1538 % 2) + 6?', 'The answer is 6.'),
    ('calculate 4 ** 4 + 14.', 'The answer is 270.'),
    ('calculate 1522 + 16 * 9!', 'The answer is 1666.'),
    ('what is (76 - 11) * 3', 'The answer is 195.'),
    ('calc (29 * 6) / 3?', 'The answer is 58.'),
    ('(1543 % 7) + 11.', 'The answer is 14.'),
    ('calculate 9 ** 3 + 19!', 'The answer is 748.'),
    ('calculate 1527 + 2 * 3', 'The answer is 1533.'),
    ('what is (81 - 3) * 3?', 'The answer is 234.'),
    ('calc (34 * 6) / 3.', 'The answer is 68.'),
    ('(1548 % 12) + 3!', 'The answer is 3.'),
    ('calculate 6 ** 2 + 24', 'The answer is 60.'),
    ('calculate 1532 + 7 * 8?', 'The answer is 1588.'),
    ('what is (86 - 8) * 3.', 'The answer is 234.'),
    ('calc (39 * 6) / 3!', 'The answer is 78.'),
    ('(1553 % 17) + 8', 'The answer is 14.'),
    ('calculate 3 ** 4 + 29?', 'The answer is 110.'),
    ('calculate 1537 + 12 * 2.', 'The answer is 1561.'),
    ('what is (91 - 13) * 3!', 'The answer is 234.'),
    ('calc (44 * 6) / 3', 'The answer is 88.'),
    ('(1558 % 5) + 13?', 'The answer is 16.'),
    ('calculate 8 ** 3 + 34.', 'The answer is 546.'),
    ('calculate 1542 + 17 * 7!', 'The answer is 1661.'),
]


def test_spec_batch_016() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
