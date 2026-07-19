"""vox_scenes.py -- Load More Warheads on a Cancer Drug and It Gets Cleared Faster
(vox-dar-optimum, slate cut, 16:9).

One Scene per GRAPHIC / CARD / DOCUMENT beat. B05 is the only STILL (ai media
slot) and has no scene here. Durations read from beat_sheet.json (actuals after
audio lock; estimates as fallback).

Color law: TEAL = optimal/survives/reaches-tumor; CRIMSON = overloaded/cleared/toxic.
GOLD = editor's pen fill highlight only, never text. Two accents max.

Exclusions honored: NO cleavable/non-cleavable linker detail, NO bystander
effect, NO five-step funnel, NO site-specific conjugation.

All DAR example numbers (68%, 11%, 2.4, 0.3, 3 mice) are illustrative.
"""
import sys, pathlib as _pl
sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[3]
                        / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene
import json, os

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 13)}

import numpy as np


# ---------------------------------------------------------------- helpers

def _antibody(center, color=TEAL, scale=1.0):
    """Y-shaped antibody: two Fab arms + Fc stem."""
    # Fc stem: vertical line down
    stem = Line(center + UP * 0.0, center + DOWN * 0.7 * scale,
                color=color, stroke_width=6 * scale)
    # hinge
    hinge = center + UP * 0.0
    # two Fab arms angled up-left and up-right
    arm_l = Line(hinge, hinge + UP * 0.65 * scale + LEFT * 0.55 * scale,
                 color=color, stroke_width=6 * scale)
    arm_r = Line(hinge, hinge + UP * 0.65 * scale + RIGHT * 0.55 * scale,
                 color=color, stroke_width=6 * scale)
    return VGroup(stem, arm_l, arm_r)


def _payload_dot(pos, color=TEAL, r=0.12):
    d = Dot(radius=r, color=color)
    d.set_fill(color, 1).set_stroke(width=0, opacity=0)
    d.move_to(pos)
    return d


def _bar_rect(bottom_center, width, height, color):
    """A filled rectangle growing up from bottom_center."""
    r = Rectangle(width=width, height=height)
    r.set_fill(color, 1).set_stroke(width=0, opacity=0)
    r.move_to(bottom_center + UP * height / 2)
    return r


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Load More Warheads on a Cancer Drug", font=DISPLAY, color=INK, font_size=26, weight=BOLD)
        t2 = Text("and It Gets Cleared Faster", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B02_LoadingLogic(Scene):
    """Naive loading logic: antibody Y accumulates 1 to 8 payload dots."""
    def construct(self):
        total = DUR["B02"]
        center = ORIGIN + LEFT * 0.3
        ab = _antibody(center, color=TEAL, scale=1.4)
        # payload attachment sites on the two arms
        l_tip = center + UP * 0.65 * 1.4 + LEFT * 0.55 * 1.4
        r_tip = center + UP * 0.65 * 1.4 + RIGHT * 0.55 * 1.4
        l_mid = center + UP * 0.32 * 1.4 + LEFT * 0.27 * 1.4
        r_mid = center + UP * 0.32 * 1.4 + RIGHT * 0.27 * 1.4
        stem_top = center + DOWN * 0.17 * 1.4
        stem_bot = center + DOWN * 0.52 * 1.4
        stem_l = center + DOWN * 0.35 * 1.4 + LEFT * 0.1
        stem_r = center + DOWN * 0.35 * 1.4 + RIGHT * 0.1

        dot_positions = [l_tip, r_tip, l_mid, r_mid, stem_top, stem_bot, stem_l, stem_r]
        count_label = Text("0", font=MONO, color=INK, font_size=64)
        count_label.move_to(RIGHT * 4.0)
        dek = Text("payloads per antibody", font=SERIF, color=INK, font_size=22, slant=ITALIC)
        dek.next_to(count_label, DOWN, buff=0.3)

        self.play(Create(ab), run_time=0.8)
        self.play(FadeIn(count_label), FadeIn(dek), run_time=0.5)

        dots = VGroup()
        for i, pos in enumerate(dot_positions):
            d = _payload_dot(pos, color=TEAL)
            dots.add(d)
            new_label = Text(str(i + 1), font=MONO, color=INK, font_size=64)
            new_label.move_to(count_label.get_center())
            self.play(FadeIn(d, scale=0.6), run_time=0.35)
            self.play(ReplacementTransform(count_label, new_label), run_time=0.2)
            count_label = new_label
            if i == 3:
                self.wait(0.5)

        self.wait(max(0.3, total - 0.8 - 0.5 - 8 * 0.55 - 0.5))


class B03_TheQuestion(Scene):
    """THE QUESTION beat — gap formula on screen."""
    def construct(self):
        total = DUR["B03"]
        t1 = Text("A cancer antibody carries more drug per molecule.", font=DISPLAY,
                  color=INK, font_size=24, weight=BOLD)
        t2 = Text("More drug should kill better.", font=DISPLAY,
                  color=INK, font_size=24, weight=BOLD)
        block1 = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.8)
        sep = Line(LEFT * 5.0, RIGHT * 5.0, color=SLATE, stroke_width=1.5)
        sep.next_to(block1, DOWN, buff=0.35)
        q = Text("Why does loading more warheads", font=DISPLAY,
                 color=CRIMSON, font_size=28, weight=BOLD)
        q2 = Text("make it clear faster -- and kill less?", font=DISPLAY,
                  color=CRIMSON, font_size=28, weight=BOLD)
        qblock = VGroup(q, q2).arrange(DOWN, buff=0.15)
        qblock.next_to(sep, DOWN, buff=0.35)
        self.play(FadeIn(block1), run_time=0.8)
        self.play(Create(sep), run_time=0.4)
        self.play(FadeIn(qblock, shift=UP * 0.2), run_time=0.8)
        self.wait(max(0.3, total - 2.0))


