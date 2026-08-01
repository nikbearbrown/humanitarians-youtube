"""scenes.py — Exoplanet Hunting: Teaching AI to Show Its Work
(exoplanet-hunting, 16:9)

Rebuilt 2026-08-01: a new presenter self-introduction beat was inserted as B02
(right after the B01 cold open), pushing every former B02-B19 beat up by one.
Old beat_ids -> new: B01 unchanged; old B02-B19 -> new B03-B20. This file's
Scene classes/DUR-key lookups were renumbered to match; the visual CONTENT of
every scene is unchanged from the first-pass 19-beat cut.

One Scene per GRAPHIC beat with source='own': B01, B04, B05, B06, B07, B10,
B11, B12, B13, B14, B15 (old numbering: B01, B03, B04, B05, B06, B09, B10,
B11, B12, B13, B14). B02 (NEW intro card), B03, B08, B09, B16, B17, B18, B19,
B20 are Remotion CARD beats (SlateCard pattern, rendered by
runtime/scripts/remotion_scenes.py, not here) — old numbering: B02, B07, B08,
B15, B16, B17, B18, B19. See beat_sheet.json.

Color law: TEAL = signal / real planet / kept.
           CRIMSON = noise / impostor / flagged.
           GOLD = editor's-pen highlight only, never text.

Mirrors the helper-function style of claude-for-astronomy/ai-vs-the-data-deluge
/scenes.py (Ep.01) for visual consistency across the series.
"""
import json, os, sys, pathlib
# Toolkit location: this reel now lives at a standalone project path (moved out
# of brutalist-art/reels/<slug>/, where parents[2] used to land on the repo
# root). Resolve robustly: ART_HOME env override > the old nested-reel guess
# (kept for back-compat if this file is ever copied back under reels/) > the
# known absolute toolkit path on this machine.
_candidates = []
if os.environ.get("ART_HOME"):
    _candidates.append(pathlib.Path(os.environ["ART_HOME"]) / "runtime" / "manim")
_candidates.append(pathlib.Path(__file__).resolve().parents[2] / "runtime" / "manim")
_candidates.append(pathlib.Path(r"E:\NEU\Jobs\Humanitarians_AI\brutalist-art\runtime\manim"))
_VOX_MANIM = next((p for p in _candidates if (p / "animated_graphics.py").exists()), _candidates[-1])
sys.path.insert(0, str(_VOX_MANIM))
from animated_graphics import *  # noqa: F401,F403
import numpy as np

_bs = os.path.join(os.path.dirname(os.path.abspath(__file__)), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 8.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 8.0 for i in range(1, 21)}


def _light_curve(n=200, dip_center=0.5, dip_width=0.06, dip_depth=0.35, noise=0.02, seed=0):
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 1, n)
    y = np.ones(n)
    dip = dip_depth * np.exp(-0.5 * ((x - dip_center) / (dip_width / 2.355)) ** 2)
    y -= dip
    y += rng.normal(0, noise, n)
    return x, y


def _curve_mobject(x, y, color, width=6.0, height=2.4, stroke_w=2.5):
    pts = [np.array([(xi - 0.5) * width, (yi - 1.0) * height * 4, 0]) for xi, yi in zip(x, y)]
    curve = VMobject()
    curve.set_points_smoothly(pts)
    curve.set_stroke(color=color, width=stroke_w, opacity=1)
    return curve


def _axes_frame(width=6.4, height=2.8, color=INK):
    box = Rectangle(width=width, height=height).set_stroke(color=color, width=1.5, opacity=0.6)
    return box


class B01_Backlog(Scene):
    """Cold open: a dense grid of small light-curve tiles, ALL the same muted
    slate color — a visual "backlog" with nothing resolved yet. Deliberately
    the inverse of Ep.01's B01 (which highlighted one signal); this beat's
    point is that these are still unproven, not that one was quietly found."""
    def construct(self):
        total = DUR["B01"]
        field = VGroup()
        rng = np.random.default_rng(7)
        cols, rows = 10, 6
        for i in range(cols * rows):
            cx, cy = i % cols, i // cols
            x, y = _light_curve(n=50, dip_center=0.5, dip_width=0.18,
                                 dip_depth=0.05 + 0.02 * rng.random(),
                                 noise=0.012, seed=int(700 + i))
            c = _curve_mobject(x, y, SLATE, width=1.05, height=0.4, stroke_w=1.0)
            c.move_to(np.array([(cx - (cols - 1) / 2) * 1.15,
                                 (rows / 2 - cy) * 0.95, 0]))
            field.add(c)
        field.set_opacity(0.4)
        label = Text("thousands of unconfirmed signals", font=SERIF, color=INK, font_size=20)
        label.to_edge(DOWN, buff=0.6)

        self.play(LaggedStart(*[FadeIn(c) for c in field], lag_ratio=0.01),
                   run_time=max(1.8, total * 0.6))
        self.play(FadeIn(label), run_time=0.6)
        self.wait(max(0.3, total - (max(1.8, total * 0.6) + 0.6)))


