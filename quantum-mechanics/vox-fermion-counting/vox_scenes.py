"""vox_scenes.py — Why three particles in two states give only one arrangement
(vox-fermion-counting, slate cut, 16:9).
Color law: TEAL=fermion/surviving; CRIMSON=classical/forbidden.
Exclusions: no Slater determinant formula.
"""
import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


def _dur(bid, fallback=8.0):
    return DUR.get(bid, fallback)


def _make_box(center, label, color=INK, box_size=0.9):
    """A labeled state box (square + label below)."""
    sq = Square(side_length=box_size, color=color, stroke_width=1.8)
    sq.move_to(center)
    lbl = Text(label, font=MONO, color=color, font_size=18)
    lbl.move_to(center + DOWN * (box_size / 2 + 0.25))
    return VGroup(sq, lbl)


def _particle_dot(center, color=TEAL, radius=0.2):
    d = Dot(center, radius=radius, color=color)
    d.set_stroke(INK, width=0.8)
    return d


# ── B01 CARD ──────────────────────────────────────────────────────────────────
class B01_TitleCard(Scene):
    def construct(self):
        d = _dur("B01", 9.0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE, font_size=22, weight="MEDIUM")
        eyebrow.move_to(UP * 1.8)
        title = Text("Why three particles in two states\ngive only one arrangement",
                     font=DISPLAY, color=INK, font_size=32, weight="BOLD", line_spacing=1.2)
        title.move_to(ORIGIN)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title), run_time=0.8)
        self.wait(d - 1.3)


# ── B02 CARD — THE QUESTION ───────────────────────────────────────────────────
class B02_TheQuestion(Scene):
    def construct(self):
        d = _dur("B02", 11.0)
        chip = LabelChip("THE QUESTION", accent=CRIMSON, size=24)
        chip.move_to(UP * 2.8)
        line1 = Text("Classical probability: 4 arrangements.", font=SERIF, color=CRIMSON, font_size=28)
        line1.move_to(UP * 0.7)
        line2 = Text("Quantum electrons: 1.", font=SERIF, color=TEAL, font_size=28)
        line2.move_to(DOWN * 0.2)
        line3 = Text("Why does the count collapse?", font=SERIF, color=INK, font_size=26, slant=ITALIC)
        line3.move_to(DOWN * 1.3)
        self.play(FadeIn(chip), run_time=0.4)
        self.play(FadeIn(line1), run_time=0.4)
        self.play(FadeIn(line2), run_time=0.4)
        self.play(FadeIn(line3), run_time=0.4)
        self.wait(d - 1.6)


