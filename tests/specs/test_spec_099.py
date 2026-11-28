"""Verification spec batch 099: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('user', 'Verified Riley payload 9801 (es)', 'es', 'llama3.2-r9801'),
    ('assistant', 'Verified Riley payload 9802 (bn)', 'bn', 'llama3.2-r9802'),
    ('system', 'Verified Riley payload 9803 (sa)', 'sa', 'llama3.2-r9803'),
    ('user', 'Verified Riley payload 9804 (en)', 'en', 'llama3.2-r9804'),
    ('assistant', 'Verified Riley payload 9805 (hi)', 'hi', 'llama3.2-r9805'),
    ('system', 'Verified Riley payload 9806 (fr)', 'fr', 'llama3.2-r9806'),
    ('user', 'Verified Riley payload 9807 (es)', 'es', 'llama3.2-r9807'),
]


def test_spec_batch_099() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
