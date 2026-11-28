"""Verification spec batch 087: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('user', 'Verified Riley payload 8601 (es)', 'es', 'llama3.2-r8601'),
    ('assistant', 'Verified Riley payload 8602 (bn)', 'bn', 'llama3.2-r8602'),
    ('system', 'Verified Riley payload 8603 (sa)', 'sa', 'llama3.2-r8603'),
    ('user', 'Verified Riley payload 8604 (en)', 'en', 'llama3.2-r8604'),
    ('assistant', 'Verified Riley payload 8605 (hi)', 'hi', 'llama3.2-r8605'),
    ('system', 'Verified Riley payload 8606 (fr)', 'fr', 'llama3.2-r8606'),
    ('user', 'Verified Riley payload 8607 (es)', 'es', 'llama3.2-r8607'),
    ('assistant', 'Verified Riley payload 8608 (bn)', 'bn', 'llama3.2-r8608'),
    ('system', 'Verified Riley payload 8609 (sa)', 'sa', 'llama3.2-r8609'),
    ('user', 'Verified Riley payload 8610 (en)', 'en', 'llama3.2-r8610'),
    ('assistant', 'Verified Riley payload 8611 (hi)', 'hi', 'llama3.2-r8611'),
    ('system', 'Verified Riley payload 8612 (fr)', 'fr', 'llama3.2-r8612'),
    ('user', 'Verified Riley payload 8613 (es)', 'es', 'llama3.2-r8613'),
    ('assistant', 'Verified Riley payload 8614 (bn)', 'bn', 'llama3.2-r8614'),
    ('system', 'Verified Riley payload 8615 (sa)', 'sa', 'llama3.2-r8615'),
]


def test_spec_batch_087() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
