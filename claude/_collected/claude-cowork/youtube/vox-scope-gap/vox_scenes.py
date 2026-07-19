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
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 12)}


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        t1 = Text("Why Read-Only Access", font=SERIF, color=INK, font_size=40, weight=BOLD)
        t2 = Text("Still Leaks", font=SERIF, color=INK, font_size=40, weight=BOLD)
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
            "You granted read-only access. "
            "A never-sent draft email ended up quoted in the report. "
            "Why did read-only leak?",
            "— the question this film answers",
            None,
            "Why?",
            DUR["B03"],
        )


class B04_TwoCircles(Scene):
    def construct(self):
        total = DUR["B04"]

        # Large CRIMSON circle — entire account
        big_circle = Circle(radius=2.5, color=CRIMSON, fill_opacity=0.08)
        big_circle.set_stroke(color=CRIMSON, width=2, opacity=1)
        big_circle.move_to(ORIGIN)
        big_lbl = Text("entire account", font=MONO, color=CRIMSON, font_size=19)
        big_lbl.move_to(UP * 2.15)

        # Small TEAL circle — 3 files intended
        small_circle = Circle(radius=0.95, color=TEAL, fill_opacity=0.15)
        small_circle.set_stroke(color=TEAL, width=2.5, opacity=1)
        small_circle.move_to(LEFT * 0.6 + DOWN * 0.4)
        small_lbl = Text("3 files\nI meant", font=MONO, color=TEAL, font_size=17)
        small_lbl.move_to(LEFT * 0.6 + DOWN * 0.4)

        # Draft email dot in the gap
        email_dot = Dot(radius=0.14, color=CRIMSON, fill_opacity=0.9)
        email_dot.move_to(RIGHT * 1.6 + UP * 0.3)
        email_lbl = Text("draft email", font=MONO, color=CRIMSON, font_size=17)
        email_lbl.next_to(email_dot, RIGHT, buff=0.15)

        self.play(FadeIn(big_circle), FadeIn(big_lbl), run_time=0.5)
        self.play(FadeIn(small_circle), FadeIn(small_lbl), run_time=0.5)
        self.play(FadeIn(email_dot), FadeIn(email_lbl, shift=LEFT * 0.05), run_time=0.5)
        self.wait(max(0.3, total - 1.5))


class B05_SectionMechanism(Scene):
    def construct(self):
        total = DUR["B05"]
        heading = Text("THE MECHANISM", font=DISPLAY, color=INK, font_size=48, weight=BOLD)
        sub = Text("read access = read everything in scope", font=SERIF, color=SLATE, font_size=26, slant=ITALIC)
        block = VGroup(heading, sub).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        self.play(FadeIn(heading, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.3, total - 0.9))


class B06_GapMechanism(Scene):
    def construct(self):
        total = DUR["B06"]

        # Intended circle (TEAL, small, left)
        intended = Circle(radius=0.85, color=TEAL, fill_opacity=0.12)
        intended.set_stroke(color=TEAL, width=2, opacity=1)
        intended.move_to(LEFT * 3.5)
        int_lbl = Text("intended", font=MONO, color=TEAL, font_size=17)
        int_lbl.move_to(LEFT * 3.5)

        # Granted circle (CRIMSON, larger, overlapping)
        granted = Circle(radius=1.6, color=CRIMSON, fill_opacity=0.06)
        granted.set_stroke(color=CRIMSON, width=2, opacity=1)
        granted.move_to(LEFT * 2.5)
        grant_lbl = Text("granted", font=MONO, color=CRIMSON, font_size=17)
        grant_lbl.move_to(LEFT * 1.6 + UP * 1.25)

        gap_label = Text("GAP", font=DISPLAY, color=CRIMSON, font_size=22, weight=BOLD)
        gap_label.move_to(LEFT * 1.3 + DOWN * 0.5)

        arrow = Arrow(LEFT * 0.9, RIGHT * 0.5, buff=0, color=CRIMSON, stroke_width=2.5)

        out_box = Rectangle(width=2.2, height=0.9, color=CRIMSON, fill_opacity=0.10)
        out_box.set_stroke(color=CRIMSON, width=1.5, opacity=1)
        out_box.move_to(RIGHT * 1.8)
        out_lbl = Text("leak", font=DISPLAY, color=CRIMSON, font_size=22)
        out_lbl.move_to(out_box.get_center())

        self.play(FadeIn(intended), FadeIn(int_lbl), run_time=0.4)
        self.play(FadeIn(granted), FadeIn(grant_lbl), run_time=0.4)
        self.play(FadeIn(gap_label), run_time=0.3)
        self.play(Create(arrow), FadeIn(out_box), FadeIn(out_lbl), run_time=0.6)
        self.wait(max(0.3, total - 1.7))