class B04_DARScale(Scene):
    """DAR horizontal scale 0-10 with teal sweet-spot bracket."""
    def construct(self):
        total = DUR["B04"]
        # number line
        axis = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=3)
        axis.move_to(DOWN * 0.3)

        # tick marks and labels 0, 2, 4, 6, 8, 10
        ticks = VGroup()
        tick_labels = VGroup()
        for val in range(0, 11, 2):
            x = -5.5 + val * 1.1
            t = Line(np.array([x, -0.3, 0]) + DOWN * 0.15,
                     np.array([x, -0.3, 0]) + UP * 0.15,
                     color=INK, stroke_width=2)
            lbl = Text(str(val), font=MONO, color=INK, font_size=22)
            lbl.move_to(np.array([x, -0.3, 0]) + DOWN * 0.45)
            ticks.add(t)
            tick_labels.add(lbl)

        axis_label = Text("drug-to-antibody ratio (DAR)", font=SERIF, color=INK,
                          font_size=22, slant=ITALIC)
        axis_label.next_to(axis, DOWN, buff=0.85)

        # teal bracket: DAR 4 to 8
        x4 = -5.5 + 4 * 1.1
        x8 = -5.5 + 8 * 1.1
        bracket = Line(np.array([x4, -0.3, 0]) + UP * 0.55,
                       np.array([x8, -0.3, 0]) + UP * 0.55,
                       color=TEAL, stroke_width=4)
        b_left = Line(np.array([x4, -0.3, 0]) + UP * 0.3,
                      np.array([x4, -0.3, 0]) + UP * 0.55,
                      color=TEAL, stroke_width=4)
        b_right = Line(np.array([x8, -0.3, 0]) + UP * 0.3,
                       np.array([x8, -0.3, 0]) + UP * 0.55,
                       color=TEAL, stroke_width=4)
        bracket_label = Text("clinical ADCs", font=DISPLAY, color=TEAL, font_size=20)
        bracket_label.move_to(np.array([(x4 + x8) / 2, -0.3 + 0.9, 0]))

        # crimson arrows at low and high ends
        low_arrow = Arrow(start=np.array([x4 - 0.3, -0.3, 0]) + UP * 0.42,
                          end=np.array([x4 - 1.5, -0.3, 0]) + UP * 0.42,
                          color=CRIMSON, buff=0.0, stroke_width=3,
                          max_tip_length_to_length_ratio=0.25)
        high_arrow = Arrow(start=np.array([x8 + 0.3, -0.3, 0]) + UP * 0.42,
                           end=np.array([x8 + 1.5, -0.3, 0]) + UP * 0.42,
                           color=CRIMSON, buff=0.0, stroke_width=3,
                           max_tip_length_to_length_ratio=0.25)
        low_lbl = Text("under-kills", font=SERIF, color=CRIMSON, font_size=20, slant=ITALIC)
        low_lbl.move_to(np.array([x4 - 2.3, -0.3, 0]) + UP * 0.42)
        high_lbl = Text("clears fast", font=SERIF, color=CRIMSON, font_size=20, slant=ITALIC)
        high_lbl.move_to(np.array([x8 + 2.3, -0.3, 0]) + UP * 0.42)

        self.play(Create(axis), FadeIn(ticks), FadeIn(tick_labels),
                  FadeIn(axis_label), run_time=1.0)
        self.play(Create(bracket), Create(b_left), Create(b_right),
                  FadeIn(bracket_label), run_time=0.9)
        self.play(GrowArrow(low_arrow), GrowArrow(high_arrow),
                  FadeIn(low_lbl), FadeIn(high_lbl), run_time=0.8)
        self.wait(max(0.3, total - 2.7))


