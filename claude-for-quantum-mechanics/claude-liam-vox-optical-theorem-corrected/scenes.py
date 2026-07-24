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


# ── B01: COLD OPEN — hard sphere cross-section comparison ────────────────────
class OldHardSphereColdOpen(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        title = Text("Hard sphere, radius a", font=DISPLAY, font_size=28, color=INK).move_to(UP * 3.0)
        classical_lbl = Text("Classical:", font=DISPLAY, font_size=24, color=CRIMSON).move_to(LEFT * 3.5 + UP * 1.2)
        classical_val = Text("sigma = pi a^2", font=MONO, font_size=24, color=CRIMSON).move_to(LEFT * 3.5 + UP * 0.4)
        quantum_lbl = Text("Quantum:", font=DISPLAY, font_size=24, color=TEAL).move_to(RIGHT * 3.0 + UP * 1.2)
        quantum_val = Text("sigma = 4 pi a^2", font=MONO, font_size=24, color=TEAL).move_to(RIGHT * 3.0 + UP * 0.4)
        ratio_lbl = Text("4x larger at low energy", font=SERIF, font_size=22,
                         color=TEAL, slant=ITALIC).move_to(DOWN * 0.8)
        divider = Line(np.array([0.0, 2.5, 0.0]), np.array([0.0, -0.2, 0.0]),
                       color=INK, stroke_width=1.0)
        self.play(FadeIn(title), Create(divider), run_time=0.4)
        self.play(FadeIn(classical_lbl), FadeIn(classical_val), run_time=dur * 0.40)
        self.play(FadeIn(quantum_lbl), FadeIn(quantum_val), run_time=dur * 0.35)
        self.play(FadeIn(ratio_lbl), divider.animate.scale(0.95), run_time=dur * 0.25)


# ── B02: COLD OPEN — high-energy still 2πa² ──────────────────────────────────
class B02_HighEnergyCrossSection(Scene):
    def construct(self):
        dur = DUR.get("B02", 9.0)
        axes = Axes(x_range=[0, 8, 2], y_range=[0, 5, 1],
                    x_length=8.0, y_length=4.0,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    x_axis_config={"include_numbers": False},
                    y_axis_config={"include_numbers": False},
                    tips=False)
        axes.move_to(DOWN * 0.2)
        # sigma/pi*a^2 vs k*a; starts at 4, approaches 2
        sigma_curve = axes.plot(
            lambda x: 2 + 2 / (1 + 0.8 * x) + 0.4 * np.cos(2 * x) * np.exp(-0.3 * x),
            x_range=[0.2, 7.5], color=TEAL, stroke_width=3)
        classical_line = DashedLine(np.array([-4.0, 0.5, 0.0]), np.array([4.0, 0.5, 0.0]),
                                    color=CRIMSON, stroke_width=2, dash_length=0.2)
        asym_line = DashedLine(np.array([-4.0, 1.5, 0.0]), np.array([4.0, 1.5, 0.0]),
                               color=TEAL, stroke_width=1.5, dash_length=0.2)
        x_lbl = Text("k*a  (energy)", font=SERIF, font_size=17, color=INK,
                     slant=ITALIC).next_to(axes, DOWN + RIGHT * 2.5, buff=0.1)
        y_lbl = Text("sigma / (pi a^2)", font=SERIF, font_size=17, color=INK,
                     slant=ITALIC).next_to(axes, UP + LEFT * 2.0, buff=0.1)
        lbl4 = Text("4", font=MONO, font_size=18, color=TEAL).move_to(np.array([-4.3, 2.5, 0.0]))
        lbl2 = Text("2", font=MONO, font_size=18, color=TEAL).move_to(np.array([-4.3, 1.5, 0.0]))
        lbl1 = Text("1 (classical)", font=MONO, font_size=16, color=CRIMSON).move_to(np.array([-3.0, 0.8, 0.0]))
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)
        self.play(Create(sigma_curve), run_time=dur * 0.50)
        self.play(Create(classical_line), Create(asym_line), FadeIn(lbl4), FadeIn(lbl2),
                  FadeIn(lbl1), run_time=dur * 0.50)


# ── B03: CARD — THE QUESTION (no scene needed) ────────────────────────────────


