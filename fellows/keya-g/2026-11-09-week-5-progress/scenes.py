"""Manim scenes for "Week 5 Progress" (Keya G.).

One scene per Manim beat in beat_sheet.json:
B01_ThisWeeksVideo     the explainer's title, a year of learning Japanese, and the five things researched
B02_TheNumber          a summary's 12%, the table behind it, "mixed" against the older method, the number out,
                       then: check what a number is compared against
B03_LandscapeVertical  a landscape and a vertical frame, the same narration, a squeezed layout that fails,
                       a vertical layout designed on its own
B04_Measure            ask for measurements; a wrong figure; measure the real frames; every scene's text above the 72 px rule
B05_EarAndEye          three words picked by ear from test clips; typing and voice out of sync, then in sync
B06_Watching           watching Brutalist videos, other fellows' topics, a topic of my own
B07_Takeaway           a number needs its comparison, a vertical video its own layout, a claim a measurement

Simple drawn shapes only, in the same style as the Week 2 progress video: no photos, no person icons, no company
or tool logos. No Duolingo logo, owl or branding: the app is only ever a generic drawn phone with plain text.
Any file, terminal, frame or ruler shown is drawn, not a screenshot.
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
PORTRAIT = False

# Portrait sync: Manim CE takes pixel dims from -r W,H but leaves frame_width at the 16:9 default.
if PORTRAIT:
    try:
        _pw, _ph = config.pixel_width, config.pixel_height
        if _pw and _ph and abs(config.frame_width - config.frame_height * _pw / _ph) > 0.01:
            config.frame_width = config.frame_height * (_pw / _ph)
    except Exception:
        pass

DUR = {"B01": 17.56, "B02": 19.99, "B03": 16.43, "B04": 13.4, "B05": 13.87, "B06": 7.68, "B07": 8.34}
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
@timed("B01")
class B01_ThisWeeksVideo(Scene):
    def construct(self):
        st = STAGE("this week")
        # 1. the explainer's title, text only (0 - 4.3)
        lab = T(L("this week's explainer", "this week's\nexplainer"), L(44, 40))
        title = T(L("How Duolingo Decides\nWhat You Practice Next", "How Duolingo\nDecides What\nYou Practice\nNext"),
                  L(70, 46), line_spacing=0.9)
        uline = Line(LEFT * L(3.6, 1.3), RIGHT * L(3.6, 1.3), stroke_color=CRIMSON, stroke_width=9)
        p1 = VGroup(lab, title, uline).arrange(DOWN, buff=0.4)
        fitfill(p1, RW - 0.4, RH - 0.2)
        p1.move_to([0, RCY, 0])
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.2, FadeIn(p1, shift=UP * 0.1), rt=0.4)
        self.go(4.2, FadeOut(p1), rt=0.25)
        # 2. over a year of Japanese, a generic phone and a year bar (4.5)
        ph = phone(L(2.2, 2.0), L(3.4, 3.1))
        pl = lines_block(3, ph[0].width - 0.7, h=0.16, gap=0.3).move_to(ph[0].get_center() + DOWN * 0.15)
        phg = VGroup(ph, pl)
        l1 = T(L("learning Japanese", "learning\nJapanese"), L(50, 44), line_spacing=0.9)
        yb = VGroup(*[RoundedRectangle(corner_radius=0.05, width=L(0.36, 0.2), height=L(0.7, 0.7), stroke_width=0,
                                       fill_color=TEAL, fill_opacity=1) for _ in range(12)]).arrange(RIGHT, buff=L(0.08, 0.05))
        l2 = T("for over a year", L(50, 44))
        right = VGroup(l1, VGroup(yb, l2).arrange(DOWN, buff=0.3)).arrange(DOWN, buff=L(0.7, 0.5))
        fit(right, L(7.0, RW - 0.4))
        yr = lay([phg, right], buff=L(0.9, 0.6))
        self.go(4.5, FadeIn(phg, shift=UP * 0.1), FadeIn(l1), rt=0.4)
        self.go(6.5, FadeIn(yb, lag_ratio=0.1), FadeIn(l2), rt=0.8)
        self.go(7.8, FadeOut(yr), rt=0.2)
        # 3. what I researched: five cards (8.06)
        rw = L(5.6, RW - 0.4)
        rh_ = L(0.78, 0.98)
        rows = VGroup(icon_row(curve_icon(), L("forgetting curve", "forgetting\ncurve"), rw, rh_, L(40, 35)),
                      icon_row(loop_icon(), L("spaced repetition", "spaced\nrepetition"), rw, rh_, L(40, 35)),
                      icon_row(boxes_icon(), L("Leitner boxes", "Leitner\nboxes"), rw, rh_, L(40, 35)),
                      icon_row(doc(0.6, 0.7, 2), "blog posts", rw, rh_, L(40, 35)),
                      icon_row(doc(0.6, 0.7, 3, TEAL), L("the research paper", "research\npaper"), rw, rh_, L(40, 35)))
        rows.arrange(DOWN, buff=L(0.22, 0.06))
        head = T("I researched", L(54, 40))
        res = VGroup(head, rows).arrange(DOWN, buff=L(0.35, 0.22))
        fitfill(res, RW - 0.2, RH - 0.1)
        res.move_to([0, RCY, 0])
        self.go(8.0, FadeIn(head), rt=0.3)
        self.go(8.7, FadeIn(rows[0], shift=UP * 0.1), rt=0.35)
        self.go(9.92, FadeIn(rows[1], shift=UP * 0.1), rt=0.35)
        self.go(11.56, FadeIn(rows[2], shift=UP * 0.1), rt=0.35)
        self.go(13.5, FadeIn(rows[3], shift=UP * 0.1), rt=0.35)
        self.go(15.42, FadeIn(rows[4], shift=UP * 0.1), rt=0.35)
        self.finish()


@timed("B02")
class B02_TheNumber(Scene):
    def construct(self):
        st = STAGE("the paper")
        # 1. a summary says 12% (0 - 6.8)
        sm = doc(L(3.6, 3.0), L(3.0, 2.2), 3)
        smt = T("a summary", L(46, 44))
        pct = T("12%", L(110, 84), CRIMSON)
        pcl = T("better engagement", L(46, 44))
        sg = VGroup(sm, smt).arrange(DOWN, buff=0.3)
        pg = VGroup(pct, pcl).arrange(DOWN, buff=0.2)
        s1 = lay([sg, pg], buff=L(1.2, 0.5))
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.4, FadeIn(sg, shift=UP * 0.1), rt=0.4)
        self.go(3.1, FadeIn(pg[1]), rt=0.3)
        self.go(5.55, FadeIn(pg[0], shift=UP * 0.1), rt=0.35)
        self.go(6.7, FadeOut(s1), rt=0.15)
        # 2. the table: that 12% compares two versions of the same model (6.92)
        a = card(L(2.6, 3.0), L(1.1, 1.0), INK, PAPER, 4)
        at = T("model\nversion 1", L(38, 36), line_spacing=0.9).move_to(a)
        b = card(L(2.6, 3.0), L(1.1, 1.0), INK, PAPER, 4)
        bt = T("model\nversion 2", L(38, 36), line_spacing=0.9).move_to(b)
        A, B = VGroup(a, at), VGroup(b, bt)
        link = VGroup(Arrow(LEFT * 0.5, RIGHT * 0.5, buff=0, color=INK, stroke_width=6) if not PORTRAIT
                      else Arrow(UP * 0.4, DOWN * 0.4, buff=0, color=INK, stroke_width=6),
                      T("12%", L(56, 56), CRIMSON)).arrange(DOWN if not PORTRAIT else RIGHT, buff=0.2)
        tbl_l = T("the results table", L(46, 38))
        grid = VGroup(A, link, B).arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.5, 0.25))
        same = pchip("same model", TEAL, L(44, 38))
        s2 = VGroup(tbl_l, grid, same).arrange(DOWN, buff=L(0.5, 0.3))
        fitfill(s2, RW - 0.4, RH - 0.1)
        s2.move_to([0, RCY, 0])
        self.go(6.85, FadeIn(tbl_l), rt=0.3)
        self.go(8.9, FadeIn(grid, lag_ratio=0.2), rt=0.6)
        self.go(10.7, FadeIn(same), rt=0.3)
        self.go(11.55, FadeOut(s2), rt=0.2)
        # 3. against the older method: mixed (11.8)
        old = card(L(2.6, 3.0), L(1.1, 1.2), LINE, PAPER, 5)
        olt = T("older\nmethod", L(40, 40), line_spacing=0.9).move_to(old)
        new = card(L(2.6, 3.0), L(1.1, 1.2), INK, PAPER, 4)
        nwt = T("the\nmodel", L(40, 40), line_spacing=0.9).move_to(new)
        up = Arrow(DOWN * 0.4, UP * 0.4, buff=0, color=TEAL, stroke_width=8)
        dn = Arrow(UP * 0.4, DOWN * 0.4, buff=0, color=CRIMSON, stroke_width=8)
        mixed = VGroup(up, dn).arrange(RIGHT, buff=0.4)
        mt = T("mixed", L(70, 76))
        mg = VGroup(mixed, mt).arrange(DOWN, buff=0.3)
        pair = VGroup(VGroup(old, olt), VGroup(new, nwt)).arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.7, 0.35))
        s3 = VGroup(pair, mg).arrange(DOWN, buff=L(0.7, 0.45))
        fitfill(s3, RW - 0.4, RH - 0.1)
        s3.move_to([0, RCY, 0])
        self.go(11.8, FadeIn(pair, lag_ratio=0.2), rt=0.4)
        self.go(13.5, FadeIn(mg, shift=UP * 0.1), rt=0.4)
        self.go(14.45, FadeOut(s3), rt=0.2)
        # 4. the number comes out (14.74)
        big = T("12%", L(120, 80), CRIMSON)
        xx = cross(L(0.7, 0.45), CRIMSON, 12)
        out_t = T("taken out", L(60, 60))
        s4 = VGroup(VGroup(big, xx).arrange(RIGHT, buff=0.5), out_t).arrange(DOWN, buff=0.5)
        s4.move_to([0, RCY, 0])
        self.go(14.74, FadeIn(big), rt=0.2)
        self.go(15.3, Create(xx), FadeIn(out_t), rt=0.4)
        self.go(16.2, FadeOut(s4), rt=0.2)
        # 5. now I check what a number is compared against (16.38)
        n_ = card(L(2.6, 3.0), L(1.0, 0.85), INK, PAPER, 4)
        n_t = T("a number", L(42, 36)).move_to(n_)
        c_ = card(L(2.6, 3.0), L(1.0, 0.85), TEAL, PAPER, 5)
        c_t = T("its comparison", L(40, 34)).move_to(c_)
        fit(c_t, c_.width - 0.2)
        ar = DoubleArrow(LEFT * 0.5, RIGHT * 0.5, buff=0, color=INK, stroke_width=6) if not PORTRAIT \
            else DoubleArrow(UP * 0.35, DOWN * 0.35, buff=0, color=INK, stroke_width=6)
        ey = eye(L(1.0, 0.9))
        pr = VGroup(VGroup(n_, n_t), ar, VGroup(c_, c_t)).arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.35, 0.2))
        ck = T(L("check what it is compared against", "check what it is\ncompared against"), L(48, 34), line_spacing=0.9)
        hl = T(L("not just the headline", "not just\nthe headline"), L(46, 34), SOFT, line_spacing=0.9)
        s5 = VGroup(*([ey] if not PORTRAIT else []), pr, ck, hl).arrange(DOWN, buff=L(0.4, 0.25))
        fitfill(s5, RW - 0.3, RH - 0.1)
        s5.move_to([0, RCY, 0])
        self.go(16.38, FadeIn(VGroup(*([ey] if not PORTRAIT else []), pr), shift=UP * 0.1), rt=0.4)
        self.go(17.4, FadeIn(ck), rt=0.4)
        self.go(18.85, FadeIn(hl), rt=0.4)
        self.finish()


@timed("B03")
class B03_LandscapeVertical(Scene):
    def construct(self):
        st = STAGE("two shapes")
        # 1. a landscape frame and a vertical frame (0 - 4.1)
        lw, lh = L(3.6, 3.2), L(2.0, 1.8)
        vw, vh = L(1.7, 1.9), L(3.0, 2.7)
        land = VGroup(card(lw, lh, INK, PAPER, 5, 0.12), T("landscape", L(44, 44)))
        land[1].move_to(land[0])
        vert = VGroup(card(vw, vh, TEAL, PAPER, 5, 0.12), T("vertical", L(44, 44)))
        vert[1].move_to(vert[0])
        fit(vert[1], vw - 0.15)
        fr = VGroup(land, vert).arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.9, 0.5))
        s1 = lay([fr], buff=0.2, h=RH - 0.3)
        s1.move_to([0, RCY, 0])
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.4, FadeIn(land, shift=UP * 0.1), rt=0.4)
        self.go(1.7, FadeIn(vert, shift=UP * 0.1), rt=0.4)
        # 2. the narration is the same (4.16)
        wv = wave(L(24, 14), L(6.0, 3.1), L(1.4, 2.4), TEAL)
        wl = T("the narration is the same", L(54, 44) if not PORTRAIT else 44)
        if PORTRAIT:
            wl = T("the narration\nis the same", 48, line_spacing=0.9)
        s2 = VGroup(wv, wl).arrange(DOWN, buff=0.5)
        s2.move_to([0, RCY, 0])
        self.go(4.1, FadeOut(s1), FadeIn(wv, lag_ratio=0.03), rt=0.5)
        self.go(4.9, FadeIn(wl), rt=0.3)
        # 3. a squeezed landscape layout does not work on a phone (5.84)
        ph = phone(L(2.4, 1.9), L(4.2, 3.0))
        ph_c = ph[0].get_center()
        sq = card(ph[0].width - 0.3, 0.9, LINE, PAPER, 3, 0.06).move_to(ph_c)
        sql = lines_block(2, sq.width - 0.3, h=0.07, gap=0.1).move_to(sq)
        sq_g = VGroup(sq, sql)
        x = cross(L(0.6, 0.55), CRIMSON, 12).move_to(ph_c + UP * 0.9)
        sqt = T(L("squeezed\nlandscape", "squeezed\nlandscape"), L(52, 46), line_spacing=0.9)
        bad = VGroup(VGroup(ph, sq_g, x), sqt)
        bad.arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.9, 0.4))
        fitfill(bad, RW - 0.4, RH - 0.1)
        bad.move_to([0, RCY, 0])
        self.go(5.7, FadeOut(s2), FadeIn(VGroup(ph)), rt=0.3)
        self.go(6.2, FadeIn(sq_g, shift=UP * 0.05), FadeIn(sqt), rt=0.4)
        self.go(8.1, Create(x), rt=0.3)
        # 4. each vertical scene needs its own design (9.54)
        ph2 = phone(L(3.2, 3.4), L(5.4, 5.0), TEAL)
        names = ["one idea\nat a time", "stacked top\nto bottom", "bigger text"]
        blocks = VGroup(*[VGroup(card(ph2[0].width - 0.5, L(1.35, 1.3), TEAL, CREAM, 4, 0.12),
                                  T(n, L(44, 44), line_spacing=0.9)) for n in names])
        for bl in blocks:
            bl[1].move_to(bl[0])
        blocks.arrange(DOWN, buff=0.22)
        blocks.move_to(ph2[0].get_center() + DOWN * 0.15)
        own = T("its own design", L(52, 48))
        rt_ = VGroup(ph2, blocks)
        s4 = VGroup(rt_, own).arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.9, 0.3))
        fitfill(s4, RW - 0.2, RH - 0.05)
        s4.move_to([0, RCY, 0])
        self.go(9.45, FadeOut(bad), FadeIn(ph2), FadeIn(own), FadeIn(VGroup(*[b[0] for b in blocks])), rt=0.4)
        self.go(12.3, FadeIn(blocks[0][1], shift=UP * 0.1), rt=0.35)
        self.go(13.85, FadeIn(blocks[1][1], shift=UP * 0.1), rt=0.35)
        self.go(15.4, FadeIn(blocks[2][1], shift=UP * 0.1), rt=0.35)
        self.finish()


@timed("B04")
class B04_Measure(Scene):
    def construct(self):
        st = STAGE("measuring")
        # 1. ask for measurements (0 - 2.9)
        rl = ruler(L(6.0, 3.0), INK, 11)
        t1 = T(L("ask for measurements", "ask for\nmeasurements"), L(60, 46), line_spacing=0.9)
        s1 = VGroup(rl, t1).arrange(DOWN, buff=0.6)
        s1.move_to([0, RCY, 0])
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.9, FadeIn(rl), rt=0.5)
        self.go(1.5, FadeIn(t1), rt=0.35)
        # 2. a wrong figure for the vertical text size (3.02)
        tw_, th_ = L(4.6, 3.3), L(3.5, 3.0)
        tc = card(tw_, th_, INK, PAPER, 4)
        td = VGroup(*[Dot(radius=0.06, color=col) for col in (CRIMSON, GOLD, TEAL)]).arrange(RIGHT, buff=0.12)
        td.move_to(tc.get_corner(UL) + np.array([0.45, -0.3, 0]))
        tm = VGroup(tc, td)
        fig = T("text size = ?", L(46, 38), INK)
        fig.move_to(tm.get_center() + DOWN * 0.15 + LEFT * L(0.3, 0.35))
        xx = cross(L(0.3, 0.25), CRIMSON, 10).move_to(tm.get_corner(DR) + np.array([-0.5, 0.55, 0]) + LEFT * L(0, 0.1))
        wl = T("a wrong figure", L(52, 48), CRIMSON)
        vl = T(L("for the vertical text size", "for the vertical\ntext size"), L(46, 42), line_spacing=0.9)
        s2 = VGroup(VGroup(tm, fig, xx), wl, vl).arrange(DOWN, buff=L(0.4, 0.3))
        fitfill(s2, RW - 0.3, RH - 0.1)
        s2.move_to([0, RCY, 0])
        self.go(2.9, FadeOut(s1), FadeIn(tm, shift=UP * 0.1), FadeIn(fig), rt=0.35)
        self.go(4.3, FadeIn(wl), Create(xx), rt=0.35)
        self.go(5.44, FadeIn(vl), rt=0.35)
        # 3. measure the real frames (7.22)
        fr = card(L(2.2, 2.3), L(3.8, 3.2), INK, PAPER, 5, 0.1)
        ln = Rectangle(width=fr.width - 0.6, height=0.4, stroke_width=0, fill_color=LINE, fill_opacity=1)
        ln.move_to(fr.get_center() + UP * 0.2)
        br = VGroup(Line(ln.get_corner(UR) + RIGHT * 0.25, ln.get_corner(DR) + RIGHT * 0.25, stroke_color=CRIMSON, stroke_width=8),
                    Line(ln.get_corner(UR) + RIGHT * 0.12, ln.get_corner(UR) + RIGHT * 0.38, stroke_color=CRIMSON, stroke_width=8),
                    Line(ln.get_corner(DR) + RIGHT * 0.12, ln.get_corner(DR) + RIGHT * 0.38, stroke_color=CRIMSON, stroke_width=8))
        rl2 = ruler(L(3.4, 1.6), INK, 6).rotate(PI / 2).next_to(fr, LEFT, buff=0.25)
        real = VGroup(fr, ln, br, rl2)
        m_t = T(L("measure the\nreal frames", "measure the\nreal frames"), L(54, 48), line_spacing=0.9)
        s3 = VGroup(real, m_t).arrange(RIGHT if not PORTRAIT else DOWN, buff=L(0.9, 0.4))
        fitfill(s3, RW - 0.4, RH - 0.1)
        s3.move_to([0, RCY, 0])
        self.go(6.9, FadeOut(s2), FadeIn(VGroup(fr, ln), shift=UP * 0.1), rt=0.35)
        self.go(7.7, FadeIn(m_t), rt=0.35)
        self.go(8.4, FadeIn(rl2), Create(br), rt=0.5)
        # 4. every scene's text sits above the 72 px rule (10.0)
        full = L(5.6, 3.0)
        lens = [0.96, 0.88, 1.0, 0.82, 0.92]
        bars = VGroup(*[RoundedRectangle(corner_radius=0.1, width=full * k, height=L(0.5, 0.74), stroke_width=0,
                                         fill_color=TEAL, fill_opacity=1) for k in lens])
        bars.arrange(DOWN, buff=L(0.2, 0.2), aligned_edge=LEFT)
        rule_x = bars.get_left()[0] + full * 0.72
        rule = DashedVMobject(Line([rule_x, bars.get_bottom()[1] - 0.25, 0], [rule_x, bars.get_top()[1] + 0.25, 0],
                                   stroke_color=CRIMSON, stroke_width=8), num_dashes=14)
        head = T(L("every scene's text", "every scene's\ntext"), L(60, 46), line_spacing=0.9)
        v72 = T("72 px rule", L(60, 52), CRIMSON)
        meter = VGroup(bars, rule)
        s4 = VGroup(head, meter, v72).arrange(DOWN, buff=L(0.45, 0.35))
        fitfill(s4, RW - 0.3, RH - 0.1)
        s4.move_to([0, RCY, 0])
        tk = tick(0.4, TEAL, 9).next_to(v72, RIGHT, buff=0.3)
        self.go(9.9, FadeOut(s3), FadeIn(head), rt=0.3)
        self.go(10.3, LaggedStart(*[FadeIn(b, shift=RIGHT * 0.3) for b in bars], lag_ratio=0.25), rt=0.9)
        self.go(11.66, FadeIn(rule), FadeIn(v72), rt=0.4)
        self.go(12.8, Create(tk), rt=0.3)
        self.finish()


@timed("B05")
class B05_EarAndEye(Scene):
    def construct(self):
        st = STAGE("listening")
        # 1. only a person catches (0 - 2.5)
        ey = eye(L(1.8, 1.3))
        t1 = T(L("some things only\na person catches", "some things\nonly a person\ncatches"), L(60, 44), line_spacing=0.9)
        s1 = VGroup(ey, t1).arrange(DOWN, buff=0.5)
        s1.move_to([0, RCY, 0])
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.4, FadeIn(ey), rt=0.3)
        self.go(0.9, FadeIn(t1), rt=0.4)
        # 2. three words picked by ear from test clips (2.64)
        cw = L(5.6, RW - 0.4)
        clips = VGroup()
        for word in ["shimasu", "mimasu", "Leitner"]:
            c = card(cw, L(1.5, 1.2), INK, PAPER, 4, 0.14)
            tri = Triangle(stroke_width=0, fill_color=TEAL, fill_opacity=1).scale(0.22).rotate(-PI / 2)
            tri.move_to(c.get_left() + RIGHT * 0.5)
            wv = wave(L(10, 5), L(1.6, 1.0), L(0.6, 0.6), LINE, seed=len(word))
            wv.move_to(c.get_right() + LEFT * (wv.width / 2 + 0.35))
            wt = T(word, L(54, 40))
            wt.move_to(c.get_center() + LEFT * L(0.3, 0.05))
            if PORTRAIT:
                wt.next_to(tri, RIGHT, buff=0.3).shift(UP * 0.26)
                wv.move_to(c.get_center() + DOWN * 0.28 + LEFT * 0.1)
            clips.add(VGroup(c, tri, wt, wv))
        clips.arrange(DOWN, buff=L(0.3, 0.2))
        ear = T(L("by ear, from test clips", "by ear, from\ntest clips"), L(50, 36), line_spacing=0.9)
        s2 = VGroup(clips, ear).arrange(DOWN, buff=L(0.45, 0.35))
        fitfill(s2, RW - 0.2, RH - 0.1)
        s2.move_to([0, RCY, 0])
        ticks = VGroup(*[bigtick().move_to(cl[0].get_corner(UR) + np.array([-0.45 if not PORTRAIT else -0.5, -0.45 if not PORTRAIT else -0.6, 0])) for cl in clips])
        self.go(2.5, FadeOut(s1), *[FadeIn(VGroup(cl[0], cl[1], cl[3]), shift=UP * 0.1) for cl in clips], rt=0.3)
        self.go(3.42, FadeIn(clips[0][2]), rt=0.2)
        self.go(4.44, FadeIn(clips[1][2]), rt=0.2)
        self.go(5.1, FadeIn(clips[2][2]), rt=0.2)
        self.go(5.55, FadeIn(ear), rt=0.3)
        self.go(6.7, LaggedStart(*[Create(t) for t in ticks], lag_ratio=0.3), rt=0.9)
        # 3. typing and voice out of sync, then fixed (7.94)
        tw = L(5.4, RW - 0.5)
        row_t = VGroup(card(tw, 0.9, INK, PAPER, 4, 0.12))
        keys = VGroup(*[RoundedRectangle(corner_radius=0.05, width=tw / 14, height=0.4, stroke_width=0,
                                         fill_color=INK, fill_opacity=1) for _ in range(8)]).arrange(RIGHT, buff=tw / 40)
        keys.move_to(row_t[0]).align_to(row_t[0], LEFT).shift(RIGHT * 0.25)
        lab_t = T("typing", L(44, 44))
        row_v = card(tw, 0.9, INK, PAPER, 4, 0.12)
        vw = wave(L(16, 10), tw * 0.5, 0.5, TEAL, seed=5)
        vw.move_to(row_v).align_to(row_v, LEFT).shift(RIGHT * 0.25)
        lab_v = T("voice", L(44, 44))
        shift = L(1.8, 1.0)
        vw.shift(RIGHT * shift)
        tr1 = VGroup(lab_t, VGroup(row_t, keys)).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        tr2 = VGroup(lab_v, VGroup(row_v, vw)).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        tracks = VGroup(tr1, tr2).arrange(DOWN, buff=L(0.7, 0.55))
        stat = pchip("out of sync", CRIMSON, L(54, 48))
        stat2 = pchip("in sync", TEAL, L(54, 48))
        s3 = VGroup(tracks, stat).arrange(DOWN, buff=L(0.7, 0.55))
        fitfill(s3, RW - 0.2, RH - 0.1)
        s3.move_to([0, RCY, 0])
        stat2.move_to(stat)
        self.go(7.7, FadeOut(s2), FadeOut(ticks), FadeIn(tracks, lag_ratio=0.3), rt=0.6)
        self.go(11.2, FadeIn(stat), rt=0.3)
        self.go(12.85, FadeOut(stat), FadeIn(stat2), vw.animate.shift(LEFT * shift), rt=0.7)
        self.finish()


@timed("B06")
class B06_Watching(Scene):
    def construct(self):
        st = STAGE("watching")
        cols, rows_ = L(3, 2), L(2, 3)
        cw, ch = L(3.3, 1.5), L(2.0, 1.45)
        grid = VGroup(*[player(cw, ch) for _ in range(cols * rows_)])
        grid.arrange_in_grid(rows=rows_, cols=cols, buff=L(0.35, 0.25))
        chip_w = T("watching Brutalist videos", L(48, 40))
        chip_o = T("other fellows' topics", L(48, 44), SLATE)
        chip_m = T("topics that are my own", L(48, 40), TEAL)
        if PORTRAIT:
            chip_w = T("watching\nBrutalist videos", 44, line_spacing=0.9)
            chip_o = T("what other\nfellows cover", 44, SLATE, line_spacing=0.9)
            chip_m = T("topics that\nare my own", 44, TEAL, line_spacing=0.9)
        s = VGroup(grid, chip_w).arrange(DOWN, buff=L(0.45, 0.3))
        fitfill(s, RW - 0.2, RH - 0.05)
        s.move_to([0, RCY, 0])
        for ch_ in (chip_o, chip_m):
            ch_.move_to(chip_w)
        mine = grid[L(4, 4)]
        glow = card(mine[0].width + 0.12, mine[0].height + 0.12, TEAL, PAPER, 9, 0.18).set_fill(opacity=0).move_to(mine[0])
        sr = star(L(0.42, 0.34)).move_to(mine[0].get_corner(UR) + np.array([-0.4, -0.4, 0]))
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.2, FadeIn(grid, lag_ratio=0.1), rt=0.4)
        self.go(0.66, FadeIn(chip_w), rt=0.35)
        self.go(2.94, FadeOut(chip_w), FadeIn(chip_o), rt=0.3)
        self.go(5.48, FadeOut(chip_o), FadeIn(chip_m), rt=0.3)
        self.go(6.9, Create(glow), FadeIn(sr), rt=0.4)
        self.finish()


@timed("B07")
class B07_Takeaway(Scene):
    def construct(self):
        st = STAGE("the details")
        head = T(L("this week, the details mattered", "the details\nmattered"), L(54, 36), line_spacing=0.9)
        cw = L(RW - 0.6, 3.4)
        ch = L(1.3, 1.25)

        def item(icon, text):
            c = card(cw, ch, INK, PAPER, 4, 0.14)
            ic = icon
            fit(ic, L(0.85, 0.5), ch - 0.25)
            ic.move_to(c.get_left() + RIGHT * L(0.65, 0.42))
            t = T(text, L(46, 32), line_spacing=0.9)
            t.next_to(ic, RIGHT, buff=L(0.3, 0.22))
            if PORTRAIT and t.get_right()[0] > c.get_right()[0] - 0.25:
                t.scale((c.get_right()[0] - 0.25 - t.get_left()[0]) / t.width)
            return VGroup(c, ic, t)

        pr = VGroup(*[RoundedRectangle(corner_radius=0.04, width=0.3, height=hh, stroke_width=0, fill_color=cc,
                                       fill_opacity=1) for hh, cc in ((0.9, CRIMSON), (0.55, TEAL))]).arrange(RIGHT, buff=0.12, aligned_edge=DOWN)
        i1 = item(pr, L("a number needs its comparison", "a number\nneeds its\ncomparison"))
        i2 = item(phone(0.5, 0.9), L("a vertical video needs its own layout", "a vertical\nvideo needs\nits own layout"))
        i3 = item(ruler(0.9, INK, 5), L("a claim needs a measurement", "a claim\nneeds a\nmeasurement"))
        items = VGroup(i1, i2, i3).arrange(DOWN, buff=L(0.3, 0.12))
        s = VGroup(head, items).arrange(DOWN, buff=L(0.5, 0.25))
        fitfill(s, RW - 0.1, RH - 0.05)
        s.move_to([0, RCY, 0])
        self.go(0.02, FadeIn(st), rt=0.15)
        self.go(0.2, FadeIn(head), *[FadeIn(VGroup(i[0], i[1])) for i in items], rt=0.4)
        self.go(2.3, FadeIn(i1[2], shift=UP * 0.1), rt=0.4)
        self.go(4.3, FadeIn(i2[2], shift=UP * 0.1), rt=0.4)
        self.go(6.7, FadeIn(i3[2], shift=UP * 0.1), rt=0.4)
        self.finish()
