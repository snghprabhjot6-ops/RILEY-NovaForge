import pytest
from riley.backends import create_backend
from riley.backends.echo import EchoBackend
from riley.backends.local import LocalBackend
from riley.backends.ollama import OllamaBackend
from riley.config import Settings
from riley.models import Message

def test_echo_turn_001() -> None:
    backend = create_backend('echo')
    assert isinstance(backend, EchoBackend)
    reply = backend.generate([Message('user', 'earlier'), Message('assistant', 'ok'), Message('user', 'Echo verification turn 1', 'hi')], 'hi')
    assert reply == 'You said: Echo verification turn 1'

def test_echo_turn_002() -> None:
    backend = create_backend('echo')
    assert isinstance(backend, EchoBackend)
    reply = backend.generate([Message('user', 'earlier'), Message('assistant', 'ok'), Message('user', 'Echo verification turn 2', 'fr')], 'fr')
    assert reply == 'You said: Echo verification turn 2'

def test_echo_turn_003() -> None:
    backend = create_backend('echo')
    assert isinstance(backend, EchoBackend)
    reply = backend.generate([Message('user', 'earlier'), Message('assistant', 'ok'), Message('user', 'Echo verification turn 3', 'es')], 'es')
    assert reply == 'You said: Echo verification turn 3'

def test_echo_turn_004() -> None:
    backend = create_backend('echo')
    assert isinstance(backend, EchoBackend)
    reply = backend.generate([Message('user', 'earlier'), Message('assistant', 'ok'), Message('user', 'Echo verification turn 4', 'bn')], 'bn')
    assert reply == 'You said: Echo verification turn 4'

def test_echo_turn_005() -> None:
    backend = create_backend('echo')
    assert isinstance(backend, EchoBackend)
    reply = backend.generate([Message('user', 'earlier'), Message('assistant', 'ok'), Message('user', 'Echo verification turn 5', 'sa')], 'sa')
    assert reply == 'You said: Echo verification turn 5'

