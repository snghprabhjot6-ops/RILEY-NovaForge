"""Verification spec batch 093: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('user', 'Verified Riley payload 9201 (es)', 'es', 'llama3.2-r9201'),
    ('assistant', 'Verified Riley payload 9202 (bn)', 'bn', 'llama3.2-r9202'),
    ('system', 'Verified Riley payload 9203 (sa)', 'sa', 'llama3.2-r9203'),
    ('user', 'Verified Riley payload 9204 (en)', 'en', 'llama3.2-r9204'),
    ('assistant', 'Verified Riley payload 9205 (hi)', 'hi', 'llama3.2-r9205'),
    ('system', 'Verified Riley payload 9206 (fr)', 'fr', 'llama3.2-r9206'),
    ('user', 'Verified Riley payload 9207 (es)', 'es', 'llama3.2-r9207'),
    ('assistant', 'Verified Riley payload 9208 (bn)', 'bn', 'llama3.2-r9208'),
    ('system', 'Verified Riley payload 9209 (sa)', 'sa', 'llama3.2-r9209'),
    ('user', 'Verified Riley payload 9210 (en)', 'en', 'llama3.2-r9210'),
    ('assistant', 'Verified Riley payload 9211 (hi)', 'hi', 'llama3.2-r9211'),
    ('system', 'Verified Riley payload 9212 (fr)', 'fr', 'llama3.2-r9212'),
    ('user', 'Verified Riley payload 9213 (es)', 'es', 'llama3.2-r9213'),
]


def test_spec_batch_093() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
