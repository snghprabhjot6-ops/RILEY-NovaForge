"""Verification spec batch 032: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (109 - 10) * 3?', 'The answer is 297.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(3128 % 11) + 10!', 'The answer is 14.'),
    ('calculate 2 ** 4 + 4', 'The answer is 20.'),
    ('calculate 3112 + 10 * 4?', 'The answer is 3152.'),
    ('what is (17 - 15) * 3.', 'The answer is 6.'),
    ('calc (119 * 6) / 3!', 'The answer is 238.'),
    ('(3133 % 16) + 15', 'The answer is 28.'),
    ('calculate 7 ** 3 + 9?', 'The answer is 352.'),
    ('calculate 3117 + 15 * 9.', 'The answer is 3252.'),
    ('what is (22 - 7) * 3!', 'The answer is 45.'),
]


def test_spec_batch_032() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
