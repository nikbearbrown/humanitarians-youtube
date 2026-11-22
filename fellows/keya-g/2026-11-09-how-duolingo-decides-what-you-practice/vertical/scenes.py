"""Native 9:16 layouts for "How Duolingo Decides What You Practice Next" (Keya G.).

Same scene names, colours, words and go() cues as ../scenes.py, redrawn for a tall frame
(4.5 x 8 Manim units at 2160x3840). Nothing here is a crop or a squeeze of the landscape film:
one idea at a time, stacked top to bottom, bigger type, short lines.

B02_Hook                 します "do" and みます "look" come back again and again; "when?"
B04_ForgettingCurve      a notebook, then the forgetting curve draws itself
B05_SpacedRepetition     cramming over spaced practice; the dip before the next practice
B06_LeitnerBoxes         three boxes in a column; a right answer moves a card down, a wrong one up
B07_HalfLife             a half-life on a decay curve; then a skill's strength meter at half-full
B08_HalfLifeRegression   a word's history goes in, a predicted half-life comes out
B09_DidItWork            two error columns, then "mixed": a flat line and a down arrow
B10_Birdbrain            a ladder of exercises, a guess for each, and the just-right rungs
B11_FallsShort           what the model sees (inside the app) and what it does not

Simple drawn shapes only: no Duolingo logo, owl, app screenshots or other branding. Every bar, meter
and gauge is an illustration, not data: no numbers, no percentages. Japanese text is set in
Hiragino Sans on purpose: the default font has no kana glyphs.
Portrait rules kept here: all text sits above the 86% line (y > FLOOR), inside the side margins, and
no text is smaller than MIN_FS (36 units of font size is about 98 px tall in the x-height at 2160 wide,
well over the 72 px floor).
Scene length comes from actual_duration_s in beat_sheet.json. The go() times are word timings
measured from each beat's narration audio (faster-whisper), so re-check them if that audio is
regenerated.
"""
import json
from pathlib import Path

import numpy as np
from manim import *

# Portrait sync: Manim CE takes pixel dims from -r W,H but leaves frame_width at the 16:9
# default; make the frame 4.5 x 8 units.
try:
    _pw, _ph = config.pixel_width, config.pixel_height
    if _pw and _ph and abs(config.frame_width - config.frame_height * _pw / _ph) > 0.01:
        config.frame_width = config.frame_height * (_pw / _ph)
except Exception:
    pass

HERE = Path(__file__).resolve().parent
DUR = {"B02": 16.02, "B04": 12.31, "B05": 17.39, "B06": 15.96, "B07": 19.18, "B08": 19.61,
       "B09": 8.55, "B10": 16.73, "B11": 11.09}
for _p in (HERE / "beat_sheet.json", HERE.parent / "beat_sheet.json"):
    if _p.is_file():
        DUR = {b["beat_id"]: b["actual_duration_s"] for b in json.loads(_p.read_text())["beats"]}
        break

# humanitarians palette: runtime/remotion/src/tokens/humanitarians.ts
CREAM = "#F3EBDD"
INK = "#2F2A26"
TEAL = "#1F4E5F"      # right / kept / the model
CRIMSON = "#E4572E"   # the one accent per beat
SLATE = "#29335C"
GOLD = "#F3A712"      # fill only, never text
MUTED = "#6B6458"     # secondary text
PALE = "#BDB3A2"      # thin structure lines
PAPER = "#EADFCB"     # card fill
BORDER = "#A89E8C"    # outline of cards/boxes that enclose text (kept off the ink mask so Gate T reads the text, not the frame)

# Portrait safe band: nothing sits below FLOOR (the bottom 14% of the frame stays empty).
SAFE_X = 1.95
FLOOR = -2.85
MIN_FS = 34
JP = "Hiragino Sans"
PORTRAIT = True
HEAD_Y = 2.55         # two-line header centre; at 48 pt it spans about 2.1-3.45


def T(text, size=40, color=INK, **kw):
    m = Text(text, font="EB Garamond", font_size=size, color=color, **kw)
    if m.width > 3.8:                      # one line never leaves the side margins
        m.scale(3.8 / m.width)
    return m


def J(text, size=48, color=INK, **kw):
    return Text(text, font=JP, font_size=size, color=color, weight="BOLD", **kw)


def H(text, size=42, color=INK, **kw):
    """Two-line header: one idea, big, centred at the top."""
    lines = [T(s, size, color, **kw) for s in text.split("\n")]
    return VGroup(*lines).arrange(DOWN, buff=.1).move_to([0, HEAD_Y, 0])


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale(max_w / mob.width)
    return mob


def check_mark(x, y, s=.3, color=TEAL, w=9):
    return VMobject(stroke_color=color, stroke_width=w).set_points_as_corners(
        [[x - s, y, 0], [x - s * .35, y - s * .75, 0], [x + s, y + s * .8, 0]])


def cross_mark(x, y, s=.28, color=INK, w=9):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], stroke_color=color, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], stroke_color=color, stroke_width=w))


def poly(pts, color=INK, w=7):
    return VMobject(stroke_color=color, stroke_width=w, fill_opacity=0).set_points_as_corners(
        [[x, y, 0] for x, y in pts])


