import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass


class B01_TitleCard(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        title = Text("Why Measuring Sideways\nErases What You Knew",
                     font=DISPLAY, color=INK, font_size=36, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.0, 0])
        sub = Text("the quantum eraser", font=SERIF, color=INK, font_size=22, slant=ITALIC).move_to([0, -0.8, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 2.3)


class B02_FirstStern(Scene):
    """First Stern-Gerlach: vertical magnet splits beam, down blocked."""
    def construct(self):
        dur = DUR.get("B02", 9.0)
        # Magnet
        magnet = Rectangle(width=1.2, height=3.0, fill_color=INK, fill_opacity=0.3,
                            stroke_color=INK, stroke_width=2.5).move_to([0, 0, 0])
        mag_lbl = SerifLabel("vertical\nmagnet", accent=INK, size=18).move_to([0, -2.3, 0])

        # Incoming beam
        beam_in = Arrow(start=[-5.5, 0, 0], end=[-0.8, 0, 0], color=TEAL, stroke_width=3, buff=0.1)
        beam_lbl = SerifLabel("mixed atoms", accent=INK, size=18).move_to([-4.0, 0.6, 0])

        # Split: up goes TEAL, down goes CRIMSON
        beam_up = Arrow(start=[0.8, 0.3, 0], end=[4.5, 1.5, 0], color=TEAL, stroke_width=3, buff=0.1)
        beam_dn = Arrow(start=[0.8, -0.3, 0], end=[4.5, -1.5, 0], color=CRIMSON, stroke_width=3, buff=0.1)
        up_lbl = LabelChip("spin-up", accent=TEAL, size=18).move_to([4.5, 2.2, 0])
        dn_lbl = LabelChip("spin-down", accent=CRIMSON, size=18).move_to([4.5, -2.2, 0])

        # Block the down beam
        block = Rectangle(width=0.4, height=0.6, fill_color=INK, fill_opacity=0.9,
                          stroke_width=0).move_to([4.8, -1.5, 0])
        block_lbl = SerifLabel("blocked", accent=INK, size=16).move_to([5.8, -1.5, 0])

        self.play(FadeIn(magnet), FadeIn(mag_lbl), run_time=0.4)
        self.play(GrowArrow(beam_in), FadeIn(beam_lbl), run_time=0.5)
        self.play(GrowArrow(beam_up), GrowFromCenter(up_lbl), run_time=0.4)
        self.play(GrowArrow(beam_dn), GrowFromCenter(dn_lbl), run_time=0.4)
        self.play(FadeIn(block), FadeIn(block_lbl), run_time=0.3)
        self.wait(dur - 2.2)


class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 10.0)
        title = Text("Every atom: confirmed spin-up.\nMeasure up-down again — all up.\nNow measure sideways first.\nThen up-down: half come back down. Why?",
                     font=DISPLAY, color=INK, font_size=17, line_spacing=1.3).move_to([0, 0.3, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.8, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_SidewaysMagnet(Scene):
    """Horizontal magnet: spin-up splits 50/50 into spin-left and spin-right."""
    def construct(self):
        dur = DUR.get("B04", 10.0)
        magnet = Rectangle(width=1.2, height=3.0, fill_color=INK, fill_opacity=0.3,
                            stroke_color=INK, stroke_width=2.5).move_to([0, 0, 0])
        mag_lbl = SerifLabel("sideways\nmagnet", accent=INK, size=18).move_to([0, -2.3, 0])

        # Incoming: confirmed spin-up
        beam_in = Arrow(start=[-5.5, 0, 0], end=[-0.8, 0, 0], color=TEAL, stroke_width=3, buff=0.1)
        in_lbl = LabelChip("confirmed spin-up", accent=TEAL, size=18).move_to([-4.0, 0.8, 0])

        # Split: left and right equally (both TEAL since both are valid outcomes)
        beam_up2 = Arrow(start=[0.8, 0.3, 0], end=[4.5, 1.5, 0], color=TEAL, stroke_width=3, buff=0.1)
        beam_dn2 = Arrow(start=[0.8, -0.3, 0], end=[4.5, -1.5, 0], color=TEAL, stroke_width=2.5, buff=0.1)
        lbl_l = LabelChip("spin-left (50%)", accent=TEAL, size=18).move_to([5.2, 2.0, 0])
        lbl_r = LabelChip("spin-right (50%)", accent=TEAL, size=18).move_to([5.2, -2.0, 0])

        surprise_lbl = SerifLabel("completely random!", accent=CRIMSON, size=22).move_to([-2.5, -2.5, 0])

        self.play(FadeIn(magnet), FadeIn(mag_lbl), run_time=0.4)
        self.play(GrowArrow(beam_in), FadeIn(in_lbl), run_time=0.5)
        self.play(GrowArrow(beam_up2), GrowFromCenter(lbl_l), run_time=0.4)
        self.play(GrowArrow(beam_dn2), GrowFromCenter(lbl_r), run_time=0.4)
        self.play(FadeIn(surprise_lbl), run_time=0.4)
        self.wait(dur - 2.3)


class B05_Superposition(Scene):
    """Spin-up = (1/sqrt2)(spin-left + spin-right) — vector decomposition."""
    def construct(self):
        dur = DUR.get("B05", 10.0)
        # Vertical arrow (spin-up)
        up_arrow = Arrow(start=[0, 0, 0], end=[0, 2.5, 0], color=TEAL, stroke_width=4, buff=0)
        up_lbl = LabelChip("|+z>", accent=TEAL, size=22).move_to([0.8, 2.8, 0])

        # Horizontal decomposition
        left_arrow = Arrow(start=[0, 0, 0], end=[-1.8, 0, 0], color=TEAL, stroke_width=2.5, buff=0)
        right_arrow = Arrow(start=[0, 0, 0], end=[1.8, 0, 0], color=TEAL, stroke_width=2.5, buff=0)
        left_lbl = SerifLabel("|+x>", accent=TEAL, size=20).move_to([-2.8, 0, 0])
        right_lbl = SerifLabel("|-x>", accent=TEAL, size=20).move_to([2.8, 0, 0])

        formula = Text("|+z> = (|+x> + |-x>) / sqrt(2)",
                       font=MONO, color=TEAL, font_size=26).move_to([0, -1.8, 0])
        interp = SerifLabel("spin-up is half left, half right", accent=INK, size=20).move_to([0, -2.8, 0])

        self.play(GrowArrow(up_arrow), GrowFromCenter(up_lbl), run_time=0.5)
        self.play(GrowArrow(left_arrow), GrowArrow(right_arrow),
                  FadeIn(left_lbl), FadeIn(right_lbl), run_time=0.6)
        self.play(FadeIn(formula), run_time=0.4)
        self.play(FadeIn(interp), run_time=0.3)
        self.wait(dur - 2.0)


class B06_CollapseErases(Scene):
    """Collapse to spin-left → now spin-up + spin-down superposition."""
    def construct(self):
        dur = DUR.get("B06", 11.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: sideways measurement collapses to spin-left
        left_title = SerifLabel("after sideways collapse", accent=TEAL, size=20).move_to([-3.5, 3.2, 0])
        left_arr = Arrow(start=[-5.5, 0.5, 0], end=[-0.5, 0.5, 0],
                         color=TEAL, stroke_width=4, buff=0)
        left_lbl = LabelChip("|+x>", accent=TEAL, size=22).move_to([-3.5, -0.5, 0])

        # Right: this is a superposition of up and down
        right_title = SerifLabel("which means...", accent=INK, size=20).move_to([3.5, 3.2, 0])
        up_comp = Arrow(start=[0.5, 0.5, 0], end=[0.5, 2.5, 0],
                        color=TEAL, stroke_width=3, buff=0)
        dn_comp = Arrow(start=[0.5, 0.5, 0], end=[0.5, -1.5, 0],
                        color=CRIMSON, stroke_width=3, buff=0)
        up_lbl2 = SerifLabel("|+z>", accent=TEAL, size=18).move_to([1.2, 2.8, 0])
        dn_lbl2 = SerifLabel("|-z>", accent=CRIMSON, size=18).move_to([1.2, -1.8, 0])

        formula = Text("|+x> = (|+z> + |-z>) / sqrt(2)",
                       font=MONO, color=INK, font_size=22).move_to([0, -3.0, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(left_title), GrowArrow(left_arr), GrowFromCenter(left_lbl), run_time=0.6)
        self.play(FadeIn(right_title), run_time=0.3)
        self.play(GrowArrow(up_comp), GrowArrow(dn_comp),
                  FadeIn(up_lbl2), FadeIn(dn_lbl2), run_time=0.6)
        self.play(FadeIn(formula), run_time=0.4)
        self.wait(dur - 2.3)


class B07_ThirdStern(Scene):
    """Third Stern-Gerlach vertical: 50/50 split — information erased."""
    def construct(self):
        dur = DUR.get("B07", 10.0)
        magnet = Rectangle(width=1.2, height=3.0, fill_color=INK, fill_opacity=0.3,
                            stroke_color=INK, stroke_width=2.5).move_to([0, 0, 0])
        mag_lbl = SerifLabel("vertical\nmagnet again", accent=INK, size=18).move_to([0, -2.3, 0])

        # Incoming: spin-left
        beam_in = Arrow(start=[-5.5, 0, 0], end=[-0.8, 0, 0], color=TEAL, stroke_width=3, buff=0.1)
        in_lbl = SerifLabel("spin-left", accent=TEAL, size=18).move_to([-4.0, 0.6, 0])

        # Split 50/50
        beam_up = Arrow(start=[0.8, 0.3, 0], end=[4.5, 1.5, 0], color=TEAL, stroke_width=3, buff=0.1)
        beam_dn = Arrow(start=[0.8, -0.3, 0], end=[4.5, -1.5, 0], color=CRIMSON, stroke_width=3, buff=0.1)
        up_lbl = LabelChip("spin-up (50%)", accent=TEAL, size=18).move_to([5.2, 2.2, 0])
        dn_lbl = LabelChip("spin-down (50%)", accent=CRIMSON, size=18).move_to([5.2, -2.2, 0])

        erase_lbl = SerifLabel("original certainty erased", accent=CRIMSON, size=20).move_to([-2.0, -2.5, 0])

        self.play(FadeIn(magnet), FadeIn(mag_lbl), run_time=0.4)
        self.play(GrowArrow(beam_in), FadeIn(in_lbl), run_time=0.5)
        self.play(GrowArrow(beam_up), GrowFromCenter(up_lbl), run_time=0.4)
        self.play(GrowArrow(beam_dn), GrowFromCenter(dn_lbl), run_time=0.4)
        self.play(FadeIn(erase_lbl), run_time=0.4)
        self.wait(dur - 2.3)


class B08_NonCommute(Scene):
    """Sz and Sx don't commute — different orderings give different results."""
    def construct(self):
        dur = DUR.get("B08", 10.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: measure Sz then Sx
        left_title = SerifLabel("measure Z then X", accent=TEAL, size=20).move_to([-3.5, 3.2, 0])
        seq1a = LabelChip("Sz: definite", accent=TEAL, size=18).move_to([-3.5, 1.5, 0])
        arr1 = Arrow(start=[-3.5, 1.0, 0], end=[-3.5, 0.1, 0], color=INK, stroke_width=2, buff=0.1)
        seq1b = LabelChip("Sx: 50/50", accent=CRIMSON, size=18).move_to([-3.5, -0.5, 0])

        # Right: measure Sx then Sz
        right_title = SerifLabel("measure X then Z", accent=CRIMSON, size=20).move_to([3.5, 3.2, 0])
        seq2a = LabelChip("Sx: definite", accent=TEAL, size=18).move_to([3.5, 1.5, 0])
        arr2 = Arrow(start=[3.5, 1.0, 0], end=[3.5, 0.1, 0], color=INK, stroke_width=2, buff=0.1)
        seq2b = LabelChip("Sz: 50/50", accent=CRIMSON, size=18).move_to([3.5, -0.5, 0])

        note = LabelChip("they do not commute", accent=INK, size=22).move_to([0, -2.5, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(left_title), GrowFromCenter(seq1a), run_time=0.5)
        self.play(GrowArrow(arr1), GrowFromCenter(seq1b), run_time=0.4)
        self.play(FadeIn(right_title), GrowFromCenter(seq2a), run_time=0.5)
        self.play(GrowArrow(arr2), GrowFromCenter(seq2b), run_time=0.4)
        self.play(GrowFromCenter(note), run_time=0.4)
        self.wait(dur - 2.6)


class B09_Example(Scene):
    """Illustrative: 100 atoms → 50 spin-left → 25 up + 25 down."""
    def construct(self):
        dur = DUR.get("B09", 11.0)
        ill_lbl = Text("illustrative", font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([-5.5, 3.3, 0])

        # Flowchart: 100 → 50 → 25+25
        start = LabelChip("100 spin-up atoms", accent=TEAL, size=20).move_to([-4.5, 2.0, 0])
        arr1 = Arrow(start=[-3.0, 2.0, 0], end=[-1.5, 2.0, 0], color=INK, stroke_width=2, buff=0.1)
        step1 = LabelChip("sideways filter", accent=INK, size=18).move_to([0.0, 2.0, 0])
        arr2 = Arrow(start=[1.5, 2.0, 0], end=[3.0, 2.0, 0], color=INK, stroke_width=2, buff=0.1)
        after1 = LabelChip("50 spin-left", accent=TEAL, size=20).move_to([4.5, 2.0, 0])

        arr3 = Arrow(start=[4.5, 1.5, 0], end=[4.5, 0.3, 0], color=INK, stroke_width=2, buff=0.1)
        step2 = LabelChip("vertical magnet", accent=INK, size=18).move_to([4.5, -0.3, 0])
        arr4 = Arrow(start=[3.5, -0.8, 0], end=[1.5, -1.5, 0], color=TEAL, stroke_width=2, buff=0.1)
        arr5 = Arrow(start=[5.5, -0.8, 0], end=[6.3, -1.5, 0], color=CRIMSON, stroke_width=2, buff=0.1)
        up_out = LabelChip("25 spin-up", accent=TEAL, size=20).move_to([1.0, -2.2, 0])
        dn_out = LabelChip("25 spin-down", accent=CRIMSON, size=20).move_to([5.5, -2.2, 0])

        conclusion = SerifLabel("from 100% up to 50/50", accent=CRIMSON, size=20).move_to([0, -3.5, 0])

        self.play(FadeIn(ill_lbl), GrowFromCenter(start), run_time=0.5)
        self.play(GrowArrow(arr1), GrowFromCenter(step1), run_time=0.4)
        self.play(GrowArrow(arr2), GrowFromCenter(after1), run_time=0.4)
        self.play(GrowArrow(arr3), GrowFromCenter(step2), run_time=0.3)
        self.play(GrowArrow(arr4), GrowArrow(arr5), run_time=0.3)
        self.play(GrowFromCenter(up_out), GrowFromCenter(dn_out), run_time=0.4)
        self.play(FadeIn(conclusion), run_time=0.4)
        self.wait(dur - 2.9)


class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        answer = Text("Measurement is not passive.\nIt collapses the state.\nSideways erases what vertical knew.",
                      font=DISPLAY, color=INK, font_size=24, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.8, 0])
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
