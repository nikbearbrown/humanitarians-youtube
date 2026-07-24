"""
scenes.py — claude-liam-claude-constitution-three-principals
The Principal Hierarchy: Why Claude Has Three Bosses.
Source: Anthropic Claude Constitution §"Claude's three types of principals"

Palette: Claude brand
  PAGE   #FAF9F5  cream ground
  INK    #3D3929  warm near-black
  SPARK  #D97757  terracotta — ONE accent per beat
  SOFT   #73705F  secondary text
  GHOST  #A9A491  caption / ghost text
  BORDER #E5E2D9  subtle divider

Render:
  manim -qh --fps 30 -r 1920,1080 scenes.py B01_ThreePrincipals
  mv media/videos/scenes/*/B01_ThreePrincipals.mp4 manim/B01.mp4
  manim -qh --fps 30 -r 1920,1080 scenes.py B02_OperatorBounds
  mv media/videos/scenes/*/B02_OperatorBounds.mp4 manim/B02.mp4
  manim -qh --fps 30 -r 1920,1080 scenes.py B03_UserFloor
  mv media/videos/scenes/*/B03_UserFloor.mp4 manim/B03.mp4
"""

from manim import *

PAGE   = "#FAF9F5"
INK    = "#3D3929"
SPARK  = "#D97757"
SOFT   = "#73705F"
GHOST  = "#A9A491"
BORDER = "#E5E2D9"

config.background_color = PAGE


