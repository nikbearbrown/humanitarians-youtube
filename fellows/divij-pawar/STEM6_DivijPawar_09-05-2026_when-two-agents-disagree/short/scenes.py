"""short/scenes.py — 9:16 portrait re-layout of B02_TheNaiveFix only.

The parent reel's B02 arranges its two conclusion bubbles side by side
(±3.6 units) and a 9-unit-wide number line at the end — both assume the
16:9 frame_width (~14.2 units). Portrait rendering (manim -r 1080,1920)
keeps frame_height at 8 units but shrinks frame_width to ~4.5, so every
horizontal arrangement here is restacked vertically instead, per
shorts.py's "Manim GRAPHIC beats are re-laid-out for portrait" rule —
never a center-cut of the 16:9 version, which would clip both bubbles
off-frame. The number-line comparison in particular is flipped from
horizontal to vertical, since a 9-unit-wide line cannot fit a 4.5-unit
frame at any legible label size (label()'s FLOOR floors text at 24pt
regardless of the size requested).

Play/wait durations are copied unchanged from the parent's retimed
B02_TheNaiveFix — this beat's audio (mp3/beat-B02.mp3) is identical in
the short, so the total must still land on 37.18s.
"""
from graphics_lib import *

BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


def bubble(text_mobj, color, h_pad=0.3, v_pad=0.22):
    box = RoundedRectangle(corner_radius=0.2,
                            width=text_mobj.width + 2 * h_pad,
                            height=text_mobj.height + 2 * v_pad,
                            color=color, stroke_width=2.5,
                            fill_color=color, fill_opacity=0.07)
    box.move_to(text_mobj)
    return VGroup(box, text_mobj)


def blender_icon(color, width=1.3, height=1.9):
    jar = Polygon([-width / 2, height / 2, 0], [width / 2, height / 2, 0],
                  [width * 0.32, -height / 2, 0], [-width * 0.32, -height / 2, 0],
                  color=color, stroke_width=2.5, fill_color=color, fill_opacity=0.06)
    stand = Rectangle(width=width * 0.9, height=0.14, color=color,
                       fill_color=color, fill_opacity=1.0, stroke_width=0)
    stand.next_to(jar, DOWN, buff=0.0)
    return VGroup(jar, stand)


