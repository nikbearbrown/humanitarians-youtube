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
        t1 = Text("Why a Model Can't", font=SERIF, color=INK, font_size=40, weight=BOLD)
        t2 = Text("Catch Its Own Mistake", font=SERIF, color=INK, font_size=40, weight=BOLD)
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
            "A verification step should catch the error. "
            "The model verified its own output and approved the error. "
            "Why can't it audit itself?",
            "— the question this film answers",
            None,
            "Why?",
            DUR["B03"],
        )


class B04_FirstPass(Scene):
    def construct(self):
        total = DUR["B04"]

        src_box = Rectangle(width=2.2, height=0.9, color=TEAL, fill_opacity=0.10)
        src_box.set_stroke(color=TEAL, width=2, opacity=1)
        src_box.move_to(LEFT * 4.0)
        src_lbl = Text("SOURCE", font=DISPLAY, color=TEAL, font_size=18)
        src_lbl.move_to(src_box.get_center())

        model_box = Rectangle(width=2.2, height=0.9, color=CRIMSON, fill_opacity=0.10)
        model_box.set_stroke(color=CRIMSON, width=2, opacity=1)
        model_box.move_to(ORIGIN)
        model_lbl = Text("MODEL", font=DISPLAY, color=CRIMSON, font_size=18)
        model_lbl.move_to(model_box.get_center())

        out_box = Rectangle(width=2.4, height=0.9, color=CRIMSON, fill_opacity=0.10)
        out_box.set_stroke(color=CRIMSON, width=2, opacity=1)
        out_box.move_to(RIGHT * 4.0)
        out_lbl = Text("wrong\ncitation", font=MONO, color=CRIMSON, font_size=17)
        out_lbl.move_to(out_box.get_center())

        arr1 = Arrow(LEFT * 2.8, LEFT * 1.2, buff=0, color=SLATE, stroke_width=2)
        arr2 = Arrow(RIGHT * 1.2, RIGHT * 2.8, buff=0, color=CRIMSON, stroke_width=2)

        error_lbl = Text("✗ error", font=MONO, color=CRIMSON, font_size=18)
        error_lbl.next_to(out_box, DOWN, buff=0.2)

        self.play(FadeIn(src_box), FadeIn(src_lbl), run_time=0.4)
        self.play(FadeIn(model_box), FadeIn(model_lbl), Create(arr1), run_time=0.5)
        self.play(FadeIn(out_box), FadeIn(out_lbl), Create(arr2), run_time=0.5)
        self.play(FadeIn(error_lbl, shift=UP * 0.05), run_time=0.4)
        self.wait(max(0.3, total - 1.8))


class B05_SameReading(Scene):
    def construct(self):
        total = DUR["B05"]

        out_box = Rectangle(width=2.4, height=0.9, color=CRIMSON, fill_opacity=0.10)
        out_box.set_stroke(color=CRIMSON, width=2, opacity=1)
        out_box.move_to(LEFT * 4.0)
        out_lbl = Text("wrong\ncitation", font=MONO, color=CRIMSON, font_size=17)
        out_lbl.move_to(out_box.get_center())

        model_box2 = Rectangle(width=2.2, height=0.9, color=CRIMSON, fill_opacity=0.10)
        model_box2.set_stroke(color=CRIMSON, width=2, opacity=1)
        model_box2.move_to(ORIGIN)
        model_lbl2 = Text("MODEL\n(same)", font=DISPLAY, color=CRIMSON, font_size=16)
        model_lbl2.move_to(model_box2.get_center())

        verify_box = Rectangle(width=2.4, height=0.9, color=CRIMSON, fill_opacity=0.15)
        verify_box.set_stroke(color=CRIMSON, width=2, opacity=1)
        verify_box.move_to(RIGHT * 4.0)
        verify_lbl = Text("VERIFIED\n✗ error", font=MONO, color=CRIMSON, font_size=17)
        verify_lbl.move_to(verify_box.get_center())

        arr1 = Arrow(LEFT * 2.8, LEFT * 1.2, buff=0, color=CRIMSON, stroke_width=2)
        arr2 = Arrow(RIGHT * 1.2, RIGHT * 2.8, buff=0, color=CRIMSON, stroke_width=2)

        verify_step = Text("VERIFY STEP", font=DISPLAY, color=SLATE, font_size=18)
        verify_step.move_to(UP * 2.0)

        self.play(FadeIn(verify_step), run_time=0.3)
        self.play(FadeIn(out_box), FadeIn(out_lbl), run_time=0.4)
        self.play(FadeIn(model_box2), FadeIn(model_lbl2), Create(arr1), run_time=0.5)
        self.play(FadeIn(verify_box), FadeIn(verify_lbl), Create(arr2), run_time=0.5)
        self.wait(max(0.3, total - 1.7))


