#!/usr/bin/env python3
"""
render_scenes.py — out-of-tree scene renderer for "What Is a Concept Map".

Built to the art direction in 2026-08-28-what-is-a-concept-map.md, verbatim:
four palette values, two type families, 12-col visible grid, border-radius 0,
no gradients / shadows / glows / blur, hard cuts only, 2-frame step reveals or
hard snaps, 4 px borders, exposed mono labels on every panel.

Nothing here writes into the brutalist toolkit. Output is per-beat mp4 in
media/, which brutalist's compile.py picks up via resolve_slot() at the top
slot precedence (media/<beat>.mp4).

Frame-exactness: every beat is assembled from unique state PNGs hard-linked
into a per-frame sequence, then encoded with -framerate 24. No concat-demuxer
duration rounding, so a 6-frame wipe is exactly 6 frames.

Usage:
    python3 render_scenes.py --aspect 16:9   --out ../media
    python3 render_scenes.py --aspect 9:16   --out ../short/media
"""
import argparse
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FPS = 24

# ── palette — four values, no more ────────────────────────────────────────────
GROUND = (0x0A, 0x0A, 0x0A)   # near-black, never pure black
PAPER  = (0xF2, 0xF0, 0xEB)   # warm off-white, never pure white
SIGNAL = (0xE8, 0x45, 0x2C)   # the ONE accent
MUTE   = (0x6B, 0x6B, 0x6B)   # secondary labels, inactive states
BLACK  = (0x00, 0x00, 0x00)   # only for the final hard cut to black

# ── type — two families total, no third ──────────────────────────────────────
# Display/headline: one grotesk, weight 700+, tracking tight to -2%.
#   The script names Archivo / Inter Tight / Helvetica Now. None are installed;
#   Helvetica Neue Bold is the nearest available true grotesk at weight 700.
# Data/labels: one mono, weight 400/700.
#   The script names JetBrains Mono / IBM Plex Mono. Neither is installed;
#   Menlo ships Regular + Bold, giving the required 400/700 pair.
DISPLAY_TTC = "/System/Library/Fonts/HelveticaNeue.ttc"
DISPLAY_IDX = 1   # Bold
MONO_TTC    = "/System/Library/Fonts/Menlo.ttc"
MONO_R, MONO_B = 0, 1

_font_cache = {}


def font(kind, size):
    key = (kind, size)
    if key not in _font_cache:
        if kind == "display":
            f = ImageFont.truetype(DISPLAY_TTC, size, index=DISPLAY_IDX)
        elif kind == "mono":
            f = ImageFont.truetype(MONO_TTC, size, index=MONO_R)
        elif kind == "monob":
            f = ImageFont.truetype(MONO_TTC, size, index=MONO_B)
        else:
            raise ValueError(kind)
        _font_cache[key] = f
    return _font_cache[key]


def blend(fg, bg, alpha):
    return tuple(int(round(f * alpha + b * (1 - alpha))) for f, b in zip(fg, bg))


GRID_INK = blend(MUTE, GROUND, 0.12)   # 1 px #6B6B6B at 12% opacity


# ── layout ───────────────────────────────────────────────────────────────────
class Layout:
    """12 columns · outer margin · gutter. Sizes from the script's 4K table."""

    def __init__(self, w, h):
        self.w, self.h = w, h
        self.portrait = h > w
        if self.portrait:
            # 2160x3840. Margin scaled to the narrower frame; type stays large
            # so it survives a phone screen (the vertical cut's whole job).
            self.margin = 120
            self.grid_w = 3
            self.s = 1.18          # type scale for portrait legibility
        else:
            self.margin = 160
            self.grid_w = 2
            self.s = 1.0
        self.gutter = 120 if not self.portrait else 72
        self.cols = 12
        inner = self.w - 2 * self.margin
        self.col = (inner - self.gutter * (self.cols - 1)) / self.cols
        # type scale
        self.display = int(320 * self.s * (0.72 if self.portrait else 1.0))
        self.h1      = int(180 * self.s * (0.80 if self.portrait else 1.0))
        self.h2      = int(96 * self.s)
        self.body    = int(64 * self.s)
        self.data    = int(44 * self.s)
        self.caption = int(32 * self.s)

    def x(self, col):
        """Left edge of column `col` (0-indexed)."""
        return self.margin + col * (self.col + self.gutter)

    def span(self, ncols):
        return ncols * self.col + (ncols - 1) * self.gutter

    @property
    def right(self):
        return self.w - self.margin

    @property
    def bottom(self):
        return self.h - self.margin


def new_frame(L, bg=GROUND, grid=True):
    im = Image.new("RGB", (L.w, L.h), bg)
    d = ImageDraw.Draw(im)
    if grid and bg == GROUND:
        # The scaffolding is part of the look.
        for c in range(L.cols):
            x0 = L.x(c)
            d.rectangle([x0, 0, x0 + L.grid_w - 1, L.h], fill=GRID_INK)
            x1 = x0 + L.col
            d.rectangle([x1, 0, x1 + L.grid_w - 1, L.h], fill=GRID_INK)
        for y in (L.margin, L.h - L.margin):
            d.rectangle([0, y, L.w, y + L.grid_w - 1], fill=GRID_INK)
    return im, d


# ── text helpers ─────────────────────────────────────────────────────────────
def tracked_width(text, f, tracking):
    if not text:
        return 0
    return sum(f.getlength(ch) for ch in text) + tracking * (len(text) - 1)


def tt(d, xy, text, f, fill, tracking=0.0, center=False, right=False):
    """Draw text with letter tracking. PIL has no tracking, so step per char."""
    x, y = xy
    w = tracked_width(text, f, tracking)
    if center:
        x -= w / 2
    elif right:
        x -= w
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill)
        x += f.getlength(ch) + tracking
    return w


def display_line(d, xy, text, L, fill=PAPER, center=False, size=None):
    """Display type, tracking tight to -2%."""
    size = size or L.display
    f = font("display", size)
    return tt(d, xy, text, f, fill, tracking=-0.02 * size, center=center)


