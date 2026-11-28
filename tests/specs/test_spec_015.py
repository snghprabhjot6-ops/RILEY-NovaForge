"""Verification spec batch 015: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (58 - 13) * 3?', 'The answer is 135.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(1428 % 11) + 13!', 'The answer is 22.'),
    ('calculate 6 ** 2 + 4', 'The answer is 40.'),
    ('calculate 1412 + 20 * 9?', 'The answer is 1592.'),
    ('what is (63 - 5) * 3.', 'The answer is 174.'),
    ('calc (169 * 6) / 3!', 'The answer is 338.'),
    ('(1433 % 16) + 5', 'The answer is 14.'),
    ('calculate 3 ** 4 + 9?', 'The answer is 90.'),
    ('calculate 1417 + 6 * 3.', 'The answer is 1435.'),
    ('what is (68 - 10) * 3!', 'The answer is 174.'),
    ('calc (174 * 6) / 3', 'The answer is 348.'),
    ('(1438 % 4) + 10?', 'The answer is 12.'),
    ('calculate 8 ** 3 + 14.', 'The answer is 526.'),
    ('calculate 1422 + 11 * 8!', 'The answer is 1510.'),
    ('what is (73 - 15) * 3', 'The answer is 174.'),
    ('calc (179 * 6) / 3?', 'The answer is 358.'),
    ('(1443 % 9) + 15.', 'The answer is 18.'),
    ('calculate 5 ** 2 + 19!', 'The answer is 44.'),
    ('calculate 1427 + 16 * 2', 'The answer is 1459.'),
    ('what is (78 - 7) * 3?', 'The answer is 213.'),
    ('calc (184 * 6) / 3.', 'The answer is 368.'),
    ('(1448 % 14) + 7!', 'The answer is 13.'),
    ('calculate 2 ** 4 + 24', 'The answer is 40.'),
    ('calculate 1432 + 2 * 7?', 'The answer is 1446.'),
    ('what is (83 - 12) * 3.', 'The answer is 213.'),
    ('calc (189 * 6) / 3!', 'The answer is 378.'),
    ('(1453 % 2) + 12', 'The answer is 13.'),
    ('calculate 7 ** 3 + 29?', 'The answer is 372.'),
    ('calculate 1437 + 7 * 1.', 'The answer is 1444.'),
    ('what is (88 - 4) * 3!', 'The answer is 252.'),
    ('calc (194 * 6) / 3', 'The answer is 388.'),
    ('(1458 % 7) + 4?', 'The answer is 6.'),
    ('calculate 4 ** 2 + 34.', 'The answer is 50.'),
    ('calculate 1442 + 12 * 6!', 'The answer is 1514.'),
    ('what is (93 - 9) * 3', 'The answer is 252.'),
    ('calc (199 * 6) / 3?', 'The answer is 398.'),
    ('(1463 % 12) + 9.', 'The answer is 20.'),
    ('calculate 9 ** 4 + 39!', 'The answer is 6600.'),
    ('calculate 1447 + 17 * 11', 'The answer is 1634.'),
    ('what is (98 - 14) * 3?', 'The answer is 252.'),
    ('calc (204 * 6) / 3.', 'The answer is 408.'),
    ('(1468 % 17) + 14!', 'The answer is 20.'),
    ('calculate 6 ** 3 + 44', 'The answer is 260.'),
    ('calculate 1452 + 3 * 5?', 'The answer is 1467.'),
    ('what is (103 - 6) * 3.', 'The answer is 291.'),
]


def test_spec_batch_015() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
