"""Verification spec batch 044: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (48 - 14) * 3?', 'The answer is 102.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(4328 % 4) + 14!', 'The answer is 14.'),
    ('calculate 2 ** 4 + 4', 'The answer is 20.'),
    ('calculate 4312 + 13 * 5?', 'The answer is 4377.'),
    ('what is (53 - 6) * 3.', 'The answer is 141.'),
    ('calc (69 * 6) / 3!', 'The answer is 138.'),
    ('(4333 % 9) + 6', 'The answer is 10.'),
    ('calculate 7 ** 3 + 9?', 'The answer is 352.'),
    ('calculate 4317 + 18 * 10.', 'The answer is 4497.'),
    ('what is (58 - 11) * 3!', 'The answer is 141.'),
    ('calc (74 * 6) / 3', 'The answer is 148.'),
    ('(4338 % 14) + 11?', 'The answer is 23.'),
    ('calculate 4 ** 2 + 14.', 'The answer is 30.'),
    ('calculate 4322 + 4 * 4!', 'The answer is 4338.'),
    ('what is (63 - 3) * 3', 'The answer is 180.'),
    ('calc (79 * 6) / 3?', 'The answer is 158.'),
    ('(4343 % 2) + 3.', 'The answer is 4.'),
    ('calculate 9 ** 4 + 19!', 'The answer is 6580.'),
    ('calculate 4327 + 9 * 9', 'The answer is 4408.'),
    ('what is (68 - 8) * 3?', 'The answer is 180.'),
    ('calc (84 * 6) / 3.', 'The answer is 168.'),
    ('(4348 % 7) + 8!', 'The answer is 9.'),
    ('calculate 6 ** 3 + 24', 'The answer is 240.'),
    ('calculate 4332 + 14 * 3?', 'The answer is 4374.'),
    ('what is (73 - 13) * 3.', 'The answer is 180.'),
    ('calc (89 * 6) / 3!', 'The answer is 178.'),
    ('(4353 % 12) + 13', 'The answer is 22.'),
    ('calculate 3 ** 2 + 29?', 'The answer is 38.'),
]


def test_spec_batch_044() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
