"""Verification spec batch 096: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('user', 'Verified Riley payload 9501 (es)', 'es', 'llama3.2-r9501'),
    ('assistant', 'Verified Riley payload 9502 (bn)', 'bn', 'llama3.2-r9502'),
    ('system', 'Verified Riley payload 9503 (sa)', 'sa', 'llama3.2-r9503'),
    ('user', 'Verified Riley payload 9504 (en)', 'en', 'llama3.2-r9504'),
    ('assistant', 'Verified Riley payload 9505 (hi)', 'hi', 'llama3.2-r9505'),
    ('system', 'Verified Riley payload 9506 (fr)', 'fr', 'llama3.2-r9506'),
    ('user', 'Verified Riley payload 9507 (es)', 'es', 'llama3.2-r9507'),
    ('assistant', 'Verified Riley payload 9508 (bn)', 'bn', 'llama3.2-r9508'),
]


def test_spec_batch_096() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
