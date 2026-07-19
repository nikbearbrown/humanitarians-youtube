import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene
import json, os

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {"B01": 8.0, "B02": 9.0, "B03": 8.0, "B04": 10.0, "B05": 9.0,
           "B06": 11.0, "B07": 10.0, "B08": 11.0, "B09": 10.0, "B10": 14.0, "B11": 8.0}


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why Two Identical Anti-HER2 Drugs", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("Kill Completely Different Tumors", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B02_TwoDrugs(Scene):
    def construct(self):
        total = DUR["B02"]
        # Two drug entity cards with identical antibody label, different outcome chips
        card_l = Rectangle(width=4.8, height=3.2, color=CRIMSON, fill_color=CRIMSON,
                           fill_opacity=0.10, stroke_width=2).move_to(LEFT * 3.0)
        card_r = Rectangle(width=4.8, height=3.2, color=TEAL, fill_color=TEAL,
                           fill_opacity=0.10, stroke_width=2).move_to(RIGHT * 3.0)
        name_l = Text("T-DM1", font=DISPLAY, font_size=22, color=CRIMSON, weight=BOLD).move_to(LEFT * 3.0 + UP * 0.9)
        name_r = Text("T-DXd", font=DISPLAY, font_size=22, color=TEAL, weight=BOLD).move_to(RIGHT * 3.0 + UP * 0.9)
        ab_l = Text("Antibody: trastuzumab", font=MONO, font_size=12, color=INK).move_to(LEFT * 3.0 + UP * 0.1)
        ab_r = Text("Antibody: trastuzumab", font=MONO, font_size=12, color=INK).move_to(RIGHT * 3.0 + UP * 0.1)
        out_l = Text("HER2-low: NOT approved", font=DISPLAY, font_size=13, color=CRIMSON).move_to(LEFT * 3.0 + DOWN * 0.7)
        out_r = Text("HER2-low: approved", font=DISPLAY, font_size=13, color=TEAL).move_to(RIGHT * 3.0 + DOWN * 0.7)
        eq_label = Text("same antibody", font=SERIF, font_size=14, color=INK, slant=ITALIC).move_to(UP * 2.8)
        bracket = Line(LEFT * 5.0 + UP * 2.6, RIGHT * 5.0 + UP * 2.6, color=GOLD, stroke_width=1.5)
        self.play(GrowFromCenter(card_l), GrowFromCenter(card_r), run_time=0.7)
        self.play(Write(name_l), Write(name_r), run_time=0.5)
        self.play(Write(ab_l), Write(ab_r), run_time=0.5)
        self.play(Create(bracket), FadeIn(eq_label, shift=DOWN * 0.15), run_time=0.6)
        self.play(Write(out_l), Write(out_r), run_time=0.5)
        self.wait(max(0.5, total - 3.2))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q_line1 = Text("Two drugs. Same antibody.", font=DISPLAY, font_size=28, color=INK, weight=BOLD)
        q_line2 = Text("One treats HER2-low tumors.", font=DISPLAY, font_size=28, color=TEAL, weight=BOLD)
        q_line3 = Text("The other cannot.", font=DISPLAY, font_size=28, color=CRIMSON, weight=BOLD)
        q_line4 = Text("The antibody is identical.", font=DISPLAY, font_size=22, color=INK)
        q_line5 = Text("Why?", font=DISPLAY, font_size=38, color=INK, weight=BOLD)
        block = VGroup(q_line1, q_line2, q_line3, q_line4, q_line5).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(q_line5.get_corner(DL) + DOWN * 0.1, q_line5.get_corner(DR) + DOWN * 0.1,
                 color=GOLD, stroke_width=2.5)
        self.play(FadeIn(q_line1), run_time=0.5)
        self.play(FadeIn(q_line2), FadeIn(q_line3), run_time=0.6)
        self.play(FadeIn(q_line4), run_time=0.4)
        self.play(FadeIn(q_line5), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 2.5))


class B04_AntibodyOneStep(Scene):
    def construct(self):
        total = DUR["B04"]
        # Show: antibody only controls BINDING. Field of cells, few HER2+.
        title = Text("The antibody controls one step: binding", font=DISPLAY, font_size=19, color=INK)
        title.move_to(UP * 3.1)

        # Draw a simple cell field — circles arranged in a grid
        cells = VGroup()
        import numpy as np
        her2_pos_indices = {2, 7, 14, 19, 25}
        idx = 0
        for row in range(5):
            for col in range(7):
                x = (col - 3) * 1.6
                y = (2 - row) * 1.1
                if idx in her2_pos_indices:
                    c = Circle(radius=0.38).set_fill(TEAL, 0.9).set_stroke(TEAL, 1.5)
                    cell = c.move_to(np.array([x, y, 0]))
                else:
                    c = Circle(radius=0.38).set_fill(INK, 0.18).set_stroke(INK, 1.0)
                    cell = c.move_to(np.array([x, y, 0]))
                cells.add(cell)
                idx += 1

        cells.move_to(DOWN * 0.3)
        note = Text("Most cells: HER2-negative (gray)  |  Few cells: HER2-positive (teal)", font=MONO, font_size=11, color=INK).move_to(DOWN * 2.8)

        self.play(Write(title), run_time=0.5)
        self.play(LaggedStart(*[GrowFromCenter(c) for c in cells], lag_ratio=0.04, run_time=1.8))
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.5, total - 3.0))


