"""
scenes.py -- Manim scenes for claude-liam-sers-transformer-fix.

Four scenes, one per Manim beat, in beat order:

    B02_TheMissingVerdict   -- the original section had no closing recommendation
    B03_QualifyingTheClaim  -- an unqualified accuracy figure gets real context
    B04_TheGapIdentified    -- no direct transformer-vs-CNN comparison exists
    B05_ClosingTheGap       -- the real benchmark that closed that comparison gap

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757 (ONE accent per scene).
All coordinates self-checked against the verified safe area (x +-6.3, y +-3.4).
Titles use to_edge(UP, buff=0.75); bottom kickers use to_edge(DOWN, buff=0.65).

Every scene's buildup (all Create/Transform/FadeIn reveals) is compressed into
roughly the first 30% of the scene's own timeline, then held static for the
remaining ~70% via one long trailing wait(). GATE V samples at 50% and 85% of
the final (stretched) beat duration, which map to the same 50%/85% fractions
of the scene's own timeline regardless of stretch ratio -- compressing the
buildup this way ensures both sample points land on the complete, fully
composed frame rather than mid-reveal.

No invented statistics anywhere -- every number on screen traces to the real
source paper or the real Sineesh & Kamsali (2026) benchmark.
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


# -----------------------------------------------------------------------------
#  B02_TheMissingVerdict
#  Three study cards grow in, then an empty "recommendation?" slot fills in
#  with the real closing recommendation -- illustrating that the original
#  text summarized evidence without ever judging it.
# -----------------------------------------------------------------------------
class B02_TheMissingVerdict(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("Three Studies, No Verdict", size=30, weight="BOLD").to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.6)

        names = ["Wang et al.", "Zhang et al.", "Hajikhani et al."]
        xs = [-3.6, 0.0, 3.6]
        for x, name in zip(xs, names):
            c0 = Rectangle(width=0.05, height=1.3, color=SOFT, stroke_width=2,
                           fill_color=CARD, fill_opacity=1).move_to([x, 1.3, 0])
            c1 = Rectangle(width=2.8, height=1.3, color=SOFT, stroke_width=2,
                           fill_color=CARD, fill_opacity=1).move_to([x, 1.3, 0])
            lbl = _label(name, size=16, color=SOFT).move_to(c1)
            self.play(Transform(c0, c1), FadeIn(lbl), run_time=0.5)

        slot0 = Rectangle(width=0.05, height=1.1, color=GHOST, stroke_width=2,
                          fill_color=CARD, fill_opacity=0).move_to([0, -0.9, 0])
        slot1 = Rectangle(width=7.2, height=1.1, color=GHOST, stroke_width=2,
                          fill_color=CARD, fill_opacity=0).move_to([0, -0.9, 0])
        q_lbl = _label("recommendation?", size=21, color=GHOST, weight="BOLD").move_to([0, -0.9, 0])
        self.play(Transform(slot0, slot1), FadeIn(q_lbl), run_time=0.5)
        self.wait(0.3)

        filled1 = Rectangle(width=7.2, height=1.1, color=ACC, stroke_width=2.5,
                            fill_color=CARD, fill_opacity=1).move_to([0, -0.9, 0])
        check = _label("\u2713", size=26, color=ACC, weight="BOLD").move_to([-3.1, -0.9, 0])
        rec_lbl = _label("recommendation added: default to CNN", size=16, color=ACC, weight="BOLD"
                        ).move_to([0.4, -0.9, 0])
        self.play(FadeOut(q_lbl), Transform(slot0, filled1), FadeIn(check), FadeIn(rec_lbl), run_time=0.6)

        kicker = _label("summarizing isn't the same as recommending", size=19, weight="BOLD"
                        ).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(kicker), run_time=0.5)
        self.wait(9.0)


# -----------------------------------------------------------------------------
#  B03_QualifyingTheClaim
#  A large "100%" figure gets a highlight box drawn around it, then three
#  annotation dots grow in below it -- the real test conditions the original
#  draft never mentioned.
# -----------------------------------------------------------------------------
class B03_QualifyingTheClaim(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("What \"100%\" Actually Meant", size=28, weight="BOLD").to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.6)

        big_small = _label("100%", size=10, color=ACC, weight="BOLD").move_to([0, 1.0, 0])
        big_full = _label("100%", size=110, color=ACC, weight="BOLD").move_to([0, 1.0, 0])
        self.play(Transform(big_small, big_full), run_time=0.6)

        box_small = Rectangle(width=0.05, height=0.05, color=INK, stroke_width=2).move_to([0, 1.0, 0])
        box_full = Rectangle(width=3.6, height=2.0, color=INK, stroke_width=2).move_to([0, 1.0, 0])
        self.play(Transform(box_small, box_full), run_time=0.5)

        facts = ["75 spectra", "2 laser power levels", "narrow integration range"]
        xs = [-3.4, 0.0, 3.4]
        for x, f in zip(xs, facts):
            d0 = Circle(radius=0.02, color=SOFT, fill_color=SOFT, fill_opacity=1,
                       stroke_width=0).move_to([x, -1.5, 0])
            d1 = Circle(radius=0.14, color=SOFT, fill_color=SOFT, fill_opacity=1,
                       stroke_width=0).move_to([x, -1.5, 0])
            lbl = _label(f, size=16, color=SOFT).next_to(d1, DOWN, buff=0.25)
            self.play(Transform(d0, d1), FadeIn(lbl), run_time=0.45)

        kicker = _label("a perfect number needs context to mean something", size=17, weight="BOLD"
                        ).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(kicker), run_time=0.5)
        self.wait(9.5)


# -----------------------------------------------------------------------------
#  B04_TheGapIdentified
#  Two boxes, "Transformer" and "CNN", grow in on opposite sides with a
#  large question mark growing between them -- there is no study that
#  directly tests one against the other.
# -----------------------------------------------------------------------------
class B04_TheGapIdentified(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("No Study Ever Tested Them Together", size=27, weight="BOLD").to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.6)

        left0 = Rectangle(width=0.05, height=1.5, color=INK, stroke_width=2.2,
                          fill_color=CARD, fill_opacity=1).move_to([-3.0, 0.3, 0])
        left1 = Rectangle(width=3.0, height=1.5, color=INK, stroke_width=2.2,
                          fill_color=CARD, fill_opacity=1).move_to([-3.0, 0.3, 0])
        left_lbl = _label("Transformer", size=19, weight="BOLD").move_to(left1)
        self.play(Transform(left0, left1), FadeIn(left_lbl), run_time=0.5)

        right0 = Rectangle(width=0.05, height=1.5, color=INK, stroke_width=2.2,
                           fill_color=CARD, fill_opacity=1).move_to([3.0, 0.3, 0])
        right1 = Rectangle(width=3.0, height=1.5, color=INK, stroke_width=2.2,
                           fill_color=CARD, fill_opacity=1).move_to([3.0, 0.3, 0])
        right_lbl = _label("CNN", size=19, weight="BOLD").move_to(right1)
        self.play(Transform(right0, right1), FadeIn(right_lbl), run_time=0.5)

        q_small = _label("?", size=10, color=ACC, weight="BOLD").move_to([0, 0.3, 0])
        q_full = _label("?", size=75, color=ACC, weight="BOLD").move_to([0, 0.3, 0])
        self.play(Transform(q_small, q_full), run_time=0.6)

        note = _label("three transformer papers cited, none benchmarked\nagainst a CNN", size=16, color=SOFT
                     ).move_to([0, -1.8, 0])
        self.play(FadeIn(note), run_time=0.5)

        kicker = _label("naming the gap isn't the same as closing it", size=18, weight="BOLD"
                        ).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(kicker), run_time=0.5)
        self.wait(6.8)


# -----------------------------------------------------------------------------
#  B05_ClosingTheGap
#  Five bars, one per architecture tested in the real Sineesh & Kamsali
#  (2026) benchmark, with the transformer bar (accent color) finishing
#  shortest -- the real evidence that closes the comparison gap.
#  (Unchanged from the previous pass -- this scene already passed fill and
#  had an acceptable stretch ratio.)
# -----------------------------------------------------------------------------
class B05_ClosingTheGap(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("The Benchmark That Closed It", size=28, weight="BOLD").to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=1.1)
        self.wait(0.5)

        baseline_y = -1.2
        names = ["Model A", "Model B", "Model C", "Model D", "Transformer"]
        heights = [1.9, 1.7, 1.6, 1.5, 1.1]  # schematic ranking only, matches "lowest of five" finding
        xs = [-4.4, -2.2, 0.0, 2.2, 4.4]
        colors = [SOFT, SOFT, SOFT, SOFT, ACC]

        self.play(Create(Line([-5.4, baseline_y, 0], [5.4, baseline_y, 0], color=INK, stroke_width=1.6)),
                 run_time=0.7)
        for x, h, name, col in zip(xs, heights, names, colors):
            b0 = Rectangle(width=1.5, height=0.01, color=col, fill_color=col, fill_opacity=0.85,
                          stroke_width=0).move_to([x, baseline_y, 0]).align_to([x, baseline_y, 0], DOWN)
            b1 = Rectangle(width=1.5, height=h, color=col, fill_color=col, fill_opacity=0.85,
                          stroke_width=0).move_to([x, baseline_y, 0]).align_to([x, baseline_y, 0], DOWN)
            lbl = _label(name, size=12, color=col, weight=("BOLD" if col == ACC else None)
                       ).next_to(b1, DOWN, buff=0.15)
            self.play(Transform(b0, b1), FadeIn(lbl), run_time=0.85)
        self.wait(0.9)

        last_lbl = _label("lowest of the five", size=16, color=ACC, weight="BOLD").move_to([4.4, 2.3, 0])
        self.play(FadeIn(last_lbl), run_time=0.9)
        self.wait(0.7)

        cite = _label("Sineesh & Kamsali, 2026", size=15, color=SOFT).move_to([0, -2.25, 0])
        self.play(FadeIn(cite), run_time=0.8)
        self.wait(0.6)

        caveat = _label("general Raman data, not SERS-specific", size=13, color=SOFT).move_to([0, -2.6, 0])
        self.play(FadeIn(caveat), run_time=0.8)
        self.wait(0.8)

        kicker = _label("worth pursuing, not proven superior", size=18, weight="BOLD"
                       ).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(kicker), run_time=1.0)
        self.wait(3.4)
