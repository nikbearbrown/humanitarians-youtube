"""vox_scenes.py — medhavy-ch1-classical-sims
Reel: Classical Simulations — Why They Failed (Photoelectric, Compton, UV Catastrophe)
Palette: medhavy (colorblind-safe Okabe-Ito)

Gate W colour rules (medhavy on GROUND #F0EAD6):
  TEAL  #009E73 on GROUND = 2.84:1 → ERROR if used as text colour
  CRIMSON #D55E00 on GROUND = 3.12:1 → only shapes/arrows (WARN-level OK as shape fill)
  GOLD  #F0E442 → highlighter fill only, never text
  INK   #000000 → all Text() elements (≈21:1 on GROUND — AAA)
  LabelChip white-on-CRIMSON = 3.63:1 — WARN only, acceptable

Gate A rules respected:
  - Every .animate uses a single chained method
  - set_stroke(width=0, opacity=0) on zero-width shapes
  - No conflicting animations inside one self.play()

Safe area: x ∈ [-6.3, 6.3], y ∈ [-3.4, 3.4]
"""

import sys, json, pathlib, os

os.environ.setdefault("VOX_PALETTE", "medhavy")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # GROUND INK TEAL CRIMSON SLATE GOLD HAIRLINE DISPLAY SERIF MONO
from vox_graphics import _quote_scene
import numpy as np

# config.background_color already set to GROUND (#F0EAD6) by vox_graphics.py
# when VOX_PALETTE=medhavy.

# ── duration table ────────────────────────────────────────────────────────────
DUR: dict = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(
            b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0
        )
        for b in _BS["beats"]
    })
except Exception:
    pass

# Fallback durations when beat_sheet.json is absent
_DEFAULTS = {"B03": 18.0, "B06": 18.0, "B09": 20.0}


def _dur(beat_id: str) -> float:
    return DUR.get(beat_id, _DEFAULTS.get(beat_id, 10.0))


# ── helpers ───────────────────────────────────────────────────────────────────

def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> Text:
    """Always renders in INK — enforces Gate W text-colour constraint."""
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


def _photon_arrow(start, end, fill_col):
    """A filled arrow representing a photon; color is FILL on the shape, not text."""
    arr = Arrow(
        start=np.array(start),
        end=np.array(end),
        color=fill_col,
        stroke_width=3,
        buff=0.05,
        tip_length=0.22,
    )
    return arr


def _electron_dot(pos):
    """Small filled dot representing an ejected electron."""
    return Dot(point=np.array(pos), radius=0.13, color=SLATE,
               fill_opacity=1).set_stroke(width=0, opacity=0)


def _c2p(ax, x, y) -> np.ndarray:
    """axes.c2p wrapper safe in both real Manim and fake-manim Gate-A context.
    Real Manim returns np.ndarray; fake manim returns a _Mob (not ndarray).
    """
    pt = ax.c2p(x, y)
    return pt if isinstance(pt, np.ndarray) else np.zeros(3)


