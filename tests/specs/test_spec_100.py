"""Verification spec batch 100: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('assistant', 'Verified Riley payload 9901 (hi)', 'hi', 'llama3.2-r9901'),
    ('system', 'Verified Riley payload 9902 (fr)', 'fr', 'llama3.2-r9902'),
    ('user', 'Verified Riley payload 9903 (es)', 'es', 'llama3.2-r9903'),
    ('assistant', 'Verified Riley payload 9904 (bn)', 'bn', 'llama3.2-r9904'),
]


def test_spec_batch_100() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
