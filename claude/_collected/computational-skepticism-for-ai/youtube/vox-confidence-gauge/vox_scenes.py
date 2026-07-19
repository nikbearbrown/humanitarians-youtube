import sys, json, pathlib, numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {
    "B01": 4.0,  "B02": 8.0, "B04": 8.5, "B05": 8.5,
    "B07": 8.5,  "B08": 8.5, "B09": 7.5, "B10": 8.5,
    "B11": 7.5,  "B12": 18.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
        for b in _BS["beats"]
    })
except Exception:
    pass


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("COMPUTATIONAL SKEPTICISM", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why Fluent Answers Make You", font=DISPLAY, color=INK, font_size=36, weight=BOLD)
        t2 = Text("Worse at Checking Them", font=DISPLAY, color=CRIMSON, font_size=36, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B02_AshReport(Scene):
    def construct(self):
        border = Rectangle(width=5.8, height=4.8, color=SLATE, fill_opacity=0.06)
        border.set_stroke(color=SLATE, width=2)
        border.move_to(UP * 0.3)
        header = LabelChip("AGENT REPORT", accent=SLATE).move_to(UP * 2.0)
        l1 = Text("Email deleted.", font=SERIF, color=INK).scale(0.65).move_to(UP * 0.9)
        l2 = Text("Account secured.", font=SERIF, color=INK).scale(0.65).move_to(UP * 0.1)
        l3 = Text("No errors detected.", font=SERIF, color=INK).scale(0.65).move_to(DOWN * 0.7)
        accept = LabelChip("ACCEPTED", accent=TEAL).move_to(DOWN * 2.1)
        self.play(GrowFromCenter(border))
        self.play(FadeIn(header))
        self.play(Create(l1), run_time=0.7)
        self.play(Create(l2), run_time=0.7)
        self.play(Create(l3), run_time=0.7)
        self.play(GrowFromCenter(accept))
        self.wait(max(0.3, DUR["B02"] - 5.8))


class B04_OldHeuristic(Scene):
    def construct(self):
        divider = Line(UP * 3.0, DOWN * 3.0, color=SLATE, stroke_width=2)
        left_lbl  = LabelChip("HUMAN PROSE",   accent=TEAL).move_to(LEFT * 3.0 + UP * 2.0)
        left_q    = Text("clear writing", font=SERIF, color=INK).scale(0.5).move_to(LEFT * 3.0 + UP * 0.9)
        left_arr  = Text("->", font=MONO, color=TEAL).scale(0.7).move_to(LEFT * 3.0 + UP * 0.1)
        left_ans  = Text("careful thinking", font=SERIF, color=TEAL).scale(0.5).move_to(LEFT * 3.0 + DOWN * 0.7)
        left_note = Text("reliable heuristic", font=MONO, color=TEAL).scale(0.38).move_to(LEFT * 3.0 + DOWN * 1.5)
        right_lbl  = LabelChip("AI PROSE",    accent=CRIMSON).move_to(RIGHT * 3.0 + UP * 2.0)
        right_q    = Text("clear writing", font=SERIF, color=INK).scale(0.5).move_to(RIGHT * 3.0 + UP * 0.9)
        right_arr  = Text("->", font=MONO, color=CRIMSON).scale(0.7).move_to(RIGHT * 3.0 + UP * 0.1)
        right_ans  = Text("???", font=MONO, color=CRIMSON).scale(0.65).move_to(RIGHT * 3.0 + DOWN * 0.7)
        right_note = Text("heuristic broken", font=MONO, color=CRIMSON).scale(0.38).move_to(RIGHT * 3.0 + DOWN * 1.5)
        self.play(Create(divider))
        self.play(FadeIn(left_lbl), FadeIn(right_lbl))
        self.play(FadeIn(left_q), FadeIn(right_q))
        self.play(FadeIn(left_arr), FadeIn(right_arr))
        self.play(FadeIn(left_ans), FadeIn(right_ans))
        self.play(FadeIn(left_note), FadeIn(right_note))
        self.wait(max(0.3, DUR["B04"] - 6.5))


class B05_FormContentSplit(Scene):
    def construct(self):
        sentence = Text('"The query returned no results."', font=SERIF, color=INK).scale(0.6).move_to(UP * 2.0)
        split = Line(UP * 0.8, DOWN * 2.8, color=SLATE, stroke_width=2)
        form_chip = LabelChip("FORM", accent=TEAL).move_to(LEFT * 3.0 + UP * 0.6)
        form_d1   = Text("statistical learning", font=MONO, color=TEAL).scale(0.42).move_to(LEFT * 3.0 + DOWN * 0.2)
        form_d2   = Text("what it looks like", font=MONO, color=TEAL).scale(0.42).move_to(LEFT * 3.0 + DOWN * 0.9)
        cont_chip = LabelChip("CONTENT", accent=CRIMSON).move_to(RIGHT * 3.0 + UP * 0.6)
        cont_d1   = Text("whatever comes out", font=MONO, color=CRIMSON).scale(0.42).move_to(RIGHT * 3.0 + DOWN * 0.2)
        cont_d2   = Text("what is actually true?", font=MONO, color=CRIMSON).scale(0.42).move_to(RIGHT * 3.0 + DOWN * 0.9)
        footer = Text("generated independently", font=MONO, color=SLATE).scale(0.4).move_to(DOWN * 2.2)
        self.play(FadeIn(sentence))
        self.play(Create(split))
        self.play(FadeIn(form_chip), FadeIn(cont_chip))
        self.play(FadeIn(form_d1), FadeIn(cont_d1))
        self.play(FadeIn(form_d2), FadeIn(cont_d2))
        self.play(FadeIn(footer))
        self.wait(max(0.3, DUR["B05"] - 6.0))


def _gauge(x_center, label_text, fill_frac, fill_color):
    """Return (outline, fill, label) for a vertical gauge at x_center."""
    outline = Rectangle(width=1.1, height=3.6, color=SLATE, fill_opacity=0.08)
    outline.set_stroke(color=SLATE, width=2)
    outline.move_to(np.array([x_center, 0.1, 0]))
    h = 3.6 * fill_frac
    fill = Rectangle(width=1.1, height=h, color=fill_color, fill_opacity=0.82)
    fill.set_stroke(width=0, opacity=0)
    fill.move_to(np.array([x_center, -1.7 + h / 2, 0]))
    lbl = Text(label_text, font=MONO, color=INK).scale(0.36)
    lbl.move_to(np.array([x_center, -2.15, 0]))
    return outline, fill, lbl


class B07_GaugeStage1(Scene):
    def construct(self):
        header = Text("STAGE 1", font=DISPLAY, color=INK).scale(0.5).move_to(UP * 3.0)
        out_outline, out_fill, out_lbl = _gauge(-1.5, "confidence\nin output", 0.82, CRIMSON)
        trigger = Text("fluent output arrives", font=SERIF, color=INK).scale(0.48).move_to(RIGHT * 2.2 + UP * 0.8)
        pump_lbl = SerifLabel("pumped by fluency", accent=CRIMSON, size=24).move_to(RIGHT * 2.5 + DOWN * 0.5)
        self.play(FadeIn(header))
        self.play(Create(out_outline))
        self.play(FadeIn(out_lbl))
        self.play(FadeIn(trigger))
        self.play(GrowFromEdge(out_fill, DOWN), run_time=2.0)
        self.play(FadeIn(pump_lbl))
        self.wait(max(0.3, DUR["B07"] - 7.0))


class B08_GaugeStage2(Scene):
    def construct(self):
        header = Text("STAGE 2  (the trap)", font=DISPLAY, color=CRIMSON).scale(0.5).move_to(UP * 3.0)
        out_outline, out_fill, out_lbl  = _gauge(-3.0, "confidence\nin output",    0.82, CRIMSON)
        jdg_outline, jdg_fill, jdg_lbl = _gauge( 0.2, "confidence\nin MY judgment", 0.78, CRIMSON)
        connector = Arrow(
            np.array([-2.35, 0.1, 0]), np.array([-0.35, 0.1, 0]),
            color=CRIMSON, stroke_width=2.5, tip_length=0.2,
            max_tip_length_to_length_ratio=0.5)
        trap_lbl = SerifLabel("pumped again", accent=CRIMSON, size=24).move_to(np.array([0.2, 2.2, 0]))
        self.play(FadeIn(header))
        self.add(out_outline, out_fill, out_lbl)
        self.play(Create(jdg_outline))
        self.play(FadeIn(jdg_lbl))
        self.play(Create(connector))
        self.play(GrowFromEdge(jdg_fill, DOWN), run_time=2.0)
        self.play(FadeIn(trap_lbl))
        self.wait(max(0.3, DUR["B08"] - 7.5))


class B09_QuoteEvalBooster(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Fluency is an evaluation booster. "
            "It boosts the wrong evaluations as readily as the right ones.",
            "Computational Skepticism for AI, Chapter 1",
            None,
            "evaluation booster",
            DUR["B09"],
        )


class B10_PoppFix(Scene):
    def construct(self):
        pre_box = Rectangle(width=5.5, height=1.4, color=TEAL, fill_opacity=0.1)
        pre_box.set_stroke(color=TEAL, width=2.5)
        pre_box.move_to(UP * 1.3)
        pre_hdr = LabelChip("BEFORE READING", accent=TEAL).move_to(UP * 2.55)
        pre_txt = Text("A wrong answer would assign low risk", font=MONO, color=TEAL).scale(0.4).move_to(UP * 1.45)
        pre_txt2 = Text("to a high-acuity patient.", font=MONO, color=TEAL).scale(0.4).move_to(UP * 0.9)
        anchor_lbl = SerifLabel("your anchor", accent=TEAL, size=24).move_to(RIGHT * 3.5 + UP * 1.3)
        divider = Line(LEFT * 4.0, RIGHT * 4.0, color=SLATE, stroke_width=1.5).move_to(DOWN * 0.05)
        out_box = Rectangle(width=5.5, height=1.4, color=SLATE, fill_opacity=0.08)
        out_box.set_stroke(color=SLATE, width=1.5)
        out_box.move_to(DOWN * 1.3)
        out_hdr = LabelChip("OUTPUT ARRIVES", accent=SLATE).move_to(DOWN * 0.6)
        out_txt = Text("Risk score: 0.22 (low acuity)", font=MONO, color=CRIMSON).scale(0.4).move_to(DOWN * 1.3)
        self.play(GrowFromCenter(pre_box))
        self.play(FadeIn(pre_hdr), FadeIn(pre_txt), FadeIn(pre_txt2))
        self.play(FadeIn(anchor_lbl))
        self.play(Create(divider))
        self.play(GrowFromCenter(out_box))
        self.play(FadeIn(out_hdr), FadeIn(out_txt))
        self.wait(max(0.3, DUR["B10"] - 7.5))


class B11_QuotePreSpec(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Before you read the output: specify what a wrong answer would look like. "
            "Not vaguely — specifically.",
            "Computational Skepticism for AI, Chapter 1",
            None,
            "specify",
            DUR["B11"],
        )


class B12_ExampleFluency(Scene):
    def construct(self):
        total = DUR["B12"]
        title = Text("Same Gap — Different Domain", font=DISPLAY, font_size=20, color=GOLD)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.5, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        col_r = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)

        lbl_l = Text("WHAT THE AI SAID", font=DISPLAY, font_size=17, color=TEAL).move_to(LEFT * 3.2 + UP * 1.55)
        lbl_r = Text("WHAT WAS WRONG", font=DISPLAY, font_size=17, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 1.55)

        sub_l = Text("Fixed: off-by-one\nin loop boundary", font="PT Mono", font_size=14, color=INK).move_to(LEFT * 3.2 + UP * 0.55)
        sub_r = Text("Off-by-one was in\na different loop", font="PT Mono", font_size=14, color=INK).move_to(RIGHT * 3.2 + UP * 0.55)

        det_l = Text("Confident. Clear.\nWell-formatted.", font=DISPLAY, font_size=13, color=TEAL).move_to(LEFT * 3.2 + DOWN * 0.45)
        det_r = Text("Diagnosis: wrong bug.\nTest still fails.", font=DISPLAY, font_size=13, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 0.45)

        res_l = Text("COMMITTED", font=DISPLAY, font_size=18, color=TEAL, weight=BOLD).move_to(LEFT * 3.2 + DOWN * 1.3)
        res_r = Text("STILL BROKEN", font=DISPLAY, font_size=18, color=CRIMSON, weight=BOLD).move_to(RIGHT * 3.2 + DOWN * 1.3)

        note = Text("The fluency was enough. The anchor was never specified.", font=DISPLAY, font_size=14, color=INK).move_to(DOWN * 2.55)
        note_rect = Rectangle(width=9.0, height=0.52, fill_color=CRIMSON, fill_opacity=0.10,
                              stroke_width=1.5, color=CRIMSON).move_to(DOWN * 2.55)

        self.play(Write(title), run_time=0.4)
        self.play(GrowFromCenter(col_l), GrowFromCenter(col_r), run_time=0.7)
        self.play(Write(lbl_l), Write(lbl_r), run_time=0.5)
        self.play(Write(sub_l), Write(sub_r), run_time=0.4)
        self.play(Write(det_l), Write(det_r), run_time=0.4)
        self.play(FadeIn(res_l), FadeIn(res_r), run_time=0.4)
        self.play(GrowFromCenter(note_rect), run_time=0.3)
        self.play(Write(note), run_time=0.4)
        self.wait(max(0.5, total - 4.5))
