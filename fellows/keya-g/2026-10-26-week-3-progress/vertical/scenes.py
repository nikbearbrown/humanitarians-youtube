"""Manim scenes for "Week 3 Progress" (Keya G.).

One scene per Manim beat in beat_sheet.json:
B01_ThisWeeksVideo     the explainer's title, a generic shared document used every day, and the backend behind it
B02_FilmAsCode         learning film as code one part at a time, going through Brutalist videos, how the pieces fit
B03_ChoosingTopics     topic cards kept and discarded, what other fellows made, where AI or STEM meets my interests
B04_ScriptAndChecks    the script as the source of every video, beat by beat with sources; every claim checked
B05_BehindTheTool      nothing especially hard; underneath: shifted, ordered, shared; a familiar tool feels new
B06_Takeaway           everyday tools hide interesting engineering; I learned to look behind them

Simple drawn shapes only, in the same style as the Week 5 progress video: no photos, no person icons, no company
or tool logos. No Google logo, Docs screenshots or branding: a shared document is only ever a generic drawn page
with plain lines and two cursors. Any file, frame or box shown is drawn, not a screenshot.
Scene length comes from actual_duration_s in beat_sheet.json. The go() times are word timings measured from each
beat's narration audio (faster-whisper), so re-check them if that audio is regenerated.

PORTRAIT: this file is the 16:9 layout. The 9:16 copy is this file with PORTRAIT = True, which re-lays every scene
natively for a 4.5 x 8 frame (nothing is a crop). Portrait rules: text at least PORTRAIT_MIN_FS (about 88 px of ink at
2160 x 3840, above the 72 px rule), nothing below 86% of the frame height, scenes fill the stage. The QC scan in
Timed prints any text that breaks them. Edit this file, then re-copy.
"""
import json
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).resolve().parent
PORTRAIT = True

# Portrait sync: Manim CE takes pixel dims from -r W,H but leaves frame_width at the 16:9 default.
if PORTRAIT:
    try:
        _pw, _ph = config.pixel_width, config.pixel_height
        if _pw and _ph and abs(config.frame_width - config.frame_height * _pw / _ph) > 0.01:
            config.frame_width = config.frame_height * (_pw / _ph)
    except Exception:
        pass

DUR = {"B01": 14.68, "B02": 11.07, "B03": 12.78, "B04": 15.08, "B05": 13.8, "B06": 6.85}
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