class B05_NaiveGuess(Scene):
    def construct(self):
        total = DUR["B05"]
        _quote_scene(self,
                     "Both should underperform equally. Antigen is scarce. Pick whichever is better tolerated.",
                     "— the naive expectation", None, "underperform", total)


class B06_TDM1Confined(Scene):
    def construct(self):
        total = DUR["B06"]
        title = Text("T-DM1: payload stays inside", font=DISPLAY, font_size=19, color=CRIMSON, weight=BOLD)
        title.move_to(UP * 3.1)

        # One large HER2-positive cell
        cell_outer = Circle(radius=1.8).set_fill(TEAL, 0.15).set_stroke(TEAL, 2.0)
        cell_label = Text("HER2-positive cell", font=MONO, font_size=11, color=TEAL)
        cell_label.next_to(cell_outer, UP, buff=0.18)

        # Payload dot inside, crimson, labeled
        payload = Circle(radius=0.22).set_fill(CRIMSON, 1.0).set_stroke(CRIMSON, 0, opacity=0)
        payload.move_to(DOWN * 0.2 + LEFT * 0.3)
        payload_lbl = Text("payload (charged)", font=MONO, font_size=10, color=CRIMSON)
        payload_lbl.next_to(payload, RIGHT, buff=0.15)

        # membrane barrier label
        barrier_lbl = Text("charged: cannot cross membrane", font=SERIF, font_size=13, color=CRIMSON, slant=ITALIC)
        barrier_lbl.move_to(DOWN * 2.5)
        barrier_line = Line(barrier_lbl.get_top() + UP * 0.05,
                            cell_outer.get_bottom() + DOWN * 0.05,
                            color=CRIMSON, stroke_width=1.2)

        # Neighbor cells (gray, untouched)
        neigh_l = Circle(radius=0.7).set_fill(INK, 0.12).set_stroke(INK, 1.0).move_to(LEFT * 3.6)
        neigh_r = Circle(radius=0.7).set_fill(INK, 0.12).set_stroke(INK, 1.0).move_to(RIGHT * 3.6)
        neigh_lbl = Text("neighbors: untouched", font=MONO, font_size=10, color=INK).move_to(DOWN * 0.8 + RIGHT * 3.5)

        group = VGroup(cell_outer, cell_label, payload, payload_lbl)
        group.move_to(UP * 0.3)

        self.play(Write(title), run_time=0.5)
        self.play(GrowFromCenter(cell_outer), run_time=0.7)
        self.play(FadeIn(cell_label), run_time=0.3)
        self.play(GrowFromCenter(payload), run_time=0.5)
        self.play(FadeIn(payload_lbl), run_time=0.3)
        self.play(GrowFromCenter(neigh_l), GrowFromCenter(neigh_r), run_time=0.6)
        self.play(FadeIn(neigh_lbl), run_time=0.3)
        self.play(Create(barrier_line), FadeIn(barrier_lbl), run_time=0.6)
        self.wait(max(0.5, total - 4.0))


class B08_TDXdSpreads(Scene):
    def construct(self):
        total = DUR["B08"]
        title = Text("T-DXd: payload crosses the membrane", font=DISPLAY, font_size=19, color=TEAL, weight=BOLD)
        title.move_to(UP * 3.1)

        # Central HER2+ cell
        cell_outer = Circle(radius=1.4).set_fill(TEAL, 0.15).set_stroke(TEAL, 2.0).move_to(ORIGIN + UP * 0.2)
        cell_label = Text("HER2+ cell", font=MONO, font_size=11, color=TEAL)
        cell_label.next_to(cell_outer, UP, buff=0.14)

        # Payload inside
        payload = Circle(radius=0.18).set_fill(TEAL, 1.0).set_stroke(TEAL, 0, opacity=0).move_to(UP * 0.2)

        # Neighbor cells
        neigh_positions = [LEFT * 3.2 + UP * 0.2, RIGHT * 3.2 + UP * 0.2,
                           LEFT * 2.0 + DOWN * 1.8, RIGHT * 2.0 + DOWN * 1.8]
        neighbors = VGroup(*[Circle(radius=0.6).set_fill(INK, 0.12).set_stroke(INK, 1.0).move_to(p)
                              for p in neigh_positions])
        neg_label = Text("HER2-negative neighbors", font=MONO, font_size=10, color=INK)
        neg_label.move_to(DOWN * 2.9)

        # Spread dots (payload diffusing)
        spread_dots = VGroup(*[Circle(radius=0.10).set_fill(TEAL, 0.85).set_stroke(TEAL, 0, opacity=0).move_to(p)
                                for p in neigh_positions])

        permeable_lbl = Text("membrane-permeable: spreads to neighbors", font=SERIF, font_size=13, color=TEAL, slant=ITALIC)
        permeable_lbl.move_to(DOWN * 2.8)

        self.play(Write(title), run_time=0.5)
        self.play(GrowFromCenter(cell_outer), run_time=0.6)
        self.play(FadeIn(cell_label), run_time=0.3)
        self.play(GrowFromCenter(payload), run_time=0.4)
        self.play(LaggedStart(*[GrowFromCenter(n) for n in neighbors], lag_ratio=0.12, run_time=0.8))
        self.play(FadeIn(neg_label), run_time=0.3)
        # Spread animation
        self.play(LaggedStart(*[GrowFromCenter(d) for d in spread_dots], lag_ratio=0.15, run_time=1.0))
        self.play(FadeIn(permeable_lbl), run_time=0.4)
        self.wait(max(0.5, total - 4.5))


