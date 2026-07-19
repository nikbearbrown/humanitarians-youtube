"""vox_scenes.py — cancer-immunoediting
B04 only: animated three-phase immunoediting timeline.
Palette: teardown — INK=#2A1A0E CREAM=#FFFFFF CRIMSON=#C8102E SLATE=#545454 GOLD=#F6D8DC
NEVER use: Axes, ParametricFunction, weight=NORMAL
ALWAYS: Manual Line for axes; CREAM Rectangle backgrounds behind text near Lines.
"""
import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_ImmunoeditingTimeline(Scene):
    """Animated three-phase cancer immunoediting timeline."""

    def construct(self):
        dur = DUR.get("B04", 20.0)

        # ── Title ──────────────────────────────────────────────────────────────
        title = Text("CANCER IMMUNOEDITING", font_size=30, color=INK, weight=BOLD)
        title.move_to(UP * 3.2)

        # ── Baseline time arrow ────────────────────────────────────────────────
        baseline = Line(start=[-6.0, -0.2, 0], end=[6.0, -0.2, 0],
                        color=INK, stroke_width=2)

        # ── Phase rectangles above baseline ───────────────────────────────────
        # ELIMINATION: left edge at x=-6.0, width=3.8, top at y=1.6, height=1.8
        elim_rect = Rectangle(width=3.8, height=1.8)
        elim_rect.set_fill(GOLD, opacity=0.4).set_stroke(width=0)
        elim_rect.move_to([-6.0 + 3.8/2, 1.6 - 1.8/2, 0])  # center

        # EQUILIBRIUM: left edge at x=-2.2, width=4.0
        equil_rect = Rectangle(width=4.0, height=1.8)
        equil_rect.set_fill(SLATE, opacity=0.2).set_stroke(width=0)
        equil_rect.move_to([-2.2 + 4.0/2, 1.6 - 1.8/2, 0])

        # ESCAPE: left edge at x=1.8, width=4.2
        escape_rect = Rectangle(width=4.2, height=1.8)
        escape_rect.set_fill(CRIMSON, opacity=0.25).set_stroke(width=0)
        escape_rect.move_to([1.8 + 4.2/2, 1.6 - 1.8/2, 0])

        # ── Phase labels with CREAM backgrounds ───────────────────────────────
        def phase_label(cx, label, col):
            bg = Rectangle(width=len(label) * 0.12 + 0.4, height=0.4)
            bg.set_fill(CREAM, opacity=1).set_stroke(width=0, opacity=0)
            bg.move_to([cx, 1.9, 0])
            txt = Text(label, font_size=16, color=col, weight=BOLD)
            txt.move_to(bg.get_center())
            return VGroup(bg, txt)

        label_elim  = phase_label(-4.1, "ELIMINATION", INK)
        label_equil = phase_label(-0.2, "EQUILIBRIUM", INK)
        label_escape= phase_label( 3.9, "ESCAPE", CRIMSON)

        # ── Molecular event text inside each phase ────────────────────────────
        def phase_events(cx, lines, col):
            bg = Rectangle(width=2.6, height=0.9)
            bg.set_fill(CREAM, opacity=1).set_stroke(width=0, opacity=0)
            bg.move_to([cx, 0.5, 0])
            txt = Text(lines, font_size=12, color=col)
            txt.move_to(bg.get_center())
            return VGroup(bg, txt)

        events_elim  = phase_events(-4.1, "CD8+ T cells\nNK cells\nIFN-γ", INK)
        events_equil = phase_events(-0.2, "Dormancy\nImmune balance\nLongest phase", INK)
        events_escape= phase_events( 3.9, "MHC-I ↓\nPD-L1 ↑\nAntigen loss", CRIMSON)

        # ── CLINICAL CANCER arrow + label ─────────────────────────────────────
        clinical_line = Line(start=[5.8, -0.2, 0], end=[5.8, -1.5, 0],
                             color=CRIMSON, stroke_width=2)
        clin_bg = Rectangle(width=1.6, height=0.6)
        clin_bg.set_fill(CREAM, opacity=1).set_stroke(width=0, opacity=0)
        clin_bg.move_to([5.8, -1.9, 0])
        clin_txt = Text("CLINICAL\nCANCER", font_size=14, color=CRIMSON)
        clin_txt.move_to(clin_bg.get_center())
        clinical_label = VGroup(clin_bg, clin_txt)

        # ── Citation label ─────────────────────────────────────────────────────
        cite_bg = Rectangle(width=3.5, height=0.35)
        cite_bg.set_fill(CREAM, opacity=1).set_stroke(width=0, opacity=0)
        cite_bg.move_to([-4.5, -2.5, 0])
        cite_txt = Text("Schreiber lab 2001 (Science)", font_size=11, color=SLATE)
        cite_txt.move_to(cite_bg.get_center())
        citation = VGroup(cite_bg, cite_txt)

        # ── Bottom crimson rule ────────────────────────────────────────────────
        bottom_rule = Line(start=[-6.0, -3.2, 0], end=[5.5, -3.2, 0],
                           color=CRIMSON, stroke_width=2)

        # ── Animation sequence (7 states) ─────────────────────────────────────
        t_unit = dur / 7.0

        # State 1: title + baseline arrow
        self.play(FadeIn(title), Create(baseline), run_time=t_unit * 0.8)
        self.wait(t_unit * 0.2)

        # State 2: ELIMINATION phase + label + events
        self.play(
            FadeIn(elim_rect), FadeIn(label_elim), FadeIn(events_elim),
            run_time=t_unit * 0.8
        )
        self.wait(t_unit * 0.2)

        # State 3: EQUILIBRIUM phase + label + events
        self.play(
            FadeIn(equil_rect), FadeIn(label_equil), FadeIn(events_equil),
            run_time=t_unit * 0.8
        )
        self.wait(t_unit * 0.2)

        # State 4: ESCAPE phase + label + events
        self.play(
            FadeIn(escape_rect), FadeIn(label_escape), FadeIn(events_escape),
            run_time=t_unit * 0.8
        )
        self.wait(t_unit * 0.2)

        # State 5: CLINICAL CANCER arrow + label
        self.play(
            Create(clinical_line), FadeIn(clinical_label),
            run_time=t_unit * 0.8
        )
        self.wait(t_unit * 0.2)

        # State 6: citation label
        self.play(FadeIn(citation), run_time=t_unit * 0.6)
        self.wait(t_unit * 0.2)

        # State 7: bottom rule
        self.play(Create(bottom_rule), run_time=t_unit * 0.6)
        self.wait(t_unit * 0.4)
