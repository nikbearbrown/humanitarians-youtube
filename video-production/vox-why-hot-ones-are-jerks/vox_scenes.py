"""vox_scenes.py — Why the Hot Ones Are Jerks (Calling Bullshit, Vox style).

One Scene per GRAPHIC/CARD beat, rendered to the beat's measured duration
(read from beat_sheet.json at import — self-updating after any audio regen).
Converted from the doodle build; SAME seeded population (SEED 42) so the two
registers share one geometry. s = u + v; cuts at 0.55 / 1.45.

Color law: crimson = the cuts · navy = the trend lines · golden highlighter =
the surviving band (the editor's pen). Ink squares = people (isotype law).

Desk preflight: 16:9 safe area ±6.4 x / ±3.5 y; every fixed placement carries
margin arithmetic in comments. Durations (audio locked, converted):
A02 2.64 · A03 2.12 · A04 2.04 · A05 3.29 · A06 4.08 · A07 2.93 · A08 2.53 ·
A09 2.35 · A10 3.89 · A11 2.22 · A12 4.49 · A13 1.67 · A14 3.29 · A15 3.11 ·
A16 4.44 · A17 2.95 · A18 3.19 · A19 4.41 · A20 3.79 · A21 4.62 · A22 3.00.

Render: bash scripts/vox_run.sh reels/vox-why-hot-ones-are-jerks
"""
import json
import sys
import pathlib

import numpy as np

_HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parents[1] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *  # noqa: F401,F403
from vox_graphics import GROUND, INK, CRIMSON, NAVY, GOLD, TERRA, SLATE, SERIF, SerifLabel, LabelChip

# ── the shared population (identical to the doodle build) ───────────────────
SEED = 42
_rng = np.random.default_rng(SEED)
N = 120
UV = _rng.uniform(0.04, 0.96, size=(N, 2))
LOW, HIGH = 0.55, 1.45

# main diagram rectangle: x −4.6..4.6, y −2.45..2.55 — inside ±6.4/±3.5 safe
X0, Y0, W, H = -4.6, -2.45, 9.2, 5.0


def px(u): return X0 + u * W
def py(v): return Y0 + v * H
def s(i): return UV[i, 0] + UV[i, 1]


def dur(bid, fb=4.0):
    try:
        sheet = json.loads((_HERE / "beat_sheet.json").read_text())
        for b in sheet["beats"]:
            if b["beat_id"] == bid and b.get("actual_duration_s"):
                return float(b["actual_duration_s"])
    except Exception:
        pass
    return fb


def _axes():
    return VGroup(
        Line([X0 - 0.2, Y0, 0], [X0 + W + 0.3, Y0, 0], color=INK, stroke_width=4),
        Line([X0, Y0 - 0.2, 0], [X0, Y0 + H + 0.3, 0], color=INK, stroke_width=4))


def _people(keep=None, ghost=None):
    """Ink isotype squares, one per person. ghost = predicate for 12% opacity."""
    g = VGroup()
    for i in range(N):
        if keep is not None and not keep(i):
            continue
        m = Square(0.10).set_fill(INK, 1).set_stroke(width=0)
        m.move_to([px(UV[i, 0]), py(UV[i, 1]), 0])
        if ghost is not None and ghost(i):
            m.set_opacity(0.12)
        g.add(m)
    return g


def _cut(th):
    u1, v1 = (max(0.0, th - 1.0), min(1.0, th))
    u2, v2 = (min(1.0, th), max(0.0, th - 1.0))
    return Line([px(u1), py(v1), 0], [px(u2), py(v2), 0], color=CRIMSON, stroke_width=6)


def _hatch(corner):
    g = VGroup()
    pts = [(0.06, 0.06), (0.22, 0.06), (0.06, 0.22), (0.20, 0.20)] if corner == "low" \
        else [(0.94, 0.94), (0.78, 0.94), (0.94, 0.78), (0.80, 0.80)]
    for (u, v) in pts:
        g.add(Line([px(u) - 0.25, py(v) - 0.25, 0], [px(u) + 0.25, py(v) + 0.25, 0],
                   color=CRIMSON, stroke_width=3).set_opacity(0.3))
    return g


def _band():
    """The golden highlighter swipe over the surviving band."""
    p = Polygon([px(0.0), py(LOW), 0], [px(LOW), py(0.0), 0],
                [px(1.0), py(HIGH - 1.0), 0], [px(HIGH - 1.0), py(1.0), 0])
    return p.set_fill(GOLD, 0.35).set_stroke(width=0)