def mono(d, xy, text, size, fill=PAPER, bold=False, center=False, right=False):
    f = font("monob" if bold else "mono", size)
    return tt(d, xy, text, f, fill, 0.0, center=center, right=right)


def panel_label(d, L, text, x, y, fill=MUTE):
    """Every panel gets an exposed label in mono caps."""
    mono(d, (x, y), text, L.caption, fill=fill, bold=True)


def rule(d, x0, y0, x1, y1, fill=PAPER, w=4):
    """Borders are 4 px, visible. border-radius: 0 everywhere."""
    d.rectangle([min(x0, x1), min(y0, y1),
                 max(x0, x1) + (w - 1 if y0 == y1 else 0),
                 max(y0, y1) + (w - 1 if x0 == x1 else 0)], fill=fill)


def hrule(d, x0, x1, y, fill=PAPER, w=4):
    d.rectangle([x0, y, x1, y + w - 1], fill=fill)


def vrule(d, y0, y1, x, fill=PAPER, w=4):
    d.rectangle([x, y0, x + w - 1, y1], fill=fill)


def box(d, x0, y0, x1, y1, fill=PAPER, w=4, bg=None):
    if bg is not None:
        d.rectangle([x0, y0, x1, y1], fill=bg)
    hrule(d, x0, x1, y0, fill, w)
    hrule(d, x0, x1, y1 - w + 1, fill, w)
    vrule(d, y0, y1, x0, fill, w)
    vrule(d, y0, y1, x1 - w + 1, fill, w)


