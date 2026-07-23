import sys, json, pathlib, numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {
    "B01": 4.0,
    "B02": 10.0, "B04": 9.0, "B05": 9.0, "B07": 9.0,
    "B08": 10.0, "B09": 8.0, "B10": 8.0, "B11": 7.0,
    "B12": 16.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
        for b in _BS["beats"]
    })
except Exception:
    pass


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("COMPUTATIONAL SKEPTICISM", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why a Prediction You Can Edit", font=DISPLAY, color=INK,
                  font_size=32, weight=BOLD)
        t2 = Text("Is Worth Nothing", font=DISPLAY, color=CRIMSON, font_size=32, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B02_EditCase(Scene):
    def construct(self):
        header = LabelChip("POST-AUDIT RETROSPECTIVE", accent=SLATE).move_to(UP * 2.8)
        border = Rectangle(width=12.5, height=4.8, color=SLATE, fill_opacity=0.0)
        border.set_stroke(color=SLATE, width=1.0, opacity=0.22)
        border.move_to(ORIGIN)
        rows = [
            ("PERSON 1", "flagging would cluster by zip code"),
            ("PERSON 2", "Group A would be over-represented"),
            ("PERSON 3", "training data had a regional gap"),
        ]
        groups = []
        for j, (person, pred) in enumerate(rows):
            y = 1.2 - j * 1.15
            chip     = LabelChip(person, accent=TEAL, size=19).move_to(np.array([-4.3, y, 0]))
            pred_txt = Text(pred, font=MONO, color=INK).scale(0.37).move_to(np.array([0.5, y, 0]))
            match    = LabelChip("MATCHES AUDIT", accent=CRIMSON, size=16).move_to(np.array([4.5, y, 0]))
            groups.append((chip, pred_txt, match))
        div1 = Line(np.array([-6.0, 0.63, 0]), np.array([6.0, 0.63, 0]), color=SLATE, stroke_width=1)
        div2 = Line(np.array([-6.0, -0.52, 0]), np.array([6.0, -0.52, 0]), color=SLATE, stroke_width=1)
        reveal = Text("AUDIT DATE: MONDAY    PREDICTION RECORDED: AFTER READING", font=MONO, color=CRIMSON).scale(0.34).move_to(DOWN * 2.5)
        self.play(FadeIn(header), GrowFromCenter(border))
        self.play(Create(div1), Create(div2))
        for chip, pred_txt, match in groups:
            self.play(FadeIn(chip), FadeIn(pred_txt), run_time=0.5)
            self.play(FadeIn(match), run_time=0.35)
        self.play(FadeIn(reveal))
        self.wait(max(0.3, DUR["B02"] - 7.5))


class B04_NaivePicture(Scene):
    def construct(self):
        header = LabelChip("NAIVE PICTURE", accent=SLATE).move_to(UP * 2.7)
        pred_box = Rectangle(width=2.4, height=0.75, color=TEAL, fill_opacity=0.13)
        pred_box.set_stroke(color=TEAL, width=2)
        pred_box.move_to(LEFT * 3.5 + UP * 0.4)
        pred_lbl = Text("PREDICTION", font=MONO, color=TEAL).scale(0.38).move_to(LEFT * 3.5 + UP * 0.4)
        arr = Line(np.array([-2.3, 0.4, 0]), np.array([2.3, 0.4, 0]), color=SLATE, stroke_width=2.5)
        out_box = Rectangle(width=2.4, height=0.75, color=SLATE, fill_opacity=0.12)
        out_box.set_stroke(color=SLATE, width=2)
        out_box.move_to(RIGHT * 3.5 + UP * 0.4)
        out_lbl = Text("OUTCOME", font=MONO, color=INK).scale(0.38).move_to(RIGHT * 3.5 + UP * 0.4)
        # Gap bracket below
        g_y = -0.8
        gap_line = Line(np.array([-2.0, g_y, 0]), np.array([2.0, g_y, 0]), color=GOLD, stroke_width=2.5)
        gap_ltic = Line(np.array([-2.0, g_y - 0.15, 0]), np.array([-2.0, g_y + 0.15, 0]), color=GOLD, stroke_width=2.5)
        gap_rtic = Line(np.array([2.0, g_y - 0.15, 0]), np.array([2.0, g_y + 0.15, 0]), color=GOLD, stroke_width=2.5)
        gap_lbl  = Text("EVIDENCE", font=MONO, color=GOLD).scale(0.38).move_to(np.array([0.0, g_y + 0.52, 0]))
        note = Text("gap = what your model of the world got wrong", font=MONO, color=SLATE).scale(0.35).move_to(DOWN * 2.5)
        self.play(FadeIn(header))
        self.play(GrowFromCenter(pred_box), FadeIn(pred_lbl))
        self.play(Create(arr))
        self.play(GrowFromCenter(out_box), FadeIn(out_lbl))
        self.play(Create(gap_line), Create(gap_ltic), Create(gap_rtic), FadeIn(gap_lbl))
        self.play(FadeIn(note))
        self.wait(max(0.3, DUR["B04"] - 8.0))


class B05_GapCollapse(Scene):
    def construct(self):
        header = LabelChip("EDITABLE PREDICTION", accent=CRIMSON).move_to(UP * 2.8)
        pred_y = 1.6
        out_y  = -1.6
        g_x    = 2.4
        pred_box = Rectangle(width=2.5, height=0.65, color=TEAL, fill_opacity=0.15)
        pred_box.set_stroke(color=TEAL, width=2)
        pred_box.move_to(np.array([0.0, pred_y, 0]))
        pred_lbl = Text("PREDICTION", font=MONO, color=TEAL).scale(0.36).move_to(np.array([0.0, pred_y, 0]))
        out_box = Rectangle(width=2.5, height=0.65, color=SLATE, fill_opacity=0.12)
        out_box.set_stroke(color=SLATE, width=2)
        out_box.move_to(np.array([0.0, out_y, 0]))
        out_lbl = Text("OUTCOME", font=MONO, color=INK).scale(0.36).move_to(np.array([0.0, out_y, 0]))
        # Vertical gap bracket on right side
        gap_line = Line(np.array([g_x, out_y, 0]), np.array([g_x, pred_y, 0]), color=GOLD, stroke_width=2.5)
        gap_top  = Line(np.array([g_x - 0.15, pred_y, 0]), np.array([g_x + 0.15, pred_y, 0]), color=GOLD, stroke_width=2.5)
        gap_bot  = Line(np.array([g_x - 0.15, out_y, 0]), np.array([g_x + 0.15, out_y, 0]), color=GOLD, stroke_width=2.5)
        gap_lbl  = Text("INFO", font=MONO, color=GOLD).scale(0.40).move_to(np.array([g_x + 0.75, 0.0, 0]))
        # Collapsed targets
        pred_box_c = Rectangle(width=2.5, height=0.65, color=CRIMSON, fill_opacity=0.15)
        pred_box_c.set_stroke(color=CRIMSON, width=2)
        pred_box_c.move_to(np.array([0.0, out_y, 0]))
        pred_lbl_c = Text("PREDICTION", font=MONO, color=CRIMSON).scale(0.36).move_to(np.array([0.0, out_y, 0]))
        zero_lbl = Text("GAP = 0", font=MONO, color=CRIMSON).scale(0.40).move_to(np.array([g_x + 0.75, out_y, 0]))
        self.play(FadeIn(header))
        self.play(GrowFromCenter(pred_box), FadeIn(pred_lbl))
        self.play(GrowFromCenter(out_box), FadeIn(out_lbl))
        self.play(Create(gap_line), Create(gap_top), Create(gap_bot), FadeIn(gap_lbl))
        self.wait(0.7)
        self.play(
            Transform(pred_box, pred_box_c),
            Transform(pred_lbl, pred_lbl_c),
            FadeOut(gap_line), FadeOut(gap_top), FadeOut(gap_bot), FadeOut(gap_lbl),
            run_time=1.6,
        )
        self.play(FadeIn(zero_lbl))
        self.wait(max(0.3, DUR["B05"] - 9.0))


class B07_PinGap(Scene):
    def construct(self):
        header = LabelChip("THE GAP IS SIGNAL", accent=SLATE).move_to(UP * 2.8)
        pred_x = -3.2
        out_x  =  3.2
        box_y  =  0.5
        pred_box = Rectangle(width=2.2, height=0.7, color=TEAL, fill_opacity=0.14)
        pred_box.set_stroke(color=TEAL, width=2)
        pred_box.move_to(np.array([pred_x, box_y, 0]))
        pred_lbl = Text("PREDICTION", font=MONO, color=TEAL).scale(0.37).move_to(np.array([pred_x, box_y, 0]))
        pred_sub = Text("written before", font=MONO, color=TEAL).scale(0.28).move_to(np.array([pred_x, box_y - 0.85, 0]))
        out_box = Rectangle(width=2.2, height=0.7, color=SLATE, fill_opacity=0.12)
        out_box.set_stroke(color=SLATE, width=2)
        out_box.move_to(np.array([out_x, box_y, 0]))
        out_lbl = Text("OUTCOME", font=MONO, color=INK).scale(0.37).move_to(np.array([out_x, box_y, 0]))
        # Gap bracket at y = -0.85
        g_y = -0.85
        gap_line = Line(np.array([pred_x + 1.1, g_y, 0]), np.array([out_x - 1.1, g_y, 0]), color=GOLD, stroke_width=2.5)
        gap_ltic = Line(np.array([pred_x + 1.1, g_y - 0.15, 0]), np.array([pred_x + 1.1, g_y + 0.15, 0]), color=GOLD, stroke_width=2.5)
        gap_rtic = Line(np.array([out_x - 1.1, g_y - 0.15, 0]), np.array([out_x - 1.1, g_y + 0.15, 0]), color=GOLD, stroke_width=2.5)
        gap_lbl  = Text("INFORMATION", font=MONO, color=GOLD).scale(0.37).move_to(np.array([0.0, g_y + 0.52, 0]))
        note = Text("gap = what you got right or wrong about the world", font=MONO, color=SLATE).scale(0.34).move_to(DOWN * 2.5)
        self.play(FadeIn(header))
        self.play(GrowFromCenter(pred_box), FadeIn(pred_lbl), FadeIn(pred_sub))
        self.play(GrowFromCenter(out_box), FadeIn(out_lbl))
        self.play(Create(gap_line), Create(gap_ltic), Create(gap_rtic), FadeIn(gap_lbl))
        self.play(FadeIn(note))
        self.wait(max(0.3, DUR["B07"] - 7.5))


class B08_LockedVsUnlocked(Scene):
    def construct(self):
        divider     = Line(np.array([0.0, 3.1, 0]), np.array([0.0, -3.1, 0]), color=SLATE, stroke_width=1.5)
        lbl_locked  = LabelChip("LOCKED", accent=TEAL, size=20).move_to(np.array([-3.2, 2.85, 0]))
        lbl_unlkd   = LabelChip("UNLOCKED", accent=CRIMSON, size=20).move_to(np.array([3.2, 2.85, 0]))
        # LEFT — locked: prediction stays, gap survives
        l_pred = Rectangle(width=2.6, height=0.65, color=TEAL, fill_opacity=0.15)
        l_pred.set_stroke(color=TEAL, width=2)
        l_pred.move_to(np.array([-3.2, 1.6, 0]))
        l_pred_lbl = Text("PREDICTION", font=MONO, color=TEAL).scale(0.35).move_to(np.array([-3.2, 1.6, 0]))
        l_out = Rectangle(width=2.6, height=0.65, color=SLATE, fill_opacity=0.12)
        l_out.set_stroke(color=SLATE, width=2)
        l_out.move_to(np.array([-3.2, -1.6, 0]))
        l_out_lbl = Text("OUTCOME", font=MONO, color=INK).scale(0.35).move_to(np.array([-3.2, -1.6, 0]))
        g_y = 0.0
        l_gap      = Line(np.array([-4.6, g_y, 0]), np.array([-1.8, g_y, 0]), color=TEAL, stroke_width=2.5)
        l_gap_ltic = Line(np.array([-4.6, g_y - 0.15, 0]), np.array([-4.6, g_y + 0.15, 0]), color=TEAL, stroke_width=2.5)
        l_gap_rtic = Line(np.array([-1.8, g_y - 0.15, 0]), np.array([-1.8, g_y + 0.15, 0]), color=TEAL, stroke_width=2.5)
        l_gap_lbl  = Text("GAP SURVIVES", font=MONO, color=TEAL).scale(0.32).move_to(np.array([-3.2, g_y + 0.48, 0]))
        # RIGHT — unlocked: prediction collapses to outcome
        r_pred = Rectangle(width=2.6, height=0.65, color=TEAL, fill_opacity=0.15)
        r_pred.set_stroke(color=TEAL, width=2)
        r_pred.move_to(np.array([3.2, 1.6, 0]))
        r_pred_lbl = Text("PREDICTION", font=MONO, color=TEAL).scale(0.35).move_to(np.array([3.2, 1.6, 0]))
        r_out = Rectangle(width=2.6, height=0.65, color=SLATE, fill_opacity=0.12)
        r_out.set_stroke(color=SLATE, width=2)
        r_out.move_to(np.array([3.2, -1.6, 0]))
        r_out_lbl = Text("OUTCOME", font=MONO, color=INK).scale(0.35).move_to(np.array([3.2, -1.6, 0]))
        r_pred_end = Rectangle(width=2.6, height=0.65, color=CRIMSON, fill_opacity=0.15)
        r_pred_end.set_stroke(color=CRIMSON, width=2)
        r_pred_end.move_to(np.array([3.2, -1.6, 0]))
        r_gap_zero = Text("GAP = 0", font=MONO, color=CRIMSON).scale(0.38).move_to(np.array([3.2, 0.0, 0]))
        self.play(Create(divider))
        self.play(FadeIn(lbl_locked), FadeIn(lbl_unlkd))
        self.play(GrowFromCenter(l_pred), FadeIn(l_pred_lbl))
        self.play(GrowFromCenter(l_out), FadeIn(l_out_lbl))
        self.play(Create(l_gap), Create(l_gap_ltic), Create(l_gap_rtic), FadeIn(l_gap_lbl))
        self.play(GrowFromCenter(r_pred), FadeIn(r_pred_lbl))
        self.play(GrowFromCenter(r_out), FadeIn(r_out_lbl))
        self.play(Transform(r_pred, r_pred_end), FadeOut(r_pred_lbl), FadeIn(r_gap_zero), run_time=1.5)
        self.wait(max(0.3, DUR["B08"] - 10.0))


class B09_QuoteLock(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Written before the result, a guess is evidence. "
            "Editable after, the identical sentence proves nothing.",
            "Computational Skepticism for AI, Chapter 1",
            None,
            "proves nothing",
            DUR["B09"],
        )


class B10_BrokenInstrument(Scene):
    def construct(self):
        header = LabelChip("WHAT THE GAP MEASURES", accent=SLATE).move_to(UP * 2.8)
        divider = Line(np.array([0.0, 2.1, 0]), np.array([0.0, -2.2, 0]), color=SLATE, stroke_width=1.5)
        l_box = Rectangle(width=4.8, height=3.8, color=TEAL, fill_opacity=0.06)
        l_box.set_stroke(color=TEAL, width=1.5)
        l_box.move_to(np.array([-3.2, -0.15, 0]))
        l_title   = Text("LOCKED", font=MONO, color=TEAL).scale(0.42).move_to(np.array([-3.2, 1.2, 0]))
        l_measure = Text("MEASURES:", font=MONO, color=TEAL).scale(0.37).move_to(np.array([-3.2, 0.3, 0]))
        l_what    = Text("UNDERSTANDING", font=MONO, color=TEAL).scale(0.42).move_to(np.array([-3.2, -0.3, 0]))
        l_note    = Text("gap > 0  ->  signal", font=MONO, color=TEAL).scale(0.34).move_to(np.array([-3.2, -1.2, 0]))
        r_box = Rectangle(width=4.8, height=3.8, color=CRIMSON, fill_opacity=0.06)
        r_box.set_stroke(color=CRIMSON, width=1.5)
        r_box.move_to(np.array([3.2, -0.15, 0]))
        r_title   = Text("UNLOCKED", font=MONO, color=CRIMSON).scale(0.42).move_to(np.array([3.2, 1.2, 0]))
        r_measure = Text("MEASURES:", font=MONO, color=CRIMSON).scale(0.37).move_to(np.array([3.2, 0.3, 0]))
        r_what    = Text("EDITING SPEED", font=MONO, color=CRIMSON).scale(0.42).move_to(np.array([3.2, -0.3, 0]))
        r_note    = Text("gap = 0  ->  nothing", font=MONO, color=CRIMSON).scale(0.34).move_to(np.array([3.2, -1.2, 0]))
        self.play(FadeIn(header), Create(divider))
        self.play(GrowFromCenter(l_box), FadeIn(l_title))
        self.play(FadeIn(l_measure), FadeIn(l_what), FadeIn(l_note))
        self.play(GrowFromCenter(r_box), FadeIn(r_title))
        self.play(FadeIn(r_measure), FadeIn(r_what), FadeIn(r_note))
        self.wait(max(0.3, DUR["B10"] - 8.0))


class B11_QuoteInfo(Scene):
    def construct(self):
        _quote_scene(
            self,
            "The information lives in the gap. "
            "Leave the prediction unlocked and it slides to meet the result.",
            "Computational Skepticism for AI, Chapter 1",
            None,
            "slides to meet the result",
            DUR["B11"],
        )


class B12_ExampleLock(Scene):
    """THE EXAMPLE — A/B test: no locked prediction, gap collapses, no calibration possible."""
    def construct(self):
        total = DUR["B12"]
        title = Text("A/B Test — algorithm recommendation", font=DISPLAY,
                     font_size=20, color=GOLD)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.5, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        col_r = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)

        lbl_l = Text("Prediction locked", font=DISPLAY, font_size=22, color=TEAL, weight=BOLD)
        lbl_l.move_to(col_l.get_top() + DOWN * 0.45)
        val_l1 = Text("written before: +2.0%", font=MONO, font_size=20, color=TEAL)
        val_l1.move_to(col_l.get_center() + UP * 0.3)
        val_l2 = Text("result: +1.8%", font=MONO, font_size=20, color=TEAL)
        val_l2.move_to(col_l.get_center() + DOWN * 0.25)
        val_l3 = Text("gap: 0.2%  ← signal", font=SERIF, font_size=18, color=TEAL)
        val_l3.move_to(col_l.get_center() + DOWN * 1.1)

        lbl_r = Text("No lock", font=DISPLAY, font_size=22, color=CRIMSON, weight=BOLD)
        lbl_r.move_to(col_r.get_top() + DOWN * 0.45)
        val_r1 = Text("result: +1.8%", font=MONO, font_size=20, color=CRIMSON)
        val_r1.move_to(col_r.get_center() + UP * 0.3)
        val_r2 = Text("remembered: +1.8%", font=MONO, font_size=20, color=CRIMSON)
        val_r2.move_to(col_r.get_center() + DOWN * 0.25)
        val_r3 = Text("gap: 0.0%  ← nothing learned", font=SERIF, font_size=18, color=CRIMSON)
        val_r3.move_to(col_r.get_center() + DOWN * 1.1)

        note_rect = Rectangle(width=9.5, height=0.52, fill_color=CRIMSON, fill_opacity=0.10,
                              stroke_width=1.5, color=CRIMSON).move_to(DOWN * 2.55)
        note_txt = Text("6 months, 3 tests — no calibration data ever captured",
                        font=SERIF, font_size=19, color=CRIMSON)
        note_txt.move_to(note_rect.get_center())

        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(col_l), FadeIn(lbl_l), run_time=0.7)
        self.play(FadeIn(val_l1), FadeIn(val_l2), FadeIn(val_l3), run_time=0.6)
        self.play(FadeIn(col_r), FadeIn(lbl_r), run_time=0.7)
        self.play(FadeIn(val_r1), FadeIn(val_r2), FadeIn(val_r3), run_time=0.6)
        self.play(FadeIn(note_rect), FadeIn(note_txt), run_time=0.7)
        self.wait(max(0.5, total - 4.0))
