"""Manim scenes for "Week 6 Progress" (Keya G.).

One scene per Manim beat in beat_sheet.json:
B01_ThisWeeksVideo     the explainer's title, CAPTCHAs on websites and two research studies, built with Claude Code
B02_FilmAsCodeDeeper   film as code, deeper: landscape and vertical frames, same narration, different checks, 41 and 72
B03_NothingUnchecked   the rule: nothing goes in unless it is checked against a source; five things to fix; each easy to fix
B04_ShapesLikeText     the text-size check flagged dial ticks as tiny letters; a paler colour fixed it, no words changed
B05_FourNumbers        a numbered verdict card split one sentence across four numbers; rewritten as four complete thoughts
B06_Takeaway           websites check how I behave; a check is only as good as what it measures; claims, sources, frames

Simple drawn shapes only, in the same style as the Week 3 progress video: no photos, no person icons, no company
or tool logos. No Google, reCAPTCHA or Cloudflare logos and no screenshots of real challenge pages: a CAPTCHA is
only ever a plain drawn grid of squares, and Claude Code a generic drawn terminal.
Scene length comes from actual_duration_s in beat_sheet.json. The go() times are word timings measured from each
beat's narration audio (faster-whisper), so re-check them if that audio is regenerated.

PORTRAIT: this file is the 16:9 layout. The 9:16 copy is this file with PORTRAIT = True, which re-lays every scene
natively for a 4.5 x 8 frame (nothing is a crop). Portrait rules: text at least PORTRAIT_MIN_FS (about 88 px of ink at
2160 x 3840, above the 72 px rule), nothing below 86% of the frame height, scenes fill the stage. The QC scan in
Timed prints any text that breaks them. Edit this file, then re-copy.

Gate T: no thin tick marks or outlines near text. The dial ticks are pale and kept away from every label.
"""
import json
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).resolve().parent
PORTRAIT = False

# Portrait sync: Manim CE takes pixel dims from -r W,H but leaves frame_width at the 16:9 default.
if PORTRAIT:
    try:
        _pw, _ph = config.pixel_width, config.pixel_height
        if _pw and _ph and abs(config.frame_width - config.frame_height * _pw / _ph) > 0.01:
            config.frame_width = config.frame_height * (_pw / _ph)
    except Exception:
        pass

DUR = {"B01": 12.63, "B02": 16.9, "B03": 18.26, "B04": 10.86, "B05": 9.09, "B06": 12.76}
for _p in (HERE / "beat_sheet.json", HERE.parent / "beat_sheet.json"):
    if _p.is_file():
        DUR = {b["beat_id"]: b["actual_duration_s"] for b in json.loads(_p.read_text())["beats"]}
        break

# humanitarians palette: runtime/remotion/src/tokens/humanitarians.ts
CREAM = "#F3EBDD"
INK = "#2F2A26"
TEAL = "#1F4E5F"      # good / done / kept
CRIMSON = "#E4572E"   # the one accent: what breaks or changes
SLATE = "#29335C"     # structure
GOLD = "#F3A712"      # fill only, never text
PAPER = "#FBF7EE"     # card ground
SOFT = "#6B6458"      # secondary text
LINE = "#BDB3A2"      # hairlines, placeholder bars
BORDER = "#A89E8C"    # outline of cards that enclose text: kept off the ink mask so Gate T reads the text, not the frame


PORTRAIT_MIN_FS = 30   # measured: Garamond x-height ink is about 2.9 px per pt at 2160 x 3840, so 30 is about 88 px
PORTRAIT_FLOOR = -2.88  # 86% of the frame height measured from the top


def L(land, port):
    return port if PORTRAIT else land


# the stage: one big window per scene, filling the safe area (Gate V needs >= 55% of it)
SX = L(6.2, 1.9)          # half width
ST = L(3.35, 3.4)         # top
SB = L(-3.35, -2.9)       # bottom (portrait: text stays above 86% of the height)
SCY = (ST + SB) / 2
SW = 2 * SX
SH = ST - SB
IW = SW - 0.5
RT = ST - 0.8             # content region: under the title bar, inside the stage
RB = SB + 0.25
RX = SX - 0.2
RW = 2 * RX
RH = RT - RB
RCY = (RT + RB) / 2


PORTRAIT_ROW_W = 3.1   # widest single text line in portrait (the stage is 3.8 wide)


def _row(s, font, size, color, kw):
    t = Text(s, font=font, font_size=size, color=color, **kw)
    if PORTRAIT and t.width > PORTRAIT_ROW_W:
        t.scale(PORTRAIT_ROW_W / t.width)
    return t


def _lines(text, font, size, color, kw):
    """Manim Text left-aligns the lines of a multi-line string; build each line separately so it is centred."""
    kw.pop("line_spacing", None)
    if "\n" not in text:
        return _row(text, font, size, color, kw)
    rows = [_row(s, font, size, color, kw) for s in text.split("\n")]
    return VGroup(*rows).arrange(DOWN, buff=size * 0.004)


def T(text, size=40, color=INK, **kw):
    return _lines(text, "EB Garamond", size, color, kw)


def M(text, size=30, color=INK, **kw):
    return _lines(text, "Menlo", size, color, kw)


def fit(mob, max_w, max_h=None):
    if mob.width > max_w:
        mob.scale(max_w / mob.width)
    if max_h is not None and mob.height > max_h:
        mob.scale(max_h / mob.height)
    return mob


def fitfill(mob, max_w, max_h):
    """Fit a phase's cast to the content region. In portrait it also scales UP (never past 1.5x) so the cast
    fills the stage, as Gate V requires; in landscape it only shrinks, like fit()."""
    fit(mob, max_w, max_h)
    if PORTRAIT:
        k = min(max_w / mob.width, max_h / mob.height, 1.5)
        if k > 1:
            mob.scale(k)
    return mob


def card(w, h, color=INK, fill=PAPER, sw=4, r=0.16):
    if color == INK:
        color = BORDER
    return RoundedRectangle(corner_radius=r, width=w, height=h, stroke_color=color, stroke_width=sw,
                            fill_color=fill, fill_opacity=1)


