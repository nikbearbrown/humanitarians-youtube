from vox_graphics import *
import json, os
_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why Every Function You Add to a", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("Nanoparticle Is a New Way to Fail", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q_line1 = Text("Six functions. Each 90% reproducible.", font=SERIF, color=INK,
                        font_size=34, weight=BOLD)
        q_line2 = Text("Why does more than half of every batch fail?", font=SERIF,
                        color=CRIMSON, font_size=30)
        block = VGroup(q_line1, q_line2).arrange(DOWN, buff=0.35).move_to(UP * 0.2)
        sub = Text("the gap formula", font=SERIF, color=SLATE, font_size=22, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.5)
        # underline bar as real shape motion
        u = Line(q_line2.get_corner(DL) + DOWN * 0.1, q_line2.get_corner(DL) + DOWN * 0.1,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q_line1), run_time=0.8)
        self.play(FadeIn(q_line2, shift=DOWN * 0.15), run_time=0.7)
        self.add(u)
        self.play(u.animate.put_start_and_end_on(
            q_line2.get_corner(DL) + DOWN * 0.1,
            q_line2.get_corner(DR) + DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(max(0.3, total - 2.5))


class B04_GateMultiply(Scene):
    def construct(self):
        total = DUR["B04"]
        title = Text("Six gates -- all must open", font=DISPLAY, font_size=20, color=INK)
        title.move_to(UP * 3.1)
        gates = VGroup()
        labels_pct = VGroup()
        labels_fn = VGroup()
        gate_x = [-4.5, -2.7, -0.9, 0.9, 2.7, 4.5]
        for i, x in enumerate(gate_x):
            post_l = Rectangle(width=0.12, height=2.0, fill_color=CRIMSON,
                               fill_opacity=0.9, stroke_width=0).move_to(RIGHT * (x - 0.35) + UP * 0.5)
            post_r = Rectangle(width=0.12, height=2.0, fill_color=CRIMSON,
                               fill_opacity=0.9, stroke_width=0).move_to(RIGHT * (x + 0.35) + UP * 0.5)
            gate = VGroup(post_l, post_r)
            pct_lbl = Text("90%", font=MONO, font_size=18, color=INK
                          ).move_to(RIGHT * x + UP * 1.85)
            fn_lbl = Text(f"F{i+1}", font=DISPLAY, font_size=16, color=SLATE
                         ).move_to(RIGHT * x + DOWN * 0.6)
            gates.add(gate)
            labels_pct.add(pct_lbl)
            labels_fn.add(fn_lbl)
        self.play(Write(title), run_time=0.5)
        for gate, pct, fn in zip(gates, labels_pct, labels_fn):
            self.play(GrowFromEdge(gate[0], DOWN), GrowFromEdge(gate[1], DOWN),
                      FadeIn(pct), FadeIn(fn), run_time=0.4)
        arrow = Arrow(LEFT * 5.5 + DOWN * 0.05, RIGHT * 5.5 + DOWN * 0.05,
                      color=TEAL, stroke_width=3, buff=0)
        pass_lbl = Text("PASS", font=DISPLAY, font_size=16, color=TEAL
                       ).next_to(arrow, RIGHT, buff=0.15)
        self.play(Create(arrow), FadeIn(pass_lbl), run_time=0.7)
        self.wait(max(0.3, total - (0.5 + 6 * 0.4 + 0.7)))


class B05_YieldCollapse(Scene):
    def construct(self):
        total = DUR["B05"]
        steps = [("F1", 0.90), ("F2", 0.81), ("F3", 0.73),
                 ("F4", 0.66), ("F5", 0.59), ("F6", 0.53)]
        bars = VGroup()
        pct_labels = VGroup()
        fn_labels = VGroup()
        bar_w = 1.1
        max_h = 3.2
        for i, (name, val) in enumerate(steps):
            h = val * max_h
            bar = Rectangle(width=bar_w, height=h, fill_color=CRIMSON, fill_opacity=0.85,
                           stroke_width=0).move_to(RIGHT * (i * 1.55 - 3.875) + DOWN * (max_h - h) / 2 + DOWN * 0.3)
            pct = Text(f"{int(round(val * 100))}%", font=MONO, font_size=18, color=INK
                      ).next_to(bar, UP, buff=0.15)
            flbl = Text(name, font=DISPLAY, font_size=15, color=SLATE
                       ).next_to(bar, DOWN, buff=0.12)
            bars.add(bar)
            pct_labels.add(pct)
            fn_labels.add(flbl)
        title = Text("Batch yield as functions stack", font=DISPLAY, font_size=20, color=INK
                    ).move_to(UP * 3.1)
        ref_y = -0.3 + 0.9 * max_h / 2
        ref_line = DashedLine(LEFT * 4.5 + UP * ref_y, RIGHT * 4.5 + UP * ref_y,
                              color=TEAL, stroke_width=2, dash_length=0.18)
        ref_lbl = Text("90% baseline", font=DISPLAY, font_size=14, color=TEAL
                      ).next_to(ref_line, RIGHT, buff=0.1)
        self.play(Write(title), run_time=0.5)
        self.play(Create(ref_line), FadeIn(ref_lbl), run_time=0.5)
        for bar, pct, fn in zip(bars, pct_labels, fn_labels):
            self.play(GrowFromEdge(bar, DOWN), Write(pct), FadeIn(fn), run_time=0.55)
        self.wait(max(0.5, total - (1.0 + 6 * 0.55)))


class B06_MathCard(Scene):
    def construct(self):
        total = DUR["B06"]
        title = Text("The multiplication", font=DISPLAY, font_size=20, color=INK
                    ).move_to(UP * 3.0)
        line1_a = Text("0.9", font=MONO, font_size=52, color=CRIMSON)
        line1_exp = Text("6", font=MONO, font_size=30, color=CRIMSON)
        line1_eq = Text("= 53%", font=MONO, font_size=52, color=CRIMSON)
        line1_exp.next_to(line1_a, UR, buff=0.05).shift(DOWN * 0.1)
        line1 = VGroup(line1_a, line1_exp, line1_eq).arrange(RIGHT, buff=0.15).move_to(UP * 0.5)
        # gold highlighter bar — Create gives real shape motion (no chained .animate)
        hi_bar = Rectangle(width=line1_eq.width + 0.3, height=line1_eq.height + 0.18)
        hi_bar.set_fill(GOLD, 0.5).set_stroke(width=0)
        hi_bar.move_to(line1_eq).set_z_index(-1)
        line2_a = Text("0.95", font=MONO, font_size=36, color=SLATE)
        line2_exp = Text("6", font=MONO, font_size=22, color=SLATE)
        line2_eq = Text("= 74%", font=MONO, font_size=36, color=SLATE)
        line2_exp.next_to(line2_a, UR, buff=0.04).shift(DOWN * 0.07)
        line2 = VGroup(line2_a, line2_exp, line2_eq).arrange(RIGHT, buff=0.12).move_to(DOWN * 1.2)
        note = Text("(at 95% per-function quality -- still lose 1 batch in 4)",
                    font=SERIF, font_size=20, color=SLATE, slant=ITALIC)
        note.next_to(line2, DOWN, buff=0.3)
        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(line1_a), FadeIn(line1_exp), FadeIn(line1_eq), run_time=0.8)
        self.play(GrowFromCenter(hi_bar), run_time=0.6)
        self.play(FadeIn(line2, shift=DOWN * 0.15), FadeIn(note), run_time=0.7)
        self.wait(max(0.3, total - 2.6))


class B07_OneVsSix(Scene):
    def construct(self):
        total = DUR["B07"]
        title = Text("One function vs six functions", font=DISPLAY, font_size=20, color=INK
                    ).move_to(UP * 3.1)
        divider = Line(UP * 2.8, DOWN * 2.5, color=SLATE, stroke_width=1.5).move_to(ORIGIN)
        # Left: single-function (TEAL)
        left_lbl = Text("Doxil — 1 function", font=DISPLAY, font_size=17, color=TEAL
                       ).move_to(LEFT * 3.2 + UP * 2.2)
        left_bar_h = 0.9 * 2.8
        left_bar = Rectangle(width=1.4, height=left_bar_h, fill_color=TEAL, fill_opacity=0.85,
                             stroke_width=0).move_to(LEFT * 3.2 + DOWN * 0.3)
        left_pct = Text("90%", font=MONO, font_size=20, color=TEAL
                       ).next_to(left_bar, UP, buff=0.12)
        left_tag = Text("reached patients", font=SERIF, font_size=16, color=TEAL,
                       slant=ITALIC).next_to(left_bar, DOWN, buff=0.25)
        # Right: six-function (CRIMSON)
        right_lbl = Text("Six-function particle", font=DISPLAY, font_size=17, color=CRIMSON
                        ).move_to(RIGHT * 3.2 + UP * 2.2)
        steps = [0.90, 0.81, 0.73, 0.66, 0.59, 0.53]
        mini_bars = VGroup()
        bw = 0.45
        for i, val in enumerate(steps):
            h = val * 2.8
            b = Rectangle(width=bw, height=h, fill_color=CRIMSON, fill_opacity=0.8,
                          stroke_width=0).move_to(RIGHT * (i * 0.62 + 1.2) + DOWN * (2.8 - h) / 2 + DOWN * 0.3)
            mini_bars.add(b)
        right_pct = Text("53%", font=MONO, font_size=20, color=CRIMSON
                        ).next_to(mini_bars[-1], UP, buff=0.12)
        right_tag = Text("did not translate", font=SERIF, font_size=16, color=CRIMSON,
                        slant=ITALIC).next_to(mini_bars, DOWN, buff=0.25)
        self.play(Write(title), run_time=0.5)
        self.play(Create(divider), run_time=0.4)
        self.play(FadeIn(left_lbl), GrowFromEdge(left_bar, DOWN), FadeIn(left_pct), run_time=0.8)
        self.play(FadeIn(left_tag), run_time=0.4)
        self.play(FadeIn(right_lbl), run_time=0.4)
        for mb in mini_bars:
            self.play(GrowFromEdge(mb, DOWN), run_time=0.3)
        self.play(FadeIn(right_pct), FadeIn(right_tag), run_time=0.5)
        self.wait(max(0.3, total - (0.5 + 0.4 + 0.8 + 0.4 + 0.4 + 6 * 0.3 + 0.5)))


class B08_ImplicationCard(Scene):
    def construct(self):
        total = DUR["B08"]
        line1 = Text("Complexity is a design problem,", font=SERIF, color=INK,
                     font_size=36, weight=BOLD)
        line2 = Text("not a manufacturing problem.", font=SERIF, color=CRIMSON,
                     font_size=36, weight=BOLD)
        block = VGroup(line1, line2).arrange(DOWN, buff=0.22).move_to(UP * 0.3)
        sub = Text("no amount of process engineering fixes multiplicative math",
                   font=SERIF, font_size=20, color=SLATE, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.5)
        u = Line(line2.get_corner(DL) + DOWN * 0.1, line2.get_corner(DR) + DOWN * 0.1,
                 color=GOLD, stroke_width=2)
        self.play(FadeIn(line1), run_time=0.7)
        self.play(FadeIn(line2), Create(u), run_time=0.8)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(max(0.3, total - 2.0))


class B09_ProgramAB(Scene):
    def construct(self):
        total = DUR["B09"]
        title = Text("Same quality. Different economics.", font=DISPLAY, font_size=20, color=INK
                    ).move_to(UP * 3.1)
        # Program A (TEAL) — 11 pass, 1 fail from 12
        a_lbl = Text("Program A", font=DISPLAY, font_size=18, color=TEAL).move_to(LEFT * 3.2 + UP * 2.5)
        a_sub = Text("1 function", font=SERIF, font_size=15, color=TEAL, slant=ITALIC
                    ).next_to(a_lbl, DOWN, buff=0.08)
        a_batches = VGroup()
        for i in range(12):
            col = TEAL if i < 11 else CRIMSON
            sq = Square(0.38).set_fill(col, 0.85).set_stroke(width=0)
            sq.move_to(LEFT * (3.9 - (i % 6) * 0.55) + DOWN * (0.1 + (i // 6) * 0.55))
            a_batches.add(sq)
        a_count = Text("11 / 12 pass", font=MONO, font_size=16, color=TEAL
                      ).next_to(a_batches, DOWN, buff=0.2)
        # Program B (CRIMSON) — 7 pass, 5 fail from 12
        b_lbl = Text("Program B", font=DISPLAY, font_size=18, color=CRIMSON).move_to(RIGHT * 2.0 + UP * 2.5)
        b_sub = Text("6 functions", font=SERIF, font_size=15, color=CRIMSON, slant=ITALIC
                    ).next_to(b_lbl, DOWN, buff=0.08)
        b_batches = VGroup()
        for i in range(12):
            col = TEAL if i < 7 else CRIMSON
            sq = Square(0.38).set_fill(col, 0.85).set_stroke(width=0)
            sq.move_to(RIGHT * (1.3 + (i % 6) * 0.55) + DOWN * (0.1 + (i // 6) * 0.55))
            b_batches.add(sq)
        b_count = Text("7 / 12 pass", font=MONO, font_size=16, color=CRIMSON
                      ).next_to(b_batches, DOWN, buff=0.2)
        note = Text("(illustrative)", font=SERIF, font_size=14, color=SLATE, slant=ITALIC
                   ).move_to(DOWN * 2.8)
        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(a_lbl), FadeIn(a_sub), FadeIn(b_lbl), FadeIn(b_sub), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(sq, scale=0.8) for sq in a_batches],
                              lag_ratio=0.07, run_time=1.4))
        self.play(FadeIn(a_count), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(sq, scale=0.8) for sq in b_batches],
                              lag_ratio=0.07, run_time=1.4))
        self.play(FadeIn(b_count), FadeIn(note), run_time=0.5)
        self.wait(max(0.3, total - (0.5 + 0.6 + 1.4 + 0.4 + 1.4 + 0.5)))


class B10_DesignChoice(Scene):
    def construct(self):
        total = DUR["B10"]
        # Rebuild the batch grid from B09 as the starting state
        a_lbl = Text("Program A", font=DISPLAY, font_size=18, color=TEAL).move_to(LEFT * 3.2 + UP * 2.5)
        a_sub = Text("1 function", font=SERIF, font_size=15, color=TEAL, slant=ITALIC
                    ).next_to(a_lbl, DOWN, buff=0.08)
        a_batches = VGroup()
        for i in range(12):
            col = TEAL if i < 11 else CRIMSON
            sq = Square(0.38).set_fill(col, 0.85).set_stroke(width=0)
            sq.move_to(LEFT * (3.9 - (i % 6) * 0.55) + DOWN * (0.1 + (i // 6) * 0.55))
            a_batches.add(sq)
        b_lbl = Text("Program B", font=DISPLAY, font_size=18, color=CRIMSON).move_to(RIGHT * 2.0 + UP * 2.5)
        b_sub = Text("6 functions", font=SERIF, font_size=15, color=CRIMSON, slant=ITALIC
                    ).next_to(b_lbl, DOWN, buff=0.08)
        b_batches = VGroup()
        for i in range(12):
            col = TEAL if i < 7 else CRIMSON
            sq = Square(0.38).set_fill(col, 0.85).set_stroke(width=0)
            sq.move_to(RIGHT * (1.3 + (i % 6) * 0.55) + DOWN * (0.1 + (i // 6) * 0.55))
            b_batches.add(sq)
        # Add all to scene immediately
        self.add(a_lbl, a_sub, a_batches, b_lbl, b_sub, b_batches)
        # Annotation: group the failed B squares (indices 7-11)
        failed_group = VGroup(*[b_batches[i] for i in range(7, 12)])
        ring = HandRing(failed_group, color=CRIMSON)
        design_lbl = Text("design choice", font=SERIF, font_size=22, color=CRIMSON, slant=ITALIC)
        design_lbl.next_to(b_lbl, RIGHT, buff=0.5).shift(UP * 0.1)
        self.play(Create(ring), run_time=1.0)
        self.play(FadeIn(design_lbl, shift=LEFT * 0.2), run_time=0.6)
        self.wait(max(0.3, total - 1.6))


class B11_Endcard(Scene):
    def construct(self):
        total = DUR["B11"]
        topic = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        line1 = Text("More functions means more ways to fail.", font=SERIF,
                     color=INK, font_size=34, weight=BOLD)
        line2 = Text("Simple designs translate. Complex ones do not.", font=SERIF,
                     color=CRIMSON, font_size=28)
        block = VGroup(line1, line2).arrange(DOWN, buff=0.28).move_to(UP * 0.1)
        u = Line(line2.get_corner(DL) + DOWN * 0.1, line2.get_corner(DR) + DOWN * 0.1,
                 color=GOLD, stroke_width=2)
        topic.next_to(block, UP, buff=0.55)
        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(line1), run_time=0.8)
        self.play(FadeIn(line2), Create(u), run_time=0.8)
        self.wait(max(0.3, total - 2.1))
