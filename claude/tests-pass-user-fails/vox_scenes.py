"""vox_scenes.py — Why the Build Passes Its Tests and Fails Its User
(tests-pass-user-fails, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'.
B05 is the STILL (ai slot) — no scene here.

Color law (teardown palette): CRIMSON = tests passing / code-level proxy / structural blind spot.
INK = user need / SDD prose / Pass 3 judgment. Single accent. Never swap.

Exclusions: no Hoare-triple notation; no ISO/IEC 25010 detail; no Therac-25/MCO history;
no mutation-testing tooling.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403

DUR = {
    "B01": 23.0, "B02": 9.0, "B03": 22.0, "B04": 20.0,
    "B06": 22.0, "B07": 22.0, "B08": 22.0, "B09": 19.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _pass_row(label, desc, color=INK, w=9.0, h=0.62):
    box = Rectangle(width=w, height=h).set_fill(color, 0.08).set_stroke(color, 1.6)
    lbl = Text(label, font=DISPLAY, color=color, font_size=20, weight="MEDIUM")
    dsc = Text(desc, font=SERIF, color=color, font_size=19, slant=ITALIC)
    group = VGroup(lbl, dsc).arrange(RIGHT, buff=0.5)
    if group.width > w * 0.90:
        group.scale_to_fit_width(w * 0.90)
    group.move_to(box)
    return VGroup(box, group)


def _step_item(num, text, color=INK):
    n = Text(f"{num}.", font=MONO, color=color, font_size=22)
    t = Text(text, font=SERIF, color=color, font_size=22, slant=ITALIC)
    row = VGroup(n, t).arrange(RIGHT, buff=0.3)
    if row.width > 11.0:
        row.scale_to_fit_width(11.0)
    return row


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("npm test: 9 of 9 passing.", font=MONO,
                  color=INK, font_size=26, weight="BOLD")
        if t1.width > 12.0:
            t1.scale_to_fit_width(12.0)
        t2 = Text("The build is done.", font=SERIF, color=INK, font_size=36)
        t3 = Text("The user can't see their data at a glance.", font=SERIF,
                  color=CRIMSON, font_size=34, weight="BOLD")
        if t3.width > 12.0:
            t3.scale_to_fit_width(12.0)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.28).move_to(UP * 0.15)
        eye.next_to(block, UP, buff=0.55)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.5)
        self.play(FadeIn(t2), run_time=0.5)
        self.play(FadeIn(t3), Create(u), run_time=0.8)
        self.wait(max(0.5, total - 2.3))


class B02_TheQuestion(Scene):
    def construct(self):
        total = DUR["B02"]
        t1 = Text("Nine tests pass.", font=SERIF, color=INK,
                  font_size=46, weight="BOLD")
        t2 = Text("Why did the build fail its user?", font=SERIF,
                  color=CRIMSON, font_size=38, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.44).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.12, t2.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B03_TestsVsNeeds(Scene):
    def construct(self):
        total = DUR["B03"]
        head = Text("Tests verify code against tests.", font=DISPLAY,
                    color=INK, font_size=28, weight="MEDIUM").to_edge(UP, buff=0.65)

        # Two columns: TESTS (CRIMSON) vs NEEDS (INK)
        left_lbl = Text("score rows", font=DISPLAY, color=CRIMSON, font_size=20,
                        weight="MEDIUM")
        left_items = VGroup(
            Text("addApplication", font=MONO, color=CRIMSON, font_size=18),
            Text("toggleSubmitted", font=MONO, color=CRIMSON, font_size=18),
            Text("deleteApplication", font=MONO, color=CRIMSON, font_size=18),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        left_col = VGroup(left_lbl, left_items).arrange(DOWN, buff=0.25)

        right_lbl = Text("SDD user need", font=DISPLAY, color=INK, font_size=20,
                         weight="MEDIUM")
        right_txt = Text("at a glance", font=SERIF, color=INK, font_size=22,
                         slant=ITALIC)
        miss = Text("(no row)", font=SERIF, color=CRIMSON, font_size=20,
                    slant=ITALIC)
        right_col = VGroup(right_lbl, right_txt, miss).arrange(DOWN, buff=0.2)

        cols = VGroup(left_col, right_col).arrange(RIGHT, buff=1.8).move_to(DOWN * 0.3)

        div = Line(
            cols.get_center() + UP * 1.4,
            cols.get_center() + DOWN * 1.4,
            color=HAIRLINE, stroke_width=1.2
        )

        note = Text("The failure was never enrolled as a test.", font=SERIF,
                    color=CRIMSON, font_size=21, slant=ITALIC).to_edge(DOWN, buff=0.5)

        self.play(FadeIn(head), run_time=0.4)
        self.play(FadeIn(left_col), run_time=0.5)
        self.play(Create(div), run_time=0.3)
        self.play(FadeIn(right_col), run_time=0.5)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.5, total - 2.1))


class B04_SelfConsistentWrong(Scene):
    def construct(self):
        total = DUR["B04"]
        t1 = Text("The tests passed.", font=SERIF, color=INK,
                  font_size=42, weight="BOLD")
        t2 = Text("The need was never tested.", font=SERIF,
                  color=CRIMSON, font_size=40, weight="BOLD")
        t3 = Text("These are not the same thing.", font=SERIF,
                  color=INK, font_size=36)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.30).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.12, t2.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.play(FadeIn(t3), run_time=0.5)
        self.wait(max(0.5, total - 1.8))


class B06_ThreePasses(Scene):
    def construct(self):
        total = DUR["B06"]
        head = Text("Three verification passes.", font=DISPLAY,
                    color=INK, font_size=26, weight="MEDIUM").to_edge(UP, buff=0.6)

        rows_data = [
            ("Pass 1", "functional — happy path", INK),
            ("Pass 2", "edge cases — boundaries the SDD names", INK),
            ("Pass 3", "SDD needs — read aloud against the running build", CRIMSON),
        ]
        rows = VGroup(*[_pass_row(lbl, dsc, col) for lbl, dsc, col in rows_data])
        rows.arrange(DOWN, buff=0.22).move_to(DOWN * 0.2)

        note = Text("Pass 3 is the pass you cannot automate.", font=SERIF,
                    color=CRIMSON, font_size=21, slant=ITALIC).to_edge(DOWN, buff=0.5)

        self.play(FadeIn(head), run_time=0.4)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.08), run_time=0.5)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.5, total - 0.4 - len(rows) * 0.5 - 0.4))


class B07_FunctionallyCorrectNeedfullyWrong(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("Pass 3 fails when the build is", font=SERIF,
                  color=INK, font_size=36)
        t2 = Text("functionally correct", font=SERIF,
                  color=INK, font_size=40, weight="BOLD")
        t3 = Text("and needfully wrong.", font=SERIF,
                  color=CRIMSON, font_size=40, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.28).move_to(ORIGIN)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.5)
        self.play(FadeIn(t2), run_time=0.5)
        self.play(FadeIn(t3), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.7))


class B08_Practice(Scene):
    def construct(self):
        total = DUR["B08"]
        head = Text("Before you commit:", font=DISPLAY,
                    color=INK, font_size=26, weight="MEDIUM").to_edge(UP, buff=0.6)

        steps_data = [
            ("1.", "Open the SDD."),
            ("2.", "Read each user-need sentence aloud."),
            ("3.", "Look at the running build after each sentence."),
            ("4.", "Ask: does a fresh user experience this as true?"),
        ]
        items = VGroup()
        for num, text in steps_data:
            n = Text(num, font=MONO, color=INK, font_size=22)
            t = Text(text, font=SERIF, color=INK, font_size=22, slant=ITALIC)
            row = VGroup(n, t).arrange(RIGHT, buff=0.3)
            if row.width > 11.2:
                row.scale_to_fit_width(11.2)
            items.add(row)
        items.arrange(DOWN, buff=0.38, aligned_edge=LEFT).move_to(DOWN * 0.1)

        note = Text("This is not a test. It is judgment.", font=SERIF,
                    color=CRIMSON, font_size=21, slant=ITALIC).to_edge(DOWN, buff=0.5)

        self.play(FadeIn(head), run_time=0.4)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.1), run_time=0.4)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.5, total - 0.4 - len(items) * 0.4 - 0.4))


class B09_End(Scene):
    def construct(self):
        total = DUR["B09"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("Tests passing is not done.", font=SERIF,
                  color=INK, font_size=42, weight="BOLD")
        t2 = Text("Done means the SDD's needs are met.", font=SERIF,
                  color=INK, font_size=34)
        if t2.width > 12.0:
            t2.scale_to_fit_width(12.0)
        t3 = Text("Read them aloud. Before you commit.", font=SERIF,
                  color=CRIMSON, font_size=36, weight="BOLD")
        if t3.width > 12.0:
            t3.scale_to_fit_width(12.0)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.25).move_to(UP * 0.15)
        eye.next_to(block, UP, buff=0.55)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.8)
        self.play(FadeIn(t3), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 2.0))
