"""
Manim scenes for claude-liam-consistent-hashing ("Claude, Ringed.")
B01_BLUF            — the one-breath executive summary, text only
B02_Ring             — the hash space as a circle; servers hashed onto points
B03_KeyAssignment    — keys walk clockwise to their owning server
B04_AddNode          — adding a server only remaps the local arc
B05_VirtualNodes     — plain ring = uneven load; virtual nodes even it out
"""

from manim import *
import numpy as np

INK = "#3D3929"
BG = "#FAF9F5"
ACCENT = "#D97757"
BLUE = "#5B7B9C"
GREEN = "#4A7C59"
RED = "#C0392B"

config.background_color = BG


def ring_point(angle_deg, radius=1.9):
    a = np.radians(angle_deg)
    return radius * np.array([np.cos(a), np.sin(a), 0])


class B01_BLUF(Scene):
    def construct(self):
        l1 = Text("Hash your servers AND your keys onto one circle.",
                   font_size=40, color=INK)
        l2 = Text("A key belongs to whichever server comes next, clockwise.",
                   font_size=40, color=INK)
        l3 = Text("Add or remove a server — only its neighbors' keys move.",
                   font_size=36, color=ACCENT)
        for _l in (l1, l2, l3):
            if _l.width > 12.0:
                _l.scale_to_fit_width(12.0)
        l1.move_to(UP * 1.3)
        l2.move_to(UP * 0.1)
        l3.move_to(DOWN * 1.1)
        self.play(Write(l1), run_time=1.4)
        self.play(Write(l2), run_time=1.4)
        self.play(Write(l3), run_time=1.2)
        self.wait(1.2)


class B02_Ring(Scene):
    def construct(self):
        title = Text("The hash space is a circle", font_size=36, color=INK)
        title.to_edge(UP, buff=0.75)
        ring = Circle(radius=1.9, color=INK, stroke_width=3)
        self.play(Write(title), run_time=0.8)
        self.play(Create(ring), run_time=1.2)

        angles = [20, 100, 190, 300]
        labels = ["S1", "S2", "S3", "S4"]
        dots = VGroup()
        for ang, name in zip(angles, labels):
            p = ring_point(ang)
            dot = Dot(p, radius=0.12, color=BLUE)
            lbl = Text(name, font_size=28, color=BLUE).move_to(p * 1.22)
            dots.add(VGroup(dot, lbl))
        self.play(*[FadeIn(d, scale=0.5) for d in dots], run_time=1.2)
        cap = Text("Each server hashes onto a point on the ring.",
                    font_size=28, color=INK).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(cap), run_time=0.8)
        self.wait(1.4)


class B03_KeyAssignment(Scene):
    def construct(self):
        ring = Circle(radius=1.9, color=INK, stroke_width=3)
        self.add(ring)
        s_angles = [20, 100, 190, 300]
        s_labels = ["S1", "S2", "S3", "S4"]
        servers = VGroup()
        for ang, name in zip(s_angles, s_labels):
            p = ring_point(ang)
            dot = Dot(p, radius=0.12, color=BLUE)
            lbl = Text(name, font_size=26, color=BLUE).move_to(p * 1.22)
            servers.add(VGroup(dot, lbl))
        self.add(servers)

        title = Text("A key walks clockwise to its owner", font_size=32, color=INK)
        title.to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.8)

        key_angles = [5, 70, 160, 250]
        owners = [20, 100, 190, 300]  # next clockwise server angle for each key
        for k_ang, o_ang in zip(key_angles, owners):
            kp = ring_point(k_ang, radius=1.9)
            key_dot = Dot(kp, radius=0.09, color=ACCENT)
            self.play(FadeIn(key_dot, scale=0.5), run_time=0.35)
            arc = Arc(radius=1.9, start_angle=np.radians(k_ang),
                      angle=np.radians((o_ang - k_ang) % 360),
                      color=ACCENT, stroke_width=5)
            self.play(Create(arc), run_time=0.5)
            self.wait(0.15)

        cap = Text("No modulo — just 'which server point is next.'",
                    font_size=26, color=INK).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(cap), run_time=0.7)
        self.wait(1.2)


