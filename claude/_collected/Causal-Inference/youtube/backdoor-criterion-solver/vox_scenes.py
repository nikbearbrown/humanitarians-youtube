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


class B04_BackdoorDAG(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # Node positions
        X_pos = [-3.5, 0.0, 0]
        Y_pos = [3.5, 0.0, 0]
        A_pos = [-3.5, 2.5, 0]
        B_pos = [3.5, 2.5, 0]
        M_pos = [0.0, 2.5, 0]

        # Title
        title = Text("BACK-DOOR CRITERION", color=INK, weight=BOLD, font_size=38)
        title.move_to([0, 3.2, 0])

        # --- Nodes ---
        def make_node(pos, label_str, fill=CREAM):
            circ = Circle(radius=0.35, color=INK, fill_color=fill, fill_opacity=1,
                          stroke_width=2)
            circ.move_to(pos)
            lbl = Text(label_str, color=INK, font_size=28, weight=BOLD)
            lbl.move_to(pos)
            return circ, lbl

        x_circ, x_lbl = make_node(X_pos, "X")
        y_circ, y_lbl = make_node(Y_pos, "Y")
        a_circ, a_lbl = make_node(A_pos, "A")
        b_circ, b_lbl = make_node(B_pos, "B")
        m_circ, m_lbl = make_node(M_pos, "M")

        x_sub = Text("Treatment", color=SLATE, font_size=20)
        x_sub.move_to([-3.5, -0.65, 0])
        y_sub = Text("Outcome", color=SLATE, font_size=20)
        y_sub.move_to([3.5, -0.65, 0])
        m_type = Text("(Collider)", color=CRIMSON, font_size=20)
        m_type.move_to([0.0, 1.85, 0])

        nodes_and_labels = VGroup(
            x_circ, x_lbl, x_sub,
            y_circ, y_lbl, y_sub,
            a_circ, a_lbl,
            b_circ, b_lbl,
            m_circ, m_lbl, m_type
        )

        # --- Edges (all as Arrow objects) ---
        # A->X
        ax_arrow = Arrow(start=[-3.5, 2.15, 0], end=[-3.5, 0.35, 0],
                         color=SLATE, buff=0, tip_length=0.2, stroke_width=2)
        # A->M
        am_arrow = Arrow(start=[-3.15, 2.5, 0], end=[-0.35, 2.5, 0],
                         color=SLATE, buff=0, tip_length=0.2, stroke_width=2)
        # B->M
        bm_arrow = Arrow(start=[3.15, 2.5, 0], end=[0.35, 2.5, 0],
                         color=SLATE, buff=0, tip_length=0.2, stroke_width=2)
        # B->Y
        by_arrow = Arrow(start=[3.5, 2.15, 0], end=[3.5, 0.35, 0],
                         color=SLATE, buff=0, tip_length=0.2, stroke_width=2)
        # X->Y
        xy_arrow = Arrow(start=[-3.15, 0.0, 0], end=[3.15, 0.0, 0],
                         color=INK, buff=0, tip_length=0.2, stroke_width=3)

        edges_group = VGroup(ax_arrow, am_arrow, bm_arrow, by_arrow, xy_arrow)

        # --- Annotations ---
        # M invalid label
        m_invalid_bg = Rectangle(width=3.5, height=0.4, fill_color=CREAM,
                                  fill_opacity=1, stroke_width=0, stroke_opacity=0)
        m_invalid_bg.move_to([0.0, 1.2, 0])
        m_invalid_txt = Text("INVALID: opens collider", color=CRIMSON, font_size=26)
        m_invalid_txt.move_to([0.0, 1.2, 0])
        m_invalid_label = VGroup(m_invalid_bg, m_invalid_txt)

        # Valid adjustment sets label
        valid_bg = Rectangle(width=5.5, height=0.4, fill_color=CREAM,
                              fill_opacity=1, stroke_width=0, stroke_opacity=0)
        valid_bg.move_to([0.0, -2.0, 0])
        valid_txt = Text("{A} or {B}: valid adjustment sets", color=PASS_CLR, font_size=28)
        valid_txt.move_to([0.0, -2.0, 0])
        valid_label = VGroup(valid_bg, valid_txt)

        # Verdict
        verdict_bg = Rectangle(width=6.0, height=0.4, fill_color=CREAM,
                                fill_opacity=1, stroke_width=0, stroke_opacity=0)
        verdict_bg.move_to([0.0, -3.0, 0])
        verdict_txt = Text("Adjusting for M INTRODUCES bias", color=CRIMSON, weight=BOLD, font_size=30)
        verdict_txt.move_to([0.0, -3.0, 0])
        verdict_text = VGroup(verdict_bg, verdict_txt)

        # Sequence — 6 play() calls
        self.play(Write(title))
        self.play(FadeIn(nodes_and_labels))
        self.play(FadeIn(edges_group))
        self.play(
            m_circ.animate.set_fill(GOLD, opacity=1),
            Write(m_invalid_label)
        )
        self.play(
            a_circ.animate.set_fill(PASS_CLR, opacity=0.4),
            b_circ.animate.set_fill(PASS_CLR, opacity=0.4),
            Write(valid_label)
        )
        self.play(Write(verdict_text))
        self.wait(1)
