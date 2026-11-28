"""Verification spec batch 008: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (37 - 15) * 3?', 'The answer is 66.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
    ('(728 % 8) + 15!', 'The answer is 15.'),
    ('calculate 2 ** 4 + 4', 'The answer is 20.'),
    ('calculate 712 + 4 * 2?', 'The answer is 720.'),
    ('what is (42 - 7) * 3.', 'The answer is 105.'),
    ('calc (219 * 6) / 3!', 'The answer is 438.'),
    ('(733 % 13) + 7', 'The answer is 12.'),
    ('calculate 7 ** 3 + 9?', 'The answer is 352.'),
    ('calculate 717 + 9 * 7.', 'The answer is 780.'),
]


def test_spec_batch_008() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
