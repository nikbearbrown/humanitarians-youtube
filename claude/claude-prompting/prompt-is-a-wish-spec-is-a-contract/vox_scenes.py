"""vox_scenes.py — Why "Write Me a Login Function" Is Not a Prompt
(prompt-is-a-wish-spec-is-a-contract, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'.
B07 is the STILL (ai slot) — no scene here.

Color law (teardown palette): CRIMSON = prompt / boondoggle / vague wish.
INK = specification / contract / verified output. Single accent. Never swap.

Exclusions: no OAuth, no security audit, no prompt tricks, no hash history.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

DUR = {
    "B01": 10.0, "B02": 9.0, "B03": 10.0, "B04": 11.0, "B05": 11.0,
    "B06": 12.0, "B08": 10.0, "B09": 9.0, "B10": 11.0, "B11": 11.0,
    "B12": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _arrow(start, end, color=INK):
    return Arrow(start, end, color=color, stroke_width=2.5,
                 max_tip_length_to_length_ratio=0.18, buff=0.06)


def _node(label, color=INK, w=2.4, h=0.58):
    box = Rectangle(width=w, height=h).set_fill(color, 0.10).set_stroke(color, 1.8)
    txt = Text(label, font=DISPLAY, color=color, font_size=20, weight="MEDIUM")
    if txt.width > w * 0.86:
        txt.scale_to_fit_width(w * 0.86)
    txt.move_to(box)
    return VGroup(box, txt)


def _spec_row(text, color=INK, w=7.0, h=0.5):
    box = Rectangle(width=w, height=h).set_fill(color, 0.06).set_stroke(color, 1.4)
    txt = Text(text, font=SERIF, color=INK, font_size=22, slant=ITALIC)
    if txt.width > w * 0.92:
        txt.scale_to_fit_width(w * 0.92)
    txt.move_to(box)
    return VGroup(box, txt)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("One sentence. Twelve lines.", font=SERIF, color=INK,
                  font_size=50, weight="BOLD")
        t2 = Text("Broken.", font=SERIF, color=CRIMSON, font_size=50,
                  weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.2)
        sub = Text("same Claude, six sentences later: production-ready", font=SERIF,
                   color=INK, font_size=26, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.45)
        eye.next_to(block, UP, buff=0.65)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.4))


class B02_TheQuestion(Scene):
    def construct(self):
        total = DUR["B02"]
        t1 = Text("The request was clear.", font=SERIF, color=INK,
                  font_size=46, weight="BOLD")
        t2 = Text("Why was the output broken?", font=SERIF, color=CRIMSON,
                  font_size=46, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.38).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B03_PromptDivergence(Scene):
    def construct(self):
        total = DUR["B03"]
        # Prompt box on left, six output boxes fan right
        prompt_box = Rectangle(width=3.2, height=0.7)
        prompt_box.set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 2.0)
        prompt_txt = Text("write me a login function", font=SERIF,
                          color=INK, font_size=20, slant=ITALIC)
        prompt_txt.move_to(prompt_box)
        prompt = VGroup(prompt_box, prompt_txt).move_to(LEFT * 4.2)

        # Six output boxes fanning right
        ys = np.linspace(2.4, -2.4, 6)
        out_boxes = VGroup()
        arrows = VGroup()
        for y in ys:
            ob = Rectangle(width=2.4, height=0.42)
            ob.set_fill(CRIMSON, 0.07).set_stroke(CRIMSON, 1.2)
            ob.move_to(RIGHT * 2.8 + UP * y)
            out_boxes.add(ob)
            arr = _arrow(prompt.get_right(), ob.get_left(), CRIMSON)
            arrows.add(arr)

        dist_lbl = SerifLabel("Claude picks from its distribution", CRIMSON, size=24)
        dist_lbl.move_to(RIGHT * 2.8 + DOWN * 3.2)

        self.play(FadeIn(prompt), run_time=0.6)
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.08),
                  LaggedStart(*[FadeIn(ob) for ob in out_boxes], lag_ratio=0.08),
                  run_time=1.2)
        self.play(FadeIn(dist_lbl, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.4))


class B04_TrainingDistribution(Scene):
    def construct(self):
        total = DUR["B04"]
        t1 = Text("Claude completed the most common pattern.", font=SERIF,
                  color=INK, font_size=42, weight="BOLD")
        t2 = Text("The most common pattern", font=SERIF, color=INK,
                  font_size=36)
        t3 = Text("is not production code.", font=SERIF, color=CRIMSON,
                  font_size=36, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.32).move_to(ORIGIN)
        u = Line(t3.get_corner(DL) + DOWN * 0.12, t3.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), FadeIn(t3), Create(u), run_time=0.8)
        self.wait(max(0.5, total - 1.5))


class B05_SpecContract(Scene):
    def construct(self):
        total = DUR["B05"]
        # Spec elements column on left -> one output box on right
        spec_items = ["INVARIANTS", "BOUNDARY", "FORMAT", "SUCCESS CRITERION"]
        chips = VGroup(*[LabelChip(it, accent=INK, size=22) for it in spec_items])
        chips.arrange(DOWN, buff=0.3).move_to(LEFT * 3.8)

        output = Rectangle(width=2.6, height=1.2)
        output.set_fill(INK, 0.10).set_stroke(INK, 2.0)
        output_txt = Text("EXACTLY THIS", font=DISPLAY, color=INK,
                          font_size=22, weight="MEDIUM")
        output_txt.move_to(output)
        out_box = VGroup(output, output_txt).move_to(RIGHT * 3.8)

        # single arrow from spec group to output
        arr = _arrow(chips.get_right(), out_box.get_left())

        head = Text("Specification", font=DISPLAY, color=INK, font_size=26,
                    weight="MEDIUM").to_edge(UP, buff=0.65)

        self.play(FadeIn(head), run_time=0.4)
        for chip in chips:
            self.play(FadeIn(chip, shift=RIGHT * 0.15), run_time=0.35)
        self.play(Create(arr), FadeIn(out_box), run_time=0.8)
        self.wait(max(0.5, total - 0.4 - len(spec_items) * 0.35 - 0.8))


class B06_SixSentences(Scene):
    def construct(self):
        total = DUR["B06"]
        head = Text("The specification:", font=DISPLAY, color=INK,
                    font_size=24, weight="MEDIUM").to_edge(UP, buff=0.6)

        rows_data = [
            "Use bcrypt, not MD5",
            "Use the parameterized helper in db.py",
            "Empty credentials: reject before DB",
            "Return token + expiry on success",
            "Do not touch schema.sql",
            "Handoff: pytest passes 5 named cases",
        ]
        rows = VGroup(*[_spec_row(r) for r in rows_data])
        rows.arrange(DOWN, buff=0.22).move_to(DOWN * 0.1)

        self.play(FadeIn(head), run_time=0.4)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.4)
        self.wait(max(0.5, total - 0.4 - len(rows_data) * 0.4))


class B08_TomasComparison(Scene):
    def construct(self):
        total = DUR["B08"]
        label = Text("illustrative", font=SERIF, color=INK, font_size=18,
                     slant=ITALIC).to_corner(DR, buff=0.4)

        lhead = LabelChip("PROMPT", accent=CRIMSON, size=24).move_to(LEFT * 3.5 + UP * 2.4)
        rhead = LabelChip("SPECIFICATION", accent=INK, size=24).move_to(RIGHT * 3.5 + UP * 2.4)

        # Left (crimson) — prompt result
        l1 = _spec_row("'add a login'", CRIMSON, w=4.0)
        l2 = _spec_row("passwords in plaintext", CRIMSON, w=4.0)
        l3 = _spec_row("Python dict", CRIMSON, w=4.0)
        l4 = LabelChip("BOONDOGGLE", accent=CRIMSON, size=22)
        left_col = VGroup(l1, l2, l3, l4).arrange(DOWN, buff=0.3)
        left_col.move_to(LEFT * 3.5 + DOWN * 0.3)

        # Right (ink) — spec result
        r1 = _spec_row("8 minutes of spec writing", INK, w=4.0)
        r2 = _spec_row("every property named", INK, w=4.0)
        r3 = _spec_row("Tomas can defend every line", INK, w=4.0)
        r4 = LabelChip("SHIPS CORRECT", accent=INK, size=22)
        right_col = VGroup(r1, r2, r3, r4).arrange(DOWN, buff=0.3)
        right_col.move_to(RIGHT * 3.5 + DOWN * 0.3)

        div = Line(UP * 3.0, DOWN * 3.0, color=HAIRLINE, stroke_width=1.3)

        self.play(FadeIn(label), FadeIn(lhead), FadeIn(rhead), FadeIn(div), run_time=0.5)
        for la, ra in zip(left_col, right_col):
            self.play(FadeIn(la), FadeIn(ra), run_time=0.45)
        self.wait(max(0.5, total - 0.5 - len(left_col) * 0.45))


class B09_DecisionIsWork(Scene):
    def construct(self):
        total = DUR["B09"]
        t1 = Text("The decision is the work.", font=SERIF, color=INK,
                  font_size=52, weight="BOLD")
        t2 = Text("The typing is the easy part.", font=SERIF, color=INK,
                  font_size=36, slant=ITALIC)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.45).move_to(ORIGIN)
        u = Line(t1.get_corner(DL) + DOWN * 0.14, t1.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), Create(u), run_time=0.8)
        self.play(FadeIn(t2, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 1.4))


class B10_FourSteps(Scene):
    def construct(self):
        total = DUR["B10"]
        head = Text("Before any code:", font=DISPLAY, color=INK,
                    font_size=26, weight="MEDIUM").to_edge(UP, buff=0.65)

        steps = [
            "DECIDE WHAT YOU'RE BUILDING",
            "READ WHAT EXISTS",
            "NAME THE BOUNDARY",
            "WRITE THE HANDOFF CONDITION",
        ]
        nodes = VGroup(*[_node(s, INK, w=4.2, h=0.62) for s in steps])
        nodes.arrange(DOWN, buff=0.38).move_to(DOWN * 0.2)

        arrows = VGroup()
        for i in range(len(nodes) - 1):
            a = _arrow(nodes[i].get_bottom() + DOWN * 0.04,
                       nodes[i+1].get_top() + UP * 0.04)
            arrows.add(a)

        self.play(FadeIn(head), run_time=0.4)
        for i, node in enumerate(nodes):
            self.play(FadeIn(node), run_time=0.5)
            if i < len(arrows):
                self.play(Create(arrows[i]), run_time=0.3)
        self.wait(max(0.5, total - 0.4 - len(nodes) * 0.8))


class B11_TimeVsQuality(Scene):
    def construct(self):
        total = DUR["B11"]
        # Two columns: 6 SECONDS vs 20 MINUTES
        lhead = Text("6 seconds", font=MONO, color=CRIMSON, font_size=38,
                     weight="BOLD").move_to(LEFT * 3.5 + UP * 1.6)
        l1 = Text("prompt", font=SERIF, color=CRIMSON, font_size=26,
                  slant=ITALIC).next_to(lhead, DOWN, buff=0.3)
        l2 = LabelChip("BOONDOGGLE", accent=CRIMSON, size=24)
        l2.next_to(l1, DOWN, buff=0.35)
        l3 = Text("fluent activity,\nno verified output", font=SERIF, color=INK,
                  font_size=22, slant=ITALIC)
        l3.next_to(l2, DOWN, buff=0.3)

        rhead = Text("20 minutes", font=MONO, color=INK, font_size=38,
                     weight="BOLD").move_to(RIGHT * 3.5 + UP * 1.6)
        r1 = Text("specification", font=SERIF, color=INK, font_size=26,
                  slant=ITALIC).next_to(rhead, DOWN, buff=0.3)
        r2 = SerifLabel("something to put your name on", INK, size=24)
        r2.next_to(r1, DOWN, buff=0.35)

        div = Line(UP * 2.6, DOWN * 2.8, color=HAIRLINE, stroke_width=1.3)

        self.play(FadeIn(lhead), FadeIn(rhead), FadeIn(div), run_time=0.6)
        self.play(FadeIn(l1), FadeIn(r1), run_time=0.5)
        self.play(FadeIn(l2), run_time=0.5)
        self.play(FadeIn(l3), FadeIn(r2), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B12_End(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("A prompt is a wish.", font=SERIF, color=INK,
                  font_size=50, weight="BOLD")
        t2 = Text("A spec is a contract.", font=SERIF, color=INK,
                  font_size=50, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(UP * 0.2)
        eye.next_to(block, UP, buff=0.65)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.9))