def pchip(text, color=TEAL, size=30, fw=None, pad=0.5):
    """Label chip: INK text on a pale tint of the colour. A dark fill with light text reads to Gate T as
    broken fragments, so the tint carries the colour and the text stays INK."""
    t = T(text, size, INK)
    if fw:
        fit(t, fw)
    box = RoundedRectangle(corner_radius=0.14, width=t.width + pad, height=t.height + 0.3,
                           stroke_width=0, fill_color=interpolate_color(ManimColor(PAPER), ManimColor(color), 0.3),
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
def doc(w, h, n=4, color=INK):
    c = card(w, h, color, PAPER, 4)
    return VGroup(c, lines_block(n, w - 0.7, h=0.14, gap=max(0.14, (h - 0.7) / n - 0.14)).move_to(c))


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


# ---------------------------------------------------------------------------------------------

# ---- Week 3 drawn pieces -----------------------------------------------------------------------
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


# ---------------------------------------------------------------------------------------------
@timed("B01")
class B01_ThisWeeksVideo(Scene):
    def construct(self):
        st = STAGE("this week")
        # 1. the explainer's title, text only (0 - 5.2)
        lab = T(L("this week's explainer", "this week's\nexplainer"), L(44, 40))
        title = T(L("How Google Docs Lets\nTwo People Type in\nthe Same Sentence",
                    "How Google\nDocs Lets Two\nPeople Type in\nthe Same\nSentence"), L(64, 44), line_spacing=0.9)
        uline = Line(LEFT * L(3.6, 1.3), RIGHT * L(3.6, 1.3), stroke_color=CRIMSON, stroke_width=9)
        p1 = column([lab, title, uline], 0.4, 0.4)
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.2, FadeIn(p1, shift=UP * 0.1), rt=0.4)
        self.go(5.1, *self.out(st), rt=0.25)
        # 2. a generic shared document, used every day (5.4)
        sd = shared_doc(L(5.4, 3.3), L(4.2, 2.7))
        l1 = T(L("shared documents", "shared\ndocuments"), L(54, 44), line_spacing=0.9)
        days = VGroup(*[RoundedRectangle(corner_radius=0.06, width=L(0.5, 0.36), height=L(0.7, 0.6), stroke_width=0,
                                         fill_color=TEAL, fill_opacity=1) for _ in range(7)]).arrange(RIGHT, buff=L(0.1, 0.07))
        l2 = T("every day", L(54, 44))
        right = VGroup(l1, VGroup(days, l2).arrange(DOWN, buff=0.3)).arrange(DOWN, buff=L(0.7, 0.5))
        s2 = place([sd, right], L(0.9, 0.5))
        self.go(5.4, FadeIn(sd, shift=UP * 0.1), rt=0.4)
        self.go(5.7, FadeIn(l1), rt=0.35)
        self.go(6.5, FadeIn(days, lag_ratio=0.08), FadeIn(l2), rt=0.55)
        # 3. never looked at what is behind them (7.9)
        bw, bh = L(3.4, 2.6), L(2.6, 0.95)
        bk = backend(bw, bh, L(44, 40))
        q = pchip(L("what happens behind?", "what's behind?"), CRIMSON, L(48, 34), fw=L(None, 2.9))
        s3 = column([bk, q], L(0.6, 0.4))
        self.go(7.9, *self.out(st), FadeIn(bk, shift=UP * 0.1), rt=0.5)
        self.go(8.6, FadeIn(q), rt=0.3)
        # 4. understanding the backend was the most interesting part (10.9)
        q2 = pchip("the backend", TEAL, L(48, 40), fw=L(None, 2.9)).move_to(q)
        q3 = pchip(L("the most interesting part", "the most\ninteresting part"), TEAL, L(48, 38), fw=L(None, 2.9)).move_to(q)
        sr = star(L(0.5, 0.4)).move_to(bk[2][0].get_corner(UR))
        self.go(10.9, FadeOut(q), FadeIn(q2), rt=0.3)
        self.go(12.8, FadeOut(q2), FadeIn(q3), FadeIn(sr), rt=0.4)
        self.finish()


