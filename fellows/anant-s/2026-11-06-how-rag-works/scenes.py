"""Manim scenes for "How RAG Works" (show-tell-how-rag-works), film #7 of the STEM/AI series.

Built on the show-tell drawing kit (iso_kit.py, pasted below, not imported) and one approved
original prop (memory-drawers). Every scene subclasses Scene directly, one per drawn beat.
"""
from manim import *
import numpy as np
import json as _json, os as _os

# ═════════════════════════════ ISO KIT (show-tell) ═════════════════════════════
STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"; CARD = "#FAF9F5"
BOX_TOP, BOX_L, BOX_R = "#F3E9D8", "#DCC9AA", "#C7AE86"          # kraft cardboard: top, left face, right face (deep enough for Gate V contrast)
BOX_IN1, BOX_IN2, BOX_FLOOR = "#CDB894", "#BFA67E", "#B39A72"     # inside walls + floor
DARK_TOP, DARK_L, DARK_R = "#3A3530", "#26221F", "#1E1B18"        # MCP / server blocks
PAGE_TOP, PAGE_L, PAGE_R = "#FFFFFF", "#ECE7DF", "#E2DCD2"         # skill pages
BAR1, BAR2, BAR3 = "#8B8F96", "#B4AFA6", "#D9D4C7"                # chart segments, dim to ghost
SERIF = "EB Garamond"
C30 = 0.8660254
config.background_color = STAGE


def T(s, size=36, color=INK, bold=False):
    return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")


