import json
from pathlib import Path

import pytest

from riley.history import ConversationHistory
from riley.models import Message


def test_history_round_trip(tmp_path: Path) -> None:
    path = tmp_path / "nested" / "history.json"
    history = ConversationHistory(path)
    history.add(Message(role="user", content="Hello"))
    loaded = ConversationHistory(path)
    loaded.load()
    assert len(loaded.messages) == 1
    assert loaded.messages[0].content == "Hello"


def test_history_is_bounded(tmp_path: Path) -> None:
    history = ConversationHistory(tmp_path / "history.json", max_messages=2)
    for number in range(3):
        history.add(Message(role="user", content=str(number)))
    assert [message.content for message in history.messages] == ["1", "2"]


def test_malformed_history_is_reported(tmp_path: Path) -> None:
    path = tmp_path / "history.json"
    path.write_text(json.dumps({"not": "a list"}), encoding="utf-8")
    with pytest.raises(ValueError):
        ConversationHistory(path).load()


def test_history_rejects_non_positive_limit(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        ConversationHistory(tmp_path / "history.json", max_messages=0)
