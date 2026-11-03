"""
scenes.py -- Manim scenes for "Why SERS Needs Machine Learning".

Two schematic diagrams support the video's central research argument:

    B02_InconsistentHotspots -- THE PROBLEM: SERS hot spots form almost
                                 randomly, so the same molecule can
                                 produce visibly different signal
                                 strength from one measurement to the next
    B03_MLPipeline            -- THE SOLUTION: a trained model can learn
                                 the underlying pattern across many noisy,
                                 inconsistent measurements and still
                                 produce a reliable identification

Both scenes are schematic by design: bar heights and pipeline flow
represent the shape of the argument, not measured intensity or accuracy
values. No specific numbers are drawn on screen for either claim.

Palette: cream #F2F0E9 background, warm ink #3D3929 for structure and
body text, terracotta #D97757 as the single accent color per scene.
"""
from manim import *

BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#6E6A57")
GHOST = ManimColor("#A8A491")
CARD  = ManimColor("#FFFFFF")


def _label(text, size=22, color=None, weight=None):
    """Shared text-styling helper so every label in this file uses the
    same font-size/color/weight conventions instead of repeating them."""
    kw = {"font_size": size, "color": color or INK}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw)


class B02_InconsistentHotspots(Scene):
    """The problem beat: three bars, representing three repeated
    measurements of the same molecule, grow to visibly different
    heights -- illustrating that SERS hot-spot formation is inconsistent
    enough to produce genuinely different-looking results from run to
    run, even with nothing else changed."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Same Molecule, Three Different Answers", size=30, weight="BOLD"
                       ).to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=1.0)
        self.wait(0.5)

        baseline_y = -1.6
        xs = [-3.2, 0.0, 3.2]
        heights = [0.7, 2.6, 1.3]  # deliberately uneven -- the inconsistency is the point
        labels = ["attempt 1", "attempt 2", "attempt 3"]
        colors = [SOFT, ACC, SOFT]

        bars = []
        for x, h, lbl, col in zip(xs, heights, labels, colors):
            bar0 = Rectangle(width=1.3, height=0.01, color=col,
                             fill_color=col, fill_opacity=0.8, stroke_width=0
                             ).move_to([x, baseline_y, 0]).align_to([x, baseline_y, 0], DOWN)
            bar_t = Rectangle(width=1.3, height=h, color=col,
                              fill_color=col, fill_opacity=0.8, stroke_width=0
                              ).move_to([x, baseline_y, 0]).align_to([x, baseline_y, 0], DOWN)
            name = _label(lbl, size=16, color=SOFT).next_to(bar_t, DOWN, buff=0.2)
            bars.append((bar0, bar_t, name))

        self.play(Create(Line([-4.4, baseline_y, 0], [4.4, baseline_y, 0], color=INK, stroke_width=1.8)),
                 run_time=0.6)
        self.wait(0.4)
        for bar0, bar_t, name in bars:
            self.play(Transform(bar0, bar_t), FadeIn(name), run_time=1.1, rate_func=rate_functions.smooth)
            self.wait(0.3)

        kicker = _label("hot spots form almost randomly", size=22, weight="BOLD"
                        ).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(kicker), run_time=1.0)
        self.wait(2.0)


class B03_MLPipeline(Scene):
    """The solution beat: three jagged, noisy spectrum lines flow into an
    ML model box and emerge as a single clean result card -- illustrating
    that a trained model can find the reliable signal underneath
    inconsistent, noisy real-world measurements."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Where Machine Learning Fits", size=30, weight="BOLD"
                       ).to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=1.0)
        self.wait(0.5)

        # Three noisy spectrum lines, hand-built as jagged zigzags rather
        # than real data -- the shape of "noisy," not a measured spectrum.
        spectra = VGroup()
        ys = [1.3, 0.0, -1.3]
        for y in ys:
            pts = []
            for i in range(14):
                xi = -5.4 + i * 0.18
                yi = y + (0.18 if i % 2 == 0 else -0.15)
                pts.append([xi, yi, 0])
            line = VMobject(color=SOFT, stroke_width=2.2)
            line.set_points_as_corners(pts)
            spectra.add(line)
        self.play(*[Create(s) for s in spectra], run_time=1.4)
        self.wait(0.4)

        # The three noisy inputs converge into a single model box.
        model_box = Rectangle(width=2.0, height=2.4, color=INK, stroke_width=2.5,
                              fill_color=CARD, fill_opacity=1).move_to([-1.0, 0, 0])
        model_lbl = _label("ML\nmodel", size=20, weight="BOLD").move_to(model_box)
        arrows_in = VGroup(*[
            Arrow(start=[-3.6, y, 0], end=[-2.05, 0, 0], color=INK, stroke_width=2, tip_length=0.18)
            for y in ys
        ])
        self.play(Create(model_box), FadeIn(model_lbl), run_time=0.8)
        self.play(*[GrowArrow(a) for a in arrows_in], run_time=1.0)
        self.wait(0.5)

        # A single clean output: one reliable identification, in the
        # accent color to read as the resolved, trustworthy result.
        out_arrow = Arrow(start=[0.05, 0, 0], end=[1.6, 0, 0], color=ACC, stroke_width=3, tip_length=0.22)
        result_card = Rectangle(width=2.6, height=1.3, color=ACC, stroke_width=2.5,
                                fill_color=CARD, fill_opacity=1).move_to([3.4, 0, 0])
        result_lbl = _label("reliable\nidentification", size=17, color=ACC, weight="BOLD"
                            ).move_to(result_card)
        self.play(GrowArrow(out_arrow), run_time=0.8)
        self.play(Create(result_card), FadeIn(result_lbl), run_time=0.9)
        self.wait(0.5)

        kicker = _label("learning the pattern across noisy data", size=21, weight="BOLD"
                        ).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(kicker), run_time=1.0)
        self.wait(2.0)
