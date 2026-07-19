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


class B04_KonigsbergGraph(Scene):
    def construct(self):
        # Node positions: N, S, W, C
        NX, NY = 0.0,  2.0
        SX, SY = 0.0, -2.0
        WX, WY = -3.5, 0.0
        CX, CY =  1.5, 0.0

        # Helper: offset perpendicular to line between two points
        def perp_offset(x1, y1, x2, y2, d):
            dx, dy = x2-x1, y2-y1
            length = (dx**2+dy**2)**0.5
            return (-dy/length*d, dx/length*d)

        NODE_R = 0.48  # node radius + small gap; shorten edges so they don't pass through text

        def shrink(x1, y1, x2, y2, r):
            """Return endpoint pair shrunk by r from each end toward center"""
            dx, dy = x2-x1, y2-y1
            length = (dx**2+dy**2)**0.5
            if length < 2*r:
                mid = ((x1+x2)/2, (y1+y2)/2)
                return mid, mid
            frac = r/length
            sx1, sy1 = x1+dx*frac, y1+dy*frac
            sx2, sy2 = x2-dx*frac, y2-dy*frac
            return (sx1, sy1), (sx2, sy2)

        def make_edge(x1, y1, x2, y2, offset=0.0):
            (sx1, sy1), (sx2, sy2) = shrink(x1, y1, x2, y2, NODE_R)
            if offset == 0.0:
                return Line((sx1,sy1,0),(sx2,sy2,0), color=SLATE, stroke_width=2)
            ox, oy = perp_offset(x1,y1,x2,y2,offset)
            return Line((sx1+ox,sy1+oy,0),(sx2+ox,sy2+oy,0), color=SLATE, stroke_width=2)

        def tick_label(txt, pos, fontsize=18, color=SLATE):
            bg = Rectangle(
                width=len(txt)*0.13+0.15, height=0.35,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            ).move_to(pos)
            t = Text(txt, font_size=fontsize, color=color).move_to(pos)
            return VGroup(bg, t)

        # Title
        title = Text(
            "KONIGSBERG BRIDGES — EULER'S THEOREM",
            font_size=30, color=INK, weight=BOLD
        ).move_to((0, 3.2, 0))

        # Build node circles and name labels
        def make_node(cx, cy, label, node_color=CREAM):
            c = Circle(radius=0.45, color=INK, stroke_width=2,
                       fill_color=node_color, fill_opacity=1).move_to((cx,cy,0))
            t = Text(label, font_size=22, color=INK, weight=BOLD).move_to((cx,cy,0))
            return VGroup(c, t)

        node_N = make_node(NX, NY, "N")
        node_S = make_node(SX, SY, "S")
        node_W = make_node(WX, WY, "W")
        node_C = make_node(CX, CY, "C")
        nodes_and_labels = VGroup(node_N, node_S, node_W, node_C)

        # Build 7 edges (with multi-edge offsets)
        # N-C ×2
        e_NC1 = make_edge(NX, NY, CX, CY, offset= 0.18)
        e_NC2 = make_edge(NX, NY, CX, CY, offset=-0.18)
        # S-C ×2
        e_SC1 = make_edge(SX, SY, CX, CY, offset= 0.18)
        e_SC2 = make_edge(SX, SY, CX, CY, offset=-0.18)
        # N-W ×1
        e_NW  = make_edge(NX, NY, WX, WY)
        # S-W ×1
        e_SW  = make_edge(SX, SY, WX, WY)
        # C-W ×1
        e_CW  = make_edge(CX, CY, WX, WY)
        edges_group = VGroup(e_NC1, e_NC2, e_SC1, e_SC2, e_NW, e_SW, e_CW)

        # Degree labels (all odd → all CRIMSON)
        # N: deg=3 (NC,NC,NW)
        dlbl_N = tick_label("deg=3", (NX+0.7, NY+0.55, 0), fontsize=18, color=CRIMSON)
        # S: deg=3 (SC,SC,SW)
        dlbl_S = tick_label("deg=3", (SX+0.7, SY-0.55, 0), fontsize=18, color=CRIMSON)
        # W: deg=3 (NW,SW,CW)
        dlbl_W = tick_label("deg=3", (WX-0.2, WY+0.65, 0), fontsize=18, color=CRIMSON)
        # C: deg=5 (NC,NC,SC,SC,CW)
        dlbl_C = tick_label("deg=5", (CX+0.85, CY+0.55, 0), fontsize=18, color=CRIMSON)
        degree_labels = VGroup(dlbl_N, dlbl_S, dlbl_W, dlbl_C)

        # Node fill → CRIMSON (all odd)
        node_N_red = make_node(NX, NY, "N", node_color="#FF8080")
        node_S_red = make_node(SX, SY, "S", node_color="#FF8080")
        node_W_red = make_node(WX, WY, "W", node_color="#FF8080")
        node_C_red = make_node(CX, CY, "C", node_color="#FF8080")
        degree_colors = VGroup(node_N_red, node_S_red, node_W_red, node_C_red)

        # Verdict banner at y=-3.0
        verdict_bg = Rectangle(width=9.5, height=0.45, fill_color=CREAM, fill_opacity=1,
                                stroke_width=0, stroke_opacity=0).move_to((0,-3.1,0))
        verdict_txt = Text("ALL ODD DEGREES -- No Euler path exists",
                           font_size=26, color=CRIMSON, weight=BOLD).move_to((0,-3.1,0))
        verdict_text = VGroup(verdict_bg, verdict_txt)

        # --- Sequence (6 play() calls) ---
        self.play(Write(title))
        self.play(FadeIn(edges_group))
        self.play(FadeIn(nodes_and_labels))  # nodes drawn after edges so circles cover edge endpoints
        self.play(*[Write(d) for d in degree_labels])
        self.play(FadeIn(degree_colors))
        self.play(Write(verdict_text))
        self.wait(1)
