"""Verification spec batch 027: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (94 - 4) * 3?', 'The answer is 270.'),
    ('calc (114 * 6) / 3.', 'The answer is 228.'),
    ('(2628 % 4) + 4!', 'The answer is 4.'),
    ('calculate 6 ** 2 + 4', 'The answer is 40.'),
    ('calculate 2612 + 4 * 10?', 'The answer is 2652.'),
    ('what is (99 - 9) * 3.', 'The answer is 270.'),
]


def test_spec_batch_027() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
