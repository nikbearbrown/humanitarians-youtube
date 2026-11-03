"""scenes.py — Manim scenes for grading-the-machine (claude-divij).

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757, soft #73705F,
ghost #A9A491 — the Claude fidelity palette per ai-explainer SKILL.md. ONE
accent per beat. The source script's [VISUAL] color cues (a green
"PLAUSIBLE" stamp, a yellow caution highlight) are retinted the same way
prior episodes handled their own out-of-palette cues: terracotta stands
in for both, carried by label/icon/position, never a second or third hue.

Type: Montserrat (DISPLAY) / EB Garamond (SERIF, editorial only) / PT Mono
(MONO, data/code only) — see graphics_lib.py. Boxes are content-fitted via
auto_box/surround_box, never hand-measured.

Two defect classes caught on prior episodes (STEM6/STEM7) are designed
out from the start here, not fixed after the fact:
  1. title() never fades mid-scene and its own bottom edge sits close to
     y=2.9 for default sizes — nothing is placed above ~y=1.6 once the
     title is on screen.
  2. Two different text strings are never crossfaded at the same anchor
     position — every caption swap here is FadeOut-fully-then-FadeIn,
     never simultaneous at a shared point.
"""
import numpy as np
from graphics_lib import *

BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


def strike(mobj, color=None):
    return Line(mobj.get_left() + LEFT * 0.08, mobj.get_right() + RIGHT * 0.08,
                color=color if color is not None else ACC, stroke_width=3.0)


def stamp_text(text, color, size=28, angle=-0.1):
    """A rubber-stamp look: bordered text, slightly rotated as one unit."""
    t = label(text, size=size, color=color, weight="BOLD")
    box = auto_box(t, h_pad=0.3, v_pad=0.2, color=color, stroke_width=3)
    grp = VGroup(box, t)
    grp.rotate(angle)
    return grp


def stamp_content(content, color, angle=-0.1, h_pad=0.3, v_pad=0.2):
    """Same rubber-stamp look as stamp_text(), but takes a pre-built content
    mobject — used when the text needs a glyph (e.g. checkmark) that must
    bypass label()'s Montserrat font, which has no ✓ glyph and renders it
    as a tofu box (the exact defect caught here via zoomed smoke-test QC,
    the same class fixed on STEM7's B08 and designed around in STEM9)."""
    box = auto_box(content, h_pad=h_pad, v_pad=v_pad, color=color, stroke_width=3)
    grp = VGroup(box, content)
    grp.rotate(angle)
    return grp


def confidence_meter(theta, radius=1.3):
    agree = Arc(radius=radius, start_angle=PI, angle=-PI, color=SOFT, stroke_width=8)
    pivot = Dot(ORIGIN, color=SOFT, radius=0.05)
    needle = Line(ORIGIN, radius * 0.8 * np.array([np.cos(theta), np.sin(theta), 0]),
                  color=ACC, stroke_width=5)
    return VGroup(agree, pivot, needle)


def model_box(text, color=INK):
    t = label(text, size=20, color=color, weight="BOLD", line_spacing=0.85)
    box = auto_box(t, h_pad=0.3, v_pad=0.24, color=color)
    return VGroup(box, t)


def panel(text, color, box_color=None, size=22, weight=None, h_pad=0.3, v_pad=0.2, line_spacing=1.0):
    t = label(text, size=size, color=color, weight=weight, line_spacing=line_spacing)
    box = auto_box(t, h_pad=h_pad, v_pad=v_pad, color=box_color if box_color else color)
    return VGroup(box, t)