def pchip(text, color=TEAL, size=30, fw=None, pad=0.5, tint=0.3):
    """Label chip: INK text on a pale tint of the colour. A dark fill with light text reads to Gate T as
    broken fragments, so the tint carries the colour and the text stays INK."""
    t = T(text, size, INK)
    if fw:
        fit(t, fw)
    box = RoundedRectangle(corner_radius=0.14, width=t.width + pad, height=t.height + 0.3,
                           stroke_width=0, fill_color=interpolate_color(ManimColor(PAPER), ManimColor(color), tint),
                           fill_opacity=1)
    t.move_to(box)
    return VGroup(box, t)


def tick(s=0.3, color=TEAL, sw=7):
    return VMobject(stroke_color=color, stroke_width=sw).set_points_as_corners(
        [[-s, 0, 0], [-s * 0.3, -s * 0.7, 0], [s, s * 0.8, 0]])


def cross(s=0.28, color=CRIMSON, sw=8):
    return VGroup(Line([-s, -s, 0], [s, s, 0], stroke_color=color, stroke_width=sw),
                  Line([-s, s, 0], [s, -s, 0], stroke_color=color, stroke_width=sw))


def eye(s=1.0, color=INK):
    out = VMobject(stroke_color=color, stroke_width=5).set_points_smoothly(
        [[-0.6, 0, 0], [0, 0.34, 0], [0.6, 0, 0], [0, -0.34, 0], [-0.6, 0, 0]])
    return VGroup(out, Circle(radius=0.17, stroke_color=color, stroke_width=4, fill_color=color,
                              fill_opacity=1)).scale(s)


def lines_block(n, w, color=LINE, h=0.13, gap=0.3, first=0.8):
    rows = VGroup(*[RoundedRectangle(corner_radius=0.06, width=w * (first if i == 0 else 1 - 0.12 * (i % 3)),
                                     height=h, stroke_width=0, fill_color=color, fill_opacity=1)
                    for i in range(n)])
    rows.arrange(DOWN, aligned_edge=LEFT, buff=gap)
    return rows


def stage(label="", lsize=28, lcol=None):
    frame = card(SW, SH, INK, PAPER, 5, 0.22).move_to([0, SCY, 0])
    bar = Line([-SX, ST - 0.6, 0], [SX, ST - 0.6, 0], stroke_color=INK, stroke_width=3)
    dots = VGroup(*[Dot(radius=0.07, color=c) for c in (CRIMSON, GOLD, TEAL)]).arrange(RIGHT, buff=0.14)
    dots.move_to([-SX + 0.55, ST - 0.3, 0])
    g = VGroup(frame, bar, dots)
    if label:
        t = T(label, lsize, lcol if lcol is not None else SOFT).move_to([0.5 if not PORTRAIT else 0.35, ST - 0.3, 0])
        fit(t, SW - 1.5)
        g.add(t)
    return g


def STAGE(label):
    return stage(label, L(28, 40), L(None, INK))


def lay(items, buff=0.5, w=None, h=None, cy=None):
    """Items side by side in 16:9, one under the other in 9:16, centred in the content region."""
    g = VGroup(*items).arrange(DOWN if PORTRAIT else RIGHT, buff=buff)
    fit(g, (w or RW - 0.4), (h or RH - 0.2))
    g.move_to([0, RCY if cy is None else cy, 0])
    return g


# ---- drawn pieces -------------------------------------------------------------------------------
def doc(w, h, n=4, color=INK, lines=LINE, lh=0.14):
    c = card(w, h, color, PAPER, 4)
    return VGroup(c, lines_block(n, w - 0.7, color=lines, h=lh, gap=max(0.14, (h - 0.7) / n - lh)).move_to(c))


def term(w, h, rows=3):
    c = card(w, h, INK, PAPER, 4)
    d = VGroup(*[Dot(radius=0.06, color=col) for col in (CRIMSON, GOLD, TEAL)]).arrange(RIGHT, buff=0.12)
    d.move_to(c.get_corner(UL) + np.array([0.45, -0.3, 0]))
    chev = VMobject(stroke_color=TEAL, stroke_width=6).set_points_as_corners(
        [[-0.12, 0.14, 0], [0.08, 0, 0], [-0.12, -0.14, 0]])
    chev.move_to(c.get_corner(UL) + np.array([0.4, -0.85, 0]))
    bars = lines_block(rows, w - 1.4, h=0.13, gap=0.28).move_to(c.get_center() + DOWN * 0.1 + RIGHT * 0.2)
    return VGroup(c, d, chev, bars)


def player(w, h):
    c = card(w, h, INK, PAPER, 4)
    tri = Triangle(stroke_width=0, fill_color=TEAL, fill_opacity=1).scale(min(w, h) * 0.2).rotate(-PI / 2)
    tri.move_to(c.get_center() + UP * h * 0.08)
    bar = Line(c.get_bottom() + UP * 0.3 + LEFT * (w / 2 - 0.4), c.get_bottom() + UP * 0.3 + RIGHT * (w / 2 - 0.4),
               stroke_color=LINE, stroke_width=8)
    knob = Dot(radius=0.1, color=INK).move_to(bar.get_start() + RIGHT * w * 0.3)
    return VGroup(c, tri, bar, knob)


def clock(r=0.5, color=INK, hands=(0.0, 1.0)):
    c = Circle(radius=r, stroke_color=color, stroke_width=5, fill_color=PAPER, fill_opacity=1)
    a = Line(ORIGIN, UP * r * 0.7, stroke_color=color, stroke_width=5).rotate(-hands[0] * TAU, about_point=ORIGIN)
    b = Line(ORIGIN, UP * r * 0.5, stroke_color=color, stroke_width=5).rotate(-hands[1] * TAU, about_point=ORIGIN)
    return VGroup(c, a, b, Dot(radius=0.05, color=color))


def target(r=0.45, color=INK):
    return VGroup(Circle(radius=r, stroke_color=color, stroke_width=5),
                  Circle(radius=r * 0.4, stroke_color=color, stroke_width=4),
                  Line(LEFT * r * 1.25, RIGHT * r * 1.25, stroke_color=color, stroke_width=4),
                  Line(DOWN * r * 1.25, UP * r * 1.25, stroke_color=color, stroke_width=4))


def star(r=0.35):
    return Star(5, outer_radius=r, inner_radius=r * 0.45, stroke_width=0, fill_color=GOLD, fill_opacity=1)


