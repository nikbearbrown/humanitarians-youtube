import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import json, os
_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ── B01  Title card ────────────────────────────────────────────────────────────
class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text('Why "Alpha Radiation Is Stronger"', font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("Is the Wrong Reason to Pick It", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ── B02  Alpha introduction ────────────────────────────────────────────────────
class B02_AlphaIntro(Scene):
    def construct(self):
        total = DUR["B02"]
        # The bound cell
        cell = Circle(0.4).set_fill(SLATE, 0.85).set_stroke(INK, 1.5)
        cell.move_to(LEFT * 3.0 + UP * 0.2)
        # Short dense alpha track
        track = Line(cell.get_right(), cell.get_right() + RIGHT * 0.6,
                     color=CRIMSON, stroke_width=7)
        # Labels
        lbl_top = Text("Alpha particle", font=DISPLAY, color=CRIMSON, font_size=22, weight=BOLD)
        lbl_top.move_to(LEFT * 3.0 + UP * 1.4)
        lbl_range = Text("range: 0.05 - 0.1 mm", font=MONO, font_size=16, color=CRIMSON)
        lbl_range.move_to(LEFT * 3.0 + DOWN * 1.1)
        lbl_let = Text("High LET  |  dense damage", font=DISPLAY, font_size=16, color=INK)
        lbl_let.move_to(LEFT * 3.0 + DOWN * 1.55)
        # Bound marker on cell
        bound_dot = Dot(radius=0.1, color=CRIMSON).move_to(cell.get_center())
        self.play(GrowFromCenter(cell), run_time=0.5)
        self.play(GrowFromCenter(bound_dot), run_time=0.3)
        self.play(Create(track), run_time=0.6)
        self.play(FadeIn(lbl_top), run_time=0.4)
        self.play(FadeIn(lbl_range), FadeIn(lbl_let), run_time=0.5)
        self.wait(max(0.3, total - 2.3))


# ── B03  Beta introduction ─────────────────────────────────────────────────────
class B03_BetaIntro(Scene):
    def construct(self):
        total = DUR["B03"]
        # The bound cell
        cell = Circle(0.4).set_fill(SLATE, 0.85).set_stroke(INK, 1.5)
        cell.move_to(LEFT * 3.5 + UP * 0.2)
        # Long sparse beta track
        track = Line(cell.get_right(), cell.get_right() + RIGHT * 3.0,
                     color=TEAL, stroke_width=2.5)
        # Neighbor cells hit by the track
        nb1 = Circle(0.3).set_fill(TEAL, 0.18).set_stroke(TEAL, 1.0)
        nb1.move_to(LEFT * 1.5 + UP * 0.2)
        nb2 = Circle(0.3).set_fill(TEAL, 0.12).set_stroke(TEAL, 0.7)
        nb2.move_to(LEFT * 0.2 + UP * 0.2)
        # Labels
        lbl_top = Text("Beta particle", font=DISPLAY, color=TEAL, font_size=22, weight=BOLD)
        lbl_top.move_to(LEFT * 1.5 + UP * 1.4)
        lbl_range = Text("range: 1 - 2 mm", font=MONO, font_size=16, color=TEAL)
        lbl_range.move_to(LEFT * 1.5 + DOWN * 1.1)
        lbl_let = Text("Low LET  |  sparse damage", font=DISPLAY, font_size=16, color=INK)
        lbl_let.move_to(LEFT * 1.5 + DOWN * 1.55)
        # Bound marker
        bound_dot = Dot(radius=0.1, color=TEAL).move_to(cell.get_center())
        self.play(GrowFromCenter(cell), run_time=0.5)
        self.play(GrowFromCenter(bound_dot), run_time=0.3)
        self.play(Create(track), run_time=0.8)
        self.play(GrowFromCenter(nb1), GrowFromCenter(nb2), run_time=0.5)
        self.play(FadeIn(lbl_top), run_time=0.4)
        self.play(FadeIn(lbl_range), FadeIn(lbl_let), run_time=0.5)
        self.wait(max(0.3, total - 3.0))


# ── B04  The Question card ────────────────────────────────────────────────────
class B04_Question(Scene):
    def construct(self):
        total = DUR["B04"]
        q1 = Text("Alpha delivers far more lethal energy", font=SERIF, color=INK,
                  font_size=26, slant=ITALIC)
        q2 = Text("per hit than beta.", font=SERIF, color=INK, font_size=26, slant=ITALIC)
        q3 = Text("For many cancers, oncologists pick the", font=SERIF, color=INK, font_size=26, slant=ITALIC)
        q4 = Text('"weaker" beta emitter anyway.', font=SERIF, color=CRIMSON, font_size=26,
                  weight=BOLD, slant=ITALIC)
        q5 = Text("Why would less lethal radiation be the better choice?", font=DISPLAY,
                  color=INK, font_size=22, weight=BOLD)
        block = VGroup(q1, q2, q3, q4, q5).arrange(DOWN, buff=0.22).move_to(UP * 0.2)
        gold_bar = Rectangle(
            width=q5.width + 0.4, height=q5.height + 0.18
        ).set_fill(GOLD, 0.35).set_stroke(width=0, opacity=0)
        gold_bar.move_to(q5)
        self.play(FadeIn(VGroup(q1, q2, q3, q4)), run_time=1.0)
        self.play(FadeIn(gold_bar), FadeIn(q5), run_time=0.8)
        self.wait(max(0.3, total - 1.8))


# ── B05  Emitter range split panel ───────────────────────────────────────────
class B05_EmitterRanges(Scene):
    def construct(self):
        total = DUR["B05"]
        title = Text("Emitter range determines crossfire", font=DISPLAY,
                     font_size=20, color=INK).move_to(UP * 3.2)

        # ---- Alpha panel (LEFT) ----
        alpha_cell = Circle(0.38).set_fill(SLATE, 0.85).set_stroke(INK, 1.5)
        alpha_cell.move_to(LEFT * 3.8 + UP * 0.4)
        alpha_bound = Dot(radius=0.09, color=CRIMSON).move_to(alpha_cell.get_center())
        # Short dense track
        alpha_track = Line(alpha_cell.get_right(),
                           alpha_cell.get_right() + RIGHT * 0.55,
                           color=CRIMSON, stroke_width=6)
        # Dashed range boundary
        alpha_dash = DashedLine(
            alpha_cell.get_right() + RIGHT * 0.55 + UP * 0.5,
            alpha_cell.get_right() + RIGHT * 0.55 + DOWN * 0.5,
            color=CRIMSON, stroke_width=1.5, dash_length=0.08
        )
        alpha_lbl = Text("Alpha", font=DISPLAY, font_size=18, color=CRIMSON, weight=BOLD)
        alpha_lbl.move_to(LEFT * 3.8 + DOWN * 1.0)
        alpha_range = Text("0.05 - 0.1 mm", font=MONO, font_size=13, color=CRIMSON)
        alpha_range.move_to(LEFT * 3.8 + DOWN * 1.45)
        # Neighbor cells — faded, unreached
        alpha_nb = Circle(0.3).set_fill(SLATE, 0.15).set_stroke(SLATE, 0.5)
        alpha_nb.move_to(LEFT * 2.5 + UP * 0.4)

        # ---- Beta panel (RIGHT) ----
        beta_cell = Circle(0.38).set_fill(SLATE, 0.85).set_stroke(INK, 1.5)
        beta_cell.move_to(RIGHT * 1.2 + UP * 0.4)
        beta_bound = Dot(radius=0.09, color=TEAL).move_to(beta_cell.get_center())
        # Long sparse track
        beta_track = Line(beta_cell.get_right(),
                          beta_cell.get_right() + RIGHT * 2.6,
                          color=TEAL, stroke_width=2.5)
        # Range boundary
        beta_dash = DashedLine(
            beta_cell.get_right() + RIGHT * 2.6 + UP * 0.5,
            beta_cell.get_right() + RIGHT * 2.6 + DOWN * 0.5,
            color=TEAL, stroke_width=1.5, dash_length=0.08
        )
        # Neighbor cells reached by beta
        beta_nb1 = Circle(0.32).set_fill(TEAL, 0.20).set_stroke(TEAL, 1.2)
        beta_nb1.move_to(RIGHT * 2.6 + UP * 0.4)
        beta_nb2 = Circle(0.32).set_fill(TEAL, 0.13).set_stroke(TEAL, 0.8)
        beta_nb2.move_to(RIGHT * 3.5 + UP * 0.4)
        beta_lbl = Text("Beta", font=DISPLAY, font_size=18, color=TEAL, weight=BOLD)
        beta_lbl.move_to(RIGHT * 2.5 + DOWN * 1.0)
        beta_range = Text("1 - 2 mm", font=MONO, font_size=13, color=TEAL)
        beta_range.move_to(RIGHT * 2.5 + DOWN * 1.45)

        # ---- divider line ----
        divider = Line(UP * 3.0, DOWN * 2.5, color=INK, stroke_width=0.8)
        divider.move_to(LEFT * 0.5 + UP * 0.25)

        # ---- GOLD highlight bar behind title ----
        gold_bar = Rectangle(width=title.width + 0.4, height=title.height + 0.16)
        gold_bar.set_fill(GOLD, 0.3).set_stroke(width=0, opacity=0).move_to(title)

        self.play(Write(title), FadeIn(gold_bar), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(GrowFromCenter(alpha_cell), GrowFromCenter(beta_cell), run_time=0.6)
        self.play(GrowFromCenter(alpha_bound), GrowFromCenter(beta_bound), run_time=0.3)
        self.play(Create(alpha_track), Create(beta_track), run_time=0.7)
        self.play(Create(alpha_dash), Create(beta_dash), run_time=0.4)
        self.play(GrowFromCenter(alpha_nb), run_time=0.4)
        self.play(GrowFromCenter(beta_nb1), GrowFromCenter(beta_nb2), run_time=0.5)
        self.play(FadeIn(alpha_lbl), FadeIn(beta_lbl), run_time=0.4)
        self.play(FadeIn(alpha_range), FadeIn(beta_range), run_time=0.4)
        self.wait(max(0.3, total - 4.5))


# ── B06  Crossfire mechanism ──────────────────────────────────────────────────
class B06_Crossfire(Scene):
    def construct(self):
        total = DUR["B06"]
        # A row of cells: alternating bound (SLATE+dot) and unbound
        n_cells = 5
        cells = VGroup()
        bound_dots = VGroup()
        cell_positions = [LEFT * 4.0 + UP * 0.5 + RIGHT * i * 1.5 for i in range(n_cells)]
        for i, pos in enumerate(cell_positions):
            c = Circle(0.38).set_fill(SLATE, 0.80).set_stroke(INK, 1.5)
            c.move_to(pos)
            cells.add(c)
            if i == 0 or i == 2:  # bound cells
                d = Dot(radius=0.09, color=TEAL).move_to(pos)
                bound_dots.add(d)

        # Beta tracks from bound cells into neighbors
        track_0 = Line(cell_positions[0] + RIGHT * 0.38,
                       cell_positions[3] + LEFT * 0.38,
                       color=TEAL, stroke_width=2.5)
        track_2 = Line(cell_positions[2] + RIGHT * 0.38,
                       cell_positions[4] + RIGHT * 0.1,
                       color=TEAL, stroke_width=2.5)

        # Irradiation glow on neighbors
        glow_1 = Circle(0.38).set_fill(TEAL, 0.22).set_stroke(TEAL, 1.0)
        glow_1.move_to(cell_positions[1])
        glow_3 = Circle(0.38).set_fill(TEAL, 0.22).set_stroke(TEAL, 1.0)
        glow_3.move_to(cell_positions[3])
        glow_4 = Circle(0.38).set_fill(TEAL, 0.15).set_stroke(TEAL, 0.8)
        glow_4.move_to(cell_positions[4])

        # Labels
        bound_lbl = SerifLabel("receptor-positive (bound)", accent=TEAL, size=16)
        bound_lbl.next_to(cells, DOWN, buff=0.9)
        bound_lbl.shift(LEFT * 1.5)
        cf_lbl = Text("crossfire", font=DISPLAY, font_size=24, color=TEAL, weight=BOLD)
        cf_lbl.move_to(UP * 2.4)
        sub_lbl = Text("beta radiation irradiates neighbors that never bound the drug",
                       font=DISPLAY, font_size=14, color=INK)
        sub_lbl.next_to(cf_lbl, DOWN, buff=0.18)

        self.play(AnimationGroup(*[GrowFromCenter(c) for c in cells],
                                 lag_ratio=0.08), run_time=0.8)
        self.play(AnimationGroup(*[GrowFromCenter(d) for d in bound_dots],
                                 lag_ratio=0.1), run_time=0.4)
        self.play(Create(track_0), Create(track_2), run_time=0.8)
        self.play(GrowFromCenter(glow_1), GrowFromCenter(glow_3),
                  GrowFromCenter(glow_4), run_time=0.6)
        self.play(Write(cf_lbl), run_time=0.4)
        self.play(FadeIn(sub_lbl), run_time=0.4)
        self.wait(max(0.3, total - 3.4))


# ── B08  Alpha fails on heterogeneous tumor ───────────────────────────────────
class B08_AlphaFail(Scene):
    def construct(self):
        total = DUR["B08"]
        # Tumor cross section — simplified as rings
        outer_ring = Annulus(inner_radius=1.2, outer_radius=2.0,
                             color=SLATE, fill_opacity=0.6, stroke_width=0)
        outer_ring.move_to(UP * 0.3)
        inner_core = Circle(1.2).set_fill(SLATE, 0.25).set_stroke(SLATE, 1.0)
        inner_core.move_to(UP * 0.3)

        # Short alpha tracks on rim only
        import numpy as np
        rim_tracks = VGroup()
        for angle_deg in [0, 45, 90, 135, 180, 225, 270, 315]:
            a = np.radians(angle_deg)
            rim_pos = outer_ring.get_center() + np.array([np.cos(a) * 1.6,
                                                           np.sin(a) * 1.6, 0])
            track_end = rim_pos + np.array([np.cos(a) * 0.35, np.sin(a) * 0.35, 0])
            t = Line(rim_pos, track_end, color=CRIMSON, stroke_width=5)
            rim_tracks.add(t)

        # Dashed reach boundary
        reach_circle = Circle(1.2 + 0.4).set_stroke(CRIMSON, 1.5)
        reach_circle.move_to(UP * 0.3)

        # Labels
        rim_lbl = LabelChip("Rim: bound", accent=CRIMSON, size=15)
        rim_lbl.move_to(RIGHT * 3.5 + UP * 1.2)
        core_lbl = LabelChip("Core: no drug", accent=SLATE, size=15)
        core_lbl.move_to(RIGHT * 3.5 + UP * 0.4)
        fail_lbl = Text("core survives", font=DISPLAY, font_size=18, color=CRIMSON, weight=BOLD)
        fail_lbl.move_to(UP * 0.3)
        title_lbl = Text("Alpha: confined track cannot reach the core",
                         font=DISPLAY, font_size=18, color=CRIMSON)
        title_lbl.move_to(UP * 3.0)

        self.play(GrowFromCenter(outer_ring), GrowFromCenter(inner_core), run_time=0.7)
        self.play(FadeIn(title_lbl), run_time=0.4)
        self.play(AnimationGroup(*[Create(t) for t in rim_tracks], lag_ratio=0.05),
                  run_time=0.8)
        self.play(Create(reach_circle), run_time=0.5)
        self.play(FadeIn(rim_lbl), FadeIn(core_lbl), run_time=0.4)
        self.play(FadeIn(fail_lbl), run_time=0.5)
        self.wait(max(0.3, total - 3.3))


# ── B09  Beta wins on heterogeneous tumor ─────────────────────────────────────
class B09_BetaWin(Scene):
    def construct(self):
        total = DUR["B09"]
        # Same tumor cross section
        outer_ring = Annulus(inner_radius=1.2, outer_radius=2.0,
                             color=SLATE, fill_opacity=0.6, stroke_width=0)
        outer_ring.move_to(UP * 0.3)
        inner_core = Circle(1.2).set_fill(SLATE, 0.25).set_stroke(SLATE, 1.0)
        inner_core.move_to(UP * 0.3)

        # Long beta tracks from rim going inward
        import numpy as np
        beta_tracks = VGroup()
        for angle_deg in [30, 90, 150, 210, 270, 330]:
            a = np.radians(angle_deg)
            # Start at rim
            rim_pos = outer_ring.get_center() + np.array([np.cos(a) * 1.6,
                                                           np.sin(a) * 1.6, 0])
            # End past the core center — 1.8 units inward toward center
            inward_dir = -np.array([np.cos(a), np.sin(a), 0])
            track_end = rim_pos + inward_dir * 1.9
            t = Line(rim_pos, track_end, color=TEAL, stroke_width=2.5)
            beta_tracks.add(t)

        # Core irradiation glow
        core_glow = Circle(1.2).set_fill(TEAL, 0.28).set_stroke(TEAL, 1.5)
        core_glow.move_to(UP * 0.3)

        # Labels
        cf_title = Text("Beta crossfire reaches the core", font=DISPLAY,
                        font_size=18, color=TEAL, weight=BOLD)
        cf_title.move_to(UP * 3.0)
        win_lbl = Text("core irradiated", font=DISPLAY, font_size=18, color=TEAL, weight=BOLD)
        win_lbl.move_to(UP * 0.3)

        self.play(GrowFromCenter(outer_ring), GrowFromCenter(inner_core), run_time=0.7)
        self.play(FadeIn(cf_title), run_time=0.4)
        self.play(AnimationGroup(*[Create(t) for t in beta_tracks], lag_ratio=0.06),
                  run_time=1.0)
        self.play(GrowFromCenter(core_glow), run_time=0.6)
        self.play(FadeIn(win_lbl), run_time=0.4)
        self.wait(max(0.3, total - 3.1))


# ── B10  Implication card ─────────────────────────────────────────────────────
class B10_Implication(Scene):
    def construct(self):
        total = DUR["B10"]
        t1 = Text("The question is not which emitter hits harder.",
                  font=SERIF, color=INK, font_size=28, slant=ITALIC)
        t2 = Text("It is which range matches the tumor's geometry.",
                  font=SERIF, color=TEAL, font_size=28, slant=ITALIC, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.3).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.1, t2.get_corner(DR) + DOWN * 0.1,
                 color=GOLD, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.3, total - 1.7))


# ── B11  Worked example — Lu-177 vs Ac-225 ───────────────────────────────────
class B11_Example(Scene):
    def construct(self):
        total = DUR["B11"]
        # Header
        header = Text("Heterogeneous neuroendocrine tumor  |  illustrative numbers",
                      font=DISPLAY, font_size=14, color=INK)
        header.move_to(UP * 3.1)

        # ---- Lu-177 panel (LEFT) ----
        lu_card = Rectangle(width=3.4, height=3.2)
        lu_card.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        lu_card.move_to(LEFT * 2.7 + UP * 0.2)
        lu_title = Text("Lu-177", font=DISPLAY, color=WHITE, font_size=22, weight=BOLD)
        lu_title.move_to(lu_card.get_top() + DOWN * 0.45)
        lu_sub = Text("beta emitter", font=DISPLAY, color=WHITE, font_size=14)
        lu_sub.next_to(lu_title, DOWN, buff=0.12)
        lu_num = Text("78%", font=MONO, color=TEAL, font_size=52, weight=BOLD)
        lu_num.move_to(lu_card.get_center() + UP * 0.15)
        lu_stat = Text("tumor cell kill", font=DISPLAY, color=WHITE, font_size=13)
        lu_stat.next_to(lu_num, DOWN, buff=0.12)
        lu_why = Text("crossfire reaches core", font=DISPLAY, color=TEAL, font_size=12)
        lu_why.move_to(lu_card.get_bottom() + UP * 0.45)
        lu_group = VGroup(lu_card, lu_title, lu_sub, lu_num, lu_stat, lu_why)

        # ---- Ac-225 panel (RIGHT) ----
        ac_card = Rectangle(width=3.4, height=3.2)
        ac_card.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        ac_card.move_to(RIGHT * 2.7 + UP * 0.2)
        ac_title = Text("Ac-225", font=DISPLAY, color=WHITE, font_size=22, weight=BOLD)
        ac_title.move_to(ac_card.get_top() + DOWN * 0.45)
        ac_sub = Text("alpha emitter", font=DISPLAY, color=WHITE, font_size=14)
        ac_sub.next_to(ac_title, DOWN, buff=0.12)
        ac_num = Text("41%", font=MONO, color=CRIMSON, font_size=52, weight=BOLD)
        ac_num.move_to(ac_card.get_center() + UP * 0.15)
        ac_stat = Text("tumor cell kill", font=DISPLAY, color=WHITE, font_size=13)
        ac_stat.next_to(ac_num, DOWN, buff=0.12)
        ac_why = Text("core untouched", font=DISPLAY, color=CRIMSON, font_size=12)
        ac_why.move_to(ac_card.get_bottom() + UP * 0.45)
        ac_group = VGroup(ac_card, ac_title, ac_sub, ac_num, ac_stat, ac_why)

        # VS separator
        vs_lbl = Text("vs", font=SERIF, font_size=22, color=INK, slant=ITALIC)
        vs_lbl.move_to(ORIGIN + UP * 0.2)

        self.play(FadeIn(header), run_time=0.4)
        self.play(GrowFromCenter(lu_card), GrowFromCenter(ac_card), run_time=0.7)
        self.play(FadeIn(lu_title), FadeIn(lu_sub), FadeIn(ac_title), FadeIn(ac_sub),
                  run_time=0.4)
        self.play(FadeIn(lu_num), FadeIn(ac_num), run_time=0.6)
        self.play(FadeIn(lu_stat), FadeIn(ac_stat), FadeIn(vs_lbl), run_time=0.4)
        self.play(FadeIn(lu_why), FadeIn(ac_why), run_time=0.5)
        self.wait(max(0.3, total - 3.0))


# ── B12  Endcard ──────────────────────────────────────────────────────────────
class B12_Endcard(Scene):
    def construct(self):
        total = DUR["B12"]
        topic = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=16)
        main = Text("More lethal per hit does not mean more useful in the tumor.",
                    font=SERIF, color=INK, font_size=26, slant=ITALIC)
        sub = Text("Geometry decides which emitter wins.",
                   font=DISPLAY, color=INK, font_size=22, weight=BOLD)
        block = VGroup(main, sub).arrange(DOWN, buff=0.28).move_to(UP * 0.1)
        u = Line(sub.get_corner(DL) + DOWN * 0.1, sub.get_corner(DR) + DOWN * 0.1,
                 color=GOLD, stroke_width=2)
        topic.next_to(block, UP, buff=0.55)
        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(main), run_time=0.8)
        self.play(FadeIn(sub), Create(u), run_time=0.8)
        self.wait(max(0.3, total - 2.1))
