"""Verification spec batch 090: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('user', 'Verified Riley payload 8901 (es)', 'es', 'llama3.2-r8901'),
    ('assistant', 'Verified Riley payload 8902 (bn)', 'bn', 'llama3.2-r8902'),
    ('system', 'Verified Riley payload 8903 (sa)', 'sa', 'llama3.2-r8903'),
    ('user', 'Verified Riley payload 8904 (en)', 'en', 'llama3.2-r8904'),
    ('assistant', 'Verified Riley payload 8905 (hi)', 'hi', 'llama3.2-r8905'),
    ('system', 'Verified Riley payload 8906 (fr)', 'fr', 'llama3.2-r8906'),
    ('user', 'Verified Riley payload 8907 (es)', 'es', 'llama3.2-r8907'),
    ('assistant', 'Verified Riley payload 8908 (bn)', 'bn', 'llama3.2-r8908'),
    ('system', 'Verified Riley payload 8909 (sa)', 'sa', 'llama3.2-r8909'),
    ('user', 'Verified Riley payload 8910 (en)', 'en', 'llama3.2-r8910'),
    ('assistant', 'Verified Riley payload 8911 (hi)', 'hi', 'llama3.2-r8911'),
    ('system', 'Verified Riley payload 8912 (fr)', 'fr', 'llama3.2-r8912'),
    ('user', 'Verified Riley payload 8913 (es)', 'es', 'llama3.2-r8913'),
    ('assistant', 'Verified Riley payload 8914 (bn)', 'bn', 'llama3.2-r8914'),
    ('system', 'Verified Riley payload 8915 (sa)', 'sa', 'llama3.2-r8915'),
    ('user', 'Verified Riley payload 8916 (en)', 'en', 'llama3.2-r8916'),
    ('assistant', 'Verified Riley payload 8917 (hi)', 'hi', 'llama3.2-r8917'),
    ('system', 'Verified Riley payload 8918 (fr)', 'fr', 'llama3.2-r8918'),
    ('user', 'Verified Riley payload 8919 (es)', 'es', 'llama3.2-r8919'),
    ('assistant', 'Verified Riley payload 8920 (bn)', 'bn', 'llama3.2-r8920'),
    ('system', 'Verified Riley payload 8921 (sa)', 'sa', 'llama3.2-r8921'),
    ('user', 'Verified Riley payload 8922 (en)', 'en', 'llama3.2-r8922'),
    ('assistant', 'Verified Riley payload 8923 (hi)', 'hi', 'llama3.2-r8923'),
    ('system', 'Verified Riley payload 8924 (fr)', 'fr', 'llama3.2-r8924'),
    ('user', 'Verified Riley payload 8925 (es)', 'es', 'llama3.2-r8925'),
    ('assistant', 'Verified Riley payload 8926 (bn)', 'bn', 'llama3.2-r8926'),
    ('system', 'Verified Riley payload 8927 (sa)', 'sa', 'llama3.2-r8927'),
    ('user', 'Verified Riley payload 8928 (en)', 'en', 'llama3.2-r8928'),
    ('assistant', 'Verified Riley payload 8929 (hi)', 'hi', 'llama3.2-r8929'),
    ('system', 'Verified Riley payload 8930 (fr)', 'fr', 'llama3.2-r8930'),
    ('user', 'Verified Riley payload 8931 (es)', 'es', 'llama3.2-r8931'),
    ('assistant', 'Verified Riley payload 8932 (bn)', 'bn', 'llama3.2-r8932'),
    ('system', 'Verified Riley payload 8933 (sa)', 'sa', 'llama3.2-r8933'),
]


def test_spec_batch_090() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