class B09_ImplicationQuote(Scene):
    def construct(self):
        total = DUR["B09"]
        _quote_scene(self,
                     "The antibody finds the cell. Everything else decides whether the drug kills it.",
                     "— Cancer Nanomedicine, Ch. 5", None, "Everything else", total)


class B10_Example(Scene):
    def construct(self):
        total = DUR["B10"]
        title = Text("HER2-low tumor: same entry points, different reach", font=DISPLAY, font_size=19, color=INK)
        title.move_to(UP * 3.1)
        col_l = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        col_r = Rectangle(width=5.5, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)
        lbl_l = Text("T-DM1", font=DISPLAY, font_size=16, color=CRIMSON).move_to(LEFT * 3.2 + UP * 1.55)
        lbl_r = Text("T-DXd", font=DISPLAY, font_size=16, color=TEAL).move_to(RIGHT * 3.2 + UP * 1.55)
        val_l1 = Text("5 HER2+ entry points", font=MONO, font_size=13, color=INK).move_to(LEFT * 3.2 + UP * 0.65)
        val_l2 = Text("payload stays inside", font=MONO, font_size=13, color=INK).move_to(LEFT * 3.2 + DOWN * 0.05)
        val_l3 = Text("5 cells killed", font=MONO, font_size=15, color=CRIMSON).move_to(LEFT * 3.2 + DOWN * 0.75)
        val_r1 = Text("5 HER2+ entry points", font=MONO, font_size=13, color=INK).move_to(RIGHT * 3.2 + UP * 0.65)
        val_r2 = Text("payload crosses membranes", font=MONO, font_size=13, color=INK).move_to(RIGHT * 3.2 + DOWN * 0.05)
        val_r3 = Text("~40 cells killed", font=MONO, font_size=15, color=TEAL).move_to(RIGHT * 3.2 + DOWN * 0.75)
        note_rect = Rectangle(width=9.5, height=0.52, fill_color=SLATE, fill_opacity=0.12,
                              stroke_width=1.5, color=SLATE).move_to(DOWN * 2.55)
        note_txt = Text("HER2-low tumor, 100 cells modeled (illustrative)", font=MONO, font_size=11, color=INK).move_to(DOWN * 2.55)
        self.play(Write(title), run_time=0.5)
        self.play(GrowFromCenter(col_l), GrowFromCenter(col_r), run_time=0.6)
        self.play(Write(lbl_l), Write(lbl_r), run_time=0.5)
        self.play(Write(val_l1), Write(val_r1), run_time=0.4)
        self.play(Write(val_l2), Write(val_r2), run_time=0.4)
        self.play(Write(val_l3), Write(val_r3), run_time=0.4)
        self.play(GrowFromCenter(note_rect), run_time=0.4)
        self.play(Write(note_txt), run_time=0.4)
        self.wait(max(0.5, total - 4.2))


class B11_Endcard(Scene):
    def construct(self):
        total = DUR["B11"]
        topic = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        q_lbl = Text("Q:", font=DISPLAY, font_size=16, color=SLATE)
        q_txt = Text("Same antibody. Different outcomes. Why?", font=SERIF, font_size=22, color=INK, slant=ITALIC)
        q_row = VGroup(q_lbl, q_txt).arrange(RIGHT, buff=0.2)
        a_lbl = Text("A:", font=DISPLAY, font_size=16, color=TEAL)
        a_txt = Text("Membrane permeability. One payload stays put.", font=SERIF, font_size=20, color=INK)
        a_row = VGroup(a_lbl, a_txt).arrange(RIGHT, buff=0.2)
        a2_txt = Text("One spreads. That is the bystander effect.", font=SERIF, font_size=20, color=TEAL)
        qa_block = VGroup(q_row, a_row, a2_txt).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        qa_block.move_to(DOWN * 0.1)
        u = Line(qa_block.get_corner(DL) + DOWN * 0.15,
                 qa_block.get_corner(DR) + DOWN * 0.15,
                 color=GOLD, stroke_width=1.5)
        topic.next_to(qa_block, UP, buff=0.55)
        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(q_row), run_time=0.5)
        self.play(FadeIn(a_row), FadeIn(a2_txt), run_time=0.7)
        self.play(Create(u), run_time=0.4)
        self.wait(max(0.5, total - 2.4))
