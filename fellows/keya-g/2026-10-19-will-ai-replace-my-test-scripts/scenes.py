"""Manim scenes for "Will AI Replace My Test Scripts?" (Keya G.).

One scene per Manim beat in beat_sheet.json:
B02_Hook             a popup with an ×, a test line that fails when the button's id changes, "?"
B04_WhatTestingIs    a drawn app checked by hand, day after day, then a script takes over
B05_SeleniumJunit    script -> browser (Selenium), JUnit framework, readable test code, page object
B06_WhyScriptsBreak  a locator, three builds with three ids, the repair loop, a grid of tests
B07_SelfHealing      Healenium saves a locator, it breaks, candidates are scored, the best is used, a report
B08_VisionAgents     Selenium looks for an id; an agent looks at a screenshot; look-decide-act-check
B09_RpaLink          a bot matches a button by its look, then decides what to do next
B10_WhereAiHelps     "In my experience": edge cases, documentation, scripts that keep running
B11_WhereItFails     cost, different choices per run, a made-up button, a wrong button that passes, who checks

Simple drawn shapes only: no photos, no person icons, no company or tool logos. "Selenium", "JUnit" and
"Healenium" appear as text labels. The Java in B05 is real JUnit 5 / Selenium API, shown as illustration
and labelled "Illustrative code, not run."
Scene length comes from actual_duration_s in beat_sheet.json. The go() times are sentence and phrase
starts measured from each beat's narration audio (ffmpeg silencedetect), so re-check them if the audio
is regenerated.

PORTRAIT: this file is the 16:9 layout. ../vertical/scenes.py is the same file with PORTRAIT = True, which
re-lays every scene natively for a 4.5 x 8 frame (nothing is a crop). Edit this file, then re-copy.
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

DUR = {"B02": 18.50, "B04": 14.44, "B05": 22.42, "B06": 20.07, "B07": 11.20,
       "B08": 19.37, "B09": 13.38, "B10": 11.95, "B11": 16.77}
for _p in (HERE / "beat_sheet.json", HERE.parent / "beat_sheet.json"):
    if _p.is_file():
        DUR = {b["beat_id"]: b["actual_duration_s"] for b in json.loads(_p.read_text())["beats"]}
        break

# humanitarians palette: runtime/remotion/src/tokens/humanitarians.ts
CREAM = "#F3EBDD"
INK = "#2F2A26"
TEAL = "#1F4E5F"      # good / kept
CRIMSON = "#E4572E"   # the one accent: what breaks
SLATE = "#29335C"
GOLD = "#F3A712"      # fill only, never text
PAPER = "#FBF7EE"     # card ground
SOFT = "#6B6458"      # secondary text (4.5:1 on paper)
LINE = "#BDB3A2"      # hairlines, placeholder bars


def L(land, port):
    return port if PORTRAIT else land


# the stage: one big window per scene, filling the safe area (Gate V needs >= 55% of it)
SX = L(6.2, 1.9)          # half width
ST = L(3.35, 3.4)         # top
SB = L(-3.35, -2.9)       # bottom (portrait: text stays above 86% of the height)
SCY = (ST + SB) / 2
SW = 2 * SX
SH = ST - SB
IT = ST - 0.85            # top of the content area (under the title bar)
IB = SB + 0.25            # bottom of the content area
ICY = (IT + IB) / 2
IW = SW - 0.5
IH = IT - IB
RT = ST - 0.8             # content region: under the title bar, inside the stage
RB = SB + 0.25
RX = SX - 0.2
RW = 2 * RX
RH = RT - RB
RCY = (RT + RB) / 2
FS = L(1.0, 0.82)         # type scale


def T(text, size=40, color=INK, **kw):
    return Text(text, font="EB Garamond", font_size=size, color=color, **kw)


def M(text, size=30, color=INK, **kw):
    return Text(text, font="Menlo", font_size=size, color=color, **kw)


def fit(mob, max_w, max_h=None):
    if mob.width > max_w:
        mob.scale(max_w / mob.width)
    if max_h is not None and mob.height > max_h:
        mob.scale(max_h / mob.height)
    return mob


def card(w, h, color=INK, fill=PAPER, sw=4, r=0.16):
    return RoundedRectangle(corner_radius=r, width=w, height=h, stroke_color=color, stroke_width=sw,
                            fill_color=fill, fill_opacity=1)


def tag(text, color=TEAL, size=26, fw=None):
    t = M(text, size, INK if color == CRIMSON else color)   # terracotta text on cream fails Gate T contrast: INK text, terracotta outline
    if fw:
        fit(t, fw)
    box = RoundedRectangle(corner_radius=0.1, width=t.width + 0.3, height=t.height + 0.26,
                           stroke_color=color, stroke_width=3, fill_color=PAPER, fill_opacity=1)
    t.move_to(box)
    return VGroup(box, t)


def chip(text, color=TEAL, size=30, tcolor=CREAM, fw=None, pad=0.5):
    t = T(text, size, tcolor)
    if fw:
        fit(t, fw)
    box = RoundedRectangle(corner_radius=0.14, width=t.width + pad, height=t.height + 0.3,
                           stroke_width=0, fill_color=color, fill_opacity=1)
    t.move_to(box)
    return VGroup(box, t)


def pchip(text, color=TEAL, size=30, fw=None, pad=0.5):
    """Portrait label chip: INK text on a pale tint of the colour. A dark fill with light text reads to
    Gate T as broken fragments, so the tint carries the colour and the text stays INK."""
    t = T(text, size, INK)
    if fw:
        fit(t, fw)
    box = RoundedRectangle(corner_radius=0.14, width=t.width + pad, height=t.height + 0.3,
                           stroke_width=0, fill_color=interpolate_color(ManimColor(PAPER), ManimColor(color), 0.3), fill_opacity=1)
    t.move_to(box)
    return VGroup(box, t)


def tick(s=0.3, color=TEAL):
    return VMobject(stroke_color=color, stroke_width=7).set_points_as_corners(
        [[-s, 0, 0], [-s * 0.3, -s * 0.7, 0], [s, s * 0.8, 0]])


def cross(s=0.28, color=CRIMSON):
    return VGroup(Line([-s, -s, 0], [s, s, 0], stroke_color=color, stroke_width=8),
                  Line([-s, s, 0], [s, -s, 0], stroke_color=color, stroke_width=8))


def xbtn(r=0.34, color=INK):
    c = Circle(radius=r, stroke_color=color, stroke_width=4, fill_color=PAPER, fill_opacity=1)
    return VGroup(c, cross(r * 0.42, color))


def cursor(s=1.0, color=INK):
    p = Polygon([0, 0, 0], [0, -0.62, 0], [0.16, -0.48, 0], [0.3, -0.78, 0], [0.42, -0.72, 0],
                [0.29, -0.43, 0], [0.5, -0.43, 0], stroke_color=PAPER, stroke_width=2,
                fill_color=color, fill_opacity=1)
    return p.scale(s)


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


def popup(w, h, simple=False):
    """A drawn popup: title, two text bars, OK, and an x in the corner. .x is the x; .tag_at is where
    the scene hangs its id tag (inside the card, under OK)."""
    c = card(w, h, INK, PAPER, 4)
    title = T("Sign up for news", L(36, 30)).move_to(c.get_top() + DOWN * 0.55)
    fit(title, w - 1.6)
    title.align_to(c, LEFT).shift(RIGHT * 0.3)
    body = lines_block(2, w - 0.9, h=0.13, gap=0.3).move_to(c.get_center() + UP * h * 0.1)
    ok = chip("OK", TEAL, L(30, 26)).move_to(c.get_bottom() + UP * (h * 0.3))
    x = xbtn(L(0.38, 0.3)).move_to(c.get_corner(UR) + np.array([-0.45, -0.45, 0]))
    if simple:
        title = T("Sign up", L(40, 20))
        title.move_to(c.get_center() + DOWN * 0.15)
        body = VGroup()
        ok = VGroup()
    g = VGroup(c, title, body, ok, x)
    g.x = x
    g.body = body
    g.card = c
    return g


class Timed:
    def setup(self):
        self.camera.background_color = CREAM

    @property
    def now(self):
        return self.renderer.time

    def go(self, t, *anims, rt=0.5):
        gap = t - self.now
        if gap > 1e-3:
            self.wait(gap)
        elif gap < -0.05:
            print(f"QC {self.BEAT}: cue {t}s is late by {-gap:.2f}s")
        if anims:
            self.play(*anims, **({} if rt is None else {"run_time": rt}))

    def finish(self):
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



# --------------------------------------------------------------------------------------------
def ppop(w, h, xs=0.5, title="Sign up\nfor news"):
    """Portrait popup: big title on two lines, large x, readable OK."""
    c = card(w, h, INK, PAPER, 4)
    t = T(title, 38)
    t.move_to(c.get_corner(UL) + np.array([0.3 + t.width / 2, -0.7, 0]))
    x = xbtn(xs).move_to(c.get_corner(UR) + np.array([-0.55, -0.55, 0]))
    body = lines_block(2, w - 0.9, h=0.13, gap=0.28).move_to(c.get_center() + DOWN * h * 0.08)
    ok = chip("OK", TEAL, 34).move_to(c.get_bottom() + UP * 0.55)
    g = VGroup(c, t, x, body, ok)
    g.card, g.x, g.body, g.ok = c, x, body, ok
    return g



@timed("B02")
class B02_Hook(Scene):
    def construct(self):
        if PORTRAIT:
            return self.construct_p()
        st = stage("the app")
        if PORTRAIT:
            pw, ph, pc = 3.55, 2.85, [0, RT - 1.45, 0]
            sw, sh, sc = 3.55, 2.3, [0, RB + 1.2, 0]
        else:
            pw, ph, pc = 6.2, RH - 0.05, [-3.0, RCY, 0]
            sw, sh, sc = 5.5, RH - 0.05, [3.25, RCY, 0]
        pop = popup(pw, ph).move_to(pc)
        idtag = tag('id="close-button"', TEAL, L(30, 21), fw=pw - 0.4).move_to(pop.card.get_bottom() + UP * L(0.65, 0.4))
        script = card(sw, sh, TEAL, PAPER, 4).move_to(sc)
        s_title = T("my test", L(40, 32), TEAL).move_to(script.get_top() + DOWN * 0.5)
        s_lines = VGroup(*[M(r, L(32, 26)) for r in (["open page", "click close-button", "popup gone?"] if not PORTRAIT else ["open page", "click close", "popup gone?"])])
        s_lines.arrange(DOWN, aligned_edge=LEFT, buff=L(0.55, 0.14))
        fit(s_lines, sw - 1.1)
        s_lines.move_to(script.get_center() + DOWN * L(0.35, 0.4) + LEFT * 0.25)
        marks = VGroup(*[tick(0.17).next_to(l, RIGHT, buff=0.25) for l in s_lines])
        self.go(0.05, FadeIn(st), rt=0.3)
        self.go(0.4, FadeIn(pop), FadeIn(script), FadeIn(s_title), FadeIn(idtag), rt=0.5)
        self.go(1.0, LaggedStart(*[FadeIn(l, shift=RIGHT * 0.1) for l in s_lines], lag_ratio=0.3), rt=0.7)
        self.go(1.9, LaggedStart(*[Create(m) for m in marks], lag_ratio=0.3), rt=0.6)
        # S2 (2.97): the test fails, the page is fine, the id changes overnight
        fail = cross(0.17).move_to(marks[1].get_center())
        self.go(3.0, ReplacementTransform(marks[1], fail), rt=0.4)
        fine = chip("the page is fine", TEAL, L(34, 26)).move_to(pop.card.get_center() + DOWN * L(0.05, 0.0))
        fine.move_to(pop.card.get_center() + UP * L(0.1, 0.05))
        self.go(3.6, FadeOut(pop.body), FadeIn(fine, scale=0.9), rt=0.4)
        night = chip("overnight", SLATE, L(34, 26)).move_to(pop.card.get_center() + UP * L(0.1, 0.0))
        new_id = tag('id="btn-4821"', CRIMSON, L(30, 21), fw=pw - 0.4).move_to(idtag)
        self.go(5.0, FadeOut(fine), FadeIn(pop.body), rt=0.3)
        self.go(5.6, Transform(idtag, new_id), FadeOut(pop.body), FadeOut(pop[3]), FadeIn(night), rt=0.5)
        # S3 (7.82): I look for the X
        ey = eye(L(1.4, 1.0)).move_to(pop.card.get_center() + UP * L(0.55, 0.55))
        look = T("I look for the X", L(44, 34), CRIMSON); fit(look, pw - 1.0)
        look.next_to(ey, DOWN, buff=0.3)
        ring = Circle(radius=L(0.5, 0.42), stroke_color=CRIMSON, stroke_width=6).move_to(pop.x)
        self.go(7.85, FadeOut(night), FadeOut(pop.body), FadeOut(pop[3]), FadeIn(ey), Create(ring), rt=0.5)
        self.go(8.9, FadeIn(look), rt=0.4)
        # S4 (10.5): my script looks for an id and finds nothing
        self.go(10.5, FadeOut(ey), FadeOut(look), FadeOut(ring), FadeIn(pop.body), FadeIn(pop[3]), s_lines.animate.set_opacity(0.4), rt=0.4)
        ghost = tag('id="close-button"', TEAL, L(30, 21), fw=sw - 0.5).move_to(script.get_bottom() + UP * L(0.6, 0.35))
        ghost_red = tag('id="close-button"', CRIMSON, L(30, 21), fw=sw - 0.5).move_to(ghost)
        nomatch = T("no match", L(38, 28), CRIMSON).next_to(ghost, UP, buff=0.12)
        self.go(11.0, FadeIn(ghost), rt=0.4)
        self.go(12.0, Transform(ghost, ghost_red), FadeIn(nomatch), rt=0.4)
        # S5 (13.59): plain English instead
        eng = VGroup(T("Open the page.", L(44, 30), SLATE), T("Close the popup.", L(44, 30), SLATE)).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        fit(eng, sw - 0.6)
        eng.move_to(script.get_center() + DOWN * L(0.25, 0.3))
        self.go(13.6, FadeOut(s_lines), FadeOut(marks[0]), FadeOut(marks[2]), FadeOut(fail), FadeOut(ghost),
                FadeOut(nomatch), Transform(s_title, T("plain English", L(40, 32), SLATE).move_to(s_title)),
                script.animate.set_stroke(SLATE), rt=0.5)
        self.go(14.2, Write(eng), rt=1.3)
        arrow = Arrow(script.get_left() if not PORTRAIT else script.get_top(), pop.card.get_right() if not PORTRAIT else pop.card.get_bottom(),
                      buff=0.12, color=SLATE, stroke_width=6)
        self.go(16.0, GrowArrow(arrow), rt=0.5)
        # S6 (17.6): should I be worried?
        q = T("?", L(280, 200), CRIMSON).move_to(script.get_center() + DOWN * 0.15)
        self.go(17.6, FadeOut(eng), FadeOut(arrow), FadeIn(q, scale=0.6), rt=0.5)
        self.finish()

    def construct_p(self):
        st = stage("the app")
        pop = ppop(3.3, 2.8).move_to([0, 0.55, 0])
        idt = tag('id="close-button"', TEAL, 24, fw=3.3).move_to([0, RB + 0.55, 0])
        self.go(0.05, FadeIn(st), rt=0.25)
        self.go(0.4, FadeIn(pop), FadeIn(idt), rt=0.6)
        # S2: my test fails, the app is fine, the id changed overnight
        tc = card(3.3, 2.0, TEAL, PAPER, 4).move_to([0, -1.6, 0])
        tt = T("my test", 36, TEAL).move_to(tc.get_top() + DOWN * 0.4)
        rows = VGroup(*[M(r, 24) for r in ["open page", "click close", "popup gone?"]]).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        rows.move_to(tc.get_center() + DOWN * 0.3)
        rows.align_to(tc, LEFT).shift(RIGHT * 0.3)
        marks = VGroup(*[tick(0.17).move_to([tc.get_right()[0] - 0.5, r.get_center()[1], 0]) for r in rows])
        fail = cross(0.17).move_to(marks[1])
        self.go(3.0, pop.animate.scale(0.55).move_to([0, 1.7, 0]), idt.animate.move_to([0, 0.5, 0]),
                FadeIn(tc), FadeIn(tt), FadeIn(rows), FadeIn(marks), rt=0.6)
        self.go(3.8, ReplacementTransform(marks[1], fail), rt=0.3)
        fine = chip("the app is fine", TEAL, 32).move_to([0, 0.5, 0])
        self.go(4.5, FadeOut(idt), FadeIn(fine, scale=0.9), rt=0.3)
        newid = tag('id="btn-4821"', CRIMSON, 24, fw=3.3).move_to([0, 0.5, 0])
        night = chip("overnight", SLATE, 30).move_to([0, -0.05, 0])
        self.go(5.6, FadeOut(fine), FadeIn(newid), rt=0.3)
        self.go(6.2, FadeIn(night, shift=UP * 0.1), rt=0.4)
        # S3 (7.82): I look for the X
        self.go(7.8, *[FadeOut(m) for m in (tc, tt, rows, marks[0], marks[2], fail, newid, night)], rt=0.3)
        self.go(8.15, pop.animate.scale(1 / 0.55).move_to([0, 0.85, 0]), rt=0.5)
        ring = Circle(radius=0.5, stroke_color=CRIMSON, stroke_width=6).move_to(pop.x)
        ey = eye(1.0).move_to([0, -0.95, 0])
        look = T("I look for\nthe X", 42, CRIMSON).move_to([0, -1.95, 0])
        self.go(8.8, Create(ring), FadeIn(ey), rt=0.4)
        self.go(9.4, FadeIn(look), rt=0.4)
        # S4 (10.5): my script looks for an id and finds nothing
        self.go(10.5, FadeOut(ey), FadeOut(look), FadeOut(ring), pop.animate.scale(0.55).move_to([0, 1.7, 0]), rt=0.5)
        sc = card(3.3, 2.1, TEAL, PAPER, 4).move_to([0, -1.6, 0])
        stt = T("my script", 36, TEAL).move_to(sc.get_top() + DOWN * 0.4)
        ghost = tag('id="close-button"', TEAL, 24, fw=3.0).move_to(sc.get_center() + DOWN * 0.15)
        ghost_red = tag('id="close-button"', CRIMSON, 24, fw=3.0).move_to(ghost)
        nomatch = T("no match", 40, CRIMSON).move_to(sc.get_bottom() + UP * 0.4)
        self.go(11.0, FadeIn(sc), FadeIn(stt), FadeIn(ghost), rt=0.5)
        self.go(12.0, Transform(ghost, ghost_red), FadeIn(nomatch), rt=0.4)
        # S5 (13.59): plain English
        eng = VGroup(T("Open the page.", 36, SLATE), T("Close the popup.", 36, SLATE)).arrange(DOWN, buff=0.25).move_to(sc.get_center() + DOWN * 0.3)
        self.go(13.6, FadeOut(ghost), FadeOut(nomatch), Transform(stt, T("plain English", 36, SLATE).move_to(stt)),
                sc.animate.set_stroke(SLATE), rt=0.5)
        self.go(14.2, Write(eng), rt=1.3)
        arrow = Arrow([0, -0.55, 0], pop.card.get_bottom() + DOWN * 0.05, buff=0.05, color=SLATE, stroke_width=7)
        self.go(16.0, GrowArrow(arrow), rt=0.5)
        # S6 (17.6)
        q = T("?", 380, CRIMSON).move_to([0, 0.1, 0])
        self.go(17.6, *[FadeOut(m) for m in (pop, sc, stt, eng, arrow)], FadeIn(q, scale=0.6), rt=0.5)
        self.finish()


# --------------------------------------------------------------------------------------------
@timed("B04")
class B04_WhatTestingIs(Scene):
    def construct(self):
        st = stage("the app")
        names = ["Login", "Menu", "Form", "Next page"]
        if PORTRAIT:
            gw, gh = IW, 2.5
            gc = [0, RT - gh / 2, 0]
            pc, pw, ph = [0, RB + 1.3, 0], IW, 2.5
            bw, bh = (gw - 0.2) / 2, (gh - 0.2) / 2
        else:
            gw, gh = 6.5, RH
            gc = [-RX + gw / 2, RCY, 0]
            pc, pw, ph = [RX - 2.6, RCY, 0], 5.2, RH
            bw, bh = (gw - 0.25) / 2, (gh - 0.25) / 2
        pos = [[gc[0] - bw / 2 - 0.1, gc[1] + bh / 2 + 0.1, 0], [gc[0] + bw / 2 + 0.1, gc[1] + bh / 2 + 0.1, 0],
               [gc[0] - bw / 2 - 0.1, gc[1] - bh / 2 - 0.1, 0], [gc[0] + bw / 2 + 0.1, gc[1] - bh / 2 - 0.1, 0]]
        btns = VGroup()
        for n, p in zip(names, pos):
            c = card(bw, bh, INK, PAPER, 4, 0.22).move_to(p)
            t = T(n, L(48, 34)); fit(t, bw - 0.3)
            t.move_to(c)
            btns.add(VGroup(c, t))
        panel = card(pw, ph, INK, PAPER, 4).move_to(pc)
        ptitle = T("by hand", L(42, 32), SOFT).move_to(panel.get_top() + DOWN * 0.45)
        day = T("Day 1", L(96, 44), INK).move_to(panel.get_center() + UP * L(0.55, 0.0) + (LEFT * 0.9 if PORTRAIT else ORIGIN))
        rr = L(0.75, 0.55)
        clock = Circle(radius=rr, stroke_color=INK, stroke_width=5, fill_color=PAPER, fill_opacity=1)
        clock.move_to(panel.get_bottom() + UP * L(1.65, 1.0) if not PORTRAIT else panel.get_center() + RIGHT * 0.95 + DOWN * 0.1)
        hand = Line(clock.get_center(), clock.get_center() + UP * rr * 0.8, stroke_color=INK, stroke_width=5)
        self.go(0.05, FadeIn(st), rt=0.2)
        self.go(0.3, LaggedStart(*[FadeIn(b, scale=0.92) for b in btns], lag_ratio=0.2), rt=1.0)
        self.go(2.25, FadeIn(panel), FadeIn(ptitle), FadeIn(day), FadeIn(clock), FadeIn(hand), rt=0.4)
        cur = cursor(L(1.4, 1.1)).move_to(btns[0].get_center() + DOWN * 0.7 + LEFT * 0.9)
        self.add(cur)
        ticks = []
        for b, t0 in zip(btns, [3.7, 4.5, 5.3, 6.05]):
            self.go(t0 - 0.45, cur.animate.move_to(b.get_corner(DR) + LEFT * L(0.7, 0.25) + DOWN * L(-0.3, 0.05)), rt=0.4)
            tk = tick(L(0.26, 0.12)).move_to(b[0].get_corner(UR) + np.array([-L(0.45, 0.2), -L(0.45, 0.2), 0]))
            ticks.append(tk)
            self.go(t0, Create(tk), rt=0.2)
        for k, t0 in enumerate([6.9, 7.6, 8.3], start=2):
            self.go(t0, Transform(day, T(f"Day {k}", L(96, 44)).move_to(day)), Rotate(hand, angle=-PI, about_point=clock.get_center()), rt=0.25)
        slow = chip("slow", CRIMSON, L(60, 44)).move_to(panel.get_bottom() + UP * L(0.7, 0.4)) if not PORTRAIT else chip("slow", CRIMSON, 40).move_to(panel.get_bottom() + UP * 0.45)
        self.go(8.5, FadeIn(slow, scale=0.7), rt=0.3)
        # S4 (9.65): scripts take over
        code = VGroup(*[M(s, L(34, 24)) for s in ["click Login", "click Menu", "fill Form", "open Next page"]])
        code.arrange(DOWN, aligned_edge=LEFT, buff=L(0.5, 0.2))
        fit(code, pw - 1.0, ph - 0.9)
        code.move_to(panel.get_center() + DOWN * L(0.0, 0.1) + RIGHT * L(0.0, 0.25))
        self.go(9.7, FadeOut(slow), FadeOut(hand), FadeOut(clock), FadeOut(day), FadeOut(*ticks),
                Transform(ptitle, T("test script", L(42, 32), TEAL).move_to(ptitle)), panel.animate.set_stroke(TEAL, 6), rt=0.4)
        self.go(10.2, LaggedStart(*[FadeIn(c, shift=RIGHT * 0.15) for c in code], lag_ratio=0.2), rt=0.8)
        self.go(11.55, cur.animate.move_to(btns[0].get_corner(DR) + LEFT * L(0.7, 0.25) + DOWN * L(-0.3, 0.05)), rt=0.2)
        for b, c in zip(btns, code):
            tk = tick(L(0.26, 0.12), TEAL).move_to(b[0].get_corner(UR) + np.array([-L(0.45, 0.2), -L(0.45, 0.2), 0]))
            ck = tick(0.2, TEAL).next_to(c, LEFT if PORTRAIT else RIGHT, buff=0.25)
            self.play(cur.animate.move_to(b.get_corner(DR) + LEFT * L(0.7, 0.25) + DOWN * L(-0.3, 0.05)), Create(tk), Create(ck), run_time=0.45)
        self.finish()


# --------------------------------------------------------------------------------------------
def code_lines():
    """The test, real JUnit 5 / Selenium API. Landscape lines; portrait wraps to short lines."""
    if not PORTRAIT:
        return [
            ('var login = driver.findElement(By.id("login"));', "find", 0),
            ("login.click();", "act", 1),
            ('var msg = driver.findElement(By.id("msg"));', "check", 2),
            ('assertEquals("Welcome", msg.getText());', "check", 2),
        ]
    return [
        ("var login = driver", "find", 0), ("  .findElement(", "find", 0), ('  By.id("login"));', "find", 0),
        ("login.click();", "act", 1),
        ("var msg = driver", "check", 2), ("  .findElement(", "check", 2), ('  By.id("msg"));', "check", 2),
        ("assertEquals(", "check", 2), ('  "Welcome",', "check", 2), ("  msg.getText());", "check", 2),
    ]


@timed("B05")
class B05_SeleniumJunit(Scene):
    def construct(self):
        st = stage("LoginTest.java")
        # --- phase 1: script -> browser, wrapped by JUnit
        if PORTRAIT:
            bw, bh = 3.1, 1.4
            sp, bp = [0, RT - 1.45, 0], [0, RB + 0.8, 0]
        else:
            bw, bh = 3.5, RH - 1.2
            sp, bp = [-3.9, RCY - 0.2, 0], [4.0, RCY - 0.2, 0]
        script = card(bw, bh, TEAL, PAPER, 5).move_to(sp)
        s_lab = T("my script", L(42, 32), TEAL).move_to(script.get_top() + DOWN * 0.5)
        if PORTRAIT:
            s_lab.move_to(script.get_corner(UL) + np.array([0.15, -0.4, 0]), aligned_edge=LEFT)
        s_rows = lines_block(3, bw - 0.9, h=0.13, gap=L(0.4, 0.2)).move_to(script.get_center() + DOWN * L(0.35, 0.22))
        browser = card(bw, bh, INK, PAPER, 5).move_to(bp)
        b_bar = Line(browser.get_corner(UL) + DOWN * 0.5, browser.get_corner(UR) + DOWN * 0.5, stroke_color=INK, stroke_width=3)
        b_dots = VGroup(*[Dot(radius=0.06, color=c) for c in (CRIMSON, GOLD, TEAL)]).arrange(RIGHT, buff=0.1)
        b_dots.move_to(browser.get_corner(UL) + np.array([0.5, -0.25, 0]))
        b_lab = T("web browser", L(42, 30)).move_to(browser.get_center() + DOWN * 0.25)
        mid = (np.array(sp) + np.array(bp)) / 2
        if PORTRAIT:
            arrow = Arrow(script.get_bottom(), browser.get_top(), buff=0.12, color=INK, stroke_width=7)
            sel = chip("Selenium", SLATE, 34).move_to(mid + LEFT * 0.0)
            sel_note = VGroup()
        else:
            arrow = Arrow(script.get_right(), browser.get_left(), buff=0.12, color=INK, stroke_width=7)
            sel = chip("Selenium", SLATE, 44).move_to(mid + UP * 0.8)
            sel_note = T("controls a browser", 32, SOFT).move_to(mid + DOWN * 0.6)
        self.go(0.05, FadeIn(st), rt=0.3)
        self.go(0.4, FadeIn(script), FadeIn(s_lab), FadeIn(s_rows), FadeIn(browser), FadeIn(b_bar), FadeIn(b_dots), FadeIn(b_lab), rt=0.5)
        self.go(1.5, GrowArrow(arrow), FadeIn(sel, shift=UP * 0.1), rt=0.6)
        if not PORTRAIT:
            self.go(2.3, FadeIn(sel_note), rt=0.4)
        # JUnit wraps the script (3.88)
        wrap = DashedVMobject(RoundedRectangle(corner_radius=0.25, width=bw + 0.3, height=bh + 0.3, stroke_color=CRIMSON, stroke_width=6).move_to(script), num_dashes=44)
        ju = chip("JUnit", CRIMSON, L(44, 34))
        ju.move_to(script.get_corner(UL) + np.array([1.0, 0.5, 0]) if not PORTRAIT else np.array([0.0, RT - 0.3, 0.0]))
        ju_note = T("runs it as a test", L(32, 28), CRIMSON).next_to(script, DOWN, buff=0.28) if not PORTRAIT else VGroup()
        self.go(3.9, Create(wrap), FadeIn(ju, scale=0.8), rt=0.7)
        if not PORTRAIT:
            self.go(5.0, FadeIn(ju_note), rt=0.4)
            self.go(6.0, Indicate(ju, color=CRIMSON, scale_factor=1.1), rt=0.6)
        # --- phase 2: the code (7.61)
        phase1 = VGroup(script, s_lab, s_rows, browser, b_bar, b_dots, b_lab, arrow, sel, sel_note, wrap, ju, ju_note)
        cl = code_lines()
        code = VGroup(*[M(t, L(26, 18)) for t, _, _ in cl]).arrange(DOWN, aligned_edge=LEFT, buff=L(0.62, 0.08))
        fit(code, IW - 0.8)
        trail = VGroup(*[chip(n, c, L(36, 22), pad=L(0.5, 0.25)) for n, c in [("FIND", TEAL), ("ACT", CRIMSON), ("CHECK", SLATE)]]).arrange(RIGHT, buff=L(0.3, 0.12))
        trail.move_to([0, RT - 0.45, 0])
        ccard = card(code.width + 0.7, code.height + 0.6, INK, PAPER, 4)
        code.move_to([0, RCY - L(0.15, 0.2), 0])
        ccard.move_to(code)
        note = T("Illustrative code, not run.", L(32, 22), SOFT).move_to([0, RB + 0.3, 0])

        def lit(idx):
            r = VGroup(*[code[i] for i, (_, _, g) in enumerate(cl) if g == idx])
            return Rectangle(width=ccard.width - 0.1, height=r.height + 0.22, stroke_width=0, fill_color=GOLD, fill_opacity=0.65).move_to(r).set_x(ccard.get_center()[0])

        def mark(idx):
            return [t.animate.set_opacity(1 if i == idx else 0.4) for i, t in enumerate(trail)]

        self.go(7.5, FadeOut(phase1), rt=0.3)
        self.go(7.9, FadeIn(ccard), FadeIn(code), FadeIn(trail), FadeIn(note), rt=0.6)
        for t in trail:
            t.set_opacity(0.4)
        hl = lit(0)
        self.go(9.3, FadeIn(hl), *mark(0), rt=0.3)
        self.go(10.45, Transform(hl, lit(1)), *mark(1), rt=0.3)
        self.go(11.15, Transform(hl, lit(2)), *mark(2), rt=0.3)
        for t0, idx in [(13.2, 0), (15.0, 1), (16.0, 2)]:
            self.go(t0, Transform(hl, lit(idx)), *mark(idx), rt=0.3)
        # --- phase 3: page object (17.5)
        po_lines = ['By login = By.id("login");', 'By msg   = By.id("msg");'] if not PORTRAIT else ['By login =', '  By.id("login");', 'By msg =', '  By.id("msg");']
        po_t = VGroup(*[M(s, L(30, 20)) for s in po_lines]).arrange(DOWN, aligned_edge=LEFT, buff=L(0.4, 0.15))
        fit(po_t, IW - 0.7)
        po_title = T("page object: LoginPage", L(42, 26), SLATE)
        fit(po_title, IW - 0.6)
        po_card = card(max(po_t.width + 0.8, po_title.width + 0.6), po_t.height + L(1.5, 1.1), SLATE, PAPER, 5)
        po_title.move_to(po_card.get_top() + DOWN * 0.55)
        po_t.move_to(po_card.get_center() + DOWN * 0.3)
        po = VGroup(po_card, po_title, po_t)
        tc = card(L(3.3, 3.3), L(1.5, 1.4), TEAL, PAPER, 4)
        tt = T("LoginTest", L(36, 28), TEAL); fit(tt, tc.width - 0.3)
        tt.move_to(tc.get_top() + DOWN * 0.4)
        tr = lines_block(3, tc.width - 0.7, h=0.12, gap=0.22).move_to(tc.get_center() + DOWN * 0.25)
        test_c = VGroup(tc, tt, tr)
        if PORTRAIT:
            test_c.move_to([0, RT - 1.4, 0]); po.move_to([0, RB + 1.3, 0])
            link = Arrow(test_c.get_bottom(), po.get_top(), buff=0.1, color=INK, stroke_width=6)
        else:
            test_c.move_to([-RX + 1.8, RCY - 0.2, 0]); po.move_to([RX - po.width / 2 - 0.2, RCY - 0.2, 0])
            link = Arrow(test_c.get_right(), po.get_left(), buff=0.1, color=INK, stroke_width=6)
        one = chip("locators live in one place", TEAL, L(40, 24), fw=IW - 0.4).move_to([0, RT - L(0.45, 0.3), 0])
        self.go(17.4, FadeOut(ccard), FadeOut(code), FadeOut(hl), FadeOut(trail), FadeOut(note), rt=0.3)
        self.go(17.8, FadeIn(test_c), FadeIn(po), rt=0.5)
        self.go(18.5, GrowArrow(link), FadeIn(one), rt=0.5)
        self.go(21.2, Indicate(po_title, color=SLATE, scale_factor=1.12), rt=0.6)
        self.finish()


# --------------------------------------------------------------------------------------------
@timed("B06")
class B06_WhyScriptsBreak(Scene):
    def construct(self):
        st = stage("the page")
        # phase 1: the button and its locator
        btn = card(L(5.6, 3.3), L(2.4, 1.7), INK, PAPER, 5, 0.3).move_to([0, RT - L(1.6, 1.4), 0])
        bl = T("Close", L(96, 64)); bl.move_to(btn)
        loc = tag('id="close-button"', TEAL, L(50, 26), fw=IW - 0.8).move_to([0, RCY - L(1.0, 0.5), 0])
        loc_lab = T("a locator", L(52, 40), SOFT).next_to(loc, DOWN, buff=0.4)
        self.go(0.05, FadeIn(st), rt=0.2)
        self.go(0.3, FadeIn(btn), FadeIn(bl), rt=0.4)
        self.go(1.0, FadeIn(loc, shift=UP * 0.1), rt=0.4)
        self.go(2.2, FadeIn(loc_lab), rt=0.4)
        # phase 2: three builds
        ids = ["close-button", "btn-4821", "x-9f2c"]
        cols = []
        for i, name in enumerate(ids):
            if PORTRAIT:
                cw, ch, c = IW, 1.2, [0, RT - 0.65 - i * 1.3, 0]
            else:
                cw, ch, c = (RW - 0.4) / 3, RH - 1.8, [-(RW - 0.4) / 3 - 0.2 + i * ((RW - 0.4) / 3 + 0.2), RT - 0.1 - (RH - 1.8) / 2, 0]
            cd = card(cw, ch, INK, PAPER, 4).move_to(c)
            lab = T(f"Build {i + 1}", L(40, 30), SOFT).move_to(cd.get_corner(UL) + np.array([0.2, -0.38, 0]), aligned_edge=LEFT)
            mini = card(L(2.4, 1.3), L(1.2, 0.7), INK, PAPER, 3, 0.15)
            ml = T("Close", L(40, 28)); ml.move_to(mini)
            mg = VGroup(mini, ml) if not PORTRAIT else VGroup()
            tg = tag(f'id="{name}"', TEAL if i == 0 else CRIMSON, L(26, 20), fw=cw - 0.3)
            if PORTRAIT:
                tg.move_to(cd.get_center() + DOWN * 0.22)
                lab.move_to(cd.get_corner(UL) + np.array([0.15, -0.25, 0]), aligned_edge=LEFT)
            else:
                mg.move_to(cd.get_center() + UP * 0.2)
                tg.move_to(cd.get_bottom() + UP * 0.8)
            cols.append(VGroup(cd, lab, mg, tg))
        statuses = [tick(0.25, TEAL), cross(0.24), cross(0.24)]
        for s, c in zip(statuses, cols):
            s.move_to(c[0].get_corner(UR) + np.array([-0.45, -0.4 if not PORTRAIT else -0.35, 0]))
        self.go(3.8, FadeOut(btn), FadeOut(bl), FadeOut(loc), FadeOut(loc_lab), rt=0.25)
        self.go(4.1, FadeIn(cols[0]), rt=0.3)
        self.go(4.8, FadeIn(cols[1]), rt=0.3)
        self.go(5.5, FadeIn(cols[2]), rt=0.3)
        self.go(6.1, *[Create(s) for s in statuses], rt=0.5)
        # combine attributes (7.15): a band under the builds
        combo = VGroup(tag("id", TEAL, L(40, 32)), T("+", L(52, 44)), tag("text", TEAL, L(40, 32)), T("+", L(52, 44)), tag("class", TEAL, L(40, 32)))
        combo.arrange(RIGHT, buff=0.3)
        fit(combo, IW - 1.0)
        band = card(IW, L(1.5, 1.2), TEAL, PAPER, 5).move_to([0, RB + L(0.85, 0.65), 0])
        combo.move_to(band)
        self.go(7.2, FadeIn(band), FadeIn(combo, scale=0.9), rt=0.5)
        # phase 3: the repair loop (9.99)
        self.go(9.95 if not PORTRAIT else 9.55, FadeOut(band), FadeOut(combo), *[FadeOut(c) for c in cols], *[FadeOut(s) for s in statuses], rt=0.3)
        steps = ["investigate", "find the new locator", "update it", "run the test again"]
        if PORTRAIT:
            nw, nh = IW - 0.6, 1.05
            pts = [[0.0, RT - 0.7 - i * 1.4, 0] for i in range(4)]
        else:
            nw, nh = 5.4, 2.0
            pts = [[-3.1, RT - 1.2, 0], [3.1, RT - 1.2, 0], [3.1, RB + 1.2, 0], [-3.1, RB + 1.2, 0]]
        nodes = VGroup()
        for i, (s_, p) in enumerate(zip(steps, pts)):
            c = card(nw, nh, INK, PAPER, 4, 0.25).move_to(p)
            n = Circle(radius=0.3, stroke_width=0, fill_color=TEAL, fill_opacity=1).move_to(c.get_left() + RIGHT * 0.55)
            nt = T(str(i + 1), 34, CREAM).move_to(n)
            t = T(s_, L(44, 32)); fit(t, nw - 1.6)
            t.move_to(c.get_center() + RIGHT * 0.35)
            nodes.add(VGroup(c, n, nt, t))
        if PORTRAIT:
            arrows = VGroup(*[Arrow(nodes[i][0].get_bottom(), nodes[i + 1][0].get_top(), buff=0.05, color=INK, stroke_width=6) for i in range(3)])
            back = CurvedArrow(nodes[3][0].get_right() + RIGHT * 0.0, nodes[0][0].get_right(), angle=PI * 0.9, color=CRIMSON, stroke_width=6)
            back.shift(LEFT * 0.0)
        else:
            arrows = VGroup(Arrow(nodes[0][0].get_right(), nodes[1][0].get_left(), buff=0.1, color=INK, stroke_width=6),
                            Arrow(nodes[1][0].get_bottom(), nodes[2][0].get_top(), buff=0.1, color=INK, stroke_width=6),
                            Arrow(nodes[2][0].get_left(), nodes[3][0].get_right(), buff=0.1, color=INK, stroke_width=6),
                            Arrow(nodes[3][0].get_top(), nodes[0][0].get_bottom(), buff=0.1, color=CRIMSON, stroke_width=6))
            back = VGroup()
        center_chip = chip("test fails", CRIMSON, 40).move_to([0, RCY, 0]) if not PORTRAIT else VGroup()
        self.go(10.3, FadeIn(center_chip) if not PORTRAIT else Wait(0.01), rt=0.3)
        self.go(11.7, FadeIn(nodes[0], scale=0.9), rt=0.3)
        self.go(13.2, FadeIn(nodes[1], scale=0.9), GrowArrow(arrows[0]), rt=0.3)
        self.go(14.2, FadeIn(nodes[2], scale=0.9), GrowArrow(arrows[1]), rt=0.3)
        self.go(15.2, FadeIn(nodes[3], scale=0.9), GrowArrow(arrows[2]), rt=0.3)
        self.go(15.75, GrowArrow(arrows[3]) if not PORTRAIT else Create(back), rt=0.3)
        # phase 4: hundreds (16.45)
        cols_n, rows_n = (9, 10) if PORTRAIT else (18, 8)
        cell = min((IW - 0.2) / cols_n, (RH - 1.2) / rows_n)
        rng = np.random.default_rng(7)
        grid = VGroup()
        for r in range(rows_n):
            for c in range(cols_n):
                bad = rng.random() < 0.28
                sq = RoundedRectangle(corner_radius=0.05, width=cell * 0.8, height=cell * 0.8, stroke_width=0,
                                      fill_color=CRIMSON if bad else TEAL, fill_opacity=1 if bad else 0.6)
                sq.move_to([(c - (cols_n - 1) / 2) * cell, (rows_n - 1) / 2 * cell - r * cell, 0])
                grid.add(sq)
        grid.move_to([0, RB + (rows_n * cell) / 2 + 0.1, 0])
        self.go(16.4, FadeOut(nodes), FadeOut(arrows), FadeOut(center_chip), FadeOut(back), rt=0.3)
        self.go(16.7, LaggedStart(*[FadeIn(g, scale=0.6) for g in grid], lag_ratio=0.002), rt=0.35)
        stamp = chip("unsustainable", CRIMSON, L(54, 40)).move_to([0, RT - 0.4, 0])
        self.go(18.05, FadeIn(stamp, scale=0.8), rt=0.4)
        self.finish()


# --------------------------------------------------------------------------------------------
@timed("B07")
class B07_SelfHealing(Scene):
    def construct(self):
        st = stage("self-healing, in the open")
        label = (pchip("Healenium", SLATE, 46) if PORTRAIT else chip("open-source Healenium", SLATE, 40, fw=IW - 0.4)).move_to([0, RT - 0.38, 0])
        top = RT - 0.85                       # region under the label
        rh = top - RB
        if PORTRAIT:
            pc, pw, ph = [0, top - 1.2, 0], IW, 2.4
            sc, sw_, sh_ = [0, RB + 0.9, 0], IW, 1.8
        else:
            pw, ph = 7.0, rh
            pc = [-RX + pw / 2, top - rh / 2, 0]
            sw_, sh_ = 4.8, (rh - 0.25) / 2
            sc = [RX - sw_ / 2, top - sh_ / 2, 0]
        page = card(pw, ph, INK, PAPER, 4).move_to(pc)
        names = ["Close", "Buy", "Help"]
        els = VGroup()
        ew = (pw - 0.8) / 3 if not PORTRAIT else pw - 0.9
        eh = L(1.5, 0.5)
        for n in names:
            c = card(ew - 0.1, eh, INK, PAPER, 3, 0.15)
            t = T(n, L(40, 28))
            t.move_to(c) if not PORTRAIT else t.move_to(c.get_left() + RIGHT * (t.width / 2 + 0.25))
            els.add(VGroup(c, t))
        if PORTRAIT:
            els.arrange(DOWN, buff=0.1)
            els.move_to(page.get_center() + DOWN * 0.3)
        else:
            els.arrange(RIGHT, buff=0.15)
            els.move_to(page.get_center() + DOWN * 0.1)
        loc = tag('id="close-button"', TEAL, L(32, 21), fw=pw - 0.6).move_to(page.get_top() + DOWN * L(0.65, 0.4))
        store = card(sw_, sh_, TEAL, PAPER, 4).move_to(sc)
        store_t = T("saved locator", L(36, 28), TEAL).move_to(store.get_top() + DOWN * 0.4)
        saved = tag('id="close-button"', TEAL, L(30, 20), fw=sw_ - 0.4).move_to(store.get_center() + UP * L(0.15, 0.1))
        self.go(0.05, FadeIn(st), FadeIn(label), rt=0.3)
        self.go(0.5, FadeIn(page), FadeIn(els), FadeIn(loc), rt=0.5)
        self.go(1.8, FadeIn(store), FadeIn(store_t), rt=0.3)
        self.go(2.3, TransformFromCopy(loc, saved), rt=0.7)
        # it breaks (4.07)
        newid = tag('id="btn-4821"', CRIMSON, L(32, 21), fw=pw - 0.6).move_to(loc)
        broke = chip("not found", CRIMSON, L(30, 24)).move_to(store.get_bottom() + UP * L(0.38, 0.3))
        self.go(4.0, Transform(loc, newid), rt=0.3)
        xx = cross(0.25).move_to(saved.get_right() + LEFT * 0.2 + UP * 0.45)
        self.go(4.45, Create(xx), FadeIn(broke), rt=0.3)
        # score the elements (5.08)
        bars = VGroup()
        for i, (e, v) in enumerate(zip(els, [0.92, 0.38, 0.2])):
            wf = e.width - 0.2 if not PORTRAIT else 0.8
            tr = Rectangle(width=wf, height=0.2, stroke_color=LINE, stroke_width=2, fill_opacity=0)
            fl = Rectangle(width=wf * v, height=0.2, stroke_width=0, fill_color=TEAL if i == 0 else LINE, fill_opacity=1).align_to(tr, LEFT)
            g = VGroup(tr, fl)
            if PORTRAIT:
                g.move_to(e.get_right() + LEFT * 0.55)
            else:
                g.next_to(e, DOWN, buff=0.2)
            bars.add(g)
        score_lab = T("score each element", L(38, 28), SOFT).move_to(page.get_bottom() + UP * 0.4)
        if PORTRAIT:
            score_lab.move_to(page.get_top() + DOWN * 0.95).set_opacity(0)
        self.go(5.1, LaggedStart(*[FadeIn(b) for b in bars], lag_ratio=0.3), FadeIn(score_lab), rt=0.8)
        # best match (7.19)
        ring = SurroundingRectangle(els[0], color=TEAL, buff=0.08, stroke_width=7, corner_radius=0.18)
        use = chip("best match", TEAL, L(38, 28)).move_to(score_lab)
        if PORTRAIT:
            use.move_to(els[0].get_right() + LEFT * 0.0).set_opacity(0)
        self.go(7.2, Create(ring), Transform(score_lab, use), rt=0.5)
        # report (9.45): the label turns into the person's job
        rep = card(sw_, sh_, SLATE, PAPER, 5).move_to(sc if PORTRAIT else [sc[0], RB + sh_ / 2, 0])
        rt_ = T("report", L(38, 30), SLATE).move_to(rep.get_top() + DOWN * 0.4)
        rl = VGroup(M("broken: close-button", L(24, 18), CRIMSON), M("healed: btn-4821", L(24, 18), TEAL)).arrange(DOWN, aligned_edge=LEFT, buff=L(0.3, 0.2))
        fit(rl, sw_ - 0.5)
        rl.move_to(rep.get_top() + DOWN * (0.9 + rl.height / 2))
        out = [FadeOut(store), FadeOut(store_t), FadeOut(saved), FadeOut(broke), FadeOut(xx)] if PORTRAIT else []
        self.go(9.4, *out, FadeIn(rep, shift=UP * 0.1), FadeIn(rt_), FadeIn(rl), rt=0.4)
        fix = (pchip if PORTRAIT else chip)("a person fixes the script", SLATE, L(40, 30), fw=IW - 0.4).move_to(label)
        cur = cursor(1.0).move_to(label.get_right() + LEFT * 0.5 + DOWN * 0.45)
        self.go(10.3, Transform(label, fix), FadeIn(cur), rt=0.4)
        self.finish()


# --------------------------------------------------------------------------------------------
@timed("B08")
class B08_VisionAgents(Scene):
    def construct(self):
        if PORTRAIT:
            return self.construct_p()
        st = stage("same popup, two ways")
        if PORTRAIT:
            h1, h2 = 2.2, 2.85
        else:
            h1, h2 = 2.45, 3.1
        c1y = RT - h1 / 2
        c2y = RB + h2 / 2
        lane1 = card(RW, h1, TEAL, PAPER, 4).move_to([0, c1y, 0])
        lane2 = card(RW, h2, SLATE, PAPER, 4).move_to([0, c2y, 0])
        pw1, ph1 = L(3.0, 1.4), L(2.05, 1.25)
        pop1 = popup(pw1, ph1, simple=True).move_to(lane1.get_right() + LEFT * (pw1 / 2 + 0.25) + UP * L(0, 0.15))
        pw2, ph2 = L(3.4, 1.25), L(2.5, 1.2)
        pop2 = popup(pw2, ph2, simple=True).move_to(lane2.get_right() + LEFT * (pw2 / 2 + L(0.6, 0.3)))
        l1_lab = chip("Selenium", TEAL, L(36, 28)).move_to(lane1.get_corner(UL) + np.array([L(1.1, 0.9), -0.45, 0]))
        l2_lab = chip("AI agent", SLATE, L(36, 28)).move_to(lane2.get_corner(UL) + np.array([L(1.0, 0.85), -0.45, 0]))
        l1_say = T("looks for an ID", L(40, 28), TEAL)
        if PORTRAIT:
            fit(l1_say, 1.5)
            l1_say.move_to(lane1.get_left() + RIGHT * (l1_say.width / 2 + 0.2) + UP * 0.1)
            l1_tag = tag('id="close-button"', TEAL, 20, fw=3.2)
            l1_tag.move_to([lane1.get_left()[0] + 0.2 + l1_tag.width / 2, lane1.get_bottom()[1] + 0.38, 0])
            stuck = cross(0.22).next_to(l1_tag, RIGHT, buff=0.25)
        else:
            l1_say.move_to(lane1.get_left() + RIGHT * 2.3 + DOWN * 0.05)
            l1_tag = tag('id="close-button"', TEAL, 28, fw=4.6).next_to(l1_say, DOWN, buff=0.25)
            stuck = cross(0.28).next_to(l1_tag, RIGHT, buff=0.25)
        l2_say = T("looks at a screenshot" if not PORTRAIT else "looks at\na screenshot", L(40, 28), SLATE); fit(l2_say, L(4.4, 1.45))
        l2_say.move_to(lane2.get_left() + RIGHT * (l2_say.width / 2 + 0.3) + UP * L(0.1, 0.15))
        shot = Rectangle(width=pw2 + 0.5, height=ph2 + 0.5, stroke_color=SLATE, stroke_width=5).move_to(pop2)
        corners = VGroup(*[Line(shot.get_corner(c), shot.get_corner(c) + d * 0.4, stroke_color=SLATE, stroke_width=9)
                           for c, d in [(UL, RIGHT), (UR, LEFT), (DL, RIGHT), (DR, LEFT)]])
        self.go(0.05, FadeIn(st), rt=0.3)
        self.go(0.5, FadeIn(lane1), FadeIn(lane2), FadeIn(pop1), FadeIn(pop2), rt=0.5)
        self.go(2.7, FadeIn(l2_lab), rt=0.3)
        ey = eye(L(0.6, 0.5)).move_to(lane2.get_left() + RIGHT * 0.7 + DOWN * L(0.55, 0.9))
        self.go(3.4, FadeIn(ey), rt=0.3)
        self.go(4.7, FadeIn(l1_lab), rt=0.3)
        self.go(7.2, FadeIn(l1_say), FadeIn(l1_tag), rt=0.4)
        self.go(8.0, FadeIn(stuck), rt=0.3)
        self.go(9.3, Create(shot), FadeIn(corners), FadeIn(l2_say), rt=0.4)
        ring = Circle(radius=L(0.42, 0.38), stroke_color=CRIMSON, stroke_width=6).move_to(pop2.x)
        self.go(11.5, Create(ring), rt=0.4)
        cur = cursor(1.0).move_to(pop2.x.get_center() + RIGHT * 0.2 + DOWN * 1.3)
        self.go(13.4, FadeIn(cur), rt=0.2)
        self.go(13.9, cur.animate.move_to(pop2.x.get_center() + RIGHT * 0.2 + DOWN * 0.12), rt=0.5)
        self.go(14.5, FadeOut(pop2), FadeOut(ring), rt=0.25)
        flash = Rectangle(width=shot.width, height=shot.height, stroke_color=SLATE, stroke_width=9, fill_color=PAPER, fill_opacity=0.6).move_to(shot)
        self.go(14.85, FadeIn(flash, rate_func=there_and_back), rt=0.5)
        # the loop (16.32)
        self.go(15.8, *[FadeOut(m) for m in list(self.mobjects) if m is not st], rt=0.25)
        R = L(2.2, 0.95)
        cen = np.array([0, RCY + 0.0, 0])
        names, cols = ["look", "decide", "act", "check"], [TEAL, SLATE, CRIMSON, TEAL]
        nodes = VGroup()
        for i, (n, c) in enumerate(zip(names, cols)):
            ang = PI / 2 - i * PI / 2
            nodes.add(chip(n, c, L(50, 28)).move_to(cen + R * np.array([np.cos(ang) * L(1.6, 1.0), np.sin(ang), 0])))
        ring_c = VGroup(*[Arrow(nodes[i].get_center(), nodes[(i + 1) % 4].get_center(), buff=L(1.0, 0.7), color=LINE, stroke_width=7) for i in range(4)])
        again = T("again and again", L(54, 40), INK); fit(again, R * 1.5)
        again.move_to(cen)
        for n_ in nodes:
            n_.set_opacity(0.4)
        self.go(16.1, Create(ring_c), FadeIn(nodes), rt=0.25)
        for t0, i in [(16.35, 0), (16.7, 1), (17.35, 2), (17.85, 3)]:
            self.go(t0, nodes[i].animate.set_opacity(1), Indicate(nodes[i], scale_factor=1.15), rt=0.25)
        self.go(18.35, FadeIn(again), rt=0.3)
        self.finish()

    def construct_p(self):
        st = stage("two ways", 44, INK)
        pop = ppop(3.3, 2.9, xs=0.65).move_to([0, 0.3, 0])
        lab_ai = pchip("AI agent", SLATE, 44).move_to([0, 2.3, 0])
        lab_se = pchip("Selenium", TEAL, 44).move_to([0, 2.3, 0])
        ey = eye(1.0).move_to([0, -1.95, 0])
        self.go(0.05, FadeIn(st), rt=0.25)
        self.go(0.5, FadeIn(pop), rt=0.6)
        self.go(2.7, FadeIn(lab_ai), rt=0.3)
        self.go(3.4, FadeIn(ey), rt=0.3)
        self.go(4.7, FadeOut(lab_ai), FadeOut(ey), FadeIn(lab_se), rt=0.3)
        say1 = T("looks for an ID", 36, TEAL).move_to([-0.2, -1.7, 0])
        stuck = cross(0.2).next_to(say1, RIGHT, buff=0.2)
        tg = tag('id="close-button"', TEAL, 24, fw=3.3).move_to([0, -2.3, 0])
        self.go(7.2, FadeIn(say1), FadeIn(tg), rt=0.4)
        self.go(8.0, FadeIn(stuck), rt=0.3)
        frame = Rectangle(width=3.6, height=3.15, stroke_color=SLATE, stroke_width=6).move_to(pop.card)
        corners = VGroup(*[Line(frame.get_corner(c), frame.get_corner(c) + d * 0.45, stroke_color=SLATE, stroke_width=11)
                           for c, d in [(UL, RIGHT), (UR, LEFT), (DL, RIGHT), (DR, LEFT)]])
        say2 = T("looks at a\nscreenshot", 40, SLATE).move_to([0, -2.05, 0])
        self.go(9.1, FadeOut(say1), FadeOut(stuck), FadeOut(tg), FadeOut(lab_se), rt=0.15)
        self.go(9.3, FadeIn(lab_ai), Create(frame), FadeIn(corners), FadeIn(say2), rt=0.3)
        ring = Circle(radius=0.55, stroke_color=CRIMSON, stroke_width=7).move_to(pop.x)
        self.go(11.45, Create(ring), rt=0.4)
        cur = cursor(1.2).move_to(pop.x.get_center() + RIGHT * 0.3 + DOWN * 1.0)
        self.go(13.4, FadeIn(cur), rt=0.2)
        self.go(13.9, cur.animate.move_to(pop.x.get_center() + RIGHT * 0.25 + DOWN * 0.15), rt=0.5)
        self.go(14.5, FadeOut(pop), FadeOut(ring), FadeOut(cur), rt=0.25)
        flash = Rectangle(width=3.6, height=3.15, stroke_color=SLATE, stroke_width=9, fill_color=PAPER, fill_opacity=0.6).move_to(frame)
        self.go(14.85, FadeIn(flash, rate_func=there_and_back), rt=0.5)
        # the loop (16.32): four steps stacked, then looped back
        self.go(15.8, *[FadeOut(m) for m in list(self.mobjects) if m is not st], rt=0.25)
        names, cols = ["look", "decide", "act", "check"], [TEAL, SLATE, CRIMSON, TEAL]
        ys = [1.85, 0.75, -0.35, -1.45]
        cards = []
        for n, c, y in zip(names, cols, ys):
            cd = card(2.6, 0.85, c, PAPER, 5, 0.2).move_to([-0.3, y, 0])
            t = T(n, 46, c).move_to(cd)
            cards.append(VGroup(cd, t))
        arrows = [Arrow(cards[i][0].get_bottom(), cards[i + 1][0].get_top(), buff=0.04, color=INK, stroke_width=6, max_tip_length_to_length_ratio=0.5) for i in range(3)]
        p0, p1, p2 = np.array([1.0, -1.45, 0]), np.array([1.5, -1.45, 0]), np.array([1.5, 1.85, 0])
        loop = VGroup(Line(p0, p1, stroke_color=CRIMSON, stroke_width=6), Line(p1, p2, stroke_color=CRIMSON, stroke_width=6),
                      Arrow(p2, np.array([1.0, 1.85, 0]), buff=0, color=CRIMSON, stroke_width=6))
        again = T("again and again", 40, INK).move_to([0, -2.3, 0])
        self.go(16.35, FadeIn(cards[0], scale=0.9), rt=0.25)
        self.go(16.7, GrowArrow(arrows[0]), FadeIn(cards[1], scale=0.9), rt=0.25)
        self.go(17.35, GrowArrow(arrows[1]), FadeIn(cards[2], scale=0.9), rt=0.25)
        self.go(17.85, GrowArrow(arrows[2]), FadeIn(cards[3], scale=0.9), rt=0.25)
        self.go(18.1, Create(loop), rt=0.25)
        self.go(18.4, FadeIn(again), rt=0.3)
        self.finish()


# --------------------------------------------------------------------------------------------
@timed("B09")
class B09_RpaLink(Scene):
    def construct(self):
        if PORTRAIT:
            return self.construct_p()
        st = stage("a desktop")
        if PORTRAIT:
            ww, wh, wc = IW, 2.75, [0, RT - 1.4, 0]
        else:
            ww, wh, wc = 6.6, RH, [-RX + 3.3, RCY, 0]
        win = card(ww, wh, INK, PAPER, 4).move_to(wc)
        wbar = Line(win.get_corner(UL) + DOWN * 0.5, win.get_corner(UR) + DOWN * 0.5, stroke_color=INK, stroke_width=3)
        wdots = VGroup(*[Dot(radius=0.06, color=c) for c in (CRIMSON, GOLD, TEAL)]).arrange(RIGHT, buff=0.1).move_to(win.get_corner(UL) + np.array([0.5, -0.25, 0]))
        ctrl = VGroup()
        for n in ["Open", "Save", "Close"]:
            c = card(L(4.4, 1.1), L(1.2, 0.7), INK, PAPER, 3, 0.15)
            t = T(n, L(38, 30)); t.move_to(c)
            ctrl.add(VGroup(c, t))
        if PORTRAIT:
            ctrl.arrange(RIGHT, buff=0.12)
            fit(ctrl, ww - 0.4)
            ctrl.move_to(win.get_center() + DOWN * 0.3)
        else:
            ctrl.arrange(DOWN, buff=0.35)
            ctrl.move_to(win.get_center() + DOWN * 0.3)
            ctrl.scale(1.0)
        # right column (landscape) / bottom (portrait)
        if PORTRAIT:
            colx, coly, colw = 0, RB + 1.25, IW
        else:
            colx, coly, colw = RX - 2.75, RCY, 5.5
        tag_lab = chip("RPA bot", SLATE, L(40, 30)).move_to([colx, (RT - 0.45) if not PORTRAIT else (RB + 2.0), 0])
        pic = card(L(3.8, 2.4), L(1.5, 0.9), SLATE, PAPER, 5, 0.18)
        pt = T("Close", L(48, 30)); pt.move_to(pic)
        picg = VGroup(pic, pt)
        picg.move_to([colx, (RT - 1.9) if not PORTRAIT else (RB + 1.1), 0])
        pic_lab = T("a picture of the button", L(34, 26), SLATE); fit(pic_lab, colw - 0.3)
        pic_lab.next_to(picg, DOWN, buff=0.2)
        target = ctrl[2]
        match = DashedLine(picg.get_left() if not PORTRAIT else picg.get_top(), target.get_right() if not PORTRAIT else target.get_bottom(), color=SLATE, stroke_width=5)
        ring = SurroundingRectangle(target, color=SLATE, buff=0.08, stroke_width=6, corner_radius=0.18)
        self.go(0.05, FadeIn(st), rt=0.3)
        self.go(0.4, FadeIn(win), FadeIn(wbar), FadeIn(wdots), FadeIn(ctrl), rt=0.5)
        self.go(2.7, FadeIn(tag_lab), rt=0.3)
        self.go(4.45, FadeIn(picg), FadeIn(pic_lab), rt=0.4)
        self.go(6.2, Create(match), Create(ring), rt=0.5)
        cur = cursor(1.2).move_to(target.get_center() + RIGHT * 2.0 + DOWN * 1.1)
        self.go(7.0, FadeIn(cur), cur.animate.move_to(target.get_center() + RIGHT * 1.5 + DOWN * 0.15), rt=0.6)
        code = M('By.id("close")', L(32, 22)); fit(code, colw - 0.4)
        code.next_to(pic_lab, DOWN, buff=0.7 if not PORTRAIT else 0.35)
        nocode = T("not just by their code", L(34, 26), SOFT); fit(nocode, colw - 0.3)
        nocode.next_to(code, DOWN, buff=0.2)
        if PORTRAIT:
            code.set_opacity(0); nocode.set_opacity(0)
        self.go(8.4, FadeIn(code), rt=0.25)
        self.go(8.7, code.animate.set_opacity(0.4), FadeIn(nocode), rt=0.4)
        # the bot decides what to do next (10.22)
        self.go(10.2, FadeOut(code), FadeOut(nocode), FadeOut(match), FadeOut(pic_lab), *([FadeOut(picg), FadeOut(tag_lab)] if PORTRAIT else []), rt=0.3)
        root = Dot(radius=0.14, color=INK)
        if PORTRAIT:
            root.move_to([0, RB + 1.2, 0])
            oc = [[-1.15, RB + 0.45, 0], [0, RB + 0.45, 0], [1.15, RB + 0.45, 0]]
        else:
            root.move_to([colx - 1.9, RB + 1.5, 0])
            oc = [[colx + 1.5, RB + 2.6, 0], [colx + 1.5, RB + 1.5, 0], [colx + 1.5, RB + 0.4, 0]]
        chips, branches = VGroup(), VGroup()
        for n, p in zip(["wait", "retry", "go on"], oc):
            ch = chip(n, SLATE, L(36, 26)).move_to(p)
            chips.add(ch)
            branches.add(Line(root.get_center(), ch.get_left() if not PORTRAIT else ch.get_top(), stroke_color=LINE, stroke_width=6))
        nxt = T("what to do next?", L(38, 28), SLATE).move_to([colx, RB + 3.5 if not PORTRAIT else RB + 2.0, 0]) if not PORTRAIT else VGroup()
        self.go(10.55, FadeIn(root), Create(branches), FadeIn(chips), rt=0.6)
        self.go(12.0, branches[1].animate.set_stroke(TEAL, 9), chips[1][0].animate.set_fill(TEAL), rt=0.4)
        self.go(12.5, chips[0].animate.set_opacity(0.4), chips[2].animate.set_opacity(0.4), rt=0.3)
        self.finish()

    def construct_p(self):
        st = stage("a desktop")
        win = card(3.4, 3.5, INK, PAPER, 4).move_to([0, 0.2, 0])
        wbar = Line(win.get_corner(UL) + DOWN * 0.5, win.get_corner(UR) + DOWN * 0.5, stroke_color=INK, stroke_width=3)
        wdots = VGroup(*[Dot(radius=0.07, color=c) for c in (CRIMSON, GOLD, TEAL)]).arrange(RIGHT, buff=0.12).move_to(win.get_corner(UL) + np.array([0.55, -0.25, 0]))
        btns = VGroup()
        for n, y in zip(["Open", "Save", "Close"], [0.8, -0.05, -0.9]):
            c = card(2.5, 0.7, INK, PAPER, 3, 0.15).move_to([0, y, 0])
            t = T(n, 40); t.move_to(c)
            btns.add(VGroup(c, t))
        w = VGroup(win, wbar, wdots, btns)
        chipb = chip("RPA bot", SLATE, 44).move_to([0, 2.28, 0])
        self.go(0.05, FadeIn(st), rt=0.25)
        self.go(0.4, FadeIn(w), rt=0.5)
        self.go(2.7, FadeIn(chipb), rt=0.3)
        # a picture of the button (4.41)
        self.go(4.4, w.animate.scale(0.55).move_to([0, 0.95, 0]), rt=0.5)
        pic = card(2.4, 1.1, SLATE, PAPER, 5, 0.18).move_to([0, -1.0, 0])
        pt = T("Close", 46, SLATE).move_to(pic)
        picg = VGroup(pic, pt)
        plab = T("a picture of\nthe button", 34, SLATE).move_to([0, -2.05, 0])
        self.go(5.0, FadeIn(picg), FadeIn(plab), rt=0.4)
        target = btns[2]
        match = DashedLine(pic.get_top(), target.get_bottom(), color=SLATE, stroke_width=6)
        ring = SurroundingRectangle(target, color=SLATE, buff=0.06, stroke_width=6, corner_radius=0.12)
        self.go(6.2, Create(match), Create(ring), rt=0.5)
        cur = cursor(1.2).move_to(target.get_center() + RIGHT * 1.3 + DOWN * 0.6)
        self.go(7.0, FadeIn(cur), cur.animate.move_to(target.get_center() + RIGHT * 0.85 + DOWN * 0.15), rt=0.6)
        # not just by their code (8.4)
        cc = card(3.3, 1.0, INK, PAPER, 4).move_to([0, -1.0, 0])
        code = M('By.id("close")', 26); fit(code, 3.0); code.move_to(cc)
        cg = VGroup(cc, code)
        nj = T("not just by\ntheir code", 36, SOFT).move_to([0, -2.05, 0])
        self.go(8.3, FadeOut(picg), FadeOut(plab), FadeOut(match), FadeOut(ring), FadeOut(cur), rt=0.2)
        self.go(8.5, FadeIn(cg), rt=0.2)
        self.go(8.8, cg.animate.set_opacity(0.5), FadeIn(nj), rt=0.4)
        # the bot decides what to do next (10.22)
        self.go(10.2, *[FadeOut(m) for m in list(self.mobjects) if m is not st], rt=0.3)
        q = T("what to do\nnext?", 46, SLATE).move_to([0, 1.7, 0])
        root = Dot(radius=0.16, color=INK).move_to([-1.1, -0.3, 0])
        chips, br = VGroup(), VGroup()
        for n, y in zip(["wait", "retry", "go on"], [0.55, -0.3, -1.15]):
            ch = chip(n, SLATE, 44).move_to([0.7, y, 0])
            chips.add(ch)
            br.add(Line(root.get_center(), ch.get_left(), stroke_color=LINE, stroke_width=7))
        self.go(10.5, FadeIn(q), FadeIn(root), Create(br), FadeIn(chips), rt=0.6)
        self.go(12.0, br[1].animate.set_stroke(TEAL, 10), chips[1][0].animate.set_fill(TEAL), rt=0.4)
        self.go(12.5, chips[0].animate.set_opacity(0.4), chips[2].animate.set_opacity(0.4), rt=0.3)
        self.finish()


# --------------------------------------------------------------------------------------------
@timed("B10")
class B10_WhereAiHelps(Scene):
    def construct(self):
        if PORTRAIT:
            return self.construct_p()
        st = stage("where AI helps")
        stamp = chip("In my experience", CRIMSON, L(46, 28)).move_to([0, RT - L(0.4, 0.33), 0])
        top = RT - L(0.95, 0.7)
        if PORTRAIT:
            ch = (top - RB - 0.2) / 3
            cw = IW
            cpos = [[0, top - ch / 2 - i * (ch + 0.1), 0] for i in range(3)]
        else:
            ch, cw = top - RB, (RW - 0.5) / 3
            cpos = [[-(cw + 0.25) + i * (cw + 0.25), top - ch / 2, 0] for i in range(3)]
        cards = [card(cw, ch, INK, PAPER, 4).move_to(p) for p in cpos]
        heads = ["edge cases", "test documentation", "scripts keep running"]
        hs = []
        for c, h in zip(cards, heads):
            t = T(h, L(40, 26), TEAL); fit(t, cw - 0.4)
            t.move_to(c.get_corner(UL) + np.array([0.25, -0.3, 0]), aligned_edge=LEFT) if PORTRAIT else t.move_to(c.get_top() + DOWN * 0.55)
            hs.append(t)
        self.go(0.05, FadeIn(st), rt=0.3)
        self.go(0.4, LaggedStart(*[FadeIn(c_) for c_ in cards], lag_ratio=0.2), LaggedStart(*[FadeIn(h_) for h_ in hs], lag_ratio=0.2), rt=0.8)
        self.go(2.75, FadeIn(stamp, scale=0.85), rt=0.4)
        # card 1
        rows = VGroup(*[T(s_, L(36, 22)) for s_ in (["valid login", "wrong password", "empty field"] if not PORTRAIT else ["valid login", "wrong password"])]).arrange(DOWN, aligned_edge=LEFT, buff=L(0.4, 0.06))
        new = T("name with an accent", L(36, 22))
        fit(rows, cw - 0.7)
        new.next_to(rows, DOWN, buff=L(0.4, 0.06), aligned_edge=LEFT)
        fit(new, cw - 0.7)
        blk = VGroup(rows, new)
        blk.move_to(cards[0].get_center() + DOWN * L(0.35, 0.27) + (LEFT * 0.5 if PORTRAIT else ORIGIN))
        if PORTRAIT:
            blk.align_to(cards[0], LEFT).shift(RIGHT * 0.45)
        hlbox = Rectangle(width=new.width + 0.3, height=new.height + 0.22, stroke_width=0, fill_color=GOLD, fill_opacity=0.65).move_to(new)
        self.go(4.2, FadeIn(rows), rt=0.5)
        self.go(5.3, FadeIn(hlbox), FadeIn(new, shift=UP * 0.1), rt=0.5)
        # card 2
        doc = lines_block(5 if not PORTRAIT else 3, cw - 1.0, h=0.14, gap=L(0.45, 0.2))
        doc.move_to(cards[1].get_center() + DOWN * L(0.35, 0.2))
        self.go(7.0, LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in doc], lag_ratio=0.25), rt=1.3)
        # card 3
        mini = card(L(3.2, 1.9), L(2.3, 0.62), INK, PAPER, 3, 0.12)
        mb = card(L(1.2, 0.8), L(0.9, 0.4), TEAL, PAPER, 3, 0.1).move_to(mini.get_center() + LEFT * L(0.6, 0.45))
        mg = VGroup(mini, mb).move_to(cards[2].get_center() + UP * L(0.35, -0.25) + (LEFT * 0.6 if PORTRAIT else ORIGIN))
        okbar = Rectangle(width=cw - 1.0 if not PORTRAIT else 0.9, height=0.24, stroke_width=0, fill_color=TEAL, fill_opacity=1)
        okbar.move_to(cards[2].get_bottom() + UP * 0.55) if not PORTRAIT else okbar.move_to(cards[2].get_center() + RIGHT * 1.15 + DOWN * 0.25)
        okl = T("passing", L(34, 20), TEAL).next_to(okbar, UP, buff=0.1)
        self.go(9.7, FadeIn(mg), rt=0.3)
        self.go(10.3, mb.animate.shift(RIGHT * L(1.0, 0.6) + DOWN * 0.1), Create(okbar), FadeIn(okl), rt=0.7)
        self.finish()

    def construct_p(self):
        st = stage("where AI helps")
        stamp = pchip("In my\nexperience", CRIMSON, 38, pad=0.4).move_to([0, 2.12, 0])
        big = card(3.3, 3.95, INK, PAPER, 4).move_to([0, -0.4, 0])
        self.go(0.05, FadeIn(st), rt=0.25)
        self.go(0.4, FadeIn(big), rt=0.4)
        self.go(2.75, FadeIn(stamp, scale=0.85), rt=0.4)
        top = big.get_top()[1]
        # 1: edge cases (4.2)
        h1 = T("edge cases", 44, TEAL).move_to([0, top - 0.5, 0])
        rows = VGroup(*[T(s_, 32) for s_ in ["valid login", "wrong password", "empty field"]]).arrange(DOWN, buff=0.18)
        rows.move_to([0, top - 1.7, 0])
        new = T("name with\nan accent", 32)
        box = Rectangle(width=2.7, height=0.95, stroke_width=0, fill_color=GOLD, fill_opacity=0.65).move_to([0, top - 3.1, 0])
        new.move_to(box)
        self.go(4.2, FadeIn(h1), FadeIn(rows), rt=0.6)
        self.go(5.3, FadeIn(box), FadeIn(new, shift=UP * 0.1), rt=0.5)
        # 2: documentation (6.3)
        h2 = T("test\ndocumentation", 38, TEAL); fit(h2, 3.0); h2.move_to([0, top - 0.85, 0])
        self.go(6.3, FadeOut(h1), FadeOut(rows), FadeOut(box), FadeOut(new), rt=0.3)
        self.go(6.6, FadeIn(h2), rt=0.3)
        doc = lines_block(5, 2.6, h=0.14, gap=0.42).move_to([0, top - 2.6, 0])
        self.go(7.0, LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in doc], lag_ratio=0.25), rt=1.4)
        # 3: scripts keep running (9.16)
        h3 = T("scripts keep\nrunning", 40, TEAL); fit(h3, 3.0); h3.move_to([0, top - 0.85, 0])
        self.go(9.1, FadeOut(h2), FadeOut(doc), rt=0.25)
        self.go(9.4, FadeIn(h3), rt=0.3)
        mini = card(2.6, 1.1, INK, PAPER, 3, 0.12).move_to([0, top - 2.4, 0])
        mb = card(0.9, 0.5, TEAL, PAPER, 3, 0.1).move_to(mini.get_center() + LEFT * 0.7)
        okbar = Rectangle(width=2.6, height=0.26, stroke_width=0, fill_color=TEAL, fill_opacity=1).move_to([0, top - 3.7, 0])
        okl = T("passing", 36, TEAL).move_to([0, top - 3.3, 0])
        self.go(9.7, FadeIn(mini), FadeIn(mb), rt=0.3)
        self.go(10.3, mb.animate.shift(RIGHT * 1.4), Create(okbar), FadeIn(okl), rt=0.7)
        self.finish()


# --------------------------------------------------------------------------------------------
@timed("B11")
class B11_WhereItFails(Scene):
    def construct(self):
        st = stage("where it fails")
        if PORTRAIT:
            pw, ph = RW, (RH - 0.45) / 4
            pos = [[0, RT - ph / 2 - i * (ph + 0.15), 0] for i in range(4)]
        else:
            pw, ph = (RW - 0.25) / 2, (RH - 0.25) / 2
            pos = [[-pw / 2 - 0.125, RT - ph / 2, 0], [pw / 2 + 0.125, RT - ph / 2, 0],
                   [-pw / 2 - 0.125, RB + ph / 2, 0], [pw / 2 + 0.125, RB + ph / 2, 0]]
        panels = [card(pw, ph, LINE, PAPER, 5).move_to(p) for p in pos]   # light border: a dark outline reads as a text blob to Gate T
        heads = ["every run costs money", "different choices each run", "it can make things up", "the wrong button, still green"]
        hs = []
        for p, h in zip(panels, heads):
            t = T(h, L(36, 30)); fit(t, pw - L(0.9, 0.4))
            t.move_to(p.get_corner(UL) + np.array([L(0.4, 0.25), -L(0.55, 0.35), 0]), aligned_edge=LEFT)
            hs.append(t)
        dy = -L(0.3, 0.22)

        def body(i, g):
            g.move_to(panels[i].get_center() + DOWN * (L(0.5, 0.2)))
            return g

        self.go(0.05, FadeIn(st), rt=0.3)
        self.go(0.4, LaggedStart(*[FadeIn(p_) for p_ in panels], lag_ratio=0.15), rt=0.7)
        self.go(1.3, FadeIn(hs[0]), rt=0.3)
        coins = VGroup(*[VGroup(Circle(radius=L(0.38, 0.27), stroke_color=INK, stroke_width=4, fill_color=GOLD, fill_opacity=1), T("$", L(40, 28))) for _ in range(5)])
        for c in coins:
            c[1].move_to(c[0])
        coins.arrange(RIGHT, buff=0.18)
        fit(coins, pw - 0.6)
        body(0, coins)
        self.go(1.7, LaggedStart(*[FadeIn(c, shift=DOWN * 0.3) for c in coins], lag_ratio=0.25), rt=0.9)
        self.go(3.25, FadeIn(hs[1]), rt=0.3)
        rl = (lambda n_: T(f"run {n_}", 34, SOFT)) if not PORTRAIT else (lambda n_: T(str(n_), 40, INK))
        r1 = VGroup(rl(1), chip("clicks Close" if not PORTRAIT else "Close", TEAL, L(34, 26))).arrange(RIGHT, buff=0.3)
        r2 = VGroup(rl(2), chip("clicks Help" if not PORTRAIT else "Help", CRIMSON, L(34, 26))).arrange(RIGHT, buff=0.3)
        both = VGroup(r1, r2).arrange(DOWN if not PORTRAIT else RIGHT, aligned_edge=LEFT if not PORTRAIT else ORIGIN, buff=L(0.22, 0.4))
        fit(both, pw - 0.6)
        body(1, both)
        self.go(3.9, FadeIn(r1), rt=0.3)
        self.go(4.7, FadeIn(r2), rt=0.3)
        self.go(6.05, FadeIn(hs[2]), rt=0.3)
        real = VGroup(card(L(1.8, 1.4), L(1.0, 0.7), INK, PAPER, 3, 0.12), T("Close", L(32, 24)))
        real[1].move_to(real[0])
        gh = RoundedRectangle(corner_radius=0.12, width=real[0].width, height=real[0].height, stroke_color=CRIMSON, stroke_width=4)
        ghost = VGroup(DashedVMobject(gh, num_dashes=24), T("Submit?", L(32, 24), CRIMSON))
        ghost[1].move_to(gh)
        pair = VGroup(real, ghost).arrange(RIGHT, buff=0.5)
        nope = T("no such button", L(34, 24), CRIMSON)
        fit(nope, pw - 0.6)
        if PORTRAIT:
            nope = cross(0.2)
        pgrp = VGroup(pair, nope).arrange(DOWN, buff=0.12) if not PORTRAIT else VGroup(pair, nope).arrange(RIGHT, buff=0.3)
        fit(pgrp, pw - 0.5)
        body(2, pgrp)
        pgrp.shift(UP * L(0.22, 0))
        self.go(6.4, FadeIn(real), rt=0.3)
        self.go(7.0, FadeIn(ghost), FadeIn(nope), rt=0.4)
        self.go(8.5, FadeIn(hs[3]), rt=0.3)
        wrong = VGroup(card(L(1.8, 1.4), L(1.0, 0.7), CRIMSON, PAPER, 5, 0.12), T("Buy", L(36, 28), CRIMSON))
        wrong[1].move_to(wrong[0])
        pas = chip("PASS", TEAL, L(38, 28))
        row = VGroup(wrong, pas).arrange(RIGHT, buff=0.7)
        body(3, row)
        self.go(9.0, FadeIn(wrong), rt=0.3)
        self.go(10.2, FadeIn(pas, scale=0.8), rt=0.3)
        # who checks the AI (11.75)
        self.go(11.7, *[FadeOut(m) for m in list(self.mobjects) if m is not st], rt=0.4)
        ai = card(L(3.0, 2.0), L(1.6, 1.2), SLATE, PAPER, 6, 0.25)
        ait = T("AI", L(84, 56), SLATE); ait.move_to(ai)
        aig = VGroup(ai, ait)
        t1 = T("decides what to test", L(48, 34)); t2 = T("decides it passed", L(48, 34))
        fit(t1, L(5.2, 3.4)); fit(t2, L(5.2, 3.4))
        if PORTRAIT:
            aig.move_to([0, RCY + 0.1, 0]); t1.move_to([0, RT - 0.6, 0]); t2.move_to([0, RCY - 1.35, 0])
            a1 = Arrow(ai.get_top(), t1.get_bottom(), buff=0.12, color=INK, stroke_width=6)
            a2 = Arrow(ai.get_bottom(), t2.get_top(), buff=0.12, color=INK, stroke_width=6)
        else:
            aig.move_to([-3.6, RCY + 0.5, 0]); t1.move_to([3.0, RCY + 1.6, 0]); t2.move_to([3.0, RCY - 0.6, 0])
            a1 = Arrow(ai.get_right(), t1.get_left(), buff=0.15, color=INK, stroke_width=6)
            a2 = Arrow(ai.get_right(), t2.get_left(), buff=0.15, color=INK, stroke_width=6)
        q = T("Who checks the AI?", L(88, 56), CRIMSON); fit(q, IW - 0.4)
        q.move_to([0, RB + (0.8 if not PORTRAIT else 0.7), 0])
        self.go(12.1, FadeIn(aig, scale=0.9), rt=0.3)
        self.go(12.6, GrowArrow(a1), FadeIn(t1), rt=0.4)
        self.go(13.7, GrowArrow(a2), FadeIn(t2), rt=0.4)
        self.go(15.6, FadeIn(q, shift=UP * 0.2), rt=0.4)
        self.finish()
