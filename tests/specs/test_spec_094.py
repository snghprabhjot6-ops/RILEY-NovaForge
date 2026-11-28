"""Verification spec batch 094: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('assistant', 'Verified Riley payload 9301 (hi)', 'hi', 'llama3.2-r9301'),
    ('system', 'Verified Riley payload 9302 (fr)', 'fr', 'llama3.2-r9302'),
    ('user', 'Verified Riley payload 9303 (es)', 'es', 'llama3.2-r9303'),
    ('assistant', 'Verified Riley payload 9304 (bn)', 'bn', 'llama3.2-r9304'),
    ('system', 'Verified Riley payload 9305 (sa)', 'sa', 'llama3.2-r9305'),
    ('user', 'Verified Riley payload 9306 (en)', 'en', 'llama3.2-r9306'),
    ('assistant', 'Verified Riley payload 9307 (hi)', 'hi', 'llama3.2-r9307'),
    ('system', 'Verified Riley payload 9308 (fr)', 'fr', 'llama3.2-r9308'),
    ('user', 'Verified Riley payload 9309 (es)', 'es', 'llama3.2-r9309'),
    ('assistant', 'Verified Riley payload 9310 (bn)', 'bn', 'llama3.2-r9310'),
    ('system', 'Verified Riley payload 9311 (sa)', 'sa', 'llama3.2-r9311'),
    ('user', 'Verified Riley payload 9312 (en)', 'en', 'llama3.2-r9312'),
    ('assistant', 'Verified Riley payload 9313 (hi)', 'hi', 'llama3.2-r9313'),
    ('system', 'Verified Riley payload 9314 (fr)', 'fr', 'llama3.2-r9314'),
    ('user', 'Verified Riley payload 9315 (es)', 'es', 'llama3.2-r9315'),
]


def test_spec_batch_094() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