class B06_HydrophobicLoad(Scene):
    """Payload accumulation past 4 causes hydrophobic aggregation."""
    def construct(self):
        total = DUR["B06"]
        center = ORIGIN + LEFT * 1.5
        ab = _antibody(center, color=TEAL, scale=1.3)
        l_tip = center + UP * 0.65 * 1.3 + LEFT * 0.55 * 1.3
        r_tip = center + UP * 0.65 * 1.3 + RIGHT * 0.55 * 1.3
        l_mid = center + UP * 0.32 * 1.3 + LEFT * 0.27 * 1.3
        r_mid = center + UP * 0.32 * 1.3 + RIGHT * 0.27 * 1.3

        dot_positions_4 = [l_tip, r_tip, l_mid, r_mid]
        extra_positions = [
            center + DOWN * 0.1 * 1.3 + LEFT * 0.4,
            center + DOWN * 0.1 * 1.3 + RIGHT * 0.4,
            center + DOWN * 0.45 * 1.3 + LEFT * 0.2,
            center + DOWN * 0.45 * 1.3 + RIGHT * 0.2,
        ]

        self.play(Create(ab), run_time=0.7)
        dots = VGroup()
        for pos in dot_positions_4:
            d = _payload_dot(pos, color=TEAL)
            dots.add(d)
            self.play(FadeIn(d, scale=0.6), run_time=0.25)

        # pause at DAR-4: label "DAR 4"
        d4_label = LabelChip("DAR 4", accent=TEAL, size=22)
        d4_label.move_to(RIGHT * 3.5 + UP * 1.5)
        self.play(FadeIn(d4_label), run_time=0.4)
        self.wait(0.4)

        # now load 4 more — they go crimson (hydrophobic overload)
        extra_dots = VGroup()
        for pos in extra_positions:
            d = _payload_dot(pos, color=CRIMSON)
            extra_dots.add(d)
            self.play(FadeIn(d, scale=0.6), run_time=0.25)

        # whole conjugate shifts right slightly (aggregation pull)
        agg_label = LabelChip("DAR 8 -- aggregating", accent=CRIMSON, size=22)
        agg_label.move_to(RIGHT * 3.5 + UP * 0.8)
        self.play(FadeOut(d4_label), FadeIn(agg_label), run_time=0.4)

        # second conjugate appears to the right to show aggregation
        center2 = center + RIGHT * 3.8
        ab2 = _antibody(center2, color=TEAL, scale=0.9)
        dots2 = VGroup(*[_payload_dot(
            center2 + UP * 0.65 * 0.9 + (LEFT if i % 2 == 0 else RIGHT) * 0.55 * 0.9,
            color=CRIMSON) for i in range(4)])
        # drift together
        self.play(FadeIn(ab2), FadeIn(dots2), run_time=0.5)
        self.play(ab2.animate.shift(LEFT * 0.8), dots2.animate.shift(LEFT * 0.8),
                  run_time=0.7)
        sticky_lbl = SerifLabel("hydrophobic / sticking together", CRIMSON, size=22)
        sticky_lbl.next_to(agg_label, DOWN, buff=0.35)
        self.play(FadeIn(sticky_lbl), run_time=0.5)
        self.wait(max(0.3, total - 0.7 - 4 * 0.25 - 0.4 - 0.4 - 4 * 0.25 - 0.4 - 0.5 - 0.7 - 0.5))


