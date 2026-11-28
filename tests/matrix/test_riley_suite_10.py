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

def test_ui_astryx_invariant_002() -> None:
    assert 'data-astryx-theme="neutral"' in _HTML

def test_ui_astryx_invariant_003() -> None:
    assert 'href="/astryx.css"' in _HTML

def test_ui_astryx_invariant_004() -> None:
    assert '✦' not in _HTML

def test_ui_astryx_invariant_005() -> None:
    assert '✦' not in _APP

def test_ui_astryx_invariant_006() -> None:
    assert '#b8a3f5' not in _ICON and '#c5aff6' not in _ICON

def test_ui_astryx_invariant_007() -> None:
    assert '#c5aff6' not in _STYLE and '#7450b9' not in _STYLE

def test_ui_astryx_invariant_008() -> None:
    assert 'class="orb"' not in _HTML

def test_ui_astryx_invariant_009() -> None:
    assert 'class="version"' not in _HTML

def test_ui_astryx_invariant_010() -> None:
    assert '<em>Riley.</em>' not in _HTML

def test_ui_astryx_invariant_011() -> None:
    assert 'YOUR CONVERSATIONS' not in _HTML

def test_ui_astryx_invariant_012() -> None:
    assert 'MAKE YOURSELF AT HOME' not in _HTML

def test_ui_astryx_invariant_013() -> None:
    assert 'A LITTLE INTELLIGENCE' not in _HTML

