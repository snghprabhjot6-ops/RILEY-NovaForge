"""Verification spec batch 037: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (27 - 3) * 3?', 'The answer is 72.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(3628 % 18) + 3!', 'The answer is 13.'),
    ('calculate 6 ** 3 + 4', 'The answer is 220.'),
    ('calculate 3612 + 16 * 9?', 'The answer is 3756.'),
    ('what is (32 - 8) * 3.', 'The answer is 72.'),
    ('calc (119 * 6) / 3!', 'The answer is 238.'),
    ('(3633 % 6) + 8', 'The answer is 11.'),
    ('calculate 3 ** 2 + 9?', 'The answer is 18.'),
    ('calculate 3617 + 2 * 3.', 'The answer is 3623.'),
    ('what is (37 - 13) * 3!', 'The answer is 72.'),
    ('calc (124 * 6) / 3', 'The answer is 248.'),
    ('(3638 % 11) + 13?', 'The answer is 21.'),
    ('calculate 8 ** 4 + 14.', 'The answer is 4110.'),
    ('calculate 3622 + 7 * 8!', 'The answer is 3678.'),
    ('what is (42 - 5) * 3', 'The answer is 111.'),
    ('calc (129 * 6) / 3?', 'The answer is 258.'),
    ('(3643 % 16) + 5.', 'The answer is 16.'),
]


def test_spec_batch_037() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
