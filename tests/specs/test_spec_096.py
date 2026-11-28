"""Verification spec batch 096: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('user', 'Verified Riley payload 9501 (es)', 'es', 'llama3.2-r9501'),
    ('assistant', 'Verified Riley payload 9502 (bn)', 'bn', 'llama3.2-r9502'),
    ('system', 'Verified Riley payload 9503 (sa)', 'sa', 'llama3.2-r9503'),
    ('user', 'Verified Riley payload 9504 (en)', 'en', 'llama3.2-r9504'),
    ('assistant', 'Verified Riley payload 9505 (hi)', 'hi', 'llama3.2-r9505'),
    ('system', 'Verified Riley payload 9506 (fr)', 'fr', 'llama3.2-r9506'),
    ('user', 'Verified Riley payload 9507 (es)', 'es', 'llama3.2-r9507'),
    ('assistant', 'Verified Riley payload 9508 (bn)', 'bn', 'llama3.2-r9508'),
    ('system', 'Verified Riley payload 9509 (sa)', 'sa', 'llama3.2-r9509'),
    ('user', 'Verified Riley payload 9510 (en)', 'en', 'llama3.2-r9510'),
    ('assistant', 'Verified Riley payload 9511 (hi)', 'hi', 'llama3.2-r9511'),
    ('system', 'Verified Riley payload 9512 (fr)', 'fr', 'llama3.2-r9512'),
    ('user', 'Verified Riley payload 9513 (es)', 'es', 'llama3.2-r9513'),
    ('assistant', 'Verified Riley payload 9514 (bn)', 'bn', 'llama3.2-r9514'),
    ('system', 'Verified Riley payload 9515 (sa)', 'sa', 'llama3.2-r9515'),
    ('user', 'Verified Riley payload 9516 (en)', 'en', 'llama3.2-r9516'),
    ('assistant', 'Verified Riley payload 9517 (hi)', 'hi', 'llama3.2-r9517'),
    ('system', 'Verified Riley payload 9518 (fr)', 'fr', 'llama3.2-r9518'),
    ('user', 'Verified Riley payload 9519 (es)', 'es', 'llama3.2-r9519'),
    ('assistant', 'Verified Riley payload 9520 (bn)', 'bn', 'llama3.2-r9520'),
    ('system', 'Verified Riley payload 9521 (sa)', 'sa', 'llama3.2-r9521'),
    ('user', 'Verified Riley payload 9522 (en)', 'en', 'llama3.2-r9522'),
    ('assistant', 'Verified Riley payload 9523 (hi)', 'hi', 'llama3.2-r9523'),
    ('system', 'Verified Riley payload 9524 (fr)', 'fr', 'llama3.2-r9524'),
    ('user', 'Verified Riley payload 9525 (es)', 'es', 'llama3.2-r9525'),
    ('assistant', 'Verified Riley payload 9526 (bn)', 'bn', 'llama3.2-r9526'),
    ('system', 'Verified Riley payload 9527 (sa)', 'sa', 'llama3.2-r9527'),
    ('user', 'Verified Riley payload 9528 (en)', 'en', 'llama3.2-r9528'),
    ('assistant', 'Verified Riley payload 9529 (hi)', 'hi', 'llama3.2-r9529'),
    ('system', 'Verified Riley payload 9530 (fr)', 'fr', 'llama3.2-r9530'),
    ('user', 'Verified Riley payload 9531 (es)', 'es', 'llama3.2-r9531'),
]


def test_spec_batch_096() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
