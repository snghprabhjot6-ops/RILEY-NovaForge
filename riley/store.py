"""SQLite chat storage. Each operation owns its connection for thread safety."""
from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from uuid import uuid4
from datetime import datetime, timezone

from .models import Message


class ChatStore:
    def __init__(self, path: Path):
        self.path = path
        path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.executescript('''
                CREATE TABLE IF NOT EXISTS chats (id TEXT PRIMARY KEY, title TEXT NOT NULL, created_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, chat_id TEXT NOT NULL REFERENCES chats(id) ON DELETE CASCADE,
                    role TEXT NOT NULL, content TEXT NOT NULL, language TEXT NOT NULL, created_at TEXT NOT NULL);
            ''')
        try:
            path.chmod(0o600)
        except OSError:
            pass

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=10)
        db.row_factory = sqlite3.Row
        db.execute('PRAGMA foreign_keys = ON')
        try:
            with db:
                yield db
        finally:
            db.close()

    def list(self):
        with self.connect() as db:
            return [dict(row) for row in db.execute('SELECT * FROM chats ORDER BY created_at DESC, rowid DESC')]

    def create(self):
        chat = {'id': uuid4().hex, 'title': 'New conversation', 'created_at': datetime.now(timezone.utc).isoformat()}
        with self.connect() as db:
            db.execute('INSERT INTO chats VALUES (:id, :title, :created_at)', chat)
        return chat

    def messages(self, chat_id: str):
        with self.connect() as db:
            if not db.execute('SELECT 1 FROM chats WHERE id=?', (chat_id,)).fetchone():
                raise KeyError('Conversation not found')
            rows = db.execute('SELECT role,content,language,created_at FROM messages WHERE chat_id=? ORDER BY id', (chat_id,)).fetchall()
            return [Message.from_dict(dict(row)) for row in rows]

    def append_turn(self, chat_id: str, prompt: Message, reply: Message):
        with self.connect() as db:
            if not db.execute('SELECT 1 FROM chats WHERE id=?', (chat_id,)).fetchone():
                raise KeyError('Conversation not found')
            first = not db.execute('SELECT 1 FROM messages WHERE chat_id=?', (chat_id,)).fetchone()
            for m in (prompt, reply):
                db.execute('INSERT INTO messages(chat_id,role,content,language,created_at) VALUES (?,?,?,?,?)',
                           (chat_id, m.role, m.content, m.language, m.created_at))
            if first:
                db.execute('UPDATE chats SET title=? WHERE id=?', (prompt.content[:55], chat_id))

    def delete(self, chat_id: str):
        with self.connect() as db:
            if not db.execute('DELETE FROM chats WHERE id=?', (chat_id,)).rowcount:
                raise KeyError('Conversation not found')
