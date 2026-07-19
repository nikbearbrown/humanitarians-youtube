"""vox_scenes.py — Why the Rap Mortality Graph Lies (Calling Bullshit, Vox style).

One Scene per GRAPHIC/CARD beat, rendered to the beat's measured duration
(read from beat_sheet.json at import — self-updating after any audio regen).

Color law: crimson = the censor window · navy = the data · golden highlighter
= the rap bars (the editor's pen, once, in A04). Ink squares = people.

REPRESENTATIVE VALUES (FACTCHECK rows A03/A06): chart bars jazz 60 · blues 63
· country 62 · gospel 65 · rap 30 · hip-hop 29; genre start-years blues 1890 ·
jazz 1910 · country 1920 · gospel 1920 · rap 1980. Narration commits only to
"past sixty vs about thirty" and "century or more vs forty years".

Desk preflight: 16:9 safe area ±6.4 x / ±3.5 y; margin arithmetic in comments.
Durations (audio locked 2026-07-06): A02 5.93 · A03 9.87 · A04 6.69 · A05 6.50
· A06 9.38 · A08 8.54 · A09 6.09 · A10 7.78 · A11 7.47 · A12 8.12 · A13 8.31 ·
A14 7.76. (A01/A07 are STILL slots — no scenes.)

Render: bash scripts/vox_run.sh reels/vox-rap-mortality-graph
"""
import json
import sys
import pathlib

import numpy as np

_HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parents[1] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *  # noqa: F401,F403
from vox_graphics import GROUND, INK, CRIMSON, NAVY, GOLD, TERRA, SLATE, SERIF, SerifLabel, LabelChip


def dur(bid, fb=6.0):
    try:
        sheet = json.loads((_HERE / "beat_sheet.json").read_text())
        for b in sheet["beats"]:
            if b["beat_id"] == bid and b.get("actual_duration_s"):
                return float(b["actual_duration_s"])
    except Exception:
        pass
    return fb


def _card(scene, t, eyebrow, title, sub):
    eye = Text(eyebrow, font=SERIF, color=BLUE, font_size=24)
    ti = Text(title, font=SERIF, color=INK, font_size=52, weight=BOLD)
    if ti.width > 12.0:                          # 12.0 < 12.8 usable — safe
        ti.scale_to_fit_width(12.0)
    u = Line(ti.get_corner(DL) + DOWN * 0.15, ti.get_corner(DR) + DOWN * 0.15,
             color=CRIMSON, stroke_width=2)
    eye.to_edge(UP, buff=1.3)                    # top ≈ 2.7 < 3.5 safe
    scene.play(FadeIn(eye), run_time=0.4)
    scene.play(FadeIn(ti), Create(u), run_time=0.8)
    used = 1.2
    if sub:
        sb = Text(sub, font=SERIF, color=INK, font_size=28)
        sb.next_to(u, DOWN, buff=0.4)
        scene.play(FadeIn(sb), run_time=0.4)
        used += 0.4
    scene.wait(max(0.1, t - used))


# ── the chart (shared by A03/A04) ────────────────────────────────────────────
GENRES = [("jazz", 60), ("blues", 63), ("country", 62), ("gospel", 65),
          ("rap", 30), ("hip-hop", 29)]
BX0, BY0, BW, BPITCH, BSCALE = -4.7, -2.6, 1.15, 1.75, 0.058
# tallest bar: gospel 65*0.058 = 3.77 from y −2.6 → top 1.17 < 3.5 safe
# labels at y −2.95 (bottom −3.1 < 3.5 safe); last bar center x 4.05 < 6.4