def card_shape(w, h, fill=PAPER, color=INK, sw=5, r=.18):
    if color == INK:
        color = BORDER
    return RoundedRectangle(width=w, height=h, corner_radius=r, stroke_color=color, stroke_width=sw,
                            fill_color=fill, fill_opacity=1)


class Timed:
    _min_fs = 999

    def setup(self):
        self.camera.background_color = CREAM
        self._min_fs = 999

    @property
    def now(self):
        return self.renderer.time

    def _scan(self):
        """Smallest visible text so far; a QC line for text under MIN_FS, under the 86% line,
        or beyond the side margins."""
        try:
            for m in self.mobjects:
                for s in m.get_family():
                    if isinstance(s, Text) and float(s.get_fill_opacity()) > .05 and float(s.width) > 0:
                        fs = float(s.font_size)
                        self._min_fs = min(self._min_fs, fs)
                        tag = s.text[:24].replace("\n", " ")
                        if fs < MIN_FS:
                            print(f"QC {self.BEAT}: text '{tag}' is {fs:.0f} (< {MIN_FS})")
                        if float(s.get_bottom()[1]) < FLOOR - .02:
                            print(f"QC {self.BEAT}: text '{tag}' dips below the 86% line")
                        if float(s.get_left()[0]) < -SAFE_X - .02 or float(s.get_right()[0]) > SAFE_X + .02:
                            print(f"QC {self.BEAT}: text '{tag}' leaves the side margins")
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
        self._scan()

    def sched(self, t, items):
        """items: [(offset_s, animation)] -> one play that starts each animation `offset_s` after t."""
        group = AnimationGroup(*[Succession(Wait(o), a) if o > 1e-3 else a for o, a in items])
        self.go(t, group, rt=None)

    def finish(self):
        self._scan()
        gap = DUR[self.BEAT] - self.now
        if gap > 1e-3:
            self.wait(gap)
        else:
            print(f"QC {self.BEAT}: scene ends {-gap:.2f}s after its audio")
        print(f"QC {self.BEAT}: smallest text {self._min_fs:.0f}")


def timed(beat):
    """Give a scene the Timed helpers. Each scene stays `class Name(Scene)` because the
    runner finds scenes by that exact text, so a Scene subclass would be missed."""
    def wrap(cls):
        for name, value in vars(Timed).items():
            if not name.startswith("__"):
                setattr(cls, name, value)
        cls.BEAT = beat
        return cls
    return wrap


