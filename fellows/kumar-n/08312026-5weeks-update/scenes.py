"""scenes.py -- Manim scenes for claude-liam-sers-ml-story.

Eight scenes, one per Manim beat, in beat order:

    B02_TheProblem          -- the original draft's structural problem
    B03_TheFix               -- the guidelines document's forced questions
    B04_TheSplit             -- how the paper's sections were divided
    B05_TheRhythm            -- the real timeline and weekly workload
    B06_LeakageDiagram       -- the PCA data-leakage mistake, wrong vs right
    B07_HotspotEvidence      -- hot-spot variability reframed as signal
    B08_ConditionalEnsemble  -- when ensembling helps vs hurts
    B10_TableFix             -- three real summary-table corrections

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757 (ONE accent per scene).
All coordinates self-checked against the verified safe area (x +-6.3, y +-3.4)
before rendering. Titles use to_edge(UP, buff=0.75); bottom kickers use
to_edge(DOWN, buff=0.65).

Every scene contains genuine shape-mobject motion spread across its runtime
(not just text fading in over a static shape) per GATE A's shape-variety check.
No invented statistics anywhere -- every number on screen traces to the real
paper content.
"""
from manim import *
import random as _r

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
#  B02_TheProblem
#  Three disconnected section boxes with broken links and a citation flag --
#  illustrates why the original AI-generated draft read as a glossary rather
#  than an argument.
# -----------------------------------------------------------------------------
class B02_TheProblem(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("A Draft That Only Defined Things", size=28, weight="BOLD").to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=1.0)
        self.wait(0.4)

        boxes = []
        xs = [-4.2, 0, 4.2]
        labels = ["\u00a71", "\u00a72", "\u00a73"]
        for x, lbl in zip(xs, labels):
            box = Rectangle(width=1.8, height=1.1, color=INK, stroke_width=2.2,
                            fill_color=CARD, fill_opacity=1).move_to([x, 0.6, 0])
            name = _label(lbl, size=24, weight="BOLD").move_to(box)
            boxes.append((box, name))
        self.play(*[Create(b) for b, _ in boxes], *[FadeIn(n) for _, n in boxes], run_time=1.2)
        self.wait(0.4)

        d1 = DashedLine([-3.3, 0.6, 0], [-0.9, 0.6, 0], color=GHOST, stroke_width=2, dash_length=0.12)
        d2 = DashedLine([0.9, 0.6, 0], [3.3, 0.6, 0], color=GHOST, stroke_width=2, dash_length=0.12)
        self.play(Create(d1), Create(d2), run_time=0.9)
        self.wait(0.4)

        flag = Triangle(color=ACC, stroke_width=2.5, fill_color=ACC, fill_opacity=0.25
                        ).scale(0.4).move_to([0, -1.7, 0])
        flag_lbl = _label("!", size=20, color=ACC, weight="BOLD").move_to([0, -1.72, 0])
        cite_lbl = _label("citations: missing or fake", size=18, color=ACC, weight="BOLD"
                          ).next_to(flag, DOWN, buff=0.3)
        self.play(FadeIn(flag), FadeIn(flag_lbl), FadeIn(cite_lbl), run_time=0.9)
        self.wait(0.5)

        kicker = _label("defined every term, explained nothing", size=20, weight="BOLD"
                        ).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(kicker), run_time=0.9)
        self.wait(1.5)


