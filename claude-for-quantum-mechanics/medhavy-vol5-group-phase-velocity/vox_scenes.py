"""vox_scenes.py — medhavy-vol5-group-phase-velocity
Reel: Group vs Phase Velocity — v_group = 2 * v_phase for quadratic dispersion
Palette: medhavy

Physics: w = hbar*k^2/(2*m); v_group = hbar*k0/m; v_phase = hbar*k0/(2*m)
v_group = 2 * v_phase

Scene: Snapshot of wave packet at two time steps showing crests sliding through envelope.
Uses static frame (animation is simulated via two superimposed waves).

Gate B: header before any curves; labels at safe fixed positions.
"""

import sys, json, pathlib, os
os.environ.setdefault("VOX_PALETTE", "medhavy")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene
import numpy as np

DUR: dict = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

def _dur(bid): return DUR.get(bid, 10.0)
def _ink_text(copy, font_size=24, font=SERIF, **kw):
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)
def _c2p(ax, x, y):
    pt = ax.c2p(x, y)
    return pt if isinstance(pt, np.ndarray) else np.zeros(3)


class B03_GroupPhaseRun(Scene):
    """Wave packet snapshot: shows envelope (TEAL) and carrier crests (CRIMSON).

    Two snapshots side by side to show crest motion vs envelope motion.
    Left: t=0; Right: t=T (some later time)

    Group velocity annotation shows v_group = 2*v_phase.
    """

    def construct(self):
        dur = _dur("B03")

        # Normalized parameters (units where hbar/m = 1)
        k0 = 2.0    # central wavevector (scene units)
        dk = 0.5    # width of packet in k-space
        # v_group = k0, v_phase = k0/2 (from omega=k^2/2)

        # Time steps
        t1, t2 = 0.0, 1.0  # normalized time steps

        def wave_packet(x, t):
            """carrier * envelope for quadratic dispersion"""
            v_g = k0       # group velocity
            v_p = k0 / 2   # phase velocity
            envelope = np.exp(-((x - v_g*t)**2) * dk**2 / 2)
            carrier = np.cos(k0*x - k0**2/2 * t)
            return envelope * carrier

        def envelope(x, t):
            v_g = k0
            return np.exp(-((x - v_g*t)**2) * dk**2 / 2)

        # Axes layout — two panels
        lx, rx = -3.2, 3.2
        cy = -0.2
        pan_w, pan_h = 5.5, 4.5

        def sx_L(xv): return lx - pan_w/2 + (xv + 3) / 6 * pan_w
        def sx_R(xv): return rx - pan_w/2 + (xv + 3) / 6 * pan_w
        def sy(yv):   return cy - pan_h/2 + (yv + 1) / 2 * pan_h

        x_arr = np.linspace(-3, 3, 300)

        # Header FIRST
        header = _ink_text("Group vs Phase Velocity", font_size=26, font=DISPLAY)
        header.move_to([1.5, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # LEFT panel: axes (t=0)
        ax_L = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 1, 0.5],
            x_length=pan_w, y_length=pan_h,
            axis_config={"color": SLATE, "stroke_width": 1.2, "include_tip": False,
                         "numbers_to_include": []},
        ).move_to([lx, cy, 0])

        # RIGHT panel: axes (t=T)
        ax_R = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 1, 0.5],
            x_length=pan_w, y_length=pan_h,
            axis_config={"color": SLATE, "stroke_width": 1.2, "include_tip": False,
                         "numbers_to_include": []},
        ).move_to([rx, cy, 0])

        self.play(Create(ax_L), Create(ax_R), run_time=0.6)

        # Panel labels
        lbl_L = _ink_text("t = 0", font_size=18)
        lbl_L.move_to([lx, cy + pan_h/2 + 0.22, 0])
        lbl_R = _ink_text("t = T", font_size=18)
        lbl_R.move_to([rx, cy + pan_h/2 + 0.22, 0])
        self.play(FadeIn(lbl_L), FadeIn(lbl_R), run_time=0.3)

        # LEFT: wave packet at t=0
        pkt_L = ax_L.plot(
            lambda xv: wave_packet(xv, t1),
            x_range=[-3, 3], color=TEAL, stroke_width=2.0
        )
        self.play(Create(pkt_L), run_time=0.7)

        # LEFT: envelope at t=0 (dashed TEAL)
        env_L = ax_L.plot(
            lambda xv: envelope(xv, t1),
            x_range=[-3, 3], color=TEAL, stroke_width=1.5
        )
        env_L_neg = ax_L.plot(
            lambda xv: -envelope(xv, t1),
            x_range=[-3, 3], color=TEAL, stroke_width=1.5
        )
        self.play(FadeIn(env_L), FadeIn(env_L_neg), run_time=0.4)

        # LEFT: dot at envelope peak (t=0 => x=0)
        peak_L = Dot(point=_c2p(ax_L, 0, 1.0), radius=0.12, color=TEAL, fill_opacity=1)
        peak_L.set_stroke(width=0, opacity=0)
        self.play(FadeIn(peak_L), run_time=0.25)

        # RIGHT: wave packet at t=T (group moves to x=k0*T=2, phase moves to x=k0/2*T=1)
        pkt_R = ax_R.plot(
            lambda xv: wave_packet(xv, t2),
            x_range=[-3, 3], color=TEAL, stroke_width=2.0
        )
        self.play(Create(pkt_R), run_time=0.7)

        # RIGHT: envelope at t=T
        env_R = ax_R.plot(
            lambda xv: envelope(xv, t2),
            x_range=[-3, 3], color=TEAL, stroke_width=1.5
        )
        self.play(FadeIn(env_R), run_time=0.3)

        # RIGHT: dot at envelope peak (t=T => x=k0*T=2)
        peak_R = Dot(point=_c2p(ax_R, k0*t2, 1.0), radius=0.12, color=TEAL, fill_opacity=1)
        peak_R.set_stroke(width=0, opacity=0)
        self.play(FadeIn(peak_R), run_time=0.25)

        # Velocity ratio chip in center bottom
        ratio_chip = LabelChip("v_group = 2 x v_phase", accent=TEAL, size=20)
        ratio_chip.move_to([0.0, -3.1, 0])
        self.play(GrowFromCenter(ratio_chip), run_time=0.4)

        # Additional label chip for phase velocity
        phase_chip = LabelChip("crests: v_phase", accent=CRIMSON, size=19)
        phase_chip.move_to([-3.2, -2.5, 0])
        self.play(GrowFromCenter(phase_chip), run_time=0.35)

        elapsed = (0.4 + 0.6 + 0.3 + 0.7 + 0.4 + 0.25 + 0.7 + 0.3 + 0.25 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
