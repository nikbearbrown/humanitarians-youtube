"""Manim scenes for "Week 4 Progress" (Keya G.).

B01_ThisWeeksVideo  title, a drawn keyboard guess (hashi -> kana -> kanji candidates), then research, script, build
B02_Watching        a video player; claims matched to sources; scenes matched to narration
B03_Gates           a scene token at four gates: one fails, fix and render again, passes; the check stays on
B04_Checksum        a final video and its copy on a drive show the same drawn fingerprint
B05_WhatILearned    a folder fills with its five parts; a terminal skill bar grows; a badge helps

Simple drawn shapes only: no photos, no person icons, no company or tool logos. Same style as the
Week 1 progress video. Each scene's length comes from actual_duration_s in beat_sheet.json. The times
passed to go() are word timings measured from the beat's narration audio (faster-whisper), so
re-check them if that audio is regenerated.
"""
import json
import math
import subprocess
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).resolve().parent
# beat_sheet.json is the master clock. The fallback is its measured values, for run.sh's
# Gate A, which checks a copy of this file in a folder without the sheet.
DUR = {"B01": 10.73, "B02": 10.43, "B03": 13.27, "B04": 10.41, "B05": 15.36}
SHEET = {}
if (HERE / "beat_sheet.json").is_file():
    SHEET = json.loads((HERE / "beat_sheet.json").read_text())
    DUR = {b["beat_id"]: b["actual_duration_s"] for b in SHEET["beats"]}

# humanitarians palette: runtime/remotion/src/tokens/humanitarians.ts
# Just inside the safe area run.sh's Gate B enforces (6.3 x 3.4), in Manim units.
SAFE_X, SAFE_Y = 6.25, 3.4
LOW = -SAFE_Y
CREAM = "#F3EBDD"
INK = "#2F2A26"
TEAL = "#1F4E5F"     # good / done / kept
CRIMSON = "#E4572E"  # problem / blocked
SLATE = "#29335C"    # structure
GOLD = "#F3A712"     # fill only, never text or fine marks
SAGE = "#A8C686"     # fill only
JP = "Hiragino Sans"


def T(text, size=48, color=INK, **kw):
    return Text(text, font="EB Garamond", font_size=size, color=color, **kw)


def JT(text, size=48, color=INK):
    """Japanese text: Hiragino Sans, set explicitly (the default font has no kana or kanji)."""
    return Text(text, font=JP, font_size=size, color=color)


def fit(mob, max_w):
    """Shrink (never grow) a label so it is at most max_w units wide."""
    if mob.width > max_w:
        mob.scale(max_w / mob.width)
    return mob


def M(text, size=30, color=INK):
    return Text(text, font="Menlo", font_size=size, color=color)


class Timed:
    """Narration-clock helpers: go(t, ...) starts animations at t seconds."""

    def setup(self):
        self.camera.background_color = CREAM
        self._reported = set()

    @property
    def now(self):
        return self.renderer.time

    def go(self, t, *anims, rt=0.5):
        """rt=None lets each animation keep its own run_time."""
        gap = t - self.now
        if gap > 1e-3:
            self.wait(gap)
        elif gap < -0.05:
            print(f"QC {self.BEAT}: cue {t}s is late by {-gap:.2f}s")
        self._audit(t)
        if anims:
            self.play(*anims, **({} if rt is None else {"run_time": rt}))

    def finish(self):
        self._audit(self.now)
        gap = DUR[self.BEAT] - self.now
        if gap > 1e-3:
            self.wait(gap)

    def _audit(self, t):
        """Log text outside the safe area or colliding with other text."""
        if not hasattr(self, "get_mobject_family_members"):  # Gate A's stand-in for Manim
            return
        texts = [m for m in self.get_mobject_family_members()
                 if isinstance(m, Text) and m.get_fill_opacity() > 0.05]
        for m in texts:
            box = (m.get_left()[0], m.get_right()[0], m.get_bottom()[1], m.get_top()[1])
            if box[0] < -SAFE_X - .01 or box[1] > SAFE_X + .01 or box[2] < LOW - .01 or box[3] > SAFE_Y + .01:
                self._say(f"t={t}: '{m.text}' leaves the safe area {tuple(round(v, 2) for v in box)}")
        for i, a in enumerate(texts):
            for b in texts[i + 1:]:
                if (a.get_left()[0] < b.get_right()[0] and b.get_left()[0] < a.get_right()[0]
                        and a.get_bottom()[1] < b.get_top()[1] and b.get_bottom()[1] < a.get_top()[1]):
                    self._say(f"t={t}: '{a.text}' overlaps '{b.text}'")

    def _say(self, msg):
        if msg not in self._reported:
            self._reported.add(msg)
            print(f"QC {self.BEAT}: {msg}")


