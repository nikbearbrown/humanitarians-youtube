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


class B04_FairnessTriangle(Scene):
    def construct(self):
        # ── Title ──────────────────────────────────────────────────────────────
        title = Text("FAIRNESS IMPOSSIBILITY (Chouldechova 2017)",
                     color=INK, weight=BOLD, font_size=28).move_to([0, 3.2, 0])

        # ── Triangle vertices — lowered top so label fits above without overlap ─
        V_DP = [ 0.0,  1.8, 0]  # Demographic Parity — top center (lowered for space)
        V_EO = [-3.3, -0.8, 0]  # Equalized Odds — bottom-left
        V_CP = [ 3.3, -0.8, 0]  # Calibration Parity — bottom-right

        # Triangle edges
        edge_dp_eo = Line(V_DP, V_EO, color=INK, stroke_width=1.5)
        edge_dp_cp = Line(V_DP, V_CP, color=INK, stroke_width=1.5)
        edge_eo_cp = Line(V_EO, V_CP, color=INK, stroke_width=1.5)
        triangle_edges = VGroup(edge_dp_eo, edge_dp_cp, edge_eo_cp)

        # Vertex labels — placed OUTSIDE the triangle, well off the lines
        def vertex_label(txt, pos, w=2.2, h=0.72):
            bg = Rectangle(width=w, height=h, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to(pos)
            t = Text(txt, color=INK, font_size=22).move_to(pos)
            return VGroup(bg, t)

        # DP label ABOVE vertex (vertex at y=1.8, label at y=2.7 — clear of title at 3.2)
        lbl_dp = vertex_label("Demographic\nParity",  [ 0.0,  2.7, 0], w=2.2, h=0.72)
        # EO label LEFT of vertex (vertex at x=-3.3, label at x=-5.1 — inside ±6.3)
        lbl_eo = vertex_label("Equalized\nOdds",      [-5.0, -0.8, 0], w=1.8, h=0.72)
        # CP label RIGHT of vertex
        lbl_cp = vertex_label("Calibration\nParity",  [ 5.0, -0.8, 0], w=1.9, h=0.72)
        vertex_labels = VGroup(lbl_dp, lbl_eo, lbl_cp)

        # ── X marks at edge midpoints (offset perpendicular from line) ───────
        def mid(a, b):
            return [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 0]

        # Offset inward (toward centroid ~(0, 0.6)) so X marks not on lines
        def offset_toward_center(pt, dx=0.5, dy=0.5):
            cx, cy = 0.0, 0.6  # triangle centroid approx
            vx = cx - pt[0]; vy = cy - pt[1]
            mag = (vx**2 + vy**2)**0.5 or 1.0
            scale = min(dx / max(abs(vx/mag), 0.01), 0.8)
            return [pt[0] + vx/mag * scale * 1.2, pt[1] + vy/mag * scale * 1.2, 0]

        mid_dp_eo = offset_toward_center(mid(V_DP, V_EO))
        mid_dp_cp = offset_toward_center(mid(V_DP, V_CP))
        mid_eo_cp = offset_toward_center(mid(V_EO, V_CP))

        def x_mark(pos):
            bg = Rectangle(width=0.70, height=0.70, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to(pos)
            t = Text("X", color=CRIMSON, weight=BOLD, font_size=48).move_to(pos)
            return VGroup(bg, t)

        x_marks = [x_mark(mid_dp_eo), x_mark(mid_dp_cp), x_mark(mid_eo_cp)]

        # ── Data table at bottom ───────────────────────────────────────────────
        # 3 rows: header, Group A, Group B
        # y centers: header=-1.75, row_a=-2.22, row_b=-2.69
        TABLE_LEFT = -5.0
        TABLE_RIGHT = 5.0
        TABLE_W = TABLE_RIGHT - TABLE_LEFT

        def table_row(texts, y_ctr, bg_color, text_color=INK):
            row_h = 0.42
            bg = Rectangle(width=TABLE_W, height=row_h,
                           fill_color=bg_color, fill_opacity=0.85,
                           stroke_width=0.5, stroke_color=INK, stroke_opacity=0.5
                           ).move_to([0, y_ctr, 0])
            cols = [-3.8, -2.0, -0.2, 1.6, 3.4]
            labels = VGroup(*[
                Text(t, color=text_color, font_size=17).move_to([cols[k], y_ctr, 0])
                for k, t in enumerate(texts)
            ])
            return VGroup(bg, labels)

        header_row = table_row(
            ["Group", "Base Rate", "PPV", "TPR", "FPR"],
            -1.72, SLATE, CREAM
        )
        row_a = table_row(
            ["A", "0.60", "0.65", "0.80", "0.44"],
            -2.18, CREAM, INK
        )
        row_b = table_row(
            ["B", "0.30", "0.65", "0.46", "0.26"],
            -2.64, CREAM, INK
        )

        # ── Verdict annotation ─────────────────────────────────────────────────
        verdict_bg = Rectangle(width=7.0, height=0.40, fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0).move_to([0, -3.15, 0])
        verdict_text = Text("TPR_A (0.80) != TPR_B (0.46)  —  Equalized Odds violated",
                            color=CRIMSON, weight=BOLD, font_size=22
                            ).move_to([0, -3.15, 0])
        verdict_annotation = VGroup(verdict_bg, verdict_text)

        # ── 6 play() calls ─────────────────────────────────────────────────────
        self.play(Write(title))
        self.play(FadeIn(triangle_edges), FadeIn(vertex_labels))
        self.play(FadeIn(header_row), FadeIn(row_a), FadeIn(row_b))
        self.play(FadeIn(x_marks[0]))
        self.play(FadeIn(x_marks[1]), FadeIn(x_marks[2]))
        self.play(FadeIn(verdict_annotation))
        self.wait(1)