# ─────────────────────────────────────────────────────────────────────────────
#  B01_SelfReportedConfidence   (target ~45s)
# ─────────────────────────────────────────────────────────────────────────────
class B01_SelfReportedConfidence(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Self-Reported Confidence", color=INK, size=42)
        self.play(Write(t), run_time=0.6)
        self.wait(1.6)

        meter = confidence_meter(PI / 2 - 0.15).move_to(UP * 1.4)
        qmark = label("?", size=28, color=SOFT).next_to(meter, UP, buff=0.15)
        pct = label("95% Confident", size=20, color=INK).next_to(meter, DOWN, buff=0.2)
        self.play(Create(meter), FadeIn(qmark), FadeIn(pct), run_time=0.7)
        self.wait(2.4)

        self.play(FadeOut(VGroup(meter, qmark, pct)), run_time=0.5)

        model = model_box("MODEL").move_to(UP * 1.5)
        ans = label('"the answer is 42"', size=18, color=INK).next_to(model, DOWN, buff=0.35)
        conf = label('"92% confident"', size=18, color=ACC).next_to(ans, DOWN, buff=0.28)
        self.play(FadeIn(model), run_time=0.5)
        self.wait(0.8)
        self.play(FadeIn(ans), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(conf), run_time=0.5)
        self.wait(1.6)

        arr1 = DashedLine(model.get_bottom() + LEFT * 0.3, ans.get_top(), color=SOFT,
                           stroke_width=2, dash_length=0.1)
        arr2 = DashedLine(model.get_bottom() + RIGHT * 0.3, conf.get_top(), color=SOFT,
                           stroke_width=2, dash_length=0.1)
        self.play(Create(arr1), Create(arr2), run_time=0.6)
        same_cap = label("same mechanism, both times", size=17, color=SOFT).next_to(conf, DOWN, buff=0.4)
        self.play(FadeIn(same_cap), run_time=0.5)
        self.wait(5.1)

        self.play(FadeOut(VGroup(model, ans, conf, arr1, arr2, same_cap)), run_time=0.6)
        cap1 = label("no separate, more-honest module watching itself", size=20, color=INK)
        cap1.move_to(DOWN * 2.4)
        self.play(FadeIn(cap1), run_time=0.5)
        self.wait(5.5)

        self.play(FadeOut(cap1), run_time=0.3)
        cap2 = label("measures how confident it sounds —\nnot how well-founded it is",
                      size=20, color=SOFT, line_spacing=0.9)
        cap2.move_to(DOWN * 2.4)
        self.play(FadeIn(cap2), run_time=0.4)
        self.wait(5.5)

        self.play(FadeOut(cap2), run_time=0.4)
        land = serif("Those two things correlate\nloosely at best.",
                      size=28, color=ACC, line_spacing=1.0).move_to(DOWN * 0.2)
        self.play(Write(land), run_time=0.9)
        self.wait(8.35)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_LLMAsJudge   (target ~56s)
# ─────────────────────────────────────────────────────────────────────────────
class B02_LLMAsJudge(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("LLM-as-a-Judge", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.6)

        model_a = model_box("MODEL A", color=INK).move_to([-3.2, 1.5, 0])
        model_b = model_box("MODEL B\n(JUDGE)", color=SOFT).move_to([3.2, 1.5, 0])
        self.play(FadeIn(model_a), FadeIn(model_b), run_time=0.6)
        self.wait(1.2)

        justification = label('"...therefore, 42"', size=18, color=INK)
        justification.next_to(model_a, DOWN, buff=0.35)
        self.play(FadeIn(justification), run_time=0.5)
        self.wait(1.6)

        arrow = Arrow(justification.get_right(), model_b.get_bottom() + LEFT * 0.3, buff=0.15,
                       color=SOFT, stroke_width=2.5, path_arc=-0.5)
        self.play(Create(arrow), run_time=0.6)
        self.wait(0.8)

        plausible_word = label("PLAUSIBLE", size=24, color=INK, weight="BOLD")
        plausible_check = Text("✓", font_size=24, color=INK)
        plausible_content = VGroup(plausible_word, plausible_check).arrange(RIGHT, buff=0.15)
        plausible = stamp_content(plausible_content, INK, angle=-0.06).move_to(DOWN * 0.5)
        self.play(FadeIn(plausible, scale=1.2), run_time=0.6)
        self.wait(7.08)

        cap1 = label("genuine reasoning vs. fluent rationalization —\nidentical from outside",
                      size=19, color=SOFT, line_spacing=0.9)
        cap1.move_to(DOWN * 2.4)
        self.play(FadeIn(cap1), run_time=0.6)
        self.wait(8.28)

        self.play(FadeOut(cap1), run_time=0.4)
        error_stamp = stamp_text("CATEGORY ERROR", ACC, size=27, angle=0.1)
        error_stamp.move_to(DOWN * 0.55 + RIGHT * 0.1)
        self.play(FadeIn(error_stamp, scale=1.3), run_time=0.7)
        self.wait(7.68)

        cap2 = label("a second opinion, same blind spot as the first", size=20, color=ACC)
        cap2.move_to(DOWN * 2.4)
        self.play(FadeIn(cap2), run_time=0.5)
        self.wait(8.68)

        self.play(FadeOut(VGroup(model_a, model_b, justification, arrow, plausible,
                                  error_stamp, cap2)), run_time=0.6)
        land = serif("Serious systems that considered this\nwalked away from it.",
                      size=27, color=ACC, line_spacing=1.0).move_to(DOWN * 0.2)
        self.play(Write(land), run_time=1.0)
        self.wait(11.08)


# ─────────────────────────────────────────────────────────────────────────────
#  B03_ComputedNotReported   (target ~54s)
# ─────────────────────────────────────────────────────────────────────────────
class B03_ComputedNotReported(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Computed, Not Reported", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.8)

        base = mono("Base score: 1.0", size=24, color=INK).move_to(UP * 1.5)
        self.play(FadeIn(base), run_time=0.5)
        self.wait(2.2)

        line_a = mono("Source A: SIMULATED   -0.1", size=20, color=ACC)
        line_a.next_to(base, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(FadeIn(line_a), run_time=0.5)
        self.wait(2.0)

        line_b = mono("Source B: FAILED        -0.1", size=20, color=ACC)
        line_b.next_to(line_a, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeIn(line_b), run_time=0.5)
        self.wait(2.0)

        rule = Line(line_b.get_left(), line_b.get_left() + RIGHT * line_b.width,
                    color=SOFT, stroke_width=2)
        rule.next_to(line_b, DOWN, buff=0.2)
        final = mono("Final: 0.8", size=24, color=INK, weight="BOLD")
        final.next_to(rule, DOWN, buff=0.3)
        self.play(Create(rule), FadeIn(final), run_time=0.6)
        self.wait(10.06)

        cap1 = label("no language model anywhere in this loop", size=21, color=SOFT)
        cap1.move_to(DOWN * 2.5)
        self.play(FadeIn(cap1), run_time=0.5)
        self.wait(10.06)

        self.play(FadeOut(cap1), run_time=0.3)
        cap2 = label("knows if the data held up —\nnot if the writing was persuasive",
                      size=21, color=SOFT, line_spacing=0.9)
        cap2.move_to(DOWN * 2.5)
        self.play(FadeIn(cap2), run_time=0.4)
        self.wait(10.86)

        self.play(FadeOut(VGroup(base, line_a, line_b, rule, final, cap2)), run_time=0.6)
        land = serif("Fluent prose was never an input\nto the calculation.",
                      size=28, color=ACC, line_spacing=1.0).move_to(DOWN * 0.2)
        self.play(Write(land), run_time=1.0)
        self.wait(13.46)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_NeverSuppress   (target ~40s)
# ─────────────────────────────────────────────────────────────────────────────
class B04_NeverSuppress(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Never Suppress a Low Score", color=INK, size=40)
        self.play(Write(t), run_time=0.6)
        self.wait(1.6)

        result = mono("Confidence: 0.4", size=22, color=SOFT).move_to(UP * 1.5)
        self.play(FadeIn(result), run_time=0.5)
        self.wait(1.4)

        branch_l = Arrow(result.get_bottom(), [-3.4, -0.1, 0], buff=0.1, color=SOFT, stroke_width=2.5)
        branch_r = Arrow(result.get_bottom(), [3.4, -0.1, 0], buff=0.1, color=SOFT, stroke_width=2.5)
        self.play(Create(branch_l), Create(branch_r), run_time=0.6)
        self.wait(0.8)

        hide_head = label("Hide it", size=22, color=SOFT, weight="BOLD").move_to([-3.4, -0.5, 0])
        hide_report = label("...clean answer,\nno caveat shown", size=15, color=GHOST, line_spacing=0.85)
        hide_report.next_to(hide_head, DOWN, buff=0.3)
        self.play(FadeIn(hide_head), FadeIn(hide_report), run_time=0.5)
        self.wait(1.2)
        hide_strike = strike(VGroup(hide_head, hide_report), color=ACC)
        self.play(Create(hide_strike), run_time=0.5)
        self.wait(5.17)

        flag_head = label("Flag it", size=22, color=INK, weight="BOLD").move_to([3.4, -0.5, 0])
        flag_report = label("HIGH UNCERTAINTY /\nSPECULATIVE", size=15, color=ACC, weight="BOLD",
                             line_spacing=0.85)
        flag_report.next_to(flag_head, DOWN, buff=0.3)
        flag_box = surround_box(flag_report, buff=0.15, color=ACC)
        self.play(FadeIn(flag_head), FadeIn(flag_report), Create(flag_box), run_time=0.6)
        self.wait(5.97)

        cap = label("a footnote doesn't count", size=21, color=INK).move_to(DOWN * 2.6)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(7.17)

        self.play(FadeOut(VGroup(result, branch_l, branch_r, hide_head, hide_report, hide_strike,
                                  flag_head, flag_report, flag_box, cap)), run_time=0.6)
        land = serif("The warning itself is\nthe safety mechanism.",
                      size=28, color=ACC, line_spacing=1.0).move_to(DOWN * 0.2)
        self.play(Write(land), run_time=0.9)
        self.wait(9.27)


# ─────────────────────────────────────────────────────────────────────────────
#  B05_StillALiveRisk   (target ~50s)
# ─────────────────────────────────────────────────────────────────────────────
class B05_StillALiveRisk(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("This Is Still a Live Risk", color=INK, size=40)
        self.play(Write(t), run_time=0.6)
        self.wait(1.8)

        base = mono("Base score: 1.0", size=22, color=INK).move_to(UP * 1.5)
        line_a = mono("Source A: SIMULATED   -0.1", size=19, color=ACC)
        line_a.next_to(base, DOWN, buff=0.35, aligned_edge=LEFT)
        line_b = mono("Source B: FAILED        -0.1", size=19, color=ACC)
        line_b.next_to(line_a, DOWN, buff=0.28, aligned_edge=LEFT)
        rule = Line(line_b.get_left(), line_b.get_left() + RIGHT * line_b.width,
                    color=SOFT, stroke_width=2)
        rule.next_to(line_b, DOWN, buff=0.18)
        final = mono("Final: 0.8", size=22, color=INK, weight="BOLD")
        final.next_to(rule, DOWN, buff=0.25)
        ledger = VGroup(base, line_a, line_b, rule, final)
        self.play(FadeIn(ledger), run_time=0.7)
        self.wait(7.3)

        ring_a = surround_box(line_a, buff=0.08, color=ACC, stroke_width=2)
        ring_b = surround_box(line_b, buff=0.08, color=ACC, stroke_width=2)
        self.play(Create(ring_a), Create(ring_b), run_time=0.6)
        tag = label("Uncalibrated — pending backtesting", size=17, color=ACC)
        tag.next_to(final, DOWN, buff=0.4)
        self.play(FadeIn(tag), run_time=0.5)
        self.wait(8.1)

        self.play(FadeOut(VGroup(ledger, ring_a, ring_b, tag)), run_time=0.6)
        cap1 = label("we replaced an opinion with an equation", size=20, color=SOFT)
        cap1.move_to(DOWN * 2.5)
        self.play(FadeIn(cap1), run_time=0.5)
        self.wait(8.3)

        self.play(FadeOut(cap1), run_time=0.3)
        cap2 = label("now we owe ourselves the work\nof checking the constants",
                      size=20, color=SOFT, line_spacing=0.9)
        cap2.move_to(DOWN * 2.5)
        self.play(FadeIn(cap2), run_time=0.4)
        self.wait(8.7)

        self.play(FadeOut(cap2), run_time=0.4)
        land = serif("You can't calibrate a number\nthat was never written down.",
                      size=27, color=ACC, line_spacing=1.0).move_to(DOWN * 0.2)
        self.play(Write(land), run_time=1.0)
        self.wait(11.1)


# ─────────────────────────────────────────────────────────────────────────────
#  B06_TheFramework   (target ~44s)
# ─────────────────────────────────────────────────────────────────────────────
class B06_TheFramework(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("The Framework", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(2.0)

        p1 = panel("Self-graded — biased", SOFT)
        p2 = panel("AI-judged — category error", SOFT)
        p3 = panel("Computed — inspectable,\nstill being calibrated", INK, box_color=ACC,
                    weight="BOLD", line_spacing=0.85, h_pad=0.32, v_pad=0.24)

        stack = VGroup(p1, p2, p3).arrange(DOWN, buff=0.35).move_to(DOWN * 0.3)

        self.play(FadeIn(p1, shift=UP * 0.15), run_time=0.5)
        self.wait(5.47)
        self.play(FadeIn(p2, shift=UP * 0.15), run_time=0.5)
        self.wait(5.47)
        self.play(FadeIn(p3, shift=UP * 0.15), run_time=0.5)
        self.wait(4.67)

        lock_body = Circle(radius=0.12, color=ACC, stroke_width=2.5)
        lock_body.next_to(p3, RIGHT, buff=0.35)
        lock_gap = Line(lock_body.get_top() + UP * 0.02, lock_body.get_top() + UP * 0.16,
                         color=ACC, stroke_width=2.5)
        auditable = label("auditable", size=15, color=ACC).next_to(lock_body, DOWN, buff=0.15)
        self.play(FadeIn(lock_body), FadeIn(lock_gap), FadeIn(auditable), run_time=0.5)
        self.wait(6.47)

        self.play(FadeOut(VGroup(stack, lock_body, lock_gap, auditable)), run_time=0.6)
        land = serif("Find the mistakes and fix them —\nthat's the actual bar.",
                      size=27, color=ACC, line_spacing=1.0).move_to(DOWN * 0.2)
        self.play(Write(land), run_time=1.0)
        self.wait(9.07)
