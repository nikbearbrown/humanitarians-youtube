"""Manim scenes for "How Do Websites Know I'm Not a Robot?" (Keya G.), 16:9.

Scenes, one per Manim beat in beat_sheet.json:
B02_Hook             a robot walks through a gate; then I get the picture grid: every traffic light, every bike
B04_WhatIsCaptcha    the acronym unfolds; human or bot?; wavy letters; three main types
B05_Checkbox         a ticked box is not the test: signals feed a gate; sure goes through, unsure gets pictures
B06_NoPuzzle         no puzzle, a watching eye, a 0-to-1 score dial
B07_Cloudflare       small background challenges; the CAPTCHAs shown shrink; a stopwatch drops
B08_BotsBeatHumans   people and bots on distorted text: time and accuracy, ranges drawn as ranges
B09_HundredPercent   a picture grid solved 100% against an earlier band; cookies and history feed the decision
B10_WhatNow          scores instead of puzzles, behaviour in the background, a gate that stops and verifies

Simple drawn shapes only: no Google, reCAPTCHA, hCaptcha or Cloudflare logos, no screenshots of real challenge
pages, no copy of any product's widget or colours. The letters in the wavy example are made up. Company and
product names appear as plain text only. Every example is an illustration; the only figures are the ones in
SCRIPT.md, and the dial shows only 0 and 1.
Scene length comes from actual_duration_s in beat_sheet.json. The go() times are word timings measured
from each beat's narration audio (faster-whisper), so re-check them if that audio is regenerated.
"""
import json
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).resolve().parent
DUR = {"B02": 13.48, "B04": 17.96, "B05": 17.75, "B06": 12.59, "B07": 20.03, "B08": 19.95, "B09": 22.51,
       "B10": 16.83}
if (HERE / "beat_sheet.json").is_file():
    DUR = {b["beat_id"]: b["actual_duration_s"]
           for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}

# humanitarians palette: runtime/remotion/src/tokens/humanitarians.ts
CREAM = "#F3EBDD"
INK = "#2F2A26"
TEAL = "#1F4E5F"      # the kept, passing or correct thing
CRIMSON = "#E4572E"   # the one accent per beat: the thing being questioned or stopped
MUTED = "#5C5448"     # secondary text
PALE = "#9C927F"      # thin structure lines
PAPER = "#EADFCB"     # card fill
BORDER = "#6A604F"    # outline of cards/windows that enclose text (kept off the ink mask)

SAFE_X, SAFE_Y = 6.25, 3.4
MIN_FS = 30           # smallest text allowed in a scene (at 8 units tall)
PORTRAIT = False
HEAD_Y = 2.9


def T(text, size=40, color=INK, max_w=None, **kw):
    """Text that is never scaled: if it is too wide the font size itself is reduced, so the size a
    scene reports is the size on screen. A "\\n" gives centred lines."""
    ls = kw.pop("line_spacing", 1)
    if "\n" in text:
        lines = [T(l, size, color, max_w, **kw) for l in text.split("\n")]
        return VGroup(*lines).arrange(DOWN, buff=.14 * ls * size / 40)
    m = Text(text, font="EB Garamond", font_size=size, color=color, **kw)
    while max_w and m.width > max_w and size > MIN_FS:
        size -= 2
        m = Text(text, font="EB Garamond", font_size=size, color=color, **kw)
    return m



def check_mark(x, y, s=.3, color=TEAL, w=9):
    return VMobject(stroke_color=color, stroke_width=w).set_points_as_corners(
        [[x - s, y, 0], [x - s * .35, y - s * .75, 0], [x + s, y + s * .8, 0]])


def cross_mark(x, y, s=.28, color=INK, w=9):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], stroke_color=color, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], stroke_color=color, stroke_width=w))


def poly(pts, color=INK, w=7):
    return VMobject(stroke_color=color, stroke_width=w, fill_opacity=0).set_points_as_corners(
        [[x, y, 0] for x, y in pts])


def win(w, h, title=None):
    """A plain window: rounded rectangle, a thin bar with three pale dots, an optional small title."""
    body = RoundedRectangle(width=w, height=h, corner_radius=.2, stroke_color=BORDER, stroke_width=5,
                            fill_color=PAPER, fill_opacity=1)
    bar = Line([-w / 2, h / 2 - .62, 0], [w / 2, h / 2 - .62, 0], stroke_color=PALE, stroke_width=4)
    dots = VGroup(*[Dot(radius=.07, color=PALE) for _ in range(3)]).arrange(RIGHT, buff=.15
                                                                          ).move_to([-w / 2 + .55, h / 2 - .31, 0])
    g = VGroup(body, bar, dots)
    if title:
        g.add(T(title, 32, MUTED, max_w=w - 1.6).move_to([0, h / 2 - .31, 0]))
    return g


def card(w, h):
    return RoundedRectangle(width=w, height=h, corner_radius=.2, stroke_color=BORDER, stroke_width=5,
                            fill_color=PAPER, fill_opacity=1)


def chip(text, color, fs=34, pad=.3, max_w=None):
    t = T(text, fs, color, max_w=max_w)
    box = RoundedRectangle(width=t.width + pad * 2, height=t.height + pad * 1.1, corner_radius=.18,
                           stroke_color=color, stroke_width=5, fill_color=CREAM, fill_opacity=1)
    t.move_to(box)
    return VGroup(box, t)


# ---- drawn pictures: plain shapes, nothing copied from any real challenge ------------------------
def light_icon(s):
    body = RoundedRectangle(width=s * .46, height=s * .86, corner_radius=s * .1, stroke_color=INK,
                            stroke_width=5, fill_color=PAPER, fill_opacity=1)
    dots = VGroup(*[Circle(radius=s * .1, stroke_width=0, fill_color=c, fill_opacity=1).move_to([0, y, 0])
                    for c, y in ((CRIMSON, s * .26), (PALE, 0), (PALE, -s * .26))])
    return VGroup(body, dots)