def cap(text, size=40, color=INK, **kw):
    return T(text, L(size, size), color, **kw)


class Timed:
    _min_fs = 999

    def setup(self):
        self.camera.background_color = CREAM
        self._min_fs = 999

    @property
    def now(self):
        return self.renderer.time

    def scan(self):
        """Print a QC line for any visible text that is too small, too low, or off the stage."""
        try:
            for m in self.mobjects:
                for s in m.get_family():
                    if isinstance(s, Text) and float(s.get_fill_opacity()) > 0.05 and float(s.width) > 0:
                        fs = float(s.font_size)
                        self._min_fs = min(self._min_fs, fs)
                        if PORTRAIT and fs < PORTRAIT_MIN_FS - 0.5:
                            print(f"QC {self.BEAT}: text '{s.text[:24]}' is {fs:.0f} (< {PORTRAIT_MIN_FS})")
                        if PORTRAIT and s.get_bottom()[1] < PORTRAIT_FLOOR:
                            print(f"QC {self.BEAT}: text '{s.text[:24]}' sits below the 86% line")
                        if s.get_left()[0] < -(SX - 0.05) or s.get_right()[0] > SX - 0.05:
                            print(f"QC {self.BEAT}: text '{s.text[:24]}' touches the stage edge")
        except (TypeError, AttributeError):
            pass

    def out(self, keep):
        """FadeOut for everything on screen except the stage frame, so no phase leaves anything behind."""
        return [FadeOut(m) for m in list(self.mobjects) if m is not keep]

    def go(self, t, *anims, rt=0.5):
        gap = t - self.now
        if gap > 1e-3:
            self.wait(gap)
        elif gap < -0.05:
            print(f"QC {self.BEAT}: cue {t}s is late by {-gap:.2f}s")
        if anims:
            self.play(*anims, **({} if rt is None else {"run_time": rt}))
        self.scan()

    def finish(self):
        self.scan()
        gap = DUR[self.BEAT] - self.now
        if gap > 1e-3:
            self.wait(gap)
        else:
            print(f"QC {self.BEAT}: scene ends {-gap:.2f}s after its audio")


def timed(beat):
    """Give a scene the Timed helpers. Each scene stays `class Name(Scene)` because the runner
    finds scenes by that exact text, so a Scene subclass would be missed."""
    def wrap(cls):
        for name, value in vars(Timed).items():
            if not name.startswith("__"):
                setattr(cls, name, value)
        cls.BEAT = beat
        return cls
    return wrap


#

# ---- extra drawn pieces ------------------------------------------------------------------------
def phone(w, h, color=INK):
    """A generic drawn phone outline. No app, no logo."""
    c = RoundedRectangle(corner_radius=0.3, width=w, height=h, stroke_color=color, stroke_width=5,
                         fill_color=PAPER, fill_opacity=1)
    n = RoundedRectangle(corner_radius=0.05, width=w * 0.3, height=0.1, stroke_width=0, fill_color=LINE,
                         fill_opacity=1).move_to(c.get_top() + DOWN * 0.22)
    return VGroup(c, n)


def wave(n, w, h, color=INK, seed=3):
    """Deterministic audio-wave bars, centred on the middle line."""
    rng = np.random.RandomState(seed)
    hs = 0.25 + 0.75 * rng.rand(n)
    bw = w / (n * 1.7)
    bars = VGroup(*[RoundedRectangle(corner_radius=bw / 2, width=bw, height=max(0.08, h * k), stroke_width=0,
                                     fill_color=color, fill_opacity=1) for k in hs])
    bars.arrange(RIGHT, buff=bw * 0.7)
    return bars


def ruler(length, color=INK, ticks=11):
    base = Line(LEFT * length / 2, RIGHT * length / 2, stroke_color=color, stroke_width=6)
    tk = VGroup(*[Line([-length / 2 + i * length / (ticks - 1), 0, 0],
                       [-length / 2 + i * length / (ticks - 1), 0.28 if i % 5 == 0 else 0.16, 0],
                       stroke_color=color, stroke_width=4) for i in range(ticks)])
    return VGroup(base, tk)


def curve_icon(w=1.0, h=0.7, color=TEAL):
    ax = VGroup(Line([0, 0, 0], [0, h, 0], stroke_color=INK, stroke_width=4),
                Line([0, 0, 0], [w, 0, 0], stroke_color=INK, stroke_width=4))
    pts = [[w * t, h * (0.05 + 0.9 * np.exp(-3.2 * t)), 0] for t in np.linspace(0.02, 1, 14)]
    cv = VMobject(stroke_color=color, stroke_width=6).set_points_smoothly(pts)
    return VGroup(ax, cv).move_to(ORIGIN)


def loop_icon(r=0.35, color=TEAL):
    arc = Arc(radius=r, start_angle=0.5, angle=TAU * 0.78, stroke_color=color, stroke_width=6)
    tip = Triangle(stroke_width=0, fill_color=color, fill_opacity=1).scale(0.13)
    tip.rotate(arc.get_end()[1] * 0 + PI / 2 + 0.5).move_to(arc.get_end())
    return VGroup(arc, tip)


def boxes_icon(color=INK):
    return VGroup(*[Rectangle(width=0.32, height=0.32 + 0.14 * i, stroke_color=color, stroke_width=4,
                              fill_color=PAPER, fill_opacity=1) for i in range(3)]).arrange(RIGHT, buff=0.06, aligned_edge=DOWN)


def icon_row(icon, label, w, h=0.78, size=40):
    c = card(w, h, INK, PAPER, 4, 0.14)
    ic = icon.copy()
    fit(ic, 0.62, h - 0.2)
    ic.move_to(c.get_left() + RIGHT * 0.55)
    t = T(label, size)
    t.next_to(ic, RIGHT, buff=0.28)
    if PORTRAIT and t.get_right()[0] > c.get_right()[0] - 0.12:      # keep the label inside its card
        t.scale((c.get_right()[0] - 0.12 - t.get_left()[0]) / t.width)
    return VGroup(c, ic, t)


def bigtick(color=TEAL):
    return tick(0.4, color, 9)


