"""vox_scenes.py — Equilibrium is just counting: the peak becomes a needle
(vox-multiplicity-peak, slate cut, 16:9).
Color law: TEAL=peak/equilibrium; CRIMSON=off-peak; GOLD=peak marker.
Exclusions: no Stirling formula.
"""
import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np
from math import comb, log

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


def _dur(bid, fallback=8.0):
    return DUR.get(bid, fallback)


def _binomial_bars(N, ax_width=10.0, ax_height=4.0, center=(0.0, -0.3)):
    """Build a VGroup of bars for the binomial distribution Omega(N, k)."""
    vals = np.array([comb(N, k) for k in range(N + 1)], dtype=float)
    vals_norm = vals / vals.max()
    n_bars = N + 1
    bar_width = ax_width / n_bars * 0.85
    grp = VGroup()
    peak_k = N // 2
    for k, v in enumerate(vals_norm):
        h = v * ax_height
        x = center[0] - ax_width / 2 + (k + 0.5) * ax_width / n_bars
        y = center[1] - ax_height / 2 + h / 2
        col = TEAL if abs(k - peak_k) <= max(1, N // 10) else CRIMSON
        bar = Rectangle(width=bar_width, height=max(h, 0.02), color=col, fill_opacity=0.75)
        bar.set_stroke(col, width=0.5)
        bar.move_to(RIGHT * x + UP * y)
        grp.add(bar)
    return grp


def _axis_frame(ax_width=10.0, ax_height=4.0, center=(0.0, -0.3)):
    """Axis frame lines for bar chart."""
    cx, cy = center
    bottom = cy - ax_height / 2
    left = cx - ax_width / 2
    right = cx + ax_width / 2
    hline = Line(RIGHT * left + UP * bottom, RIGHT * right + UP * bottom,
                 color=INK, stroke_width=1.2)
    vline = Line(RIGHT * left + UP * bottom, RIGHT * left + UP * (bottom + ax_height + 0.3),
                 color=INK, stroke_width=1.2)
    return VGroup(hline, vline)


# ── B01 CARD ──────────────────────────────────────────────────────────────────
class B01_TitleCard(Scene):
    def construct(self):
        d = _dur("B01", 9.0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE, font_size=22, weight="MEDIUM")
        eyebrow.move_to(UP * 1.8)
        title = Text("Equilibrium is just counting:\nthe peak becomes a needle",
                     font=DISPLAY, color=INK, font_size=32, weight="BOLD", line_spacing=1.2)
        title.move_to(ORIGIN)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title), run_time=0.8)
        self.wait(d - 1.3)


# ── B02 CARD — THE QUESTION ───────────────────────────────────────────────────
class B02_TheQuestion(Scene):
    def construct(self):
        d = _dur("B02", 11.0)
        chip = LabelChip("THE QUESTION", accent=CRIMSON, size=24)
        chip.move_to(UP * 2.8)
        line1 = Text("Why does every system drift toward equilibrium",
                     font=SERIF, color=INK, font_size=26)
        line1.move_to(UP * 0.6)
        line2 = Text("and never come back?", font=SERIF, color=CRIMSON, font_size=26)
        line2.move_to(DOWN * 0.2)
        line3 = Text("What force pushes it there?", font=SERIF, color=INK, font_size=24, slant=ITALIC)
        line3.move_to(DOWN * 1.2)
        self.play(FadeIn(chip), run_time=0.4)
        self.play(FadeIn(line1), run_time=0.4)
        self.play(FadeIn(line2), run_time=0.4)
        self.play(FadeIn(line3), run_time=0.4)
        self.wait(d - 1.6)


# ── B03 GRAPHIC — N=6 bar chart builds up ─────────────────────────────────────
class B03_N6Bars(Scene):
    def construct(self):
        d = _dur("B03", 12.0)
        ax = _axis_frame(ax_width=8.0, ax_height=4.0, center=(0.0, -0.2))
        bars = _binomial_bars(6, ax_width=8.0, ax_height=4.0, center=(0.0, -0.2))
        n_label = Text("N = 6 coins", font=MONO, color=INK, font_size=22)
        n_label.move_to(UP * 2.8)
        peak_label = Text("peak at half-and-half", font=SERIF, color=TEAL, font_size=22)
        peak_label.move_to(UP * 2.3)

        # Reveal bars one by one (7 bars for N=6)
        n_bars = len(bars)
        step = (d - 0.3) / (n_bars + 2)
        self.play(Create(ax), FadeIn(n_label), run_time=0.3)
        for bar in bars:
            self.play(FadeIn(bar), run_time=step)
        self.play(FadeIn(peak_label), run_time=step * 2)