def source_caption(scene):
    cap = Text(
        "After Anthropic Claude Constitution (2026) — Three Principals",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_ThreePrincipals(Scene):
    def construct(self):
        dur = 22.3

        title = Text("Three Principals. Three Trust Levels.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Concentric rings centered slightly left to leave room for labels
        center = LEFT * 0.5 + DOWN * 0.3

        ring3 = Circle(radius=3.2, color=BORDER, stroke_width=2.0).move_to(center)
        ring3_fill = Circle(radius=3.2, color=BORDER, fill_color=PAGE, fill_opacity=1, stroke_width=0).move_to(center)
        ring2 = Circle(radius=2.1, color=SOFT, stroke_width=2.0).move_to(center)
        ring2_fill = Circle(radius=2.1, color=SOFT, fill_color=PAGE, fill_opacity=1, stroke_width=0).move_to(center)
        ring1 = Circle(radius=1.1, color=SPARK, stroke_width=2.5).move_to(center)
        ring1_fill = Circle(radius=1.1, color=SPARK, fill_color=SPARK, fill_opacity=0.18, stroke_width=0).move_to(center)

        # Center label
        core_lbl = Text("Anthropic", font_size=18, color=SPARK, weight=BOLD)
        core_lbl.move_to(center)
        core_sub = Text("hardcoded at training", font_size=13, color=SPARK)
        core_sub.next_to(core_lbl, DOWN, buff=0.12)

        # Middle ring label
        mid_lbl = Text("Operator", font_size=18, color=SOFT, weight=BOLD)
        mid_lbl.move_to(center + UP * 1.6 + RIGHT * 0.3)
        mid_sub = Text("system prompt + ToS", font_size=13, color=SOFT)
        mid_sub.next_to(mid_lbl, DOWN, buff=0.1)

        # Outer ring label
        out_lbl = Text("User", font_size=18, color=INK, weight=BOLD)
        out_lbl.move_to(center + UP * 2.7 + RIGHT * 0.3)
        out_sub = Text("conversation", font_size=13, color=INK)
        out_sub.next_to(out_lbl, DOWN, buff=0.1)

        # Side annotation
        ann = Text("Authority flows inward.\nInner ring cannot be overridden.", font_size=18, color=SOFT)
        ann.move_to(RIGHT * 4.5 + DOWN * 0.3)

        self.play(FadeIn(ring3_fill), Create(ring3), run_time=0.6)
        self.play(FadeIn(ring2_fill), Create(ring2), run_time=0.6)
        self.play(FadeIn(ring1_fill), Create(ring1), run_time=0.7)
        self.play(FadeIn(core_lbl), FadeIn(core_sub), run_time=0.5)
        self.play(FadeIn(mid_lbl), FadeIn(mid_sub), run_time=0.5)
        self.play(FadeIn(out_lbl), FadeIn(out_sub), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(ann), run_time=0.6)
        self.wait(dur - 6.4)


class B02_OperatorBounds(Scene):
    def construct(self):
        dur = 20.8

        title = Text("Operators Can Restrict. Cannot Weaponize.", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        col_left_x = -3.5
        col_right_x = 3.5
        divider = Line(UP * 2.2, DOWN * 3.0, color=BORDER, stroke_width=1.5)
        self.add(divider)

        hdr_can = Text("Operators CAN", font_size=21, color=INK, weight=BOLD)
        hdr_can.move_to([col_left_x, 2.0, 0])
        hdr_cannot = Text("Operators CANNOT", font_size=21, color=SPARK, weight=BOLD)
        hdr_cannot.move_to([col_right_x, 2.0, 0])
        self.add(hdr_can, hdr_cannot)

        can_items = [
            "Restrict topics",
            "Require a persona",
            "Limit task scope",
            "Expand safe content\nfor adult platforms",
        ]
        cannot_items = [
            "Weaponize Claude\nagainst users",
            "Order Claude to\ndeceive users",
            "Override hardcoded\nsafety behaviors",
            "Deny users a\nsafe-exit floor",
        ]

        for i, (can, cannot) in enumerate(zip(can_items, cannot_items)):
            y = 1.2 - i * 0.9
            c_txt = Text(can, font_size=17, color=INK)
            c_txt.move_to([col_left_x, y, 0])
            n_txt = Text(cannot, font_size=17, color=SPARK)
            n_txt.move_to([col_right_x, y, 0])
            self.play(Write(c_txt), run_time=0.35)
            self.play(FadeIn(n_txt, shift=LEFT * 0.15), run_time=0.35)
            self.wait(0.15)

        verdict = Text("The floor belongs to the user regardless.", font_size=20, color=SPARK, weight=BOLD)
        verdict.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(verdict), run_time=0.6)
        self.wait(dur - 7.0)


class B03_UserFloor(Scene):
    def construct(self):
        dur = 21.9

        title = Text("The User's Floor: Three Guarantees.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Floor base bar
        floor_bar = Rectangle(
            width=11.0, height=0.5, color=SPARK,
            fill_color=SPARK, fill_opacity=0.22, stroke_width=2
        ).move_to([0, -2.6, 0])
        floor_lbl = Text("User's floor — cannot be removed by any operator", font_size=17, color=SPARK)
        floor_lbl.next_to(floor_bar, DOWN, buff=0.18)
        self.add(floor_bar, floor_lbl)

        guarantees = [
            ("1", "Always tells you it cannot help\nwith something here.", "Even if it can't say why."),
            ("2", "Never denies being an AI\nto someone sincerely asking.", "Personas don't override honesty."),
            ("3", "Always refers to emergency\nservices if life is at risk.", "Regardless of operator scope."),
        ]

        xs = [-4.0, 0.0, 4.0]
        for (num, main, sub), x in zip(guarantees, xs):
            box = RoundedRectangle(
                width=3.5, height=2.8, corner_radius=0.18,
                color=BORDER, fill_color=PAGE, fill_opacity=1, stroke_width=1.5
            ).move_to([x, 0.2, 0])
            num_txt = Text(num, font_size=28, color=SPARK, weight=BOLD)
            num_txt.move_to(box).shift(UP * 0.85)
            main_txt = Text(main, font_size=16, color=INK)
            main_txt.move_to(box).shift(DOWN * 0.05)
            sub_txt = Text(sub, font_size=14, color=SOFT)
            sub_txt.move_to(box).shift(DOWN * 0.85)
            grp = VGroup(box, num_txt, main_txt, sub_txt)
            self.play(FadeIn(grp), run_time=0.7)
            self.wait(0.2)

        callout = Text("The system prompt is the contract that makes operators accountable.", font_size=19, color=INK)
        callout.to_edge(DOWN, buff=2.2)
        self.play(FadeIn(callout), run_time=0.6)
        self.wait(dur - 5.7)
