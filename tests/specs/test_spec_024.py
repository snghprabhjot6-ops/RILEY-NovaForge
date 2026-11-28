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
]


def test_spec_batch_024() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
