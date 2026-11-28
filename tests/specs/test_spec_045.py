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
    ('calculate 4417 + 4 * 11.', 'The answer is 4461.'),
    ('what is (61 - 7) * 3!', 'The answer is 162.'),
    ('calc (174 * 6) / 3', 'The answer is 348.'),
    ('(4438 % 12) + 7?', 'The answer is 17.'),
    ('calculate 8 ** 3 + 14.', 'The answer is 526.'),
    ('calculate 4422 + 9 * 5!', 'The answer is 4467.'),
    ('what is (66 - 12) * 3', 'The answer is 162.'),
    ('calc (179 * 6) / 3?', 'The answer is 358.'),
    ('(4443 % 17) + 12.', 'The answer is 18.'),
    ('calculate 5 ** 2 + 19!', 'The answer is 44.'),
    ('calculate 4427 + 14 * 10', 'The answer is 4567.'),
    ('what is (71 - 4) * 3?', 'The answer is 201.'),
    ('calc (184 * 6) / 3.', 'The answer is 368.'),
    ('(4448 % 5) + 4!', 'The answer is 7.'),
]


def test_spec_batch_045() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