# ── B03 GRAPHIC — Classical MB: 4 configurations ─────────────────────────────
class B03_ClassicalFour(Scene):
    def construct(self):
        d = _dur("B03", 13.0)
        header = Text("Maxwell-Boltzmann (distinguishable): 4 arrangements",
                      font=SERIF, color=CRIMSON, font_size=22)
        header.move_to(UP * 3.0)

        config_xs = [-5.0, -1.8, 1.4, 4.2]
        box_y = 0.3
        configs = [
            [(0, CRIMSON), (1, TEAL)],
            [(1, CRIMSON), (0, TEAL)],
            [(0, CRIMSON), (0, TEAL)],
            [(1, CRIMSON), (1, TEAL)],
        ]

        # Pre-build all box-pairs (shapes that will change progressively)
        box_pairs = []
        for ci, cx in enumerate(config_xs):
            bp = VGroup(
                _make_box(RIGHT * cx + LEFT * 0.5 + UP * box_y, "A", color=SLATE),
                _make_box(RIGHT * cx + RIGHT * 0.5 + UP * box_y, "B", color=SLATE),
            )
            box_pairs.append(bp)

        # Particle dots per config
        offsets = [UP * 0.12 + LEFT * 0.06, DOWN * 0.12 + RIGHT * 0.06]
        dots_per_config = []
        for ci, cx in enumerate(config_xs):
            grp = VGroup()
            for pi, (state_idx, pcol) in enumerate(configs[ci]):
                px = cx + (-0.5 if state_idx == 0 else 0.5)
                dot = _particle_dot(RIGHT * px + UP * box_y + offsets[pi], color=pcol, radius=0.18)
                grp.add(dot)
            dots_per_config.append(grp)

        # Progress bar: a colored Rectangle growing with each added config
        prog_bars = []
        for ci in range(1, 5):
            bar = Rectangle(width=ci * 2.0, height=0.18, color=CRIMSON, fill_opacity=0.6)
            bar.set_stroke(CRIMSON, width=0)
            bar.move_to(DOWN * 2.5 + LEFT * (4.0 - ci * 1.0))
            prog_bars.append(bar)

        count_label = Text("Total: 4 microstates", font=SERIF, color=CRIMSON, font_size=24)
        count_label.move_to(DOWN * 3.0)

        step = (d - 0.4) / 9
        self.play(FadeIn(header), run_time=0.4)
        self.play(FadeIn(box_pairs[0]), run_time=step)
        self.play(FadeIn(dots_per_config[0]), FadeIn(prog_bars[0]), run_time=step)
        self.play(FadeIn(box_pairs[1]), FadeIn(box_pairs[2]), run_time=step)
        self.play(FadeIn(dots_per_config[1]), FadeIn(prog_bars[1]), run_time=step)
        self.play(FadeIn(box_pairs[3]), run_time=step)
        self.play(FadeIn(dots_per_config[2]), FadeIn(prog_bars[2]), run_time=step)
        self.play(FadeIn(dots_per_config[3]), FadeIn(prog_bars[3]), run_time=step)
        self.play(FadeOut(prog_bars[3]), FadeIn(count_label), run_time=step * 2)


# ── B04 GRAPHIC — Bosons: 4→3 ──────────────────────────────────────────────
class B04_BosonThree(Scene):
    def construct(self):
        d = _dur("B04", 11.0)
        header_mb = Text("Maxwell-Boltzmann: 4  →", font=SERIF, color=CRIMSON, font_size=22)
        header_mb.move_to(UP * 3.0 + LEFT * 2.5)
        header_be = Text("Bose-Einstein: 3", font=SERIF, color=TEAL, font_size=22)
        header_be.move_to(UP * 3.0 + RIGHT * 2.5)

        config_xs = [-4.5, 0.0, 4.5]
        configs_be = [
            [(0,), (0,)],
            [(1,), (1,)],
            [(0,), (1,)],
        ]
        box_y = 0.3
        offsets_be = [UP * 0.12, DOWN * 0.12]

        box_pairs = []
        dot_groups = []
        for ci, cx in enumerate(config_xs):
            bp = VGroup(
                _make_box(RIGHT * cx + LEFT * 0.5 + UP * box_y, "A", color=SLATE),
                _make_box(RIGHT * cx + RIGHT * 0.5 + UP * box_y, "B", color=SLATE),
            )
            box_pairs.append(bp)
            dg = VGroup()
            for pi, (state_idx,) in enumerate(configs_be[ci]):
                px = cx + (-0.5 if state_idx == 0 else 0.5)
                dot = _particle_dot(RIGHT * px + UP * box_y + offsets_be[pi], color=TEAL, radius=0.18)
                dg.add(dot)
            dot_groups.append(dg)

        # Connector arrows showing collapse from MB to BE
        arrow1 = Arrow(LEFT * 2.0 + UP * 0.3, LEFT * 0.5 + UP * 0.3, buff=0.05,
                       color=CRIMSON, stroke_width=2)
        arrow1_label = Text("same!", font=MONO, color=CRIMSON, font_size=18)
        arrow1_label.move_to(LEFT * 1.2 + UP * 0.7)

        note = Text("Swapping identical bosons = no new microstate",
                    font=SERIF, color=TEAL, font_size=22)
        note.move_to(DOWN * 2.5)
        count_rect = Rectangle(width=3.0, height=0.5, color=TEAL, fill_opacity=0.15)
        count_rect.set_stroke(TEAL, width=1.5)
        count_rect.move_to(DOWN * 3.2)
        count_label = Text("Total: 3 microstates", font=SERIF, color=TEAL, font_size=24)
        count_label.move_to(DOWN * 3.2)

        step = (d - 0.5) / 7
        self.play(FadeIn(header_mb), FadeIn(header_be), run_time=0.5)
        self.play(FadeIn(box_pairs[0]), run_time=step)
        self.play(FadeIn(dot_groups[0]), run_time=step)
        self.play(FadeIn(box_pairs[1]), FadeIn(dot_groups[1]), run_time=step)
        self.play(FadeIn(arrow1), FadeIn(arrow1_label), run_time=step)
        self.play(FadeIn(box_pairs[2]), FadeIn(dot_groups[2]), run_time=step)
        self.play(FadeIn(note), run_time=step)
        self.play(FadeIn(count_rect), FadeIn(count_label), run_time=step)