def bike_icon(s):
    w1 = Circle(radius=s * .2, stroke_color=INK, stroke_width=5).move_to([-s * .27, -s * .12, 0])
    w2 = Circle(radius=s * .2, stroke_color=INK, stroke_width=5).move_to([s * .27, -s * .12, 0])
    fr = poly([(-s * .27, -s * .12), (-s * .04, -s * .12), (s * .1, s * .16), (s * .27, -s * .12)], INK, 5)
    fr2 = poly([(-s * .04, -s * .12), (-s * .14, s * .16), (-s * .24, s * .16)], INK, 5)
    fr3 = poly([(s * .1, s * .16), (s * .2, s * .26), (s * .3, s * .26)], INK, 5)
    return VGroup(w1, w2, fr, fr2, fr3)


def shape_icon(s, k):
    if k == "circ":
        return Circle(radius=s * .22, stroke_width=0, fill_color=PALE, fill_opacity=1)
    if k == "tri":
        return Triangle(stroke_width=0, fill_color=PALE, fill_opacity=1).scale(s * .26)
    return Square(side_length=s * .4, stroke_width=0, fill_color=PALE, fill_opacity=1)


def cell(s, kind):
    box = RoundedRectangle(width=s, height=s, corner_radius=s * .08, stroke_color=BORDER, stroke_width=4,
                           fill_color=PAPER, fill_opacity=1)
    icon = light_icon(s) if kind == "light" else bike_icon(s) if kind == "bike" else shape_icon(s, kind)
    return VGroup(box, icon.move_to(box))


def grid(s, kinds, gap=.1, n=3):
    return VGroup(*[cell(s, k) for k in kinds]).arrange_in_grid(rows=n, cols=n, buff=gap)


def pick(c, color=TEAL):
    s = c[0].width
    ring = RoundedRectangle(width=s, height=s, corner_radius=s * .08, stroke_color=color, stroke_width=9,
                            fill_opacity=0).move_to(c)
    return VGroup(ring, check_mark(c.get_right()[0] - s * .22, c.get_top()[1] - s * .22, s * .1, color, 8))


def robot(s=1.0, color=INK):
    head = RoundedRectangle(width=s * .9, height=s * .65, corner_radius=s * .12, stroke_color=color,
                            stroke_width=6, fill_color=PAPER, fill_opacity=1).move_to([0, s * .55, 0])
    eyes = VGroup(Dot(radius=s * .07, color=color).move_to([-s * .2, s * .57, 0]),
                  Dot(radius=s * .07, color=color).move_to([s * .2, s * .57, 0]))
    ant = VGroup(Line([0, s * .875, 0], [0, s * 1.1, 0], stroke_color=color, stroke_width=6),
                 Dot(radius=s * .07, color=CRIMSON).move_to([0, s * 1.15, 0]))
    body = RoundedRectangle(width=s * 1.05, height=s * .7, corner_radius=s * .12, stroke_color=color,
                            stroke_width=6, fill_color=PAPER, fill_opacity=1).move_to([0, -s * .1, 0])
    return VGroup(body, head, eyes, ant)


def pointer(s=1.0, color=INK):
    pts = [(0, 0), (0, -1.0), (.27, -.76), (.46, -1.18), (.62, -1.1), (.43, -.7), (.76, -.7)]
    return Polygon(*[[x * s * .7, y * s * .7, 0] for x, y in pts], stroke_color=CREAM, stroke_width=3,
                   fill_color=color, fill_opacity=1)


def tip_to(m, x, y):
    v = m.get_vertices()
    if len(v) == 0:
        return np.array([x, y, 0])
    return np.array([x, y, 0]) - v[0]


def dial(r, tick=INK):
    a1 = Arc(radius=r, start_angle=PI / 2, angle=PI / 2, stroke_color=CRIMSON, stroke_width=14)
    a2 = Arc(radius=r, start_angle=0, angle=PI / 2, stroke_color=TEAL, stroke_width=14)
    ticks = VGroup(*[Line([(r - .28) * np.cos(a), (r - .28) * np.sin(a), 0], [r * np.cos(a), r * np.sin(a), 0],
                          stroke_color=tick, stroke_width=5) for a in np.linspace(0, PI, 9)])
    hub = Dot(radius=.13, color=INK)
    return VGroup(a1, a2, ticks, hub)


def needle(r, ang=0.0):
    return Line(ORIGIN, [r * .82 * np.cos(ang), r * .82 * np.sin(ang), 0], stroke_color=INK, stroke_width=10)


def stopwatch(r):
    body = Circle(radius=r, stroke_color=INK, stroke_width=7, fill_color=PAPER, fill_opacity=1)
    btn = RoundedRectangle(width=r * .35, height=r * .2, corner_radius=r * .05, stroke_color=INK, stroke_width=6,
                           fill_color=PAPER, fill_opacity=1).move_to([0, r + r * .1, 0])
    ticks = VGroup(*[Line([(r - .2) * np.cos(a), (r - .2) * np.sin(a), 0], [(r - .02) * np.cos(a),
                          (r - .02) * np.sin(a), 0], stroke_color=PALE, stroke_width=5)
                     for a in np.linspace(0, 2 * PI, 12, endpoint=False)])
    return VGroup(btn, body, ticks, Dot(radius=.1, color=INK))


def hand(r, ang):
    return Line(ORIGIN, [r * .75 * np.cos(ang), r * .75 * np.sin(ang), 0], stroke_color=CRIMSON, stroke_width=10)


def eye_shape(w):
    e = Ellipse(width=w, height=w * .5, stroke_color=INK, stroke_width=6, fill_color=PAPER, fill_opacity=1)
    return VGroup(e, Circle(radius=w * .11, stroke_width=0, fill_color=INK, fill_opacity=1))


