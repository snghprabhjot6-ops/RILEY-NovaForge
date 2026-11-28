"""Verification spec batch 026: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (91 - 8) * 3?', 'The answer is 249.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(2528 % 6) + 8!', 'The answer is 10.'),
    ('calculate 2 ** 4 + 4', 'The answer is 20.'),
    ('calculate 2512 + 18 * 9?', 'The answer is 2674.'),
    ('what is (96 - 13) * 3.', 'The answer is 249.'),
    ('calc (19 * 6) / 3!', 'The answer is 38.'),
    ('(2533 % 11) + 13', 'The answer is 16.'),
    ('calculate 7 ** 3 + 9?', 'The answer is 352.'),
    ('calculate 2517 + 4 * 3.', 'The answer is 2529.'),
    ('what is (101 - 5) * 3!', 'The answer is 288.'),
    ('calc (24 * 6) / 3', 'The answer is 48.'),
    ('(2538 % 16) + 5?', 'The answer is 15.'),
    ('calculate 4 ** 2 + 14.', 'The answer is 30.'),
    ('calculate 2522 + 9 * 8!', 'The answer is 2594.'),
    ('what is (106 - 10) * 3', 'The answer is 288.'),
    ('calc (29 * 6) / 3?', 'The answer is 58.'),
    ('(2543 % 4) + 10.', 'The answer is 13.'),
    ('calculate 9 ** 4 + 19!', 'The answer is 6580.'),
    ('calculate 2527 + 14 * 2', 'The answer is 2555.'),
    ('what is (111 - 15) * 3?', 'The answer is 288.'),
    ('calc (34 * 6) / 3.', 'The answer is 68.'),
    ('(2548 % 9) + 15!', 'The answer is 16.'),
]


def test_spec_batch_026() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
