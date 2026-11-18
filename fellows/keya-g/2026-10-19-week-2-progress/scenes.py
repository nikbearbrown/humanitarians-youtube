"""Manim scenes for "Week 2 Progress" (Keya G.).

One scene per Manim beat in beat_sheet.json:
B01_ThisWeeksVideo   the explainer's title, then the steps behind it: own work, research, script, Claude Code,
                     watching videos, choosing topics (one idea at a time)
B02_ManimRemotion    three failing checks, a frozen render, fixes with the checks left on, a new browser and a timer
B03_Files            a folder with four files: script, beat sheet, fact check, build state
B04_DoneNotPassed    "done" and "pass" are not proof; a pass from old frames; the build state records the real result
B05_LateChange       one edited intro line: only its beat is re-voiced and re-rendered; every other beat stays the same
B06_WhatWasHard      a terminal: a clear prompt, understanding each step, not just approving, still learning
B07_Takeaway         testing agents and Claude Code do the work; the person decides what correct looks like

Simple drawn shapes only, in the same style as the Week 1 and Week 4 progress videos: no photos, no person icons,
no company or tool logos. "Selenium", "Manim", "Remotion" and "Claude Code" appear as plain text or generic drawn
shapes. Any file, folder, frame or terminal shown is drawn, not a screenshot.
Scene length comes from actual_duration_s in beat_sheet.json. The go() times are word timings measured from each
beat's narration audio (faster-whisper), so re-check them if that audio is regenerated.

PORTRAIT: this file is the 16:9 layout. The 9:16 copy is this file with PORTRAIT = True, which re-lays every scene
natively for a 4.5 x 8 frame (nothing is a crop). Edit this file, then re-copy.
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

DUR = {"B01": 21.23, "B02": 19.22, "B03": 13.91, "B04": 12.71, "B05": 11.01, "B06": 12.63, "B07": 6.34}
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


def _lines(text, font, size, color, kw):
    """Manim Text left-aligns the lines of a multi-line string; build each line separately so it is centred."""
    kw.pop("line_spacing", None)
    if "\n" not in text:
        return Text(text, font=font, font_size=size, color=color, **kw)
    rows = [Text(s, font=font, font_size=size, color=color, **kw) for s in text.split("\n")]
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


def card(w, h, color=INK, fill=PAPER, sw=4, r=0.16):
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
@timed("B01")
class B01_ThisWeeksVideo(Scene):
    def construct(self):
        st = STAGE("this week")
        # 1. the title (0 - 3.6)
        lab = T(L("this week's explainer", "this week's\nexplainer"), L(44, 40))
        title = T(L("Will AI Replace\nMy Test Scripts?", "Will AI\nReplace\nMy Test\nScripts?"), L(84, 58), line_spacing=0.9)
        uline = Line(LEFT * L(3.2, 1.3), RIGHT * L(3.2, 1.3), stroke_color=CRIMSON, stroke_width=9)
        p1 = VGroup(lab, title, uline).arrange(DOWN, buff=0.4)
        fit(p1, RW - 0.6, RH - 0.2)
        p1.move_to([0, RCY, 0])
        self.go(0.05, FadeIn(st), rt=0.25)
        self.go(0.3, FadeIn(p1, shift=UP * 0.1), rt=0.5)
        self.go(3.5, FadeOut(p1), rt=0.25)
        # 2. my own work: Selenium tests (3.94)
        code = VGroup(card(L(5.2, 3.1), L(3.1, 2.3), INK, PAPER, 4))
        code.add(lines_block(5, code[0].width - 0.7, h=0.15, gap=0.3).move_to(code[0]))
        own_h = T("my own work", L(60, 48))
        own_s = T("Selenium tests", L(48, 44), TEAL)
        own_t = VGroup(own_h, own_s).arrange(DOWN, buff=0.3)
        own = lay([code, own_t], buff=L(0.9, 0.6))
        self.go(3.94, FadeIn(code, shift=UP * 0.1), FadeIn(own_h), rt=0.4)
        self.go(5.1, FadeIn(own_s), rt=0.4)
        self.go(6.95, FadeOut(own), rt=0.25)
        # 3. researched: locators and AI testing agents (7.2)
        r1 = VGroup(target(L(0.7, 0.55)), T("self-healing\nlocators", L(50, 42), line_spacing=0.9)).arrange(DOWN, buff=0.25)
        r2 = VGroup(eye(L(1.6, 1.2)), T("AI testing\nagents", L(50, 42), line_spacing=0.9)).arrange(DOWN, buff=0.25)
        head = T("I researched", L(54, 44))
        res = VGroup(head, lay([r1, r2], buff=L(1.6, 0.5), h=RH - 1.0)).arrange(DOWN, buff=L(0.5, 0.3)) if not PORTRAIT \
            else lay([r1, r2], buff=0.5)
        if not PORTRAIT:
            fit(res, RW - 0.6, RH - 0.2)
            res.move_to([0, RCY, 0])
            head = res[0]
            r1, r2 = res[1][0], res[1][1]
        self.go(7.2, *([FadeIn(head)] if not PORTRAIT else []), rt=0.3)
        self.go(7.5, FadeIn(r1, shift=UP * 0.1), rt=0.4)
        self.go(9.2, FadeIn(r2, shift=UP * 0.1), rt=0.4)
        self.go(10.7, FadeOut(res if not PORTRAIT else VGroup(r1, r2)), rt=0.2)
        # 4. wrote the script, built with Claude Code (10.94)
        sd = doc(L(3.0, 2.6), L(1.9, 1.5), 4)
        sdt = T("wrote the script", L(46, 40))
        sc = VGroup(sd, sdt).arrange(DOWN, buff=0.25)
        tm = term(L(3.4, 2.9), L(3.0, 1.7), 3)
        tmt = T("built with\nClaude Code", L(46, 40), line_spacing=0.9)
        tc = VGroup(tm, tmt).arrange(DOWN, buff=0.25)
        both = lay([sc, tc], buff=L(1.0, 0.55))
        self.go(10.94, FadeIn(both[0], shift=UP * 0.1), rt=0.4)
        self.go(12.14, FadeIn(both[1], shift=UP * 0.1), rt=0.4)
        self.go(14.5, FadeOut(both), rt=0.25)
        # 5. checked some Brutalist videos (14.78)
        pl = player(L(6.0, 3.1), L(3.1, 2.2))
        plt = T("checked Brutalist videos", L(50, 44))
        if PORTRAIT:
            plt = T("checked\nBrutalist\nvideos", 46, line_spacing=0.9)
        pv = lay([pl, plt], buff=L(0.9, 0.45))
        tk = tick(0.4, TEAL, 9).move_to(pl[0].get_corner(UR) + np.array([-0.55, -0.55, 0]))
        self.go(14.78, FadeIn(pv, shift=UP * 0.1), rt=0.4)
        self.go(15.8, Create(tk), rt=0.3)
        self.go(16.5, FadeOut(VGroup(pv, tk)), rt=0.2)
        # 6. topics that matter to me and that I'm interested in (16.66)
        cards = VGroup(*[doc(L(3.2, 2.2), L(3.0, 1.2), 3) for _ in range(3)])
        cards.arrange(DOWN if PORTRAIT else RIGHT, buff=L(0.5, 0.3))
        fit(cards, RW - 0.6, RH - L(1.7, 1.9))
        cards.move_to([0, RCY + L(0.7, 0.9), 0])
        st1 = star(L(0.42, 0.32)).move_to(cards[0].get_corner(UR) + np.array([-0.35, -0.35, 0]))
        st2 = star(L(0.42, 0.32)).move_to(cards[2].get_corner(UR) + np.array([-0.35, -0.35, 0]))
        l1 = pchip("matter to me", TEAL, L(44, 40))
        l2 = pchip("interested in", CRIMSON, L(44, 40))
        lab_row = VGroup(l1, l2).arrange(DOWN if PORTRAIT else RIGHT, buff=0.3)
        lab_row.move_to([0, RB + (0.95 if PORTRAIT else 0.55), 0]) if not PORTRAIT else lab_row.move_to([0, RB + 0.85, 0])
        self.go(16.66, FadeIn(cards, lag_ratio=0.2), rt=0.5)
        self.go(18.9, FadeIn(st1), FadeIn(l1), rt=0.3)
        self.go(20.2, FadeIn(st2), FadeIn(l2), rt=0.3)
        self.finish()


@timed("B02")
class B02_ManimRemotion(Scene):
    def construct(self):
        st = STAGE("the checks")
        cw, ch = L(3.7, 3.3), L(3.0, 2.8)
        s_ = L(1.2, 1.0)

        def prob(icon, label):
            c = card(cw, ch, LINE, PAPER, 5)
            tt = T(label, L(40, 44))
            fit(tt, cw - 0.3)
            icon.scale(s_).move_to(c.get_center() + UP * L(0.45, 0.55))
            tt.move_to(c.get_bottom() + UP * L(0.6, 0.75))
            return VGroup(c, icon, tt)

        ic1 = VGroup(term(1.6, 1.2, 2), cross(0.22).move_to([0.8, 0.6, 0]))
        ic2 = VGroup(Rectangle(width=1.7, height=1.25, stroke_color=INK, stroke_width=4, fill_color=PAPER, fill_opacity=1),
                     DashedVMobject(Rectangle(width=1.35, height=0.95, stroke_color=LINE, stroke_width=4), num_dashes=16),
                     RoundedRectangle(corner_radius=0.04, width=1.0, height=0.14, stroke_width=0, fill_color=CRIMSON,
                                      fill_opacity=1).shift(RIGHT * 0.75 + UP * 0.15))
        ic3 = VGroup(Rectangle(width=1.7, height=1.25, stroke_color=INK, stroke_width=4, fill_color=PAPER, fill_opacity=1),
                     Dot(radius=0.08, color=INK).shift(LEFT * 0.45 + UP * 0.3))
        pcs = VGroup(prob(ic1, "code that\nwouldn't run"), prob(ic2, "labels outside\nthe safe area"),
                     prob(ic3, "frames that were\ntoo empty"))
        head = T(L("my Manim scenes kept failing the quality checks", "my Manim\nscenes kept\nfailing"), L(46, 44))
        if PORTRAIT:
            blk = VGroup(head, pcs[0]).arrange(DOWN, buff=0.7)
            fit(blk, RW - 0.4, RH - 0.1)
            blk.move_to([0, RCY, 0])
            pcs[1].move_to(pcs[0])
            pcs[2].move_to(pcs[0])
        else:
            pcs.arrange(RIGHT, buff=0.4)
            blk = VGroup(head, pcs).arrange(DOWN, buff=0.5)
            fit(blk, RW - 0.4, RH - 0.1)
            blk.move_to([0, RCY, 0])
        self.go(0.05, FadeIn(st), rt=0.25)
        self.go(1.1, FadeIn(head), rt=0.4)
        self.go(4.0, FadeIn(pcs[0], shift=UP * 0.1), rt=0.4)
        if PORTRAIT:
            self.go(5.6, FadeOut(pcs[0]), FadeIn(pcs[1], shift=UP * 0.1), rt=0.4)
            self.go(7.5, FadeOut(pcs[1]), FadeIn(pcs[2], shift=UP * 0.1), rt=0.4)
            self.go(9.7, FadeOut(VGroup(head, pcs[2])), rt=0.2)
        else:
            self.go(5.6, FadeIn(pcs[1], shift=UP * 0.1), rt=0.4)
            self.go(7.5, FadeIn(pcs[2], shift=UP * 0.1), rt=0.4)
            self.go(9.7, FadeOut(blk), rt=0.2)
        # 2. Remotion froze for over an hour (9.86)
        bar_bg = RoundedRectangle(corner_radius=0.18, width=L(5.2, 2.9), height=0.5, stroke_color=INK, stroke_width=4,
                                  fill_color=PAPER, fill_opacity=1)
        bar_fg = RoundedRectangle(corner_radius=0.18, width=L(5.2, 2.9) * 0.55, height=0.5, stroke_width=0,
                                  fill_color=TEAL, fill_opacity=1).align_to(bar_bg, LEFT)
        stuck = cross(0.28).next_to(bar_bg, RIGHT, buff=0.1) if not PORTRAIT else cross(0.28).next_to(bar_bg, DOWN, buff=0.2)
        bar = VGroup(bar_bg, bar_fg)
        bl = T(L("a Remotion render", "a Remotion\nrender"), L(46, 42))
        barg = VGroup(bar, bl).arrange(DOWN, buff=0.3)
        stuck.next_to(bar_bg, UP, buff=0.15).align_to(bar_bg, RIGHT) if False else None
        ck = clock(L(1.1, 0.95), INK, (0.0, 0.85))
        ckl = T("frozen for\nover an hour", L(46, 40), line_spacing=0.9)
        ckg = VGroup(ck, ckl).arrange(DOWN, buff=0.3)
        fz = lay([barg, ckg], buff=L(1.2, 0.8))
        self.go(9.86, FadeIn(barg, shift=UP * 0.1), rt=0.4)
        self.go(11.4, FadeIn(ckg, shift=UP * 0.1), rt=0.4)
        self.go(12.8, FadeOut(fz), rt=0.2)
        # 3. fixed each scene, the checks stay on (12.96)
        fixed = VGroup(*[VGroup(card(L(1.9, 0.8), L(1.0, 0.95), TEAL, PAPER, 5),
                                tick(L(0.4, 0.28), TEAL, 8)) for _ in range(3)])
        for f in fixed:
            f[1].move_to(f[0])
        fixed.arrange(RIGHT, buff=L(0.5, 0.15))
        fl = T(L("fixed each scene", "fixed each\nscene"), L(52, 44))
        pw_ = L(2.2, 1.25)
        pill_on = VGroup(RoundedRectangle(corner_radius=0.35, width=pw_, height=0.7, stroke_width=0,
                                          fill_color=TEAL, fill_opacity=1))
        knob = Circle(radius=0.27, stroke_width=0, fill_color=PAPER, fill_opacity=1).move_to(
            pill_on[0].get_right() + LEFT * 0.4)
        sw_on = VGroup(pill_on, knob)
        off = VGroup(RoundedRectangle(corner_radius=0.35, width=pw_, height=0.7, stroke_color=LINE,
                                      stroke_width=5, fill_color=PAPER, fill_opacity=1))
        off.add(Circle(radius=0.27, stroke_width=0, fill_color=LINE, fill_opacity=1).move_to(off[0].get_left() + RIGHT * 0.4))
        off.add(cross(0.3).move_to(off[0]))
        if PORTRAIT:
            sw_lab = T("checks\nstay on", 44)
            pills = VGroup(sw_on, off).arrange(RIGHT, buff=0.3)
            sw_g = VGroup(pills, sw_lab).arrange(DOWN, buff=0.3)
            off_g = off
            sw_row = sw_g
        else:
            sw_lab = T("checks stay on", 46)
            sw_g = VGroup(sw_on, sw_lab).arrange(DOWN, buff=0.3)
            off_g = VGroup(off, T("off", 46)).arrange(DOWN, buff=0.3)
            sw_row = VGroup(sw_g, off_g).arrange(RIGHT, buff=1.2)
        fx = VGroup(VGroup(fixed, fl).arrange(DOWN, buff=0.3), sw_row).arrange(DOWN, buff=L(0.7, 0.5))
        fit(fx, RW - 0.6, RH - 0.1)
        fx.move_to([0, RCY, 0])
        self.go(12.96, FadeIn(fx[0], shift=UP * 0.1), rt=0.4)
        self.go(14.3, FadeIn(sw_on), FadeIn(sw_lab), rt=0.4)
        self.go(14.9, FadeIn(off_g, shift=UP * 0.1), rt=0.4)
        self.go(15.75, FadeOut(fx), rt=0.15)
        # 4. a different browser and a time limit (15.9)
        def browser(color):
            c = card(L(2.3, 1.55), L(1.0, 0.85), INK, PAPER, 4)
            b = Line(c.get_corner(UL) + DOWN * 0.3, c.get_corner(UR) + DOWN * 0.3, stroke_color=INK, stroke_width=3)
            d = VGroup(*[Dot(radius=0.05, color=col) for col in (CRIMSON, GOLD, color)]).arrange(RIGHT, buff=0.1)
            d.move_to(c.get_corner(UL) + np.array([0.4, -0.15, 0]))
            ad = RoundedRectangle(corner_radius=0.05, width=L(1.5, 0.6), height=0.14, stroke_width=0, fill_color=LINE,
                                  fill_opacity=1).move_to(c.get_center() + DOWN * 0.2)
            return VGroup(c, b, d, ad)
        b1, b2 = browser(TEAL), browser(SLATE)
        arr = Arrow(LEFT * L(0.4, 0.2), RIGHT * L(0.4, 0.2), buff=0, color=INK, stroke_width=6)
        brow = VGroup(b1, arr, b2).arrange(RIGHT, buff=0.25)
        bl2 = T(L("a different browser", "a different\nbrowser"), L(46, 44))
        bg = VGroup(brow, bl2).arrange(DOWN, buff=0.3)
        ring = VGroup(Circle(radius=L(0.95, 0.8), stroke_color=LINE, stroke_width=9),
                      Arc(radius=L(0.95, 0.8), start_angle=PI / 2, angle=-TAU * 0.6, stroke_color=CRIMSON, stroke_width=9),
                      Line(ORIGIN, UP * L(0.6, 0.5), stroke_color=INK, stroke_width=5))
        tl = T("a time limit", L(46, 42))
        tg = VGroup(ring, tl).arrange(DOWN, buff=0.3)
        fin = lay([bg, tg], buff=L(1.4, 0.7))
        self.go(15.95, FadeIn(bg, shift=UP * 0.1), rt=0.3)
        self.go(18.1, FadeIn(tg, shift=UP * 0.1), rt=0.35)
        self.finish()


@timed("B03")
class B03_Files(Scene):
    def construct(self):
        st = STAGE("the files")
        w, h = L(5.6, 3.3), L(2.4, 1.12)

        def slot(pos):
            return DashedVMobject(RoundedRectangle(corner_radius=0.16, width=w, height=h, stroke_color=LINE, stroke_width=5),
                                  num_dashes=28).move_to(pos)

        def file_card(icon, label):
            c = card(w, h, INK, PAPER, 4)
            t = T(label, L(52, 44))
            if PORTRAIT:
                icon.move_to(c.get_left() + RIGHT * 0.8)
                t.move_to(c.get_center() + RIGHT * 0.65)
            else:
                icon.move_to(c.get_left() + RIGHT * 1.0)
                t.move_to(c.get_center() + RIGHT * 0.7)
            fit(t, w - L(2.4, 1.9))
            return VGroup(c, icon, t)

        ic_script = lines_block(4, L(1.2, 0.9), h=0.12, gap=0.2)
        tl = clock(L(0.42, 0.34), INK, (0.0, 0.3))
        cl = VGroup(RoundedRectangle(corner_radius=0.05, width=L(0.55, 0.42), height=0.4, stroke_color=INK, stroke_width=4),
                    Arrow(LEFT * 0.12, RIGHT * 0.12, buff=0, color=INK, stroke_width=4, max_tip_length_to_length_ratio=0.9),
                    RoundedRectangle(corner_radius=0.05, width=L(0.55, 0.42), height=0.4, stroke_color=TEAL, stroke_width=4)
                    ).arrange(RIGHT, buff=0.08)
        bd = VGroup(Circle(radius=L(0.4, 0.34), stroke_color=TEAL, stroke_width=5), tick(L(0.2, 0.17), TEAL, 6))
        icons = [ic_script, tl, cl, bd]
        labels = ["script", "beat sheet", "fact check", "build state"]
        if PORTRAIT:
            pos = [[0, RT - 0.6 - i * (h + 0.22), 0] for i in range(4)]
        else:
            pos = [[-w / 2 - 0.2, RT - 1.25, 0], [w / 2 + 0.2, RT - 1.25, 0], [-w / 2 - 0.2, RB + 1.45, 0], [w / 2 + 0.2, RB + 1.45, 0]]
        slots = VGroup(*[slot(p) for p in pos])
        files = [file_card(i_, l_).move_to(p) for i_, l_, p in zip(icons, labels, pos)]
        # re-centre icons after the card moved (they were placed relative to the card at the origin)
        self.go(0.05, FadeIn(st), rt=0.25)
        self.go(0.4, FadeIn(slots, lag_ratio=0.15), rt=0.6)
        self.go(3.45, FadeOut(slots[0]), FadeIn(files[0], shift=UP * 0.1), rt=0.35)
        self.go(5.5, FadeOut(slots[1]), FadeIn(files[1], shift=UP * 0.1), rt=0.35)
        self.go(7.85, FadeOut(slots[2]), FadeIn(files[2], shift=UP * 0.1), rt=0.35)
        self.go(10.8, FadeOut(slots[3]), FadeIn(files[3], shift=UP * 0.1), rt=0.35)
        self.go(12.9, files[3][1][1].animate.set_color(TEAL), Indicate(files[3][1], color=TEAL, scale_factor=1.15), rt=0.4)
        self.finish()


@timed("B04")
class B04_DoneNotPassed(Scene):
    def construct(self):
        st = STAGE("done is not passed")
        # 1. a command says done, or pass: that is not proof (1.9)
        tw, th = L(6.4, 3.0), L(3.0, 3.3)
        tm = term(tw, th, 0)
        tm.move_to([0, RCY + L(0.35, 0.9), 0])
        l1 = M("done", L(54, 46), INK).next_to(tm[2], RIGHT, buff=0.3)
        l2 = M("pass", L(54, 46), INK).next_to(l1, DOWN, buff=0.4, aligned_edge=LEFT)
        nope = VGroup(RoundedRectangle(corner_radius=0.14, width=L(3.0, 2.5), height=0.9, stroke_color=CRIMSON, stroke_width=6,
                                       fill_color=PAPER, fill_opacity=1))
        nt = T("not proof", L(50, 44)).move_to(nope)
        nope.add(nt)
        nope.move_to([0, RB + 0.8 + L(0.1, 0.25), 0])
        self.go(0.05, FadeIn(st), rt=0.25)
        self.go(1.7, FadeIn(tm, shift=UP * 0.1), rt=0.4)
        self.go(2.65, FadeIn(l1), rt=0.25)
        self.go(3.75, FadeIn(l2), rt=0.25)
        self.go(4.55, FadeIn(nope, scale=0.9), rt=0.3)
        self.go(5.35, FadeOut(VGroup(tm, l1, l2, nope)), rt=0.2)
        # 2. a pass that came from old frames (5.6)
        fw, fh = L(3.2, 2.5), L(1.9, 1.5)
        frs = VGroup(*[card(fw, fh, INK, PAPER, 4).set_opacity(1) for _ in range(3)])
        for i, f in enumerate(frs):
            f.shift(RIGHT * 0.35 * i + DOWN * 0.3 * i)
            f.set_stroke(opacity=1 - 0.2 * (2 - i))
        frs.move_to([0, RCY + L(0.5, 0.9), 0])
        stamp = VGroup(RoundedRectangle(corner_radius=0.12, width=L(2.1, 1.7), height=0.85, stroke_color=TEAL, stroke_width=6,
                                        fill_color=PAPER, fill_opacity=1))
        stamp.add(T("PASS", L(50, 44), TEAL).move_to(stamp[0]))
        stamp.move_to(frs[2].get_center())
        ol = T("old frames", L(54, 48))
        ol.move_to([0, RB + 0.75, 0])
        self.go(5.5, FadeIn(frs, lag_ratio=0.2), rt=0.3)
        self.go(5.85, FadeIn(stamp, scale=0.9), rt=0.25)
        self.go(6.9, FadeIn(ol), rt=0.3)
        self.go(8.0, FadeOut(VGroup(frs, stamp, ol)), rt=0.2)
        # 3. build-state.json records the real result (8.3)
        bw, bh = L(5.0, 3.0), L(2.8, 2.5)
        bs = card(bw, bh, INK, PAPER, 5)
        nm = M("build-state\n.json", L(48, 38), INK, line_spacing=0.9)
        nm.move_to(bs.get_center() + UP * 0.2)
        fit(nm, bw - 0.6)
        eye_i = eye(L(1.4, 1.2)).move_to([0, RT - 0.75, 0])
        bsg = VGroup(bs, nm)
        bsg.move_to([0, RCY + L(-0.1, 0.1), 0])
        eye_i.move_to(bs.get_top() + UP * 0.8)
        badge = VGroup(Circle(radius=L(0.5, 0.45), stroke_color=TEAL, stroke_width=7, fill_color=PAPER, fill_opacity=1))
        badge.add(tick(L(0.25, 0.22), TEAL, 8).move_to(badge[0]))
        rr = T(L("real result", "real\nresult"), L(52, 46))
        res = VGroup(badge, rr).arrange(RIGHT, buff=0.3)
        res.move_to([0, RB + L(0.8, 0.7), 0])
        self.go(8.25, FadeIn(bsg, shift=UP * 0.1), rt=0.4)
        self.go(8.7, FadeIn(eye_i, shift=DOWN * 0.1), rt=0.3)
        self.go(10.95, FadeIn(res, shift=UP * 0.1), rt=0.35)
        self.finish()


@timed("B05")
class B05_LateChange(Scene):
    def construct(self):
        st = STAGE("a late change")
        # one edited intro line (0.3)
        iw, ih = L(4.6, 3.2), L(2.4, 1.3)
        intro = doc(iw, ih, 3)
        intro_l = T("intro line", L(46, 40))
        intro_g = VGroup(intro, intro_l).arrange(DOWN, buff=0.25)
        edit = Line(LEFT * (iw / 2 - 0.5), RIGHT * (iw / 2 - 0.5), stroke_color=CRIMSON, stroke_width=9)
        # grid of beat blocks: 14 of them, the first is the intro
        n_c = 7
        bsz = L(0.62, 0.38)
        gap = L(0.14, 0.08)
        blocks = VGroup(*[RoundedRectangle(corner_radius=0.06, width=bsz, height=bsz, stroke_color=TEAL, stroke_width=4,
                                           fill_color=PAPER, fill_opacity=1) for _ in range(14)])
        for i, b in enumerate(blocks):
            r, c = divmod(i, n_c)
            b.move_to([(c - (n_c - 1) / 2) * (bsz + gap), -r * (bsz + gap), 0])
        if PORTRAIT:
            intro_g.move_to([0, RT - 1.0, 0])
            ck = clock(0.32, INK, (0.0, 0.3)).move_to([-1.25, RT - 2.75, 0])
            tbar = Line([-0.7, RT - 2.75, 0], [1.4, RT - 2.75, 0], stroke_color=LINE, stroke_width=9)
            blocks.move_to([0, RT - 3.55, 0])
            chip1_pos = [0, RB + 0.85, 0]
            chip2_pos = [0, RB + 0.2, 0]
        else:
            intro_g.move_to([-3.1, RCY + 0.85, 0])
            ck = clock(0.42, INK, (0.0, 0.3)).move_to([-5.0, RB + 1.0, 0])
            tbar = Line([-4.4, RB + 1.0, 0], [-1.6, RB + 1.0, 0], stroke_color=LINE, stroke_width=9)
            blocks.move_to([2.9, RCY + 0.9, 0])
            chip1_pos = [1.9, RB + 1.25, 0]
            chip2_pos = [4.6, RB + 1.25, 0]
        knob = Dot(radius=0.12, color=CRIMSON).move_to(tbar.get_start())
        edit.move_to(intro[1][0].get_center())
        clk_l = T("the narration is the clock", 34).next_to(tbar, DOWN, buff=0.2).align_to(tbar, LEFT) if not PORTRAIT else None
        c1 = pchip("new audio", CRIMSON, L(44, 40)).move_to(chip1_pos)
        c2 = pchip("new render", CRIMSON, L(44, 40)).move_to(chip2_pos)
        ticks = VGroup(*[tick(L(0.18, 0.11), TEAL, 5).move_to(b) for b in blocks[1:]])
        same = T(L("the rest stays the same", "the rest\nstays the same"), L(40, 40), line_spacing=0.9)
        same.move_to([0, RB + 0.6, 0] if PORTRAIT else [3.2, RB + 0.8, 0])
        fit(same, RW - 0.6)
        self.go(0.05, FadeIn(st), rt=0.25)
        self.go(0.3, FadeIn(intro_g, shift=UP * 0.1), rt=0.4)
        self.go(1.1, Create(edit), rt=0.4)
        self.go(3.2, FadeIn(ck), Create(tbar), FadeIn(knob), *([FadeIn(clk_l)] if clk_l is not None else []), rt=0.4)
        self.go(3.75, knob.animate.move_to(tbar.get_end()), rt=0.9)
        self.go(4.85, FadeIn(blocks, lag_ratio=0.05), rt=0.5)
        self.go(5.6, blocks[0].animate.set_stroke(CRIMSON, 7).set_fill(interpolate_color(ManimColor(PAPER), ManimColor(CRIMSON), 0.35)),
                rt=0.01)
        self.go(6.15, FadeIn(c1, shift=UP * 0.1), rt=0.35)
        self.go(7.5, FadeIn(c2, shift=UP * 0.1), rt=0.35)
        self.go(8.45, FadeOut(c1), FadeOut(c2), rt=0.2)
        self.go(8.7, FadeIn(ticks, lag_ratio=0.06), FadeIn(same), rt=0.5)
        self.finish()


@timed("B06")
class B06_WhatWasHard(Scene):
    def construct(self):
        st = STAGE("in the terminal")
        tw, th = L(9.4, 3.3), L(5.0, 4.9)
        tm = term(tw, th, 0)
        tm.move_to([0, RCY, 0])
        tm[0].set_stroke(INK, 5)
        top = tm[0].get_top()[1]
        self.go(0.05, FadeIn(st), rt=0.25)
        self.go(0.3, FadeIn(tm, shift=UP * 0.1), rt=0.45)
        # a clear prompt: what I expect (4.1)
        pr_bars = lines_block(2, L(5.4, 2.4), h=0.16, gap=0.3).move_to([L(-0.6, 0.0), top - L(1.6, 1.3), 0])
        pr_c = pchip("what I expect", TEAL, L(46, 36)).move_to([0, top - L(2.8, 3.6), 0])
        ptg = target(L(0.5, 0.42)).next_to(pr_c, LEFT, buff=0.3) if not PORTRAIT else target(0.42).move_to([0, top - 2.45, 0])
        pr = VGroup(pr_bars, pr_c, ptg)
        self.go(4.0, FadeIn(pr_bars, shift=UP * 0.1), rt=0.35)
        self.go(4.6, FadeIn(pr_c), FadeIn(ptg), rt=0.35)
        # understand each step (6.0)
        steps = VGroup(*[VGroup(RoundedRectangle(corner_radius=0.1, width=L(4.2, 2.1), height=L(0.62, 0.55), stroke_color=INK,
                                                  stroke_width=4, fill_color=PAPER, fill_opacity=1),
                                tick(0.2, TEAL, 7)) for _ in range(3)])
        for s_ in steps:
            s_[1].move_to(s_[0].get_left() + RIGHT * 0.4)
        steps.arrange(DOWN, buff=L(0.2, 0.15)).move_to([L(-0.6, -0.4), top - L(2.15, 2.2), 0])
        ey = eye(L(1.1, 0.55)).move_to([L(3.3, 1.1), top - L(2.35, 2.2), 0])
        ul = pchip("understand each step", TEAL, L(44, 38), fw=tw - 0.8).move_to([0, top - L(4.2, 4.3), 0])
        if PORTRAIT:
            ul = pchip("understand\neach step", TEAL, 38).move_to([0, top - 3.95, 0])
        self.go(5.75, FadeOut(pr), rt=0.2)
        self.go(6.0, FadeIn(steps, lag_ratio=0.2), rt=0.25)
        self.go(7.0, FadeIn(ul), FadeIn(ey), rt=0.35)
        # not just approving (8.6)
        ap = VGroup(card(L(3.0, 2.4), L(0.9, 0.9), INK, PAPER, 5), T("Approve", L(48, 42)))
        ap[1].move_to(ap[0])
        ap_x = cross(L(0.35, 0.3)).move_to(ap[0].get_corner(UR) + np.array([0.05, 0.05, 0]))
        apg = VGroup(ap, ap_x).move_to([0, top - 2.7, 0])
        apg.shift(LEFT * ap.get_center()[0])
        self.go(8.35, FadeOut(VGroup(steps, ul, ey)), rt=0.2)
        self.go(8.6, FadeIn(ap, scale=0.95), rt=0.3)
        self.go(9.2, Create(ap_x), rt=0.3)
        # still learning (10.2)
        pb = RoundedRectangle(corner_radius=0.18, width=L(5.0, 2.7), height=0.5, stroke_color=INK, stroke_width=4,
                              fill_color=PAPER, fill_opacity=1)
        pf = RoundedRectangle(corner_radius=0.18, width=L(5.0, 2.7) * 0.3, height=0.5, stroke_width=0,
                              fill_color=TEAL, fill_opacity=1).align_to(pb, LEFT)
        pl_t = T("week two: still learning", L(46, 36)) if not PORTRAIT else T("week two:\nstill learning", 40, line_spacing=0.9)
        pg = VGroup(VGroup(pb, pf), pl_t).arrange(DOWN, buff=0.3).move_to([0, top - 2.7, 0])
        self.go(9.95, FadeOut(VGroup(ap, ap_x)), rt=0.2)
        self.go(10.2, FadeIn(pg, shift=UP * 0.1), rt=0.35)
        self.finish()


@timed("B07")
class B07_Takeaway(Scene):
    def construct(self):
        st = STAGE("the takeaway")
        cw, ch = L(3.8, 3.3), L(3.4, 1.45)
        # testing agents: look, act, check
        def stepchip(txt):
            return pchip(txt, TEAL, L(38, 34), pad=0.3)
        loop = VGroup(stepchip("look"), stepchip("act"), stepchip("check")).arrange(RIGHT, buff=0.15)
        fit(loop, cw - 0.4)
        c1 = card(cw, L(3.4, 1.3), INK, PAPER, 4)
        t1 = T("testing agents", L(44, 40))
        g1 = VGroup(c1, VGroup(loop, t1).arrange(DOWN, buff=0.25).move_to(c1))
        # Claude Code does the work
        tm = term(L(1.7, 1.1), L(1.1, 0.9), 0)
        tm.add(lines_block(2, L(1.1, 0.6), h=0.1, gap=0.16).move_to(tm[0].get_center() + DOWN * 0.15))
        t2 = T(L("Claude Code\ndoes the work", "Claude\nCode does\nthe work"), L(42, 40), line_spacing=0.9)
        c2 = card(cw, L(3.4, 2.5), INK, PAPER, 4)
        if PORTRAIT:
            chev = VMobject(stroke_color=TEAL, stroke_width=7).set_points_as_corners(
                [[-0.12, 0.16, 0], [0.1, 0, 0], [-0.12, -0.16, 0]])
            inner2 = VGroup(chev, t2).arrange(DOWN, buff=0.12).move_to(c2)
        else:
            inner2 = VGroup(tm, t2).arrange(DOWN, buff=0.25).move_to(c2)
        g2 = VGroup(c2, inner2)
        # I decide what correct looks like
        ey = eye(L(1.0, 0.55))
        ck = tick(L(0.3, 0.2), TEAL, 8)
        t3 = T(L("I decide what\ncorrect looks like", "I decide\nwhat correct\nlooks like"), L(36, 36), line_spacing=0.9)
        c3 = card(cw, L(3.4, 2.4), L(TEAL, INK), PAPER, L(6, 4))
        row3 = VGroup(ey, ck).arrange(RIGHT, buff=0.3)
        inner3 = VGroup(row3, t3).arrange(DOWN, buff=0.25).move_to(c3)
        g3 = VGroup(c3, inner3)
        gs = lay([g1, g2, g3], buff=L(0.35, 0.3))
        ck.save_state()
        self.go(0.05, FadeIn(st), rt=0.25)
        self.go(0.3, FadeIn(g1, shift=UP * 0.1), rt=0.4)
        self.go(2.0, FadeIn(g2, shift=UP * 0.1), rt=0.4)
        self.go(3.8, FadeIn(c3), FadeIn(inner3[1]), FadeIn(ey), rt=0.4)
        self.go(4.6, Create(ck), rt=0.35)
        self.finish()