class B03_ThreeImpostors(Scene):
    """One light curve with a dip, three branch-lines fanning out toward three
    (as-yet unlabeled) icon placeholders — sets up beats 4-6, which each fill
    in one impostor."""
    def construct(self):
        total = DUR["B04"]
        title = Text("THREE IMPOSTORS", font=DISPLAY, color=INK, font_size=22, weight=BOLD)
        title.to_edge(UP, buff=0.7)
        frame = _axes_frame(width=5.2, height=2.0).shift(UP * 1.4)
        x, y = _light_curve(n=250, dip_center=0.5, dip_width=0.09, dip_depth=0.28, noise=0.01, seed=41)
        curve = _curve_mobject(x, y, CRIMSON, width=4.6, height=1.6, stroke_w=2.4).move_to(frame.get_center())
        dip_point = Dot(radius=0.12, color=CRIMSON).move_to(frame.get_center() + DOWN * 0.35)

        slots = VGroup()
        for i, dx in enumerate([-3.2, 0.0, 3.2]):
            box = RoundedRectangle(corner_radius=0.12, width=2.2, height=1.1,
                                    color=SLATE, stroke_width=1.5, fill_opacity=0.0)
            box.move_to(np.array([dx, -1.8, 0]))
            slots.add(box)
        lines = VGroup(*[
            Line(dip_point.get_center(), s.get_top(), color=SLATE, stroke_width=1.5, stroke_opacity=0.6)
            for s in slots
        ])

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(frame), Create(curve), run_time=max(1.4, total * 0.32))
        self.play(FadeIn(dip_point), run_time=0.4)
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.2),
                   LaggedStart(*[Create(b) for b in slots], lag_ratio=0.2),
                   run_time=max(1.4, total * 0.32))
        self.wait(max(0.3, total - (0.9 + 2 * max(1.4, total * 0.32))))


class B04_EclipsingBinary(Scene):
    """Two-star icon eclipsing; the resulting curve shows the matching primary
    dip PLUS a faint secondary dip elsewhere in the orbit — the eclipsing-
    binary signature named in FACTCHECK."""
    def construct(self):
        total = DUR["B05"]
        title = Text("IMPOSTOR 1 — ECLIPSING BINARY", font=DISPLAY, color=CRIMSON, font_size=20, weight=BOLD)
        title.to_edge(UP, buff=0.6)
        star_a = Dot(radius=0.22, color=INK).move_to(LEFT * 1.0 + UP * 1.6)
        star_b = Dot(radius=0.14, color=SLATE).move_to(RIGHT * 1.0 + UP * 1.6)
        orbit = DashedVMobject(Circle(radius=1.0, color=SLATE, stroke_width=1.2).move_to(UP * 1.6), num_dashes=24)

        bx = np.linspace(0, 1, 300)
        by = np.ones(300)
        by -= 0.26 * np.exp(-0.5 * ((bx - 0.5) / (0.09 / 2.355)) ** 2)
        by -= 0.10 * np.exp(-0.5 * ((bx - 0.82) / (0.06 / 2.355)) ** 2)
        by += np.random.default_rng(42).normal(0, 0.010, 300)
        curve = _curve_mobject(bx, by, CRIMSON, width=5.6, height=1.6, stroke_w=2.4).move_to(DOWN * 1.4)
        secondary_ring = HandRing(around=curve, color=CRIMSON)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(star_a), FadeIn(star_b), Create(orbit), run_time=max(1.2, total * 0.28))
        self.play(Create(curve), run_time=max(1.6, total * 0.35), rate_func=linear)
        if secondary_ring is not None:
            self.play(Create(secondary_ring), run_time=0.6)
        self.wait(max(0.3, total - (0.5 + max(1.2, total * 0.28) + max(1.6, total * 0.35) + 0.6)))