# ---- shared drawn pieces -----------------------------------------------------------------------
def grow(g, w, h):
    """Fit the cast to the content region, then scale it up (never past 1.7x in 16:9, 1.5x in 9:16) so it fills the stage."""
    fit(g, w, h)
    k = min(w / g.width, h / g.height, L(1.7, 1.5))
    if k > 1:
        g.scale(k)
    return g


def place(items, buff=0.4, pad=0.2, cy=None):
    """Stack the cast (side by side in 16:9, top to bottom in 9:16), fill the content region, centre it."""
    g = VGroup(*items).arrange(DOWN if PORTRAIT else RIGHT, buff=buff)
    grow(g, RW - pad, RH - 0.1)
    g.move_to([0, RCY if cy is None else cy, 0])
    return g


def column(items, buff=0.4, pad=0.2):
    """Stack the cast top to bottom in both layouts."""
    g = VGroup(*items).arrange(DOWN, buff=buff)
    grow(g, RW - pad, RH - 0.1)
    g.move_to([0, RCY, 0])
    return g


def cursor(color, h=0.4):
    bar = Rectangle(width=0.08, height=h, stroke_width=0, fill_color=color, fill_opacity=1)
    flag = Rectangle(width=0.24, height=0.12, stroke_width=0, fill_color=color, fill_opacity=1)
    flag.next_to(bar, UP, buff=0, aligned_edge=LEFT)
    return VGroup(bar, flag)


def shared_doc(w, h, cursors=True):
    """A generic drawn page: plain lines and two cursors in the same sentence. No app, no logo."""
    c = card(w, h, INK, PAPER, 4)
    rows = lines_block(4, w - 0.8, h=0.14, gap=max(0.16, (h - 1.0) / 4 - 0.14)).move_to(c).shift(DOWN * 0.12)
    r = rows[1]
    y = r.get_center()[1]
    a = cursor(GOLD).move_to([r.get_left()[0] + r.width * 0.55, y, 0])
    b = cursor(TEAL).move_to([r.get_right()[0] + 0.14, y, 0])
    return VGroup(c, rows, a, b) if cursors else VGroup(c, rows)


def nodes_icon(w=1.6, h=1.0, color=TEAL):
    """Boxes and arrows: the drawn 'engineering' behind a tool."""
    ps = [np.array(p) for p in ([-w * 0.38, h * 0.2, 0], [w * 0.0, -h * 0.25, 0], [w * 0.38, h * 0.2, 0])]
    ls = VGroup(Line(ps[0], ps[1], stroke_color=color, stroke_width=5), Line(ps[1], ps[2], stroke_color=color, stroke_width=5))
    bx = VGroup(*[Square(side_length=0.3, stroke_color=color, stroke_width=5, fill_color=PAPER, fill_opacity=1).move_to(p)
                  for p in ps])
    return VGroup(ls, bx)


def backend(w, h, size=40):
    """Copy - server - copy, drawn as plain boxes with double arrows."""
    cs = []
    for s in ("copy", "server", "copy"):
        c = card(w, h, TEAL if s == "server" else INK, PAPER, 5 if s == "server" else 4, 0.14)
        cs.append(VGroup(c, T(s, size).move_to(c)))
    mk = (lambda: DoubleArrow(UP * 0.18, DOWN * 0.18, buff=0, color=INK, stroke_width=6)) if PORTRAIT \
        else (lambda: DoubleArrow(LEFT * 0.35, RIGHT * 0.35, buff=0, color=INK, stroke_width=6))
    return VGroup(cs[0], mk(), cs[1], mk(), cs[2]).arrange(DOWN if PORTRAIT else RIGHT, buff=0.12 if PORTRAIT else 0.25)


def chev(side, s=0.32, color=TEAL):
    d = -1 if side == "l" else 1
    return VMobject(stroke_color=color, stroke_width=11).set_points_as_corners(
        [[-d * s * 0.7, s, 0], [d * s * 0.7, 0, 0], [-d * s * 0.7, -s, 0]])


def code_mark(s=1.0):
    """< / >: angle brackets around a slash."""
    sl = Line([0.18, 0.4, 0], [-0.18, -0.4, 0], stroke_color=CRIMSON, stroke_width=11)
    return VGroup(chev("l").shift(LEFT * 0.62), sl, chev("r").shift(RIGHT * 0.62)).scale(s)


def film_frame(w=1.6, h=1.1):
    c = card(w, h, INK, PAPER, 5, 0.12)
    tri = Triangle(stroke_width=0, fill_color=TEAL, fill_opacity=1).scale(min(w, h) * 0.2).rotate(-PI / 2).move_to(c)
    return VGroup(c, tri)


def slot_row(n, w, h, filled, gap=0.12):
    """n small blocks in a row; the first `filled` are teal, the rest outlined."""
    bs = VGroup(*[RoundedRectangle(corner_radius=0.06, width=w, height=h, stroke_color=BORDER, stroke_width=4,
                                   fill_color=PAPER, fill_opacity=1) for _ in range(n)]).arrange(RIGHT, buff=gap)
    return bs


def topic_card(w, h):
    c = card(w, h, INK, PAPER, 4, 0.12)
    return VGroup(c, lines_block(3, w - 0.5, h=0.12, gap=0.2).move_to(c))


# ---- Week 6 drawn pieces -----------------------------------------------------------------------
def frame_box(w, h, lines, color=INK):
    """A plain drawn video frame holding one or two stacked labels: [(text, size), ...]."""
    c = card(w, h, color, PAPER, 5, 0.12)
    parts = VGroup(*[T(t, s) for t, s in lines]).arrange(DOWN, buff=0.12)
    fit(parts, w - 0.3, h - 0.3)
    return VGroup(c, parts.move_to(c))


def wavepath(w, h, color=TEAL):
    """A smooth drawn mouse path: one thick curve, no ticks."""
    pts = [[-w / 2, -h * 0.35, 0], [-w * 0.22, h * 0.4, 0], [0, -h * 0.2, 0], [w * 0.24, h * 0.38, 0], [w / 2, -h * 0.05, 0]]
    return VMobject(stroke_color=color, stroke_width=10).set_points_smoothly(pts)


