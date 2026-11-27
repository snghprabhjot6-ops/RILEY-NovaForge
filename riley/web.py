"""Loopback-only Riley application. Start with python -m riley.web."""
from __future__ import annotations

import argparse
from dataclasses import replace
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import logging
from pathlib import Path
import secrets
import threading
import webbrowser

from .backends import create_backend
from .config import Settings, SUPPORTED_LANGUAGES
from .exceptions import RileyError
from .models import Message
from .store import ChatStore

STATIC = Path(__file__).with_name('static')


class AppServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, address, settings: Settings, store: ChatStore):
        self.settings, self.store = settings, store
        self.token = secrets.token_urlsafe(32)
        self.turn_lock = threading.Lock()
        super().__init__(address, Handler)


class Handler(BaseHTTPRequestHandler):
    server: AppServer

    def log_message(self, format, *args):
        # Do not log conversation bodies or tokens.
        logging.getLogger('riley.web').debug(format, *args)

    def send(self, status, value, mime='application/json; charset=utf-8'):
        data = json.dumps(value, ensure_ascii=False).encode() if mime.startswith('application/json') else value
        self.send_response(status)
        self.send_header('Content-Type', mime)
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'")
        self.end_headers()
        self.wfile.write(data)

    def allowed(self):
        expected = f'127.0.0.1:{self.server.server_port}'
        if self.headers.get('Host') != expected:
            self.send(403, {'error': 'Open Riley using its 127.0.0.1 address.'})
            return False
        origin = self.headers.get('Origin')
        if origin and origin != f'http://{expected}':
            self.send(403, {'error': 'Cross-origin request blocked.'})
            return False
        return True

    def do_GET(self):
        if not self.allowed():
            return
        if self.path == '/api/state':
            self.send(200, {'token': self.server.token, 'chats': self.server.store.list(),
                            'language': self.server.settings.language, 'backend': self.server.settings.backend,
                            'model': self.server.settings.ollama_model})
        elif self.path.startswith('/api/chats/'):
            try:
                messages = self.server.store.messages(self.path.removeprefix('/api/chats/'))
                self.send(200, {'messages': [m.to_dict() for m in messages]})
            except KeyError:
                self.send(404, {'error': 'Conversation not found.'})
        elif self.path in {'/', '/app.js', '/style.css', '/icon.svg'}:
            name = 'index.html' if self.path == '/' else self.path[1:]
            mime = {'html': 'text/html', 'js': 'text/javascript', 'css': 'text/css', 'svg': 'image/svg+xml'}[name.rsplit('.', 1)[1]]
            self.send(200, (STATIC / name).read_bytes(), mime + '; charset=utf-8')
        else:
            self.send(404, {'error': 'Not found.'})

    def do_POST(self):
        if not self.allowed():
            return
        if not secrets.compare_digest(self.headers.get('X-Riley-Token', ''), self.server.token):
            self.send(403, {'error': 'Session expired. Reload Riley.'})
            return
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= 65_536:
                raise ValueError('Request is empty or too large.')
            body = json.loads(self.rfile.read(length))
            if not isinstance(body, dict):
                raise ValueError('Expected a JSON object.')
            if self.path == '/api/chats':
                self.send(201, self.server.store.create())
            elif self.path == '/api/delete':
                with self.server.turn_lock:
                    self.server.store.delete(body.get('chat_id', ''))
                self.send(200, {'ok': True})
            elif self.path == '/api/chat':
                self.chat(body)
            else:
                self.send(404, {'error': 'Not found.'})
        except KeyError:
            self.send(404, {'error': 'Conversation not found.'})
        except (ValueError, TypeError, RileyError) as exc:
            self.send(400, {'error': str(exc)})
        except Exception:
            logging.getLogger('riley.web').exception('Request failed')
            self.send(500, {'error': 'Riley could not save or complete this request. Please try again.'})

    def chat(self, body):
        prompt = body.get('prompt')
        if not isinstance(prompt, str) or not prompt.strip() or len(prompt) > 12_000:
            raise ValueError('Enter a message between 1 and 12,000 characters.')
        config = replace(self.server.settings, language=body.get('language', self.server.settings.language),
                         backend=body.get('backend', self.server.settings.backend),
                         ollama_model=body.get('model', self.server.settings.ollama_model))
        if not all(isinstance(v, str) for v in (config.language, config.backend, config.ollama_model)):
            raise ValueError('Invalid chat settings.')
        config.validate()
        if not self.server.turn_lock.acquire(blocking=False):
            self.send(409, {'error': 'Riley is finishing another response. Please try again.'})
            return
        try:
            chat_id = body.get('chat_id', '')
            history = self.server.store.messages(chat_id)
            message = Message(role='user', content=prompt.strip(), language=config.language)
            try:
                response = create_backend(config.backend, config).generate([*history[-39:], message], config.language)
                if not response.strip():
                    raise ValueError('The model returned an empty response.')
            except RileyError as exc:
                self.send(502, {'error': str(exc)})
                return
            reply = Message(role='assistant', content=response, language=config.language)
            self.server.store.append_turn(chat_id, message, reply)
            self.send(200, {'messages': [message.to_dict(), reply.to_dict()], 'chats': self.server.store.list()})
        finally:
            self.server.turn_lock.release()


def main():
    parser = argparse.ArgumentParser(description='RILEY by NovaForge — local desktop web app')
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--no-browser', action='store_true')
    args = parser.parse_args()
    try:
        settings = Settings.from_env()
        server = AppServer(('127.0.0.1', args.port), settings, ChatStore(settings.history_file.parent / 'chats.db'))
    except (OSError, ValueError, RileyError) as exc:
        print(f'Could not start Riley: {exc}. If the port is busy, use --port 8766.')
        return 1
    address = f'http://127.0.0.1:{server.server_port}'
    print(f'RILEY by NovaForge is ready: {address}\nKeep this window open. Press Ctrl+C to stop.')
    if not args.no_browser:
        threading.Timer(0.5, lambda: webbrowser.open(address)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