def arrow_v(d, x, y0, y1, fill, w=4, head=26):
    """Straight vertical arrow. No curves, no decoration."""
    vrule(d, min(y0, y1), max(y0, y1), x - w // 2, fill, w)
    s = 1 if y1 > y0 else -1
    d.polygon([(x, y1), (x - head, y1 - s * head), (x + head, y1 - s * head)], fill=fill)


def arrow_h(d, y, x0, x1, fill, w=4, head=26):
    hrule(d, min(x0, x1), max(x0, x1), y - w // 2, fill, w)
    s = 1 if x1 > x0 else -1
    d.polygon([(x1, y), (x1 - s * head, y - head), (x1 - s * head, y + head)], fill=fill)


def strike(d, x0, x1, y, fill=SIGNAL, w=6):
    hrule(d, x0, x1, y, fill, w)


# ── the node record (FIG. 03 / FIG. 04) ──────────────────────────────────────
# Values read off the cancer fixture, per the script's Appendix C.
NODE_ROWS_FULL = [
    ("canonical_name",       "Paclitaxel"),
    ("aliases",              '["Taxol", "paclitaxel"]'),
    ("chapter / section",    "22 / 1"),
    ("knowledge_type",       "factual"),
    ("prerequisite_nodes",   '["cancer_22_1_microtubules"]'),
    ("wikipedia_categories", '["Taxanes", "Antineoplastic"]'),
    ("confidence",           "high"),
    ("source_url",           "en.wikipedia.org/wiki/Paclitaxel"),
    ("thin_content",         "false"),
]
# FIG. 03 shows the seven rows the script prints on screen in Scene 3.
NODE_ROWS_FIG3 = [r for r in NODE_ROWS_FULL
                  if r[0] not in ("wikipedia_categories", "source_url")]
STRIPPED = ("wikipedia_categories", "confidence", "source_url")


def draw_node_table(d, L, rows, nvisible=None, highlight=None, struck=(),
                    labels=("FIG. 03 — NODE RECORD", "SOURCE: types/concept-map.ts:10")):
    """A bordered data table, mono, one row per line. Returns row y-centres."""
    nvisible = len(rows) if nvisible is None else nvisible
    # "fills frame as a bordered data table" — the record is the beat's content,
    # so it takes the script's Body size, not the smaller Mono-data size.
    # Portrait is capped at 50 px because the longest value (source_url, 32 ch)
    # plus the key column has to fit 1920 px of usable width.
    size = L.body if not L.portrait else 52
    # Portrait has vertical room to spare, so the rows breathe instead of
    # huddling in the top fifth of a 3840-tall frame.
    lead = int(size * (2.0 if not L.portrait else 3.6))
    tw = L.span(10) if not L.portrait else L.span(12)
    x0 = L.x(1) if not L.portrait else L.x(0)
    th = lead * len(rows) + int(size * 1.6)
    y0 = (L.h - th) // 2
    box(d, x0, y0, x0 + tw, y0 + th, fill=PAPER, w=4)
    panel_label(d, L, labels[0], x0, y0 - int(L.caption * 2.2))
    mono(d, (x0 + tw, y0 - int(L.caption * 2.2)), labels[1], L.caption,
         fill=MUTE, bold=True, right=True)
    keyx = x0 + int(size * 1.4)
    valx = x0 + int(size * 1.4) + int(size * 0.62 * 22)
    centres = []
    for i, (k, v) in enumerate(rows):
        y = y0 + int(size * 0.8) + i * lead
        centres.append(y + size * 0.55)
        if i >= nvisible:
            continue
        ink = SIGNAL if highlight == k else PAPER
        mono(d, (keyx, y), k, size, fill=MUTE if highlight and highlight != k else ink)
        mono(d, (valx, y), v, size, fill=ink, bold=(highlight == k))
        if k in struck:
            strike(d, keyx, x0 + tw - int(size * 1.4), int(y + size * 0.62))
    return centres, (x0, y0, tw, th)


# ══ scenes ════════════════════════════════════════════════════════════════════
# Each scene returns a list of segments: (frames|None, draw_fn).
# frames=None marks an elastic segment that absorbs the leftover frame budget.

def b00(L):
    """Requested spoken intro. A neutral title card — no new framing."""
    lines = ["WHAT IS A", "CONCEPT", "MAP"] if L.portrait else ["WHAT IS A", "CONCEPT MAP"]

    def draw(title=0, cap=False, wipe=0.0):
        im, d = new_frame(L)
        size = L.display
        lead = int(size * 1.06)
        y = L.margin + (int(L.h * 0.10) if not L.portrait else int(L.h * 0.16))
        for i, ln in enumerate(lines[:title]):
            display_line(d, (L.x(1), y + i * lead), ln, L, PAPER)
        ybase = y + len(lines) * lead + int(size * 0.30)
        if wipe > 0:
            x0 = L.x(1)
            hrule(d, x0, int(x0 + (L.right - x0) * wipe), ybase, SIGNAL, 8)
        if cap:
            yy = ybase + int(L.body * 1.5)
            mono(d, (L.x(1), yy), "MEDHAVY RESEARCH LOG", L.body, fill=PAPER, bold=True)
            mono(d, (L.x(1), yy + int(L.body * 1.5)),
                 "2026-08-28  ·  CONCEPT MAP SUBSYSTEM AUDIT", L.data, fill=MUTE)
        return im

    segs = [(12, lambda: draw())]
    for i in range(1, len(lines) + 1):
        segs.append((3, lambda i=i: draw(title=i)))
    segs.append((10, lambda: draw(title=len(lines))))
    segs.append((8, lambda: draw(title=len(lines), cap=True)))
    for k in range(1, 7):                      # 6-frame linear wipe
        segs.append((1, lambda k=k: draw(title=len(lines), cap=True, wipe=k / 6)))
    segs.append((None, lambda: draw(title=len(lines), cap=True, wipe=1.0)))
    return segs


def b01(L):
    """SCENE 1 — COLD OPEN. TOC, 2 s hold, 6-frame strike, THIS IS NOT A MAP."""
    toc = ["CH 21  CELL CYCLE CONTROL",
           "CH 22  CHEMOTHERAPEUTIC AGENTS",
           "CH 23  CLINICAL ONCOLOGY"]
    dl = ["THIS IS", "NOT A MAP"] if L.portrait else ["THIS IS NOT A MAP"]

    def draw(toc_on=False, wipe=0.0, headline=False):
        im, d = new_frame(L)
        size = L.body
        lead = int(size * 1.9)
        y0 = L.margin + int(L.h * 0.09)
        if toc_on:
            panel_label(d, L, "§ TABLE OF CONTENTS", L.x(1), y0 - int(L.caption * 2.4))
            for i, ln in enumerate(toc):
                mono(d, (L.x(1), y0 + i * lead), ln, size, fill=PAPER)
            if wipe > 0:
                x0 = L.x(1) - int(size * 0.3)
                wmax = max(tracked_width(t, font("mono", size), 0) for t in toc)
                x1 = int(x0 + (wmax + size * 0.6) * wipe)
                for i in range(len(toc)):
                    strike(d, x0, x1, int(y0 + i * lead + size * 0.62), SIGNAL, 8)
        if headline:
            dsz = L.display
            lead2 = int(dsz * 1.06)
            yy = int(L.h * (0.56 if not L.portrait else 0.58))
            for i, ln in enumerate(dl):
                display_line(d, (L.w // 2, yy + i * lead2), ln, L, PAPER, center=True)
        return im

    segs = [(24, lambda: draw())]                     # 1 s of empty frame
    segs.append((48, lambda: draw(toc_on=True)))      # snap in, hold 2 s
    for k in range(1, 7):                             # 6 frames, linear
        segs.append((1, lambda k=k: draw(toc_on=True, wipe=k / 6)))
    segs.append((14, lambda: draw(toc_on=True, wipe=1.0)))
    segs.append((None, lambda: draw(toc_on=True, wipe=1.0, headline=True)))
    return segs


def b02(L):
    """SCENE 2 — THE DEFINITION. Split frame: sequence vs dependency."""
    chapters = ["CH 21", "CH 22", "CH 23"]
    # Deliberately not a neat tree — lopsided, as specified.
    nodes = [("CELL CYCLE", 0.10, 0.06), ("CHECKPOINTS", 0.58, 0.30),
             ("MICROTUBULES", 0.06, 0.54), ("PACLITAXEL", 0.50, 0.72),
             ("RESISTANCE", 0.13, 0.88)]
    edges = [(1, 0), (3, 2), (4, 3), (4, 1)]

    def draw(left=False, right=False, lower=0):
        im, d = new_frame(L)
        if L.portrait:
            midy = L.h // 2
            hrule(d, 0, L.w, midy - 2, PAPER, 4)
            LZ = (L.margin, L.margin + int(L.h * 0.04), L.w - L.margin, midy - int(L.h * 0.06))
            RZ = (L.margin, midy + int(L.h * 0.05), L.w - L.margin, L.h - L.margin - int(L.h * 0.10))
        else:
            midx = L.w // 2
            vrule(d, 0, L.h, midx - 2, PAPER, 4)
            LZ = (L.margin, L.margin + int(L.h * 0.06), midx - int(L.w * 0.045), L.h - L.margin - int(L.h * 0.16))
            RZ = (midx + int(L.w * 0.045), L.margin + int(L.h * 0.06), L.w - L.margin, L.h - L.margin - int(L.h * 0.16))

        if left:
            x0, y0, x1, y1 = LZ
            panel_label(d, L, "FIG. 01 — SEQUENCE", x0, y0 - int(L.caption * 2.4))
            bh = int((y1 - y0) * 0.20)
            gap = int((y1 - y0 - 3 * bh) / 2)
            bw = min(int((x1 - x0) * 0.74), int((x1 - x0)))
            for i, c in enumerate(chapters):
                by = y0 + i * (bh + gap)
                box(d, x0, by, x0 + bw, by + bh, PAPER, 4)
                mono(d, (x0 + int(bw * 0.5), by + bh // 2 - L.h2 // 2), c,
                     L.h2, fill=PAPER, bold=True, center=True)
                if i < 2:
                    arrow_v(d, x0 + bw // 2, by + bh + 12, by + bh + gap - 14, MUTE, 4, 22)
        if right:
            x0, y0, x1, y1 = RZ
            panel_label(d, L, "FIG. 02 — DEPENDENCY", x0, y0 - int(L.caption * 2.4))
            zw, zh = x1 - x0, y1 - y0
            nb_w, nb_h = int(zw * 0.44), int(zh * 0.115)
            pos = {}
            for i, (nm, fx, fy) in enumerate(nodes):
                nx, ny = x0 + int(zw * fx), y0 + int(zh * fy)
                pos[i] = (nx, ny, nx + nb_w, ny + nb_h)
            for a, b in edges:                     # arrows point BACK into prereqs
                ax0, ay0, ax1, ay1 = pos[a]
                bx0, by0, bx1, by1 = pos[b]
                sx, sy = (ax0 + ax1) // 2, ay0
                tx, ty = (bx0 + bx1) // 2, by1
                vrule(d, min(sy, ty), max(sy, ty), sx - 2, SIGNAL, 4)
                hrule(d, min(sx, tx), max(sx, tx), ty - 2, SIGNAL, 4)
                d.polygon([(tx, ty), (tx - 20, ty + 22), (tx + 20, ty + 22)], fill=SIGNAL)
            for i, (nm, _, _) in enumerate(nodes):
                bx0, by0, bx1, by1 = pos[i]
                box(d, bx0, by0, bx1, by1, PAPER, 4, bg=GROUND)
                mono(d, ((bx0 + bx1) // 2, by0 + (by1 - by0) // 2 - L.data // 2), nm,
                     L.data, fill=PAPER, bold=True, center=True)
        if lower:
            yy = L.h - L.margin - int(L.body * (2.6 if not L.portrait else 3.0))
            if lower >= 1:
                mono(d, (L.x(1), yy), "NODE = ONE TEACHABLE IDEA", L.body, fill=PAPER, bold=True)
            if lower >= 2:
                mono(d, (L.x(1), yy + int(L.body * 1.45)), "EDGE = PREREQUISITE",
                     L.body, fill=PAPER, bold=True)
        return im

    return [
        (18, lambda: draw(left=True)),
        (None, lambda: draw(left=True, right=True)),
        (2, lambda: draw(left=True, right=True, lower=1)),
        (None, lambda: draw(left=True, right=True, lower=2)),
    ]


def b03(L):
    """SCENE 3 — ANATOMY OF A NODE. 7 rows × 4-frame step-reveal."""
    rows = NODE_ROWS_FIG3
    dl = ["THE EDGE IS", "THE POINT"] if L.portrait else ["THE EDGE IS THE POINT"]

    def draw(n=0, highlight=None):
        im, d = new_frame(L)
        draw_node_table(d, L, rows, nvisible=n, highlight=highlight)
        return im

    def headline():
        im, d = new_frame(L)
        dsz = L.display
        lead = int(dsz * 1.06)
        yy = (L.h - lead * len(dl)) // 2
        for i, ln in enumerate(dl):
            display_line(d, (L.w // 2, yy + i * lead), ln, L, PAPER, center=True)
        return im

    segs = []
    for i in range(1, len(rows) + 1):
        segs.append((4, lambda i=i: draw(n=i)))       # 4 frames apart
    segs.append((None, lambda: draw(n=len(rows))))
    segs.append((None, lambda: draw(n=len(rows), highlight="canonical_name")))
    segs.append((None, lambda: draw(n=len(rows))))
    segs.append((None, lambda: draw(n=len(rows), highlight="prerequisite_nodes")))
    segs.append((16, lambda: draw(n=len(rows))))
    segs.append((None, headline))                     # hard cut
    return segs


def b04(L):
    """SCENE 4 — WHY HUMANS. Brutalist bar chart, 3-frame steps."""
    bars = [("HIGH", 9, PAPER), ("MEDIUM", 10, PAPER), ("LOW", 6, SIGNAL)]
    vmax = 10

    def chart(nvis=0, grow=1.0):
        im, d = new_frame(L)
        x0 = L.x(1)
        panel_label(d, L, "CONFIDENCE, 25-NODE RUN", x0, L.margin + int(L.h * 0.06))
        top = L.margin + int(L.h * 0.14)
        bh = int(L.h * (0.15 if not L.portrait else 0.10))
        gap = int(bh * 0.55)
        labw = int(L.h2 * 0.62 * 8)
        track = L.right - (x0 + labw) - int(L.h1 * 1.4)
        for i, (nm, v, col) in enumerate(bars):
            y = top + i * (bh + gap)
            mono(d, (x0, y + bh // 2 - L.h2 // 2), nm, L.h2, fill=PAPER, bold=True)
            if i >= nvis:
                continue
            g = grow if i == nvis - 1 else 1.0
            bw = int(track * (v / vmax) * g)
            d.rectangle([x0 + labw, y, x0 + labw + bw, y + bh], fill=col)
            if g >= 1.0:
                mono(d, (x0 + labw + bw + int(L.h1 * 0.28),
                         y + bh // 2 - L.h1 // 2), str(v), L.h1,
                     fill=col, bold=True)
        return im

    def thin():
        im, d = new_frame(L)
        display_line(d, (L.w // 2, L.h // 2 - L.display // 2),
                     "THIN_CONTENT: 2", L, SIGNAL, center=True)
        return im

    def weak(sub=False):
        im, d = new_frame(L)
        display_line(d, (L.w // 2, int(L.h * 0.34) - L.display // 2),
                     "THIN_CONTENT: 2", L, SIGNAL, center=True)
        if sub:
            txt = "THE PIPELINE MARKS ITS OWN WEAK SPOTS"
            if L.portrait:
                mono(d, (L.w // 2, int(L.h * 0.56)), "THE PIPELINE MARKS", L.body,
                     fill=PAPER, bold=True, center=True)
                mono(d, (L.w // 2, int(L.h * 0.56) + int(L.body * 1.5)),
                     "ITS OWN WEAK SPOTS", L.body, fill=PAPER, bold=True, center=True)
            else:
                mono(d, (L.w // 2, int(L.h * 0.58)), txt, L.body,
                     fill=PAPER, bold=True, center=True)
        return im

    # The empty chart scaffold is a 12-frame establishing beat, NOT an elastic:
    # left elastic it absorbed 7.5 s and read as failed media.
    segs = [(12, lambda: chart(0))]
    for i in range(1, 4):                             # bars snap in, 3-frame steps
        segs.append((3, lambda i=i: chart(nvis=i, grow=0.55)))
        segs.append((3 if i < 3 else 24, lambda i=i: chart(nvis=i, grow=1.0)))
    segs.append((EL(5), lambda: chart(3)))            # the exhibit holds longest
    segs.append((EL(2), thin))                        # hard cut
    segs.append((6, weak))
    segs.append((EL(2), lambda: weak(sub=True)))
    return segs


def b05(L):
    """SCENE 5 — THE FOUR STAGES. Four panels, hard cuts, no slide."""
    stages = [
        ("01", "GENERATE", "s3://…/pipeline/<run>.json   ·   external, not in this repo"),
        ("02", "IMPORT",   "validated   ·   every node lands  pending"),
        ("03", "REVIEW",   "node by node   ·   accept | edit | remove"),
        ("04", "EXPORT",   "hard-blocked while any node is pending"),
    ]
    verdicts = ["ACCEPT", "EDIT", "REMOVE"]

    def band(active=-1, top_rule=True, vstack=0, struck=False):
        im, d = new_frame(L)
        n = len(stages)
        if L.portrait:
            x0, x1 = L.margin, L.w - L.margin
            top = L.margin + int(L.h * 0.07)
            ph = int(L.h * 0.105)
            gap = int(ph * 0.34)
            zones = [(x0, top + i * (ph + gap), x1, top + i * (ph + gap) + ph)
                     for i in range(n)]
        else:
            top = L.margin + int(L.h * 0.09)
            ph = int(L.h * 0.22)          # a BAND, not four tall hollow boxes
            gap = 48
            pw = int((L.w - 2 * L.margin - gap * (n - 1)) / n)
            zones = [(L.margin + i * (pw + gap), top,
                      L.margin + i * (pw + gap) + pw, top + ph) for i in range(n)]
        for i, (num, nm, sub) in enumerate(stages):
            zx0, zy0, zx1, zy1 = zones[i]
            on = (i == active)
            ink = PAPER if on else MUTE
            box(d, zx0, zy0, zx1, zy1, ink, 4)
            if on and top_rule:
                # active panel: Paper with a signal top rule
                hrule(d, zx0, zx1, zy0, SIGNAL, 12)
            mono(d, (zx0 + int(L.h2 * 0.4), zy0 + int(ph * 0.20)), num, L.h2,
                 fill=ink, bold=True)
            mono(d, (zx0 + int(L.h2 * 0.4), zy0 + int(ph * 0.54)), nm, L.h2,
                 fill=ink, bold=True)
        if active >= 0:
            sub = stages[active][2]
            zx0, zy0, zx1, zy1 = zones[active]
            sy = zy1 + int(L.data * 1.3)
            # under the ACTIVE panel, clamped so panel 04's line cannot bleed
            sw = tracked_width(sub, font("mono", L.data), 0.0)
            sx = min(zx0, L.right - int(sw))
            mono(d, (sx, sy), sub, L.data, fill=PAPER)
        if vstack:
            bh = int(L.h2 * 1.5)
            gapv = int(bh * 0.28)
            total = len(verdicts) * bh + (len(verdicts) - 1) * gapv
            vy = L.h - L.margin - total - int(L.h * 0.02)
            bw = int(L.span(5) if not L.portrait else L.span(9))
            vx = L.x(1) if not L.portrait else L.margin
            for j, v in enumerate(verdicts[:vstack]):
                by = vy + j * (bh + gapv)
                d.rectangle([vx, by, vx + bw, by + bh], fill=SIGNAL)
                mono(d, (vx + int(L.h2 * 0.45), by + bh // 2 - L.h2 // 2), v, L.h2,
                     fill=GROUND, bold=True)
                if v == "REMOVE" and struck:
                    strike(d, vx + int(L.h2 * 0.3), vx + bw - int(L.h2 * 0.3),
                           by + bh // 2 - 4, GROUND, 8)
        return im

    def zero():
        im, d = new_frame(L)
        lines = ["ZERO PENDING", "OR NOTHING"] if L.portrait else ["ZERO PENDING OR NOTHING"]
        dsz = int(L.display * (1.0 if L.portrait else 0.78))
        lead = int(dsz * 1.08)
        yy = (L.h - lead * len(lines)) // 2
        for i, ln in enumerate(lines):
            display_line(d, (L.w // 2, yy + i * lead), ln, L, SIGNAL,
                         center=True, size=dsz)
        return im

    segs = [(8, lambda: band(-1))]
    segs.append((None, lambda: band(0)))
    segs.append((None, lambda: band(1)))
    segs.append((None, lambda: band(2)))
    # On "three verdicts", the three words snap in as stacked signal blocks.
    # The panel's signal top rule drops to Paper here: the script's own hard
    # rule is "never two red things at once", and the verdicts are the point.
    for j in (1, 2, 3):
        segs.append((3, lambda j=j: band(2, top_rule=False, vstack=j)))
    segs.append((None, lambda: band(2, top_rule=False, vstack=3)))
    segs.append((None, lambda: band(2, top_rule=False, vstack=3, struck=True)))
    segs.append((None, lambda: band(3)))
    segs.append((48, zero))                            # held 2 s
    return segs


def b06(L):
    """SCENE 6 — WHAT GETS THROWN AWAY. Strike 3 rows, fall out, close gap."""
    full = NODE_ROWS_FULL
    kept = [r for r in full if r[0] not in STRIPPED]
    L3 = ("FIG. 03 — NODE RECORD", "SOURCE: types/concept-map.ts:10")
    L4 = ("FIG. 04 — VERIFIED OUTPUT", "SOURCE: export/route.ts:62")

    def draw(rows, struck=(), labels=L3, drop=0):
        im, d = new_frame(L)
        if drop:
            # struck rows fall out of frame on a 2-frame step
            shown = [r for r in rows if r[0] not in STRIPPED or drop < 2]
            draw_node_table(d, L, rows, struck=struck, labels=labels)
        else:
            draw_node_table(d, L, rows, struck=struck, labels=labels)
        return im

    def falling(step):
        """Struck rows slide down out of frame; survivors hold position."""
        im, d = new_frame(L)
        size = L.body if not L.portrait else 52
        lead = int(size * (2.0 if not L.portrait else 3.6))
        tw = L.span(10) if not L.portrait else L.span(12)
        x0 = L.x(1) if not L.portrait else L.x(0)
        th = lead * len(full) + int(size * 1.6)
        y0 = (L.h - th) // 2
        box(d, x0, y0, x0 + tw, y0 + th, fill=PAPER, w=4)
        panel_label(d, L, L3[0], x0, y0 - int(L.caption * 2.2))
        mono(d, (x0 + tw, y0 - int(L.caption * 2.2)), L3[1], L.caption,
             fill=MUTE, bold=True, right=True)
        keyx = x0 + int(size * 1.4)
        valx = x0 + int(size * 1.4) + int(size * 0.62 * 22)
        for i, (k, v) in enumerate(full):
            y = y0 + int(size * 0.8) + i * lead
            if k in STRIPPED:
                y += int(step * lead * 3.2)
                if y > y0 + th:
                    continue
                mono(d, (keyx, y), k, size, fill=SIGNAL)
                mono(d, (valx, y), v, size, fill=SIGNAL)
                strike(d, keyx, x0 + tw - int(size * 1.4), int(y + size * 0.62))
            else:
                mono(d, (keyx, y), k, size, fill=PAPER)
                mono(d, (valx, y), v, size, fill=PAPER)
        return im

    def closed(tag=False):
        im, d = new_frame(L)
        draw_node_table(d, L, kept, labels=L4)
        if tag:
            yy = L.h - L.margin - int(L.body * 1.4)
            mono(d, (L.w // 2, yy), "SCAFFOLDING ≠ CONTENT", L.body,
                 fill=PAPER, bold=True, center=True)
        return im

    segs = [(None, lambda: draw(full))]
    segs.append((None, lambda: draw(full, struck=STRIPPED)))
    for s in (1, 2, 3):                                # 2-frame step fall-out
        segs.append((2, lambda s=s: falling(s)))
    segs.append((None, lambda: closed()))              # hard snap, gap closed
    segs.append((None, lambda: closed(tag=True)))
    return segs


def b07(L):
    """SCENE 7 — THE HONEST FINDING. Hairline draw, then 3 s of nothing."""
    steps = ["PIPELINE", "IMPORT", "REVIEW", "EXPORT", "S3"]
    HAIR = 3

    def draw(n=0, tail=0.0, grep=False, headline=False):
        im, d = new_frame(L)
        if L.portrait:
            x = L.w // 2
            top = L.margin + int(L.h * 0.10)
            step = int(L.h * 0.115)
            bw, bh = L.span(8), int(L.h * 0.062)
            for i, s in enumerate(steps[:n]):
                y = top + i * step
                box(d, x - bw // 2, y, x + bw // 2, y + bh, PAPER, HAIR, bg=GROUND)
                mono(d, (x, y + bh // 2 - L.h2 // 2), s, L.h2, fill=PAPER,
                     bold=True, center=True)
                if i > 0:
                    arrow_v(d, x, top + (i - 1) * step + bh + 6, y - 8, PAPER, HAIR, 20)
            if tail > 0:
                y = top + (len(steps) - 1) * step + bh
                ymax = L.h - L.margin
                vrule(d, y + 6, int(y + 6 + (ymax - y - 6) * tail), x - 1, PAPER, HAIR)
        else:
            y = int(L.h * 0.40)
            bw = int(L.span(2) * 1.02)
            bh = int(L.h * 0.13)
            gap = int((L.right - L.margin - len(steps) * bw) / (len(steps) - 1))
            for i, s in enumerate(steps[:n]):
                x = L.margin + i * (bw + gap)
                box(d, x, y, x + bw, y + bh, PAPER, HAIR, bg=GROUND)
                mono(d, (x + bw // 2, y + bh // 2 - L.data // 2), s, L.data,
                     fill=PAPER, bold=True, center=True)
                if i > 0:
                    px = L.margin + (i - 1) * (bw + gap) + bw
                    arrow_h(d, y + bh // 2, px + 6, x - 8, PAPER, HAIR, 18)
            if tail > 0:
                x = L.margin + (len(steps) - 1) * (bw + gap) + bw
                hrule(d, x + 6, int(x + 6 + (L.w - x - 6) * tail), y + bh // 2 - 1,
                      PAPER, HAIR)
        if grep:
            mono(d, (L.right, L.bottom - L.caption), "grep: 0 consumers",
                 L.caption, fill=MUTE, bold=True, right=True)
        if headline:
            lines = ["STORED,", "NOT SPENT"] if L.portrait else ["STORED, NOT SPENT"]
            dsz = L.display
            lead = int(dsz * 1.06)
            yy = (L.h - lead * len(lines)) // 2
            im2, d2 = new_frame(L)
            for i, ln in enumerate(lines):
                display_line(d2, (L.w // 2, yy + i * lead), ln, L, SIGNAL, center=True)
            return im2
        return im

    segs = []
    for i in range(1, len(steps) + 1):
        segs.append((6, lambda i=i: draw(n=i)))
    segs.append((None, lambda: draw(n=len(steps))))
    for k in range(1, 9):                              # the arrow to nowhere
        segs.append((2, lambda k=k: draw(n=len(steps), tail=k / 8)))
    segs.append((72, lambda: draw(n=len(steps), tail=1.0)))   # 3 s, no sound
    segs.append((None, lambda: draw(n=len(steps), tail=1.0, grep=True)))
    segs.append((None, lambda: draw(headline=True)))
    return segs


def b08(L):
    """SCENE 8 — THE CRACK. Fourth box hard-cuts out; edges persist."""
    deps = ["PACLITAXEL", "CISPLATIN", "DOXORUBICIN"]
    target = "MICROTUBULE DYNAMICS"

    def draw(target_on=True, tag=False):
        im, d = new_frame(L)
        panel_label(d, L, "FIG. 05 — DANGLING EDGE", L.x(1),
                    L.margin + int(L.h * 0.05))
        mono(d, (L.right, L.margin + int(L.h * 0.05)),
             "SOURCE: export/route.ts:76", L.caption, fill=MUTE, bold=True, right=True)
        top = L.margin + int(L.h * (0.13 if not L.portrait else 0.11))
        # Three dependents, three SEPARATE edges, three arrowheads. When the
        # fourth box is removed the script needs three edges left pointing at
        # empty frame — a merged bus would read as one.
        if L.portrait:
            bw, bh = L.span(7), int(L.h * 0.075)
            gap = int(bh * 0.50)
            xs = L.margin
            tx, tw = L.margin, L.span(12)
            ty = top + 3 * (bh + gap) + int(L.h * 0.13)
            for i, nm in enumerate(deps):
                y = top + i * (bh + gap)
                box(d, xs, y, xs + bw, y + bh, PAPER, 4, bg=GROUND)
                mono(d, (xs + bw // 2, y + bh // 2 - L.data // 2), nm, L.data,
                     fill=PAPER, bold=True, center=True)
            for i in range(len(deps)):
                sy = top + i * (bh + gap) + bh // 2
                xj = xs + bw + int(L.w * 0.055) + i * int(L.w * 0.052)
                hrule(d, xs + bw, xj, sy - 2, SIGNAL, 4)
                vrule(d, sy, ty - 34, xj - 2, SIGNAL, 4)
                arrow_v(d, xj, ty - 34, ty - 8, SIGNAL, 4, 22)
            if target_on:
                box(d, tx, ty, tx + tw, ty + bh, PAPER, 4, bg=GROUND)
                mono(d, (tx + tw // 2, ty + bh // 2 - L.data // 2), target, L.data,
                     fill=PAPER, bold=True, center=True)
        else:
            bw, bh = L.span(3), int(L.h * 0.115)
            gap = int(bh * 0.52)
            xs = L.x(0)
            tx, tw = L.x(8), L.span(4)
            ty = top + (bh + gap)
            for i, nm in enumerate(deps):
                y = top + i * (bh + gap)
                box(d, xs, y, xs + bw, y + bh, PAPER, 4, bg=GROUND)
                mono(d, (xs + bw // 2, y + bh // 2 - L.data // 2), nm, L.data,
                     fill=PAPER, bold=True, center=True)
            for i in range(len(deps)):
                sy = top + i * (bh + gap) + bh // 2
                ey = ty + int(bh * (0.22 + 0.28 * i))
                xj = xs + bw + int(L.w * 0.03) + i * int(L.w * 0.022)
                hrule(d, xs + bw, xj, sy - 2, SIGNAL, 4)
                vrule(d, min(sy, ey), max(sy, ey), xj - 2, SIGNAL, 4)
                arrow_h(d, ey, xj, tx - 12, SIGNAL, 4, 24)
            if target_on:
                box(d, tx, ty, tx + tw, ty + bh, PAPER, 4, bg=GROUND)
                mono(d, (tx + tw // 2, ty + bh // 2 - L.data // 2), target, L.data,
                     fill=PAPER, bold=True, center=True)
        if tag:
            mono(d, (L.w // 2, L.bottom - int(L.body * 1.2)),
                 "18 EDGES · 0 DANGLING · TODAY", L.body,
                 fill=PAPER, bold=True, center=True)
        return im

    return [
        (None, lambda: draw(target_on=True)),
        (72, lambda: draw(target_on=False)),           # hard cut out, hold 3 s
        (None, lambda: draw(target_on=False, tag=True)),
    ]


def b09(L):
    """SCENE 9 — CLOSE. Four lines, then all to black but the last."""
    lines = [("CONCEPT MAP", "DEPENDENCY GRAPH"),
             ("REVIEW GATE", "STRICT, WORKING"),
             ("OUTPUT", "CORRECT"),
             ("CONSUMERS", "0")]

    def draw(n=0):
        im, d = new_frame(L)
        size = L.body if not L.portrait else int(L.body * 1.15)
        lead = int(size * 2.1)
        keyw = int(size * 0.62 * 14)
        y0 = (L.h - lead * len(lines)) // 2
        x0 = L.x(1)
        for i, (k, v) in enumerate(lines[:n]):
            y = y0 + i * lead
            mono(d, (x0, y), k, size, fill=PAPER, bold=True)
            mono(d, (x0 + keyw, y), "=", size, fill=MUTE, bold=True)
            mono(d, (x0 + keyw + int(size * 1.6), y), v, size, fill=PAPER, bold=True)
        return im

    def last(red=True):
        im, d = new_frame(L, bg=BLACK, grid=False)
        size = L.body if not L.portrait else int(L.body * 1.15)
        keyw = int(size * 0.62 * 14)
        lead = int(size * 2.1)
        y = (L.h - lead * len(lines)) // 2 + 3 * lead
        x0 = L.x(1)
        col = SIGNAL if red else PAPER
        mono(d, (x0, y), "CONSUMERS", size, fill=col, bold=True)
        mono(d, (x0 + keyw, y), "=", size, fill=col, bold=True)
        mono(d, (x0 + keyw + int(size * 1.6), y), "0", size, fill=col, bold=True)
        return im

    def black():
        im, _ = new_frame(L, bg=BLACK, grid=False)
        return im

    segs = []
    for i in range(1, 5):
        segs.append((None, lambda i=i: draw(n=i)))
    segs.append((6, lambda: draw(n=4)))
    segs.append((48, lambda: last(red=True)))          # hold CONSUMERS 0, 2 s
    segs.append((8, black))                            # hard cut to black
    return segs


def end(L):
    """Silent endcard for the 9:16 short — points at the long, per SHORTS LAW.

    Replaces shorts.py's generated card, which renders in the CLAUDE brand
    (ink-brown ground, EB Garamond serif, @nikbearbrown) at 1080x1920. That
    card is wrong three ways here: not this reel's palette, introduces a third
    type family the script forbids, and names a channel this reel isn't on.
    """
    title = ["WHAT IS A", "CONCEPT", "MAP"] if L.portrait else ["WHAT IS A CONCEPT MAP"]

    def draw():
        im, d = new_frame(L)
        y = int(L.h * (0.30 if L.portrait else 0.28))
        mono(d, (L.x(1) if not L.portrait else L.margin, y),
             "FULL VIDEO", L.body, fill=SIGNAL, bold=True)
        dsz = int(L.display * 0.74)
        lead = int(dsz * 1.06)
        y2 = y + int(L.body * 2.2)
        for i, ln in enumerate(title):
            display_line(d, (L.x(1) if not L.portrait else L.margin, y2 + i * lead),
                         ln, L, PAPER, size=dsz)
        ybase = y2 + len(title) * lead + int(dsz * 0.22)
        x0 = L.x(1) if not L.portrait else L.margin
        hrule(d, x0, L.right, ybase, SIGNAL, 8)
        mono(d, (x0, ybase + int(L.body * 0.9)), "MEDHAVY · RESEARCH LOG",
             L.body, fill=PAPER, bold=True)
        mono(d, (x0, ybase + int(L.body * 2.3)), "2026-08-28", L.data, fill=MUTE)
        return im

    return [(None, draw)]


SCENES = {"B00": b00, "B01": b01, "B02": b02, "B03": b03, "B04": b04,
          "B05": b05, "B06": b06, "B07": b07, "B08": b08, "B09": b09,
          "END": end}


# ── assembly ─────────────────────────────────────────────────────────────────
def EL(weight=1):
    """An elastic segment: absorbs leftover frames in proportion to `weight`.

    Weights matter. An empty or transitional state must never take the same
    share as the settled state that carries the beat's content — that is how
    a chart ends up sitting on screen with no bars in it.
    """
    return ("el", weight)


def _is_fixed(f):
    return isinstance(f, int)


def allocate(segs, total):
    """Give fixed segments their frames; split the remainder among elastics."""
    fixed = sum(f for f, _ in segs if _is_fixed(f))
    weights = [(i, (1 if f is None else f[1]))
               for i, (f, _) in enumerate(segs) if not _is_fixed(f)]
    elastic = [i for i, _ in weights]
    out = [f if _is_fixed(f) else 0 for f, _ in segs]
    left = total - fixed
    if elastic:
        if left < len(elastic):
            # Audio is shorter than the scene's fixed choreography needs.
            # Shrink fixed holds proportionally rather than dropping reveals.
            scale = max(0.0, (total - len(elastic)) / max(fixed, 1))
            for i, (f, _) in enumerate(segs):
                out[i] = max(1, int(f * scale)) if _is_fixed(f) else 1
            drift = total - sum(out)
            out[-1] = max(1, out[-1] + drift)
            return out
        wsum = sum(w for _, w in weights)
        acc = 0
        for j, (i, w) in enumerate(weights):
            share = left * w // wsum if j < len(weights) - 1 else left - acc
            out[i] = share
            acc += share
    else:
        out[-1] += left
    drift = total - sum(out)
    if drift:
        out[-1] = max(1, out[-1] + drift)
    return out


def render_beat(bid, L, duration_s, outdir, workroot):
    total = max(1, int(round(duration_s * FPS)))
    segs = SCENES[bid](L)
    counts = allocate(segs, total)
    work = workroot / bid
    if work.exists():
        shutil.rmtree(work)
    (work / "states").mkdir(parents=True)
    frames = work / "frames"
    frames.mkdir()

    n = 0
    for idx, ((_, fn), cnt) in enumerate(zip(segs, counts)):
        if cnt <= 0:
            continue
        state = work / "states" / f"s{idx:04d}.png"
        fn().save(state, compress_level=1)
        for _ in range(cnt):
            n += 1
            os.link(state, frames / f"{n:06d}.png")

    out = outdir / f"{bid}.mp4"
    cmd = ["ffmpeg", "-y", "-framerate", str(FPS), "-i", str(frames / "%06d.png"),
           "-c:v", "libx264", "-preset", "medium", "-crf", "16",
           "-pix_fmt", "yuv420p", "-color_primaries", "bt709",
           "-color_trc", "bt709", "-colorspace", "bt709", str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"[render] ffmpeg failed on {bid}:\n{r.stderr[-1500:]}")
    shutil.rmtree(work)
    return out, n, len(counts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--aspect", default="16:9", choices=["16:9", "9:16"])
    ap.add_argument("--sheet", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--only", nargs="*", default=None)
    a = ap.parse_args()

    here = Path(__file__).resolve().parent
    reel = here.parent
    sheet_path = Path(a.sheet) if a.sheet else reel / "beat_sheet.json"
    sheet = json.loads(sheet_path.read_text())

    W, H = (3840, 2160) if a.aspect == "16:9" else (2160, 3840)
    L = Layout(W, H)
    outdir = Path(a.out) if a.out else reel / "media"
    outdir.mkdir(parents=True, exist_ok=True)
    workroot = Path(tempfile.mkdtemp(prefix="cmscenes-"))

    print(f"[render] {a.aspect}  {W}x{H}  @{FPS}fps  -> {outdir}")
    for b in sheet["beats"]:
        bid = b["beat_id"]
        if a.only and bid not in a.only:
            continue
        if bid not in SCENES:
            print(f"[render] {bid}: no scene defined — skipped")
            continue
        dur = b.get("actual_duration_s") or b.get("estimated_duration_s")
        out, nframes, nstates = render_beat(bid, L, float(dur), outdir, workroot)
        print(f"[render] {bid}  {dur:>6.2f}s  {nframes:>5d} frames  "
              f"{nstates:>3d} states  -> {out.name}")
    shutil.rmtree(workroot, ignore_errors=True)
    print("[render] done")


if __name__ == "__main__":
    main()
