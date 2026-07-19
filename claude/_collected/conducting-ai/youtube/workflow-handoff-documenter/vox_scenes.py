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


class B04_PipelineComparison(Scene):
    def construct(self):
        title = Text("WORKFLOW HANDOFF AUDIT", color=INK, font_size=36, weight=BOLD).move_to([0, 3.2, 0])

        # Divider
        divider = Line((0.0, -2.5, 0), (0.0, 2.8, 0), color=SLATE, stroke_width=1, stroke_opacity=0.4)

        # Labels
        broken_label_bg = Rectangle(width=2.6, height=0.38, fill_color=CREAM, fill_opacity=1,
                                   stroke_width=0, stroke_opacity=0).move_to([-3.0, 2.5, 0])
        broken_label = Text("BROKEN PIPELINE", color=CRIMSON, font_size=24, weight=BOLD).move_to([-3.0, 2.5, 0])

        repaired_label_bg = Rectangle(width=2.9, height=0.38, fill_color=CREAM, fill_opacity=1,
                                     stroke_width=0, stroke_opacity=0).move_to([3.2, 2.5, 0])
        repaired_label = Text("REPAIRED PIPELINE", color=PASS_CLR, font_size=24, weight=BOLD).move_to([3.2, 2.5, 0])

        broken_label_grp = VGroup(broken_label_bg, broken_label)
        repaired_label_grp = VGroup(repaired_label_bg, repaired_label)

        # --- BROKEN PIPELINE --- (nodes at x=-4.5, -3.0, -1.5; y=0.8)
        def make_node(x, y, label_str, lbl_below):
            circ = Circle(radius=0.35, color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2)
            circ.move_to([x, y, 0])
            lbl = Text(label_str, color=INK, font_size=16).move_to([x, y, 0])
            below_bg = Rectangle(width=1.2, height=0.32, fill_color=CREAM, fill_opacity=1,
                                stroke_width=0, stroke_opacity=0).move_to([x, y-0.65, 0])
            below = Text(lbl_below, color=INK, font_size=16).move_to([x, y-0.65, 0])
            return VGroup(circ, lbl, below_bg, below)

        bn1 = make_node(-4.5, 0.8, "LLM", "$4.2B")
        bn2 = make_node(-3.0, 0.8, "JSON", "JSON")
        bn3 = make_node(-1.5, 0.8, "Slide", "Slide")
        broken_nodes = VGroup(bn1, bn2, bn3)

        # Broken arrows (red — no verification)
        b_arr1 = Arrow((-4.1, 0.8, 0), (-3.4, 0.8, 0), color=CRIMSON, stroke_width=2)
        b_arr2 = Arrow((-2.6, 0.8, 0), (-1.9, 0.8, 0), color=CRIMSON, stroke_width=2)
        broken_arrows = VGroup(b_arr1, b_arr2)

        # "NO GATE" labels above seams
        ng1_bg = Rectangle(width=1.0, height=0.32, fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0).move_to([-3.75, 1.2, 0])
        ng1 = Text("NO GATE", color=CRIMSON, font_size=18).move_to([-3.75, 1.2, 0])
        ng2_bg = Rectangle(width=1.0, height=0.32, fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0).move_to([-2.25, 1.2, 0])
        ng2 = Text("NO GATE", color=CRIMSON, font_size=18).move_to([-2.25, 1.2, 0])
        broken_no_gate_labels = VGroup(ng1_bg, ng1, ng2_bg, ng2)

        # --- REPAIRED PIPELINE --- (nodes at 1.5, 3.5, 5.5; gates at 2.5, 4.5; y=0.8)
        rn1 = make_node(1.5, 0.8, "LLM", "LLM")
        rn2 = make_node(3.5, 0.8, "JSON", "JSON")
        rn3 = make_node(5.5, 0.8, "Slide", "Slide")
        repaired_nodes = VGroup(rn1, rn2, rn3)

        # Gate squares
        gate1 = Rectangle(width=0.4, height=0.4, fill_color=PASS_CLR, fill_opacity=1,
                         stroke_width=0, stroke_opacity=0).move_to([2.5, 0.8, 0])
        gate2 = Rectangle(width=0.4, height=0.4, fill_color=PASS_CLR, fill_opacity=1,
                         stroke_width=0, stroke_opacity=0).move_to([4.5, 0.8, 0])
        gate_squares = VGroup(gate1, gate2)

        # Repaired arrows (green)
        r_arr1 = Arrow((1.9, 0.8, 0), (2.3, 0.8, 0), color=PASS_CLR, stroke_width=2)
        r_arr2 = Arrow((2.7, 0.8, 0), (3.1, 0.8, 0), color=PASS_CLR, stroke_width=2)
        r_arr3 = Arrow((3.9, 0.8, 0), (4.3, 0.8, 0), color=PASS_CLR, stroke_width=2)
        r_arr4 = Arrow((4.7, 0.8, 0), (5.1, 0.8, 0), color=PASS_CLR, stroke_width=2)
        repaired_arrows = VGroup(r_arr1, r_arr2, r_arr3, r_arr4)

        # "GATE" labels above gates
        g1_bg = Rectangle(width=0.6, height=0.32, fill_color=CREAM, fill_opacity=1,
                         stroke_width=0, stroke_opacity=0).move_to([2.5, 1.3, 0])
        g1 = Text("GATE", color=PASS_CLR, font_size=18).move_to([2.5, 1.3, 0])
        g2_bg = Rectangle(width=0.6, height=0.32, fill_color=CREAM, fill_opacity=1,
                         stroke_width=0, stroke_opacity=0).move_to([4.5, 1.3, 0])
        g2 = Text("GATE", color=PASS_CLR, font_size=18).move_to([4.5, 1.3, 0])
        repaired_gate_labels = VGroup(g1_bg, g1, g2_bg, g2)

        # Audit rows below pipelines (y from -0.5 to -2.5)
        # Left broken row
        row_broken_bg = Rectangle(width=5.5, height=0.65, fill_color=CREAM, fill_opacity=1,
                                 stroke_width=0, stroke_opacity=0).move_to([-2.8, -1.1, 0])
        row_broken_txt = Text("LLM->JSON | gpt-4o | model agreed | CORRELATED",
                             color=CRIMSON, font_size=17).move_to([-2.8, -1.1, 0])
        # Right repaired row
        row_repaired_bg = Rectangle(width=5.2, height=0.65, fill_color=CREAM, fill_opacity=1,
                                   stroke_width=0, stroke_opacity=0).move_to([3.0, -1.1, 0])
        row_repaired_txt = Text("LLM->JSON | code check | eval() | INDEPENDENT",
                               color=PASS_CLR, font_size=17).move_to([3.0, -1.1, 0])
        audit_rows = VGroup(row_broken_bg, row_broken_txt, row_repaired_bg, row_repaired_txt)

        verdict_bg = Rectangle(width=6.0, height=0.38, fill_color=CREAM, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0).move_to([0, -3.2, 0])
        verdict_text = Text(
            "The seam is the unit of risk — name every trust decision",
            color=INK, font_size=24
        ).move_to([0, -3.2, 0])

        # 7 play() calls
        self.play(Write(title))
        self.play(FadeIn(broken_label_grp), FadeIn(repaired_label_grp), FadeIn(divider))
        self.play(FadeIn(broken_nodes), FadeIn(broken_arrows))
        self.play(Write(broken_no_gate_labels))
        self.play(FadeIn(repaired_nodes), FadeIn(repaired_arrows), FadeIn(gate_squares))
        self.play(Write(repaired_gate_labels), FadeIn(audit_rows))
        self.play(FadeIn(verdict_bg), Write(verdict_text))
