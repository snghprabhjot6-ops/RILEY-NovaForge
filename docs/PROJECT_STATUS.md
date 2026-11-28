# Project status

Reviewed: 2026-11-27

## Implemented

- Modular Python assistant and CLI, with built-in and echo engines.
- Responsive browser UI, light/dark appearance, preferences and six response languages.
- Separate SQLite conversations with persistence, export and confirmed deletion.
- Optional local Ollama backend with bounded recent context and actionable connection errors.
- Browser dictation with disclosure, microphone permission and draft review; browser speech output with voice selection.
- Windows double-click source launcher and macOS/Linux launcher.
- Python packaging with UI assets, plus a Windows PyInstaller entry point.
- GitHub Actions test matrix and Windows executable build/smoke-test workflow.
- Loopback binding, Host/Origin checks, write token, fixed static asset routing, and text-only message rendering.

## Validation boundaries

The Python tests run locally without live audio or model inference. Ollama requests are tested with a fake transport; successful real-model generation depends on a running service and downloaded model. JavaScript syntax and DOM interactions can be checked separately. A browser preview could not connect to the isolated development server, so a visual browser inspection was not completed in this environment.

Windows launch scripts and packaging are supplied, with remote CI configured to validate the binary. Do not describe an executable as built or verified until the workflow has actually passed. No physical Windows microphone/speaker test or guarantee of installed feminine voices is implied.

## Data and limitations

This is a single-user local app. Chats are unencrypted local SQLite data; CLI JSON history is separate. Built-in mode is deterministic, while Ollama is optional model-backed conversation. Browser dictation may send audio to the vendor's recognition service. The app does not perform external actions or access personal files, email, calendars, or devices.

The earlier browser prototype is preserved on `copilot/add-ai-agent-riley`.
