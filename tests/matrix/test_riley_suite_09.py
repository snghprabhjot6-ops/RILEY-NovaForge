from pathlib import Path
import pytest
from riley.history import ConversationHistory
from riley.models import Message
from riley.store import ChatStore

def test_history_bounds_001(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_1.json', max_messages=2)
    for n in range(4):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 2
    assert hist.messages[-1].content == 'turn-3'

