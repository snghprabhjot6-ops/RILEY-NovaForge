"""Entry point for the optional PyInstaller Windows executable."""
import os
from pathlib import Path
import sys

from riley.web import main

if __name__ == '__main__':
    if getattr(sys, 'frozen', False):
        # Keep writable data out of Program Files / temporary extraction directories.
        directory = Path(os.getenv('LOCALAPPDATA', str(Path.home()))) / 'NovaForge' / 'Riley'
        directory.mkdir(parents=True, exist_ok=True)
        os.chdir(directory)
    raise SystemExit(main())
