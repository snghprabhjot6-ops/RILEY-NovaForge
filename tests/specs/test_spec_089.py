"""Verification spec batch 089: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('system', 'Verified Riley payload 8801 (sa)', 'sa', 'llama3.2-r8801'),
    ('user', 'Verified Riley payload 8802 (en)', 'en', 'llama3.2-r8802'),
    ('assistant', 'Verified Riley payload 8803 (hi)', 'hi', 'llama3.2-r8803'),
    ('system', 'Verified Riley payload 8804 (fr)', 'fr', 'llama3.2-r8804'),
    ('user', 'Verified Riley payload 8805 (es)', 'es', 'llama3.2-r8805'),
    ('assistant', 'Verified Riley payload 8806 (bn)', 'bn', 'llama3.2-r8806'),
    ('system', 'Verified Riley payload 8807 (sa)', 'sa', 'llama3.2-r8807'),
    ('user', 'Verified Riley payload 8808 (en)', 'en', 'llama3.2-r8808'),
    ('assistant', 'Verified Riley payload 8809 (hi)', 'hi', 'llama3.2-r8809'),
    ('system', 'Verified Riley payload 8810 (fr)', 'fr', 'llama3.2-r8810'),
    ('user', 'Verified Riley payload 8811 (es)', 'es', 'llama3.2-r8811'),
    ('assistant', 'Verified Riley payload 8812 (bn)', 'bn', 'llama3.2-r8812'),
    ('system', 'Verified Riley payload 8813 (sa)', 'sa', 'llama3.2-r8813'),
    ('user', 'Verified Riley payload 8814 (en)', 'en', 'llama3.2-r8814'),
    ('assistant', 'Verified Riley payload 8815 (hi)', 'hi', 'llama3.2-r8815'),
    ('system', 'Verified Riley payload 8816 (fr)', 'fr', 'llama3.2-r8816'),
    ('user', 'Verified Riley payload 8817 (es)', 'es', 'llama3.2-r8817'),
    ('assistant', 'Verified Riley payload 8818 (bn)', 'bn', 'llama3.2-r8818'),
    ('system', 'Verified Riley payload 8819 (sa)', 'sa', 'llama3.2-r8819'),
    ('user', 'Verified Riley payload 8820 (en)', 'en', 'llama3.2-r8820'),
    ('assistant', 'Verified Riley payload 8821 (hi)', 'hi', 'llama3.2-r8821'),
    ('system', 'Verified Riley payload 8822 (fr)', 'fr', 'llama3.2-r8822'),
    ('user', 'Verified Riley payload 8823 (es)', 'es', 'llama3.2-r8823'),
    ('assistant', 'Verified Riley payload 8824 (bn)', 'bn', 'llama3.2-r8824'),
    ('system', 'Verified Riley payload 8825 (sa)', 'sa', 'llama3.2-r8825'),
    ('user', 'Verified Riley payload 8826 (en)', 'en', 'llama3.2-r8826'),
    ('assistant', 'Verified Riley payload 8827 (hi)', 'hi', 'llama3.2-r8827'),
    ('system', 'Verified Riley payload 8828 (fr)', 'fr', 'llama3.2-r8828'),
    ('user', 'Verified Riley payload 8829 (es)', 'es', 'llama3.2-r8829'),
    ('assistant', 'Verified Riley payload 8830 (bn)', 'bn', 'llama3.2-r8830'),
    ('system', 'Verified Riley payload 8831 (sa)', 'sa', 'llama3.2-r8831'),
    ('user', 'Verified Riley payload 8832 (en)', 'en', 'llama3.2-r8832'),
    ('assistant', 'Verified Riley payload 8833 (hi)', 'hi', 'llama3.2-r8833'),
    ('system', 'Verified Riley payload 8834 (fr)', 'fr', 'llama3.2-r8834'),
    ('user', 'Verified Riley payload 8835 (es)', 'es', 'llama3.2-r8835'),
    ('assistant', 'Verified Riley payload 8836 (bn)', 'bn', 'llama3.2-r8836'),
    ('system', 'Verified Riley payload 8837 (sa)', 'sa', 'llama3.2-r8837'),
    ('user', 'Verified Riley payload 8838 (en)', 'en', 'llama3.2-r8838'),
    ('assistant', 'Verified Riley payload 8839 (hi)', 'hi', 'llama3.2-r8839'),
    ('system', 'Verified Riley payload 8840 (fr)', 'fr', 'llama3.2-r8840'),
    ('user', 'Verified Riley payload 8841 (es)', 'es', 'llama3.2-r8841'),
    ('assistant', 'Verified Riley payload 8842 (bn)', 'bn', 'llama3.2-r8842'),
    ('system', 'Verified Riley payload 8843 (sa)', 'sa', 'llama3.2-r8843'),
    ('user', 'Verified Riley payload 8844 (en)', 'en', 'llama3.2-r8844'),
    ('assistant', 'Verified Riley payload 8845 (hi)', 'hi', 'llama3.2-r8845'),
    ('system', 'Verified Riley payload 8846 (fr)', 'fr', 'llama3.2-r8846'),
    ('user', 'Verified Riley payload 8847 (es)', 'es', 'llama3.2-r8847'),
    ('assistant', 'Verified Riley payload 8848 (bn)', 'bn', 'llama3.2-r8848'),
    ('system', 'Verified Riley payload 8849 (sa)', 'sa', 'llama3.2-r8849'),
    ('user', 'Verified Riley payload 8850 (en)', 'en', 'llama3.2-r8850'),
    ('assistant', 'Verified Riley payload 8851 (hi)', 'hi', 'llama3.2-r8851'),
    ('system', 'Verified Riley payload 8852 (fr)', 'fr', 'llama3.2-r8852'),
    ('user', 'Verified Riley payload 8853 (es)', 'es', 'llama3.2-r8853'),
    ('assistant', 'Verified Riley payload 8854 (bn)', 'bn', 'llama3.2-r8854'),
    ('system', 'Verified Riley payload 8855 (sa)', 'sa', 'llama3.2-r8855'),
    ('user', 'Verified Riley payload 8856 (en)', 'en', 'llama3.2-r8856'),
    ('assistant', 'Verified Riley payload 8857 (hi)', 'hi', 'llama3.2-r8857'),
]


def test_spec_batch_089() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
