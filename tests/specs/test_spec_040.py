"""Verification spec batch 040: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (36 - 4) * 3?', 'The answer is 96.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(3928 % 12) + 4!', 'The answer is 8.'),
    ('calculate 2 ** 3 + 4', 'The answer is 12.'),
    ('calculate 3912 + 12 * 1?', 'The answer is 3924.'),
    ('what is (41 - 9) * 3.', 'The answer is 96.'),
    ('calc (169 * 6) / 3!', 'The answer is 338.'),
    ('(3933 % 17) + 9', 'The answer is 15.'),
    ('calculate 7 ** 2 + 9?', 'The answer is 58.'),
    ('calculate 3917 + 17 * 6.', 'The answer is 4019.'),
    ('what is (46 - 14) * 3!', 'The answer is 96.'),
    ('calc (174 * 6) / 3', 'The answer is 348.'),
    ('(3938 % 5) + 14?', 'The answer is 17.'),
    ('calculate 4 ** 4 + 14.', 'The answer is 270.'),
    ('calculate 3922 + 3 * 11!', 'The answer is 3955.'),
    ('what is (51 - 6) * 3', 'The answer is 135.'),
    ('calc (179 * 6) / 3?', 'The answer is 358.'),
    ('(3943 % 10) + 6.', 'The answer is 9.'),
    ('calculate 9 ** 3 + 19!', 'The answer is 748.'),
    ('calculate 3927 + 8 * 5', 'The answer is 3967.'),
    ('what is (56 - 11) * 3?', 'The answer is 135.'),
    ('calc (184 * 6) / 3.', 'The answer is 368.'),
    ('(3948 % 15) + 11!', 'The answer is 14.'),
    ('calculate 6 ** 2 + 24', 'The answer is 60.'),
    ('calculate 3932 + 13 * 10?', 'The answer is 4062.'),
    ('what is (61 - 3) * 3.', 'The answer is 174.'),
    ('calc (189 * 6) / 3!', 'The answer is 378.'),
    ('(3953 % 3) + 3', 'The answer is 5.'),
    ('calculate 3 ** 4 + 29?', 'The answer is 110.'),
]


def test_spec_batch_040() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