def shield_shape(h, color=TEAL):
    pts = [(-.5, .6), (0, .78), (.5, .6), (.5, .0), (.25, -.45), (0, -.72), (-.25, -.45), (-.5, .0)]
    sh = Polygon(*[[x * h, y * h, 0] for x, y in pts], stroke_color=color, stroke_width=9, fill_color=PAPER,
                 fill_opacity=1)
    return VGroup(sh, check_mark(0, h * .02, h * .17, color, 10))


def gear(r, color=INK):
    teeth = VGroup(*[Square(side_length=r * .5, stroke_color=color, stroke_width=5, fill_color=PAPER,
                            fill_opacity=1).move_to([r * np.cos(a), r * np.sin(a), 0]).rotate(a)
                     for a in np.linspace(0, 2 * PI, 8, endpoint=False)])
    body = Circle(radius=r, stroke_color=color, stroke_width=6, fill_color=PAPER, fill_opacity=1)
    hole = Circle(radius=r * .35, stroke_color=color, stroke_width=5, fill_color=CREAM, fill_opacity=1)
    return VGroup(teeth, body, hole)


def wavy(txt, size=96, color=INK, seed=3):
    """Made-up distorted letters (not a real challenge): each letter tilted and bobbing, with wavy lines."""
    rng = np.random.RandomState(seed)
    ls = VGroup(*[Text(c, font="EB Garamond", font_size=size, color=color) for c in txt]).arrange(RIGHT, buff=.1)
    for i, l in enumerate(ls):
        l.rotate(float(rng.uniform(-.35, .35)))
        l.shift(UP * .16 * np.sin(i * 1.7))
    w = ls.width + .3
    lines = VGroup(*[FunctionGraph(lambda x, p=p: .12 * np.sin(6.5 * x + p), x_range=[-w / 2, w / 2],
                                   stroke_color=PALE, stroke_width=4).shift(UP * y)
                     for p, y in ((0, -ls.height / 2 - .12), (1.7, ls.height / 2 + .12))])
    return VGroup(ls, lines)


def sound_bars(w, h, n=9):
    hs = [.35, .7, 1.0, .55, .85, .4, .75, .95, .5][:n]
    bars = VGroup(*[Line([0, -hh * h / 2, 0], [0, hh * h / 2, 0], stroke_color=TEAL, stroke_width=9)
                    for hh in hs]).arrange(RIGHT, buff=w / n - .06)
    return bars


class Timed:
    _min_fs = 999

    def setup(self):
        self.camera.background_color = CREAM
        self._min_fs = 999

    @property
    def now(self):
        return self.renderer.time

    def _scan(self):
        """Smallest visible text so far; a QC line is printed for anything under MIN_FS."""
        try:
            for m in self.mobjects:
                for s in m.get_family():
                    if isinstance(s, Text) and float(s.get_fill_opacity()) > .05 and float(s.width) > 0:
                        self._min_fs = min(self._min_fs, float(s.font_size))
                        if float(s.font_size) < MIN_FS:
                            print(f"QC {self.BEAT}: text '{s.text[:24]}' is {float(s.font_size):.0f} (< {MIN_FS})")
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
    """Give a scene the Timed helpers. Each scene stays `class Name(Scene)` because the runner finds
    scenes by that exact text, so a Scene subclass would be missed."""
    def wrap(cls):
        for name, value in vars(Timed).items():
            if not name.startswith("__"):
                setattr(cls, name, value)
        cls.BEAT = beat
        return cls
    return wrap


K1 = ["light", "sq", "light", "tri", "light", "circ", "sq", "light", "tri"]
K2 = ["circ", "bike", "tri", "sq", "bike", "circ", "bike", "tri", "sq"]
K3 = ["sq", "light", "circ", "light", "tri", "light", "sq", "circ", "light"]