class B07_MechanismQuote(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Read access means read everything in scope. "
            "Read-only is not safe if the scope is too wide.",
            "— the mechanism",
            None,
            "everything",
            DUR["B07"],
        )


class B08_Example(Scene):
    def construct(self):
        total = DUR["B08"]

        task_lbl = Text("TASK", font=DISPLAY, color=SLATE, font_size=18)
        task_lbl.move_to(LEFT * 4.5 + UP * 2.0)
        task_items = VGroup(
            Text("program-report-1.pdf", font=MONO, color=TEAL, font_size=19),
            Text("program-report-2.pdf", font=MONO, color=TEAL, font_size=19),
            Text("program-report-3.pdf", font=MONO, color=TEAL, font_size=19),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        task_items.next_to(task_lbl, DOWN, buff=0.2)

        divider = Line(LEFT * 0.8 + UP * 2.6, LEFT * 0.8 + DOWN * 2.6,
                       color=SLATE, stroke_width=1)
        divider.set_stroke(opacity=0.35)

        account_lbl = Text("CONNECTED ACCOUNT", font=DISPLAY, color=CRIMSON, font_size=17)
        account_lbl.move_to(RIGHT * 2.5 + UP * 2.0)
        count_lbl = Text("~4,000 items", font=MONO, color=CRIMSON, font_size=19)
        count_lbl.next_to(account_lbl, DOWN, buff=0.2)
        email_item = Text("draft-funder-email.txt  ←", font=MONO, color=CRIMSON, font_size=20, weight=BOLD)
        email_item.next_to(count_lbl, DOWN, buff=0.3)

        arrow = Arrow(RIGHT * 2.2, RIGHT * 4.2, buff=0, color=CRIMSON, stroke_width=2)
        arrow.move_to(RIGHT * 3.2 + DOWN * 1.2)
        output_lbl = Text("quoted in summary", font=MONO, color=CRIMSON, font_size=18)
        output_lbl.next_to(arrow, DOWN, buff=0.15)

        illus = Text("illustrative", font=MONO, color=SLATE, font_size=15, slant=ITALIC)
        illus.to_corner(DR, buff=0.35)

        self.play(FadeIn(task_lbl), FadeIn(task_items), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(account_lbl), FadeIn(count_lbl), run_time=0.4)
        self.play(FadeIn(email_item, shift=LEFT * 0.05), run_time=0.4)
        self.play(Create(arrow), FadeIn(output_lbl), run_time=0.5)
        self.play(FadeIn(illus), run_time=0.3)
        self.wait(max(0.3, total - 2.4))


class B09_Quote(Scene):
    def construct(self):
        _quote_scene(
            self,
            "The permission was read-only. "
            "The scope was the whole account. "
            "The leak was the gap between them.",
            "— the example",
            None,
            "gap",
            DUR["B09"],
        )


class B10_Endcard(Scene):
    def construct(self):
        total = DUR["B10"]
        copy = Text("Read-only is not safe.\nIt is safe for the right scope.",
                    font=SERIF, color=INK, font_size=34, weight=BOLD)
        sub = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        u = Line(copy.get_corner(DL) + DOWN * 0.14, copy.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        u.set_stroke(opacity=1)
        block = VGroup(copy, u).move_to(UP * 0.15)
        sub.next_to(block, DOWN, buff=0.5)
        self.play(FadeIn(copy, shift=UP * 0.1), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.4))