def pair_row(w, h, size=36, color=TEAL):
    """claim -> source: two plain cards and an arrow (side by side in 16:9, stacked in 9:16)."""
    if PORTRAIT:
        w, h, size = 3.0, 1.15, 42
    cl = VGroup(card(w, h, INK, PAPER, 4, 0.12))
    cl.add(T("claim", size).move_to(cl[0]))
    so = VGroup(card(w, h, color, PAPER, 5, 0.12))
    so.add(T("source", size).move_to(so[0]))
    ar = Arrow(UP * 0.4, DOWN * 0.4, buff=0, color=INK, stroke_width=6) if PORTRAIT \
        else Arrow(LEFT * 0.3, RIGHT * 0.3, buff=0, color=INK, stroke_width=6)
    return VGroup(cl, ar, so).arrange(DOWN if PORTRAIT else RIGHT, buff=L(0.35, 0.3))


def dial_quiet(r, tick_color):
    """A half dial: two thick arcs, a hub, and pale ticks. No text sits inside or near it."""
    a1 = Arc(radius=r, start_angle=PI / 2, angle=PI / 2, stroke_color=CRIMSON, stroke_width=14)
    a2 = Arc(radius=r, start_angle=0, angle=PI / 2, stroke_color=TEAL, stroke_width=14)
    ticks = VGroup(*[Line([(r - .28) * np.cos(a), (r - .28) * np.sin(a), 0], [(r - .06) * np.cos(a), (r - .06) * np.sin(a), 0],
                          stroke_color=tick_color, stroke_width=6) for a in np.linspace(0.12, PI - 0.12, 9)])
    hub = Dot(radius=.12, color=SLATE)
    return VGroup(a1, a2, ticks, hub)


def num_row(n, w, h, frac, fill=LINE):
    """One numbered line: the digit, then a bar `frac` of the available width."""
    num = T(str(n), L(40, 34))
    full = w - 1.0
    bar = RoundedRectangle(corner_radius=0.08, width=full * frac, height=h, stroke_width=0, fill_color=fill, fill_opacity=1)
    slot = Rectangle(width=full, height=h, stroke_width=0, fill_opacity=0)
    bar.align_to(slot, LEFT)
    return VGroup(num, VGroup(slot, bar)).arrange(RIGHT, buff=0.3)


# ---------------------------------------------------------------------------------------------
@timed("B01")
class B01_ThisWeeksVideo(Scene):
    def construct(self):
        st = STAGE("this week")
        # 1. the explainer's title, text only (0 - 3.9)
        lab = T(L("this week's explainer", "this week's\nexplainer"), L(44, 40))
        title = T(L("How Do Websites\nKnow I'm Not\na Robot?", "How Do\nWebsites\nKnow I'm\nNot a Robot?"), L(72, 46))
        uline = Line(LEFT * L(3.2, 1.3), RIGHT * L(3.2, 1.3), stroke_color=CRIMSON, stroke_width=9)
        column([lab, title, uline], 0.45, 0.4)
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.2, FadeIn(VGroup(lab, title, uline), shift=UP * 0.1), rt=0.5)
        self.go(3.9, *self.out(st), rt=0.25)
        # 2. CAPTCHAs on websites (4.0), then two research studies (6.3)
        sq = L(0.95, 0.9)
        cells = VGroup(*[RoundedRectangle(corner_radius=0.1, width=sq, height=sq, stroke_color=BORDER, stroke_width=4,
                                          fill_color=PAPER, fill_opacity=1) for _ in range(9)]).arrange_in_grid(rows=3, cols=3, buff=0.14)
        picks = VGroup(*[Circle(radius=sq * 0.22, stroke_width=0, fill_color=TEAL, fill_opacity=1).move_to(cells[i])
                         for i in (1, 4, 6)])
        gridg = VGroup(cells, picks)
        cap1 = T(L("CAPTCHAs on websites", "CAPTCHAs on\nwebsites"), L(50, 44))
        column([gridg, cap1], L(0.5, 0.4), 0.3)
        d1, d2 = doc(L(2.6, 1.7), L(3.3, 2.3), 4), doc(L(2.6, 1.7), L(3.3, 2.3), 4)
        papers = VGroup(d1, d2).arrange(RIGHT, buff=0.35)
        cap2 = T(L("two research studies", "two research\nstudies"), L(50, 44))
        column([papers, cap2], L(0.5, 0.4), 0.3)
        self.go(4.0, *self.out(st), FadeIn(gridg, shift=UP * 0.1), rt=0.4)
        self.go(4.5, FadeIn(cap1), rt=0.3)
        self.go(5.3, FadeIn(picks, lag_ratio=0.3), rt=0.4)
        self.go(6.3, *self.out(st), FadeIn(papers, shift=UP * 0.1), rt=0.4)
        self.go(6.9, FadeIn(cap2), rt=0.3)
        # 3. built with Claude Code: a drawn terminal (7.9)
        tm = term(L(5.4, 3.3), L(3.4, 2.6), 3)
        cc = pchip("Claude Code", TEAL, L(52, 44), fw=L(None, 2.9))
        column([tm, cc], L(0.55, 0.4), 0.3)
        self.go(7.9, *self.out(st), FadeIn(tm, shift=UP * 0.1), rt=0.5)
        self.go(8.7, FadeIn(cc), rt=0.35)
        # 4. everything was new for me (10.3)
        mini = VGroup(gridg.copy(), d1.copy(), tm.copy())
        for m_ in mini:
            fit(m_, L(2.2, 2.4), L(1.9, 1.3))
        mini.arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.4, 0.25))
        nw = pchip("all new for me", TEAL, L(56, 44), fw=L(None, 2.9))
        column([mini, nw], L(0.55, 0.4), 0.3)
        sr = star(L(0.55, 0.45)).move_to(nw.get_corner(UR) + np.array([0.1, 0.25, 0]))
        self.go(10.3, *self.out(st), FadeIn(mini, lag_ratio=0.15), rt=0.5)
        self.go(11.2, FadeIn(nw), FadeIn(sr, scale=0.5), rt=0.4)
        self.finish()


