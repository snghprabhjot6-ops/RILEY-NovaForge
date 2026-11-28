"""Verification spec batch 043: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (45 - 5) * 3?', 'The answer is 120.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(4228 % 6) + 5!', 'The answer is 9.'),
    ('calculate 6 ** 3 + 4', 'The answer is 220.'),
    ('calculate 4212 + 8 * 4?', 'The answer is 4244.'),
    ('what is (50 - 10) * 3.', 'The answer is 120.'),
    ('calc (219 * 6) / 3!', 'The answer is 438.'),
    ('(4233 % 11) + 10', 'The answer is 19.'),
    ('calculate 3 ** 2 + 9?', 'The answer is 18.'),
]


def test_spec_batch_043() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