# ── B04 GRAPHIC — N=20 bars ───────────────────────────────────────────────────
class B04_N20Bars(Scene):
    def construct(self):
        d = _dur("B04", 10.0)
        ax = _axis_frame(ax_width=10.0, ax_height=4.0)
        bars_n6 = _binomial_bars(6, ax_width=10.0, ax_height=4.0)
        bars_n20 = _binomial_bars(20, ax_width=10.0, ax_height=4.0)
        n_label_6 = Text("N = 6", font=MONO, color=INK, font_size=22)
        n_label_6.move_to(UP * 2.8)
        n_label_20 = Text("N = 20", font=MONO, color=TEAL, font_size=22)
        n_label_20.move_to(UP * 2.4)
        note = Text("peak narrows — extremes rarer", font=SERIF, color=TEAL, font_size=22)
        note.move_to(DOWN * 2.8)

        # Peak markers (vertical lines at peak position)
        peak_line_6 = Line(UP * 1.8, DOWN * 0.3, color=TEAL, stroke_width=2.5)
        peak_line_6.move_to(ORIGIN + DOWN * 0.3)
        peak_line_20 = Line(UP * 2.0, DOWN * 0.3, color=TEAL, stroke_width=2.5)
        peak_line_20.move_to(ORIGIN + DOWN * 0.3)
        width_arrow_6 = DoubleArrow(LEFT * 2.5 + DOWN * 2.0, RIGHT * 2.5 + DOWN * 2.0,
                                    buff=0, stroke_width=2, color=CRIMSON,
                                    max_tip_length_to_length_ratio=0.15)
        width_arrow_20 = DoubleArrow(LEFT * 1.5 + DOWN * 2.0, RIGHT * 1.5 + DOWN * 2.0,
                                     buff=0, stroke_width=2, color=TEAL,
                                     max_tip_length_to_length_ratio=0.15)

        # Extra highlight rectangle for equilibrium region
        equil_box = Rectangle(width=1.8, height=4.2, color=TEAL, fill_opacity=0.1)
        equil_box.set_stroke(TEAL, width=1.5)
        equil_box.move_to(ORIGIN + DOWN * 0.3)

        step = (d - 0.3) / 7
        self.play(Create(ax), FadeIn(n_label_6), run_time=0.3)
        self.play(FadeIn(bars_n6), run_time=step)
        self.play(FadeIn(peak_line_6), FadeIn(width_arrow_6), run_time=step)
        self.play(Transform(bars_n6, bars_n20), FadeOut(n_label_6), FadeIn(n_label_20),
                  run_time=step)
        self.play(Transform(peak_line_6, peak_line_20), Transform(width_arrow_6, width_arrow_20),
                  run_time=step)
        self.play(FadeIn(equil_box), run_time=step)
        self.play(FadeIn(note), run_time=step * 2)


# ── B05 GRAPHIC — N=100 spike ─────────────────────────────────────────────────
class B05_N100Spike(Scene):
    def construct(self):
        d = _dur("B05", 12.0)
        ax = _axis_frame(ax_width=10.0, ax_height=4.0)
        bars_n20 = _binomial_bars(20, ax_width=10.0, ax_height=4.0)
        bars_n50 = _binomial_bars(50, ax_width=10.0, ax_height=4.0)
        bars_n100 = _binomial_bars(100, ax_width=10.0, ax_height=4.0)

        n_label = Text("N = 20", font=MONO, color=INK, font_size=22)
        n_label.move_to(UP * 2.8)
        n_label_50 = Text("N = 50", font=MONO, color=INK, font_size=22)
        n_label_50.move_to(UP * 2.4)
        n_label_100 = Text("N = 100", font=MONO, color=TEAL, font_size=22)
        n_label_100.move_to(UP * 2.0)
        spike_note = Text("sharp spike — near-equil. states dominate", font=SERIF,
                          color=TEAL, font_size=21)
        spike_note.move_to(DOWN * 2.8)

        # Width markers
        width_broad = DoubleArrow(LEFT * 3.5 + DOWN * 2.1, RIGHT * 3.5 + DOWN * 2.1,
                                  buff=0, stroke_width=2, color=CRIMSON,
                                  max_tip_length_to_length_ratio=0.1)
        width_medium = DoubleArrow(LEFT * 2.2 + DOWN * 2.1, RIGHT * 2.2 + DOWN * 2.1,
                                   buff=0, stroke_width=2, color=CRIMSON,
                                   max_tip_length_to_length_ratio=0.1)
        width_narrow = DoubleArrow(LEFT * 0.9 + DOWN * 2.1, RIGHT * 0.9 + DOWN * 2.1,
                                   buff=0, stroke_width=2, color=TEAL,
                                   max_tip_length_to_length_ratio=0.15)

        # Peak highlight box
        peak_box = Rectangle(width=1.5, height=4.2, color=TEAL, fill_opacity=0.15)
        peak_box.set_stroke(TEAL, width=1.5)
        peak_box.move_to(ORIGIN + DOWN * 0.3)

        step = (d - 0.3) / 6
        self.play(Create(ax), FadeIn(n_label), run_time=0.3)
        self.play(FadeIn(bars_n20), FadeIn(width_broad), run_time=step)
        self.play(Transform(bars_n20, bars_n50), FadeOut(n_label), FadeIn(n_label_50),
                  Transform(width_broad, width_medium), run_time=step)
        self.play(Transform(bars_n20, bars_n100), FadeOut(n_label_50), FadeIn(n_label_100),
                  Transform(width_broad, width_narrow), run_time=step)
        self.play(FadeIn(peak_box), run_time=step)
        self.play(FadeIn(spike_note), run_time=step * 2)


