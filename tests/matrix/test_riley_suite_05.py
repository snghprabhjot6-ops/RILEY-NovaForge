from riley.backends.local import LocalBackend, TEXT
from riley.models import Message

_BACKEND = LocalBackend()

def test_multilingual_en_hello_001() -> None:
    reply = _BACKEND.generate([Message('user', 'hello', language='en')], 'en')
    assert reply == TEXT['en']['hello']

def test_multilingual_en_help_002() -> None:
    reply = _BACKEND.generate([Message('user', 'Can you help me?', language='en')], 'en')
    assert reply == TEXT['en']['help']

def test_multilingual_en_thanks_003() -> None:
    reply = _BACKEND.generate([Message('user', 'thanks!', language='en')], 'en')
    assert reply == TEXT['en']['thanks']

def test_multilingual_en_time_004() -> None:
    reply = _BACKEND.generate([Message('user', 'What time is it?', language='en')], 'en')
    assert reply.startswith(TEXT['en']['time'].split('{value}')[0])

def test_multilingual_en_date_005() -> None:
    reply = _BACKEND.generate([Message('user', "What is today's date?", language='en')], 'en')
    assert reply.startswith(TEXT['en']['date'].split('{value}')[0])

def test_multilingual_en_unknown_006() -> None:
    reply = _BACKEND.generate([Message('user', 'random topic alpha', language='en')], 'en')
    assert reply == TEXT['en']['unknown']

def test_multilingual_hi_hello_007() -> None:
    reply = _BACKEND.generate([Message('user', 'नमस्ते', language='hi')], 'hi')
    assert reply == TEXT['hi']['hello']

def test_multilingual_hi_help_008() -> None:
    reply = _BACKEND.generate([Message('user', 'सहायता चाहिए', language='hi')], 'hi')
    assert reply == TEXT['hi']['help']

def test_multilingual_hi_thanks_009() -> None:
    reply = _BACKEND.generate([Message('user', 'धन्यवाद', language='hi')], 'hi')
    assert reply == TEXT['hi']['thanks']

def test_multilingual_hi_time_010() -> None:
    reply = _BACKEND.generate([Message('user', 'समय क्या है', language='hi')], 'hi')
    assert reply.startswith(TEXT['hi']['time'].split('{value}')[0])

def test_multilingual_hi_date_011() -> None:
    reply = _BACKEND.generate([Message('user', 'आज की तारीख', language='hi')], 'hi')
    assert reply.startswith(TEXT['hi']['date'].split('{value}')[0])

def test_multilingual_hi_unknown_012() -> None:
    reply = _BACKEND.generate([Message('user', 'अज्ञात विषय', language='hi')], 'hi')
    assert reply == TEXT['hi']['unknown']

def test_multilingual_fr_hello_013() -> None:
    reply = _BACKEND.generate([Message('user', 'bonjour', language='fr')], 'fr')
    assert reply == TEXT['fr']['hello']

def test_multilingual_fr_help_014() -> None:
    reply = _BACKEND.generate([Message('user', "besoin d'aide", language='fr')], 'fr')
    assert reply == TEXT['fr']['help']

