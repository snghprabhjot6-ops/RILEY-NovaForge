"""Verification spec batch 097: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('assistant', 'Verified Riley payload 9601 (hi)', 'hi', 'llama3.2-r9601'),
    ('system', 'Verified Riley payload 9602 (fr)', 'fr', 'llama3.2-r9602'),
    ('user', 'Verified Riley payload 9603 (es)', 'es', 'llama3.2-r9603'),
]


def test_spec_batch_097() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