def timed(beat):
    """Give a scene the Timed helpers. Each scene stays `class Name(Scene)` because
    run.sh finds scenes by that exact text, so it would miss a Scene subclass."""
    def wrap(cls):
        for name, value in vars(Timed).items():
            if not name.startswith("__"):
                setattr(cls, name, value)
        cls.BEAT = beat
        return cls
    return wrap


# ---- generic drawn shapes (never a company or tool logo) ---------------------------

def box(x, y, w, h, stroke=INK, width=3, fill=CREAM, fill_opacity=1):
    return RoundedRectangle(corner_radius=.14, width=w, height=h, stroke_color=stroke,
                            stroke_width=width, fill_color=fill,
                            fill_opacity=fill_opacity).move_to([x, y, 0])


def dashed(mob, n=28):
    return DashedVMobject(mob, num_dashes=n)


def check(at, size=.5, color=TEAL):
    at = np.array(at, dtype=float)
    pts = [at + np.array([-.5, 0, 0]) * size, at + np.array([-.1, -.45, 0]) * size,
           at + np.array([.6, .55, 0]) * size]
    return VMobject(stroke_color=color, stroke_width=10).set_points_as_corners(pts)


def cross(at, size=.5, color=CRIMSON):
    at = np.array(at, dtype=float)
    d = size * .5
    return VGroup(Line(at + [-d, -d, 0], at + [d, d, 0], stroke_color=color, stroke_width=12),
                  Line(at + [-d, d, 0], at + [d, -d, 0], stroke_color=color, stroke_width=12))


def play_icon(x, y, s=1.0, color=TEAL):
    return Triangle(fill_color=color, fill_opacity=1, stroke_width=0).rotate(-PI / 2).scale(.45 * s).move_to([x, y, 0])


def code_icon(x, y, s=1.0, color=SLATE):
    """< / > drawn as strokes."""
    w = 8 * s
    left = VMobject(stroke_color=color, stroke_width=w).set_points_as_corners(
        [[-.25, .4, 0], [-.65, 0, 0], [-.25, -.4, 0]])
    right = VMobject(stroke_color=color, stroke_width=w).set_points_as_corners(
        [[.25, .4, 0], [.65, 0, 0], [.25, -.4, 0]])
    slash = Line([.12, .45, 0], [-.12, -.45, 0], stroke_color=color, stroke_width=w)
    return VGroup(left, slash, right).scale(s).move_to([x, y, 0])


def cloud_icon(x, y, s=1.0, color=SLATE):
    parts = [Circle(radius=r, fill_color=color, fill_opacity=1, stroke_width=0).move_to(p)
             for r, p in ((.32, [-.38, -.05, 0]), (.42, [.05, .12, 0]), (.3, [.45, -.08, 0]))]
    base = RoundedRectangle(corner_radius=.18, width=1.3, height=.42, fill_color=color,
                            fill_opacity=1, stroke_width=0).move_to([.03, -.2, 0])
    return VGroup(*parts, base).scale(s).move_to([x, y, 0])


def magnifier_icon(x, y, s=1.0, color=SLATE):
    ring = Circle(radius=.34, stroke_color=color, stroke_width=8 * s, fill_opacity=0).move_to([-.1, .1, 0])
    handle = Line([.15, -.15, 0], [.5, -.5, 0], stroke_color=color, stroke_width=10 * s)
    return VGroup(ring, handle).scale(s).move_to([x, y, 0])


def page_icon(x, y, s=1.0, color=SLATE):
    page = RoundedRectangle(corner_radius=.06, width=.8, height=1.0, stroke_color=color,
                            stroke_width=5 * s, fill_color=CREAM, fill_opacity=1)
    rows = VGroup(*[Line([-.25, yy, 0], [.25 - .1 * i, yy, 0], stroke_color=color, stroke_width=5 * s)
                    for i, yy in enumerate((.25, 0, -.25))])
    return VGroup(page, rows).scale(s).move_to([x, y, 0])