class B05_StellarVariability(Scene):
    """Single star, irregular jittery brightness curve driven by starspots/
    flares — no clean periodic dip, unlike the eclipsing-binary or planet
    cases."""
    def construct(self):
        total = DUR["B06"]
        title = Text("IMPOSTOR 2 — STELLAR VARIABILITY", font=DISPLAY, color=CRIMSON, font_size=20, weight=BOLD)
        title.to_edge(UP, buff=0.6)
        star = Dot(radius=0.24, color=INK).move_to(UP * 1.7)
        flare = Text("starspots + flares", font=SERIF, color=SLATE, font_size=18)
        flare.next_to(star, DOWN, buff=0.25)

        rng = np.random.default_rng(51)
        x = np.linspace(0, 1, 300)
        y = 1.0 + 0.10 * np.sin(2 * np.pi * 3.3 * x) + 0.06 * np.sin(2 * np.pi * 7.1 * x + 1.1)
        y += rng.normal(0, 0.02, 300)
        curve = _curve_mobject(x, y, CRIMSON, width=5.6, height=1.6, stroke_w=2.2).move_to(DOWN * 1.4)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(star), FadeIn(flare), run_time=max(1.2, total * 0.28))
        self.play(Create(curve), run_time=max(1.8, total * 0.45), rate_func=linear)
        self.wait(max(0.3, total - (0.5 + max(1.2, total * 0.28) + max(1.8, total * 0.45))))


class B06_InstrumentalArtifact(Scene):
    """A sharp, jagged glitch-style dip rendered in a visibly different
    (angular) line style than the two real-astrophysical curves above —
    signals the dip isn't astrophysical at all."""
    def construct(self):
        total = DUR["B07"]
        title = Text("IMPOSTOR 3 — INSTRUMENTAL ARTIFACT", font=DISPLAY, color=CRIMSON, font_size=18, weight=BOLD)
        title.to_edge(UP, buff=0.6)
        frame = _axes_frame()
        xs = np.linspace(0, 1, 40)
        ys = np.ones(40)
        ys[16:20] -= np.array([0.05, 0.32, 0.30, 0.06])
        pts = [np.array([(xi - 0.5) * 6.0, (yi - 1.0) * 2.4 * 4, 0]) for xi, yi in zip(xs, ys)]
        jagged = VMobject()
        jagged.set_points_as_corners(pts)
        jagged.set_stroke(color=CRIMSON, width=2.6, opacity=1)
        camera_icon = Text("[ camera glitch ]", font=MONO, color=SLATE, font_size=18)
        camera_icon.next_to(frame, DOWN, buff=0.4)

        self.play(FadeIn(title), Create(frame), run_time=0.9)
        self.play(Create(jagged), run_time=max(1.4, total * 0.4), rate_func=linear)
        self.play(FadeIn(camera_icon), run_time=0.5)
        self.wait(max(0.3, total - (0.9 + max(1.4, total * 0.4) + 0.5)))


class B09_BranchIntro(Scene):
    """One curve splitting into several parallel branch-lines, each ending in
    an empty checkbox — sets up B10's labeling and B11-13's payoff."""
    def construct(self):
        total = DUR["B10"]
        title = Text("TWO OR MORE VIEWS ISN'T ENOUGH", font=DISPLAY, color=INK, font_size=20, weight=BOLD)
        title.to_edge(UP, buff=0.6)
        x, y = _light_curve(n=250, dip_center=0.5, dip_width=0.09, dip_depth=0.24, noise=0.01, seed=61)
        curve = _curve_mobject(x, y, TEAL, width=4.4, height=1.3, stroke_w=2.2).move_to(UP * 1.7)

        boxes = VGroup()
        lines = VGroup()
        for dx in (-2.6, 0.0, 2.6):
            b = Square(side_length=0.5, color=SLATE, stroke_width=1.6).move_to(np.array([dx, -1.6, 0]))
            l = Line(curve.get_bottom(), b.get_top(), color=SLATE, stroke_width=1.5, stroke_opacity=0.6)
            boxes.add(b)
            lines.add(l)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(curve), run_time=max(1.4, total * 0.32))
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.2),
                   LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.2),
                   run_time=max(1.6, total * 0.36))
        self.wait(max(0.3, total - (0.5 + max(1.4, total * 0.32) + max(1.6, total * 0.36))))