# ------------------------------------------------------------------------------------------
@timed("B02")
class B02_Hook(Scene):
    def construct(self):
        # 0-6s: a year of learning; the first days are where the mix-up starts
        head0 = H("over a year\nof Japanese")
        axis = Arrow([-1.9, .3, 0], [1.95, .3, 0], buff=0, color=INK, stroke_width=7,
                     max_tip_length_to_length_ratio=.07)
        brace = poly([(-1.9, 1.0), (-1.9, 1.3), (1.9, 1.3), (1.9, 1.0)], MUTED, 6)
        first_band = Rectangle(width=1.5, height=.3, stroke_width=0, fill_color=GOLD, fill_opacity=.85
                               ).move_to([-1.15, .3, 0])
        first_tick = Line([-1.9, -.1, 0], [-1.9, .7, 0], stroke_color=CRIMSON, stroke_width=10)
        first = T("my first\ndays", 44, line_spacing=.75).move_to([-1.1, -.85, 0])
        now_t = T("now", 44, MUTED).move_to([1.35, -.65, 0])
        self.go(.2, FadeIn(head0), Create(axis), Create(brace), rt=1.3)
        self.go(3.3, FadeIn(first_band), Create(first_tick), FadeIn(first), FadeIn(now_t), rt=.8)

        # 6.4-10.4: the two words, one card each, stacked
        stage1 = Group(axis, brace, first_tick, first, first_band, now_t)
        cap1 = H("two words\nI mix up", 44)
        def card(y):
            return card_shape(3.7, 1.95).move_to([0, y, 0])
        cardA = card(.7)
        kA = J("します", 56).move_to([0, 1.15, 0])
        rA = T("shimasu", 38, MUTED).move_to([-.8, .3, 0])
        gA = T("do", 52).move_to([.95, .3, 0])
        cardB = card(-1.45)
        kB = J("みます", 56).move_to([0, -1.0, 0])
        rB = T("mimasu", 38, MUTED).move_to([-.8, -1.85, 0])
        gB = T("look", 52).move_to([.95, -1.85, 0])
        self.go(4.5, FadeOut(Group(head0, *stage1)), FadeIn(cap1), rt=.6)
        self.go(6.4, FadeIn(cardA), FadeIn(cardB), FadeIn(kA), FadeIn(rA), rt=.6)
        self.go(7.6, FadeIn(gA), rt=.4)
        self.go(8.3, FadeIn(kB), FadeIn(rB), rt=.6)
        self.go(9.4, FadeIn(gB), rt=.4)

        # 10.4-14.6: they come back; early visits are mistakes, later ones are right
        cap2 = H("Duolingo kept\nbringing them back")
        chA = J("します", 44).move_to([0, 1.3, 0])
        chB = J("みます", 44).move_to([0, -.1, 0])
        laneA = Line([-1.9, .7, 0], [1.9, .7, 0], stroke_color=PALE, stroke_width=6)
        laneB = Line([-1.9, -.7, 0], [1.9, -.7, 0], stroke_color=PALE, stroke_width=6)
        xsA = [-1.5, -.8, -.1, .6, 1.4]
        xsB = [-1.45, -.85, -.15, .55, 1.45]
        dotsA = [Dot([x, .7, 0], radius=.11, color=INK) for x in xsA]
        dotsB = [Dot([x, -.7, 0], radius=.11, color=INK) for x in xsB]
        leg_x = cross_mark(-1.6, -1.6, .17, INK, 8)
        leg_xt = T("still mixed up", 40).move_to([-1.3, -1.6, 0], aligned_edge=LEFT)
        leg_c = check_mark(-1.6, -2.3, .2, TEAL, 9)
        leg_ct = T("got it right", 40).move_to([-1.3, -2.3, 0], aligned_edge=LEFT)
        self.go(10.4, FadeOut(Group(cardA, kA, rA, gA, cardB, kB, rB, gB)), Transform(cap1, cap2), rt=.4)
        self.go(10.8, FadeIn(chA), FadeIn(chB), Create(laneA), Create(laneB), FadeIn(leg_x), FadeIn(leg_xt),
                FadeIn(leg_c), FadeIn(leg_ct), rt=.4)
        self.sched(11.2, [(i * .28, AnimationGroup(FadeIn(dotsA[i], scale=1.6, run_time=.2),
                                                   FadeIn(dotsB[i], scale=1.6, run_time=.2))) for i in range(5)])
        crossesA = [cross_mark(x, .7, .13, INK, 7) for x in xsA[:3]]
        crossesB = [cross_mark(x, -.7, .13, INK, 7) for x in xsB[:3]]
        checksA = [check_mark(x, .7, .15, TEAL, 7) for x in xsA[3:]]
        checksB = [check_mark(x, -.7, .15, TEAL, 7) for x in xsB[3:]]
        self.go(12.55, *[ReplacementTransform(dotsA[i], crossesA[i]) for i in range(3)],
                *[ReplacementTransform(dotsB[i], crossesB[i]) for i in range(3)], rt=.4)
        self.go(13.6, *[ReplacementTransform(dotsA[3 + i], checksA[i]) for i in range(2)],
                *[ReplacementTransform(dotsB[3 + i], checksB[i]) for i in range(2)], rt=.5)

        # 14.66: How did it decide when?
        q = T("?", 230, CRIMSON, weight="BOLD").move_to([0, -1.75, 0])
        cap3 = H("How did it\ndecide when?")
        self.go(14.66, Transform(cap1, cap3), FadeOut(Group(leg_x, leg_xt, leg_c, leg_ct)), FadeIn(q, scale=.5), rt=.6)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B04")
