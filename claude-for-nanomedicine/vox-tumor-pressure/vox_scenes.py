"""vox_scenes.py — Why the Drug Reached the Tumor and the Tumor Still Grew Back
(vox-tumor-pressure, slate cut, 16:9)

One Scene per GRAPHIC / CARD / DOCUMENT / COMPOSITE beat whose source is 'own'.
B02 is a STILL (ai media slot) and has no scene here.

Color law:
  TEAL   = drug / nanoparticles accumulating at the rim
  CRIMSON = unreached core / outward pressure / regrowth
  GOLD   = pressure gradient highlight (fill only, once per graphic)

EXCLUSIONS: diffusion limit derivation, four-barrier list, 30-vs-150nm debate,
radiation resistance. Kept: outward-pressure mechanism + inside-out regrowth.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene
import json, os
import numpy as np

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 12)}


# ─────────────────────────────────────────────────────── B01 · Title card

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why the Drug Reached the Tumor", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("and the Tumor Still Grew Back", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ─────────────────────────────────────────────────────── B03 · Question card

class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text("A drug reaches the tumor.", font=SERIF, color=INK, font_size=34)
        q2 = Text("Vessels are leaky. Particles accumulate.", font=SERIF, color=INK, font_size=34)
        q3 = Text("The outer rim is cleared.", font=SERIF, color=TEAL, font_size=34)
        q4 = Text("Weeks later, the tumor regrows from the inside.", font=SERIF, color=CRIMSON, font_size=34)
        q5 = Text("The drug was there.", font=SERIF, color=INK, font_size=34, slant=ITALIC)
        q6 = Text("Why did the core survive?", font=DISPLAY, color=INK, font_size=38, weight=BOLD)
        block = VGroup(q1, q2, q3, q4, q5).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        block.move_to(UP * 0.4)
        q6.next_to(block, DOWN, buff=0.38)
        u = Line(q6.get_corner(DL) + DOWN * 0.12, q6.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(block), run_time=1.0)
        self.play(FadeIn(q6), Create(u), run_time=0.9)
        self.wait(max(0.3, total - 1.9))


# ─────────────────────────────────────────────────────── B04 · Leaky vessels reveal

class B04_LeakyVessels(Scene):
    def construct(self):
        total = DUR["B04"]
        # Vessel on left, interstitium in center, arrow pointing right (inward)
        vessel = Rectangle(width=1.6, height=3.0)
        vessel.set_fill(TEAL, 0.18).set_stroke(TEAL, 2.5)
        vessel.move_to(LEFT * 4.5)
        vlabel = LabelChip("leaky vessel", accent=TEAL, size=18)
        vlabel.next_to(vessel, UP, buff=0.22)

        # Gap in vessel wall — small opening
        gap = Line(vessel.get_right() + UP * 0.3, vessel.get_right() + DOWN * 0.3,
                   color=GROUND, stroke_width=6)

        # Particles leaking out (small TEAL dots)
        particles = VGroup()
        for offset in [UP * 0.28, ORIGIN, DOWN * 0.28]:
            dot = Dot(radius=0.10, color=TEAL).move_to(vessel.get_right() + offset)
            particles.add(dot)

        # Interstitium — wide space in the middle (above the arrow, clear of strokes)
        matrix_label = SerifLabel("interstitium", SLATE, size=22).move_to(ORIGIN + UP * 1.2)

        # Arrows going right (inward, toward the core)
        arrow_in = Arrow(LEFT * 1.8, LEFT * 0.4, buff=0, color=TEAL,
                         stroke_width=3, max_tip_length_to_length_ratio=0.25)
        in_label = SerifLabel("particles enter", TEAL, size=18)
        in_label.next_to(arrow_in, UP, buff=0.18)

        # Core on right
        core = Circle(radius=1.0)
        core.set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2)
        core.move_to(RIGHT * 3.8)
        clabel = LabelChip("core", accent=CRIMSON, size=20)
        clabel.move_to(core.get_center())

        self.play(FadeIn(vessel), FadeIn(vlabel), run_time=0.7)
        self.play(Create(gap), FadeIn(particles), run_time=0.6)
        self.play(FadeIn(matrix_label), run_time=0.5)
        self.play(GrowArrow(arrow_in), FadeIn(in_label), run_time=0.7)
        self.play(GrowFromCenter(core), FadeIn(clabel), run_time=0.7)
        self.wait(max(0.3, total - 3.2))


# ─────────────────────────────────────────────────────── B05 · Pressure builds

class B05_PressureBuilds(Scene):
    def construct(self):
        total = DUR["B05"]

        # Tumor circle
        tumor = Circle(radius=2.0)
        tumor.set_stroke(INK, 2).set_fill(GROUND, 1)
        tumor.move_to(ORIGIN)

        # Fluid pouring in — arrows from outside pointing inward
        in_arrows = VGroup()
        for angle in np.linspace(0, 2 * np.pi, 5, endpoint=False):
            start = np.array([np.cos(angle) * 3.0, np.sin(angle) * 3.0, 0])
            end = np.array([np.cos(angle) * 2.15, np.sin(angle) * 2.15, 0])
            a = Arrow(start, end, buff=0, color=TEAL, stroke_width=3,
                      max_tip_length_to_length_ratio=0.3)
            in_arrows.add(a)

        fluid_label = LabelChip("fluid pours in", accent=TEAL, size=18)
        fluid_label.move_to(UP * 3.1)

        # Broken lymphatic — label with strikethrough
        lymph = SerifLabel("lymphatics: broken", CRIMSON, size=22)
        lymph.move_to(DOWN * 3.1)

        # Pressure rising — fill the tumor interior with GOLD highlight
        pressure_fill = Circle(radius=1.8)
        pressure_fill.set_fill(GOLD, 0.28).set_stroke(width=0, opacity=0)
        pressure_fill.move_to(ORIGIN)

        pressure_label = LabelChip("pressure builds", accent=CRIMSON, size=20)
        pressure_label.move_to(ORIGIN)

        self.play(GrowFromCenter(tumor), run_time=0.6)
        self.play(FadeIn(fluid_label), *[GrowArrow(a) for a in in_arrows], run_time=0.8)
        self.play(FadeIn(lymph, shift=UP * 0.1), run_time=0.6)
        self.play(GrowFromCenter(pressure_fill), run_time=0.7)
        self.play(FadeIn(pressure_label), run_time=0.5)
        self.wait(max(0.3, total - 3.2))


# ─────────────────────────────────────────────────────── B06 · Pressure flow trace

class B06_PressureFlow(Scene):
    def construct(self):
        total = DUR["B06"]

        # Tumor cross-section
        tumor = Circle(radius=2.2)
        tumor.set_stroke(INK, 2).set_fill(GROUND, 1)

        # Rim band (TEAL — where particles accumulate)
        rim = Annulus(inner_radius=1.6, outer_radius=2.2, color=TEAL)
        rim.set_fill(TEAL, 0.25).set_stroke(width=0, opacity=0)

        # Core (CRIMSON — unreached)
        core = Circle(radius=1.1)
        core.set_fill(CRIMSON, 0.25).set_stroke(CRIMSON, 1.5)

        # Labels
        rim_label = Text("drug accumulates", font=DISPLAY, font_size=14, color=TEAL)
        rim_label.move_to(RIGHT * 1.9 + UP * 1.85)
        core_label = Text("unreached core", font=DISPLAY, font_size=14, color=CRIMSON)
        core_label.move_to(ORIGIN)

        # Outward pressure arrows (CRIMSON) — from center outward
        arrows = VGroup()
        for angle in np.linspace(0, 2 * np.pi, 6, endpoint=False):
            start = np.array([np.cos(angle) * 0.4, np.sin(angle) * 0.4, 0])
            end = np.array([np.cos(angle) * 1.0, np.sin(angle) * 1.0, 0])
            a = Arrow(start, end, buff=0, color=CRIMSON, stroke_width=3,
                      max_tip_length_to_length_ratio=0.3)
            arrows.add(a)

        # IFP label with GOLD highlight
        ifp_label = SerifLabel("outward fluid pressure", CRIMSON, size=20)
        ifp_label.move_to(DOWN * 3.1)

        self.play(GrowFromCenter(tumor), run_time=0.6)
        self.play(GrowFromCenter(rim), run_time=0.5)
        self.play(GrowFromCenter(core), run_time=0.5)
        self.play(Write(rim_label), Write(core_label), run_time=0.5)
        self.play(*[GrowArrow(a) for a in arrows], run_time=0.8)
        self.play(FadeIn(ifp_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.4))


# ─────────────────────────────────────────────────────── B07 · Particles pushed back

class B07_ParticlesPushedBack(Scene):
    def construct(self):
        total = DUR["B07"]

        # Tumor cross-section
        tumor = Circle(radius=2.2)
        tumor.set_stroke(INK, 2).set_fill(GROUND, 1)

        # Rim band (TEAL)
        rim = Annulus(inner_radius=1.6, outer_radius=2.2, color=TEAL)
        rim.set_fill(TEAL, 0.30).set_stroke(width=0, opacity=0)

        # Core (CRIMSON)
        core = Circle(radius=1.1)
        core.set_fill(CRIMSON, 0.30).set_stroke(CRIMSON, 1.5)

        core_label = Text("particle-free core", font=DISPLAY, font_size=13, color=CRIMSON)
        core_label.move_to(ORIGIN)

        # Outward pressure arrows
        out_arrows = VGroup()
        for angle in np.linspace(0, 2 * np.pi, 6, endpoint=False):
            start = np.array([np.cos(angle) * 0.35, np.sin(angle) * 0.35, 0])
            end = np.array([np.cos(angle) * 0.95, np.sin(angle) * 0.95, 0])
            a = Arrow(start, end, buff=0, color=CRIMSON, stroke_width=2.5,
                      max_tip_length_to_length_ratio=0.3)
            out_arrows.add(a)

        # Particle dots accumulating in rim
        rim_dots = VGroup()
        for angle in np.linspace(0, 2 * np.pi, 10, endpoint=False):
            r = 1.85 + 0.18 * np.sin(angle * 3)
            dot = Dot(radius=0.09, color=TEAL)
            dot.move_to(np.array([np.cos(angle) * r, np.sin(angle) * r, 0]))
            rim_dots.add(dot)

        # A particle path: enters from outside, gets pushed back
        entry_pt = np.array([3.0, 0.0, 0])
        rim_pt = np.array([2.0, 0.0, 0])
        pushed_pt = np.array([1.8, 0.0, 0])
        tracer = Dot(radius=0.13, color=TEAL).move_to(entry_pt)

        # Annotation
        pushback_label = SerifLabel("pushed back to rim", CRIMSON, size=20)
        pushback_label.move_to(DOWN * 3.1)

        self.play(GrowFromCenter(tumor), run_time=0.5)
        self.play(GrowFromCenter(rim), GrowFromCenter(core), run_time=0.5)
        self.play(FadeIn(core_label), run_time=0.4)
        self.play(*[GrowArrow(a) for a in out_arrows], run_time=0.7)
        self.play(FadeIn(tracer), run_time=0.3)
        self.play(tracer.animate.move_to(rim_pt), run_time=0.5)
        self.play(tracer.animate.move_to(pushed_pt), run_time=0.4)
        self.play(FadeIn(rim_dots), run_time=0.5)
        self.play(FadeIn(pushback_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 4.3))


# ─────────────────────────────────────────────────────── B08 · Hypoxic core reveal

class B08_HypoxicCore(Scene):
    def construct(self):
        total = DUR["B08"]

        # Large tumor cross-section, emphasis on the core
        tumor = Circle(radius=2.2)
        tumor.set_stroke(INK, 2).set_fill(GROUND, 1)

        rim = Annulus(inner_radius=1.6, outer_radius=2.2, color=TEAL)
        rim.set_fill(TEAL, 0.20).set_stroke(width=0, opacity=0)

        core = Circle(radius=1.1)
        core.set_fill(CRIMSON, 0.35).set_stroke(CRIMSON, 2)

        # Labels
        rim_label = LabelChip("rim cleared", accent=TEAL, size=18)
        rim_label.move_to(RIGHT * 1.95 + UP * 1.9)

        core_chip = LabelChip("hypoxic core", accent=CRIMSON, size=20)
        core_chip.move_to(ORIGIN)

        # Selection text — appears below
        sel_label = SerifLabel("hypoxia selects for resistant cells", CRIMSON, size=22)
        sel_label.move_to(DOWN * 3.1)

        # Small dots inside core representing surviving resistant cells
        resistant_dots = VGroup()
        for angle in np.linspace(0, 2 * np.pi, 7, endpoint=False):
            r = 0.55
            dot = Dot(radius=0.10, color=CRIMSON)
            dot.move_to(np.array([np.cos(angle) * r, np.sin(angle) * r, 0]))
            resistant_dots.add(dot)

        self.play(GrowFromCenter(tumor), run_time=0.5)
        self.play(GrowFromCenter(rim), FadeIn(rim_label), run_time=0.6)
        self.play(GrowFromCenter(core), run_time=0.5)
        self.play(FadeIn(core_chip), run_time=0.4)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in resistant_dots],
                               lag_ratio=0.1, run_time=0.9))
        self.play(FadeIn(sel_label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.5))


# ─────────────────────────────────────────────────────── B09 · Inside-out quote

class B09_InsideOutQuote(Scene):
    def construct(self):
        total = DUR["B09"]
        _quote_scene(
            self,
            "The rim cells the drug killed were not the cells most likely to cause recurrence."
            " The core cells it never reached were.",
            "— outward pressure, inward selection",
            None,
            "core cells",
            total,
            qsize=36,
        )


# ─────────────────────────────────────────────────────── B10 · Example drawon

class B10_Example(Scene):
    def construct(self):
        total = DUR["B10"]

        # Header
        header = LabelChip("illustrative scenario", accent=SLATE, size=20)
        header.to_edge(UP, buff=0.55)

        # Tumor diagram — show pressure gradient with numbers
        tumor_outline = Circle(radius=1.8)
        tumor_outline.set_stroke(INK, 2).set_fill(GROUND, 1)
        tumor_outline.move_to(LEFT * 3.2 + DOWN * 0.2)

        rim_band = Annulus(inner_radius=1.25, outer_radius=1.8, color=TEAL)
        rim_band.set_fill(TEAL, 0.30).set_stroke(width=0, opacity=0)
        rim_band.move_to(tumor_outline.get_center())

        core_circle = Circle(radius=0.75)
        core_circle.set_fill(CRIMSON, 0.40).set_stroke(CRIMSON, 2)
        core_circle.move_to(tumor_outline.get_center())

        # Rim label
        rim_tag = Text("rim", font=DISPLAY, font_size=13, color=TEAL)
        rim_tag.move_to(tumor_outline.get_center() + RIGHT * 1.56 + UP * 0.5)

        # Pressure values — MONO font for numbers
        core_pressure = Text("25 mmHg", font=MONO, font_size=22, color=CRIMSON)
        core_pressure.move_to(tumor_outline.get_center())

        rim_pressure = Text("5 mmHg", font=MONO, font_size=18, color=TEAL)
        rim_pressure.move_to(tumor_outline.get_center() + RIGHT * 1.5 + DOWN * 0.4)

        ifp_arrow = Arrow(
            tumor_outline.get_center() + RIGHT * 0.4,
            tumor_outline.get_center() + RIGHT * 1.15,
            buff=0, color=CRIMSON, stroke_width=2.5, max_tip_length_to_length_ratio=0.28
        )

        # Right panel — timeline text
        wk3 = Text("Week 3: rim -60%, core intact", font=SERIF, font_size=24, color=INK)
        wk8 = Text("Week 8: volume doubled", font=SERIF, font_size=24, color=CRIMSON)
        origin = Text("growth from core", font=SERIF, font_size=24, color=CRIMSON, slant=ITALIC)
        timeline = VGroup(wk3, wk8, origin).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        timeline.move_to(RIGHT * 2.8 + DOWN * 0.2)

        self.play(FadeIn(header), run_time=0.5)
        self.play(GrowFromCenter(tumor_outline), run_time=0.5)
        self.play(GrowFromCenter(rim_band), GrowFromCenter(core_circle), run_time=0.6)
        self.play(FadeIn(rim_tag), run_time=0.4)
        self.play(FadeIn(core_pressure), FadeIn(rim_pressure), GrowArrow(ifp_arrow), run_time=0.7)
        self.play(FadeIn(wk3, shift=LEFT * 0.2), run_time=0.6)
        self.play(FadeIn(wk8, shift=LEFT * 0.2), run_time=0.6)
        self.play(FadeIn(origin, shift=LEFT * 0.2), run_time=0.6)
        self.wait(max(0.3, total - 4.5))


# ─────────────────────────────────────────────────────── B11 · Endcard

class B11_Endcard(Scene):
    def construct(self):
        total = DUR["B11"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("The accumulation was real.", font=DISPLAY, color=INK,
                  font_size=32, weight=BOLD)
        t2 = Text("The delivery was not.", font=DISPLAY, color=CRIMSON,
                  font_size=32, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.5)
        sub = Text("outward pressure walls off the core", font=SERIF, color=INK, font_size=22,
                   slant=ITALIC)
        sub.next_to(u, DOWN, buff=0.42)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 2.2))
