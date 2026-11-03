"""scenes.py — Manim scenes for when-two-agents-disagree (claude-divij).

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757, soft #73705F,
ghost #A9A491 — the Claude fidelity palette per ai-explainer SKILL.md. ONE
accent per beat. The source script's [VISUAL] color cues (green speech
bubble / red speech bubble, green "AGREEMENT" / red "DIVERGENCE" gauge) are
deliberately NOT carried literally, same retint rule used on why-agents-fail
(STEM2) and how-do-you-know-it-worked (STEM5): good/bad is carried by label,
position, and ink-vs-terracotta, so the frame stays legible in grayscale and
under any colour vision. No blue, no green, no red.

Type: Montserrat (DISPLAY, structural default) / EB Garamond (SERIF,
editorial voice only) / PT Mono (MONO, logs + code + data only) — see
graphics_lib.py. Boxes are content-fitted via auto_box/surround_box, never
hand-measured. This file never calls raw Text() for body copy.

Pace: normal-speed creates/fades with deliberate HOLDS sized to the
narration. Targets below are against `estimated_duration_s` in
beat_sheet.json; RETIME against `actual_duration_s` once Kokoro has run
(see BUILD-PROMPT.md Step 3 — not yet done, this reel is pre-audio).

Unlike STEM5's persistent three-mechanism legend, this reel's spine is a
pair of agent nameplates (AGENT A / AGENT B, via graphics_lib's
label_chip()) that recur across B04, B05 and B07 — the arbitration beats —
carrying the same two identities from setup through outcome through blind
spot, so the viewer never loses track of which "witness" is which.
"""
import numpy as np
from graphics_lib import *

# ── Palette (claude-stage retint, per ai-explainer SKILL.md) ──────────────────
BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


def strike(mobj, color=None):
    """A struck-through line sized to the mobject it cancels."""
    return Line(mobj.get_left() + LEFT * 0.08, mobj.get_right() + RIGHT * 0.08,
                color=color if color is not None else ACC, stroke_width=3.0)


def mic_icon(color, height=0.85):
    """A constructed microphone glyph — capsule head, stand, base — built
    from primitives, not a stock icon."""
    head = RoundedRectangle(corner_radius=0.16, width=0.42, height=height,
                             color=color, fill_color=color, fill_opacity=1.0,
                             stroke_width=0)
    stand = Line(head.get_bottom(), head.get_bottom() + DOWN * 0.45,
                 color=color, stroke_width=4)
    base = Line(LEFT * 0.22, RIGHT * 0.22, color=color, stroke_width=4)
    base.move_to(stand.get_end())
    return VGroup(head, stand, base)


def bubble(text_mobj, color, h_pad=0.35, v_pad=0.25):
    """A rounded conclusion card standing in for a speech bubble — no tail,
    to avoid a stroke-fill collision at the anchor point."""
    box = RoundedRectangle(corner_radius=0.22,
                            width=text_mobj.width + 2 * h_pad,
                            height=text_mobj.height + 2 * v_pad,
                            color=color, stroke_width=2.5,
                            fill_color=color, fill_opacity=0.07)
    box.move_to(text_mobj)
    return VGroup(box, text_mobj)


def blender_icon(color, width=1.0, height=1.5):
    """A trapezoid jar on a base — a constructed diagram element."""
    jar = Polygon([-width / 2, height / 2, 0], [width / 2, height / 2, 0],
                  [width * 0.32, -height / 2, 0], [-width * 0.32, -height / 2, 0],
                  color=color, stroke_width=2.5, fill_color=color, fill_opacity=0.06)
    stand = Rectangle(width=width * 0.9, height=0.16, color=color,
                       fill_color=color, fill_opacity=1.0, stroke_width=0)
    stand.next_to(jar, DOWN, buff=0.0)
    return VGroup(jar, stand)


