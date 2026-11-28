"""Verification spec batch 098: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('system', 'Verified Riley payload 9701 (sa)', 'sa', 'llama3.2-r9701'),
    ('user', 'Verified Riley payload 9702 (en)', 'en', 'llama3.2-r9702'),
    ('assistant', 'Verified Riley payload 9703 (hi)', 'hi', 'llama3.2-r9703'),
    ('system', 'Verified Riley payload 9704 (fr)', 'fr', 'llama3.2-r9704'),
    ('user', 'Verified Riley payload 9705 (es)', 'es', 'llama3.2-r9705'),
    ('assistant', 'Verified Riley payload 9706 (bn)', 'bn', 'llama3.2-r9706'),
    ('system', 'Verified Riley payload 9707 (sa)', 'sa', 'llama3.2-r9707'),
    ('user', 'Verified Riley payload 9708 (en)', 'en', 'llama3.2-r9708'),
    ('assistant', 'Verified Riley payload 9709 (hi)', 'hi', 'llama3.2-r9709'),
    ('system', 'Verified Riley payload 9710 (fr)', 'fr', 'llama3.2-r9710'),
    ('user', 'Verified Riley payload 9711 (es)', 'es', 'llama3.2-r9711'),
    ('assistant', 'Verified Riley payload 9712 (bn)', 'bn', 'llama3.2-r9712'),
    ('system', 'Verified Riley payload 9713 (sa)', 'sa', 'llama3.2-r9713'),
    ('user', 'Verified Riley payload 9714 (en)', 'en', 'llama3.2-r9714'),
    ('assistant', 'Verified Riley payload 9715 (hi)', 'hi', 'llama3.2-r9715'),
    ('system', 'Verified Riley payload 9716 (fr)', 'fr', 'llama3.2-r9716'),
    ('user', 'Verified Riley payload 9717 (es)', 'es', 'llama3.2-r9717'),
    ('assistant', 'Verified Riley payload 9718 (bn)', 'bn', 'llama3.2-r9718'),
    ('system', 'Verified Riley payload 9719 (sa)', 'sa', 'llama3.2-r9719'),
    ('user', 'Verified Riley payload 9720 (en)', 'en', 'llama3.2-r9720'),
    ('assistant', 'Verified Riley payload 9721 (hi)', 'hi', 'llama3.2-r9721'),
    ('system', 'Verified Riley payload 9722 (fr)', 'fr', 'llama3.2-r9722'),
]


def test_spec_batch_098() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