def _chart_bars():
    bars, labels = VGroup(), VGroup()
    for k, (name, val) in enumerate(GENRES):
        x = BX0 + k * BPITCH
        b = Rectangle(width=BW, height=val * BSCALE)
        b.set_fill(NAVY, 0.85).set_stroke(NAVY, 2)
        b.move_to([x, BY0 + val * BSCALE / 2, 0])
        lb = Text(name, font=SERIF, color=INK, font_size=22)
        lb.move_to([x, BY0 - 0.35, 0])
        bars.add(b); labels.add(lb)
    base = Line([BX0 - 1.0, BY0, 0], [BX0 + 5 * BPITCH + 1.0, BY0, 0],
                color=INK, stroke_width=4)
    return base, bars, labels


class A02_Card(Scene):             # 5.93s
    def construct(self):
        _card(self, dur("A02", 5.93), "CALLING BULLSHIT",
              "THE RAP MORTALITY GRAPH", "a lie the data told itself")


class A03_TheChart(Scene):         # 9.87s
    def construct(self):
        t = dur("A03", 9.87)
        base, bars, labels = _chart_bars()
        ax_lb = SerifLabel("average age at death", accent=NAVY, size=26)
        ax_lb.move_to([0, 2.9, 0])               # top ≈ 3.1 < 3.5 safe
        self.play(Create(base), FadeIn(ax_lb), run_time=t * 0.15)
        for b, lb in zip(bars, labels):
            self.play(GrowFromEdge(b, DOWN), FadeIn(lb), run_time=t * 0.11)
        self.wait(t * (1 - 0.15 - 0.66))


class A04_RapBar(Scene):           # 6.69s — the editor's pen, once
    def construct(self):
        t = dur("A04", 6.69)
        base, bars, labels = _chart_bars()
        ax_lb = SerifLabel("average age at death", accent=NAVY, size=26)
        ax_lb.move_to([0, 2.9, 0])
        self.add(base, bars, labels, ax_lb)
        # highlighter sweep over the two short bars (rap, hip-hop)
        x_left = BX0 + 4 * BPITCH - BW / 2 - 0.15
        x_right = BX0 + 5 * BPITCH + BW / 2 + 0.15
        hi = Rectangle(width=x_right - x_left, height=30 * BSCALE + 0.5)
        hi.set_fill(GOLD, 0.4).set_stroke(width=0)
        hi.move_to([(x_left + x_right) / 2, BY0 + 15 * BSCALE + 0.1, 0])
        self.add(hi)
        self.bring_to_back(hi)
        hi.set_opacity(0)
        self.play(hi.animate.set_opacity(1), run_time=t * 0.3)
        self.wait(t * 0.7)


class A05_Card(Scene):             # 6.50s
    def construct(self):
        _card(self, dur("A05", 6.5), "THE QUESTION",
              "WHO CAN BE IN A DEAD-MUSICIANS DATASET?", "")


class A06_GenreAges(Scene):        # 9.38s — the genres aren't the same age
    def construct(self):
        t = dur("A06", 9.38)
        # timeline 1890..2030 → x −5.6..+5.5 (0.0793/yr); inside ±6.4 safe
        def yx(year): return -5.6 + (year - 1890) * 0.0793
        axis = Line([yx(1885), -2.6, 0], [yx(2032), -2.6, 0], color=INK, stroke_width=4)
        ticks = VGroup()
        for yr in (1900, 1950, 2000):
            tk = Line([yx(yr), -2.6, 0], [yx(yr), -2.45, 0], color=INK, stroke_width=3)
            lb = Text(str(yr), font=SERIF, color=INK, font_size=20).move_to([yx(yr), -3.0, 0])
            ticks.add(tk, lb)
        rows = [("blues", 1890, 2.1), ("jazz", 1910, 1.2), ("country", 1920, 0.3),
                ("gospel", 1920, -0.6), ("rap / hip-hop", 1980, -1.5)]
        self.play(Create(axis), FadeIn(ticks), run_time=t * 0.18)
        for name, start, y in rows:
            col = NAVY if start == 1980 else INK
            bar = Line([yx(start), y, 0], [yx(2026), y, 0], color=col, stroke_width=8)
            lb = Text(name, font=SERIF, color=col, font_size=22)
            lb.move_to([yx(start) - 0.15, y + 0.02, 0], aligned_edge=RIGHT)  # left ≥ −6.3
            self.play(Create(bar), FadeIn(lb), run_time=t * 0.12, rate_func=linear)
        self.wait(t * (1 - 0.18 - 0.6))


