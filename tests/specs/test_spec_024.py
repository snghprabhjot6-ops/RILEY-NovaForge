"""Verification spec batch 024: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (85 - 3) * 3?', 'The answer is 246.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(2328 % 10) + 3!', 'The answer is 11.'),
    ('calculate 2 ** 2 + 4', 'The answer is 8.'),
    ('calculate 2312 + 8 * 7?', 'The answer is 2368.'),
    ('what is (90 - 8) * 3.', 'The answer is 246.'),
    ('calc (69 * 6) / 3!', 'The answer is 138.'),
    ('(2333 % 15) + 8', 'The answer is 16.'),
    ('calculate 7 ** 4 + 9?', 'The answer is 2410.'),
    ('calculate 2317 + 13 * 1.', 'The answer is 2330.'),
    ('what is (95 - 13) * 3!', 'The answer is 246.'),
    ('calc (74 * 6) / 3', 'The answer is 148.'),
    ('(2338 % 3) + 13?', 'The answer is 14.'),
    ('calculate 4 ** 3 + 14.', 'The answer is 78.'),
    ('calculate 2322 + 18 * 6!', 'The answer is 2430.'),
    ('what is (100 - 5) * 3', 'The answer is 285.'),
    ('calc (79 * 6) / 3?', 'The answer is 158.'),
    ('(2343 % 8) + 5.', 'The answer is 12.'),
    ('calculate 9 ** 2 + 19!', 'The answer is 100.'),
    ('calculate 2327 + 4 * 11', 'The answer is 2371.'),
    ('what is (105 - 10) * 3?', 'The answer is 285.'),
    ('calc (84 * 6) / 3.', 'The answer is 168.'),
    ('(2348 % 13) + 10!', 'The answer is 18.'),
    ('calculate 6 ** 4 + 24', 'The answer is 1320.'),
]


def test_spec_batch_024() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