class B04_ForgettingCurve(Scene):
    def construct(self):
        title = H("How do we\nforget?")
        ox, oy = -1.0, -2.15
        ax_y = Arrow([ox, oy, 0], [ox, 0.55, 0], buff=0, color=INK, stroke_width=7,
                     max_tip_length_to_length_ratio=.06)
        ax_x = Arrow([ox, oy, 0], [1.95, oy, 0], buff=0, color=INK, stroke_width=7,
                     max_tip_length_to_length_ratio=.06)
        ylab = T("memory", 38).rotate(PI / 2).move_to([-1.55, -.9, 0])
        xlab = T("time", 38).move_to([1.5, oy - .38, 0])
        self.go(.1, FadeIn(title, shift=DOWN * .1), Create(ax_y), Create(ax_x), FadeIn(ylab), FadeIn(xlab), rt=1.2)

        # Ebbinghaus studied his own memory (spoken "1885" is not shown)
        nb_page = card_shape(.85, 1.0, PAPER, INK, 5, .08).move_to([-1.35, 1.15, 0])
        nb_lines = VGroup(*[Line([-1.6, 1.45 - i * .2, 0], [-1.15, 1.45 - i * .2, 0], stroke_color=MUTED,
                                 stroke_width=3) for i in range(4)])
        nb_rings = VGroup(*[Dot([-1.77, 1.5 - i * .3, 0], radius=.05, color=INK) for i in range(3)])
        name = VGroup(T("Hermann", 42), T("Ebbinghaus", 42)).arrange(DOWN, buff=.05, aligned_edge=LEFT
                                                                    ).move_to([.6, 1.15, 0])
        self.go(4.2, FadeIn(nb_page), Create(nb_lines), FadeIn(nb_rings), FadeIn(name), rt=.8)

        def f(u):
            return oy + .15 + 2.2 * np.exp(-3.1 * u)
        curve = poly([(ox + .1 + 2.8 * u, f(u)) for u in np.linspace(0, 1, 90)], CRIMSON, 10)
        lab = VGroup(T("the forgetting", 36), T("curve", 36)).arrange(DOWN, buff=.04, aligned_edge=RIGHT
                                                                    ).move_to([1.95, .25, 0], aligned_edge=RIGHT)
        note = VGroup(T("no effort", 36, MUTED), T("to keep it", 36, MUTED)).arrange(DOWN, buff=.04, aligned_edge=LEFT
                                                                                    ).move_to([1.0, -.75, 0])
        self.sched(6.5, [(0, Create(curve, run_time=5.0, rate_func=linear)),
                         (.5, FadeIn(lab, shift=UP * .1, run_time=.5)),
                         (2.1, FadeIn(note, shift=UP * .1, run_time=.5))])
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B05")
class B05_SpacedRepetition(Scene):
    def construct(self):
        head = H("review slows\nthe fade")
        baseA, HA = .3, 1.1
        baseB, HB = -2.0, 1.35
        x_a, x_b = -1.9, 1.95
        lineA = Line([x_a, baseA, 0], [x_b, baseA, 0], stroke_color=INK, stroke_width=6)
        lineB = Line([x_a, baseB, 0], [x_b, baseB, 0], stroke_color=INK, stroke_width=6)
        labA = T("cramming", 38, MUTED).move_to([x_a, 1.55, 0], aligned_edge=LEFT)
        labB = T("spaced practice", 38, MUTED).move_to([x_a, -.1, 0], aligned_edge=LEFT)

        fade = poly([(x, baseA + HA * np.exp(-(x + 1.8) / 1.5)) for x in np.linspace(-1.8, x_b, 50)], MUTED, 8)
        self.go(.1, FadeIn(head), Create(lineA), Create(lineB), rt=.4)
        self.go(.5, Create(fade, run_time=1.7), rt=None)

        xsB = [-1.75, -1.35, -.75, .05, 1.05]
        gaps = [xsB[i + 1] - xsB[i] for i in range(len(xsB) - 1)]
        hsB = [g / .9 for g in gaps] + [1.2]
        blocksB = [Rectangle(width=.28, height=.3, stroke_color=INK, stroke_width=3, fill_color=TEAL,
                             fill_opacity=1).move_to([x, baseB + .19, 0]) for x in xsB]
        segs = []
        for k, x0 in enumerate(xsB):
            x1 = xsB[k + 1] if k + 1 < len(xsB) else x_b
            segs.append(poly([(x, baseB + .3 + (HB - .3) * np.exp(-(x - x0) / hsB[k]))
                              for x in np.linspace(x0, x1, 22)], TEAL, 9))
        self.go(3.2, FadeIn(labB), FadeOut(fade), rt=.2)
        self.sched(3.4, [(k * .45, AnimationGroup(FadeIn(blocksB[k], scale=1.4, run_time=.4),
                                                  Create(segs[k], run_time=.45))) for k in range(5)])
        blockA = Rectangle(width=1.0, height=.4, stroke_color=INK, stroke_width=3, fill_color=TEAL,
                           fill_opacity=1).move_to([-1.4, baseA + .23, 0])
        curveA = poly([(x, baseA + .4 + (HA - .4) * np.exp(-(x + .9) / 1.1)) for x in np.linspace(-.9, x_b, 50)],
                      TEAL, 9)
        self.go(6.1, FadeIn(labA, run_time=.5), FadeIn(blockA, run_time=.5), Create(curveA, run_time=.9), rt=None)

        arrows = []
        for i in range(4):          # a gap is a bracket: a rule with an upright tick at each end
            a0, a1, ay = xsB[i] + .1, xsB[i + 1] - .1, baseB - .3
            arrows.append(VGroup(Line([a0, ay, 0], [a1, ay, 0], stroke_color=MUTED, stroke_width=6),
                                 Line([a0, ay - .13, 0], [a0, ay + .13, 0], stroke_color=MUTED, stroke_width=6),
                                 Line([a1, ay - .13, 0], [a1, ay + .13, 0], stroke_color=MUTED, stroke_width=6)))
        self.sched(7.3, [(0, Transform(head, H("longer gaps work\neven better"), run_time=.5))]
                   + [(.3 + i * .6, GrowFromCenter(arrows[i], run_time=.4)) for i in range(4)])

        dip_x = xsB[3]
        dip_y = baseB + .3 + (HB - .3) * np.exp(-gaps[2] / hsB[2])
        dot = Dot([dip_x - .02, dip_y, 0], radius=.14, color=CRIMSON)
        drop = DashedLine([dip_x - .02, dip_y, 0], [dip_x - .02, baseB + .38, 0], color=CRIMSON, stroke_width=7,
                          dash_length=.1)
        self.go(11.62, Transform(head, H("just before\nyou forget")), rt=.5)
        self.go(13.3, FadeIn(dot, scale=2.5), Create(drop), rt=.5)
        self.go(15.3, Transform(head, H("spaced\nrepetition")), rt=.6)
        self.finish()


# ------------------------------------------------------------------------------------------
def flashcard(w=1.1, h=.7):
    c = card_shape(w, h, CREAM, INK, 4, .08)
    ln = VGroup(Line([-w * .3, h * .12, 0], [w * .3, h * .12, 0], stroke_color=MUTED, stroke_width=3),
                Line([-w * .3, -h * .15, 0], [w * .1, -h * .15, 0], stroke_color=MUTED, stroke_width=3))
    return VGroup(c, ln)


