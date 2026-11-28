"""Verification spec batch 031: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (106 - 14) * 3?', 'The answer is 276.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(3028 % 13) + 14!', 'The answer is 26.'),
    ('calculate 6 ** 3 + 4', 'The answer is 220.'),
    ('calculate 3012 + 5 * 3?', 'The answer is 3027.'),
    ('what is (111 - 6) * 3.', 'The answer is 315.'),
]


def test_spec_batch_031() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
