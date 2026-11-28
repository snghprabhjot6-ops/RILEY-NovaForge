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

def test_history_bounds_004(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_4.json', max_messages=5)
    for n in range(7):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 5
    assert hist.messages[-1].content == 'turn-6'

def test_history_bounds_005(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_5.json', max_messages=1)
    for n in range(3):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 1
    assert hist.messages[-1].content == 'turn-2'

def test_history_bounds_006(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_6.json', max_messages=2)
    for n in range(4):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 2
    assert hist.messages[-1].content == 'turn-3'

def test_history_bounds_007(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_7.json', max_messages=3)
    for n in range(5):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 3
    assert hist.messages[-1].content == 'turn-4'

def test_history_bounds_008(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_8.json', max_messages=4)
    for n in range(6):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 4
    assert hist.messages[-1].content == 'turn-5'

def test_history_bounds_009(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_9.json', max_messages=5)
    for n in range(7):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 5
    assert hist.messages[-1].content == 'turn-6'

def test_history_bounds_010(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_10.json', max_messages=1)
    for n in range(3):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 1
    assert hist.messages[-1].content == 'turn-2'

def test_history_bounds_011(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_11.json', max_messages=2)
    for n in range(4):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 2
    assert hist.messages[-1].content == 'turn-3'

def test_history_bounds_012(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_12.json', max_messages=3)
    for n in range(5):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 3
    assert hist.messages[-1].content == 'turn-4'

def test_history_bounds_013(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_13.json', max_messages=4)
    for n in range(6):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 4
    assert hist.messages[-1].content == 'turn-5'

def test_history_bounds_014(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_14.json', max_messages=5)
    for n in range(7):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 5
    assert hist.messages[-1].content == 'turn-6'

def test_history_bounds_015(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_15.json', max_messages=1)
    for n in range(3):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 1
    assert hist.messages[-1].content == 'turn-2'

def test_history_bounds_016(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_16.json', max_messages=2)
    for n in range(4):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 2
    assert hist.messages[-1].content == 'turn-3'

def test_history_bounds_017(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_17.json', max_messages=3)
    for n in range(5):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 3
    assert hist.messages[-1].content == 'turn-4'

def test_history_bounds_018(tmp_path: Path) -> None:
    hist = ConversationHistory(tmp_path / 'h_18.json', max_messages=4)
    for n in range(6):
        hist.add(Message('user', f'turn-{n}'))
    assert len(hist.messages) == 4
    assert hist.messages[-1].content == 'turn-5'

