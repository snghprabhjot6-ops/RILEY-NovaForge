@echo off
setlocal
cd /d "%~dp0"
title RILEY by NovaForge
if exist ".venv\Scripts\python.exe" goto launch
where py >nul 2>nul
if not errorlevel 1 (
    py -3 -c "import sys; sys.exit(sys.version_info < (3,11))" >nul 2>nul
    if errorlevel 1 goto python_missing
    py -3 -m venv .venv
) else (
    where python >nul 2>nul
    if errorlevel 1 goto python_missing
    python -c "import sys; sys.exit(sys.version_info < (3,11))" >nul 2>nul
    if errorlevel 1 goto python_missing
    python -m venv .venv
)
if errorlevel 1 goto failed
:launch
".venv\Scripts\python.exe" -c "import dotenv" >nul 2>nul
if not errorlevel 1 goto ready
echo Setting up Riley for the first time. Internet access is needed for this step.
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto failed
:ready
".venv\Scripts\python.exe" -m riley.web
if errorlevel 1 goto failed
exit /b 0
:python_missing
echo Riley needs Python 3.11 or newer. Install it from https://www.python.org/downloads/windows/
echo Enable "Add python.exe to PATH", then open this file again.
pause
exit /b 1
:failed
echo Riley could not start. Review the error above. Setup help is in docs\WINDOWS.md.
pause
exit /b 1