# ── B05 GRAPHIC — Antisymmetry: swap rule ─────────────────────────────────────
class B05_Antisymmetry(Scene):
    def construct(self):
        d = _dur("B05", 12.0)

        title = Text("Fermion rule: antisymmetric wavefunction",
                     font=SERIF, color=INK, font_size=24)
        title.move_to(UP * 2.8)

        # Two boxes before swap
        box_a = _make_box(LEFT * 3.0 + UP * 1.0, "A", color=SLATE)
        box_b = _make_box(RIGHT * 3.0 + UP * 1.0, "B", color=SLATE)
        dot1 = _particle_dot(LEFT * 3.0 + UP * 1.0 + UP * 0.1, color=TEAL, radius=0.2)
        dot2 = _particle_dot(RIGHT * 3.0 + UP * 1.0 + DOWN * 0.1, color=TEAL, radius=0.2)

        # Swap arrow
        swap_arc = CurvedArrow(LEFT * 1.5 + UP * 1.3, RIGHT * 1.5 + UP * 1.3,
                               angle=-TAU / 6, color=SLATE, stroke_width=2)
        swap_lbl = Text("swap", font=MONO, color=SLATE, font_size=18)
        swap_lbl.move_to(UP * 1.9)

        # After-swap: minus sign indicator
        minus_circle = Circle(radius=0.4, color=CRIMSON, fill_opacity=0.2)
        minus_circle.set_stroke(CRIMSON, width=2)
        minus_circle.move_to(ORIGIN + UP * 0.2)
        minus_sign = Text("−", font=DISPLAY, color=CRIMSON, font_size=40, weight="BOLD")
        minus_sign.move_to(ORIGIN + UP * 0.2)

        # Same-state forbidden diagram
        same_box_a = _make_box(LEFT * 3.5 + DOWN * 1.2, "A", color=CRIMSON)
        same_box_b = _make_box(LEFT * 2.1 + DOWN * 1.2, "B", color=CRIMSON)
        dot_s1 = _particle_dot(LEFT * 3.5 + DOWN * 1.05, color=CRIMSON, radius=0.18)
        dot_s2 = _particle_dot(LEFT * 3.5 + DOWN * 1.35, color=CRIMSON, radius=0.18)
        cross_x = Line(LEFT * 4.3 + DOWN * 0.5, LEFT * 1.3 + DOWN * 1.9, color=CRIMSON, stroke_width=3)

        same_label = Text("both in A: amplitude = 0", font=SERIF, color=CRIMSON, font_size=22)
        same_label.move_to(RIGHT * 1.5 + DOWN * 1.2)

        step = (d - 0.3) / 7
        self.play(FadeIn(title), run_time=0.3)
        self.play(FadeIn(box_a), FadeIn(box_b), run_time=step)
        self.play(FadeIn(dot1), FadeIn(dot2), run_time=step)
        self.play(FadeIn(swap_arc), FadeIn(swap_lbl), run_time=step)
        self.play(FadeIn(minus_circle), FadeIn(minus_sign), run_time=step)
        self.play(FadeIn(same_box_a), FadeIn(same_box_b), FadeIn(dot_s1), FadeIn(dot_s2), run_time=step)
        self.play(FadeIn(cross_x), run_time=step)
        self.play(FadeIn(same_label), run_time=step)


