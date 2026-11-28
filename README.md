# RILEY · A Personal AI Assistant by NovaForge

**Intelligence, with a human touch.**

Riley gives you a calm space to ask a question, work out a calculation, or have a conversation with a local AI model. Type or dictate, choose your language, and hear replies in an available installed voice. Riley is a **NovaForge** project.


1. Install **Python 3.11 or newer** from [python.org](https://www.python.org/downloads/windows/). Enable **Add python.exe to PATH**.
2. Download this repository using **Code → Download ZIP**, then **extract the whole ZIP**.
3. Double-click **`Start-Riley.bat`** in the extracted folder.

The first launch creates a private Python environment and downloads the small runtime dependency. Riley then opens at **http://127.0.0.1:8765** in your browser. Keep the launcher window open while using the app; press **Ctrl+C** in that window to stop it. No account or API key is needed for built-in mode.

See [the Windows guide](docs/WINDOWS.md) for troubleshooting, shortcuts, and the optional `.exe` build.

## What you can do

- Use a responsive chat interface with dark and light themes, a conversation sidebar, and keyboard shortcuts.
- Create separate conversations, return to saved chats, export a conversation as JSON, or delete it with confirmation.
- Choose English, Hindi, French, Bengali, Sanskrit, or Spanish response text.
- Use **built-in mode** for greetings, date, time, help, and safe arithmetic, with no model download.
- Connect **Ollama** for open-ended conversations with a model running on your computer.
- Read replies aloud using browser speech synthesis. Riley prefers an available feminine voice in the chosen language; Preferences lets you choose another installed voice.
- Dictate a message in a supported browser, review the text, and send it yourself.
- Continue using the modular Python CLI and optional native audio modules.

Built-in mode is a small deterministic assistant, **not a general-purpose AI model**. Select Ollama for broader questions. Calendar, email, computer control, wake words, and vision are future work; the app does not perform those actions.

## Full AI conversations with Ollama



```sh
ollama pull llama3.2
```

Open Riley → **Preferences** → choose **Ollama**, enter `llama3.2` (or another model you downloaded), and save. The first response can take longer while the model loads. Available languages and response quality depend on your model. Hardware and free memory determine which models you can run comfortably.

Riley connects to `http://127.0.0.1:11434` by default. It sends the recent conversation context and selected response language to your local Ollama service. It does not download a model automatically or silently substitute a different engine when Ollama fails.

## macOS / Linux / manual setup

Use Python 3.11 or newer. On macOS, `Start-Riley.command` also sets up and opens the app.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m riley.web
```

On Windows, activate with `.venv\Scripts\activate` instead. To use another port or suppress browser launch:

```sh
python -m riley.web --port 8766 --no-browser
```

You can also install the package with `python -m pip install .`, then run `riley-app` for the graphical interface or `riley` for the CLI.

## Voice and languages

The web app uses browser audio APIs and needs no Python audio packages. **Voice on** reads new replies; **Read aloud** speaks an existing reply. Installed voices differ across devices, and a feminine voice is not guaranteed for every language. Browser support varies: use Edge or Chrome for dictation where available. Audio hardware and live recognition have not been verified in this development environment.

Dictation is off until you start it and approve microphone access. Browser recognition may send audio to the browser vendor's service; the app explains this before starting. It inserts a draft and never sends the dictated message automatically. Built-in text chat remains available if audio is unsupported.


```sh
python -m pip install -r requirements-voice.txt
python -m riley
```

On macOS, CLI output uses `say`; portable output uses `pyttsx3`. CLI microphone input defaults to offline PocketSphinx, which may need additional language models. PyAudio may need PortAudio from your OS package manager. `/help`, `/listen`, `/history`, `/clear`, `/voice off`, and `/quit` are available.

## Configuration and data

Copy `.env.example` to `.env` if you want to change startup defaults. Web preferences are saved in your browser; they override the startup defaults for that browser.

| Variable | Default | Purpose |
|---|---|---|
| `RILEY_BACKEND` | `local` | `local`, `ollama`, or `echo` (testing) |
| `RILEY_LANGUAGE` | `en` | `en`, `hi`, `fr`, `bn`, `sa`, or `es` |
| `RILEY_OLLAMA_URL` | `http://127.0.0.1:11434` | Loopback HTTP model endpoint |
| `RILEY_OLLAMA_MODEL` | `llama3.2` | Installed Ollama model |
| `RILEY_HISTORY_FILE` | `.riley/history.json` | CLI history path; web `chats.db` lives beside it |
| `RILEY_VOICE_ENABLED` | `true` | CLI voice output; web voice starts off |
| `RILEY_VOICE_NAME` | `Samantha` | CLI preferred installed voice |
| `RILEY_SPEECH_ENGINE` | `sphinx` | CLI `sphinx` or network-based `google` recognition |
| `RILEY_LOG_LEVEL` | `INFO` | CLI logging level |

Source launches store chats in `.riley/chats.db` in the project directory. Packaged Windows launches use `%LOCALAPPDATA%\NovaForge\Riley\.riley\chats.db`. The CLI's older JSON history stays separate. Chats are stored locally as plaintext, not encrypted; use your OS account and disk protections for privacy. Browser preferences contain no conversation text. `.env` and runtime data are ignored by Git.

The web server listens on **127.0.0.1 only**, checks Host and Origin, and requires a per-launch token for writes. It serves a fixed asset list and renders model output as text rather than HTML. This is a **single-user local app**, not an authenticated public web service; do not expose it through a proxy or port forward.

## Development and verification

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
node --check riley/static/app.js
# Optional frontend development checks (Node.js 18+):
npm ci --ignore-scripts
npm test
```

The Python suite covers configuration, arithmetic, multilingual responses, history, voice selection, Ollama payloads and failures, chat persistence/isolation, API validation, CSRF protection, and retry behavior. It uses test doubles for models and audio. GitHub Actions runs the suite on Windows, macOS, and Linux with Python 3.11 and 3.13, then builds and smoke-tests a Windows executable. A workflow being configured does not by itself mean those remote checks have passed.

```text
riley/
  static/       Browser UI (HTML, CSS, JavaScript; no build step or CDN)
  web.py        Local HTTP application and API
  store.py      SQLite conversations
  backends/     Built-in, echo and Ollama conversation engines
  cli.py        Command-line assistant
  voice.py      Optional native speech output
  speech.py     Optional native speech input
tests/          Unit and HTTP integration tests
docs/           Windows setup, status, roadmap
```

See [Project Status](docs/PROJECT_STATUS.md), [Roadmap](docs/ROADMAP.md), [Contributing](CONTRIBUTING.md), and [Security](SECURITY.md). Licensing and distribution terms have not been declared; no license is implied.
