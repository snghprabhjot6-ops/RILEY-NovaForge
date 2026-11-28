"""Verification spec batch 021: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (76 - 15) * 3?', 'The answer is 183.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(2028 % 16) + 15!', 'The answer is 27.'),
    ('calculate 6 ** 2 + 4', 'The answer is 40.'),
    ('calculate 2012 + 12 * 4?', 'The answer is 2060.'),
    ('what is (81 - 7) * 3.', 'The answer is 222.'),
    ('calc (19 * 6) / 3!', 'The answer is 38.'),
    ('(2033 % 4) + 7', 'The answer is 8.'),
    ('calculate 3 ** 4 + 9?', 'The answer is 90.'),
    ('calculate 2017 + 17 * 9.', 'The answer is 2170.'),
]


def test_spec_batch_021() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
