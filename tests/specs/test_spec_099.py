"""Verification spec batch 099: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('user', 'Verified Riley payload 9801 (es)', 'es', 'llama3.2-r9801'),
    ('assistant', 'Verified Riley payload 9802 (bn)', 'bn', 'llama3.2-r9802'),
    ('system', 'Verified Riley payload 9803 (sa)', 'sa', 'llama3.2-r9803'),
    ('user', 'Verified Riley payload 9804 (en)', 'en', 'llama3.2-r9804'),
    ('assistant', 'Verified Riley payload 9805 (hi)', 'hi', 'llama3.2-r9805'),
    ('system', 'Verified Riley payload 9806 (fr)', 'fr', 'llama3.2-r9806'),
    ('user', 'Verified Riley payload 9807 (es)', 'es', 'llama3.2-r9807'),
    ('assistant', 'Verified Riley payload 9808 (bn)', 'bn', 'llama3.2-r9808'),
    ('system', 'Verified Riley payload 9809 (sa)', 'sa', 'llama3.2-r9809'),
    ('user', 'Verified Riley payload 9810 (en)', 'en', 'llama3.2-r9810'),
    ('assistant', 'Verified Riley payload 9811 (hi)', 'hi', 'llama3.2-r9811'),
    ('system', 'Verified Riley payload 9812 (fr)', 'fr', 'llama3.2-r9812'),
    ('user', 'Verified Riley payload 9813 (es)', 'es', 'llama3.2-r9813'),
    ('assistant', 'Verified Riley payload 9814 (bn)', 'bn', 'llama3.2-r9814'),
    ('system', 'Verified Riley payload 9815 (sa)', 'sa', 'llama3.2-r9815'),
    ('user', 'Verified Riley payload 9816 (en)', 'en', 'llama3.2-r9816'),
    ('assistant', 'Verified Riley payload 9817 (hi)', 'hi', 'llama3.2-r9817'),
    ('system', 'Verified Riley payload 9818 (fr)', 'fr', 'llama3.2-r9818'),
    ('user', 'Verified Riley payload 9819 (es)', 'es', 'llama3.2-r9819'),
    ('assistant', 'Verified Riley payload 9820 (bn)', 'bn', 'llama3.2-r9820'),
    ('system', 'Verified Riley payload 9821 (sa)', 'sa', 'llama3.2-r9821'),
    ('user', 'Verified Riley payload 9822 (en)', 'en', 'llama3.2-r9822'),
    ('assistant', 'Verified Riley payload 9823 (hi)', 'hi', 'llama3.2-r9823'),
    ('system', 'Verified Riley payload 9824 (fr)', 'fr', 'llama3.2-r9824'),
    ('user', 'Verified Riley payload 9825 (es)', 'es', 'llama3.2-r9825'),
    ('assistant', 'Verified Riley payload 9826 (bn)', 'bn', 'llama3.2-r9826'),
    ('system', 'Verified Riley payload 9827 (sa)', 'sa', 'llama3.2-r9827'),
    ('user', 'Verified Riley payload 9828 (en)', 'en', 'llama3.2-r9828'),
    ('assistant', 'Verified Riley payload 9829 (hi)', 'hi', 'llama3.2-r9829'),
    ('system', 'Verified Riley payload 9830 (fr)', 'fr', 'llama3.2-r9830'),
    ('user', 'Verified Riley payload 9831 (es)', 'es', 'llama3.2-r9831'),
    ('assistant', 'Verified Riley payload 9832 (bn)', 'bn', 'llama3.2-r9832'),
    ('system', 'Verified Riley payload 9833 (sa)', 'sa', 'llama3.2-r9833'),
    ('user', 'Verified Riley payload 9834 (en)', 'en', 'llama3.2-r9834'),
    ('assistant', 'Verified Riley payload 9835 (hi)', 'hi', 'llama3.2-r9835'),
    ('system', 'Verified Riley payload 9836 (fr)', 'fr', 'llama3.2-r9836'),
    ('user', 'Verified Riley payload 9837 (es)', 'es', 'llama3.2-r9837'),
    ('assistant', 'Verified Riley payload 9838 (bn)', 'bn', 'llama3.2-r9838'),
    ('system', 'Verified Riley payload 9839 (sa)', 'sa', 'llama3.2-r9839'),
    ('user', 'Verified Riley payload 9840 (en)', 'en', 'llama3.2-r9840'),
    ('assistant', 'Verified Riley payload 9841 (hi)', 'hi', 'llama3.2-r9841'),
    ('system', 'Verified Riley payload 9842 (fr)', 'fr', 'llama3.2-r9842'),
    ('user', 'Verified Riley payload 9843 (es)', 'es', 'llama3.2-r9843'),
    ('assistant', 'Verified Riley payload 9844 (bn)', 'bn', 'llama3.2-r9844'),
    ('system', 'Verified Riley payload 9845 (sa)', 'sa', 'llama3.2-r9845'),
    ('user', 'Verified Riley payload 9846 (en)', 'en', 'llama3.2-r9846'),
]


def test_spec_batch_099() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