class B04_AddNode(Scene):
    def construct(self):
        ring = Circle(radius=1.9, color=INK, stroke_width=3)
        self.add(ring)
        s_angles = [20, 100, 190, 300]
        s_labels = ["S1", "S2", "S3", "S4"]
        servers = VGroup()
        for ang, name in zip(s_angles, s_labels):
            p = ring_point(ang)
            dot = Dot(p, radius=0.12, color=BLUE)
            lbl = Text(name, font_size=26, color=BLUE).move_to(p * 1.22)
            servers.add(VGroup(dot, lbl))
        self.add(servers)

        title = Text("Add a 5th server", font_size=32, color=INK).to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.8)

        new_ang = 60
        new_p = ring_point(new_ang)
        new_dot = Dot(new_p, radius=0.14, color=GREEN)
        new_lbl = Text("S5", font_size=26, color=GREEN).move_to(new_p * 1.22)
        self.play(FadeIn(VGroup(new_dot, new_lbl), scale=0.5), run_time=0.8)

        # only the arc between S5 and its counter-clockwise neighbor (S1 at 20deg) remaps
        remap_arc = Arc(radius=1.9, start_angle=np.radians(20), angle=np.radians(40),
                         color=GREEN, stroke_width=8)
        self.play(Create(remap_arc), run_time=1.0)
        remap_cap = Text("Only this arc's keys move to S5.", font_size=26, color=GREEN)
        remap_cap.move_to(DOWN * 2.3)
        self.play(FadeIn(remap_cap), run_time=0.6)

        other_cap = Text("S2, S3, S4 keep every key they had.", font_size=26, color=INK)
        other_cap.move_to(DOWN * 3.05)
        self.play(FadeIn(other_cap), run_time=0.7)
        self.wait(1.4)


class B05_VirtualNodes(Scene):
    def construct(self):
        title = Text("Few servers = uneven arcs", font_size=32, color=INK).to_edge(UP, buff=0.75)
        ring1 = Circle(radius=1.9, color=INK, stroke_width=3).shift(LEFT * 3.3)
        self.play(Write(title), run_time=0.7)
        self.play(Create(ring1), run_time=1.0)

        angs = [10, 40, 220]  # deliberately uneven
        for ang in angs:
            p = ring_point(ang, radius=1.9) + LEFT * 3.3
            self.add(Dot(p, radius=0.11, color=RED))
        arcs1 = [(10, 30), (40, 180), (220, 150)]
        for start, span in arcs1:
            a = Arc(radius=1.9, start_angle=np.radians(start), angle=np.radians(span),
                    color=RED, stroke_width=6).shift(LEFT * 3.3)
            self.play(Create(a), run_time=0.4)
        cap1 = Text("one server owns most of the ring", font_size=22, color=RED)
        cap1.next_to(ring1, DOWN, buff=0.3)
        self.play(FadeIn(cap1), run_time=0.6)

        title2 = Text("Virtual nodes even it out", font_size=32, color=INK)
        ring2 = Circle(radius=1.9, color=INK, stroke_width=3).shift(RIGHT * 3.3)
        self.play(Create(ring2), run_time=1.0)
        vangs = [10, 40, 90, 130, 175, 220, 260, 300, 340]
        colors_cycle = [RED, BLUE, GREEN] * 3
        for ang, col in zip(vangs, colors_cycle):
            p = ring_point(ang, radius=1.9) + RIGHT * 3.3
            self.add(Dot(p, radius=0.08, color=col))
        cap2 = Text("each server owns many small arcs", font_size=22, color=GREEN)
        cap2.next_to(ring2, DOWN, buff=0.3)
        self.play(FadeIn(cap2), run_time=0.6)
        self.wait(1.6)
