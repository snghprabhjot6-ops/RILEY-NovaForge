"""Verification spec batch 036: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (24 - 7) * 3?', 'The answer is 51.'),
    ('calc (14 * 6) / 3.', 'The answer is 28.'),
    ('(3528 % 3) + 7!', 'The answer is 7.'),
    ('calculate 2 ** 2 + 4', 'The answer is 8.'),
    ('calculate 3512 + 11 * 8?', 'The answer is 3600.'),
    ('what is (29 - 12) * 3.', 'The answer is 51.'),
    ('calc (19 * 6) / 3!', 'The answer is 38.'),
    ('(3533 % 8) + 12', 'The answer is 17.'),
    ('calculate 7 ** 4 + 9?', 'The answer is 2410.'),
    ('calculate 3517 + 16 * 2.', 'The answer is 3549.'),
    ('what is (34 - 4) * 3!', 'The answer is 90.'),
    ('calc (24 * 6) / 3', 'The answer is 48.'),
]


def test_spec_batch_036() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
