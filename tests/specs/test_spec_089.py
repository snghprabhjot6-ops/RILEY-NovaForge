"""Verification spec batch 089: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('system', 'Verified Riley payload 8801 (sa)', 'sa', 'llama3.2-r8801'),
    ('user', 'Verified Riley payload 8802 (en)', 'en', 'llama3.2-r8802'),
    ('assistant', 'Verified Riley payload 8803 (hi)', 'hi', 'llama3.2-r8803'),
    ('system', 'Verified Riley payload 8804 (fr)', 'fr', 'llama3.2-r8804'),
]


def test_spec_batch_089() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
