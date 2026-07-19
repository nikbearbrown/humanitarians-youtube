"""vox_scenes.py — matrix-signaling-reservoir
B04 only: animated vertical mechanosignaling cascade (7 nodes).
Palette: teardown — INK=#2A1A0E CREAM=#FFFFFF CRIMSON=#C8102E SLATE=#545454 GOLD=#F6D8DC
NEVER use: Axes, ParametricFunction, weight=NORMAL
ALWAYS: Manual Line for connectors; CREAM Rectangle backgrounds behind text near Lines.
"""
import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_MechanoPathway(Scene):
    """Animated vertical 7-node mechanosignaling cascade."""

    def construct(self):
        dur = DUR.get("B04", 20.0)

        # ── Title ──────────────────────────────────────────────────────────────
        title = Text("MECHANOSIGNALING CASCADE", font_size=28, color=INK, weight=BOLD)
        title.move_to(UP * 3.2)

        # ── Node definitions: (y, fill, stroke_color, stroke_width, label, text_color)
        node_specs = [
            (2.3,  GOLD,  INK,    1,  "LOX: Collagen Crosslinking", INK),
            (1.5,  CREAM, SLATE,  2,  "Stiff ECM (50× normal)",     SLATE),
            (0.7,  CREAM, INK,    1,  "Integrin Clustering",         INK),
            (-0.1, CREAM, INK,    1,  "FAK Kinase Activation",       INK),
            (-0.9, CREAM, INK,    1,  "Rho GTPase Activation",       INK),
            (-1.7, GOLD,  CRIMSON,2,  "YAP/TAZ → Nucleus",           CRIMSON),
            (-2.5, CREAM, CRIMSON,2,  "EMT + Proliferation Genes",   CRIMSON),
        ]

        nodes = VGroup()
        node_mobs = []
        for (y, fill, stroke_col, stroke_w, label, txt_col) in node_specs:
            bg = Rectangle(width=4.0, height=0.55)
            bg.set_fill(fill, opacity=1).set_stroke(color=stroke_col, width=stroke_w)
            bg.move_to([0, y, 0])
            txt = Text(label, font_size=14, color=txt_col)
            txt.move_to(bg.get_center())
            group = VGroup(bg, txt)
            node_mobs.append(group)
            nodes.add(group)

        # ── Connector lines between nodes ──────────────────────────────────────
        # Each node is 0.55 tall, so bottom = y - 0.275, top of next = y_next + 0.275
        conn_ys = [
            (2.3 - 0.275, 1.5 + 0.275),   # 1→2
            (1.5 - 0.275, 0.7 + 0.275),   # 2→3
            (0.7 - 0.275, -0.1 + 0.275),  # 3→4
            (-0.1 - 0.275, -0.9 + 0.275), # 4→5
            (-0.9 - 0.275, -1.7 + 0.275), # 5→6
            (-1.7 - 0.275, -2.5 + 0.275), # 6→7
        ]
        connectors = []
        for (y_from, y_to) in conn_ys:
            line = Line(start=[0, y_from, 0], end=[0, y_to, 0],
                        color=INK, stroke_width=1.5)
            connectors.append(line)

        # ── Side annotation (mammographic density note) at ECM node (y=1.5) ──
        annot_bg = Rectangle(width=3.5, height=0.75)
        annot_bg.set_fill(CREAM, opacity=1).set_stroke(width=0, opacity=0)
        annot_bg.move_to([3.8, 1.5, 0])
        annot_txt = Text("Mammographic density\npredicts breast cancer risk\n(4× RR highest quartile)",
                         font_size=11, color=SLATE)
        annot_txt.move_to(annot_bg.get_center())
        annot_line = Line(start=[2.1, 1.5, 0], end=[2.9, 1.5, 0],
                          color=SLATE, stroke_width=1)
        annotation = VGroup(annot_bg, annot_txt, annot_line)

        # ── Bottom crimson rule ────────────────────────────────────────────────
        bottom_rule = Line(start=[-6.0, -3.2, 0], end=[5.5, -3.2, 0],
                           color=CRIMSON, stroke_width=2)

        # ── Animation sequence (7 states) ─────────────────────────────────────
        t_unit = dur / 7.0

        # State 1: title
        self.play(FadeIn(title), run_time=t_unit * 0.8)
        self.wait(t_unit * 0.2)

        # State 2: Node 1 (LOX) + Node 2 (Stiff ECM) + connector 1-2
        self.play(
            FadeIn(node_mobs[0]), FadeIn(node_mobs[1]),
            Create(connectors[0]),
            run_time=t_unit * 0.8
        )
        self.wait(t_unit * 0.2)

        # State 3: Node 3 (Integrin) + Node 4 (FAK) + connectors 2-3, 3-4
        self.play(
            FadeIn(node_mobs[2]), FadeIn(node_mobs[3]),
            Create(connectors[1]), Create(connectors[2]),
            run_time=t_unit * 0.8
        )
        self.wait(t_unit * 0.2)

        # State 4: Node 5 (Rho) + connector 4-5
        self.play(
            FadeIn(node_mobs[4]), Create(connectors[3]),
            run_time=t_unit * 0.8
        )
        self.wait(t_unit * 0.2)

        # State 5: Node 6 (YAP/TAZ, gold/crimson) + connector 5-6
        self.play(
            FadeIn(node_mobs[5]), Create(connectors[4]),
            run_time=t_unit * 0.8
        )
        self.wait(t_unit * 0.2)

        # State 6: Node 7 (EMT genes, crimson) + connector 6-7
        self.play(
            FadeIn(node_mobs[6]), Create(connectors[5]),
            run_time=t_unit * 0.8
        )
        self.wait(t_unit * 0.2)

        # State 7: side annotation + bottom rule
        self.play(
            FadeIn(annotation), Create(bottom_rule),
            run_time=t_unit * 0.8
        )
        self.wait(t_unit * 0.2)
