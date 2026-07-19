"""vox_scenes.py — Audit a Codex Session for the Five Supervisory Capacities
(supervisory-capacities-audit, slate cut, 16:9)

B04 and B06 are MANIM type — animated session timeline scenes.
All other beats are SLATE.

Color law: INK = labeled/active nodes; SLATE = gap/unlabeled nodes;
CRIMSON = gap annotation / violation markers.
"""
import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE_COL="#545454"; GOLD="#F6D8DC"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---- B04: SessionTimeline
# Horizontal timeline with 8 step nodes.
# Steps 1=PF, 2=TO, 3=none(gap), 4=PA, 5=none(gap), 6=IJ, 7=EI, 8=none(gap)

class B04_SessionTimeline(Scene):
    def construct(self):
        total = DUR.get("B04", 20.0)

        # Title
        title = Text("SESSION CAPACITY AUDIT", font=DISPLAY, color=INK,
                     font_size=32, weight="BOLD")
        title.move_to(UP * 3.2)

        # Node data: (step_num, label, is_gap)
        node_data = [
            (1, "PF", False),
            (2, "TO", False),
            (3, "",   True),
            (4, "PA", False),
            (5, "",   True),
            (6, "IJ", False),
            (7, "EI", False),
            (8, "",   True),
        ]

        # x positions: -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5
        node_xs = [-3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5]
        node_y = 0.0

        nodes = VGroup()
        node_centers = []
        for i, (step_num, cap_label, is_gap) in enumerate(node_data):
            x = node_xs[i]
            circle = Circle(radius=0.25)
            if is_gap:
                circle.set_fill(SLATE_COL, opacity=1).set_stroke(color=INK, width=1.5)
                num_color = CREAM
            else:
                circle.set_fill(CREAM, opacity=1).set_stroke(color=INK, width=1.5)
                num_color = INK
            circle.move_to(RIGHT * x + UP * node_y)
            node_num = Text(str(step_num), font=DISPLAY, color=num_color,
                            font_size=14, weight="BOLD")
            node_num.move_to(circle.get_center())
            nodes.add(VGroup(circle, node_num))
            node_centers.append(RIGHT * x + UP * node_y)

        # Connecting lines between adjacent nodes (horizontal baseline)
        connectors = VGroup()
        for i in range(len(node_xs) - 1):
            x1 = node_xs[i] + 0.25   # right edge of node i
            x2 = node_xs[i+1] - 0.25  # left edge of node i+1
            line = Line(RIGHT * x1 + UP * node_y, RIGHT * x2 + UP * node_y,
                        stroke_width=1.5, color=INK)
            connectors.add(line)

        # Capacity labels above non-gap nodes
        cap_labels = VGroup()
        for i, (step_num, cap_label, is_gap) in enumerate(node_data):
            if not is_gap and cap_label:
                x = node_xs[i]
                lbl = Text(cap_label, font=DISPLAY, color=INK, font_size=18,
                           weight="BOLD")
                lbl.move_to(RIGHT * x + UP * (node_y + 0.8))
                cap_labels.add(lbl)

        # GAP labels below gap nodes with CREAM backgrounds
        gap_labels = VGroup()
        for i, (step_num, cap_label, is_gap) in enumerate(node_data):
            if is_gap:
                x = node_xs[i]
                gap_txt = Text("GAP", font=DISPLAY, color=CRIMSON, font_size=16,
                               weight="BOLD")
                gap_txt.move_to(RIGHT * x + UP * (node_y - 0.8))
                gap_bg = Rectangle(
                    width=gap_txt.width + 0.2,
                    height=gap_txt.height + 0.1
                ).set_fill(CREAM, opacity=1).set_stroke(width=0, opacity=0)
                gap_bg.move_to(gap_txt.get_center())
                gap_labels.add(VGroup(gap_bg, gap_txt))

        # Animation sequence (6 states)
        # 1. Title
        self.play(FadeIn(title), run_time=0.5)
        # 2. All 8 node circles appear
        self.play(LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.08, run_time=1.0))
        # 3. Connecting lines appear
        self.play(LaggedStart(*[Create(c) for c in connectors], lag_ratio=0.08, run_time=0.8))
        # 4. Non-gap capacity labels appear
        self.play(LaggedStart(*[FadeIn(l) for l in cap_labels], lag_ratio=0.12, run_time=0.8))
        # 5. Gap nodes color to SLATE (they're already SLATE; animate to emphasize)
        gap_node_circles = [nodes[2][0], nodes[4][0], nodes[7][0]]
        self.play(*[circ.animate.set_fill(SLATE_COL) for circ in gap_node_circles], run_time=0.5)
        # 6. GAP labels appear below gray nodes
        self.play(LaggedStart(*[FadeIn(g) for g in gap_labels], lag_ratio=0.2, run_time=0.7))

        self.wait(max(0.5, total - 4.3))


# ---- B06: EIGapTrace
# Same timeline but step 7 is gray. Arrow from step 7 down to violation box.
# Dashed line connects violation back to step 7.

