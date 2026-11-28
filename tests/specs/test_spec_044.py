"""Verification spec batch 044: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (48 - 14) * 3?', 'The answer is 102.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(4328 % 4) + 14!', 'The answer is 14.'),
    ('calculate 2 ** 4 + 4', 'The answer is 20.'),
    ('calculate 4312 + 13 * 5?', 'The answer is 4377.'),
    ('what is (53 - 6) * 3.', 'The answer is 141.'),
]


def test_spec_batch_044() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
