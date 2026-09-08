"""short/scenes.py — 9:16 portrait re-layout of B02_ClaimExtraction only.

The parent reel's B02 arranges its four claim-type cards in a horizontal
row and its worked-example line across two wide lines — both assume the
16:9 frame_width (~14.2 units). Portrait rendering (manim -r 1080,1920)
keeps frame_height at 8 units but shrinks frame_width to ~4.5, so every
horizontal arrangement here is restacked vertically instead, per shorts.py's
"Manim GRAPHIC beats are re-laid-out for portrait" rule (never a center-cut
of the 16:9 version, which would clip the CITATION/CAUSAL cards off-frame).
"""
from graphics_lib import *

BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")

WORKED_LINE = "Revenue grew 34% YoY,\ndriven by international\nexpansion — source: 10-K"


class B02_ClaimExtraction916(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Claim Extraction", color=INK, size=34)
        self.play(Write(t), run_time=0.6)
        self.wait(2.56)

        prose_lines = VGroup(*[
            label(ln, size=16, color=SOFT) for ln in (
                "dense, confident prose —",
                "fed through a parser",
                "instead of read as a story",
            )
        ]).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        prose_box = auto_box(prose_lines, h_pad=0.28, v_pad=0.22, color=SOFT)
        prose = VGroup(prose_box, prose_lines).move_to(UP * 1.7)
        self.play(Create(prose_box), FadeIn(prose_lines), run_time=0.8)
        self.wait(6.23)
        self.play(FadeOut(prose), run_time=0.4)

        # Four cards, stacked (portrait has ~4.5 units of width — a
        # horizontal row here would either overflow or need to shrink past
        # the legibility floor).
        names = ["CITATION", "QUANTITATIVE", "HEDGE", "CAUSAL"]
        cards = VGroup()
        for name in names:
            head = label(name, size=22, color=ACC, weight="BOLD")
            box = auto_box(head, h_pad=0.28, v_pad=0.2, color=INK,
                            fill_color=BG, fill_opacity=1.0)
            cards.add(VGroup(box, head))
        # Center low enough that the stack's TOP card clears the title,
        # which never fades out this scene — the stack's own height
        # (4 cards + 3 gaps, ~2.7 units) was underestimated against a
        # too-high UP*1.6 center in the first pass and collided with the
        # title's bottom edge (caught in portrait smoke-test QC).
        cards.arrange(DOWN, buff=0.22).move_to(UP * 0.3)

        for c in cards:
            self.play(FadeIn(c, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(1.65)
        self.wait(1.83)

        code = mono("citation | quantitative\n| hedge | causal",
                     size=14, color=SOFT, line_spacing=0.9)
        code.next_to(cards, DOWN, buff=0.35)
        self.play(FadeIn(code), run_time=0.5)
        self.wait(4.4)

        # Worked example, tagged three ways at once.
        self.play(FadeOut(code), run_time=0.3)
        worked = mono(WORKED_LINE, size=15, color=INK, line_spacing=1.0)
        worked.next_to(cards, DOWN, buff=0.4)
        self.play(FadeIn(worked), run_time=0.6)
        self.wait(3.3)

        targets = {0: cards[0], 1: cards[1], 3: cards[3]}
        lines = VGroup()
        for idx in targets:
            ln = DashedLine(targets[idx].get_left() + LEFT * 0.05,
                             worked.get_top() + UP * 0.05,
                             color=ACC, stroke_width=2, dash_length=0.1)
            lines.add(ln)
            targets[idx][1].set_color(ACC)
        self.play(*[Create(ln) for ln in lines], run_time=0.9)
        self.wait(5.13)

        hedges = label("approximately\nunclear · assumed", size=15,
                        color=GHOST, line_spacing=0.85)
        hedges.next_to(worked, DOWN, buff=0.35)
        self.play(FadeIn(hedges), run_time=0.5)
        self.wait(4.03)

        self.play(FadeOut(VGroup(cards, worked, hedges, *lines)), run_time=0.5)
        caption = label("no second AI —\njust pattern matching", size=22,
                         color=INK, line_spacing=0.9).move_to(DOWN * 1.2)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(5.5)

        land = serif("Prose becomes a\nchecklist of\nfalsifiable pieces.",
                      size=24, color=ACC, line_spacing=1.0).move_to(DOWN * 2.7)
        self.play(FadeOut(caption), FadeIn(land), run_time=0.6)
        self.wait(6.41)