# -----------------------------------------------------------------------------
#  B03_TheFix
#  A checklist card that grows into place, with three forced questions
#  arriving one at a time -- the guidelines document every section had
#  to satisfy.
# -----------------------------------------------------------------------------
class B03_TheFix(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("Every Section Had to Answer Three Questions", size=25, weight="BOLD"
                       ).to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=1.0)
        self.wait(0.4)

        card_start = Rectangle(width=8.6, height=0.05, color=INK, stroke_width=2.2,
                               fill_color=CARD, fill_opacity=1).move_to([0, -0.1, 0])
        card_full = Rectangle(width=8.6, height=3.2, color=INK, stroke_width=2.2,
                              fill_color=CARD, fill_opacity=1).move_to([0, -0.1, 0])
        self.play(Transform(card_start, card_full), run_time=0.9)
        self.wait(0.3)

        qs = [
            "What has actually been done?",
            "Why does it work or fail?",
            "What do we recommend?",
        ]
        for i, q in enumerate(qs):
            y = 0.7 - i * 0.8
            dot_small = Circle(radius=0.02, color=ACC, fill_color=ACC, fill_opacity=1,
                              stroke_width=0).move_to([-3.6, y, 0])
            dot_full = Circle(radius=0.16, color=ACC, fill_color=ACC, fill_opacity=1,
                             stroke_width=0).move_to([-3.6, y, 0])
            txt = _label(q, size=21, color=INK).next_to(dot_full, RIGHT, buff=0.35)
            self.play(Transform(dot_small, dot_full), FadeIn(txt), run_time=0.9)
            self.wait(0.3)

        kicker = _label("a definition without an answer wasn't finished", size=18, weight="BOLD"
                        ).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(kicker), run_time=0.9)
        self.wait(1.5)


# -----------------------------------------------------------------------------
#  B04_TheSplit
#  An org chart: PM writes the introduction, then the remaining sections
#  split between the two co-authors.
# -----------------------------------------------------------------------------
class B04_TheSplit(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("Who Wrote What", size=30, weight="BOLD").to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=1.0)
        self.wait(0.4)

        pm_box = Rectangle(width=2.4, height=0.9, color=INK, stroke_width=2.2,
                           fill_color=CARD, fill_opacity=1).move_to([0, 2.0, 0])
        pm_lbl = _label("PM", size=20, weight="BOLD").move_to(pm_box)
        self.play(Create(pm_box), FadeIn(pm_lbl), run_time=0.7)

        intro_box = Rectangle(width=3.2, height=0.8, color=SOFT, stroke_width=2,
                              fill_color=CARD, fill_opacity=1).move_to([0, 0.7, 0])
        intro_lbl = _label("Introduction", size=18, color=SOFT).move_to(intro_box)
        arrow0 = Arrow(pm_box.get_bottom(), intro_box.get_top(), color=INK, stroke_width=2,
                       tip_length=0.18, buff=0.05)
        self.play(GrowArrow(arrow0), Create(intro_box), FadeIn(intro_lbl), run_time=0.9)
        self.wait(0.3)

        left_box = Rectangle(width=3.6, height=1.3, color=SOFT, stroke_width=2.2,
                             fill_color=CARD, fill_opacity=1).move_to([-2.6, -1.4, 0])
        left_lbl = _label("Teammate\n2.1\u20132.3 \u00b7 3.1\u20133.2", size=16, color=SOFT).move_to(left_box)
        right_box = Rectangle(width=3.6, height=1.3, color=ACC, stroke_width=2.5,
                              fill_color=CARD, fill_opacity=1).move_to([2.6, -1.4, 0])
        right_lbl = _label("Kumar Karthik\n2.4\u20132.6 \u00b7 3.3\u20133.5", size=16, color=ACC, weight="BOLD"
                          ).move_to(right_box)

        arrow_l = Arrow(intro_box.get_bottom(), left_box.get_top(), color=SOFT, stroke_width=2,
                        tip_length=0.16, buff=0.05)
        arrow_r = Arrow(intro_box.get_bottom(), right_box.get_top(), color=ACC, stroke_width=2,
                        tip_length=0.16, buff=0.05)

        self.play(GrowArrow(arrow_l), GrowArrow(arrow_r), run_time=0.8)
        self.play(Create(left_box), FadeIn(left_lbl), Create(right_box), FadeIn(right_lbl), run_time=1.1)
        self.wait(0.5)

        kicker = _label("the same rules applied to every section", size=19, weight="BOLD"
                        ).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(kicker), run_time=0.9)
        self.wait(1.5)


