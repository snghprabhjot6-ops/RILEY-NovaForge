"""Verification spec batch 095: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('system', 'Verified Riley payload 9401 (sa)', 'sa', 'llama3.2-r9401'),
    ('user', 'Verified Riley payload 9402 (en)', 'en', 'llama3.2-r9402'),
    ('assistant', 'Verified Riley payload 9403 (hi)', 'hi', 'llama3.2-r9403'),
    ('system', 'Verified Riley payload 9404 (fr)', 'fr', 'llama3.2-r9404'),
    ('user', 'Verified Riley payload 9405 (es)', 'es', 'llama3.2-r9405'),
    ('assistant', 'Verified Riley payload 9406 (bn)', 'bn', 'llama3.2-r9406'),
    ('system', 'Verified Riley payload 9407 (sa)', 'sa', 'llama3.2-r9407'),
    ('user', 'Verified Riley payload 9408 (en)', 'en', 'llama3.2-r9408'),
    ('assistant', 'Verified Riley payload 9409 (hi)', 'hi', 'llama3.2-r9409'),
    ('system', 'Verified Riley payload 9410 (fr)', 'fr', 'llama3.2-r9410'),
    ('user', 'Verified Riley payload 9411 (es)', 'es', 'llama3.2-r9411'),
    ('assistant', 'Verified Riley payload 9412 (bn)', 'bn', 'llama3.2-r9412'),
    ('system', 'Verified Riley payload 9413 (sa)', 'sa', 'llama3.2-r9413'),
    ('user', 'Verified Riley payload 9414 (en)', 'en', 'llama3.2-r9414'),
    ('assistant', 'Verified Riley payload 9415 (hi)', 'hi', 'llama3.2-r9415'),
    ('system', 'Verified Riley payload 9416 (fr)', 'fr', 'llama3.2-r9416'),
]


def test_spec_batch_095() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