def _xlab(): return SerifLabel("attractive", accent=NAVY, size=28).move_to([px(0.85), Y0 - 0.55, 0])
def _ylab(): return SerifLabel("nice", accent=NAVY, size=28).move_to([X0 + 0.95, py(0.96), 0])
def _flat(): return Line([px(0.04), py(0.5), 0], [px(0.96), py(0.5), 0], color=NAVY, stroke_width=5)
def _tilt(): return Line([px(0.08), py(0.92), 0], [px(0.92), py(0.13), 0], color=NAVY, stroke_width=5)


# ── Act 1 — the world as it is ──────────────────────────────────────────────
class A02_Axes(Scene):             # 2.64s
    def construct(self):
        t = dur("A02", 2.64)
        self.play(Create(_axes()), run_time=t * 0.7, rate_func=linear)
        self.wait(t * 0.3)


class A03_LabelX(Scene):           # 2.12s
    def construct(self):
        t = dur("A03", 2.12)
        self.add(_axes())
        self.play(FadeIn(_xlab(), shift=UP * 0.1), run_time=t * 0.55)
        self.wait(t * 0.45)


class A04_LabelY(Scene):           # 2.04s
    def construct(self):
        t = dur("A04", 2.04)
        self.add(_axes(), _xlab())
        self.play(FadeIn(_ylab(), shift=UP * 0.1), run_time=t * 0.55)
        self.wait(t * 0.45)


class A05_Cloud(Scene):            # 3.29s — isotype count-up in the audio window
    def construct(self):
        t = dur("A05", 3.29)
        self.add(_axes(), _xlab(), _ylab())
        ppl = _people()
        self.play(AnimationGroup(*[FadeIn(m, scale=0.7) for m in ppl],
                                 lag_ratio=0.008, run_time=t * 0.82))
        self.wait(t * 0.18)


class A06_FlatLine(Scene):         # 4.08s
    def construct(self):
        t = dur("A06", 4.08)
        self.add(_axes(), _xlab(), _ylab(), _people())
        self.play(Create(_flat()), run_time=t * 0.5, rate_func=linear)
        self.wait(t * 0.5)


# ── Act 2 — your filters ────────────────────────────────────────────────────
class A07_PoolAgain(Scene):        # 2.93s — same seed, fresh canvas
    def construct(self):
        t = dur("A07", 2.93)
        ax, ppl = _axes(), _people()
        self.play(FadeIn(ax), run_time=t * 0.25)
        self.play(AnimationGroup(*[FadeIn(m, scale=0.7) for m in ppl],
                                 lag_ratio=0.004, run_time=t * 0.55))
        self.wait(t * 0.2)


class A08_CutLow(Scene):           # 2.53s
    def construct(self):
        t = dur("A08", 2.53)
        self.add(_axes(), _people())
        self.play(Create(_cut(LOW)), run_time=t * 0.65, rate_func=linear)
        self.wait(t * 0.35)


class A09_FadeLow(Scene):          # 2.35s
    def construct(self):
        t = dur("A09", 2.35)
        ppl = _people()
        self.add(_axes(), ppl, _cut(LOW))
        gone = VGroup(*[m for i, m in enumerate(ppl) if s(i) < LOW])
        self.play(gone.animate.set_opacity(0.12), FadeIn(_hatch("low")),
                  run_time=t * 0.65)
        self.wait(t * 0.35)


class A10_CutHigh(Scene):          # 3.89s
    def construct(self):
        t = dur("A10", 3.89)
        self.add(_axes(), _people(ghost=lambda i: s(i) < LOW), _cut(LOW), _hatch("low"))
        self.play(Create(_cut(HIGH)), run_time=t * 0.5, rate_func=linear)
        self.wait(t * 0.5)


class A11_FadeHigh(Scene):         # 2.22s
    def construct(self):
        t = dur("A11", 2.22)
        ppl = _people(ghost=lambda i: s(i) < LOW)
        self.add(_axes(), ppl, _cut(LOW), _hatch("low"), _cut(HIGH))
        gone = VGroup(*[m for i, m in enumerate(ppl) if s(i) > HIGH])
        self.play(gone.animate.set_opacity(0.12), FadeIn(_hatch("high")),
                  run_time=t * 0.6)
        self.wait(t * 0.4)


class A12_Band(Scene):             # 4.49s — the editor's pen, once
    def construct(self):
        t = dur("A12", 4.49)
        self.add(_axes(), _people(ghost=lambda i: not (LOW <= s(i) <= HIGH)),
                 _cut(LOW), _hatch("low"), _cut(HIGH), _hatch("high"))
        band = _band()
        band.set_opacity(0)
        self.add(band)
        self.bring_to_back(band)  # highlighter sits UNDER the ink, like a marker
        self.play(band.animate.set_opacity(1), run_time=t * 0.45)
        self.wait(t * 0.55)


