import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# vox-bainbridge-irony — Why More Automation Creates More Supervision Work, Not Less
# AGENTIC AI · ~150s · 10 beats
# Color law: TEAL = agent capability / automated work; CRIMSON = supervisory load / human decisions

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B02_SupervisoryAccumulate(Scene):
    """Four CRIMSON task chips accumulate below 'SUPERVISOR'."""

    def construct(self):
        title = Text("SUPERVISOR", font=DISPLAY, color=INK, font_size=34, weight="BOLD")
        title.to_edge(UP, buff=0.9)

        tasks = ["READ DIFF", "VERIFY TESTS", "CHECK EDGE CASES", "AUDIT SCOPE"]
        chips = VGroup()
        for task in tasks:
            lbl = Text(task, font=DISPLAY, color=INK, font_size=22, weight="BOLD")
            box = SurroundingRectangle(lbl, buff=0.18, color=CRIMSON,
                                       fill_color=CRIMSON, fill_opacity=0.25)
            chips.add(VGroup(box, lbl))
        chips.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        chips.next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)

        for chip in chips:
            self.play(FadeIn(chip, shift=RIGHT * 0.3), run_time=0.55)
            self.wait(0.4)

        count_lbl = SerifLabel("4 new decisions", accent=CRIMSON, size=28)
        count_lbl.next_to(chips, RIGHT, buff=0.8)
        self.play(FadeIn(count_lbl, shift=LEFT * 0.2), run_time=0.6)
        self.wait(5.5)


