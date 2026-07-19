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


class B04_DAGDiscovery(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # ---- Title ----
        title = Text(
            "PC Algorithm: Learning Causal Structure from Data",
            color=INK, weight=BOLD, font_size=28
        )
        title.move_to([0, 3.2, 0])

        # ====================================================
        # Node positions
        # ====================================================
        node_pos = {
            "X1": [-4.0, 0.0, 0],
            "X2": [-1.5, 1.5, 0],
            "X3": [-1.5, -1.5, 0],
            "X4": [1.5, 0.5, 0],
            "X5": [4.0, 0.0, 0],
        }
        node_radius = 0.45

        # Build node circles and labels
        nodes = VGroup()
        node_labels_grp = VGroup()
        for name, pos in node_pos.items():
            circ = Circle(radius=node_radius,
                          fill_color=CREAM, fill_opacity=1,
                          stroke_color=INK, stroke_width=2)
            circ.move_to(pos)
            lbl = Text(name, color=INK, font_size=24, weight=BOLD)
            lbl.move_to(pos)
            nodes.add(circ)
            node_labels_grp.add(lbl)

        all_nodes = VGroup(nodes, node_labels_grp)

        # ====================================================
        # Helper: compute shrunk edge endpoints
        # ====================================================
        def edge_pts(p1, p2, r=node_radius):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            dist = (dx**2 + dy**2)**0.5
            ux = dx / dist
            uy = dy / dist
            sx = p1[0] + r*ux
            sy = p1[1] + r*uy
            ex = p2[0] - r*ux
            ey = p2[1] - r*uy
            return [sx, sy, 0], [ex, ey, 0]

        # True edges: X1->X2, X1->X3, X2->X4, X3->X4, X4->X5, X2->X5
        true_edges = [
            ("X1", "X2"),
            ("X1", "X3"),
            ("X2", "X4"),
            ("X3", "X4"),
            ("X4", "X5"),
            ("X2", "X5"),
        ]

        # Skeleton: undirected gray lines
        skeleton_grp = VGroup()
        for (a, b) in true_edges:
            s, e = edge_pts(node_pos[a], node_pos[b])
            seg = Line(start=s, end=e, color=SLATE, stroke_width=2)
            skeleton_grp.add(seg)

        # False positive edge X1-X4 (undirected)
        fp_s, fp_e = edge_pts(node_pos["X1"], node_pos["X4"])
        false_positive_edge = Line(start=fp_s, end=fp_e,
                                   color=CRIMSON, stroke_width=2)

        # Colored arrows (oriented DAG)
        arrows_grp = VGroup()
        for (a, b) in true_edges:
            s, e = edge_pts(node_pos[a], node_pos[b])
            arr = Arrow(start=s, end=e,
                        tip_length=0.2,
                        stroke_color=PASS_CLR, stroke_width=3,
                        buff=0)
            arrows_grp.add(arr)

        # ====================================================
        # V-structure annotation
        # ====================================================
        vs_bg = Rectangle(width=8.0, height=0.35,
                          fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0)
        vs_bg.move_to([-0.5, 2.5, 0])
        vs_txt = Text(
            "V-structure: X2 -> X4 <- X3 (X2,X3 independent given nothing)",
            font_size=18, color=SLATE
        )
        vs_txt.move_to([-0.5, 2.5, 0])
        v_structure_annotation = VGroup(vs_bg, vs_txt)

        # ====================================================
        # Metrics box
        # ====================================================
        metrics_bg = Rectangle(width=4.5, height=0.65,
                               fill_color=GOLD, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0)
        metrics_bg.move_to([3.0, -2.7, 0])
        metrics_txt = Text(
            "Precision: 0.86 | Recall: 1.0 | SHD: 1",
            font_size=20, color=INK
        )
        metrics_txt.move_to([3.0, -2.7, 0])
        metrics_box = VGroup(metrics_bg, metrics_txt)

        # ---- Animation ----
        self.play(Write(title))
        self.play(FadeIn(all_nodes))
        self.play(Create(skeleton_grp), Create(false_positive_edge))
        self.play(FadeOut(false_positive_edge))
        self.play(FadeIn(v_structure_annotation))
        self.play(FadeOut(skeleton_grp), FadeIn(arrows_grp))
        self.play(FadeIn(metrics_box))
        self.wait(1)
