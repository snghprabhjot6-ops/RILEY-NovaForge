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
]


def test_spec_batch_028() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
