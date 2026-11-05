"""inelastic-collision.py — Chapter 9, Types of Collisions.

2 kg at 4 m/s hits 2 kg at rest; they stick: v_f = 2 m/s. Momentum 8 -> 8
kg·m/s (conserved); kinetic energy 16 J -> 8 J (half becomes deformation,
heat and sound). Perfectly inelastic.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh inelastic-collision.py InelasticCollision
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching inelastic-collision.py InelasticCollision
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

C1, C2 = CRIMSON, TEAL
P_COLOR = INK
K_COLOR = CRIMSON
LOST = "#9A9A9A"


def hatch_rect(w, h, spacing=0.12):
    rect = Rectangle(width=w, height=h, stroke_color=SLATE, stroke_width=2, fill_color=LOST, fill_opacity=0.55)
    lines = VGroup()
    c = -h + spacing / 2
    while c < w:
        x0, x1 = max(c, 0), min(w, c + h)
        if x1 > x0:
            lines.add(Line([x0, x0 - c, 0], [x1, x1 - c, 0], color=INK, stroke_width=1.2))
        c += spacing
    lines.shift(rect.get_corner(DL))
    return VGroup(rect, lines)


class InelasticCollision(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        if self.PORTRAIT:
            self.cfg = dict(base=2.4, side=0.5, x1=-1.35, x2=0.0, va=0.8, fs=28, lfs=15,
                            bar_base=-1.9, bar_h=1.9, bar_w=0.5, px=[-1.3, -0.6], kx=[0.6, 1.3],
                            title_y=0.75, slot=np.array([0, 1.65, 0]))
        else:
            self.cfg = dict(base=1.3, side=1.1, x1=-5.0, x2=-0.5, va=1.4, fs=44, lfs=28,
                            bar_base=-2.7, bar_h=2.6, bar_w=0.9, px=[-5.8, -4.5], kx=[1.3, 2.6],
                            title_y=0.6, slot=np.array([-1.6, -1.1, 0]))

        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.b00_setup()
        self.b01_collide()
        self.b02_momentum()
        self.b03_energy()
        self.b04_hold()

    def block(self, color, label, width=None):
        c = self.cfg
        sq = Rectangle(width=width or c["side"], height=c["side"], color=INK, stroke_width=3,
                       fill_color=color, fill_opacity=1)
        t = MathTex(label, font_size=c["fs"] - 6, color=CREAM).move_to(sq)
        return VGroup(sq, t)

    def v_group(self, blk, length, tex):
        c = self.cfg
        y = blk.get_top()[1] + 0.25
        a = Arrow([blk.get_x() - length / 2, y, 0], [blk.get_x() + length / 2, y, 0], buff=0,
                  color=INK, stroke_width=6, max_tip_length_to_length_ratio=0.25)
        lab = MathTex(tex, font_size=c["fs"] - 4, color=INK).next_to(a, UP, buff=0.1)
        return VGroup(a, lab)

    # ---------------- B00 ----------------
    def b00_setup(self):
        c = self.cfg
        y = c["base"] + c["side"] / 2
        ground = Line([-safe_half_w(), c["base"], 0], [safe_half_w(), c["base"], 0], color=INK, stroke_width=5)
        b1 = self.block(C1, r"2\,\mathrm{kg}").move_to([c["x1"], y, 0])
        b2 = self.block(C2, r"2\,\mathrm{kg}").move_to([c["x2"], y, 0])
        v1 = self.v_group(b1, c["va"], r"v_1 = 4\ \mathrm{m/s}")
        v1.add_updater(lambda m: m.move_to([b1.get_x(), m.get_y(), 0]))
        self.play(Create(ground), FadeIn(b1), FadeIn(b2), run_time=1.0)
        self.play(FadeIn(v1), run_time=0.8)
        t_slide = 5.0
        self.wait(DURS["B00"] - 1.8 - t_slide)
        x_contact = c["x2"] - c["side"]
        self.play(b1.animate.move_to([x_contact, y, 0]), run_time=t_slide, rate_func=linear)
        v1.clear_updaters()
        self.speed = (x_contact - c["x1"]) / t_slide
        self.ground, self.b1, self.b2, self.v1 = ground, b1, b2, v1

    # ---------------- B01 ----------------
    def b01_collide(self):
        c = self.cfg
        y = c["base"] + c["side"] / 2
        contact = np.array([c["x2"] - c["side"] / 2, y, 0])
        burst = Star(n=8, outer_radius=0.45 * c["side"], inner_radius=0.22 * c["side"], color=INK,
                     stroke_width=2, fill_color=GOLD, fill_opacity=1).move_to(contact + UP * 0.05)
        burst.set_z_index(5)
        sq1 = Rectangle(width=c["side"], height=c["side"], stroke_width=0, fill_color=C1, fill_opacity=1)
        sq2 = sq1.copy().set_fill(C2)
        halves = VGroup(sq1, sq2).arrange(RIGHT, buff=0)
        outline = Rectangle(width=2 * c["side"], height=c["side"], color=INK, stroke_width=3)
        lab = MathTex(r"4\,\mathrm{kg}", font_size=c["fs"] - 4, color=CREAM)
        merged = VGroup(halves, outline, lab).move_to(contact)
        outline.move_to(halves)
        lab.move_to(halves)
        vf = self.v_group(merged, c["va"] / 2, r"v_f = 2\ \mathrm{m/s}")

        old = VGroup(self.b1, self.b2)
        self.remove(self.b1, self.b2)
        self.add(old)
        self.play(FadeIn(burst, scale=0.4), run_time=0.2)
        self.play(FadeOut(burst), ReplacementTransform(old, merged),
                  ReplacementTransform(self.v1, vf), run_time=0.8)
        T = DURS["B01"] - 1.0
        d = self.speed / 2 * T
        self.play(merged.animate.shift(RIGHT * d), vf.animate.shift(RIGHT * d), run_time=T, rate_func=linear)
        self.merged, self.vf = merged, vf

    # ---------------- bars ----------------
    def bar(self, x, frac, color):
        c = self.cfg
        h = max(frac * c["bar_h"], 0.001)
        r = Rectangle(width=c["bar_w"], height=h, stroke_color=INK, stroke_width=2.5, fill_color=color, fill_opacity=1)
        r.move_to([x, c["bar_base"], 0], aligned_edge=DOWN)
        return r

    def under(self, x, text):
        c = self.cfg
        return crisp_text(text, c["lfs"] - 2, color=SLATE, font=CAPTION_STYLE).move_to(
            [x, c["bar_base"] - 0.22, 0])

    def title(self, xs, text, color=INK):
        c = self.cfg
        t = crisp_text(text, c["lfs"], color=color, weight=BOLD, font=CAPTION_STYLE, line_spacing=1.0)
        t.move_to([(xs[0] + xs[1]) / 2, c["title_y"], 0])
        lim = safe_half_w()
        if t.get_right()[0] > lim:
            t.shift(LEFT * (t.get_right()[0] - lim))
        if t.get_left()[0] < -lim:
            t.shift(RIGHT * (-lim - t.get_left()[0]))
        return t

    # ---------------- B02 — momentum ----------------
    def b02_momentum(self):
        c = self.cfg
        px = c["px"]
        base_line = Line([px[0] - 0.7 * c["bar_w"], c["bar_base"], 0], [px[1] + 0.7 * c["bar_w"], c["bar_base"], 0],
                         color=INK, stroke_width=3)
        ttl = self.title(px, "momentum\n(kg·m/s)" if self.PORTRAIT else "momentum (kg·m/s)")
        pb = self.bar(px[0], 1.0, P_COLOR)
        pa = self.bar(px[1], 1.0, P_COLOR)
        vb = MathTex("8", font_size=c["fs"] - 4, color=INK).next_to(pb, UP, buff=0.08)
        va = MathTex("8", font_size=c["fs"] - 4, color=INK).next_to(pa, UP, buff=0.08)
        ub, ua = self.under(px[0], "before"), self.under(px[1], "after")
        eq = MathTex(r"m_1 v_1 = (m_1 + m_2)\,v_f", font_size=c["fs"] - 2, color=INK)
        eq2 = MathTex(r"(2)(4) = (4)(2) = 8", font_size=c["fs"] - 6, color=SLATE)
        eqg = VGroup(eq, eq2).arrange(DOWN, buff=0.15).move_to(c["slot"])
        if eqg.width > 2 * safe_half_w():
            eqg.scale_to_fit_width(2 * safe_half_w())
        self.play(FadeIn(ttl), Create(base_line), FadeIn(ub), FadeIn(ua), run_time=0.6)
        self.play(GrowFromEdge(pb, DOWN), FadeIn(vb), run_time=1.0)
        self.wait(5.0)
        self.play(GrowFromEdge(pa, DOWN), FadeIn(va), run_time=1.0)
        self.wait(1.5)
        self.play(Write(eqg), run_time=1.2)
        self.p_title, self.eqg = ttl, eqg
        self.p_group = VGroup(base_line, pb, pa, vb, va, ub, ua)
        self.wait(DURS["B02"] - 10.3)

    # ---------------- B03 — kinetic energy ----------------
    def b03_energy(self):
        c = self.cfg
        kx = c["kx"]
        base_line = Line([kx[0] - 0.7 * c["bar_w"], c["bar_base"], 0], [kx[1] + 0.7 * c["bar_w"], c["bar_base"], 0],
                         color=INK, stroke_width=3)
        ttl = self.title(kx, "kinetic energy\n(J)" if self.PORTRAIT else "kinetic energy (J)")
        kb = self.bar(kx[0], 1.0, K_COLOR)
        ka = self.bar(kx[1], 1.0, K_COLOR)
        vb = MathTex("16", font_size=c["fs"] - 4, color=INK).next_to(kb, UP, buff=0.08)
        ub, ua = self.under(kx[0], "before"), self.under(kx[1], "after")
        full_h = c["bar_h"]
        ghost = DashedVMobject(Rectangle(width=c["bar_w"], height=full_h, color=SLATE, stroke_width=2),
                               num_dashes=36).move_to([kx[1], c["bar_base"], 0], aligned_edge=DOWN)
        num = ValueTracker(16.0)
        # counter sits above the full-height outline, level with the "16", never over the lost piece
        va = always_redraw(lambda: Integer(round(num.get_value()), font_size=c["fs"] - 4, color=INK).next_to(
            ghost, UP, buff=0.08))
        lost = hatch_rect(c["bar_w"], full_h / 2).move_to([kx[1], c["bar_base"] + full_h, 0], aligned_edge=UP)

        self.play(FadeIn(ttl), Create(base_line), FadeIn(ub), FadeIn(ua), run_time=0.6)
        self.play(GrowFromEdge(kb, DOWN), FadeIn(vb), run_time=1.0)
        self.wait(4.0)
        self.add(ghost)
        self.play(FadeIn(ka), FadeIn(va), run_time=0.6)
        self.wait(1.0)
        self.add(lost)
        self.bring_to_front(ka)
        self.play(ka.animate.stretch_to_fit_height(full_h / 2, about_edge=DOWN), num.animate.set_value(8),
                  run_time=2.0, rate_func=linear)
        self.wait(2.5)
        heat = crisp_text("heat, deformation,\nsound", c["lfs"] - 1, color=SLATE, font=CAPTION_STYLE, line_spacing=1.05)
        if self.PORTRAIT:
            heat.move_to(c["slot"])
            anims = [FadeOut(self.eqg)]
        else:
            heat.next_to(ghost, RIGHT, buff=0.25).align_to(ghost, UP).shift(DOWN * 0.1)
            anims = []
        self.play(lost.animate.shift(UP * 0.6).set_opacity(0), FadeIn(heat), *anims, run_time=1.5)
        self.remove(lost)
        va.clear_updaters()
        self.k_title, self.heat = ttl, heat
        self.k_group = VGroup(base_line, kb, ka, vb, va, ub, ua, ghost)
        self.wait(DURS["B03"] - 13.2)

    # ---------------- B04 — verdicts ----------------
    def b04_hold(self):
        c = self.cfg
        if self.PORTRAIT:
            pt = self.title(c["px"], "momentum\nCONSERVED", TEAL)
            kt = self.title(c["kx"], "kinetic energy\nNOT CONSERVED", CRIMSON)
            summary_txt = "perfectly inelastic:\nobjects stick, kinetic\nenergy is lost, momentum is not"
            out = self.heat
        else:
            pt = self.title(c["px"], "momentum: CONSERVED", TEAL)
            kt = self.title(c["kx"], "kinetic energy: NOT CONSERVED", CRIMSON)
            summary_txt = "perfectly inelastic:\nobjects stick, kinetic energy\nis lost, momentum is not"
            out = self.eqg
        summary = crisp_text(summary_txt, c["lfs"], color=INK, font=CAPTION_STYLE, line_spacing=1.1).move_to(c["slot"])
        max_w = 2 * safe_half_w() if self.PORTRAIT else 4.0
        if summary.width > max_w:
            summary.scale_to_fit_width(max_w)
        self.play(ReplacementTransform(self.p_title, pt), ReplacementTransform(self.k_title, kt), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(out), run_time=0.5)
        self.play(FadeIn(summary), run_time=1.0)
        self.wait(DURS["B04"] - 4.5)
