# Riley on Windows

## Double-click launch

1. Install Python 3.11+ from https://www.python.org/downloads/windows/ and enable **Add python.exe to PATH**.
2. Download the repository ZIP and use **Extract All**. Keep all files together.
3. Double-click `Start-Riley.bat`.
4. Allow the first-run dependency download to finish. Riley opens in your default browser.

The `.bat` uses `py -3` if available, falls back to `python`, creates `.venv`, installs the minimal runtime if missing, and starts the app. It does not need administrator access or change your system Python packages. Do not run it from inside the ZIP. You can make a desktop shortcut to this batch file.

Keep its terminal window open. Close the app with **Ctrl+C**, then close the window. Browser refresh does not stop or restart the server.

## Full AI mode

Install Ollama from https://ollama.com/, start it, and run `ollama pull llama3.2`. In Riley's Preferences, choose Ollama and enter the same model name. Otherwise, built-in mode works without Ollama for a limited set of offline tasks.

## Standalone executable

The **Riley checks and Windows app** GitHub Actions workflow builds `Riley.exe` after its cross-platform test jobs pass. Open a successful workflow run under **Actions**, download **Riley-Windows** from Artifacts, extract it, and open `Riley.exe`. Artifact availability depends on the workflow finishing successfully and GitHub's artifact retention. The executable does not require Python; Ollama remains a separate optional install.

The executable is unsigned. Do not bypass security warnings blindly; review the source/build provenance and use the source launcher if your system blocks it. No code-signing certificate or installer is included.

To build it yourself on Windows:

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt pyinstaller
.venv\Scripts\python.exe -m PyInstaller --noconfirm --clean --onefile --name Riley --add-data "riley/static;riley/static" desktop.py
```

Output: `dist\Riley.exe`. Build Windows binaries on Windows. The console stays visible so you can diagnose startup problems and stop the local server.

## Troubleshooting

| Problem | What to do |
|---|---|
| Python missing / Microsoft Store opens | Install Python from python.org, enable PATH, and relaunch. |
| Setup fails | Check your connection; run `.venv\Scripts\python.exe -m pip install -r requirements.txt` from the extracted folder to see the error. |
| Port already in use | Stop the other Riley window, or run `.venv\Scripts\python.exe -m riley.web --port 8766`. |
| Browser did not open | Open the exact `http://127.0.0.1:8765` URL shown in the terminal. `localhost` is intentionally not accepted by Host checks. |
| Cannot reach Riley after launch | Keep the terminal open. Check its error output and retry. |
| Ollama unavailable | Start Ollama, check the model name, and run `ollama pull` for that model. Your draft remains available to retry. |
| No voice / wrong voice | Choose a voice in Preferences; install the desired language voice through Windows settings if needed. |
| No microphone button support | Try Edge or Chrome; text chat works independently. Check browser microphone permissions. |
| Need a fresh local setup | Stop Riley, back up `.riley` if you want to keep chats, then remove only `.venv` and reopen the launcher. |

The UI uses your browser as its window. Native Windows hardware/audio behavior must still be checked on your machine; automated server tests do not verify your microphone or speakers.
