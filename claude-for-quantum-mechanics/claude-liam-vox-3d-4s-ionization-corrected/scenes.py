"""vox_scenes.py — Why Filling First Doesn't Mean Leaving Last: The 3d/4s Paradox
(vox-3d-4s-paradox, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL·ai slots.
Color law: TEAL = 4s orbital (fills first in neutral Fe); CRIMSON = 3d orbital (stays in ion).
Exclusions: no Hartree-Fock derivation, no exchange-energy calculation, no full transition survey.
"""
import sys, json, pathlib, numpy as np
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

def _dur(bid, fallback=9.0):
    return DUR.get(bid, fallback)


# ── B01 — Title card ─────────────────────────────────────────────────────────
class B01_TitleCard(Scene):
    def construct(self):
        total = _dur("B01", 10.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        title = Text("Why Filling First Doesn't Mean Leaving Last:", font=DISPLAY,
                     color=INK, font_size=38)
        sub = Text("The 3d/4s Paradox", font=SERIF, color=CRIMSON, font_size=40, slant=ITALIC)
        content = VGroup(title, sub)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=TEAL, stroke_width=2.5)
        rule.next_to(sub, DOWN, buff=0.4)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.8)
        self.play(Create(rule), run_time=0.6)
        self.wait(total - 3.5)


