"""Verification spec batch 028: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (97 - 13) * 3?', 'The answer is 252.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(2728 % 2) + 13!', 'The answer is 13.'),
    ('calculate 2 ** 3 + 4', 'The answer is 12.'),
    ('calculate 2712 + 9 * 11?', 'The answer is 2811.'),
    ('what is (102 - 5) * 3.', 'The answer is 291.'),
]


def test_spec_batch_028() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