class B10_BranchLabeled(Scene):
    """The branch diagram from B09, now labeled with the three named tests,
    each branch shown as its own small convolutional block."""
    def construct(self):
        total = DUR["B11"]
        title = Text("THREE SEPARATE, EXPLAINABLE TESTS", font=DISPLAY, color=INK, font_size=18, weight=BOLD)
        title.to_edge(UP, buff=0.6)
        names = ["centroid", "odd / even", "secondary\neclipse"]
        chips = VGroup()
        for dx, name in zip((-3.0, 0.0, 3.0), names):
            chip = LabelChip(name.upper(), accent=TEAL, size=16)
            chip.move_to(np.array([dx, -1.0, 0]))
            chips.add(chip)
        root = Dot(radius=0.12, color=INK).move_to(UP * 1.6)
        lines = VGroup(*[Line(root.get_center(), c.get_top(), color=TEAL, stroke_width=1.8)
                         for c in chips])

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(root), run_time=0.4)
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.2),
                   run_time=max(1.2, total * 0.3))
        self.play(LaggedStart(*[FadeIn(c) for c in chips], lag_ratio=0.25),
                   run_time=max(1.4, total * 0.32))
        self.wait(max(0.3, total - (0.9 + max(1.2, total * 0.3) + max(1.4, total * 0.32))))


class B11_CentroidTest(Scene):
    """Target star + faint neighbor; centroid marker shifts toward the
    neighbor during the dip, flagged in CRIMSON — the centroid-offset test."""
    def construct(self):
        total = DUR["B12"]
        title = Text("TEST 1 — CENTROID OFFSET", font=DISPLAY, color=TEAL, font_size=20, weight=BOLD)
        title.to_edge(UP, buff=0.6)
        target = Dot(radius=0.22, color=INK).move_to(LEFT * 0.6)
        neighbor = Dot(radius=0.12, color=SLATE).move_to(RIGHT * 1.6)
        centroid = Dot(radius=0.08, color=TEAL).move_to(target.get_center())
        q = Text("light really from THIS star?", font=SERIF, color=INK, font_size=18)
        q.next_to(VGroup(target, neighbor), DOWN, buff=0.6)
        ring = HandRing(around=neighbor, color=CRIMSON)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(target), FadeIn(neighbor), FadeIn(centroid), run_time=max(1.2, total * 0.26))
        self.play(FadeIn(q), run_time=0.6)
        self.play(centroid.animate.move_to(target.get_center() + RIGHT * 0.9), run_time=max(1.2, total * 0.26))
        if ring is not None:
            self.play(Create(ring), run_time=0.6)
        self.wait(max(0.3, total - (0.5 + max(1.2, total * 0.26) + 0.6 + max(1.2, total * 0.26) + 0.6)))


class B12_OddEvenTest(Scene):
    """Two stacked mini-panels, "odd transits" vs "even transits" — matched
    (TEAL) depths for the planet case, mismatched (CRIMSON) for the binary
    case, side by side for comparison."""
    def construct(self):
        total = DUR["B13"]
        title = Text("TEST 2 — ODD / EVEN DEPTH", font=DISPLAY, color=TEAL, font_size=20, weight=BOLD)
        title.to_edge(UP, buff=0.6)

        ox, oy = _light_curve(n=150, dip_center=0.5, dip_width=0.14, dip_depth=0.24, noise=0.008, seed=71)
        ex, ey = _light_curve(n=150, dip_center=0.5, dip_width=0.14, dip_depth=0.24, noise=0.008, seed=72)
        odd_curve = _curve_mobject(ox, oy, TEAL, width=3.0, height=1.2, stroke_w=2.2).move_to(UP * 0.9 + LEFT * 2.6)
        even_curve = _curve_mobject(ex, ey, TEAL, width=3.0, height=1.2, stroke_w=2.2).move_to(UP * 0.9 + RIGHT * 2.6)
        match_tag = LabelChip("MATCHES", accent=TEAL, size=16).next_to(VGroup(odd_curve, even_curve), DOWN, buff=0.35)

        ox2, oy2 = _light_curve(n=150, dip_center=0.5, dip_width=0.14, dip_depth=0.24, noise=0.008, seed=73)
        ex2, ey2 = _light_curve(n=150, dip_center=0.5, dip_width=0.14, dip_depth=0.12, noise=0.008, seed=74)
        odd_curve2 = _curve_mobject(ox2, oy2, CRIMSON, width=3.0, height=1.2, stroke_w=2.2).move_to(DOWN * 1.6 + LEFT * 2.6)
        even_curve2 = _curve_mobject(ex2, ey2, CRIMSON, width=3.0, height=1.2, stroke_w=2.2).move_to(DOWN * 1.6 + RIGHT * 2.6)
        mismatch_tag = LabelChip("MISMATCHES", accent=CRIMSON, size=16).next_to(
            VGroup(odd_curve2, even_curve2), DOWN, buff=0.35)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(odd_curve), Create(even_curve), run_time=max(1.4, total * 0.3))
        self.play(FadeIn(match_tag), run_time=0.4)
        self.play(Create(odd_curve2), Create(even_curve2), run_time=max(1.4, total * 0.3))
        self.play(FadeIn(mismatch_tag), run_time=0.4)
        self.wait(max(0.3, total - (0.5 + 0.8 + 2 * max(1.4, total * 0.3))))


