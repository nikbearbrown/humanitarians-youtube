from manim import *
import numpy as np

config.background_color = "#FAF9F5"
INK = "#3D3929"
ACCENT = "#D97757"
BLUE = "#5E7D7A"

def get_photon(start, end, frequency=1, color=INK, amplitude=0.2):
    path = Line(start, end)
    photon = FunctionGraph(
        lambda t: amplitude * np.sin(2 * PI * frequency * t),
        x_range=[0, path.get_length()],
        color=color
    )
    angle = path.get_angle()
    photon.rotate(angle).shift(start)
    return photon

class B02_PhotonCollision(Scene):
    def construct(self):
        # Molecule
        molecule = Circle(radius=0.5, color=INK).set_fill(INK, opacity=0.2)
        molecule.move_to(ORIGIN)
        
        label = Text("Molecule", color=INK, font_size=24).next_to(molecule, DOWN)
        self.play(FadeIn(molecule), FadeIn(label))
        
        # 1. Rayleigh (Elastic) - same frequency
        title = Text("Elastic Scattering (Rayleigh)", color=INK, font_size=32).to_edge(UP)
        self.play(Write(title))
        
        p_in = get_photon(LEFT*5, molecule.get_left(), frequency=2, color=INK)
        self.play(Create(p_in), run_time=1.5)
        
        # Vibrate molecule a bit
        self.play(molecule.animate.scale(1.1), run_time=0.1)
        self.play(molecule.animate.scale(1/1.1), run_time=0.1)
        
        p_out = get_photon(molecule.get_right(), RIGHT*5 + UP*2, frequency=2, color=INK)
        self.play(FadeOut(p_in), Create(p_out), run_time=1.5)
        self.play(FadeOut(p_out), FadeOut(title))
        
        # 2. Stokes (Inelastic) - lower frequency (longer wavelength), molecule vibrates more
        title2 = Text("Inelastic Scattering (Stokes Raman)", color=ACCENT, font_size=32).to_edge(UP)
        self.play(Write(title2))
        
        p_in2 = get_photon(LEFT*5, molecule.get_left(), frequency=2, color=INK)
        self.play(Create(p_in2), run_time=1.5)
        
        # Vibrate molecule more
        self.play(molecule.animate.scale(1.2).set_color(ACCENT), run_time=0.15)
        self.play(molecule.animate.scale(1/1.2), run_time=0.15)
        self.play(molecule.animate.scale(1.1), run_time=0.1)
        self.play(molecule.animate.scale(1/1.1), run_time=0.1)
        
        # Output is lower frequency
        p_out2 = get_photon(molecule.get_right(), RIGHT*5 + DOWN*2, frequency=1, color=ACCENT)
        self.play(FadeOut(p_in2), Create(p_out2), run_time=1.5)
        self.play(FadeOut(p_out2), FadeOut(title2))
        
        # 3. Anti-Stokes (Inelastic) - higher frequency, molecule calms down
        title3 = Text("Inelastic Scattering (Anti-Stokes)", color=BLUE, font_size=32).to_edge(UP)
        self.play(Write(title3))
        
        p_in3 = get_photon(LEFT*5, molecule.get_left(), frequency=2, color=INK)
        self.play(Create(p_in3), run_time=1.5)
        
        # Vibrate molecule back to normal
        self.play(molecule.animate.scale(1.1).set_color(INK), run_time=0.1)
        self.play(molecule.animate.scale(1/1.1), run_time=0.1)
        
        # Output is higher frequency
        p_out3 = get_photon(molecule.get_right(), RIGHT*5, frequency=4, color=BLUE)
        self.play(FadeOut(p_in3), Create(p_out3), run_time=1.5)
        
        self.play(FadeOut(Group(molecule, label, title3, p_out3)))

