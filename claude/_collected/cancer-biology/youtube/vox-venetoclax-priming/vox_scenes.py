from vox_graphics import *
import json, os
_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why a Cancer Cell's Refusal to Die", font=DISPLAY, color=INK, font_size=24, weight=BOLD)
        t2 = Text("Is an Active Defense", font=DISPLAY, color=CRIMSON, font_size=24, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q_line = Text("DNA damage failed.", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        a_line = Text("A non-damaging drug kills.", font=DISPLAY, color=TEAL, font_size=30, weight=BOLD)
        why = Text("Why?", font=DISPLAY, color=INK, font_size=36, weight=BOLD)
        block = VGroup(q_line, a_line, why).arrange(DOWN, buff=0.28).move_to(ORIGIN)
        u = Line(why.get_corner(DL) + DOWN * 0.10, why.get_corner(DR) + DOWN * 0.10,
                 color=GOLD, stroke_width=2)
        self.play(FadeIn(q_line, shift=UP * 0.15), run_time=0.8)
        self.play(FadeIn(a_line, shift=UP * 0.15), run_time=0.8)
        self.play(FadeIn(why), Create(u), run_time=0.9)
        self.wait(max(0.3, total - 2.5))


class B04_NaiveExpectation(Scene):
    def construct(self):
        total = DUR["B04"]
        # Damage box -> Cell box -> Death label, left to right
        dmg_box = Rectangle(width=2.4, height=1.0).set_fill(CRIMSON, 0.85).set_stroke(width=0)
        dmg_lbl = Text("DAMAGE", font=DISPLAY, color=WHITE, font_size=20, weight=BOLD)
        dmg_lbl.move_to(dmg_box)
        dmg = VGroup(dmg_box, dmg_lbl)

        cell_box = Rectangle(width=2.0, height=1.0).set_fill(SLATE, 0.85).set_stroke(width=0)
        cell_lbl = Text("CELL", font=DISPLAY, color=WHITE, font_size=20, weight=BOLD)
        cell_lbl.move_to(cell_box)
        cell = VGroup(cell_box, cell_lbl)

        death_box = Rectangle(width=2.2, height=1.0).set_fill(TEAL, 0.85).set_stroke(width=0)
        death_lbl = Text("DEATH", font=DISPLAY, color=WHITE, font_size=20, weight=BOLD)
        death_lbl.move_to(death_box)
        death = VGroup(death_box, death_lbl)

        row = VGroup(dmg, cell, death).arrange(RIGHT, buff=1.0).move_to(ORIGIN)

        arr1 = Arrow(dmg.get_right(), cell.get_left(), buff=0.1,
                     color=INK, stroke_width=3, max_tip_length_to_length_ratio=0.25)
        arr2 = Arrow(cell.get_right(), death.get_left(), buff=0.1,
                     color=INK, stroke_width=3, max_tip_length_to_length_ratio=0.25)

        caption = Text("The naive model: damage causes death", font=SERIF, color=INK,
                       font_size=22, slant=ITALIC)
        caption.next_to(row, DOWN, buff=0.6)

        self.play(FadeIn(dmg, shift=RIGHT * 0.2), run_time=0.7)
        self.play(GrowArrow(arr1), run_time=0.5)
        self.play(FadeIn(cell, shift=RIGHT * 0.2), run_time=0.6)
        self.play(GrowArrow(arr2), run_time=0.5)
        self.play(FadeIn(death, shift=RIGHT * 0.2), run_time=0.6)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(max(0.3, total - 3.4))


class B05_WallBlocking(Scene):
    def construct(self):
        total = DUR["B05"]
        # Same logic but now a crimson wall blocks death from exiting
        dmg_box = Rectangle(width=2.2, height=1.0).set_fill(CRIMSON, 0.85).set_stroke(width=0)
        dmg_lbl = Text("DAMAGE", font=DISPLAY, color=WHITE, font_size=20, weight=BOLD)
        dmg_lbl.move_to(dmg_box)
        dmg = VGroup(dmg_box, dmg_lbl)

        wall = Rectangle(width=0.5, height=2.2).set_fill(CRIMSON, 1.0).set_stroke(width=0)
        wall_lbl = Text("BCL-2", font=DISPLAY, color=WHITE, font_size=16, weight=BOLD)
        wall_lbl.next_to(wall, UP, buff=0.15)

        death_box = Rectangle(width=2.0, height=1.0).set_fill(SLATE, 0.5).set_stroke(width=0)
        death_lbl = Text("DEATH", font=DISPLAY, color=WHITE, font_size=20, weight=BOLD)
        death_lbl.move_to(death_box)
        death_grp = VGroup(death_box, death_lbl)

        # Arrange: damage ... wall ... death (blocked)
        dmg.move_to(LEFT * 4.0)
        wall.move_to(ORIGIN)
        wall_lbl.next_to(wall, UP, buff=0.15)
        death_grp.move_to(RIGHT * 3.5)

        arr1 = Arrow(dmg.get_right(), wall.get_left(), buff=0.1,
                     color=INK, stroke_width=3, max_tip_length_to_length_ratio=0.25)
        blocked = Text("BLOCKED", font=DISPLAY, color=CRIMSON, font_size=22, weight=BOLD)
        blocked.move_to(RIGHT * 1.9 + DOWN * 0.0)

        caption = Text("BCL-2 overexpression blocks the death signal", font=SERIF,
                       color=INK, font_size=22, slant=ITALIC)
        caption.next_to(VGroup(dmg, wall, death_grp), DOWN, buff=0.65)

        self.play(FadeIn(dmg, shift=RIGHT * 0.2), run_time=0.6)
        self.play(GrowArrow(arr1), run_time=0.5)
        self.play(GrowFromCenter(wall), FadeIn(wall_lbl), run_time=0.8)
        self.play(FadeIn(death_grp), run_time=0.5)
        self.play(FadeIn(blocked, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(max(0.3, total - 3.5))


class B06_MOMPDiagram(Scene):
    def construct(self):
        total = DUR["B06"]
        # Mitochondrion oval; BAX approaches; pore forms; cytochrome c dots exit
        mito = Ellipse(width=3.2, height=2.0).set_fill(SLATE, 0.85).set_stroke(SLATE, 2)
        mito_lbl = Text("mitochondrion", font=SERIF, color=WHITE, font_size=20, slant=ITALIC)
        mito_lbl.move_to(mito)
        mito_grp = VGroup(mito, mito_lbl).move_to(ORIGIN)

        # BAX proteins approaching from left
        bax_dots = VGroup(*[Dot(radius=0.18, color=TEAL) for _ in range(4)])
        bax_dots.arrange(DOWN, buff=0.22).move_to(LEFT * 4.5)
        bax_label = Text("BAX", font=DISPLAY, color=TEAL, font_size=20, weight=BOLD)
        bax_label.next_to(bax_dots, UP, buff=0.15)

        # Pore indicator on mito surface
        pore = Line(mito.get_left() + UP * 0.3, mito.get_left() + DOWN * 0.3,
                    color=TEAL, stroke_width=5)

        # Cytochrome c dots exiting right
        cyt_dots = VGroup(*[Dot(radius=0.14, color=TEAL) for _ in range(5)])
        cyt_dots.arrange(DOWN, buff=0.24).move_to(RIGHT * 4.8)
        cyt_label = Text("cytochrome c", font=SERIF, color=TEAL, font_size=18, slant=ITALIC)
        cyt_label.next_to(cyt_dots, UP, buff=0.15)

        death_chip = LabelChip("DEATH", accent=TEAL, size=22)
        death_chip.move_to(RIGHT * 4.8 + DOWN * 2.0)

        momp_label = Text("MOMP", font=DISPLAY, color=TEAL, font_size=20, weight=BOLD)
        momp_label.next_to(mito_grp, DOWN, buff=0.55)

        self.play(FadeIn(mito_grp), run_time=0.7)
        self.play(FadeIn(bax_dots), FadeIn(bax_label), run_time=0.6)
        self.play(bax_dots.animate.move_to(mito.get_left() + LEFT * 0.2), run_time=1.0)
        self.play(Create(pore), run_time=0.5)
        self.play(FadeIn(momp_label, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(cyt_dots), FadeIn(cyt_label), run_time=0.7)
        self.play(FadeIn(death_chip, shift=UP * 0.15), run_time=0.5)
        self.wait(max(0.3, total - 4.4))


class B08_DamVisual(Scene):
    def construct(self):
        total = DUR["B08"]
        # Dam: crimson wall; teal water on left; gate opens; water floods right

        # Water pressure block (left side)
        water = Rectangle(width=3.5, height=2.8).set_fill(TEAL, 0.75).set_stroke(width=0)
        water.move_to(LEFT * 4.5)
        water_lbl = Text("pro-apoptotic\npressure", font=SERIF, color=WHITE,
                         font_size=20, slant=ITALIC)
        water_lbl.move_to(water)

        # Dam wall
        dam = Rectangle(width=0.55, height=3.4).set_fill(CRIMSON, 1.0).set_stroke(width=0)
        dam.move_to(LEFT * 1.4)
        dam_lbl = Text("BCL-2", font=DISPLAY, color=WHITE, font_size=18, weight=BOLD)
        dam_lbl.move_to(dam)

        # Venetoclax chip above dam
        vx_chip = LabelChip("venetoclax", accent=TEAL, size=20)
        vx_chip.next_to(dam, UP, buff=0.4)

        # Right side (empty, will fill with flood)
        flood = Rectangle(width=5.0, height=2.8).set_fill(TEAL, 0.75).set_stroke(width=0)
        flood.move_to(RIGHT * 3.2)
        flood.scale(0.01)  # start invisible
        momp_chip = LabelChip("MOMP", accent=TEAL, size=22)
        momp_chip.move_to(RIGHT * 3.2)

        self.play(FadeIn(water), FadeIn(water_lbl), run_time=0.8)
        self.play(GrowFromCenter(dam), FadeIn(dam_lbl), run_time=0.7)
        self.play(FadeIn(vx_chip, shift=DOWN * 0.2), run_time=0.6)
        # Gate opens: dam collapses downward
        self.play(dam.animate.scale(0.05), dam_lbl.animate.scale(0.05), run_time=0.8)
        # Water floods right
        self.play(flood.animate.scale(200), run_time=1.0)
        self.play(FadeIn(momp_chip), run_time=0.5)
        self.wait(max(0.3, total - 4.4))


class B09_VenetoclaxDisplacement(Scene):
    def construct(self):
        total = DUR["B09"]
        # BCL-2 oval grips BAX; venetoclax displaces BAX; freed BAX -> mito -> pore

        # BCL-2 with groove
        bcl2 = Ellipse(width=2.2, height=1.4).set_fill(CRIMSON, 0.85).set_stroke(width=0)
        bcl2_lbl = Text("BCL-2", font=DISPLAY, color=WHITE, font_size=18, weight=BOLD)
        bcl2_lbl.move_to(bcl2)
        bcl2_grp = VGroup(bcl2, bcl2_lbl).move_to(LEFT * 3.5)

        # BAX initially gripped (inside groove area)
        bax = Dot(radius=0.28, color=INK)
        bax.move_to(bcl2_grp.get_right() + LEFT * 0.3)
        bax_lbl = Text("BAX", font=DISPLAY, color=INK, font_size=16, weight=BOLD)
        bax_lbl.next_to(bax, UP, buff=0.12)

        # Venetoclax chip
        vx = LabelChip("venetoclax", accent=TEAL, size=18)
        vx.move_to(LEFT * 3.5 + UP * 2.2)

        # Mitochondrion (right side)
        mito = Ellipse(width=2.4, height=1.6).set_fill(SLATE, 0.8).set_stroke(width=0)
        mito_lbl = Text("mito", font=SERIF, color=WHITE, font_size=18, slant=ITALIC)
        mito_lbl.move_to(mito)
        mito_grp = VGroup(mito, mito_lbl).move_to(RIGHT * 2.5)

        pore = Line(mito.get_left() + UP * 0.25, mito.get_left() + DOWN * 0.25,
                    color=TEAL, stroke_width=5)

        cyt_dots = VGroup(*[Dot(radius=0.12, color=TEAL) for _ in range(4)])
        cyt_dots.arrange(RIGHT, buff=0.25).move_to(RIGHT * 5.2)
        cyt_lbl = Text("cytochrome c", font=SERIF, color=TEAL, font_size=16, slant=ITALIC)
        cyt_lbl.next_to(cyt_dots, DOWN, buff=0.12)

        death_chip = LabelChip("DEATH", accent=TEAL, size=20)
        death_chip.move_to(RIGHT * 5.2 + DOWN * 1.4)

        self.play(FadeIn(bcl2_grp), FadeIn(bax), FadeIn(bax_lbl), run_time=0.8)
        self.play(FadeIn(mito_grp), run_time=0.6)
        # Venetoclax arrives
        self.play(vx.animate.move_to(bcl2_grp.get_top() + DOWN * 0.4), run_time=0.8)
        # BAX displaced rightward
        self.play(bax.animate.move_to(RIGHT * 0.5), bax_lbl.animate.move_to(RIGHT * 0.5 + UP * 0.4),
                  run_time=0.7)
        # BAX moves to mitochondrion
        arr = Arrow(RIGHT * 0.7, mito_grp.get_left(), buff=0.1,
                    color=TEAL, stroke_width=3, max_tip_length_to_length_ratio=0.25)
        self.play(GrowArrow(arr), run_time=0.5)
        self.play(bax.animate.move_to(mito.get_left() + LEFT * 0.1), run_time=0.6)
        self.play(Create(pore), run_time=0.4)
        self.play(FadeIn(cyt_dots), FadeIn(cyt_lbl), run_time=0.6)
        self.play(FadeIn(death_chip, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.3, total - 5.4))


class B10_NormalVsCLL(Scene):
    def construct(self):
        total = DUR["B10"]
        # Two-panel comparison: CLL (left) vs Normal B cell (right)

        # --- CLL panel ---
        cll_label = Text("CLL cell", font=DISPLAY, color=CRIMSON, font_size=22, weight=BOLD)
        cll_label.move_to(LEFT * 3.5 + UP * 3.0)

        cll_bcl2 = Rectangle(width=0.45, height=2.8).set_fill(CRIMSON, 1.0).set_stroke(width=0)
        cll_bcl2_lbl = Text("BCL-2", font=DISPLAY, color=WHITE, font_size=14, weight=BOLD)
        cll_bcl2_lbl.move_to(cll_bcl2)
        cll_bcl2_grp = VGroup(cll_bcl2, cll_bcl2_lbl).move_to(LEFT * 3.5)

        # Large teal mass (lots of BAX)
        cll_water = Rectangle(width=2.2, height=2.5).set_fill(TEAL, 0.75).set_stroke(width=0)
        cll_water.next_to(cll_bcl2_grp, LEFT, buff=0.05)
        cll_water_lbl = Text("BAX\npressure", font=SERIF, color=WHITE, font_size=16, slant=ITALIC)
        cll_water_lbl.move_to(cll_water)

        cll_vx = LabelChip("venetoclax", accent=TEAL, size=16)
        cll_vx.next_to(cll_bcl2_grp, UP, buff=0.35)

        cll_death = LabelChip("DEATH", accent=TEAL, size=18)
        cll_death.move_to(LEFT * 3.5 + DOWN * 2.4)

        # --- Normal panel ---
        norm_label = Text("Normal B cell", font=DISPLAY, color=TEAL, font_size=22, weight=BOLD)
        norm_label.move_to(RIGHT * 3.5 + UP * 3.0)

        norm_bcl2 = Rectangle(width=0.35, height=1.0).set_fill(CRIMSON, 0.7).set_stroke(width=0)
        norm_bcl2_lbl = Text("BCL-2", font=DISPLAY, color=WHITE, font_size=12, weight=BOLD)
        norm_bcl2_lbl.move_to(norm_bcl2)
        norm_bcl2_grp = VGroup(norm_bcl2, norm_bcl2_lbl).move_to(RIGHT * 3.5)

        # Tiny water mass (minimal BAX)
        norm_water = Rectangle(width=0.7, height=0.9).set_fill(TEAL, 0.4).set_stroke(width=0)
        norm_water.next_to(norm_bcl2_grp, LEFT, buff=0.05)

        norm_vx = LabelChip("venetoclax", accent=TEAL, size=16)
        norm_vx.next_to(norm_bcl2_grp, UP, buff=0.35)

        norm_survives = LabelChip("SURVIVES", accent=SLATE, size=18)
        norm_survives.move_to(RIGHT * 3.5 + DOWN * 2.4)

        # Divider
        divider = Line(UP * 3.5, DOWN * 3.5, color=INK, stroke_width=1.0)
        divider.move_to(ORIGIN)

        self.play(FadeIn(cll_label), FadeIn(norm_label), Create(divider), run_time=0.7)
        self.play(FadeIn(cll_water), FadeIn(cll_water_lbl), FadeIn(norm_water), run_time=0.8)
        self.play(GrowFromCenter(cll_bcl2_grp), GrowFromCenter(norm_bcl2_grp), run_time=0.7)
        self.play(FadeIn(cll_vx, shift=DOWN * 0.2), FadeIn(norm_vx, shift=DOWN * 0.2), run_time=0.6)
        # CLL dam collapses, flood and death
        self.play(cll_bcl2_grp.animate.scale(0.1), run_time=0.6)
        self.play(FadeIn(cll_death, shift=UP * 0.15), run_time=0.5)
        # Normal: block but nothing floods
        self.play(norm_bcl2_grp.animate.set_fill(SLATE, 0.5), run_time=0.5)
        self.play(FadeIn(norm_survives, shift=UP * 0.15), run_time=0.5)
        self.wait(max(0.3, total - 4.9))


class B11_BH3Profiling(Scene):
    def construct(self):
        total = DUR["B11"]
        # Table: rows = CLL / Normal; cols = BIM response / venetoclax fate
        title = Text("BH3 Profiling  [illustrative]", font=DISPLAY, color=INK,
                     font_size=22, weight=BOLD)
        title.move_to(UP * 3.2)

        # Header row
        h_cell = Text("Cell type", font=DISPLAY, color=INK, font_size=18, weight=BOLD)
        h_bim = Text("BIM peptide", font=DISPLAY, color=INK, font_size=18, weight=BOLD)
        h_vx = Text("Venetoclax 40 nM", font=DISPLAY, color=INK, font_size=18, weight=BOLD)

        h_row = VGroup(h_cell, h_bim, h_vx).arrange(RIGHT, buff=1.2)
        h_row.move_to(UP * 2.2)

        # CLL row
        r1_cell = Text("CLL biopsy", font=SERIF, color=CRIMSON, font_size=20, weight=BOLD)
        r1_bim = Text("cytochrome c\nwithin seconds", font=SERIF, color=TEAL, font_size=18)
        r1_vx = Text("dead in 2h", font=SERIF, color=TEAL, font_size=20, weight=BOLD)

        r1 = VGroup(r1_cell, r1_bim, r1_vx).arrange(RIGHT, buff=1.2)
        r1.move_to(UP * 0.5)

        # Normal row
        r2_cell = Text("Normal B cell", font=SERIF, color=INK, font_size=20)
        r2_bim = Text("minimal\ncytochrome c", font=SERIF, color=CRIMSON, font_size=18)
        r2_vx = Text("survives", font=SERIF, color=INK, font_size=20)

        r2 = VGroup(r2_cell, r2_bim, r2_vx).arrange(RIGHT, buff=1.2)
        r2.move_to(DOWN * 1.4)

        # Rule lines
        header_rule = Line(h_row.get_corner(DL) + DOWN * 0.15,
                           h_row.get_corner(DR) + DOWN * 0.15,
                           stroke_width=1.5, color=INK)
        mid_rule = Line(r1.get_corner(DL) + DOWN * 0.2,
                        r1.get_corner(DR) + DOWN * 0.2,
                        stroke_width=0.8, color=SLATE)

        # Align columns
        for group in [h_row, r1, r2]:
            group[0].align_to(h_row[0], LEFT)
            group[1].align_to(h_row[1], LEFT)
            group[2].align_to(h_row[2], LEFT)

        illus_note = Text("Numbers illustrative — experiment confirmed in literature",
                          font=SERIF, color=SLATE, font_size=16, slant=ITALIC)
        illus_note.move_to(DOWN * 3.0)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(h_row), Create(header_rule), run_time=0.7)
        self.play(FadeIn(r1_cell), run_time=0.4)
        self.play(FadeIn(r1_bim, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(r1_vx, shift=UP * 0.1), run_time=0.5)
        self.play(Create(mid_rule), run_time=0.4)
        self.play(FadeIn(r2_cell), run_time=0.4)
        self.play(FadeIn(r2_bim, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(r2_vx, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(illus_note), run_time=0.5)
        self.wait(max(0.3, total - 5.0))


class B12_Recap(Scene):
    def construct(self):
        total = DUR["B12"]
        topic = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        main = Text("The cells were already dying.", font=DISPLAY, color=INK,
                    font_size=26, weight=BOLD)
        sub = Text("BCL-2 was the only lock.", font=DISPLAY, color=CRIMSON,
                   font_size=26, weight=BOLD)
        block = VGroup(main, sub).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(sub.get_corner(DL) + DOWN * 0.12, sub.get_corner(DR) + DOWN * 0.12,
                 color=GOLD, stroke_width=2)
        topic.next_to(block, UP, buff=0.55)
        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.1)
        self.wait(max(0.3, total - 1.6))
