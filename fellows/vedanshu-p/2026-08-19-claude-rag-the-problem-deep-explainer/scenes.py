"""scenes.py — Manim scenes for claude-rag-the-problem-deep-explainer.

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757 (ONE accent per scene).
No invented numbers/units on screen — qualitative comparisons only, citations
carried as small SOFT text alongside any claim that needs one (DOUBLE-CHECK LAW).
No slant=ITALIC on multi-word text (Pango collapses spaces).
"""
from manim import *
import numpy as np

# ── Palette ───────────────────────────────────────────────────────────────────
BG    = ManimColor("#F2F0E9")   # claude cream
INK   = ManimColor("#3D3929")   # warm ink — all body text
ACC   = ManimColor("#D97757")   # terracotta — ONE accent per scene
SOFT  = ManimColor("#6E6A57")   # secondary / muted text
GHOST = ManimColor("#A8A491")   # dimmed / placeholder
CARD  = ManimColor("#FFFFFF")   # white card surface


def _label(text, size=22, color=None, weight=None):
    kw = {"font_size": size, "color": color or INK}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw)


def _cite(text):
    return Text(text, font_size=14, color=SOFT)


# ─────────────────────────────────────────────────────────────────────────────
#  B08_HallucinationSplit
#  A question node splits into two labeled paths: intrinsic (contradicts a
#  source) vs. extrinsic (no source to check at all). Both read confident.
# ─────────────────────────────────────────────────────────────────────────────
class B08_HallucinationSplit(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("Two Flavors", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        q = Rectangle(width=2.4, height=0.8, color=INK, stroke_width=1.5,
                       fill_color=CARD, fill_opacity=1).shift(UP * 1.6)
        q_lbl = _label("the question", size=15).move_to(q)
        self.play(FadeIn(q), FadeIn(q_lbl), run_time=0.5)

        left_box = Rectangle(width=3.4, height=1.6, color=INK, stroke_width=1.5,
                              fill_color=CARD, fill_opacity=1).shift(LEFT * 2.6 + DOWN * 1.2)
        left_lbl = _label("intrinsic", size=18, weight="BOLD").move_to(left_box).shift(UP * 0.35)
        left_sub = _label("contradicts a source", size=14, color=SOFT).move_to(left_box).shift(DOWN * 0.3)

        right_box = Rectangle(width=3.4, height=1.6, color=ACC, stroke_width=1.5,
                               fill_color=CARD, fill_opacity=1).shift(RIGHT * 2.6 + DOWN * 1.2)
        right_lbl = _label("extrinsic", size=18, weight="BOLD", color=ACC).move_to(right_box).shift(UP * 0.35)
        right_sub = _label("no source to check", size=14, color=SOFT).move_to(right_box).shift(DOWN * 0.3)

        arrow_l = Arrow(q.get_bottom(), left_box.get_top(), color=INK, stroke_width=2, buff=0.1)
        arrow_r = Arrow(q.get_bottom(), right_box.get_top(), color=INK, stroke_width=2, buff=0.1)
        self.play(GrowArrow(arrow_l), GrowArrow(arrow_r), run_time=0.6)
        self.play(FadeIn(left_box), FadeIn(left_lbl), FadeIn(left_sub),
                   FadeIn(right_box), FadeIn(right_lbl), FadeIn(right_sub), run_time=0.8)

        cite = _cite("Ji et al., 2023; Huang et al., 2023 — both read equally confident")
        cite.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(cite), run_time=0.5)
        # held wait so the native clip isn't extreme-slow-mo'd to fill the beat
        self.wait(5.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B10_ReductionNotElimination
#  A descending curve that flattens ABOVE zero — grounding reduces
#  hallucination, it does not eliminate it. No invented rate on screen.
# ─────────────────────────────────────────────────────────────────────────────
class B10_ReductionNotElimination(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("Reduced. Not Eliminated.", size=28, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        axis = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=2).shift(DOWN * 1.6)
        zero_lbl = _label("zero", size=14, color=SOFT).next_to(axis, DOWN, buff=0.2).align_to(axis, RIGHT)
        self.play(Create(axis), FadeIn(zero_lbl), run_time=0.6)

        curve = ParametricFunction(
            lambda t: np.array([t, 1.6 * np.exp(-1.1 * (t + 4.5)) + 0.5, 0]),
            t_range=[-4.5, 4.3], color=ACC, stroke_width=4,
        ).shift(DOWN * 1.6)
        self.play(Create(curve), run_time=1.4, rate_func=rate_functions.ease_out_cubic)

        gap = DashedLine(curve.get_end(), [curve.get_end()[0], axis.get_y(), 0],
                          color=GHOST, stroke_width=2)
        self.play(Create(gap), run_time=0.5)

        cite = _cite("Shuster et al., 2021 — grounding measurably reduces hallucination in dialogue")
        cite.to_edge(DOWN, buff=1.3)
        self.play(FadeIn(cite), run_time=0.5)

        stamp = _label("the curve never reaches zero", size=18, color=ACC).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(stamp), run_time=0.6)
        self.wait(0.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B12_TrainOnceDeployStop
#  Two timelines: the model's line stops at "deploy"; the world's line keeps
#  moving. The gap between them is the whole mechanism.
# ─────────────────────────────────────────────────────────────────────────────
class B12_TrainOnceDeployStop(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("Train Once. Deploy. Stop.", size=28, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        model_line = Line(LEFT * 4.5, ORIGIN, color=INK, stroke_width=3).shift(UP * 0.6)
        self.play(Create(model_line), run_time=0.8)
        deploy_tick = Line(UP * 0.15, DOWN * 0.15, color=INK, stroke_width=2).move_to(model_line.get_end())
        deploy_lbl = _label("deploy", size=15).next_to(deploy_tick, UP, buff=0.2)
        self.play(Create(deploy_tick), FadeIn(deploy_lbl), run_time=0.5)

        world_line = Line(LEFT * 4.5, RIGHT * 4.3, color=ACC, stroke_width=3).shift(DOWN * 0.6)
        self.play(Create(world_line), run_time=1.2, rate_func=rate_functions.linear)
        world_lbl = _label("the world keeps changing", size=15, color=ACC).next_to(
            world_line.get_end(), UP, buff=0.2)
        self.play(FadeIn(world_lbl), run_time=0.4)

        stop_dot = Dot(radius=0.09, color=INK).move_to(model_line.get_end())
        self.play(FadeIn(stop_dot), run_time=0.3)

        stamp = _label("frozen the moment training stops", size=17, color=ACC).to_edge(DOWN, buff=0.8)
        cite = _cite("OpenAI, 2023 — a stated cutoff, not an accident")
        cite.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(stamp), run_time=0.5)
        self.play(FadeIn(cite), run_time=0.4)
        self.wait(0.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B13_NoFlag
#  A status indicator reads "current" the whole time; a "policy changed"
#  marker passes by unnoticed. No internal flag ever trips.
# ─────────────────────────────────────────────────────────────────────────────
class B13_NoFlag(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("No Internal Flag", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        indicator = Rectangle(width=3.2, height=1.1, color=INK, stroke_width=1.5,
                               fill_color=CARD, fill_opacity=1).shift(UP * 0.4)
        status = _label("current", size=20, weight="BOLD").move_to(indicator)
        self.play(FadeIn(indicator), FadeIn(status), run_time=0.6)

        track = Line(LEFT * 4, RIGHT * 4, color=GHOST, stroke_width=2).shift(DOWN * 1.4)
        self.play(Create(track), run_time=0.6)

        marker = Rectangle(width=1.0, height=0.5, color=ACC, stroke_width=1.5,
                            fill_color=CARD, fill_opacity=1).move_to(track.get_left())
        marker_lbl = _label("policy changed", size=13, color=ACC).next_to(marker, DOWN, buff=0.15)
        self.play(FadeIn(marker), FadeIn(marker_lbl), run_time=0.4)
        self.play(marker.animate.move_to(track.get_right()), marker_lbl.animate.next_to(
            track.get_right(), DOWN, buff=0.15), run_time=1.6, rate_func=rate_functions.linear)

        self.play(Indicate(indicator, color=GHOST, scale_factor=1.0), run_time=0.4)
        stamp = _label("status never changes — nothing tripped it", size=17, color=ACC
                        ).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(stamp), run_time=0.6)
        self.wait(0.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B18_TokenCeiling
#  A box fills toward a hard ceiling across several "generation" ticks — the
#  ceiling itself never disappears, only moves.
# ─────────────────────────────────────────────────────────────────────────────
class B18_TokenCeiling(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("A Ceiling That Moves. Never Vanishes.", size=26, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        base_y = -1.6
        gens = [1.0, 1.8, 2.6]
        boxes = VGroup()
        for i, h in enumerate(gens):
            x = -3 + i * 3
            box_bg = Rectangle(width=1.8, height=3.0, color=GHOST, stroke_width=0,
                                fill_color=GHOST, fill_opacity=0.2).move_to([x, base_y + 1.5, 0]
                                ).align_to([0, base_y, 0], DOWN)
            ceiling = Line(LEFT * 0.9, RIGHT * 0.9, color=INK, stroke_width=2.5
                            ).move_to([x, base_y + 3.0, 0])
            fill = Rectangle(width=1.8, height=h, color=ACC, stroke_width=0,
                              fill_color=ACC, fill_opacity=0.9).move_to([x, base_y + h / 2, 0])
            gen_lbl = _label(f"gen {i+1}", size=14, color=SOFT).next_to(box_bg, DOWN, buff=0.2)
            boxes.add(VGroup(box_bg, ceiling, fill, gen_lbl))
        for b in boxes:
            self.play(FadeIn(b), run_time=0.6)

        stamp = _label("bigger each generation — never unbounded", size=17, color=ACC
                        ).to_edge(DOWN, buff=0.8)
        cite = _cite("OpenAI, 2023")
        cite.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(stamp), run_time=0.6)
        self.play(FadeIn(cite), run_time=0.4)
        self.wait(0.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B19_PositionEffect
#  A reading-order scan across a bar: bright at the edges, dim in the
#  middle. QUALITATIVE ordering only — no invented accuracy numbers.
# ─────────────────────────────────────────────────────────────────────────────
class B19_PositionEffect(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("Where The Fact Sits", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        bar = Rectangle(width=8.0, height=1.2, color=INK, stroke_width=1.5,
                         fill_color=CARD, fill_opacity=1)
        self.play(FadeIn(bar), run_time=0.5)

        n = 9
        segs = VGroup()
        for i in range(n):
            t = i / (n - 1)
            level = 0.85 if t < 0.25 or t > 0.75 else 0.85 - 0.7 * np.sin(np.pi * (t - 0.25) / 0.5)
            seg = Rectangle(width=8.0 / n - 0.04, height=1.0, color=None, stroke_width=0,
                             fill_color=ACC, fill_opacity=max(0.12, level)
                             ).move_to(bar.get_left() + RIGHT * (8.0 / n) * (i + 0.5))
            segs.add(seg)
        self.play(*[FadeIn(s) for s in segs], run_time=1.0, lag_ratio=0.05)

        start_lbl = _label("start", size=15).next_to(bar, DOWN, buff=0.25).align_to(bar, LEFT)
        mid_lbl = _label("middle", size=15, color=SOFT).next_to(bar, DOWN, buff=0.25)
        end_lbl = _label("end", size=15).next_to(bar, DOWN, buff=0.25).align_to(bar, RIGHT)
        self.play(FadeIn(start_lbl), FadeIn(mid_lbl), FadeIn(end_lbl), run_time=0.5)

        cite = _cite("Liu et al., 2024 — ordering only, no accuracy figures stated")
        cite.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(cite), run_time=0.5)
        # held wait so the native clip isn't extreme-slow-mo'd to fill the beat
        self.wait(5.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B22_BiggerBoxSameLoss
#  A box scales up (2x, 3x); a marked "lost item" inside stays exactly as
#  lost regardless of the box's size. The size was never the variable.
# ─────────────────────────────────────────────────────────────────────────────
class B22_BiggerBoxSameLoss(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("Bigger Box. Same Loss.", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        box = Rectangle(width=2.6, height=1.8, color=INK, stroke_width=1.5,
                         fill_color=CARD, fill_opacity=1).shift(DOWN * 0.3)
        lost = Dot(radius=0.1, color=GHOST).move_to(box.get_center() + LEFT * 0.4 + UP * 0.2)
        lost_ring = Circle(radius=0.22, color=GHOST, stroke_width=2).move_to(lost)
        self.play(FadeIn(box), FadeIn(lost), Create(lost_ring), run_time=0.6)

        for scale in (1.6, 2.2):
            new_box = Rectangle(width=2.6 * scale, height=1.8 * scale, color=INK,
                                 stroke_width=1.5, fill_color=CARD, fill_opacity=1).move_to(box)
            self.play(Transform(box, new_box), run_time=1.0, rate_func=rate_functions.ease_out_cubic)
            self.wait(0.2)

        still_lost = _label("still lost", size=16, color=GHOST).next_to(lost_ring, DOWN, buff=0.15)
        self.play(FadeIn(still_lost), run_time=0.4)

        stamp = _label("size was never the variable", size=18, color=ACC).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(stamp), run_time=0.6)
        # held wait so the native clip isn't extreme-slow-mo'd to fill the beat
        self.wait(6.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B28_ConvergingBridge
#  Three labeled lines (the three failures) converge toward a single point.
#  The point itself stays UNLABELED beyond "chapter three" — no mechanism
#  from Chapter 3 is depicted or claimed here.
# ─────────────────────────────────────────────────────────────────────────────
class B28_ConvergingBridge(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("One Missing Step", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        target = RIGHT * 3.2
        starts = [LEFT * 4 + UP * 1.6, LEFT * 4, LEFT * 4 + DOWN * 1.6]
        labels = ["invented", "gone stale", "buried"]
        lines = VGroup()
        lbls = VGroup()
        for s, text in zip(starts, labels):
            ln = Line(s, target, color=GHOST, stroke_width=2.5)
            lbl = _label(text, size=15, color=SOFT).next_to(s, LEFT, buff=0.25)
            lines.add(ln)
            lbls.add(lbl)
        for ln, lbl in zip(lines, lbls):
            self.play(Create(ln), FadeIn(lbl), run_time=0.6)

        node = Dot(radius=0.14, color=ACC).move_to(target)
        glow = Circle(radius=0.3, color=ACC, stroke_width=2).move_to(target)
        self.play(FadeIn(node), Create(glow), run_time=0.6)

        node_lbl = _label("chapter three", size=16, color=ACC).next_to(node, RIGHT, buff=0.3)
        self.play(FadeIn(node_lbl), run_time=0.5)

        stamp = _label("same missing step, three times", size=17, color=ACC).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(stamp), run_time=0.6)
        self.wait(0.5)