# ── B06 GRAPHIC — Fermion: 3→2→1 (erase forbidden configs) ───────────────────
class B06_FermionOne(Scene):
    def construct(self):
        d = _dur("B06", 10.0)

        header = Text("Fermi-Dirac: erase double occupancy", font=SERIF, color=TEAL, font_size=22)
        header.move_to(UP * 3.0)

        config_xs = [-4.5, 0.0, 4.5]
        configs_be = [
            [(0,), (0,)],
            [(1,), (1,)],
            [(0,), (1,)],
        ]
        config_colors = [CRIMSON, CRIMSON, TEAL]
        box_y = 0.3
        offsets_be = [UP * 0.12, DOWN * 0.12]

        box_pairs = []
        dot_groups = []
        for ci, cx in enumerate(config_xs):
            col = config_colors[ci]
            bp = VGroup(
                _make_box(RIGHT * cx + LEFT * 0.5 + UP * box_y, "A", color=SLATE),
                _make_box(RIGHT * cx + RIGHT * 0.5 + UP * box_y, "B", color=SLATE),
            )
            box_pairs.append(bp)
            dg = VGroup()
            for pi, (state_idx,) in enumerate(configs_be[ci]):
                px = cx + (-0.5 if state_idx == 0 else 0.5)
                dot = _particle_dot(RIGHT * px + UP * box_y + offsets_be[pi], color=col, radius=0.18)
                dg.add(dot)
            dot_groups.append(dg)

        # Red X overlays for forbidden configs
        x_marks = []
        for ci in range(2):
            cx = config_xs[ci]
            ln1 = Line(RIGHT * (cx - 0.6) + UP * (box_y + 0.5),
                       RIGHT * (cx + 0.6) + UP * (box_y - 0.5), color=CRIMSON, stroke_width=4)
            ln2 = Line(RIGHT * (cx + 0.6) + UP * (box_y + 0.5),
                       RIGHT * (cx - 0.6) + UP * (box_y - 0.5), color=CRIMSON, stroke_width=4)
            x_marks.append(VGroup(ln1, ln2))

        # Highlight box for surviving config
        highlight = Rectangle(width=1.4, height=1.2, color=TEAL, fill_opacity=0.12)
        highlight.set_stroke(TEAL, width=2)
        highlight.move_to(RIGHT * config_xs[2] + UP * box_y)

        count_rect = Rectangle(width=3.5, height=0.55, color=TEAL, fill_opacity=0.15)
        count_rect.set_stroke(TEAL, width=2)
        count_rect.move_to(DOWN * 2.8)
        count_label = Text("Total: 1 microstate", font=SERIF, color=TEAL, font_size=26)
        count_label.move_to(DOWN * 2.8)

        step = (d - 0.3) / 7
        self.play(FadeIn(header), run_time=0.3)
        self.play(*[FadeIn(bp) for bp in box_pairs], run_time=step)
        self.play(*[FadeIn(dg) for dg in dot_groups], run_time=step)
        self.play(FadeIn(x_marks[0]), run_time=step)
        self.play(FadeIn(x_marks[1]), run_time=step)
        self.play(FadeOut(box_pairs[0]), FadeOut(dot_groups[0]), FadeOut(x_marks[0]),
                  FadeOut(box_pairs[1]), FadeOut(dot_groups[1]), FadeOut(x_marks[1]), run_time=step)
        self.play(FadeIn(highlight), run_time=step)
        self.play(FadeIn(count_rect), FadeIn(count_label), run_time=step)