def film_icon(x, y, w=2.6, h=1.4, color=SLATE):
    strip = Rectangle(width=w, height=h, fill_color=color, fill_opacity=1, stroke_width=0)
    holes = VGroup(*[RoundedRectangle(corner_radius=.03, width=.14, height=.12, fill_color=CREAM,
                                      fill_opacity=1, stroke_width=0).move_to([-w / 2 + .2 + i * (w - .4) / 7, yy, 0])
                     for i in range(8) for yy in (h / 2 - .14, -h / 2 + .14)])
    frames = VGroup(*[Rectangle(width=(w - .5) / 3 - .1, height=h - .65, fill_color=SAGE, fill_opacity=1,
                                stroke_width=0).move_to([-w / 2 + .25 + (w - .5) / 6 + i * (w - .5) / 3, 0, 0])
                      for i in range(3)])
    return VGroup(strip, holes, frames).move_to([x, y, 0])


def fingerprint(x, y, w, h, seed, color=SLATE):
    """A drawn 'fingerprint': a strip of bars. An illustration, never a real hash."""
    rng = np.random.default_rng(seed)
    n = 22
    bars = VGroup()
    for i in range(n):
        bh = h * (.45 + .5 * rng.random())
        bx = -w / 2 + w * (i + .5) / n
        bars.add(Line([bx, -bh / 2, 0], [bx, bh / 2, 0], stroke_color=color,
                      stroke_width=3 + 6 * rng.random()))
    return bars.move_to([x, y, 0])


def wave(x, y, w, h, seed, color=TEAL):
    rng = np.random.default_rng(seed)
    n = 30
    bars = VGroup()
    for i in range(n):
        bh = h * (.2 + .8 * rng.random())
        bx = -w / 2 + w * (i + .5) / n
        bars.add(Line([bx, -bh / 2, 0], [bx, bh / 2, 0], stroke_color=color, stroke_width=6))
    return bars.move_to([x, y, 0])


def switch(x, y, on=True, w=1.5, h=.78):
    body = RoundedRectangle(corner_radius=h / 2, width=w, height=h, stroke_color=TEAL if on else SLATE,
                            stroke_width=5, fill_color=TEAL if on else CREAM, fill_opacity=1)
    knob = Circle(radius=h / 2 - .1, fill_color=CREAM if on else SLATE, fill_opacity=1, stroke_width=0)
    knob.move_to([(w / 2 - h / 2) * (1 if on else -1), 0, 0])
    return VGroup(body, knob).move_to([x, y, 0])


# ---- scenes -----------------------------------------------------------------------