class A08_LivingVanish(Scene):     # 8.54s — the living can't be counted
    def construct(self):
        t = dur("A08", 8.54)
        r = np.random.default_rng(5)
        # two isotype rows: old genre (all countable) vs young genre
        def row(y, n=20):
            return [(-5.2 + k * 0.55, y) for k in range(n)]   # ends 5.25 < 6.4
        jazz_lb = SerifLabel("a century-old genre", accent=NAVY, size=24)
        jazz_lb.move_to([-5.2, 2.5, 0], aligned_edge=LEFT)
        jazz = VGroup(*[Square(0.16).set_fill(INK, 1).set_stroke(width=0)
                        .move_to([x, 1.6, 0]) for x, _ in row(1.6)])
        rap_lb = SerifLabel("a forty-year-old genre", accent=NAVY, size=24)
        rap_lb.move_to([-5.2, 0.2, 0], aligned_edge=LEFT)
        alive_mask = r.uniform(size=20) < 0.75   # most still alive
        rap = VGroup()
        for k, (x, _) in enumerate(row(-0.7)):
            col = NAVY if alive_mask[k] else INK
            rap.add(Square(0.16).set_fill(col, 1).set_stroke(width=0).move_to([x, -0.7, 0]))
        key = Text("navy = still alive · ink = deceased", font=SERIF, color=INK,
                   font_size=22, slant=ITALIC).move_to([0, -2.6, 0])
        self.play(FadeIn(jazz_lb), FadeIn(jazz), run_time=t * 0.2)
        self.play(FadeIn(rap_lb), FadeIn(rap), FadeIn(key), run_time=t * 0.2)
        gone = VGroup(*[m for k, m in enumerate(rap) if alive_mask[k]])
        self.play(gone.animate.set_opacity(0.1), run_time=t * 0.25)
        self.wait(t * 0.35)


class A09_CensorLine(Scene):       # 6.09s — THE beat
    def construct(self):
        t = dur("A09", 6.09)
        r = np.random.default_rng(9)
        # lifespan bars on a timeline; 'today' at x = 3.4; bars start −5.6..1.5
        today = 3.4
        bars, crossing = VGroup(), []
        for k in range(9):
            y = 2.4 - k * 0.55                    # rows 2.4..−2.0, safe
            x0 = -5.6 + r.uniform(0, 6.5)
            length = r.uniform(2.0, 5.5)
            x1 = x0 + length
            runs_past = x1 > today
            bar = Line([x0, y, 0], [min(x1, today + 1.6), y, 0],
                       color=(NAVY if runs_past else INK), stroke_width=7)
            bars.add(bar)
            if runs_past:
                crossing.append(bar)
        self.play(AnimationGroup(*[Create(b) for b in bars], lag_ratio=0.08),
                  run_time=t * 0.35, rate_func=linear)
        wall = Line([today, 2.8, 0], [today, -2.5, 0], color=CRIMSON, stroke_width=7)
        wl = Text("today", font=SERIF, color=CRIMSON, font_size=24)
        wl.move_to([today, 3.1, 0])               # top ≈ 3.25 < 3.5 safe
        self.play(Create(wall), FadeIn(wl), run_time=t * 0.18, rate_func=linear)
        self.play(VGroup(*crossing).animate.set_opacity(0.08), run_time=t * 0.22)
        self.wait(t * 0.25)


class A10_Card(Scene):             # 7.78s
    def construct(self):
        _card(self, dur("A10", 7.78), "THE MECHANISM",
              "RIGHT-CENSORING", "the window hides the living")


