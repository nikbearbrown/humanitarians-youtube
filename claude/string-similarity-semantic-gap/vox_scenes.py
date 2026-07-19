"""vox_scenes.py — Why String Similarity Is Not Semantic Equivalence
(string-similarity-semantic-gap, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'.
B05 is the STILL (ai slot) — no scene here.

Color law (teardown palette): CRIMSON = string similarity / wrong frame / tests passing but wrong.
INK = semantic equivalence / domain knowledge / plausibility audit. Single accent. Never swap.

Exclusions: no full NLP embeddings, no model comparisons, no Polanyi at length,
no slopsquatting (that is candidate 08).
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403

DUR = {
    "B01": 18.0, "B02": 10.0, "B03": 24.0, "B04": 20.0,
    "B06": 24.0, "B07": 16.0, "B08": 20.0, "B09": 20.0, "B10": 18.0,
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


def _box(label, color=INK, w=3.4, h=0.64):
    box = Rectangle(width=w, height=h).set_fill(color, 0.09).set_stroke(color, 1.8)
    txt = Text(label, font=DISPLAY, color=color, font_size=20, weight="MEDIUM")
    if txt.width > w * 0.86:
        txt.scale_to_fit_width(w * 0.86)
    txt.move_to(box)
    return VGroup(box, txt)


def _row(text, color=INK, w=5.8, h=0.52):
    box = Rectangle(width=w, height=h).set_fill(color, 0.07).set_stroke(color, 1.4)
    txt = Text(text, font=SERIF, color=color, font_size=20, slant=ITALIC)
    if txt.width > w * 0.90:
        txt.scale_to_fit_width(w * 0.90)
    txt.move_to(box)
    return VGroup(box, txt)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("85% accuracy.", font=SERIF, color=INK, font_size=46,
                  weight="BOLD")
        t2 = Text("All tests pass.", font=SERIF, color=INK, font_size=46)
        t3 = Text("hunting  ↔  haunting:  0.93", font=MONO, color=CRIMSON,
                  font_size=34, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.28).move_to(UP * 0.15)
        eye.next_to(block, UP, buff=0.6)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.7)
        self.play(FadeIn(t3), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.9))


class B02_TheQuestion(Scene):
    def construct(self):
        total = DUR["B02"]
        t1 = Text("85% accurate should be reliable.", font=SERIF,
                  color=INK, font_size=40, weight="BOLD")
        t2 = Text("Why was it not ready to ship?", font=SERIF,
                  color=CRIMSON, font_size=40, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.42).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B03_WrongFrame(Scene):
    def construct(self):
        total = DUR["B03"]
        # Two paths diverging from one starting point
        start = LEFT * 4.8
        start_dot = Dot(start, color=INK, radius=0.12)
        start_lbl = Text("Seth's prompt", font=SERIF, color=INK, font_size=22,
                         slant=ITALIC).next_to(start_dot, DOWN, buff=0.2)

        # Upper path: what Claude solved (CRIMSON)
        upper_end = RIGHT * 1.0 + UP * 1.5
        upper_arr = _arrow(start_dot.get_right(), upper_end, CRIMSON)
        upper_box = _box("STRING SIMILARITY", CRIMSON, w=3.8)
        upper_box.move_to(RIGHT * 3.6 + UP * 1.5)
        upper_sub = Text("what Claude built", font=SERIF, color=CRIMSON,
                         font_size=18, slant=ITALIC).next_to(upper_box, DOWN, buff=0.15)

        # Lower path: what Seth needed (INK)
        lower_end = RIGHT * 1.0 + DOWN * 1.5
        lower_arr = _arrow(start_dot.get_right(), lower_end, INK)
        lower_box = _box("SEMANTIC EQUIVALENCE", INK, w=3.8)
        lower_box.move_to(RIGHT * 3.6 + DOWN * 1.5)
        lower_sub = Text("what Seth needed", font=SERIF, color=INK,
                         font_size=18, slant=ITALIC).next_to(lower_box, DOWN, buff=0.15)

        note = Text("same prompt → different problems", font=SERIF, color=CRIMSON,
                    font_size=22, slant=ITALIC).to_edge(DOWN, buff=0.5)

        self.play(FadeIn(start_dot), FadeIn(start_lbl), run_time=0.5)
        self.play(Create(upper_arr), FadeIn(upper_box), run_time=0.7)
        self.play(FadeIn(upper_sub), run_time=0.4)
        self.play(Create(lower_arr), FadeIn(lower_box), run_time=0.7)
        self.play(FadeIn(lower_sub), run_time=0.4)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.2))


class B04_TestsVerify(Scene):
    def construct(self):
        total = DUR["B04"]
        t1 = Text("Tests verify what the function does.", font=SERIF,
                  color=INK, font_size=38, weight="BOLD")
        t2 = Text("Not what you needed it to do.", font=SERIF,
                  color=CRIMSON, font_size=38, weight="BOLD")
        sub = Text("Claude wrote tests for Claude's problem.", font=SERIF,
                   color=INK, font_size=26, slant=ITALIC)
        block = VGroup(t1, t2, sub).arrange(DOWN, buff=0.38).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.9))


class B06_TheProbe(Scene):
    def construct(self):
        total = DUR["B06"]
        # Pair display with score, then semantic mismatch revealed
        pair_lbl = Text('"hunting"  ↔  "haunting"', font=MONO, color=INK,
                        font_size=36, weight="BOLD").move_to(UP * 2.0)

        score_lbl = Text("similarity: 0.93", font=MONO, color=CRIMSON,
                         font_size=34, weight="BOLD").move_to(UP * 1.1)
        score_u = Line(score_lbl.get_corner(DL) + DOWN * 0.1,
                       score_lbl.get_corner(DR) + DOWN * 0.1,
                       color=CRIMSON, stroke_width=2)

        # Two semantic boxes below
        hunt_box = _box("HUNTING\nactive chase", CRIMSON, w=3.4, h=0.9)
        hunt_box.move_to(LEFT * 3.0 + DOWN * 0.6)
        haunt_box = _box("HAUNTING\nambient presence", INK, w=3.4, h=0.9)
        haunt_box.move_to(RIGHT * 3.0 + DOWN * 0.6)

        neq = Text("≠", font=SERIF, color=CRIMSON, font_size=60).move_to(DOWN * 0.6)
        label = Text("opposite NPC states", font=SERIF, color=CRIMSON,
                     font_size=22, slant=ITALIC).move_to(DOWN * 1.9)

        self.play(FadeIn(pair_lbl), run_time=0.6)
        self.play(FadeIn(score_lbl), Create(score_u), run_time=0.6)
        self.play(FadeIn(hunt_box), FadeIn(haunt_box), FadeIn(neq), run_time=0.8)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(max(0.5, total - 2.5))


class B07_PlausibilityAuditing(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("Plausibility auditing", font=SERIF, color=INK,
                  font_size=46, weight="BOLD")
        t2 = Text("is hearing the wrong note", font=SERIF, color=INK,
                  font_size=40)
        t3 = Text("before the proof is ready.", font=SERIF, color=CRIMSON,
                  font_size=40, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.32).move_to(ORIGIN)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), FadeIn(t3), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B08_LeilaGrader(Scene):
    def construct(self):
        total = DUR["B08"]
        label = Text("illustrative", font=SERIF, color=INK, font_size=18,
                     slant=ITALIC).to_corner(DR, buff=0.4)
        head = Text("Leila's quiz grader", font=DISPLAY, color=INK,
                    font_size=26, weight="MEDIUM").to_edge(UP, buff=0.6)

        rows = [
            ("student answer: photosynthesis", INK),
            ("correct answer: cellular respiration", INK),
            ('similarity score: 0.67  (threshold: 0.6)', CRIMSON),
            ("grader marks it: CORRECT", CRIMSON),
            ("biology says: WRONG", INK),
        ]
        items = VGroup()
        for text, color in rows:
            dot = Dot(color=color, radius=0.09)
            lbl = Text(text, font=SERIF, color=color, font_size=22, slant=ITALIC)
            if lbl.width > 9.0:
                lbl.scale_to_fit_width(9.0)
            row = VGroup(dot, lbl).arrange(RIGHT, buff=0.3)
            items.add(row)
        items.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(DOWN * 0.15)

        self.play(FadeIn(label), FadeIn(head), run_time=0.5)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.12), run_time=0.4)
        self.wait(max(0.5, total - 0.5 - len(rows) * 0.4))


class B09_Practice(Scene):
    def construct(self):
        total = DUR["B09"]
        head = Text("Before shipping:", font=DISPLAY, color=INK,
                    font_size=26, weight="MEDIUM").to_edge(UP, buff=0.65)

        steps = [
            ("ASK", "What is the hardest case\nfor this approach?"),
            ("WRITE", "Write that case by hand."),
            ("RUN", "Run it. If it feels wrong,\nit probably is wrong."),
        ]
        nodes = VGroup()
        for label, desc in steps:
            chip = LabelChip(label, accent=INK, size=22)
            desc_txt = Text(desc, font=SERIF, color=INK, font_size=20, slant=ITALIC)
            row = VGroup(chip, desc_txt).arrange(RIGHT, buff=0.4)
            nodes.add(row)
        nodes.arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(DOWN * 0.1)

        arrows = VGroup()
        for i in range(len(nodes) - 1):
            a = Arrow(nodes[i].get_bottom() + DOWN * 0.06,
                      nodes[i+1].get_top() + UP * 0.06,
                      color=INK, stroke_width=2.0,
                      max_tip_length_to_length_ratio=0.18)
            arrows.add(a)

        note = Text("domain knowledge Claude doesn't have", font=SERIF,
                    color=CRIMSON, font_size=22, slant=ITALIC).to_edge(DOWN, buff=0.5)

        self.play(FadeIn(head), run_time=0.4)
        for i, node in enumerate(nodes):
            self.play(FadeIn(node), run_time=0.5)
            if i < len(arrows):
                self.play(Create(arrows[i]), run_time=0.3)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 0.4 - len(nodes) * 0.8 - 0.5))


class B10_End(Scene):
    def construct(self):
        total = DUR["B10"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("Tests verify the problem Claude solved.", font=SERIF,
                  color=INK, font_size=36, weight="BOLD")
        t2 = Text("Auditing verifies the problem", font=SERIF, color=INK,
                  font_size=36)
        t3 = Text("you needed to solve.", font=SERIF, color=CRIMSON,
                  font_size=36, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.25).move_to(UP * 0.15)
        eye.next_to(block, UP, buff=0.6)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), FadeIn(t3), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.9))
