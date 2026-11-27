import json
from pathlib import Path
import threading
from urllib.request import Request, urlopen
from urllib.error import HTTPError

import pytest

from riley.config import Settings
from riley.store import ChatStore
from riley.web import AppServer


@pytest.fixture
def app(tmp_path):
    server = AppServer(('127.0.0.1', 0), Settings(), ChatStore(tmp_path / 'chats.db'))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield server
    server.shutdown()
    server.server_close()
    thread.join()


def request(app, path, body=None, token=True, headers=None):
    extra = headers or {}
    if token:
        extra['X-Riley-Token'] = app.token
    data = None if body is None else json.dumps(body).encode()
    req = Request(f'http://127.0.0.1:{app.server_port}{path}', data=data, headers=extra)
    try:
        with urlopen(req) as response:
            return response.status, json.load(response)
    except HTTPError as exc:
        return exc.code, json.load(exc)


def test_saved_conversation_round_trip_and_delete(app):
    status, chat = request(app, '/api/chats', {})
    assert status == 201
    status, result = request(app, '/api/chat', {'chat_id': chat['id'], 'prompt': 'calculate 2+3*4', 'language':'en', 'backend':'local'})
    assert status == 200
    assert '14' in result['messages'][1]['content']
    assert result['chats'][0]['title'] == 'calculate 2+3*4'
    assert len(request(app, '/api/chats/' + chat['id'])[1]['messages']) == 2
    assert request(app, '/api/delete', {'chat_id':chat['id']})[0] == 200
    assert request(app, '/api/chats/' + chat['id'])[0] == 404


def test_reject_cross_origin_and_missing_token(app):
    assert request(app, '/api/chats', {}, token=False)[0] == 403
    assert request(app, '/api/state', headers={'Origin':'https://example.com'})[0] == 403
    assert request(app, '/api/state', headers={'Host':'evil.example'})[0] == 403


def test_invalid_requests_do_not_store_messages(app):
    _, chat = request(app, '/api/chats', {})
    for fields in ({'prompt':' '}, {'prompt':'x'*12001}, {'prompt':'hello','backend':'invalid'}, {'prompt':'hello','language':'xx'}, {'prompt':'hello','model':[]}):
        assert request(app, '/api/chat', {'chat_id':chat['id'], **fields})[0] == 400
    assert request(app, '/api/chats/'+chat['id'])[1]['messages'] == []


def test_backend_failure_keeps_turn_retryable(app, monkeypatch):
    from riley.exceptions import BackendError
    class FailedBackend:
        def generate(self, *args):
            raise BackendError('Ollama unavailable')
    monkeypatch.setattr('riley.web.create_backend', lambda *args: FailedBackend())
    _, chat = request(app, '/api/chats', {})
    assert request(app, '/api/chat', {'chat_id':chat['id'], 'prompt':'hello'})[0] == 502
    assert app.store.messages(chat['id']) == []


def test_busy_backend_returns_conflict(app):
    _, chat = request(app, '/api/chats', {})
    with app.turn_lock:
        assert request(app, '/api/chat', {'chat_id':chat['id'], 'prompt':'hello'})[0] == 409


def test_static_assets_and_path_traversal(app):
    for path in ('/', '/app.js', '/style.css', '/icon.svg'):
        with urlopen(f'http://127.0.0.1:{app.server_port}{path}') as response:
            assert response.status == 200
            assert response.headers['X-Content-Type-Options'] == 'nosniff'
            assert "frame-ancestors 'none'" in response.headers['Content-Security-Policy']
    assert request(app, '/../.env')[0] == 404


def test_store_persists_and_isolates_chats(tmp_path: Path):
    from riley.models import Message
    store = ChatStore(tmp_path / 'db')
    a, b = store.create(), store.create()
    store.append_turn(a['id'], Message('user', 'こんにちは'), Message('assistant', 'hello'))
    reopened = ChatStore(tmp_path / 'db')
    assert reopened.messages(a['id'])[0].content == 'こんにちは'
    assert reopened.messages(b['id']) == []
    reopened.delete(a['id'])
    with reopened.connect() as db:
        assert db.execute('SELECT count(*) FROM messages').fetchone()[0] == 0
