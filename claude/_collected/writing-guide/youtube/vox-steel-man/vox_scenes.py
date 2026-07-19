"""vox_scenes.py — Why Steel-Manning the Opposition Makes Your Argument
Harder to Attack (vox-steel-man, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat (source: own). B02 and B11 are STILL ai beats
with no scene here. B01 and B12 are CARD beats rendered as Manim title/endcard.

Color law:
  TEAL    (#1F6F5C, newsprint palette) = steel man — honest, strong, credible
  CRIMSON (#BF3339, newsprint palette) = straw man — softened, dismissible
  GOLD    (#F5D061) = editor-pen sweep, fill only, once (B09 only)
  SLATE   (#3E5559) = structure / entity cards
  INK     (#2F2A26) = all body text

Exclusions: NO claim-construction mechanics, NO LBJ example, NO position-argument
structure overview, NO thesis-first/delayed-thesis, NO voice/measured-advocacy.

Gate B convention: every zero-width stroke is also zero-opacity.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

# Duration lookup — estimates; overridden by actual_duration_s after audio lock
DUR = {
    "B01": 11.0, "B03": 12.0, "B04": 11.0, "B05": 12.0, "B06": 13.0,
    "B07": 14.0, "B08": 10.0, "B09": 11.0, "B10": 12.0, "B12": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 9.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _panel_box(center, w, h, fill_color=WHITE, fill_opacity=0.15,
               stroke_color=None, stroke_width=1.8):
    """A framed panel rectangle."""
    if stroke_color is None:
        stroke_color = INK
    p = Rectangle(width=w, height=h)
    p.set_fill(fill_color, fill_opacity)
    p.set_stroke(stroke_color, stroke_width)
    p.move_to(center)
    return p


def _attention_line(left_x, right_x, y_base, y_end, color=CRIMSON):
    """A reader-attention line from left to right, dropping from y_base to y_end.
    Returns a VMobject path."""
    mid_x = (left_x + right_x) / 2.0
    pts = [
        np.array([left_x, y_base, 0]),
        np.array([mid_x * 0.6 + left_x * 0.4, y_base, 0]),
        np.array([right_x, y_end, 0]),
    ]
    line = VMobject(color=color, stroke_width=3)
    line.set_points_smoothly(pts)
    return line


def _attention_line_flat(left_x, right_x, y_val, color=TEAL):
    """A flat (non-dropping) reader-attention line."""
    pts = [
        np.array([left_x, y_val, 0]),
        np.array([(left_x + right_x) / 2, y_val + 0.15, 0]),
        np.array([right_x, y_val + 0.05, 0]),
    ]
    line = VMobject(color=color, stroke_width=3)
    line.set_points_smoothly(pts)
    return line


def _text_block(lines, font=None, color=INK, size=24, buff=0.18):
    """Stack a list of strings into a VGroup."""
    if font is None:
        font = SERIF
    items = [Text(l, font=font, color=color, font_size=size) for l in lines]
    g = VGroup(*items)
    g.arrange(DOWN, aligned_edge=LEFT, buff=buff)
    return g


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    """COLD OPEN title card — the hook question."""
    def construct(self):
        total = DUR["B01"]
        eyebrow = LabelChip("WRITING", accent=TEAL, size=22)
        eyebrow.to_edge(UP, buff=0.65).shift(LEFT * 4.5)
        q1 = Text("Why does addressing", font=DISPLAY, color=INK, font_size=46)
        q2 = Text("the counterargument", font=DISPLAY, color=INK, font_size=46)
        q3 = Text("sometimes make things worse?", font=DISPLAY, color=CRIMSON, font_size=46)
        block = VGroup(q1, q2, q3).arrange(DOWN, buff=0.15).move_to(UP * 0.2)
        sub = Text("the reader who already disagrees",
                   font=SERIF, color=INK, font_size=28, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(
            FadeIn(q1, shift=UP * 0.15),
            run_time=0.7
        )
        self.play(
            FadeIn(q2, shift=UP * 0.15),
            run_time=0.5
        )
        self.play(
            FadeIn(q3, shift=UP * 0.15),
            run_time=0.7
        )
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.0))


class B03_Question(Scene):
    """THE QUESTION — straw-man objection text + reader-attention drop."""
    def construct(self):
        total = DUR["B03"]
        # THE QUESTION label chip top-left
        q_chip = LabelChip("THE QUESTION", accent=SLATE, size=20)
        q_chip.to_corner(UL, buff=0.6)

        # Straw-man panel with the soft objection text
        panel = _panel_box(UP * 0.6, 9.5, 2.6, stroke_color=CRIMSON, stroke_width=2.5)
        chip = LabelChip("STRAW MAN", accent=CRIMSON, size=22)
        chip.next_to(panel, UP, buff=0.18)
        objection_text = Text(
            '"Some might say cheating is bad,\nbut detectors create problems too."',
            font=SERIF, color=INK, font_size=28, slant=ITALIC
        )
        objection_text.move_to(panel.get_center())

        # Reader-attention line below — drops from neutral to zero
        ax_y = -1.5
        ax_left, ax_right = -4.5, 4.5
        ax_line = Line(np.array([ax_left, ax_y, 0]), np.array([ax_right, ax_y, 0]),
                       color=INK, stroke_width=1.2)
        ax_label = SerifLabel("reader attention", CRIMSON, size=20)
        ax_label.next_to(ax_line, LEFT, buff=0.2)
        drop_path = _attention_line(ax_left + 0.3, ax_right - 0.3,
                                    ax_y + 0.6, ax_y - 0.55, color=CRIMSON)
        zero_label = Text("disengages", font=SERIF, color=CRIMSON, font_size=20)
        zero_label.next_to(drop_path.get_end(), DOWN, buff=0.18)

        self.play(FadeIn(q_chip), run_time=0.4)
        self.play(
            FadeIn(panel, scale=0.96),
            FadeIn(chip),
            run_time=0.7
        )
        self.play(FadeIn(objection_text), run_time=0.8)
        self.play(FadeIn(ax_line), FadeIn(ax_label), run_time=0.5)
        self.play(Create(drop_path), run_time=1.0)
        self.play(FadeIn(zero_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.9))


class B04_TwoVersions(Scene):
    """THE PROBLEM — two-panel split: straw man (crimson) vs steel man (teal)."""
    def construct(self):
        total = DUR["B04"]
        # Left panel: straw man
        lp = _panel_box(LEFT * 3.2, 5.6, 4.2, stroke_color=CRIMSON, stroke_width=2.5)
        lchip = LabelChip("STRAW MAN", accent=CRIMSON, size=22)
        lchip.next_to(lp, UP, buff=0.2)
        lstraw = _text_block([
            "Cheating is bad.",
            "But detectors cause problems.",
            "So detectors are wrong.",
        ], size=24, buff=0.22)
        lstraw.move_to(lp.get_center())

        # Right panel: steel man
        rp = _panel_box(RIGHT * 3.2, 5.6, 4.2, stroke_color=TEAL, stroke_width=2.5)
        rchip = LabelChip("STEEL MAN", accent=TEAL, size=22)
        rchip.next_to(rp, UP, buff=0.2)
        rsteel = _text_block([
            "Even imperfect detectors",
            "raise the cost of casual cheating",
            "enough to reduce dishonesty.",
            "Harms to non-native speakers",
            "are a known, accepted cost.",
        ], size=22, buff=0.18)
        rsteel.move_to(rp.get_center())

        label = SerifLabel("the same objection — two versions", INK, size=24)
        label.to_edge(DOWN, buff=0.55)

        self.play(
            FadeIn(lp, shift=RIGHT * 0.4),
            FadeIn(lchip),
            run_time=0.8
        )
        self.play(FadeIn(lstraw), run_time=0.7)
        self.play(
            FadeIn(rp, shift=LEFT * 0.4),
            FadeIn(rchip),
            run_time=0.8
        )
        self.play(FadeIn(rsteel), run_time=0.7)
        self.play(FadeIn(label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.5))


class B05_StrawMan(Scene):
    """THE PROBLEM — straw-man anatomy with reader-attention line declining."""
    def construct(self):
        total = DUR["B05"]
        panel = _panel_box(UP * 0.8, 9.5, 3.4, stroke_color=CRIMSON, stroke_width=2.5)
        chip = LabelChip("STRAW MAN", accent=CRIMSON, size=22)
        chip.next_to(panel, UP, buff=0.2)

        # The soft objection text
        obj = Text(
            '"Some might say cheating is bad, but detectors create problems too."',
            font=SERIF, color=INK, font_size=26, slant=ITALIC
        )
        obj.move_to(panel.get_center() + UP * 0.4)
        # One-sentence dismissal below
        dismiss = Text(
            "Dismissed: detectors are therefore harmful.",
            font=SERIF, color=CRIMSON, font_size=24
        )
        dismiss.next_to(obj, DOWN, buff=0.3)
        # Label
        built_label = SerifLabel("built to knock down", CRIMSON, size=24)
        built_label.next_to(panel, LEFT, buff=0.3)

        # Reader-attention axis
        ax_y = -2.4
        ax_left, ax_right = -4.5, 4.5
        ax_line = Line(np.array([ax_left, ax_y, 0]), np.array([ax_right, ax_y, 0]),
                       color=INK, stroke_width=1.0)
        ax_label = SerifLabel("reader attention", CRIMSON, size=20)
        ax_label.next_to(ax_line, LEFT, buff=0.15)
        drop = _attention_line(ax_left + 0.3, ax_right - 0.3,
                               ax_y + 0.55, ax_y - 0.6, color=CRIMSON)

        self.play(FadeIn(chip), FadeIn(panel, scale=0.97), run_time=0.7)
        self.play(FadeIn(obj), run_time=0.7)
        self.play(FadeIn(dismiss, shift=LEFT * 0.1), run_time=0.6)
        self.play(FadeIn(built_label), run_time=0.5)
        self.play(FadeIn(ax_line), FadeIn(ax_label), run_time=0.4)
        self.play(Create(drop), run_time=1.1)
        self.wait(max(0.5, total - 4.0))


class B06_SteelMan(Scene):
    """THE MECHANISM — steel-man anatomy: the full-strength objection animates in."""
    def construct(self):
        total = DUR["B06"]
        panel = _panel_box(UP * 0.4, 10.5, 4.2, stroke_color=TEAL, stroke_width=2.5)
        chip = LabelChip("STEEL MAN", accent=TEAL, size=22)
        chip.next_to(panel, UP, buff=0.2)

        lines = [
            "Even imperfect detectors raise the cost of casual cheating",
            "enough that they reduce overall academic dishonesty.",
            "The harms to non-native speakers are a known cost",
            "the institution has decided to accept.",
            "The full accounting may favor the policy.",
        ]
        line_mobs = [
            Text(l, font=SERIF, color=INK, font_size=24)
            for l in lines
        ]
        block = VGroup(*line_mobs)
        block.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        block.move_to(panel.get_center())

        cred_label = SerifLabel("what serious critics actually argue", TEAL, size=24)
        cred_label.next_to(panel, DOWN, buff=0.3)

        self.play(FadeIn(chip), FadeIn(panel, scale=0.97), run_time=0.7)
        # Lines animate in one by one
        for mob in line_mobs:
            self.play(FadeIn(mob, shift=UP * 0.08), run_time=0.45)
        self.play(FadeIn(cred_label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 0.7 - len(lines) * 0.45 - 0.6))


class B07_ReaderAttention(Scene):
    """THE MECHANISM — split screen: both reader-attention lines animate simultaneously.
    This is the key animation — the visual argument for the whole film."""
    def construct(self):
        total = DUR["B07"]

        # ---- LEFT PANEL: straw man ----
        lp = _panel_box(LEFT * 3.3 + UP * 0.6, 5.8, 3.2,
                        stroke_color=CRIMSON, stroke_width=2.5)
        lchip = LabelChip("STRAW MAN", accent=CRIMSON, size=20)
        lchip.next_to(lp, UP, buff=0.18)
        lstraw_text = Text(
            '"...but detectors\ncreate problems too."',
            font=SERIF, color=INK, font_size=22, slant=ITALIC
        )
        lstraw_text.move_to(lp.get_center())

        # Left attention axis
        l_ax_y = -1.6
        l_left, l_right = -6.2, -0.6
        l_ax = Line(np.array([l_left, l_ax_y, 0]), np.array([l_right, l_ax_y, 0]),
                    color=INK, stroke_width=1.0)
        l_ax_label = Text("attention", font=SERIF, color=CRIMSON, font_size=18)
        l_ax_label.next_to(l_ax, LEFT, buff=0.1)
        l_drop = _attention_line(l_left + 0.2, l_right - 0.2,
                                 l_ax_y + 0.55, l_ax_y - 0.65, color=CRIMSON)
        l_zero = Text("drops to zero", font=SERIF, color=CRIMSON, font_size=18)
        l_zero.next_to(l_drop.get_end(), DOWN, buff=0.12)

        # ---- RIGHT PANEL: steel man ----
        rp = _panel_box(RIGHT * 3.3 + UP * 0.6, 5.8, 3.2,
                        stroke_color=TEAL, stroke_width=2.5)
        rchip = LabelChip("STEEL MAN", accent=TEAL, size=20)
        rchip.next_to(rp, UP, buff=0.18)
        rsteel_text = Text(
            '"...even imperfect detectors\nraise the cost of casual\ncheating enough..."',
            font=SERIF, color=INK, font_size=22, slant=ITALIC
        )
        rsteel_text.move_to(rp.get_center())

        # Right attention axis
        r_ax_y = -1.6
        r_left, r_right = 0.6, 6.2
        r_ax = Line(np.array([r_left, r_ax_y, 0]), np.array([r_right, r_ax_y, 0]),
                    color=INK, stroke_width=1.0)
        r_ax_label = Text("attention", font=SERIF, color=TEAL, font_size=18)
        r_ax_label.next_to(r_ax, LEFT, buff=0.1)
        r_hold = _attention_line_flat(r_left + 0.2, r_right - 0.2,
                                      r_ax_y + 0.4, color=TEAL)
        r_engaged = Text("stays engaged", font=SERIF, color=TEAL, font_size=18)
        r_engaged.next_to(r_hold.get_end(), DOWN, buff=0.12)

        # Divider
        divider = Line(UP * 3.2, DOWN * 2.6, color=INK, stroke_width=1.5)

        # Build-in
        self.play(
            FadeIn(lp, shift=RIGHT * 0.3),
            FadeIn(lchip),
            FadeIn(rp, shift=LEFT * 0.3),
            FadeIn(rchip),
            FadeIn(divider),
            run_time=0.9
        )
        self.play(
            FadeIn(lstraw_text),
            FadeIn(rsteel_text),
            run_time=0.8
        )
        self.play(
            FadeIn(l_ax), FadeIn(l_ax_label),
            FadeIn(r_ax), FadeIn(r_ax_label),
            run_time=0.5
        )
        # Animate both attention lines simultaneously — the key motion
        self.play(
            Create(l_drop),
            Create(r_hold),
            run_time=1.5
        )
        self.play(
            FadeIn(l_zero, shift=UP * 0.08),
            FadeIn(r_engaged, shift=UP * 0.08),
            run_time=0.6
        )
        self.wait(max(0.5, total - 4.3))


class B08_TwoReaders(Scene):
    """THE IMPLICATION — two reader panels showing who the straw man loses.
    Both panels use INK text on light fills — WCAG W6 safe (no white adrift)."""
    def construct(self):
        total = DUR["B08"]

        # Left panel: reader who already agrees — light SLATE tint, INK text
        lbg = Rectangle(width=5.0, height=3.8)
        lbg.set_fill(SLATE, 0.10).set_stroke(SLATE, 2.0)
        lbg.move_to(LEFT * 3.0 + UP * 0.3)
        lchip = LabelChip("READER: AGREES", accent=SLATE, size=20)
        lchip.move_to(lbg.get_center() + UP * 1.1)
        lstraw_note = Text("straw man:", font=SERIF, color=INK, font_size=22)
        lstraw_note.move_to(lbg.get_center() + UP * 0.15)
        lstraw_result = Text("still convinced", font=SERIF, color=SLATE,
                             font_size=24, weight=BOLD)
        lstraw_result.next_to(lstraw_note, DOWN, buff=0.2)
        lgroup = VGroup(lbg, lchip, lstraw_note, lstraw_result)

        # Right panel: skeptical reader — light CRIMSON tint, INK text
        rbg = Rectangle(width=5.0, height=3.8)
        rbg.set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 2.5)
        rbg.move_to(RIGHT * 3.0 + UP * 0.3)
        rchip = LabelChip("READER: SKEPTIC", accent=CRIMSON, size=20)
        rchip.move_to(rbg.get_center() + UP * 1.1)
        rstraw_note = Text("straw man:", font=SERIF, color=INK, font_size=22)
        rstraw_note.move_to(rbg.get_center() + UP * 0.15)
        rstraw_result = Text("disengages here", font=SERIF, color=CRIMSON,
                             font_size=24, weight=BOLD)
        rstraw_result.next_to(rstraw_note, DOWN, buff=0.2)
        rgroup = VGroup(rbg, rchip, rstraw_note, rstraw_result)

        caption = SerifLabel("the straw man earns only the wrong reader", CRIMSON, size=22)
        caption.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(lgroup, shift=RIGHT * 0.3), run_time=0.8)
        self.play(FadeIn(rgroup, shift=LEFT * 0.3), run_time=0.8)
        self.play(
            rbg.animate.set_stroke(CRIMSON, 3.5),
            run_time=0.6
        )
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.7))


class B09_Example(Scene):
    """THE EXAMPLE — Priya's steel-man objection + evidence-anchored refutation.
    GOLD highlight bar sweeps the specific evidence claim. Labeled illustrative."""
    def construct(self):
        total = DUR["B09"]

        # Top half: steel-man objection (TEAL)
        steel_chip = LabelChip("STEEL MAN", accent=TEAL, size=22)
        steel_chip.move_to(UP * 2.8 + LEFT * 3.8)

        steel_text = Text(
            '"Even imperfect detectors raise the cost\n'
            'of casual cheating enough to reduce\n'
            'overall dishonesty."',
            font=SERIF, color=INK, font_size=20, slant=ITALIC
        )
        steel_text.move_to(UP * 1.85)

        divider = Line(LEFT * 4.8, RIGHT * 4.8, color=INK, stroke_width=1.0)
        divider.move_to(UP * 0.75)

        # Bottom half: refutation with evidence
        refute_chip = LabelChip("REFUTATION", accent=CRIMSON, size=20)
        refute_chip.move_to(UP * 0.35 + LEFT * 2.8)

        refute_text = Text(
            '"The false-positive rate flagged\n'
            '18 percent of multilingual submissions —\n'
            'a harm the benefit cannot absorb."',
            font=SERIF, color=INK, font_size=20, slant=ITALIC
        )
        refute_text.move_to(DOWN * 0.7)

        # GOLD highlight bar behind the specific evidence figure
        highlight = Rectangle(width=3.4, height=0.42)
        highlight.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        # Position over "18 percent" line (approximate)
        highlight.move_to(DOWN * 0.38 + LEFT * 1.1)
        highlight._qc_intentional = True   # the gold sweep is intentional

        # Illustrative label at bottom
        illus = SerifLabel("illustrative example", INK, size=18)
        illus.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(steel_chip), FadeIn(steel_text), run_time=0.8)
        self.play(Create(divider), run_time=0.4)
        self.play(FadeIn(refute_chip), FadeIn(refute_text), run_time=0.8)
        # Gold sweep
        self.play(
            highlight.animate.scale(1.03),
            FadeIn(highlight),
            run_time=0.7
        )
        self.play(FadeIn(illus), run_time=0.4)
        self.wait(max(0.5, total - 3.1))


class B10_Practice(Scene):
    """THE PRACTICE — two-step concrete checklist."""
    def construct(self):
        total = DUR["B10"]

        title = Text("The move", font=DISPLAY, color=INK, font_size=36)
        title.to_edge(UP, buff=0.7)

        # Step 1
        s1_chip = LabelChip("1", accent=TEAL, size=28)
        s1_chip.move_to(LEFT * 5.5 + UP * 0.7)
        s1_text = Text(
            "Write the strongest version of the opposing\n"
            "argument — as if you hold it.",
            font=SERIF, color=INK, font_size=26
        )
        s1_text.next_to(s1_chip, RIGHT, buff=0.4)
        s1_text.align_to(s1_chip, UP)

        # Step 2
        s2_chip = LabelChip("2", accent=TEAL, size=28)
        s2_chip.move_to(LEFT * 5.5 + DOWN * 0.85)
        s2_text = Text(
            "Ask: would the reader who holds this position\n"
            "feel it was taken seriously?",
            font=SERIF, color=INK, font_size=26
        )
        s2_text.next_to(s2_chip, RIGHT, buff=0.4)
        s2_text.align_to(s2_chip, UP)

        # Divider between steps
        step_div = Line(LEFT * 5.8, RIGHT * 5.8, color=INK, stroke_width=0.8)
        step_div.move_to(DOWN * 0.0)

        # Final directive
        directive = SerifLabel("If not — revise.", TEAL, size=28)
        directive.to_edge(DOWN, buff=0.65)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.5)
        self.play(
            FadeIn(s1_chip, scale=0.9),
            FadeIn(s1_text, shift=RIGHT * 0.1),
            run_time=0.8
        )
        self.play(Create(step_div), run_time=0.4)
        self.play(
            FadeIn(s2_chip, scale=0.9),
            FadeIn(s2_text, shift=RIGHT * 0.1),
            run_time=0.8
        )
        self.play(FadeIn(directive, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.1))


class B12_End(Scene):
    """RECAP endcard — question restated, answer in one line. WRITING kicker."""
    def construct(self):
        total = DUR["B12"]
        eyebrow = LabelChip("WRITING", accent=TEAL, size=22)
        eyebrow.to_edge(UP, buff=0.65).shift(LEFT * 4.5)

        line1 = Text("Steel-man earns", font=DISPLAY, color=TEAL,
                     font_size=52, weight=BOLD)
        line2 = Text("the reader who disagrees.", font=DISPLAY, color=INK,
                     font_size=52, weight=BOLD)
        block = VGroup(line1, line2).arrange(DOWN, buff=0.2).move_to(UP * 0.4)

        underline = Line(
            line2.get_corner(DL) + DOWN * 0.18,
            line2.get_corner(DR) + DOWN * 0.18,
            color=TEAL, stroke_width=2.5
        )

        sub = Text("Straw-man earns only the one who already agrees.",
                   font=SERIF, color=INK, font_size=28, slant=ITALIC)
        sub.next_to(underline, DOWN, buff=0.5)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(
            FadeIn(line1, shift=DOWN * 0.1),
            run_time=0.7
        )
        self.play(
            FadeIn(line2, shift=DOWN * 0.1),
            Create(underline),
            run_time=0.8
        )
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))
