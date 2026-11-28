"""Verification spec batch 029: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (100 - 9) * 3?', 'The answer is 273.'),
    ('calc (64 * 6) / 3.', 'The answer is 128.'),
    ('(2828 % 17) + 9!', 'The answer is 15.'),
]


def test_spec_batch_029() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
