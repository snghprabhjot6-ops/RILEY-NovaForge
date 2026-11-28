"""Verification spec batch 028: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (97 - 13) * 3?', 'The answer is 252.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(2728 % 2) + 13!', 'The answer is 13.'),
    ('calculate 2 ** 3 + 4', 'The answer is 12.'),
    ('calculate 2712 + 9 * 11?', 'The answer is 2811.'),
    ('what is (102 - 5) * 3.', 'The answer is 291.'),
    ('calc (219 * 6) / 3!', 'The answer is 438.'),
    ('(2733 % 7) + 5', 'The answer is 8.'),
    ('calculate 7 ** 2 + 9?', 'The answer is 58.'),
    ('calculate 2717 + 14 * 5.', 'The answer is 2787.'),
    ('what is (107 - 10) * 3!', 'The answer is 291.'),
    ('calc (224 * 6) / 3', 'The answer is 448.'),
    ('(2738 % 12) + 10?', 'The answer is 12.'),
    ('calculate 4 ** 4 + 14.', 'The answer is 270.'),
    ('calculate 2722 + 19 * 10!', 'The answer is 2912.'),
    ('what is (15 - 15) * 3', 'The answer is 0.'),
    ('calc (229 * 6) / 3?', 'The answer is 458.'),
    ('(2743 % 17) + 15.', 'The answer is 21.'),
    ('calculate 9 ** 3 + 19!', 'The answer is 748.'),
    ('calculate 2727 + 5 * 4', 'The answer is 2747.'),
    ('what is (20 - 7) * 3?', 'The answer is 39.'),
    ('calc (234 * 6) / 3.', 'The answer is 468.'),
    ('(2748 % 5) + 7!', 'The answer is 10.'),
    ('calculate 6 ** 2 + 24', 'The answer is 60.'),
    ('calculate 2732 + 10 * 9?', 'The answer is 2822.'),
    ('what is (25 - 12) * 3.', 'The answer is 39.'),
    ('calc (239 * 6) / 3!', 'The answer is 478.'),
    ('(2753 % 10) + 12', 'The answer is 15.'),
    ('calculate 3 ** 4 + 29?', 'The answer is 110.'),
    ('calculate 2737 + 15 * 3.', 'The answer is 2782.'),
    ('what is (30 - 4) * 3!', 'The answer is 78.'),
    ('calc (244 * 6) / 3', 'The answer is 488.'),
    ('(2758 % 15) + 4?', 'The answer is 17.'),
    ('calculate 8 ** 3 + 34.', 'The answer is 546.'),
    ('calculate 2742 + 20 * 8!', 'The answer is 2902.'),
    ('what is (35 - 9) * 3', 'The answer is 78.'),
    ('calc (249 * 6) / 3?', 'The answer is 498.'),
    ('(2763 % 3) + 9.', 'The answer is 9.'),
    ('calculate 5 ** 2 + 39!', 'The answer is 64.'),
    ('calculate 2747 + 6 * 2', 'The answer is 2759.'),
    ('what is (40 - 14) * 3?', 'The answer is 78.'),
]


def test_spec_batch_028() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
