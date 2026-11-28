"""Verification spec batch 001: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (16 - 4) * 3?', 'The answer is 36.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(28 % 5) + 4!', 'The answer is 7.'),
    ('calculate 6 ** 3 + 4', 'The answer is 220.'),
    ('calculate 12 + 7 * 6?', 'The answer is 54.'),
    ('what is (21 - 9) * 3.', 'The answer is 36.'),
    ('calc (19 * 6) / 3!', 'The answer is 38.'),
    ('(33 % 10) + 9', 'The answer is 12.'),
    ('calculate 3 ** 2 + 9?', 'The answer is 18.'),
    ('calculate 17 + 12 * 11.', 'The answer is 149.'),
    ('what is (26 - 14) * 3!', 'The answer is 36.'),
    ('calc (24 * 6) / 3', 'The answer is 48.'),
    ('(38 % 15) + 14?', 'The answer is 22.'),
    ('calculate 8 ** 4 + 14.', 'The answer is 4110.'),
    ('calculate 22 + 17 * 5!', 'The answer is 107.'),
    ('what is (31 - 6) * 3', 'The answer is 75.'),
    ('calc (29 * 6) / 3?', 'The answer is 58.'),
    ('(43 % 3) + 6.', 'The answer is 7.'),
    ('calculate 5 ** 3 + 19!', 'The answer is 144.'),
    ('calculate 27 + 3 * 10', 'The answer is 57.'),
    ('what is (36 - 11) * 3?', 'The answer is 75.'),
    ('calc (34 * 6) / 3.', 'The answer is 68.'),
    ('(48 % 8) + 11!', 'The answer is 11.'),
]


def test_spec_batch_001() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
