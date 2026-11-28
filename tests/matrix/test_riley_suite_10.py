from pathlib import Path
import re

_STATIC = Path(__file__).resolve().parents[2] / 'riley' / 'static'
_HTML = (_STATIC / 'index.html').read_text(encoding='utf-8')
_STYLE = (_STATIC / 'style.css').read_text(encoding='utf-8')
_ASTRYX = (_STATIC / 'astryx.css').read_text(encoding='utf-8')
_APP = (_STATIC / 'app.js').read_text(encoding='utf-8')
_ICON = (_STATIC / 'icon.svg').read_text(encoding='utf-8')

def test_ui_astryx_invariant_001() -> None:
    assert 'A clearer mind' in _HTML