# ── Act 3 — the reveal ──────────────────────────────────────────────────────
class A13_BandAlone(Scene):        # 1.67s — tight; single composite fade
    def construct(self):
        t = dur("A13", 1.67)
        grp = VGroup(_axes(), _people(keep=lambda i: LOW <= s(i) <= HIGH))
        self.play(FadeIn(grp), run_time=min(0.9, t * 0.6))
        self.wait(max(0.1, t - min(0.9, t * 0.6)))


class A14_Tilt(Scene):             # 3.29s
    def construct(self):
        t = dur("A14", 3.29)
        self.add(_axes(), _people(keep=lambda i: LOW <= s(i) <= HIGH))
        self.play(Create(_tilt()), run_time=t * 0.6, rate_func=linear)
        self.wait(t * 0.4)


class A15_YourPool(Scene):         # 3.11s
    def construct(self):
        t = dur("A15", 3.11)
        self.add(_axes(), _people(keep=lambda i: LOW <= s(i) <= HIGH), _tilt())
        chip = LabelChip("in YOUR pool", accent=TERRA, size=24)
        chip.move_to([3.1, 2.1, 0])            # top ≈ 2.4 < 3.5, right ≈ 5.0 < 6.4
        arrow = Line(chip.get_bottom() + DOWN * 0.08, [px(0.72), py(0.33), 0],
                     color=TERRA, stroke_width=2.5)
        self.play(FadeIn(chip, shift=UP * 0.1), run_time=t * 0.4)
        self.play(Create(arrow), run_time=t * 0.25, rate_func=linear)
        self.wait(t * 0.35)


class A16_Ghosts(Scene):           # 4.44s
    def construct(self):
        t = dur("A16", 4.44)
        chip = LabelChip("in YOUR pool", accent=TERRA, size=24).move_to([3.1, 2.1, 0])
        arrow = Line(chip.get_bottom() + DOWN * 0.08, [px(0.72), py(0.33), 0],
                     color=TERRA, stroke_width=2.5)
        self.add(_axes(), _people(keep=lambda i: LOW <= s(i) <= HIGH), _tilt(),
                 chip, arrow)
        ghosts = VGroup(_cut(LOW), _cut(HIGH)).set_stroke(opacity=0.4)
        self.play(FadeIn(ghosts), run_time=t * 0.4)
        self.wait(t * 0.6)


class A17_Card(Scene):             # 2.95s — the mid-film title card
    def construct(self):
        t = dur("A17", 2.95)
        eye = Text("CALLING BULLSHIT", font=SERIF, color=BLUE, font_size=24)
        ti = Text("BERKSON'S PARADOX", font=SERIF, color=INK, font_size=54,
                  weight=BOLD)
        if ti.width > 12.0:
            ti.scale_to_fit_width(12.0)
        u = Line(ti.get_corner(DL) + DOWN * 0.15, ti.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        sub = Text("how filters invent patterns", font=SERIF, color=INK,
                   font_size=28)
        eye.to_edge(UP, buff=1.3)              # top ≈ 2.7 < 3.5 safe
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.4)
        self.play(FadeIn(ti), Create(u), run_time=0.8)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(max(0.1, t - 1.6))


# ── Act 4 — the kicker ──────────────────────────────────────────────────────
class A18_GoogleQuote(Scene):      # 3.19s — paraphrase card, attributed
    def construct(self):
        t = dur("A18", 3.19)
        chip = LabelChip("GOOGLE · PEOPLE ANALYTICS", accent=SLATE, size=22)
        chip.move_to([0, 2.3, 0])              # top ≈ 2.6 < 3.5 safe
        line1 = Text("Contest wins predicted", font=SERIF, color=INK, font_size=40)
        line2 = Text("worse job performance.", font=SERIF, color=INK, font_size=40)
        quote = VGroup(line1, line2).arrange(DOWN, buff=0.25).move_to([0, 0.3, 0])
        bar = Rectangle(width=line2.width + 0.3, height=line2.height + 0.25)
        bar.set_fill(GOLD, 0.45).set_stroke(width=0).move_to(line2)
        attr = Text("internal finding — as reported in Calling Bullshit, ch. 6",
                    font=SERIF, color=INK, font_size=22, slant=ITALIC)
        attr.move_to([0, -1.6, 0])
        self.play(FadeIn(chip), run_time=0.4)
        self.play(FadeIn(quote, shift=UP * 0.1), run_time=0.8)
        self.add(bar)
        self.bring_to_back(bar)
        bar.set_opacity(0)
        self.play(bar.animate.set_opacity(1), FadeIn(attr), run_time=0.6)
        self.wait(max(0.1, t - 1.8))


