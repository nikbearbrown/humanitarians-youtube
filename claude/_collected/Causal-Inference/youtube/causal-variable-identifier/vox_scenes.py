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


class B04_VariableDAG(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # Title — kept at y=3.2 per spec but font_size reduced to avoid arrow overlap
        title = Text("LLM-ASSISTED DAG CONSTRUCTION", color=INK, weight=BOLD, font_size=30)
        title.move_to([0, 3.2, 0])

        # Node positions
        HRT_pos = [-4.0, 0.0, 0]
        HD_pos = [4.0, 0.0, 0]
        HC_pos = [0.0, 2.3, 0]   # lowered so circle top stays below title at y=3.2
        INC_pos = [-2.0, -2.5, 0]
        DIET_pos = [2.0, -2.5, 0]

        # Helper to make a node
        def make_node(pos, label_str, fill=CREAM, label_color=INK, radius=0.4):
            circ = Circle(radius=radius, color=INK, fill_color=fill, fill_opacity=1,
                          stroke_width=2)
            circ.move_to(pos)
            lbl = Text(label_str, color=label_color, font_size=20, weight=BOLD)
            lbl.move_to(pos)
            return circ, lbl

        # Treatment and Outcome nodes
        hrt_circ, hrt_lbl = make_node(HRT_pos, "HRT")
        hd_circ, hd_lbl = make_node(HD_pos, "Heart\nDisease", radius=0.5)
        hd_lbl = Text("HD", color=INK, font_size=20, weight=BOLD)
        hd_lbl.move_to(HD_pos)

        # Sub-labels
        hrt_sub = Text("Treatment", color=SLATE, font_size=18)
        hrt_sub.move_to([-4.0, -0.65, 0])
        hd_sub = Text("Outcome", color=SLATE, font_size=18)
        hd_sub.move_to([4.0, -0.65, 0])

        treatment_node = VGroup(hrt_circ, hrt_lbl, hrt_sub)
        outcome_node = VGroup(hd_circ, hd_lbl, hd_sub)

        # Confounder nodes (GOLD fill)
        hc_circ, hc_lbl_inner = make_node(HC_pos, "HC", fill=GOLD, radius=0.38)
        # hc_label placed to the left of the node, not above (avoids title overlap)
        hc_label = Text("H-Conscious", color=INK, font_size=18)
        hc_label.move_to([-1.2, 2.8, 0])
        hc_node = VGroup(hc_circ, hc_lbl_inner)

        inc_circ, inc_lbl_inner = make_node(INC_pos, "Inc", fill=GOLD, radius=0.35)
        income_label = Text("Income", color=INK, font_size=18)
        income_label.move_to([-2.8, -2.5, 0])
        income_node = VGroup(inc_circ, inc_lbl_inner)

        # Mediator node (light blue fill)
        diet_circ, diet_lbl_inner = make_node(DIET_pos, "Diet", fill="#CCE5FF", radius=0.35)
        diet_label = Text("Diet", color=INK, font_size=18)
        diet_label.move_to([2.0, -2.2, 0])
        diet_node = VGroup(diet_circ, diet_lbl_inner)

        # Edges
        def mk_arrow(from_p, to_p):
            return Arrow(start=from_p, end=to_p, color=SLATE, buff=0.38,
                         tip_length=0.18, stroke_width=2)

        hc_hrt = mk_arrow(HC_pos, HRT_pos)
        hc_hd = mk_arrow(HC_pos, HD_pos)
        inc_hrt = mk_arrow(INC_pos, HRT_pos)
        inc_hd = mk_arrow(INC_pos, HD_pos)
        hrt_diet = mk_arrow(HRT_pos, DIET_pos)
        diet_hd = mk_arrow(DIET_pos, HD_pos)

        all_edges_group = VGroup(hc_hrt, hc_hd, inc_hrt, inc_hd, hrt_diet, diet_hd)

        # Legend at x=3.5, y=1.5-2.5
        leg_conf_bg = Rectangle(width=0.5, height=0.3, fill_color=GOLD,
                                 fill_opacity=1, stroke_width=0, stroke_opacity=0)
        leg_conf_bg.move_to([3.2, 2.3, 0])
        leg_conf_txt = Text("confounder", color=INK, font_size=18)
        leg_conf_txt.move_to([4.2, 2.3, 0])
        leg_conf = VGroup(leg_conf_bg, leg_conf_txt)

        leg_med_bg = Rectangle(width=0.5, height=0.3, fill_color="#CCE5FF",
                                fill_opacity=1, stroke_width=0, stroke_opacity=0)
        leg_med_bg.move_to([3.2, 1.8, 0])
        leg_med_txt = Text("mediator", color=INK, font_size=18)
        leg_med_txt.move_to([4.1, 1.8, 0])
        leg_med = VGroup(leg_med_bg, leg_med_txt)

        leg_col_bg = Rectangle(width=0.5, height=0.3, fill_color="#FFD6D6",
                                fill_opacity=1, stroke_width=0, stroke_opacity=0)
        leg_col_bg.move_to([3.2, 1.3, 0])
        leg_col_txt = Text("collider", color=INK, font_size=18)
        leg_col_txt.move_to([4.0, 1.3, 0])
        leg_col = VGroup(leg_col_bg, leg_col_txt)

        legend = VGroup(leg_conf, leg_med, leg_col)

        # Verdict text — placed at safe y position
        verdict_bg = Rectangle(width=7.5, height=0.4, fill_color=CREAM,
                                fill_opacity=1, stroke_width=0, stroke_opacity=0)
        verdict_bg.move_to([0, -3.0, 0])
        verdict_txt = Text("Adj set {H-Conscious, Income} identifies effect",
                           color=PASS_CLR, font_size=26)
        verdict_txt.move_to([0, -3.0, 0])
        verdict_text = VGroup(verdict_bg, verdict_txt)

        # Sequence — 7 play() calls
        self.play(Write(title))
        self.play(FadeIn(treatment_node), FadeIn(outcome_node))
        self.play(FadeIn(hc_node), Write(hc_label))
        self.play(FadeIn(income_node), Write(income_label))
        self.play(FadeIn(diet_node), Write(diet_label))
        self.play(FadeIn(all_edges_group))
        self.play(Write(verdict_text), FadeIn(legend))
        self.wait(1)
