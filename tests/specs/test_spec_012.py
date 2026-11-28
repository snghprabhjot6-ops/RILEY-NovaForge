"""Verification spec batch 012: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (49 - 12) * 3?', 'The answer is 111.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(1128 % 17) + 12!', 'The answer is 18.'),
    ('calculate 2 ** 2 + 4', 'The answer is 8.'),
    ('calculate 1112 + 5 * 6?', 'The answer is 1142.'),
    ('what is (54 - 4) * 3.', 'The answer is 150.'),
    ('calc (119 * 6) / 3!', 'The answer is 238.'),
    ('(1133 % 5) + 4', 'The answer is 7.'),
    ('calculate 7 ** 4 + 9?', 'The answer is 2410.'),
]


def test_spec_batch_012() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