# -----------------------------------------------------------------------------
#  B05_TheRhythm
#  A Gantt-style timeline: four alternating research/rewrite blocks across
#  the real five-week window, with the actual weekly-hours breakdown below.
# -----------------------------------------------------------------------------
class B05_TheRhythm(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("Same Two-Week Cycle, Twice", size=28, weight="BOLD").to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=1.0)
        self.wait(0.3)

        date_lbl = _label("Aug 1 \u2013 Sep 2, 2026", size=20, color=SOFT).move_to([0, 1.9, 0])
        self.play(FadeIn(date_lbl), run_time=0.7)

        segs = [
            ("research", SOFT, "Sec. 2"),
            ("rewrite", ACC, "Sec. 2"),
            ("research", SOFT, "Sec. 3"),
            ("rewrite", ACC, "Sec. 3"),
        ]
        bar_y = 0.5
        seg_w = 2.6
        start_x = -5.2

        for i, (kind, col, sec) in enumerate(segs):
            x = start_x + i * seg_w + seg_w / 2
            block_start = Rectangle(width=0.05, height=0.9, color=col, stroke_width=2,
                                    fill_color=col, fill_opacity=0.5).move_to([x, bar_y, 0])
            block_full = Rectangle(width=seg_w - 0.1, height=0.9, color=col, stroke_width=2,
                                   fill_color=col, fill_opacity=0.5).move_to([x, bar_y, 0])
            klabel = _label(kind, size=16, weight="BOLD").move_to(block_full)
            slabel = _label(sec, size=13, color=SOFT).next_to(block_full, DOWN, buff=0.15)
            self.play(Transform(block_start, block_full), FadeIn(klabel), FadeIn(slabel), run_time=0.8)
            self.wait(0.15)

        hours = _label("~3-5h/wk meetings \u00b7 10-15h research & rewriting\n1h PM check-in every other week",
                       size=14, color=SOFT).move_to([0, -1.3, 0])
        self.play(FadeIn(hours), run_time=0.9)
        self.wait(0.5)

        kicker = _label("the pattern repeated exactly, section after section", size=18, weight="BOLD"
                        ).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(kicker), run_time=0.9)
        self.wait(1.5)


