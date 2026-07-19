"""scenes.py — Manim for stable-element-refs. Source: Claude Quickstarts (Anthropic)"""
from manim import *

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_Brittle(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Brittle", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Browser frame
        frame = Rectangle(width=5.0, height=3.2, color=INK, stroke_width=2)
        frame.move_to([0, 0.0, 0])
        self.play(Create(frame))

        # Button chip with dot
        button = Rectangle(width=1.8, height=0.55, fill_color=SOFT, fill_opacity=0.2, stroke_color=SOFT, stroke_width=1.5)
        button.move_to([0.3, 0.2, 0])
        button_label = Text("Confirm Order", font_size=13, color=INK)
        button_label.move_to(button.get_center())
        dot = Dot(point=button.get_center() + np.array([1.1, 0, 0]), radius=0.1, color=ACC)
        coord_label = Text("(960, 540)", font_size=12, color=INK)
        coord_label.next_to(dot, RIGHT, buff=0.12)

        self.play(Create(button), FadeIn(button_label), FadeIn(dot), FadeIn(coord_label))

        # Scale the whole frame group down to 75%
        frame_group = VGroup(frame, button, button_label, dot, coord_label)
        new_dot_pos = frame.get_center() + np.array([0.75 * 0.3 + 0.75 * 1.1 - 0.3 - 1.1 + 0.3 + 1.1 - 0.3, 0, 0])

        self.play(frame_group.animate.scale(0.75), run_time=1.0)

        # New label at new position
        new_coord = Text("(720, 405)", font_size=12, color=ACC)
        new_coord.next_to(dot, DOWN, buff=0.12)
        self.play(FadeIn(new_coord))

        # Cross mark over old coordinates
        cross = Text("X", font_size=24, color=ACC, weight=BOLD)
        cross.move_to(coord_label.get_center())
        self.play(FadeIn(cross))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B02_Stable(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Stable", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Code line
        code_line = Text("element.setAttribute('data-ref', 'confirm_order_1')", font_size=16, color=INK)
        code_line.move_to([0, 1.0, 0])
        self.play(FadeIn(code_line))

        # Button rectangle
        button = Rectangle(width=2.2, height=0.65, fill_color=SOFT, fill_opacity=0.2, stroke_color=INK, stroke_width=1.5)
        button.move_to([0, -0.4, 0])
        button_label = Text("Confirm Order", font_size=15, color=INK)
        button_label.move_to(button.get_center())

        # Ref tag above the button
        ref_tag = Rectangle(width=2.0, height=0.4, fill_color=ACC, fill_opacity=0.2, stroke_color=ACC, stroke_width=1.5)
        ref_tag.next_to(button, UP, buff=0.05)
        ref_text = Text("ref=confirm_order_1", font_size=12, color=ACC)
        ref_text.move_to(ref_tag.get_center())

        self.play(Create(button), FadeIn(button_label))
        self.play(Create(ref_tag), FadeIn(ref_text))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B03_Survives(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Survives", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Left state — 1920x1080
        left_frame = Rectangle(width=3.0, height=2.0, color=INK, stroke_width=2)
        left_frame.move_to([-2.8, 0.2, 0])
        left_frame_label = Text("1920x1080", font_size=12, color=INK)
        left_frame_label.next_to(left_frame, UP, buff=0.12)

        left_btn = Rectangle(width=1.4, height=0.45, fill_color=SOFT, fill_opacity=0.2, stroke_color=SOFT, stroke_width=1.5)
        left_btn.move_to(left_frame.get_center())
        left_coord = Text("(960, 540)", font_size=11, color=SOFT)
        left_coord.next_to(left_btn, DOWN, buff=0.1)
        left_ref_tag = Rectangle(width=1.5, height=0.32, fill_color=ACC, fill_opacity=0.15, stroke_color=ACC, stroke_width=1.5)
        left_ref_tag.next_to(left_btn, UP, buff=0.04)
        left_ref_text = Text("confirm_order_1", font_size=10, color=ACC)
        left_ref_text.move_to(left_ref_tag.get_center())

        self.play(Create(left_frame), FadeIn(left_frame_label))
        self.play(Create(left_btn), FadeIn(left_coord))
        self.play(Create(left_ref_tag), FadeIn(left_ref_text))

        # Arrow to right
        arrow = Arrow(
            start=left_frame.get_right() + np.array([0.1, 0, 0]),
            end=left_frame.get_right() + np.array([1.0, 0, 0]),
            color=SOFT, stroke_width=2, buff=0.0
        )
        self.play(GrowArrow(arrow))

        # Right state — 1440x900
        right_frame = Rectangle(width=2.4, height=1.6, color=SOFT, stroke_width=2)
        right_frame.move_to([2.8, 0.2, 0])
        right_frame_label = Text("1440x900", font_size=12, color=SOFT)
        right_frame_label.next_to(right_frame, UP, buff=0.12)

        right_btn = Rectangle(width=1.2, height=0.4, fill_color=SOFT, fill_opacity=0.2, stroke_color=SOFT, stroke_width=1.5)
        right_btn.move_to(right_frame.get_center() + np.array([0.2, -0.2, 0]))
        right_coord = Text("(720, 405)", font_size=11, color=SOFT)
        right_coord.next_to(right_btn, DOWN, buff=0.1)
        right_ref_tag = Rectangle(width=1.5, height=0.32, fill_color=ACC, fill_opacity=0.15, stroke_color=ACC, stroke_width=1.5)
        right_ref_tag.next_to(right_btn, UP, buff=0.04)
        right_ref_text = Text("confirm_order_1", font_size=10, color=ACC)
        right_ref_text.move_to(right_ref_tag.get_center())

        self.play(Create(right_frame), FadeIn(right_frame_label))
        self.play(Create(right_btn), FadeIn(right_coord))
        self.play(Create(right_ref_tag), FadeIn(right_ref_text))

        # Bottom caption
        caption = Text("Claude clicks ref=confirm_order_1. Lands every time.", font_size=14, color=INK)
        caption.move_to([0, -2.4, 0])
        self.play(FadeIn(caption))

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
            "JS injection implementation",
            "CSS specificity conflicts",
            "Dynamic post-load elements",
        ]
        for i, item in enumerate(items):
            t = Text(item, font_size=18, color=SOFT)
            t.move_to([0, 0.3 - i * 0.7, 0])
            self.play(FadeIn(t))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)
