"""vox_scenes.py — Why You Can Never Dig Below the Ground State
(vox-variational-floor, slate cut, 16:9)

Color law: TEAL = floor / ground state / lower bound
           CRIMSON = trial state / estimate above ground state
EXCLUSIONS: no eigenbasis-expansion proof, no helium integral,
            no Rayleigh-Ritz matrix.
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


# ── B01: COLD OPEN — any guess lands above ground state ──────────────────────
class LegacyAnyGuessAbove(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        # A vertical energy axis with a hard floor at E0 and trial state above
        axes = Axes(x_range=[0, 4, 1], y_range=[0, 6, 1],
                    x_length=5.0, y_length=5.0,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(LEFT * 1.5 + DOWN * 0.5)
        y_lbl = SerifLabel("energy", INK, size=20).next_to(axes, UP + LEFT * 2.0, buff=0.1)
        # Floor at E0
        floor = Line(axes.c2p(0, 1), axes.c2p(4, 1), color=TEAL, stroke_width=3)
        floor_lbl = LabelChip("E₀ (true ground state)", accent=TEAL, size=22)
        floor_lbl.move_to(RIGHT * 2.8 + DOWN * 1.8)
        # Trial state marker (higher)
        trial_dot = Dot(axes.c2p(2, 3.5), radius=0.2, color=CRIMSON)
        trial_lbl = LabelChip("trial energy", accent=CRIMSON, size=22)
        trial_lbl.move_to(RIGHT * 2.8 + UP * 0.8)
        arrow_to_floor = DashedLine(axes.c2p(2, 3.5), axes.c2p(2, 1.1),
                                     color=INK, stroke_width=1.5, dash_length=0.15)
        cannot_lbl = SerifLabel("can approach but never cross", INK, size=20)
        cannot_lbl.move_to(DOWN * 3.2)
        self.play(Create(axes), FadeIn(y_lbl), run_time=0.5)
        self.play(Create(floor), FadeIn(floor_lbl), run_time=dur * 0.30)
        self.play(FadeIn(trial_dot), FadeIn(trial_lbl), run_time=dur * 0.30)
        self.play(Create(arrow_to_floor), FadeIn(cannot_lbl), run_time=dur * 0.30)
        self.wait(dur * 0.10)


# ── B02: COLD OPEN — Hylleraas helium result ──────────────────────────────────
class B02_Hylleraas(Scene):
    def construct(self):
        dur = DUR.get("B02", 9.0)
        title = Text("Helium (1929): Hylleraas", font=DISPLAY, font_size=28, color=INK)
        title.move_to(UP * 3.0)
        # Three values on a vertical bar
        exact_val = Text("exact:  −78.98 eV", font=MONO, font_size=26, color=TEAL)
        exact_val.move_to(ORIGIN)
        hylleraas = Text("1 param: −77.5 eV", font=MONO, font_size=26, color=CRIMSON)
        hylleraas.move_to(UP * 1.2)
        gap_lbl = SerifLabel("above by ~2% — and provably above", CRIMSON, size=20)
        gap_lbl.move_to(DOWN * 1.2)
        arrow = Arrow(hylleraas.get_bottom(), exact_val.get_top(),
                      color=INK, stroke_width=2, buff=0.1)
        provably = LabelChip("wrong in the right direction", accent=TEAL, size=22)
        provably.move_to(DOWN * 2.5)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(exact_val), run_time=dur * 0.25)
        self.play(FadeIn(hylleraas), GrowArrow(arrow), run_time=dur * 0.30)
        self.play(FadeIn(gap_lbl), run_time=dur * 0.20)
        self.play(FadeIn(provably), run_time=dur * 0.25)


# ── B03: THE QUESTION — CARD beat, no scene class ────────────────────────────

class B03_OneSidedQuestion(Scene):
    def construct(self):
        dur = DUR.get("B03", 8.0)
        title = Text("THE QUESTION", font=MONO, font_size=18, color=CRIMSON).to_edge(UP)
        q1 = Text("Why is the error one-sided", font=DISPLAY, font_size=34, color=INK)
        q2 = Text("instead of merely small?", font=DISPLAY, font_size=34, color=TEAL)
        group = VGroup(q1, q2).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(FadeIn(title), FadeIn(group), run_time=1.0)
        self.wait(max(0.1, dur - 1.0))


# ── B04: THE PROBLEM — superposition of eigenstates ──────────────────────────
class B04_Superposition(Scene):
    def construct(self):
        dur = DUR.get("B04", 9.0)
        title = Text("Any state = superposition of eigenstates", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        # Formula: |psi> = c0|0> + c1|1> + c2|2> + ...
        expand_line = VGroup(
            Text("|ψ〉 = ", font=MONO, font_size=28, color=INK),
            Text("c₀|0〉", font=MONO, font_size=28, color=TEAL),
            Text(" + ", font=MONO, font_size=28, color=INK),
            Text("c₁|1〉", font=MONO, font_size=28, color=CRIMSON),
            Text(" + ", font=MONO, font_size=28, color=INK),
            Text("c₂|2〉", font=MONO, font_size=28, color=CRIMSON),
            Text(" + ...", font=MONO, font_size=28, color=INK),
        )
        expand_line.arrange(RIGHT, buff=0.08).move_to(UP * 1.0)
        lbl_gs = SerifLabel("ground state", TEAL, size=20)
        lbl_gs.move_to(LEFT * 2.8 + DOWN * 0.2)
        lbl_ex = SerifLabel("excited states", CRIMSON, size=20)
        lbl_ex.move_to(RIGHT * 1.5 + DOWN * 0.2)
        note = SerifLabel("Every normalized trial state decomposes this way.", INK, size=20)
        note.move_to(DOWN * 1.8)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(expand_line), run_time=dur * 0.40)
        self.play(FadeIn(lbl_gs), FadeIn(lbl_ex), run_time=dur * 0.25)
        self.play(FadeIn(note), run_time=dur * 0.25)
        self.wait(dur * 0.10)


# ── B05: THE PROBLEM — weighted average energy ───────────────────────────────
class B05_WeightedAverage(Scene):
    def construct(self):
        dur = DUR.get("B05", 9.0)
        title = Text("Energy = weighted average of eigenstate energies", font=DISPLAY,
                     font_size=22, color=INK).move_to(UP * 3.0)
        # Show: <H> = |c0|^2 E0 + |c1|^2 E1 + ...
        avg_line = Text("<H> = |c₀|² E₀ + |c₁|² E₁ + |c₂|² E₂ + ...",
                        font=MONO, font_size=24, color=INK).move_to(UP * 1.2)
        weights_lbl = SerifLabel("weights are non-negative:", INK, size=20)
        weights_lbl.move_to(DOWN * 0.3)
        weights_eq = Text("|c₀|² ≥ 0,   |c₁|² ≥ 0,   sum = 1",
                          font=MONO, font_size=24, color=INK).move_to(DOWN * 1.0)
        chip = LabelChip("non-negative weights summing to 1", accent=TEAL, size=22)
        chip.move_to(DOWN * 2.3)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(avg_line), run_time=dur * 0.35)
        self.play(FadeIn(weights_lbl), FadeIn(weights_eq), run_time=dur * 0.30)
        self.play(FadeIn(chip), run_time=dur * 0.25)
        self.wait(dur * 0.10)


# ── B06: THE PROBLEM — STILL·ai, no scene class ──────────────────────────────

class B06_LowerBoundReplacement(Scene):
    def construct(self):
        dur = DUR.get("B06", 12.0)
        title = Text("Replace every energy by the lower bound", font=DISPLAY,
                     font_size=27, color=INK).to_edge(UP)
        before = Text("sum |c_n|^2 E_n", font=MONO, font_size=31, color=CRIMSON)
        arrow = Text("≥", font=DISPLAY, font_size=38, color=INK)
        after = Text("sum |c_n|^2 E_0", font=MONO, font_size=31, color=TEAL)
        chain = VGroup(before, arrow, after).arrange(RIGHT, buff=0.7).move_to(ORIGIN)
        note = Text("because every Eₙ ≥ E₀", font=SERIF, font_size=24,
                    color=SLATE).next_to(chain, DOWN, buff=0.8)
        self.play(FadeIn(title), FadeIn(chain), FadeIn(note), run_time=1.0)
        self.wait(max(0.1, dur - 1.0))


# ── B07: THE MECHANISM — each E_n >= E_0 ─────────────────────────────────────
class B07_FloorArgument(Scene):
    def construct(self):
        dur = DUR.get("B07", 10.0)
        title = Text("Each energy is at or above E₀", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        # Show energy ladder
        energies = [(0, "E₀", TEAL), (1.2, "E₁ ≥ E₀", CRIMSON),
                    (2.0, "E₂ ≥ E₀", CRIMSON), (2.8, "E₃ ≥ E₀", CRIMSON)]
        group = VGroup()
        for y_off, label, col in energies:
            line = Line(LEFT * 3.0 + DOWN * (1.5 - y_off),
                        RIGHT * 0.5 + DOWN * (1.5 - y_off),
                        color=col, stroke_width=2.5)
            lbl = Text(label, font=MONO, font_size=22, color=col)
            lbl.move_to(RIGHT * 2.0 + DOWN * (1.5 - y_off))
            group.add(line, lbl)
        therefore = SerifLabel("every term in the average is ≥ E₀ × weight", INK, size=20)
        therefore.move_to(DOWN * 3.0)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(group), run_time=dur * 0.50)
        self.play(FadeIn(therefore), run_time=dur * 0.35)
        self.wait(dur * 0.15)


# ── B08: THE MECHANISM — total average ≥ E0 ──────────────────────────────────
class B08_EqualityCondition(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)
        title = Text("When can equality hold?", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        # Equality chain
        step1 = Text("<H> = E₀", font=MONO, font_size=30, color=TEAL)
        step1.move_to(UP * 1.6)
        step2 = Text("only if excited-state weight = 0", font=SERIF, font_size=25, color=INK)
        step2.move_to(UP * 0.7)
        step3 = Text("|ψ〉 lies entirely in the ground eigenspace", font=SERIF, font_size=24, color=TEAL)
        step3.move_to(DOWN * 0.2)
        therefore = LabelChip("unique ground state: equality up to phase", accent=TEAL, size=24)
        therefore.move_to(DOWN * 1.8)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(step1), run_time=dur * 0.20)
        self.play(FadeIn(step2), run_time=dur * 0.20)
        self.play(FadeIn(step3), run_time=dur * 0.20)
        self.play(FadeIn(therefore), run_time=dur * 0.25)
        self.wait(dur * 0.15)


# ── B09: THE MECHANISM — variational method: minimize to get best bound ───────
class B09_Minimize(Scene):
    def construct(self):
        dur = DUR.get("B09", 10.0)
        title = Text("Minimize to push the bound down", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        # Axes: parameter alpha vs energy
        axes = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1],
                    x_length=6.0, y_length=4.0,
                    axis_config={"color": INK, "stroke_width": 1.2},
                    tips=False)
        axes.move_to(DOWN * 0.3)
        x_lbl = SerifLabel("variational parameter α", INK, size=20).next_to(axes, RIGHT, buff=0.1)
        y_lbl = SerifLabel("E_trial(α)", INK, size=20).next_to(axes, UP + LEFT * 3.0, buff=0.1)
        # Parabola-like curve with minimum
        curve = axes.plot(lambda x: 0.5 * (x - 2.5) ** 2 + 1.2,
                          x_range=[0.2, 4.8, 0.05], color=CRIMSON, stroke_width=3)
        # Minimum marker
        min_dot = Dot(axes.c2p(2.5, 1.2), radius=0.18, color=TEAL)
        min_lbl = LabelChip("best upper bound", accent=TEAL, size=22)
        min_lbl.move_to(LEFT * 1.5 + UP * 0.2)
        # Floor line
        floor = DashedLine(axes.c2p(0, 0.8), axes.c2p(5, 0.8),
                            color=TEAL, stroke_width=2, dash_length=0.15)
        floor_lbl = SerifLabel("true E₀", TEAL, size=20).move_to(LEFT * 0.8 + DOWN * 2.5)
        self.play(FadeIn(title), Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)
        self.play(Create(curve), run_time=dur * 0.35)
        self.play(FadeIn(min_dot), FadeIn(min_lbl), run_time=dur * 0.25)
        self.play(Create(floor), FadeIn(floor_lbl), run_time=dur * 0.25)
        self.wait(dur * 0.15)


# ── B10: THE MECHANISM — section CARD, no scene class ────────────────────────

class B10_HardFloor(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        floor = Line(LEFT * 5, RIGHT * 5, color=TEAL, stroke_width=5).shift(DOWN)
        label = Text("E₀ — spectral floor", font=DISPLAY, font_size=29, color=TEAL).next_to(floor, DOWN, buff=0.4)
        dot = Dot(UP * 1.6, radius=0.18, color=CRIMSON)
        trial = Text("valid trial expectation", font=SERIF, font_size=24, color=CRIMSON).next_to(dot, RIGHT, buff=0.4)
        arrow = Arrow(dot.get_bottom(), floor.get_top(), color=INK, buff=0.12)
        note = Text("approach or equal — never cross", font=SERIF, font_size=25, color=INK).to_edge(UP)
        self.play(FadeIn(note), Create(floor), FadeIn(label), run_time=0.7)
        self.play(FadeIn(dot), FadeIn(trial), GrowArrow(arrow), run_time=0.8)
        self.wait(max(0.1, dur - 1.5))


# ── B11: THE IMPLICATION — one-sided guarantee ───────────────────────────────
class B11_AssumptionAudit(Scene):
    def construct(self):
        dur = DUR.get("B11", 10.0)
        title = Text("The theorem has entry conditions", font=DISPLAY,
                     font_size=28, color=INK).move_to(UP * 3.0)
        items = ["normalized trial state", "correct operator / form domain",
                 "same self-adjoint Hamiltonian", "Hamiltonian bounded below"]
        rows = VGroup(*[Text("✓  " + x, font=SERIF, font_size=25, color=TEAL)
                        for x in items]).arrange(DOWN, aligned_edge=LEFT, buff=0.42).move_to(ORIGIN)
        warn = Text("A lower result flags the setup or arithmetic — not a broken theorem.",
                    font=SERIF, font_size=20, color=CRIMSON).move_to(DOWN * 2.45)
        self.play(FadeIn(title), FadeIn(rows), run_time=1.0)
        self.play(FadeIn(warn), run_time=0.5)
        self.wait(max(0.1, dur - 1.5))


# ── B12: THE IMPLICATION — sanity check + quantum chemistry ──────────────────
class B12_YourTurn(Scene):
    def construct(self):
        dur = DUR.get("B12", 10.0)
        title = Text("YOUR TURN", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        sanity = SerifLabel("weights: 0.70 on E₀, 0.30 on E₁", INK, size=23)
        sanity.move_to(UP * 1.2)
        chem = SerifLabel("E₁ = E₀ + 2 eV", TEAL, size=25).move_to(UP * 0.2)
        limit = LabelChip("How far above E₀ is <H>?", accent=CRIMSON, size=24).move_to(DOWN * 1.2)
        note = Text("Pause and calculate.", font=SERIF, font_size=20, color=INK, slant=ITALIC).move_to(DOWN * 2.3)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(sanity), run_time=dur * 0.25)
        self.play(FadeIn(chem), run_time=dur * 0.25)
        self.play(FadeIn(limit), run_time=dur * 0.25)
        self.play(FadeIn(note), run_time=dur * 0.25)


# ── B13: THE EXAMPLE — illustrative numbers ───────────────────────────────────
class B13_YourTurnAnswer(Scene):
    def construct(self):
        dur = DUR.get("B13", 16.0)
        title = Text("ANSWER: 0.60 eV ABOVE E₀", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.1)
        subtitle = Text("excess = 0.30 × 2 eV", font=SERIF,
                        font_size=20, color=INK, slant=ITALIC).move_to(UP * 2.5)
        rows = [("ground contribution", "0.70 × 0 eV", TEAL),
                ("excited excess", "0.30 × 2 eV", CRIMSON),
                ("total excess", "0.60 eV", INK)]
        row_groups = VGroup()
        for i, (label, value, col) in enumerate(rows):
            y = 1.0 - i * 1.4
            r = VGroup(
                SerifLabel(label, col, size=20).move_to(LEFT * 3.0 + UP * y),
                Text(value, font=MONO, font_size=20, color=col).move_to(RIGHT * 2.5 + UP * y),
            )
            row_groups.add(r)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        for rg in row_groups:
            self.play(FadeIn(rg, shift=RIGHT * 0.3), run_time=dur * 0.25)
        self.wait(dur * 0.10)


class B14_CorrectTitleOutro(Scene):
    def construct(self):
        dur = DUR.get("B14", 5.0)
        self.camera.background_color = "#201F1C"
        title = Text("Why You Cannot Dig Below the Ground State", font=DISPLAY,
                     font_size=31, color="#F2EFE8")
        credit = Text("Liam, in for Bear", font=SERIF, font_size=20,
                      color="#D97757").next_to(title, DOWN, buff=0.45)
        series = Text("QUANTUM MECHANICS  ·  VOLUME THREE", font=MONO,
                      font_size=14, color="#AAA49A").next_to(credit, DOWN, buff=0.35)
        self.play(FadeIn(title), FadeIn(credit), FadeIn(series), run_time=1.0)
        self.wait(max(0.1, dur - 1.0))


# ── B14: RECAP — CARD beat, no scene class ───────────────────────────────────