@timed("B02")
class B02_FilmAsCodeDeeper(Scene):
    def construct(self):
        st = STAGE("film as code")
        # 1. film as code, deeper (0 - 2.3)
        cm = code_mark(L(1.3, 0.8))
        ar = Arrow(LEFT * 0.4, RIGHT * 0.4, buff=0, color=INK, stroke_width=6) if not PORTRAIT \
            else Arrow(UP * 0.3, DOWN * 0.3, buff=0, color=INK, stroke_width=6)
        ff = film_frame(L(3.2, 1.3), L(2.3, 0.95))
        pair = VGroup(cm, ar, ff).arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.6, 0.35))
        t1 = T(L("film as code, deeper", "film as code,\ndeeper"), L(56, 46))
        column([pair, t1], L(0.5, 0.35), 0.3)
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.2, FadeIn(pair, shift=UP * 0.1), rt=0.4)
        self.go(0.9, FadeIn(t1), rt=0.35)
        # 2. landscape and vertical videos (2.4)
        wide = frame_box(L(4.6, 3.4), L(2.6, 1.6), [("landscape", L(52, 40))])
        tall = frame_box(L(2.4, 2.7), L(3.8, 2.8), [("vertical", L(52, 40))])
        place([wide, tall], L(0.8, 0.3))
        self.go(2.4, *self.out(st), FadeIn(wide[0]), FadeIn(tall[0]), rt=0.4)
        self.go(3.2, FadeIn(wide[1]), rt=0.3)
        self.go(4.15, FadeIn(tall[1]), rt=0.3)
        # 3. the narration is the same, but the checks are not (6.0)
        rows = []
        for ic, lb, chip_ in ((wave(L(9, 7), L(1.5, 1.0), L(0.9, 0.7), TEAL), "narration", pchip("the same", TEAL, L(48, 40), fw=L(None, 2.6))),
                              (boxes_icon(), "checks", pchip("not the same", CRIMSON, L(48, 40), fw=L(None, 2.7)))):
            ic = fit(ic, L(1.7, 0.9), L(1.2, 0.8))
            tl = T(lb, L(52, 44))
            if PORTRAIT:
                inner = VGroup(VGroup(ic, tl).arrange(RIGHT, buff=0.35), chip_).arrange(DOWN, buff=0.3)
            else:
                inner = VGroup(ic, VGroup(tl, chip_).arrange(DOWN, buff=0.25)).arrange(RIGHT, buff=0.5)
            bx = card(L(7.2, 3.4), inner.height + L(0.6, 1.3), INK, PAPER, 4, 0.16)
            inner.move_to(bx)
            rows.append(VGroup(bx, inner))
        column(rows, L(0.5, 0.35), 0.3)
        self.go(6.0, *self.out(st), FadeIn(rows[0][0]), rt=0.3)
        self.go(6.3, FadeIn(rows[0][1][:-1] if PORTRAIT else rows[0][1][0]), *([] if PORTRAIT else [FadeIn(rows[0][1][1][0])]), rt=0.3)
        self.go(7.1, FadeIn(rows[0][1][-1] if PORTRAIT else rows[0][1][1][1]), rt=0.3)
        self.go(7.8, FadeIn(rows[1][0]), rt=0.3)
        self.go(8.0, FadeIn(rows[1][1][:-1] if PORTRAIT else rows[1][1][0]), *([] if PORTRAIT else [FadeIn(rows[1][1][1][0])]), rt=0.3)
        self.go(8.5, FadeIn(rows[1][1][-1] if PORTRAIT else rows[1][1][1][1]), rt=0.3)
        # 4. text size: at least 41 for landscape (9.6), at least 72 for vertical (13.9)
        hd = pchip("text size", SLATE, L(52, 44), fw=L(None, 2.9))
        w2 = frame_box(L(4.6, 3.4), L(2.8, 2.2), [("landscape", L(40, 40)), ("at least", L(36, 36)), ("41 px", L(80, 60))])
        column([hd, w2], L(0.5, 0.4), 0.3)
        self.go(9.6, *self.out(st), FadeIn(hd), FadeIn(w2[0]), FadeIn(w2[1][0]), rt=0.5)
        self.go(11.9, FadeIn(w2[1][1]), rt=0.3)
        self.go(12.5, FadeIn(w2[1][2]), rt=0.3)
        hd2 = pchip("text size", SLATE, L(52, 44), fw=L(None, 2.9))
        t2 = frame_box(L(2.8, 2.7), L(3.8, 2.7), [("vertical", L(40, 40)), ("at least", L(36, 36)), ("72 px", L(80, 56))])
        column([hd2, t2], L(0.5, 0.4), 0.3)
        self.go(13.9, *self.out(st), FadeIn(hd2), FadeIn(t2[0]), FadeIn(t2[1][0]), rt=0.5)
        self.go(15.0, FadeIn(t2[1][1]), rt=0.3)
        self.go(15.7, FadeIn(t2[1][2]), rt=0.3)
        self.finish()


