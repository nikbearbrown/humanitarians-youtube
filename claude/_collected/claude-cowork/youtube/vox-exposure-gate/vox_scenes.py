import sys, pathlib, os, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {}
try:
    _data = json.load(open(os.path.join(os.path.dirname(__file__), "beat_sheet.json")))
    DUR = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 10.0)
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 15)}


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        t1 = Text("Why Checking the Output", font=SERIF, color=INK, font_size=44, weight=BOLD)
        t2 = Text("Won't Save You", font=SERIF, color=INK, font_size=44, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.15).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        u.set_stroke(opacity=1)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(block, shift=UP * 0.1), Create(u), run_time=1.1)
        self.wait(max(0.5, total - 1.6))


class B03_TheQuestion(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Reviewing the output before you act should let you catch the problem. "
            "By the time an output exists, the exposure is already behind you. "
            "Why doesn't the review protect you?",
            "— the question this film answers",
            None,
            "Why?",
            DUR["B03"],
        )


class B04_Pipeline(Scene):
    def construct(self):
        total = DUR["B04"]
        labels = ["FILE IN", "SESSION", "OUTPUT", "REVIEW"]
        boxes = VGroup()
        for lbl in labels:
            rect = RoundedRectangle(width=2.0, height=0.9, corner_radius=0.12,
                                    color=SLATE, fill_opacity=0)
            rect.set_stroke(color=SLATE, width=2, opacity=1)
            txt = Text(lbl, font=DISPLAY, color=SLATE, font_size=22)
            g = VGroup(rect, txt)
            boxes.add(g)
        boxes.arrange(RIGHT, buff=0.55).move_to(ORIGIN)
        arrows = VGroup()
        for i in range(len(boxes) - 1):
            a = Arrow(
                boxes[i][0].get_right(),
                boxes[i + 1][0].get_left(),
                buff=0.05, color=SLATE, stroke_width=2,
            )
            arrows.add(a)
        self.play(FadeIn(boxes[0], shift=RIGHT * 0.1), run_time=0.4)
        for i in range(len(arrows)):
            self.play(GrowArrow(arrows[i]), FadeIn(boxes[i + 1], shift=RIGHT * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 0.4 * (len(labels) + len(arrows) - 1) - 0.4))


