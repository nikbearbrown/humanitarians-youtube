"""vox_scenes.py — The Smaller Nanoparticle That Accumulates Less but Cures More
(vox-size-paradox, slate cut, 16:9)

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE beat with source='own'.
B02 and B07 are STILL·ai — no scene here.

Color law: TEAL #1F6F5C = small particle / deep penetration / cure
           CRIMSON #BF3339 = large particle / rim-crowded / bad outcome
           GOLD = editor's-pen fill highlight only (B10 quote), never text
           Two accents max — never swapped mid-film.

Card exclusions: NO IFP derivation, NO four-barrier list,
NO size-shrinking strategies, NO EPR 10-50x claim.
All B12 numbers are illustrative (labeled in FACTCHECK.md).

Gate B: every zero-width stroke is also zero-opacity.
Gate A: single-method .animate only; every scene has real shape motion.
"""
import json, os, sys, pathlib
# Resolve the vox toolkit's manim library from this file's location.
# This file lives at books/<book>/youtube/<slug>/vox_scenes.py.
# parents[3] = books/, so the toolkit is books/vox/aspects/explainer/vox-explainer/manim
_VOX_MANIM = pathlib.Path(__file__).resolve().parents[3] / "vox" / "aspects" / "explainer" / "vox-explainer" / "manim"
sys.path.insert(0, str(_VOX_MANIM))
from vox_graphics import *  # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

# ── DUR dict ─────────────────────────────────────────────────────────────────
_bs = os.path.join(os.path.dirname(os.path.abspath(__file__)), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}

# ── helpers ──────────────────────────────────────────────────────────────────

def _particle(size, color, label_text=None):
    """A single nanoparticle dot with optional label chip."""
    d = Dot(radius=size)
    d.set_fill(color, 1).set_stroke(width=0, opacity=0)
    if label_text:
        chip = LabelChip(label_text, accent=color, size=18)
        chip.next_to(d, DOWN, buff=0.12)
        return VGroup(d, chip)
    return d