class A19_MiniScatter(Scene):      # 4.41s — the hired pool
    def construct(self):
        t = dur("A19", 4.41)
        # mini diagram: x −3.4..3.6, y −1.9..2.0 — well inside safe
        x0, y0, w, h = -3.4, -1.9, 6.8, 3.8
        ax = VGroup(Line([x0, y0, 0], [x0 + w + 0.2, y0, 0], color=INK, stroke_width=4),
                    Line([x0, y0, 0], [x0, y0 + h + 0.2, 0], color=INK, stroke_width=4))
        r2 = np.random.default_rng(7)
        us = r2.uniform(0.08, 0.92, 26)
        vs = np.clip(1.02 - us + r2.normal(0, 0.10, 26), 0.06, 0.96)
        dots = VGroup(*[Square(0.10).set_fill(INK, 1).set_stroke(width=0)
                        .move_to([x0 + u * w, y0 + v * h, 0]) for u, v in zip(us, vs)])
        trend = Line([x0 + 0.06 * w, y0 + 0.94 * h, 0],
                     [x0 + 0.94 * w, y0 + 0.10 * h, 0], color=NAVY, stroke_width=5)
        self.play(Create(ax), run_time=t * 0.2)
        self.play(AnimationGroup(*[FadeIn(m, scale=0.7) for m in dots],
                                 lag_ratio=0.02, run_time=t * 0.4))
        self.play(Create(trend), run_time=t * 0.25, rate_func=linear)
        self.wait(t * 0.15)


class A20_HiringBar(Scene):        # 3.79s
    def construct(self):
        t = dur("A20", 3.79)
        x0, y0, w, h = -3.4, -1.9, 6.8, 3.8
        ax = VGroup(Line([x0, y0, 0], [x0 + w + 0.2, y0, 0], color=INK, stroke_width=4),
                    Line([x0, y0, 0], [x0, y0 + h + 0.2, 0], color=INK, stroke_width=4))
        r2 = np.random.default_rng(7)
        us = r2.uniform(0.08, 0.92, 26)
        vs = np.clip(1.02 - us + r2.normal(0, 0.10, 26), 0.06, 0.96)
        dots = VGroup(*[Square(0.10).set_fill(INK, 1).set_stroke(width=0)
                        .move_to([x0 + u * w, y0 + v * h, 0]) for u, v in zip(us, vs)])
        trend = Line([x0 + 0.06 * w, y0 + 0.94 * h, 0],
                     [x0 + 0.94 * w, y0 + 0.10 * h, 0], color=NAVY, stroke_width=5)
        self.add(ax, dots, trend)
        bar = Line([x0 - 0.1, y0 + 0.55 * h, 0], [x0 + 0.55 * w, y0 - 0.1, 0],
                   color=CRIMSON, stroke_width=6)
        self.play(Create(bar), run_time=t * 0.5, rate_func=linear)
        self.wait(t * 0.5)


class A21_GateFunnel(Scene):       # 4.62s — isotype through the gate
    def construct(self):
        t = dur("A21", 4.62)
        # funnel mouth x=−1.2, exit x=1.2; crowd −5.4..−2.0; out ends 4.6 < 6.4
        top = Line([-1.2, 2.2, 0], [1.2, 0.55, 0], color=INK, stroke_width=5)
        bot = Line([-1.2, -2.2, 0], [1.2, -0.55, 0], color=INK, stroke_width=5)
        r3 = np.random.default_rng(11)
        crowd = VGroup(*[Square(0.12).set_fill(INK, 1).set_stroke(width=0)
                         .move_to([-5.4 + r3.uniform(0, 3.4), r3.uniform(-2.4, 2.4), 0])
                         for _ in range(40)])
        out = VGroup(*[Square(0.12).set_fill(NAVY, 1).set_stroke(width=0)
                       .move_to([2.4 + k * 0.55, 0, 0]) for k in range(5)])
        self.play(AnimationGroup(*[FadeIn(m, scale=0.7) for m in crowd],
                                 lag_ratio=0.01, run_time=t * 0.35))
        self.play(Create(top), Create(bot), run_time=t * 0.25, rate_func=linear)
        self.play(AnimationGroup(*[FadeIn(m, shift=RIGHT * 0.2) for m in out],
                                 lag_ratio=0.12, run_time=t * 0.25))
        self.wait(t * 0.15)


class A22_Card(Scene):             # 3.00s — closer (outro law pads this beat)
    def construct(self):
        t = dur("A22", 3.0)
        eye = Text("THE RULE", font=SERIF, color=BLUE, font_size=24)
        ti = Text("ASK WHO GOT FILTERED OUT", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        if ti.width > 12.0:
            ti.scale_to_fit_width(12.0)
        u = Line(ti.get_corner(DL) + DOWN * 0.15, ti.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        sub = Text("before you trust a pattern", font=SERIF, color=INK, font_size=28)
        eye.to_edge(UP, buff=1.3)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.4)
        self.play(FadeIn(ti), Create(u), run_time=0.8)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(max(0.1, t - 1.6))
