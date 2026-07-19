import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np
import math

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass


# ── B01: COLD OPEN — scattering angles at different deflections ───────────────
class OldScatteringAnglesColdOpen(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        target = Circle(radius=0.5, stroke_width=2, color=CRIMSON)
        target.set_fill(CRIMSON, opacity=0.25).move_to(ORIGIN)
        # Incoming arrows
        angles_out = [10, 45, 135]
        colors = [TEAL, TEAL, TEAL]
        inc_arrows = VGroup()
        out_arrows = VGroup()
        angle_lbls = VGroup()
        for angle_deg, col in zip(angles_out, colors):
            # All come from left
            inc = Arrow(np.array([-5.0, 0.0, 0.0]), np.array([-0.6, 0.0, 0.0]),
                        buff=0.0, color=col, stroke_width=1.5)
            inc_arrows.add(inc)
            angle_rad = angle_deg * np.pi / 180
            end = np.array([3.0 * np.cos(angle_rad), 3.0 * np.sin(angle_rad), 0.0])
            out = Arrow(np.array([0.6, 0.0, 0.0]), end, buff=0.0, color=col, stroke_width=1.5)
            out_arrows.add(out)
            lbl = Text(f"{angle_deg}°", font=MONO, font_size=16, color=col).move_to(
                end + np.array([0.4, 0.15, 0.0]))
            angle_lbls.add(lbl)
        x_lbl = Text("different angles = different q", font=SERIF, font_size=19,
                     color=INK, slant=ITALIC).move_to(DOWN * 2.8)
        self.play(FadeIn(target), run_time=0.3)
        self.play(Create(inc_arrows), Create(out_arrows), run_time=dur * 0.55)
        self.play(FadeIn(angle_lbls), FadeIn(x_lbl), target.animate.scale(1.05), run_time=dur * 0.45)


# ── B02: COLD OPEN — Born = Fourier transform ─────────────────────────────────
class B02_BornFourier(Scene):
    def construct(self):
        dur = DUR.get("B02", 9.0)
        title = Text("Born approximation", font=DISPLAY, font_size=30, color=INK).move_to(UP * 3.0)
        formula = Text("f_Born(theta)  proportional to  V_tilde(q)", font=MONO,
                       font_size=24, color=TEAL).move_to(UP * 1.6)
        box = Rectangle(width=9.5, height=0.85, stroke_width=2, color=TEAL)
        box.set_fill(TEAL, opacity=0.08).move_to(UP * 1.6)
        where = Text("where V_tilde(q) = Fourier transform of V(r) at momentum transfer q",
                     font=SERIF, font_size=18, color=INK, slant=ITALIC).move_to(UP * 0.4)
        insight = Text("detector = Fourier analyzer", font=DISPLAY, font_size=26,
                       color=TEAL).move_to(DOWN * 0.8)
        self.play(FadeIn(title), run_time=0.3)
        self.play(FadeIn(box), FadeIn(formula), run_time=dur * 0.35)
        self.play(FadeIn(where), run_time=dur * 0.30)
        self.play(FadeIn(insight), box.animate.scale(1.01), run_time=dur * 0.35)


# ── B03: CARD — THE QUESTION (no scene needed) ────────────────────────────────


# ── B04: THE PROBLEM — momentum transfer q ───────────────────────────────────
class B04_MomentumTransfer(Scene):
    def construct(self):
        dur = DUR.get("B04", 11.0)
        title = Text("Momentum transfer q = 2k sin(theta/2)", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        # Vector triangle: k (incident), k' (scattered), q = k - k'
        k_arrow = Arrow(np.array([-2.5, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]),
                        buff=0.0, color=TEAL, stroke_width=3)
        theta = 50 * np.pi / 180
        kp_end = np.array([2.5 * np.cos(theta), 2.5 * np.sin(theta), 0.0])
        kp_arrow = Arrow(np.array([0.0, 0.0, 0.0]), kp_end,
                         buff=0.0, color=TEAL, stroke_width=3)
        q_arrow = Arrow(np.array([-2.5, 0.0, 0.0]), kp_end,
                        buff=0.0, color=CRIMSON, stroke_width=2.5)
        k_lbl = Text("k (incident)", font=MONO, font_size=17, color=TEAL).move_to(np.array([-1.5, -0.4, 0.0]))
        kp_lbl = Text("k' (scattered)", font=MONO, font_size=17, color=TEAL).move_to(
            np.array([1.2, 1.5, 0.0]))
        q_lbl = Text("q = k - k'", font=MONO, font_size=17, color=CRIMSON).move_to(
            np.array([-0.5, 1.0, 0.0]))
        theta_lbl = Text("theta = 50°", font=MONO, font_size=16, color=INK).move_to(
            np.array([0.5, 0.3, 0.0]))
        q_small = Text("small theta: q ~ 0", font=SERIF, font_size=18,
                       color=TEAL, slant=ITALIC).move_to(np.array([-3.5, -2.0, 0.0]))
        q_large = Text("theta ~ 180: q ~ 2k", font=SERIF, font_size=18,
                       color=CRIMSON, slant=ITALIC).move_to(np.array([3.0, -2.0, 0.0]))
        self.play(FadeIn(title), run_time=0.3)
        self.play(Create(k_arrow), FadeIn(k_lbl), run_time=dur * 0.25)
        self.play(Create(kp_arrow), FadeIn(kp_lbl), FadeIn(theta_lbl), run_time=dur * 0.25)
        self.play(Create(q_arrow), FadeIn(q_lbl), run_time=dur * 0.25)
        self.play(FadeIn(q_small), FadeIn(q_large), run_time=dur * 0.25)


# ── B05: THE PROBLEM — Fourier evaluation ─────────────────────────────────────
class B05_FourierEval(Scene):
    def construct(self):
        dur = DUR.get("B05", 11.0)
        title = Text("Each angle evaluates the potential's Fourier transform", font=DISPLAY,
                     font_size=20, color=INK).move_to(UP * 3.0)
        axes = Axes(x_range=[-4, 4, 1], y_range=[0, 1.2, 0.5],
                    x_length=8.0, y_length=3.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    x_axis_config={"include_numbers": False},
                    y_axis_config={"include_numbers": False},
                    tips=False)
        axes.move_to(DOWN * 0.3)
        # Fourier transform of potential (peaked at q=0, decaying)
        vq_curve = axes.plot(lambda x: np.exp(-0.4 * x**2),
                             x_range=[-3.8, 3.8], color=CRIMSON, stroke_width=3)
        x_lbl = Text("q (momentum transfer)", font=SERIF, font_size=17, color=INK,
                     slant=ITALIC).next_to(axes, DOWN + RIGHT * 2, buff=0.1)
        y_lbl = Text("|V_tilde(q)|", font=SERIF, font_size=17, color=CRIMSON,
                     slant=ITALIC).next_to(axes, UP + LEFT * 2.5, buff=0.1)
        fwd_lbl = Text("forward (q=0): long-range", font=SERIF, font_size=17,
                       color=TEAL, slant=ITALIC).move_to(np.array([-0.2, 2.3, 0.0]))
        back_lbl = Text("large q: fine structure", font=SERIF, font_size=17,
                        color=CRIMSON, slant=ITALIC).move_to(np.array([2.5, 0.9, 0.0]))
        self.play(FadeIn(title), Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)
        self.play(Create(vq_curve), run_time=dur * 0.50)
        self.play(FadeIn(fwd_lbl), FadeIn(back_lbl), vq_curve.animate.set_stroke(width=4), run_time=dur * 0.50)


# ── B06: THE MECHANISM — q=0 to q=2k scan ─────────────────────────────────────
class B06_QScan(Scene):
    def construct(self):
        dur = DUR.get("B06", 12.0)
        title = Text("Angle scans q from 0 to 2k", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        rows = [
            ("theta = 0  (forward)", "q = 0", "reads V_tilde(0) = integral of V"),
            ("theta = 90°         ", "q = k*sqrt(2)", "reads medium frequencies"),
            ("theta = 180° (back) ", "q = 2k", "reads finest structure"),
        ]
        group = VGroup()
        box_bg = Rectangle(width=12.5, height=2.8, stroke_width=1, color=INK)
        box_bg.set_fill(INK, opacity=0.04).move_to(UP * 0.5)
        for i, (angle, q_val, what) in enumerate(rows):
            y = 1.2 - i * 1.1
            a_lbl = Text(angle, font=MONO, font_size=17, color=TEAL).move_to(LEFT * 3.8 + UP * y)
            q_lbl = Text(q_val, font=MONO, font_size=17, color=INK).move_to(LEFT * 0.3 + UP * y)
            w_lbl = Text(what, font=SERIF, font_size=16, color=CRIMSON,
                         slant=ITALIC).move_to(RIGHT * 3.0 + UP * y)
            group.add(a_lbl, q_lbl, w_lbl)
        key_lbl = Text("scanning theta = scanning q = reading Fourier modes", font=DISPLAY,
                       font_size=18, color=TEAL).move_to(DOWN * 2.0)
        self.play(FadeIn(title), FadeIn(box_bg), run_time=0.4)
        self.play(FadeIn(group), run_time=dur * 0.55)
        self.play(FadeIn(key_lbl), box_bg.animate.scale(1.01), run_time=dur * 0.45)


# ── B07: THE MECHANISM — full angular scan = full Fourier spectrum ────────────
class OldFullReconstructionOverclaim(Scene):
    def construct(self):
        dur = DUR.get("B07", 11.0)
        axes_v = Axes(x_range=[-4, 4, 1], y_range=[0, 1.2, 0.5],
                      x_length=4.5, y_length=2.8,
                      axis_config={"color": INK, "stroke_width": 1.2},
                      x_axis_config={"include_numbers": False},
                      y_axis_config={"include_numbers": False},
                      tips=False)
        axes_v.move_to(LEFT * 3.0 + DOWN * 0.5)
        axes_d = Axes(x_range=[0, 3.5, 1], y_range=[0, 1.2, 0.5],
                      x_length=4.5, y_length=2.8,
                      axis_config={"color": INK, "stroke_width": 1.2},
                      x_axis_config={"include_numbers": False},
                      y_axis_config={"include_numbers": False},
                      tips=False)
        axes_d.move_to(RIGHT * 3.0 + DOWN * 0.5)
        potential = axes_v.plot(lambda x: np.exp(-0.5 * x**2),
                                x_range=[-3.8, 3.8], color=CRIMSON, stroke_width=2.5)
        detector = axes_d.plot(lambda x: np.exp(-0.4 * x**2),
                               x_range=[0, 3.2], color=TEAL, stroke_width=2.5)
        v_lbl = Text("V_tilde(q)", font=SERIF, font_size=17, color=CRIMSON,
                     slant=ITALIC).move_to(LEFT * 3.0 + UP * 1.6)
        d_lbl = Text("d-sigma/d-Omega", font=SERIF, font_size=17, color=TEAL,
                     slant=ITALIC).move_to(RIGHT * 3.0 + UP * 1.6)
        eq_arrow = Arrow(np.array([-0.4, -0.5, 0.0]), np.array([0.4, -0.5, 0.0]),
                         buff=0.1, color=INK, stroke_width=2)
        eq_lbl = Text("IFT", font=MONO, font_size=16, color=INK).move_to(np.array([0.0, -0.1, 0.0]))
        self.play(Create(axes_v), Create(axes_d), run_time=0.4)
        self.play(Create(potential), FadeIn(v_lbl), run_time=dur * 0.40)
        self.play(Create(detector), FadeIn(d_lbl), Create(eq_arrow), FadeIn(eq_lbl), run_time=dur * 0.60)


# ── B08: THE IMPLICATION — form factor for extended targets ───────────────────
class B08_FormFactor(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)
        title = Text("Extended target: form factor F(q)", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        axes = Axes(x_range=[0, 6, 1], y_range=[0, 1.2, 0.5],
                    x_length=7.5, y_length=3.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    x_axis_config={"include_numbers": False},
                    y_axis_config={"include_numbers": False},
                    tips=False)
        axes.move_to(DOWN * 0.3)
        # |F(q)|^2 for uniform sphere: oscillates and falls
        def form_sq(x):
            if x < 0.05:
                return 1.0
            return max(0, (3 * (np.sin(x) - x * np.cos(x)) / x**3) ** 2)
        form_curve = axes.plot(form_sq, x_range=[0.05, 5.8], color=TEAL, stroke_width=3)
        x_lbl = Text("q*R", font=SERIF, font_size=17, color=INK, slant=ITALIC).next_to(axes, DOWN + RIGHT * 2, buff=0.1)
        y_lbl = Text("|F(q)|^2", font=SERIF, font_size=17, color=TEAL, slant=ITALIC).next_to(axes, UP + LEFT * 2.0, buff=0.1)
        supp_lbl = Text("large q suppressed: no high-freq structure", font=SERIF,
                        font_size=18, color=TEAL, slant=ITALIC).move_to(np.array([1.5, 2.3, 0.0]))
        self.play(FadeIn(title), Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)
        self.play(Create(form_curve), run_time=dur * 0.55)
        self.play(FadeIn(supp_lbl), form_curve.animate.set_stroke(width=4), run_time=dur * 0.45)


# ── B09: THE IMPLICATION — SLAC found quarks ─────────────────────────────────
class OldSLACOverclaim(Scene):
    def construct(self):
        dur = DUR.get("B09", 10.0)
        title = Text("SLAC 1969: deep inelastic scattering", font=DISPLAY,
                     font_size=22, color=INK).move_to(UP * 3.0)
        smooth_lbl = Text("smooth proton (no quarks)", font=SERIF, font_size=20,
                          color=INK, slant=ITALIC).move_to(UP * 1.5)
        smooth_box = Rectangle(width=7.0, height=0.65, stroke_width=0)
        smooth_box.set_fill(SLATE, opacity=0.15).move_to(UP * 1.5)
        smooth_pred = Text("F(q) drops to 0 at large q — no large-angle scattering", font=SERIF,
                           font_size=17, color=SLATE, slant=ITALIC).move_to(UP * 0.6)
        quark_lbl = Text("with quarks (point charges inside)", font=SERIF, font_size=20,
                         color=TEAL, slant=ITALIC).move_to(DOWN * 0.2)
        quark_box = Rectangle(width=7.5, height=0.65, stroke_width=0)
        quark_box.set_fill(TEAL, opacity=0.15).move_to(DOWN * 0.2)
        quark_pred = Text("F(q) stays large — hard substructure scatters at large angles", font=SERIF,
                          font_size=17, color=TEAL, slant=ITALIC).move_to(DOWN * 1.1)
        result_lbl = Text("experiment saw large-angle signal => quarks exist", font=DISPLAY,
                          font_size=18, color=TEAL).move_to(DOWN * 2.3)
        self.play(FadeIn(title), FadeIn(smooth_box), FadeIn(smooth_lbl), run_time=0.4)
        self.play(FadeIn(smooth_pred), run_time=dur * 0.30)
        self.play(FadeIn(quark_box), FadeIn(quark_lbl), FadeIn(quark_pred), run_time=dur * 0.40)
        self.play(FadeIn(result_lbl), quark_box.animate.scale(1.02), run_time=dur * 0.30)


# ── B10: THE EXAMPLE — illustrative Yukawa numbers ───────────────────────────
class B10_YukawaExample(Scene):
    def construct(self):
        dur = DUR.get("B10", 12.0)
        title = Text("Illustrative: Yukawa potential", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        subtitle = Text("(labeled illustrative)", font=SERIF, font_size=17,
                        color=INK, slant=ITALIC).move_to(UP * 2.35)
        params = [
            ("range 1/mu", "1 fm"),
            ("k/mu = 5   ", "resolved range"),
        ]
        param_group = VGroup()
        for i, (k, v) in enumerate(params):
            k_lbl = Text(k + ":", font=SERIF, font_size=20, color=INK,
                         slant=ITALIC).move_to(LEFT * 3.0 + UP * (1.0 - i * 0.8))
            v_lbl = Text(v, font=MONO, font_size=20, color=TEAL).move_to(
                RIGHT * 0.8 + UP * (1.0 - i * 0.8))
            param_group.add(k_lbl, v_lbl)
        forward_lbl = Text("forward peak: narrow (small q range)", font=MONO, font_size=19,
                           color=TEAL).move_to(DOWN * 0.5)
        side_lbl = Text("theta = 90°: q = k*sqrt(2), form factor falls", font=MONO,
                        font_size=18, color=CRIMSON).move_to(DOWN * 1.3)
        highlight = Rectangle(width=9.0, height=0.65, stroke_width=0)
        highlight.set_fill(GOLD, opacity=0.28).move_to(DOWN * 0.5)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        self.play(FadeIn(param_group), run_time=dur * 0.30)
        self.play(FadeIn(highlight), FadeIn(forward_lbl), run_time=dur * 0.30)
        self.play(FadeIn(side_lbl), run_time=dur * 0.25)
        self.wait(dur * 0.15)


# ── B11: RECAP — CARD beat — no scene needed ─────────────────────────────────
class B03_WhatDataContains(Scene):
    def construct(self):
        d=DUR.get("B03",9); title=Text("ANGLE → q → FOURIER SAMPLE",font=DISPLAY,font_size=40,color=INK).to_edge(UP)
        amp=Text("amplitude: complex Ṽ(q)",font=MONO,font_size=30,color=TEAL).move_to(UP*.5)
        data=Text("detector: usually |f(q)|²",font=MONO,font_size=30,color=CRIMSON).move_to(DOWN*.6)
        self.play(FadeIn(title),FadeIn(amp),FadeIn(data),run_time=d*.45);self.wait(d*.55)

class B07_FiniteQCoverage(Scene):
    def construct(self):
        d=DUR.get("B07",12); title=Text("ONE ENERGY SAMPLES 0 ≤ q ≤ 2k",font=DISPLAY,font_size=37,color=INK).to_edge(UP)
        line=NumberLine(x_range=[0,10,2],length=9,color=INK,include_numbers=False).move_to(UP*.3)
        band=Line(line.n2p(0),line.n2p(10),color=TEAL,stroke_width=12)
        labels=VGroup(Text("forward q=0",font=SERIF,font_size=23,color=TEAL),Text("backward q=2k",font=SERIF,font_size=23,color=CRIMSON)).arrange(RIGHT,buff=4).move_to(DOWN*1.2)
        missing=Text("cross-section gives magnitude squared; phase is not automatic",font=SERIF,font_size=23,color=INK).move_to(DOWN*2.2)
        self.play(FadeIn(title),Create(line),Create(band),run_time=d*.35);self.play(FadeIn(labels),FadeIn(missing),run_time=d*.25);self.wait(d*.4)

class B09_InverseProblem(Scene):
    def construct(self):
        d=DUR.get("B09",12); title=Text("RECONSTRUCTION IS AN INVERSE PROBLEM",font=DISPLAY,font_size=34,color=INK).to_edge(UP)
        items=VGroup(Text("missing phase",font=SERIF,font_size=27,color=CRIMSON),Text("finite q coverage",font=SERIF,font_size=27,color=CRIMSON),Text("multiple scattering",font=SERIF,font_size=27,color=CRIMSON),Text("noise + model assumptions",font=SERIF,font_size=27,color=CRIMSON)).arrange_in_grid(rows=2,cols=2,buff=(1.6,.9))
        self.play(FadeIn(title),FadeIn(items),run_time=d*.45);self.wait(d*.55)

class B11_BornValidity(Scene):
    def construct(self):
        d=DUR.get("B11",12); title=Text("FIRST BORN: WEAK DISTORTION",font=DISPLAY,font_size=39,color=INK).to_edge(UP)
        yes=Text("WORKS BETTER\nweak potential\nhigher energy",font=SERIF,font_size=28,color=TEAL,line_spacing=1.1).move_to(LEFT*3)
        no=Text("CAN FAIL\nstrong potential\nlow energy · resonance",font=SERIF,font_size=28,color=CRIMSON,line_spacing=1.1).move_to(RIGHT*3)
        self.play(FadeIn(title),FadeIn(yes),FadeIn(no),run_time=d*.45);self.wait(d*.55)

class B12_QualifiedRecap(Scene):
    def construct(self):
        d=DUR.get("B12",11); title=Text("A PARTIAL FOURIER SAMPLER",font=DISPLAY,font_size=40,color=INK).to_edge(UP)
        chain=VGroup(Text("detector angle θ",font=SERIF,font_size=28,color=INK),Text("transfer q",font=SERIF,font_size=28,color=TEAL),Text("Ṽ(q)",font=MONO,font_size=34,color=CRIMSON)).arrange(RIGHT,buff=1.5)
        limits=Text("finite range · magnitude data · approximation error",font=SERIF,font_size=25,color=INK).move_to(DOWN*1.6)
        self.play(FadeIn(title),FadeIn(chain),run_time=d*.4);self.play(FadeIn(limits),run_time=d*.2);self.wait(d*.4)

class B13_YourTurn(Scene):
    def construct(self):
        d=DUR.get("B13",12); title=Text("YOUR TURN",font=DISPLAY,font_size=42,color=INK).to_edge(UP)
        eq=Text("q = 2k sin(θ/2)",font=MONO,font_size=38,color=INK).move_to(UP*.5)
        ans=Text("θ = 180°  →  q_max = 2k",font=MONO,font_size=36,color=TEAL).move_to(DOWN*.9)
        self.play(FadeIn(title),FadeIn(eq),run_time=d*.35);self.wait(d*.3);self.play(FadeIn(ans),run_time=d*.15);self.wait(d*.2)

class B14_CorrectTitleOutro(Scene):
    def construct(self):
        d=DUR.get("B14",8); bg=Rectangle(width=14.4,height=8.2,stroke_width=0).set_fill("#1E1D1A",1)
        title=Text("Scattering Is a Diffraction Experiment\non the Potential",font=DISPLAY,font_size=40,color="#F3EFE6",line_spacing=.9).move_to(UP*.45)
        by=Text("Liam, in for Bear",font=SERIF,font_size=25,color="#D97757").move_to(DOWN*1.05)
        series=Text("QUANTUM MECHANICS · VOLUME THREE",font=MONO,font_size=19,color="#B8B1A5").move_to(DOWN*1.65)
        self.add(bg);self.play(FadeIn(title),FadeIn(by),FadeIn(series),run_time=d*.35);self.wait(d*.65)