class B07_ClearanceTrap(Scene):
    """Blood vessel channel: DAR-4 flows through, DAR-8 gets cleared by liver."""
    def construct(self):
        total = DUR["B07"]
        # vessel channel
        vessel_top = Line(LEFT * 6.5, RIGHT * 6.5, color=INK, stroke_width=2)
        vessel_bot = Line(LEFT * 6.5, RIGHT * 6.5, color=INK, stroke_width=2)
        vessel_top.move_to(UP * 1.2)
        vessel_bot.move_to(DOWN * 1.2)
        vessel_fill = Rectangle(width=13.0, height=2.4)
        vessel_fill.set_fill(SLATE, 0.07).set_stroke(width=0, opacity=0)
        vessel_fill.move_to(ORIGIN)

        # clearance box on the right
        clear_box = Rectangle(width=2.5, height=2.2)
        clear_box.set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 2)
        clear_box.move_to(RIGHT * 5.0 + DOWN * 0.8)
        clear_lbl = Text("liver /", font=DISPLAY, color=CRIMSON, font_size=20, weight=BOLD)
        clear_lbl2 = Text("immune system", font=DISPLAY, color=CRIMSON, font_size=20, weight=BOLD)
        clear_text = VGroup(clear_lbl, clear_lbl2).arrange(DOWN, buff=0.1)
        clear_text.move_to(clear_box.get_center())

        self.play(Create(vessel_top), Create(vessel_bot), FadeIn(vessel_fill), run_time=0.7)
        self.play(FadeIn(clear_box), FadeIn(clear_text), run_time=0.5)

        # DAR-4: teal dot flows left to right through channel
        d4 = Dot(radius=0.18, color=TEAL)
        d4.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        d4.move_to(LEFT * 5.5)
        lbl_d4 = Text("DAR 4", font=MONO, color=TEAL, font_size=20)
        lbl_d4.next_to(d4, UP, buff=0.15)
        self.play(FadeIn(d4), FadeIn(lbl_d4), run_time=0.4)
        self.play(d4.animate.move_to(RIGHT * 1.5),
                  lbl_d4.animate.move_to(RIGHT * 1.5 + UP * 0.33),
                  run_time=1.2)
        # add tick "survives"
        ok_lbl = LabelChip("survives", accent=TEAL, size=20)
        ok_lbl.next_to(d4, DOWN, buff=0.25)
        self.play(FadeIn(ok_lbl), run_time=0.4)

        # DAR-8: crimson cluster enters, slows, gets pulled aside
        d8 = VGroup(*[Dot(radius=0.13, color=CRIMSON).set_fill(CRIMSON, 1)
                      .set_stroke(width=0, opacity=0)
                      .shift(np.array([i * 0.25, j * 0.18, 0]))
                      for i, j in [(-0.2, 0), (0, 0.15), (0.2, 0),
                                   (0, -0.15), (0.1, 0.08)]])
        d8.move_to(LEFT * 5.5 + UP * 0.3)
        lbl_d8 = Text("DAR 8", font=MONO, color=CRIMSON, font_size=20)
        lbl_d8.next_to(d8, UP, buff=0.1)
        self.play(FadeIn(d8), FadeIn(lbl_d8), run_time=0.4)
        # slow drift then pulled down
        self.play(d8.animate.move_to(RIGHT * 2.2 + UP * 0.1),
                  lbl_d8.animate.move_to(RIGHT * 2.2 + UP * 0.55),
                  run_time=1.0)
        self.play(d8.animate.move_to(RIGHT * 5.0 + DOWN * 1.0),
                  lbl_d8.animate.move_to(RIGHT * 5.0 + DOWN * 0.35),
                  run_time=0.9)
        cleared_chip = LabelChip("cleared", accent=CRIMSON, size=20)
        cleared_chip.next_to(d8, DOWN, buff=0.15)
        self.play(FadeIn(cleared_chip), run_time=0.4)
        self.wait(max(0.3, total - 0.7 - 0.5 - 0.4 - 1.2 - 0.4 - 0.4 - 1.0 - 0.9 - 0.4))


