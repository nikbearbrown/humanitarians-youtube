import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
WARN_CLR = "#8A6A00"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_DirectoryTree(Scene):
    def construct(self):
        # state 1: title
        title_bg = Rectangle(width=10.0, height=0.65, fill_color=CREAM, fill_opacity=1.0,
                              stroke_width=0, stroke_opacity=0)
        title_bg.move_to([0, 3.2, 0])
        title = Text("Agent Folder Reliability Audit", font_size=32, color=INK)
        title.move_to([0, 3.2, 0])
        self.play(FadeIn(VGroup(title_bg, title)))
        self.wait(0.3)

        # state 2: column headers + separator
        hdr_y = 2.35
        hdr_a_bg = Rectangle(width=5.5, height=0.48, fill_color=CREAM, fill_opacity=1.0,
                              stroke_width=0, stroke_opacity=0)
        hdr_a_bg.move_to([-2.5, hdr_y, 0])
        hdr_a = Text("PATH", font_size=17, color=SLATE)
        hdr_a.move_to([-2.5, hdr_y, 0])
        hdr_b_bg = Rectangle(width=2.0, height=0.48, fill_color=CREAM, fill_opacity=1.0,
                              stroke_width=0, stroke_opacity=0)
        hdr_b_bg.move_to([4.0, hdr_y, 0])
        hdr_b = Text("RISK", font_size=17, color=SLATE)
        hdr_b.move_to([4.0, hdr_y, 0])
        sep_hdr = Line([-5.5, hdr_y - 0.30, 0], [5.5, hdr_y - 0.30, 0],
                       stroke_color=INK, stroke_width=1.0)
        self.play(FadeIn(VGroup(hdr_a_bg, hdr_a, hdr_b_bg, hdr_b, sep_hdr)), run_time=0.5)
        self.wait(0.2)

        entries = [
            ("project/",        None,   INK),
            ("├─ src/",         None,   INK),
            ("├─ data/",        None,   INK),
            ("├─ config.py",    "HIGH", CRIMSON),
            ("├─ secrets.env",  "HIGH", CRIMSON),
            ("├─ temp/",        "MED",  WARN_CLR),
            ("└─ __pycache__/", "HIGH", CRIMSON),
        ]
        y_top = 1.75
        gap   = 0.60

        # state 3: entries 1–3 (no risk)
        grp_a = VGroup()
        for j in range(3):
            y = y_top - j * gap
            row_bg = Rectangle(width=9.5, height=0.52, fill_color=CREAM, fill_opacity=1.0,
                                stroke_width=0, stroke_opacity=0)
            row_bg.move_to([0, y, 0])
            path_txt = Text(entries[j][0], font_size=17, color=INK)
            path_txt.move_to([-2.5, y, 0])
            grp_a.add(row_bg, path_txt)
        self.play(FadeIn(grp_a), run_time=0.6)
        self.wait(0.2)

        # state 4: entries 4–7 (with risk badges)
        grp_b = VGroup()
        for j in range(3, 7):
            y = y_top - j * gap
            row_bg = Rectangle(width=9.5, height=0.52, fill_color=CREAM, fill_opacity=1.0,
                                stroke_width=0, stroke_opacity=0)
            row_bg.move_to([0, y, 0])
            path_txt = Text(entries[j][0], font_size=17, color=entries[j][2])
            path_txt.move_to([-2.5, y, 0])
            badge_bg = Rectangle(width=1.0, height=0.38, fill_color=CREAM, fill_opacity=1.0,
                                  stroke_color=entries[j][2], stroke_width=1.5)
            badge_bg.move_to([4.0, y, 0])
            badge_txt = Text(entries[j][1], font_size=13, color=entries[j][2])
            badge_txt.move_to([4.0, y, 0])
            grp_b.add(row_bg, path_txt, badge_bg, badge_txt)
        self.play(FadeIn(grp_b), run_time=0.65)
        self.wait(0.3)

        # state 5: separator
        y_sep = y_top - 7 * gap - 0.05
        sep = Line([-5.5, y_sep, 0], [5.5, y_sep, 0], stroke_color=INK, stroke_width=1.0)
        self.play(FadeIn(sep), run_time=0.35)
        self.wait(0.1)

        # state 6: summary
        y_sum = y_sep - 0.46
        sum_bg = Rectangle(width=9.5, height=0.52, fill_color=CREAM, fill_opacity=1.0,
                            stroke_width=0, stroke_opacity=0)
        sum_bg.move_to([0, y_sum, 0])
        sum_txt = Text("3 HIGH · 1 MED risk — restructure before agent use",
                       font_size=17, color=CRIMSON)
        sum_txt.move_to([0, y_sum, 0])
        self.play(FadeIn(VGroup(sum_bg, sum_txt)), run_time=0.55)
        self.wait(0.3)

        # state 7: crimson rule
        rule = Line([-5.0, -3.3, 0], [-2.0, -3.3, 0], stroke_color=CRIMSON, stroke_width=2)
        self.play(FadeIn(rule), run_time=0.4)
        self.wait(0.8)
