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


class B04_CausalDiagnosis(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)
        title = Text("Causal Diagnosis: Churn Model Features", font="Prism", font_size=22, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)
        hdrs = ["Feature", "P(churn|X)", "P(churn|do(X))", "Verdict"]
        x_pos = [-3.8, -1.2, 1.4, 4.0]
        hdr_line = Line(start=[-5.5, 2.4, 0], end=[5.5, 2.4, 0], color=INK, stroke_width=2)
        self.play(Create(hdr_line), run_time=0.3)
        for h, xp in zip(hdrs, x_pos):
            lbl = Text(h, font="Prism", font_size=15, color=SLATE, weight=BOLD)
            lbl.move_to([xp, 2.7, 0])
            self.play(FadeIn(lbl), run_time=0.15)
        data = [
            ("login_freq",     "0.42", "unknown", "confound",  GOLD),
            ("support_tickets","0.58", "causal",  "safe",      CREAM),
            ("plan_price",     "0.31", "unknown", "overreach", "#FFF0F0"),
            ("last_login_days","0.71", "unknown", "confound",  GOLD),
            ("nps_score",      "0.65", "unknown", "overreach", "#FFF0F0"),
        ]
        y_top = 1.9
        for i, (feat, p_obs, p_do, verdict, bg) in enumerate(data):
            y = y_top - i * 0.72
            row_bg = Rectangle(width=11.0, height=0.62, fill_color=bg, fill_opacity=0.6,
                               stroke_color=SLATE, stroke_width=0.5)
            row_bg.move_to([0, y, 0])
            self.play(GrowFromCenter(row_bg), run_time=0.2)
            feat_lbl = Text(feat, font="Prism", font_size=14, color=INK)
            feat_lbl.move_to([x_pos[0], y, 0])
            pobs_lbl = Text(p_obs, font="Prism", font_size=14, color=INK)
            pobs_lbl.move_to([x_pos[1], y, 0])
            pdo_lbl = Text(p_do, font="Prism", font_size=14, color=SLATE)
            pdo_lbl.move_to([x_pos[2], y, 0])
            clr = CRIMSON if verdict != "safe" else INK
            vrd_lbl = Text(verdict, font="Prism", font_size=14, color=clr, weight=BOLD if verdict != "safe" else "NORMAL")
            vrd_lbl.move_to([x_pos[3], y, 0])
            self.play(FadeIn(feat_lbl), FadeIn(pobs_lbl), FadeIn(pdo_lbl), FadeIn(vrd_lbl), run_time=0.3)
        self.wait(max(0, dur - 5.0))


class B06_InterventionColumn(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("What Intervention Tests Each Claim?", font="Prism", font_size=22, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)
        hdrs = ["Feature", "Verdict", "Intervention to test"]
        x_pos = [-4.0, -1.2, 2.0]
        hdr_line = Line(start=[-5.5, 2.4, 0], end=[5.5, 2.4, 0], color=INK, stroke_width=2)
        self.play(Create(hdr_line), run_time=0.3)
        for h, xp in zip(hdrs, x_pos):
            lbl = Text(h, font="Prism", font_size=15, color=SLATE, weight=BOLD)
            lbl.move_to([xp, 2.7, 0])
            self.play(FadeIn(lbl), run_time=0.15)
        data = [
            ("support_tickets", "safe",      "randomize contact rate",   CREAM),
            ("plan_price",      "overreach", "run price A/B experiment", GOLD),
            ("nps_score",       "overreach", "send survey intervention", GOLD),
            ("login_freq",      "confound",  "nudge in-app prompts",     "#FFF0F0"),
            ("last_login_days", "confound",  "re-engagement email blast","#FFF0F0"),
        ]
        y_top = 1.9
        for i, (feat, verdict, interv, bg) in enumerate(data):
            y = y_top - i * 0.72
            row_bg = Rectangle(width=11.0, height=0.62, fill_color=bg, fill_opacity=0.6,
                               stroke_color=SLATE, stroke_width=0.5)
            row_bg.move_to([0, y, 0])
            self.play(GrowFromCenter(row_bg), run_time=0.2)
            feat_lbl = Text(feat, font="Prism", font_size=14, color=INK)
            feat_lbl.move_to([x_pos[0], y, 0])
            clr = CRIMSON if verdict != "safe" else INK
            vrd_lbl = Text(verdict, font="Prism", font_size=13, color=clr)
            vrd_lbl.move_to([x_pos[1], y, 0])
            int_lbl = Text(interv, font="Prism", font_size=13, color=INK)
            int_lbl.move_to([x_pos[2], y, 0])
            self.play(FadeIn(feat_lbl), FadeIn(vrd_lbl), FadeIn(int_lbl), run_time=0.3)
        summary_box = Rectangle(width=7.0, height=0.6, fill_color=CREAM,
                                fill_opacity=1, stroke_color=CRIMSON, stroke_width=2)
        summary_box.move_to([0, -1.8, 0])
        self.play(GrowFromCenter(summary_box), run_time=0.35)
        sum_lbl = Text("Each row is a testable do-operation", font="Prism", font_size=16, color=CRIMSON, weight=BOLD)
        sum_lbl.move_to([0, -1.8, 0])
        self.play(FadeIn(sum_lbl), run_time=0.3)
        self.wait(max(0, dur - 5.5))
