"""vox_scenes.py — Why the One-Sentence Problem Statement Is the Most Expensive Thing You Write
(one-sentence-problem-statement, slate cut, 16:9, 1-minute band).

One Scene per GRAPHIC/CARD beat whose source is 'own'.
No STILL·ai slot (4-beat 1-minute film — lean structure).

Color law (teardown palette): CRIMSON = the 'and' / multiple hidden projects / the sentence that fails.
INK = the single system / the chosen sentence / conceptual integrity. Single accent. Never swap.

Exclusions: no full Gru command syntax; no Brooks history; no formal requirements methodology;
no arc42 or ADR templates.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403

DUR = {
    "B01": 20.0, "B02": 10.0, "B03": 22.0, "B04": 16.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("Refused. Two ands.", font=SERIF, color=CRIMSON,
                  font_size=38, weight="BOLD")
        t2 = Text("That is four projects.", font=SERIF, color=INK,
                  font_size=36)
        t3 = Text("14 minutes. No code. One sentence.", font=SERIF,
                  color=INK, font_size=32, weight="BOLD")
        if t3.width > 12.0:
            t3.scale_to_fit_width(12.0)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.28).move_to(UP * 0.15)
        eye.next_to(block, UP, buff=0.55)
        u = Line(t1.get_corner(DL) + DOWN * 0.12, t1.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), Create(u), run_time=0.6)
        self.play(FadeIn(t2), run_time=0.5)
        self.play(FadeIn(t3), run_time=0.5)
        self.wait(max(0.5, total - 2.1))


class B02_TheQuestion(Scene):
    def construct(self):
        total = DUR["B02"]
        t1 = Text("One sentence should be fast.", font=SERIF,
                  color=INK, font_size=44, weight="BOLD")
        t2 = Text("Why did it take 14 minutes?", font=SERIF,
                  color=CRIMSON, font_size=40, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.44).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.12, t2.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B03_TheMechanism(Scene):
    def construct(self):
        total = DUR["B03"]
        # Show the failing sentence with "and" highlighted, then show the split
        head = Text("One sentence with two ands", font=DISPLAY,
                    color=INK, font_size=24, weight="MEDIUM").to_edge(UP, buff=0.6)

        # The sentence — split into parts with "and" in CRIMSON
        part1 = Text("audits scripts", font=MONO, color=INK, font_size=19)
        and1  = Text("and", font=SERIF, color=CRIMSON, font_size=22, weight="BOLD")
        part2 = Text("refactors them", font=MONO, color=INK, font_size=19)
        and2  = Text("and", font=SERIF, color=CRIMSON, font_size=22, weight="BOLD")
        part3 = Text("writes tests", font=MONO, color=INK, font_size=19)
        and3  = Text("and", font=SERIF, color=CRIMSON, font_size=22, weight="BOLD")
        part4 = Text("generates CLAUDE.md", font=MONO, color=INK, font_size=19)
        sentence_row = VGroup(part1, and1, part2, and2, part3, and3, part4).arrange(RIGHT, buff=0.18)
        if sentence_row.width > 12.5:
            sentence_row.scale_to_fit_width(12.5)
        sentence_row.move_to(UP * 0.6)

        arrow_lbl = Text("= two projects disguised as one", font=SERIF,
                         color=CRIMSON, font_size=24, slant=ITALIC).move_to(DOWN * 0.05)

        note = Text("The 'and' is a tell.", font=SERIF,
                    color=CRIMSON, font_size=26, weight="BOLD").move_to(DOWN * 1.0)

        sub = Text("The refusal forces the decision the list was deferring.",
                   font=SERIF, color=INK, font_size=20, slant=ITALIC).to_edge(DOWN, buff=0.5)
        if sub.width > 12.0:
            sub.scale_to_fit_width(12.0)

        self.play(FadeIn(head), run_time=0.4)
        self.play(FadeIn(sentence_row), run_time=0.6)
        self.play(FadeIn(arrow_lbl), run_time=0.4)
        self.play(FadeIn(note), run_time=0.4)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(max(0.5, total - 2.2))


class B04_Practice(Scene):
    def construct(self):
        total = DUR["B04"]
        t1 = Text("One system. One user. One done-condition.", font=SERIF,
                  color=INK, font_size=32, weight="BOLD")
        if t1.width > 12.5:
            t1.scale_to_fit_width(12.5)
        t2 = Text("No ands.", font=SERIF, color=CRIMSON, font_size=44,
                  weight="BOLD")
        t3 = Text("That sentence is your project.", font=SERIF,
                  color=INK, font_size=34)
        if t3.width > 12.0:
            t3.scale_to_fit_width(12.0)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.30).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.play(FadeIn(t3), run_time=0.5)
        self.wait(max(0.5, total - 1.8))
