"""Verification spec batch 005: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (28 - 14) * 3?', 'The answer is 42.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(428 % 14) + 14!', 'The answer is 22.'),
    ('calculate 6 ** 4 + 4', 'The answer is 1300.'),
    ('calculate 412 + 8 * 10?', 'The answer is 492.'),
    ('what is (33 - 6) * 3.', 'The answer is 81.'),
    ('calc (169 * 6) / 3!', 'The answer is 338.'),
    ('(433 % 2) + 6', 'The answer is 7.'),
    ('calculate 3 ** 3 + 9?', 'The answer is 36.'),
    ('calculate 417 + 13 * 4.', 'The answer is 469.'),
    ('what is (38 - 11) * 3!', 'The answer is 81.'),
    ('calc (174 * 6) / 3', 'The answer is 348.'),
    ('(438 % 7) + 11?', 'The answer is 15.'),
    ('calculate 8 ** 2 + 14.', 'The answer is 78.'),
    ('calculate 422 + 18 * 9!', 'The answer is 584.'),
    ('what is (43 - 3) * 3', 'The answer is 120.'),
    ('calc (179 * 6) / 3?', 'The answer is 358.'),
    ('(443 % 12) + 3.', 'The answer is 14.'),
    ('calculate 5 ** 4 + 19!', 'The answer is 644.'),
    ('calculate 427 + 4 * 3', 'The answer is 439.'),
    ('what is (48 - 8) * 3?', 'The answer is 120.'),
    ('calc (184 * 6) / 3.', 'The answer is 368.'),
    ('(448 % 17) + 8!', 'The answer is 14.'),
    ('calculate 2 ** 3 + 24', 'The answer is 32.'),
    ('calculate 432 + 9 * 8?', 'The answer is 504.'),
    ('what is (53 - 13) * 3.', 'The answer is 120.'),
    ('calc (189 * 6) / 3!', 'The answer is 378.'),
    ('(453 % 5) + 13', 'The answer is 16.'),
    ('calculate 7 ** 2 + 29?', 'The answer is 78.'),
    ('calculate 437 + 14 * 2.', 'The answer is 465.'),
    ('what is (58 - 5) * 3!', 'The answer is 159.'),
    ('calc (194 * 6) / 3', 'The answer is 388.'),
    ('(458 % 10) + 5?', 'The answer is 13.'),
    ('calculate 4 ** 4 + 34.', 'The answer is 290.'),
    ('calculate 442 + 19 * 7!', 'The answer is 575.'),
    ('what is (63 - 10) * 3', 'The answer is 159.'),
    ('calc (199 * 6) / 3?', 'The answer is 398.'),
    ('(463 % 15) + 10.', 'The answer is 23.'),
    ('calculate 9 ** 3 + 39!', 'The answer is 768.'),
    ('calculate 447 + 5 * 1', 'The answer is 452.'),
    ('what is (68 - 15) * 3?', 'The answer is 159.'),
    ('calc (204 * 6) / 3.', 'The answer is 408.'),
    ('(468 % 3) + 15!', 'The answer is 15.'),
    ('calculate 6 ** 2 + 44', 'The answer is 80.'),
    ('calculate 452 + 10 * 6?', 'The answer is 512.'),
    ('what is (73 - 7) * 3.', 'The answer is 198.'),
    ('calc (209 * 6) / 3!', 'The answer is 418.'),
    ('(473 % 8) + 7', 'The answer is 8.'),
    ('calculate 3 ** 4 + 49?', 'The answer is 130.'),
    ('calculate 457 + 15 * 11.', 'The answer is 622.'),
    ('what is (78 - 12) * 3!', 'The answer is 198.'),
    ('calc (214 * 6) / 3', 'The answer is 428.'),
]


def test_spec_batch_005() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
