from pathlib import Path

from riley.assistant import RileyAssistant
from riley.backends.echo import EchoBackend
from riley.config import Settings
from riley.history import ConversationHistory


class RecordingVoice:
    def __init__(self) -> None:
        self.spoken: list[str] = []

    def speak(self, text: str) -> None:
        self.spoken.append(text)


class FixedSpeech:
    def listen(self, locale: str) -> str:
        return f"heard:{locale}"


def test_assistant_records_both_sides_and_speaks(tmp_path: Path) -> None:
    voice = RecordingVoice()
    settings = Settings(history_file=tmp_path / "history.json")
    assistant = RileyAssistant(settings, EchoBackend(), ConversationHistory(settings.history_file), voice=voice)
    assistant.start()
    response = assistant.respond("Hello")
    assert response == "You said: Hello"
    assert [message.role for message in assistant.history.messages] == ["user", "assistant"]
    assert voice.spoken == [response]


def test_assistant_can_disable_speech(tmp_path: Path) -> None:
    voice = RecordingVoice()
    settings = Settings(history_file=tmp_path / "history.json")
    assistant = RileyAssistant(settings, EchoBackend(), ConversationHistory(settings.history_file), voice=voice)
    assistant.respond("Quiet", speak=False)
    assert voice.spoken == []


def test_assistant_uses_language_locale_for_listening(tmp_path: Path) -> None:
    settings = Settings(language="hi", history_file=tmp_path / "history.json")
    assistant = RileyAssistant(
        settings, EchoBackend(), ConversationHistory(settings.history_file), speech=FixedSpeech()
    )
    assert assistant.listen() == "heard:hi-IN"


def test_failed_backend_does_not_leave_an_unanswered_turn(tmp_path):
    import pytest
    from riley.exceptions import BackendError
    class FailedBackend:
        def generate(self, *args):
            raise RuntimeError('unavailable')
    settings = Settings(history_file=tmp_path/'history.json')
    assistant = RileyAssistant(settings, FailedBackend(), ConversationHistory(settings.history_file))
    with pytest.raises(BackendError):
        assistant.respond('hello', speak=False)
    assert assistant.history.messages == ()