# ── B06 GRAPHIC — knife-edge: arrow showing width shrinking ───────────────────
class B06_KnifeEdge(Scene):
    def construct(self):
        d = _dur("B06", 12.0)

        # Three bar charts side by side at different scales, showing shrinking
        charts = [
            (_binomial_bars(10, ax_width=2.5, ax_height=3.0, center=(-5.0, -0.3)),
             Text("N=10", font=MONO, color=INK, font_size=18), -5.0),
            (_binomial_bars(30, ax_width=2.5, ax_height=3.0, center=(0.0, -0.3)),
             Text("N=30", font=MONO, color=INK, font_size=18), 0.0),
            (_binomial_bars(100, ax_width=2.5, ax_height=3.0, center=(5.0, -0.3)),
             Text("N=100", font=MONO, color=TEAL, font_size=18), 5.0),
        ]

        axes = VGroup()
        for _, lbl, cx in charts:
            ax = _axis_frame(ax_width=2.5, ax_height=3.0, center=(cx, -0.3))
            axes.add(ax)

        arrows_down = VGroup()
        for _, lbl, cx in charts:
            arr = Arrow(RIGHT * cx + UP * 2.6, RIGHT * cx + UP * 1.5,
                        buff=0, stroke_width=2, color=SLATE,
                        max_tip_length_to_length_ratio=0.3)
            arrows_down.add(arr)

        knife_note = Text("N = 10^23: knife-edge — all states are near the peak",
                          font=SERIF, color=TEAL, font_size=20)
        knife_note.move_to(DOWN * 2.8)

        step = (d - 0.3) / 6
        self.play(FadeIn(axes), run_time=0.3)
        for bars, lbl, cx in charts:
            lbl.move_to(RIGHT * cx + UP * 3.2)
            self.play(FadeIn(bars), FadeIn(lbl), run_time=step)
        self.play(FadeIn(arrows_down), run_time=step)
        self.play(FadeIn(knife_note), run_time=step * 2)


# ── B07 GRAPHIC — second law = law of large numbers ───────────────────────────
class B07_SecondLaw(Scene):
    def construct(self):
        d = _dur("B07", 10.0)

        bars = _binomial_bars(50, ax_width=10.0, ax_height=4.0)
        ax = _axis_frame(ax_width=10.0, ax_height=4.0)

        # Arrow pointing to peak
        peak_arrow = Arrow(UP * 2.5, UP * 0.8, buff=0, color=TEAL, stroke_width=3,
                           max_tip_length_to_length_ratio=0.2)
        peak_dot = Dot(UP * 0.8, color=TEAL, radius=0.12)

        # Wide annotation span (line with tick marks)
        peak_span = Line(LEFT * 0.8 + DOWN * 1.8, RIGHT * 0.8 + DOWN * 1.8,
                         color=TEAL, stroke_width=2)
        tick_l = Line(LEFT * 0.8 + DOWN * 1.6, LEFT * 0.8 + DOWN * 2.0,
                      color=TEAL, stroke_width=2)
        tick_r = Line(RIGHT * 0.8 + DOWN * 1.6, RIGHT * 0.8 + DOWN * 2.0,
                      color=TEAL, stroke_width=2)
        peak_region = VGroup(peak_span, tick_l, tick_r)

        label_law = Text("peak = almost all states", font=SERIF, color=TEAL, font_size=22)
        label_law.move_to(DOWN * 2.5)
        label_law2 = Text("second law = going to where counts are highest",
                          font=SERIF, color=INK, font_size=20, slant=ITALIC)
        label_law2.move_to(DOWN * 3.1)

        # Highlight rectangles for off-peak regions
        left_rect = Rectangle(width=3.5, height=4.0, color=CRIMSON, fill_opacity=0.08)
        left_rect.set_stroke(CRIMSON, width=0)
        left_rect.move_to(LEFT * 3.5 + DOWN * 0.3)
        right_rect = Rectangle(width=3.5, height=4.0, color=CRIMSON, fill_opacity=0.08)
        right_rect.set_stroke(CRIMSON, width=0)
        right_rect.move_to(RIGHT * 3.5 + DOWN * 0.3)
        peak_box = Rectangle(width=2.5, height=4.0, color=TEAL, fill_opacity=0.10)
        peak_box.set_stroke(TEAL, width=1.5)
        peak_box.move_to(ORIGIN + DOWN * 0.3)

        # Entropy arrow: increasing along bottom
        entropy_arrow = Arrow(LEFT * 4.5 + DOWN * 3.0, RIGHT * 4.5 + DOWN * 3.0,
                              buff=0, stroke_width=3, color=TEAL,
                              max_tip_length_to_length_ratio=0.1)

        step = (d - 0.3) / 7
        self.play(Create(ax), FadeIn(bars), run_time=0.3)
        self.play(FadeIn(peak_arrow), FadeIn(peak_dot), run_time=step)
        self.play(FadeIn(left_rect), FadeIn(right_rect), run_time=step)
        self.play(FadeIn(peak_box), FadeIn(peak_region), run_time=step)
        self.play(FadeIn(label_law), run_time=step)
        self.play(FadeIn(entropy_arrow), run_time=step)
        self.play(FadeIn(label_law2), run_time=step)


