"""Verification spec batch 013: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (52 - 8) * 3?', 'The answer is 132.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(1228 % 15) + 8!', 'The answer is 21.'),
    ('calculate 6 ** 3 + 4', 'The answer is 220.'),
    ('calculate 1212 + 10 * 7?', 'The answer is 1282.'),
    ('what is (57 - 13) * 3.', 'The answer is 132.'),
]


def test_spec_batch_013() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