def gauge_arcs(radius=1.7):
    """A two-zone semicircular dial: AGREEMENT (ink, left half) and
    DIVERGENCE (accent, right half), plus a pivot dot for the needle."""
    agree = Arc(radius=radius, start_angle=PI, angle=-PI / 2, color=INK,
                stroke_width=10)
    diverge = Arc(radius=radius, start_angle=PI / 2, angle=-PI / 2, color=ACC,
                  stroke_width=10)
    pivot = Dot(ORIGIN, color=SOFT, radius=0.06)
    return VGroup(agree, diverge, pivot)


def needle_at(theta, radius=1.7, color=SOFT):
    return Line(ORIGIN, radius * 0.82 * np.array([np.cos(theta), np.sin(theta), 0]),
                color=color, stroke_width=5)


def crack_line(rect, color, jitter=0.14):
    """A jagged VMobject cutting through rect's height — a visible flaw
    neither party notices, standing in for shared contamination."""
    top, bottom = rect.get_top(), rect.get_bottom()
    n = 6
    pts = []
    for i in range(n + 1):
        y = top[1] + (bottom[1] - top[1]) * i / n
        x = rect.get_center()[0] + (jitter if i % 2 == 0 else -jitter)
        pts.append([x, y, 0])
    line = VMobject(color=color, stroke_width=3)
    line.set_points_as_corners(pts)
    return line


# ─────────────────────────────────────────────────────────────────────────────
#  B01_OneVoiceThenMany   (target ~43s)
#  Executive-summary/BLUF beat: one voice multiplies into four specialized
#  agents; two of them contradict each other; the reframe lands — disagreement
#  is a signal, not a bug — before any mechanism is introduced.
# ─────────────────────────────────────────────────────────────────────────────
class B01_OneVoiceThenMany(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("One Voice, Then Many", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.4)

        mic = mic_icon(INK).move_to(UP * 0.3)
        self.play(FadeIn(mic), run_time=0.5)
        self.wait(1.8)

        # ── Multiply into four specialized agents ─────────────────────────────
        self.play(FadeOut(mic), run_time=0.3)
        mics = VGroup(*[mic_icon(GHOST) for _ in range(4)]).arrange(RIGHT, buff=2.0)
        mics.move_to(UP * 0.7)
        table = Line(mics.get_left() + LEFT * 0.4, mics.get_right() + RIGHT * 0.4,
                     color=GHOST, stroke_width=2.5)
        table.next_to(mics, DOWN, buff=0.55)
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.2) for m in mics], lag_ratio=0.25),
                   Create(table), run_time=1.1)
        self.wait(1.6)

        # label()'s size floor clamps anything under 24 back up to 24 (see
        # graphics_lib.py FLOOR) — at the original buff=1.1 spacing, four
        # floor-sized labels (esp. the two-word "earnings calls") collided
        # into unreadable overlap, caught in mid-scene QC. Fixed by widening
        # mic spacing (buff=2.0) and shortening to single words that fit the
        # wider gap instead of trying to shrink text below the floor.
        names = ["financial", "competitive", "patents", "earnings"]
        labels = VGroup()
        for m, n in zip(mics, names):
            lb = label(n, size=24, color=SOFT)
            lb.next_to(m, DOWN, buff=0.15).align_to(table, UP).shift(DOWN * 0.25)
            labels.add(lb)
        self.play(LaggedStart(*[FadeIn(lb) for lb in labels], lag_ratio=0.25), run_time=0.9)
        self.wait(2.3)

        # ── Two agents flatly contradict each other ────────────────────────────
        mics[0][0].set_color(ACC)
        mics[2][0].set_color(ACC)
        self.play(mics[0].animate.set_color(ACC), mics[2].animate.set_color(ACC),
                   run_time=0.5)
        conn_y = mics.get_bottom()[1] - 0.55
        dotted = DashedLine([mics[0].get_center()[0], conn_y, 0],
                             [mics[2].get_center()[0], conn_y, 0], color=ACC,
                             stroke_width=2.5, dash_length=0.14)
        # `contra` was positioned via next_to(dotted, DOWN, buff=0.2), which
        # computed to almost the exact same y as the `labels` row beneath
        # the mics (dotted sits only ~0.25 above labels to begin with) — a
        # direct text overlap caught after the fact, not by any render
        # succeeding. Anchored off `labels` explicitly instead, so it can
        # never land at the same height regardless of where `dotted` sits.
        contra = label("flatly contradict", size=22, color=ACC)
        contra.next_to(labels, DOWN, buff=0.35)
        self.play(Create(dotted), FadeIn(contra), run_time=0.7)
        self.wait(5.4)

        # ── Bug, struck, replaced with signal ─────────────────────────────────
        self.play(FadeOut(VGroup(mics, table, labels, dotted, contra)), run_time=0.5)
        bug = label("bug", size=50, color=INK, weight="BOLD").move_to(UP * 0.6)
        self.play(Write(bug), run_time=0.6)
        self.wait(1.4)
        bug_strike = strike(bug, color=ACC)
        self.play(Create(bug_strike), run_time=0.5)
        self.wait(0.7)
        signal = label("signal", size=50, color=ACC, weight="BOLD")
        signal.next_to(bug, DOWN, buff=0.5)
        self.play(FadeIn(signal, shift=UP * 0.2), run_time=0.5)
        self.wait(4.1)

        # ── Landing line ────────────────────────────────────────────────────────
        self.play(FadeOut(VGroup(bug, bug_strike, signal)), run_time=0.5)
        land = serif("Maybe the honest answer is: we don't actually know.",
                      size=30, color=ACC, line_spacing=1.0).move_to(DOWN * 0.2)
        self.play(Write(land), run_time=1.0)
        self.wait(8.92)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_TheNaiveFix   (target ~44s)
