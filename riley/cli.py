from __future__ import annotations

import logging

from .assistant import RileyAssistant
from .backends import create_backend
from .config import Settings
from .exceptions import RileyError
from .history import ConversationHistory


HELP = "Commands: /listen, /history, /clear, /voice on, /voice off, /help, /quit"


def build_assistant(settings: Settings) -> RileyAssistant:
    return RileyAssistant(settings, create_backend(settings.backend, settings), ConversationHistory(settings.history_file))


def main() -> int:
    try:
        settings = Settings.from_env()
    except RileyError as exc:
        print(f"Configuration error: {exc}")
        return 2
    logging.basicConfig(level=getattr(logging, settings.log_level), format="%(levelname)s %(name)s: %(message)s")
    assistant = build_assistant(settings)
    try:
        assistant.start()
    except ValueError as exc:
        print(f"History warning: {exc}")
    voice_enabled = settings.voice_enabled
    print("RILEY — A Personal AI Assistant by NovaForge")
    print(HELP)
    while True:
        try:
            prompt = input("You: ").strip()
            if not prompt:
                continue
            command = prompt.casefold()
            if command in {"/quit", "/exit"}:
                print("Riley: Goodbye!")
                return 0
            if command == "/help":
                print(HELP)
                continue
            if command == "/clear":
                assistant.history.clear()
                print("Riley: Conversation history cleared.")
                continue
            if command == "/history":
                for message in assistant.history.messages:
                    print(f"{message.role.title()}: {message.content}")
                continue
            if command in {"/voice on", "/voice off"}:
                voice_enabled = command.endswith("on")
                print(f"Riley: Voice {'enabled' if voice_enabled else 'disabled'} for this session.")
                continue
            if command == "/listen":
                print("Riley: Listening…")
                prompt = assistant.listen()
                print(f"You: {prompt}")
            print(f"Riley: {assistant.respond(prompt, speak=voice_enabled)}")
        except (KeyboardInterrupt, EOFError):
            print("\nRiley: Goodbye!")
            return 0
        except (RileyError, ValueError) as exc:
            print(f"Riley: {exc}")
