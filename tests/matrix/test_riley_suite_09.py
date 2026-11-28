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

def test_history_bounds_002(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_2.json', max_messages=3)
    for n in range(5):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 3
    assert hist.messages[-1].content == 'turn-4'

def test_history_bounds_003(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_3.json', max_messages=4)
    for n in range(6):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 4
    assert hist.messages[-1].content == 'turn-5'