def _particle_grid(n, color, radius=0.10, cols=8, row_gap=0.28, col_gap=0.28):
    """Grid of n particle dots."""
    g = VGroup()
    for i in range(n):
        d = Dot(radius=radius)
        d.set_fill(color, 1).set_stroke(width=0, opacity=0)
        x = (i % cols) * col_gap
        y = -(i // cols) * row_gap
        d.move_to(RIGHT * x + UP * y)
        g.add(d)
    return g


def _bar(width, height, color, opacity=1.0):
    b = Rectangle(width=width, height=height)
    b.set_fill(color, opacity).set_stroke(width=0, opacity=0)
    return b


def _axis_label(text, color=INK, size=22):
    return Text(text, font=MONO, color=color, font_size=size)


# ── scenes ────────────────────────────────────────────────────────────────────

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("The Smaller Nanoparticle", font=DISPLAY, color=INK, font_size=32, weight=BOLD)
        t2 = Text("That Accumulates Less but Cures More", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B03_OutcomeContrast(Scene):
    """Two tumor-volume reduction bars: crimson 150nm (15%), teal 30nm (72%)."""
    def construct(self):
        total = DUR["B03"]
        max_h = 3.8
        bar_w = 1.6

        # left: 150nm crimson — 15% reduction (small bar)
        h_left = max_h * 0.15
        bar_left = _bar(bar_w, h_left, CRIMSON)
        bar_left.align_to(DOWN * 1.6, DOWN)
        bar_left.shift(LEFT * 2.6)

        # right: 30nm teal — 72% reduction (large bar)
        h_right = max_h * 0.72
        bar_right = _bar(bar_w, h_right, TEAL)
        bar_right.align_to(DOWN * 1.6, DOWN)
        bar_right.shift(RIGHT * 2.6)

        # labels above bars
        lbl_left = Text("150 nm", font=DISPLAY, color=CRIMSON, font_size=24, weight=BOLD)
        lbl_right = Text("30 nm", font=DISPLAY, color=TEAL, font_size=24, weight=BOLD)
        lbl_left.next_to(bar_left, UP, buff=0.22)
        lbl_right.next_to(bar_right, UP, buff=0.22)

        # percent labels
        pct_left = Text("15%", font=MONO, color=CRIMSON, font_size=28)
        pct_right = Text("72%", font=MONO, color=TEAL, font_size=28)
        pct_left.next_to(bar_left, UP, buff=0.55)
        pct_right.next_to(bar_right, UP, buff=0.55)

        # axis label
        ax = SerifLabel("tumor volume reduction at day 21", INK, size=22)
        ax.move_to(DOWN * 2.1)

        # baseline
        base = Line(LEFT * 4.5 + DOWN * 1.6, RIGHT * 4.5 + DOWN * 1.6,
                    color=SLATE, stroke_width=1.8)

        # title
        eyebrow = Text("illustrative", font=MONO, color=SLATE, font_size=18)
        eyebrow.to_edge(UP, buff=0.45)

        self.play(FadeIn(base), FadeIn(eyebrow), run_time=0.5)
        self.play(
            GrowFromEdge(bar_left, DOWN),
            GrowFromEdge(bar_right, DOWN),
            run_time=1.2
        )
        self.play(
            FadeIn(lbl_left), FadeIn(lbl_right),
            FadeIn(pct_left), FadeIn(pct_right),
            FadeIn(ax),
            run_time=0.8
        )
        self.wait(max(0.3, total - 2.5))


class B04_Question(Scene):
    """THE QUESTION beat — gap formula on screen."""
    def construct(self):
        total = DUR["B04"]
        q1 = Text("A larger nanoparticle loads more drug", font=DISPLAY,
                  color=INK, font_size=26, weight=BOLD)
        q2 = Text("into the tumor than a smaller one.", font=DISPLAY,
                  color=INK, font_size=26, weight=BOLD)
        q3 = Text("The smaller one cures more.", font=DISPLAY,
                  color=CRIMSON, font_size=28, weight=BOLD)
        q4 = Text("How?", font=DISPLAY, color=TEAL, font_size=38, weight=BOLD)
        block = VGroup(q1, q2, q3).arrange(DOWN, buff=0.18)
        q4.next_to(block, DOWN, buff=0.42)
        full = VGroup(block, q4).move_to(ORIGIN)
        u = Line(q3.get_corner(DL) + DOWN * 0.12, q3.get_corner(DR) + DOWN * 0.12,
                 color=GOLD, stroke_width=2)
        self.play(FadeIn(block), Create(u), run_time=1.0)
        self.play(GrowFromCenter(q4), run_time=0.8)
        self.wait(max(0.3, total - 1.8))


class B05_LeakyVessel(Scene):
    """Leaky vessel: particles extravasate, impaired lymphatics can't drain them."""
    def construct(self):
        total = DUR["B05"]

        # vessel tube (left side)
        vessel = Rectangle(width=1.2, height=4.0)
        vessel.set_fill(SLATE, 0.15).set_stroke(SLATE, 2.5)
        vessel.move_to(LEFT * 5.0)

        vessel_lbl = LabelChip("tumor vessel", accent=SLATE, size=20)
        vessel_lbl.next_to(vessel, UP, buff=0.25)

        # gaps in vessel wall (three horizontal lines as "openings")
        gaps = VGroup()
        for y in [-0.8, 0.0, 0.8]:
            g = Line(LEFT * 4.4 + UP * y, LEFT * 3.8 + UP * y,
                     color=GROUND, stroke_width=5)
            gaps.add(g)

        # particles: crimson (150nm, large) and teal (30nm, small)
        p_large = VGroup(*[Dot(radius=0.18).set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
                           for _ in range(3)])
        p_large.arrange(DOWN, buff=0.4).move_to(LEFT * 2.6 + UP * 0.2)

        p_small = VGroup(*[Dot(radius=0.09).set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
                           for _ in range(5)])
        p_small.arrange_in_grid(rows=2, cols=3, buff=0.3).move_to(RIGHT * 0.3 + UP * 0.0)

        # label chips
        lbl_large = LabelChip("150 nm", accent=CRIMSON, size=20)
        lbl_large.next_to(p_large, UP, buff=0.2)
        lbl_small = LabelChip("30 nm", accent=TEAL, size=20)
        lbl_small.next_to(p_small, UP, buff=0.2)

        # crossed-out drain
        drain_box = Rectangle(width=1.6, height=0.7)
        drain_box.set_fill(SLATE, 0.08).set_stroke(SLATE, 1.5)
        drain_box.move_to(RIGHT * 4.6 + DOWN * 1.0)
        drain_txt = Text("lymphatic drain", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        drain_txt.move_to(drain_box.get_center())
        drain_strike = Line(drain_box.get_corner(DL), drain_box.get_corner(UR),
                            color=CRIMSON, stroke_width=3)
        drain_strike._qc_intentional = True

        # "stays" label
        stays = SerifLabel("stays in tumor", CRIMSON, size=24)
        stays.move_to(RIGHT * 4.2 + UP * 1.2)

        self.play(FadeIn(vessel), FadeIn(vessel_lbl), Create(gaps), run_time=0.8)
        self.play(
            FadeIn(p_large, shift=RIGHT * 0.5),
            FadeIn(lbl_large),
            run_time=0.7
        )
        self.play(
            FadeIn(p_small, shift=RIGHT * 0.5),
            FadeIn(lbl_small),
            run_time=0.7
        )
        self.play(FadeIn(drain_box), FadeIn(drain_txt), Create(drain_strike), run_time=0.6)
        self.play(FadeIn(stays, shift=LEFT * 0.2), run_time=0.5)
        self.wait(max(0.3, total - 3.3))


class B06_TotalMassBars(Scene):
    """Total accumulation bars: 150nm 6.2% (crimson) vs 30nm 2.1% (teal)."""
    def construct(self):
        total = DUR["B06"]
        max_w = 8.5

        # 150nm bar
        w_large = max_w * (6.2 / 8.0)
        bar_large = _bar(w_large, 0.60, CRIMSON)
        bar_large.move_to(UP * 0.8 + LEFT * (max_w / 2 - w_large / 2) + LEFT * 0.3)

        # 30nm bar
        w_small = max_w * (2.1 / 8.0)
        bar_small = _bar(w_small, 0.60, TEAL)
        bar_small.move_to(DOWN * 0.4 + LEFT * (max_w / 2 - w_small / 2) + LEFT * 0.3)

        # row labels (left edge)
        lbl_large = Text("150 nm", font=DISPLAY, color=CRIMSON, font_size=24, weight=BOLD)
        lbl_large.next_to(bar_large, LEFT, buff=0.25)
        lbl_small = Text("30 nm", font=DISPLAY, color=TEAL, font_size=24, weight=BOLD)
        lbl_small.next_to(bar_small, LEFT, buff=0.25)

        # value labels (right of bars)
        val_large = Text("6.2% ID/g", font=MONO, color=CRIMSON, font_size=24)
        val_large.next_to(bar_large, RIGHT, buff=0.25)
        val_small = Text("2.1% ID/g", font=MONO, color=TEAL, font_size=24)
        val_small.next_to(bar_small, RIGHT, buff=0.25)

        # annotation
        annotation = SerifLabel("bigger wins on total mass", CRIMSON, size=22)
        annotation.move_to(DOWN * 1.8)

        eyebrow = Text("illustrative", font=MONO, color=SLATE, font_size=18)
        eyebrow.to_edge(UP, buff=0.45)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(
            GrowFromEdge(bar_large, LEFT),
            FadeIn(lbl_large),
            run_time=0.8
        )
        self.play(FadeIn(val_large), run_time=0.4)
        self.play(
            GrowFromEdge(bar_small, LEFT),
            FadeIn(lbl_small),
            run_time=0.8
        )
        self.play(FadeIn(val_small), run_time=0.4)
        self.play(FadeIn(annotation, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.4))


class B08_OutwardPressure(Scene):
    """Outward pressure traps large particles at the rim; small particles move farther."""
    def construct(self):
        total = DUR["B08"]

        # spatial axis: vessel (left) to core (right)
        ax = Line(LEFT * 6.0 + DOWN * 2.8, RIGHT * 6.0 + DOWN * 2.8,
                  color=SLATE, stroke_width=1.5)
        ax_lbl_l = Text("vessel", font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        ax_lbl_r = Text("core", font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        ax_lbl_l.next_to(ax.get_left(), UP, buff=0.18)
        ax_lbl_r.next_to(ax.get_right(), UP, buff=0.18)

        # large particles (crimson) crowded near left
        large_particles = VGroup()
        for i in range(6):
            d = Dot(radius=0.22)
            d.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
            x = -5.2 + (i % 3) * 0.65
            y = 0.5 - (i // 3) * 0.65
            d.move_to(RIGHT * x + UP * y)
            large_particles.add(d)

        lbl_large = LabelChip("150 nm", accent=CRIMSON, size=20)
        lbl_large.next_to(large_particles, UP, buff=0.25)

        # outward pressure arrows (pointing left = toward rim/vessel)
        arrows = VGroup()
        for y in [1.4, 0.8, 0.2, -0.4]:
            a = Arrow(RIGHT * 1.5 + UP * y, LEFT * 0.3 + UP * y,
                      color=CRIMSON, stroke_width=2.5, max_tip_length_to_length_ratio=0.2,
                      buff=0)
            arrows.add(a)

        pressure_lbl = SerifLabel("outward pressure", CRIMSON, size=24)
        pressure_lbl.move_to(RIGHT * 0.8 + UP * 2.0)

        # zone label: rim region
        rim_zone = Rectangle(width=3.6, height=5.0)
        rim_zone.set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 1.2)
        rim_zone.move_to(LEFT * 4.3 + DOWN * 0.1)

        rim_lbl = Text("rim zone", font=DISPLAY, color=CRIMSON, font_size=20)
        rim_lbl.move_to(LEFT * 4.3 + UP * 2.7)

        # core zone (empty / dark)
        core_zone = Rectangle(width=4.5, height=5.0)
        core_zone.set_fill(SLATE, 0.06).set_stroke(SLATE, 1.2)
        core_zone.move_to(RIGHT * 3.2 + DOWN * 0.1)

        core_lbl = Text("core — no particles", font=DISPLAY, color=SLATE, font_size=20)
        core_lbl.move_to(RIGHT * 3.2 + UP * 2.7)

        self.play(FadeIn(ax), FadeIn(ax_lbl_l), FadeIn(ax_lbl_r), run_time=0.6)
        self.play(FadeIn(rim_zone), FadeIn(core_zone), run_time=0.5)
        self.play(FadeIn(rim_lbl), FadeIn(core_lbl), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(p, scale=0.8) for p in large_particles], lag_ratio=0.08),
            FadeIn(lbl_large),
            run_time=0.9
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1),
            run_time=0.7
        )
        self.play(FadeIn(pressure_lbl, shift=DOWN * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 3.6))


class B09_PenetrationCompare(Scene):
    """Split compare: 30nm (teal) spreads evenly; 150nm (crimson) crowds rim."""
    def construct(self):
        total = DUR["B09"]

        # dividing line
        divider = Line(UP * 3.6, DOWN * 3.6, color=SLATE, stroke_width=1.2)
        divider.move_to(ORIGIN)

        # shared axis labels
        ax_vessel_l = Text("vessel", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        ax_core_l = Text("core", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        ax_vessel_l.move_to(LEFT * 5.8 + DOWN * 3.0)
        ax_core_l.move_to(LEFT * 0.6 + DOWN * 3.0)

        ax_vessel_r = Text("vessel", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        ax_core_r = Text("core", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        ax_vessel_r.move_to(RIGHT * 0.6 + DOWN * 3.0)
        ax_core_r.move_to(RIGHT * 5.8 + DOWN * 3.0)

        # panel headers
        hdr_left = Text("30 nm", font=DISPLAY, color=TEAL, font_size=28, weight=BOLD)
        hdr_right = Text("150 nm", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        hdr_left.move_to(LEFT * 3.5 + UP * 3.0)
        hdr_right.move_to(RIGHT * 3.5 + UP * 3.0)

        # left panel: 30nm — dots spread across full width
        left_particles = VGroup()
        positions_l = [
            (-5.5, 1.2), (-4.8, 0.4), (-4.1, 1.6), (-3.4, 0.8),
            (-2.7, 1.4), (-2.0, 0.2), (-1.5, 1.0), (-5.2, -0.6),
            (-4.5, -1.2), (-3.8, -0.2), (-3.1, -0.8), (-2.4, -1.4),
            (-1.8, -0.4), (-1.4, 1.8), (-5.7, 2.0),
        ]
        for (x, y) in positions_l:
            d = Dot(radius=0.10)
            d.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
            d.move_to(RIGHT * x + UP * y)
            left_particles.add(d)

        even_lbl = SerifLabel("80% distributed evenly", TEAL, size=20)
        even_lbl.move_to(LEFT * 3.5 + DOWN * 2.0)

        # right panel: 150nm — larger dots crowded at vessel side (right edge = vessel)
        right_particles = VGroup()
        positions_r = [
            (0.8, 1.2), (1.4, 0.4), (0.9, -0.4), (1.5, 1.8),
            (1.1, -1.0), (1.6, 0.9), (0.7, 1.5), (1.2, -1.5),
            (1.8, 0.2), (0.6, 2.0),
        ]
        for (x, y) in positions_r:
            d = Dot(radius=0.20)
            d.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
            d.move_to(RIGHT * x + UP * y)
            right_particles.add(d)

        rim_lbl = SerifLabel("rim-crowded", CRIMSON, size=20)
        rim_lbl.move_to(RIGHT * 3.5 + DOWN * 2.0)

        core_absent = Text("core: none", font=MONO, color=SLATE, font_size=20)
        core_absent.move_to(RIGHT * 4.8 + UP * 0.3)

        self.play(
            FadeIn(divider), FadeIn(hdr_left), FadeIn(hdr_right),
            FadeIn(ax_vessel_l), FadeIn(ax_core_l),
            FadeIn(ax_vessel_r), FadeIn(ax_core_r),
            run_time=0.7
        )
        self.play(
            LaggedStart(*[FadeIn(p, scale=0.7) for p in left_particles], lag_ratio=0.04),
            run_time=1.1
        )
        self.play(FadeIn(even_lbl), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(p, scale=0.7) for p in right_particles], lag_ratio=0.06),
            run_time=0.9
        )
        self.play(FadeIn(rim_lbl), FadeIn(core_absent), run_time=0.5)
        self.wait(max(0.3, total - 3.7))


class B10_HypoxicCore(Scene):
    """DOCUMENT beat — quote about hypoxic core cells."""
    def construct(self):
        _quote_scene(
            self,
            "The cells in the unreached, hypoxic core are exactly the cells the drug never reached.",
            "— cancer-nanomedicine chapter 2",
            None,
            "exactly",
            DUR["B10"]
        )


class B11_DistributionVerdict(Scene):
    """Verdict: distribution (teal) beats total mass (crimson)."""
    def construct(self):
        total = DUR["B11"]

        # left panel: TOTAL MASS — high bar, rim-only label
        lp_bg = Rectangle(width=3.6, height=5.0)
        lp_bg.set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 1.5)
        lp_bg.move_to(LEFT * 3.2)

        lp_hdr = Text("TOTAL MASS", font=DISPLAY, color=CRIMSON, font_size=22, weight=BOLD)
        lp_hdr.move_to(LEFT * 3.2 + UP * 2.5)

        bar_big = _bar(1.4, 2.8, CRIMSON, 0.8)
        bar_big.move_to(LEFT * 3.2 + UP * 0.2)

        bar_val = Text("6.2%", font=MONO, color=CRIMSON, font_size=28)
        bar_val.next_to(bar_big, UP, buff=0.15)

        rim_only = SerifLabel("rim only", CRIMSON, size=22)
        rim_only.move_to(LEFT * 3.2 + DOWN * 2.0)

        strike = Line(rim_only.get_left() + LEFT * 0.08, rim_only.get_right() + RIGHT * 0.08,
                      color=CRIMSON, stroke_width=3)
        strike._qc_intentional = True

        # right panel: DISTRIBUTION — lower bar but dot grid
        rp_bg = Rectangle(width=3.6, height=5.0)
        rp_bg.set_fill(TEAL, 0.06).set_stroke(TEAL, 1.5)
        rp_bg.move_to(RIGHT * 3.2)

        rp_hdr = Text("DISTRIBUTION", font=DISPLAY, color=TEAL, font_size=22, weight=BOLD)
        rp_hdr.move_to(RIGHT * 3.2 + UP * 2.5)

        bar_small = _bar(1.4, 1.1, TEAL, 0.8)
        bar_small.move_to(RIGHT * 3.2 + UP * 0.15 + DOWN * 0.85)

        bar_val2 = Text("2.1%", font=MONO, color=TEAL, font_size=28)
        bar_val2.next_to(bar_small, UP, buff=0.15)

        # small dot grid spread across right panel (showing even distribution)
        dots = VGroup()
        for row in range(3):
            for col in range(4):
                d = Dot(radius=0.10)
                d.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
                d.move_to(RIGHT * (1.6 + col * 0.55) + UP * (-0.3 - row * 0.5))
                dots.add(d)

        deep_lbl = SerifLabel("reaches the core", TEAL, size=22)
        deep_lbl.move_to(RIGHT * 3.2 + DOWN * 2.0)

        # verdict
        verdict = Text("Distribution beats total mass.", font=DISPLAY,
                       color=INK, font_size=26, weight=BOLD)
        verdict.to_edge(DOWN, buff=0.35)

        self.play(FadeIn(lp_bg), FadeIn(rp_bg), run_time=0.5)
        self.play(FadeIn(lp_hdr), FadeIn(rp_hdr), run_time=0.4)
        self.play(
            GrowFromEdge(bar_big, DOWN), FadeIn(bar_val),
            run_time=0.7
        )
        self.play(FadeIn(rim_only), Create(strike), run_time=0.6)
        self.play(
            GrowFromEdge(bar_small, DOWN), FadeIn(bar_val2),
            run_time=0.7
        )
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.8) for d in dots], lag_ratio=0.05),
            FadeIn(deep_lbl),
            run_time=0.9
        )
        self.play(FadeIn(verdict, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 4.4))


