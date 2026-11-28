"""Verification spec batch 100: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('assistant', 'Verified Riley payload 9901 (hi)', 'hi', 'llama3.2-r9901'),
    ('system', 'Verified Riley payload 9902 (fr)', 'fr', 'llama3.2-r9902'),
    ('user', 'Verified Riley payload 9903 (es)', 'es', 'llama3.2-r9903'),
    ('assistant', 'Verified Riley payload 9904 (bn)', 'bn', 'llama3.2-r9904'),
    ('system', 'Verified Riley payload 9905 (sa)', 'sa', 'llama3.2-r9905'),
    ('user', 'Verified Riley payload 9906 (en)', 'en', 'llama3.2-r9906'),
    ('assistant', 'Verified Riley payload 9907 (hi)', 'hi', 'llama3.2-r9907'),
    ('system', 'Verified Riley payload 9908 (fr)', 'fr', 'llama3.2-r9908'),
    ('user', 'Verified Riley payload 9909 (es)', 'es', 'llama3.2-r9909'),
    ('assistant', 'Verified Riley payload 9910 (bn)', 'bn', 'llama3.2-r9910'),
    ('system', 'Verified Riley payload 9911 (sa)', 'sa', 'llama3.2-r9911'),
    ('user', 'Verified Riley payload 9912 (en)', 'en', 'llama3.2-r9912'),
    ('assistant', 'Verified Riley payload 9913 (hi)', 'hi', 'llama3.2-r9913'),
    ('system', 'Verified Riley payload 9914 (fr)', 'fr', 'llama3.2-r9914'),
    ('user', 'Verified Riley payload 9915 (es)', 'es', 'llama3.2-r9915'),
    ('assistant', 'Verified Riley payload 9916 (bn)', 'bn', 'llama3.2-r9916'),
    ('system', 'Verified Riley payload 9917 (sa)', 'sa', 'llama3.2-r9917'),
    ('user', 'Verified Riley payload 9918 (en)', 'en', 'llama3.2-r9918'),
    ('assistant', 'Verified Riley payload 9919 (hi)', 'hi', 'llama3.2-r9919'),
    ('system', 'Verified Riley payload 9920 (fr)', 'fr', 'llama3.2-r9920'),
    ('user', 'Verified Riley payload 9921 (es)', 'es', 'llama3.2-r9921'),
    ('assistant', 'Verified Riley payload 9922 (bn)', 'bn', 'llama3.2-r9922'),
]


def test_spec_batch_100() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
