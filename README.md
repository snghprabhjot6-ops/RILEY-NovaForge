# RILEY — A Personal AI Assistant by NovaForge

> Intelligence, with a human touch.

Riley is a personal assistant designed to make everyday interaction with software feel more natural: type or speak, choose a language, and let Riley respond in a recognizable female-voice experience where the operating system provides a suitable voice.

This repository contains a modular Python implementation and a responsive browser prototype. Riley is a NovaForge project.

## Project status

Riley is an early working implementation. It runs without an AI service or API key. The current conversational engine is a small, deterministic local backend—not a general-purpose language model.

### Implemented and tested

- Modular Python package and command-line personal assistant interface
- Configurable `local` and `echo` conversation backends
- Local conversational intents for greetings, help, time, date, thanks, and safe arithmetic
- English, Hindi, French, Bengali, Sanskrit, and Spanish response text
- Persistent conversation history stored outside tracked source files
- macOS speech output through the built-in `say` command
- Preference for the configured feminine voice (Samantha by default) when installed
- Portable speech-output fallback prepared for Windows through `pyttsx3`
- Microphone input through `SpeechRecognition`
- Offline-first recognition through PocketSphinx; optional Google recognition can be selected by configuration
- Environment-based, validated configuration with a safe `.env.example`
- Recoverable error handling and automated tests

### Implemented with environment-dependent behavior

- The exact voice depends on voices installed on the computer. Riley prefers the configured voice and then a feminine-named voice, but falls back safely if neither is available.
- Microphone access depends on operating-system permission and a working audio device.
- PocketSphinx language-model availability varies by selected language. The six-language text interface is implemented; offline speech recognition may need additional language data beyond English.
- Windows speech output has an implementation path but has not yet been verified on Windows hardware.

### Planned, not implemented

- A model-backed conversational provider
- Long-term memory and user profiles
- Calendar, email, reminders, and application integrations
- Image understanding and multimodal input
- Native desktop and mobile applications
- Wake-word activation and background operation
- Automated Windows test coverage and packaging

See [Project Status](docs/PROJECT_STATUS.md) and [Roadmap](docs/ROADMAP.md) for the evidence behind these labels.

## Installation on macOS

### 1. Prerequisites

- macOS with Python 3.11 or newer
- A working microphone for speech input
- Xcode Command Line Tools if your Python environment needs to compile an audio dependency
- Homebrew is recommended for installing PortAudio when PyAudio cannot use a prebuilt wheel

If PortAudio is needed:

```bash
brew install portaudio
```

### 2. Create an isolated environment

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3. Configure Riley

```bash
cp .env.example .env
```

The defaults use the local backend, English, macOS voice output, offline PocketSphinx speech recognition, and `.riley/history.json` for local conversation history. No API key is required.

Available languages: `en`, `hi`, `fr`, `bn`, `sa`, and `es`.

### 4. Start Riley

```bash
python -m riley
```

Inside Riley, use `/help` to see commands. `/listen` captures microphone input, `/history` shows the current history, `/clear` removes it, and `/voice off` disables speech for that session.

macOS may ask for microphone permission the first time Riley listens. Permission can be reviewed in **System Settings → Privacy & Security → Microphone**.

## Browser prototype

The responsive browser interface provides multilingual demo chat, coding and image/vision entry points, local image previews, and optional browser speech output and speech input where supported.

Run it by opening `index.html` in a modern browser, or serve the repository root with a static file server:

```sh
python3 -m http.server 8000
```

Then visit `http://localhost:8000`. The prototype does not connect to an AI service: chat and image analysis are not generated, and no messages or images are sent to a service. Browser speech recognition may use the browser or operating system’s speech service; check its privacy settings. Speech characteristics and available languages depend on installed browser and system voices.

## Automated tests

```bash
python -m pytest
```

The automated suite tests configuration validation, both backends, multilingual behavior, safe calculation, persistence, assistant orchestration, locale selection, and voice preference logic. It uses test doubles instead of activating the microphone or speakers.

## Configuration

| Variable | Default | Purpose |
|---|---|---|
| `RILEY_BACKEND` | `local` | Selects `local` or `echo` |
| `RILEY_LANGUAGE` | `en` | Chooses Riley's response language |
| `RILEY_VOICE_ENABLED` | `true` | Enables spoken responses |
| `RILEY_VOICE_NAME` | `Samantha` | Preferred installed voice |
| `RILEY_SPEECH_ENGINE` | `sphinx` | Selects offline `sphinx` or network-based `google` recognition |
| `RILEY_HISTORY_FILE` | `.riley/history.json` | Local conversation-history path |
| `RILEY_LOG_LEVEL` | `INFO` | Logging detail |

`.env` and Riley's runtime history are ignored by Git. Never commit credentials or private conversation data.

## Repository structure

```text
riley/                    Python application package
  backends/               Conversation backend interface and local implementations
  assistant.py            Assistant orchestration
  cli.py                  Personal assistant command-line interface
  config.py               Environment configuration and validation
  history.py              Atomic local conversation persistence
  speech.py               Speech-to-text input
  voice.py                macOS-first and portable speech output
tests/                    Automated tests
docs/                     Status and proposed roadmap
.github/ISSUE_TEMPLATE/   Structured issue forms
```

## Security and privacy

Riley does not require credentials in its current local configuration. Conversation history is written to a user-configurable local file with restrictive permissions where supported. The default speech engine is offline. Choosing the optional `google` speech engine sends audio through the recognition service used by the installed library.

Please read [SECURITY.md](SECURITY.md) before reporting a vulnerability. Licensing and distribution terms have not been declared; no license is implied by this repository.

## Contributing

Use the issue templates for bugs and proposals, and keep claims aligned with tested behavior. See [CONTRIBUTING.md](CONTRIBUTING.md).