# -----------------------------------------------------------------------------
#  B06_LeakageDiagram
#  Two stacked flow diagrams contrasting the wrong PCA fitting order
#  (full data, then split -- a data-leakage mistake) against the correct
#  order (split first, fit PCA on training data only).
# -----------------------------------------------------------------------------
class B06_LeakageDiagram(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("The PCA Leakage Trap", size=30, weight="BOLD").to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=1.3)
        self.wait(0.6)

        wrong_lbl = _label("WRONG", size=17, color=ACC, weight="BOLD").move_to([-5.0, 2.3, 0])
        w1 = Rectangle(width=1.85, height=0.65, color=SOFT, stroke_width=2, fill_color=CARD, fill_opacity=1
                      ).move_to([-3.2, 2.3, 0])
        w1_lbl = _label("full data", size=13).move_to(w1)
        w2 = Rectangle(width=1.85, height=0.65, color=SOFT, stroke_width=2, fill_color=CARD, fill_opacity=1
                      ).move_to([0.0, 2.3, 0])
        w2_lbl = _label("fit PCA", size=13).move_to(w2)
        w3 = Rectangle(width=1.85, height=0.65, color=SOFT, stroke_width=2, fill_color=CARD, fill_opacity=1
                      ).move_to([3.2, 2.3, 0])
        w3_lbl = _label("split", size=13).move_to(w3)
        aw1 = Arrow(w1.get_right(), w2.get_left(), color=SOFT, stroke_width=2, tip_length=0.13, buff=0.05)
        aw2 = Arrow(w2.get_right(), w3.get_left(), color=SOFT, stroke_width=2, tip_length=0.13, buff=0.05)

        self.play(FadeIn(wrong_lbl), run_time=0.7)
        self.play(Create(w1), FadeIn(w1_lbl), run_time=0.9)
        self.play(GrowArrow(aw1), run_time=0.7)
        self.play(Create(w2), FadeIn(w2_lbl), run_time=0.9)
        self.play(GrowArrow(aw2), run_time=0.7)
        self.play(Create(w3), FadeIn(w3_lbl), run_time=0.9)
        self.wait(0.5)
        x_mark = _label("\u2717", size=26, color=ACC, weight="BOLD").move_to([0.0, 1.55, 0])
        self.play(FadeIn(x_mark), run_time=0.7)
        self.wait(0.6)

        reported = _label("looks accurate", size=19, color=ACC, weight="BOLD").move_to([0, 0.95, 0])
        self.play(FadeIn(reported), run_time=1.0)
        self.wait(0.8)

        right_lbl = _label("RIGHT", size=17, color=INK, weight="BOLD").move_to([-5.0, -0.4, 0])
        r1 = Rectangle(width=1.85, height=0.65, color=INK, stroke_width=2, fill_color=CARD, fill_opacity=1
                      ).move_to([-3.2, -0.4, 0])
        r1_lbl = _label("split first", size=12).move_to(r1)
        r2 = Rectangle(width=1.85, height=0.65, color=INK, stroke_width=2, fill_color=CARD, fill_opacity=1
                      ).move_to([0.0, -0.4, 0])
        r2_lbl = _label("fit PCA\non train", size=11).move_to(r2)
        r3 = Rectangle(width=1.85, height=0.65, color=ACC, stroke_width=2.3, fill_color=CARD, fill_opacity=1
                      ).move_to([3.2, -0.4, 0])
        r3_lbl = _label("apply to\ntest", size=11, color=ACC).move_to(r3)
        ar1 = Arrow(r1.get_right(), r2.get_left(), color=INK, stroke_width=2, tip_length=0.13, buff=0.05)
        ar2 = Arrow(r2.get_right(), r3.get_left(), color=ACC, stroke_width=2, tip_length=0.13, buff=0.05)

        self.play(FadeIn(right_lbl), run_time=0.7)
        self.play(Create(r1), FadeIn(r1_lbl), run_time=0.9)
        self.play(GrowArrow(ar1), run_time=0.7)
        self.play(Create(r2), FadeIn(r2_lbl), run_time=0.9)
        self.play(GrowArrow(ar2), run_time=0.7)
        self.play(Create(r3), FadeIn(r3_lbl), run_time=0.9)
        self.wait(0.5)
        check = _label("\u2713", size=24, color=ACC, weight="BOLD").move_to([0.0, -1.15, 0])
        self.play(FadeIn(check), run_time=0.7)
        self.wait(0.6)

        real = _label("doesn't generalize", size=19, color=INK, weight="BOLD").move_to([0, -1.75, 0])
        self.play(FadeIn(real), run_time=1.0)
        self.wait(0.8)

        cite = _label("2.4: Savorani 2010 \u00b7 Liu 2017", size=13, color=SOFT).move_to([0, -2.45, 0])
        self.play(FadeIn(cite), run_time=0.7)
        self.wait(0.4)

        kicker = _label("train-only fitting is the whole rule", size=18, weight="BOLD"
                        ).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(kicker), run_time=1.0)
        self.wait(1.8)


