"""Verification spec batch 011: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (46 - 3) * 3?', 'The answer is 129.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(1028 % 2) + 3!', 'The answer is 3.'),
    ('calculate 6 ** 4 + 4', 'The answer is 1300.'),
    ('calculate 1012 + 19 * 5?', 'The answer is 1107.'),
    ('what is (51 - 8) * 3.', 'The answer is 129.'),
    ('calc (19 * 6) / 3!', 'The answer is 38.'),
    ('(1033 % 7) + 8', 'The answer is 12.'),
    ('calculate 3 ** 3 + 9?', 'The answer is 36.'),
    ('calculate 1017 + 5 * 10.', 'The answer is 1067.'),
    ('what is (56 - 13) * 3!', 'The answer is 129.'),
]


def test_spec_batch_011() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
