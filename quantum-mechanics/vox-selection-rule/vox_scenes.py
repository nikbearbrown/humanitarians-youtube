"""vox_scenes.py — Why Some Light an Atom Should Emit Is Forbidden
(vox-selection-rule, slate cut, 16:9)

Color law: TEAL = allowed transitions (Δℓ=±1)
           CRIMSON = forbidden transitions (Δℓ=0)
EXCLUSIONS: no Gaunt-integral/parity proof, no dipole-matrix-element
            computation, no golden-rule derivation.
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


# ── B01: COLD OPEN — 2p fast, 2s slow ────────────────────────────────────────
class B01_LifetimeContrast(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        title = Text("Same atom, same energy. Different rules.", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        # Side-by-side comparison
        p_grp = VGroup(
            LabelChip("2p state", accent=TEAL, size=24),
            Text("ℓ = 1 (pear-shaped)", font=SERIF, font_size=22, color=TEAL, slant=ITALIC),
            Text("decays in ~1 ns", font=MONO, font_size=24, color=TEAL),
        )
        p_grp.arrange(DOWN, buff=0.3).move_to(LEFT * 3.2 + DOWN * 0.3)
        s_grp = VGroup(
            LabelChip("2s state", accent=CRIMSON, size=24),
            Text("ℓ = 0 (spherical)", font=SERIF, font_size=22, color=CRIMSON, slant=ITALIC),
            Text("stuck for ~0.1 s", font=MONO, font_size=24, color=CRIMSON),
        )
        s_grp.arrange(DOWN, buff=0.3).move_to(RIGHT * 3.2 + DOWN * 0.3)
        divider = Line(UP * 2.0, DOWN * 2.3, color=INK, stroke_width=1.5)
        ratio_lbl = LabelChip("ratio: 100 million times", accent=INK, size=22)
        ratio_lbl.move_to(DOWN * 2.8)
        self.play(FadeIn(title), Create(divider), run_time=0.4)
        self.play(FadeIn(p_grp), run_time=dur * 0.35)
        self.play(FadeIn(s_grp), run_time=dur * 0.35)
        self.play(FadeIn(ratio_lbl), run_time=dur * 0.20)
        self.wait(dur * 0.10)


# ── B02: COLD OPEN — orbital shape and angular momentum ──────────────────────
class B02_OrbitalShape(Scene):
    def construct(self):
        dur = DUR.get("B02", 9.0)
        title = Text("The shape encodes the angular momentum", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        # 2s: circle (s orbital)
        s_circle = Circle(radius=1.0, color=CRIMSON, stroke_width=3)
        s_circle.move_to(LEFT * 3.5 + DOWN * 0.3)
        s_lbl = Text("2s: ℓ = 0", font=MONO, font_size=22, color=CRIMSON)
        s_lbl.next_to(s_circle, DOWN, buff=0.3)
        s_note = SerifLabel("no angular momentum", CRIMSON, size=20)
        s_note.next_to(s_circle, DOWN, buff=1.0)
        # 2p: elongated (p orbital)
        p_ell = Ellipse(width=1.0, height=2.2, color=TEAL, stroke_width=3)
        p_ell.move_to(RIGHT * 3.5 + DOWN * 0.3)
        p_lbl = Text("2p: ℓ = 1", font=MONO, font_size=22, color=TEAL)
        p_lbl.next_to(p_ell, DOWN, buff=0.3)
        p_note = SerifLabel("one unit of angular momentum", TEAL, size=20)
        p_note.next_to(p_ell, DOWN, buff=1.0)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(s_circle), FadeIn(s_lbl), run_time=dur * 0.30)
        self.play(FadeIn(s_note), run_time=dur * 0.15)
        self.play(Create(p_ell), FadeIn(p_lbl), run_time=dur * 0.30)
        self.play(FadeIn(p_note), run_time=dur * 0.25)


# ── B03: THE QUESTION — CARD beat, no scene class ────────────────────────────


# ── B04: THE PROBLEM — STILL·ai beat, no scene class ─────────────────────────


# ── B05: THE PROBLEM — photon carries one unit of angular momentum ────────────
class B05_PhotonSpin(Scene):
    def construct(self):
        dur = DUR.get("B05", 9.0)
        title = Text("A photon carries spin 1", font=DISPLAY,
                     font_size=28, color=INK).move_to(UP * 3.0)
        photon_chip = LabelChip("photon: spin = 1 unit", accent=TEAL, size=24)
        photon_chip.move_to(UP * 1.4)
        conservation = SerifLabel("angular momentum is conserved in any decay", INK, size=22)
        conservation.move_to(UP * 0.2)
        rule_chip = LabelChip("atom loses 1 unit → photon carries 1 unit", accent=TEAL, size=22)
        rule_chip.move_to(DOWN * 1.0)
        therefore = SerifLabel("atom's ℓ must change by exactly 1", INK, size=20)
        therefore.move_to(DOWN * 2.2)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(photon_chip), run_time=dur * 0.25)
        self.play(FadeIn(conservation), run_time=dur * 0.25)
        self.play(FadeIn(rule_chip), run_time=dur * 0.25)
        self.play(FadeIn(therefore), run_time=dur * 0.25)


# ── B06: THE PROBLEM — Δℓ = ±1 selection rule ────────────────────────────────
class B06_SelectionRule(Scene):
    def construct(self):
        dur = DUR.get("B06", 9.0)
        title = Text("The electric-dipole selection rule", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        rule = Text("Δℓ = ±1", font=MONO, font_size=48, color=TEAL).move_to(UP * 1.2)
        allowed = Text("Δℓ = +1 or −1  →  allowed (fast)", font=MONO,
                       font_size=24, color=TEAL).move_to(DOWN * 0.3)
        forbidden = Text("Δℓ = 0          →  forbidden (very slow)", font=MONO,
                         font_size=24, color=CRIMSON).move_to(DOWN * 1.3)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(rule), run_time=dur * 0.30)
        self.play(FadeIn(allowed), run_time=dur * 0.30)
        self.play(FadeIn(forbidden), run_time=dur * 0.30)
        self.wait(dur * 0.10)


# ── B07: THE MECHANISM — 2p→1s: Δℓ=−1, allowed ──────────────────────────────
class B07_AllowedTransition(Scene):
    def construct(self):
        dur = DUR.get("B07", 10.0)
        title = Text("2p → 1s: Δℓ = −1  (allowed)", font=DISPLAY,
                     font_size=26, color=TEAL).move_to(UP * 3.0)
        # Two energy levels with an arrow
        level_2p = Line(LEFT * 3.0 + UP * 1.0, RIGHT * 1.0 + UP * 1.0,
                        color=TEAL, stroke_width=3)
        lbl_2p = Text("2p   (ℓ=1)", font=MONO, font_size=22, color=TEAL)
        lbl_2p.move_to(RIGHT * 2.2 + UP * 1.0)
        level_1s = Line(LEFT * 3.0 + DOWN * 1.5, RIGHT * 1.0 + DOWN * 1.5,
                        color=TEAL, stroke_width=3)
        lbl_1s = Text("1s   (ℓ=0)", font=MONO, font_size=22, color=TEAL)
        lbl_1s.move_to(RIGHT * 2.2 + DOWN * 1.5)
        arrow = Arrow(LEFT * 0.5 + UP * 0.9, LEFT * 0.5 + DOWN * 1.4,
                      color=TEAL, stroke_width=3, buff=0.0)
        delta_lbl = Text("Δℓ = −1", font=MONO, font_size=22, color=TEAL)
        delta_lbl.move_to(LEFT * 1.8 + DOWN * 0.3)
        photon_lbl = LabelChip("photon emitted!", accent=TEAL, size=22)
        photon_lbl.move_to(DOWN * 3.0)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(level_2p), FadeIn(lbl_2p), run_time=dur * 0.20)
        self.play(Create(level_1s), FadeIn(lbl_1s), run_time=dur * 0.20)
        self.play(GrowArrow(arrow), FadeIn(delta_lbl), run_time=dur * 0.30)
        self.play(FadeIn(photon_lbl), run_time=dur * 0.30)


# ── B08: THE MECHANISM — 2s→1s: Δℓ=0, forbidden ─────────────────────────────
class B08_ForbiddenTransition(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)
        title = Text("2s → 1s: Δℓ = 0  (E1 forbidden)", font=DISPLAY,
                     font_size=24, color=CRIMSON).move_to(UP * 3.0)
        level_2s = Line(LEFT * 3.0 + UP * 1.0, RIGHT * 1.0 + UP * 1.0,
                        color=CRIMSON, stroke_width=3)
        lbl_2s = Text("2s   (ℓ=0)", font=MONO, font_size=22, color=CRIMSON)
        lbl_2s.move_to(RIGHT * 2.2 + UP * 1.0)
        level_1s = Line(LEFT * 3.0 + DOWN * 1.5, RIGHT * 1.0 + DOWN * 1.5,
                        color=CRIMSON, stroke_width=3)
        lbl_1s = Text("1s   (ℓ=0)", font=MONO, font_size=22, color=CRIMSON)
        lbl_1s.move_to(RIGHT * 2.2 + DOWN * 1.5)
        # Crossed-out arrow
        cross_body = Line(LEFT * 0.5 + UP * 0.9, LEFT * 0.5 + DOWN * 1.4,
                          color=CRIMSON, stroke_width=2, stroke_opacity=0.5)
        cross1 = Line(LEFT * 1.0 + UP * 0.2, ORIGIN + DOWN * 0.5,
                      color=CRIMSON, stroke_width=3)
        cross2 = Line(ORIGIN + DOWN * 0.5, LEFT * 1.0 + DOWN * 1.2,
                      color=CRIMSON, stroke_width=3)
        delta_lbl = Text("Δℓ = 0", font=MONO, font_size=22, color=CRIMSON)
        delta_lbl.move_to(LEFT * 1.8 + DOWN * 0.3)
        no_go = LabelChip("where does the spin go?", accent=CRIMSON, size=22)
        no_go.move_to(DOWN * 3.0)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(level_2s), FadeIn(lbl_2s), run_time=dur * 0.20)
        self.play(Create(level_1s), FadeIn(lbl_1s), run_time=dur * 0.20)
        self.play(Create(cross_body), FadeIn(delta_lbl), run_time=dur * 0.25)
        self.play(Create(cross1), Create(cross2), run_time=dur * 0.15)
        self.play(FadeIn(no_go), run_time=dur * 0.20)


# ── B09: THE MECHANISM — parity argument ─────────────────────────────────────
class B09_ParityArgument(Scene):
    def construct(self):
        dur = DUR.get("B09", 10.0)
        title = Text("Why: the parity argument", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        # Parity table
        rows = [
            ("s (ℓ=0)", "even parity: (+1)^0 = +1", INK),
            ("p (ℓ=1)", "odd parity:  (+1)^1 = −1", INK),
            ("dipole r̂", "odd parity  (flips sign)", INK),
        ]
        row_group = VGroup()
        for i, (item, parity, col) in enumerate(rows):
            y = 1.4 - i * 1.2
            r = VGroup(
                LabelChip(item, accent=col, size=20).move_to(LEFT * 3.5 + UP * y),
                SerifLabel(parity, col, size=20).move_to(RIGHT * 1.5 + UP * y),
            )
            row_group.add(r)
        integral = SerifLabel("∫ (s) × (dipole) × (p) = even×odd×odd = even → nonzero ✓", TEAL, size=18)
        integral.move_to(DOWN * 1.6)
        integral2 = SerifLabel("∫ (s) × (dipole) × (s) = even×odd×even = odd → zero ✗", CRIMSON, size=18)
        integral2.move_to(DOWN * 2.5)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(row_group), run_time=dur * 0.40)
        self.play(FadeIn(integral), run_time=dur * 0.25)
        self.play(FadeIn(integral2), run_time=dur * 0.25)
        self.wait(dur * 0.10)


# ── B10: THE MECHANISM — section CARD, no scene class ────────────────────────


# ── B11: THE IMPLICATION — hydrogen spectral series ──────────────────────────
class B11_SpectralSeries(Scene):
    def construct(self):
        dur = DUR.get("B11", 10.0)
        title = Text("The selection rule patterns the spectrum", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        # Lyman, Balmer, Paschen
        series = [
            ("Lyman series",  "n→1s, Δℓ = −1 each", TEAL),
            ("Balmer series", "n→2s or 2p, Δℓ = ±1", TEAL),
            ("Paschen series","n→3s, 3p, 3d, Δℓ = ±1", TEAL),
        ]
        grp = VGroup()
        for i, (name, rule, col) in enumerate(series):
            y = 1.2 - i * 1.4
            r = VGroup(
                LabelChip(name, accent=col, size=22).move_to(LEFT * 3.0 + UP * y),
                SerifLabel(rule, col, size=20).move_to(RIGHT * 2.0 + UP * y),
            )
            grp.add(r)
        note = Text("Every line satisfies Δℓ = ±1. Forbidden transitions have no line.",
                    font=SERIF, font_size=20, color=INK, slant=ITALIC).move_to(DOWN * 2.5)
        self.play(FadeIn(title), run_time=0.4)
        for r in grp:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=dur * 0.22)
        self.play(FadeIn(note), run_time=dur * 0.20)
        self.wait(dur * 0.10)


# ── B12: THE IMPLICATION — 21 cm line ─────────────────────────────────────────
class B12_TwentyCm(Scene):
    def construct(self):
        dur = DUR.get("B12", 10.0)
        title = Text("Even forbidden transitions happen — just slowly", font=DISPLAY,
                     font_size=22, color=INK).move_to(UP * 3.0)
        rows = [
            ("21 cm line", "H hyperfine, magnetic dipole", "Δℓ=0, E1 forbidden", "~10⁷ years", CRIMSON),
        ]
        lbl1 = LabelChip("21 cm hydrogen line", accent=CRIMSON, size=22)
        lbl1.move_to(UP * 1.4)
        lbl2 = SerifLabel("magnetic-dipole transition, Δℓ = 0", CRIMSON, size=20)
        lbl2.move_to(UP * 0.4)
        lbl3 = Text("lifetime: ~10 million years", font=MONO, font_size=24, color=CRIMSON)
        lbl3.move_to(DOWN * 0.7)
        lbl4 = SerifLabel("visible across the entire observable universe", TEAL, size=20)
        lbl4.move_to(DOWN * 1.8)
        note = Text("Forbidden means slow — not impossible.", font=SERIF,
                    font_size=20, color=INK, slant=ITALIC).move_to(DOWN * 3.0)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(lbl1), run_time=dur * 0.20)
        self.play(FadeIn(lbl2), run_time=dur * 0.20)
        self.play(FadeIn(lbl3), run_time=dur * 0.20)
        self.play(FadeIn(lbl4), run_time=dur * 0.20)
        self.play(FadeIn(note), run_time=dur * 0.20)


# ── B13: THE EXAMPLE — illustrative numbers ───────────────────────────────────
class B13_IllustrativeExample(Scene):
    def construct(self):
        dur = DUR.get("B13", 16.0)
        title = Text("Illustrative: hydrogen transition lifetimes", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.1)
        subtitle = Text("(from textbook, labeled illustrative)", font=SERIF,
                        font_size=20, color=INK, slant=ITALIC).move_to(UP * 2.5)
        rows = [
            ("2p → 1s", "Δℓ = −1, allowed", "~1.6 ns", TEAL),
            ("2s → 1s", "Δℓ = 0, E1 forbidden", "~0.12 s", CRIMSON),
            ("21 cm",   "Δℓ = 0, mag. dip.",    "~10⁷ yr", CRIMSON),
        ]
        row_groups = VGroup()
        for i, (transition, note, lifetime, col) in enumerate(rows):
            y = 1.0 - i * 1.5
            r = VGroup(
                Text(transition, font=MONO, font_size=22, color=col).move_to(LEFT * 4.5 + UP * y),
                SerifLabel(note, col, size=18).move_to(LEFT * 0.5 + UP * y),
                Text(lifetime, font=MONO, font_size=22, color=col).move_to(RIGHT * 4.0 + UP * y),
            )
            row_groups.add(r)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        for rg in row_groups:
            self.play(FadeIn(rg, shift=RIGHT * 0.3), run_time=dur * 0.25)
        self.wait(dur * 0.10)


# ── B14: RECAP — CARD beat, no scene class ───────────────────────────────────
