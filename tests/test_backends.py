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
