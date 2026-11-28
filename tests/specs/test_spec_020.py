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
    ('what is (98 - 5) * 3.', 'The answer is 279.'),
    ('calc (189 * 6) / 3!', 'The answer is 378.'),
    ('(1953 % 9) + 5', 'The answer is 5.'),
    ('calculate 3 ** 2 + 29?', 'The answer is 38.'),
    ('calculate 1937 + 13 * 6.', 'The answer is 2015.'),
    ('what is (103 - 10) * 3!', 'The answer is 279.'),
    ('calc (194 * 6) / 3', 'The answer is 388.'),
    ('(1958 % 14) + 10?', 'The answer is 22.'),
    ('calculate 8 ** 4 + 34.', 'The answer is 4130.'),
    ('calculate 1942 + 18 * 11!', 'The answer is 2140.'),
    ('what is (108 - 15) * 3', 'The answer is 279.'),
    ('calc (199 * 6) / 3?', 'The answer is 398.'),
    ('(1963 % 2) + 15.', 'The answer is 16.'),
    ('calculate 5 ** 3 + 39!', 'The answer is 164.'),
    ('calculate 1947 + 4 * 5', 'The answer is 1967.'),
    ('what is (16 - 7) * 3?', 'The answer is 27.'),
    ('calc (204 * 6) / 3.', 'The answer is 408.'),
    ('(1968 % 7) + 7!', 'The answer is 8.'),
    ('calculate 2 ** 2 + 44', 'The answer is 48.'),
    ('calculate 1952 + 9 * 10?', 'The answer is 2042.'),
    ('what is (21 - 12) * 3.', 'The answer is 27.'),
    ('calc (209 * 6) / 3!', 'The answer is 418.'),
    ('(1973 % 12) + 12', 'The answer is 17.'),
]


def test_spec_batch_020() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
