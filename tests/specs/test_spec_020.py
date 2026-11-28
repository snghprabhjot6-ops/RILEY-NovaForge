"""Verification spec batch 020: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (73 - 6) * 3?', 'The answer is 201.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(1928 % 18) + 6!', 'The answer is 8.'),
    ('calculate 2 ** 4 + 4', 'The answer is 20.'),
    ('calculate 1912 + 7 * 3?', 'The answer is 1933.'),
    ('what is (78 - 11) * 3.', 'The answer is 201.'),
    ('calc (169 * 6) / 3!', 'The answer is 338.'),
    ('(1933 % 6) + 11', 'The answer is 12.'),
    ('calculate 7 ** 3 + 9?', 'The answer is 352.'),
    ('calculate 1917 + 12 * 8.', 'The answer is 2013.'),
    ('what is (83 - 3) * 3!', 'The answer is 240.'),
    ('calc (174 * 6) / 3', 'The answer is 348.'),
    ('(1938 % 11) + 3?', 'The answer is 5.'),
    ('calculate 4 ** 2 + 14.', 'The answer is 30.'),
    ('calculate 1922 + 17 * 2!', 'The answer is 1956.'),
    ('what is (88 - 8) * 3', 'The answer is 240.'),
    ('calc (179 * 6) / 3?', 'The answer is 358.'),
    ('(1943 % 16) + 8.', 'The answer is 15.'),
    ('calculate 9 ** 4 + 19!', 'The answer is 6580.'),
    ('calculate 1927 + 3 * 7', 'The answer is 1948.'),
    ('what is (93 - 13) * 3?', 'The answer is 240.'),
    ('calc (184 * 6) / 3.', 'The answer is 368.'),
    ('(1948 % 4) + 13!', 'The answer is 13.'),
    ('calculate 6 ** 3 + 24', 'The answer is 240.'),
    ('calculate 1932 + 8 * 1?', 'The answer is 1940.'),
]


def test_spec_batch_020() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
