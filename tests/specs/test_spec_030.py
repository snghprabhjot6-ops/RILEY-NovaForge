"""Verification spec batch 030: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (103 - 5) * 3?', 'The answer is 294.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(2928 % 15) + 5!', 'The answer is 8.'),
    ('calculate 2 ** 2 + 4', 'The answer is 8.'),
    ('calculate 2912 + 19 * 2?', 'The answer is 2950.'),
    ('what is (108 - 10) * 3.', 'The answer is 294.'),
    ('calc (169 * 6) / 3!', 'The answer is 338.'),
    ('(2933 % 3) + 10', 'The answer is 12.'),
]


def test_spec_batch_030() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
