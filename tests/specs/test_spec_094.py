"""Verification spec batch 094: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('assistant', 'Verified Riley payload 9301 (hi)', 'hi', 'llama3.2-r9301'),
    ('system', 'Verified Riley payload 9302 (fr)', 'fr', 'llama3.2-r9302'),
    ('user', 'Verified Riley payload 9303 (es)', 'es', 'llama3.2-r9303'),
]


def test_spec_batch_094() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
