"""scenes.py — AI vs. the Data Deluge (explainer--ai-vs-data-deluge, 16:9)

Rebuilt 2026-07-27 for the 18-beat second-pass cut (SCRIPT/SHOTLIST revised
2026-07-26). One Scene per GRAPHIC beat with source='own': B01, B03, B04, B08,
B09, B10, B11, B12. B09/B10/B11 are new/changed for this pass — the AstroNet
dual-view CNN architecture (global+local views, beat 9), the impostor-catching
payoff (beat 10), and the two-view synthesis (beat 11), replacing the old
Earth/Sun beat and the old generic "network learned..." beat.
B02, B05, B06, B07, B14, B16, B18 are Remotion CARD beats (SlateCard pattern,
rendered by runtime/scripts/remotion_scenes.py, not here).
B13, B15 are STILL·archive; B17 is FOOTAGE·archive.

Color law: TEAL = signal / confirmed transit / kept.
           CRIMSON = noise / false positive / discarded.
           GOLD = editor's-pen highlight only, never text.
"""
import json, os, sys, pathlib
_VOX_MANIM = pathlib.Path(__file__).resolve().parents[2] / "runtime" / "manim"
sys.path.insert(0, str(_VOX_MANIM))
from animated_graphics import *  # noqa: F401,F403
import numpy as np

_bs = os.path.join(os.path.dirname(os.path.abspath(__file__)), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 8.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 8.0 for i in range(1, 18)}


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


