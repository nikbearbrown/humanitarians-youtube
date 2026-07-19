import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_BoondoggleTable(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)
        title = Text("Boondoggle Score: Application Tracker Phase 1", font="Prism", font_size=20, color=INK, weight=BOLD)
        title.move_to([0, 3.2, 0])
        self.play(FadeIn(title), run_time=0.4)
        hdrs = ["#", "Phase", "Labor", "Capacity", "Handoff Condition"]
        x_pos = [-5.0, -3.5, -1.8, -0.2, 2.8]
        hdr_line = Line(start=[-5.5, 2.5, 0], end=[5.5, 2.5, 0], color=INK, stroke_width=2)
        self.play(Create(hdr_line), run_time=0.3)
        for h, xp in zip(hdrs, x_pos):
            bg = Rectangle(width=len(h)*0.18+0.3, height=0.38, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([xp, 2.75, 0])
            lbl = Text(h, font="Prism", font_size=13, color=SLATE, weight=BOLD)
            lbl.move_to([xp, 2.75, 0])
            self.play(GrowFromCenter(bg), FadeIn(lbl), run_time=0.12)
        data = [
            ("1","Data model","Claude","—",     "pytest tests/test_models.py exits 0",  CREAM,  False),
            ("2","Add form",  "Claude","PA",    "pytest tests/test_add.py -k happy",    CREAM,  False),
            ("3","State pers.","Claude","PA+IJ","all 3 apps survive reload in browser", CRIMSON,True),
            ("4","Delete",    "Human", "PF",    "pytest tests/test_delete.py exits 0",  CREAM,  False),
            ("5","UI polish", "Human", "IJ",    "screenshot matches wireframe.png",     CREAM,  False),
        ]
        y_top = 2.0
        for i, (num, phase, labor, cap, handoff, border_clr, is_risk) in enumerate(data):
            y = y_top - i * 0.78
            bg_clr = "#FFF0F0" if is_risk else CREAM
            row_bg = Rectangle(width=11.0, height=0.68, fill_color=bg_clr, fill_opacity=0.8,
                               stroke_color=border_clr, stroke_width=2.5 if is_risk else 0.5)
            row_bg.move_to([0, y, 0])
            self.play(GrowFromCenter(row_bg), run_time=0.2)
            for val, xp in zip([num, phase, labor, cap, handoff], x_pos):
                clr = CRIMSON if is_risk else INK
                lbl = Text(val, font="Prism", font_size=12, color=clr)
                lbl.move_to([xp, y, 0])
                self.play(FadeIn(lbl), run_time=0.08)
            if is_risk:
                risk_bg = Rectangle(width=2.2, height=0.38, fill_color=GOLD, fill_opacity=1,
                                    stroke_width=0, stroke_opacity=0)
                risk_bg.move_to([5.0, y, 0])
                risk_lbl = Text("HIGH RISK", font="Prism", font_size=12, color=CRIMSON, weight=BOLD)
                risk_lbl.move_to([5.0, y, 0])
                self.play(GrowFromCenter(risk_bg), FadeIn(risk_lbl), run_time=0.2)
        crit_box = Rectangle(width=7.0, height=0.58, fill_color=GOLD, fill_opacity=0.9,
                             stroke_color=CRIMSON, stroke_width=2)
        crit_box.move_to([0, -2.05, 0])
        self.play(GrowFromCenter(crit_box), run_time=0.35)
        crit_lbl = Text("Critical path: step 1 -> 2 -> 3  (state persistence blocks all others)", font="Prism", font_size=13, color=CRIMSON, weight=BOLD)
        crit_lbl.move_to([0, -2.05, 0])
        self.play(FadeIn(crit_lbl), run_time=0.3)
        self.wait(max(0, dur - 6.0))


class B06_InvalidHandoff(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("Handoff Condition Validator", font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.2, 0])
        self.play(FadeIn(title), run_time=0.4)
        bad_bg = Rectangle(width=9.0, height=0.75, fill_color="#FFF0F0", fill_opacity=1,
                           stroke_color=CRIMSON, stroke_width=2)
        bad_bg.move_to([0, 2.4, 0])
        self.play(GrowFromCenter(bad_bg), run_time=0.35)
        bad_lbl = Text('Step 1 handoff: "Claude completes the data model"', font="Prism", font_size=16, color=CRIMSON)
        bad_lbl.move_to([0, 2.4, 0])
        self.play(FadeIn(bad_lbl), run_time=0.3)
        flag_bg = Rectangle(width=6.5, height=0.65, fill_color=CRIMSON, fill_opacity=1.0,
                            stroke_width=0, stroke_opacity=0)
        flag_bg.move_to([0, 1.55, 0])
        self.play(GrowFromCenter(flag_bg), run_time=0.35)
        flag_lbl = Text("NOT MACHINE-CHECKABLE -- revise required", font="Prism", font_size=16, color=INK, weight=BOLD)
        flag_lbl.move_to([0, 1.55, 0])
        self.play(FadeIn(flag_lbl), run_time=0.3)
        reasons_box = Rectangle(width=8.5, height=1.5, fill_color=CREAM, fill_opacity=1,
                                stroke_color=SLATE, stroke_width=1.5)
        reasons_box.move_to([0, 0.6, 0])
        self.play(GrowFromCenter(reasons_box), run_time=0.3)
        r1_bg = Rectangle(width=8.3, height=0.38, fill_color=CREAM, fill_opacity=1, stroke_width=0, stroke_opacity=0)
        r1_bg.move_to([0, 0.85, 0])
        r1 = Text("No test file named", font="Prism", font_size=15, color=SLATE)
        r1.move_to([0, 0.85, 0])
        r2_bg = Rectangle(width=8.3, height=0.38, fill_color=CREAM, fill_opacity=1, stroke_width=0, stroke_opacity=0)
        r2_bg.move_to([0, 0.5, 0])
        r2 = Text("No exit code to check", font="Prism", font_size=15, color=SLATE)
        r2.move_to([0, 0.5, 0])
        r3_bg = Rectangle(width=8.3, height=0.38, fill_color=CREAM, fill_opacity=1, stroke_width=0, stroke_opacity=0)
        r3_bg.move_to([0, 0.15, 0])
        r3 = Text("Claude completes = subjective, not observable", font="Prism", font_size=15, color=SLATE)
        r3.move_to([0, 0.15, 0])
        self.play(GrowFromCenter(r1_bg), FadeIn(r1), GrowFromCenter(r2_bg), FadeIn(r2), GrowFromCenter(r3_bg), FadeIn(r3), run_time=0.4)
        fix_bg = Rectangle(width=9.0, height=0.75, fill_color=GOLD, fill_opacity=0.9,
                           stroke_color=INK, stroke_width=2)
        fix_bg.move_to([0, -0.65, 0])
        self.play(GrowFromCenter(fix_bg), run_time=0.35)
        fix_lbl = Text('Corrected: "pytest tests/test_models.py exits 0"', font="Prism", font_size=16, color=INK, weight=BOLD)
        fix_lbl.move_to([0, -0.65, 0])
        self.play(FadeIn(fix_lbl), run_time=0.3)
        ok_bg = Rectangle(width=3.5, height=0.6, fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0)
        ok_bg.move_to([0, -1.5, 0])
        self.play(GrowFromCenter(ok_bg), run_time=0.3)
        ok_lbl = Text("MACHINE-CHECKABLE", font="Prism", font_size=16, color=INK, weight=BOLD)
        ok_lbl.move_to([0, -1.5, 0])
        self.play(FadeIn(ok_lbl), run_time=0.25)
        self.wait(max(0, dur - 6.5))