# -----------------------------------------------------------------------------
#  B07_HotspotEvidence
#  A before/after bar comparison showing that training on deliberately
#  varied hot-spot conditions cut prediction error by 84.8%, plus a
#  scattered-dot representation of the 35-instrument cross-lab study.
# -----------------------------------------------------------------------------
class B07_HotspotEvidence(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("Variability Isn't Always Noise", size=27, weight="BOLD").to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=1.2)
        self.wait(0.6)

        baseline_y = 0.6
        b1 = Rectangle(width=1.5, height=0.01, color=SOFT, fill_color=SOFT, fill_opacity=0.85,
                      stroke_width=0).move_to([-3.6, baseline_y, 0]).align_to([-3.6, baseline_y, 0], DOWN)
        b1t = Rectangle(width=1.5, height=1.7, color=SOFT, fill_color=SOFT, fill_opacity=0.85,
                       stroke_width=0).move_to([-3.6, baseline_y, 0]).align_to([-3.6, baseline_y, 0], DOWN)
        b1lbl = _label("identical\nconditions", size=14, color=SOFT).next_to(b1t, DOWN, buff=0.2)

        b2 = Rectangle(width=1.5, height=0.01, color=ACC, fill_color=ACC, fill_opacity=0.9,
                      stroke_width=0).move_to([-0.9, baseline_y, 0]).align_to([-0.9, baseline_y, 0], DOWN)
        b2t = Rectangle(width=1.5, height=0.3, color=ACC, fill_color=ACC, fill_opacity=0.9,
                       stroke_width=0).move_to([-0.9, baseline_y, 0]).align_to([-0.9, baseline_y, 0], DOWN)
        b2lbl = _label("deliberately\nvaried", size=14, color=ACC, weight="BOLD").next_to(b2t, DOWN, buff=0.2)

        self.play(Create(Line([-4.6, baseline_y, 0], [0.2, baseline_y, 0], color=INK, stroke_width=1.6)),
                 run_time=0.8)
        self.play(Transform(b1, b1t), FadeIn(b1lbl), run_time=1.4, rate_func=rate_functions.smooth)
        self.wait(0.4)
        self.play(Transform(b2, b2t), FadeIn(b2lbl), run_time=1.4, rate_func=rate_functions.smooth)
        self.wait(0.5)

        drop_lbl = _label("\u221284.8% error", size=21, color=ACC, weight="BOLD").move_to([-2.2, 2.5, 0])
        self.play(FadeIn(drop_lbl), run_time=0.9)
        self.wait(0.7)

        cite1 = _label("Zhao et al., 2025", size=13, color=SOFT).move_to([-2.2, -1.8, 0])
        self.play(FadeIn(cite1), run_time=0.7)
        self.wait(0.5)

        dots_lbl = _label("35 instruments \u00b7 15 institutes", size=15, color=INK, weight="BOLD"
                         ).move_to([3.2, 1.9, 0])
        self.play(FadeIn(dots_lbl), run_time=0.9)
        self.wait(0.3)

        dots = VGroup()
        _r.seed(7)
        for i in range(14):
            dx = _r.uniform(-1.1, 1.1)
            dy = _r.uniform(-0.6, 0.6)
            d = Dot([3.2 + dx, 0.9 + dy, 0], radius=0.06, color=SOFT, fill_opacity=0.85)
            dots.add(d)
        self.play(*[FadeIn(d) for d in dots], run_time=1.5)
        self.wait(0.6)

        cite2 = _label("cross-instrument drift confirmed\n(Guo et al., 2020)", size=12, color=SOFT
                      ).move_to([3.2, -0.3, 0])
        self.play(FadeIn(cite2), run_time=0.9)
        self.wait(0.7)

        kicker = _label("the variation itself became the training signal", size=17, weight="BOLD"
                        ).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(kicker), run_time=1.1)
        self.wait(2.2)