@timed("B02")
class B02_FilmAsCode(Scene):
    def construct(self):
        st = STAGE("film as code")
        # 1. learning film as code, one part at a time (0 - 4.3)
        cm = code_mark(L(1.3, 0.8))
        ar = Arrow(LEFT * 0.4, RIGHT * 0.4, buff=0, color=INK, stroke_width=6) if not PORTRAIT \
            else Arrow(UP * 0.3, DOWN * 0.3, buff=0, color=INK, stroke_width=6)
        ff = film_frame(L(3.2, 1.3), L(2.3, 0.95))
        pair = VGroup(cm, ar, ff).arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.6, 0.35))
        t1 = T(L("learning film as code", "learning\nfilm as code"), L(56, 46), line_spacing=0.9)
        bl = slot_row(4, L(0.9, 0.62), L(0.5, 0.5), 3, L(0.15, 0.1))
        t2 = T(L("one part at a time", "one part\nat a time"), L(46, 38), line_spacing=0.9)
        s1 = column([pair, t1, bl, t2], L(0.45, 0.3), 0.3)
        fill_ = [b.copy().set_fill(TEAL, 1).set_stroke(TEAL, 4) for b in bl[:3]]
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.2, FadeIn(pair, shift=UP * 0.1), rt=0.4)
        self.go(0.9, FadeIn(t1), rt=0.35)
        self.go(1.9, FadeIn(bl), rt=0.3)
        self.go(2.58, FadeIn(t2), FadeIn(fill_[0]), rt=0.25)
        self.go(3.0, FadeIn(fill_[1]), rt=0.25)
        self.go(3.36, FadeIn(fill_[2]), rt=0.25)
        # 2. the first few days: going through Brutalist videos (4.3)
        cols, rows_ = L(3, 2), L(2, 3)
        grid = VGroup(*[player(L(3.3, 1.6), L(2.0, 1.2)) for _ in range(cols * rows_)])
        grid.arrange_in_grid(rows=rows_, cols=cols, buff=L(0.35, 0.22))
        wk = VGroup(*[RoundedRectangle(corner_radius=0.06, width=L(0.6, 0.4), height=L(0.5, 0.45), stroke_color=BORDER,
                                       stroke_width=4, fill_color=TEAL if i < 3 else PAPER, fill_opacity=1)
                      for i in range(7)]).arrange(RIGHT, buff=L(0.12, 0.08))
        c1 = T("the first few days", L(48, 40))
        c2 = T(L("going through Brutalist videos", "going through\nBrutalist videos"), L(48, 36), line_spacing=0.9)
        cap2 = VGroup(wk, c1).arrange(DOWN, buff=0.25)
        s2 = column([grid, cap2], L(0.4, 0.3), 0.2)
        c2.move_to(c1)
        self.go(4.3, *self.out(st), FadeIn(grid, lag_ratio=0.08), rt=0.5)
        self.go(5.0, FadeIn(wk), FadeIn(c1), rt=0.4)
        self.go(6.6, FadeOut(c1), FadeIn(c2), rt=0.3)
        # 3. understanding how each piece fits together (8.4)
        names = ["script", "audio", "scenes", "video"]
        cw, ch = L(2.5, 3.0), L(2.8, 0.78)
        pcs = VGroup(*[VGroup(card(cw, ch, TEAL if n == "video" else INK, PAPER, 5, 0.14)) for n in names])
        for p_, n in zip(pcs, names):
            p_.add(T(n, L(44, 44)).move_to(p_[0]))
        arrs = VGroup(*[Arrow(LEFT * 0.3, RIGHT * 0.3, buff=0, color=INK, stroke_width=6) if not PORTRAIT
                        else Arrow(UP * 0.1, DOWN * 0.1, buff=0, color=INK, stroke_width=6) for _ in range(3)])
        chain = VGroup(pcs[0], arrs[0], pcs[1], arrs[1], pcs[2], arrs[2], pcs[3]).arrange(
            RIGHT if not PORTRAIT else DOWN, buff=L(0.2, 0.07))
        cap3 = T(L("how each piece fits together", "how each piece\nfits together"), L(50, 38), line_spacing=0.9)
        s3 = column([chain, cap3], L(0.6, 0.25), 0.2)
        self.go(8.4, *self.out(st), FadeIn(pcs, lag_ratio=0.12), rt=0.6)
        self.go(9.5, FadeIn(cap3), rt=0.35)
        self.go(10.4, FadeIn(arrs, lag_ratio=0.2), rt=0.5)
        self.finish()