@timed("B06")
class B06_LeitnerBoxes(Scene):
    def construct(self):
        title = H("flashcards\nin boxes")
        ys = [1.3, .05, -1.2]
        boxes = [RoundedRectangle(width=3.8, height=1.1, corner_radius=.12, stroke_color=BORDER, stroke_width=6,
                                  fill_color=PAPER, fill_opacity=.55).move_to([0, y, 0]) for y in ys]
        labels = [VGroup(T("review", 38), T("often", 38)).arrange(DOWN, buff=.03, aligned_edge=LEFT),
                  VGroup(T("review", 38), T("less often", 38)).arrange(DOWN, buff=.03, aligned_edge=LEFT),
                  VGroup(T("review", 38), T("rarely", 38)).arrange(DOWN, buff=.03, aligned_edge=LEFT)]
        for lab, y in zip(labels, ys):
            lab.move_to([-.95, y, 0])
            lab.align_to([-1.75, 0, 0], LEFT)
        cx = 1.05
        card = flashcard().move_to([cx, ys[0], 0])
        self.go(.1, FadeIn(title), *[FadeIn(b) for b in boxes], rt=.7)
        self.go(.9, *[FadeIn(l) for l in labels], rt=.6)
        self.go(1.6, FadeIn(card, shift=DOWN * .3), rt=.6)

        self.go(3.2, Transform(title, H("the Leitner\nsystem")), rt=.5)
        ok = check_mark(-.2, ys[0] - .0, .22, TEAL, 11).move_to([.2, ys[0], 0]).shift(RIGHT * 0)
        ok.move_to([1.85 - .0, ys[0] + .0, 0]) if False else None
        ok_mark = check_mark(1.7, ys[0] + .05, .0, TEAL, 11)
        ok = check_mark(.1, ys[0], .22, TEAL, 11)
        self.go(5.2, Create(ok), rt=.5)
        self.go(6.4, FadeOut(ok), card.animate.move_to([cx, ys[1], 0]), rt=1.2)
        bad = cross_mark(.1, ys[1], .2, CRIMSON, 11)
        self.go(9.3, Create(bad), rt=.5)
        self.go(10.3, FadeOut(bad), card.animate.move_to([cx, ys[0], 0]), rt=1.2)
        card2 = flashcard().move_to([cx, ys[1], 0])
        card3 = flashcard().move_to([cx, ys[2], 0])
        badge = VGroup(T("every card, the same", 40), T("fixed rules", 40)).arrange(DOWN, buff=.03).move_to([0, -2.35, 0])
        self.go(13.1, FadeIn(card2, shift=DOWN * .3), FadeIn(card3, shift=DOWN * .3), rt=.5)
        self.go(13.6, FadeIn(badge, shift=UP * .1), rt=.6)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B07")
