"""vox_scenes.py — Why Trying Harder to Sound Academic Makes Your Writing Less Academic
(vox-academic-register, slate cut, 16:9).

One Scene per GRAPHIC / CARD beat whose source is own. B01 is the only STILL
(ai media slot) and has no scene here.

Color law (teardown palette):
  CRIMSON = both failure modes (overshoot RIGHT, refusal LEFT)
  INK (plain) = the target zone — analytical work in the clearest possible sentences
  SLATE = structural labels and scaffold

Conventions:
  - Single-method .animate chains only
  - Every scene needs real shape motion
  - Font-safe glyphs only (no arrows, checks, not-equal, multiply-sign as text)
  - Anchor-not-transcript: on-screen text never copies the narration sentence
  - W7: kicker is WRITING, never chapter or book title
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B02": 10.0, "B03": 11.0, "B04": 12.0, "B05": 11.0,
    "B06": 13.0, "B07": 14.0, "B08": 12.0, "B09": 10.0,
    "B10": 14.0, "B11": 11.0, "B12": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 10.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _bar(w=5.0, h=0.12, color=INK):
    b = Rectangle(width=w, height=h)
    b.set_fill(color, 1).set_stroke(width=0, opacity=0)
    return b


def _tick_mark(x_pos, y_pos, label_text, color=INK, size=22):
    """A short vertical tick on the spectrum with a label below."""
    tick = Line(
        np.array([x_pos, y_pos - 0.18, 0]),
        np.array([x_pos, y_pos + 0.18, 0]),
        stroke_width=2.5, color=color
    )
    lbl = Text(label_text, font=DISPLAY, color=color, font_size=size)
    lbl.move_to(np.array([x_pos, y_pos - 0.52, 0]))
    return VGroup(tick, lbl)


def _spectrum_bar(width=11.0):
    """The horizontal spectrum bar — the main visual object."""
    bar = Rectangle(width=width, height=0.18)
    bar.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
    return bar


def _spectrum_target(bar, target_w=2.8):
    """The narrow target zone — teal-colored segment at center."""
    t = Rectangle(width=target_w, height=0.18)
    t.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
    t.move_to(bar.get_center())
    return t


def _marker_dot(color=CRIMSON, r=0.22):
    d = Circle(radius=r)
    d.set_fill(color, 1).set_stroke(width=0, opacity=0)
    return d


# ---------------------------------------------------------------- scenes

class B02_BorderLine(Scene):
    """COLD OPEN — the unmarked border between two registers."""
    def construct(self):
        total = DUR["B02"]
        # Two labels on opposite sides of a dividing line
        left_lbl = Text("sounds like you", font=SERIF, color=INK, font_size=36)
        right_lbl = Text("sounds academic", font=SERIF, color=INK, font_size=36)
        left_lbl.move_to(LEFT * 3.6)
        right_lbl.move_to(RIGHT * 3.6)
        divider = Line(UP * 1.8, DOWN * 1.8, stroke_width=2.5, color=SLATE)
        divider.move_to(ORIGIN)
        # q_mark placed off-center so it does not cross the divider line
        q_mark = Text("?", font=DISPLAY, color=CRIMSON, font_size=72)
        q_mark.move_to(LEFT * 0.6 + UP * 0.5)
        # Gap label below
        gap_lbl = SerifLabel("the border is not marked", CRIMSON, size=24)
        gap_lbl.move_to(DOWN * 2.2)

        self.play(FadeIn(left_lbl, shift=RIGHT * 0.4),
                  FadeIn(right_lbl, shift=LEFT * 0.4), run_time=1.0)
        self.play(Create(divider), run_time=0.8)
        self.play(FadeIn(q_mark, scale=0.7), run_time=0.6)
        self.play(FadeIn(gap_lbl, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.0))


class B03_QuestionCard(Scene):
    """THE QUESTION — named on screen and in narration."""
    def construct(self):
        total = DUR["B03"]
        eyebrow = LabelChip("WRITING", accent=SLATE, size=22)
        eyebrow.move_to(UP * 2.8)
        q_line1 = Text("Why does trying harder to", font=DISPLAY, color=INK, font_size=40)
        q_line2 = Text("sound academic make writing", font=DISPLAY, color=INK, font_size=40)
        q_line3 = Text("less academic?", font=DISPLAY, color=CRIMSON, font_size=40)
        block = VGroup(q_line1, q_line2, q_line3).arrange(DOWN, buff=0.22)
        block.move_to(ORIGIN)
        sub = Text("two failure modes", font=SERIF, color=SLATE, font_size=28, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.55)

        self.play(FadeIn(eyebrow, scale=0.9), run_time=0.5)
        self.play(FadeIn(q_line1, shift=UP * 0.15), run_time=0.5)
        self.play(FadeIn(q_line2, shift=UP * 0.15), run_time=0.5)
        self.play(FadeIn(q_line3, scale=0.9), run_time=0.6)
        self.play(q_line3.animate.scale(1.06), run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.0))


class B04_ReachForAcademic(Scene):
    """THE PROBLEM — feedback lands; student reaches for Latinate features."""
    def construct(self):
        total = DUR["B04"]
        # Feedback chip at top
        feedback = LabelChip("feedback: try to sound more academic", accent=CRIMSON, size=22)
        feedback.move_to(UP * 2.8)
        # Arrow pointing down
        arrow = Line(UP * 2.0, UP * 1.0, stroke_width=3, color=CRIMSON)
        arrow_tip = Triangle(color=CRIMSON).scale(0.13).set_fill(CRIMSON, 1)
        arrow_tip.set_stroke(width=0, opacity=0)
        arrow_tip.move_to(arrow.get_end()).rotate(-PI / 2)

        # Feature labels stacking in
        features = [
            "Latinate vocabulary",
            "passive constructions",
            "nominalized verbs",
            "three clauses before the verb",
        ]
        feature_mobs = VGroup(*[
            Text(f, font=SERIF, color=INK, font_size=30, slant=ITALIC)
            for f in features
        ]).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        feature_mobs.move_to(DOWN * 0.2 + LEFT * 1.5)

        # Label chips for each feature
        chips = VGroup(*[
            LabelChip("signal", accent=CRIMSON, size=18)
            for _ in features
        ])
        for chip, feat in zip(chips, feature_mobs):
            chip.next_to(feat, RIGHT, buff=0.3)

        self.play(FadeIn(feedback, scale=0.9), run_time=0.6)
        self.play(Create(arrow), FadeIn(arrow_tip), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(f, shift=RIGHT * 0.3) for f in feature_mobs],
                        lag_ratio=0.18),
            run_time=1.4
        )
        self.play(
            LaggedStart(*[FadeIn(c, scale=0.8) for c in chips],
                        lag_ratio=0.18),
            run_time=1.0
        )
        self.wait(max(0.5, total - 3.5))


class B05_RefusalSide(Scene):
    """THE PROBLEM — refusal: the writer turns away from the academic zone."""
    def construct(self):
        total = DUR["B05"]
        # Two zones: personal voice (left) and academic conventions (right)
        left_box = Rectangle(width=4.2, height=2.6)
        left_box.set_fill(INK, 0.06).set_stroke(INK, 1.5)
        left_box.move_to(LEFT * 3.0)
        right_box = Rectangle(width=4.2, height=2.6)
        right_box.set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 1.5)
        right_box.move_to(RIGHT * 3.0)

        left_head = SerifLabel("authentic voice", INK, size=26)
        left_head.next_to(left_box, UP, buff=0.2)
        right_head = SerifLabel("academic conventions", CRIMSON, size=26)
        right_head.next_to(right_box, UP, buff=0.2)

        # Gap: the writer stays left
        writer_dot = Circle(radius=0.28)
        writer_dot.set_fill(INK, 1).set_stroke(width=0, opacity=0)
        writer_dot.move_to(left_box.get_center())

        # "betrayal" label at center
        label = LabelChip("reads as betrayal", accent=CRIMSON, size=22)
        label.move_to(ORIGIN + DOWN * 2.4)

        self.play(FadeIn(left_box, shift=RIGHT * 0.3),
                  FadeIn(right_box, shift=LEFT * 0.3),
                  FadeIn(left_head), FadeIn(right_head), run_time=1.0)
        self.play(FadeIn(writer_dot, scale=0.6), run_time=0.5)
        # Writer dot stays in left box — it does NOT move right
        self.play(writer_dot.animate.shift(LEFT * 0.5), run_time=0.8)
        self.play(FadeIn(label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.9))


class B06_Spectrum(Scene):
    """THE MECHANISM — the horizontal spectrum visual object introduced."""
    def construct(self):
        total = DUR["B06"]
        bar = _spectrum_bar(width=11.0)
        bar.move_to(ORIGIN)
        target = _spectrum_target(bar, target_w=2.8)

        # End labels
        left_end = LabelChip("Refuses translation", accent=CRIMSON, size=22)
        left_end.next_to(bar, UP, buff=0.55).align_to(bar, LEFT)
        right_end = LabelChip("Overshoots to jargon", accent=CRIMSON, size=22)
        right_end.next_to(bar, UP, buff=0.55).align_to(bar, RIGHT)

        # Center label
        center_lbl = SerifLabel("analytical work in the\nclearest possible sentences", INK, size=22)
        center_lbl.next_to(target, DOWN, buff=0.5)

        self.play(Create(bar), run_time=0.9)
        self.play(FadeIn(left_end, shift=RIGHT * 0.3),
                  FadeIn(right_end, shift=LEFT * 0.3), run_time=0.8)
        self.play(FadeIn(target, scale=0.8), run_time=0.7)
        self.play(FadeIn(center_lbl, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 3.1))


class B07_SpectrumTrace(Scene):
    """THE MECHANISM — marker traces to OVERSHOOT; sentence transforms."""
    def construct(self):
        total = DUR["B07"]
        bar = _spectrum_bar(width=11.0)
        bar.move_to(UP * 0.6)
        target = _spectrum_target(bar, target_w=2.8)

        left_end = LabelChip("Refuses translation", accent=CRIMSON, size=20)
        left_end.next_to(bar, UP, buff=0.45).align_to(bar, LEFT)
        right_end = LabelChip("Overshoots to jargon", accent=CRIMSON, size=20)
        right_end.next_to(bar, UP, buff=0.45).align_to(bar, RIGHT)

        # Marker starts at center
        marker = _marker_dot(color=CRIMSON)
        marker.move_to(bar.get_center())

        # Sentence at center (clear version) — anchor phrase only
        sent_clear = Text("the war began because the diplomats ran out of moves",
                          font=SERIF, color=INK, font_size=22)
        sent_clear.move_to(DOWN * 1.2)

        # Sentence after moving to overshoot (jargon version)
        # Use VGroup of individual lines for reliable width control
        jargon_lines = [
            "the occurrence of hostilities",
            "was precipitated by the incapacity",
            "of diplomatic mechanisms",
            "to produce resolution",
        ]
        sent_jargon = VGroup(*[
            Text(ln, font=SERIF, color=CRIMSON, font_size=20)
            for ln in jargon_lines
        ]).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        sent_jargon.move_to(DOWN * 1.8)

        # Strip label
        strip_lbl = SerifLabel("strip the surface features:", INK, size=22)
        strip_lbl.move_to(DOWN * 2.6)
        nothing_lbl = LabelChip("nothing underneath", accent=CRIMSON, size=22)
        nothing_lbl.next_to(strip_lbl, DOWN, buff=0.3)

        self.play(Create(bar), FadeIn(target), run_time=0.7)
        self.play(FadeIn(left_end), FadeIn(right_end), run_time=0.6)
        self.play(FadeIn(marker, scale=0.6), run_time=0.4)
        self.play(FadeIn(sent_clear, shift=UP * 0.15), run_time=0.6)

        # Move marker RIGHT toward overshoot
        overshoot_x = bar.get_right()[0] - 1.0
        self.play(marker.animate.move_to(np.array([overshoot_x, bar.get_center()[1], 0])),
                  run_time=1.0)
        # Transform sentence to jargon
        self.play(ReplacementTransform(sent_clear, sent_jargon), run_time=0.9)
        self.play(FadeIn(strip_lbl, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(nothing_lbl, scale=0.8), run_time=0.5)
        self.wait(max(0.5, total - 4.7))


class B08_RefusalTrace(Scene):
    """THE MECHANISM — marker traces to REFUSAL; conventions = the work."""
    def construct(self):
        total = DUR["B08"]
        bar = _spectrum_bar(width=11.0)
        bar.move_to(UP * 0.6)
        target = _spectrum_target(bar, target_w=2.8)

        left_end = LabelChip("Refuses translation", accent=CRIMSON, size=20)
        left_end.next_to(bar, UP, buff=0.45).align_to(bar, LEFT)
        right_end = LabelChip("Overshoots to jargon", accent=CRIMSON, size=20)
        right_end.next_to(bar, UP, buff=0.45).align_to(bar, RIGHT)

        marker = _marker_dot(color=CRIMSON)
        marker.move_to(bar.get_center())

        # Refusal: writer stays left of the target
        refusal_x = bar.get_left()[0] + 1.0

        # Convention labels that appear (what the conventions actually do)
        conv_items = [
            "cite sources -- the reader checks the reasoning",
            "define terms -- ensure disagreements are real",
        ]
        conv_mobs = VGroup(*[
            Text(c, font=SERIF, color=INK, font_size=24, slant=ITALIC)
            for c in conv_items
        ]).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        conv_mobs.move_to(DOWN * 1.5 + LEFT * 0.5)

        lbl = SerifLabel("conventions = the work the genre does", INK, size=22)
        lbl.move_to(DOWN * 2.8)

        self.play(Create(bar), FadeIn(target), run_time=0.7)
        self.play(FadeIn(left_end), FadeIn(right_end), run_time=0.6)
        self.play(FadeIn(marker, scale=0.6), run_time=0.4)

        # Move marker LEFT to refusal zone
        self.play(marker.animate.move_to(np.array([refusal_x, bar.get_center()[1], 0])),
                  run_time=1.0)
        self.play(
            LaggedStart(*[FadeIn(c, shift=RIGHT * 0.3) for c in conv_mobs],
                        lag_ratio=0.3),
            run_time=1.0
        )
        self.play(FadeIn(lbl, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 4.3))


class B09_BothFailures(Scene):
    """THE IMPLICATION — both failure markers on spectrum simultaneously."""
    def construct(self):
        total = DUR["B09"]
        bar = _spectrum_bar(width=11.0)
        bar.move_to(UP * 0.6)
        target = _spectrum_target(bar, target_w=2.8)

        left_end = LabelChip("Refuses translation", accent=CRIMSON, size=20)
        left_end.next_to(bar, UP, buff=0.45).align_to(bar, LEFT)
        right_end = LabelChip("Overshoots to jargon", accent=CRIMSON, size=20)
        right_end.next_to(bar, UP, buff=0.45).align_to(bar, RIGHT)

        # Both failure markers
        refusal_x = bar.get_left()[0] + 1.0
        overshoot_x = bar.get_right()[0] - 1.0

        marker_r = _marker_dot(color=CRIMSON, r=0.20)
        marker_r.move_to(np.array([refusal_x, bar.get_center()[1], 0]))
        marker_o = _marker_dot(color=CRIMSON, r=0.20)
        marker_o.move_to(np.array([overshoot_x, bar.get_center()[1], 0]))

        lbl_r = Text("refusal", font=SERIF, color=CRIMSON, font_size=24)
        lbl_r.move_to(np.array([refusal_x, bar.get_center()[1] - 0.6, 0]))
        lbl_o = Text("overshoot", font=SERIF, color=CRIMSON, font_size=24)
        lbl_o.move_to(np.array([overshoot_x, bar.get_center()[1] - 0.6, 0]))

        # Center "target" label below the target zone
        center_lbl = SerifLabel("the target", INK, size=22)
        center_lbl.move_to(DOWN * 0.3)

        # Structural reason label
        reason = SerifLabel("same structural failure: surface over substance", CRIMSON, size=22)
        reason.move_to(DOWN * 1.9)

        self.play(Create(bar), FadeIn(target), run_time=0.7)
        self.play(FadeIn(left_end), FadeIn(right_end), run_time=0.6)
        self.play(FadeIn(marker_r, scale=0.6), FadeIn(lbl_r, shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(marker_o, scale=0.6), FadeIn(lbl_o, shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(center_lbl, scale=0.9), run_time=0.5)
        self.play(FadeIn(reason, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.6))


class B10_SentenceExample(Scene):
    """THE EXAMPLE — two sentences at different spectrum positions."""
    def construct(self):
        total = DUR["B10"]
        # Mini spectrum bar at top for orientation
        mini_bar = _spectrum_bar(width=9.0)
        mini_bar.move_to(UP * 3.0)
        mini_target = _spectrum_target(mini_bar, target_w=2.1)

        # Jargon sentence — at overshoot position
        overshoot_x = mini_bar.get_right()[0] - 0.9
        o_marker = _marker_dot(color=CRIMSON, r=0.15)
        o_marker.move_to(np.array([overshoot_x, mini_bar.get_center()[1], 0]))

        # Clear sentence — at target position
        c_marker = _marker_dot(color=INK, r=0.15)
        c_marker.move_to(mini_bar.get_center())

        # Jargon sentence
        label_o = LabelChip("overshoot", accent=CRIMSON, size=20)
        label_o.move_to(UP * 1.8 + LEFT * 0.3)
        sent_o_a = Text(
            '"the occurrence of hostilities was precipitated',
            font=SERIF, color=CRIMSON, font_size=26
        )
        sent_o_b = Text(
            'by the incapacity of diplomatic mechanisms to produce resolution"',
            font=SERIF, color=CRIMSON, font_size=26
        )
        jargon_block = VGroup(sent_o_a, sent_o_b).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        jargon_block.move_to(UP * 0.9 + LEFT * 0.3)

        # Clear sentence
        label_c = LabelChip("target", accent=SLATE, size=20)
        label_c.move_to(DOWN * 0.6 + LEFT * 0.3)
        sent_c = Text(
            '"the war began because the diplomats ran out of moves"',
            font=SERIF, color=INK, font_size=28
        )
        sent_c.move_to(DOWN * 1.4 + LEFT * 0.3)

        divider = Line(LEFT * 5.5, RIGHT * 5.5, stroke_width=1.2, color=SLATE)
        divider.move_to(DOWN * 0.1)

        # Bottom verdict
        verdict = SerifLabel("the analysis is the same. the prose is not.", INK, size=22)
        verdict.move_to(DOWN * 2.7)

        # Animate in the mini bar first
        self.play(Create(mini_bar), FadeIn(mini_target), run_time=0.6)
        self.play(FadeIn(o_marker, scale=0.6), run_time=0.4)

        # Overshoot sentence appears
        self.play(FadeIn(label_o, scale=0.8), run_time=0.4)
        self.play(FadeIn(jargon_block, shift=RIGHT * 0.3), run_time=0.7)

        # Divider
        self.play(Create(divider), run_time=0.5)

        # Clear sentence appears; marker at target
        self.play(FadeIn(c_marker, scale=0.6), run_time=0.4)
        self.play(FadeIn(label_c, scale=0.8), run_time=0.4)
        self.play(FadeIn(sent_c, shift=RIGHT * 0.3), run_time=0.7)

        self.play(FadeIn(verdict, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 4.7))


class B11_PracticeCard(Scene):
    """THE PRACTICE — the actionable heuristic."""
    def construct(self):
        total = DUR["B11"]
        eyebrow = LabelChip("THE PRACTICE", accent=SLATE, size=22)
        eyebrow.move_to(UP * 2.8)

        heuristic = Text("Read in the genre", font=DISPLAY, color=INK, font_size=52)
        heuristic2 = Text("before you write in it.", font=DISPLAY, color=INK, font_size=52)
        block = VGroup(heuristic, heuristic2).arrange(DOWN, buff=0.22)
        block.move_to(UP * 0.2)

        underline = Line(
            heuristic2.get_corner(DL) + DOWN * 0.14,
            heuristic2.get_corner(DR) + DOWN * 0.14,
            stroke_width=2.2, color=CRIMSON
        )

        sub = Text("not to imitate -- to understand", font=SERIF, color=SLATE,
                   font_size=28, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.6)

        self.play(FadeIn(eyebrow, scale=0.9), run_time=0.5)
        self.play(FadeIn(heuristic, shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(heuristic2, shift=UP * 0.15), Create(underline), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.4))


class B12_EndCard(Scene):
    """RECAP endcard — question to answer, WRITING kicker."""
    def construct(self):
        total = DUR["B12"]
        kicker = LabelChip("WRITING", accent=SLATE, size=22)
        kicker.move_to(UP * 2.8)

        line1 = Text("The signal is not the work.", font=DISPLAY, color=INK, font_size=54)
        line1.move_to(UP * 0.4)
        underline = Line(
            line1.get_corner(DL) + DOWN * 0.16,
            line1.get_corner(DR) + DOWN * 0.16,
            stroke_width=2.2, color=CRIMSON
        )

        sub = Text("surface features vs. analytical substance", font=SERIF,
                   color=SLATE, font_size=28, slant=ITALIC)
        sub.next_to(underline, DOWN, buff=0.55)

        self.play(FadeIn(kicker, scale=0.9), run_time=0.5)
        self.play(FadeIn(line1, shift=UP * 0.15), run_time=0.8)
        self.play(Create(underline), run_time=0.6)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))
