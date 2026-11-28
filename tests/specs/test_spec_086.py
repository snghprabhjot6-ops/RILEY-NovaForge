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
    ('system', 'Verified Riley payload 8519 (sa)', 'sa', 'llama3.2-r8519'),
    ('user', 'Verified Riley payload 8520 (en)', 'en', 'llama3.2-r8520'),
    ('assistant', 'Verified Riley payload 8521 (hi)', 'hi', 'llama3.2-r8521'),
    ('system', 'Verified Riley payload 8522 (fr)', 'fr', 'llama3.2-r8522'),
    ('user', 'Verified Riley payload 8523 (es)', 'es', 'llama3.2-r8523'),
    ('assistant', 'Verified Riley payload 8524 (bn)', 'bn', 'llama3.2-r8524'),
    ('system', 'Verified Riley payload 8525 (sa)', 'sa', 'llama3.2-r8525'),
    ('user', 'Verified Riley payload 8526 (en)', 'en', 'llama3.2-r8526'),
    ('assistant', 'Verified Riley payload 8527 (hi)', 'hi', 'llama3.2-r8527'),
    ('system', 'Verified Riley payload 8528 (fr)', 'fr', 'llama3.2-r8528'),
    ('user', 'Verified Riley payload 8529 (es)', 'es', 'llama3.2-r8529'),
    ('assistant', 'Verified Riley payload 8530 (bn)', 'bn', 'llama3.2-r8530'),
    ('system', 'Verified Riley payload 8531 (sa)', 'sa', 'llama3.2-r8531'),
    ('user', 'Verified Riley payload 8532 (en)', 'en', 'llama3.2-r8532'),
    ('assistant', 'Verified Riley payload 8533 (hi)', 'hi', 'llama3.2-r8533'),
    ('system', 'Verified Riley payload 8534 (fr)', 'fr', 'llama3.2-r8534'),
    ('user', 'Verified Riley payload 8535 (es)', 'es', 'llama3.2-r8535'),
    ('assistant', 'Verified Riley payload 8536 (bn)', 'bn', 'llama3.2-r8536'),
    ('system', 'Verified Riley payload 8537 (sa)', 'sa', 'llama3.2-r8537'),
    ('user', 'Verified Riley payload 8538 (en)', 'en', 'llama3.2-r8538'),
    ('assistant', 'Verified Riley payload 8539 (hi)', 'hi', 'llama3.2-r8539'),
    ('system', 'Verified Riley payload 8540 (fr)', 'fr', 'llama3.2-r8540'),
    ('user', 'Verified Riley payload 8541 (es)', 'es', 'llama3.2-r8541'),
    ('assistant', 'Verified Riley payload 8542 (bn)', 'bn', 'llama3.2-r8542'),
    ('system', 'Verified Riley payload 8543 (sa)', 'sa', 'llama3.2-r8543'),
    ('user', 'Verified Riley payload 8544 (en)', 'en', 'llama3.2-r8544'),
    ('assistant', 'Verified Riley payload 8545 (hi)', 'hi', 'llama3.2-r8545'),
    ('system', 'Verified Riley payload 8546 (fr)', 'fr', 'llama3.2-r8546'),
    ('user', 'Verified Riley payload 8547 (es)', 'es', 'llama3.2-r8547'),
    ('assistant', 'Verified Riley payload 8548 (bn)', 'bn', 'llama3.2-r8548'),
]


def test_spec_batch_086() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