@timed("B03")
class B03_NothingUnchecked(Scene):
    def construct(self):
        st = STAGE("checked")
        # 1. my rule: nothing goes in unless it's checked against a source (0 - 5.5)
        pr = pair_row(L(4.2, 1.5), L(1.5, 1.15), L(40, 36))
        ca = T("my rule", L(54, 46))
        cb = T(L("nothing goes in unless it's\nchecked against a source", "nothing goes in\nunless it's checked\nagainst a source"), L(46, 34))
        column([pr, cb], L(0.6, 0.4), 0.3)
        ca.move_to(cb)
        tk = tick(0.28, TEAL, 10).move_to(pr[1])
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.2, FadeIn(pr, shift=UP * 0.1), rt=0.4)
        self.go(0.9, FadeIn(ca), rt=0.3)
        self.go(2.5, FadeOut(ca), FadeIn(cb), rt=0.3)
        self.go(4.6, FadeOut(pr[1]), Create(tk), rt=0.3)
        # 2. five things to fix: lines that said more, one source that could not be opened (5.5)
        rw, rh = L(7.2, 3.5), L(0.8, 0.5)
        rows = []
        for _ in range(5):
            c = card(rw, rh, INK, PAPER, 4, 0.12)
            bar = RoundedRectangle(corner_radius=0.07, width=rw * L(0.42, 0.34), height=L(0.2, 0.16), stroke_width=0,
                                   fill_color=SOFT, fill_opacity=1)
            sl = card(rw * L(0.26, 0.34), rh * 0.62, BORDER, PAPER, 3, 0.08)
            inner = VGroup(bar, sl).arrange(RIGHT, buff=L(0.7, 0.35)).move_to(c).shift(RIGHT * L(0.3, 0.2))
            rows.append(VGroup(c, inner))
        rg = VGroup(*rows).arrange(DOWN, buff=L(0.22, 0.14))
        h1 = pchip("five things to fix", CRIMSON, L(48, 40), fw=L(None, 2.9), tint=0.55)
        h1b = pchip(L("lines that said more\nthan the sources did", "lines that said\nmore than the\nsources did"), CRIMSON, L(46, 34), fw=L(None, 2.9), tint=0.55)
        h1c = pchip(L("one source that\ncouldn't be opened", "one source that\ncouldn't be\nopened"), SLATE, L(46, 34), fw=L(None, 2.9), tint=0.55)
        h2 = pchip(L("every line pointed\nto a source", "every line pointed\nto a source"), TEAL, L(46, 34), fw=L(None, 2.9), tint=0.55)
        h3 = pchip(L("each one was easy to fix", "each one was\neasy to fix"), TEAL, L(46, 34), fw=L(None, 2.9), tint=0.55)
        column([rg, h1b], L(0.4, 0.3), 0.2)
        h1.move_to(h1b)
        h1c.move_to(h1b)
        h2.move_to(h1b)
        h3.move_to(h1b)
        tks = VGroup(*[tick(0.2, TEAL, 9).move_to(r[0].get_left() + np.array([0.42, 0, 0])) for r in rows])
        def mark(r, col):
            return AnimationGroup(r[0].animate.set_stroke(col, 7), r[1][0].animate.set_fill(col, 1))

        self.go(5.5, *self.out(st), FadeIn(rg, lag_ratio=0.1), rt=0.5)
        self.go(7.3, FadeIn(h1), rt=0.3)
        self.go(7.5, LaggedStart(*[mark(r, CRIMSON) for r in rows], lag_ratio=0.3), rt=1.4)
        self.go(9.3, FadeOut(h1), FadeIn(h1b), rt=0.3)
        self.go(11.7, FadeOut(h1b), FadeIn(h1c), mark(rows[4], SLATE), rt=0.3)
        self.go(14.4, FadeOut(h1c), FadeIn(h2), *[AnimationGroup(r[0].animate.set_stroke(BORDER, 4), r[1][0].animate.set_fill(SOFT, 1)) for r in rows], rt=0.3)
        self.go(15.4, *[r[1][1].animate.set_fill(TEAL, 1).set_stroke(TEAL, 5) for r in rows], rt=0.5)
        self.go(16.5, FadeOut(h2), FadeIn(h3), rt=0.3)
        self.go(16.9, LaggedStart(*[AnimationGroup(mark(r, TEAL), Create(t_)) for r, t_ in zip(rows, tks)], lag_ratio=0.25), rt=0.7)
        self.finish()


@timed("B04")
class B04_ShapesLikeText(Scene):
    def construct(self):
        st = STAGE("text size")
        # 1. the text-size check surprised me (0 - 2.4)
        dc = doc(L(4.6, 3.0), L(3.4, 2.4), 4, lines=SOFT, lh=0.2)
        c1 = pchip(L("the text-size check", "the text-size\ncheck"), SLATE, L(48, 40), fw=L(None, 2.9), tint=0.55)
        column([dc, c1], L(0.6, 0.4), 0.3)
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.2, FadeIn(dc, shift=UP * 0.1), rt=0.4)
        self.go(0.7, FadeIn(c1), rt=0.3)
        # 2. it flagged tick marks on a dial: read as tiny letters (2.5)
        r = L(2.3, 1.45)
        dl = dial_quiet(r, BORDER)
        dgrp = VGroup(dl)
        pg = doc(L(4.6, 3.3), L(3.0, 1.7), 3, lines=SOFT, lh=0.2)
        top = VGroup(dgrp, pg).arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.7, 0.5))
        d1 = pchip(L("tick marks on a dial", "tick marks\non a dial"), SLATE, L(48, 40), fw=L(None, 2.9), tint=0.55)
        d2 = pchip(L("read as tiny letters", "read as tiny\nletters"), CRIMSON, L(48, 40), fw=L(None, 2.9), tint=0.55)
        column([top, d1], L(0.7, 0.5), 0.3)
        d2.move_to(d1)
        self.go(2.5, *self.out(st), FadeIn(top, shift=UP * 0.1), rt=0.5)
        self.go(2.9, FadeIn(d1), rt=0.4)
        self.go(5.1, FadeOut(d1), FadeIn(d2), rt=0.3)
        # 3. a paler colour fixed it, no words changed (6.8)
        dl2 = dial_quiet(r, LINE)
        dgrp2 = VGroup(dl2)
        ok = tick(0.3, TEAL, 11)
        ln = doc(L(4.6, 3.3), L(3.0, 1.7), 3, lines=SOFT, lh=0.2)
        top2 = VGroup(dgrp2, ln).arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.7, 0.5))
        e1 = pchip("a paler colour", TEAL, L(50, 40), fw=L(None, 2.9), tint=0.55)
        e2 = pchip(L("no words changed", "no words\nchanged"), TEAL, L(50, 40), fw=L(None, 2.9), tint=0.55)
        column([top2, e2], L(0.6, 0.5), 0.3)
        e1.move_to(e2)
        ok.move_to(dl2[3].get_center() + UP * r * 0.42)
        self.go(6.8, *self.out(st), FadeIn(top2, shift=UP * 0.1), FadeIn(e1), rt=0.5)
        self.go(8.3, Create(ok), rt=0.4)
        self.go(8.9, FadeOut(e1), FadeIn(e2), rt=0.3)
        self.finish()


