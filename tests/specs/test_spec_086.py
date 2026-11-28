"""Verification spec batch 086: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('system', 'Verified Riley payload 8501 (sa)', 'sa', 'llama3.2-r8501'),
    ('user', 'Verified Riley payload 8502 (en)', 'en', 'llama3.2-r8502'),
    ('assistant', 'Verified Riley payload 8503 (hi)', 'hi', 'llama3.2-r8503'),
]


def test_spec_batch_086() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
