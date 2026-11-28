import json
from urllib.error import URLError

import pytest

from riley.backends.ollama import OllamaBackend
from riley.models import Message
from riley.config import Settings
from riley.exceptions import BackendError, ConfigurationError


def test_ollama_sends_context_and_language(monkeypatch):
    class Response:
        def __enter__(self): return self
        def __exit__(self, *args): pass
        def read(self, limit): return b'{"message":{"content":"Bonjour"}}'
    class Opener:
        def open(self, request, timeout):
            payload = json.loads(request.data)
            assert payload['model'] == 'llama3.2'
            assert payload['stream'] is False
            assert 'French' in payload['messages'][0]['content']
            assert payload['messages'][1]['content'] == 'Hello'
            assert timeout == 120
            return Response()
    monkeypatch.setattr('riley.backends.ollama.build_opener', lambda *args: Opener())
    assert OllamaBackend().generate([Message('user','Hello')], 'fr') == 'Bonjour'


def test_ollama_unavailable_has_setup_guidance(monkeypatch):
    class Opener:
        def open(self, *args, **kwargs): raise URLError('offline')
    monkeypatch.setattr('riley.backends.ollama.build_opener', lambda *args: Opener())
    with pytest.raises(BackendError, match='ollama pull'):
        OllamaBackend().generate([Message('user','hello')], 'en')


@pytest.mark.parametrize('url',['https://example.com','http://example.com','http://localhost@evil.com','http://127.0.0.1/path','http://127.0.0.1?key=secret'])
def test_ollama_rejects_remote_endpoint(url):
    with pytest.raises(ConfigurationError):
        Settings(ollama_url=url).validate()
