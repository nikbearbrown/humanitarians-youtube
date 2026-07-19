"""vox_scenes.py -- embedded-ai/youtube/cli-pareto-selector
Reel: Build a Pareto Model-Selector with Claude Code
Palette: teardown (white ground, ink originals, crimson = error/mash)

teardown token mapping:
  GROUND  #FFFFFF  background
  INK     #2A1A0E  originals, axes, all text
  CRIMSON #C8102E  quantized / error / mash
  SLATE   #545454  structure, neutral chips (dominated models)

Gate A: every scene needs Create/GrowFromCenter/Transform.
Gate W: no Unicode arrows/checkmarks in Text(). x in [-6.3, 6.3], y in [-3.4, 3.4].
No Manim Axes class -- draw axes manually with Line().
"""

import sys, json, pathlib, os, numpy as np
os.environ.setdefault("VOX_PALETTE", "teardown")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene

DUR: dict = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass
_DEFAULTS = {"B01":14.0,"B04":17.0,"B06":12.0,"B07":11.0,"B08":10.0}
def _dur(bid): return DUR.get(bid,_DEFAULTS.get(bid,10.0))


# =============================================================================
# B01_Problem -- leaderboard accuracy lie
# =============================================================================
class B01_Problem(Scene):
    """Title card: leaderboard winner fails on device; Pareto as the fix."""

    def construct(self):
        dur = _dur("B01")

        hdr = Text("PARETO MODEL SELECTION", font=DISPLAY, color=INK, font_size=30)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.5)

        chip_lb = LabelChip("LEADERBOARD WINNER: 94% ACC", accent=CRIMSON, size=22)
        chip_lb.move_to([0.0, 1.7, 0])
        self.play(GrowFromCenter(chip_lb), run_time=0.4)

        row_bad = Text("400ms on device  --  deadline missed",
                       font=DISPLAY, color=INK, font_size=21)
        row_bad.move_to([0.0, 1.0, 0])
        self.play(FadeIn(row_bad), run_time=0.4)

        sep2 = Line([-5.5, 0.45, 0], [5.5, 0.45, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.35)
        self.play(Create(sep2), run_time=0.3)

        chip_p = LabelChip("PARETO FRONTIER", accent=INK, size=22)
        chip_p.move_to([0.0, -0.2, 0])
        self.play(GrowFromCenter(chip_p), run_time=0.4)

        row_good = Text("90% acc  60ms  -- fits the deadline",
                        font=DISPLAY, color=INK, font_size=21)
        row_good.move_to([0.0, -0.9, 0])
        self.play(FadeIn(row_good), run_time=0.4)

        foot = Text("Single-number benchmarks optimize for the wrong constraints.",
                    font=SERIF, color=INK, font_size=20)
        foot.move_to([0.0, -2.0, 0])
        self.play(FadeIn(foot), run_time=0.5)

        elapsed = 0.4+0.5+0.4+0.4+0.3+0.4+0.4+0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B04_Pareto -- scatter plot + Pareto frontier animation
# =============================================================================
class B04_Pareto(Scene):
    """8 model dots appear, dominated ones transform to SLATE,
    Pareto frontier line draws through survivors.

    Illustrative model positions (accuracy vs latency):
    A: acc=90%, lat=100ms  scene: (-3.0, 0.0)  -- frontier
    B: acc=88%, lat=80ms   scene: (-3.8, -0.8) -- frontier
    C: acc=85%, lat=60ms   scene: (-4.6, -2.0) -- frontier
    D: acc=92%, lat=200ms  scene: (0.8, 1.0)   -- frontier
    E: acc=94%, lat=400ms  scene: (3.8, 2.0)   -- frontier
    F: acc=87%, lat=150ms  scene: (-1.5, -1.2) -- DOMINATED
    G: acc=89%, lat=250ms  scene: (1.5, -0.5)  -- DOMINATED
    H: acc=86%, lat=200ms  scene: (0.8, -1.6)  -- DOMINATED
    """

    def construct(self):
        dur = _dur("B04")

        # ── header ────────────────────────────────────────────────────────────
        hdr = Text("PARETO FRONTIER", font=DISPLAY, color=INK, font_size=28)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── axes (manual, no Axes class) ──────────────────────────────────────
        # X axis: latency 0-500ms, scene x=-5.5 to 5.5
        # Y axis: accuracy 75-95%, scene y=-2.8 to 2.8
        ax_x = Line([-5.5, -2.8, 0], [5.5, -2.8, 0], stroke_width=1.2, color=SLATE)
        ax_y = Line([-5.5, -2.8, 0], [-5.5, 2.8, 0], stroke_width=1.2, color=SLATE)
        ax_x.set_stroke(opacity=0.7)
        ax_y.set_stroke(opacity=0.7)
        self.play(Create(ax_x), Create(ax_y), run_time=0.5)

        # Axis labels
        lbl_x = Text("LATENCY (ms)", font=DISPLAY, color=SLATE, font_size=17)
        lbl_x.move_to([0.0, -3.25, 0])
        lbl_y = Text("ACC %", font=DISPLAY, color=SLATE, font_size=17)
        lbl_y.rotate(PI / 2)
        lbl_y.move_to([-5.0, 0.0, 0])
        self.play(FadeIn(lbl_x), FadeIn(lbl_y), run_time=0.3)

        # ── model positions ────────────────────────────────────────────────────
        models = {
            "A": {"pos": [-3.0,  0.0, 0], "frontier": True},
            "B": {"pos": [-3.8, -0.8, 0], "frontier": True},
            "C": {"pos": [-4.6, -2.0, 0], "frontier": True},
            "D": {"pos": [ 0.8,  1.0, 0], "frontier": True},
            "E": {"pos": [ 3.8,  2.0, 0], "frontier": True},
            "F": {"pos": [-1.5, -1.2, 0], "frontier": False},
            "G": {"pos": [ 1.5, -0.5, 0], "frontier": False},
            "H": {"pos": [ 0.8, -1.6, 0], "frontier": False},
        }

        dots = {}
        labels = {}
        for name, info in models.items():
            dot = Dot(point=info["pos"], radius=0.18, color=INK)
            lbl = Text(name, font=DISPLAY, color=INK, font_size=18)
            lbl.move_to([info["pos"][0] + 0.3, info["pos"][1] + 0.3, 0])
            self.play(GrowFromCenter(dot), run_time=0.3)
            self.play(FadeIn(lbl), run_time=0.2)
            dots[name] = dot
            labels[name] = lbl

        # ── transform dominated models to SLATE ───────────────────────────────
        for name in ["F", "G", "H"]:
            grey_dot = Dot(point=models[name]["pos"], radius=0.18, color=SLATE)
            grey_lbl = Text(name, font=DISPLAY, color=SLATE, font_size=18)
            grey_lbl.move_to([models[name]["pos"][0] + 0.3,
                               models[name]["pos"][1] + 0.3, 0])
            self.play(
                Transform(dots[name], grey_dot),
                Transform(labels[name], grey_lbl),
                run_time=0.5
            )

        # ── draw Pareto frontier line through survivors ────────────────────────
        # Frontier models sorted by latency: C, B, A, D, E
        frontier_pts = [
            models["C"]["pos"],
            models["B"]["pos"],
            models["A"]["pos"],
            models["D"]["pos"],
            models["E"]["pos"],
        ]
        for i in range(len(frontier_pts) - 1):
            p0 = frontier_pts[i]
            p1 = frontier_pts[i + 1]
            seg = Line(p0, p1, stroke_width=2.0, color=INK)
            self.play(Create(seg), run_time=0.4)

        # ── frontier chip ─────────────────────────────────────────────────────
        chip_f = LabelChip("PARETO FRONTIER", accent=INK, size=19)
        chip_f.move_to([0.0, 2.5, 0])
        self.play(GrowFromCenter(chip_f), run_time=0.4)

        elapsed = 0.4 + 0.5 + 0.3 + 8*0.3 + 8*0.2 + 3*0.5 + 4*0.4 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B06_ParetoCap -- apply 250ms constraint mask, recompute frontier
# =============================================================================
class B06_ParetoCap(Scene):
    """Same plane. 250ms vertical constraint line appears.
    Model E (400ms) transforms to SLATE. New frontier redraws.
    """

    def construct(self):
        dur = _dur("B06")

        hdr = Text("CONSTRAINT: 250ms CAP", font=DISPLAY, color=INK, font_size=28)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── axes ──────────────────────────────────────────────────────────────
        ax_x = Line([-5.5, -2.8, 0], [5.5, -2.8, 0], stroke_width=1.2, color=SLATE)
        ax_y = Line([-5.5, -2.8, 0], [-5.5, 2.8, 0], stroke_width=1.2, color=SLATE)
        ax_x.set_stroke(opacity=0.7)
        ax_y.set_stroke(opacity=0.7)
        self.play(Create(ax_x), Create(ax_y), run_time=0.4)

        lbl_x = Text("LATENCY (ms)", font=DISPLAY, color=SLATE, font_size=17)
        lbl_x.move_to([0.0, -3.25, 0])
        self.play(FadeIn(lbl_x), run_time=0.25)

        # ── model positions (same as B04) ──────────────────────────────────────
        models = {
            "A": {"pos": [-3.0,  0.0, 0], "dominated": False, "over_cap": False},
            "B": {"pos": [-3.8, -0.8, 0], "dominated": False, "over_cap": False},
            "C": {"pos": [-4.6, -2.0, 0], "dominated": False, "over_cap": False},
            "D": {"pos": [ 0.8,  1.0, 0], "dominated": False, "over_cap": False},
            "E": {"pos": [ 3.8,  2.0, 0], "dominated": False, "over_cap": True},
            "F": {"pos": [-1.5, -1.2, 0], "dominated": True,  "over_cap": False},
            "G": {"pos": [ 1.5, -0.5, 0], "dominated": True,  "over_cap": False},
            "H": {"pos": [ 0.8, -1.6, 0], "dominated": True,  "over_cap": False},
        }

        dots = {}
        labels_obj = {}
        for name, info in models.items():
            if info["dominated"]:
                c = SLATE
            else:
                c = INK
            dot = Dot(point=info["pos"], radius=0.18, color=c)
            lbl = Text(name, font=DISPLAY, color=c, font_size=18)
            lbl.move_to([info["pos"][0] + 0.3, info["pos"][1] + 0.3, 0])
            self.play(GrowFromCenter(dot), run_time=0.25)
            self.play(FadeIn(lbl), run_time=0.15)
            dots[name] = dot
            labels_obj[name] = lbl

        # ── draw existing frontier before constraint ───────────────────────────
        frontier_pre = [models["C"]["pos"], models["B"]["pos"],
                        models["A"]["pos"], models["D"]["pos"],
                        models["E"]["pos"]]
        pre_segs = []
        for i in range(len(frontier_pre) - 1):
            seg = Line(frontier_pre[i], frontier_pre[i+1],
                       stroke_width=1.5, color=SLATE)
            seg.set_stroke(opacity=0.5)
            self.play(Create(seg), run_time=0.3)
            pre_segs.append(seg)

        # ── 250ms constraint line (x=1.5 in scene coordinates: 250ms) ─────────
        # X mapping: 0ms=-5.5, 500ms=5.5 -> 250ms = 0.0 scene x
        cap_x = 0.0   # 250ms maps to x=0.0
        cap_line = Line([cap_x, -2.8, 0], [cap_x, 2.8, 0],
                        stroke_width=2.0, color=CRIMSON)
        cap_line.set_stroke(opacity=0.8)
        self.play(Create(cap_line), run_time=0.6)

        cap_chip = LabelChip("250ms CAP", accent=CRIMSON, size=19)
        cap_chip.move_to([1.4, 2.5, 0])
        self.play(GrowFromCenter(cap_chip), run_time=0.35)

        # ── Model E greys out (over cap) ──────────────────────────────────────
        grey_e = Dot(point=models["E"]["pos"], radius=0.18, color=SLATE)
        grey_lbl_e = Text("E", font=DISPLAY, color=SLATE, font_size=18)
        grey_lbl_e.move_to([models["E"]["pos"][0] + 0.3,
                             models["E"]["pos"][1] + 0.3, 0])
        self.play(Transform(dots["E"], grey_e),
                  Transform(labels_obj["E"], grey_lbl_e), run_time=0.5)

        # ── new frontier: C, B, A, D only ─────────────────────────────────────
        frontier_new = [models["C"]["pos"], models["B"]["pos"],
                        models["A"]["pos"], models["D"]["pos"]]
        for i in range(len(frontier_new) - 1):
            seg = Line(frontier_new[i], frontier_new[i+1],
                       stroke_width=2.5, color=INK)
            self.play(Create(seg), run_time=0.4)

        new_chip = LabelChip("FRONTIER: 4 MODELS", accent=INK, size=19)
        new_chip.move_to([-3.0, 2.5, 0])
        self.play(GrowFromCenter(new_chip), run_time=0.35)

        elapsed = 0.4+0.4+0.25+8*0.25+8*0.15+4*0.3+0.6+0.35+0.5+3*0.4+0.35
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B07_Summary -- the lesson
# =============================================================================
class B07_Summary(Scene):
    """Recap: single benchmark vs Pareto frontier."""

    def construct(self):
        dur = _dur("B07")

        hdr = Text("THE LESSON", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        row1 = Text("Single benchmark:", font=DISPLAY, color=INK, font_size=23)
        row1.move_to([-2.4, 1.6, 0])
        chip1 = LabelChip("WRONG CONSTRAINTS", accent=CRIMSON, size=22)
        chip1.move_to([3.0, 1.6, 0])
        self.play(FadeIn(row1), run_time=0.35)
        self.play(GrowFromCenter(chip1), run_time=0.35)

        sep2 = Line([-5.5, 1.0, 0], [5.5, 1.0, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.35)
        self.play(Create(sep2), run_time=0.3)

        row2 = Text("Pareto frontier:", font=DISPLAY, color=INK, font_size=23)
        row2.move_to([-2.4, 0.4, 0])
        chip2 = LabelChip("YOUR CONSTRAINTS", accent=INK, size=22)
        chip2.move_to([3.0, 0.4, 0])
        self.play(FadeIn(row2), run_time=0.35)
        self.play(GrowFromCenter(chip2), run_time=0.35)

        sep3 = Line([-5.5, -0.2, 0], [5.5, -0.2, 0], stroke_width=0.8, color=SLATE)
        sep3.set_stroke(opacity=0.35)
        self.play(Create(sep3), run_time=0.3)

        foot = Text("Plot the whole field. Keep only what nothing beats on every axis.",
                    font=SERIF, color=INK, font_size=19)
        foot.move_to([0.0, -0.9, 0])
        self.play(FadeIn(foot), run_time=0.5)

        elapsed = 0.4+0.4+0.35+0.35+0.3+0.35+0.35+0.3+0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B08_NextSteps -- action items
# =============================================================================
class B08_NextSteps(Scene):
    """Next steps: eval accuracy, measure on-target, run pareto.py."""

    def construct(self):
        dur = _dur("B08")

        hdr = Text("YOUR MOVE", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        step1 = Text("· eval accuracy on your validation set",
                     font=DISPLAY, color=INK, font_size=21)
        step1.move_to([0.0, 1.7, 0])
        self.play(FadeIn(step1), run_time=0.4)

        step2 = Text("· measure latency and flash on the target hardware",
                     font=DISPLAY, color=INK, font_size=21)
        step2.move_to([0.0, 0.9, 0])
        self.play(FadeIn(step2), run_time=0.4)

        step3 = Text("· run pareto.py on your real numbers",
                     font=DISPLAY, color=INK, font_size=21)
        step3.move_to([0.0, 0.1, 0])
        self.play(FadeIn(step3), run_time=0.4)

        sep2 = Line([-5.5, -0.5, 0], [5.5, -0.5, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.35)

        note = Text("Output beats use illustrative data -- swap in real measurements.",
                    font=SERIF, color=INK, font_size=18)
        note.move_to([0.0, -1.1, 0])
        self.play(FadeIn(note), run_time=0.4)

        elapsed = 0.4+0.4+0.4+0.4+0.4+0.35+0.4
        self.wait(max(0.5, dur - elapsed))
