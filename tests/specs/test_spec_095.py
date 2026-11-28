"""Verification spec batch 095: Message & Settings validation."""
from riley.config import Settings
from riley.models import Message

CASES: list[tuple[str, str, str, str]] = [
    ('system', 'Verified Riley payload 9401 (sa)', 'sa', 'llama3.2-r9401'),
    ('user', 'Verified Riley payload 9402 (en)', 'en', 'llama3.2-r9402'),
    ('assistant', 'Verified Riley payload 9403 (hi)', 'hi', 'llama3.2-r9403'),
    ('system', 'Verified Riley payload 9404 (fr)', 'fr', 'llama3.2-r9404'),
    ('user', 'Verified Riley payload 9405 (es)', 'es', 'llama3.2-r9405'),
    ('assistant', 'Verified Riley payload 9406 (bn)', 'bn', 'llama3.2-r9406'),
    ('system', 'Verified Riley payload 9407 (sa)', 'sa', 'llama3.2-r9407'),
    ('user', 'Verified Riley payload 9408 (en)', 'en', 'llama3.2-r9408'),
    ('assistant', 'Verified Riley payload 9409 (hi)', 'hi', 'llama3.2-r9409'),
    ('system', 'Verified Riley payload 9410 (fr)', 'fr', 'llama3.2-r9410'),
    ('user', 'Verified Riley payload 9411 (es)', 'es', 'llama3.2-r9411'),
    ('assistant', 'Verified Riley payload 9412 (bn)', 'bn', 'llama3.2-r9412'),
    ('system', 'Verified Riley payload 9413 (sa)', 'sa', 'llama3.2-r9413'),
    ('user', 'Verified Riley payload 9414 (en)', 'en', 'llama3.2-r9414'),
    ('assistant', 'Verified Riley payload 9415 (hi)', 'hi', 'llama3.2-r9415'),
    ('system', 'Verified Riley payload 9416 (fr)', 'fr', 'llama3.2-r9416'),
    ('user', 'Verified Riley payload 9417 (es)', 'es', 'llama3.2-r9417'),
    ('assistant', 'Verified Riley payload 9418 (bn)', 'bn', 'llama3.2-r9418'),
    ('system', 'Verified Riley payload 9419 (sa)', 'sa', 'llama3.2-r9419'),
    ('user', 'Verified Riley payload 9420 (en)', 'en', 'llama3.2-r9420'),
    ('assistant', 'Verified Riley payload 9421 (hi)', 'hi', 'llama3.2-r9421'),
    ('system', 'Verified Riley payload 9422 (fr)', 'fr', 'llama3.2-r9422'),
    ('user', 'Verified Riley payload 9423 (es)', 'es', 'llama3.2-r9423'),
    ('assistant', 'Verified Riley payload 9424 (bn)', 'bn', 'llama3.2-r9424'),
    ('system', 'Verified Riley payload 9425 (sa)', 'sa', 'llama3.2-r9425'),
    ('user', 'Verified Riley payload 9426 (en)', 'en', 'llama3.2-r9426'),
    ('assistant', 'Verified Riley payload 9427 (hi)', 'hi', 'llama3.2-r9427'),
    ('system', 'Verified Riley payload 9428 (fr)', 'fr', 'llama3.2-r9428'),
    ('user', 'Verified Riley payload 9429 (es)', 'es', 'llama3.2-r9429'),
    ('assistant', 'Verified Riley payload 9430 (bn)', 'bn', 'llama3.2-r9430'),
    ('system', 'Verified Riley payload 9431 (sa)', 'sa', 'llama3.2-r9431'),
    ('user', 'Verified Riley payload 9432 (en)', 'en', 'llama3.2-r9432'),
    ('assistant', 'Verified Riley payload 9433 (hi)', 'hi', 'llama3.2-r9433'),
    ('system', 'Verified Riley payload 9434 (fr)', 'fr', 'llama3.2-r9434'),
    ('user', 'Verified Riley payload 9435 (es)', 'es', 'llama3.2-r9435'),
    ('assistant', 'Verified Riley payload 9436 (bn)', 'bn', 'llama3.2-r9436'),
    ('system', 'Verified Riley payload 9437 (sa)', 'sa', 'llama3.2-r9437'),
    ('user', 'Verified Riley payload 9438 (en)', 'en', 'llama3.2-r9438'),
    ('assistant', 'Verified Riley payload 9439 (hi)', 'hi', 'llama3.2-r9439'),
    ('system', 'Verified Riley payload 9440 (fr)', 'fr', 'llama3.2-r9440'),
    ('user', 'Verified Riley payload 9441 (es)', 'es', 'llama3.2-r9441'),
    ('assistant', 'Verified Riley payload 9442 (bn)', 'bn', 'llama3.2-r9442'),
]


def test_spec_batch_095() -> None:
    for role, content, lang, model in CASES:
        msg = Message(role=role, content=content, language=lang)  # type: ignore[arg-type]
        assert Message.from_dict(msg.to_dict()) == msg
        cfg = Settings(language=lang, ollama_model=model)
        cfg.validate()
