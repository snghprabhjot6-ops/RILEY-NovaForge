"""Verification spec batch 088: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('assistant', 'Verified Riley payload 8701 (hi)', 'hi', 'llama3.2-r8701'),
    ('system', 'Verified Riley payload 8702 (fr)', 'fr', 'llama3.2-r8702'),
    ('user', 'Verified Riley payload 8703 (es)', 'es', 'llama3.2-r8703'),
    ('assistant', 'Verified Riley payload 8704 (bn)', 'bn', 'llama3.2-r8704'),
    ('system', 'Verified Riley payload 8705 (sa)', 'sa', 'llama3.2-r8705'),
    ('user', 'Verified Riley payload 8706 (en)', 'en', 'llama3.2-r8706'),
    ('assistant', 'Verified Riley payload 8707 (hi)', 'hi', 'llama3.2-r8707'),
    ('system', 'Verified Riley payload 8708 (fr)', 'fr', 'llama3.2-r8708'),
]


def test_spec_batch_088() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
