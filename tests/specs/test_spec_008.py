"""Verification spec batch 008: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (37 - 15) * 3?', 'The answer is 66.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(728 % 8) + 15!', 'The answer is 15.'),
    ('calculate 2 ** 4 + 4', 'The answer is 20.'),
    ('calculate 712 + 4 * 2?', 'The answer is 720.'),
    ('what is (42 - 7) * 3.', 'The answer is 105.'),
    ('calc (219 * 6) / 3!', 'The answer is 438.'),
    ('(733 % 13) + 7', 'The answer is 12.'),
    ('calculate 7 ** 3 + 9?', 'The answer is 352.'),
    ('calculate 717 + 9 * 7.', 'The answer is 780.'),
    ('what is (47 - 12) * 3!', 'The answer is 105.'),
    ('calc (224 * 6) / 3', 'The answer is 448.'),
    ('(738 % 18) + 12?', 'The answer is 12.'),
    ('calculate 4 ** 2 + 14.', 'The answer is 30.'),
    ('calculate 722 + 14 * 1!', 'The answer is 736.'),
    ('what is (52 - 4) * 3', 'The answer is 144.'),
    ('calc (229 * 6) / 3?', 'The answer is 458.'),
    ('(743 % 6) + 4.', 'The answer is 9.'),
    ('calculate 9 ** 4 + 19!', 'The answer is 6580.'),
    ('calculate 727 + 19 * 6', 'The answer is 841.'),
    ('what is (57 - 9) * 3?', 'The answer is 144.'),
    ('calc (234 * 6) / 3.', 'The answer is 468.'),
    ('(748 % 11) + 9!', 'The answer is 9.'),
    ('calculate 6 ** 3 + 24', 'The answer is 240.'),
    ('calculate 732 + 5 * 11?', 'The answer is 787.'),
    ('what is (62 - 14) * 3.', 'The answer is 144.'),
    ('calc (239 * 6) / 3!', 'The answer is 478.'),
    ('(753 % 16) + 14', 'The answer is 15.'),
    ('calculate 3 ** 2 + 29?', 'The answer is 38.'),
    ('calculate 737 + 10 * 5.', 'The answer is 787.'),
    ('what is (67 - 6) * 3!', 'The answer is 183.'),
    ('calc (244 * 6) / 3', 'The answer is 488.'),
    ('(758 % 4) + 6?', 'The answer is 8.'),
    ('calculate 8 ** 4 + 34.', 'The answer is 4130.'),
    ('calculate 742 + 15 * 10!', 'The answer is 892.'),
    ('what is (72 - 11) * 3', 'The answer is 183.'),
    ('calc (249 * 6) / 3?', 'The answer is 498.'),
    ('(763 % 9) + 11.', 'The answer is 18.'),
    ('calculate 5 ** 3 + 39!', 'The answer is 164.'),
    ('calculate 747 + 20 * 4', 'The answer is 827.'),
]


def test_spec_batch_008() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
