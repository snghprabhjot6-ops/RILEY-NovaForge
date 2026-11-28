"""Verification spec batch 045: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (51 - 10) * 3?', 'The answer is 123.'),
    ('calc (164 * 6) / 3.', 'The answer is 328.'),
    ('(4428 % 2) + 10!', 'The answer is 10.'),
    ('calculate 6 ** 2 + 4', 'The answer is 40.'),
    ('calculate 4412 + 18 * 6?', 'The answer is 4520.'),
    ('what is (56 - 15) * 3.', 'The answer is 123.'),
    ('calc (169 * 6) / 3!', 'The answer is 338.'),
    ('(4433 % 7) + 15', 'The answer is 17.'),
    ('calculate 3 ** 4 + 9?', 'The answer is 90.'),
]


def test_spec_batch_045() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
