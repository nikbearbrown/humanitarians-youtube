"""terminal-velocity.py — Chapter 6, Drag Force and Terminal Speed.

A falling skydiver accelerates under constant gravity while speed-dependent
drag grows. When drag equals gravity, net force is zero and the diver falls
at constant speed — terminal velocity. Communicated entirely through arrow
length and afterimage spacing, black background per storyboard.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh terminal-velocity.py TerminalVelocity
  Portrait  (9:16): manim -r 1080,1920 --fps 60 --disable_caching terminal-velocity.py TerminalVelocity
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from medhavy_common import *

HERE = Path(__file__).parent
SHEET = json.loads((HERE / "beat_sheet.json").read_text())
DURS = {b["beat_id"]: b["actual_duration_s"] for b in SHEET["beats"]}
NARR = {b["beat_id"]: b["narration_text"] for b in SHEET["beats"]}

# module-level (before camera construction)
PORTRAIT = is_portrait()
FIGURE_COLOR = INK


def make_figure(scale=1.0, opacity=1.0):
    s = scale
    head = Circle(radius=0.13 * s, color=FIGURE_COLOR, fill_color=FIGURE_COLOR, fill_opacity=opacity, stroke_opacity=opacity)
    body = Line([0, 0.5 * s, 0], [0, 0, 0], color=FIGURE_COLOR, stroke_width=3, stroke_opacity=opacity)
    arm_l = Line([0, 0.4 * s, 0], [-0.35 * s, 0.55 * s, 0], color=FIGURE_COLOR, stroke_width=3, stroke_opacity=opacity)
    arm_r = Line([0, 0.4 * s, 0], [0.35 * s, 0.55 * s, 0], color=FIGURE_COLOR, stroke_width=3, stroke_opacity=opacity)
    leg_l = Line([0, 0, 0], [-0.3 * s, -0.35 * s, 0], color=FIGURE_COLOR, stroke_width=3, stroke_opacity=opacity)
    leg_r = Line([0, 0, 0], [0.3 * s, -0.35 * s, 0], color=FIGURE_COLOR, stroke_width=3, stroke_opacity=opacity)
    head.move_to([0, 0.63 * s, 0])
    return VGroup(head, body, arm_l, arm_r, leg_l, leg_r)


class TerminalVelocity(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        self.SCALE = 0.8 if self.PORTRAIT else 1.0
        self.FIG_X = 0.0

        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        # 1.4 (was 0.9): the initial afterimage trail above the figure was
        # clipped by the top of the frame
        self.top_y = safe_half_h() - 1.4
        self.bottom_y = -safe_half_h() + 1.4

        self.b00_hook()
        self.b01_drag_grows()
        self.b02_balance()
        self.b03_outro()

    # ---------------- shared: build figure + afterimages at position ----------------
    def _set_scene(self, y, spacing):
        s = self.SCALE
        fig = make_figure(s).move_to([self.FIG_X, y, 0])
        after = VGroup(*[
            make_figure(s, opacity=0.35 - 0.08 * i).move_to([self.FIG_X, y + spacing * (i + 1), 0])
            for i in range(3)
        ])
        return fig, after

    # ---------------- B00 — falling, gravity arrow fixed, spacing widening ----------------
    def b00_hook(self):
        s = self.SCALE
        y0 = self.top_y
        fig, after = self._set_scene(y0, 0.35)
        g_arrow = Arrow(
            [self.FIG_X + 0.5 * s, y0, 0], [self.FIG_X + 0.5 * s, y0 - 0.9 * s, 0],
            color=CRIMSON, buff=0, stroke_width=7,
        )
        g_label = crisp_text("F_gravity", font_size=18, color=CRIMSON).next_to(g_arrow, RIGHT, buff=0.15)

        self.play(FadeIn(after), FadeIn(fig), GrowArrow(g_arrow), FadeIn(g_label), run_time=1.0)
        self.fig, self.after, self.g_arrow, self.g_label = fig, after, g_arrow, g_label

        # widen spacing over the beat: figure + afterimages fall, spacing grows
        spacings = [0.35, 0.55, 0.8]
        n = len(spacings)
        step_t = max((DURS["B00"] - 1.0) / n, 0.3)
        for sp in spacings:
            new_y = self.fig.get_center()[1] - 0.45  # 0.45 (was 0.6) keeps the end position unchanged after the lower start
            new_fig = make_figure(s).move_to([self.FIG_X, new_y, 0])
            new_after = VGroup(*[
                make_figure(s, opacity=0.35 - 0.08 * i).move_to([self.FIG_X, new_y + sp * (i + 1), 0])
                for i in range(3)
            ])
            self.play(
                Transform(self.fig, new_fig), Transform(self.after, new_after),
                self.g_arrow.animate.move_to([self.FIG_X + 0.5 * s, new_y - 0.45 * s, 0]),
                self.g_label.animate.move_to(
                    [self.FIG_X + 0.5 * s + 0.15 + self.g_label.width / 2, new_y - 0.45 * s, 0]
                ),
                run_time=step_t,
            )

    # ---------------- B01 — drag arrow appears, grows in discrete steps ----------------
    def b01_drag_grows(self):
        s = self.SCALE
        fig_pos = self.fig.get_center()
        d_arrow = Arrow(
            [self.FIG_X - 0.5 * s, fig_pos[1], 0], [self.FIG_X - 0.5 * s, fig_pos[1] + 0.15 * s, 0],
            color=TEAL, buff=0, stroke_width=7,
        )
        d_label = crisp_text("F_drag", font_size=18, color=TEAL).next_to(d_arrow, LEFT, buff=0.15)
        self.play(GrowArrow(d_arrow), FadeIn(d_label), run_time=0.5)
        self.d_arrow, self.d_label = d_arrow, d_label

        lengths = [0.3, 0.45, 0.6]
        n = len(lengths)
        step_t = max((DURS["B01"] - 0.5) / n, 0.3)
        for ln in lengths:
            new_y = self.fig.get_center()[1] - 0.5
            new_fig = make_figure(s).move_to([self.FIG_X, new_y, 0])
            new_after = VGroup(*[
                make_figure(s, opacity=0.35 - 0.08 * i).move_to([self.FIG_X, new_y + 0.85 * (i + 1), 0])
                for i in range(3)
            ])
            new_d = Arrow(
                [self.FIG_X - 0.5 * s, new_y, 0], [self.FIG_X - 0.5 * s, new_y + ln * s, 0],
                color=TEAL, buff=0, stroke_width=7,
            )
            new_d_label = crisp_text("F_drag", font_size=18, color=TEAL).next_to(new_d, LEFT, buff=0.15)
            self.play(
                Transform(self.fig, new_fig), Transform(self.after, new_after),
                Transform(self.d_arrow, new_d), Transform(self.d_label, new_d_label),
                self.g_arrow.animate.move_to([self.FIG_X + 0.5 * s, new_y - 0.45 * s, 0]),
                self.g_label.animate.move_to([self.FIG_X + 0.5 * s + 0.15 + self.g_label.width / 2, new_y - 0.45 * s, 0]),
                run_time=step_t,
            )

    # ---------------- B02 — drag matches gravity, F_net = 0, even spacing ----------------
    def b02_balance(self):
        s = self.SCALE
        y = self.fig.get_center()[1] - 0.4
        new_fig = make_figure(s).move_to([self.FIG_X, y, 0])
        even_sp = 0.55
        new_after = VGroup(*[
            make_figure(s, opacity=0.35 - 0.08 * i).move_to([self.FIG_X, y + even_sp * (i + 1), 0])
            for i in range(3)
        ])
        new_g = Arrow(
            [self.FIG_X + 0.5 * s, y, 0], [self.FIG_X + 0.5 * s, y - 0.9 * s, 0],
            color=CRIMSON, buff=0, stroke_width=7,
        )
        new_d = Arrow(
            [self.FIG_X - 0.5 * s, y, 0], [self.FIG_X - 0.5 * s, y + 0.9 * s, 0],
            color=TEAL, buff=0, stroke_width=7,
        )
        guide = DashedLine(
            [self.FIG_X, y - 0.9 * s, 0], [self.FIG_X, y + 0.9 * s, 0], color=SLATE, stroke_width=1.5,
        )
        # right of the figure, above the F_gravity label (was centred on the
        # figure's x, drawn straight over the afterimages)
        net_label = crisp_text("F_net = 0", font_size=20, color=GOLD)
        net_label.move_to([self.FIG_X + 0.55 * s + 0.15 + net_label.width / 2, y + 0.55 * s, 0])

        self.play(
            Transform(self.fig, new_fig), Transform(self.after, new_after),
            Transform(self.g_arrow, new_g),
            self.g_label.animate.next_to(new_g, RIGHT, buff=0.15),
            Transform(self.d_arrow, new_d),
            self.d_label.animate.next_to(new_d, LEFT, buff=0.15),
            Create(guide),
            run_time=0.9,
        )
        self.play(FadeIn(net_label), run_time=0.5)
        self.guide, self.net_label = guide, net_label
        self.wait(max(DURS["B02"] - 1.4, 0.3))

    # ---------------- B03 — outro: hold, terminal velocity stamp ----------------
    def b03_outro(self):
        s = self.SCALE
        # Fixed near the top, well clear of the caption band at the bottom
        # (confirmed bug: placing this near bottom_y collided with the
        # burned-in caption rectangle in portrait).
        stamp_y = safe_half_h() - 1.0
        stamp = crisp_text("TERMINAL VELOCITY", font_size=26, color=INK).move_to([0, stamp_y, 0])
        sub = crisp_text("a = 0,  v = constant", font_size=18, color=GOLD).next_to(stamp, DOWN, buff=0.2)
        self.play(FadeIn(stamp), FadeIn(sub), run_time=0.6)
        self.wait(max(DURS["B03"] - 0.6, 0.3))
