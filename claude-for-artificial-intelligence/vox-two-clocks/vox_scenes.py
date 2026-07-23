import sys, json, pathlib, numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {
    "B01": 4.0,
    "B02": 10.0, "B04": 8.0, "B05": 8.0, "B07": 10.0,
    "B08": 9.0,  "B09": 9.0, "B10": 8.0, "B11": 7.0, "B12": 12.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
        for b in _BS["beats"]
    })
except Exception:
    pass

# ── B01 — Title ───────────────────────────────────────────────────────────────

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("COMPUTATIONAL SKEPTICISM", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why the Study Method That Feels Best", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("Teaches the Least", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# Shared curve geometry
_OX, _OY = -4.5, -2.3
_AXW = 8.2
_AXH = 3.8
_NT   = 40
_T_MAX = 8.0


def _t_to_x(t):
    return _OX + (t / _T_MAX) * _AXW


def _p_to_y(p):
    return _OY + p * _AXH


def _fluent_pts():
    return [np.array([_t_to_x(i / _NT * _T_MAX),
                      _p_to_y(0.85 * np.exp(-0.40 * i / _NT * _T_MAX) + 0.15), 0])
            for i in range(_NT + 1)]


def _friction_pts():
    return [np.array([_t_to_x(i / _NT * _T_MAX),
                      _p_to_y(0.35 + 0.30 * (1.0 - np.exp(-0.50 * i / _NT * _T_MAX))), 0])
            for i in range(_NT + 1)]


def _curve_vgroup(pts, color, sw=3.2):
    return VGroup(*[Line(pts[i], pts[i + 1], color=color, stroke_width=sw)
                    for i in range(len(pts) - 1)])


def _chart_axes():
    x_ax = Line(np.array([_OX, _OY, 0]), np.array([_OX + _AXW, _OY, 0]), color=SLATE, stroke_width=2)
    y_ax = Line(np.array([_OX, _OY, 0]), np.array([_OX, _OY + _AXH, 0]), color=SLATE, stroke_width=2)
    x_lbl = Text("TIME", font=MONO, color=SLATE).scale(0.34).move_to(np.array([_OX + _AXW / 2, _OY - 0.48, 0]))
    y_lbl = Text("PERFORMANCE", font=MONO, color=SLATE).scale(0.30).move_to(np.array([_OX - 0.85, _OY + _AXH / 2, 0]))
    return x_ax, y_ax, x_lbl, y_lbl


class B02_StudyComparison(Scene):
    def construct(self):
        header = LabelChip("SAME EXAM — ONE WEEK APART", accent=SLATE).move_to(UP * 2.8)
        border = Rectangle(width=12.5, height=5.0, color=SLATE, fill_opacity=0.0)
        border.set_stroke(color=SLATE, width=1.0, opacity=0.22)
        border.move_to(ORIGIN + DOWN * 0.1)
        col_h1 = Text("STUDY METHOD", font=MONO, color=SLATE).scale(0.33).move_to(np.array([-3.5, 1.8, 0]))
        col_h2 = Text("EXAM DAY", font=MONO, color=SLATE).scale(0.33).move_to(np.array([0.7, 1.8, 0]))
        col_h3 = Text("ONE WEEK LATER", font=MONO, color=SLATE).scale(0.33).move_to(np.array([3.8, 1.8, 0]))
        rows = [
            ("FLUENT", "reads notes, comfortable",  "85%",  "45%",  CRIMSON),
            ("FRICTIONAL", "retrieval practice, confused", "70%", "68%", TEAL),
        ]
        row_groups = []
        for j, (label, method, score_now, score_later, col) in enumerate(rows):
            y = 0.5 - j * 1.6
            chip          = LabelChip(label, accent=col, size=18).move_to(np.array([-5.0, y, 0]))
            method_txt    = Text(method, font=MONO, color=INK).scale(0.30).move_to(np.array([-2.5, y, 0]))
            score_now_txt = Text(score_now, font=MONO, color=col).scale(0.46).move_to(np.array([0.7, y, 0]))
            score_late_txt = Text(score_later, font=MONO, color=col).scale(0.46).move_to(np.array([3.8, y, 0]))
            row_groups.append((chip, method_txt, score_now_txt, score_late_txt))
        div_h1 = Line(np.array([-6.0, 1.3, 0]), np.array([6.0, 1.3, 0]), color=SLATE, stroke_width=1)
        div_h2 = Line(np.array([-6.0, -0.3, 0]), np.array([6.0, -0.3, 0]), color=SLATE, stroke_width=1)
        div_v1 = Line(np.array([-0.7, 1.3, 0]), np.array([-0.7, -2.1, 0]), color=SLATE, stroke_width=1)
        div_v2 = Line(np.array([2.2, 1.3, 0]), np.array([2.2, -2.1, 0]), color=SLATE, stroke_width=1)
        note = Text("frictional: lower on day one, higher one week later", font=MONO, color=SLATE).scale(0.33).move_to(DOWN * 2.6)
        self.play(FadeIn(header), GrowFromCenter(border))
        self.play(FadeIn(col_h1), FadeIn(col_h2), FadeIn(col_h3))
        self.play(Create(div_h1), Create(div_h2), Create(div_v1), Create(div_v2))
        for chip, method_txt, score_now_txt, _ in row_groups:
            self.play(FadeIn(chip), FadeIn(method_txt), FadeIn(score_now_txt), run_time=0.5)
        self.wait(0.5)
        for _, _, _, score_late_txt in row_groups:
            self.play(FadeIn(score_late_txt), run_time=0.45)
        self.play(FadeIn(note))
        self.wait(max(0.3, DUR["B02"] - 8.5))


class B04_NaivePicture(Scene):
    def construct(self):
        header = LabelChip("NAIVE ASSUMPTION", accent=SLATE).move_to(UP * 2.8)
        divider = Line(np.array([0.0, 2.1, 0]), np.array([0.0, -2.2, 0]), color=SLATE, stroke_width=1.5)
        lbl_f = LabelChip("FLUENT", accent=CRIMSON, size=20).move_to(np.array([-3.2, 2.1, 0]))
        lbl_r = LabelChip("FRICTIONAL", accent=TEAL, size=20).move_to(np.array([3.2, 2.1, 0]))
        # Left: high performance, learning "???"
        f_perf = Rectangle(width=3.2, height=0.65, color=CRIMSON, fill_opacity=0.12)
        f_perf.set_stroke(color=CRIMSON, width=2)
        f_perf.move_to(np.array([-3.2, 1.0, 0]))
        f_perf_lbl = Text("PERFORMANCE: HIGH", font=MONO, color=CRIMSON).scale(0.35).move_to(np.array([-3.2, 1.0, 0]))
        f_learn = Rectangle(width=3.2, height=0.65, color=SLATE, fill_opacity=0.05)
        f_learn.set_stroke(color=SLATE, width=1.5, opacity=0.45)
        f_learn.move_to(np.array([-3.2, -0.1, 0]))
        f_learn_lbl = Text("LEARNING: ???", font=MONO, color=SLATE).scale(0.35).move_to(np.array([-3.2, -0.1, 0]))
        # Right: lower performance, learning "???"
        r_perf = Rectangle(width=3.2, height=0.65, color=TEAL, fill_opacity=0.12)
        r_perf.set_stroke(color=TEAL, width=2)
        r_perf.move_to(np.array([3.2, 1.0, 0]))
        r_perf_lbl = Text("PERFORMANCE: LOWER", font=MONO, color=TEAL).scale(0.35).move_to(np.array([3.2, 1.0, 0]))
        r_learn = Rectangle(width=3.2, height=0.65, color=SLATE, fill_opacity=0.05)
        r_learn.set_stroke(color=SLATE, width=1.5, opacity=0.45)
        r_learn.move_to(np.array([3.2, -0.1, 0]))
        r_learn_lbl = Text("LEARNING: ???", font=MONO, color=SLATE).scale(0.35).move_to(np.array([3.2, -0.1, 0]))
        note = Text("naive view: FLUENT = better learning", font=MONO, color=SLATE).scale(0.35).move_to(DOWN * 1.9)
        self.play(FadeIn(header), Create(divider))
        self.play(FadeIn(lbl_f), FadeIn(lbl_r))
        self.play(GrowFromCenter(f_perf), FadeIn(f_perf_lbl))
        self.play(GrowFromCenter(r_perf), FadeIn(r_perf_lbl))
        self.play(GrowFromCenter(f_learn), FadeIn(f_learn_lbl))
        self.play(GrowFromCenter(r_learn), FadeIn(r_learn_lbl))
        self.play(FadeIn(note))
        self.wait(max(0.3, DUR["B04"] - 7.5))


class B05_TwoClocks(Scene):
    def construct(self):
        header = LabelChip("REALITY: TWO SEPARATE CLOCKS", accent=CRIMSON).move_to(UP * 2.8)
        divider = Line(np.array([0.0, 2.1, 0]), np.array([0.0, -2.2, 0]), color=SLATE, stroke_width=1.5)
        lbl_f = LabelChip("FLUENT", accent=CRIMSON, size=20).move_to(np.array([-3.2, 2.1, 0]))
        lbl_r = LabelChip("FRICTIONAL", accent=TEAL, size=20).move_to(np.array([3.2, 2.1, 0]))
        # Left: high performance, LOW learning
        f_perf = Rectangle(width=3.2, height=0.65, color=CRIMSON, fill_opacity=0.12)
        f_perf.set_stroke(color=CRIMSON, width=2)
        f_perf.move_to(np.array([-3.2, 1.0, 0]))
        f_perf_lbl = Text("PERFORMANCE: HIGH", font=MONO, color=CRIMSON).scale(0.35).move_to(np.array([-3.2, 1.0, 0]))
        f_learn = Rectangle(width=3.2, height=0.65, color=CRIMSON, fill_opacity=0.08)
        f_learn.set_stroke(color=CRIMSON, width=2)
        f_learn.move_to(np.array([-3.2, -0.1, 0]))
        f_learn_lbl = Text("LEARNING: LOW", font=MONO, color=CRIMSON).scale(0.35).move_to(np.array([-3.2, -0.1, 0]))
        # Right: lower performance, HIGH learning
        r_perf = Rectangle(width=3.2, height=0.65, color=TEAL, fill_opacity=0.12)
        r_perf.set_stroke(color=TEAL, width=2)
        r_perf.move_to(np.array([3.2, 1.0, 0]))
        r_perf_lbl = Text("PERFORMANCE: LOWER", font=MONO, color=TEAL).scale(0.35).move_to(np.array([3.2, 1.0, 0]))
        r_learn = Rectangle(width=3.2, height=0.65, color=TEAL, fill_opacity=0.12)
        r_learn.set_stroke(color=TEAL, width=2)
        r_learn.move_to(np.array([3.2, -0.1, 0]))
        r_learn_lbl = Text("LEARNING: HIGH", font=MONO, color=TEAL).scale(0.35).move_to(np.array([3.2, -0.1, 0]))
        note = Text("two clocks running in opposite directions", font=MONO, color=SLATE).scale(0.35).move_to(DOWN * 1.9)
        self.play(FadeIn(header), Create(divider))
        self.play(FadeIn(lbl_f), FadeIn(lbl_r))
        self.play(GrowFromCenter(f_perf), FadeIn(f_perf_lbl))
        self.play(GrowFromCenter(r_perf), FadeIn(r_perf_lbl))
        self.play(GrowFromCenter(f_learn), FadeIn(f_learn_lbl))
        self.play(GrowFromCenter(r_learn), FadeIn(r_learn_lbl))
        self.play(FadeIn(note))
        self.wait(max(0.3, DUR["B05"] - 7.5))


class B07_DrawCurves(Scene):
    def construct(self):
        x_ax, y_ax, x_lbl, y_lbl = _chart_axes()
        fluent_pts   = _fluent_pts()
        friction_pts = _friction_pts()
        fluent_curve   = _curve_vgroup(fluent_pts,   CRIMSON)
        friction_curve = _curve_vgroup(friction_pts, TEAL)
        fluent_lbl   = LabelChip("FLUENT",      accent=CRIMSON, size=18).move_to(np.array([-3.2, 1.8, 0]))
        friction_lbl = LabelChip("FRICTIONAL",  accent=TEAL,    size=18).move_to(np.array([2.5,  0.55, 0]))
        self.play(Create(x_ax), Create(y_ax), FadeIn(x_lbl), FadeIn(y_lbl))
        self.play(Create(fluent_curve, lag_ratio=0.03), run_time=1.6)
        self.play(FadeIn(fluent_lbl))
        self.play(Create(friction_curve, lag_ratio=0.03), run_time=1.6)
        self.play(FadeIn(friction_lbl))
        self.wait(max(0.3, DUR["B07"] - 8.5))


class B08_CrossPoint(Scene):
    def construct(self):
        # Pre-add axes and curves
        x_ax, y_ax, x_lbl, y_lbl = _chart_axes()
        fluent_pts   = _fluent_pts()
        friction_pts = _friction_pts()
        t_cross  = 2.0
        n_cross  = int(_NT * t_cross / _T_MAX)  # 10
        f_early  = _curve_vgroup(fluent_pts[:n_cross + 1],   CRIMSON)
        f_late   = _curve_vgroup(fluent_pts[n_cross:],       CRIMSON)
        r_early  = _curve_vgroup(friction_pts[:n_cross + 1], TEAL)
        r_late   = _curve_vgroup(friction_pts[n_cross:],     TEAL)
        fluent_lbl   = LabelChip("FLUENT",     accent=CRIMSON, size=18).move_to(np.array([-3.2, 1.8, 0]))
        friction_lbl = LabelChip("FRICTIONAL", accent=TEAL,    size=18).move_to(np.array([2.5,  0.55, 0]))
        # Crossing marker
        cross_x  = _t_to_x(t_cross)
        cross_p  = 0.85 * np.exp(-0.40 * t_cross) + 0.15
        cross_y  = _p_to_y(cross_p)
        cross_dot = Rectangle(width=0.28, height=0.28, color=GOLD, fill_opacity=1.0)
        cross_dot.set_stroke(width=0)
        cross_dot.move_to(np.array([cross_x, cross_y, 0]))
        cross_lbl = Text("CURVES CROSS", font=MONO, color=GOLD).scale(0.35).move_to(
            np.array([cross_x + 1.8, cross_y + 0.55, 0]))
        time_note = Text("one week later: frictional stays, fluent fades", font=MONO, color=SLATE).scale(0.33).move_to(
            np.array([0.0, _OY - 0.48, 0]))
        self.play(Create(x_ax), Create(y_ax), FadeIn(x_lbl), FadeIn(y_lbl))
        self.play(Create(f_early, lag_ratio=0.0), Create(r_early, lag_ratio=0.0), run_time=0.7)
        self.play(FadeIn(fluent_lbl), FadeIn(friction_lbl))
        self.play(Create(f_late, lag_ratio=0.03), Create(r_late, lag_ratio=0.03), run_time=1.6)
        self.play(GrowFromCenter(cross_dot), FadeIn(cross_lbl))
        self.play(FadeIn(time_note))
        self.wait(max(0.3, DUR["B08"] - 8.5))


class B09_QuoteStruggle(Scene):
    def construct(self):
        _quote_scene(
            self,
            "The student who feels they are mastering the material under fluent conditions "
            "is often learning less than the student who feels confused under more friction. "
            "The fluency is the trap.",
            "Computational Skepticism for AI, Chapter 4",
            None,
            "feels confused",
            DUR["B09"],
        )


class B10_StorageStrength(Scene):
    def construct(self):
        header = LabelChip("WHAT PERSISTS", accent=SLATE).move_to(UP * 2.8)
        divider = Line(np.array([0.0, 2.1, 0]), np.array([0.0, -2.3, 0]), color=SLATE, stroke_width=1.5)
        lbl_f = LabelChip("FLUENT", accent=CRIMSON, size=20).move_to(np.array([-3.2, 2.1, 0]))
        lbl_r = LabelChip("FRICTIONAL", accent=TEAL, size=20).move_to(np.array([3.2, 2.1, 0]))
        f_perf = Rectangle(width=3.4, height=0.65, color=CRIMSON, fill_opacity=0.12)
        f_perf.set_stroke(color=CRIMSON, width=2)
        f_perf.move_to(np.array([-3.2, 1.1, 0]))
        f_perf_lbl = Text("PERFORMANCE: HIGH", font=MONO, color=CRIMSON).scale(0.35).move_to(np.array([-3.2, 1.1, 0]))
        f_store = Rectangle(width=3.4, height=0.65, color=CRIMSON, fill_opacity=0.08)
        f_store.set_stroke(color=CRIMSON, width=2)
        f_store.move_to(np.array([-3.2, -0.05, 0]))
        f_store_lbl = Text("STORAGE STRENGTH: LOW", font=MONO, color=CRIMSON).scale(0.32).move_to(np.array([-3.2, -0.05, 0]))
        f_decay = Text("decays monotonically", font=MONO, color=CRIMSON).scale(0.30).move_to(np.array([-3.2, -0.95, 0]))
        r_perf = Rectangle(width=3.4, height=0.65, color=TEAL, fill_opacity=0.12)
        r_perf.set_stroke(color=TEAL, width=2)
        r_perf.move_to(np.array([3.2, 1.1, 0]))
        r_perf_lbl = Text("PERFORMANCE: LOWER", font=MONO, color=TEAL).scale(0.35).move_to(np.array([3.2, 1.1, 0]))
        r_store = Rectangle(width=3.4, height=0.65, color=TEAL, fill_opacity=0.12)
        r_store.set_stroke(color=TEAL, width=2)
        r_store.move_to(np.array([3.2, -0.05, 0]))
        r_store_lbl = Text("STORAGE STRENGTH: HIGH", font=MONO, color=TEAL).scale(0.32).move_to(np.array([3.2, -0.05, 0]))
        r_persist = Text("persists under spacing", font=MONO, color=TEAL).scale(0.30).move_to(np.array([3.2, -0.95, 0]))
        self.play(FadeIn(header), Create(divider))
        self.play(FadeIn(lbl_f), FadeIn(lbl_r))
        self.play(GrowFromCenter(f_perf), FadeIn(f_perf_lbl))
        self.play(GrowFromCenter(r_perf), FadeIn(r_perf_lbl))
        self.play(GrowFromCenter(f_store), FadeIn(f_store_lbl), FadeIn(f_decay))
        self.play(GrowFromCenter(r_store), FadeIn(r_store_lbl), FadeIn(r_persist))
        self.wait(max(0.3, DUR["B10"] - 8.0))


class B11_QuoteDecay(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Borrowed certainty has no storage strength to retrieve. "
            "Performance decays monotonically and the spacing effect is absent.",
            "Computational Skepticism for AI, Chapter 4",
            None,
            "storage strength",
            DUR["B11"],
        )


# ── B12 — ExampleTwoClocks ────────────────────────────────────────────────────

class B12_ExampleTwoClocks(Scene):
    def construct(self):
        total = DUR["B12"]
        title = Text("Onboarding program — retention after 2 weeks", font=DISPLAY, font_size=18, color=GOLD)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        col_r = Rectangle(width=5.5, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)

        lbl_l = Text("Fluent (explainer video)", font=DISPLAY, font_size=15, color=CRIMSON).move_to(LEFT * 3.2 + UP * 1.55)
        lbl_r = Text("Frictional (retrieval practice)", font=DISPLAY, font_size=14, color=TEAL).move_to(RIGHT * 3.2 + UP * 1.55)

        val_l1 = Text("Experience rating: 8 / 10", font=MONO, font_size=13, color=CRIMSON).move_to(LEFT * 3.2 + UP * 0.65)
        val_l2 = Text("Retention test: 41%", font=MONO, font_size=14, color=CRIMSON).move_to(LEFT * 3.2 + DOWN * 0.05)
        val_l3 = Text("Felt productive → decayed", font=MONO, font_size=12, color=CRIMSON).move_to(LEFT * 3.2 + DOWN * 0.75)

        val_r1 = Text("Experience rating: 6 / 10", font=MONO, font_size=13, color=TEAL).move_to(RIGHT * 3.2 + UP * 0.65)
        val_r2 = Text("Retention test: 73%", font=MONO, font_size=14, color=TEAL).move_to(RIGHT * 3.2 + DOWN * 0.05)
        val_r3 = Text("Felt harder → persisted", font=MONO, font_size=12, color=TEAL).move_to(RIGHT * 3.2 + DOWN * 0.75)

        note_rect = Rectangle(width=9.5, height=0.52, fill_color=GOLD, fill_opacity=0.10,
                              stroke_width=1.5, color=GOLD).move_to(DOWN * 2.55)
        note_txt = Text("fluency measured the video quality, not the learning (illustrative)",
                        font=MONO, font_size=11, color=GOLD).move_to(DOWN * 2.55)

        self.play(Write(title), run_time=0.5)
        self.play(GrowFromCenter(col_l), GrowFromCenter(col_r), run_time=0.6)
        self.play(Write(lbl_l), Write(lbl_r), run_time=0.5)
        self.play(Write(val_l1), Write(val_r1), run_time=0.4)
        self.play(Write(val_l2), Write(val_r2), run_time=0.4)
        self.play(Write(val_l3), Write(val_r3), run_time=0.4)
        self.play(GrowFromCenter(note_rect), run_time=0.4)
        self.play(Write(note_txt), run_time=0.4)
        self.wait(max(0.5, total - 4.2))