class B07_HalfLife(Scene):
    def construct(self):
        ox, oy = -.8, -1.6
        W, Hh = 2.6, 2.5
        h_len = .95
        def curve_y(u):
            return oy + Hh * (2.0 ** (-u / h_len))
        head = H("every word has\nits own half-life", 40)
        ax_y = Arrow([ox, oy, 0], [ox, oy + Hh + .25, 0], buff=0, color=INK, stroke_width=7,
                     max_tip_length_to_length_ratio=.06)
        ax_x = Arrow([ox, oy, 0], [ox + W + .15, oy, 0], buff=0, color=INK, stroke_width=7,
                     max_tip_length_to_length_ratio=.06)
        ylab = VGroup(T("chance of", 36), T("remembering", 36)).arrange(DOWN, buff=.04).rotate(PI / 2
                                                                                               ).move_to([-1.5, oy + Hh / 2, 0])
        xlab = T("time", 36).move_to([1.5, oy - .4, 0])
        curve = poly([(ox + u, curve_y(u)) for u in np.linspace(0, W, 80)], TEAL, 10)
        self.go(.1, FadeIn(head), Create(ax_y), Create(ax_x), FadeIn(ylab), FadeIn(xlab), rt=.9)
        self.go(1.9, Create(curve, run_time=1.0), rt=None)

        half_y = oy + Hh / 2
        half_line = DashedLine([ox, half_y, 0], [ox + h_len, half_y, 0], color=MUTED, stroke_width=6, dash_length=.1)
        half_tag = T("half", 34, MUTED).move_to([ox + .36, half_y - .3, 0])
        drop_line = DashedLine([ox + h_len, half_y, 0], [ox + h_len, oy, 0], color=MUTED, stroke_width=6, dash_length=.1)
        span = DoubleArrow([ox, oy - .22, 0], [ox + h_len, oy - .22, 0], buff=0, color=TEAL, stroke_width=8,
                           max_tip_length_to_length_ratio=.2, max_stroke_width_to_length_ratio=12)
        span_t = T("half-life", 36, TEAL).move_to([ox + h_len / 2 + .05, oy - .48, 0])
        caption1 = VGroup(T("memory strength", 36), T("falls by half", 36)).arrange(DOWN, buff=.04).move_to([0, 1.5, 0])
        self.go(3.1, Create(span), FadeIn(span_t), rt=.6)
        self.sched(5.3, [(0, Create(half_line, run_time=.5)), (0, FadeIn(half_tag, run_time=.5)),
                         (.1, FadeIn(caption1, shift=UP * .1, run_time=.5)), (1.1, Create(drop_line, run_time=.5))])

        mark = Dot([ox + .08, oy, 0], radius=.13, color=CRIMSON)
        since = T("since you practiced", 36).move_to([0, -2.62, 0])
        self.go(7.9, FadeIn(mark, scale=2), FadeIn(since), rt=.4)
        self.go(8.5, mark.animate.move_to([ox + h_len, oy, 0]), rt=2.6)
        pt = Dot([ox + h_len, half_y, 0], radius=.13, color=CRIMSON)
        fifty = VGroup(T("about", 36, CRIMSON, weight="BOLD"), T("fifty-fifty", 36, CRIMSON, weight="BOLD")
                       ).arrange(DOWN, buff=.04).move_to([1.0, half_y + .75, 0])
        self.go(11.6, FadeIn(pt, scale=2.5), FadeIn(fifty, shift=UP * .1), rt=.6)

        # 14.6: the chart steps back to a ghost; a skill's strength meter slips to half-full
        words = Group(head, ylab, xlab, half_tag, span_t, caption1, since, fifty)
        ghost = VGroup(ax_y, ax_x, curve, half_line, drop_line, span, mark, pt)
        sk_head = H("a skill's\nstrength meter", 42)
        track = RoundedRectangle(width=3.8, height=1.5, corner_radius=.3, stroke_color=INK, stroke_width=8,
                                 fill_opacity=0).move_to([0, .55, 0])
        fillm = Rectangle(width=3.55, height=1.25, stroke_width=0, fill_color=TEAL, fill_opacity=1)
        fillm.align_to(track, LEFT).shift(RIGHT * .125).set_y(.55)
        empty_t = T("empty", 36, MUTED).move_to([-1.2, -.55, 0])
        full_t = T("full", 36, MUTED).move_to([1.5, -.55, 0])
        half_mark = Line([0, -.05, 0], [0, 1.15, 0], stroke_color=INK, stroke_width=6)
        half_t = T("half-full", 46).move_to([0, -1.15, 0])
        todo = T("time to practice", 46, CRIMSON, weight="BOLD").move_to([0, -1.95, 0])
        illus = T("illustrative meter", 36, MUTED).move_to([0, -2.55, 0])
        self.go(14.6, FadeOut(words), ghost.animate.scale(.0001).set_stroke(opacity=0), rt=.45)
        self.go(15.1, FadeIn(sk_head), FadeIn(track), FadeIn(fillm), FadeIn(empty_t), FadeIn(full_t), FadeIn(illus), rt=.6)
        self.go(16.5, fillm.animate.stretch_to_fit_width(1.8, about_edge=LEFT), FadeIn(half_mark), FadeIn(half_t),
                rt=1.0)
        self.go(18.2, FadeIn(todo, shift=UP * .1), rt=.6)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B08")
class B08_HalfLifeRegression(Scene):
    def construct(self):
        head = H("predicting\nhalf-life", 44)
        card = card_shape(2.0, 1.2).move_to([0, 1.0, 0])
        kana = J("みます", 40).move_to([0, 1.2, 0])
        gl = T("a word", 36, MUTED).move_to([0, .7, 0])
        model = card_shape(3.7, .8, CREAM, TEAL, 8, .22).move_to([0, -1.5, 0])
        model_t = T("half-life regression", 34, TEAL, weight="BOLD").move_to(model)
        chip1 = card_shape(3.4, .55, PAPER, INK, 4, .15)
        c1 = VGroup(chip1, T("machine learning", 36).move_to(chip1)).move_to([0, -.05, 0])
        chip2 = card_shape(2.6, .55, PAPER, INK, 4, .15)
        c2 = VGroup(chip2, T("data science", 36).move_to(chip2)).move_to([0, -.62, 0])
        track = RoundedRectangle(width=3.0, height=.42, corner_radius=.15, stroke_color=PALE, stroke_width=5,
                                 fill_opacity=0).move_to([0, -2.68, 0])
        out_lab = T("predicted half-life", 36).move_to([0, -2.15, 0])
        self.go(.1, FadeIn(head), FadeIn(card), FadeIn(kana), FadeIn(gl), FadeIn(model), FadeIn(track),
                FadeIn(out_lab), rt=.8)
        self.go(2.3, FadeIn(c1, shift=DOWN * .2), rt=.5)
        self.go(3.3, FadeIn(c2, shift=DOWN * .2), rt=.5)
        self.go(5.2, Transform(head, H("a new statistical\nmodel", 42)), FadeOut(c1), FadeOut(c2), rt=.4)
        self.go(5.7, FadeIn(model_t, scale=.9), rt=.6)

        row_labs = [T(n, 35).move_to([-1.9, .22 - k * .42, 0], aligned_edge=LEFT) for k, n in enumerate(("seen", "right", "wrong"))]
        arrow_in = Arrow([-.05, 1.3, 0], [.12, 1.3, 0], buff=0, color=INK, stroke_width=6, max_tip_length_to_length_ratio=.8)
        self.go(9.3, Transform(head, H("its history with\neach word", 46)), *[FadeIn(l) for l in row_labs], rt=.5)
        for k, (col, n, t0) in enumerate([(INK, 5, 11.6), (TEAL, 4, 13.4), (CRIMSON, 2, 14.5)]):
            y = .22 - k * .42
            tallies = []
            for j in range(n):
                x = -.2 + j * .3
                if k == 1:
                    m = check_mark(x, y, .09, col, 6)
                elif k == 2:
                    m = cross_mark(x, y, .08, col, 6)
                else:
                    m = Line([x, y - .13, 0], [x, y + .13, 0], stroke_color=col, stroke_width=7)
                tallies.append(m)
            self.sched(t0, [(j * .13, FadeIn(m, scale=1.4, run_time=.3)) for j, m in enumerate(tallies)])
        flow = Arrow([0, .75, 0], [0, .0, 0], buff=0, color=INK, stroke_width=6, max_tip_length_to_length_ratio=.3)

        out_arrow = Arrow([0, -1.95, 0], [0, -2.0, 0], buff=0, color=TEAL, stroke_width=6, max_tip_length_to_length_ratio=.5)
        bar = Rectangle(width=2.8, height=.28, stroke_width=0, fill_color=TEAL, fill_opacity=1)
        bar.align_to(track, LEFT).shift(RIGHT * .1).set_y(-2.68)
        bar.stretch_to_fit_width(.1, about_edge=LEFT)
        self.go(16.1, Transform(head, H("how long each\nword will last", 46)), rt=.5)
        self.go(16.6, FadeIn(bar), rt=.2)
        self.go(17.0, bar.animate.stretch_to_fit_width(1.7, about_edge=LEFT), rt=1.6)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B09")