class B04_NaiveScale(Scene):
    """Lever-scale: capability arm rises (TEAL), workload arm falls (CRIMSON) — naive model."""

    def construct(self):
        # Fulcrum (triangle)
        fulcrum = Triangle(fill_color=SLATE, fill_opacity=1, stroke_width=0)
        fulcrum.scale(0.4).move_to(DOWN * 1.0)

        # Lever bar (horizontal line at equilibrium)
        lever = Line(LEFT * 4.5 + DOWN * 0.3, RIGHT * 4.5 + DOWN * 0.3,
                     stroke_width=5, color=INK)
        lever.move_to(DOWN * 0.3)

        # Left weight (TEAL - capability)
        cap_box = Rectangle(width=2.4, height=0.9)
        cap_box.set_fill(TEAL, 0.25).set_stroke(TEAL, 2)
        cap_lbl = Text("agent capability", font=DISPLAY, color=INK, font_size=20)
        cap_lbl.move_to(cap_box)
        cap_weight = VGroup(cap_box, cap_lbl)
        cap_weight.next_to(lever.get_left(), DOWN, buff=0.1)

        # Right weight (CRIMSON - workload)
        work_box = Rectangle(width=2.4, height=0.9)
        work_box.set_fill(CRIMSON, 0.25).set_stroke(CRIMSON, 2)
        work_lbl = Text("human workload", font=DISPLAY, color=INK, font_size=20)
        work_lbl.move_to(work_box)
        work_weight = VGroup(work_box, work_lbl)
        work_weight.next_to(lever.get_right(), DOWN, buff=0.1)

        naive_lbl = SerifLabel("naive model", accent=SLATE, size=24)
        naive_lbl.to_edge(DOWN, buff=0.5)

        self.play(Create(fulcrum), Create(lever), run_time=0.7)
        self.play(FadeIn(cap_weight, shift=DOWN * 0.2),
                  FadeIn(work_weight, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(naive_lbl, shift=UP * 0.1), run_time=0.4)

        # Animate: left (capability) rises up, right (workload) goes down — naive expectation
        self.play(
            cap_weight.animate.shift(UP * 1.2),
            work_weight.animate.shift(DOWN * 1.2),
            run_time=2.0
        )
        self.wait(7.0)


class B06_RealScale(Scene):
    """Both lever arms rise together — Bainbridge's Irony."""

    def construct(self):
        # Fulcrum
        fulcrum = Triangle(fill_color=SLATE, fill_opacity=1, stroke_width=0)
        fulcrum.scale(0.4).move_to(DOWN * 1.0)

        # Lever
        lever = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=5, color=INK)
        lever.move_to(DOWN * 0.3)

        # Left weight (TEAL)
        cap_box = Rectangle(width=2.4, height=0.9)
        cap_box.set_fill(TEAL, 0.25).set_stroke(TEAL, 2)
        cap_lbl = Text("agent capability", font=DISPLAY, color=INK, font_size=20)
        cap_lbl.move_to(cap_box)
        cap_weight = VGroup(cap_box, cap_lbl)
        cap_weight.next_to(lever.get_left(), DOWN, buff=0.1)

        # Right weight (CRIMSON)
        work_box = Rectangle(width=2.4, height=0.9)
        work_box.set_fill(CRIMSON, 0.25).set_stroke(CRIMSON, 2)
        work_lbl = Text("supervisory load", font=DISPLAY, color=INK, font_size=20)
        work_lbl.move_to(work_box)
        work_weight = VGroup(work_box, work_lbl)
        work_weight.next_to(lever.get_right(), DOWN, buff=0.1)

        real_lbl = SerifLabel("Bainbridge's Irony", accent=CRIMSON, size=24)
        real_lbl.to_edge(DOWN, buff=0.5)

        self.play(Create(fulcrum), Create(lever), run_time=0.7)
        self.play(FadeIn(cap_weight, shift=DOWN * 0.2),
                  FadeIn(work_weight, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(real_lbl, shift=UP * 0.1), run_time=0.4)

        # Both rise together — the irony
        self.play(
            cap_weight.animate.shift(UP * 1.0),
            work_weight.animate.shift(UP * 1.0),
            run_time=2.2
        )
        self.wait(7.5)


class B07_PriyaCompare(Scene):
    """Two columns: without agent (20 file squares, 20 decisions) vs with agent (robot + 5 decision chips)."""

    def construct(self):
        # Column headers
        without_hdr = Text("WITHOUT AGENT", font=DISPLAY, color=INK, font_size=26, weight="BOLD")
        with_hdr = Text("WITH AGENT", font=DISPLAY, color=INK, font_size=26, weight="BOLD")
        without_hdr.move_to(LEFT * 3.5 + UP * 3.0)
        with_hdr.move_to(RIGHT * 3.0 + UP * 3.0)

        # Divider
        divider = Line(UP * 3.5, DOWN * 3.5, stroke_width=1.5, color=SLATE)
        divider.move_to(ORIGIN)

        # Left: 20 TEAL file squares
        file_squares = VGroup()
        for i in range(20):
            sq = Square(0.28).set_fill(TEAL, 0.6).set_stroke(TEAL, 1.5)
            file_squares.add(sq)
        file_squares.arrange_in_grid(rows=4, cols=5, buff=0.1)
        file_squares.next_to(without_hdr, DOWN, buff=0.3)

        decisions_20 = SerifLabel("20 manual moves", accent=TEAL, size=20)
        decisions_20.next_to(file_squares, DOWN, buff=0.3)

        # Right: Robot icon (circle) + 5 CRIMSON decision chips
        robot = Circle(radius=0.5).set_fill(TEAL, 0.25).set_stroke(TEAL, 2)
        robot_lbl = Text("agent", font=DISPLAY, color=TEAL, font_size=18)
        robot_lbl.move_to(robot)
        robot_icon = VGroup(robot, robot_lbl)
        robot_icon.next_to(with_hdr, DOWN, buff=0.3)

        decision_names = ["SCOPE", "TAXONOMY", "BATCHES", "COUNTS", "AUDIT"]
        decision_chips = VGroup()
        for name in decision_names:
            lbl = Text(name, font=DISPLAY, color=INK, font_size=18, weight="BOLD")
            box = SurroundingRectangle(lbl, buff=0.12, color=CRIMSON,
                                       fill_color=CRIMSON, fill_opacity=0.25)
            decision_chips.add(VGroup(box, lbl))
        decision_chips.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        decision_chips.next_to(robot_icon, DOWN, buff=0.3)

        self.play(FadeIn(without_hdr, shift=UP * 0.2),
                  FadeIn(with_hdr, shift=UP * 0.2),
                  Create(divider), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(sq, scale=0.7) for sq in file_squares],
                               lag_ratio=0.03, run_time=1.5))
        self.play(FadeIn(decisions_20, shift=UP * 0.15), run_time=0.4)
        self.play(FadeIn(robot_icon, scale=0.8), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(chip, shift=RIGHT * 0.3) for chip in decision_chips],
                               lag_ratio=0.15, run_time=1.5))
        self.wait(5.0)