# ── B07 GRAPHIC — Summary comparison table ────────────────────────────────────
class B07_ComparisonTable(Scene):
    def construct(self):
        d = _dur("B07", 11.0)

        title = Text("Three statistics, one setup: 2 particles, 2 states",
                     font=SERIF, color=INK, font_size=22)
        title.move_to(UP * 3.0)

        rows = [
            ("Maxwell-Boltzmann", "distinguishable", "4", CRIMSON),
            ("Bose-Einstein", "identical bosons", "3", SLATE),
            ("Fermi-Dirac", "identical fermions", "1", TEAL),
        ]
        ys = [1.2, 0.0, -1.2]

        # Row highlight bars (geometric shapes that change)
        row_bars = []
        for (stats, rule, count, col), y in zip(rows, ys):
            bar = Rectangle(width=12.0, height=0.9, color=col, fill_opacity=0.08)
            bar.set_stroke(col, width=0.8)
            bar.move_to(UP * y)
            row_bars.append(bar)

        row_groups = []
        for (stats, rule, count, col), y in zip(rows, ys):
            stats_t = Text(stats, font=SERIF, color=col, font_size=22)
            stats_t.move_to(LEFT * 3.5 + UP * y)
            rule_t = Text(rule, font=MONO, color=INK, font_size=20)
            rule_t.move_to(UP * y)
            count_t = Text(count, font=DISPLAY, color=col, font_size=28, weight="BOLD")
            count_t.move_to(RIGHT * 4.0 + UP * y)
            rg = VGroup(stats_t, rule_t, count_t)
            row_groups.append(rg)

        h1 = Text("Statistics", font=DISPLAY, color=SLATE, font_size=20, weight="MEDIUM")
        h1.move_to(LEFT * 3.5 + UP * 2.3)
        h2 = Text("Particle type", font=DISPLAY, color=SLATE, font_size=20, weight="MEDIUM")
        h2.move_to(UP * 2.3)
        h3 = Text("Count", font=DISPLAY, color=SLATE, font_size=20, weight="MEDIUM")
        h3.move_to(RIGHT * 4.0 + UP * 2.3)
        divider = Line(LEFT * 6.0, RIGHT * 6.0, color=SLATE, stroke_width=1.0)
        divider.move_to(UP * 1.8)

        pauli_note = Text("Pauli exclusion = amplitude is zero, not forbidden by decree",
                          font=SERIF, color=TEAL, font_size=21, slant=ITALIC)
        pauli_note.move_to(DOWN * 2.5)

        step = (d - 0.3) / 6
        self.play(FadeIn(title), FadeIn(h1), FadeIn(h2), FadeIn(h3), FadeIn(divider), run_time=0.3)
        underline = Line(LEFT * 5.5, RIGHT * 5.5, color=TEAL, stroke_width=2)
        underline.move_to(DOWN * 1.8)

        self.play(FadeIn(row_bars[0]), FadeIn(row_groups[0]), run_time=step)
        self.play(FadeIn(row_bars[1]), FadeIn(row_groups[1]), run_time=step)
        self.play(FadeIn(row_bars[2]), FadeIn(row_groups[2]), run_time=step)
        self.play(FadeOut(row_bars[0]), FadeOut(row_bars[1]), run_time=step)
        self.play(FadeIn(underline), run_time=step)
        self.play(FadeIn(pauli_note), run_time=step)


