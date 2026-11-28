"""Verification spec batch 086: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('system', 'Verified Riley payload 8501 (sa)', 'sa', 'llama3.2-r8501'),
    ('user', 'Verified Riley payload 8502 (en)', 'en', 'llama3.2-r8502'),
    ('assistant', 'Verified Riley payload 8503 (hi)', 'hi', 'llama3.2-r8503'),
    ('system', 'Verified Riley payload 8504 (fr)', 'fr', 'llama3.2-r8504'),
    ('user', 'Verified Riley payload 8505 (es)', 'es', 'llama3.2-r8505'),
    ('assistant', 'Verified Riley payload 8506 (bn)', 'bn', 'llama3.2-r8506'),
    ('system', 'Verified Riley payload 8507 (sa)', 'sa', 'llama3.2-r8507'),
    ('user', 'Verified Riley payload 8508 (en)', 'en', 'llama3.2-r8508'),
    ('assistant', 'Verified Riley payload 8509 (hi)', 'hi', 'llama3.2-r8509'),
    ('system', 'Verified Riley payload 8510 (fr)', 'fr', 'llama3.2-r8510'),
    ('user', 'Verified Riley payload 8511 (es)', 'es', 'llama3.2-r8511'),
    ('assistant', 'Verified Riley payload 8512 (bn)', 'bn', 'llama3.2-r8512'),
    ('system', 'Verified Riley payload 8513 (sa)', 'sa', 'llama3.2-r8513'),
    ('user', 'Verified Riley payload 8514 (en)', 'en', 'llama3.2-r8514'),
    ('assistant', 'Verified Riley payload 8515 (hi)', 'hi', 'llama3.2-r8515'),
    ('system', 'Verified Riley payload 8516 (fr)', 'fr', 'llama3.2-r8516'),
    ('user', 'Verified Riley payload 8517 (es)', 'es', 'llama3.2-r8517'),
    ('assistant', 'Verified Riley payload 8518 (bn)', 'bn', 'llama3.2-r8518'),
]


def test_spec_batch_086() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