class B09_ScopeUpstream(Scene):
    """Timeline arrow with three zones: BEFORE (scope, wide), DURING (agent), AFTER (verify)."""

    def construct(self):
        # Main timeline arrow
        timeline = Arrow(LEFT * 6.0 + DOWN * 0.5, RIGHT * 6.0 + DOWN * 0.5,
                         buff=0, stroke_width=3, color=SLATE,
                         max_tip_length_to_length_ratio=0.06)

        # Zone boxes
        # BEFORE zone (wider, TEAL)
        before_box = Rectangle(width=4.0, height=2.2)
        before_box.set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        before_box.move_to(LEFT * 3.5 + UP * 0.8)

        before_title = Text("BEFORE", font=DISPLAY, color=TEAL, font_size=22, weight="BOLD")
        before_title.move_to(before_box.get_top() + DOWN * 0.25)

        before_items = VGroup(
            Text("define scope", font=SERIF, color=INK, font_size=18),
            Text("what it can touch", font=SERIF, color=INK, font_size=18),
            Text("what it must not touch", font=SERIF, color=INK, font_size=18),
        )
        before_items.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        before_items.next_to(before_title, DOWN, buff=0.15)

        # DURING zone (small, neutral)
        during_box = Rectangle(width=1.8, height=2.2)
        during_box.set_fill(SLATE, 0.1).set_stroke(SLATE, 1.5)
        during_box.move_to(ORIGIN + UP * 0.8)

        during_title = Text("DURING", font=DISPLAY, color=SLATE, font_size=20, weight="BOLD")
        during_title.move_to(during_box.get_top() + DOWN * 0.25)
        during_sub = Text("agent runs", font=SERIF, color=SLATE, font_size=16, slant=ITALIC)
        during_sub.next_to(during_title, DOWN, buff=0.2)

        # AFTER zone (CRIMSON)
        after_box = Rectangle(width=3.5, height=2.2)
        after_box.set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 2)
        after_box.move_to(RIGHT * 4.2 + UP * 0.8)

        after_title = Text("AFTER", font=DISPLAY, color=CRIMSON, font_size=22, weight="BOLD")
        after_title.move_to(after_box.get_top() + DOWN * 0.25)
        after_sub = Text("verify output", font=SERIF, color=INK, font_size=18)
        after_sub.next_to(after_title, DOWN, buff=0.2)

        self.play(Create(timeline), run_time=0.6)
        self.play(Create(before_box), FadeIn(before_title, shift=DOWN * 0.1), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(item, shift=RIGHT * 0.15) for item in before_items],
                               lag_ratio=0.2, run_time=1.0))
        self.play(Create(during_box), FadeIn(during_title, shift=DOWN * 0.1),
                  FadeIn(during_sub, shift=DOWN * 0.1), run_time=0.5)
        self.play(Create(after_box), FadeIn(after_title, shift=DOWN * 0.1),
                  FadeIn(after_sub, shift=DOWN * 0.1), run_time=0.5)
        self.wait(7.0)