@timed("B03")
class B03_ChoosingTopics(Scene):
    def construct(self):
        st = STAGE("topics")
        # 1. researching topics: understanding some, discarding others (0 - 5.7)
        cols, rows_ = L(3, 2), L(2, 3)
        tcs = VGroup(*[topic_card(L(2.7, 1.7), L(2.2, 1.1)) for _ in range(6)])
        tcs.arrange_in_grid(rows=rows_, cols=cols, buff=L(0.4, 0.3))
        t1 = T("researching topics", L(52, 36))
        chip_k = pchip("understood some", TEAL, L(46, 38), fw=L(None, 2.9))
        chip_d = pchip("discarded others", CRIMSON, L(46, 38), fw=L(None, 2.9))
        s1 = column([tcs, t1], L(0.4, 0.25), 0.2)
        chip_k.move_to(t1)
        chip_d.move_to(t1)
        kept, gone = [0, 1, 3], [2, 4, 5]
        tks = VGroup(*[tick(0.3, TEAL, 9).move_to(tcs[i][0].get_corner(UR) + np.array([-0.45, -0.45, 0])) for i in kept])
        xs = VGroup(*[cross(0.25, CRIMSON, 9).move_to(tcs[i][0].get_corner(UR) + np.array([-0.45, -0.45, 0])) for i in gone])
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.2, FadeIn(tcs, lag_ratio=0.1), rt=0.5)
        self.go(1.0, FadeIn(t1), rt=0.35)
        self.go(2.68, FadeOut(t1), FadeIn(chip_k), LaggedStart(*[Create(t) for t in tks], lag_ratio=0.3), rt=0.8)
        self.go(4.2, FadeOut(chip_k), FadeIn(chip_d), LaggedStart(*[Create(x) for x in xs], lag_ratio=0.3), rt=0.8)
        # 2. what other fellows have already made (5.8)
        grid = VGroup(*[player(L(3.3, 1.6), L(2.1, 1.2)) for _ in range(6)])
        grid.arrange_in_grid(rows=rows_, cols=cols, buff=L(0.35, 0.22))
        c2 = T(L("what other fellows have made", "what other fellows\nhave already made"), L(48, 36), line_spacing=0.9)
        s2 = column([grid, c2], L(0.45, 0.3), 0.2)
        self.go(5.8, *self.out(st), FadeIn(grid, lag_ratio=0.08), rt=0.5)
        self.go(6.3, FadeIn(c2), rt=0.4)
        # 3. a topic where AI or STEM meets my own interests (8.3)
        r = L(2.4, 1.05)
        ca = Circle(radius=r, stroke_color=SLATE, stroke_width=6, fill_color=SLATE, fill_opacity=0.07)
        cb = Circle(radius=r, stroke_color=CRIMSON, stroke_width=6, fill_color=CRIMSON, fill_opacity=0.07)
        off = L(1.6, 0.7)
        ca.move_to(LEFT * off if not PORTRAIT else UP * off)
        cb.move_to(RIGHT * off if not PORTRAIT else DOWN * off)
        ta = T(L("AI or STEM", "AI or\nSTEM"), L(44, 36), line_spacing=0.9)
        tb = T(L("my interests", "my\ninterests"), L(44, 36), line_spacing=0.9)
        ta.move_to(ca.get_center() + (LEFT * 0.85 if not PORTRAIT else UP * 0.4))
        tb.move_to(cb.get_center() + (RIGHT * 0.85 if not PORTRAIT else DOWN * 0.4))
        vn = VGroup(ca, cb, ta, tb)
        sr = star(L(0.5, 0.42)).move_to(ORIGIN)
        c3 = T(L("a topic that connects them", "a topic that\nconnects them"), L(48, 40), line_spacing=0.9)
        s3 = column([vn, c3], L(0.5, 0.3), 0.2)
        sr.move_to(VGroup(ca, cb).get_center())
        self.go(8.3, *self.out(st), FadeIn(VGroup(ca, cb), shift=UP * 0.1), rt=0.5)
        self.go(8.9, FadeIn(ta), FadeIn(tb), rt=0.35)
        self.go(9.62, FadeIn(c3), rt=0.4)
        self.go(11.5, FadeIn(sr, scale=0.5), rt=0.4)
        self.finish()