class B05_ExposureAt(Scene):
    def construct(self):
        total = DUR["B05"]
        labels = ["FILE IN", "SESSION", "OUTPUT", "REVIEW"]
        colors = [CRIMSON, CRIMSON, SLATE, SLATE]
        opacities = [1.0, 1.0, 0.35, 0.35]
        boxes = VGroup()
        for lbl, col, op in zip(labels, colors, opacities):
            rect = RoundedRectangle(width=2.0, height=0.9, corner_radius=0.12,
                                    color=col, fill_opacity=0)
            rect.set_stroke(color=col, width=2, opacity=op)
            txt = Text(lbl, font=DISPLAY, color=col, font_size=22)
            txt.set_opacity(op)
            g = VGroup(rect, txt)
            boxes.add(g)
        boxes.arrange(RIGHT, buff=0.55).move_to(UP * 0.3)
        arrows = VGroup()
        for i in range(len(boxes) - 1):
            a_col = CRIMSON if i == 0 else SLATE
            a_op = 1.0 if i == 0 else 0.35
            a = Arrow(
                boxes[i][0].get_right(),
                boxes[i + 1][0].get_left(),
                buff=0.05, color=a_col, stroke_width=2,
            )
            a.set_stroke(opacity=a_op)
            arrows.add(a)
        exp_lbl = LabelChip("EXPOSURE HERE", accent=CRIMSON, size=20)
        exp_lbl.next_to(boxes[0], DOWN, buff=0.35)
        too_late = Text("too late", font=SERIF, color=SLATE, font_size=22, slant=ITALIC)
        too_late.set_opacity(0.45)
        too_late.next_to(boxes[3], DOWN, buff=0.35)
        self.play(FadeIn(VGroup(*boxes, *arrows), shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(exp_lbl, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(too_late, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 1.7))


class B06_SectionMechanism(Scene):
    def construct(self):
        total = DUR["B06"]
        heading = Text("THE MECHANISM", font=DISPLAY, color=INK, font_size=48, weight=BOLD)
        sub = Text("hazard is the processing", font=SERIF, color=SLATE, font_size=28, slant=ITALIC)
        block = VGroup(heading, sub).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        self.play(FadeIn(heading, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.3, total - 0.9))


class B07_HazardNode(Scene):
    def construct(self):
        total = DUR["B07"]
        labels = ["FILE IN", "SESSION", "OUTPUT", "REVIEW"]
        box_colors = [SLATE, CRIMSON, SLATE, SLATE]
        boxes = VGroup()
        for lbl, col in zip(labels, box_colors):
            rect = RoundedRectangle(width=2.0, height=0.9, corner_radius=0.12,
                                    color=col, fill_opacity=0)
            rect.set_stroke(color=col, width=2, opacity=1)
            txt = Text(lbl, font=DISPLAY, color=col, font_size=22)
            g = VGroup(rect, txt)
            boxes.add(g)
        boxes.arrange(RIGHT, buff=0.55).move_to(UP * 0.4)
        arrows = VGroup()
        for i in range(len(boxes) - 1):
            a = Arrow(
                boxes[i][0].get_right(),
                boxes[i + 1][0].get_left(),
                buff=0.05, color=SLATE, stroke_width=2,
            )
            arrows.add(a)
        hazard_lbl = Text("HAZARD", font=DISPLAY, color=CRIMSON, font_size=20)
        hazard_lbl.next_to(boxes[1], DOWN, buff=0.28)
        dest_lbl = Text("destination", font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        dest_lbl.set_opacity(0.6)
        dest_lbl.next_to(boxes[2], DOWN, buff=0.28)
        self.play(FadeIn(VGroup(*boxes, *arrows), shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(hazard_lbl, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(dest_lbl, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 1.6))


class B08_KeyClaim(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Exposure occurs at ingestion. A review placed at the end sits downstream "
            "of the event it was meant to prevent.",
            "— the mechanism",
            None,
            "ingestion",
            DUR["B08"],
        )


class B09_GatePosition(Scene):
    def construct(self):
        total = DUR["B09"]
        pipe_labels = ["FILE IN", "SESSION", "OUTPUT", "REVIEW"]

        def make_row(highlight_idx, gate_before_idx, gate_col, row_label, row_col):
            boxes = VGroup()
            for i, lbl in enumerate(pipe_labels):
                col = row_col if i <= 1 else SLATE
                op = 1.0 if i <= 1 else 0.45
                rect = RoundedRectangle(width=1.6, height=0.7, corner_radius=0.1,
                                        color=col, fill_opacity=0)
                rect.set_stroke(color=col, width=1.5, opacity=op)
                txt = Text(lbl, font=DISPLAY, color=col, font_size=17)
                txt.set_opacity(op)
                g = VGroup(rect, txt)
                boxes.add(g)
            boxes.arrange(RIGHT, buff=0.4)
            arrows = VGroup()
            for i in range(len(boxes) - 1):
                a = Arrow(
                    boxes[i][0].get_right(),
                    boxes[i + 1][0].get_left(),
                    buff=0.04, color=SLATE, stroke_width=1.5,
                )
                a.set_stroke(opacity=0.45)
                arrows.add(a)
            gate = Text("▶ GATE", font=DISPLAY, color=gate_col, font_size=18)
            gate.next_to(boxes[gate_before_idx][0], UP, buff=0.18)
            lbl_chip = LabelChip(row_label, accent=gate_col, size=17)
            lbl_chip.next_to(boxes, LEFT, buff=0.3)
            return VGroup(lbl_chip, boxes, arrows, gate)

        row_a = make_row(3, 3, CRIMSON, "A: review-first", SLATE)
        row_b = make_row(0, 0, TEAL, "B: gate before", TEAL)
        rows = VGroup(row_a, row_b).arrange(DOWN, buff=0.65).move_to(ORIGIN)
        self.play(FadeIn(row_a, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(row_b, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 1.4))


class B11_Timeline(Scene):
    def construct(self):
        total = DUR["B11"]
        line = Line(LEFT * 4.5, RIGHT * 4.5, color=SLATE, stroke_width=2)
        line.set_stroke(opacity=0.5)
        times = [(-3.8, "2:00 PM", CRIMSON, "FILE IN\nEXPOSURE", 1.0),
                 (0.0,  "2:04",    SLATE,   "OUTPUT",           0.6),
                 (3.6,  "2:06",    SLATE,   "REVIEW",           0.6)]
        dots = VGroup()
        time_labels = VGroup()
        event_labels = VGroup()
        for x, t_str, col, ev, op in times:
            d = Dot(point=line.get_left() + RIGHT * (x + 4.5), radius=0.13,
                    color=col, fill_opacity=op)
            t_lbl = Text(t_str, font=MONO, color=col, font_size=20)
            t_lbl.set_opacity(op)
            t_lbl.next_to(d, UP, buff=0.22)
            ev_lbl = Text(ev, font=SERIF, color=col, font_size=18, line_spacing=1.2)
            ev_lbl.set_opacity(op)
            ev_lbl.next_to(d, DOWN, buff=0.22)
            dots.add(d)
            time_labels.add(t_lbl)
            event_labels.add(ev_lbl)
        illus = LabelChip("illustrative", accent=SLATE, size=17)
        illus.set_opacity(0.55)
        illus.move_to(DOWN * 2.2)
        self.play(Create(line), run_time=0.5)
        self.play(FadeIn(dots[0], shift=UP * 0.1), FadeIn(time_labels[0]), FadeIn(event_labels[0]), run_time=0.5)
        self.play(FadeIn(dots[1], shift=UP * 0.1), FadeIn(time_labels[1]), FadeIn(event_labels[1]), run_time=0.4)
        self.play(FadeIn(dots[2], shift=UP * 0.1), FadeIn(time_labels[2]), FadeIn(event_labels[2]), run_time=0.4)
        self.play(FadeIn(illus, shift=UP * 0.1), run_time=0.3)
        self.wait(max(0.5, total - 2.1))


class B12_GateMoved(Scene):
    def construct(self):
        total = DUR["B12"]
        line = Line(LEFT * 4.5, RIGHT * 4.5, color=SLATE, stroke_width=2)
        line.set_stroke(opacity=0.5)
        times = [(-3.8, "2:00 PM", CRIMSON, "EXPOSURE", 1.0),
                 (0.0,  "2:04",    SLATE,   "OUTPUT",   0.5),
                 (3.6,  "2:06",    SLATE,   "REVIEW",   0.5)]
        dots = VGroup()
        time_labels = VGroup()
        event_labels = VGroup()
        for x, t_str, col, ev, op in times:
            d = Dot(point=line.get_left() + RIGHT * (x + 4.5), radius=0.13,
                    color=col, fill_opacity=op)
            t_lbl = Text(t_str, font=MONO, color=col, font_size=20)
            t_lbl.set_opacity(op)
            t_lbl.next_to(d, UP, buff=0.22)
            ev_lbl = Text(ev, font=SERIF, color=col, font_size=18)
            ev_lbl.set_opacity(op)
            ev_lbl.next_to(d, DOWN, buff=0.22)
            dots.add(d)
            time_labels.add(t_lbl)
            event_labels.add(ev_lbl)
        gate_sym = Text("▶ GATE", font=DISPLAY, color=TEAL, font_size=20)
        gate_sym.next_to(dots[0], UP, buff=0.7)
        gate_line = DashedLine(gate_sym.get_bottom() + DOWN * 0.1, dots[0].get_top() + UP * 0.05,
                               color=TEAL, dash_length=0.12)
        gate_line.set_stroke(opacity=0.8)
        gate_lbl = Text("effective gate position", font=SERIF, color=TEAL, font_size=18)
        gate_lbl.next_to(gate_sym, RIGHT, buff=0.2)
        illus = LabelChip("illustrative", accent=SLATE, size=17)
        illus.set_opacity(0.55)
        illus.move_to(DOWN * 2.5)
        self.play(Create(line), run_time=0.4)
        self.play(FadeIn(VGroup(*dots, *time_labels, *event_labels), shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(gate_sym, shift=DOWN * 0.1), Create(gate_line), run_time=0.6)
        self.play(FadeIn(gate_lbl, shift=LEFT * 0.1), FadeIn(illus), run_time=0.5)
        self.wait(max(0.5, total - 2.1))


class B13_Quote(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Moving the gate doesn't change what happened at ingestion.",
            "— the example",
            None,
            "ingestion",
            DUR["B13"],
        )


class B14_Endcard(Scene):
    def construct(self):
        total = DUR["B14"]
        copy = Text("The gate belongs before the file goes in.",
                    font=SERIF, color=INK, font_size=38, weight=BOLD)
        sub = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        u = Line(copy.get_corner(DL) + DOWN * 0.14, copy.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        u.set_stroke(opacity=1)
        block = VGroup(copy, u).move_to(UP * 0.15)
        sub.next_to(block, DOWN, buff=0.5)
        self.play(FadeIn(copy, shift=UP * 0.1), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.4))
