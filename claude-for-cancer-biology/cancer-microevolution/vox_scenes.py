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


class B04_MultihitTimeline(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # Title
        # ------------------------------------------------------------------
        title = Text(
            "Cancer as Microevolution: Decades of Selection",
            font_size=26, color=INK, weight=BOLD
        ).move_to((0, 3.2, 0))

        # ------------------------------------------------------------------
        # Main timeline line: x=-5.5 to 5.5, y=-0.3
        # ------------------------------------------------------------------
        timeline_line = Line((-5.5, -0.3, 0), (5.5, -0.3, 0),
                             color=INK, stroke_width=3)

        # ------------------------------------------------------------------
        # Event 1 — Year 0, ABOVE; label box shifted right (centered x=-4.0)
        # ------------------------------------------------------------------
        e1_dot = Circle(radius=0.18, fill_color=SLATE, fill_opacity=1,
                        stroke_width=0, stroke_opacity=0).move_to((-5.0, -0.3, 0))
        e1_vline = Line((-5.0, -0.3, 0), (-5.0, 0.4, 0), color=SLATE, stroke_width=1.5)
        e1_box = Rectangle(width=2.4, height=0.9, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to((-4.0, 1.1, 0))
        e1_gene = Text("APC MUTATION", font_size=20, color=INK, weight=BOLD
                       ).move_to((-4.0, 1.32, 0))
        e1_stage = Text("Normal->polyp", font_size=18, color=INK
                        ).move_to((-4.0, 0.88, 0))
        e1_tick_bg = Rectangle(width=0.7, height=0.3, fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0).move_to((-5.0, -0.65, 0))
        e1_tick = Text("Yr 0", font_size=17, color=SLATE).move_to((-5.0, -0.65, 0))
        event_1 = VGroup(e1_dot, e1_vline, e1_box, e1_gene, e1_stage, e1_tick_bg, e1_tick)

        # ------------------------------------------------------------------
        # Event 2 — Year 7, BELOW; x=-2.2
        # ------------------------------------------------------------------
        e2_dot = Circle(radius=0.18, fill_color=SLATE, fill_opacity=1,
                        stroke_width=0, stroke_opacity=0).move_to((-2.2, -0.3, 0))
        e2_vline = Line((-2.2, -0.3, 0), (-2.2, -1.0, 0), color=SLATE, stroke_width=1.5)
        e2_box = Rectangle(width=2.4, height=0.9, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to((-2.2, -1.9, 0))
        e2_gene = Text("KRAS MUTATION", font_size=20, color=INK, weight=BOLD
                       ).move_to((-2.2, -1.68, 0))
        e2_stage = Text("Adenoma", font_size=18, color=INK
                        ).move_to((-2.2, -2.12, 0))
        e2_tick_bg = Rectangle(width=0.7, height=0.3, fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0).move_to((-2.2, 0.05, 0))
        e2_tick = Text("Yr 7", font_size=17, color=SLATE).move_to((-2.2, 0.05, 0))
        event_2 = VGroup(e2_dot, e2_vline, e2_box, e2_gene, e2_stage, e2_tick_bg, e2_tick)

        # ------------------------------------------------------------------
        # Event 3 — Year 14, ABOVE; x=0.6
        # ------------------------------------------------------------------
        e3_dot = Circle(radius=0.18, fill_color=SLATE, fill_opacity=1,
                        stroke_width=0, stroke_opacity=0).move_to((0.6, -0.3, 0))
        e3_vline = Line((0.6, -0.3, 0), (0.6, 0.4, 0), color=SLATE, stroke_width=1.5)
        e3_box = Rectangle(width=2.4, height=0.9, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to((0.6, 1.1, 0))
        e3_gene = Text("SMAD4 / p53", font_size=20, color=INK, weight=BOLD
                       ).move_to((0.6, 1.32, 0))
        e3_stage = Text("Adv. adenoma", font_size=18, color=INK
                        ).move_to((0.6, 0.88, 0))
        e3_tick_bg = Rectangle(width=0.82, height=0.3, fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0).move_to((0.6, -0.65, 0))
        e3_tick = Text("Yr 14", font_size=17, color=SLATE).move_to((0.6, -0.65, 0))
        event_3 = VGroup(e3_dot, e3_vline, e3_box, e3_gene, e3_stage, e3_tick_bg, e3_tick)

        # ------------------------------------------------------------------
        # Event 4 — Year 20, BELOW; x=3.0
        # ------------------------------------------------------------------
        e4_dot = Circle(radius=0.18, fill_color=SLATE, fill_opacity=1,
                        stroke_width=0, stroke_opacity=0).move_to((3.0, -0.3, 0))
        e4_vline = Line((3.0, -0.3, 0), (3.0, -1.0, 0), color=SLATE, stroke_width=1.5)
        e4_box = Rectangle(width=2.4, height=0.9, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to((3.0, -1.9, 0))
        e4_gene = Text("TP53 LOSS", font_size=20, color=INK, weight=BOLD
                       ).move_to((3.0, -1.68, 0))
        e4_stage = Text("Carcinoma in situ", font_size=18, color=INK
                        ).move_to((3.0, -2.12, 0))
        e4_tick_bg = Rectangle(width=0.82, height=0.3, fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0).move_to((3.0, 0.05, 0))
        e4_tick = Text("Yr 20", font_size=17, color=SLATE).move_to((3.0, 0.05, 0))
        event_4 = VGroup(e4_dot, e4_vline, e4_box, e4_gene, e4_stage, e4_tick_bg, e4_tick)

        # ------------------------------------------------------------------
        # Event 5 — Year 25, ABOVE; label box shifted left (centered x=4.0)
        # CRIMSON dot and box to mark arrival
        # ------------------------------------------------------------------
        e5_dot = Circle(radius=0.18, fill_color=CRIMSON, fill_opacity=1,
                        stroke_width=0, stroke_opacity=0).move_to((5.0, -0.3, 0))
        e5_vline = Line((5.0, -0.3, 0), (5.0, 0.4, 0), color=SLATE, stroke_width=1.5)
        e5_box = Rectangle(width=2.4, height=0.9, fill_color=CRIMSON, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to((4.0, 1.1, 0))
        e5_gene = Text("INVASION", font_size=20, color=CREAM, weight=BOLD
                       ).move_to(e5_box)
        e5_stage = Text("Yr 25 detection", font_size=18, color=INK
                        ).move_to((4.0, 0.88, 0))
        e5_tick_bg = Rectangle(width=0.82, height=0.3, fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0).move_to((5.0, -0.65, 0))
        e5_tick = Text("Yr 25", font_size=17, color=SLATE).move_to((5.0, -0.65, 0))
        event_5 = VGroup(e5_dot, e5_vline, e5_box, e5_gene, e5_stage, e5_tick_bg, e5_tick)

        # ------------------------------------------------------------------
        # Knudson annotation at y=2.5 — CREAM bg, SLATE text
        # ------------------------------------------------------------------
        knudson_bg = Rectangle(
            width=10.5, height=0.38,
            fill_color=CREAM, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, 2.5, 0))
        knudson_txt = Text(
            "Knudson 1971: two-hit model -- both alleles of a tumor suppressor must be lost",
            font_size=19, color=SLATE
        ).move_to((0, 2.5, 0))
        knudson_annotation = VGroup(knudson_bg, knudson_txt)

        # ------------------------------------------------------------------
        # Li-Fraumeni callout at y=-2.9 — CREAM bg, CRIMSON text
        # ------------------------------------------------------------------
        lf_bg = Rectangle(
            width=10.0, height=0.36,
            fill_color=CREAM, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, -2.9, 0))
        lf_txt = Text(
            "Li-Fraumeni syndrome (p53 germline): one hit done -> onset 10-15 yr earlier",
            font_size=19, color=CRIMSON
        ).move_to((0, -2.9, 0))
        li_fraumeni_callout = VGroup(lf_bg, lf_txt)

        # ------------------------------------------------------------------
        # Animation sequence (8 distinct play() calls — Gate A: 5+ OK)
        # ------------------------------------------------------------------
        self.play(Write(title))
        self.play(Create(timeline_line))
        self.play(FadeIn(event_1))
        self.play(FadeIn(event_2))
        self.play(FadeIn(event_3))
        self.play(FadeIn(event_4))
        self.play(FadeIn(event_5))
        self.play(FadeIn(knudson_annotation), FadeIn(li_fraumeni_callout))
        self.wait(1)