@timed("B05")
class B05_FourNumbers(Scene):
    def construct(self):
        st = STAGE("verdict")
        cw = L(7.0, 2.8)
        # 1. a numbered list, one sentence split across four numbers (0 - 6.5)
        fr = [0.45, 0.7, 0.35, 0.55]
        rows = [num_row(i + 1, cw, L(0.3, 0.42), f, SOFT) for i, f in enumerate(fr)]
        rg = VGroup(*rows).arrange(DOWN, buff=L(0.7, 0.5), aligned_edge=LEFT)
        pg = card(cw + 0.7, rg.height + L(0.8, 0.8), INK, PAPER, 4, 0.16)
        rg.move_to(pg)
        lst = VGroup(pg, rg)
        a1 = T("a numbered list", L(54, 44))
        a2 = T(L("one sentence, four numbers", "one sentence,\nfour numbers"), L(54, 40))
        a3 = T("it read oddly", L(54, 44))
        column([lst, a2], L(0.5, 0.35), 0.3)
        a1.move_to(a2)
        a3.move_to(a2)
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.15, FadeIn(lst, shift=UP * 0.1), rt=0.4)
        self.go(0.6, FadeIn(a1), rt=0.3)
        self.go(2.4, FadeOut(a1), FadeIn(a2), rt=0.3)
        self.go(3.3, *[r[1][1].animate.set_fill(CRIMSON, 1) for r in rows], rt=0.6)
        self.go(5.1, FadeOut(a2), FadeIn(a3), rt=0.3)
        # 2. four complete thoughts (6.8)
        rows2 = [num_row(i + 1, cw, L(0.3, 0.42), 0.82, TEAL) for i in range(4)]
        rg2 = VGroup(*rows2).arrange(DOWN, buff=L(0.7, 0.5), aligned_edge=LEFT)
        pg2 = card(cw + 0.7, rg2.height + L(0.8, 0.8), INK, PAPER, 4, 0.16)
        rg2.move_to(pg2)
        lst2 = VGroup(pg2, rg2)
        b1 = pchip(L("four complete thoughts", "four complete\nthoughts"), TEAL, L(52, 36), fw=L(None, 2.9))
        column([lst2, b1], L(0.5, 0.35), 0.3)
        tks = VGroup(*[tick(0.2, TEAL, 9).move_to(r[1].get_right() + LEFT * 0.0) for r in rows2])
        for t_, r in zip(tks, rows2):
            t_.move_to([r[1].get_right()[0] - 0.25, r[1].get_center()[1], 0])
        self.go(6.8, *self.out(st), FadeIn(lst2, shift=UP * 0.1), rt=0.5)
        self.go(7.7, FadeIn(b1), LaggedStart(*[Create(t_) for t_ in tks], lag_ratio=0.3), rt=0.9)
        self.finish()


@timed("B06")
class B06_Takeaway(Scene):
    def construct(self):
        st = STAGE("check")
        # 1. more and more websites check how I behave (0 - 2.7)
        pg = card(L(4.6, 3.3), L(3.1, 2.8), INK, PAPER, 4, 0.14)
        wp = wavepath(L(3.6, 2.5), L(2.0, 2.0)).move_to(pg)
        cu = cursor(INK, 0.4).move_to(wp.get_end() + UP * 0.1)
        ey = eye(L(1.5, 1.1))
        scene1 = VGroup(VGroup(pg, wp, cu), ey).arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.7, 0.5))
        a1 = T(L("more and more websites\ncheck how I behave", "more and more\nwebsites check\nhow I behave"), L(48, 38))
        column([scene1, a1], L(0.6, 0.4), 0.3)
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.15, FadeIn(VGroup(pg, wp, cu), shift=UP * 0.1), FadeIn(ey), rt=0.4)
        self.go(0.45, FadeIn(a1), rt=0.3)
        # 2. a check is only as good as what it measures (2.8)
        ck = VGroup(card(L(1.9, 1.4), L(1.6, 1.4), TEAL, PAPER, 5, 0.12), tick(L(0.4, 0.4), TEAL, 11))
        ck[1].move_to(ck[0])
        ms = VGroup(card(L(2.7, 2.2), L(2.2, 1.4), INK, PAPER, 4, 0.12))
        ms.add(lines_block(3, ms[0].width - 0.7, h=0.14, gap=0.24).move_to(ms[0]))
        ar = Arrow(LEFT * 0.3, RIGHT * 0.3, buff=0, color=INK, stroke_width=6) if not PORTRAIT \
            else Arrow(UP * 0.2, DOWN * 0.2, buff=0, color=INK, stroke_width=6)
        meas = VGroup(ck, ar, ms).arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.4, 0.25))
        a2 = T(L("a check is only as good\nas what it measures", "a check is only\nas good as what\nit measures"), L(48, 38))
        column([meas, a2], L(0.6, 0.4), 0.3)
        self.go(2.8, *self.out(st), FadeIn(meas, shift=UP * 0.1), FadeIn(a2), rt=0.5)
        # 3. check my videos the same way (5.0)
        pv = player(L(4.6, 3.3), L(3.1, 3.0))
        tv = tick(0.35, TEAL, 12)
        vg = VGroup(pv, tv).arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.7, 0.4))
        a3 = T(L("check my videos the same way", "check my videos\nthe same way"), L(50, 40))
        column([vg, a3], L(0.6, 0.4), 0.3)
        self.go(5.6, *self.out(st), FadeIn(pv, shift=UP * 0.1), FadeIn(a3), rt=0.5)
        self.go(7.8, Create(tv), rt=0.4)
        # 4. every claim needs a source (8.4)
        pr = pair_row(L(4.2, 1.5), L(1.5, 1.15), L(40, 36))
        a4 = T(L("every claim needs a source", "every claim\nneeds a source"), L(52, 42))
        column([pr, a4], L(0.6, 0.4), 0.3)
        tk = tick(0.28, TEAL, 10).move_to(pr[1])
        self.go(9.0, *self.out(st), FadeIn(pr, shift=UP * 0.1), FadeIn(a4), rt=0.5)
        self.go(10.0, FadeOut(pr[1]), Create(tk), rt=0.3)
        # 5. every frame needs a second look (9.9)
        pv2 = player(L(4.6, 3.3), L(3.1, 3.0))
        ey2 = eye(L(1.6, 1.2))
        fg = VGroup(pv2, ey2).arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.7, 0.4))
        a5 = T(L("every frame needs a second look", "every frame needs\na second look"), L(50, 40))
        column([fg, a5], L(0.6, 0.4), 0.3)
        self.go(10.7, *self.out(st), FadeIn(pv2, shift=UP * 0.1), FadeIn(a5), rt=0.5)
        self.go(11.5, FadeIn(ey2, scale=0.6), rt=0.4)
        self.finish()
