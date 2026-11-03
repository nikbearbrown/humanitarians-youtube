"""
scenes.py -- Manim scenes for "SERS: Why a Whisper Becomes a Shout".

Two schematic diagrams support the video's two central claims:

    B02_PlasmonicHotspot   -- HOW the SERS enhancement mechanism works
                              (the electromagnetic "hot spot" between
                              two closely spaced metal nanoparticles)
    B03_SignalComparison   -- WHY the resulting sensitivity matters
                              (a qualitative magnitude comparison between
                              normal Raman scattering and SERS)

Both scenes are schematic by design: no field-strength values, intensity
numbers, or enhancement factors are drawn on screen. The video's spoken
claims (e.g. "up to a billion-fold") are supported separately in the
project's fact-check documentation, not illustrated as literal on-screen
statistics.

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


class B02_PlasmonicHotspot(Scene):
    """The mechanism beat: two metal nanoparticles set close together
    concentrate an incoming laser's field into the narrow gap between
    them (the "hot spot"). A molecule sitting in that gap scatters light
    far more strongly than it would anywhere else on the surface."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("The Hot Spot", size=32, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        # Two metal nanoparticles, drawn as solid ink-colored circles with
        # a deliberate small gap between them -- the gap is the subject.
        left_np = Circle(radius=1.35, color=INK, stroke_width=3,
                          fill_color=INK, fill_opacity=0.55).shift(LEFT * 1.9)
        right_np = Circle(radius=1.35, color=INK, stroke_width=3,
                           fill_color=INK, fill_opacity=0.55).shift(RIGHT * 1.9)
        left_lbl = _label("metal", size=18, color=CARD).move_to(left_np)
        right_lbl = _label("metal", size=18, color=CARD).move_to(right_np)

        self.play(Create(left_np), Create(right_np), FadeIn(left_lbl), FadeIn(right_lbl), run_time=1.0)

        # Incoming laser, aimed at the gap between the two nanoparticles.
        laser = Arrow(
            start=[-5.2, 2.5, 0], end=[0, 0.2, 0],
            color=INK, stroke_width=3.5, buff=0, tip_length=0.3,
        )
        laser_lbl = _label("laser", size=20, color=SOFT).next_to(laser.get_start(), UP, buff=0.15)
        self.play(GrowArrow(laser), FadeIn(laser_lbl), run_time=0.9)

        # The concentrated field itself, rendered as a soft accent-colored
        # glow rather than any specific intensity value.
        glow = Circle(radius=0.85, color=ACC, stroke_width=0,
                      fill_color=ACC, fill_opacity=0.4).move_to(ORIGIN)
        self.play(FadeIn(glow), run_time=0.6)

        # A single molecule sitting inside the hot spot.
        molecule = Dot(ORIGIN, color=ACC, radius=0.14)
        mol_lbl = _label("molecule", size=18, color=ACC).next_to(molecule, DOWN, buff=1.5)
        self.play(FadeIn(molecule), FadeIn(mol_lbl), run_time=0.5)

        # The amplified scattered signal leaving the hot spot -- drawn
        # larger and in the accent color to read as "boosted," without
        # attaching a literal enhancement-factor number to the arrow.
        signal = Arrow(
            start=[0, 0.2, 0], end=[4.6, 2.7, 0],
            color=ACC, stroke_width=6, buff=0, tip_length=0.4,
        )
        self.play(GrowArrow(signal), run_time=1.0)

        hotspot_lbl = _label("the electromagnetic hot spot", size=22, color=ACC, weight="BOLD"
                             ).move_to([0, -2.5, 0])
        self.play(FadeIn(hotspot_lbl), run_time=0.6)

        kicker = _label("the gap between metals is where it happens", size=20, weight="BOLD"
                        ).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(kicker), run_time=0.7)
        self.wait(0.4)


class B03_SignalComparison(Scene):
    """The importance beat: a qualitative side-by-side comparison showing
    that SERS produces a dramatically larger signal than normal Raman
    scattering. The bar heights and the scale-break mark communicate
    'orders of magnitude' without asserting a specific enhancement value."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Orders of Magnitude", size=32, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        baseline_y = -2.3

        # Normal Raman: a short bar, grown from a thin sliver so the
        # growth itself reads as an animation, not a static insert.
        raman_bar = Rectangle(width=1.7, height=0.01, color=SOFT,
                              fill_color=SOFT, fill_opacity=0.85, stroke_width=0
                              ).move_to([-2.6, baseline_y, 0]).align_to([-2.6, baseline_y, 0], DOWN)
        raman_target = Rectangle(width=1.7, height=0.9, color=SOFT,
                                 fill_color=SOFT, fill_opacity=0.85, stroke_width=0
                                 ).move_to([-2.6, baseline_y, 0]).align_to([-2.6, baseline_y, 0], DOWN)
        raman_lbl = _label("normal Raman", size=19, color=SOFT).next_to(raman_target, DOWN, buff=0.25)

        self.play(Create(Line([-5.2, baseline_y, 0], [5.2, baseline_y, 0], color=INK, stroke_width=2)),
                 run_time=0.5)
        self.play(Transform(raman_bar, raman_target), FadeIn(raman_lbl), run_time=1.0)

        # SERS: a much taller bar in the accent color.
        sers_bar = Rectangle(width=1.7, height=0.01, color=ACC,
                             fill_color=ACC, fill_opacity=0.9, stroke_width=0
                             ).move_to([2.6, baseline_y, 0]).align_to([2.6, baseline_y, 0], DOWN)
        sers_target = Rectangle(width=1.7, height=4.7, color=ACC,
                                fill_color=ACC, fill_opacity=0.9, stroke_width=0
                                ).move_to([2.6, baseline_y, 0]).align_to([2.6, baseline_y, 0], DOWN)
        sers_lbl = _label("SERS", size=22, color=ACC, weight="BOLD").next_to(sers_target, DOWN, buff=0.25)

        self.play(Transform(sers_bar, sers_target), run_time=1.4, rate_func=rate_functions.smooth)
        self.play(FadeIn(sers_lbl), run_time=0.4)

        # A small zigzag "scale break" mark on the tall bar signals that
        # the two bars are not drawn to a shared linear scale.
        break_y = baseline_y + 1.3
        break_mark = VGroup(
            Line([2.6 - 0.42, break_y, 0], [2.6 - 0.18, break_y + 0.2, 0], color=BG, stroke_width=4),
            Line([2.6 - 0.18, break_y + 0.2, 0], [2.6 + 0.06, break_y - 0.12, 0], color=BG, stroke_width=4),
            Line([2.6 + 0.06, break_y - 0.12, 0], [2.6 + 0.3, break_y + 0.12, 0], color=BG, stroke_width=4),
        )
        self.play(Create(break_mark), run_time=0.5)

        gap_lbl = _label("orders of magnitude", size=24, weight="BOLD"
                         ).move_to([0, 2.1, 0])
        self.play(FadeIn(gap_lbl), run_time=0.7)
        self.wait(0.4)