class A11_JazzCentury(Scene):      # 7.47s — deaths at every age vs survivors
    def construct(self):
        t = dur("A11", 7.47)
        r = np.random.default_rng(13)
        jazz_lb = SerifLabel("jazz — a century of deaths, all ages", accent=NAVY, size=24)
        jazz_lb.move_to([-3.1, 2.7, 0])           # top ≈ 2.9 < 3.5 safe
        rap_lb = SerifLabel("rap — four decades, mostly survivors", accent=NAVY, size=24)
        rap_lb.move_to([3.2, 2.7, 0])
        jazz = VGroup(*[Square(0.15).set_fill(INK, 1).set_stroke(width=0)
                        .move_to([-5.4 + r.uniform(0, 4.6), r.uniform(-2.3, 1.9), 0])
                        for _ in range(34)])
        rap = VGroup()
        for _ in range(34):
            alive = r.uniform() < 0.8
            rap.add(Square(0.15).set_fill(NAVY if alive else INK, 1)
                    .set_stroke(width=0)
                    .move_to([1.0 + r.uniform(0, 4.6), r.uniform(-2.3, 1.9), 0]))
        divider = Line([0, -2.5, 0], [0, 2.3, 0], color=INK, stroke_width=2).set_opacity(0.4)
        self.play(FadeIn(jazz_lb), Create(divider), run_time=t * 0.15)
        self.play(AnimationGroup(*[FadeIn(m, scale=0.7) for m in jazz],
                                 lag_ratio=0.015, run_time=t * 0.3))
        self.play(FadeIn(rap_lb), run_time=t * 0.1)
        self.play(AnimationGroup(*[FadeIn(m, scale=0.7) for m in rap],
                                 lag_ratio=0.015, run_time=t * 0.3))
        self.wait(t * 0.15)


class A12_ChopTheWindow(Scene):    # 8.12s — the null model
    def construct(self):
        t = dur("A12", 8.12)
        # identical lifespans, staggered starts; the window chops the late ones
        L = 3.6                                   # every life the same length
        today = 3.4
        bars, avgs = VGroup(), VGroup()
        starts = [-5.6, -4.6, -3.6, -2.6, -1.6, -0.6, 0.4, 1.4]
        for k, x0 in enumerate(starts):
            y = 2.3 - k * 0.55                    # rows 2.3..−1.55, safe
            bar = Line([x0, y, 0], [x0 + L, y, 0], color=INK, stroke_width=7)
            if x0 + L > today:
                bar.set_color(NAVY)
            bars.add(bar)
        note = Text("every lifespan identical", font=SERIF, color=INK,
                    font_size=24, slant=ITALIC).move_to([-2.5, 3.0, 0])
        self.play(FadeIn(note), AnimationGroup(*[Create(b) for b in bars],
                  lag_ratio=0.08, run_time=t * 0.3), run_time=t * 0.3)
        wall = Line([today, 2.7, 0], [today, -2.0, 0], color=CRIMSON, stroke_width=7)
        self.play(Create(wall), run_time=t * 0.15, rate_func=linear)
        chopped = VGroup(*[b for b in bars if b.get_end()[0] > today])
        self.play(chopped.animate.set_opacity(0.08), run_time=t * 0.2)
        verdict = SerifLabel("the gap rebuilds itself", accent=TERRA, size=28)
        verdict.move_to([0, -2.9, 0])             # bottom ≈ −3.1 < 3.5 safe
        self.play(FadeIn(verdict, shift=UP * 0.1), run_time=t * 0.15)
        self.wait(t * 0.2)


class A13_Card(Scene):             # 8.31s
    def construct(self):
        _card(self, dur("A13", 8.31), "TO BE FAIR",
              "SHE FLAGGED IT", "but no caveat survives a screenshot")


class A14_Card(Scene):             # 7.76s — closer (outro law pads this beat)
    def construct(self):
        _card(self, dur("A14", 7.76), "THE RULE",
              "ASK HOW OLD THE CATEGORY IS", "before you mourn it")
