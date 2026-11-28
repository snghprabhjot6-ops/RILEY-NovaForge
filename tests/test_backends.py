from riley.backends.echo import EchoBackend
from riley.backends.local import LocalBackend
from riley.models import Message


def user_message(content: str) -> list[Message]:
    return [Message(role="user", content=content)]


def test_local_backend_greeting() -> None:
    assert "Riley" in LocalBackend().generate(user_message("hello"), "en")


def test_local_backend_multilingual_greeting() -> None:
    assert "नमस्ते" in LocalBackend().generate(user_message("नमस्ते"), "hi")


def test_local_backend_calculates_safe_expression() -> None:
    assert "14" in LocalBackend().generate(user_message("calculate 2 + 3 * 4"), "en")


def test_local_backend_rejects_code_execution() -> None:
    response = LocalBackend().generate(user_message("calculate __import__('os').system('id')"), "en")
    assert "learning" in response


def test_echo_backend() -> None:
    assert EchoBackend().generate(user_message("test"), "en") == "You said: test"


def test_greeting_does_not_match_inside_words():
    assert 'learning' in LocalBackend().generate(user_message('Explain this thing'), 'en')


def test_calculation_rejects_complex_and_infinite_results():
    for prompt in ('calculate (-1)**0.5', 'calculate 1' + '0' * 99, 'calculate 9' + '**10' * 20):
        assert 'safely' in LocalBackend().generate(user_message(prompt), 'en')


def test_intent_word_boundaries_prevent_false_matches():
    backend = LocalBackend()
    assert 'learning' in backend.generate(user_message('Can you update my notes?'), 'en')
    assert 'learning' in backend.generate(user_message('Sometimes I write code'), 'en')
    assert 'learning' in backend.generate(user_message('That is unhelpful'), 'en')


def test_arithmetic_handles_punctuation_and_bare_expressions():
    backend = LocalBackend()
    assert '4' in backend.generate(user_message('what is 2 + 2?'), 'en')
    assert '150.' in backend.generate(user_message('calculate (1250 * 12) / 100'), 'en')
    assert '42' in backend.generate(user_message('6 * 7'), 'en')
