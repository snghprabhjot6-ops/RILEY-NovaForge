from __future__ import annotations

from dataclasses import dataclass

from .exceptions import SpeechInputError


@dataclass(slots=True)
class SpeechInput:
    engine: str = "sphinx"
    timeout: float = 5.0
    phrase_time_limit: float = 15.0

    def listen(self, locale: str) -> str:
        try:
            import speech_recognition as sr
        except ImportError as exc:
            raise SpeechInputError("SpeechRecognition is not installed") from exc

        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=self.timeout, phrase_time_limit=self.phrase_time_limit)
            if self.engine == "sphinx":
                result = recognizer.recognize_sphinx(audio, language=locale)
            elif self.engine == "google":
                result = recognizer.recognize_google(audio, language=locale)
            else:
                raise SpeechInputError(f"Unsupported speech engine: {self.engine}")
        except sr.WaitTimeoutError as exc:
            raise SpeechInputError("No speech was detected before the timeout") from exc
        except sr.UnknownValueError as exc:
            raise SpeechInputError("Riley could not understand the audio") from exc
        except sr.RequestError as exc:
            raise SpeechInputError(f"The speech engine is unavailable: {exc}") from exc
        except (OSError, AttributeError) as exc:
            raise SpeechInputError(f"The microphone is unavailable: {exc}") from exc
        return result.strip()