# ── B09 GRAPHIC — Illustrative: 3 particles, 2 states ─────────────────────────
class B09_ThreeParticles(Scene):
    def construct(self):
        d = _dur("B09", 14.0)

        title = Text("Illustrative: 3 particles, 2 spin states",
                     font=SERIF, color=INK, font_size=22, slant=ITALIC)
        title.move_to(UP * 3.2)

        rows = [
            ("MB (classical)", "8", CRIMSON, "2^3 = 8"),
            ("BE (bosons)", "4", SLATE, "(0,3)(1,2)(2,1)(3,0)"),
            ("FD (fermions)", "0", TEAL, "impossible!"),
        ]
        ys = [1.3, 0.0, -1.3]

        # Row bars (geometric) that reveal one by one
        row_bars = []
        for (stats, count, col, note), y in zip(rows, ys):
            bar = Rectangle(width=12.5, height=0.85, color=col, fill_opacity=0.09)
            bar.set_stroke(col, width=0.8)
            bar.move_to(UP * y)
            row_bars.append(bar)

        row_groups = []
        for (stats, count, col, note), y in zip(rows, ys):
            s = Text(stats, font=SERIF, color=col, font_size=22)
            s.move_to(LEFT * 3.5 + UP * y)
            c = Text(count, font=DISPLAY, color=col, font_size=30, weight="BOLD")
            c.move_to(RIGHT * 0.5 + UP * y)
            n = Text(note, font=MONO, color=col, font_size=18)
            n.move_to(RIGHT * 3.5 + UP * y)
            row_groups.append(VGroup(s, c, n))

        header_stats = Text("Statistics", font=DISPLAY, color=SLATE, font_size=19, weight="MEDIUM")
        header_stats.move_to(LEFT * 3.5 + UP * 2.5)
        header_count = Text("# configs", font=DISPLAY, color=SLATE, font_size=19, weight="MEDIUM")
        header_count.move_to(RIGHT * 0.5 + UP * 2.5)
        header_note = Text("Reason", font=DISPLAY, color=SLATE, font_size=19, weight="MEDIUM")
        header_note.move_to(RIGHT * 3.5 + UP * 2.5)
        divider = Line(LEFT * 6.0, RIGHT * 6.0, color=SLATE, stroke_width=1.0)
        divider.move_to(UP * 2.0)

        # Gold highlight box on the fermion row
        gold_box = Rectangle(width=12.5, height=0.85, color=GOLD, fill_opacity=0.18)
        gold_box.set_stroke(GOLD, width=2)
        gold_box.move_to(UP * (-1.3))

        punchline = Text("Three fermions cannot fit in two states.\nPauli exclusion is arithmetic.",
                         font=SERIF, color=TEAL, font_size=22, line_spacing=1.3)
        punchline.move_to(DOWN * 2.8)

        step = (d - 0.3) / 7
        teal_line = Line(LEFT * 5.8, RIGHT * 5.8, color=TEAL, stroke_width=2.5)
        teal_line.move_to(DOWN * (-1.3) + DOWN * 0.6)

        self.play(FadeIn(title), FadeIn(header_stats), FadeIn(header_count),
                  FadeIn(header_note), FadeIn(divider), run_time=0.3)
        self.play(FadeIn(row_bars[0]), FadeIn(row_groups[0]), run_time=step)
        self.play(FadeIn(row_bars[1]), FadeIn(row_groups[1]), run_time=step)
        self.play(FadeIn(row_bars[2]), FadeIn(row_groups[2]), run_time=step)
        self.play(FadeOut(row_bars[2]), FadeIn(gold_box), run_time=step)
        self.play(FadeOut(gold_box), FadeIn(row_bars[2]), FadeIn(teal_line), run_time=step)
        self.play(FadeIn(punchline), run_time=step * 2)


# ── B10 CARD — RECAP ──────────────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        d = _dur("B10", 10.0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE, font_size=22, weight="MEDIUM")
        eyebrow.move_to(UP * 2.5)
        answer = Text("Antisymmetric wavefunction\n= zero amplitude for double occupancy\n= Pauli exclusion = 1 microstate",
                      font=SERIF, color=INK, font_size=24, line_spacing=1.3)
        answer.move_to(ORIGIN)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(answer), run_time=0.8)
        self.wait(d - 1.3)
