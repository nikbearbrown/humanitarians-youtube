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


class B04_UnitMismatch(Scene):
    def construct(self):
        def tick_label(txt, pos, fontsize=18, color=SLATE):
            bg = Rectangle(
                width=max(len(txt)*0.118, 0.4)+0.15, height=0.34,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            ).move_to(pos)
            t = Text(txt, font_size=fontsize, color=color).move_to(pos)
            return VGroup(bg, t)

        # Title
        title = Text(
            "UNIT MISMATCH — MARS CLIMATE ORBITER ($325M)",
            font_size=24, color=INK, weight=BOLD
        ).move_to((0, 3.2, 0))

        # --- Pipeline nodes ---
        # Thruster node (left) at x=-4.0, y=0.8
        thruster_box = Rectangle(width=2.5, height=1.0,
                                 fill_color=SLATE, fill_opacity=1,
                                 stroke_width=0, stroke_opacity=0
                                 ).move_to((-4.0, 0.8, 0))
        thruster_name = Text("THRUSTER", font_size=20, color=CREAM, weight=BOLD
                             ).move_to((-4.0, 1.05, 0))
        thruster_val  = Text("18.9 lbf·s", font_size=17, color=GOLD
                             ).move_to((-4.0, 0.58, 0))
        thruster_node = thruster_box
        thruster_labels = VGroup(thruster_name, thruster_val)

        # Interface gate (center) at x=0.0, y=0.8 — CRIMSON box
        gate_box = Rectangle(width=1.8, height=1.0,
                             fill_color=CRIMSON, fill_opacity=1,
                             stroke_width=0, stroke_opacity=0
                             ).move_to((0.0, 0.8, 0))
        gate_lbl = Text("UNIT\nMISMATCH", font_size=16, color=CREAM, weight=BOLD
                        ).move_to((0.0, 0.8, 0))
        gate_node = gate_box
        gate_labels = VGroup(gate_lbl)

        # Big X above gate
        x_bg = Rectangle(width=0.6, height=0.65, fill_color=CREAM, fill_opacity=1,
                         stroke_width=0, stroke_opacity=0).move_to((0.0,1.55,0))
        x_mark_txt = Text("X", font_size=44, color=CRIMSON, weight=BOLD).move_to((0.0,1.55,0))
        x_mark = VGroup(x_bg, x_mark_txt)
        gate_labels.add(x_mark)

        # Navigation node (right) at x=4.0, y=0.8
        nav_box = Rectangle(width=2.5, height=1.0,
                            fill_color=SLATE, fill_opacity=1,
                            stroke_width=0, stroke_opacity=0
                            ).move_to((4.0, 0.8, 0))
        nav_lbl = Text("NAVIGATION", font_size=18, color=CREAM).move_to((4.0, 0.8, 0))
        nav_node = nav_box

        # Arrows
        interface_arrow = Arrow(
            (-2.7, 0.8, 0), (-0.95, 0.8, 0),
            color=CRIMSON, buff=0, stroke_width=3,
            max_tip_length_to_length_ratio=0.18
        )
        nav_arrow = Arrow(
            (0.95, 0.8, 0), (2.7, 0.8, 0),
            color=CRIMSON, buff=0, stroke_width=3,
            max_tip_length_to_length_ratio=0.18
        )

        lbf_label   = tick_label("lbf·s",         (-1.85, 1.2, 0), fontsize=19, color=CRIMSON)
        treating_as = tick_label("treating as N·s", (1.85, 1.2, 0), fontsize=17, color=CRIMSON)
        treating_as_label = treating_as

        # --- Trajectory chart (below pipeline) ---
        # y range -1.2 to -3.0
        expected_path = DashedLine(
            (-5.0,-1.6,0),(5.0,-1.6,0),
            color=PASS_CLR, stroke_width=2.5, dash_length=0.15
        )
        actual_path = Line(
            (-5.0,-1.6,0),(5.0,-3.0,0),
            color=CRIMSON, stroke_width=2.5
        )

        # Labels for paths — avoid placing label at line endpoint
        # "Expected path": left anchor, not near line ends
        exp_lbl  = tick_label("Expected path", (-3.5,-1.35,0), fontsize=17, color=PASS_CLR)
        # "Actual path": anchor left side, line end at (5,-3) so left is safe
        act_lbl  = tick_label("Actual path",   (-3.5,-2.35,0), fontsize=17, color=CRIMSON)
        path_labels = VGroup(exp_lbl, act_lbl)

        # Place "lost here" label ABOVE the actual_path line at this x position
        # At x=0, line is at y≈-2.2; y=-1.9 is above the line and clear
        lost_bg = Rectangle(width=3.2, height=0.36, fill_color=CREAM, fill_opacity=1,
                            stroke_width=0, stroke_opacity=0).move_to((0.0,-1.95,0))
        lost_txt = Text("Mars Orbiter lost here", font_size=18, color=CRIMSON).move_to((0.0,-1.95,0))

        # Verdict — single line at safe y; combine both messages
        verdict_bg = Rectangle(width=9.0, height=0.38, fill_color=CREAM, fill_opacity=1,
                                stroke_width=0, stroke_opacity=0).move_to((0,-3.15,0))
        verdict_txt = Text("1 lbf = 4.44822 N — a labeled interface catches what an unlabeled one buries",
                           font_size=18, color=CRIMSON, weight=BOLD).move_to((0,-3.15,0))
        verdict_text = VGroup(verdict_bg, verdict_txt)
        conversion_annotation = verdict_text

        # --- Sequence (7 play() calls) ---
        self.play(Write(title))
        self.play(FadeIn(thruster_node), Write(thruster_labels))
        self.play(FadeIn(interface_arrow), Write(lbf_label))
        self.play(FadeIn(gate_node), Write(gate_labels))
        self.play(
            FadeIn(nav_arrow), Write(treating_as_label),
            FadeIn(nav_node), Write(nav_lbl)
        )
        self.play(
            FadeIn(expected_path), FadeIn(actual_path),
            Write(path_labels), FadeIn(lost_bg), Write(lost_txt)
        )
        self.play(Write(conversion_annotation), Write(verdict_text))
        self.wait(1)