class B02_TheNaiveFix916(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("The Naive Fix", color=INK, size=34)
        self.play(Write(t), run_time=0.6)
        self.wait(1.2)

        # ── Bubbles + doc, stacked vertically (portrait has ~4.5 units of
        # width — the parent's ±3.6 side-by-side placement would run off
        # both edges) ───────────────────────────────────────────────────────
        # title() never fades out in this scene, and to_edge(UP, buff=0.7)
        # puts its bottom edge around y=2.75 — bub_a at the original UP*2.7
        # (and the Agent-A/B column below at UP*2.6) both collided with it,
        # caught in portrait contact-sheet QC. Everything here is pushed
        # down to clear y≈2.75 with margin.
        # Graphics enlarged per review — the first pass left generous empty
        # margin on all sides at portrait's ~4.5-unit width, and several
        # labels were requested below label()'s 24pt FLOOR (so "bigger"
        # requests below 24 were silently no-ops); everything below is
        # explicitly sized above the floor and the shapes scaled up to
        # match, with positions re-spaced so the larger elements still
        # clear the persistent title (bottom edge ~y=2.75, see below).
        # Positions below are computed from measured mobject heights, not
        # guessed — title's own bottom edge sits at y≈2.925 (not the ~2.75
        # estimated in the first pass), and the full bub_a→doc→bub_b→
        # blender→grey→caption chain does not fit if blender is placed
        # strictly *below* bub_b's rest position (there isn't enough
        # vertical room left for grey+caption, which stay on screen
        # together with blender for several seconds — a real, held
        # collision risk, unlike the brief bub_a/bub_b-vs-blender transient
        # below). Since bub_a/bub_b actually shrink-and-fade *into*
        # blender's center rather than needing to rest beside it, blender
        # is placed centered in the bub_a/bub_b gap instead of below both.
        txt_a = label("margins\nimproving", size=26, color=INK, line_spacing=0.9)
        txt_b = label("margins\ndeclining", size=26, color=ACC, line_spacing=0.9)
        bub_a = bubble(txt_a, INK).move_to(UP * 2.0)
        bub_b = bubble(txt_b, ACC).move_to(DOWN * 0.9)
        doc = Rectangle(width=1.2, height=1.3, color=SOFT, stroke_width=3,
                         fill_color=SOFT, fill_opacity=0.05).move_to(UP * 0.55)
        arr_a = Arrow(bub_a.get_bottom(), doc.get_top(), buff=0.08, color=SOFT, stroke_width=3)
        arr_b = Arrow(bub_b.get_top(), doc.get_bottom(), buff=0.08, color=SOFT, stroke_width=3)
        self.play(FadeIn(doc), FadeIn(bub_a), FadeIn(bub_b), Create(arr_a), Create(arr_b),
                   run_time=0.8)
        self.wait(2.5)

        # ── Both slide into a blender — positioned where `doc` was (which
        # fades out in the same beat), not below bub_b, so grey/caption
        # below it have real room to breathe ────────────────────────────
        blender = blender_icon(SOFT, width=1.05, height=1.4).move_to(UP * 0.55)
        self.play(FadeOut(doc), FadeOut(arr_a), FadeOut(arr_b), FadeIn(blender), run_time=0.4)
        self.wait(0.4)
        self.play(bub_a.animate.move_to(blender.get_center()).scale(0.2).set_opacity(0),
                   bub_b.animate.move_to(blender.get_center()).scale(0.2).set_opacity(0),
                   run_time=1.1)
        self.play(Wiggle(blender, scale_value=1.08, rotation_angle=0.02 * TAU), run_time=0.5)
        grey_txt = label("results\nmay vary", size=26, color=GHOST, line_spacing=0.9)
        grey = bubble(grey_txt, GHOST)
        grey.next_to(blender, DOWN, buff=0.3)
        self.play(FadeIn(grey, shift=DOWN * 0.2), run_time=0.5)
        self.wait(1.8)

        caption = label("nobody's actual\nopinion", size=26, color=SOFT, line_spacing=0.9)
        caption.next_to(grey, DOWN, buff=0.3)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(5.9)

        # ── If A was right, the blend makes it worse — a vertical axis
        # instead of the parent's 9-unit-wide horizontal one, which cannot
        # fit a 4.5-unit portrait frame at any legible label size ─────────
        self.play(FadeOut(VGroup(blender, grey, caption)), run_time=0.5)
        right_lab = label("Agent A — right", size=32, color=INK, weight="BOLD")
        wrong_lab = label("Agent B — wrong", size=32, color=SOFT)
        col = VGroup(right_lab, wrong_lab).arrange(DOWN, buff=0.32).move_to(UP * 1.9)
        self.play(FadeIn(col), run_time=0.5)
        self.wait(1.6)

        vline = Line(UP * 1.0, DOWN * 2.0, color=GHOST, stroke_width=3.5).move_to(LEFT * 0.95)
        truth = Dot(vline.get_top() + DOWN * 0.35, color=INK, radius=0.15)
        truth_lab = label("true answer", size=28, color=INK).next_to(truth, RIGHT, buff=0.3)
        blend_pt = Dot(vline.get_bottom() + UP * 0.6, color=ACC, radius=0.15)
        blend_lab = label("blended\nanswer", size=28, color=ACC, line_spacing=0.9).next_to(blend_pt, RIGHT, buff=0.3)
        self.play(Create(vline), run_time=0.5)
        self.play(FadeIn(truth), FadeIn(truth_lab), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(blend_pt), FadeIn(blend_lab), run_time=0.5)
        self.wait(4.2)

        land = serif("Erases the one fact\nthat mattered:\nthey disagreed.",
                      size=32, color=ACC, line_spacing=1.0).move_to(DOWN * 2.9)
        self.play(FadeOut(col), Write(land), run_time=0.8)
        self.wait(10.88)