# ------------------------------------------------------------------------------------------
@timed("B02")
class B02_Hook(Scene):
    def construct(self):
        # 0.2: my bots never ran into a CAPTCHA: a robot walks straight through a gate
        lab = T("automation developer", 52, MUTED).move_to([0, 3.0, 0])
        gl = poly([(-1.0, -2.0), (-1.0, 1.6)], BORDER, 11)
        gr = poly([(1.0, -2.0), (1.0, 1.6)], BORDER, 11)
        bar = DashedLine([-1.0, 1.6, 0], [1.0, 1.6, 0], color=TEAL, stroke_width=9)
        ground = Line([-6.2, -2.0, 0], [6.2, -2.0, 0], stroke_color=PALE, stroke_width=4)
        bot = robot(1.5).move_to([-5.0, -.75, 0])
        self.go(.2, FadeIn(lab), FadeIn(gl), FadeIn(gr), FadeIn(bar), FadeIn(ground), FadeIn(bot), rt=.7)
        tag = chip("CAPTCHA", CRIMSON, 46).move_to([0, 2.1, 0])
        self.sched(1.5, [(0, bot.animate.move_to([5.0, -.75, 0]).set_run_time(2.0)), (1.4, FadeIn(tag))])

        # 4.0: but I do: a cursor reaches the same gate and it shuts
        ptr = pointer(1.8)
        ptr.shift(tip_to(ptr, -6.0, -1.0))
        self.go(4.0, FadeOut(bot), FadeOut(lab), FadeIn(ptr), rt=.4)
        self.go(4.4, ptr.animate.shift(tip_to(ptr, -1.9, -.8)), rt=.8)
        shut = Line([-1.0, -.2, 0], [1.0, -.2, 0], stroke_color=CRIMSON, stroke_width=14)
        self.go(5.2, FadeOut(bar), Create(shut), rt=.4)

        # 5.6: the picture grid, and the three things I click
        g1 = grid(1.5, K1).move_to([-3.3, -.1, 0])
        self.go(5.6, FadeOut(gl), FadeOut(gr), FadeOut(shut), FadeOut(tag), FadeOut(ground), FadeIn(g1), rt=.3)
        p1 = T("every traffic light", 60, INK, max_w=5.4).move_to([3.5, 1.5, 0])
        p2 = T("then every bike", 60, INK, max_w=5.4).move_to([3.5, .3, 0])
        p3 = T("sometimes two in a row", 60, INK, max_w=5.4).move_to([3.5, -.9, 0])
        marks = []

        def hit(t, g, i):
            c = g[i].get_center()
            m = pick(g[i])
            marks.append(m)
            self.go(t, ptr.animate.shift(tip_to(ptr, c[0] + .15, c[1] - .15)), FadeIn(m), rt=.25)

        self.go(5.9, FadeIn(p1, shift=LEFT * .2), rt=.25)
        for t, i in ((6.2, 0), (6.5, 2), (6.8, 4), (7.1, 7)):
            hit(t, g1, i)
        g2 = grid(1.5, K2).move_to([-3.3, -.1, 0])
        self.go(7.4, FadeOut(g1), *[FadeOut(m) for m in marks], FadeIn(g2), FadeIn(p2, shift=LEFT * .2), rt=.4)
        marks.clear()
        for t, i in ((7.95, 1), (8.3, 4), (8.65, 6)):
            hit(t, g2, i)
        g3 = grid(1.5, K3).move_to([-3.3, -.1, 0])
        self.go(9.1, FadeOut(g2), *[FadeOut(m) for m in marks], FadeIn(g3), FadeIn(p3, shift=LEFT * .2), rt=.4)
        marks.clear()
        for t, i in ((9.65, 1), (9.95, 3)):
            hit(t, g3, i)

        # 10.6: why does a website keep asking me to prove I'm human?
        q = VGroup(T("Why does a website", 64, INK, max_w=5.6), T("keep asking me", 64, INK, max_w=5.6),
                   T("to prove I'm human?", 64, CRIMSON, max_w=5.6)).arrange(DOWN, buff=.25).move_to([3.5, .2, 0])
        self.go(10.7, FadeOut(p1), FadeOut(p2), FadeOut(p3), FadeOut(ptr), FadeIn(q), rt=.6)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B04")
class B04_WhatIsCaptcha(Scene):
    def construct(self):
        # 1.0: CAPTCHA unfolds, one word per letter
        spec = [("C", "Completely", 1.0), ("A", "Automated", 1.62), ("P", "Public", 2.14), ("T", "Turing\ntest", 2.58),
                ("C", "Computers", 3.86), ("H", "Humans", 4.62), ("A", "Apart", 4.94)]
        xs = np.linspace(-5.2, 5.2, 7)
        acro = VGroup()
        for k, ((ch, word, t), x) in enumerate(zip(spec, xs)):
            L = Text(ch, font="EB Garamond", font_size=140, color=INK).move_to([x, 2.1, 0])
            W = T(word, 34, MUTED, max_w=1.8, line_spacing=.8).move_to([x, 1.05 if k % 2 == 0 else .35, 0])
            acro.add(VGroup(L, W))
            self.go(t, FadeIn(L, scale=.8), FadeIn(W, shift=UP * .1), rt=.3)

        # 6.08: a test that checks whether you're a human or a bot
        frame = card(9.4, 2.8).move_to([0, -1.55, 0])
        test = T("a test", 40, MUTED).move_to([-3.9, -.5, 0])
        self.go(6.2, FadeIn(frame), FadeIn(test), rt=.5)
        hum = chip("human", TEAL, 66).move_to([-2.7, -1.7, 0])
        orr = T("or", 50, MUTED).move_to([0, -1.7, 0])
        bot = chip("bot", CRIMSON, 66).move_to([2.7, -1.7, 0])
        self.go(7.8, FadeIn(hum, shift=UP * .15), rt=.3)
        self.go(8.15, FadeIn(orr), rt=.25)
        self.go(8.5, FadeIn(bot, shift=UP * .15), rt=.3)

        # 9.56: early versions: wavy, distorted letters
        early = T("early versions", 50, MUTED).move_to([0, -.5, 0])
        self.go(9.6, FadeOut(frame), FadeOut(test), FadeOut(hum), FadeOut(orr), FadeOut(bot), FadeIn(early), rt=.5)
        wcard = card(8.6, 2.6).move_to([0, -2.1, 0])
        wl = wavy("mKtRw", 110).move_to([0, -1.75, 0])
        box = RoundedRectangle(width=5.2, height=.62, corner_radius=.1, stroke_color=BORDER, stroke_width=4,
                               fill_color=CREAM, fill_opacity=1).move_to([0, -2.85, 0])
        self.go(11.1, FadeIn(wcard), FadeIn(wl), FadeIn(box), rt=.6)
        typedt = T("mKtRw", 44, INK).move_to([0, -2.85, 0])
        self.go(12.3, AddTextLetterByLetter(typedt, time_per_char=.1), rt=None)

        # 13.48: today, three main types: text, images, audio
        head = T("three main types", 62, INK).move_to([0, 2.9, 0])
        self.go(13.5, FadeOut(acro), FadeOut(early), FadeOut(wcard), FadeOut(wl), FadeOut(box), FadeOut(typedt),
                FadeIn(head), rt=.5)
        cs = [card(3.9, 3.8).move_to([x, -.3, 0]) for x in (-4.4, 0, 4.4)]
        c1 = wavy("kRt", 84, seed=5).move_to([-4.4, .25, 0])
        c2 = grid(.95, ["light", "bike", "circ", "tri"], gap=.1, n=2).move_to([0, .25, 0])
        c3 = sound_bars(2.6, 1.9).move_to([4.4, .25, 0])
        self.go(14.2, *[FadeIn(c) for c in cs], FadeIn(c1), FadeIn(c2), FadeIn(c3), rt=.6)
        for t, txt, x in ((15.1, "text", -4.4), (16.76, "images", 0), (17.4, "audio", 4.4)):
            self.go(t, FadeIn(T(txt, 56, INK).move_to([x, -1.8, 0]), shift=UP * .1), rt=.35)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B05")
