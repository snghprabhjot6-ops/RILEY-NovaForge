"""Verification spec batch 088: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('assistant', 'Verified Riley payload 8701 (hi)', 'hi', 'llama3.2-r8701'),
    ('system', 'Verified Riley payload 8702 (fr)', 'fr', 'llama3.2-r8702'),
]


def test_spec_batch_088() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
