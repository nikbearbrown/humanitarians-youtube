import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
PASS_CLR="#2A7A2A"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

# Row data: (rung_str, type_str, result_str, color)
_ROWS = [
    ("Rung 1", "Observational", "V PASS", SLATE),
    ("Rung 1", "Observational", "V PASS", SLATE),
    ("Rung 1", "Observational", "V PASS", SLATE),
    ("Rung 2", "Interventional", "V PASS", "#E06400"),
    ("Rung 2", "Interventional", "V PASS", "#E06400"),
    ("Rung 2", "Interventional", "X FAIL", "#E06400"),
    ("Rung 2", "Interventional", "X FAIL", "#E06400"),
    ("Rung 3", "Counterfactual", "X FAIL", CRIMSON),
    ("Rung 3", "Counterfactual", "X FAIL", CRIMSON),
    ("Rung 3", "Counterfactual", "X FAIL", CRIMSON),
]


class B04_CausalReportCard(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # Title
        title = Text("LLM CAUSAL BENCHMARK", color=INK, weight=BOLD, font_size=36)
        title.move_to([0, 3.2, 0])

        # Header row
        header_bg = Rectangle(width=11.2, height=0.5, fill_color=INK,
                               fill_opacity=1, stroke_width=0, stroke_opacity=0)
        header_bg.move_to([0, 2.6, 0])
        header_txt = Text("RUNG  |  QUESTION TYPE  |  RESULT", color=CREAM,
                          font_size=22, weight=BOLD)
        header_txt.move_to(header_bg)
        table_header = VGroup(header_bg, header_txt)

        # Build rows
        row_height = 0.46
        start_y = 2.3
        all_row_groups = []

        for i, (rung_s, type_s, result_s, clr) in enumerate(_ROWS):
            y = start_y - i * row_height
            row_bg = Rectangle(width=11.2, height=row_height - 0.02,
                                fill_color=CREAM, fill_opacity=1,
                                stroke_width=0, stroke_opacity=0)
            row_bg.move_to([0, y, 0])
            sep_line = Line(start=[-5.5, y - row_height / 2 + 0.01, 0],
                            end=[5.5, y - row_height / 2 + 0.01, 0],
                            color=SLATE, stroke_width=0.5)
            row_txt = Text(f"{rung_s}  |  {type_s}  |  {result_s}",
                           color=clr, font_size=22)
            row_txt.move_to([0, y, 0])
            all_row_groups.append(VGroup(row_bg, sep_line, row_txt))

        rung1_rows = all_row_groups[0:3]
        rung2_rows = all_row_groups[3:7]
        rung3_rows = all_row_groups[7:10]

        # Summary line
        summary_bg = Rectangle(width=7.0, height=0.4, fill_color=CREAM,
                                fill_opacity=1, stroke_width=0, stroke_opacity=0)
        summary_bg.move_to([0, -3.0, 0])
        summary_txt = Text("Rung 1: 100%  |  Rung 2: 50%  |  Rung 3: 0%",
                           color=INK, font_size=26)
        summary_txt.move_to([0, -3.0, 0])
        summary_line = VGroup(summary_bg, summary_txt)

        # Verdict
        verdict_bg = Rectangle(width=6.5, height=0.4, fill_color=CREAM,
                                fill_opacity=1, stroke_width=0, stroke_opacity=0)
        verdict_bg.move_to([0, -3.35, 0])
        verdict_txt = Text("Rung 3 failures: structural reasoning gap",
                           color=CRIMSON, font_size=24)
        verdict_txt.move_to([0, -3.35, 0])
        verdict = VGroup(verdict_bg, verdict_txt)

        # Sequence — 7 play() calls
        self.play(Write(title))
        self.play(FadeIn(table_header))
        self.play(*[FadeIn(r) for r in rung1_rows])
        self.play(*[FadeIn(r) for r in rung2_rows])
        self.play(*[FadeIn(r) for r in rung3_rows])
        self.play(Write(summary_line))
        self.play(Write(verdict))
        self.wait(1)