class B12_Example(Scene):
    """Two-column illustrative example: 150nm vs 30nm. All numbers illustrative."""
    def construct(self):
        total = DUR["B12"]

        # header
        hdr = Text("illustrative example", font=MONO, color=SLATE, font_size=20)
        hdr.to_edge(UP, buff=0.4)

        # column headers
        col_left = Text("150 nm", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        col_right = Text("30 nm", font=DISPLAY, color=TEAL, font_size=30, weight=BOLD)
        col_left.move_to(LEFT * 3.2 + UP * 2.2)
        col_right.move_to(RIGHT * 3.2 + UP * 2.2)

        # divider
        div = Line(UP * 3.4, DOWN * 3.4, color=SLATE, stroke_width=1.2).move_to(ORIGIN)
        hdiv1 = Line(LEFT * 6.5 + UP * 1.5, RIGHT * 6.5 + UP * 1.5,
                     color=SLATE, stroke_width=0.8)
        hdiv2 = Line(LEFT * 6.5 + DOWN * 0.3, RIGHT * 6.5 + DOWN * 0.3,
                     color=SLATE, stroke_width=0.8)
        hdiv3 = Line(LEFT * 6.5 + DOWN * 2.1, RIGHT * 6.5 + DOWN * 2.1,
                     color=SLATE, stroke_width=0.8)

        # row labels (far left)
        row1_lbl = Text("accumulation", font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        row2_lbl = Text("distribution", font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        row3_lbl = Text("tumor shrink", font=SERIF, color=SLATE, font_size=20, slant=ITALIC)

        # We will show row labels centered in a narrow left column if possible;
        # Instead place them in left half as sub-labels.

        # row 1: accumulation
        acc_left = Text("6.2% ID/g", font=MONO, color=CRIMSON, font_size=26)
        acc_right = Text("2.1% ID/g", font=MONO, color=TEAL, font_size=26)
        acc_left.move_to(LEFT * 3.2 + UP * 0.9)
        acc_right.move_to(RIGHT * 3.2 + UP * 0.9)
        row1_lbl.move_to(UP * 0.9).set_opacity(0.5)

        # row 2: distribution
        dist_left = Text("rim only", font=MONO, color=CRIMSON, font_size=26)
        dist_right = Text("80% even", font=MONO, color=TEAL, font_size=26)
        dist_left.move_to(LEFT * 3.2 + DOWN * 0.9)
        dist_right.move_to(RIGHT * 3.2 + DOWN * 0.9)
        row2_lbl.move_to(DOWN * 0.9).set_opacity(0.5)

        # row 3: outcome
        out_left = Text("15% shrink", font=MONO, color=CRIMSON, font_size=26)
        out_right = Text("72% shrink", font=MONO, color=TEAL, font_size=26)
        out_left.move_to(LEFT * 3.2 + DOWN * 2.7)
        out_right.move_to(RIGHT * 3.2 + DOWN * 2.7)
        row3_lbl.move_to(DOWN * 2.7).set_opacity(0.5)

        # day 21 note
        day_note = Text("day 21", font=MONO, color=SLATE, font_size=18)
        day_note.next_to(out_left, DOWN, buff=0.2)

        self.play(FadeIn(hdr), FadeIn(div), FadeIn(hdiv1), FadeIn(hdiv2), FadeIn(hdiv3),
                  run_time=0.6)
        self.play(FadeIn(col_left), FadeIn(col_right), run_time=0.5)

        # row 1
        self.play(FadeIn(row1_lbl), run_time=0.3)
        self.play(FadeIn(acc_left, shift=RIGHT * 0.2), FadeIn(acc_right, shift=LEFT * 0.2),
                  run_time=0.7)

        # row 2
        self.play(FadeIn(row2_lbl), run_time=0.3)
        self.play(FadeIn(dist_left, shift=RIGHT * 0.2), FadeIn(dist_right, shift=LEFT * 0.2),
                  run_time=0.7)

        # row 3
        self.play(FadeIn(row3_lbl), run_time=0.3)
        self.play(FadeIn(out_left, shift=RIGHT * 0.2), FadeIn(out_right, shift=LEFT * 0.2),
                  run_time=0.7)
        self.play(FadeIn(day_note), run_time=0.4)
        self.wait(max(0.3, total - 4.5))


class B13_End(Scene):
    """Endcard — question restated, answer given."""
    def construct(self):
        total = DUR["B13"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Distribution beats total mass.", font=DISPLAY,
                  color=INK, font_size=34, weight=BOLD)
        t2 = Text("Smaller particles penetrate deeper", font=DISPLAY,
                  color=SLATE, font_size=24)
        t3 = Text("and kill more — even when bigger ones accumulate more.", font=DISPLAY,
                  color=SLATE, font_size=24)
        sub = VGroup(t2, t3).arrange(DOWN, buff=0.14)
        block = VGroup(t1, sub).arrange(DOWN, buff=0.38).move_to(UP * 0.1)
        u = Line(t1.get_corner(DL) + DOWN * 0.13, t1.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.3, total - 2.1))
