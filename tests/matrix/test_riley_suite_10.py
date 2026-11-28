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

def test_ui_astryx_invariant_014() -> None:
    assert 'id="new-chat"' in _HTML and 'data-astryx-component="button"' in _HTML

def test_ui_astryx_invariant_015() -> None:
    assert 'id="send"' in _HTML and 'data-astryx-component="icon-button"' in _HTML

def test_ui_astryx_invariant_016() -> None:
    assert 'id="voice"' in _HTML and 'data-astryx-component="toggle-button"' in _HTML

def test_ui_astryx_invariant_017() -> None:
    assert 'id="mic"' in _HTML and 'data-astryx-component="toggle-button"' in _HTML

def test_ui_astryx_invariant_018() -> None:
    assert 'data-variant="destructive"' in _HTML

def test_ui_astryx_invariant_019() -> None:
    assert '@layer reset, astryx-base, astryx-theme;' in _ASTRYX

def test_ui_astryx_invariant_020() -> None:
    assert '.astryx-button {' in _ASTRYX

def test_ui_astryx_invariant_021() -> None:
    assert '.astryx-button[data-variant="primary"]' in _ASTRYX

def test_ui_astryx_invariant_022() -> None:
    assert '.astryx-button[data-variant="secondary"]' in _ASTRYX

def test_ui_astryx_invariant_023() -> None:
    assert '.astryx-button[data-variant="ghost"]' in _ASTRYX

def test_ui_astryx_invariant_024() -> None:
    assert '.astryx-button[data-variant="destructive"]' in _ASTRYX

def test_ui_astryx_invariant_025() -> None:
    assert '.astryx-toggle-button[aria-pressed="true"]' in _ASTRYX

def test_ui_astryx_invariant_026() -> None:
    assert '@scope ([data-astryx-theme="neutral"])' in _ASTRYX

def test_ui_astryx_invariant_027() -> None:
    assert 'forced-colors: active' in _ASTRYX

def test_ui_astryx_invariant_028() -> None:
    assert 'prefers-reduced-motion: reduce' in _ASTRYX

def test_ui_astryx_invariant_029() -> None:
    assert 'pointer-events: none;' in _ASTRYX

def test_ui_astryx_invariant_030() -> None:
    assert 'var(--color-background-body)' in _STYLE

def test_ui_astryx_invariant_031() -> None:
    assert 'var(--color-background-surface)' in _STYLE

def test_ui_astryx_invariant_032() -> None:
    assert 'var(--color-border)' in _STYLE

def test_ui_astryx_invariant_033() -> None:
    assert 'var(--spacing-4)' in _STYLE

def test_ui_astryx_invariant_034() -> None:
    assert 'var(--radius-container)' in _STYLE

def test_ui_astryx_invariant_035() -> None:
    assert 'select::picker-icon' in _STYLE

def test_ui_astryx_invariant_036() -> None:
    assert 'function createAstryxButton' in _APP

def test_ui_astryx_invariant_037() -> None:
    assert 'function createSvgIcon' in _APP

def test_ui_astryx_invariant_038() -> None:
    assert 'async function copyText' in _APP

def test_ui_astryx_invariant_039() -> None:
    assert 'm.role === "user" ? "Y" : "R"' in _APP

def test_ui_astryx_invariant_040() -> None:
    assert all(ch not in _HTML for ch in ('＋', '⚙', '◐', '⌫', '♩', '⌗', '☷', '◌'))

def test_ui_astryx_invariant_041() -> None:
    assert 'id="new-chat"' in _HTML

def test_ui_astryx_invariant_042() -> None:
    assert 'id="settings-open"' in _HTML

def test_ui_astryx_invariant_043() -> None:
    assert 'id="theme"' in _HTML

def test_ui_astryx_invariant_044() -> None:
    assert 'id="mobile-settings"' in _HTML

def test_ui_astryx_invariant_045() -> None:
    assert 'id="mobile-theme"' in _HTML

def test_ui_astryx_invariant_046() -> None:
    assert 'id="export"' in _HTML

def test_ui_astryx_invariant_047() -> None:
    assert 'id="delete"' in _HTML

def test_ui_astryx_invariant_048() -> None:
    assert 'id="mic"' in _HTML

def test_ui_astryx_invariant_049() -> None:
    assert 'id="voice"' in _HTML

def test_ui_astryx_invariant_050() -> None:
    assert 'id="send"' in _HTML

def test_ui_astryx_invariant_051() -> None:
    assert '--spacing-1' in _ASTRYX

def test_ui_astryx_invariant_052() -> None:
    assert '--spacing-2' in _ASTRYX

def test_ui_astryx_invariant_053() -> None:
    assert '--spacing-3' in _ASTRYX

def test_ui_astryx_invariant_054() -> None:
    assert '--spacing-4' in _ASTRYX

def test_ui_astryx_invariant_055() -> None:
    assert '--spacing-6' in _ASTRYX

def test_ui_astryx_invariant_056() -> None:
    assert '--spacing-8' in _ASTRYX

def test_ui_astryx_invariant_057() -> None:
    assert '--size-element-sm' in _ASTRYX

def test_ui_astryx_invariant_058() -> None:
    assert '--size-element-md' in _ASTRYX

def test_ui_astryx_invariant_059() -> None:
    assert '--size-element-lg' in _ASTRYX

def test_ui_astryx_invariant_060() -> None:
    assert '--radius-inner' in _ASTRYX

def test_ui_astryx_invariant_061() -> None:
    assert '--radius-element' in _ASTRYX

def test_ui_astryx_invariant_062() -> None:
    assert '--radius-container' in _ASTRYX

def test_ui_astryx_invariant_063() -> None:
    assert '--radius-full' in _ASTRYX

def test_ui_astryx_invariant_064() -> None:
    assert '--color-background-body' in _ASTRYX

def test_ui_astryx_invariant_065() -> None:
    assert '--color-background-surface' in _ASTRYX

def test_ui_astryx_invariant_066() -> None:
    assert '--color-accent' in _ASTRYX

def test_ui_astryx_invariant_067() -> None:
    assert '--color-on-accent' in _ASTRYX