@timed("B04")
class B04_ScriptAndChecks(Scene):
    def construct(self):
        st = STAGE("script")
        # 1. the script holds my words, beat by beat, with the sources behind them (0 - 7.9)
        cw = L(8.0, 2.7)
        rows = []
        for i in range(4):
            bar = RoundedRectangle(corner_radius=0.06, width=cw * L(0.5, 0.4), height=L(0.16, 0.22), stroke_width=0,
                                   fill_color=LINE, fill_opacity=1)
            num = T(str(i + 1), L(40, 34))
            slot = RoundedRectangle(corner_radius=0.12, width=L(1.7, 1.4), height=L(0.8, 0.5), stroke_color=BORDER,
                                    stroke_width=3, fill_color=PAPER, fill_opacity=1)
            rows.append(VGroup(num, bar, slot).arrange(RIGHT, buff=L(0.35, 0.2)))
        rows_g = VGroup(*rows).arrange(DOWN, buff=L(0.65, 0.22), aligned_edge=LEFT)
        sc = card(cw + 0.8, rows_g.height + 0.6, INK, PAPER, 4)
        rows_g.move_to(sc)
        script = VGroup(sc, rows_g)
        cap_a = T("the script", L(54, 44))
        cap_b = T(L("my words, beat by beat", "my words,\nbeat by beat"), L(54, 38), line_spacing=0.9).move_to(cap_a)
        cap_c = T(L("with the sources behind them", "with the sources\nbehind them"), L(50, 36), line_spacing=0.9).move_to(cap_a)
        s1 = column([script, cap_a], L(0.45, 0.3), 0.2)
        for c_ in (cap_b, cap_c):
            c_.move_to(cap_a)
        inks = [r[1].copy().set_fill(INK, 1) for r in rows]
        tags = VGroup(*[T("source", L(32, 31), SOFT).move_to(r[2]) for r in rows])
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.2, FadeIn(script, shift=UP * 0.1), rt=0.4)
        self.go(0.7, FadeIn(cap_a), rt=0.3)
        self.go(3.58, FadeOut(cap_a), FadeIn(cap_b), rt=0.3)
        self.go(4.22, *[FadeIn(k) for k in inks[:2]], rt=0.3)
        self.go(5.4, *[FadeIn(k) for k in inks[2:]], rt=0.3)
        self.go(6.2, FadeOut(cap_b), FadeIn(cap_c), FadeIn(tags, lag_ratio=0.2), rt=0.5)
        # 2. every claim is checked against a source (8.0)
        cw2, ch2 = L(4.2, 1.35), L(1.5, 1.15)
        pr = []
        for _ in range(3):
            cl = VGroup(card(cw2, ch2, INK, PAPER, 4, 0.12))
            cl.add(T("claim", L(40, 36)).move_to(cl[0]))
            so = VGroup(card(cw2, ch2, TEAL, PAPER, 5, 0.12))
            so.add(T("source", L(40, 36)).move_to(so[0]))
            ar = Arrow(LEFT * 0.3, RIGHT * 0.3, buff=0, color=INK, stroke_width=6)
            pr.append(VGroup(cl, ar, so).arrange(RIGHT, buff=L(0.35, 0.22)))
        prs = VGroup(*pr).arrange(DOWN, buff=L(0.5, 0.35))
        head = T("fact checks", L(56, 48))
        gate = pchip("quality gates", TEAL, L(50, 40))
        s2 = column([head, prs, gate], L(0.4, 0.35), 0.2)
        tks = VGroup(*[tick(0.28, TEAL, 10).move_to(p_[1]) for p_ in pr])
        self.go(8.0, *self.out(st), FadeIn(VGroup(head, prs), shift=UP * 0.1), rt=0.5)
        self.go(10.4, FadeOut(pr[0][1]), Create(tks[0]), rt=0.3)
        self.go(11.1, FadeOut(pr[1][1]), Create(tks[1]), rt=0.3)
        self.go(11.8, FadeOut(pr[2][1]), Create(tks[2]), rt=0.3)
        self.go(12.64, FadeIn(gate), rt=0.4)
        self.finish()


