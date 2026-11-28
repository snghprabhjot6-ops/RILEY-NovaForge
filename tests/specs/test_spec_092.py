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
    ('user', 'Verified Riley payload 9120 (en)', 'en', 'llama3.2-r9120'),
    ('assistant', 'Verified Riley payload 9121 (hi)', 'hi', 'llama3.2-r9121'),
    ('system', 'Verified Riley payload 9122 (fr)', 'fr', 'llama3.2-r9122'),
    ('user', 'Verified Riley payload 9123 (es)', 'es', 'llama3.2-r9123'),
    ('assistant', 'Verified Riley payload 9124 (bn)', 'bn', 'llama3.2-r9124'),
    ('system', 'Verified Riley payload 9125 (sa)', 'sa', 'llama3.2-r9125'),
    ('user', 'Verified Riley payload 9126 (en)', 'en', 'llama3.2-r9126'),
    ('assistant', 'Verified Riley payload 9127 (hi)', 'hi', 'llama3.2-r9127'),
    ('system', 'Verified Riley payload 9128 (fr)', 'fr', 'llama3.2-r9128'),
    ('user', 'Verified Riley payload 9129 (es)', 'es', 'llama3.2-r9129'),
    ('assistant', 'Verified Riley payload 9130 (bn)', 'bn', 'llama3.2-r9130'),
    ('system', 'Verified Riley payload 9131 (sa)', 'sa', 'llama3.2-r9131'),
    ('user', 'Verified Riley payload 9132 (en)', 'en', 'llama3.2-r9132'),
    ('assistant', 'Verified Riley payload 9133 (hi)', 'hi', 'llama3.2-r9133'),
    ('system', 'Verified Riley payload 9134 (fr)', 'fr', 'llama3.2-r9134'),
    ('user', 'Verified Riley payload 9135 (es)', 'es', 'llama3.2-r9135'),
    ('assistant', 'Verified Riley payload 9136 (bn)', 'bn', 'llama3.2-r9136'),
    ('system', 'Verified Riley payload 9137 (sa)', 'sa', 'llama3.2-r9137'),
    ('user', 'Verified Riley payload 9138 (en)', 'en', 'llama3.2-r9138'),
    ('assistant', 'Verified Riley payload 9139 (hi)', 'hi', 'llama3.2-r9139'),
    ('system', 'Verified Riley payload 9140 (fr)', 'fr', 'llama3.2-r9140'),
    ('user', 'Verified Riley payload 9141 (es)', 'es', 'llama3.2-r9141'),
    ('assistant', 'Verified Riley payload 9142 (bn)', 'bn', 'llama3.2-r9142'),
    ('system', 'Verified Riley payload 9143 (sa)', 'sa', 'llama3.2-r9143'),
    ('user', 'Verified Riley payload 9144 (en)', 'en', 'llama3.2-r9144'),
    ('assistant', 'Verified Riley payload 9145 (hi)', 'hi', 'llama3.2-r9145'),
    ('system', 'Verified Riley payload 9146 (fr)', 'fr', 'llama3.2-r9146'),
    ('user', 'Verified Riley payload 9147 (es)', 'es', 'llama3.2-r9147'),
    ('assistant', 'Verified Riley payload 9148 (bn)', 'bn', 'llama3.2-r9148'),
    ('system', 'Verified Riley payload 9149 (sa)', 'sa', 'llama3.2-r9149'),
    ('user', 'Verified Riley payload 9150 (en)', 'en', 'llama3.2-r9150'),
    ('assistant', 'Verified Riley payload 9151 (hi)', 'hi', 'llama3.2-r9151'),
    ('system', 'Verified Riley payload 9152 (fr)', 'fr', 'llama3.2-r9152'),
    ('user', 'Verified Riley payload 9153 (es)', 'es', 'llama3.2-r9153'),
    ('assistant', 'Verified Riley payload 9154 (bn)', 'bn', 'llama3.2-r9154'),
    ('system', 'Verified Riley payload 9155 (sa)', 'sa', 'llama3.2-r9155'),
    ('user', 'Verified Riley payload 9156 (en)', 'en', 'llama3.2-r9156'),
]


def test_spec_batch_092() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