#  Two contradicting conclusions get blended into one wishy-washy answer —
#  then checked against the case where one agent was actually right.
# ─────────────────────────────────────────────────────────────────────────────
class B02_TheNaiveFix(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("The Naive Fix", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.2)

        txt_a = label("margins\nimproving", size=20, color=INK, line_spacing=0.85)
        txt_b = label("margins\ndeclining", size=20, color=ACC, line_spacing=0.85)
        bub_a = bubble(txt_a, INK).move_to([-3.6, 1.4, 0])
        bub_b = bubble(txt_b, ACC).move_to([3.6, 1.4, 0])
        doc = Rectangle(width=1.1, height=1.4, color=SOFT, stroke_width=2.5,
                         fill_color=SOFT, fill_opacity=0.05).move_to(UP * 1.4)
        arr_a = Arrow(bub_a.get_right(), doc.get_left(), buff=0.1, color=SOFT, stroke_width=2.5)
        arr_b = Arrow(bub_b.get_left(), doc.get_right(), buff=0.1, color=SOFT, stroke_width=2.5)
        self.play(FadeIn(doc), FadeIn(bub_a), FadeIn(bub_b), Create(arr_a), Create(arr_b),
                   run_time=0.8)
        self.wait(2.5)

        # ── Both slide into a blender ──────────────────────────────────────────
        blender = blender_icon(SOFT).move_to(DOWN * 0.6)
        self.play(FadeOut(doc), FadeOut(arr_a), FadeOut(arr_b), FadeIn(blender), run_time=0.4)
        self.wait(0.4)
        # Both bubbles shrink and fade *continuously* while converging on the
        # blender's center, rather than parking side by side first — at the
        # original two-step version they briefly sat almost fully overlapped
        # at near-full size and near-full opacity, an illegible text
        # collision caught in mid-scene QC. Shrinking throughout the move
        # means they're already small/near-transparent by the time they'd
        # otherwise touch.
        self.play(bub_a.animate.move_to(blender.get_center()).scale(0.2).set_opacity(0),
                   bub_b.animate.move_to(blender.get_center()).scale(0.2).set_opacity(0),
                   run_time=1.1)
        self.play(Wiggle(blender, scale_value=1.08, rotation_angle=0.02 * TAU), run_time=0.5)
        grey_txt = label("results may vary", size=22, color=GHOST)
        grey = bubble(grey_txt, GHOST)
        grey.next_to(blender, DOWN, buff=0.4)
        self.play(FadeIn(grey, shift=DOWN * 0.2), run_time=0.5)
        self.wait(1.8)

        caption = label("nobody's actual opinion", size=23, color=SOFT)
        caption.next_to(grey, DOWN, buff=0.35)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(5.9)

        # ── If A was right, the blend makes it worse ──────────────────────────
        self.play(FadeOut(VGroup(blender, grey, caption)), run_time=0.5)
        right_lab = label("Agent A — right", size=22, color=INK, weight="BOLD")
        wrong_lab = label("Agent B — wrong", size=22, color=SOFT)
        row = VGroup(right_lab, wrong_lab).arrange(RIGHT, buff=1.2).move_to(UP * 0.9)
        self.play(FadeIn(row), run_time=0.5)
        self.wait(1.6)

        number_line = Line(LEFT * 4.5, RIGHT * 4.5, color=GHOST, stroke_width=2.5)
        number_line.move_to(DOWN * 0.4)
        truth = Dot(number_line.get_left() + RIGHT * 1.0, color=INK, radius=0.09)
        truth_lab = label("the true answer", size=16, color=INK).next_to(truth, UP, buff=0.2)
        blend_pt = Dot(number_line.get_center() + RIGHT * 0.6, color=ACC, radius=0.09)
        blend_lab = label("the blended answer", size=16, color=ACC).next_to(blend_pt, DOWN, buff=0.2)
        self.play(Create(number_line), run_time=0.5)
        self.play(FadeIn(truth), FadeIn(truth_lab), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(blend_pt), FadeIn(blend_lab), run_time=0.5)
        self.wait(4.2)

        land = serif("Erases the one fact that mattered: they disagreed.",
                      size=28, color=ACC).move_to(DOWN * 2.9)
        self.play(FadeOut(row), Write(land), run_time=0.8)
        self.wait(10.88)


# ─────────────────────────────────────────────────────────────────────────────
#  B03_DetectingDivergence   (target ~48s)
#  A two-zone gauge, driven by a widening gap between structured signal
#  cards, crossing a calibrated threshold rather than comparing raw text.
# ─────────────────────────────────────────────────────────────────────────────
class B03_DetectingDivergence(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Detecting the Divergence", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.3)

        gauge_center = np.array([0.0, -0.6, 0.0])
        g = gauge_arcs(radius=1.7)
        needle = needle_at(3 * PI / 4)
        VGroup(g, needle).move_to(gauge_center)
        z1 = label("AGREEMENT", size=16, color=INK).next_to(g, LEFT, buff=0.1).shift(UP * 0.6)
        z2 = label("DIVERGENCE", size=16, color=ACC).next_to(g, RIGHT, buff=0.1).shift(UP * 0.6)
        self.play(Create(g), Create(needle), FadeIn(z1), FadeIn(z2), run_time=0.8)
        self.wait(2.0)

        c1 = label("confidence score", size=19, color=SOFT)
        c2 = label("directional vector", size=19, color=SOFT)
        cards = VGroup(c1, c2).arrange(RIGHT, buff=1.0).next_to(g, UP, buff=0.9)
        self.play(FadeIn(cards), run_time=0.5)
        self.wait(5.6)

        # ── The gap widens; needle sweeps into divergence ──────────────────────
        target_theta = PI / 6
        new_needle = needle_at(target_theta).shift(gauge_center)
        self.play(c1.animate.set_color(INK), c2.animate.set_color(ACC),
                   Transform(needle, new_needle), run_time=1.4)
        self.wait(1.6)

        thresh = DashedLine(gauge_center, gauge_center + 1.9 * np.array([np.cos(PI / 2 - 0.35),
                                                                          np.sin(PI / 2 - 0.35), 0]),
                             color=SOFT, stroke_width=2.5, dash_length=0.12)
        self.play(Create(thresh), run_time=0.5)
        self.wait(5.4)

        caption = label("below: ignored · above: escalated", size=22, color=SOFT)
        caption.next_to(g, DOWN, buff=0.6)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(7.6)

        land = serif("Something real is happening.", size=30, color=ACC).move_to(DOWN * 3.2)
        self.play(FadeIn(land), run_time=0.6)
        self.wait(11.22)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_ArbitrationSetup   (target ~41s)
#  The two agent nameplates route through a single arbitration node with one
#  exchange each — an unbounded, spiraling debate is shown and struck.
# ─────────────────────────────────────────────────────────────────────────────
class B04_ArbitrationSetup(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("The Arbitration Step", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.2)

        a = label_chip("Agent A", INK).move_to([-3.6, 1.2, 0])
        b = label_chip("Agent B", ACC).move_to([3.6, 1.2, 0])
        self.play(FadeIn(a), FadeIn(b), run_time=0.5)
        self.wait(1.2)

        node_txt = label("ARBITRATION", size=22, color=SOFT, weight="BOLD")
        node = auto_box(node_txt, h_pad=0.35, v_pad=0.25, color=SOFT)
        node_grp = VGroup(node, node_txt).move_to(UP * 2.4)
        self.play(a.animate.move_to([-2.0, 1.2, 0]), b.animate.move_to([2.0, 1.2, 0]),
                   FadeIn(node_grp), run_time=0.7)

        arr_down_a = Arrow(node.get_bottom(), a.get_top(), buff=0.12, color=SOFT, stroke_width=2.5)
        arr_down_b = Arrow(node.get_bottom(), b.get_top(), buff=0.12, color=SOFT, stroke_width=2.5)
        arr_up_a = Arrow(a.get_top(), node.get_bottom(), buff=0.12, color=SOFT, stroke_width=2.5).shift(LEFT * 0.25)
        arr_up_b = Arrow(b.get_top(), node.get_bottom(), buff=0.12, color=SOFT, stroke_width=2.5).shift(RIGHT * 0.25)
        self.play(Create(arr_down_a), Create(arr_down_b), Create(arr_up_a), Create(arr_up_b),
                   run_time=0.7)
        self.wait(2.0)

        caption = label("one chance: defend · revise · concede", size=21, color=INK)
        caption.move_to(DOWN * 0.5)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(4.4)

        stamp_txt = label("1 ROUND ONLY", size=22, color=ACC, weight="BOLD")
        stamp = auto_box(stamp_txt, h_pad=0.3, v_pad=0.22, color=ACC)
        VGroup(stamp, stamp_txt).move_to(DOWN * 1.5)
        self.play(FadeIn(VGroup(stamp, stamp_txt), scale=1.15), run_time=0.5)
        self.wait(1.8)

        # ── The crossed-out unbounded alternative ─────────────────────────────
        spiral = ParametricFunction(
            lambda t: np.array([0.5 * t * np.cos(4 * t), 0.5 * t * np.sin(4 * t), 0]),
            t_range=[0.05, 1.3], color=GHOST, stroke_width=2.5,
        ).scale(0.9).move_to(DOWN * 2.7)
        self.play(Create(spiral), run_time=0.8)
        self.wait(0.9)
        spiral_strike = Line(spiral.get_corner(UL), spiral.get_corner(DR), color=ACC, stroke_width=3)
        tone_cap = label("persuasive tone ≠ correct", size=19, color=SOFT)
        tone_cap.next_to(spiral, RIGHT, buff=0.4)
        self.play(Create(spiral_strike), FadeIn(tone_cap), run_time=0.6)
        self.wait(5.1)

        self.play(FadeOut(VGroup(spiral, spiral_strike, tone_cap, caption)), run_time=0.5)
        land = serif("Enough to catch a plain error.", size=28, color=ACC).move_to(DOWN * 2.6)
        self.play(FadeIn(land), run_time=0.6)
        self.wait(10.83)


# ─────────────────────────────────────────────────────────────────────────────
#  B05_ArbitrationOutcomes   (target ~31s)
#  The single round branches into two named, equally legitimate outcomes:
#  RESOLVED (merged) and UNRESOLVED (both nameplates stay apart, lit).
# ─────────────────────────────────────────────────────────────────────────────
class B05_ArbitrationOutcomes(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Two Outcomes", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.1)

        node_txt = label("ARBITRATION", size=22, color=SOFT, weight="BOLD")
        node = auto_box(node_txt, h_pad=0.35, v_pad=0.25, color=SOFT)
        node_grp = VGroup(node, node_txt).move_to(UP * 2.6)
        self.play(FadeIn(node_grp), run_time=0.4)
        self.wait(0.8)

        branch_l = Arrow(node.get_bottom(), [-3.4, 0.4, 0], buff=0.1, color=SOFT, stroke_width=2.5)
        branch_r = Arrow(node.get_bottom(), [3.4, 0.4, 0], buff=0.1, color=SOFT, stroke_width=2.5)
        self.play(Create(branch_l), Create(branch_r), run_time=0.6)
        self.wait(1.0)

        # ── RESOLVED: merge ────────────────────────────────────────────────────
        res_head = label("RESOLVED", size=22, color=INK, weight="BOLD").move_to([-3.4, 0.0, 0])
        a1 = label_chip("A", INK, size=18).move_to([-4.0, -1.0, 0])
        b1 = label_chip("B", ACC, size=18).move_to([-2.8, -1.0, 0])
        merged_txt = label("one conclusion", size=17, color=INK)
        merged = bubble(merged_txt, INK).move_to([-3.4, -2.1, 0])
        self.play(FadeIn(res_head), FadeIn(a1), FadeIn(b1), run_time=0.5)
        self.wait(1.0)
        self.play(a1.animate.move_to(merged.get_center() + LEFT * 0.15),
                   b1.animate.move_to(merged.get_center() + RIGHT * 0.15),
                   run_time=0.6)
        self.play(FadeOut(a1), FadeOut(b1), FadeIn(merged), run_time=0.4)

        # ── UNRESOLVED: stay apart, both lit ──────────────────────────────────
        unres_head = label("UNRESOLVED", size=22, color=ACC, weight="BOLD").move_to([3.4, 0.0, 0])
        a2 = label_chip("A", INK, size=18).move_to([2.6, -1.4, 0])
        b2 = label_chip("B", ACC, size=18).move_to([4.2, -1.4, 0])
        self.play(FadeIn(unres_head), FadeIn(a2), FadeIn(b2), run_time=0.5)
        self.wait(3.8)

        caption = label("recorded, not smoothed over", size=19, color=SOFT)
        caption.next_to(VGroup(a2, b2), DOWN, buff=0.35)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(5.4)

        land = serif("Here is each one's case.", size=28, color=ACC).move_to(DOWN * 3.1)
        self.play(FadeIn(land), run_time=0.6)
        self.wait(8.69)


# ─────────────────────────────────────────────────────────────────────────────
#  B06_UnresolvedHandling   (target ~41s)
#  A clean report holds a boxed disagreement section — checked against a
#  ghosted version where that box was quietly folded away.
# ─────────────────────────────────────────────────────────────────────────────
class B06_UnresolvedHandling(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("What You Do With Unresolved", color=INK, size=40)
        self.play(Write(t), run_time=0.6)
        self.wait(1.3)

        doc = Rectangle(width=5.4, height=3.4, color=INK, stroke_width=2.5,
                         fill_color=INK, fill_opacity=0.03).move_to([-2.6, -0.2, 0])
        body_lines = VGroup(*[
            Line(LEFT * 2.2, RIGHT * 2.2, color=GHOST, stroke_width=1.5)
            for _ in range(4)
        ]).arrange(DOWN, buff=0.28).move_to(doc.get_center() + UP * 0.9)
        flag_txt = label("AGENTS DISAGREED —\nSEE BOTH POSITIONS", size=15, color=ACC,
                          weight="BOLD", line_spacing=0.9)
        flag_box = auto_box(flag_txt, h_pad=0.22, v_pad=0.18, color=ACC)
        flag = VGroup(flag_box, flag_txt).move_to(doc.get_center() + DOWN * 0.9)
        self.play(Create(doc), FadeIn(body_lines), run_time=0.6)
        self.wait(1.2)
        self.play(FadeIn(flag, shift=UP * 0.15), run_time=0.6)
        self.wait(5.4)

        # ── Ghosted alternate: box folded away, struck ─────────────────────────
        ghost_doc = Rectangle(width=5.4, height=3.4, color=GHOST, stroke_width=2.5,
                               fill_color=GHOST, fill_opacity=0.03).move_to([3.0, -0.2, 0])
        ghost_lines = VGroup(*[
            Line(LEFT * 2.2, RIGHT * 2.2, color=GHOST, stroke_width=1.5)
            for _ in range(6)
        ]).arrange(DOWN, buff=0.24).move_to(ghost_doc.get_center())
        self.play(FadeIn(ghost_doc), FadeIn(ghost_lines), run_time=0.6)
        self.wait(1.0)
        fold_strike = Line(ghost_doc.get_corner(UL) + DOWN * 0.3, ghost_doc.get_corner(UR) + DOWN * 0.3,
                            color=ACC, stroke_width=3)
        self.play(Create(fold_strike), run_time=0.5)
        self.wait(1.4)

        caption = label("front and center, not a footnote", size=21, color=SOFT)
        caption.move_to(DOWN * 2.6)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(7.6)

        land = serif("Tells you exactly where to look before you trust it.",
                      size=27, color=ACC).move_to(DOWN * 3.3)
        self.play(FadeOut(VGroup(doc, body_lines, flag, ghost_doc, ghost_lines, fold_strike, caption)),
                   Write(land), run_time=0.8)
        self.wait(15.96)


# ─────────────────────────────────────────────────────────────────────────────
#  B07_SharedContamination   (target ~52s)
#  The dedicated falsifiability beat: both nameplates glow the same color,
#  both pointing at one shared, cracked document neither notices.
# ─────────────────────────────────────────────────────────────────────────────
class B07_SharedContamination(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("The Blind Spot", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.5)

        a = label_chip("Agent A", SOFT).move_to([-3.4, 1.2, 0])
        b = label_chip("Agent B", SOFT).move_to([3.4, 1.2, 0])
        doc = Rectangle(width=1.3, height=1.7, color=SOFT, stroke_width=2.5,
                         fill_color=SOFT, fill_opacity=0.05).move_to(DOWN * 0.6)
        self.play(FadeIn(a), FadeIn(b), FadeIn(doc), run_time=0.6)
        self.wait(1.2)

        arr_a = Arrow(a.get_bottom(), doc.get_top() + LEFT * 0.3, buff=0.1, color=SOFT, stroke_width=2.5)
        arr_b = Arrow(b.get_bottom(), doc.get_top() + RIGHT * 0.3, buff=0.1, color=SOFT, stroke_width=2.5)
        self.play(Create(arr_a), Create(arr_b), run_time=0.6)
        self.wait(1.4)

        self.play(a[0].animate.set_color(ACC), b[0].animate.set_color(ACC), run_time=0.6)
        self.wait(1.0)

        crack = crack_line(doc, ACC)
        self.play(Create(crack), run_time=0.7)
        self.wait(4.2)

        cap1 = label("arbitration only fires on disagreement", size=21, color=SOFT)
        cap1.move_to(DOWN * 2.4)
        self.play(FadeIn(cap1), run_time=0.5)
        self.wait(4.5)

        cap2 = label("shared contamination produces agreement instead", size=21, color=SOFT)
        cap2.move_to(DOWN * 2.4)
        self.play(FadeOut(cap1), FadeIn(cap2), run_time=0.5)
        self.wait(4.5)

        cap3 = label("not a flaw a cleverer threshold fixes", size=21, color=SOFT)
        cap3.move_to(DOWN * 2.4)
        self.play(FadeOut(cap2), FadeIn(cap3), run_time=0.5)
        self.wait(4.5)

        self.play(FadeOut(VGroup(a, b, doc, arr_a, arr_b, crack, cap3)), run_time=0.6)
        land = serif("Lowers your risk. Doesn't take it to zero.",
                      size=30, color=ACC).move_to(DOWN * 0.2)
        self.play(Write(land), run_time=0.9)
        self.wait(13.21)


# ─────────────────────────────────────────────────────────────────────────────
#  B08_TheFramework   (target ~41s)
#  The four transferable rules, each paired with the icon of its mechanism,
#  collected into a 2x2 grid before the bookends.
# ─────────────────────────────────────────────────────────────────────────────
class B08_TheFramework(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("The Framework", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.6)

        def rule_row(icon, text):
            icon.scale_to_fit_height(0.5)
            txt = label(text, size=20, color=INK)
            row = VGroup(icon, txt).arrange(RIGHT, buff=0.35)
            box = auto_box(row, h_pad=0.3, v_pad=0.22, color=GHOST)
            return VGroup(box, row)

        icon1 = VGroup(Dot(color=INK, radius=0.12), Dot(color=ACC, radius=0.12)).arrange(RIGHT, buff=0.15)
        icon2 = gauge_arcs(radius=0.35)
        icon3 = CurvedArrow(LEFT * 0.22, RIGHT * 0.22, color=SOFT, stroke_width=3, angle=-TAU * 0.4)
        icon4 = Rectangle(width=0.5, height=0.4, color=ACC, stroke_width=2.5)

        r1 = rule_row(icon1, "disagreement is signal,\nnot noise")
        r2 = rule_row(icon2, "detect on structure,\nnot wording")
        r3 = rule_row(icon3, "bound the debate\nto one round")
        r4 = rule_row(icon4, "unresolved must reach\nthe output unresolved")

        grid = VGroup(
            VGroup(r1, r2).arrange(RIGHT, buff=0.6),
            VGroup(r3, r4).arrange(RIGHT, buff=0.6),
        ).arrange(DOWN, buff=0.5)
        if grid.width > 12.0:
            grid.scale(12.0 / grid.width)
        grid.move_to(DOWN * 0.3)

        for r in (r1, r2, r3, r4):
            self.play(FadeIn(r, shift=UP * 0.15), run_time=0.5)
            self.wait(2.4)

        # Montserrat (label()'s font) has no ✓ glyph — Pango silently falls
        # back to a tofu box, exactly the gotcha graphics_lib.py's checked()
        # docstring warns about. Caught in mid-scene QC as blank boxes above
        # each rule; fixed by using plain Text() (Manim's default font
        # resolves the glyph correctly), same fix checked() already applies.
        checks = VGroup(*[
            Text("✓", font_size=22, color=ACC).next_to(r, UP, buff=0.08) for r in (r1, r2, r3, r4)
        ])
        self.play(LaggedStart(*[FadeIn(c) for c in checks], lag_ratio=0.2), run_time=0.8)
        self.wait(4.2)

        footnote = serif("Lowers risk. Doesn't take it to zero.",
                          size=26, color=ACC).move_to(DOWN * 3.3)
        self.play(FadeIn(footnote), run_time=0.6)
        self.wait(12.09)