# ── B09 GRAPHIC — illustrative: N=6 exact values ─────────────────────────────
class B09_N6Exact(Scene):
    def construct(self):
        d = _dur("B09", 12.0)

        title = Text("Illustrative: N=6 coins, exact multiplicity",
                     font=SERIF, color=INK, font_size=22, slant=ITALIC)
        title.move_to(UP * 3.2)

        rows = [
            (0, "all tails", 1, CRIMSON),
            (1, "one head", 6, CRIMSON),
            (2, "two heads", 15, CRIMSON),
            (3, "three heads", 20, TEAL),
            (4, "four heads", 15, CRIMSON),
            (5, "five heads", 6, CRIMSON),
            (6, "all heads", 1, CRIMSON),
        ]
        ys = np.linspace(2.3, -2.3, 7)

        row_bars_shapes = []
        row_groups = []
        for (k, desc, count, col), y in zip(rows, ys):
            bar_w = count * 0.28
            bar = Rectangle(width=bar_w, height=0.28, color=col, fill_opacity=0.65)
            bar.set_stroke(col, width=0)
            bar.move_to(RIGHT * (3.5 + bar_w / 2 - 3.0) + UP * y)
            row_bars_shapes.append(bar)
            k_t = Text(f"k={k}", font=MONO, color=col, font_size=18)
            k_t.move_to(LEFT * 4.5 + UP * y)
            d_t = Text(desc, font=SERIF, color=col, font_size=18)
            d_t.move_to(LEFT * 2.0 + UP * y)
            c_t = Text(str(count), font=DISPLAY, color=col, font_size=22, weight="BOLD")
            c_t.move_to(RIGHT * 2.5 + UP * y)
            row_groups.append(VGroup(k_t, d_t, c_t))

        peak_highlight = Rectangle(width=12.0, height=0.38, color=TEAL, fill_opacity=0.12)
        peak_highlight.set_stroke(TEAL, width=1.5)
        peak_highlight.move_to(UP * ys[3])

        total_label = Text("Total: 64 arrangements.  Peak: 20/64 = 31%",
                           font=SERIF, color=TEAL, font_size=20)
        total_label.move_to(DOWN * 3.0)

        step = (d - 0.3) / 9
        self.play(FadeIn(title), run_time=0.3)
        for bar, rg in zip(row_bars_shapes, row_groups):
            self.play(FadeIn(bar), FadeIn(rg), run_time=step)
        self.play(FadeIn(peak_highlight), run_time=step)
        self.play(FadeIn(total_label), run_time=step)


# ── B10 CARD — RECAP ──────────────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        d = _dur("B10", 9.0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE, font_size=22, weight="MEDIUM")
        eyebrow.move_to(UP * 2.5)
        answer = Text("Equilibrium = peak of multiplicity.\nPeak sharpens with N.\nSecond law = arithmetic.",
                      font=SERIF, color=INK, font_size=24, line_spacing=1.3)
        answer.move_to(ORIGIN)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(answer), run_time=0.8)
        self.wait(d - 1.3)
