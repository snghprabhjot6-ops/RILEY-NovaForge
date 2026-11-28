"""Verification spec batch 006: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (31 - 10) * 3?', 'The answer is 63.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(528 % 12) + 10!', 'The answer is 10.'),
    ('calculate 2 ** 2 + 4', 'The answer is 8.'),
    ('calculate 512 + 13 * 11?', 'The answer is 655.'),
    ('what is (36 - 15) * 3.', 'The answer is 63.'),
    ('calc (19 * 6) / 3!', 'The answer is 38.'),
    ('(533 % 17) + 15', 'The answer is 21.'),
    ('calculate 7 ** 4 + 9?', 'The answer is 2410.'),
    ('calculate 517 + 18 * 5.', 'The answer is 607.'),
    ('what is (41 - 7) * 3!', 'The answer is 102.'),
    ('calc (24 * 6) / 3', 'The answer is 48.'),
    ('(538 % 5) + 7?', 'The answer is 10.'),
    ('calculate 4 ** 3 + 14.', 'The answer is 78.'),
]


def test_spec_batch_006() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
