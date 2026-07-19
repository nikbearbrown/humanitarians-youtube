"""scenes.py — Manim for browser-coordinate-scaling. Source: Claude Quickstarts (Anthropic)"""
from manim import *

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_TwoSpaces(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Two Spaces", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Left viewport — Claude sees this (smaller)
        left_rect = Rectangle(width=2.8, height=1.8, color=SOFT, stroke_width=2)
        left_rect.move_to([-3.0, -0.3, 0])
        left_label = Text("1456x819", font_size=14, color=SOFT)
        left_label.next_to(left_rect, UP, buff=0.15)
        left_sub = Text("Claude sees this", font_size=12, color=SOFT)
        left_sub.next_to(left_label, UP, buff=0.05)

        # Right viewport — Desktop (larger)
        right_rect = Rectangle(width=3.8, height=2.4, color=INK, stroke_width=2)
        right_rect.move_to([3.0, -0.3, 0])
        right_label = Text("1920x1080", font_size=14, color=INK)
        right_label.next_to(right_rect, UP, buff=0.15)
        right_sub = Text("Desktop", font_size=12, color=INK)
        right_sub.next_to(right_label, UP, buff=0.05)

        self.play(Create(left_rect), FadeIn(left_label), FadeIn(left_sub))
        self.play(Create(right_rect), FadeIn(right_label), FadeIn(right_sub))

        # ACC dot in left viewport at approximate button position
        left_dot = Dot(point=left_rect.get_center() + np.array([0.5, 0.3, 0]), radius=0.12, color=ACC)
        right_dot = Dot(point=right_rect.get_center() + np.array([0.8, 0.4, 0]), radius=0.12, color=ACC)

        self.play(FadeIn(left_dot), FadeIn(right_dot))

        # Bridge arrow with "?" label
        bridge = Arrow(
            start=left_rect.get_right() + np.array([0.1, 0, 0]),
            end=right_rect.get_left() + np.array([-0.1, 0, 0]),
            color=ACC, stroke_width=2, buff=0.1
        )
        q_label = Text("?", font_size=22, color=ACC)
        q_label.move_to(bridge.get_center() + np.array([0, 0.35, 0]))

        self.play(GrowArrow(bridge), FadeIn(q_label))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B02_TheRatio(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("The Ratio", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Formula lines
        fx = Text("real_x  =  claude_x  x  (viewport_w / 1456)", font_size=20, color=INK)
        fy = Text("real_y  =  claude_y  x  (viewport_h / 819)", font_size=20, color=INK)
        fx.move_to([0, 1.4, 0])
        fy.move_to([0, 0.7, 0])

        self.play(FadeIn(fx))
        self.play(FadeIn(fy))

        # X calculation
        cx_label = Text("claude_x = 728", font_size=17, color=SOFT)
        vw_label  = Text("viewport_w = 2560", font_size=17, color=SOFT)
        rx_result = Text("real_x = 1280", font_size=20, color=ACC)
        cx_label.move_to([-3.0, -0.3, 0])
        vw_label.move_to([0.8, -0.3, 0])
        rx_result.move_to([0, -0.9, 0])

        self.play(FadeIn(cx_label))
        self.play(FadeIn(vw_label))
        self.play(FadeIn(rx_result))

        # Y calculation
        cy_label = Text("claude_y = 409", font_size=17, color=SOFT)
        vh_label  = Text("viewport_h = 1440", font_size=17, color=SOFT)
        ry_result = Text("real_y = 720", font_size=20, color=ACC)
        cy_label.move_to([-3.0, -1.7, 0])
        vh_label.move_to([0.8, -1.7, 0])
        ry_result.move_to([0, -2.4, 0])

        self.play(FadeIn(cy_label))
        self.play(FadeIn(vh_label))
        self.play(FadeIn(ry_result))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B03_TheHit(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("The Hit", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Left panel — Claude sees
        left_rect = Rectangle(width=2.6, height=1.8, color=SOFT, stroke_width=2)
        left_rect.move_to([-2.8, -0.2, 0])
        left_label = Text("Claude sees 1456x819", font_size=13, color=SOFT)
        left_label.next_to(left_rect, UP, buff=0.15)

        left_dot = Dot(point=left_rect.get_center(), radius=0.13, color=ACC)
        left_coord = Text("(728, 409)", font_size=12, color=SOFT)
        left_coord.next_to(left_dot, DOWN, buff=0.15)

        self.play(Create(left_rect), FadeIn(left_label))
        self.play(FadeIn(left_dot), FadeIn(left_coord))

        # Right panel — Desktop
        right_rect = Rectangle(width=3.2, height=2.2, color=INK, stroke_width=2)
        right_rect.move_to([2.8, -0.2, 0])
        right_label = Text("Desktop 1920x1080", font_size=13, color=INK)
        right_label.next_to(right_rect, UP, buff=0.15)

        right_dot = Dot(point=right_rect.get_center() + np.array([0.3, 0.2, 0]), radius=0.13, color=ACC)
        right_coord = Text("(923, 541)", font_size=12, color=SOFT)
        right_coord.next_to(right_dot, DOWN, buff=0.15)

        self.play(Create(right_rect), FadeIn(right_label))
        self.play(FadeIn(right_dot), FadeIn(right_coord))

        # Formula between panels
        formula = Text("real = claude x viewport / 1456", font_size=16, color=ACC)
        formula.move_to([0, -2.5, 0])
        self.play(FadeIn(formula))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B04_Scope(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Scope", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        header = Text("Not covered:", font_size=20, color=INK)
        header.move_to([0, 1.2, 0])
        self.play(FadeIn(header))

        items = [
            "DOM navigation / CSS selector clicks",
            "Non-16:9 aspect ratios",
        ]
        for i, item in enumerate(items):
            t = Text(item, font_size=18, color=SOFT)
            t.move_to([0, 0.3 - i * 0.7, 0])
            self.play(FadeIn(t))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)