class B05_Checkbox(Scene):
    def construct(self):
        # 0.64: the "I'm not a robot" checkbox (a drawn box and plain words)
        box = RoundedRectangle(width=1.6, height=1.6, corner_radius=.15, stroke_color=BORDER, stroke_width=7,
                               fill_color=PAPER, fill_opacity=1)
        lab = T("I'm not a robot", 64, INK)
        row = VGroup(box, lab).arrange(RIGHT, buff=.5).move_to([-2.6, 2.3, 0])
        self.go(.64, FadeIn(row, shift=UP * .1), rt=.6)
        tick = check_mark(box.get_center()[0], box.get_center()[1] - .05, .45, TEAL, 14)
        self.go(1.7, Create(tick), rt=.4)
        # 3.02: the click itself isn't the test
        cap = T("the click itself isn't the test", 50, MUTED).move_to([-2.3, .85, 0])
        self.go(3.0, FadeIn(cap), rt=.5)
        # 5.28: behind it, the system looks at signals
        gate = Polygon([0, 1.6, 0], [1.8, 0, 0], [0, -1.6, 0], [-1.8, 0, 0], stroke_color=BORDER, stroke_width=7,
                       fill_color=PAPER, fill_opacity=1).move_to([2.2, -.7, 0])
        gl = T("the system", 42, INK, max_w=2.6).move_to(gate)
        self.go(5.4, FadeIn(gate), FadeIn(gl), rt=.5)
        chips = []
        for t, txt, y in ((7.8, "cookies", -.05), (8.76, "browsing history", -1.2), (10.2, "mouse movements", -2.35)):
            c = chip(txt, INK, 48, max_w=3.4).move_to([-4.0, y, 0])
            ar = Arrow([c.get_right()[0] + .1, y, 0], [.55, -.7 + (y + .7) * .35, 0], buff=0, color=PALE,
                       stroke_width=6, max_tip_length_to_length_ratio=.2)
            chips.append((c, ar))
            self.go(t, FadeIn(c, shift=RIGHT * .3), FadeIn(ar), rt=.45)
        # 11.56: confident you're human: straight through
        conf = T("confident?", 44, INK, max_w=2.6).move_to(gate)
        self.go(11.6, FadeOut(gl), FadeIn(conf), rt=.4)
        thru = Arrow([3.9, -.1, 0], [5.0, .6, 0], buff=0, color=TEAL, stroke_width=9,
                     max_tip_length_to_length_ratio=.25)
        ok = check_mark(5.6, .75, .45, TEAL, 14)
        tl = T("straight through", 40, TEAL, max_w=2.6).move_to([4.8, 1.7, 0])
        self.go(13.3, Create(thru), FadeIn(tl), rt=.5)
        self.go(14.0, Create(ok), rt=.4)
        # 15.04: only if it's unsure: pictures
        unsure = Arrow([3.7, -1.5, 0], [4.7, -2.0, 0], buff=0, color=CRIMSON, stroke_width=9,
                       max_tip_length_to_length_ratio=.25)
        ul = T("unsure", 40, CRIMSON, max_w=2.0).move_to([3.4, -2.6, 0])
        self.go(15.1, Create(unsure), FadeIn(ul), rt=.5)
        pics = grid(.62, ["light", "sq", "bike", "tri", "light", "circ", "sq", "bike", "tri"], gap=.06
                    ).move_to([5.2, -2.0, 0])
        self.go(16.9, FadeIn(pics, shift=LEFT * .2), rt=.5)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B06")
class B06_NoPuzzle(Scene):
    def construct(self):
        # 0.2: a plain page; 1.2: reCAPTCHA v3 (plain text)
        w = win(6.0, 4.6, None).move_to([-3.2, -.35, 0])
        self.go(.2, FadeIn(w), rt=.6)
        head = T("reCAPTCHA v3", 60, INK).move_to([0, 3.0, 0])
        self.go(1.2, FadeIn(head, shift=DOWN * .1), rt=.5)
        # 2.64: shows no puzzle at all
        g = grid(1.05, K1, gap=.08).move_to([-3.4, -.55, 0])
        self.go(2.6, FadeIn(g), rt=.4)
        no = T("no puzzle", 50, CRIMSON).move_to([-3.4, -3.05, 0])
        x = cross_mark(-3.4, -.55, 1.6, CRIMSON, 12)
        self.go(3.5, Create(x), FadeIn(no), rt=.5)
        self.go(4.4, FadeOut(g), FadeOut(x), FadeOut(no), rt=.4)
        # 4.68: it watches how each visitor behaves
        eye = eye_shape(1.9).move_to([-3.4, .75, 0])
        path = VMobject(stroke_color=TEAL, stroke_width=8).set_points_smoothly(
            [[-6.0, -1.9, 0], [-5.0, -.9, 0], [-4.2, -1.6, 0], [-3.2, -.5, 0], [-2.4, -1.3, 0], [-1.2, -.2, 0]])
        ptr = pointer(1.2)
        ptr.shift(tip_to(ptr, -6.0, -1.9))
        self.go(4.7, FadeIn(eye), FadeIn(ptr), rt=.4)
        self.go(5.0, Create(path), ptr.animate.shift(tip_to(ptr, -1.2, -.2)), rt=1.1)
        # 6.2: the score dial: zero to one
        d = dial(2.4).move_to([3.8, -.5, 0])
        c = d[3].get_center()
        zero = T("0", 60, CRIMSON).move_to(c + np.array([-2.25, -.45, 0]))
        one = T("1", 60, TEAL).move_to(c + np.array([2.25, -.45, 0]))
        nd = needle(2.4, PI / 2).shift(c)
        self.go(6.2, FadeIn(d), FadeIn(zero), FadeIn(one), rt=.5)
        self.go(7.4, FadeIn(nd), rt=.3)
        self.go(8.7, Rotate(nd, angle=PI * .38, about_point=c), rt=.8)
        tagl = T("closer to 0:\nmore likely a bot", 46, CRIMSON, line_spacing=.8).move_to([3.8, -2.75, 0])
        self.go(9.6, FadeIn(tagl, shift=UP * .1), rt=.5)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B07")
