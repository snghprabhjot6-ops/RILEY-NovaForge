"""Verification spec batch 023: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (82 - 7) * 3?', 'The answer is 225.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(2228 % 12) + 7!', 'The answer is 15.'),
    ('calculate 6 ** 4 + 4', 'The answer is 1300.'),
    ('calculate 2212 + 3 * 6?', 'The answer is 2230.'),
]


def test_spec_batch_023() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
