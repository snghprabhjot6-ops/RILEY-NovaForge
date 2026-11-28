"""Verification spec batch 091: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('assistant', 'Verified Riley payload 9001 (hi)', 'hi', 'llama3.2-r9001'),
    ('system', 'Verified Riley payload 9002 (fr)', 'fr', 'llama3.2-r9002'),
    ('user', 'Verified Riley payload 9003 (es)', 'es', 'llama3.2-r9003'),
    ('assistant', 'Verified Riley payload 9004 (bn)', 'bn', 'llama3.2-r9004'),
    ('system', 'Verified Riley payload 9005 (sa)', 'sa', 'llama3.2-r9005'),
]


def test_spec_batch_091() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