class B06_SectionMechanism(Scene):
    def construct(self):
        total = DUR["B06"]
        heading = Text("THE MECHANISM", font=DISPLAY, color=INK, font_size=48, weight=BOLD)
        sub = Text("same weights, same blind spots", font=SERIF, color=SLATE, font_size=28, slant=ITALIC)
        block = VGroup(heading, sub).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        self.play(FadeIn(heading, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.3, total - 0.9))


class B07_SameWeights(Scene):
    def construct(self):
        total = DUR["B07"]

        weights_box = Rectangle(width=2.8, height=1.1, color=CRIMSON, fill_opacity=0.15)
        weights_box.set_stroke(color=CRIMSON, width=2.5, opacity=1)
        weights_box.move_to(ORIGIN)
        weights_lbl = Text("WEIGHTS", font=DISPLAY, color=CRIMSON, font_size=24, weight=BOLD)
        weights_lbl.move_to(weights_box.get_center())

        produce_box = Rectangle(width=2.6, height=0.9, color=CRIMSON, fill_opacity=0.10)
        produce_box.set_stroke(color=CRIMSON, width=1.5, opacity=1)
        produce_box.move_to(LEFT * 3.8 + DOWN * 1.0)
        produce_lbl = Text("produce\noutput", font=MONO, color=CRIMSON, font_size=18)
        produce_lbl.move_to(produce_box.get_center())

        audit_box = Rectangle(width=2.6, height=0.9, color=CRIMSON, fill_opacity=0.10)
        audit_box.set_stroke(color=CRIMSON, width=1.5, opacity=1)
        audit_box.move_to(RIGHT * 3.8 + DOWN * 1.0)
        audit_lbl = Text("audit\noutput", font=MONO, color=CRIMSON, font_size=18)
        audit_lbl.move_to(audit_box.get_center())

        arr_left = Arrow(LEFT * 0.9 + DOWN * 0.3, LEFT * 2.6 + DOWN * 0.8,
                         buff=0, color=CRIMSON, stroke_width=2)
        arr_right = Arrow(RIGHT * 0.9 + DOWN * 0.3, RIGHT * 2.6 + DOWN * 0.8,
                          buff=0, color=CRIMSON, stroke_width=2)

        same_lbl = Text("same source", font=MONO, color=SLATE, font_size=16, slant=ITALIC)
        same_lbl.move_to(DOWN * 2.4)

        self.play(FadeIn(weights_box), FadeIn(weights_lbl), run_time=0.5)
        self.play(Create(arr_left), FadeIn(produce_box), FadeIn(produce_lbl), run_time=0.5)
        self.play(Create(arr_right), FadeIn(audit_box), FadeIn(audit_lbl), run_time=0.5)
        self.play(FadeIn(same_lbl, shift=UP * 0.05), run_time=0.4)
        self.wait(max(0.3, total - 1.9))


class B08_MechanismQuote(Scene):
    def construct(self):
        _quote_scene(
            self,
            "The same weights that produced the output are the weights doing the audit. "
            "A model cannot step outside its own patterns.",
            "— the mechanism",
            None,
            "cannot",
            DUR["B08"],
        )


class B09_BlindSpot(Scene):
    def construct(self):
        total = DUR["B09"]

        model_circle = Circle(radius=1.8, color=CRIMSON, fill_opacity=0.08)
        model_circle.set_stroke(color=CRIMSON, width=2, opacity=1)
        model_circle.move_to(ORIGIN)
        model_lbl = Text("MODEL", font=DISPLAY, color=CRIMSON, font_size=20)
        model_lbl.move_to(UP * 0.55)

        error_dot = Dot(radius=0.18, color=CRIMSON, fill_opacity=0.9)
        error_dot.move_to(DOWN * 0.45 + LEFT * 0.5)
        error_lbl = Text("error", font=MONO, color=CRIMSON, font_size=16)
        error_lbl.next_to(error_dot, RIGHT, buff=0.12)

        blind_lbl = Text("blind spot", font=MONO, color=CRIMSON, font_size=16, slant=ITALIC)
        blind_lbl.next_to(error_dot, DOWN, buff=0.25)

        human_lbl = Text("HUMAN", font=DISPLAY, color=TEAL, font_size=22, weight=BOLD)
        human_lbl.move_to(RIGHT * 3.8)
        human_sees = Text("sees the error", font=MONO, color=TEAL, font_size=18)
        human_sees.next_to(human_lbl, DOWN, buff=0.2)
        arr_human = Arrow(RIGHT * 3.0, RIGHT * 1.9 + DOWN * 0.1,
                          buff=0, color=TEAL, stroke_width=2)

        self.play(FadeIn(model_circle), FadeIn(model_lbl), run_time=0.5)
        self.play(FadeIn(error_dot), FadeIn(error_lbl), FadeIn(blind_lbl), run_time=0.5)
        self.play(FadeIn(human_lbl), FadeIn(human_sees), Create(arr_human), run_time=0.6)
        self.wait(max(0.3, total - 1.6))


