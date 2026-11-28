"""Verification spec batch 023: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (82 - 7) * 3?', 'The answer is 225.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(2228 % 12) + 7!', 'The answer is 15.'),
    ('calculate 6 ** 4 + 4', 'The answer is 1300.'),
    ('calculate 2212 + 3 * 6?', 'The answer is 2230.'),
    ('what is (87 - 12) * 3.', 'The answer is 225.'),
    ('calc (219 * 6) / 3!', 'The answer is 438.'),
    ('(2233 % 17) + 12', 'The answer is 18.'),
    ('calculate 3 ** 3 + 9?', 'The answer is 36.'),
    ('calculate 2217 + 8 * 11.', 'The answer is 2305.'),
    ('what is (92 - 4) * 3!', 'The answer is 264.'),
    ('calc (224 * 6) / 3', 'The answer is 448.'),
    ('(2238 % 5) + 4?', 'The answer is 7.'),
    ('calculate 8 ** 2 + 14.', 'The answer is 78.'),
    ('calculate 2222 + 13 * 5!', 'The answer is 2287.'),
    ('what is (97 - 9) * 3', 'The answer is 264.'),
    ('calc (229 * 6) / 3?', 'The answer is 458.'),
    ('(2243 % 10) + 9.', 'The answer is 12.'),
    ('calculate 5 ** 4 + 19!', 'The answer is 644.'),
    ('calculate 2227 + 18 * 10', 'The answer is 2407.'),
    ('what is (102 - 14) * 3?', 'The answer is 264.'),
    ('calc (234 * 6) / 3.', 'The answer is 468.'),
    ('(2248 % 15) + 14!', 'The answer is 27.'),
    ('calculate 2 ** 3 + 24', 'The answer is 32.'),
    ('calculate 2232 + 4 * 4?', 'The answer is 2248.'),
    ('what is (107 - 6) * 3.', 'The answer is 303.'),
    ('calc (239 * 6) / 3!', 'The answer is 478.'),
    ('(2253 % 3) + 6', 'The answer is 6.'),
    ('calculate 7 ** 2 + 29?', 'The answer is 78.'),
    ('calculate 2237 + 9 * 9.', 'The answer is 2318.'),
    ('what is (15 - 11) * 3!', 'The answer is 12.'),
    ('calc (244 * 6) / 3', 'The answer is 488.'),
    ('(2258 % 8) + 11?', 'The answer is 13.'),
    ('calculate 4 ** 4 + 34.', 'The answer is 290.'),
    ('calculate 2242 + 14 * 3!', 'The answer is 2284.'),
    ('what is (20 - 3) * 3', 'The answer is 51.'),
    ('calc (249 * 6) / 3?', 'The answer is 498.'),
    ('(2263 % 13) + 3.', 'The answer is 4.'),
    ('calculate 9 ** 3 + 39!', 'The answer is 768.'),
    ('calculate 2247 + 19 * 8', 'The answer is 2399.'),
    ('what is (25 - 8) * 3?', 'The answer is 51.'),
    ('calc (254 * 6) / 3.', 'The answer is 508.'),
    ('(2268 % 18) + 8!', 'The answer is 8.'),
    ('calculate 6 ** 2 + 44', 'The answer is 80.'),
]


def test_spec_batch_023() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