class B07_Cloudflare(Scene):
    def construct(self):
        # 0.0: Cloudflare (plain text); it moved away from puzzles
        w = win(9.8, 5.8, "Cloudflare").move_to([0, -.15, 0])
        g = grid(1.1, K1, gap=.08).move_to([0, -.4, 0])
        self.go(.1, FadeIn(w), FadeIn(g), rt=.6)
        self.go(1.3, g.animate.shift(LEFT * 3).set_opacity(0), rt=.8)
        # 3.0: instead, your browser quietly solves small background challenges
        gears = [gear(.75).move_to([x, .9, 0]) for x in (-2.8, 0, 2.8)]
        for t, gg in zip((3.4, 3.9, 4.4), gears):
            self.go(t, FadeIn(gg, scale=.7), rt=.4)
        cap = T("small background challenges", 46, MUTED).move_to([0, -.55, 0])
        self.sched(4.9, [(0, Rotate(gg, angle=(PI * 1.2) * (1 if i % 2 == 0 else -1), about_point=gg.get_center(),
                                    rate_func=linear, run_time=2.4)) for i, gg in enumerate(gears)]
                   + [(.4, FadeIn(cap))])
        # 7.5: the system checks for signs of a real browser and human behaviour
        r1 = T("a real browser", 50, INK).move_to([-1.4, -1.45, 0])
        r2 = T("human behaviour", 50, INK).move_to([-1.2, -2.35, 0])
        self.go(7.6, FadeIn(r1), rt=.4)
        k1 = check_mark(1.9, -1.45, .32, TEAL, 12)
        k2 = check_mark(2.0, -2.35, .32, TEAL, 12)
        self.go(9.2, Create(k1), rt=.35)
        self.go(9.7, FadeIn(r2), rt=.4)
        self.go(10.4, Create(k2), rt=.35)
        # 11.64: Cloudflare reported: CAPTCHAs shown fell by 91% in a year
        shown = T("CAPTCHAs shown", 52, INK).move_to([-3.3, 2.1, 0])
        full = Rectangle(width=8.4, height=.85, stroke_width=0, fill_color=INK, fill_opacity=1)
        full.move_to([1.45, 1.1, 0])
        self.go(11.3, *[FadeOut(m) for m in (w, g, cap, r1, r2, k1, k2, *gears)], rt=.3)
        self.go(11.7, FadeIn(shown), FadeIn(full), rt=.5)
        small = Rectangle(width=.76, height=.85, stroke_width=0, fill_color=INK, fill_opacity=1)
        small.move_to(full.get_left() + RIGHT * .38)
        self.go(13.9, Transform(full, small), rt=1.0)
        fell = T("91% fewer", 92, CRIMSON).move_to([2.6, 1.1, 0])
        self.go(15.0, FadeIn(fell, scale=.8), rt=.5)
        # 16.4: the average check: 32 seconds to about one
        sw = stopwatch(1.35).move_to([-4.6, -1.75, 0])
        h0 = hand(1.35, PI / 2).shift(sw[3].get_center())
        lbl = T("average check", 52, MUTED).move_to([-.2, -.7, 0])
        self.go(16.4, FadeIn(sw), FadeIn(h0), FadeIn(lbl), rt=.5)
        n32 = T("32 seconds", 90, INK).move_to([1.1, -1.9, 0])
        self.go(17.9, Rotate(h0, angle=-PI * 1.1, about_point=sw[3].get_center()), FadeIn(n32), rt=1.0)
        n1 = T("about 1 second", 90, CRIMSON, max_w=7.6).move_to([1.1, -1.9, 0])
        self.go(19.2, Rotate(h0, angle=PI * 1.0, about_point=sw[3].get_center()), Transform(n32, n1), rt=.6)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B08")