class Iso:
    """Isometric projection: x runs right-up, y runs left-up, z runs up. (ox, oy) is where (0,0,0) lands."""
    def __init__(self, ox=0.0, oy=0.0, s=1.0):
        self.ox, self.oy, self.s = ox, oy, s

    def p(self, x, y, z=0.0):
        return np.array([self.ox + (x - y) * C30 * self.s, self.oy + (x + y) * 0.5 * self.s + z * self.s, 0.0])

    def v(self, dx, dy, dz=0.0):
        return self.p(dx, dy, dz) - self.p(0, 0, 0)

    def quad(self, pts, fill, stroke=INK, sw=4):
        return Polygon(*[self.p(*q) for q in pts], fill_color=fill, fill_opacity=1, stroke_color=stroke, stroke_width=sw)

    def box(self, x0, y0, z0, w, d, h, top=BOX_TOP, left=BOX_L, right=BOX_R, sw=4):
        """Closed box: the two front faces (x = x0 and y = y0) plus the top."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        return VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], left, sw=sw),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], right, sw=sw),
            self.quad([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], top, sw=sw))

    def open_box(self, x0, y0, z0, w, d, h):
        """(back, front): floor + inner back walls, then the front walls. Put contents between them."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        back = VGroup(
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)], BOX_FLOOR),
            self.quad([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], BOX_IN1),
            self.quad([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], BOX_IN2))
        front = VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], BOX_L),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], BOX_R))
        back.set_z_index(0); front.set_z_index(2)
        return back, front

    def tape(self, x0, y0, z1, w, d, drop=0.35, t=0.22):
        """Terracotta tape across the top (along x) and down the left front face."""
        ym = y0 + d / 2
        return VGroup(
            self.quad([(x0, ym - t, z1), (x0 + w, ym - t, z1), (x0 + w, ym + t, z1), (x0, ym + t, z1)], TERRA, sw=0),
            self.quad([(x0, ym - t, z1), (x0, ym + t, z1), (x0, ym + t, z1 - drop), (x0, ym - t, z1 - drop)], TERRA, sw=0))

    def mcp(self, x0, y0, z0, w=1.3, d=1.3, h=0.7):
        """Dark MCP block with two light ports on its right front face."""
        body = self.box(x0, y0, z0, w, d, h, DARK_TOP, DARK_L, DARK_R)
        ports = VGroup(*[self.box(x0 + w * f, y0 - 0.18, z0 + h * 0.3, w * 0.16, 0.18, h * 0.3, GHOST, BOX_IN1, BOX_IN2, sw=1)
                         for f in (0.22, 0.58)])
        return VGroup(body, ports)

    def page(self, x0, y0, z0, w=1.1, d=1.4):
        """A skill page lying flat: white slab, three ghost text lines, one terracotta dot."""
        slab = self.box(x0, y0, z0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
        zt = z0 + 0.06
        lines = VGroup(*[Line(self.p(x0 + 0.2, y0 + d * f, zt), self.p(x0 + w - 0.2, y0 + d * f, zt), color=GHOST, stroke_width=4)
                         for f in (0.3, 0.5, 0.7)])
        dot = Dot(self.p(x0 + 0.2, y0 + d * 0.86, zt), radius=0.06, color=TERRA)
        return VGroup(slab, lines, dot)

    def server(self, x0, y0, z0, w=1.4, d=1.4, slab=0.42, n=3):
        """A stack of dark server slabs; returns (stack, lights) — lights start ghost, turn terracotta."""
        stack = VGroup(*[self.box(x0, y0, z0 + i * (slab + 0.04), w, d, slab, DARK_TOP, DARK_L, DARK_R) for i in range(n)])
        lights = VGroup(*[Dot(self.p(x0 + 0.25, y0, z0 + i * (slab + 0.04) + slab / 2), radius=0.06, color=GHOST) for i in range(n)])
        return stack, lights


def ease_in(t):
    """Quadratic ease-in (things dropping into a box). Local: Gate A's stub has no ease_in_quad."""
    return t * t


def check(x, y, s=0.2, color=INK, w=7):
    return VGroup(Line([x - s, y, 0], [x - s * 0.3, y - s * 0.75, 0], color=color, stroke_width=w),
                  Line([x - s * 0.3, y - s * 0.75, 0], [x + s * 1.1, y + s * 0.85, 0], color=color, stroke_width=w))


def cursor(x, y, s=0.45):
    return Polygon([x, y, 0], [x, y - s, 0], [x + s * 0.28, y - s * 0.72, 0], [x + s * 0.62, y - s * 0.66, 0],
                   fill_color=INK, fill_opacity=1, stroke_color=CARD, stroke_width=2)


def pill(x, y, w, h=0.62, fill="#FFFFFF"):
    return RoundedRectangle(width=w, height=h, corner_radius=h / 2, fill_color=fill, fill_opacity=1, stroke_width=0).move_to([x, y, 0])


# ═════════════════════════════ WRITING KIT (quill, ink, paper, scribble) ═════════════════════════════
# Added 2026-10-07 from Bear's two reference drawings: a quill drawing a branching outline on a
# scroll, and three scattered pages of scribbled handwriting with a quill. Use when a beat is
# about writing, drafting, authorship, notes, a manuscript, a log, a letter, a signature.
# Terracotta here is only the ink drop and the outline's nodes (dots) — never the lines.


def quill(x, y, s=1.0, angle=0.0, color=INK, fill=BOX_TOP):
    """A drawn quill with its NIB at (x, y); the feather points up-right. `g.nib` is the nib point.
    Kraft-filled feather, ink outline, a shaft line and one barb. Rotate with `angle` (radians)."""
    o = np.array([x, y, 0.0])
    def P(u, v):  # icon units (0..1) → scene, nib at origin, tip at (1, 1.1)·s
        return o + np.array([u * s, v * s, 0.0])
    body = VMobject(fill_color=fill, fill_opacity=1, stroke_color=color, stroke_width=4)
    body.set_points_smoothly([P(0.00, 0.00), P(0.12, 0.62), P(0.55, 1.02), P(1.00, 1.10),
                              P(0.95, 0.68), P(0.62, 0.22), P(0.00, 0.00)])
    shaft = Line(P(0.02, 0.02), P(0.98, 1.06), color=color, stroke_width=3)
    barb = Line(P(0.46, 0.50), P(0.40, 0.72), color=color, stroke_width=2.5)
    g = VGroup(body, shaft, barb)
    if angle:
        g.rotate(angle, about_point=o)
    g.nib = o.copy()
    return g


def inkwell(iso, x0=0.0, y0=0.0, z0=0.0, s=0.7):
    """A dark ink bottle (iso box + narrow neck) with one terracotta ink dot on the lid."""
    body = iso.box(x0, y0, z0, s, s, s * 0.9, DARK_TOP, DARK_L, DARK_R)
    neck = iso.box(x0 + s * 0.3, y0 + s * 0.3, z0 + s * 0.9, s * 0.4, s * 0.4, s * 0.25, DARK_TOP, DARK_L, DARK_R)
    drop = Dot(iso.p(x0 + s * 0.5, y0 + s * 0.5, z0 + s * 1.15), radius=0.07, color=TERRA)
    return VGroup(body, neck, drop)


def paper(x, y, w=2.4, h=3.0, tilt=0.0, fill=PAGE_TOP):
    """A flat 2-D sheet (the scattered-pages drawing): white page, ink outline, kraft drop shadow.
    `tilt` in radians. Returns a VGroup; `.sheet` is the page rectangle for placing lines on it."""
    shadow = Rectangle(width=w, height=h, fill_color=BOX_L, fill_opacity=1, stroke_width=0).move_to([x + 0.12, y - 0.12, 0])
    sheet = Rectangle(width=w, height=h, fill_color=fill, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    g = VGroup(shadow, sheet)
    if tilt:
        g.rotate(tilt, about_point=[x, y, 0])
    g.sheet = sheet
    g.cx, g.cy, g.w, g.h, g.tilt = float(x), float(y), float(w), float(h), float(tilt)   # read these; never ask the stub for vertices
    return g


def scribble(x, y, w, amp=0.07, waves=None, color=INK, sw=4):
    """One wavy handwriting line from (x, y) rightwards for `w` units. Reads as script, never as type."""
    n = waves or max(3, int(round(w * 3)))
    pts = []
    for i in range(n * 4 + 1):
        t = i / (n * 4)
        pts.append([x + w * t, y + amp * np.sin(t * n * 2 * np.pi) * (0.6 + 0.4 * np.cos(t * 5.3)), 0])
    m = VMobject(stroke_color=color, stroke_width=sw)
    m.set_points_smoothly(pts)
    return m


def scribble_block(x, y, w, n=3, gap=0.34, last=0.62, color=INK, sw=4):
    """`n` scribble lines stacked downward from (x, y); the last one is `last`× as long (a paragraph end)."""
    return VGroup(*[scribble(x, y - i * gap, w * (last if i == n - 1 else 1.0), color=color, sw=sw) for i in range(n)])


def scribbles_on(page, n=3, inset=0.3, gap=0.34, color=INK, sw=4):
    """Scribble lines laid on a `paper()` group, following its tilt (uses the page's stored geometry)."""
    w = page.w - 2 * inset
    g = scribble_block(page.cx - w / 2, page.cy + page.h / 2 - inset - 0.1, w, n=n, gap=gap, color=color, sw=sw)
    if abs(page.tilt) > 1e-3:
        g.rotate(page.tilt, about_point=[page.cx, page.cy, 0])
    return g


def outline_tree(x, y, h=1.6, levels=2, spread=0.55, color=INK, node=TERRA):
    """A branching outline (the scroll drawing): a trunk rising from (x, y), forking `levels` times,
    a terracotta dot at every tip. Returns VGroup(lines, dots) — draw lines first, dots last."""
    lines, dots = VGroup(), VGroup()
    def grow(px, py, length, lvl, dx):
        qx, qy = px + dx, py + length
        lines.add(Line([px, py, 0], [qx, qy, 0], color=color, stroke_width=4))
        if lvl == 0:
            dots.add(Dot([qx, qy, 0], radius=0.075, color=node))
            return
        for d in (-spread, spread):
            grow(qx, qy, length * 0.62, lvl - 1, d * (0.75 ** (levels - lvl)))
    grow(x, y, h * 0.42, levels, 0.0)
    g = VGroup(lines, dots)
    g.lines, g.dots = lines, dots
    return g


def write_lines(self, q, lines, speed=1.6, hop=0.22, dip=0.06):
    """Animate the quill `q` WRITING each line in `lines`: the nib hops to the line's start, then the
    line draws while the nib rides its tip (the writing motion). `speed` is scene units per second.
    Call between `until()` phrases so each line lands on its words. Works with the midpoint guard."""
    for ln in lines:
        start = np.array(ln.get_start(), dtype=float)
        self.play(q.animate.shift(start - q.nib), run_time=hop, rate_func=smooth)
        q.nib = start.copy()
        off = np.array(q.get_center(), dtype=float) - q.nib
        def ride(m, a, ln=ln, off=off):
            m.move_to(np.array(ln.point_from_proportion(min(1.0, a)), dtype=float) + off)
        try:
            length = float(ln.get_arc_length())
        except Exception:          # Gate A's stub has no arc length; any positive number keeps the check moving
            length = 2.0
        rt = max(0.35, length / speed)
        self.play(Create(ln), UpdateFromAlphaFunc(q, ride), run_time=rt, rate_func=linear)
        q.nib = np.array(ln.get_end(), dtype=float)
        # the small lift between lines keeps the quill from fusing with the ink at GATE T's midpoint
        q.shift([0, dip, 0]); q.nib = q.nib + np.array([0, dip, 0])


def grow_tree(self, q, tree, per=0.45):
    """Animate the quill drawing an `outline_tree`: each segment draws as the nib rides it; dots land last."""
    for ln in tree.lines:
        start = np.array(ln.get_start(), dtype=float)
        self.play(q.animate.shift(start - q.nib), run_time=0.18, rate_func=smooth)
        q.nib = start.copy()
        off = np.array(q.get_center(), dtype=float) - q.nib
        def ride(m, a, ln=ln, off=off):
            m.move_to(np.array(ln.point_from_proportion(min(1.0, a)), dtype=float) + off)
        self.play(Create(ln), UpdateFromAlphaFunc(q, ride), run_time=per, rate_func=linear)
        q.nib = np.array(ln.get_end(), dtype=float)
    self.play(LaggedStart(*[GrowFromCenter(d) for d in tree.dots], lag_ratio=0.15), run_time=0.6)


# ═════════════════════════════ PROFESSOR BEAR (a person is never an icon) ═════════════════════════════
# PROFESSOR BEAR LAW (Bear, 2026-10-07): when a beat needs an icon of a person, or Professor Bear himself,
# do not draw a person token and do not pull a person icon. Show one of the Professor Bear portraits in
# brutalist.art/professor-bear/, chosen at random among those of the right aspect ratio (1x1 · 2x3 · 16x9).
# `./art bear <ratio> --seed <beat>` picks the same way from the shell.
def _pb_dir():
    env = _os.environ.get("ART_HOME")
    cands = [env and _os.path.join(env, "professor-bear")]
    here = _os.path.dirname(_os.path.abspath(__file__))
    for _ in range(8):
        cands.append(_os.path.join(here, "brutalist.art", "professor-bear"))
        cands.append(_os.path.join(here, "professor-bear"))
        here = _os.path.dirname(here)
    cands.append("/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/professor-bear")
    for c in cands:
        if c and _os.path.isdir(c):
            return c
    return cands[-1]


_PB_RATIOS = {"1x1": (1.0, 287), "2x3": (2 / 3, 46), "16x9": (16 / 9, 13)}


def _pb_circle(path):
    """A circular cut (alpha outside the circle), cached beside the set in _crops/. Cropping is fine (Bear, 2026-10-07)."""
    from PIL import Image as _Im, ImageDraw as _Dr
    out_dir = _os.path.join(_os.path.dirname(path), "_crops"); _os.makedirs(out_dir, exist_ok=True)
    out = _os.path.join(out_dir, _os.path.splitext(_os.path.basename(path))[0] + "-circle.png")
    if not _os.path.exists(out):
        im = _Im.open(path).convert("RGBA"); w, h = im.size; s = min(w, h); top = max(0, (h - s) // 3)
        im = im.crop(((w - s) // 2, top, (w - s) // 2 + s, top + s))
        mask = _Im.new("L", (s, s), 0); _Dr.Draw(mask).ellipse((0, 0, s - 1, s - 1), fill=255)
        im.putalpha(mask); im.save(out)
    return out


def professor_bear(ratio="2x3", height=3.0, seed=None, x=0.0, y=0.0, frame=True, shape="rect"):
    """A Professor Bear portrait (random within `ratio`; `seed` = the beat id for a stable pick across re-renders).
    Returns a Group: kraft drop shadow, the photo, an ink frame. Place with `x, y`; size with `height`.
    `shape="circle"` gives a round cut (use a 1x1 portrait). Cropping is fine: circle, rounded square, tight head shot."""
    import random as _random
    ar, n = _PB_RATIOS[ratio]
    k = _random.Random(str(seed) if seed is not None else None).randint(1, n)
    path = _os.path.join(_pb_dir(), f"professor-bear-{ratio}-{k:02d}.png")
    circle = shape == "circle"
    if circle:
        ar = 1.0
    w = height * ar
    if circle:
        shadow = Circle(radius=height / 2, fill_color=BOX_L, fill_opacity=1, stroke_width=0).move_to([x + 0.12, y - 0.12, 0])
        border = Circle(radius=height / 2, stroke_color=INK, stroke_width=4, fill_opacity=0).move_to([x, y, 0])
    else:
        shadow = Rectangle(width=w, height=height, fill_color=BOX_L, fill_opacity=1, stroke_width=0).move_to([x + 0.12, y - 0.12, 0])
        border = Rectangle(width=w, height=height, stroke_color=INK, stroke_width=4, fill_opacity=0).move_to([x, y, 0])
    try:
        img = ImageMobject(_pb_circle(path) if circle else path)
        img.height = height
        img.move_to([x, y, 0])
    except Exception:
        img = Rectangle(width=w, height=height, fill_color=BAR2, fill_opacity=1, stroke_width=0).move_to([x, y, 0])
    g = Group(shadow, img, border) if frame else Group(img)
    g.path = path
    return g


# ═════════════════════════════ pacing (narration is the clock) ═════════════════════════════
try:
    _SHEET = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}


def _elapsed(self):
    rt = getattr(getattr(self, "renderer", None), "time", None)
    return float(rt) if isinstance(rt, (int, float)) else 0.0


def until(self, phrase, lead=0.25):
    """Wait until `phrase` is spoken (its character share of the narration × the measured audio)."""
    bid = type(self).__name__.split("_")[0]
    n, target = _NARR.get(bid, ""), _TARGET.get(bid, 0)
    if not n or not target or phrase not in n:
        return
    gap = target * n.index(phrase) / len(n) - lead - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)


def finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    self.wait(max(0.3, target - _elapsed(self)) if target else 2.0)

# ═════════════════════════════ APPROVED ORIGINAL PROPS (subset of templates/iso_originals_25.py) ═════════════════════════════
# Pasted, not imported (Gate A copies only scenes.py). Only the props this film uses.
_ST_ORIGINALS_25 = {'memory-drawers': {'moves': {'drawer': [0.7794228634059948, 0.45]},
                    'parts': {'cabinet': [{'fill': '#DCC9AA',
                                           'kind': 'polygon',
                                           'pts': [[0.0, 0.0], [-1.3856406460551018, -0.8], [-1.3856406460551018, -2.8], [0.0, -2.0]],
                                           'stroke': '#3D3929',
                                           'width': 0.035},
                                          {'fill': '#C7AE86',
                                           'kind': 'polygon',
                                           'pts': [[0.0, 0.0], [1.7320508075688772, -1.0], [1.7320508075688772, -3.0], [0.0, -2.0]],
                                           'stroke': '#3D3929',
                                           'width': 0.035},
                                          {'fill': '#F3E9D8',
                                           'kind': 'polygon',
                                           'pts': [[0.0, -2.0], [1.7320508075688772, -3.0], [0.34641016151377535, -3.8], [-1.3856406460551018, -2.8]],
                                           'stroke': '#3D3929',
                                           'width': 0.035}],
                              'cabinet-top': [{'fill': '#DCC9AA',
                                               'kind': 'polygon',
                                               'pts': [[0.0, -1.96], [-1.3856406460551018, -2.76], [-1.3856406460551018, -2.88], [0.0, -2.08]],
                                               'stroke': '#3D3929',
                                               'width': 0.035},
                                              {'fill': '#C7AE86',
                                               'kind': 'polygon',
                                               'pts': [[0.0, -1.96], [1.7320508075688772, -2.96], [1.7320508075688772, -3.08], [0.0, -2.08]],
                                               'stroke': '#3D3929',
                                               'width': 0.035},
                                              {'fill': '#F3E9D8',
                                               'kind': 'polygon',
                                               'pts': [[0.0, -2.08], [1.7320508075688772, -3.08], [0.34641016151377535, -3.88],
                                                       [-1.3856406460551018, -2.88]],
                                               'stroke': '#3D3929',
                                               'width': 0.035}],
                              'drawer': [{'fill': '#B4AFA6',
                                          'kind': 'polygon',
                                          'pts': [[0.19918584287042088, -0.765], [-0.9266471820493491, -1.415], [-0.9266471820493491, -1.875],
                                                  [0.19918584287042088, -1.2249999999999999]],
                                          'stroke': '#3D3929',
                                          'width': 0.035},
                                         {'fill': '#8B8F96',
                                          'kind': 'polygon',
                                          'pts': [[0.19918584287042088, -0.765], [1.7060700454553441, -1.635],
                                                  [1.7060700454553441, -2.0949999999999998], [0.19918584287042088, -1.2249999999999999]],
                                          'stroke': '#3D3929',
                                          'width': 0.035},
                                         {'fill': '#D9D4C7',
                                          'kind': 'polygon',
                                          'pts': [[0.19918584287042088, -1.2249999999999999], [1.7060700454553441, -2.0949999999999998],
                                                  [0.580237020535574, -2.745], [-0.9266471820493491, -1.875]],
                                          'stroke': '#3D3929',
                                          'width': 0.035},
                                         {'fill': '#26221F',
                                          'kind': 'polygon',
                                          'pts': [[0.7707626093681503, -1.115], [0.6408587988004846, -1.19],
                                                  [0.6408587988004846, -1.2799999999999998], [0.7707626093681503, -1.2049999999999998]],
                                          'stroke': '#3D3929',
                                          'width': 0.035},
                                         {'fill': '#1E1B18',
                                          'kind': 'polygon',
                                          'pts': [[0.7707626093681503, -1.115], [1.3336791218280355, -1.44],
                                                  [1.3336791218280355, -1.5299999999999998], [0.7707626093681503, -1.2049999999999998]],
                                          'stroke': '#3D3929',
                                          'width': 0.035},
                                         {'fill': '#3A3530',
                                          'kind': 'polygon',
                                          'pts': [[0.7707626093681503, -1.2049999999999998], [1.3336791218280355, -1.5299999999999998],
                                                  [1.2037753112603697, -1.605], [0.6408587988004846, -1.2799999999999998]],
                                          'stroke': '#3D3929',
                                          'width': 0.035}],
                              'fixed-drawer-0': [{'fill': '#B4AFA6',
                                                  'kind': 'polygon',
                                                  'pts': [[0.19918584287042088, -0.16499999999999998], [-0.9266471820493491, -0.8150000000000001],
                                                          [-0.9266471820493491, -1.275], [0.19918584287042088, -0.625]],
                                                  'stroke': '#3D3929',
                                                  'width': 0.035},
                                                 {'fill': '#8B8F96',
                                                  'kind': 'polygon',
                                                  'pts': [[0.19918584287042088, -0.16499999999999998], [1.7060700454553441, -1.035],
                                                          [1.7060700454553441, -1.495], [0.19918584287042088, -0.625]],
                                                  'stroke': '#3D3929',
                                                  'width': 0.035},
                                                 {'fill': '#D9D4C7',
                                                  'kind': 'polygon',
                                                  'pts': [[0.19918584287042088, -0.625], [1.7060700454553441, -1.495], [0.580237020535574, -2.145],
                                                          [-0.9266471820493491, -1.275]],
                                                  'stroke': '#3D3929',
                                                  'width': 0.035},
                                                 {'fill': '#26221F',
                                                  'kind': 'polygon',
                                                  'pts': [[0.7707626093681503, -0.515], [0.6408587988004846, -0.5900000000000001],
                                                          [0.6408587988004846, -0.68], [0.7707626093681503, -0.605]],
                                                  'stroke': '#3D3929',
                                                  'width': 0.035},
                                                 {'fill': '#1E1B18',
                                                  'kind': 'polygon',
                                                  'pts': [[0.7707626093681503, -0.515], [1.3336791218280355, -0.8400000000000001],
                                                          [1.3336791218280355, -0.93], [0.7707626093681503, -0.605]],
                                                  'stroke': '#3D3929',
                                                  'width': 0.035},
                                                 {'fill': '#3A3530',
                                                  'kind': 'polygon',
                                                  'pts': [[0.7707626093681503, -0.605], [1.3336791218280355, -0.93], [1.2037753112603697, -1.005],
                                                          [0.6408587988004846, -0.68]],
                                                  'stroke': '#3D3929',
                                                  'width': 0.035}],
                              'fixed-drawer-2': [{'fill': '#B4AFA6',
                                                  'kind': 'polygon',
                                                  'pts': [[0.19918584287042088, -1.3649999999999998], [-0.9266471820493491, -2.0149999999999997],
                                                          [-0.9266471820493491, -2.4749999999999996], [0.19918584287042088, -1.8249999999999997]],
                                                  'stroke': '#3D3929',
                                                  'width': 0.035},
                                                 {'fill': '#8B8F96',
                                                  'kind': 'polygon',
                                                  'pts': [[0.19918584287042088, -1.3649999999999998], [1.7060700454553441, -2.235],
                                                          [1.7060700454553441, -2.695], [0.19918584287042088, -1.8249999999999997]],
                                                  'stroke': '#3D3929',
                                                  'width': 0.035},
                                                 {'fill': '#D9D4C7',
                                                  'kind': 'polygon',
                                                  'pts': [[0.19918584287042088, -1.8249999999999997], [1.7060700454553441, -2.695],
                                                          [0.580237020535574, -3.3449999999999998], [-0.9266471820493491, -2.4749999999999996]],
                                                  'stroke': '#3D3929',
                                                  'width': 0.035},
                                                 {'fill': '#26221F',
                                                  'kind': 'polygon',
                                                  'pts': [[0.7707626093681503, -1.715], [0.6408587988004846, -1.79],
                                                          [0.6408587988004846, -1.8800000000000001], [0.7707626093681503, -1.8050000000000002]],
                                                  'stroke': '#3D3929',
                                                  'width': 0.035},
                                                 {'fill': '#1E1B18',
                                                  'kind': 'polygon',
                                                  'pts': [[0.7707626093681503, -1.715], [1.3336791218280355, -2.04], [1.3336791218280355, -2.13],
                                                          [0.7707626093681503, -1.8050000000000002]],
                                                  'stroke': '#3D3929',
                                                  'width': 0.035},
                                                 {'fill': '#3A3530',
                                                  'kind': 'polygon',
                                                  'pts': [[0.7707626093681503, -1.8050000000000002], [1.3336791218280355, -2.13],
                                                          [1.2037753112603697, -2.205], [0.6408587988004846, -1.8800000000000001]],
                                                  'stroke': '#3D3929',
                                                  'width': 0.035}]}}}

def make_original(prop_id, height=3.2, x=0.0, y=0.0):
    """Return native VGroup with .parts and scale-correct .action_vectors."""
    from manim import VGroup, Polygon, VMobject, Circle
    import numpy as np
    if not np.isfinite(height) or height <= 0:
        raise ValueError('height must be positive and finite')
    p = _ST_ORIGINALS_25[prop_id]
    pts = []
    for name, shapes in p['parts'].items():
        dx, dy = p['moves'].get(name, (0, 0))
        for s in shapes:
            q = s.get('pts') or [(s['cx']-s['r'],s['cy']-s['r']), (s['cx']+s['r'],s['cy']+s['r'])]
            pts.extend(q)
            pts.extend((a+dx, b+dy) for a,b in q)
    x0,y0 = min(a for a,b in pts), min(b for a,b in pts)
    x1,y1 = max(a for a,b in pts), max(b for a,b in pts)
    scale = min(height/(y1-y0), 4.8/(x1-x0))
    cx,cy = (x0+x1)/2, (y0+y1)/2
    def point(a,b): return np.array([(a-cx)*scale+x, -(b-cy)*scale+y, 0])
    rig = VGroup()
    rig.parts, rig.action_vectors = {}, {}
    for name, shapes in p['parts'].items():
        part = VGroup()
        for s in shapes:
            if s['kind'] == 'circle':
                mob = Circle(radius=s['r']*scale).move_to(point(s['cx'],s['cy']))
            elif s['kind'] == 'polygon':
                mob = Polygon(*[point(a,b) for a,b in s['pts']])
            else:
                mob = VMobject().set_points_as_corners([point(a,b) for a,b in s['pts']])
            mob.set_fill(s['fill'] if s['fill']!='none' else '#FFFFFF', opacity=0 if s['fill']=='none' else 1)
            mob.set_stroke(s['stroke'] if s['stroke']!='none' else '#FFFFFF', width=s['width']*100, opacity=0 if s['stroke']=='none' else 1)
            part.add(mob)
        rig.parts[name] = part
        rig.add(part)
        if name in p['moves']:
            dx,dy = p['moves'][name]
            rig.action_vectors[name] = np.array([dx*scale, -dy*scale, 0])
    return rig


# ═════════════════════════════ FILM: How RAG Works (show-tell-how-rag-works) ═════════════════════════════
# One drawn beat per scene. Cast for the whole film: the kraft BOX (handbook), three PAGES, paper SLIPS
# (chunks; the returns chunk carries a terracotta dot, the stale FAQ chunk a folded corner), the SCANNER
# arch over a BELT, bar STRIPS (embeddings: 29 slots, real TF-IDF weights), the DRAWER cabinet
# (vector store, approved original `memory-drawers`) with its LAMP panel, the PROMPT sheet, the dark MODEL
# block, and the ANSWER card.
#
# Timing: reveals sit on spoken words from mp3/words.json (align.py); frames are counted as
# ceil(run_time * fps); nothing moves inside the GATE T / V midpoint window (45–55 % of the beat, ± 0.22 s).
# Gate A pre-flights an isolated copy of this file, so every data file falls back to the reel folder,
# and every number used on screen is also inlined below.
import math
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REEL = Path(_os.environ.get("ART_REEL", r"C:/Users/anant/stem-films/youtube/show-tell-how-rag-works"))


def _load(rel, default):
    for base in (HERE, REEL):
        try:
            if (base / rel).exists():
                return _json.loads((base / rel).read_text(encoding="utf-8"))
        except Exception:
            pass
    return default


SHEET = _load("beat_sheet.json", {"beats": []})
WORDS = _load("mp3/words.json", {"fps": 24, "beats": {}})
EV = _load("demo/evidence.json", None)
FPS = 24
DUR = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in SHEET["beats"]}
NARR = {b["beat_id"]: b["narration_text"] for b in SHEET["beats"]}

# Evidence (demo/rag_demo.py → demo/evidence.json), inlined for the isolated Gate A copy and cross-checked.
DIMS, N_CHUNKS, ANS_RIGHT, ANS_STALE = 29, 6, "30 days", "14 days"
if EV:
    assert EV["film"]["dims"] == DIMS and EV["film"]["n_chunks"] == N_CHUNKS
    assert EV["film"]["A_answer"] == ANS_RIGHT and EV["film"]["B_answer"] == ANS_STALE
# Non-zero embedding slots (index, weight) of each chunk in run A, and of the question; printed from
# rag_demo.build_store / embed_query (see BUILD-LOG). Zero slots are drawn as ghost ticks.
VEC = {
    "returns#1": [(0, .45), (7, .37), (11, .37), (17, .45), (20, .45), (27, .37)],
    "returns#2": [(2, .45), (4, .45), (8, .45), (18, .45), (21, .45)],
    "shipping#1": [(3, .43), (7, .35), (15, .43), (22, .43), (24, .43), (27, .35)],
    "shipping#2": [(1, .5), (9, .5), (13, .5), (23, .5)],
    "warranty#1": [(10, .48), (11, .39), (14, .48), (25, .39), (28, .48)],
    "warranty#2": [(5, .39), (6, .39), (12, .39), (16, .39), (19, .39), (25, .32), (26, .39)],
    "question": [(11, .63), (20, .77)],
}
ORDER = ["returns#1", "returns#2", "shipping#1", "shipping#2", "warranty#1", "warranty#2"]
DEEP = "#9C8462"          # deep kraft: threads, belt edge (never fuses with ink). Arrows are INK, never terracotta.
BELT = "#E6E1D5"          # within 28 of the stage


def _norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def cue(bid, phrase):
    """Beat-local seconds at which `phrase` starts (words.json); falls back to its character share."""
    words = WORDS.get("beats", {}).get(bid)
    want = [_norm(p) for p in phrase.split()]
    if words:
        toks = [_norm(w["text"]) for w in words]
        for i in range(len(toks) - len(want) + 1):
            if toks[i:i + len(want)] == want:
                return words[i]["startFrame"] / FPS
    n = NARR.get(bid, "")
    if n and phrase in n and DUR.get(bid):
        return DUR[bid] * n.index(phrase) / len(n)
    return 0.0


class Clock:
    """Narration clock in whole frames, with the midpoint guard (no motion in 45–55 % ± 0.22 s)."""

    def __init__(self, scene, bid):
        self.s, self.bid, self.t = scene, bid, 0.0
        self.D = DUR.get(bid) or 10.0
        self.g0, self.g1 = 0.45 * self.D - 0.22, 0.55 * self.D + 0.22

    def at(self, t):
        frames = int(math.floor((t - self.t) * FPS + 1e-6))
        if frames >= 1:
            self.s.wait(frames / FPS)          # wait() floors its frame count; play() ceils (measured 2026-11-22)
            self.t += frames / FPS

    def play(self, *anims, rt=0.8, rf=None):
        frames = max(1, int(math.ceil(rt * FPS - 1e-6)))
        if self.t < self.g1 and self.t + frames / FPS > self.g0:
            self.at(self.g1)
        kw = {"rate_func": rf} if rf else {}
        self.s.play(*anims, run_time=frames / FPS - 1e-6, **kw)
        self.t += frames / FPS

    def go(self, phrase, *anims, rt=0.8, lead=0.15):
        self.at(max(self.t, cue(self.bid, phrase) - lead))
        self.play(*anims, rt=rt)

    def end(self):
        if self.t > self.D:
            print(f"[clock] {self.bid}: overran audio by {self.t - self.D:.2f}s")
        self.at(self.D)


def L(s, x, y, size=40):
    """A label: ink, EB Garamond, size ≥ 32, placed beside its object."""
    return T(s, size=max(32, size)).move_to([x, y, 0])


# ── cast ──────────────────────────────────────────────────────────────────────────────────────────
def crate(ox, oy, s):
    """The handbook box: left, right, top faces + tape; also its open-box back for B01."""
    iso = Iso(ox, oy, s)
    closed = iso.box(0, 0, 0, 2.6, 2.0, 1.6)
    tape = iso.tape(0, 0, 1.6, 2.6, 2.0)
    back, front = iso.open_box(0, 0, 0, 2.6, 2.0, 1.6)
    return closed, tape, back, front


def shadow(x, y, w, h=0.9):
    s = Ellipse(width=w, height=h, fill_color=BAR2, fill_opacity=1, stroke_width=0).move_to([x, y, 0])
    s.set_z_index(-1)
    return s


def model_block(x, y, s=1.0):
    """The model: a dark block with one lamp (starts ghost; `light()` gives the terracotta lamp)."""
    iso = Iso(x, y, s)
    body = iso.box(0, 0, 0, 1.5, 1.5, 1.1, DARK_TOP, DARK_L, DARK_R)
    lamp = Dot(iso.p(1.05, 0, 0.55), radius=0.08, color=GHOST)
    g = VGroup(body, lamp)
    g.lamp_xy = iso.p(1.05, 0, 0.55)
    return g


def sheet(x, y, w, h, lines=2, edge=INK, ink=None):
    """A page or slip: white sheet, kraft drop shadow, wavy scribble lines (never glyphs)."""
    pg = paper(x, y, w, h)
    if edge != INK:
        pg.sheet.set_stroke(edge)
    inset = min(0.25, w * 0.14)
    gap = min(0.34, (h - 2 * inset) / max(1, lines))
    sc = VGroup(*[scribble(x - w / 2 + inset, y + h / 2 - inset - 0.08 - i * gap,
                           (w - 2 * inset) * (0.62 if i == lines - 1 and lines > 1 else 1.0),
                           amp=min(0.06, h * 0.06), color=ink or (BAR1 if edge != INK else INK), sw=3)
                  for i in range(lines)])
    return VGroup(pg, sc)


def slip(x, y, w=1.5, h=0.8, mark=False, dog=False, edge=INK):
    """A chunk. `mark`: the returns chunk (terracotta dot). `dog`: the stale FAQ chunk (folded corner)."""
    g = sheet(x, y, w, h, lines=1, edge=edge)
    if mark:
        g.add(Dot([x - w / 2 + 0.2, y - h / 2 + 0.2, 0], radius=0.07, color=TERRA))
    if dog:
        c = 0.3
        g.add(Polygon([x + w / 2 - c, y + h / 2, 0], [x + w / 2, y + h / 2 - c, 0], [x + w / 2 - c, y + h / 2 - c, 0],
                      fill_color=BOX_L, fill_opacity=1, stroke_color=edge, stroke_width=3))
    return g


def strip(x, y, key, slot=0.075, hmax=0.62):
    """An embedding: a base bar with 29 slots; non-zero slots grow grey bars to their weight. (x, y) = base centre."""
    w = DIMS * slot
    base = Rectangle(width=w + 0.12, height=0.1, fill_color=DIM, fill_opacity=1, stroke_width=0).move_to([x, y, 0])
    vals = dict(VEC[key])
    bars = VGroup()
    for j in range(DIMS):
        bx = x - w / 2 + slot * (j + 0.5)
        if j in vals:
            h = max(0.12, vals[j] / 0.8 * hmax)
            bars.add(Rectangle(width=slot * 0.66, height=h, fill_color=(BAR1 if j % 2 else INK), fill_opacity=1,
                               stroke_width=0).move_to([bx, y + 0.05 + h / 2, 0]))
        else:
            bars.add(Rectangle(width=slot * 0.5, height=0.07, fill_color=GHOST, fill_opacity=1,
                               stroke_width=0).move_to([bx, y + 0.085, 0]))
    return VGroup(base, bars)


def belt(x0, x1, y):
    body = RoundedRectangle(width=x1 - x0, height=0.5, corner_radius=0.25, fill_color=BELT, fill_opacity=1,
                            stroke_color=DEEP, stroke_width=4).move_to([(x0 + x1) / 2, y, 0])
    dashes = VGroup(*[Line([xx, y - 0.11, 0], [xx, y + 0.11, 0], color=GHOST, stroke_width=4)
                      for xx in np.arange(x0 + 0.45, x1 - 0.3, 0.6)])
    return VGroup(body, dashes)


def arch(x, y, s=0.8):
    """The scanner: two dark posts and a beam, straddling the belt at (x, y). Returns (back, front, beam_xy)."""
    iso = Iso(x + 0.62 * s / 0.8, y - 0.36 * s / 0.8, s)
    back = iso.box(0, 1.8, 0, 0.3, 0.3, 2.2, DARK_TOP, DARK_L, DARK_R)
    front = VGroup(iso.box(0, 0, 0, 0.3, 0.3, 2.2, DARK_TOP, DARK_L, DARK_R),
                   iso.box(0, 0, 2.2, 0.3, 2.1, 0.32, DARK_TOP, DARK_L, DARK_R))
    back.set_z_index(1); front.set_z_index(4)
    lamp = Dot(iso.p(0.15, 0.9, 2.52), radius=0.07, color=GHOST).set_z_index(5)
    return back, front, lamp


def scan_line(x, y):
    return Line([x, y + 1.55, 0], [x, y - 0.2, 0], color=TERRA, stroke_width=6).set_z_index(3)


CAB_H = 4.2


def cabinet(x, y, h=CAB_H):
    """The vector store: the approved `memory-drawers` rig plus a lamp panel on its left (six lamps)."""
    rig = make_original("memory-drawers", height=h, x=x, y=y)
    k = h / 3.88
    py = y + h / 2 + 0.35
    panel = RoundedRectangle(width=2.6 * k, height=0.42, corner_radius=0.12, fill_color=DARK_L, fill_opacity=1,
                             stroke_width=0).move_to([x, py, 0])
    lamps = [Dot([x + (-1.0 + 0.4 * i) * k, py, 0], radius=0.07, color=GHOST) for i in range(6)]
    lit = [Dot([x + (-1.0 + 0.4 * i) * k, py, 0], radius=0.08, color=TERRA) for i in range(6)]
    return rig, VGroup(panel, *lamps), lit, py


def answer_card(x, y):
    # soft-grey squiggles: a short dark-ink squiggle reads as a sub-41-px text run under GATE T §8.1
    return sheet(x, y, 1.9, 1.2, lines=2, ink=BAR1)


# ─────────────────────────────────────────────────────────────────── B00 the hero arrives
class B10_Handbook(Scene):
    def construct(self):
        c = Clock(self, "B10")
        closed, tape, _, _ = crate(-1.7, -2.5, 1.15)
        box = VGroup(closed, tape)
        sh = shadow(-1.3, -2.55, 5.4)
        mb = model_block(3.7, -1.3, 1.0)
        dash = DashedLine([3.3, 0.35, 0], [1.6, 0.35, 0], color=DIM, stroke_width=5, dash_length=0.18)
        q = T("?", 72).move_to([1.15, 0.4, 0])
        box.shift(UP * 2.6)
        c.at(0.2)
        c.play(box.animate.shift(DOWN * 2.6), rt=0.7, rf=ease_in)
        c.play(FadeIn(sh), rt=0.3)
        c.go("Here, it's", FadeIn(mb, shift=LEFT * 0.4), FadeIn(L("model", 4.85, -2.15, 40)), rt=0.6)
        c.go("handbook", FadeIn(L("handbook", -5.1, 0.7, 44)), rt=0.5)
        c.go("can only guess", Create(dash), FadeIn(q), rt=0.7)
        c.end()


# ─────────────────────────────────────────────────────────────────── B01 it opens: three pages
PG_X, PG_Y, PG_W, PG_H = [-4.6, -1.7, 1.2], 2.05, 1.6, 1.95
PG_NAMES = ["returns", "shipping", "warranty"]


class B11_ThreePages(Scene):
    def construct(self):
        c = Clock(self, "B11")
        closed, tape, back, front = crate(-1.7, -2.5, 1.15)
        sh = shadow(-1.3, -2.55, 5.4)
        mb = model_block(3.7, -1.3, 1.0)
        ml = L("model", 4.85, -2.15, 40)
        self.add(sh, closed, tape, mb, ml)
        k, piv = 0.5, np.array([-1.3, -2.6, 0])
        back.scale(k, about_point=piv)
        closed[0].set_z_index(2); closed[1].set_z_index(2); back.set_z_index(0)
        c.at(0.2)
        c.play(VGroup(closed, tape, sh).animate.scale(k, about_point=piv), rt=0.6)
        top = closed[2]
        c.play(FadeOut(tape), FadeOut(top), FadeIn(back), rt=0.5)
        pages = [sheet(x, PG_Y, PG_W, PG_H, lines=3) for x in PG_X]
        pages[0].add(Dot([PG_X[0] - PG_W / 2 + 0.25, PG_Y - PG_H / 2 + 0.25, 0], radius=0.07, color=TERRA))
        for p in pages:
            p.scale(0.25).move_to([-1.35, -1.5, 0])
        labels = [L(n, x, PG_Y - PG_H / 2 - 0.4, 38) for n, x in zip(PG_NAMES, PG_X)]
        for i, (p, x) in enumerate(zip(pages, PG_X)):
            phrase = ["three documents", "shipping", "warranty"][i]
            c.go(phrase, p.animate.scale(4.0).move_to([x, PG_Y, 0]), FadeIn(labels[i]), rt=0.6)
        hand = pages[0].copy()
        c.go("the right page", hand.animate.scale(0.45).move_to([1.75, -1.75, 0]), rt=0.8)
        c.end()


# ─────────────────────────────────────────────────────────────────── B02 step one: chunks
ROW_Y, ROW_X, SL_W, SL_H = -1.5, [-5.0, -3.0, -1.0, 1.0, 3.0, 5.0], 1.6, 0.85


class B12_Chunks(Scene):
    def construct(self):
        c = Clock(self, "B12")
        px, py, pw, ph = [-4.0, 0.0, 4.0], 1.2, 1.9, 2.3
        pages = [sheet(x, py, pw, ph, lines=3) for x in px]
        pages[0].add(Dot([px[0] - pw / 2 + 0.25, py - ph / 2 + 0.25, 0], radius=0.07, color=TERRA))
        self.add(*pages)
        cut = [Line([x - pw / 2 - 0.2, py, 0], [x + pw / 2 + 0.2, py, 0], color=TERRA, stroke_width=6) for x in px]
        halves = []
        for i, x in enumerate(px):
            top = slip(x, py + 0.62, SL_W, SL_H, mark=(i == 0))
            bot = slip(x, py - 0.62, SL_W, SL_H)
            halves += [top, bot]
        c.at(0.2)
        lab = L("chunk", -4.0, -1.0, 40)
        c.play(Create(cut[0]), rt=0.5)
        c.play(FadeOut(pages[0]), FadeOut(cut[0]), FadeIn(halves[0]), FadeIn(halves[1]), FadeIn(lab), rt=0.6)
        c.go("into chunks", Create(cut[1]), Create(cut[2]), rt=0.5)
        c.play(FadeOut(pages[1]), FadeOut(pages[2]), FadeOut(cut[1]), FadeOut(cut[2]),
               *[FadeIn(h) for h in halves[2:]], rt=0.6)
        c.go("so each becomes", *[h.animate.move_to([ROW_X[j], ROW_Y, 0]) for j, h in enumerate(halves)],
             FadeOut(lab), rt=1.0)
        c.go("Six chunks", FadeIn(L("6 chunks", 0.0, -2.75, 46)),
             Create(Line([-5.9, ROW_Y - 0.62, 0], [5.9, ROW_Y - 0.62, 0], color=DEEP, stroke_width=4)), rt=0.6)
        c.end()


# ─────────────────────────────────────────────────────────────────── B03 step two: embeddings
OUT_Y = [2.3, 1.35, 0.4, -0.55, -1.5, -2.45]
OUT_SX, OUT_BX = 2.1, 4.55
COL_X = -5.15


class B13_Scanner(Scene):
    def construct(self):
        c = Clock(self, "B13")
        slips = [slip(ROW_X[j], ROW_Y, SL_W, SL_H, mark=(j == 0)) for j in range(6)]
        self.add(*slips)
        bl = belt(-4.3, 0.9, 0.0)
        ab, af, lamp = arch(-1.7, 0.0)
        strips = [strip(OUT_BX, OUT_Y[j] - 0.3, ORDER[j]) for j in range(6)]
        c.at(0.2)
        c.play(*[s.animate.scale(0.7).move_to([COL_X, OUT_Y[j], 0]) for j, s in enumerate(slips)],
               FadeIn(bl), FadeIn(ab), FadeIn(af), rt=0.9)
        for s in slips:
            s.set_z_index(2)
        flash = scan_line(-1.7, 0.0)
        c.go("turn each chunk", slips[0].animate.move_to([-1.7, 0.05, 0]), rt=0.7)
        c.play(Create(flash), rt=0.3)
        c.play(FadeOut(flash), slips[0].animate.move_to([OUT_SX, OUT_Y[0], 0]), GrowFromEdge(strips[0], LEFT),
               FadeIn(L("embedding", OUT_BX, 3.0, 38)), rt=0.7)
        c.go("Our toy version", LaggedStart(*[AnimationGroup(slips[j].animate.move_to([OUT_SX, OUT_Y[j], 0]),
                                                             GrowFromEdge(strips[j], LEFT)) for j in range(1, 6)],
                                            lag_ratio=0.25), rt=1.8)
        c.go("twenty-nine key", FadeIn(L("29 numbers", OUT_BX, -3.05, 38)), rt=0.5)
        c.go("Real systems", lamp.animate.set_color(TERRA), Indicate(VGroup(ab, af), color=INK, scale_factor=1.04), rt=0.7)
        c.end()


# ─────────────────────────────────────────────────────────────────── B04 step three: the vector store
CAB_X, CAB_Y = 3.75, -0.2
SRC_X, STR_X = -5.15, -2.75


class B14_Drawers(Scene):
    def construct(self):
        c = Clock(self, "B14")
        slips = [slip(OUT_SX, OUT_Y[j], SL_W, SL_H, mark=(j == 0)).scale(0.7) for j in range(6)]
        strips = [strip(OUT_BX, OUT_Y[j] - 0.3, ORDER[j]) for j in range(6)]
        self.add(*slips, *strips)
        rig, panel, lit, px = cabinet(CAB_X, CAB_Y)
        c.at(0.2)
        c.play(*[s.animate.shift(LEFT * (OUT_SX - SRC_X)) for s in slips],
               *[s.animate.shift(LEFT * (OUT_BX - STR_X)) for s in strips], rt=0.8)
        c.play(FadeIn(rig, shift=LEFT * 0.3), FadeIn(panel), rt=0.6)
        c.go("vector store", FadeIn(L("vector store", CAB_X, -3.0, 40)),
             rig.parts["drawer"].animate.shift(rig.action_vectors["drawer"]), rt=0.6)
        dest = np.array([CAB_X + 0.5, CAB_Y - 0.2, 0])
        for j in range(6):
            off = dest - np.array([STR_X, OUT_Y[j] - 0.3, 0])
            c.play(strips[j].animate.shift(off).scale(0.25).set_opacity(0), FadeIn(lit[j]), rt=0.42)
        c.go("This happens once", rig.parts["drawer"].animate.shift(-rig.action_vectors["drawer"]), rt=0.6)
        c.end()


# ─────────────────────────────────────────────────────────────────── B05 the question, embedded the same way
class B15_Question(Scene):
    def construct(self):
        c = Clock(self, "B15")
        slips = [slip(SRC_X, OUT_Y[j], SL_W, SL_H, mark=(j == 0)).scale(0.7) for j in range(6)]
        rig, panel, lit, px = cabinet(CAB_X, CAB_Y)
        self.add(*slips, rig, panel, *lit)
        bl = belt(-5.0, 0.2, 0.0)
        ab, af, lamp = arch(-2.6, 0.0)
        qs = slip(-5.4, 0.05, 1.3, 0.75).set_z_index(2)
        qm = T("?", 64).move_to([-5.4, 0.95, 0]).set_z_index(2)
        qg = VGroup(qs, qm)
        qstrip = strip(-1.0, -1.3, "question")
        c.at(0.2)
        c.play(*[FadeOut(s) for s in slips], FadeIn(bl), FadeIn(ab), FadeIn(af), rt=0.7)
        c.go("question arrives", FadeIn(qg, shift=RIGHT * 0.5), FadeIn(L("question", -5.05, -0.95, 40)), rt=0.6)
        flash = scan_line(-2.6, 0.0)
        c.go("same scanner", FadeOut(qm), qs.animate.shift(RIGHT * 2.8), rt=0.8)
        c.play(Create(flash), rt=0.3)
        c.play(FadeOut(flash), qs.animate.shift(RIGHT * 2.6), GrowFromEdge(qstrip, LEFT), rt=0.7)
        tip = Dot([-1.0 + DIMS * 0.075 / 2 + 0.2, -1.25, 0], radius=0.08, color=TERRA)
        c.go("same space", FadeIn(tip), rt=0.4)
        c.play(VGroup(qstrip, tip).animate.shift(RIGHT * 0.55), rt=0.6)
        c.end()


# ─────────────────────────────────────────────────────────────────── B06 step four: nearest chunks retrieved
# Executed ranking for the question (demo/evidence.json, run A): rank 1-3 of six chunks.
RANK = [("returns#1", "within 30 days", 0.5774), ("warranty#1", "one year warranty", 0.2494),
        ("returns#2", "receipt and charger", 0.0)]
if EV:
    _ra = EV["runs"]["A"]["ranking"]
    assert [(r["id"], r["score"]) for r in _ra[:3]] == [(k, v) for k, _, v in RANK], "B06 disagrees with evidence"
    assert EV["film"]["question"] == "How long do I have to return a laptop?"
R_SX, R_QY, R_Y = -3.75, 2.35, [0.95, -0.55, -2.05]
R_BX, R_BW = -1.95, 4.2           # score bars: left edge, length of a score of 1.0


class B16_Ranking(Scene):
    def construct(self):
        c = Clock(self, "B16")
        rig, panel, lit, py = cabinet(4.45, -0.45, 3.4)
        self.add(rig, panel, *lit)
        q = strip(R_SX, R_QY, "question")
        qtip = Dot([R_SX + DIMS * 0.075 / 2 + 0.2, R_QY + 0.05, 0], radius=0.08, color=TERRA)
        rows = [strip(R_SX, y, k) for (k, _, _), y in zip(RANK, R_Y)]
        w = DIMS * 0.075
        guides = VGroup(*[DashedLine([R_SX - w / 2 + 0.075 * (j + 0.5), R_QY - 0.12, 0],
                                     [R_SX - w / 2 + 0.075 * (j + 0.5), R_Y[-1] - 0.12, 0],
                                     color=DIM, stroke_width=3, dash_length=0.1)
                          for j, _ in VEC["question"]]).set_z_index(-1)
        bars, nums, labs = [], [], []
        for (k, name, v), y in zip(RANK, R_Y):
            ln = v * R_BW
            if ln > 0:
                bars.append(Rectangle(width=ln, height=0.3, fill_color=BAR1, fill_opacity=1, stroke_width=0)
                            .move_to([R_BX + ln / 2, y + 0.12, 0]))
            else:   # a zero score gets no bar (a stub beside the numeral reads as part of the type)
                bars.append(Dot([R_BX + 0.06, y + 0.12, 0], radius=0.06, color=BAR1))
            nums.append(L(f"{v:.2f}", R_BX + ln + 0.75, y + 0.14, 44))
            labs.append(L(name, -0.15, y + 0.72, 38))
        c.at(0.2)
        c.play(FadeIn(q), FadeIn(qtip), FadeIn(L("question", -1.3, R_QY + 0.3, 40)), rt=0.6)
        c.play(LaggedStart(*[FadeIn(r, shift=DOWN * 0.15) for r in rows], lag_ratio=0.25), rt=0.8)
        c.go("compares", Create(guides), rt=0.8)
        c.go("The returns chunk", GrowFromEdge(bars[0], LEFT), FadeIn(labs[0]), FadeIn(nums[0]), rt=0.8)
        c.go("The warranty chunk", GrowFromEdge(bars[1], LEFT), FadeIn(labs[1]), FadeIn(nums[1]), rt=0.8)
        c.go("The other four", FadeIn(bars[2]), FadeIn(labs[2]), FadeIn(nums[2]), rt=0.8)
        c.go("score zero", Create(check(R_BX + R_BW * RANK[0][2] + 1.8, R_Y[0] + 0.12, 0.18)), rt=0.5)
        c.end()


# ─────────────────────────────────────────────────────────────────── B07 step five: into the prompt
CAB2_X, CAB2_Y, CAB2_H = -4.2, -0.4, 3.6
SH_X, SH_Y, SH_W, SH_H = 0.2, 0.0, 3.4, 4.7
TOP1, TOP2, QY = (SH_X, 1.15), (SH_X, 0.05), (SH_X, -1.35)
MB_X, MB_Y = 3.6, 0.15


def prompt_sheet():
    return paper(SH_X, SH_Y, SH_W, SH_H)


class B17_Prompt(Scene):
    def construct(self):
        c = Clock(self, "B17")
        rig, panel, lit, px = cabinet(CAB2_X, CAB2_Y, CAB2_H)
        q = slip(3.0, -2.3, 1.5, 0.7, edge=BAR1).set_z_index(2)
        self.add(rig, panel, *lit, q)
        ps = prompt_sheet()
        mb = model_block(MB_X, MB_Y)
        s1 = slip(CAB2_X + 0.4, CAB2_Y - 0.3, 2.4, 0.8, mark=True, edge=BAR1).scale(0.4).set_z_index(2)
        s2 = slip(CAB2_X + 0.4, CAB2_Y - 0.3, 2.4, 0.8, edge=BAR1).scale(0.4).set_z_index(2)
        instr = scribble(SH_X - 1.3, 2.05, 2.6, color=INK, sw=4)
        c.at(0.2)
        c.play(FadeIn(ps), FadeIn(L("prompt", SH_X, -3.0, 40)), FadeIn(mb), rt=0.7)
        c.go("top two chunks", rig.parts["drawer"].animate.shift(rig.action_vectors["drawer"]), FadeIn(s1), FadeIn(s2), rt=0.5)
        c.play(s1.animate.scale(2.5).move_to([TOP1[0], TOP1[1], 0]), s2.animate.scale(2.5).move_to([TOP2[0], TOP2[1], 0]),
               rt=0.8)
        c.go("above the question", q.animate.move_to([QY[0], QY[1], 0]).scale(1.4), rt=0.7)
        c.go("one instruction", Create(instr), rt=0.8)
        arr = Arrow([SH_X + SH_W / 2 + 0.15, 0.4, 0], [MB_X - 0.8, 0.4, 0], buff=0, color=INK, stroke_width=6,
                    max_tip_length_to_length_ratio=0.25)
        c.go("in front of the model", GrowArrow(arr), rig.parts["drawer"].animate.shift(-rig.action_vectors["drawer"]), rt=0.6)
        c.end()


def prompt_state(scene, top=("returns", "warranty"), arrow=True):
    """Rebuild the B07 end state: cabinet, lamps, prompt sheet with two chunks + question, model, arrow."""
    rig, panel, lit, px = cabinet(CAB2_X, CAB2_Y, CAB2_H)
    ps = prompt_sheet()
    sl = {"returns": slip(TOP1[0], TOP1[1], 2.4, 0.8, mark=True, edge=BAR1),
          "warranty": slip(TOP2[0], TOP2[1], 2.4, 0.8, edge=BAR1)}
    q = slip(QY[0], QY[1], 2.1, 0.98, edge=BAR1)
    instr = scribble(SH_X - 1.3, 2.05, 2.6, color=INK, sw=4)
    mb = model_block(MB_X, MB_Y)
    arr = Arrow([SH_X + SH_W / 2 + 0.15, 0.4, 0], [MB_X - 0.8, 0.4, 0], buff=0, color=INK, stroke_width=6,
                max_tip_length_to_length_ratio=0.25)
    scene.add(rig, panel, *lit, ps, sl["returns"], sl["warranty"], q, instr, mb, arr)
    return rig, sl, mb


ANS_X, ANS_Y = 4.9, -1.75


# ─────────────────────────────────────────────────────────────────── B08 the grounded answer
class B18_Answer(Scene):
    def construct(self):
        c = Clock(self, "B18")
        rig, sl, mb = prompt_state(self)
        lampon = Dot(mb.lamp_xy, radius=0.09, color=TERRA)
        card = answer_card(ANS_X, ANS_Y)
        num = L(ANS_RIGHT, ANS_X, ANS_Y - 1.05, 52)
        thread = ArcBetweenPoints(np.array([ANS_X - 1.0, ANS_Y + 0.2, 0]), np.array([TOP1[0] + 1.3, TOP1[1], 0]),
                                  angle=0.35, color=DEEP, stroke_width=5)
        c.at(0.2)
        c.play(FadeIn(lampon), FadeIn(L("illustrated", 5.1, 3.0, 36)), rt=0.5)
        c.go("writes a grounded answer", FadeIn(card, shift=DOWN * 0.4), rt=0.6)
        c.go("thirty days", FadeIn(num), rt=0.5)
        c.go("point back", Create(thread), FadeIn(L("source", 2.65, -0.95, 36)), rt=0.8)
        c.go("check it", Create(check(ANS_X - 1.75, ANS_Y - 1.0, 0.18)), rt=0.5)
        c.end()


# ─────────────────────────────────────────────────────────────────── B10 the confident wrong answer
class B20_WrongAnswer(Scene):
    def construct(self):
        c = Clock(self, "B20")
        rig, sl, mb = prompt_state(self)
        old = slip(CAB2_X + 0.4, CAB2_Y - 0.3, 2.4, 0.8, dog=True, edge=BAR1).scale(0.4)
        card = answer_card(ANS_X, ANS_Y)
        num = L(ANS_STALE, ANS_X, ANS_Y - 1.05, 52)
        thread = ArcBetweenPoints(np.array([ANS_X - 1.0, ANS_Y + 0.2, 0]), np.array([TOP1[0] + 1.3, TOP1[1], 0]),
                                  angle=0.35, color=DEEP, stroke_width=5)
        ring = Circle(radius=1.05, color=TERRA, stroke_width=6).move_to([CAB2_X - 0.15, CAB2_Y - 0.17, 0])
        c.at(0.2)
        c.play(FadeIn(old), FadeIn(L("illustrated", 5.1, 3.0, 36)), rt=0.4)
        c.go("leads with the old", old.animate.scale(2.5).move_to([TOP1[0], TOP1[1], 0]),
             sl["returns"].animate.move_to([TOP2[0], TOP2[1], 0]), FadeOut(sl["warranty"]), rt=0.8)
        c.play(FadeIn(L("old FAQ", SH_X, 2.85, 36)), rt=0.4)
        c.go("can answer fourteen", FadeIn(card, shift=DOWN * 0.4), FadeIn(num), rt=0.6)
        c.go("Nothing in the writing", Create(check(ANS_X - 1.75, ANS_Y - 1.0, 0.18)), Create(thread), rt=0.7)
        c.go("at retrieval", Create(ring), FadeIn(L("retrieval", CAB2_X + 0.2, -3.0, 38)), rt=0.7)
        c.end()


# ─────────────────────────────────────────────────────────────────── B11 the fix lives in the store
class B21_Fix(Scene):
    def construct(self):
        c = Clock(self, "B21")
        rig, panel, lit, px = cabinet(CAB2_X, CAB2_Y, CAB2_H)
        ps = prompt_sheet()
        old = slip(TOP1[0], TOP1[1], 2.4, 0.8, dog=True, edge=BAR1)
        ret = slip(TOP2[0], TOP2[1], 2.4, 0.8, mark=True, edge=BAR1)
        q = slip(QY[0], QY[1], 2.1, 0.98, edge=BAR1)
        instr = scribble(SH_X - 1.3, 2.05, 2.6, color=INK, sw=4)
        mb = model_block(MB_X, MB_Y)
        arr = Arrow([SH_X + SH_W / 2 + 0.15, 0.4, 0], [MB_X - 0.8, 0.4, 0], buff=0, color=INK, stroke_width=6,
                    max_tip_length_to_length_ratio=0.25)
        card = answer_card(ANS_X, ANS_Y)
        stale = L(ANS_STALE, ANS_X, ANS_Y - 1.05, 52)
        ring = Circle(radius=1.05, color=TERRA, stroke_width=6).move_to([CAB2_X - 0.15, CAB2_Y - 0.17, 0])
        self.add(rig, panel, *lit, ps, old, ret, q, instr, mb, arr, card, stale, ring)
        war = slip(TOP2[0], TOP2[1], 2.4, 0.8, edge=BAR1)
        right = L(ANS_RIGHT, ANS_X, ANS_Y - 1.05, 52)
        c.at(0.2)
        c.play(FadeOut(ring), FadeIn(L("store", CAB2_X + 0.2, -3.0, 40)), rt=0.5)
        c.go("Take the old page", old.animate.shift(UP * 0.9).set_opacity(0), rt=0.7)
        c.go("back on top", ret.animate.move_to([TOP1[0], TOP1[1], 0]), FadeIn(war, shift=UP * 0.2), rt=0.7)
        c.go("Nobody retrained", FadeOut(stale), FadeIn(right), rt=0.5)
        c.play(Create(check(ANS_X - 1.75, ANS_Y - 1.0, 0.18)), rt=0.4)
        c.end()


# ─────────────────────────────────────────────────────────────────── B12 why now: 21 million passages
def mini_cabinet(iso, x, y, fresh=False):
    body = iso.box(x, y, 0, 1.4, 1.4, 1.6, BOX_TOP if fresh else "#E9E3D6", BOX_L if fresh else BAR3, BOX_R if fresh else BAR2)
    lines = VGroup(*[Line(iso.p(x, y + 0.2, z), iso.p(x, y + 1.2, z), color=BAR1, stroke_width=4) for z in (0.55, 1.05)])
    g = VGroup(body, lines)
    if fresh:
        g.add(Dot(iso.p(x + 0.7, y, 1.2), radius=0.07, color=TERRA))
    return g


class B22_Scale(Scene):
    def construct(self):
        c = Clock(self, "B22")
        rig, panel, lit, px = cabinet(-2.0, -0.3, 3.6)
        self.add(rig, panel, *lit)
        iso = Iso(-2.3, -2.9, 0.5)
        cells = [(i, j) for j in (2, 1, 0) for i in (4, 3, 2, 1, 0)]      # back to front (painter's order)
        grid = {ij: mini_cabinet(iso, ij[0] * 2.0, ij[1] * 2.0) for ij in cells}
        c.at(0.2)
        c.play(FadeIn(L("RAG", -5.2, 2.2, 48)), rt=0.5)
        c.go("named it", FadeOut(rig), FadeOut(panel), *[FadeOut(d) for d in lit],
             LaggedStart(*[FadeIn(grid[ij], shift=DOWN * 0.15) for ij in cells], lag_ratio=0.06), rt=1.4)
        c.go("twenty-one million", FadeIn(L("21M", 3.9, 1.2, 120), scale=0.8), rt=0.6)
        c.play(FadeIn(L("per Lewis et al. 2020", 3.9, -0.2, 36)), rt=0.4)
        old_ij = (2, 0)
        new = mini_cabinet(iso, 4.0, 0.0, fresh=True)
        c.go("swapping in", grid[old_ij].animate.shift(np.array([-1.2, -0.7, 0])).set_opacity(0), rt=0.6)
        c.play(FadeIn(new, shift=DOWN * 0.4), rt=0.6)
        c.end()
