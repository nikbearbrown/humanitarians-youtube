"""vox_scenes.py — Why Slopsquatting Turns Claude's Wrong Answer Into a Security Hole
(slopsquatting-hallucinated-package, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'.
B07 is the STILL (ai slot) — no scene here.

Color law (teardown palette): CRIMSON = hallucinated package / attacker / silent compromise.
INK = verified package / plausibility audit / the defense. Single accent. Never swap.

Exclusions: no supply-chain methodology, no PyPI policy, no formal threat model, no cross-ecosystem.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403

DUR = {
    "B01": 18.0, "B02": 11.0, "B03": 20.0, "B04": 20.0,
    "B05": 24.0, "B06": 16.0, "B08": 22.0, "B09": 17.0,
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


def _step_box(label, color=INK, w=3.2, h=0.64):
    box = Rectangle(width=w, height=h).set_fill(color, 0.10).set_stroke(color, 1.8)
    txt = Text(label, font=SERIF, color=color, font_size=19, slant=ITALIC)
    if txt.width > w * 0.88:
        txt.scale_to_fit_width(w * 0.88)
    txt.move_to(box)
    return VGroup(box, txt)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("Claude writes: import requests_oauth_helper", font=MONO,
                  color=CRIMSON, font_size=22, weight="BOLD")
        if t1.width > 12.0:
            t1.scale_to_fit_width(12.0)
        t2 = Text("pip install: succeeds.", font=SERIF, color=INK, font_size=36)
        t3 = Text("Attacker's code runs.", font=SERIF, color=CRIMSON, font_size=44,
                  weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.30).move_to(UP * 0.2)
        eye.next_to(block, UP, buff=0.6)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), FadeIn(t3), Create(u), run_time=0.8)
        self.wait(max(0.5, total - 1.9))


class B02_TheQuestion(Scene):
    def construct(self):
        total = DUR["B02"]
        t1 = Text("A package that exists should be safe.", font=SERIF,
                  color=INK, font_size=36, weight="BOLD")
        t2 = Text("Why did this one run the attacker's code?", font=SERIF,
                  color=CRIMSON, font_size=34, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.44).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.12, t2.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B03_HallucRate(Scene):
    def construct(self):
        total = DUR["B03"]
        # Bar: 20% hallucinated of all recommended packages
        head = Text("~20% of recommended package names", font=DISPLAY, color=INK,
                    font_size=24, weight="MEDIUM").to_edge(UP, buff=0.65)
        sub = Text("don't exist (Spracklen et al.)", font=SERIF, color=INK,
                   font_size=22, slant=ITALIC).next_to(head, DOWN, buff=0.15)

        # Bar chart: 80% real (INK), 20% hallucinated (CRIMSON)
        bar_w = 9.0
        bar_h = 1.0
        real_w = bar_w * 0.80
        hall_w = bar_w * 0.20

        real_bar = Rectangle(width=real_w, height=bar_h)
        real_bar.set_fill(INK, 0.25).set_stroke(INK, 1.4)
        hall_bar = Rectangle(width=hall_w, height=bar_h)
        hall_bar.set_fill(CRIMSON, 0.60).set_stroke(CRIMSON, 1.8)

        bars = VGroup(real_bar, hall_bar).arrange(RIGHT, buff=0).move_to(DOWN * 0.3)

        real_lbl = Text("80% real", font=DISPLAY, color=INK, font_size=20,
                        weight="MEDIUM").move_to(real_bar)
        hall_lbl = Text("20%", font=DISPLAY, color=INK, font_size=22,
                        weight="MEDIUM").next_to(hall_bar, UP, buff=0.15)

        note = Text("plausible names that do not exist", font=SERIF, color=CRIMSON,
                    font_size=22, slant=ITALIC).move_to(DOWN * 1.6)

        self.play(FadeIn(head), FadeIn(sub), run_time=0.5)
        self.play(Create(real_bar), Create(hall_bar), run_time=0.8)
        self.play(FadeIn(real_lbl), FadeIn(hall_lbl), run_time=0.5)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.5, total - 2.2))


class B04_Recurrence(Scene):
    def construct(self):
        total = DUR["B04"]
        t1 = Text("58% of hallucinated names", font=SERIF, color=INK,
                  font_size=40, weight="BOLD")
        t2 = Text("repeat across queries.", font=SERIF, color=INK, font_size=40)
        t3 = Text("Attackers can predict them.", font=SERIF, color=CRIMSON,
                  font_size=44, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.30).move_to(ORIGIN)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.8)
        self.play(FadeIn(t3), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.5))


class B05_ThreeSteps(Scene):
    def construct(self):
        total = DUR["B05"]
        steps = [
            ("model hallucinates\npackage name", CRIMSON),
            ("attacker registers\nthat name on PyPI", CRIMSON),
            ("student installs —\nattacker's code runs", CRIMSON),
        ]
        boxes = VGroup(*[_step_box(t, c, w=3.4, h=0.9) for t, c in steps])
        boxes.arrange(RIGHT, buff=0.5).move_to(UP * 0.2)

        arrows = VGroup()
        for i in range(len(boxes) - 1):
            a = _arrow(boxes[i].get_right(), boxes[i+1].get_left(), CRIMSON)
            arrows.add(a)

        nums = VGroup()
        for i, box in enumerate(boxes):
            n = Text(str(i+1), font=DISPLAY, color=CRIMSON, font_size=30,
                     weight="MEDIUM").next_to(box, UP, buff=0.2)
            nums.add(n)

        label = Text("slopsquatting", font=SERIF, color=CRIMSON, font_size=28,
                     slant=ITALIC, weight="BOLD").move_to(DOWN * 1.8)

        self.play(FadeIn(boxes[0]), FadeIn(nums[0]), run_time=0.5)
        self.play(Create(arrows[0]), FadeIn(boxes[1]), FadeIn(nums[1]), run_time=0.6)
        self.play(Create(arrows[1]), FadeIn(boxes[2]), FadeIn(nums[2]), run_time=0.6)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(max(0.5, total - 2.2))


class B06_Predictable(Scene):
    def construct(self):
        total = DUR["B06"]
        t1 = Text("The hallucination is predictable.", font=SERIF,
                  color=INK, font_size=44, weight="BOLD")
        t2 = Text("Which means it is targetable.", font=SERIF,
                  color=CRIMSON, font_size=44, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.44).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B08_Defense(Scene):
    def construct(self):
        total = DUR["B08"]
        head = Text("Before every pip install or npm install:", font=DISPLAY,
                    color=INK, font_size=24, weight="MEDIUM").to_edge(UP, buff=0.6)

        checks = [
            ("open pypi.org or npmjs.com", INK),
            ("confirm the package exists", INK),
            ("confirm it is the one you meant", INK),
            ("confirm it has a real history", INK),
            ("then install", INK),
        ]
        items = VGroup()
        for i, (text, color) in enumerate(checks):
            num = Text(f"{i+1}.", font=MONO, color=color, font_size=22)
            lbl = Text(text, font=SERIF, color=color, font_size=22, slant=ITALIC)
            row = VGroup(num, lbl).arrange(RIGHT, buff=0.3)
            items.add(row)
        items.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(DOWN * 0.1)

        note = Text("never let Claude's import be the only source of truth", font=SERIF,
                    color=CRIMSON, font_size=21, slant=ITALIC).to_edge(DOWN, buff=0.5)

        self.play(FadeIn(head), run_time=0.4)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.1), run_time=0.4)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.5, total - 0.4 - len(checks) * 0.4 - 0.4))


class B09_End(Scene):
    def construct(self):
        total = DUR["B09"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("Claude's suggested import", font=SERIF, color=INK,
                  font_size=42, weight="BOLD")
        t2 = Text("is not a verified package.", font=SERIF, color=INK,
                  font_size=42)
        t3 = Text("Verify before you install.", font=SERIF, color=CRIMSON,
                  font_size=44, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.25).move_to(UP * 0.15)
        eye.next_to(block, UP, buff=0.6)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.8)
        self.play(FadeIn(t3), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 2.0))
