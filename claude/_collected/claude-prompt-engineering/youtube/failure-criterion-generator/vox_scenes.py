import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
PASS_CLR = "#2A7A2A"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_FailureCriteria(Scene):
    def construct(self):
        # state 1: title
        title_bg = Rectangle(width=10.0, height=0.65, fill_color=CREAM, fill_opacity=1.0,
                              stroke_width=0, stroke_opacity=0)
        title_bg.move_to([0, 3.2, 0])
        title = Text("Failure Criterion Checklist", font_size=34, color=INK)
        title.move_to([0, 3.2, 0])
        self.play(FadeIn(VGroup(title_bg, title)))
        self.wait(0.3)

        # state 2: prompt label
        plbl_bg = Rectangle(width=10.5, height=0.58, fill_color=GOLD, fill_opacity=1.0,
                             stroke_width=0, stroke_opacity=0)
        plbl_bg.move_to([0, 2.4, 0])
        plbl_txt = Text("PROMPT: generate failure criteria for a data analysis task",
                        font_size=17, color=INK)
        plbl_txt.move_to([0, 2.4, 0])
        self.play(FadeIn(VGroup(plbl_bg, plbl_txt)), run_time=0.6)
        self.wait(0.3)

        items = [
            ("1. Cites a source that does not exist",       CRIMSON),
            ("2. Makes prediction beyond data scope",       CRIMSON),
            ("3. Omits confidence intervals",               CRIMSON),
            ("4. Uses undefined technical jargon",          CRIMSON),
            ("5. Draws causal inference from correlation",  CRIMSON),
            ("6. Fails to bound conclusion to sample size", PASS_CLR),
        ]

        y_top = 1.55
        gap   = 0.70

        # state 3: items 1–2
        grp_a = VGroup()
        for j in range(2):
            y = y_top - j * gap
            row_bg = Rectangle(width=11.0, height=0.58, fill_color=CREAM, fill_opacity=1.0,
                                stroke_width=0, stroke_opacity=0)
            row_bg.move_to([0, y, 0])
            txt = Text(items[j][0], font_size=18, color=items[j][1])
            txt.move_to([0, y, 0])
            grp_a.add(row_bg, txt)
        self.play(FadeIn(grp_a), run_time=0.65)
        self.wait(0.25)

        # state 4: items 3–4
        grp_b = VGroup()
        for j in range(2, 4):
            y = y_top - j * gap
            row_bg = Rectangle(width=11.0, height=0.58, fill_color=CREAM, fill_opacity=1.0,
                                stroke_width=0, stroke_opacity=0)
            row_bg.move_to([0, y, 0])
            txt = Text(items[j][0], font_size=18, color=items[j][1])
            txt.move_to([0, y, 0])
            grp_b.add(row_bg, txt)
        self.play(FadeIn(grp_b), run_time=0.65)
        self.wait(0.25)

        # state 5: items 5–6
        grp_c = VGroup()
        for j in range(4, 6):
            y = y_top - j * gap
            row_bg = Rectangle(width=11.0, height=0.58, fill_color=CREAM, fill_opacity=1.0,
                                stroke_width=0, stroke_opacity=0)
            row_bg.move_to([0, y, 0])
            txt = Text(items[j][0], font_size=18, color=items[j][1])
            txt.move_to([0, y, 0])
            grp_c.add(row_bg, txt)
        self.play(FadeIn(grp_c), run_time=0.65)
        self.wait(0.25)

        # state 6: summary count
        y_sum = y_top - 6 * gap - 0.25
        count_bg = Rectangle(width=10.0, height=0.60, fill_color=CREAM, fill_opacity=1.0,
                              stroke_width=0, stroke_opacity=0)
        count_bg.move_to([0, y_sum, 0])
        count_txt = Text("5 failure criteria identified — add as negative constraints to the prompt",
                         font_size=17, color=CRIMSON)
        count_txt.move_to([0, y_sum, 0])
        self.play(FadeIn(VGroup(count_bg, count_txt)), run_time=0.7)
        self.wait(0.5)

        # state 7: crimson rule
        rule = Line([-5.0, -3.3, 0], [-2.0, -3.3, 0], stroke_color=CRIMSON, stroke_width=2)
        self.play(FadeIn(rule), run_time=0.4)
        self.wait(0.8)
