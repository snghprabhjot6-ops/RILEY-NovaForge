"""Verification spec batch 090: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('user', 'Verified Riley payload 8901 (es)', 'es', 'llama3.2-r8901'),
    ('assistant', 'Verified Riley payload 8902 (bn)', 'bn', 'llama3.2-r8902'),
    ('system', 'Verified Riley payload 8903 (sa)', 'sa', 'llama3.2-r8903'),
]


def test_spec_batch_090() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
