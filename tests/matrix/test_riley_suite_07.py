import pytest
from riley.models import Message

def test_message_roundtrip_001() -> None:
    msg = Message(role='assistant', content='Riley message payload #1 · नमस्ते · Bonjour', language='hi')
    restored = Message.from_dict(msg.to_dict())
    assert restored == msg

