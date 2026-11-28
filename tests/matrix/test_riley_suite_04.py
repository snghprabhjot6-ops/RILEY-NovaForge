from riley.backends.local import LocalBackend
from riley.models import Message

_BACKEND = LocalBackend()

def test_word_boundary_guard_001() -> None:
    reply = _BACKEND.generate([Message('user', 'Please review update item 1')], 'en')
    assert 'learning' in reply

def test_word_boundary_guard_002() -> None:
    reply = _BACKEND.generate([Message('user', 'Please review candidate item 2')], 'en')
    assert 'learning' in reply

def test_word_boundary_guard_003() -> None:
    reply = _BACKEND.generate([Message('user', 'Please review validate item 3')], 'en')
    assert 'learning' in reply

def test_word_boundary_guard_004() -> None:
    reply = _BACKEND.generate([Message('user', 'Please review sedate item 4')], 'en')
    assert 'learning' in reply

def test_word_boundary_guard_005() -> None:
    reply = _BACKEND.generate([Message('user', 'Please review mandate item 5')], 'en')
    assert 'learning' in reply

def test_word_boundary_guard_006() -> None:
    reply = _BACKEND.generate([Message('user', 'Please review predate item 6')], 'en')
    assert 'learning' in reply

def test_word_boundary_guard_007() -> None:
    reply = _BACKEND.generate([Message('user', 'Please review outdated item 7')], 'en')
    assert 'learning' in reply