@timed("B01")
class B01_ThisWeeksVideo(Scene):
    def construct(self):
        title = fit(T("How Your Phone Types Japanese", 84, SLATE), 11.8).move_to([0, 2.85, 0])
        sub = T("this week's explainer", 52).move_to([0, 2.02, 0])
        self.go(.1, FadeIn(title, shift=UP * .1), rt=.5)
        self.go(.55, FadeIn(sub), rt=.45)

        # Steps: three cards along the bottom, each landing on its spoken words.
        sy, sw, sh = -2.55, 4.1, 1.5
        xs = [-4.2, 0, 4.2]
        slots = VGroup(*[dashed(box(x, sy, sw, sh, stroke=INK, width=3, fill_opacity=0)) for x in xs])
        icons = [magnifier_icon(xs[0] - 1.5, sy, 1.0), page_icon(xs[1] - 1.5, sy, .9), code_icon(xs[2] - 1.62, sy, .66, TEAL)]
        lbls = [T("researched", 48).move_to([xs[0] + .4, sy, 0]),
                VGroup(T("wrote the", 48), T("script", 48)).arrange(DOWN, buff=.06).move_to([xs[1] + .4, sy, 0]),
                VGroup(T("built with", 46), T("Claude Code", 42)).arrange(DOWN, buff=.06).move_to([xs[2] + .3, sy, 0])]
        cards = [VGroup(box(x, sy, sw, sh, stroke=SLATE, width=5), i, l) for x, i, l in zip(xs, icons, lbls)]
        self.go(3.74, Create(slots), FadeIn(cards[0], scale=.9), rt=.15)

        # A keyboard guess: hashi, typed as romaji, becomes kana, then the kanji it might mean.
        ky = .25
        kx = [-5.6 + .9 * i for i in range(5)]
        keys = VGroup(*[VGroup(box(x, ky, .82, .86, stroke=SLATE, width=4), M(c, 44, SLATE).move_to([x, ky, 0]))
                        for x, c in zip(kx, "hashi")])
        for k, t in zip(keys, (3.9, 4.1, 4.3, 4.5, 4.7)):
            self.go(t, FadeIn(k, shift=DOWN * .1), rt=.15)
        arrow1 = Arrow([-1.55, ky, 0], [-.85, ky, 0], buff=0, stroke_width=6, color=INK)
        kana = VGroup(box(.2, ky, 1.9, 1.1, stroke=SLATE, width=5), JT("はし", 62, SLATE).move_to([.2, ky, 0]))
        self.go(4.95, GrowArrow(arrow1), FadeIn(kana, scale=.9), rt=.35)
        arrow2 = Arrow([1.3, ky, 0], [1.9, ky, 0], buff=0, stroke_width=6, color=INK)
        rows = []
        for (kj, en), y in zip((("橋", "bridge"), ("箸", "chopsticks"), ("端", "edge")), (1.15, ky, -.65)):
            card = box(4.1, y, 4.1, .82, stroke=SLATE, width=4)
            rows.append(VGroup(card, JT(kj, 52, SLATE).move_to([2.75, y, 0]),
                               T(en, 46).move_to([4.7, y, 0])))
        self.go(5.35, GrowArrow(arrow2), LaggedStart(*[FadeIn(r, shift=LEFT * .2) for r in rows], lag_ratio=.35), rt=.9)
        # "which kanji you mean": one candidate is chosen.
        self.go(6.76, rows[0][0].animate.set_stroke(TEAL, 7).set_fill(TEAL, .12), rt=.4)
        self.go(7.38, FadeIn(cards[1], scale=.9), rt=.45)
        self.go(8.76, FadeIn(cards[2], scale=.9), rt=.45)
        self.go(9.6, Indicate(cards[2], color=TEAL, scale_factor=1.04), rt=.6)
        self.finish()


@timed("B02")
class B02_Watching(Scene):
    def construct(self):
        # The stage: a video player, with a timeline that runs the length of the beat.
        stage = box(0, .2, 12.2, 4.5, stroke=SLATE, width=5)
        ty = -2.75
        track = Line([-6.0, ty, 0], [6.0, ty, 0], stroke_color=INK, stroke_width=6)
        dot = Dot(radius=.2, color=TEAL).move_to([-6.0, ty, 0])
        dot.add_updater(lambda m: m.move_to([-6.0 + 12.0 * min(1.0, self.now / DUR["B02"]), ty, 0]))
        head = T("watching Brutalist videos", 58, SLATE).move_to([0, 2.85, 0])
        self.add(stage, track, dot)
        ring = VGroup(Circle(radius=1.15, stroke_color=TEAL, stroke_width=8, fill_color=CREAM, fill_opacity=1),
                      play_icon(.1, .2, 1.9)).move_to([0, .2, 0])
        films = VGroup(film_icon(-4.05, .2, 3.4, 1.9), film_icon(4.05, .2, 3.4, 1.9))
        self.go(.1, FadeIn(ring, scale=.8), FadeIn(films), rt=.5)
        self.go(1.0, FadeIn(head, shift=UP * .1), rt=.5)

        # Review 1: each claim is checked against its source.
        ys = [1.15, .1, -.95]
        lx, rx = -4.1, 4.1
        claims = VGroup(*[VGroup(box(lx, y, 3.6, .8, stroke=SLATE, width=4),
                                 Line([lx - 1.3, y + .12, 0], [lx + 1.3, y + .12, 0], stroke_color=INK, stroke_width=5),
                                 Line([lx - 1.3, y - .14, 0], [lx + .5, y - .14, 0], stroke_color=INK, stroke_width=5))
                          for y in ys])
        sources = VGroup(*[VGroup(box(rx, y, 3.6, .8, stroke=TEAL, width=4), page_icon(rx - 1.1, y, .62, TEAL),
                                  Line([rx - .6, y, 0], [rx + 1.3, y, 0], stroke_color=TEAL, stroke_width=5))
                           for y in ys])
        claim_h = T("claims", 54, SLATE).move_to([lx, 2.0, 0])
        src_h = T("sources", 54, TEAL).move_to([rx, 2.0, 0])
        self.go(4.55, FadeOut(ring), FadeOut(films), FadeIn(claim_h), FadeIn(src_h),
                LaggedStart(*[FadeIn(c) for c in claims], lag_ratio=.2),
                LaggedStart(*[FadeIn(s) for s in sources], lag_ratio=.2), rt=.45)
        links = [Arrow([lx + 1.9, y, 0], [rx - 1.9, y, 0], buff=0, stroke_width=5, color=INK) for y in ys]
        ticks = [check([0, y + .42, 0], .5) for y in ys]
        for t, a in zip((5.9, 6.3, 6.7), links):
            self.go(t, GrowArrow(a), rt=.3)
        for t, c in zip((7.05, 7.3, 7.55), ticks):
            self.go(t, Create(c), rt=.2)

        # Review 2: every scene is watched with its narration.
        fx = [-4.1, 0, 4.1]
        frames = VGroup(*[VGroup(box(x, 1.0, 3.5, 1.5, stroke=SLATE, width=5),
                                 T("scene", 54, SLATE).move_to([x, 1.0, 0])) for x in fx])
        waves = VGroup(*[wave(x, -.45, 3.3, .8, 3 + i) for i, x in enumerate(fx)])
        wl = VGroup(*[T("narration", 46, TEAL).move_to([x, -1.2, 0]) for x in fx])
        joins = [Line([x, .22, 0], [x, -.0, 0], stroke_color=INK, stroke_width=5) for x in fx]
        self.go(8.06, FadeOut(claims), FadeOut(sources), FadeOut(claim_h), FadeOut(src_h),
                *[FadeOut(a) for a in links], *[FadeOut(c) for c in ticks], rt=.4)
        self.go(8.45, LaggedStart(*[FadeIn(f) for f in frames], lag_ratio=.15), rt=.4)
        self.go(8.9, LaggedStart(*[Create(w, lag_ratio=.03) for w in waves], lag_ratio=.2),
                *[FadeIn(l) for l in wl], rt=.5)
        vticks = [check([x + 1.45, 1.55, 0], .45) for x in fx]
        for t, c in zip((9.5, 9.8, 10.1), vticks):
            self.go(t, Create(c), rt=.2)
        self.finish()


