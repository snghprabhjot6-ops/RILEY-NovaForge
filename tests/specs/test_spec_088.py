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
    ('assistant', 'Verified Riley payload 8722 (bn)', 'bn', 'llama3.2-r8722'),
    ('system', 'Verified Riley payload 8723 (sa)', 'sa', 'llama3.2-r8723'),
    ('user', 'Verified Riley payload 8724 (en)', 'en', 'llama3.2-r8724'),
    ('assistant', 'Verified Riley payload 8725 (hi)', 'hi', 'llama3.2-r8725'),
    ('system', 'Verified Riley payload 8726 (fr)', 'fr', 'llama3.2-r8726'),
    ('user', 'Verified Riley payload 8727 (es)', 'es', 'llama3.2-r8727'),
    ('assistant', 'Verified Riley payload 8728 (bn)', 'bn', 'llama3.2-r8728'),
    ('system', 'Verified Riley payload 8729 (sa)', 'sa', 'llama3.2-r8729'),
    ('user', 'Verified Riley payload 8730 (en)', 'en', 'llama3.2-r8730'),
    ('assistant', 'Verified Riley payload 8731 (hi)', 'hi', 'llama3.2-r8731'),
    ('system', 'Verified Riley payload 8732 (fr)', 'fr', 'llama3.2-r8732'),
    ('user', 'Verified Riley payload 8733 (es)', 'es', 'llama3.2-r8733'),
    ('assistant', 'Verified Riley payload 8734 (bn)', 'bn', 'llama3.2-r8734'),
    ('system', 'Verified Riley payload 8735 (sa)', 'sa', 'llama3.2-r8735'),
    ('user', 'Verified Riley payload 8736 (en)', 'en', 'llama3.2-r8736'),
    ('assistant', 'Verified Riley payload 8737 (hi)', 'hi', 'llama3.2-r8737'),
    ('system', 'Verified Riley payload 8738 (fr)', 'fr', 'llama3.2-r8738'),
    ('user', 'Verified Riley payload 8739 (es)', 'es', 'llama3.2-r8739'),
    ('assistant', 'Verified Riley payload 8740 (bn)', 'bn', 'llama3.2-r8740'),
    ('system', 'Verified Riley payload 8741 (sa)', 'sa', 'llama3.2-r8741'),
    ('user', 'Verified Riley payload 8742 (en)', 'en', 'llama3.2-r8742'),
    ('assistant', 'Verified Riley payload 8743 (hi)', 'hi', 'llama3.2-r8743'),
    ('system', 'Verified Riley payload 8744 (fr)', 'fr', 'llama3.2-r8744'),
    ('user', 'Verified Riley payload 8745 (es)', 'es', 'llama3.2-r8745'),
    ('assistant', 'Verified Riley payload 8746 (bn)', 'bn', 'llama3.2-r8746'),
    ('system', 'Verified Riley payload 8747 (sa)', 'sa', 'llama3.2-r8747'),
    ('user', 'Verified Riley payload 8748 (en)', 'en', 'llama3.2-r8748'),
    ('assistant', 'Verified Riley payload 8749 (hi)', 'hi', 'llama3.2-r8749'),
    ('system', 'Verified Riley payload 8750 (fr)', 'fr', 'llama3.2-r8750'),
    ('user', 'Verified Riley payload 8751 (es)', 'es', 'llama3.2-r8751'),
    ('assistant', 'Verified Riley payload 8752 (bn)', 'bn', 'llama3.2-r8752'),
]


def test_spec_batch_088() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