class B06_EIGapTrace(Scene):
    def construct(self):
        total = DUR.get("B06", 14.0)

        # Title
        title = Text("SESSION CAPACITY AUDIT", font=DISPLAY, color=INK,
                     font_size=32, weight="BOLD")
        title.move_to(UP * 3.2)

        # Same 8 nodes but step 7 is now gray (EI absent)
        node_data = [
            (1, "PF", False),
            (2, "TO", False),
            (3, "",   True),
            (4, "PA", False),
            (5, "",   True),
            (6, "IJ", False),
            (7, "",   True),   # EI absent — step 7 becomes gap
            (8, "",   True),
        ]
        node_xs = [-3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5]
        node_y = 0.0

        nodes = VGroup()
        for i, (step_num, cap_label, is_gap) in enumerate(node_data):
            x = node_xs[i]
            circle = Circle(radius=0.25)
            if is_gap:
                circle.set_fill(SLATE_COL, opacity=1).set_stroke(color=INK, width=1.5)
                num_color = CREAM
            else:
                circle.set_fill(CREAM, opacity=1).set_stroke(color=INK, width=1.5)
                num_color = INK
            circle.move_to(RIGHT * x + UP * node_y)
            node_num = Text(str(step_num), font=DISPLAY, color=num_color,
                            font_size=14, weight="BOLD")
            node_num.move_to(circle.get_center())
            nodes.add(VGroup(circle, node_num))

        connectors = VGroup()
        for i in range(len(node_xs) - 1):
            x1 = node_xs[i] + 0.25
            x2 = node_xs[i+1] - 0.25
            line = Line(RIGHT * x1 + UP * node_y, RIGHT * x2 + UP * node_y,
                        stroke_width=1.5, color=INK)
            connectors.add(line)

        # Capacity labels for non-gap nodes (PF, TO, PA, IJ only — not EI at 7)
        cap_labels_data = [(0, "PF"), (1, "TO"), (3, "PA"), (5, "IJ")]
        cap_labels = VGroup()
        for idx, lbl_text in cap_labels_data:
            x = node_xs[idx]
            lbl = Text(lbl_text, font=DISPLAY, color=INK, font_size=18, weight="BOLD")
            lbl.move_to(RIGHT * x + UP * (node_y + 0.8))
            cap_labels.add(lbl)

        # Step 7 node center at x=2.5, y=0
        step7_center = RIGHT * 2.5 + UP * 0.0

        # Violation box at y=-2.0, x=2.5
        viol_rect = Rectangle(width=4.0, height=0.8)
        viol_rect.set_fill(CREAM, opacity=1).set_stroke(color=CRIMSON, width=2)
        viol_rect.move_to(RIGHT * 2.5 + DOWN * 2.0)

        viol_text = Text("CONSTRAINT VIOLATION\nstep 30: out-of-scope feature",
                         font=DISPLAY, color=CRIMSON, font_size=14, weight="BOLD")
        viol_text.move_to(viol_rect.get_center())
        if viol_text.width > 3.7:
            viol_text.scale_to_fit_width(3.7)
        violation_box = VGroup(viol_rect, viol_text)

        # Arrow from step 7 node (y=0, x=2.5) down to violation box top
        arrow_start = step7_center + DOWN * 0.25
        arrow_end = viol_rect.get_top()
        arrow = Line(arrow_start, arrow_end, color=CRIMSON, stroke_width=2)
        arrow.add_tip(tip_length=0.2)

        # DashedLine from violation box top-left back to step 7 node
        dashed = DashedLine(
            viol_rect.get_corner(UL),
            step7_center,
            stroke_color=CRIMSON,
            dash_length=0.1,
            stroke_width=1.5
        )

        # Caption at y=-3.0
        caption_text = Text("EI gap → 23-prompt correction cycle",
                            font=DISPLAY, color=SLATE_COL, font_size=16,
                            weight="BOLD")
        caption_text.move_to(DOWN * 3.0)
        caption_bg = Rectangle(
            width=caption_text.width + 0.3,
            height=caption_text.height + 0.15
        ).set_fill(CREAM, opacity=1).set_stroke(width=0, opacity=0)
        caption_bg.move_to(caption_text.get_center())

        # Animation sequence (6 states)
        # 1. Title + timeline (fast)
        self.play(FadeIn(title), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.06, run_time=0.7),
            LaggedStart(*[Create(c) for c in connectors], lag_ratio=0.06, run_time=0.6),
            LaggedStart(*[FadeIn(l) for l in cap_labels], lag_ratio=0.1, run_time=0.5),
        )
        # 2. Step 7 turns gray (animate to confirm it's EI gap)
        self.play(nodes[6][0].animate.set_fill(SLATE_COL), run_time=0.5)
        # 3. Arrow appears pointing down to violation area
        self.play(Create(arrow), run_time=0.6)
        # 4. Violation box appears
        self.play(FadeIn(violation_box), run_time=0.5)
        # 5. DashedLine appears connecting violation back to step 7
        self.play(Create(dashed), run_time=0.6)
        # 6. Caption appears
        self.play(FadeIn(caption_bg), FadeIn(caption_text), run_time=0.5)

        self.wait(max(0.5, total - 4.4))