class B11_Example(Scene):
    def construct(self):
        total = DUR["B11"]

        pass1_lbl = Text("PASS 1", font=DISPLAY, color=SLATE, font_size=16)
        pass1_lbl.move_to(LEFT * 4.5 + UP * 1.8)
        out1 = Text('"metric from Q3 report"', font=MONO, color=CRIMSON, font_size=20)
        out1.next_to(pass1_lbl, DOWN, buff=0.2)
        wrong1 = Text("✗ wrong", font=MONO, color=CRIMSON, font_size=16)
        wrong1.next_to(out1, DOWN, buff=0.12)

        divider = Line(LEFT * 0.5 + UP * 2.2, LEFT * 0.5 + DOWN * 2.2,
                       color=SLATE, stroke_width=1)
        divider.set_stroke(opacity=0.4)

        pass2_lbl = Text("VERIFY", font=DISPLAY, color=SLATE, font_size=16)
        pass2_lbl.move_to(RIGHT * 3.0 + UP * 1.8)
        out2 = Text('"CONFIRMED: Q3 report"', font=MONO, color=CRIMSON, font_size=20)
        out2.next_to(pass2_lbl, DOWN, buff=0.2)
        wrong2 = Text("✗ still wrong", font=MONO, color=CRIMSON, font_size=16)
        wrong2.next_to(out2, DOWN, buff=0.12)

        actual = Text("actual source: projection slide", font=SERIF, color=TEAL, font_size=19)
        actual.move_to(DOWN * 1.8)

        illus = Text("illustrative", font=MONO, color=SLATE, font_size=15, slant=ITALIC)
        illus.to_corner(DR, buff=0.35)

        self.play(FadeIn(pass1_lbl), FadeIn(out1), run_time=0.5)
        self.play(FadeIn(wrong1), run_time=0.3)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(pass2_lbl), FadeIn(out2), run_time=0.5)
        self.play(FadeIn(wrong2), run_time=0.3)
        self.play(FadeIn(actual, shift=UP * 0.05), run_time=0.5)
        self.play(FadeIn(illus), run_time=0.3)
        self.wait(max(0.3, total - 2.7))


class B12_OutsideCheck(Scene):
    def construct(self):
        total = DUR["B12"]

        loop_border = Circle(radius=1.6, color=CRIMSON, fill_opacity=0.06)
        loop_border.set_stroke(color=CRIMSON, width=2, opacity=1)
        loop_border.move_to(LEFT * 1.8)
        loop_lbl = Text("MODEL LOOP", font=MONO, color=CRIMSON, font_size=15)
        loop_lbl.move_to(LEFT * 1.8 + UP * 0.4)
        error_inside = Text("✗ error repeats", font=MONO, color=CRIMSON, font_size=16)
        error_inside.move_to(LEFT * 1.8 + DOWN * 0.3)

        human_box = Rectangle(width=2.4, height=1.0, color=TEAL, fill_opacity=0.12)
        human_box.set_stroke(color=TEAL, width=2, opacity=1)
        human_box.move_to(RIGHT * 3.8)
        human_lbl = Text("HUMAN\ncheck", font=DISPLAY, color=TEAL, font_size=20)
        human_lbl.move_to(human_box.get_center())

        outside_lbl = Text("outside the loop", font=MONO, color=TEAL, font_size=18)
        outside_lbl.next_to(human_box, DOWN, buff=0.25)

        arr_break = Arrow(RIGHT * 2.0, RIGHT * 2.6,
                          buff=0, color=TEAL, stroke_width=2.5)

        self.play(FadeIn(loop_border), FadeIn(loop_lbl), FadeIn(error_inside), run_time=0.6)
        self.play(FadeIn(human_box), FadeIn(human_lbl), run_time=0.5)
        self.play(Create(arr_break), FadeIn(outside_lbl), run_time=0.5)
        self.wait(max(0.3, total - 1.6))


class B13_Quote(Scene):
    def construct(self):
        _quote_scene(
            self,
            "The check that catches the mistake must come from outside the model.",
            "— the example",
            None,
            "outside",
            DUR["B13"],
        )


class B14_Endcard(Scene):
    def construct(self):
        total = DUR["B14"]
        copy = Text("The model verified its own error.\nThe check must come from outside.",
                    font=SERIF, color=INK, font_size=32, weight=BOLD)
        sub = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        u = Line(copy.get_corner(DL) + DOWN * 0.14, copy.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        u.set_stroke(opacity=1)
        block = VGroup(copy, u).move_to(UP * 0.15)
        sub.next_to(block, DOWN, buff=0.5)
        self.play(FadeIn(copy, shift=UP * 0.1), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.4))
