"""steel-ship-buoyancy.py — Chapter 14, 14.4 Archimedes' Principle and Buoyancy.

A solid steel block displaces only its own volume and sinks (F_B ≈ W/8).
The same steel reshaped into a hollow hull displaces far more water and
settles until F_B = w_fl = W: it floats.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh steel-ship-buoyancy.py SteelShipBuoyancy
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching steel-ship-buoyancy.py SteelShipBuoyancy
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

PORTRAIT = is_portrait()

WATER = "#56B4E9"       # Okabe-Ito sky blue
SURFACE = "#0072B2"     # Okabe-Ito blue
STEEL = "#8C8C8C"

# ---- design-space geometry (landscape units), mapped to screen by P() ----
RHO_RATIO = 7.86                 # iron / water, Table 14.1
S = 0.9                          # block side
A_STEEL = S * S
HW, HH = 3.8, 2.3                # hull outer width, height
# wall thickness t so that the U-shaped hull has the block's steel area:
# HW*HH - (HW-2t)(HH-t) = A_STEEL  ->  2t^2 - (HW+2HH)t + A_STEEL = 0
_b = HW + 2 * HH
T = (_b - np.sqrt(_b * _b - 8 * A_STEEL)) / 4
H_SUB = RHO_RATIO * A_STEEL / HW  # submerged depth when floating
YS, YF = 0.6, -3.0               # water surface, pool floor
# block column, hull column (portrait: pulled in so the block's labels and the
# hull stay inside the narrow frame instead of touching the pool walls)
XB, XH = (-1.9, 1.3) if PORTRAIT else (-3.0, 1.6)
W_LEN = 1.6                      # weight arrow length (same steel -> same W)
Y_MID = -0.6                     # block center when shown submerged mid-water

if PORTRAIT:
    K = 0.47
    OFF = np.array([-0.012, -0.59, 0])
    LBL, EQ, TXT = 28, 34, 17
    SLOTS = [np.array([0, 2.75, 0]), np.array([0, 1.85, 0])]
else:
    K = 1.0
    OFF = np.array([0.0, -0.3, 0])
    LBL, EQ, TXT = 40, 50, 30
    SLOTS = [np.array([-3.0, 2.75, 0]), np.array([-3.0, 1.75, 0])]


def P(x, y):
    return OFF + K * np.array([x, y, 0.0])


def fit(m):
    maxw = 2 * safe_half_w() if PORTRAIT else 5.5
    if m.width > maxw:
        m.scale_to_fit_width(maxw)
    return m


def block_at(cx, cy):
    return Square(side_length=K * S, color=INK, fill_color=STEEL, fill_opacity=1,
                  stroke_width=2.5).move_to(P(cx, cy))


def hull_at(cx, yb):
    h = [(-HW / 2, HH), (-HW / 2, 0), (HW / 2, 0), (HW / 2, HH), (HW / 2 - T, HH),
         (HW / 2 - T, T), (-HW / 2 + T, T), (-HW / 2 + T, HH)]
    return Polygon(*[P(cx + x, yb + y) for x, y in h], color=INK, fill_color=STEEL,
                   fill_opacity=1, stroke_width=2.5)


def air_at(cx, yb):
    # hull interior is air: mask the water so it does not appear inside the hull
    return Polygon(P(cx - HW / 2 + T, yb + T), P(cx + HW / 2 - T, yb + T),
                   P(cx + HW / 2 - T, yb + HH), P(cx - HW / 2 + T, yb + HH),
                   stroke_width=0, fill_color=CREAM, fill_opacity=1)


def ghost(x0, x1, y0, y1):
    r = Polygon(P(x0, y0), P(x1, y0), P(x1, y1), P(x0, y1), stroke_width=0,
                fill_color=TEAL, fill_opacity=0.22)
    outline = DashedVMobject(Polygon(P(x0, y0), P(x1, y0), P(x1, y1), P(x0, y1), color=TEAL,
                                     stroke_width=3), num_dashes=36)
    return VGroup(r, outline)


def arrow(a, b, color, sw=7, ratio=0.2):
    return Arrow(a, b, buff=0, color=color, stroke_width=sw, max_tip_length_to_length_ratio=ratio,
                 max_stroke_width_to_length_ratio=40)


class SteelShipBuoyancy(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])
        self.b00_sink()
        self.b01_ship()
        self.b02_archimedes()
        self.b03_reshape()
        self.b04_balance()
        self.b05_hold()

    # ---------------- B00 — block sinks ----------------
    def b00_sink(self):
        xl, xr = -safe_half_w(), safe_half_w()
        ys, yf = P(0, YS)[1], P(0, YF)[1]
        water = Rectangle(width=xr - xl, height=ys - yf, stroke_width=0, fill_color=WATER,
                          fill_opacity=0.45).move_to([0, (ys + yf) / 2, 0])
        amp, k = 0.035, 2 * PI / (0.9 if PORTRAIT else 1.4)
        surface = ParametricFunction(lambda t: np.array([t, ys + amp * np.sin(k * t), 0]),
                                     t_range=[xl, xr], color=SURFACE, stroke_width=4)
        walls = VMobject(color=INK, stroke_width=5).set_points_as_corners(
            [[xl, ys + 0.35, 0], [xl, yf, 0], [xr, yf, 0], [xr, ys + 0.35, 0]])
        self.water, self.surface, self.walls = water, surface, walls
        self.play(FadeIn(water), Create(surface), Create(walls), run_time=1.0)

        self.block = block_at(XB, YS + 1.3)
        self.block_lbl = crisp_text("steel", 11 if PORTRAIT else 22, color=INK, font=CAPTION_STYLE)
        self.block_lbl.add_updater(lambda m: m.move_to(self.block.get_center()))
        self.play(FadeIn(self.block), FadeIn(self.block_lbl), run_time=0.4)
        self.play(self.block.animate.move_to(P(XB, YS)), run_time=0.5, rate_func=rush_into)

        bubbles = VGroup(*[Circle(radius=K * r, color=SURFACE, stroke_width=2).move_to(P(XB + dx, YS - 0.3))
                           for r, dx in ((0.08, -0.2), (0.06, 0.15), (0.05, -0.05), (0.07, 0.25))])
        self.play(self.block.animate.move_to(P(XB, YF + S / 2)),
                  LaggedStart(*[b.animate(rate_func=linear).shift(UP * K * 0.25).set_opacity(0) for b in bubbles],
                              lag_ratio=0.25),
                  run_time=2.0, rate_func=smooth)
        self.remove(bubbles)
        self.wait(max(DURS["B00"] - 3.9, 0.1))

    # ---------------- B01 — same steel, a ship floats ----------------
    def b01_ship(self):
        yb = YS - H_SUB
        hull = hull_at(XH, yb)
        air = air_at(XH, yb)
        mast = Line(P(XH, yb + T), P(XH, yb + HH + 0.9), color=INK, stroke_width=4)
        flag = Polygon(P(XH, yb + HH + 0.9), P(XH + 0.55, yb + HH + 0.75), P(XH, yb + HH + 0.6),
                       color=INK, fill_color=CRIMSON, fill_opacity=1, stroke_width=1.5)
        self.ship = VGroup(air, mast, hull, flag)
        self.ship_lbl = crisp_text("same steel", TXT, color=CRIMSON, font=CAPTION_STYLE).next_to(
            hull, RIGHT if not PORTRAIT else UP, buff=0.15)
        if PORTRAIT:
            self.ship_lbl.next_to(flag, UP, buff=0.12)
        self.play(FadeIn(self.ship, shift=DOWN * 0.2), run_time=1.0)
        self.play(FadeIn(self.ship_lbl), run_time=0.5)
        self.wait(max(DURS["B01"] - 1.5, 0.1))

    # ---------------- B02 — Archimedes: block displaces only its own volume ----------------
    def b02_archimedes(self):
        self.play(FadeOut(self.ship), FadeOut(self.ship_lbl), run_time=0.5)
        self.play(self.block.animate.move_to(P(XB, Y_MID)), run_time=0.8)
        g = ghost(XB - S / 2 - 0.07, XB + S / 2 + 0.07, Y_MID - S / 2 - 0.07, Y_MID + S / 2 + 0.07)
        self.add(g)
        self.bring_to_front(self.block, self.block_lbl)
        self.play(FadeIn(g), run_time=0.6)
        # right of the ghost (above the W label): above it collides with the surface line
        g_lbl = crisp_text("displaced\nwater", TXT - 2, color=TEAL, font=CAPTION_STYLE, line_spacing=1.0)
        g_lbl.next_to(g, RIGHT, buff=0.12).align_to(g, UP)
        self.play(FadeIn(g_lbl), run_time=0.3)
        self.b_ghost = VGroup(g, g_lbl)

        yb = Y_MID - S / 2
        w = arrow(P(XB + 0.22, yb), P(XB + 0.22, yb - W_LEN), INK)
        # tip on the ghost's lower edge (not inside it), label centered below the tail
        gy = yb - 0.07
        fb = arrow(P(XB - 0.38, gy - W_LEN / RHO_RATIO), P(XB - 0.38, gy), TEAL, ratio=0.6)
        w_lbl = MathTex("W", font_size=LBL, color=INK).next_to(w, RIGHT, buff=0.12)
        fb_lbl = MathTex("F_B", font_size=LBL, color=TEAL).next_to(fb, DOWN, buff=0.1)
        self.play(GrowArrow(w), FadeIn(w_lbl), run_time=0.5)
        self.play(GrowArrow(fb), FadeIn(fb_lbl), run_time=0.5)
        self.b_arrows = VGroup(w, fb, w_lbl, fb_lbl)

        self.eq1 = fit(MathTex(r"F_B = w_{\text{fl}} \approx \tfrac{1}{8}\,W", font_size=EQ, color=INK)).move_to(SLOTS[0])
        self.play(Write(self.eq1), run_time=0.8)
        self.wait(max(DURS["B02"] - 5.4, 0.1))
        self.play(FadeOut(self.b_arrows), FadeOut(self.b_ghost), run_time=0.4)
        self.play(self.block.animate.move_to(P(XB, YF + S / 2)), run_time=1.0, rate_func=rush_into)

    # ---------------- B03 — same steel, hollow hull ----------------
    def b03_reshape(self):
        self.play(FadeOut(self.eq1), run_time=0.4)
        self.play(self.block.animate.move_to(P(XB, YS + 1.0)), run_time=1.2)
        self.block_lbl.clear_updaters()

        y_above = YS + 0.3
        hull_static = hull_at(XH, y_above)
        self.play(ReplacementTransform(self.block, hull_static), FadeOut(self.block_lbl), run_time=1.5)

        self.hy = ValueTracker(y_above)
        self.air = always_redraw(lambda: air_at(XH, self.hy.get_value()))
        self.h_ghost = always_redraw(lambda: ghost(XH - HW / 2, XH + HW / 2, self.hy.get_value(), YS)
                                     if self.hy.get_value() < YS - 0.02 else VGroup())
        self.hull = always_redraw(lambda: hull_at(XH, self.hy.get_value()))
        self.remove(hull_static)
        self.add(self.air, self.h_ghost, self.hull)
        self.play(self.hy.animate.set_value(YS - H_SUB), run_time=2.0, rate_func=smooth)

        self.same_lbl = crisp_text("same steel, same mass", TXT, color=INK, font=CAPTION_STYLE)
        self.same_lbl.next_to(self.hull, UP, buff=0.2)
        yb = YS - H_SUB
        self.hg_lbl = crisp_text("displaced\nwater" if PORTRAIT else "displaced water", TXT - 2, color=TEAL,
                                 font=CAPTION_STYLE, line_spacing=1.0)
        # left edge pinned just inside the hull's inner wall, bottom just above its floor
        self.hg_lbl.next_to(P(XH - HW / 2 + T, yb + T), UR, buff=0.1)
        self.play(FadeIn(self.same_lbl), FadeIn(self.hg_lbl), run_time=0.5)
        self.wait(max(DURS["B03"] - 5.6, 0.1))

    # ---------------- B04 — balance ----------------
    def b04_balance(self):
        yb = YS - H_SUB
        w = arrow(P(XH, yb + T + 0.05 + W_LEN), P(XH, yb + T + 0.05), INK, ratio=0.2)
        fb = arrow(P(XH, yb - W_LEN), P(XH, yb), TEAL, sw=9, ratio=0.2)
        w_lbl = MathTex("W", font_size=LBL, color=INK).next_to(w, RIGHT, buff=0.12)
        fb_lbl = MathTex("F_B", font_size=LBL, color=TEAL).next_to(fb, RIGHT, buff=0.12)
        extra = []
        if self.PORTRAIT:
            # narrow hull: the 'displaced water' label would touch the W arrow
            extra = [FadeOut(self.hg_lbl)]
        self.play(GrowArrow(w), FadeIn(w_lbl), GrowArrow(fb), FadeIn(fb_lbl), *extra, run_time=1.0)
        self.h_arrows = VGroup(w, fb, w_lbl, fb_lbl)

        self.eq2 = fit(MathTex(r"F_B = w_{\text{fl}} = W", font_size=EQ, color=INK)).move_to(SLOTS[0])
        self.eq3 = fit(MathTex(r"\bar{\rho}_{\text{ship}} < \rho_{\text{water}}", font_size=EQ,
                               color=TEAL)).move_to(SLOTS[1])
        self.play(Write(self.eq2), run_time=0.8)
        self.play(Write(self.eq3), run_time=0.8)
        self.wait(max(DURS["B04"] - 2.6, 0.1))

    # ---------------- B05 — hold: same steel, different shape ----------------
    def b05_hold(self):
        self.play(FadeOut(self.eq2), FadeOut(self.eq3), FadeOut(self.same_lbl), FadeOut(self.h_arrows),
                  run_time=0.5)
        block = block_at(XB, YF + S / 2)
        sinks = crisp_text("sinks", TXT, color=INK, font=CAPTION_STYLE).next_to(block, UP, buff=0.15)
        floats = crisp_text("floats", TXT, color=INK, font=CAPTION_STYLE).next_to(self.hull, UP, buff=0.2)
        self.play(FadeIn(block), run_time=0.6)
        self.play(FadeIn(sinks), FadeIn(floats), run_time=0.5)
        summary = crisp_text("SAME STEEL, DIFFERENT SHAPE", TXT + 4, color=INK, font=CAPTION_STYLE)
        fit(summary).move_to(SLOTS[0])
        self.play(FadeIn(summary), run_time=0.6)
        self.end_group = VGroup(block, sinks, floats, summary)
        self.wait(max(DURS["B05"] - 2.2, 0.1))