# ── B02 — Cold open: neutral Fe Madelung filling ─────────────────────────────
class B02_NeutralFeFilling(Scene):
    def construct(self):
        total = _dur("B02", 11.0)
        eyebrow = LabelChip("neutral iron", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        header = Text("Observed neutral configuration", font=DISPLAY, color=INK, font_size=30)
        header.move_to(UP * 1.8)

        rule_top = Line(LEFT * 4.5, RIGHT * 4.5, color=SLATE, stroke_width=1.5)
        rule_top.next_to(header, DOWN, buff=0.25)

        # Configuration lines built up step by step
        core = Text("[Ar]  — argon core  (18 electrons)", font=MONO, color=SLATE, font_size=28)
        core.move_to(UP * 0.6)

        d_row = Text("+ 3d⁶  (six 3d electrons)", font=MONO, color=CRIMSON, font_size=28)
        d_row.next_to(core, DOWN, buff=0.3)

        s_row = Text("+ 4s²  (two 4s electrons)", font=MONO, color=TEAL, font_size=28)
        s_row.next_to(d_row, DOWN, buff=0.3)

        config_label = LabelChip("Fe:  [Ar] 3d⁶ 4s²", accent=TEAL, size=26)
        config_label.to_edge(DOWN, buff=0.9)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(header), Create(rule_top), run_time=0.6)
        self.play(FadeIn(core, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(d_row, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(s_row, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(config_label, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.5)


# ── B03 — Cold open: Fe²⁺ ion — 4s leaves first ─────────────────────────────
class B03_IronIonConfig(Scene):
    def construct(self):
        total = _dur("B03", 11.0)
        eyebrow = LabelChip("doubly ionized iron", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Left: neutral Fe
        col_neutral = VGroup(
            LabelChip("Fe  (neutral)", accent=TEAL, size=22),
            Text("[Ar] 3d⁶ 4s²", font=MONO, color=TEAL, font_size=30),
            Text("4s²  present", font=SERIF, color=TEAL, font_size=24, slant=ITALIC),
        )
        col_neutral.arrange(DOWN, buff=0.4)
        col_neutral.move_to(LEFT * 3.0)

        # Right: Fe²⁺
        col_ion = VGroup(
            LabelChip("Fe²⁺  (ion)", accent=CRIMSON, size=22),
            Text("[Ar] 3d⁶", font=MONO, color=CRIMSON, font_size=30),
            Text("4s gone, 3d intact", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC),
        )
        col_ion.arrange(DOWN, buff=0.4)
        col_ion.move_to(RIGHT * 3.0)

        div = Line(UP * 1.5, DOWN * 1.5, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        arrow = Arrow(LEFT * 1.0, RIGHT * 1.0, color=SLATE, stroke_width=2.0, buff=0)
        arrow.move_to(ORIGIN + UP * 2.1)
        arrow_lbl = Text("−2e", font=MONO, color=SLATE, font_size=26)
        arrow_lbl.next_to(arrow, UP, buff=0.1)

        note = Text("both 4s removed — none of the 3d", font=SERIF,
                    color=INK, font_size=26, slant=ITALIC)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(GrowArrow(arrow), FadeIn(arrow_lbl), run_time=0.6)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_neutral[0]), FadeIn(col_ion[0]), run_time=0.5)
        self.play(FadeIn(col_neutral[1]), FadeIn(col_ion[1]), run_time=0.6)
        self.play(FadeIn(col_neutral[2]), FadeIn(col_ion[2]), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 11.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        q1 = Text("Aufbau places 4s before 3d.", font=DISPLAY, color=TEAL, font_size=34)
        q2 = Text("4s leaves first  (easier to remove).", font=DISPLAY, color=CRIMSON, font_size=34)
        q3 = Text("How can the same orbital be both?", font=SERIF,
                  color=INK, font_size=36, slant=ITALIC)
        content = VGroup(q1, q2, q3)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 4.5, RIGHT * 4.5, color=SLATE, stroke_width=2.0)
        rule.next_to(q2, DOWN, buff=0.25)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(q1, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(q2, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(q3, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.0)


# ── B05 — THE PROBLEM: naive fixed-energy model ───────────────────────────────
class B05_NaiveModel(Scene):
    def construct(self):
        total = _dur("B05", 12.0)
        eyebrow = LabelChip("NAIVE READING", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Two energy rungs: 4s at top (lower energy), 3d below
        lbl_4s = Text("4s", font=MONO, color=TEAL, font_size=34)
        lbl_4s.move_to(UP * 0.6 + LEFT * 0.8)
        rung_4s = Line(LEFT * 1.5, RIGHT * 1.5, color=TEAL, stroke_width=3.5)
        rung_4s.move_to(UP * 0.6 + RIGHT * 0.6)
        elbl_4s = Text("lower energy  →  fills first", font=SERIF, color=TEAL,
                       font_size=24, slant=ITALIC)
        elbl_4s.move_to(UP * 0.6 + RIGHT * 3.8)

        lbl_3d = Text("3d", font=MONO, color=CRIMSON, font_size=34)
        lbl_3d.move_to(DOWN * 0.4 + LEFT * 0.8)
        rung_3d = Line(LEFT * 1.5, RIGHT * 1.5, color=CRIMSON, stroke_width=3.5)
        rung_3d.move_to(DOWN * 0.4 + RIGHT * 0.6)
        elbl_3d = Text("higher energy  →  leaves first", font=SERIF, color=CRIMSON,
                       font_size=24, slant=ITALIC)
        elbl_3d.move_to(DOWN * 0.4 + RIGHT * 3.8)

        conclusion = Text("naive prediction: Fe²⁺ = [Ar] 3d⁴ 4s²", font=MONO,
                          color=CRIMSON, font_size=28)
        conclusion.to_edge(DOWN, buff=0.9)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(lbl_4s), Create(rung_4s), FadeIn(elbl_4s), run_time=0.8)
        self.play(FadeIn(lbl_3d), Create(rung_3d), FadeIn(elbl_3d), run_time=0.8)
        self.play(FadeIn(conclusion, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.5)


# ── B06 — MECHANISM: orbital energies depend on occupation ───────────────────
class B06_OccupationDependent(Scene):
    def construct(self):
        total = _dur("B06", 12.0)
        eyebrow = LabelChip("THE MECHANISM", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        heading = Text("Orbital energies are NOT fixed labels.", font=DISPLAY,
                       color=INK, font_size=32)
        heading.move_to(UP * 1.5)

        rule_h = Line(LEFT * 5.0 + UP * 0.9, RIGHT * 5.0 + UP * 0.9,
                      color=SLATE, stroke_width=1.5)

        body1 = Text("Each electron moves in the average field", font=SERIF,
                     color=INK, font_size=28)
        body1.move_to(UP * 0.3)

        body2 = Text("of all the other electrons.", font=SERIF, color=INK, font_size=28)
        body2.move_to(DOWN * 0.3)

        body3 = Text("Change the electron count  →  effective potential shifts", font=SERIF,
                     color=TEAL, font_size=26, slant=ITALIC)
        body3.move_to(DOWN * 0.85)

        body4 = Text("→  orbital energies shift too.", font=DISPLAY, color=TEAL, font_size=28)
        body4.move_to(DOWN * 1.4)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(heading, shift=DOWN * 0.1), run_time=0.8)
        self.play(Create(rule_h), run_time=0.4)
        self.play(FadeIn(body1), run_time=0.6)
        self.play(FadeIn(body2), run_time=0.5)
        self.play(FadeIn(body3), run_time=0.7)
        self.play(FadeIn(body4, shift=DOWN * 0.1), run_time=0.6)
        self.wait(total - 5.5)


# ── B07 — MECHANISM: neutral Fe — 4s lower ────────────────────────────────────
class Legacy07_NeutralOrdering(Scene):
    def construct(self):
        total = _dur("B07", 12.0)
        eyebrow = LabelChip("neutral Fe  (8 outer electrons)", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Energy diagram for neutral Fe
        header = Text("Self-consistent orbital energies in Fe°", font=DISPLAY,
                      color=INK, font_size=28)
        header.move_to(LEFT * 1.5 + UP * 1.4)

        rung_4s = Line(LEFT * 1.8, RIGHT * 1.8, color=TEAL, stroke_width=3.5)
        rung_4s.move_to(LEFT * 1.0 + UP * 0.35)
        lbl_4s = Text("4s  (lower)", font=MONO, color=TEAL, font_size=28)
        lbl_4s.next_to(rung_4s, LEFT, buff=0.3)

        rung_3d = Line(LEFT * 1.8, RIGHT * 1.8, color=CRIMSON, stroke_width=3.5)
        rung_3d.move_to(LEFT * 1.0 + DOWN * 0.45)
        lbl_3d = Text("3d  (higher)", font=MONO, color=CRIMSON, font_size=28)
        lbl_3d.next_to(rung_3d, LEFT, buff=0.3)

        # Vertical axis arrow — far right, clear of header
        v_axis = Arrow(RIGHT * 4.5 + DOWN * 1.2, RIGHT * 4.5 + UP * 1.2,
                       color=SLATE, stroke_width=2.0, buff=0)
        v_lbl = Text("energy", font=SERIF, color=SLATE, font_size=22)
        v_lbl.next_to(v_axis.get_end(), UP, buff=0.1)

        madelung_note = Text("Madelung applies here — neutral atom only.", font=SERIF,
                             color=TEAL, font_size=24, slant=ITALIC)
        madelung_note.to_edge(DOWN, buff=0.9)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(header), run_time=0.6)
        self.play(GrowArrow(v_axis), FadeIn(v_lbl), run_time=0.6)
        self.play(Create(rung_4s), FadeIn(lbl_4s), run_time=0.6)
        self.play(Create(rung_3d), FadeIn(lbl_3d), run_time=0.6)
        self.play(FadeIn(madelung_note, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 5.0)


# ── B08 — MECHANISM: remove 2e — ordering flips ────────────────────────────────
class Legacy08_OrderingFlips(Scene):
    def construct(self):
        total = _dur("B08", 12.0)
        eyebrow = LabelChip("ion:  2 electrons removed", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Left panel: neutral ordering
        neutral_header = LabelChip("Fe°", accent=TEAL, size=22)
        neutral_header.move_to(UP * 1.4 + LEFT * 3.2)

        n_4s = Line(LEFT * 1.0, RIGHT * 1.0, color=TEAL, stroke_width=3.5)
        n_4s.move_to(UP * 0.4 + LEFT * 3.2)
        n_4s_lbl = Text("4s", font=MONO, color=TEAL, font_size=26)
        n_4s_lbl.next_to(n_4s, LEFT, buff=0.2)

        n_3d = Line(LEFT * 1.0, RIGHT * 1.0, color=CRIMSON, stroke_width=3.5)
        n_3d.move_to(DOWN * 0.4 + LEFT * 3.2)
        n_3d_lbl = Text("3d", font=MONO, color=CRIMSON, font_size=26)
        n_3d_lbl.next_to(n_3d, LEFT, buff=0.2)

        # Arrow in the middle
        arrow = Arrow(LEFT * 0.6, RIGHT * 0.6, color=SLATE, stroke_width=2.5, buff=0)
        arrow.move_to(ORIGIN + UP * 0.2)
        arr_lbl = Text("−2e", font=MONO, color=SLATE, font_size=24)
        arr_lbl.next_to(arrow, UP, buff=0.1)

        # Right panel: ion ordering (flipped)
        ion_header = LabelChip("Fe²⁺", accent=CRIMSON, size=22)
        ion_header.move_to(UP * 1.4 + RIGHT * 3.2)

        i_3d = Line(LEFT * 1.0, RIGHT * 1.0, color=CRIMSON, stroke_width=3.5)
        i_3d.move_to(UP * 0.4 + RIGHT * 3.2)
        i_3d_lbl = Text("3d", font=MONO, color=CRIMSON, font_size=26)
        i_3d_lbl.next_to(i_3d, LEFT, buff=0.2)

        i_4s = Line(LEFT * 1.0, RIGHT * 1.0, color=TEAL, stroke_width=3.5)
        i_4s.move_to(DOWN * 0.4 + RIGHT * 3.2)
        i_4s_lbl = Text("4s", font=MONO, color=TEAL, font_size=26)
        i_4s_lbl.next_to(i_4s, LEFT, buff=0.2)

        note = Text("3d sinks below 4s in the ion — ordering has crossed.", font=SERIF,
                    color=INK, font_size=24, slant=ITALIC)
        note.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(neutral_header), FadeIn(ion_header), run_time=0.5)
        self.play(Create(n_4s), FadeIn(n_4s_lbl), Create(n_3d), FadeIn(n_3d_lbl), run_time=0.7)
        self.play(GrowArrow(arrow), FadeIn(arr_lbl), run_time=0.5)
        self.play(Create(i_3d), FadeIn(i_3d_lbl), Create(i_4s), FadeIn(i_4s_lbl), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 5.0)


# ── B09 — Implication: two separate questions ────────────────────────────────
class B09_TwoQuestions(Scene):
    def construct(self):
        total = _dur("B09", 11.0)
        eyebrow = LabelChip("THE IMPLICATION", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_fill = VGroup(
            LabelChip("FILLING ORDER", accent=TEAL, size=22),
            Text("organize configurations", font=SERIF, color=TEAL, font_size=26),
            Text("empirical mnemonic", font=MONO, color=TEAL, font_size=24),
        )
        col_fill.arrange(DOWN, buff=0.38)
        col_fill.move_to(LEFT * 3.0)

        col_rem = VGroup(
            LabelChip("REMOVAL ORDER", accent=CRIMSON, size=22),
            Text("compare total energies", font=SERIF, color=CRIMSON, font_size=26),
            Text("include relaxation", font=MONO, color=CRIMSON, font_size=24),
        )
        col_rem.arrange(DOWN, buff=0.38)
        col_rem.move_to(RIGHT * 3.0)

        div = Line(UP * 1.5, DOWN * 1.5, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        note = Text("Two separate calculations — two different answers.", font=DISPLAY,
                    color=INK, font_size=26)
        note.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_fill[0]), FadeIn(col_rem[0]), run_time=0.6)
        self.play(FadeIn(col_fill[1]), FadeIn(col_rem[1]), run_time=0.6)
        self.play(FadeIn(col_fill[2]), FadeIn(col_rem[2]), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.5)


# ── B10 — THE EXAMPLE ─────────────────────────────────────────────────────────
class B10_Example(Scene):
    def construct(self):
        total = _dur("B10", 13.0)
        eyebrow = LabelChip("EXAMPLE (illustrative)", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_wrong = VGroup(
            LabelChip("student's answer", accent=CRIMSON, size=22),
            Text("Fe²⁺ = [Ar] 3d⁴ 4s²", font=MONO, color=CRIMSON, font_size=28),
            Text("3d removed first", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC),
            Text("(Madelung applied to ion)", font=SERIF, color=CRIMSON,
                 font_size=22, slant=ITALIC),
        )
        col_wrong.arrange(DOWN, buff=0.32)
        col_wrong.move_to(LEFT * 2.8 + DOWN * 0.2)

        col_right = VGroup(
            LabelChip("NIST actual", accent=TEAL, size=22),
            Text("Fe²⁺ = [Ar] 3d⁶", font=MONO, color=TEAL, font_size=28),
            Text("4s removed first", font=SERIF, color=TEAL, font_size=24, slant=ITALIC),
            Text("(many-electron ground state)", font=SERIF, color=TEAL, font_size=22, slant=ITALIC),
        )
        col_right.arrange(DOWN, buff=0.32)
        col_right.move_to(RIGHT * 2.8 + DOWN * 0.2)

        div = Line(UP * 1.4, DOWN * 2.1, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN + DOWN * 0.35)

        rule_top = Line(LEFT * 5.5, RIGHT * 5.5, color=SLATE, stroke_width=1.5)
        rule_top.move_to(UP * 1.55)
        setup = Text("Ionizing iron: which electrons leave?", font=DISPLAY, color=INK, font_size=26)
        setup.move_to(UP * 1.9)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(setup), Create(rule_top), run_time=0.6)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_wrong[0]), FadeIn(col_right[0]), run_time=0.6)
        self.play(FadeIn(col_wrong[1]), FadeIn(col_right[1]), run_time=0.6)
        self.play(FadeIn(col_wrong[2]), FadeIn(col_right[2]), run_time=0.6)
        self.play(FadeIn(col_wrong[3]), FadeIn(col_right[3]), run_time=0.6)
        self.wait(total - 5.0)


# ── B11 — RECAP endcard ──────────────────────────────────────────────────────
class B11_Endcard(Scene):
    def construct(self):
        total = _dur("B11", 10.0)
        kicker = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=24)
        kicker.to_corner(UL, buff=0.6)
        line1 = Text("Aufbau  →  configuration mnemonic.", font=MONO, color=TEAL, font_size=28)
        line1.move_to(UP * 0.9)
        line2 = Text("Ionization  →  total-energy differences.", font=MONO, color=CRIMSON, font_size=26)
        line2.move_to(UP * 0.2)
        line3 = Text("Orbital energies shift with occupation.", font=SERIF,
                     color=INK, font_size=26, slant=ITALIC)
        line3.move_to(DOWN * 0.5)
        line4 = Text("Filling  ≠  removal.", font=DISPLAY, color=INK, font_size=30)
        line4.move_to(DOWN * 1.2)
        sub = Text("Filling is not ionization run backward.", font=SERIF,
                   color=SLATE, font_size=24, slant=ITALIC)
        sub.to_edge(DOWN, buff=0.9)

        end_box = Rectangle(width=0.6, height=0.6).set_fill(SLATE, 0.8).set_stroke(SLATE, 2.0)
        end_box.to_corner(DR, buff=0.6)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(line1, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(line2, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(line3, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(line4, shift=DOWN * 0.1), run_time=0.6)
        self.play(GrowFromCenter(end_box), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.12), run_time=0.6)
        self.wait(total - 4.8)

class B07_Mnemonic(Scene):
    def construct(self):
        total=_dur("B07",12); title=LabelChip("WHAT AUFBAU DOES — AND DOES NOT — SAY",accent=SLATE,size=22); title.to_corner(UL,buff=.6)
        yes=VGroup(Text("DOES",font=DISPLAY,font_size=32,color=TEAL),Text("organizes common",font=MONO,font_size=29,color=TEAL),Text("ground configurations",font=MONO,font_size=29,color=TEAL)).arrange(DOWN,buff=.4).shift(LEFT*3)
        no=VGroup(Text("DOES NOT",font=DISPLAY,font_size=32,color=CRIMSON),Text("freeze 4s and 3d",font=MONO,font_size=29,color=CRIMSON),Text("energies for every ion",font=MONO,font_size=29,color=CRIMSON)).arrange(DOWN,buff=.4).shift(RIGHT*3)
        div=Line(UP*2,DOWN*2,color=INK); self.play(FadeIn(title),Create(div),FadeIn(yes,no),run_time=1.2); self.wait(max(.1,total-1.2))

class B08_TotalEnergies(Scene):
    def construct(self):
        total=_dur("B08",12); title=LabelChip("IONIZATION IS A MANY-ELECTRON ENERGY DIFFERENCE",accent=CRIMSON,size=22); title.to_corner(UL,buff=.6)
        eq=Text("I = E(Fe+) - E(Fe)",font=MONO,font_size=40,color=INK).move_to(UP*1.3)
        factors=VGroup(Text("screening changes",font=MONO,font_size=29,color=TEAL),Text("orbitals relax",font=MONO,font_size=29,color=TEAL),Text("4s is more diffuse",font=MONO,font_size=29,color=CRIMSON)).arrange(RIGHT,buff=.9).move_to(DOWN*.3)
        result=Text("not one frozen orbital-energy lookup",font=SERIF,font_size=30,color=INK).move_to(DOWN*2)
        self.play(FadeIn(title,eq),run_time=.8); self.play(FadeIn(factors,result),run_time=.8); self.wait(max(.1,total-1.6))

class B12_YourTurn(Scene):
    def construct(self):
        total=_dur("B12",12); title=LabelChip("YOUR TURN",accent=SLATE,size=24); title.to_corner(UL,buff=.6)
        start=Text("Fe: [Ar] 3d6 4s2",font=MONO,font_size=39,color=INK).move_to(UP*1.3)
        arrow=Arrow(LEFT,RIGHT,color=CRIMSON); label=Text("remove two 4s electrons",font=MONO,font_size=28,color=CRIMSON).next_to(arrow,UP)
        end=Text("Fe2+: [Ar] 3d6",font=MONO,font_size=40,color=TEAL).move_to(DOWN*1.6)
        self.play(FadeIn(title,start),run_time=.8); self.wait(total*.35); self.play(GrowArrow(arrow),FadeIn(label,end),run_time=.8); self.wait(max(.1,total*.65-1.6))