class B01_DataField(Scene):
    """Cold open: an abstract field of data points / light curves, most of them
    unremarkable, with ONE quietly highlighted — the beat's own visual metaphor
    for "a computer found what every human who'd looked had missed." Deliberately
    NO literal computer or planet imagery (shot changed from Higgsfield 2026-07-26,
    no spend occurred on the slate it replaces)."""
    def construct(self):
        total = DUR["B01"]
        field = VGroup()
        rng = np.random.default_rng(1)
        cols, rows = 10, 6
        for i in range(cols * rows):
            cx, cy = i % cols, i // cols
            x, y = _light_curve(n=50, dip_center=0.5, dip_width=0.18,
                                 dip_depth=0.05 + 0.02 * rng.random(),
                                 noise=0.012, seed=int(100 + i))
            c = _curve_mobject(x, y, SLATE, width=1.05, height=0.4, stroke_w=1.0)
            c.move_to(np.array([(cx - (cols - 1) / 2) * 1.15,
                                 (rows / 2 - cy) * 0.95, 0]))
            field.add(c)
        field.set_opacity(0.32)

        # the one quietly highlighted signal, near the visual center
        hi_idx = (rows // 2) * cols + cols // 2 + 1
        highlighted = field[hi_idx]

        self.play(LaggedStart(*[FadeIn(c) for c in field], lag_ratio=0.01),
                   run_time=max(1.6, total * 0.45))
        self.play(highlighted.animate.set_stroke(color=TEAL, width=2.6).set_opacity(1),
                   run_time=1.0)
        ring = HandRing(around=highlighted, color=TEAL)
        if ring is not None:
            self.play(Create(ring), run_time=0.8)
        self.wait(max(0.3, total - (max(1.6, total * 0.45) + 1.0 + 0.8)))


class B03_KeplerScale(Scene):
    """Stat overlay: 200,000 stars, 30-min cadence, 4 years -> millions of light curves."""
    def construct(self):
        total = DUR["B03"]
        eyebrow = Text("THE PROBLEM", font=DISPLAY, color=TEAL, font_size=20, weight=BOLD)
        eyebrow.to_edge(UP, buff=0.6)
        n_stars = Text("200,000", font=MONO, color=INK, font_size=64, weight=BOLD)
        lbl_stars = Text("stars watched at once", font=SERIF, color=INK, font_size=24)
        cadence = Text("every 30 min", font=MONO, color=TEAL, font_size=36)
        years = Text("for 4 years", font=MONO, color=TEAL, font_size=36)
        stat_group = VGroup(n_stars, lbl_stars).arrange(DOWN, buff=0.15)
        row = VGroup(cadence, years).arrange(RIGHT, buff=0.8)
        block = VGroup(stat_group, row).arrange(DOWN, buff=0.55).move_to(ORIGIN)
        result = Text("millions of light curves", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        result.next_to(block, DOWN, buff=0.6)

        # background: stacking light curves suggestion (thin grid of small curves)
        mini = VGroup()
        for i in range(24):
            x, y = _light_curve(n=60, dip_center=0.5, dip_width=0.15, dip_depth=0.08,
                                 noise=0.01, seed=i)
            c = _curve_mobject(x, y, SLATE, width=1.0, height=0.35, stroke_w=1.0)
            c.move_to(np.array([(i % 8 - 3.5) * 1.5, (i // 8 - 1) * 1.6 + 2.6, 0]))
            mini.add(c)
        mini.set_opacity(0.25)

        self.play(FadeIn(mini, lag_ratio=0.02), run_time=1.2)
        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(stat_group, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(row), run_time=0.8)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.8)
        self.wait(max(0.3, total - 4.1))


class B04_TransitSignature(Scene):
    """Animated transit dip on a single light curve — draw-on."""
    def construct(self):
        total = DUR["B04"]
        title = Text("THE TRANSIT SIGNATURE", font=DISPLAY, color=INK, font_size=22, weight=BOLD)
        title.to_edge(UP, buff=0.7)
        frame = _axes_frame()
        x, y = _light_curve(n=300, dip_center=0.5, dip_width=0.10, dip_depth=0.30, noise=0.012, seed=3)
        curve = _curve_mobject(x, y, TEAL, width=6.0, height=2.4)
        dip_label = Text("periodic dip", font=SERIF, color=CRIMSON, font_size=22)
        dip_target = Dot(radius=0.35).move_to(np.array([0.0, -0.7, 0]))
        ring = HandRing(around=dip_target, color=CRIMSON)
        dip_label.next_to(frame, DOWN, buff=0.35)

        self.play(FadeIn(title), Create(frame), run_time=1.0)
        self.play(Create(curve), run_time=max(1.5, total * 0.45), rate_func=linear)
        if ring is not None:
            self.play(Create(ring), run_time=0.7)
        self.play(FadeIn(dip_label), run_time=0.5)
        self.wait(max(0.3, total - (1.0 + max(1.5, total * 0.45) + 0.7 + 0.5)))


class B08_TrainingSet(Scene):
    """Training-set diagram: 15,000 labeled light curves -> 'planet' / 'not a planet'.
    (Was B09 in the old 17-beat numbering — content unchanged, beat renumbered.)"""
    def construct(self):
        total = DUR["B08"]
        title = Text("15,000 LABELED LIGHT CURVES", font=DISPLAY, color=INK, font_size=22, weight=BOLD)
        title.to_edge(UP, buff=0.7)
        n = 60
        grid = VGroup()
        for i in range(n):
            is_planet = (i % 5 == 0)
            d = Dot(radius=0.075)
            d.set_fill(TEAL if is_planet else SLATE, 1).set_stroke(width=0)
            d.move_to(np.array([(i % 15 - 7) * 0.42, (i // 15 - 1.5) * 0.42 + 0.2, 0]))
            grid.add(d)
        chip_planet = LabelChip("PLANET", accent=TEAL, size=18)
        chip_not = LabelChip("NOT A PLANET", accent=SLATE, size=18)
        chips = VGroup(chip_planet, chip_not).arrange(RIGHT, buff=0.6)
        chips.next_to(grid, DOWN, buff=0.6)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(d) for d in grid], lag_ratio=0.006), run_time=max(1.8, total * 0.5))
        self.play(FadeIn(chips), run_time=0.6)
        self.wait(max(0.3, total - (0.5 + max(1.8, total * 0.5) + 0.6)))


class B09_DualView(Scene):
    """NEW 2026-07-26 (second pass). Split-screen: the global view (full folded
    orbit, top) vs. the local view (zoomed transit, bottom) — sets up beat 10's
    payoff. Per FACTCHECK: global = 2,001 bins / 8 conv layers; local = 201
    bins / 4 conv layers (labeled here, not derived on screen — a tangent would
    over-teach the architecture for a 3-min explainer)."""
    def construct(self):
        total = DUR["B09"]
        title = Text("TWO VIEWS, NOT ONE", font=DISPLAY, color=INK, font_size=22, weight=BOLD)
        title.to_edge(UP, buff=0.6)
        divider = Line(UP * 2.6, DOWN * 2.6, color=INK, stroke_width=1.5, stroke_opacity=0.5)

        # global view: full folded orbit, wide + flat
        gx, gy = _light_curve(n=300, dip_center=0.5, dip_width=0.05, dip_depth=0.10, noise=0.012, seed=21)
        global_curve = _curve_mobject(gx, gy, SLATE, width=5.6, height=1.6, stroke_w=2.0)
        global_curve.move_to(UP * 1.6)
        global_label = Text("GLOBAL VIEW — full orbit, 2,001 bins", font=SERIF, color=INK, font_size=18)
        global_label.next_to(global_curve, UP, buff=0.25)

        # local view: zoomed dip, sharp and tall
        lx, ly = _light_curve(n=300, dip_center=0.5, dip_width=0.16, dip_depth=0.30, noise=0.008, seed=22)
        local_curve = _curve_mobject(lx, ly, TEAL, width=3.6, height=2.2, stroke_w=2.6)
        local_curve.move_to(DOWN * 1.7)
        local_label = Text("LOCAL VIEW — zoomed transit, 201 bins", font=SERIF, color=TEAL, font_size=18)
        local_label.next_to(local_curve, UP, buff=0.25)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(divider), run_time=0.4)
        self.play(FadeIn(global_label), Create(global_curve), run_time=max(1.6, total * 0.35))
        self.play(FadeIn(local_label), Create(local_curve), run_time=max(1.6, total * 0.35))
        self.wait(max(0.3, total - (0.9 + 2 * max(1.6, total * 0.35))))


class B10_ImpostorCheck(Scene):
    """NEW 2026-07-26 (second pass). Two side-by-side examples: a real transit
    (clean single dip, both views agree) vs. an eclipsing binary (a second,
    fainter dip visible only in the global/wide view — the false-positive
    signature named in FACTCHECK)."""
    def construct(self):
        total = DUR["B10"]
        title = Text("REAL TRANSIT VS. IMPOSTOR", font=DISPLAY, color=INK, font_size=20, weight=BOLD)
        title.to_edge(UP, buff=0.6)
        divider = Line(UP * 2.4, DOWN * 2.4, color=INK, stroke_width=1.5, stroke_opacity=0.5)

        # left: real transit — one clean dip, global view flat elsewhere
        rx, ry = _light_curve(n=300, dip_center=0.5, dip_width=0.09, dip_depth=0.26, noise=0.010, seed=31)
        real_curve = _curve_mobject(rx, ry, TEAL, width=3.2, height=2.0, stroke_w=2.4)
        real_curve.move_to(LEFT * 3.3)
        real_label = Text("real transit", font=SERIF, color=TEAL, font_size=20)
        real_label.next_to(real_curve, DOWN, buff=0.35)
        real_tag = LabelChip("PLANET", accent=TEAL, size=16)
        real_tag.next_to(real_label, DOWN, buff=0.2)

        # right: eclipsing binary — primary dip PLUS a secondary dip elsewhere in the orbit
        bx = np.linspace(0, 1, 300)
        by = np.ones(300)
        by -= 0.26 * np.exp(-0.5 * ((bx - 0.5) / (0.09 / 2.355)) ** 2)
        by -= 0.10 * np.exp(-0.5 * ((bx - 0.82) / (0.06 / 2.355)) ** 2)  # secondary eclipse
        by += np.random.default_rng(32).normal(0, 0.010, 300)
        binary_curve = _curve_mobject(bx, by, CRIMSON, width=3.2, height=2.0, stroke_w=2.4)
        binary_curve.move_to(RIGHT * 3.3)
        binary_label = Text("eclipsing binary", font=SERIF, color=CRIMSON, font_size=20)
        binary_label.next_to(binary_curve, DOWN, buff=0.35)
        binary_tag = LabelChip("NOT A PLANET", accent=CRIMSON, size=16)
        binary_tag.next_to(binary_label, DOWN, buff=0.2)
        secondary_ring = HandRing(around=binary_curve, color=CRIMSON)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(divider), run_time=0.4)
        self.play(Create(real_curve), FadeIn(real_label), run_time=max(1.4, total * 0.3))
        self.play(FadeIn(real_tag), run_time=0.4)
        self.play(Create(binary_curve), FadeIn(binary_label), run_time=max(1.4, total * 0.3))
        self.play(FadeIn(binary_tag), run_time=0.4)
        self.wait(max(0.3, total - (1.7 + 2 * max(1.4, total * 0.3))))


class B11_Synthesis(Scene):
    """CHANGED 2026-07-26 (second pass) — replaces the old, more generic
    'network learned what a transit looks like' framing (old B10). The two
    views (global + local) merge at a single fully-connected layer into one
    probability: planet, or not."""
    def construct(self):
        total = DUR["B11"]
        title = Text("ONE FINAL ANSWER", font=DISPLAY, color=INK, font_size=22, weight=BOLD)
        title.to_edge(UP, buff=0.7)
        global_chip = LabelChip("GLOBAL VIEW", accent=SLATE, size=18).move_to(UP * 0.9 + LEFT * 2.6)
        local_chip = LabelChip("LOCAL VIEW", accent=TEAL, size=18).move_to(DOWN * 0.9 + LEFT * 2.6)
        merge_node = Dot(radius=0.28, color=INK).move_to(RIGHT * 0.6)
        merge_ring = HandRing(around=merge_node, color=CRIMSON)
        arrow1 = Arrow(global_chip.get_right(), merge_node.get_left(), buff=0.15,
                       color=SLATE, stroke_width=3)
        arrow2 = Arrow(local_chip.get_right(), merge_node.get_left(), buff=0.15,
                       color=TEAL, stroke_width=3)
        output = Text("planet, or not.", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        output.next_to(merge_node, RIGHT, buff=0.9)
        out_arrow = Arrow(merge_node.get_right(), output.get_left(), buff=0.15,
                          color=INK, stroke_width=3)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(global_chip), FadeIn(local_chip), run_time=0.7)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2), FadeIn(merge_node), run_time=0.9)
        if merge_ring is not None:
            self.play(Create(merge_ring), run_time=0.5)
        self.play(GrowArrow(out_arrow), FadeIn(output), run_time=0.8)
        self.wait(max(0.3, total - 3.4))


class B12_FlagKepler90i(Scene):
    """Light curve highlight/zoom on the flagged dip — 1-in-10,000 false-alarm odds.
    (Was B11 in the old 17-beat numbering — content unchanged, beat renumbered.)"""
    def construct(self):
        total = DUR["B12"]
        title = Text("KEPLER-90i FLAGGED", font=DISPLAY, color=TEAL, font_size=24, weight=BOLD)
        title.to_edge(UP, buff=0.7)
        frame = _axes_frame()
        x, y = _light_curve(n=300, dip_center=0.5, dip_width=0.08, dip_depth=0.28, noise=0.010, seed=11)
        curve = _curve_mobject(x, y, TEAL, width=6.0, height=2.4)
        flag_target = Dot(radius=0.4).move_to(np.array([0.0, -0.55, 0]))
        ring = HandRing(around=flag_target, color=CRIMSON)
        odds = Text("1-in-10,000 false-alarm odds", font=MONO, color=CRIMSON, font_size=26, weight=BOLD)
        odds.next_to(frame, DOWN, buff=0.4)

        self.play(FadeIn(title), Create(frame), run_time=0.8)
        self.play(Create(curve), run_time=max(1.5, total * 0.4), rate_func=linear)
        if ring is not None:
            self.play(Create(ring), run_time=0.6)
        self.play(FadeIn(odds), run_time=0.5)
        self.wait(max(0.3, total - (0.8 + max(1.5, total * 0.4) + 0.6 + 0.5)))