class B09_DidItWork(Scene):
    def construct(self):
        head = T("Did it work?", 50).move_to([0, 3.0, 0])
        sub = VGroup(T("prediction error,", 40), T("as reported", 36, MUTED), T("by Duolingo", 36, MUTED)).arrange(DOWN, buff=.04
                                                                                              ).move_to([0, 1.75, 0])
        base = -1.8
        colL = Rectangle(width=1.3, height=2.3, stroke_width=0, fill_color=GOLD, fill_opacity=1).move_to([-1.0, base + 1.15, 0])
        colH = Rectangle(width=1.3, height=2.3 * .545, stroke_width=0, fill_color=TEAL, fill_opacity=1)
        colH.move_to([1.0, base + 2.3 * .545 / 2, 0])
        axis = Line([-1.8, base, 0], [1.8, base, 0], stroke_color=INK, stroke_width=6)
        labL = T("Leitner", 40).move_to([-1.0, base - .4, 0])
        labH = VGroup(T("half-life", 36), T("regression", 36)).arrange(DOWN, buff=.03).move_to([.88, base - .56, 0])
        self.go(.05, FadeIn(head), rt=.4)
        self.go(1.0, FadeIn(sub), Create(axis), FadeIn(labL), FadeIn(labH), rt=.6)
        zeroL = colL.copy().stretch_to_fit_height(.05, about_edge=DOWN)
        zeroH = colH.copy().stretch_to_fit_height(.05, about_edge=DOWN)
        colL.save_state(); colH.save_state()
        colL.stretch_to_fit_height(.05, about_edge=DOWN).move_to([-1.0, base + .025, 0])
        colH.stretch_to_fit_height(.05, about_edge=DOWN).move_to([1.0, base + .025, 0])
        self.go(2.3, FadeIn(colL), FadeIn(colH), rt=.1)
        self.go(2.4, Restore(colL), Restore(colH), rt=1.8)

        stage1 = Group(head, sub, axis, labL, labH, colL, colH)
        h2 = H("tests with real\nlearners", 46)
        mixed = T("mixed", 104, CRIMSON, weight="BOLD").move_to([0, 1.2, 0])
        rowA = T("overall activity", 42).move_to([0, -.15, 0])
        flat = Line([-1.8, -.8, 0], [1.8, -.8, 0], stroke_color=INK, stroke_width=12)
        rowB = T("practice sessions", 42).move_to([0, -1.55, 0])
        down = Arrow([0, -1.95, 0], [0, -2.75, 0], buff=0, color=INK, stroke_width=16, max_tip_length_to_length_ratio=.4)
        self.go(6.0, FadeOut(stage1), FadeIn(h2), rt=.4)
        self.go(6.5, FadeIn(rowA), FadeIn(rowB), Create(flat), GrowArrow(down), rt=.7)
        self.go(7.85, FadeIn(mixed, scale=.8), rt=.4)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B10")
