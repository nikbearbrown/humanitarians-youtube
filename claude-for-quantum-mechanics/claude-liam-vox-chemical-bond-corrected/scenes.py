import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass


# ── B01: COLD OPEN — plus combination builds bond ────────────────────────────
class OldColdOpenBondingOrbitals(Scene):
    def construct(self):
        dur = DUR.get("B01", 8.0)
        # Two protons as dots
        p_left = Dot(radius=0.22, color=INK).move_to(LEFT * 2.8)
        p_right = Dot(radius=0.22, color=INK).move_to(RIGHT * 2.8)
        p_left_lbl = Text("p+", font=MONO, font_size=22, color=INK).move_to(LEFT * 2.8 + DOWN * 0.55)
        p_right_lbl = Text("p+", font=MONO, font_size=22, color=INK).move_to(RIGHT * 2.8 + DOWN * 0.55)
        # Orbital lobes (circles representing 1s orbitals)
        orb_left = Circle(radius=1.1, color=TEAL, stroke_width=2.5).move_to(LEFT * 2.0)
        orb_left.set_fill(TEAL, opacity=0.18)
        orb_right = Circle(radius=1.1, color=TEAL, stroke_width=2.5).move_to(RIGHT * 2.0)
        orb_right.set_fill(TEAL, opacity=0.18)
        # Merged bonding cloud in center
        bond_cloud = Ellipse(width=4.2, height=1.6, color=TEAL, stroke_width=0)
        bond_cloud.set_fill(TEAL, opacity=0.45).move_to(ORIGIN)
        plus_lbl = Text("psi_A + psi_B", font=MONO, font_size=24, color=TEAL).move_to(UP * 2.8)
        bond_lbl = Text("density between nuclei", font=SERIF, font_size=22, color=TEAL,
                        slant=ITALIC).move_to(DOWN * 1.5)
        self.play(FadeIn(p_left), FadeIn(p_right),
                  FadeIn(p_left_lbl), FadeIn(p_right_lbl), run_time=0.4)
        self.play(Create(orb_left), Create(orb_right), run_time=dur * 0.30)
        self.play(FadeIn(plus_lbl), run_time=dur * 0.15)
        self.play(Transform(orb_left, bond_cloud), Transform(orb_right, bond_cloud),
                  run_time=dur * 0.35)
        self.play(FadeIn(bond_lbl), run_time=dur * 0.20)


# ── B02: COLD OPEN — minus combination: node, no bond ────────────────────────
class B02_H2PlusSetup(Scene):
    def construct(self):
        dur = DUR.get("B02", 8.0)
        p_left = Dot(radius=0.22, color=INK).move_to(LEFT * 2.8)
        p_right = Dot(radius=0.22, color=INK).move_to(RIGHT * 2.8)
        # Two lobes with opposite phase (one TEAL +, one CRIMSON -)
        lobe_plus = Circle(radius=1.1, color=TEAL, stroke_width=2.5).move_to(LEFT * 2.0)
        lobe_plus.set_fill(TEAL, opacity=0.20)
        lobe_minus = Circle(radius=1.1, color=CRIMSON, stroke_width=2.5).move_to(RIGHT * 2.0)
        lobe_minus.set_fill(CRIMSON, opacity=0.20)
        minus_lbl = Text("psi_A - psi_B", font=MONO, font_size=24, color=CRIMSON).move_to(UP * 2.8)
        # Node plane in center
        node_line = DashedLine(UP * 2.0, DOWN * 2.0, color=CRIMSON, stroke_width=3,
                               dash_length=0.2).move_to(ORIGIN)
        node_lbl = Text("NODE", font=DISPLAY, font_size=28, color=CRIMSON).move_to(RIGHT * 1.5 + UP * 0.0)
        no_bond_lbl = Text("nodal plane", font=SERIF, font_size=22, color=CRIMSON,
                           slant=ITALIC).move_to(LEFT * 3.5 + DOWN * 1.5)
        self.play(FadeIn(p_left), FadeIn(p_right), run_time=0.4)
        self.play(Create(lobe_plus), Create(lobe_minus), run_time=dur * 0.30)
        self.play(FadeIn(minus_lbl), run_time=dur * 0.15)
        self.play(Create(node_line), FadeIn(node_lbl), run_time=dur * 0.30)
        self.play(FadeIn(no_bond_lbl), run_time=dur * 0.25)


