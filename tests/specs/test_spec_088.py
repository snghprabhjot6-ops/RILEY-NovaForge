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
    ('user', 'Verified Riley payload 8709 (es)', 'es', 'llama3.2-r8709'),
    ('assistant', 'Verified Riley payload 8710 (bn)', 'bn', 'llama3.2-r8710'),
    ('system', 'Verified Riley payload 8711 (sa)', 'sa', 'llama3.2-r8711'),
    ('user', 'Verified Riley payload 8712 (en)', 'en', 'llama3.2-r8712'),
    ('assistant', 'Verified Riley payload 8713 (hi)', 'hi', 'llama3.2-r8713'),
    ('system', 'Verified Riley payload 8714 (fr)', 'fr', 'llama3.2-r8714'),
    ('user', 'Verified Riley payload 8715 (es)', 'es', 'llama3.2-r8715'),
    ('assistant', 'Verified Riley payload 8716 (bn)', 'bn', 'llama3.2-r8716'),
    ('system', 'Verified Riley payload 8717 (sa)', 'sa', 'llama3.2-r8717'),
    ('user', 'Verified Riley payload 8718 (en)', 'en', 'llama3.2-r8718'),
    ('assistant', 'Verified Riley payload 8719 (hi)', 'hi', 'llama3.2-r8719'),
    ('system', 'Verified Riley payload 8720 (fr)', 'fr', 'llama3.2-r8720'),
    ('user', 'Verified Riley payload 8721 (es)', 'es', 'llama3.2-r8721'),
]


def test_spec_batch_088() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