# ── B04: THE PROBLEM — wave diffracts around sphere ──────────────────────────
class B04_WaveDiffraction(Scene):
    def construct(self):
        dur = DUR.get("B04", 10.0)
        title = Text("Quantum particle = wave that diffracts", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        # Sphere in center
        sphere = Circle(radius=0.7, stroke_width=3, color=INK)
        sphere.set_fill(SLATE, opacity=0.3).move_to(np.array([0.0, 0.0, 0.0]))
        sphere_lbl = Text("sphere", font=SERIF, font_size=17, color=INK,
                          slant=ITALIC).move_to(np.array([0.0, -1.15, 0.0]))
        # Incoming arrows
        inc_arrows = VGroup()
        for y in [-1.8, -0.9, 0.0, 0.9, 1.8]:
            a = Arrow(np.array([-5.5, y, 0.0]), np.array([-1.0, y, 0.0]),
                      buff=0.1, color=TEAL, stroke_width=1.5)
            inc_arrows.add(a)
        inc_lbl = Text("incoming wave", font=SERIF, font_size=17, color=TEAL,
                       slant=ITALIC).move_to(np.array([-4.2, 2.5, 0.0]))
        # Scattered arrows (multiple directions)
        scat_arrows = VGroup()
        for angle_deg in [30, 60, 90, 120, 150, 210, 240, 270, 300, 330]:
            angle = angle_deg * np.pi / 180
            start = np.array([0.8 * np.cos(angle), 0.8 * np.sin(angle), 0.0])
            end = np.array([2.2 * np.cos(angle), 2.2 * np.sin(angle), 0.0])
            a = Arrow(start, end, buff=0.0, color=TEAL, stroke_width=1.2)
            scat_arrows.add(a)
        scat_lbl = Text("wave scatters in all directions", font=SERIF,
                        font_size=18, color=TEAL, slant=ITALIC).move_to(DOWN * 2.7)
        self.play(FadeIn(title), FadeIn(sphere), FadeIn(sphere_lbl), run_time=0.4)
        self.play(Create(inc_arrows), FadeIn(inc_lbl), run_time=dur * 0.40)
        self.play(Create(scat_arrows), FadeIn(scat_lbl), run_time=dur * 0.60)


# ── B05: THE PROBLEM — s-wave isotropic, gives 4πa² ─────────────────────────
class B05_IsotropicSwave(Scene):
    def construct(self):
        dur = DUR.get("B05", 10.0)
        title = Text("Low energy: only s-wave (isotropic)", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        sphere = Circle(radius=0.8, stroke_width=2, color=INK)
        sphere.set_fill(SLATE, opacity=0.25).move_to(ORIGIN)
        # Concentric scattered circles in all directions
        rings = VGroup()
        for r in [1.3, 1.9, 2.5]:
            ring = Circle(radius=r, stroke_width=1.5, color=TEAL, stroke_opacity=0.6)
            ring.move_to(ORIGIN)
            rings.add(ring)
        scat_lbl = Text("scatters into all 4pi steradians", font=SERIF, font_size=18,
                        color=TEAL, slant=ITALIC).move_to(np.array([0.0, 2.2, 0.0]))
        result_lbl = Text("sigma = 4 pi a^2  (4x classical)", font=MONO,
                          font_size=22, color=TEAL).move_to(DOWN * 2.5)
        self.play(FadeIn(title), FadeIn(sphere), run_time=0.4)
        self.play(Create(rings), FadeIn(scat_lbl), run_time=dur * 0.55)
        self.play(FadeIn(result_lbl), rings.animate.set_stroke(opacity=0.85), run_time=dur * 0.45)


# ── B06: THE MECHANISM — shadow requires forward scattering ──────────────────
class B06_ShadowForward(Scene):
    def construct(self):
        dur = DUR.get("B06", 12.0)
        title = Text("To cast a shadow, you must scatter forward", font=DISPLAY,
                     font_size=22, color=INK).move_to(UP * 3.0)
        sphere = Circle(radius=0.7, stroke_width=2, color=INK)
        sphere.set_fill(SLATE, opacity=0.3).move_to(np.array([-1.0, 0.0, 0.0]))
        # Incoming beam
        beam_top = Arrow(np.array([-5.5, 0.5, 0.0]), np.array([-1.7, 0.5, 0.0]),
                         buff=0.0, color=TEAL, stroke_width=2)
        beam_bot = Arrow(np.array([-5.5, -0.5, 0.0]), np.array([-1.7, -0.5, 0.0]),
                         buff=0.0, color=TEAL, stroke_width=2)
        # Forward scattered wave (toward shadow zone)
        fwd_arrow = Arrow(np.array([-0.3, 0.0, 0.0]), np.array([3.5, 0.0, 0.0]),
                          buff=0.0, color=CRIMSON, stroke_width=2.5)
        fwd_lbl = Text("forward-scattered wave\n(creates shadow)", font=SERIF,
                       font_size=17, color=CRIMSON, slant=ITALIC).move_to(np.array([1.5, -1.6, 0.0]))
        shadow_region = Rectangle(width=2.5, height=1.4, stroke_width=0)
        shadow_region.set_fill(INK, opacity=0.15).move_to(np.array([4.5, 0.0, 0.0]))
        shadow_lbl = Text("shadow", font=SERIF, font_size=18, color=INK,
                          slant=ITALIC).move_to(np.array([4.5, 0.0, 0.0]))
        self.play(FadeIn(title), FadeIn(sphere), Create(beam_top), Create(beam_bot), run_time=0.4)
        self.play(FadeIn(shadow_region), FadeIn(shadow_lbl), run_time=dur * 0.35)
        self.play(Create(fwd_arrow), FadeIn(fwd_lbl), run_time=dur * 0.40)
        self.play(fwd_arrow.animate.set_stroke(width=3.5), run_time=dur * 0.25)


# ── B07: THE MECHANISM — forward wave contributes πa² ────────────────────────
class B07_TwoContributions(Scene):
    def construct(self):
        dur = DUR.get("B07", 11.0)
        title = Text("High energy: two contributions to sigma", font=DISPLAY,
                     font_size=22, color=INK).move_to(UP * 3.0)
        sideways = Text("sideways scattering:", font=DISPLAY, font_size=22,
                        color=TEAL).move_to(LEFT * 3.5 + UP * 1.2)
        sideways_val = Text("pi a^2", font=MONO, font_size=26, color=TEAL).move_to(LEFT * 3.5 + UP * 0.4)
        forward = Text("forward (shadow):", font=DISPLAY, font_size=22,
                       color=CRIMSON).move_to(RIGHT * 3.0 + UP * 1.2)
        forward_val = Text("pi a^2", font=MONO, font_size=26, color=CRIMSON).move_to(RIGHT * 3.0 + UP * 0.4)
        plus_lbl = Text("+", font=DISPLAY, font_size=36, color=INK).move_to(np.array([0.0, 0.4, 0.0]))
        total_lbl = Text("total: 2 pi a^2", font=MONO, font_size=28, color=TEAL).move_to(DOWN * 1.5)
        highlight = Rectangle(width=5.5, height=0.75, stroke_width=2, color=TEAL)
        highlight.set_fill(TEAL, opacity=0.08).move_to(DOWN * 1.5)
        self.play(FadeIn(title), FadeIn(plus_lbl), run_time=0.4)
        self.play(FadeIn(sideways), FadeIn(sideways_val), run_time=dur * 0.35)
        self.play(FadeIn(forward), FadeIn(forward_val), run_time=dur * 0.30)
        self.play(FadeIn(highlight), FadeIn(total_lbl), highlight.animate.scale(1.01), run_time=dur * 0.35)


# ── B08: THE IMPLICATION — optical theorem formula ───────────────────────────
class B08_OpticalTheorem(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)
        title = Text("The optical theorem", font=DISPLAY, font_size=32, color=INK).move_to(UP * 3.0)
        formula = Text("sigma_tot = (4*pi / k) * Im[ f(theta=0) ]",
                       font=MONO, font_size=22, color=TEAL).move_to(UP * 1.7)
        box = Rectangle(width=9.5, height=0.85, stroke_width=2, color=TEAL)
        box.set_fill(TEAL, opacity=0.08).move_to(UP * 1.7)
        f0_lbl = Text("f(0) : forward scattering amplitude", font=SERIF,
                      font_size=19, color=INK, slant=ITALIC).move_to(UP * 0.5)
        unitary_lbl = Text("flux conservation; forward elastic amplitude", font=SERIF,
                           font_size=18, color=INK, slant=ITALIC).move_to(DOWN * 0.3)
        universal_lbl = Text("even inelastic: absorption, reaction, anything", font=SERIF,
                             font_size=18, color=TEAL, slant=ITALIC).move_to(DOWN * 1.2)
        self.play(FadeIn(title), run_time=0.3)
        self.play(FadeIn(box), FadeIn(formula), run_time=dur * 0.30)
        self.play(FadeIn(f0_lbl), run_time=dur * 0.25)
        self.play(FadeIn(unitary_lbl), run_time=dur * 0.20)
        self.play(FadeIn(universal_lbl), box.animate.scale(1.01), run_time=dur * 0.25)


# ── B09: THE IMPLICATION — never smaller than geometric ──────────────────────
class OldUniversalShadowOverclaim(Scene):
    def construct(self):
        dur = DUR.get("B09", 10.0)
        title = Text("Quantum objects always exceed their geometric shadow", font=DISPLAY,
                     font_size=20, color=INK).move_to(UP * 3.0)
        rule = Text("sigma_tot >= pi a^2  always", font=MONO, font_size=26,
                    color=TEAL).move_to(UP * 1.5)
        reason = Text("Shadow = forward scattering = counted in sigma_tot", font=SERIF,
                      font_size=19, color=INK, slant=ITALIC).move_to(UP * 0.4)
        examples = [
            "nuclei: sigma_nuc >> pi R^2",
            "electrons: sigma_e >> pi a_Bohr^2",
            "light on atom: sigma > classical estimate",
        ]
        ex_group = VGroup()
        for i, ex in enumerate(examples):
            lbl = Text(ex, font=SERIF, font_size=18, color=TEAL,
                       slant=ITALIC).move_to(DOWN * (0.6 + i * 0.75))
            ex_group.add(lbl)
        bound_box = Rectangle(width=9.5, height=0.65, stroke_width=2, color=TEAL)
        bound_box.set_fill(TEAL, opacity=0.08).move_to(UP * 1.5)
        self.play(FadeIn(title), FadeIn(bound_box), FadeIn(rule), run_time=0.4)
        self.play(FadeIn(reason), bound_box.animate.scale(1.02), run_time=dur * 0.35)
        self.play(FadeIn(ex_group), run_time=dur * 0.65)


# ── B10: THE EXAMPLE — illustrative hard sphere numbers ──────────────────────
class B10_IllustrativeExample(Scene):
    def construct(self):
        dur = DUR.get("B10", 12.0)
        title = Text("Illustrative: hard sphere a = 2 angstroms", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        subtitle = Text("(labeled illustrative)", font=SERIF, font_size=17,
                        color=INK, slant=ITALIC).move_to(UP * 2.35)
        rows = [
            ("k*a = 0.1  (low E)", "sigma = 4 pi a^2", "~50 x 10^-20 m^2"),
            ("k*a = 10   (high E)", "sigma ~ 2 pi a^2", "~25 x 10^-20 m^2"),
            ("classical  (any E)", "sigma = pi a^2",   "~13 x 10^-20 m^2"),
        ]
        colors = [TEAL, TEAL, CRIMSON]
        group = VGroup()
        for i, (energy, formula, val) in enumerate(rows):
            y = 0.9 - i * 1.1
            e_lbl = Text(energy, font=SERIF, font_size=18, color=INK,
                         slant=ITALIC).move_to(LEFT * 3.8 + UP * y)
            f_lbl = Text(formula, font=MONO, font_size=18, color=colors[i]).move_to(LEFT * 0.2 + UP * y)
            v_lbl = Text(val, font=MONO, font_size=16, color=colors[i]).move_to(RIGHT * 3.5 + UP * y)
            group.add(e_lbl, f_lbl, v_lbl)
        highlight = Rectangle(width=12.0, height=0.65, stroke_width=0)
        highlight.set_fill(GOLD, opacity=0.25).move_to(UP * 0.9)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        self.play(FadeIn(highlight), FadeIn(group), run_time=dur * 0.55)
        self.wait(dur * 0.45)


# ── B11: RECAP — CARD beat — no scene needed ─────────────────────────────────
class B03_TwoDifferentLimits(Scene):
    def construct(self):
        d=DUR.get("B03",9); title=Text("TWO FACTORS · TWO REGIMES",font=DISPLAY,font_size=38,color=INK).to_edge(UP)
        low=Text("ka ≪ 1\n4πa²\none s wave",font=SERIF,font_size=29,color=TEAL,line_spacing=1.1).move_to(LEFT*3)
        high=Text("ka ≫ 1\n2πa²\nextinction",font=SERIF,font_size=29,color=CRIMSON,line_spacing=1.1).move_to(RIGHT*3)
        self.play(FadeIn(title),FadeIn(low),FadeIn(high),run_time=d*.45);self.wait(d*.55)

class B09_NotAUniversalBound(Scene):
    def construct(self):
        d=DUR.get("B09",12); title=Text("NOT A UNIVERSAL LOWER BOUND",font=DISPLAY,font_size=37,color=INK).to_edge(UP)
        hard=Text("HARD SPHERE\n2πa² high-energy limit",font=SERIF,font_size=27,color=TEAL,line_spacing=1.1).move_to(LEFT*3)
        transparent=Text("OTHER POTENTIALS\ntransparency minima can occur",font=SERIF,font_size=27,color=CRIMSON,line_spacing=1.1).move_to(RIGHT*3)
        note=Text("Long-range Coulomb scattering needs modified treatment.",font=SERIF,font_size=23,color=INK).move_to(DOWN*2.1)
        self.play(FadeIn(title),FadeIn(hard),FadeIn(transparent),run_time=d*.4);self.play(FadeIn(note),run_time=d*.15);self.wait(d*.45)

class B11_LimitAudit(Scene):
    def construct(self):
        d=DUR.get("B11",11); title=Text("SAME SPHERE · DIFFERENT WAVE CONTENT",font=DISPLAY,font_size=34,color=INK).to_edge(UP)
        rows=VGroup(Text("LOW ENERGY   one isotropic s wave   → 4πa²",font=MONO,font_size=28,color=TEAL),Text("HIGH ENERGY  many partial waves + diffraction → 2πa²",font=MONO,font_size=25,color=CRIMSON)).arrange(DOWN,buff=.9)
        self.play(FadeIn(title),FadeIn(rows),run_time=d*.45);self.wait(d*.55)

class B12_QualifiedRecap(Scene):
    def construct(self):
        d=DUR.get("B12",10); title=Text("HARD-SPHERE EXTINCTION",font=DISPLAY,font_size=40,color=INK).to_edge(UP)
        disk=Circle(radius=1.1,color=INK).set_fill(SLATE,.25).move_to(LEFT*3)
        low=Circle(radius=2.0,color=TEAL).set_fill(TEAL,.08).move_to(RIGHT*2.5)
        labels=VGroup(Text("geometric disk πa²",font=SERIF,font_size=24,color=INK),Text("wave cross-section\n4πa² → 2πa²",font=SERIF,font_size=24,color=TEAL)).arrange(RIGHT,buff=2.4).move_to(DOWN*2.3)
        self.play(FadeIn(title),FadeIn(disk),FadeIn(low),run_time=d*.4);self.play(FadeIn(labels),run_time=d*.2);self.wait(d*.4)

class B13_YourTurn(Scene):
    def construct(self):
        d=DUR.get("B13",12); title=Text("YOUR TURN · a → 2a",font=DISPLAY,font_size=42,color=INK).to_edge(UP)
        q=Text("σ_low = 4πa²     σ_high → 2πa²",font=MONO,font_size=32,color=INK).move_to(UP*.5)
        ans=Text("both cross-sections × 4",font=MONO,font_size=38,color=TEAL).move_to(DOWN*.9)
        self.play(FadeIn(title),FadeIn(q),run_time=d*.35);self.wait(d*.3);self.play(FadeIn(ans),run_time=d*.15);self.wait(d*.2)

class B14_CorrectTitleOutro(Scene):
    def construct(self):
        d=DUR.get("B14",8); bg=Rectangle(width=14.4,height=8.2,stroke_width=0).set_fill("#1E1D1A",1)
        title=Text("Why a Quantum Ball Casts\na Bigger Shadow Than Itself",font=DISPLAY,font_size=42,color="#F3EFE6",line_spacing=.9).move_to(UP*.45)
        by=Text("Kore, in for Humanitarians AI",font=SERIF,font_size=25,color="#D97757").move_to(DOWN*1.05)
        series=Text("QUANTUM MECHANICS · VOLUME THREE",font=MONO,font_size=19,color="#B8B1A5").move_to(DOWN*1.65)
        self.add(bg);self.play(FadeIn(title),FadeIn(by),FadeIn(series),run_time=d*.35);self.wait(d*.65)