# ── B03: THE QUESTION — CARD beat — no scene needed ──────────────────────────


# ── B04: THE PROBLEM — classical expectation ─────────────────────────────────
class B04_ClassicalExpectation(Scene):
    def construct(self):
        dur = DUR.get("B04", 9.0)
        # Electron as a dot between two protons, arrows pulling protons inward
        proton_l = Dot(radius=0.22, color=INK).move_to(LEFT * 3.0)
        proton_r = Dot(radius=0.22, color=INK).move_to(RIGHT * 3.0)
        electron = Dot(radius=0.18, color=TEAL).move_to(ORIGIN)
        e_lbl = Text("e-", font=MONO, font_size=22, color=TEAL).move_to(UP * 0.45)
        arrow_l = Arrow(start=LEFT * 3.0, end=LEFT * 1.5, color=TEAL,
                        stroke_width=3, buff=0.25)
        arrow_r = Arrow(start=RIGHT * 3.0, end=RIGHT * 1.5, color=TEAL,
                        stroke_width=3, buff=0.25)
        classical_lbl = Text("Classical: electron always pulls protons together",
                             font=SERIF, font_size=20, color=INK,
                             slant=ITALIC).move_to(DOWN * 2.0)
        question_lbl = Text("Then why does the sign matter?", font=DISPLAY,
                            font_size=24, color=CRIMSON).move_to(DOWN * 2.9)
        self.play(FadeIn(proton_l), FadeIn(proton_r), run_time=0.4)
        self.play(Create(electron), FadeIn(e_lbl), run_time=dur * 0.25)
        self.play(GrowArrow(arrow_l), GrowArrow(arrow_r), run_time=dur * 0.30)
        self.play(FadeIn(classical_lbl), run_time=dur * 0.20)
        self.play(FadeIn(question_lbl), run_time=dur * 0.25)


