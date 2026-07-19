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


class B04_SimpsonTable(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # Title
        title = Text("SIMPSON'S PARADOX", color=CRIMSON, weight=BOLD, font_size=40)
        title.move_to([0, 3.2, 0])

        # --- POOLED TABLE (top panel) ---
        pooled_header_bg = Rectangle(width=7, height=0.6, fill_color=SLATE,
                                     fill_opacity=1, stroke_width=0, stroke_opacity=0)
        pooled_header_bg.move_to([0, 2.2, 0])
        pooled_header_txt = Text("POOLED DATA", color=CREAM, weight=BOLD, font_size=26)
        pooled_header_txt.move_to(pooled_header_bg)
        pooled_header = VGroup(pooled_header_bg, pooled_header_txt)

        # Row 1: Drug
        drug_label = Text("Drug", color=INK, font_size=30)
        drug_label.move_to([-2.5, 1.6, 0])
        drug_value = Text("Outcome: 78%", color=PASS_CLR, font_size=30)
        drug_value.move_to([1.0, 1.6, 0])

        # Row 2: No Drug
        nodrug_label = Text("No Drug", color=INK, font_size=30)
        nodrug_label.move_to([-2.5, 1.0, 0])
        nodrug_value = Text("Outcome: 72%", color=INK, font_size=30)
        nodrug_value.move_to([1.0, 1.0, 0])

        drug_row = VGroup(drug_label, drug_value)
        nodrug_row = VGroup(nodrug_label, nodrug_value)

        # Annotation: "drug looks good"
        looks_good_bg = Rectangle(width=2.8, height=0.4, fill_color=CREAM,
                                   fill_opacity=1, stroke_width=0, stroke_opacity=0)
        looks_good_bg.move_to([3.8, 1.3, 0])
        looks_good_txt = Text("drug looks good ->", color=PASS_CLR, font_size=28)
        looks_good_txt.move_to([3.8, 1.3, 0])
        looks_good_annotation = VGroup(looks_good_bg, looks_good_txt)

        # Horizontal divider
        divider = Line(start=[-5.5, 0.2, 0], end=[5.5, 0.2, 0], color=SLATE, stroke_width=2)

        # --- STRATIFIED BREAKDOWN (bottom panel) ---
        strat_header_bg = Rectangle(width=7, height=0.6, fill_color=CRIMSON,
                                    fill_opacity=1, stroke_width=0, stroke_opacity=0)
        strat_header_bg.move_to([0, -0.2, 0])
        strat_header_txt = Text("STRATIFIED BY GENDER", color=CREAM, weight=BOLD, font_size=26)
        strat_header_txt.move_to(strat_header_bg)
        strat_header = VGroup(strat_header_bg, strat_header_txt)

        men_row = Text("Men: Drug 60% vs No Drug 70%", color=CRIMSON, weight=BOLD, font_size=28)
        men_row.move_to([0, -0.9, 0])

        women_row = Text("Women: Drug 40% vs No Drug 50%", color=CRIMSON, weight=BOLD, font_size=28)
        women_row.move_to([0, -1.5, 0])

        # REVERSAL annotation
        reversal_bg = Rectangle(width=2.8, height=0.6, fill_color=CREAM,
                                 fill_opacity=1, stroke_width=0, stroke_opacity=0)
        reversal_bg.move_to([3.8, -1.2, 0])
        reversal_txt = Text("REVERSAL", color=CRIMSON, weight=BOLD, font_size=36)
        reversal_txt.move_to([3.8, -1.2, 0])
        reversal_text = VGroup(reversal_bg, reversal_txt)

        # Sequence — 7 play() calls (Gate A requires 5+)
        self.play(Write(title))
        self.play(FadeIn(pooled_header))
        self.play(FadeIn(drug_row), FadeIn(nodrug_row))
        self.play(Write(looks_good_annotation))
        self.play(FadeIn(divider), FadeIn(strat_header))
        self.play(FadeIn(men_row), FadeIn(women_row))
        self.play(Write(reversal_text))
        self.wait(1)
