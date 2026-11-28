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
]


def test_spec_batch_026() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
