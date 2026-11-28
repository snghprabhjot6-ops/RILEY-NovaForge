"""Verification spec batch 098: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('system', 'Verified Riley payload 9701 (sa)', 'sa', 'llama3.2-r9701'),
    ('user', 'Verified Riley payload 9702 (en)', 'en', 'llama3.2-r9702'),
    ('assistant', 'Verified Riley payload 9703 (hi)', 'hi', 'llama3.2-r9703'),
    ('system', 'Verified Riley payload 9704 (fr)', 'fr', 'llama3.2-r9704'),
    ('user', 'Verified Riley payload 9705 (es)', 'es', 'llama3.2-r9705'),
]


def test_spec_batch_098() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
