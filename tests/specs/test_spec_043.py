"""Verification spec batch 043: deterministic arithmetic evaluation."""
from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

CASES: list[tuple[str, str]] = [
    ('what is (45 - 5) * 3?', 'The answer is 120.'),
    ('calc (214 * 6) / 3.', 'The answer is 428.'),
]


def test_spec_batch_043() -> None:
    for prompt, expected in CASES:
        assert _BACKEND.generate([Message('user', prompt)], 'en') == expected
