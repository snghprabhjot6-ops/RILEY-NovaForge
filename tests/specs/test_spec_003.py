"""Verification spec batch 003: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (22 - 9) * 3?', 'The answer is 39.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(228 % 18) + 9!', 'The answer is 21.'),
    ('calculate 6 ** 2 + 4', 'The answer is 40.'),
    ('calculate 212 + 17 * 8?', 'The answer is 348.'),
]


def test_spec_batch_003() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
