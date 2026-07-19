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


class B04_DAGPaths(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # Node positions
        S_pos = [-4.0, 0.0, 0]
        T_pos = [0.0, 0.0, 0]
        C_pos = [4.0, 0.0, 0]
        G_pos = [-2.0, 2.0, 0]  # lowered so label doesn't overlap title

        # --- Nodes ---
        def make_node(pos, label_str):
            circ = Circle(radius=0.35, color=INK, fill_color=CREAM, fill_opacity=1,
                          stroke_width=2)
            circ.move_to(pos)
            lbl = Text(label_str, color=INK, font_size=26, weight=BOLD)
            lbl.move_to([pos[0], pos[1] + 0.65, 0])
            return circ, lbl

        s_circ, s_lbl = make_node(S_pos, "S")
        t_circ, t_lbl = make_node(T_pos, "T")
        c_circ, c_lbl = make_node(C_pos, "C")
        g_circ, g_lbl = make_node(G_pos, "G")

        # Node sublabels
        s_sub = Text("Smoking", color=SLATE, font_size=20)
        s_sub.move_to([-4.0, -0.65, 0])
        t_sub = Text("Tar", color=SLATE, font_size=20)
        t_sub.move_to([0.0, -0.65, 0])
        c_sub = Text("Cancer", color=SLATE, font_size=20)
        c_sub.move_to([4.0, -0.65, 0])
        g_sub = Text("Genotype", color=SLATE, font_size=20)
        g_sub.move_to([-2.0, 1.3, 0])

        nodes_group = VGroup(
            s_circ, s_lbl, s_sub,
            t_circ, t_lbl, t_sub,
            c_circ, c_lbl, c_sub,
            g_circ, g_lbl, g_sub
        )

        # --- Edges ---
        st_arrow = Arrow(start=[-3.65, 0.0, 0], end=[-0.35, 0.0, 0],
                         color=INK, buff=0, tip_length=0.2, stroke_width=3)
        tc_arrow = Arrow(start=[0.35, 0.0, 0], end=[3.65, 0.0, 0],
                         color=INK, buff=0, tip_length=0.2, stroke_width=3)
        # G->S: from G_pos (y=2.0) toward S_pos
        gs_arrow = Arrow(start=[-2.25, 1.78, 0], end=[-3.75, 0.3, 0],
                         color=INK, buff=0, tip_length=0.2, stroke_width=3)
        # G->C: from G_pos (y=2.0) toward C_pos
        gc_arrow = Arrow(start=[-1.75, 1.78, 0], end=[3.65, 0.3, 0],
                         color=INK, buff=0, tip_length=0.2, stroke_width=3)

        edges_group = VGroup(st_arrow, tc_arrow, gs_arrow, gc_arrow)

        # Title
        title = Text("DAG PATH ANALYSIS", color=INK, weight=BOLD, font_size=38)
        title.move_to([0, 3.2, 0])

        # Path labels
        causal_bg = Rectangle(width=3.5, height=0.4, fill_color=CREAM,
                               fill_opacity=1, stroke_width=0, stroke_opacity=0)
        causal_bg.move_to([0.0, -1.5, 0])
        causal_txt = Text("CAUSAL: S -> T -> C", color=PASS_CLR, weight=BOLD, font_size=26)
        causal_txt.move_to([0.0, -1.5, 0])
        causal_label = VGroup(causal_bg, causal_txt)

        backdoor_bg = Rectangle(width=4.0, height=0.4, fill_color=CREAM,
                                 fill_opacity=1, stroke_width=0, stroke_opacity=0)
        backdoor_bg.move_to([0.0, -2.1, 0])
        backdoor_txt = Text("BACK-DOOR: S <- G -> C", color="#E06400", weight=BOLD, font_size=26)
        backdoor_txt.move_to([0.0, -2.1, 0])
        backdoor_label = VGroup(backdoor_bg, backdoor_txt)

        # Verdict
        verdict_bg = Rectangle(width=7.0, height=0.4, fill_color=CREAM,
                                fill_opacity=1, stroke_width=0, stroke_opacity=0)
        verdict_bg.move_to([0.0, -2.8, 0])
        verdict_txt = Text("d-separation: block G to identify effect", color=INK, font_size=28)
        verdict_txt.move_to([0.0, -2.8, 0])
        verdict_text = VGroup(verdict_bg, verdict_txt)

        # Sequence — 6 play() calls
        self.play(FadeIn(nodes_group))
        self.play(FadeIn(edges_group))
        self.play(Write(title))
        self.play(
            st_arrow.animate.set_color(PASS_CLR),
            tc_arrow.animate.set_color(PASS_CLR),
            Write(causal_label)
        )
        self.play(
            gs_arrow.animate.set_color("#E06400"),
            gc_arrow.animate.set_color("#E06400"),
            Write(backdoor_label)
        )
        self.play(Write(verdict_text))
        self.wait(1)
