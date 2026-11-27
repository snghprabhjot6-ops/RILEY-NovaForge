# Project Status

Last reviewed: 2026-11-26

This document separates observable implementation from product direction.

## Verified in source and automated tests

| Capability | Evidence | Notes |
|---|---|---|
| Modular assistant | `riley/assistant.py`, `riley/backends/` | Backends are isolated behind an abstract interface. |
| Local conversation | `riley/backends/local.py` | Deterministic intents; not a general-purpose model. |
| Backend selection | `riley/backends/factory.py`, `riley/config.py` | `local` and `echo` are available. |
| Multilingual text | `riley/backends/local.py` | Six response languages. |
| Conversation history | `riley/history.py` | Atomic JSON persistence and bounded history. |
| Voice selection | `riley/voice.py` | Prefers the configured voice, then feminine voice-name hints. |
| Speech input | `riley/speech.py` | Offline PocketSphinx or optional Google recognizer. |
| Configuration safety | `riley/config.py`, `.env.example`, `.gitignore` | Secrets and runtime history are excluded from Git. |
| Error handling | `riley/exceptions.py` and service boundaries | User-facing failures are recoverable. |
| Automated tests | `tests/` | No live microphone, speaker, or network calls. |

## Implemented but dependent on the host

- Speech output requires macOS `say` or a compatible `pyttsx3` environment.
- A specifically female-sounding voice cannot be guaranteed on every computer. Riley chooses Samantha by default when present and otherwise prefers an installed feminine-named voice.
- Speech recognition requires microphone permission and supported audio hardware.
- PocketSphinx needs appropriate language data for high-quality non-English recognition.
- Windows fallback code is present but not yet verified on a Windows machine.

## Preserved earlier work

The `copilot/add-ai-agent-riley` branch contains a browser-based prototype with `index.html`, `styles.css`, and `app.js`. It was inspected before this Python implementation was added and has not been overwritten or deleted.

## Not implemented

No model service, external personal-data integration, autonomous action system, computer vision model, wake word, or graphical Python desktop interface is included. These belong to the proposed roadmap.
