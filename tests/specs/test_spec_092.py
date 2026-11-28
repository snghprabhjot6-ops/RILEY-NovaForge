"""Verification spec batch 092: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('system', 'Verified Riley payload 9101 (sa)', 'sa', 'llama3.2-r9101'),
    ('user', 'Verified Riley payload 9102 (en)', 'en', 'llama3.2-r9102'),
    ('assistant', 'Verified Riley payload 9103 (hi)', 'hi', 'llama3.2-r9103'),
    ('system', 'Verified Riley payload 9104 (fr)', 'fr', 'llama3.2-r9104'),
    ('user', 'Verified Riley payload 9105 (es)', 'es', 'llama3.2-r9105'),
    ('assistant', 'Verified Riley payload 9106 (bn)', 'bn', 'llama3.2-r9106'),
    ('system', 'Verified Riley payload 9107 (sa)', 'sa', 'llama3.2-r9107'),
    ('user', 'Verified Riley payload 9108 (en)', 'en', 'llama3.2-r9108'),
    ('assistant', 'Verified Riley payload 9109 (hi)', 'hi', 'llama3.2-r9109'),
    ('system', 'Verified Riley payload 9110 (fr)', 'fr', 'llama3.2-r9110'),
    ('user', 'Verified Riley payload 9111 (es)', 'es', 'llama3.2-r9111'),
    ('assistant', 'Verified Riley payload 9112 (bn)', 'bn', 'llama3.2-r9112'),
    ('system', 'Verified Riley payload 9113 (sa)', 'sa', 'llama3.2-r9113'),
    ('user', 'Verified Riley payload 9114 (en)', 'en', 'llama3.2-r9114'),
    ('assistant', 'Verified Riley payload 9115 (hi)', 'hi', 'llama3.2-r9115'),
    ('system', 'Verified Riley payload 9116 (fr)', 'fr', 'llama3.2-r9116'),
    ('user', 'Verified Riley payload 9117 (es)', 'es', 'llama3.2-r9117'),
    ('assistant', 'Verified Riley payload 9118 (bn)', 'bn', 'llama3.2-r9118'),
    ('system', 'Verified Riley payload 9119 (sa)', 'sa', 'llama3.2-r9119'),
]


def test_spec_batch_092() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
