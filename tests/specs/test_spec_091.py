"""Verification spec batch 091: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('assistant', 'Verified Riley payload 9001 (hi)', 'hi', 'llama3.2-r9001'),
    ('system', 'Verified Riley payload 9002 (fr)', 'fr', 'llama3.2-r9002'),
    ('user', 'Verified Riley payload 9003 (es)', 'es', 'llama3.2-r9003'),
    ('assistant', 'Verified Riley payload 9004 (bn)', 'bn', 'llama3.2-r9004'),
    ('system', 'Verified Riley payload 9005 (sa)', 'sa', 'llama3.2-r9005'),
    ('user', 'Verified Riley payload 9006 (en)', 'en', 'llama3.2-r9006'),
    ('assistant', 'Verified Riley payload 9007 (hi)', 'hi', 'llama3.2-r9007'),
    ('system', 'Verified Riley payload 9008 (fr)', 'fr', 'llama3.2-r9008'),
    ('user', 'Verified Riley payload 9009 (es)', 'es', 'llama3.2-r9009'),
    ('assistant', 'Verified Riley payload 9010 (bn)', 'bn', 'llama3.2-r9010'),
    ('system', 'Verified Riley payload 9011 (sa)', 'sa', 'llama3.2-r9011'),
    ('user', 'Verified Riley payload 9012 (en)', 'en', 'llama3.2-r9012'),
    ('assistant', 'Verified Riley payload 9013 (hi)', 'hi', 'llama3.2-r9013'),
    ('system', 'Verified Riley payload 9014 (fr)', 'fr', 'llama3.2-r9014'),
    ('user', 'Verified Riley payload 9015 (es)', 'es', 'llama3.2-r9015'),
    ('assistant', 'Verified Riley payload 9016 (bn)', 'bn', 'llama3.2-r9016'),
    ('system', 'Verified Riley payload 9017 (sa)', 'sa', 'llama3.2-r9017'),
    ('user', 'Verified Riley payload 9018 (en)', 'en', 'llama3.2-r9018'),
    ('assistant', 'Verified Riley payload 9019 (hi)', 'hi', 'llama3.2-r9019'),
    ('system', 'Verified Riley payload 9020 (fr)', 'fr', 'llama3.2-r9020'),
    ('user', 'Verified Riley payload 9021 (es)', 'es', 'llama3.2-r9021'),
    ('assistant', 'Verified Riley payload 9022 (bn)', 'bn', 'llama3.2-r9022'),
    ('system', 'Verified Riley payload 9023 (sa)', 'sa', 'llama3.2-r9023'),
    ('user', 'Verified Riley payload 9024 (en)', 'en', 'llama3.2-r9024'),
    ('assistant', 'Verified Riley payload 9025 (hi)', 'hi', 'llama3.2-r9025'),
    ('system', 'Verified Riley payload 9026 (fr)', 'fr', 'llama3.2-r9026'),
    ('user', 'Verified Riley payload 9027 (es)', 'es', 'llama3.2-r9027'),
    ('assistant', 'Verified Riley payload 9028 (bn)', 'bn', 'llama3.2-r9028'),
    ('system', 'Verified Riley payload 9029 (sa)', 'sa', 'llama3.2-r9029'),
    ('user', 'Verified Riley payload 9030 (en)', 'en', 'llama3.2-r9030'),
    ('assistant', 'Verified Riley payload 9031 (hi)', 'hi', 'llama3.2-r9031'),
    ('system', 'Verified Riley payload 9032 (fr)', 'fr', 'llama3.2-r9032'),
    ('user', 'Verified Riley payload 9033 (es)', 'es', 'llama3.2-r9033'),
    ('assistant', 'Verified Riley payload 9034 (bn)', 'bn', 'llama3.2-r9034'),
    ('system', 'Verified Riley payload 9035 (sa)', 'sa', 'llama3.2-r9035'),
]


def test_spec_batch_091() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
