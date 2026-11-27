import subprocess

from riley.voice import VoiceOutput


def test_macos_voice_prefers_requested_name(monkeypatch) -> None:
    output = VoiceOutput("Samantha")
    monkeypatch.setattr(
        subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(
            args[0], 0, stdout="Samantha              en_US    # Hello\nAlex                  en_US    # Hello\n"
        ),
    )
    assert output._select_macos_voice() == "Samantha"


def test_macos_voice_falls_back_to_feminine_hint(monkeypatch) -> None:
    output = VoiceOutput("Missing")
    monkeypatch.setattr(
        subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(
            args[0], 0, stdout="Victoria              en_US    # Hello\nAlex                  en_US    # Hello\n"
        ),
    )
    assert output._select_macos_voice() == "Victoria"
