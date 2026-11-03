"""short/scenes.py — 9:16 portrait re-layout of B01_DataAndInstructions only.

The parent reel's B01 arranges 12 small squares in a single horizontal
row (~5.1 units wide) — exceeds the ~4.5-unit portrait frame width. Cut
down to 6 squares (from an earlier 8-square pass) at 1.5x the original
size (0.3 -> 0.45), which fits comfortably (~3.3 units) with margin to
spare inside the ~4.5-unit frame. All diagram graphics (squares, wall,
strike line) and their labels/captions are enlarged ~50% from the
original pass per feedback that the clip read too small — text sizes
are capped below a literal 1.5x wherever the measured width would have
overflowed the frame (documented per-element below); every position was
recomputed and verified via direct measurement, not guessed.
"""
import numpy as np
from graphics_lib import *

BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_DataAndInstructions916(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Data and Instructions\nLook Identical", color=INK, size=28, line_spacing=0.9)
        self.play(Write(t), run_time=0.6)
        self.wait(1.8)

        # 1.5x the original 0.3 square size; cut to 6 (from 8) to keep the
        # wider row centered with margin inside the ~4.5-unit portrait frame.
        stream = VGroup(*[
            Rectangle(width=0.45, height=0.45, color=GHOST, stroke_width=1.6,
                      fill_color=GHOST, fill_opacity=0.15)
            for _ in range(6)
        ])
        stream.arrange(RIGHT, buff=0.12).move_to(UP * 1.1)
        self.play(LaggedStart(*[FadeIn(s) for s in stream], lag_ratio=0.08), run_time=1.0)
        self.wait(5.51)

        # Segments at opposite ends of the row (same reasoning as the prior
        # 8-square pass): 0:2 and 4:6 keep their labels clear of each other.
        seg_instr = VGroup(*stream[0:2])
        seg_data = VGroup(*stream[4:6])
        self.play(seg_instr.animate.set_color(INK).set_fill(INK, opacity=0.3),
                   seg_data.animate.set_color(SOFT).set_fill(SOFT, opacity=0.3), run_time=0.7)
        # size 28, not the literal 1.5x-of-24 (36) — measured: 36pt pushed
        # both labels past the frame edge once centered under the wider
        # segments; 28 is the largest that stays inside with margin.
        lab_instr = label("instruction", size=28, color=INK).next_to(seg_instr, DOWN, buff=0.2)
        lab_data = label("data to read", size=28, color=SOFT).next_to(seg_data, DOWN, buff=0.2)
        self.play(FadeIn(lab_instr), FadeIn(lab_data), run_time=0.5)
        self.wait(6.11)

        # size 26 (not 36) for the same frame-width reason — this is a long
        # two-line caption and 36pt measured wider than the frame itself.
        cap1 = label("same font, same color —\nuntil the labels appear",
                      size=26, color=SOFT, line_spacing=0.9)
        cap1.move_to(DOWN * 0.6)
        self.play(FadeIn(cap1), run_time=0.5)
        self.wait(5.31)

        self.play(FadeOut(cap1), run_time=0.3)
        # Wall geometry scaled 1.5x along with the squares (pure geometry,
        # no frame-width constraint the way text has).
        wall_top = np.array([0.0, stream.get_y() + 0.525, 0.0])
        wall_bot = np.array([0.0, stream.get_y() - 1.125, 0.0])
        wall = DashedLine(wall_top, wall_bot, color=SOFT, stroke_width=3.0, dash_length=0.11)
        wall_lab = label("the wall a human\nassumes exists", size=32, color=SOFT, line_spacing=0.85)
        wall_lab.next_to(wall, DOWN, buff=0.25)
        self.play(Create(wall), FadeIn(wall_lab), run_time=0.6)
        self.wait(6.31)

        strike_line = Line(wall_top + DOWN * 0.12 + LEFT * 0.18, wall_bot + UP * 0.12 + RIGHT * 0.18,
                            color=ACC, stroke_width=4.0)
        self.play(Create(strike_line), run_time=0.5)
        cap2 = label("no chemical difference\nto the model", size=28, color=ACC, line_spacing=0.9)
        cap2.move_to(DOWN * 2.7)
        self.play(FadeIn(cap2), run_time=0.5)
        self.wait(6.51)

        self.play(FadeOut(VGroup(stream, lab_instr, lab_data, wall, wall_lab, strike_line, cap2)),
                   run_time=0.6)
        cap3 = label("text that looks like\nan instruction gets\ntreated like one",
                      size=32, color=INK, line_spacing=0.9)
        cap3.move_to(UP * 0.2)
        self.play(FadeIn(cap3), run_time=0.6)
        self.wait(9.11)

        self.play(FadeOut(cap3), run_time=0.4)
        land = serif("Just more text\nin the context.", size=38, color=ACC, line_spacing=1.0)
        land.move_to(DOWN * 0.2)
        self.play(Write(land), run_time=0.9)
        self.wait(5.42)
