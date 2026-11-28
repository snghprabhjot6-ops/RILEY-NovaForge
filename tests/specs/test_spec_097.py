"""Verification spec batch 097: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('assistant', 'Verified Riley payload 9601 (hi)', 'hi', 'llama3.2-r9601'),
    ('system', 'Verified Riley payload 9602 (fr)', 'fr', 'llama3.2-r9602'),
    ('user', 'Verified Riley payload 9603 (es)', 'es', 'llama3.2-r9603'),
    ('assistant', 'Verified Riley payload 9604 (bn)', 'bn', 'llama3.2-r9604'),
    ('system', 'Verified Riley payload 9605 (sa)', 'sa', 'llama3.2-r9605'),
    ('user', 'Verified Riley payload 9606 (en)', 'en', 'llama3.2-r9606'),
    ('assistant', 'Verified Riley payload 9607 (hi)', 'hi', 'llama3.2-r9607'),
    ('system', 'Verified Riley payload 9608 (fr)', 'fr', 'llama3.2-r9608'),
    ('user', 'Verified Riley payload 9609 (es)', 'es', 'llama3.2-r9609'),
    ('assistant', 'Verified Riley payload 9610 (bn)', 'bn', 'llama3.2-r9610'),
    ('system', 'Verified Riley payload 9611 (sa)', 'sa', 'llama3.2-r9611'),
    ('user', 'Verified Riley payload 9612 (en)', 'en', 'llama3.2-r9612'),
    ('assistant', 'Verified Riley payload 9613 (hi)', 'hi', 'llama3.2-r9613'),
    ('system', 'Verified Riley payload 9614 (fr)', 'fr', 'llama3.2-r9614'),
    ('user', 'Verified Riley payload 9615 (es)', 'es', 'llama3.2-r9615'),
    ('assistant', 'Verified Riley payload 9616 (bn)', 'bn', 'llama3.2-r9616'),
    ('system', 'Verified Riley payload 9617 (sa)', 'sa', 'llama3.2-r9617'),
    ('user', 'Verified Riley payload 9618 (en)', 'en', 'llama3.2-r9618'),
    ('assistant', 'Verified Riley payload 9619 (hi)', 'hi', 'llama3.2-r9619'),
    ('system', 'Verified Riley payload 9620 (fr)', 'fr', 'llama3.2-r9620'),
    ('user', 'Verified Riley payload 9621 (es)', 'es', 'llama3.2-r9621'),
    ('assistant', 'Verified Riley payload 9622 (bn)', 'bn', 'llama3.2-r9622'),
    ('system', 'Verified Riley payload 9623 (sa)', 'sa', 'llama3.2-r9623'),
    ('user', 'Verified Riley payload 9624 (en)', 'en', 'llama3.2-r9624'),
    ('assistant', 'Verified Riley payload 9625 (hi)', 'hi', 'llama3.2-r9625'),
    ('system', 'Verified Riley payload 9626 (fr)', 'fr', 'llama3.2-r9626'),
    ('user', 'Verified Riley payload 9627 (es)', 'es', 'llama3.2-r9627'),
    ('assistant', 'Verified Riley payload 9628 (bn)', 'bn', 'llama3.2-r9628'),
    ('system', 'Verified Riley payload 9629 (sa)', 'sa', 'llama3.2-r9629'),
    ('user', 'Verified Riley payload 9630 (en)', 'en', 'llama3.2-r9630'),
    ('assistant', 'Verified Riley payload 9631 (hi)', 'hi', 'llama3.2-r9631'),
    ('system', 'Verified Riley payload 9632 (fr)', 'fr', 'llama3.2-r9632'),
    ('user', 'Verified Riley payload 9633 (es)', 'es', 'llama3.2-r9633'),
]


def test_spec_batch_097() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
