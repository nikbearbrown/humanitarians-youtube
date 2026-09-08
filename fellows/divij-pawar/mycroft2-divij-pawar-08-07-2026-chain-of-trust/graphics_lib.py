"""graphics_lib.py — house Manim helpers (real fonts + content-fitted boxes).

Registers the house type system (Montserrat / EB Garamond / PT Mono, per
runtime/design/DESIGN.md) with Pango at import time via
manimpango.register_font(), so Text(font=...) actually resolves them instead
of silently falling back to a generic default (verified: without this,
font="EB Garamond" / font="PT Mono" render as whatever Manim's system
fallback is, with no warning).

Font jobs (DESIGN.md "Typography — four fonts, four jobs"):
  DISPLAY (Montserrat) — titles, structural labels, chips. The default for
    almost everything in a diagram — "structural motion graphics are
    Montserrat, don't set a whole graphic in serif out of habit."
  SERIF (EB Garamond)  — editorial moments only: quotes, judgment lines.
  MONO (PT Mono)       — data, code, numbers. Never running prose.

auto_box() / surround_box() size a box to its actual content so a label can
never overflow its frame — the exact defect class (text clipped by its own
box) that kept recurring when boxes were hand-measured.

label_chip() is a solid-fill accent block with tracked caps — a real graphic
element (not a thin-stroke circle/line) for naming an entity or a key term.

checked() composes a checkmark/X glyph with a word: Montserrat (and most
display fonts) has NO glyph for ✓/✕ — Pango silently renders a '.notdef' box
showing the raw codepoint instead of erroring. The symbol must render in
Manim's default font (which resolves it); only the word takes DISPLAY.
"""
import os as _os
import manimpango as _mp

_FONT_DIR = r"C:\Users\divij\Desktop\mycroft\brutalist.art\runtime\fonts"
for _rel in (
    "Montserrat/static/Montserrat-Regular.ttf",
    "Montserrat/static/Montserrat-Bold.ttf",
    "Montserrat/static/Montserrat-Medium.ttf",
    "EB_Garamond/static/EBGaramond-Regular.ttf",
    "EB_Garamond/static/EBGaramond-Italic.ttf",
    "EB_Garamond/static/EBGaramond-Medium.ttf",
    "PT_Mono/PTMono-Regular.ttf",
):
    _p = _os.path.join(_FONT_DIR, _rel)
    if _os.path.exists(_p):
        _mp.register_font(_p)

from manim import *

DISPLAY = "Montserrat"
SERIF = "EB Garamond"
MONO = "PT Mono"

# Legibility floor (ai-explainer SKILL.md FILL-THE-CANVAS/TYPESIZE LAW):
# ~24px effective is a FLOOR, not a target. Never author a label under this.
FLOOR = 24


def _clamp(size):
    return max(size, FLOOR)


def label(text, size=28, color=None, weight=None, font=DISPLAY, **kw):
    """The default text unit — Montserrat, floor-clamped."""
    k = {"font_size": _clamp(size), "font": font, **kw}
    if color is not None:
        k["color"] = color
    if weight:
        k["weight"] = weight
    return Text(text, **k)


def title(text, size=48, color=None, **kw):
    return label(text, size=size, weight="BOLD", color=color, **kw).to_edge(UP, buff=0.7)


def mono(text, size=28, color=None, **kw):
    """Data / code / numbers only — never running prose."""
    return label(text, size=size, font=MONO, color=color, **kw)


def serif(text, size=28, color=None, italic=False, **kw):
    """Editorial voice only — a quote, a judgment line. Not the default."""
    k = dict(kw)
    if italic:
        k["slant"] = ITALIC
    return label(text, size=size, font=SERIF, color=color, **k)


def auto_box(content, h_pad=0.35, v_pad=0.28, color=None, stroke_width=2.5,
             fill_color=None, fill_opacity=0, **rect_kw):
    """A box sized to *content*'s actual bounding box, centered on it.
    Compose with VGroup(box, content) to get a movable unit."""
    box = Rectangle(
        width=content.width + 2 * h_pad,
        height=content.height + 2 * v_pad,
        color=color, stroke_width=stroke_width,
        fill_color=fill_color if fill_color is not None else color,
        fill_opacity=fill_opacity,
        **rect_kw,
    )
    box.move_to(content)
    return box


def surround_box(content, buff=0.3, color=None, stroke_width=2.5,
                  fill_color=None, fill_opacity=0, **rect_kw):
    """SurroundingRectangle sized at render time — safer for multi-line
    VGroups whose exact bounds aren't known until Manim lays them out."""
    return SurroundingRectangle(
        content, buff=buff, color=color, stroke_width=stroke_width,
        fill_color=fill_color if fill_color is not None else color,
        fill_opacity=fill_opacity,
        **rect_kw,
    )


def label_chip(text, accent, text_color=None, size=24, weight="BOLD",
               h_pad=0.3, v_pad=0.18, upper=True):
    """Solid accent block + tracked Montserrat caps — a real graphic mark
    for an entity name or key term, not a thin line of text."""
    t = label(text.upper() if upper else text, size=size,
              color=text_color if text_color is not None else "#FFFFFF",
              weight=weight)
    box = Rectangle(width=t.width + 2 * h_pad, height=t.height + 2 * v_pad,
                     fill_color=accent, fill_opacity=1, stroke_width=0)
    box.move_to(t)
    return VGroup(box, t)


def checked(text, size=26, color=None, weight=None, symbol="✓", buff=0.18,
            font=DISPLAY, trailing=False):
    """Checkmark/X + word, symbol in Manim's default font (real glyph),
    word in the house DISPLAY font. trailing=True puts the symbol after
    the word ('Structure enforced ✓') instead of before ('✓ Sourced')."""
    sym = Text(symbol, font_size=_clamp(size), color=color)
    word = label(text, size=size, color=color, weight=weight, font=font)
    parts = [word, sym] if trailing else [sym, word]
    return VGroup(*parts).arrange(RIGHT, buff=buff)