class B13_SecondaryEclipseTest(Scene):
    """Full-orbit phase-folded curve; primary dip + small secondary dip,
    secondary ringed in CRIMSON — the secondary-eclipse test."""
    def construct(self):
        total = DUR["B14"]
        title = Text("TEST 3 — SECONDARY ECLIPSE", font=DISPLAY, color=TEAL, font_size=20, weight=BOLD)
        title.to_edge(UP, buff=0.6)
        frame = _axes_frame()
        x = np.linspace(0, 1, 300)
        y = np.ones(300)
        y -= 0.24 * np.exp(-0.5 * ((x - 0.5) / (0.08 / 2.355)) ** 2)
        y -= 0.07 * np.exp(-0.5 * ((x - 0.85) / (0.05 / 2.355)) ** 2)
        y += np.random.default_rng(81).normal(0, 0.010, 300)
        curve = _curve_mobject(x, y, TEAL, width=6.0, height=2.2, stroke_w=2.4)
        secondary_dot = Dot(radius=0.1).move_to(np.array([1.3, -0.35, 0]))
        ring = HandRing(around=secondary_dot, color=CRIMSON)
        label = Text("hidden stellar companion?", font=SERIF, color=CRIMSON, font_size=18)
        label.next_to(frame, DOWN, buff=0.4)

        self.play(FadeIn(title), Create(frame), run_time=0.9)
        self.play(Create(curve), run_time=max(1.8, total * 0.44), rate_func=linear)
        if ring is not None:
            self.play(Create(ring), run_time=0.6)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(max(0.3, total - (0.9 + max(1.8, total * 0.44) + 0.6 + 0.5)))


class B14_Synthesis(Scene):
    """Three labeled branch chips each feed an arrow into one merge node,
    which outputs a single verdict chip — mirrors Ep.01's B11 synthesis shot
    but with three inputs instead of two."""
    def construct(self):
        total = DUR["B15"]
        title = Text("ONE EXPLAINABLE VERDICT", font=DISPLAY, color=INK, font_size=22, weight=BOLD)
        title.to_edge(UP, buff=0.7)
        chip_a = LabelChip("CENTROID", accent=TEAL, size=16).move_to(UP * 1.6 + LEFT * 2.8)
        chip_b = LabelChip("ODD/EVEN", accent=TEAL, size=16).move_to(LEFT * 2.8)
        chip_c = LabelChip("SEC. ECLIPSE", accent=TEAL, size=16).move_to(DOWN * 1.6 + LEFT * 2.8)
        merge_node = Dot(radius=0.28, color=INK).move_to(RIGHT * 0.4)
        arrows = VGroup(*[
            Arrow(c.get_right(), merge_node.get_left(), buff=0.15, color=TEAL, stroke_width=3)
            for c in (chip_a, chip_b, chip_c)
        ])
        merge_ring = HandRing(around=merge_node, color=CRIMSON)
        output = Text("planet, or not — and why.", font=DISPLAY, color=CRIMSON, font_size=26, weight=BOLD)
        output.next_to(merge_node, RIGHT, buff=0.9)
        out_arrow = Arrow(merge_node.get_right(), output.get_left(), buff=0.15, color=INK, stroke_width=3)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(chip_a), FadeIn(chip_b), FadeIn(chip_c), run_time=0.8)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15),
                   FadeIn(merge_node), run_time=1.0)
        if merge_ring is not None:
            self.play(Create(merge_ring), run_time=0.5)
        self.play(GrowArrow(out_arrow), FadeIn(output), run_time=0.9)
        # 0.5 + 0.8 + 1.0 + 0.5 + 0.9 = 3.7s of play() calls above (was hardcoded
        # as 4.7 in the original scenes.py, which shorted this beat by ~1.0s and
        # forced compile.py's ladder to slow the whole clip down ~17% to fit —
        # fixed here to the correct sum).
        self.wait(max(0.3, total - 3.7))
