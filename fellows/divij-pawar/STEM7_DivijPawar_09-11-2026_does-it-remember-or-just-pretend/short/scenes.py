"""short/scenes.py — 9:16 portrait re-layout of B01_OneWordTwoMechanisms only.

The parent reel's B01 splits "Memory" left/right into two boxes side by
side (±3.6 units) — assumes the 16:9 frame_width (~14.2 units). Portrait
rendering (manim -r 1080,1920) keeps frame_height at 8 units but shrinks
frame_width to ~4.5, so the split is restacked vertically instead: word,
then the context-window box, then the persistent-memory box beneath it
(dimmed context-window box still visible above, matching the parent's own
"cw persists at 15% opacity" beat, not a fresh cut), per shorts.py's
"Manim GRAPHIC beats are re-laid-out for portrait" rule.

Positions below are computed from measured mobject heights (title bottom
sits at y≈2.88 for this title's wrap, not guessed) — see the STEM6 short
scene's own note about the same title-collision defect class.
"""
from graphics_lib import *

BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


def cabinet_icon(color, width=0.55, height=0.75):
    body = Rectangle(width=width, height=height, color=color, stroke_width=2.5)
    drawer1 = Line(body.get_corner(UL) + DOWN * height * 0.33,
                    body.get_corner(UR) + DOWN * height * 0.33, color=color, stroke_width=1.5)
    drawer2 = Line(body.get_corner(UL) + DOWN * height * 0.66,
                    body.get_corner(UR) + DOWN * height * 0.66, color=color, stroke_width=1.5)
    handle1 = Dot(body.get_left() + RIGHT * width * 0.15 + DOWN * height * 0.17,
                   color=color, radius=0.03)
    handle2 = Dot(body.get_left() + RIGHT * width * 0.15 + DOWN * height * 0.5,
                   color=color, radius=0.03)
    return VGroup(body, drawer1, drawer2, handle1, handle2)


class B01_OneWordTwoMechanisms916(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("One Word, Two Mechanisms", color=INK, size=32)
        self.play(Write(t), run_time=0.6)
        self.wait(1.6)

        word = label("Memory", size=40, color=INK, weight="BOLD").move_to(UP * 2.3)
        self.play(FadeIn(word, scale=1.1), run_time=0.7)
        self.wait(2.2)

        cw_txt = label("Context\nWindow", size=20, color=INK, line_spacing=0.85)
        cw_box = auto_box(cw_txt, h_pad=0.26, v_pad=0.2, color=INK)
        cw = VGroup(cw_box, cw_txt).move_to(UP * 1.3)
        cw_tag = label("temporary", size=16, color=SOFT).next_to(cw, DOWN, buff=0.15)
        arr_top = Arrow(word.get_bottom(), cw.get_top(), buff=0.08, color=SOFT, stroke_width=2.2)
        self.play(Create(arr_top), FadeIn(cw), FadeIn(cw_tag), run_time=0.6)
        self.wait(3.0)

        evap = label("gone the moment\nthe chat ends", size=15, color=ACC, line_spacing=0.85)
        evap.next_to(cw_tag, DOWN, buff=0.2)
        self.play(FadeIn(evap), run_time=0.5)
        self.wait(1.6)
        self.play(cw.animate.set_opacity(0.15).scale(0.85),
                   FadeOut(cw_tag), FadeOut(evap), run_time=1.1)
        self.wait(2.4)

        pm_txt = label("Persistent\nMemory", size=22, color=INK, line_spacing=0.85, weight="BOLD")
        pm_box = auto_box(pm_txt, h_pad=0.3, v_pad=0.22, color=INK)
        pm = VGroup(pm_box, pm_txt).move_to(UP * 0.05)
        cabinet = cabinet_icon(SOFT).next_to(pm, DOWN, buff=0.25)
        link = Line(pm_box.get_bottom(), cabinet.get_top(), buff=0.05, color=SOFT, stroke_width=1.8)
        arr_mid = Arrow(cw.get_bottom(), pm.get_top(), buff=0.08, color=SOFT, stroke_width=2.2)
        self.play(Create(arr_mid), FadeIn(pm), Create(link), FadeIn(cabinet), run_time=0.7)
        self.wait(1.8)

        pm_tag = label("retrieved later", size=16, color=SOFT).next_to(cabinet, DOWN, buff=0.25)
        self.play(FadeIn(pm_tag), run_time=0.5)
        self.wait(2.9)

        caption = label("the model isn't\nrecalling — it's\nreacting to re-inserted text",
                         size=17, color=INK, line_spacing=0.85)
        caption.move_to(DOWN * 2.7)
        self.play(FadeOut(VGroup(arr_top, arr_mid, cw)), FadeIn(caption), run_time=0.7)
        self.wait(12.0)

        self.play(FadeOut(VGroup(word, pm, cabinet, link, pm_tag, caption)), run_time=0.6)
        land = serif("One name, two very\ndifferent mechanisms.",
                      size=25, color=ACC, line_spacing=1.0).move_to(DOWN * 0.2)
        self.play(Write(land), run_time=0.9)
        self.wait(13.96)
