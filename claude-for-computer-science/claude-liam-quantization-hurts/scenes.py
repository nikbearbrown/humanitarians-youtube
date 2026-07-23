"""scenes.py — Manim for claude-liam-quantization-hurts. Source: embedded-ai Ch. 12"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


def _linemap(v, v0, v1, x0, x1):
    """Map v in [v0,v1] to pixel x in [x0,x1]."""
    return x0 + (v - v0) / (v1 - v0) * (x1 - x0)


class B01_WideRange(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Wide Range: Quantization Harmless", font_size=26, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        nline = Line(start=[-4.5, 0.8, 0], end=[4.5, 0.8, 0], color=INK, stroke_width=2)
        self.play(Create(nline))

        for v, lbl_txt in [(-1.5, "-1.5"), (0, "0"), (1.5, "1.5")]:
            x = _linemap(v, -1.8, 1.8, -4.5, 4.5)
            lbl = Text(lbl_txt, font_size=14, color=SOFT)
            lbl.move_to([x, 0.45, 0])
            tick = Line(start=[x, 0.7, 0], end=[x, 0.9, 0], color=INK, stroke_width=1.5)
            self.add(lbl, tick)

        # Float dots — spread across range
        float_vals = np.linspace(-1.5, 1.5, 10)
        float_dots = VGroup()
        for v in float_vals:
            x = _linemap(float(v), -1.8, 1.8, -4.5, 4.5)
            dot = Dot(point=[x, 1.2, 0], radius=0.09, color=SOFT, fill_opacity=0.85)
            float_dots.add(dot)
        self.play(FadeIn(float_dots))

        n_bins = 8
        grid_lines = VGroup()
        for i in range(n_bins + 1):
            v = -1.5 + i * (3.0 / n_bins)
            x = _linemap(v, -1.8, 1.8, -4.5, 4.5)
            gline = DashedLine(start=[x, 0.55, 0], end=[x, 1.05, 0],
                               color=GHOST, dash_length=0.08, stroke_width=1)
            grid_lines.add(gline)
        self.play(FadeIn(grid_lines))

        # Snapped dots — distinct bins
        snapped_dots = VGroup()
        for v in float_vals:
            bin_idx = int((float(v) - (-1.5)) / (3.0 / n_bins))
            bin_idx = max(0, min(n_bins - 1, bin_idx))
            snapped_v = -1.5 + (bin_idx + 0.5) * (3.0 / n_bins)
            x = _linemap(snapped_v, -1.8, 1.8, -4.5, 4.5)
            dot = Dot(point=[x, 0.1, 0], radius=0.09, color=SOFT, fill_opacity=0.9)
            snapped_dots.add(dot)
        self.play(FadeIn(snapped_dots))

        verdict = Text("Distinct floats map to distinct bins. Harmless.", font_size=16, color=SOFT)
        verdict.move_to([0, -0.7, 0])
        self.play(FadeIn(verdict))

        scale_note = Text("Range [-1.5, 1.5]: scale = 0.012, error < 0.005.", font_size=14, color=GHOST)
        scale_note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(scale_note))

        self.wait(1.2)


class B02_NarrowRange(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Narrow Range: Quantization Harmful", font_size=26, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        nline = Line(start=[-4.5, 0.8, 0], end=[4.5, 0.8, 0], color=INK, stroke_width=2)
        self.play(Create(nline))

        for v, lbl_txt in [(0.001, "0.001"), (0.005, "0.005"), (0.010, "0.010")]:
            x = _linemap(v, 0.0, 0.012, -4.5, 4.5)
            lbl = Text(lbl_txt, font_size=13, color=SOFT)
            lbl.move_to([x, 0.45, 0])
            tick = Line(start=[x, 0.7, 0], end=[x, 0.9, 0], color=INK, stroke_width=1.5)
            self.add(lbl, tick)

        # Float values in narrow range
        float_vals = np.linspace(0.001, 0.010, 12)
        float_dots = VGroup()
        for v in float_vals:
            x = _linemap(float(v), 0.0, 0.012, -4.5, 4.5)
            dot = Dot(point=[x, 1.2, 0], radius=0.08, color=SOFT, fill_opacity=0.8)
            float_dots.add(dot)
        self.play(FadeIn(float_dots))

        # Mash zone — terracotta highlight
        x_lo = _linemap(0.001, 0.0, 0.012, -4.5, 4.5)
        x_hi = _linemap(0.010, 0.0, 0.012, -4.5, 4.5)
        mash_zone = Rectangle(width=x_hi - x_lo, height=0.55, fill_color=ACC, fill_opacity=0.3, stroke_width=0)
        mash_zone.move_to([(x_lo + x_hi) / 2, 0.8, 0])
        self.play(FadeIn(mash_zone))

        mash_lbl = Text("MASH ZONE", font_size=14, color=ACC, weight="BOLD")
        mash_lbl.move_to([(x_lo + x_hi) / 2, 0.3, 0])
        self.play(FadeIn(mash_lbl))

        # Collapsed dots: only 3 bins
        n_bins = 3
        bin_centers_v = [0.001 + (i + 0.5) * (0.009 / n_bins) for i in range(n_bins)]
        collapse_dots = VGroup()
        for v in float_vals:
            bin_idx = min(int((float(v) - 0.001) / (0.009 / n_bins)), n_bins - 1)
            cv = bin_centers_v[bin_idx]
            x = _linemap(cv, 0.0, 0.012, -4.5, 4.5)
            dot = Dot(point=[x, -0.2, 0], radius=0.09, color=ACC, fill_opacity=0.9)
            collapse_dots.add(dot)
        self.play(FadeIn(collapse_dots))

        verdict = Text("12 distinct floats collapse to 3 bins. Information destroyed.", font_size=16, color=ACC)
        verdict.move_to([0, -1.0, 0])
        self.play(FadeIn(verdict))

        scale_note = Text("Range [0.001, 0.01]: scale = 0.000039 — values collapse.", font_size=14, color=GHOST)
        scale_note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(scale_note))

        self.wait(1.2)


class B03_Comparison(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Harmless vs Harmful Quantization", font_size=26, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Left box: harmless
        left_box = Rectangle(width=4.5, height=3.8, fill_color=SOFT, fill_opacity=0.1,
                             stroke_color=SOFT, stroke_width=1.5)
        left_box.move_to([-3.0, -0.2, 0])
        left_title = Text("Harmless", font_size=22, color=SOFT, weight="BOLD")
        left_title.next_to(left_box, UP, buff=0.15)
        self.play(FadeIn(left_box), FadeIn(left_title))

        left_items = [
            "Wide range: [-1.5, 1.5]",
            "256 bins span the range",
            "Distinct floats -> distinct bins",
            "Error < 0.005",
        ]
        for i, item in enumerate(left_items):
            lbl = Text(item, font_size=14, color=INK)
            lbl.move_to([-3.0, 0.9 - i * 0.65, 0])
            self.play(FadeIn(lbl), run_time=0.25)

        # Right box: harmful
        right_box = Rectangle(width=4.5, height=3.8, fill_color=ACC, fill_opacity=0.1,
                              stroke_color=ACC, stroke_width=1.5)
        right_box.move_to([3.0, -0.2, 0])
        right_title = Text("Harmful", font_size=22, color=ACC, weight="BOLD")
        right_title.next_to(right_box, UP, buff=0.15)
        self.play(FadeIn(right_box), FadeIn(right_title))

        right_items = [
            "Narrow range: [0.001, 0.01]",
            "Only 2-3 bins used",
            "Distinct floats -> same bin",
            "Information destroyed",
        ]
        for i, item in enumerate(right_items):
            color = ACC if i >= 1 else INK
            lbl = Text(item, font_size=14, color=color)
            lbl.move_to([3.0, 0.9 - i * 0.65, 0])
            self.play(FadeIn(lbl), run_time=0.25)

        note = Text("Narrow range + small-magnitude signal = quantization damage.", font_size=14, color=SOFT)
        note.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note))
        self.wait(1.2)