@timed("B03")
class B03_Gates(Scene):
    def construct(self):
        head = T("quality gates", 70, SLATE).move_to([0, 2.8, 0])
        self.go(1.7, FadeIn(head, shift=UP * .1), rt=.5)

        py = .35
        gx = [-4.3, -1.9, .5, 2.9]
        names = ["layout", "text size", "contrast", "facts"]
        path = Arrow([-6.15, py, 0], [4.6, py, 0], buff=0, stroke_width=6, color=INK, max_tip_length_to_length_ratio=.05)
        gates, lbls = [], []
        for x, n in zip(gx, names):
            g = VGroup(Line([x - .6, py - 1.0, 0], [x - .6, py + 1.0, 0], stroke_color=SLATE, stroke_width=10),
                       Line([x + .6, py - 1.0, 0], [x + .6, py + 1.0, 0], stroke_color=SLATE, stroke_width=10),
                       Line([x - .75, py + 1.0, 0], [x + .75, py + 1.0, 0], stroke_color=SLATE, stroke_width=10))
            gates.append(g)
            lbls.append(T(n, 48).move_to([x, py - 1.45, 0]))
        final = VGroup(box(5.4, py, 1.5, 1.2, stroke=TEAL, width=0, fill=TEAL), T("final", 52, CREAM).move_to([5.4, py, 0]))
        token = Square(side_length=.7, fill_color=GOLD, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([-5.8, py, 0])
        self.add(path, token)
        self.go(2.7, LaggedStart(*[Create(g) for g in gates], lag_ratio=.12), LaggedStart(*[FadeIn(l) for l in lbls], lag_ratio=.12),
                FadeIn(final), rt=1.0)

        # The four tests, in the order they are named: the token passes each.
        for i, t in enumerate((4.46, 5.32, 6.36, 7.06)):
            self.go(t, token.animate.move_to([gx[i] + 0, py, 0]), gates[i].animate.set_color(TEAL),
                    lbls[i].animate.set_color(TEAL), rt=.4)

        # A gate fails: the scene is sent back round the loop.
        self.go(8.2, token.animate.move_to([-5.8, py, 0]), *[g.animate.set_color(SLATE) for g in gates],
                *[l.animate.set_color(INK) for l in lbls], rt=.3)
        self.go(8.55, token.animate.move_to([gx[2] - .9, py, 0]), rt=.35)
        x_fail = cross([gx[2], py + 1.65, 0], .8)
        self.go(8.95, gates[2].animate.set_color(CRIMSON), FadeIn(x_fail, scale=1.3), rt=.3)
        loop = VMobject(stroke_color=TEAL, stroke_width=7).set_points_as_corners(
            [[gx[2], py - 1.9, 0], [gx[2], -2.0, 0], [-5.8, -2.0, 0], [-5.8, py - .55, 0]])
        tip = Triangle(fill_color=TEAL, fill_opacity=1, stroke_width=0).scale(.2).move_to([-5.8, py - .5, 0])
        fix = T("fix the scene", 56, TEAL).move_to([-4.3, -2.75, 0])
        again = T("render it again", 56, TEAL).move_to([-.1, -2.75, 0])
        self.go(9.2, Create(loop), FadeIn(tip), rt=.22)
        self.go(9.44, FadeIn(fix, shift=UP * .1), rt=.4)
        self.go(10.4, FadeIn(again, shift=UP * .1), token.animate.move_to([-5.8, py, 0]), rt=.35)
        self.go(10.85, FadeOut(x_fail), gates[2].animate.set_color(TEAL), token.animate.move_to([4.25, py, 0]),
                *[g.animate.set_color(TEAL) for g in (gates[0], gates[1], gates[3])], rt=.8)

        # You never switch the check off.
        cap = T("check stays on", 52, TEAL).move_to([4.15, -2.0, 0])
        on = switch(3.2, -2.9, True)
        off = VGroup(switch(5.3, -2.9, False), cross([5.3, -2.9, 0], 1.0))
        self.go(11.7, FadeIn(cap), FadeIn(on), FadeIn(off, scale=.9), rt=.5)
        self.finish()


@timed("B04")
class B04_Checksum(Scene):
    def construct(self):
        lx, rx, cy = -4.05, 4.05, .9
        # The finished video file, and a dashed slot waiting for its copy on a drive.
        vid = VGroup(box(lx, cy, 4.1, 3.0, stroke=SLATE, width=5), play_icon(lx + .1, cy, 1.9),
                     film_icon(lx, cy + 1.05, 3.5, .62))
        vlbl = T("final video", 58, SLATE).move_to([lx, 2.95, 0])
        slot = dashed(box(rx, cy, 4.1, 3.0, stroke=INK, width=4, fill_opacity=0), 36)
        self.go(.1, FadeIn(vid, scale=.9), FadeIn(vlbl), Create(slot), rt=.5)

        # A fingerprint of the file: a drawn pattern, not a real hash.
        fy = -1.55
        fp1 = fingerprint(lx, fy, 3.7, .9, 7)
        fbox1 = box(lx, fy, 4.1, 1.3, stroke=SLATE, width=4)
        clbl = T("checksum", 56, SLATE).move_to([lx, -2.8, 0])
        self.go(2.1, FadeIn(fbox1), Create(fp1, lag_ratio=.05), FadeIn(clbl, shift=UP * .1), rt=1.0)

        # The copy on a drive carries the same fingerprint.
        drive = VGroup(box(rx, cy, 4.1, 3.0, stroke=TEAL, width=5), cloud_icon(rx, cy + .55, 1.9, TEAL),
                       T("Drive", 54, TEAL).move_to([rx, cy - .95, 0]))
        fp2 = fingerprint(rx, fy, 3.7, .9, 7, TEAL)
        fbox2 = box(rx, fy, 4.1, 1.3, stroke=TEAL, width=4)
        self.go(6.9, FadeOut(slot), FadeIn(drive, scale=.9), rt=.5)
        self.go(7.5, FadeIn(fbox2), Create(fp2, lag_ratio=.05), rt=.9)

        # Same file, and it passed the gates.
        eq = VGroup(Line([-.6, fy + .2, 0], [.6, fy + .2, 0], stroke_color=INK, stroke_width=9),
                    Line([-.6, fy - .2, 0], [.6, fy - .2, 0], stroke_color=INK, stroke_width=9))
        same = T("same file", 58, TEAL).move_to([0, -2.8, 0])
        self.go(8.5, FadeIn(eq, scale=.8), FadeIn(same, shift=UP * .1), rt=.4)
        gate = check([lx + 1.5, cy - 1.15, 0], .7)
        self.go(9.3, Create(gate), rt=.4)
        self.go(9.9, Indicate(eq, color=TEAL, scale_factor=1.15), rt=.5)
        self.finish()


@timed("B05")
class B05_WhatILearned(Scene):
    def construct(self):
        # A folder with five parts.
        fx, fw = -3.25, 5.6
        body = box(fx, -.05, fw, 4.5, stroke=SLATE, width=5)
        tab = Polygon([fx - fw / 2 + .1, 2.15, 0], [fx - fw / 2 + 1.7, 2.15, 0], [fx - fw / 2 + 1.95, 2.4, 0],
                      [fx - fw / 2 + .1, 2.4, 0], stroke_color=SLATE, stroke_width=5, fill_color=SLATE, fill_opacity=1)
        head = T("a complete folder", 56, SLATE).move_to([fx, 2.85, 0])
        names = ["script", "beat sheet", "fact check", "scenes", "write-up"]
        ry = [1.5, .72, -.06, -.84, -1.62]
        slots = VGroup(*[dashed(box(fx, y, 4.8, .66, stroke=INK, width=2, fill_opacity=0), 24) for y in ry])
        rows = [VGroup(box(fx, y, 4.8, .66, stroke=TEAL, width=4), T(n, 46).move_to([fx, y, 0])) for n, y in zip(names, ry)]

        # The terminal, waiting.
        tx, tw = 3.5, 5.4
        term_slot = dashed(box(tx, .9, tw, 2.9, stroke=INK, width=4, fill_opacity=0), 36)
        self.go(.1, FadeIn(body), FadeIn(tab), Create(slots), Create(term_slot), rt=.5)
        self.go(1.76, FadeIn(head, shift=UP * .1), rt=.45)
        for t, r in zip((3.28, 4.16, 5.14, 6.26, 7.14), rows):
            self.go(t, FadeIn(r, shift=RIGHT * .2), rt=.3)
        done = check([-.15, 2.8, 0], .6)
        self.go(7.5, Create(done), rt=.35)

        # Better at the terminal with Claude Code: the skill bar grows.
        term = VGroup(box(tx, .9, tw, 2.9, stroke=SLATE, width=5),
                      Rectangle(width=tw, height=.5, fill_color=SLATE, fill_opacity=1, stroke_width=0).move_to([tx, 2.1, 0]),
                      M(">_ claude", 36, CREAM).move_to([tx, 2.1, 0]).align_to([tx - tw / 2 + .3, 0, 0], LEFT),
                      M("> better every week", 32, INK).move_to([tx, 1.2, 0]).align_to([tx - tw / 2 + .3, 0, 0], LEFT))
        track = RoundedRectangle(corner_radius=.17, width=4.6, height=.34, stroke_color=SLATE, stroke_width=4,
                                 fill_opacity=0).move_to([tx, .2, 0])
        fill = RoundedRectangle(corner_radius=.17, width=1.0, height=.34, fill_color=TEAL, fill_opacity=1,
                                stroke_width=0).move_to(track.get_left() + RIGHT * .5)
        full = RoundedRectangle(corner_radius=.17, width=4.6, height=.34, fill_color=TEAL, fill_opacity=1,
                                stroke_width=0).move_to(track.get_center())
        self.go(8.56, FadeOut(term_slot), FadeIn(term), Create(track), FadeIn(fill), rt=.5)
        self.go(10.2, Transform(fill, full), rt=1.3)

        # Humanitarians AI helped: a plain badge sends a helped-arrow to the terminal.
        badge = VGroup(box(tx, -2.35, 5.4, 1.0, stroke=SLATE, width=5, fill=SLATE),
                       T("Humanitarians AI", 46, CREAM).move_to([tx, -2.35, 0]))
        up = Arrow([tx, -1.78, 0], [tx, -.75, 0], buff=0, stroke_width=7, color=TEAL)
        helped = T("helped", 50, TEAL).move_to([tx + 1.55, -1.27, 0])
        self.go(11.88, FadeIn(badge, shift=UP * .15), rt=.5)
        self.go(13.06, GrowArrow(up), FadeIn(helped), rt=.5)
        self.finish()