class B08_MechanismCard(Scene):
    """Section card: cleared / poisons healthy tissue."""
    def construct(self):
        total = DUR["B08"]
        t1 = Text("Cleared before it reaches the tumor.", font=DISPLAY,
                  color=INK, font_size=28, weight=BOLD)
        t2 = Text("Free payload poisons healthy tissue instead.", font=DISPLAY,
                  color=CRIMSON, font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.12, t2.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.3, total - 1.6))


class B09_OptimumCurve(Scene):
    """Optimum curve: DAR vs tumor delivery with both failure modes."""
    def construct(self):
        total = DUR["B09"]
        # axes
        ax = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 1.1, 0.5],
            x_length=9.0,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 2,
                         "include_tip": False,
                         "numbers_to_include": [0, 2, 4, 6, 8, 10]},
        )
        ax.move_to(DOWN * 0.3)
        x_label = Text("DAR", font=MONO, color=INK, font_size=22)
        x_label.next_to(ax.x_axis, DOWN, buff=0.4)
        y_label = Text("tumor drug delivery", font=SERIF, color=INK,
                       font_size=20, slant=ITALIC)
        y_label.next_to(ax.y_axis, LEFT, buff=0.15).rotate(PI / 2)

        # bell-ish curve peaking around DAR 5-6
        def delivery(x):
            return 0.95 * np.exp(-0.28 * (x - 5.5) ** 2)

        curve = ax.plot(delivery, x_range=[0.1, 10], color=INK, stroke_width=2.5)

        # teal shading under curve in sweet spot 4-8
        teal_area = ax.get_area(curve, x_range=[4, 8], color=TEAL, opacity=0.3)

        # crimson zones for the two failure sides
        crimson_l = ax.get_area(curve, x_range=[0.1, 4], color=CRIMSON, opacity=0.2)
        crimson_r = ax.get_area(curve, x_range=[8, 10], color=CRIMSON, opacity=0.2)

        # labels
        sweet_lbl = Text("sweet spot", font=SERIF, color=TEAL, font_size=20, slant=ITALIC)
        sweet_lbl.move_to(ax.c2p(5.5, 0.85))
        under_lbl = Text("under-delivers", font=SERIF, color=CRIMSON,
                         font_size=18, slant=ITALIC)
        under_lbl.move_to(ax.c2p(2.0, 0.5))
        over_lbl = Text("overloaded /", font=SERIF, color=CRIMSON,
                        font_size=18, slant=ITALIC)
        over_lbl2 = Text("cleared fast", font=SERIF, color=CRIMSON,
                         font_size=18, slant=ITALIC)
        over_block = VGroup(over_lbl, over_lbl2).arrange(DOWN, buff=0.1)
        over_block.move_to(ax.c2p(9.0, 0.5))

        self.play(Create(ax), FadeIn(x_label), FadeIn(y_label), run_time=0.9)
        self.play(Create(curve), run_time=1.0)
        self.play(FadeIn(teal_area), FadeIn(crimson_l), FadeIn(crimson_r), run_time=0.7)
        self.play(FadeIn(sweet_lbl), FadeIn(under_lbl), FadeIn(over_block), run_time=0.7)
        self.wait(max(0.3, total - 3.3))


