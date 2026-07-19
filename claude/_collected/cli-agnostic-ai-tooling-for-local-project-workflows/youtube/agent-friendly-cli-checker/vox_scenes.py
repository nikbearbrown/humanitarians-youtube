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


class B04_CLIChecklist(Scene):
    def construct(self):
        # state 1: title
        title_bg = Rectangle(width=10.0, height=0.65, fill_color=CREAM, fill_opacity=1.0,
                              stroke_width=0, stroke_opacity=0)
        title_bg.move_to([0, 3.2, 0])
        title = Text("Agent-Friendly CLI Design Checker", font_size=30, color=INK)
        title.move_to([0, 3.2, 0])
        self.play(FadeIn(VGroup(title_bg, title)))
        self.wait(0.3)

        rules = [
            ("1. Machine-readable output (JSON or TSV)", "PASS", PASS_CLR),
            ("2. Non-zero exit code on error",           "PASS", PASS_CLR),
            ("3. No ANSI color codes in piped output",   "FAIL", CRIMSON),
            ("4. Deterministic output order",            "PASS", PASS_CLR),
            ("5. Progress to stderr, data to stdout",    "FAIL", CRIMSON),
            ("6. --dry-run flag available",              "FAIL", CRIMSON),
            ("7. --output-format flag available",        "PASS", PASS_CLR),
        ]
        y_top = 2.1
        gap   = 0.65

        # state 2: rules 1–2
        grp_a = VGroup()
        for j in range(2):
            y = y_top - j * gap
            rule_bg = Rectangle(width=11.0, height=0.58, fill_color=CREAM, fill_opacity=1.0,
                                stroke_width=0, stroke_opacity=0)
            rule_bg.move_to([0, y, 0])
            rule_txt = Text(rules[j][0], font_size=17, color=rules[j][2])
            rule_txt.move_to([-1.0, y, 0])
            badge_bg = Rectangle(width=1.2, height=0.42, fill_color=CREAM, fill_opacity=1.0,
                                  stroke_color=rules[j][2], stroke_width=1.5)
            badge_bg.move_to([4.8, y, 0])
            badge_txt = Text(rules[j][1], font_size=14, color=rules[j][2])
            badge_txt.move_to([4.8, y, 0])
            grp_a.add(rule_bg, rule_txt, badge_bg, badge_txt)
        self.play(FadeIn(grp_a), run_time=0.65)
        self.wait(0.2)

        # state 3: rules 3–4
        grp_b = VGroup()
        for j in range(2, 4):
            y = y_top - j * gap
            rule_bg = Rectangle(width=11.0, height=0.58, fill_color=CREAM, fill_opacity=1.0,
                                stroke_width=0, stroke_opacity=0)
            rule_bg.move_to([0, y, 0])
            rule_txt = Text(rules[j][0], font_size=17, color=rules[j][2])
            rule_txt.move_to([-1.0, y, 0])
            badge_bg = Rectangle(width=1.2, height=0.42, fill_color=CREAM, fill_opacity=1.0,
                                  stroke_color=rules[j][2], stroke_width=1.5)
            badge_bg.move_to([4.8, y, 0])
            badge_txt = Text(rules[j][1], font_size=14, color=rules[j][2])
            badge_txt.move_to([4.8, y, 0])
            grp_b.add(rule_bg, rule_txt, badge_bg, badge_txt)
        self.play(FadeIn(grp_b), run_time=0.65)
        self.wait(0.2)

        # state 4: rules 5–7
        grp_c = VGroup()
        for j in range(4, 7):
            y = y_top - j * gap
            rule_bg = Rectangle(width=11.0, height=0.58, fill_color=CREAM, fill_opacity=1.0,
                                stroke_width=0, stroke_opacity=0)
            rule_bg.move_to([0, y, 0])
            rule_txt = Text(rules[j][0], font_size=17, color=rules[j][2])
            rule_txt.move_to([-1.0, y, 0])
            badge_bg = Rectangle(width=1.2, height=0.42, fill_color=CREAM, fill_opacity=1.0,
                                  stroke_color=rules[j][2], stroke_width=1.5)
            badge_bg.move_to([4.8, y, 0])
            badge_txt = Text(rules[j][1], font_size=14, color=rules[j][2])
            badge_txt.move_to([4.8, y, 0])
            grp_c.add(rule_bg, rule_txt, badge_bg, badge_txt)
        self.play(FadeIn(grp_c), run_time=0.65)
        self.wait(0.2)

        # state 5: separator
        y_sep = y_top - 7 * gap - 0.1
        sep = Line([-5.5, y_sep, 0], [5.5, y_sep, 0], stroke_color=INK, stroke_width=1.0)
        self.play(FadeIn(sep), run_time=0.35)
        self.wait(0.1)

        # state 6: score summary
        y_sum = y_sep - 0.44
        score_bg = Rectangle(width=9.5, height=0.52, fill_color=CREAM, fill_opacity=1.0,
                              stroke_width=0, stroke_opacity=0)
        score_bg.move_to([0, y_sum, 0])
        score_txt = Text("4 / 7 PASS — add --dry-run, stderr routing, --output-format",
                         font_size=16, color=CRIMSON)
        score_txt.move_to([0, y_sum, 0])
        self.play(FadeIn(VGroup(score_bg, score_txt)), run_time=0.55)
        self.wait(0.3)

        # state 7: crimson rule
        rule_line = Line([-5.0, -3.3, 0], [-2.0, -3.3, 0], stroke_color=CRIMSON, stroke_width=2)
        self.play(FadeIn(rule_line), run_time=0.4)
        self.wait(0.8)