# -----------------------------------------------------------------------------
#  B08_ConditionalEnsemble
#  Two side-by-side ensemble scenarios: models that disagree usefully
#  (ensemble beats every individual classifier) versus models that
#  disagree unhelpfully (ensemble underperforms the best solo model).
# -----------------------------------------------------------------------------
class B08_ConditionalEnsemble(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("When Ensembling Helps \u2014 and When It Doesn't", size=23, weight="BOLD"
                       ).to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=1.2)
        self.wait(0.5)

        left_hdr = _label("models disagree usefully", size=15, color=ACC, weight="BOLD"
                         ).move_to([-3.3, 2.3, 0])
        self.play(FadeIn(left_hdr), run_time=0.7)
        c1a = Circle(radius=0.32, color=INK, stroke_width=2, fill_color=CARD, fill_opacity=1
                    ).move_to([-4.0, 1.5, 0])
        c1b = Circle(radius=0.32, color=INK, stroke_width=2, fill_color=CARD, fill_opacity=1
                    ).move_to([-2.6, 1.5, 0])
        self.play(Create(c1a), run_time=0.6)
        self.play(Create(c1b), run_time=0.6)
        check_l = _label("\u2713", size=22, color=ACC, weight="BOLD").move_to([-3.3, 0.75, 0])
        self.play(FadeIn(check_l), run_time=0.7)
        self.wait(0.4)

        base_y = -1.3
        bar_a1 = Rectangle(width=0.85, height=1.1, color=SOFT, fill_color=SOFT, fill_opacity=0.8,
                          stroke_width=0).move_to([-3.8, base_y, 0]).align_to([-3.8, base_y, 0], DOWN)
        bar_a2 = Rectangle(width=0.85, height=1.5, color=ACC, fill_color=ACC, fill_opacity=0.9,
                          stroke_width=0).move_to([-2.8, base_y, 0]).align_to([-2.8, base_y, 0], DOWN)
        lbl_a1 = _label("best solo", size=12, color=SOFT).next_to(bar_a1, DOWN, buff=0.15)
        lbl_a2 = _label("97.9%", size=13, color=ACC, weight="BOLD").next_to(bar_a2, DOWN, buff=0.15)
        self.play(Create(bar_a1), FadeIn(lbl_a1), run_time=0.8)
        self.play(Create(bar_a2), FadeIn(lbl_a2), run_time=0.8)
        self.wait(0.5)

        right_hdr = _label("models disagree unhelpfully", size=15, color=SOFT, weight="BOLD"
                          ).move_to([3.3, 2.3, 0])
        self.play(FadeIn(right_hdr), run_time=0.7)
        c2a = Circle(radius=0.32, color=INK, stroke_width=2, fill_color=CARD, fill_opacity=1
                    ).move_to([2.6, 1.5, 0])
        c2b = Circle(radius=0.32, color=INK, stroke_width=2, fill_color=CARD, fill_opacity=1
                    ).move_to([4.0, 1.5, 0])
        self.play(Create(c2a), run_time=0.6)
        self.play(Create(c2b), run_time=0.6)
        x_r = _label("\u2717", size=22, color=SOFT, weight="BOLD").move_to([3.3, 0.75, 0])
        self.play(FadeIn(x_r), run_time=0.7)
        self.wait(0.4)

        bar_b1 = Rectangle(width=0.85, height=1.4, color=ACC, fill_color=ACC, fill_opacity=0.85,
                          stroke_width=0).move_to([2.8, base_y, 0]).align_to([2.8, base_y, 0], DOWN)
        bar_b2 = Rectangle(width=0.85, height=0.85, color=GHOST, fill_color=GHOST, fill_opacity=0.85,
                          stroke_width=0).move_to([3.8, base_y, 0]).align_to([3.8, base_y, 0], DOWN)
        lbl_b1 = _label("XGBoost\n97.4%", size=11, color=ACC).next_to(bar_b1, DOWN, buff=0.15)
        lbl_b2 = _label("ensemble\n76.1%", size=11, color=SOFT).next_to(bar_b2, DOWN, buff=0.15)
        self.play(Create(bar_b1), FadeIn(lbl_b1), run_time=0.8)
        self.play(Create(bar_b2), FadeIn(lbl_b2), run_time=0.8)
        self.wait(0.5)

        note = _label("decision trees & logistic regression:\nensemble parts only, never solo",
                      size=13, color=SOFT).move_to([0, -2.5, 0])
        self.play(FadeIn(note), run_time=0.9)
        self.wait(0.7)

        kicker = _label("ensemble when models fail differently, not by default", size=16, weight="BOLD"
                        ).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(kicker), run_time=1.0)
        self.wait(2.0)