# ── B06: THE MECHANISM — constructive interference ───────────────────────────
class B06_ConstructiveInterference(Scene):
    def construct(self):
        dur = DUR.get("B06", 10.0)
        # Two Gaussian-like bumps adding to give a big central peak
        axes = Axes(x_range=[-5, 5, 1], y_range=[-0.2, 1.5, 0.5],
                    x_length=9.0, y_length=4.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(DOWN * 0.3)
        psi_a = axes.plot(lambda x: np.exp(-((x + 2) ** 2) / 1.5),
                          color=SLATE, stroke_width=2.5)
        psi_b = axes.plot(lambda x: np.exp(-((x - 2) ** 2) / 1.5),
                          color=SLATE, stroke_width=2.5)
        psi_plus = axes.plot(
            lambda x: 0.7 * (np.exp(-((x + 2) ** 2) / 1.5) + np.exp(-((x - 2) ** 2) / 1.5)),
            color=TEAL, stroke_width=3.5)
        lbl_a = Text("psi_A", font=MONO, font_size=20, color=SLATE).move_to(np.array([-4.0, 1.8, 0.0]))
        lbl_b = Text("psi_B", font=MONO, font_size=20, color=SLATE).move_to(np.array([4.0, 1.8, 0.0]))
        plus_sum_lbl = Text("psi_A + psi_B", font=MONO, font_size=22, color=TEAL).move_to(
            np.array([0.0, 3.2, 0.0]))
        peak_arrow = Arrow(start=np.array([0.0, 2.8, 0.0]), end=np.array([0.0, 1.5, 0.0]),
                           color=TEAL, stroke_width=2.5, buff=0.1)
        peak_lbl = Text("peaks between nuclei", font=SERIF, font_size=20, color=TEAL,
                        slant=ITALIC).move_to(np.array([2.5, 3.0, 0.0]))
        self.play(Create(axes), run_time=0.4)
        self.play(Create(psi_a), Create(psi_b), FadeIn(lbl_a), FadeIn(lbl_b),
                  run_time=dur * 0.35)
        self.play(Create(psi_plus), FadeIn(plus_sum_lbl), run_time=dur * 0.35)
        self.play(GrowArrow(peak_arrow), FadeIn(peak_lbl), run_time=dur * 0.30)


# ── B07: THE MECHANISM — midplane density pulls both protons ─────────────────
class B07_MidplaneDensity(Scene):
    def construct(self):
        dur = DUR.get("B07", 10.0)
        proton_l = Dot(radius=0.25, color=INK).move_to(LEFT * 3.2)
        proton_r = Dot(radius=0.25, color=INK).move_to(RIGHT * 3.2)
        p_lbl_l = Text("p+", font=MONO, font_size=22, color=INK).move_to(LEFT * 3.2 + DOWN * 0.55)
        p_lbl_r = Text("p+", font=MONO, font_size=22, color=INK).move_to(RIGHT * 3.2 + DOWN * 0.55)
        # Central density blob
        density = Ellipse(width=3.2, height=1.4, stroke_width=0)
        density.set_fill(TEAL, opacity=0.55).move_to(ORIGIN)
        density_lbl = Text("electron density", font=SERIF, font_size=22, color=TEAL,
                           slant=ITALIC).move_to(UP * 1.5)
        # Arrows from protons toward center (pulled by density)
        pull_l = Arrow(start=LEFT * 3.2, end=LEFT * 1.0, color=TEAL,
                       stroke_width=3, buff=0.25)
        pull_r = Arrow(start=RIGHT * 3.2, end=RIGHT * 1.0, color=TEAL,
                       stroke_width=3, buff=0.25)
        bond_lbl = Text("stabilizing density", font=DISPLAY, font_size=26, color=TEAL).move_to(DOWN * 2.2)
        self.play(FadeIn(proton_l), FadeIn(proton_r),
                  FadeIn(p_lbl_l), FadeIn(p_lbl_r), run_time=0.4)
        self.play(FadeIn(density), FadeIn(density_lbl), run_time=dur * 0.30)
        self.play(GrowArrow(pull_l), GrowArrow(pull_r), run_time=dur * 0.35)
        self.play(FadeIn(bond_lbl), density.animate.scale(1.05), run_time=dur * 0.35)


# ── B08: THE MECHANISM — destructive interference → node ─────────────────────
class B08_DestructiveNode(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)
        axes = Axes(x_range=[-5, 5, 1], y_range=[-1.1, 1.1, 0.5],
                    x_length=9.0, y_length=4.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(DOWN * 0.3)
        psi_a = axes.plot(lambda x: np.exp(-((x + 2) ** 2) / 1.5),
                          color=SLATE, stroke_width=2.0)
        neg_psi_b = axes.plot(lambda x: -np.exp(-((x - 2) ** 2) / 1.5),
                              color=CRIMSON, stroke_width=2.0)
        psi_minus = axes.plot(
            lambda x: 0.7 * (np.exp(-((x + 2) ** 2) / 1.5) - np.exp(-((x - 2) ** 2) / 1.5)),
            color=CRIMSON, stroke_width=3.5)
        node_dot = Dot(np.array([0.0, -0.3 + 0.3, 0.0]), radius=0.14, color=CRIMSON)
        node_dot.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        node_lbl = Text("NODE (zero density)", font=DISPLAY, font_size=22, color=CRIMSON)
        node_lbl.move_to(np.array([2.5, 0.9, 0.0]))
        minus_sum_lbl = Text("psi_A - psi_B", font=MONO, font_size=22, color=CRIMSON).move_to(
            np.array([-3.0, 3.0, 0.0]))
        self.play(Create(axes), run_time=0.4)
        self.play(Create(psi_a), Create(neg_psi_b), run_time=dur * 0.30)
        self.play(Create(psi_minus), FadeIn(minus_sum_lbl), run_time=dur * 0.35)
        self.play(FadeIn(node_dot), FadeIn(node_lbl), run_time=dur * 0.35)


# ── B09: THE MECHANISM — node means repulsion ────────────────────────────────
class B09_NodeRepulsion(Scene):
    def construct(self):
        dur = DUR.get("B09", 11.0)
        proton_l = Dot(radius=0.25, color=INK).move_to(LEFT * 3.0)
        proton_r = Dot(radius=0.25, color=INK).move_to(RIGHT * 3.0)
        # Empty midplane — node marker
        node_line = DashedLine(UP * 1.8, DOWN * 1.8, color=CRIMSON,
                               stroke_width=3, dash_length=0.2).move_to(ORIGIN)
        node_lbl = Text("node", font=DISPLAY, font_size=26, color=CRIMSON).move_to(
            RIGHT * 1.4 + UP * 2.2)
        # Density pushed outward
        density_l = Ellipse(width=1.6, height=1.2, stroke_width=0)
        density_l.set_fill(CRIMSON, opacity=0.30).move_to(LEFT * 4.2)
        density_r = Ellipse(width=1.6, height=1.2, stroke_width=0)
        density_r.set_fill(CRIMSON, opacity=0.30).move_to(RIGHT * 4.2)
        # Repulsion arrows pointing outward
        rep_l = Arrow(start=LEFT * 3.0, end=LEFT * 4.5, color=CRIMSON,
                      stroke_width=3, buff=0.25)
        rep_r = Arrow(start=RIGHT * 3.0, end=RIGHT * 4.5, color=CRIMSON,
                      stroke_width=3, buff=0.25)
        no_bond_lbl = Text("no binding minimum", font=DISPLAY, font_size=28, color=CRIMSON).move_to(DOWN * 2.5)
        self.play(FadeIn(proton_l), FadeIn(proton_r), run_time=0.4)
        self.play(Create(node_line), FadeIn(node_lbl), run_time=dur * 0.25)
        self.play(FadeIn(density_l), FadeIn(density_r), run_time=dur * 0.25)
        self.play(GrowArrow(rep_l), GrowArrow(rep_r), run_time=dur * 0.30)
        self.play(FadeIn(no_bond_lbl), node_line.animate.scale(0.95), run_time=dur * 0.20)


# ── B10: THE IMPLICATION — every covalent bond ───────────────────────────────
class OldCovalentBondOverstatement(Scene):
    def construct(self):
        dur = DUR.get("B10", 10.0)
        # Two-panel: bond (TEAL) vs antibond (CRIMSON)
        bond_box = Rectangle(width=4.8, height=3.0, stroke_width=0)
        bond_box.set_fill(TEAL, opacity=0.12).move_to(LEFT * 2.8)
        antibond_box = Rectangle(width=4.8, height=3.0, stroke_width=0)
        antibond_box.set_fill(CRIMSON, opacity=0.12).move_to(RIGHT * 2.8)
        bond_title = Text("Bonding", font=DISPLAY, font_size=28, color=TEAL).move_to(
            LEFT * 2.8 + UP * 1.0)
        antibond_title = Text("Antibonding", font=DISPLAY, font_size=28, color=CRIMSON).move_to(
            RIGHT * 2.8 + UP * 1.0)
        bond_desc = Text("+ interference\ndensity between nuclei\nCoulomb attraction",
                         font=SERIF, font_size=18, color=TEAL, slant=ITALIC).move_to(
            LEFT * 2.8 + DOWN * 0.2)
        antibond_desc = Text("- interference\nnode between nuclei\nno glue",
                             font=SERIF, font_size=18, color=CRIMSON, slant=ITALIC).move_to(
            RIGHT * 2.8 + DOWN * 0.2)
        every_lbl = Text("Every covalent bond", font=DISPLAY, font_size=24, color=INK).move_to(
            DOWN * 2.5)
        self.play(FadeIn(bond_box), FadeIn(antibond_box), run_time=0.4)
        self.play(FadeIn(bond_title), FadeIn(antibond_title), run_time=dur * 0.25)
        self.play(FadeIn(bond_desc), FadeIn(antibond_desc), run_time=dur * 0.35)
        self.play(FadeIn(every_lbl), bond_box.animate.scale(1.02), run_time=dur * 0.40)


# ── B11: THE EXAMPLE — illustrative H2+ numbers ──────────────────────────────
class B11_IllustrativeExample(Scene):
    def construct(self):
        dur = DUR.get("B11", 12.0)
        title = Text("Illustrative: H2+ (hydrogen molecule ion)", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        subtitle = Text("Born-Oppenheimer H2+ calculation", font=SERIF,
                        font_size=18, color=INK, slant=ITALIC).move_to(UP * 2.45)
        # Simple energy vs bond-length sketch (two curves)
        axes = Axes(x_range=[0.5, 5.0, 1.0], y_range=[-2.5, 2.0, 1.0],
                    x_length=7.5, y_length=3.8,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(DOWN * 0.3)
        bonding_curve = axes.plot(
            lambda r: -1.8 * np.exp(-((r - 1.3) ** 2) / 0.4) + 0.2 * (1 - np.exp(-(r - 0.5))) - 0.3,
            x_range=[0.6, 4.8], color=TEAL, stroke_width=3)
        antibond_curve = axes.plot(
            lambda r: 1.5 * np.exp(-((r - 0.8) ** 2) / 1.5) + 0.5,
            x_range=[0.6, 4.8], color=CRIMSON, stroke_width=3)
        bond_lbl = Text("bonding: minimum ~1.3 A", font=SERIF, font_size=18, color=TEAL,
                        slant=ITALIC).move_to(np.array([2.8, -2.0, 0.0]))
        anti_lbl = Text("antibonding: no minimum", font=SERIF, font_size=18, color=CRIMSON,
                        slant=ITALIC).move_to(np.array([2.8, 1.5, 0.0]))
        x_lbl = Text("bond length", font=SERIF, font_size=18, color=INK,
                     slant=ITALIC).next_to(axes, RIGHT, buff=0.1)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        self.play(Create(axes), FadeIn(x_lbl), run_time=dur * 0.20)
        self.play(Create(bonding_curve), FadeIn(bond_lbl), run_time=dur * 0.35)
        self.play(Create(antibond_curve), FadeIn(anti_lbl), run_time=dur * 0.35)
        self.wait(dur * 0.10)


# ── Corrected explanatory beats ──────────────────────────────────────────────
class B03_EnergyQuestion(Scene):
    def construct(self):
        dur = DUR.get("B03", 9)
        title = Text("SAME PARTICLES. DIFFERENT ENERGY.", font=DISPLAY, font_size=34, color=INK).to_edge(UP)
        plus = Text("1sA + 1sB", font=MONO, font_size=42, color=TEAL).move_to(LEFT*3)
        minus = Text("1sA - 1sB", font=MONO, font_size=42, color=CRIMSON).move_to(RIGHT*3)
        q = Text("Which curve develops a minimum?", font=SERIF, font_size=30, color=INK).move_to(DOWN*1.8)
        self.play(FadeIn(title), FadeIn(plus), FadeIn(minus), run_time=dur*.35)
        self.play(FadeIn(q), run_time=dur*.25); self.wait(dur*.4)

class B05_TwoTrialShapes(Scene):
    def construct(self):
        dur = DUR.get("B05", 10)
        title = Text("TWO TRIAL SHAPES", font=DISPLAY, font_size=34, color=INK).to_edge(UP)
        a = Circle(radius=1.35, color=TEAL).set_fill(TEAL,.22).move_to(LEFT*2)
        b = Circle(radius=1.35, color=TEAL).set_fill(TEAL,.22).move_to(RIGHT*2)
        labels = VGroup(Text("SUM", font=DISPLAY, font_size=28, color=TEAL), Text("DIFFERENCE", font=DISPLAY, font_size=28, color=CRIMSON)).arrange(RIGHT,buff=3).move_to(DOWN*2)
        self.play(FadeIn(title), Create(a), Create(b), run_time=dur*.4)
        self.play(FadeIn(labels), run_time=dur*.25); self.wait(dur*.35)

class B10_TotalEnergyMinimum(Scene):
    def construct(self):
        dur = DUR.get("B10", 11)
        axes = Axes(x_range=[.5,5,1], y_range=[-2,3,1], x_length=8, y_length=4.5, tips=False, axis_config={"color":INK}).shift(DOWN*.2)
        curve = axes.plot(lambda r: 2.6/(r**2)-3.2*np.exp(-.75*r), x_range=[.65,4.8], color=TEAL, stroke_width=4)
        title = Text("A BOND REQUIRES A TOTAL-ENERGY MINIMUM", font=DISPLAY, font_size=30, color=INK).to_edge(UP)
        lbl = Text("equilibrium", font=SERIF, font_size=23, color=TEAL).move_to(DOWN*1.6+LEFT*.8)
        self.play(FadeIn(title), Create(axes), run_time=dur*.25)
        self.play(Create(curve), run_time=dur*.4); self.play(FadeIn(lbl), run_time=dur*.15); self.wait(dur*.2)

class B12_QualifiedRecap(Scene):
    def construct(self):
        dur = DUR.get("B12", 11)
        title = Text("THE H2+ LESSON", font=DISPLAY, font_size=36, color=INK).to_edge(UP)
        left = Text("constructive overlap\nmore internuclear density\ncan lower energy", font=SERIF, font_size=28, color=TEAL, line_spacing=1.2).move_to(LEFT*3)
        right = Text("destructive overlap\nmidplane node\nhigher energy", font=SERIF, font_size=28, color=CRIMSON, line_spacing=1.2).move_to(RIGHT*3)
        self.play(FadeIn(title), FadeIn(left), FadeIn(right), run_time=dur*.45); self.wait(dur*.55)

class B13_YourTurn(Scene):
    def construct(self):
        dur = DUR.get("B13", 12)
        title = Text("YOUR TURN", font=DISPLAY, font_size=42, color=INK).to_edge(UP)
        task = Text("Sketch 1sA + 1sB and 1sA - 1sB\nMark the node. Predict the energy minimum.", font=SERIF, font_size=30, color=INK, line_spacing=1.25).move_to(UP*.4)
        pause = Text("PAUSE BEFORE THE ANSWER", font=MONO, font_size=25, color=CRIMSON).move_to(DOWN*2)
        self.play(FadeIn(title), FadeIn(task), run_time=dur*.35); self.play(FadeIn(pause), run_time=dur*.15); self.wait(dur*.5)

class B14_CorrectTitleOutro(Scene):
    def construct(self):
        dur = DUR.get("B14", 8)
        bg = Rectangle(width=14.4, height=8.2, stroke_width=0).set_fill("#1E1D1A", 1)
        title = Text("Where a Chemical Bond Actually\nComes From", font=DISPLAY, font_size=42, color="#F3EFE6", line_spacing=.9).move_to(UP*.45)
        byline = Text("Kore, in for Humanitarians AI", font=SERIF, font_size=25, color="#D97757").move_to(DOWN*1.05)
        series = Text("QUANTUM MECHANICS · VOLUME THREE", font=MONO, font_size=19, color="#B8B1A5").move_to(DOWN*1.65)
        self.add(bg); self.play(FadeIn(title), FadeIn(byline), FadeIn(series), run_time=dur*.35); self.wait(dur*.65)