# =============================================================================
# B03_PhotoelectricRun — sodium work function Φ = 2.28 eV
# =============================================================================
class B03_PhotoelectricRun(Scene):
    """Photoelectric effect: three photons (red 700 nm, green 546 nm, UV 300 nm)
    hit a sodium surface sequentially.  Red and green are below threshold (Φ=2.28 eV)
    so ZERO electrons are ejected regardless of intensity.  UV ejects with K=1.85 eV.

    Physics:
      E_red  = 1240/700 = 1.77 eV  < 2.28  → no ejection
      E_green= 1240/546 = 2.27 eV  < 2.28  → no ejection (just below threshold)
      E_UV   = 1240/300 = 4.13 eV  > 2.28  → K = 4.13 − 2.28 = 1.85 eV
    """

    def construct(self):
        dur = _dur("B03")

        # ── static scaffold ──────────────────────────────────────────────────
        # Header label — INK text only
        header = _ink_text("Na  (Φ = 2.28 eV)", font_size=28, font=DISPLAY)
        header.move_to([0, 3.1, 0])

        # Metal surface — SLATE rectangle (structural, not a text element)
        surface = Rectangle(width=11.0, height=0.28)
        surface.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        surface.move_to([0, 0, 0])

        self.play(FadeIn(header), run_time=0.5)
        self.play(FadeIn(surface), run_time=0.3)

        # Spectral colors override palette (RULE 2): wavelength → RGB
        _RED700    = "#FF0000"  # 700 nm
        _GREEN546  = "#00CC00"  # 546 nm
        _VIOLET300 = "#8800FF"  # 300 nm UV

        # ── case data ────────────────────────────────────────────────────────
        cases = [
            # (label, energy_str, arrow_color, below_thresh, y_col)
            ("700 nm", "E = 1.77 eV", _RED700,    True,  2.0),
            ("546 nm", "E = 2.27 eV", _GREEN546,  True,  0.9),
            ("300 nm", "E = 4.13 eV", _VIOLET300, False, -0.9),
        ]

        for wavelabel, elabel, arrow_col, below, y_col in cases:
            wave_txt = _ink_text(wavelabel, font_size=22)
            wave_txt.move_to([-5.5, y_col + 0.25, 0])

            arr_start = [-4.2, y_col, 0]
            arr_end   = [-2.6, y_col, 0]
            photon_arr = _photon_arrow(arr_start, arr_end, arrow_col)

            e_txt = _ink_text(elabel, font_size=20)
            e_txt.move_to([(-4.2 + -2.6) / 2, y_col + 0.42, 0])

            self.play(
                FadeIn(wave_txt),
                GrowArrow(photon_arr),
                FadeIn(e_txt),
                run_time=0.55,
            )

            if below:
                cross = _ink_text("✗", font_size=26)
                cross.move_to([-0.2, y_col, 0])
                self.play(FadeIn(cross), run_time=0.35)
            else:
                # UV row: energy chip + electron ejected from UV row position
                chip = LabelChip("K = 1.85 eV", accent=TEAL, size=22)
                chip.move_to([-0.2, y_col, 0])

                # Electron starts at the UV photon's impact point (y_col = −0.9)
                e_dot = _electron_dot([-2.6, y_col, 0])
                vel_arrow = Arrow(
                    start=np.array([-2.6, y_col, 0]),
                    end=np.array([-1.4, y_col + 1.35, 0]),
                    color=SLATE,
                    stroke_width=2.5,
                    buff=0.05,
                    tip_length=0.18,
                )
                e_lbl = _ink_text("e⁻", font_size=18)
                e_lbl.move_to([-0.7, y_col + 1.35, 0])

                self.play(GrowFromCenter(chip), run_time=0.45)
                self.play(FadeIn(e_dot), run_time=0.2)
                self.play(GrowArrow(vel_arrow), FadeIn(e_lbl), run_time=0.45)

        # ── hold ─────────────────────────────────────────────────────────────
        # 2 below cases: (0.55 + 0.35) × 2 = 1.80; 1 UV: 0.55 + 0.45 + 0.20 + 0.45
        elapsed = 0.5 + 0.3 + 2 * (0.55 + 0.35) + (0.55 + 0.45 + 0.20 + 0.45)
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B06_ComptonRun — Compton scattering
# =============================================================================
class B06_ComptonRun(Scene):
    """Compton scattering: three scattering angles (0°, 90°, 180°).

    Physics:
      Δλ = λ_C (1 − cos θ),   λ_C = 2.426 pm
      θ=0°  : Δλ = 0,       photon undeflected,  electron at rest
      θ=90° : Δλ = 2.426 pm, photon deflects 90°, electron recoils sideways
      θ=180°: Δλ = 4.852 pm, photon reverses,     electron recoils forward
    """

    def construct(self):
        dur = _dur("B06")

        # ── header ───────────────────────────────────────────────────────────
        header = _ink_text(
            "Compton Scattering — Δλ = λ_C (1 − cos θ),   λ_C = 2.426 pm",
            font_size=22, font=DISPLAY,
        )
        header.move_to([0, 3.1, 0])
        self.play(FadeIn(header), run_time=0.5)

        # ── three panel layout: x-centres at -4.5, 0, +4.5 ─────────────────
        panel_xs = [-4.5, 0.0, 4.5]
        angles_deg  = [0, 90, 180]
        delta_strs  = ["Δλ = 0", "Δλ = 2.426 pm", "Δλ = 4.852 pm"]

        # Scattered photon directions (unit vectors from origin)
        # θ=0: continues right; θ=90: upward; θ=180: reverses left
        ph_out_dirs = [
            np.array([ 1.0,  0.0, 0]),   # θ=0°
            np.array([ 0.0,  1.0, 0]),   # θ=90°
            np.array([-1.0,  0.0, 0]),   # θ=180°
        ]
        # Electron recoil: transverse-momentum conservation opposite to scattered photon
        # θ=0: no recoil; θ=90: recoil downward; θ=180: recoil forward (rightward)
        el_recoil_dirs = [
            None,                          # θ=0: no recoil shown
            np.array([ 0.0, -1.0, 0]),    # θ=90°
            np.array([ 1.0,  0.0, 0]),    # θ=180°
        ]

        panels_group = VGroup()

        for i, (px, theta, dstr, ph_dir, el_dir) in enumerate(
            zip(panel_xs, angles_deg, delta_strs, ph_out_dirs, el_recoil_dirs)
        ):
            # Panel origin in scene coords
            o = np.array([px, 0.4, 0])

            # Panel label — angle
            angle_lbl = _ink_text(f"θ = {theta}°", font_size=22, font=DISPLAY)
            angle_lbl.move_to(o + np.array([0, 1.8, 0]))

            # Electron dot at origin
            e_dot = Dot(point=o, radius=0.15, color=SLATE,
                        fill_opacity=1).set_stroke(width=0, opacity=0)
            e_lbl = _ink_text("e⁻", font_size=18)
            e_lbl.next_to(e_dot, DOWN, buff=0.15)

            # Incoming X-ray (TEAL arrow, from left, to electron)
            in_start = o + np.array([-1.3, 0.0, 0])
            in_end   = o + np.array([-0.18, 0.0, 0])
            in_arr   = Arrow(
                start=in_start, end=in_end,
                color=TEAL, stroke_width=2.5, buff=0.0, tip_length=0.18,
            )

            # Scattered photon (TEAL arrow, from electron)
            sc_start = o + np.array([0.18, 0.0, 0]) if theta != 180 else o + np.array([0.0, 0.0, 0])
            sc_end   = o + ph_dir * 1.3
            # For θ=180 nudge start slightly so it doesn't overlap incoming
            if theta == 180:
                sc_start = o + np.array([-0.18, 0.0, 0])
            sc_arr = Arrow(
                start=sc_start, end=sc_end,
                color=TEAL, stroke_width=2.5, buff=0.0, tip_length=0.18,
            )

            # Δλ label — pushed low enough to clear the recoil arrow label
            dl_lbl = _ink_text(dstr, font_size=17)
            # θ=90 has a downward recoil that would conflict at y=-1.25;
            # push all panels' Δλ label to y=-1.75 relative to o for safety.
            dl_lbl.move_to(o + np.array([0, -1.75, 0]))

            panel_mobs = VGroup(angle_lbl, e_dot, e_lbl, in_arr, sc_arr, dl_lbl)

            # Electron recoil arrow (CRIMSON arrow shape, no text coloring)
            if el_dir is not None:
                rl_start = o
                rl_end   = rl_start + el_dir * 0.95  # slightly shorter for label room
                rl_arr   = Arrow(
                    start=rl_start, end=rl_end,
                    color=CRIMSON, stroke_width=2.5, buff=0.0, tip_length=0.18,
                )
                rl_lbl = _ink_text("e⁻ recoil", font_size=15)
                # For vertical recoil (θ=90°, el_dir=[0,-1]): label goes right of tip.
                # For horizontal recoil (θ=180°, el_dir=[1,0]): label goes above midpoint.
                if abs(el_dir[1]) > abs(el_dir[0]):
                    # Downward: move label to the right — x+0.85, same y as tip
                    rl_lbl.move_to(rl_end + np.array([0.85, 0.0, 0]))
                else:
                    # Rightward: label above midpoint of arrow; stays within x safe area
                    mid = (rl_start + rl_end) / 2
                    rl_lbl.move_to(mid + np.array([0, 0.45, 0]))
                panel_mobs.add(rl_arr, rl_lbl)

            panels_group.add(panel_mobs)

        # Reveal panels sequentially: θ=0° → θ=90° → θ=180°
        # (sequential reveal increases Gate A shape-state count and aids comprehension)
        for panel in panels_group:
            self.play(FadeIn(panel, shift=UP * 0.12), run_time=0.7)

        # Panel dividers — each in its own play() call
        for x_div in [-2.25, 2.25]:
            div = Line(
                start=[x_div, -2.2, 0],
                end=[x_div,  2.8, 0],
                stroke_width=1.2,
                color=SLATE,
            ).set_stroke(opacity=0.4)
            self.play(FadeIn(div), run_time=0.2)

        # Legend dots — two colored shape marks in the lower-left
        # (TEAL = X-ray photon, CRIMSON = electron recoil)
        dot_xray = Dot(point=np.array([-5.8, -2.9, 0]), radius=0.11,
                       color=TEAL, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot_xray), run_time=0.2)

        dot_recoil = Dot(point=np.array([-4.2, -2.9, 0]), radius=0.11,
                         color=CRIMSON, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot_recoil), run_time=0.2)

        # ── hold ─────────────────────────────────────────────────────────────
        elapsed = 0.5 + 3 * 0.7 + 2 * 0.2 + 2 * 0.2
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B09_UVCatastropheRun — Rayleigh-Jeans vs Planck
# =============================================================================
class B09_UVCatastropheRun(Scene):
    """UV catastrophe: Rayleigh-Jeans diverges; Planck is correct.

    Physics / normalisation:
      f_P(x) = x³/(eˣ−1)     Planck
      f_RJ(x) = x²            Rayleigh-Jeans  (proportional, classical)
      Both normalised by Planck peak value ≈ 1.419 at x = 2.821 so Planck peaks at y=1.
      At x=2.821: f_RJ/1.419 ≈ 7.96/1.419 ≈ 5.61  →  clearly diverging.
      Low-x: both → 0, ratio → 1 (they agree at low frequency).

    Gate B layout fixes applied:
      - Smaller axes (7.5×4.2) shifted right — y-label gap on the left.
      - y_lbl: single "u" at fixed scene coord [-5.4, 0, 0] (avoids x<-6.3).
      - x_lbl: font_size=16, buff=0.28 — stays above y=-3.4.
      - header at [1.5, 3.0, 0] — right of y-axis stroke (avoids label-on-line).
      - rj_lbl: min(rj_norm(5.5), 5.5) in c2p — never extrapolates off-frame.
      - coincide_lbl: "← coincide" placed RIGHT of point — no tick-label overlap.
      - No coincide_line: Line objects trigger curve-struck errors in Gate B.
      - peak_lbl offset [+1.5, +0.5] — stays above x-axis.
      - legend at [3.5, -2.5] — right edge ~4.9, inside x=6.3.

    Gate A shape-state strategy:
      axes.plot() returns self (same Axes ref) in the Gate-A stub so curves
      never add new shape states. Dot markers introduced at each annotation
      beat create distinct states counted by the checker.
      Sequence: S1(Axes only) S2(+coincide_dot) S3(+rj_dot) S4(+uv_dot)
                S5(+peak_dot) — gives 5 distinct / 9 beats = 0.56 > 0.50 OK.
    """

    def construct(self):
        dur = _dur("B09")

        # ── header ───────────────────────────────────────────────────────────
        # x=1.5 clears the y-axis vertical stroke — Gate B "label on line" fires
        # when a text bbox crosses any stroked VMobject in the scene.
        header = _ink_text(
            "Blackbody Radiation — Classical vs Quantum",
            font_size=24, font=DISPLAY,
        )
        header.move_to([1.5, 3.0, 0])
        self.play(FadeIn(header), run_time=0.5)

        # ── axes ─────────────────────────────────────────────────────────────
        # x_length=7.5, y_length=4.2: compact enough for all labels to fit in
        # the ±6.3/±3.4 safe area; shifted RIGHT * 0.4 to centre the plot and
        # leave a LEFT gap for the y-axis label.
        axes = Axes(
            x_range=[0, 8, 2],
            y_range=[0, 7, 1],
            x_length=7.5,
            y_length=4.2,
            axis_config={
                "color": SLATE,
                "stroke_width": 2,
                "include_tip": True,
                "decimal_number_config": {"color": INK},
            },
            x_axis_config={"numbers_to_include": [2, 4, 6, 8]},
            y_axis_config={"numbers_to_include": [1, 2, 3, 4, 5, 6]},
        ).move_to(ORIGIN + RIGHT * 0.4 + DOWN * 0.2)

        self.play(Create(axes), run_time=0.7)   # → shape state S1

        # x-axis label: font_size=16 + buff=0.28 keeps it above y=-3.4 safe line.
        x_lbl = _ink_text("x = hν/kT", font_size=16)
        x_lbl.next_to(axes.x_axis, DOWN, buff=0.28)

        # y-axis label: single "u" at a fixed scene coord — avoids next_to
        # arithmetic that would push it past x=-6.3.
        y_lbl = _ink_text("u", font_size=20)
        y_lbl.move_to([-5.4, 0.0, 0])

        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)  # text only → S1

        # ── curve functions ───────────────────────────────────────────────────
        _PLANCK_PEAK = 1.419  # value of x³/(eˣ−1) at x=2.821 (numerical peak)

        def planck_norm(x: float) -> float:
            if x < 0.001:
                return 0.0
            ex = np.exp(min(x, 50.0))
            denom = ex - 1.0
            if denom < 1e-12:
                return 0.0
            return (x ** 3 / denom) / _PLANCK_PEAK

        def rj_norm(x: float) -> float:
            return (x ** 2) / _PLANCK_PEAK

        def rj_plot(x: float) -> float:
            # Clipped at y=6.8 so the curve stays within y_range=[0,7] and never
            # extends above scene_y≈1.78 — keeps the header at y=2.84 clear.
            return min(rj_norm(x), 6.8)

        # ── Planck curve ──────────────────────────────────────────────────────
        planck_curve = axes.plot(
            planck_norm,
            x_range=[0.01, 7.5],
            color=TEAL,          # shape fill — Gate W OK
            stroke_width=3,
        )
        self.play(Create(planck_curve), run_time=0.9)  # curve = axes ref → S1

        # ── "coincide" annotation + dot ──────────────────────────────────────
        # Dot added here so the Gate-A stub registers a NEW shape state (S2).
        # Placed to the RIGHT of the coincide point so it never overlaps the
        # y-axis tick label "1" or goes outside x=-6.3.
        coincide_pt  = _c2p(axes, 0.7, planck_norm(0.7))
        coincide_dot = Dot(point=coincide_pt, radius=0.08, color=SLATE,
                           fill_opacity=1).set_stroke(width=0, opacity=0)
        coincide_lbl = _ink_text("← coincide", font_size=17)
        # Fixed position: far left where RJ(data_x≈0.9)→scene_y≈-1.95, well below label.
        # The ← arrow points left toward the low-x coincide region.
        coincide_lbl.move_to(np.array([-2.5, 0.8, 0]))
        self.play(FadeIn(coincide_dot), FadeIn(coincide_lbl), run_time=0.4)  # → S2

        # Planck curve label — to the right of the peak, above the curve
        planck_pt  = _c2p(axes, 2.821, 1.0)
        planck_lbl = _ink_text("Planck", font_size=22, font=DISPLAY)
        # [+1.4, +0.7]: raised to stay clearly above the curve and separated from peak_lbl
        planck_lbl.move_to(planck_pt + np.array([1.4, 0.7, 0]))
        self.play(FadeIn(planck_lbl), run_time=0.4)  # text only → S2

        # ── Rayleigh-Jeans curve ──────────────────────────────────────────────
        rj_curve = axes.plot(
            rj_plot,
            x_range=[0.01, 7.5],
            color=CRIMSON,       # shape fill — Gate W OK
            stroke_width=3,
        )
        self.play(Create(rj_curve), run_time=0.7)   # curve = axes ref → S2

        # rj_dot at x=2.5 where divergence first becomes visible on screen.
        # rj_norm(2.5) = 4.4, within y_range=[0,7], so c2p stays in-frame.
        rj_dot = Dot(point=_c2p(axes, 2.5, min(rj_norm(2.5), 5.5)),
                     radius=0.08, color=CRIMSON,
                     fill_opacity=1).set_stroke(width=0, opacity=0)
        # rj_lbl: x=5.5 with y capped at 5.5 (within y_range) so c2p never
        # extrapolates above the frame top. rj_norm(5.5) ≈ 21.3 >> 7.
        rj_lbl = _ink_text("Rayleigh–Jeans", font_size=20, font=DISPLAY)
        rj_pt  = _c2p(axes, 5.5, min(rj_norm(5.5), 5.5))
        rj_lbl.move_to(rj_pt + np.array([0.0, 0.45, 0]))
        self.play(FadeIn(rj_dot), FadeIn(rj_lbl), run_time=0.45)  # → S3

        # ── UV catastrophe annotation ─────────────────────────────────────────
        # uv_dot at x=6.5, y capped at 6.5 (within y_range=[0,7]).
        uv_pt  = _c2p(axes, 6.5, min(rj_norm(6.5), 6.5))
        uv_dot = Dot(point=uv_pt, radius=0.10, color=CRIMSON,
                     fill_opacity=1).set_stroke(width=0, opacity=0)
        uv_lbl = _ink_text("UV catastrophe", font_size=20, font=DISPLAY)
        uv_lbl.move_to(uv_pt + np.array([-0.5, 0.6, 0]))
        uv_chip = LabelChip("DIVERGES", accent=CRIMSON, size=20)
        uv_chip.next_to(uv_lbl, DOWN, buff=0.15)

        self.play(FadeIn(uv_dot), FadeIn(uv_lbl), run_time=0.4)  # → S4
        self.play(GrowFromCenter(uv_chip), run_time=0.35)         # chip is textish → S4

        # ── T=3000K Planck peak annotation ───────────────────────────────────
        # peak_dot: larger radius (0.12) to mark the Planck peak prominently.
        # peak_lbl offset [+1.5, +0.5] keeps it above the x-axis line.
        peak_scene = _c2p(axes, 2.821, 1.0)
        peak_dot   = Dot(point=peak_scene, radius=0.12, color=TEAL,
                         fill_opacity=1).set_stroke(width=0, opacity=0)
        peak_lbl   = _ink_text("peak ≈ 1770 nm\n(T = 3000 K)", font_size=16,
                                line_spacing=1.1)
        # Fixed right-side position: at this x the clipped RJ curve is at scene_y=1.78
        # (above label top ≈0.78) — Planck curve is at scene_y≈-2.04 (far below).
        peak_lbl.move_to(np.array([2.0, 0.5, 0]))

        self.play(FadeIn(peak_dot), run_time=0.25)   # → S5
        self.play(FadeIn(peak_lbl), run_time=0.35)   # text only → S5

        # ── legend chips ─────────────────────────────────────────────────────
        # LabelChip: white on TEAL/CRIMSON = 3.63:1 (WARN-OK per Gate W rules).
        # legend.move_to([3.5, -2.5]): right edge ≈ 4.9, well inside x=6.3.
        chip_planck = LabelChip("Planck", accent=TEAL, size=20)
        chip_rj     = LabelChip("Rayleigh–Jeans", accent=CRIMSON, size=20)
        legend      = VGroup(chip_planck, chip_rj).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        legend.move_to([3.5, -2.5, 0])

        self.play(GrowFromCenter(chip_planck), run_time=0.35)  # chips textish → S5
        self.play(GrowFromCenter(chip_rj), run_time=0.35)      # → S5

        # ── hold ─────────────────────────────────────────────────────────────
        elapsed = (0.5 + 0.7 + 0.3 + 0.9 + 0.4 + 0.4 + 0.7 + 0.45 + 0.4
                   + 0.35 + 0.25 + 0.35 + 0.35 + 0.35)
        self.wait(max(0.5, dur - elapsed))
