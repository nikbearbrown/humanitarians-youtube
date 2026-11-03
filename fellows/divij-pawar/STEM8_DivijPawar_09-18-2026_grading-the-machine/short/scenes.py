"""short/scenes.py — 9:16 portrait re-layout of B01_SelfReportedConfidence only.

The parent reel's B01 is already mostly single-column (meter, then model
box with two lines stacked beneath it), so the portrait version reuses
that structure directly rather than restacking a horizontal layout — the
main changes are: positions pulled down slightly for extra clearance
under this title's bottom edge (measured at y≈2.89, not guessed), and
cap1 wrapped to two lines since its original single-line width (48
chars) exceeds the ~4.5-unit portrait frame.

All graphics (meter, model box, arrows) and their labels/captions are
enlarged ~50% from the original pass per feedback that the clip read too
small. Pure geometry (meter radius, dash/stroke widths, box padding)
scales a clean 1.5x. Text was capped below a literal 1.5x wherever the
measured width would have overflowed the ~4.5-unit frame — cap1, cap2,
and land got smaller bumps than the diagram elements for that reason;
every size/position below was verified by direct measurement.
"""
import numpy as np
from graphics_lib import *

BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


def confidence_meter(theta, radius=1.65):
    agree = Arc(radius=radius, start_angle=PI, angle=-PI, color=SOFT, stroke_width=9)
    pivot = Dot(ORIGIN, color=SOFT, radius=0.07)
    needle = Line(ORIGIN, radius * 0.8 * np.array([np.cos(theta), np.sin(theta), 0]),
                  color=ACC, stroke_width=6.5)
    return VGroup(agree, pivot, needle)


def model_box(text, color=INK):
    t = label(text, size=32, color=color, weight="BOLD", line_spacing=0.85)
    box = auto_box(t, h_pad=0.42, v_pad=0.33, color=color)
    return VGroup(box, t)


class B01_SelfReportedConfidence916(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Self-Reported Confidence", color=INK, size=30)
        self.play(Write(t), run_time=0.6)
        self.wait(1.6)

        meter = confidence_meter(PI / 2 - 0.15).move_to(UP * 1.1)
        qmark = label("?", size=36, color=SOFT).next_to(meter, UP, buff=0.12)
        pct = label("95% Confident", size=32, color=INK).next_to(meter, DOWN, buff=0.18)
        self.play(Create(meter), FadeIn(qmark), FadeIn(pct), run_time=0.7)
        self.wait(5.1)

        self.play(FadeOut(VGroup(meter, qmark, pct)), run_time=0.5)

        model = model_box("MODEL").move_to(UP * 1.3)
        ans = label('"the answer is 42"', size=32, color=INK).next_to(model, DOWN, buff=0.3)
        conf = label('"92% confident"', size=32, color=ACC).next_to(ans, DOWN, buff=0.24)
        self.play(FadeIn(model), run_time=0.5)
        self.wait(0.8)
        self.play(FadeIn(ans), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(conf), run_time=0.5)
        self.wait(1.6)

        arr1 = DashedLine(model.get_bottom() + LEFT * 0.3, ans.get_top(), color=SOFT,
                           stroke_width=2.2, dash_length=0.1)
        arr2 = DashedLine(model.get_bottom() + RIGHT * 0.3, conf.get_top(), color=SOFT,
                           stroke_width=2.2, dash_length=0.1)
        self.play(Create(arr1), Create(arr2), run_time=0.6)
        same_cap = label("same mechanism,\nboth times", size=32, color=SOFT, line_spacing=0.85)
        same_cap.next_to(conf, DOWN, buff=0.35)
        self.play(FadeIn(same_cap), run_time=0.5)
        self.wait(5.5)

        self.play(FadeOut(VGroup(model, ans, conf, arr1, arr2, same_cap)), run_time=0.6)
        # cap1/cap2/land kept closer to their original size than the
        # diagram elements above — measured: pushing them to a literal
        # 1.5x (e.g. cap1 at 36) overflowed the ~4.5-unit frame width for
        # these longer lines. Bumped as far as width allowed with margin.
        cap1 = label("no separate, more-honest\nmodule watching itself",
                      size=24, color=INK, line_spacing=0.9)
        cap1.move_to(UP * 0.3)
        self.play(FadeIn(cap1), run_time=0.5)
        self.wait(5.5)

        self.play(FadeOut(cap1), run_time=0.3)
        cap2 = label("measures how confident\nit sounds — not how\nwell-founded it is",
                      size=25, color=SOFT, line_spacing=0.85)
        cap2.move_to(UP * 0.3)
        self.play(FadeIn(cap2), run_time=0.4)
        self.wait(5.5)

        self.play(FadeOut(cap2), run_time=0.4)
        land = serif("Those two things correlate\nloosely at best.",
                      size=29, color=ACC, line_spacing=1.0).move_to(DOWN * 0.2)
        self.play(Write(land), run_time=0.9)
        self.wait(5.35)