# -----------------------------------------------------------------------------
#  B10_TableFix
#  Three summary-table rows built one at a time, then corrected live:
#  a mismatched citation flagged and removed, a citation gap filled with
#  a real study, and an ensemble row split into two honest rows.
# -----------------------------------------------------------------------------
class B10_TableFix(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _label("Fixing the Summary Table", size=30, weight="BOLD").to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=1.0)
        self.wait(0.3)

        rows_data = [
            ("Random Forest", "Rothemund et al. \u2014 not even Raman", True),
            ("PLSR", "citation needed", False),
            ("Ensemble", "one row, two different kinds", None),
        ]
        row_h = 0.85
        y0 = 1.5
        row_boxes = []
        for i, (name, note, strike) in enumerate(rows_data):
            y = y0 - i * (row_h + 0.25)
            box_start = Rectangle(width=0.05, height=row_h, color=INK, stroke_width=1.8,
                                  fill_color=CARD, fill_opacity=1).move_to([0, y, 0])
            box_full = Rectangle(width=8.4, height=row_h, color=INK, stroke_width=1.8,
                                 fill_color=CARD, fill_opacity=1).move_to([0, y, 0])
            name_lbl = _label(name, size=18, weight="BOLD").move_to(box_full).align_to(box_full, LEFT).shift(RIGHT * 0.4)
            note_lbl = _label(note, size=14, color=(ACC if strike else SOFT)
                             ).move_to(box_full).align_to(box_full, RIGHT).shift(LEFT * 0.4)
            self.play(Transform(box_start, box_full), run_time=0.7)
            self.play(FadeIn(name_lbl), FadeIn(note_lbl), run_time=0.6)
            self.wait(0.2)
            row_boxes.append((box_start, name_lbl, note_lbl, strike))

        self.wait(0.3)

        box1, name1, note1, _ = row_boxes[0]
        flag_small = Circle(radius=0.02, color=ACC, stroke_width=2.5, fill_opacity=0).move_to(note1.get_center())
        flag_full = SurroundingRectangle(note1, color=ACC, stroke_width=2.5, buff=0.08)
        self.play(Transform(flag_small, flag_full), run_time=0.6)
        self.wait(0.3)
        removed_lbl = _label("removed", size=14, color=ACC, weight="BOLD").move_to(note1)
        self.play(FadeOut(note1), FadeOut(flag_small), FadeIn(removed_lbl), run_time=0.8)
        self.wait(0.3)

        box2, name2, note2, _ = row_boxes[1]
        badge_small = Circle(radius=0.02, color=ACC, fill_color=ACC, fill_opacity=1,
                             stroke_width=0).move_to(note2.get_right() + RIGHT * 0.3)
        badge_full = Circle(radius=0.12, color=ACC, fill_color=ACC, fill_opacity=1,
                            stroke_width=0).move_to(note2.get_right() + RIGHT * 0.3)
        filled_lbl = _label("Hou et al., 2016", size=14, color=ACC, weight="BOLD").move_to(note2).shift(LEFT * 0.15)
        self.play(FadeOut(note2), FadeIn(filled_lbl), run_time=0.7)
        self.play(Transform(badge_small, badge_full), run_time=0.6)
        self.wait(0.3)

        box3, name3, note3, _ = row_boxes[2]
        bracket_start = Line(note3.get_left(), note3.get_left(), color=ACC, stroke_width=2.5)
        bracket_full = Line(note3.get_left() + DOWN * 0.05, note3.get_right() + DOWN * 0.05,
                            color=ACC, stroke_width=2.5)
        split_lbl = _label("split: heterogeneous \u00b7 voting", size=13, color=ACC, weight="BOLD"
                          ).move_to(note3).shift(UP * 0.02)
        self.play(FadeOut(note3), FadeIn(split_lbl), run_time=0.7)
        self.play(Transform(bracket_start, bracket_full), run_time=0.6)
        self.wait(0.5)

        kicker = _label("a mismatched citation reads as false evidence", size=17, weight="BOLD"
                        ).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(kicker), run_time=0.9)
        self.wait(1.4)