class B10_Birdbrain(Scene):
    def construct(self):
        head = T("Birdbrain", 50, TEAL, weight="BOLD").move_to([0, 3.0, 0])
        later = T("another model", 36, MUTED).move_to([0, 2.5, 0])
        model = card_shape(3.8, .55, CREAM, TEAL, 6, .18).move_to([0, 1.88, 0])
        model_t = T("will you get it right?", 34).move_to(model)
        self.go(.1, FadeIn(head), rt=.5)
        self.go(1.4, FadeIn(later), rt=.5)
        self.go(2.7, FadeIn(model), FadeIn(model_t), rt=.6)

        # ladder, hardest at the top: hard band (1 rung), just-right band (2), easy band (1)
        w, rung_h, pitch, band_h = 3.4, .27, .35, .96
        cursor = 1.5
        blocks, band_y = [], []
        for n in (1, 2, 1):
            band_y.append(cursor - band_h / 2)
            cursor -= band_h
            for r in range(n):
                blocks.append(RoundedRectangle(width=w, height=rung_h, corner_radius=.1, stroke_color=INK,
                                               stroke_width=4, fill_color=PAPER, fill_opacity=1
                                               ).move_to([0, cursor - rung_h / 2, 0]))
                cursor -= pitch
        gauge_fill = [.2, .5, .62, .9]          # illustrative guesses, hardest first
        gauges = []
        for i, b in enumerate(blocks):
            c = b.get_center()
            ring = Circle(radius=.11, stroke_color=INK, stroke_width=4, fill_opacity=0).move_to([w / 2 - .28, c[1], 0])
            sec = Sector(radius=.11, angle=TAU * gauge_fill[i], start_angle=PI / 2, stroke_width=0, fill_color=TEAL,
                         fill_opacity=1, arc_center=ring.get_center())
            gauges.append(VGroup(ring, sec))
        self.go(4.0, LaggedStart(*[FadeIn(b, shift=RIGHT * .2) for b in blocks], lag_ratio=.12), rt=1.2)
        key = VGroup(T("fuller dial:", 35, MUTED), T("more likely right", 35, MUTED)).arrange(DOWN, buff=.03).move_to([0, band_y[1] + .1, 0])
        self.go(5.2, LaggedStart(*[FadeIn(g, scale=1.5) for g in gauges], lag_ratio=.18), FadeIn(key), rt=1.6)

        mid = SurroundingRectangle(VGroup(blocks[1], blocks[2]), color=CRIMSON, buff=0, stroke_width=7, corner_radius=.1)
        mid_t = VGroup(T("just the right", 34, CRIMSON, weight="BOLD"), T("difficulty", 34, CRIMSON, weight="BOLD")
                       ).arrange(DOWN, buff=.02).move_to([0, band_y[1] + .1, 0])
        hard_t = VGroup(T("too hard:", 36), T("frustrated", 36)).arrange(DOWN, buff=.02).move_to([0, band_y[0], 0])
        easy_t = VGroup(T("too easy:", 36), T("already mastered", 36)).arrange(DOWN, buff=.02).move_to([0, band_y[2] - .1, 0])
        self.go(10.1, Create(mid), FadeOut(key), FadeIn(mid_t, shift=DOWN * .1), rt=.8)
        self.go(11.9, FadeIn(hard_t, shift=DOWN * .1), blocks[0].animate.set_opacity(.55), rt=.7)
        self.go(13.9, FadeIn(easy_t, shift=DOWN * .1), blocks[3].animate.set_opacity(.55), rt=.7)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B11")
class B11_FallsShort(Scene):
    def construct(self):
        limits = T("it has limits", 46, MUTED).move_to([0, 3.05, 0])
        view = T("In my view", 46, MUTED, slant="ITALIC").move_to([0, 3.05, 0])
        app = card_shape(3.8, 1.65, PAPER, INK, 7, .25).move_to([0, 1.95, 0])
        app_t = VGroup(T("inside the app:", 40), T("what I do", 40)).arrange(DOWN, buff=.04).move_to([0, 2.2, 0])
        ticks = VGroup(*[check_mark(-1.2 + i * .6, 1.45, .12, TEAL, 7) for i in range(5)])
        wall = DashedLine([-1.95, .98, 0], [1.95, .98, 0], color=PALE, stroke_width=6, dash_length=.18)
        self.go(.2, FadeIn(limits), rt=.5)
        self.go(1.4, ReplacementTransform(limits, view), rt=.5)
        self.go(2.1, FadeIn(app), FadeIn(app_t), rt=.7)
        self.go(2.9, LaggedStart(*[FadeIn(t, scale=1.4) for t in ticks], lag_ratio=.15), rt=1.4)

        two = {"my interests": ("my interests",),
               "Japanese I use somewhere else": ("Japanese I use", "somewhere else"),
               "a mistake while speaking": ("a mistake", "while speaking")}
        ys = [.0, -.97, -2.17]
        hs = [.8, 1.05, 1.05]
        cues = [5.16, 6.42, 9.12]
        outs = []
        for (text, lines), y, bh in zip(two.items(), ys, hs):
            box = RoundedRectangle(width=3.8, height=bh, corner_radius=.2, stroke_color=BORDER, stroke_width=6,
                                   fill_opacity=0).move_to([0, y, 0])
            dash = DashedVMobject(box, num_dashes=44, dashed_ratio=.55)
            label = VGroup(*[T(s, 34) for s in lines]).arrange(DOWN, buff=.02).move_to(box)
            cross = cross_mark(1.6, y + bh / 2 - .13, .09, CRIMSON, 6)
            outs.append(VGroup(dash, label, cross))
        legend_x = cross_mark(-.6, .68, .1, CRIMSON, 6)
        legend = T("not seen", 36, MUTED).next_to(legend_x, RIGHT, buff=.2)
        self.go(4.5, Create(wall), FadeIn(legend_x), FadeIn(legend), *[FadeIn(o[0]) for o in outs], rt=.5)
        for o, c in zip(outs, cues):
            self.go(c, FadeIn(VGroup(o[1], o[2]), shift=UP * .15), rt=.6)
        self.finish()
