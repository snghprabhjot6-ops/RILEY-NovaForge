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
    ('calculate 7 ** 4 + 9?', 'The answer is 2410.'),
    ('calculate 2917 + 5 * 7.', 'The answer is 2952.'),
    ('what is (16 - 15) * 3!', 'The answer is 3.'),
    ('calc (174 * 6) / 3', 'The answer is 348.'),
    ('(2938 % 8) + 15?', 'The answer is 17.'),
    ('calculate 4 ** 3 + 14.', 'The answer is 78.'),
    ('calculate 2922 + 10 * 1!', 'The answer is 2932.'),
    ('what is (21 - 7) * 3', 'The answer is 42.'),
]


def test_spec_batch_030() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