class B08_BotsBeatHumans(Scene):
    def construct(self):
        x0 = -3.2
        # 0.2: a twist: a robot and a pointer, side by side
        bot = robot(1.3).move_to([-2.0, -.2, 0])
        ptr = pointer(1.8)
        ptr.shift(tip_to(ptr, 1.8, .9))
        vs = T("vs", 56, MUTED).move_to([0, -.1, 0])
        self.go(.2, FadeIn(bot), FadeIn(ptr), FadeIn(vs), rt=.5)
        # 1.86: researchers at UC Irvine (plain text)
        uc = T("UC Irvine", 54, INK).move_to([-4.6, 3.05, 0])
        self.go(1.9, FadeOut(bot), FadeOut(ptr), FadeOut(vs), FadeIn(uc), rt=.5)
        n1 = T("1,400", 120, INK).move_to([-3.3, .7, 0])
        p1 = T("people", 64, MUTED).move_to([-3.3, -.7, 0])
        n2 = T("14,000", 120, INK).move_to([3.3, .7, 0])
        p2 = T("CAPTCHAs", 64, MUTED).move_to([3.3, -.7, 0])
        self.go(3.4, FadeIn(n1, scale=.9), rt=.4)
        self.go(4.0, FadeIn(p1), rt=.3)
        self.go(4.8, FadeIn(n2, scale=.9), rt=.4)
        self.go(5.9, FadeIn(p2), rt=.3)
        # 7.1: on distorted text: the chart skeleton
        hdr = T("1,400 people · 14,000 CAPTCHAs", 44, MUTED, max_w=7.4).move_to([2.2, 3.05, 0])
        dt = chip("distorted text", INK, 40).move_to([4.5, 2.1, 0])
        t1 = T("time to solve", 46, INK).move_to([-6.1, 2.1, 0], aligned_edge=LEFT)
        t1.align_to([-6.1, 0, 0], LEFT)
        t2 = T("how often right", 46, INK).move_to([-6.1, -.55, 0])
        t2.align_to([-6.1, 0, 0], LEFT)
        axis = VGroup(Line([x0, 1.75, 0], [x0, -.0, 0], stroke_color=PALE, stroke_width=5),
                      Line([x0, -.9, 0], [x0, -2.65, 0], stroke_color=PALE, stroke_width=5))
        labs = VGroup(*[T(s_, 40, MUTED).move_to([-5.5, y, 0]) for s_, y in
                        (("people", 1.3), ("bots", .45), ("people", -1.35), ("bots", -2.2))])
        self.go(7.1, *[FadeOut(m) for m in (n1, p1, n2, p2)], FadeIn(hdr), FadeIn(dt), FadeIn(t1), FadeIn(t2),
                FadeIn(axis), FadeIn(labs), rt=.5)

        def band(a, b, y, color):
            r = Rectangle(width=b - a, height=.7, stroke_width=0, fill_color=color, fill_opacity=1)
            return r.move_to([x0 + a + (b - a) / 2, y, 0])

        tx = lambda v: v / 16 * 9.4          # seconds -> units along the time row
        ax = lambda v: v / 100 * 9.4         # percent -> units along the accuracy row
        pt = band(tx(9), tx(15), 1.3, TEAL)
        self.go(8.55, GrowFromEdge(pt, LEFT), rt=1.2)
        self.go(9.9, FadeIn(T("9 to 15 seconds", 38, CREAM, max_w=3.4).move_to(pt)), rt=.4)
        pa = band(ax(50), ax(84), -1.35, TEAL)
        self.go(11.0, GrowFromEdge(pa, LEFT), rt=1.2)
        self.go(12.3, FadeIn(T("50 to 84%", 38, CREAM, max_w=3.0).move_to(pa)), rt=.4)
        # 14.52: bots, from earlier studies
        cap = T("bots: from earlier studies", 40, MUTED).move_to([1.6, -3.1, 0])
        self.go(14.5, FadeIn(cap), rt=.4)
        bt = band(0, tx(1), .45, CRIMSON)
        self.go(16.0, GrowFromEdge(bt, LEFT), FadeIn(T("under 1 second", 40, CRIMSON).move_to([x0 + 2.4, .45, 0])), rt=.5)
        ba = band(0, ax(99.8), -2.2, CRIMSON)
        self.go(17.3, GrowFromEdge(ba, LEFT), rt=1.2)
        self.go(18.6, FadeIn(T("99.8%", 38, CREAM).move_to([x0 + ax(99.8) - .9, -2.2, 0])), rt=.4)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B09")
class B09_HundredPercent(Scene):
    def construct(self):
        gx = -3.9
        g = grid(1.45, K1).move_to([gx, .15, 0])
        self.go(.2, FadeIn(g), rt=.5)
        marks = [pick(g[i]) for i in (0, 2, 4, 7)]
        self.go(.9, *[FadeIn(m) for m in marks], rt=.5)
        # 2.56: a team at ETH Zurich (plain text); 4.26: an AI image model
        eth = T("ETH Zurich", 58, INK).move_to([3.4, 3.0, 0])
        self.go(2.5, FadeIn(eth, shift=DOWN * .1), rt=.4)
        ai = T("AI image model", 44, MUTED).move_to([3.4, 2.2, 0])
        self.go(4.3, FadeIn(ai), rt=.4)
        # 5.86: solved 100% of Google's picture challenges
        track = RoundedRectangle(width=5.6, height=.95, corner_radius=.12, stroke_color=BORDER, stroke_width=5,
                                 fill_opacity=0).move_to([3.4, 1.2, 0])
        fill = Rectangle(width=5.6, height=.95, stroke_width=0, fill_color=TEAL, fill_opacity=1).move_to(track)
        self.go(5.9, FadeIn(track), GrowFromEdge(fill, LEFT), rt=.5)
        t100 = T("100%", 60, CREAM).move_to(track)
        self.go(6.4, FadeIn(t100), rt=.4)
        gc = T("Google's picture challenges", 40, MUTED, max_w=5.2).move_to([-3.6, -2.9, 0])
        self.go(7.4, FadeIn(gc), rt=.4)
        # 9.3: earlier work solved 68 to 71%
        track2 = RoundedRectangle(width=5.6, height=.95, corner_radius=.12, stroke_color=BORDER, stroke_width=5,
                                  fill_opacity=0).move_to([3.4, -.5, 0])
        f68 = Rectangle(width=5.6 * .68, height=.95, stroke_width=0, fill_color=PALE, fill_opacity=1)
        f68.move_to(track2.get_left() + RIGHT * (5.6 * .34))
        f71 = Rectangle(width=5.6 * .03, height=.95, stroke_width=0, fill_color=CRIMSON, fill_opacity=1)
        f71.move_to(track2.get_left() + RIGHT * (5.6 * .695))
        self.go(9.4, FadeIn(track2), GrowFromEdge(f68, LEFT), rt=.8)
        self.go(10.4, FadeIn(f71), rt=.3)
        lab2 = T("earlier work: 68 to 71%", 46, INK, max_w=5.6).move_to([3.4, -1.55, 0])
        self.go(11.0, FadeIn(lab2), rt=.4)
        # 12.54: the same researchers found the system relies heavily on cookies and browsing history
        self.go(12.6, *[FadeOut(m) for m in (track, fill, t100, ai, track2, f68, f71, lab2)], rt=.5)
        gate = Polygon([0, 1.3, 0], [1.4, 0, 0], [0, -1.3, 0], [-1.4, 0, 0], stroke_color=BORDER, stroke_width=7,
                       fill_color=PAPER, fill_opacity=1).move_to([4.9, -.2, 0])
        gl = T("who's\nhuman?", 38, INK, line_spacing=.8).move_to(gate)
        self.go(13.4, FadeIn(gate), FadeIn(gl), rt=.5)
        c1 = chip("cookies", INK, 50, max_w=3.2).move_to([1.4, .7, 0])
        a1 = Arrow([c1.get_right()[0] + .1, .6, 0], [3.5, .05, 0], buff=0, color=PALE, stroke_width=12,
                   max_tip_length_to_length_ratio=.25)
        self.go(15.2, FadeIn(c1, shift=RIGHT * .3), FadeIn(a1), rt=.45)
        c2 = chip("browsing history", INK, 50, max_w=3.4).move_to([1.4, -1.2, 0])
        a2 = Arrow([c2.get_right()[0] + .1, -1.1, 0], [3.5, -.45, 0], buff=0, color=PALE, stroke_width=12,
                   max_tip_length_to_length_ratio=.25)
        self.go(16.9, FadeIn(c2, shift=RIGHT * .3), FadeIn(a2), rt=.45)
        # 20.06: the picture alone was never the whole test
        end = T("The picture alone was never the whole test", 50, INK, max_w=11.5).move_to([0, -3.0, 0])
        self.go(20.0, FadeOut(gc), FadeIn(end, shift=UP * .1), rt=.45)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B10")
