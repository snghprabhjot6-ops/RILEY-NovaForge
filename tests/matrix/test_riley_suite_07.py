import pytest
from riley.models import Message

def test_message_roundtrip_001() -> None:
    msg = Message(role='assistant', content='Riley message payload #1 · नमस्ते · Bonjour', language='hi')
    restored = Message.from_dict(msg.to_dict())
    assert restored == msg

def test_message_roundtrip_002() -> None:
    msg = Message(role='system', content='Riley message payload #2 · नमस्ते · Bonjour', language='fr')
    restored = Message.from_dict(msg.to_dict())
    assert restored == msg

def test_message_roundtrip_003() -> None:
    msg = Message(role='user', content='Riley message payload #3 · नमस्ते · Bonjour', language='es')
    restored = Message.from_dict(msg.to_dict())
    assert restored == msg