@timed("B05")
class B05_BehindTheTool(Scene):
    def construct(self):
        st = STAGE("behind")
        # 1. understanding the topic was not hard: a tool I already use (0 - 6.6)
        sd = shared_doc(L(4.6, 3.2), L(3.4, 2.3))
        pa = VGroup(Dot(radius=0.12, color=INK), Line(LEFT * L(1.6, 0.9), RIGHT * L(1.6, 0.9), stroke_color=TEAL, stroke_width=9),
                    tick(0.35, TEAL, 10)).arrange(RIGHT, buff=0.12)
        a1 = T(L("understanding the topic", "understanding\nthe topic"), L(54, 40), line_spacing=0.9)
        a2 = T(L("a tool I already use", "a tool I\nalready use"), L(54, 44), line_spacing=0.9).move_to(a1)
        left_ = VGroup(sd, pa).arrange(DOWN, buff=0.45)
        s1 = column([left_, a1], L(0.6, 0.4), 0.2)
        a2.move_to(a1)
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.2, FadeIn(sd, shift=UP * 0.1), rt=0.4)
        self.go(0.4, FadeIn(pa), FadeIn(a1), rt=0.5)
        self.go(4.6, FadeOut(a1), FadeIn(a2), rt=0.3)
        # 2. underneath: shifted, ordered, shared (6.2)
        top = shared_doc(L(3.0, 1.3), L(1.9, 1.15), cursors=False)
        uh = T("underneath", L(54, 36))

        def shift_icon():
            return VGroup(Rectangle(width=0.7, height=0.14, stroke_width=0, fill_color=LINE, fill_opacity=1),
                          Rectangle(width=0.7, height=0.14, stroke_width=0, fill_color=TEAL, fill_opacity=1).shift(DOWN * 0.26 + RIGHT * 0.22))

        def order_icon():
            return VGroup(*[Rectangle(width=0.2, height=0.16 + 0.16 * i, stroke_width=0, fill_color=TEAL, fill_opacity=1)
                            for i in range(3)]).arrange(RIGHT, buff=0.06, aligned_edge=DOWN)

        def share_icon():
            return VGroup(Dot(radius=0.1, color=TEAL).shift(LEFT * 0.3), Dot(radius=0.1, color=TEAL).shift(RIGHT * 0.3 + UP * 0.22),
                          Dot(radius=0.1, color=TEAL).shift(RIGHT * 0.3 + DOWN * 0.22),
                          Line(LEFT * 0.3, RIGHT * 0.3 + UP * 0.22, stroke_color=TEAL, stroke_width=4),
                          Line(LEFT * 0.3, RIGHT * 0.3 + DOWN * 0.22, stroke_color=TEAL, stroke_width=4))
        cwid = L(3.7, 3.4)
        steps = VGroup(*[icon_row(ic, lb, cwid, L(2.3, 1.15), L(46, 38)) for ic, lb in
                         ((shift_icon(), "shifted"), (order_icon(), "ordered"), (share_icon(), "shared"))])
        steps.arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.3, 0.2))
        s2 = column([VGroup(top, uh).arrange(RIGHT, buff=0.4), steps], L(0.6, 0.35), 0.2)
        self.go(6.2, *self.out(st), FadeIn(top, shift=UP * 0.1), FadeIn(uh), rt=0.5)
        self.go(6.5, FadeIn(VGroup(*[s_[0] for s_ in steps]), lag_ratio=0.1), rt=0.4)
        self.go(9.78, FadeIn(VGroup(steps[0][1], steps[0][2])), rt=0.25)
        self.go(10.62, FadeIn(VGroup(steps[1][1], steps[1][2])), rt=0.25)
        self.go(11.14, FadeIn(VGroup(steps[2][1], steps[2][2])), rt=0.25)
        # 3. a familiar tool feels new (11.9)
        sd2 = shared_doc(L(5.8, 3.4), L(3.9, 3.3))
        nw = pchip("feels new", TEAL, L(60, 44))
        s3 = column([sd2, nw], L(0.6, 0.4), 0.2)
        sr = star(L(0.55, 0.45)).move_to(sd2[0].get_corner(UR) + np.array([-0.4, -0.4, 0]))
        self.go(11.9, *self.out(st), FadeIn(sd2, shift=UP * 0.1), rt=0.4)
        self.go(12.9, FadeIn(nw), FadeIn(sr, scale=0.5), rt=0.4)
        self.finish()


@timed("B06")
class B06_Takeaway(Scene):
    def construct(self):
        st = STAGE("look behind")
        icons = [shared_doc(1.5, 1.0), phone(0.6, 1.0), clock(0.42)]
        fronts, backs = [], []
        for ic in icons:
            fc = card(L(3.4, 1.75), L(3.0, 1.15), INK, PAPER, 4, 0.14)
            ic = ic.copy()
            fit(ic, fc.width - 0.6, fc.height - 0.35)
            ic.move_to(fc)
            fronts.append(VGroup(fc, ic))
            bc = card(L(3.4, 1.75), L(2.2, 1.15), TEAL, PAPER, 5, 0.14)
            ni = nodes_icon(L(1.8, 1.4), L(1.0, 0.8))
            ni.move_to(bc)
            backs.append(VGroup(bc, ni))
        items = VGroup(*[VGroup(b, f).arrange(DOWN if not PORTRAIT else RIGHT, buff=L(0.2, 0.15)) for b, f in zip(backs, fronts)])
        items.arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.5, 0.22))
        h1 = T(L("the tools I use every day", "the tools I use\nevery day"), L(54, 38), line_spacing=0.9)
        h2 = T(L("hide interesting engineering", "hide interesting\nengineering"), L(54, 38), line_spacing=0.9)
        h3 = T(L("learn to look behind them", "learn to look\nbehind them"), L(54, 38), line_spacing=0.9)
        s = column([items, h1], L(0.5, 0.35), 0.2)
        h2.move_to(h1)
        h3.move_to(h1)
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.1, FadeIn(VGroup(*[f for f in fronts]), shift=UP * 0.1), FadeIn(h1), rt=0.4)
        self.go(1.5, FadeIn(VGroup(*[b for b in backs])), rt=0.5)
        self.go(2.2, FadeOut(h1), FadeIn(h2), rt=0.3)
        self.go(4.42, FadeOut(h2), FadeIn(h3), rt=0.3)
        self.finish()