class B10_WhatNow(Scene):
    def construct(self):
        xs = (-4.3, 0, 4.3)
        cards = [card(3.9, 4.5).move_to([x, .3, 0]) for x in xs]
        head = T("what they check", 56, INK).move_to([0, 2.95, 0])
        g = grid(.95, K1, gap=.08).move_to([xs[0], .6, 0])
        self.go(.2, FadeIn(head), *[FadeIn(c) for c in cards], FadeIn(g), rt=.6)
        # 2.84: scores instead of puzzles
        d = dial(1.5, PALE).move_to([xs[0], -.2, 0])
        c = d[3].get_center()
        nd = needle(1.5, PI * .25).shift(c)
        self.go(2.9, g.animate.shift(LEFT * 2.5).set_opacity(0), rt=.6)
        self.go(3.5, FadeIn(d), FadeIn(nd), rt=.4)
        cap1 = T("scores,\nnot puzzles", 44, INK, line_spacing=.8).move_to([xs[0], -2.75, 0])
        self.go(4.0, FadeIn(cap1), rt=.35)
        # 5.04: watch behaviour in the background
        eye = eye_shape(2.2).move_to([xs[1], 1.4, 0])
        path = VMobject(stroke_color=TEAL, stroke_width=8).set_points_smoothly(
            [[-1.5, -.8, 0], [-.7, .2, 0], [0, -.7, 0], [.7, .1, 0], [1.4, -.5, 0]])
        ptr = pointer(1.1)
        ptr.shift(tip_to(ptr, -1.5, -.8))
        self.go(5.1, FadeIn(eye), FadeIn(ptr), rt=.4)
        cap2 = T("behaviour,\nin the background", 44, INK, line_spacing=.8, max_w=3.6).move_to([xs[1], -2.75, 0])
        self.sched(5.5, [(0, Create(path, run_time=1.4)), (0, ptr.animate.shift(tip_to(ptr, 1.4, -.5)).set_run_time(1.4)),
                         (.7, FadeIn(cap2))])
        # 7.62: one Cloudflare leader argues for blocking bad behaviour rather than every bot
        tagA = T("one Cloudflare\nleader argues", 38, MUTED, line_spacing=.8).move_to([xs[2], 1.85, 0])
        sh = shield_shape(1.6).move_to([xs[2] + .95, -.1, 0])
        bad = robot(.8).move_to([xs[2] - 1.0, -.3, 0])
        badl = chip("bad behaviour", CRIMSON, 32, pad=.15, max_w=2.6).move_to([xs[2] - .4, -1.25, 0])
        self.go(7.7, FadeIn(tagA), FadeIn(sh), rt=.5)
        self.go(8.2, FadeIn(bad), rt=.4)
        self.go(9.4, FadeIn(badl), rt=.4)
        self.go(10.4, bad.animate.shift(RIGHT * .55), rt=.5)
        stop = cross_mark(xs[2] + .25, -.1, .3, CRIMSON, 12)
        self.go(10.9, Create(stop), rt=.3)
        cap3 = T("block the behaviour,\nnot every bot", 40, INK, line_spacing=.8, max_w=3.7).move_to([xs[2], -2.75, 0])
        self.go(11.3, FadeIn(cap3), rt=.4)
        # 12.54: companies are working on ways to verify which AI agents are allowed in
        tagB = T("companies are\nworking on it", 38, MUTED, line_spacing=.8).move_to([xs[2], 1.85, 0])
        ok = robot(.8).move_to([xs[2] - 1.0, -.3, 0])
        okl = chip("verified", TEAL, 32, pad=.15).move_to([xs[2] - .6, -1.25, 0])
        self.go(12.6, FadeOut(tagA), FadeOut(bad), FadeOut(badl), FadeOut(stop), FadeOut(cap3), FadeIn(tagB), rt=.4)
        self.go(14.1, FadeIn(ok), FadeIn(okl), rt=.4)
        cap4 = T("verify which AI agents\nare allowed in", 38, INK, line_spacing=.8, max_w=3.7).move_to([xs[2], -2.75, 0])
        self.sched(14.7, [(0, ok.animate.move_to([xs[2] + 1.5, -.3, 0]).set_run_time(.9)), (.5, FadeIn(cap4))])
        self.finish()
