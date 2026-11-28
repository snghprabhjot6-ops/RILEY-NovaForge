"""Verification spec batch 093: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('user', 'Verified Riley payload 9201 (es)', 'es', 'llama3.2-r9201'),
    ('assistant', 'Verified Riley payload 9202 (bn)', 'bn', 'llama3.2-r9202'),
    ('system', 'Verified Riley payload 9203 (sa)', 'sa', 'llama3.2-r9203'),
    ('user', 'Verified Riley payload 9204 (en)', 'en', 'llama3.2-r9204'),
]


def test_spec_batch_093() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