class B10_ExamplePharma(Scene):
    """DAR-4 vs DAR-8 plasma levels at 24 hours (illustrative)."""
    def construct(self):
        total = DUR["B10"]
        # bar chart: two bars on a common baseline
        baseline_y = DOWN * 1.8
        bar_w = 1.8
        bar_max_h = 4.0
        lx = LEFT * 2.5
        rx = RIGHT * 2.5

        # baselines
        base = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=2)
        base.move_to(baseline_y)

        # percentage marks
        pct_100 = baseline_y + UP * bar_max_h
        tick_100 = Line(LEFT * 5.2, LEFT * 4.9, color=INK, stroke_width=1.5)
        tick_100.move_to(pct_100)
        lbl_100 = Text("100%", font=MONO, color=INK, font_size=18)
        lbl_100.next_to(tick_100, LEFT, buff=0.1)

        # DAR-4 bar at 68%
        h4 = bar_max_h * 0.68
        bar4 = _bar_rect(lx + baseline_y, bar_w, h4, TEAL)
        lbl4_pct = Text("68%", font=MONO, color=TEAL, font_size=32, weight=BOLD)
        lbl4_pct.next_to(bar4, UP, buff=0.2)
        lbl4_name = LabelChip("DAR 4", accent=TEAL, size=22)
        lbl4_name.next_to(base, DOWN, buff=0.25).shift(lx)

        # DAR-8 bar at 11%
        h8 = bar_max_h * 0.11
        bar8 = _bar_rect(rx + baseline_y, bar_w, h8, CRIMSON)
        lbl8_pct = Text("11%", font=MONO, color=CRIMSON, font_size=32, weight=BOLD)
        lbl8_pct.next_to(bar8, UP, buff=0.2)
        lbl8_name = LabelChip("DAR 8", accent=CRIMSON, size=22)
        lbl8_name.next_to(base, DOWN, buff=0.25).shift(rx)

        # title and illustrative note
        title_lbl = Text("plasma at 24 hours", font=SERIF, color=INK,
                         font_size=22, slant=ITALIC)
        title_lbl.move_to(UP * 2.4)
        illus_lbl = Text("illustrative", font=MONO, color=SLATE, font_size=18)
        illus_lbl.next_to(base, DOWN, buff=0.85)

        self.play(Create(base), FadeIn(tick_100), FadeIn(lbl_100),
                  FadeIn(title_lbl), FadeIn(illus_lbl), run_time=0.7)
        self.play(FadeIn(lbl4_name), FadeIn(lbl8_name), run_time=0.4)
        self.play(GrowFromEdge(bar4, DOWN), run_time=0.8)
        self.play(FadeIn(lbl4_pct), run_time=0.4)
        self.play(GrowFromEdge(bar8, DOWN), run_time=0.8)
        self.play(FadeIn(lbl8_pct), run_time=0.4)
        self.wait(max(0.3, total - 0.7 - 0.4 - 0.8 - 0.4 - 0.8 - 0.4))


class B11_ExampleTumor(Scene):
    """DOCUMENT beat -- quote card with tumor drug level numbers (illustrative)."""
    def construct(self):
        _quote_scene(self,
                     "DAR-4: 2.4 ug/g tumor   DAR-8: 0.3 ug/g tumor at 72 hours.",
                     "-- illustrative example (same antibody, same payload, same dose)",
                     None,
                     "0.3",
                     DUR["B11"])


class B12_End(Scene):
    """Endcard — DAR is an optimum not a maximum."""
    def construct(self):
        total = DUR["B12"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("DAR is an optimum, not a maximum.", font=DISPLAY,
                  color=INK, font_size=30, weight=BOLD)
        t2 = Text("Past the sweet spot, more warheads means less delivery.", font=DISPLAY,
                  color=CRIMSON, font_size=22, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.3).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.12, t2.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.3, total - 2.3))
