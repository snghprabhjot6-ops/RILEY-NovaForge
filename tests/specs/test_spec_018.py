"""Verification spec batch 018: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (67 - 14) * 3?', 'The answer is 159.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(1728 % 5) + 14!', 'The answer is 17.'),
    ('calculate 2 ** 2 + 4', 'The answer is 8.'),
    ('calculate 1712 + 16 * 1?', 'The answer is 1728.'),
    ('what is (72 - 6) * 3.', 'The answer is 198.'),
    ('calc (219 * 6) / 3!', 'The answer is 438.'),
    ('(1733 % 10) + 6', 'The answer is 9.'),
]


def test_spec_batch_018() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
