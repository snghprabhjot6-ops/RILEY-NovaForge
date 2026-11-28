"""Verification spec batch 094: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('assistant', 'Verified Riley payload 9301 (hi)', 'hi', 'llama3.2-r9301'),
    ('system', 'Verified Riley payload 9302 (fr)', 'fr', 'llama3.2-r9302'),
    ('user', 'Verified Riley payload 9303 (es)', 'es', 'llama3.2-r9303'),
    ('assistant', 'Verified Riley payload 9304 (bn)', 'bn', 'llama3.2-r9304'),
    ('system', 'Verified Riley payload 9305 (sa)', 'sa', 'llama3.2-r9305'),
    ('user', 'Verified Riley payload 9306 (en)', 'en', 'llama3.2-r9306'),
    ('assistant', 'Verified Riley payload 9307 (hi)', 'hi', 'llama3.2-r9307'),
    ('system', 'Verified Riley payload 9308 (fr)', 'fr', 'llama3.2-r9308'),
    ('user', 'Verified Riley payload 9309 (es)', 'es', 'llama3.2-r9309'),
    ('assistant', 'Verified Riley payload 9310 (bn)', 'bn', 'llama3.2-r9310'),
    ('system', 'Verified Riley payload 9311 (sa)', 'sa', 'llama3.2-r9311'),
    ('user', 'Verified Riley payload 9312 (en)', 'en', 'llama3.2-r9312'),
    ('assistant', 'Verified Riley payload 9313 (hi)', 'hi', 'llama3.2-r9313'),
    ('system', 'Verified Riley payload 9314 (fr)', 'fr', 'llama3.2-r9314'),
    ('user', 'Verified Riley payload 9315 (es)', 'es', 'llama3.2-r9315'),
    ('assistant', 'Verified Riley payload 9316 (bn)', 'bn', 'llama3.2-r9316'),
    ('system', 'Verified Riley payload 9317 (sa)', 'sa', 'llama3.2-r9317'),
    ('user', 'Verified Riley payload 9318 (en)', 'en', 'llama3.2-r9318'),
    ('assistant', 'Verified Riley payload 9319 (hi)', 'hi', 'llama3.2-r9319'),
    ('system', 'Verified Riley payload 9320 (fr)', 'fr', 'llama3.2-r9320'),
    ('user', 'Verified Riley payload 9321 (es)', 'es', 'llama3.2-r9321'),
    ('assistant', 'Verified Riley payload 9322 (bn)', 'bn', 'llama3.2-r9322'),
    ('system', 'Verified Riley payload 9323 (sa)', 'sa', 'llama3.2-r9323'),
    ('user', 'Verified Riley payload 9324 (en)', 'en', 'llama3.2-r9324'),
    ('assistant', 'Verified Riley payload 9325 (hi)', 'hi', 'llama3.2-r9325'),
    ('system', 'Verified Riley payload 9326 (fr)', 'fr', 'llama3.2-r9326'),
    ('user', 'Verified Riley payload 9327 (es)', 'es', 'llama3.2-r9327'),
    ('assistant', 'Verified Riley payload 9328 (bn)', 'bn', 'llama3.2-r9328'),
    ('system', 'Verified Riley payload 9329 (sa)', 'sa', 'llama3.2-r9329'),
    ('user', 'Verified Riley payload 9330 (en)', 'en', 'llama3.2-r9330'),
    ('assistant', 'Verified Riley payload 9331 (hi)', 'hi', 'llama3.2-r9331'),
    ('system', 'Verified Riley payload 9332 (fr)', 'fr', 'llama3.2-r9332'),
    ('user', 'Verified Riley payload 9333 (es)', 'es', 'llama3.2-r9333'),
    ('assistant', 'Verified Riley payload 9334 (bn)', 'bn', 'llama3.2-r9334'),
    ('system', 'Verified Riley payload 9335 (sa)', 'sa', 'llama3.2-r9335'),
    ('user', 'Verified Riley payload 9336 (en)', 'en', 'llama3.2-r9336'),
    ('assistant', 'Verified Riley payload 9337 (hi)', 'hi', 'llama3.2-r9337'),
    ('system', 'Verified Riley payload 9338 (fr)', 'fr', 'llama3.2-r9338'),
    ('user', 'Verified Riley payload 9339 (es)', 'es', 'llama3.2-r9339'),
    ('assistant', 'Verified Riley payload 9340 (bn)', 'bn', 'llama3.2-r9340'),
    ('system', 'Verified Riley payload 9341 (sa)', 'sa', 'llama3.2-r9341'),
    ('user', 'Verified Riley payload 9342 (en)', 'en', 'llama3.2-r9342'),
    ('assistant', 'Verified Riley payload 9343 (hi)', 'hi', 'llama3.2-r9343'),
]


def test_spec_batch_094() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
