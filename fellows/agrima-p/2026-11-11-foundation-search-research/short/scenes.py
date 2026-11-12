"""
Portrait (9:16) Manim scenes for foundation-search-research-short

Ports of the seven graphic beats kept in the Short (B00B, B01, B04, B05, B07, B08,
B09). B02, B03 and B06 are dropped to fit the 3:00 Shorts cap (see short/FACTCHECK.md).
Stacked layouts for a 4.5 x 8.0 frame; same palette, copy and audio timing as the
16:9 scenes. All visuals are generated: no photos, no real people, no real brand or
company logos. The cosnova results are labeled company-reported; the late-night scene
and the deep-shade example are labeled illustrations.
"""

from manim import *
import numpy as np

config.frame_width = 4.5
config.frame_height = 8.0

PALETTE = {
    "bg":     "#FAF9F5",
    "ink":    "#3D3929",
    "accent": "#D97757",
    "good":   "#4A7C59",
    "miss":   "#C0392B",
    "card":   "#FFFFFF",
    "border": "#E8E4DA",
    "dim":    "#8B8878",
    "warm":   "#FBEFE3",
    "wood":   "#C9A27E",
}

SHADES = ["#F6E0CE", "#EFCDAE", "#E3B792", "#D49F78", "#BD8559", "#9A6840", "#744A2E", "#573622", "#3F2618"]

W = 3.7     # content width


def card_bg(width, height, stroke_color=None, fill=None):
    return RoundedRectangle(
        corner_radius=0.12, width=width, height=height,
        fill_color=fill or PALETTE["card"], fill_opacity=1,
        stroke_color=stroke_color or PALETTE["border"], stroke_width=1.5,
    )


def grow_in(scene, mob, target_width, run_time=0.5, **kwargs):
    mob.stretch(0.01, 0)
    scene.play(mob.animate.stretch_to_fit_width(target_width), run_time=run_time, **kwargs)


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


def fit_in(mob, max_w, max_h):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    if mob.height > max_h:
        mob.scale_to_fit_height(max_h)
    return mob


def lines(txt, fs, color, max_w=None, buff=0.08, weight=None):
    kw = {"weight": weight} if weight else {}
    g = VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split("\n")]).arrange(DOWN, buff=buff)
    return fit(g, max_w) if max_w else g


def reveal(scene, card, t1=0.35, t2=0.4):
    box, inner = card[0], card[1]
    w = box.width
    box.stretch(0.01, 0)
    scene.play(box.animate.stretch_to_fit_width(w), run_time=t1)
    scene.play(FadeIn(inner), run_time=t2)


def wait_until(scene, t):
    d = t - scene.renderer.time
    if d > 0.02:
        scene.wait(d)


def chip(label, w=2.6, h=0.5, border=None, color=None, fs=14):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(lines(label, fs, color or PALETTE["ink"], buff=0.05), w - 0.2)
    return VGroup(box, txt.move_to(box.get_center()))


def meter(w, frac, color, h=0.16):
    track = RoundedRectangle(corner_radius=0.07, width=w, height=h, fill_color=PALETTE["border"],
                              fill_opacity=1, stroke_width=0)
    fill = RoundedRectangle(corner_radius=0.07, width=max(w * frac, 0.2), height=h, fill_color=color,
                             fill_opacity=1, stroke_width=0).align_to(track, LEFT)
    return VGroup(track, fill)


def src_chip(label, w=3.2, border=None, color=None):
    return chip(label, w=w, h=0.34, border=border or PALETTE["dim"], color=color or PALETTE["dim"], fs=11)


def person(h=1.0, color=None):
    c = color or PALETTE["ink"]
    head = Circle(radius=0.26 * h, color=c, fill_color=c, fill_opacity=1, stroke_width=0)
    body = RoundedRectangle(corner_radius=0.18 * h, width=0.7 * h, height=0.8 * h,
                             fill_color=c, fill_opacity=1, stroke_width=0)
    return VGroup(head, body).arrange(DOWN, buff=0.05)


def tick(color=None, s=1.0, sw=4):
    t = VMobject(color=color or PALETTE["good"], stroke_width=sw)
    t.set_points_as_corners([[-0.1, 0.0, 0], [-0.02, -0.1, 0], [0.13, 0.12, 0]])
    return t.scale(s)


def cross(color=None, s=1.0, sw=3.5):
    c = color or PALETTE["miss"]
    return VGroup(Line([-0.09, -0.09, 0], [0.09, 0.09, 0], color=c, stroke_width=sw),
                  Line([-0.09, 0.09, 0], [0.09, -0.09, 0], color=c, stroke_width=sw)).scale(s)


def swatch(color, w=0.9, h=0.9, stroke=None):
    return RoundedRectangle(corner_radius=0.08, width=w, height=h, fill_color=color, fill_opacity=1,
                            stroke_color=stroke or PALETTE["ink"], stroke_width=1.5)


def face(r=1.0, tone="#D7AA8A"):
    head = Ellipse(width=1.5 * r, height=1.9 * r, fill_color=tone, fill_opacity=1,
                   stroke_color=PALETTE["ink"], stroke_width=2.5)
    eyes = VGroup(*[Dot(radius=0.06 * r, color=PALETTE["ink"]) for _ in range(2)]).arrange(RIGHT, buff=0.5 * r)
    eyes.move_to(head.get_center() + UP * 0.25 * r)
    smile = Arc(radius=0.32 * r, start_angle=PI * 1.2, angle=PI * 0.6, color=PALETTE["ink"], stroke_width=2.5)
    smile.move_to(head.get_center() + DOWN * 0.42 * r)
    return VGroup(head, eyes, smile)


def phone(w=2.0, h=3.2):
    body = RoundedRectangle(corner_radius=0.25, width=w, height=h, fill_color=PALETTE["card"], fill_opacity=1,
                            stroke_color=PALETTE["ink"], stroke_width=3)
    screen = RoundedRectangle(corner_radius=0.16, width=w - 0.24, height=h - 0.3, fill_color=PALETTE["bg"],
                              fill_opacity=1, stroke_width=0).move_to(body.get_center())
    return VGroup(body, screen)


def lock_icon(s=1.0, color=None):
    c = color or PALETTE["ink"]
    shackle = Arc(radius=0.3 * s, start_angle=0, angle=PI, color=c, stroke_width=6 * s)
    body = RoundedRectangle(corner_radius=0.08 * s, width=0.8 * s, height=0.62 * s, fill_color=c,
                            fill_opacity=1, stroke_width=0)
    shackle.next_to(body, UP, buff=-0.02)
    keyhole = Dot(radius=0.07 * s, color=PALETTE["card"]).move_to(body.get_center())
    return VGroup(shackle, body, keyhole)


def toggle(on=True, s=1.0):
    col = PALETTE["good"] if on else PALETTE["dim"]
    track = RoundedRectangle(corner_radius=0.25 * s, width=1.0 * s, height=0.5 * s, fill_color=col,
                             fill_opacity=1, stroke_width=0)
    knob = Circle(radius=0.19 * s, fill_color=PALETTE["card"], fill_opacity=1, stroke_width=0)
    knob.move_to(track.get_right() + LEFT * 0.25 * s if on else track.get_left() + RIGHT * 0.25 * s)
    return VGroup(track, knob)


# --- scenes -----------------------------------------------------------------

class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=34)
        summary = fit(lines("Today: how late-night\nshade testing helps\nbeauty brands decide\nwhat to make next.", 22,
                            PALETTE["ink"], buff=0.14), W)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        wait_until(self, 6.7)


class B01_LateNightTryOn(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        note = chip("illustration -- not a real case", w=3.4, h=0.4, border=PALETTE["ink"], color=PALETTE["ink"], fs=13)
        note.move_to([0, 3.15, 0])

        moon = VGroup(Circle(radius=0.22, fill_color=PALETTE["wood"], fill_opacity=1, stroke_width=0),
                      Circle(radius=0.19, fill_color=PALETTE["bg"], fill_opacity=1, stroke_width=0).shift(RIGHT * 0.13 + UP * 0.07))
        clock = chip("11:00 p.m.", w=1.5, h=0.42, border=PALETTE["ink"], color=PALETTE["ink"], fs=15)
        cookie = VGroup(Circle(radius=0.2, fill_color="#D8B07A", fill_opacity=1, stroke_color=PALETTE["wood"], stroke_width=2),
                        *[Dot(radius=0.025, color=PALETTE["ink"]).move_to(np.array(p)) for p in ((-0.07, 0.06, 0), (0.08, 0.02, 0), (0.0, -0.1, 0))])
        cookie_l = Text("snack", color=PALETTE["dim"], font_size=11)
        snack = VGroup(cookie, cookie_l).arrange(DOWN, buff=0.04)
        night = VGroup(moon, clock, snack).arrange(RIGHT, buff=0.3).move_to([0, 2.5, 0])

        ph = phone(2.0, 2.6).move_to([0, 0.75, 0])
        screen = ph[1]
        fc = face(0.6).move_to(screen.get_center() + UP * 0.2)
        tab = chip("try on", w=1.0, h=0.3, border=PALETTE["accent"], color=PALETTE["accent"], fs=11)
        tab.move_to(screen.get_top() + DOWN * 0.25)
        pale, orange, almost = "#F7E3D3", "#E0944F", "#D9AE8E"
        sw = VGroup(*[swatch(c, 0.42, 0.42) for c in (pale, orange, almost)]).arrange(RIGHT, buff=0.15)
        sw.move_to(screen.get_center() + DOWN * 0.75)

        def row(col, label, mark, mcol):
            s = swatch(col, 0.36, 0.36)
            t = Text(label, color=PALETTE["ink"], font_size=20)
            m = mark.copy().set_color(mcol)
            return VGroup(s, t, m).arrange(RIGHT, buff=0.25)
        r1 = row(pale, "too pale", cross(s=1.2), PALETTE["miss"])
        r2 = row(orange, "too orange", cross(s=1.2), PALETTE["miss"])
        r3 = row(almost, "almost right", tick(s=1.4), PALETTE["good"])
        rows = VGroup(r1, r2, r3).arrange(DOWN, buff=0.16, aligned_edge=LEFT).move_to([0, -1.5, 0])

        ding = VGroup(card_bg(1.5, 0.34, stroke_color=PALETTE["accent"]),
                      Text("new text", color=PALETTE["accent"], font_size=12))
        ding[1].move_to(ding[0].get_center())
        ding.move_to(tab.get_center())
        closed = chip("tab closed", w=1.4, h=0.36, border=PALETTE["dim"], color=PALETTE["dim"], fs=12)
        closed.move_to(screen.get_center())

        nothing = VGroup(cross(s=1.2), Text("bought nothing", color=PALETTE["ink"], font_size=20)).arrange(RIGHT, buff=0.2)
        nothing.move_to([0, -2.6, 0])
        clue_ring = Circle(radius=0.24, color=PALETTE["accent"], stroke_width=3)
        clue = Dot(radius=0.09, color=PALETTE["accent"])
        clue_txt = Text("a small clue just arrived", color=PALETTE["accent"], font_size=17, weight="BOLD")
        clue_row = VGroup(VGroup(clue_ring, clue), clue_txt).arrange(RIGHT, buff=0.2)
        fit(clue_row, W).move_to([0, -3.1, 0])

        self.play(FadeIn(night, shift=DOWN * 0.1), FadeIn(note), run_time=0.7)
        wait_until(self, 1.6)
        self.play(FadeIn(ph), FadeIn(fc), FadeIn(tab), run_time=0.8)
        wait_until(self, 5.9)
        self.play(FadeIn(sw, shift=UP * 0.1), run_time=0.6)
        wait_until(self, 8.9)
        self.play(FadeIn(r1, shift=LEFT * 0.15), run_time=0.45)
        wait_until(self, 10.1)
        self.play(FadeIn(r2, shift=LEFT * 0.15), run_time=0.45)
        wait_until(self, 11.7)
        self.play(FadeIn(r3, shift=LEFT * 0.15), run_time=0.45)
        wait_until(self, 13.2)
        self.play(FadeOut(tab), FadeIn(ding, shift=DOWN * 0.1), run_time=0.45)
        self.play(FadeOut(fc), FadeOut(sw), FadeOut(ding), FadeIn(closed), run_time=0.7)
        wait_until(self, 15.4)
        self.play(FadeIn(nothing, shift=RIGHT * 0.1), run_time=0.5)
        wait_until(self, 19.0)
        self.play(FadeIn(clue_row, shift=UP * 0.1), run_time=0.6)
        self.play(clue_ring.animate.scale(1.5).set_stroke(opacity=0.2), run_time=0.9)
        wait_until(self, 24.27)


class B04_CosnovaExample(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = chip("cosnova -- AI shade matching", w=3.4, h=0.4, border=PALETTE["ink"], color=PALETTE["ink"], fs=13)
        head.move_to([0, 3.15, 0])
        badge = chip("COMPANY-REPORTED", w=2.6, h=0.4, border=PALETTE["miss"], color=PALETTE["miss"], fs=13)
        badge.move_to([0, 2.65, 0])

        def card(big, bfs, label, col, extra, y):
            b = card_bg(W, 1.3)
            inner = VGroup(Text(big, color=col, font_size=bfs, weight="BOLD"),
                           Text(label, color=PALETTE["ink"], font_size=14), extra).arrange(DOWN, buff=0.1)
            return VGroup(b, fit_in(inner, W - 0.3, 1.15).move_to(b.get_center())).move_to([0, y, 0])

        c1 = card("over 90%", 34, "consumer satisfaction", PALETTE["accent"], meter(2.6, 0.9, PALETTE["accent"]), 1.5)
        up = Arrow([0, -0.12, 0], [0, 0.12, 0], buff=0, color=PALETTE["good"], stroke_width=5,
                   max_tip_length_to_length_ratio=0.8)
        c2 = card("20%+", 34, "increase in add-to-cart rates", PALETTE["good"], up, 0.05)
        dots = VGroup(*[Dot(radius=0.045, color=PALETTE["accent"]) for _ in range(20)]).arrange_in_grid(
            rows=2, cols=10, buff=0.09)
        c3 = card("tens of thousands", 22, "of shopper sessions", PALETTE["ink"], dots, -1.4)
        src = src_chip("Arbelle, 2026 -- reporting on cosnova", 3.5).move_to([0, -2.4, 0])
        foot = lines("Arbelle sells this technology:\ncompany-reported,\nnot independent research", 13,
                     PALETTE["miss"], buff=0.06, weight="BOLD").move_to([0, -3.0, 0])

        wait_until(self, 1.7)
        self.play(FadeIn(head, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 6.7)
        self.play(FadeIn(badge, shift=DOWN * 0.1), run_time=0.4)
        reveal(self, c1, t1=0.4, t2=0.4)
        wait_until(self, 10.7)
        reveal(self, c2, t1=0.4, t2=0.4)
        wait_until(self, 14.4)
        reveal(self, c3, t1=0.4, t2=0.4)
        self.play(FadeIn(src), run_time=0.3)
        wait_until(self, 18.1)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.6)
        wait_until(self, 24.1)


class B05_GapVisible(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        ex = chip("EXAMPLE -- not a real case", w=3.3, h=0.4, border=PALETTE["ink"], color=PALETTE["ink"], fs=13)
        ex.move_to([0, 3.25, 0])

        sws = VGroup(*[swatch(c, 0.36, 0.7, stroke=PALETTE["border"]) for c in SHADES]).arrange(RIGHT, buff=0.04)
        sws.move_to([0, 1.9, 0])
        deep = VGroup(*sws[-3:])
        box = SurroundingRectangle(deep, color=PALETTE["accent"], buff=0.05, stroke_width=3, corner_radius=0.08)
        tried = lines("tried again\nand again", 12, PALETTE["accent"], buff=0.04, weight="BOLD")
        tried.next_to(box, UP, buff=0.08).align_to(box, RIGHT)
        ticks = VGroup(*[tick(s=0.8).move_to(sws[i].get_bottom() + DOWN * 0.22) for i in range(6)])
        crosses = VGroup(*[cross(s=0.9).move_to(sws[i].get_bottom() + DOWN * 0.22) for i in range(6, 9)])
        bought = Text("bought", color=PALETTE["good"], font_size=12).next_to(ticks[2], DOWN, buff=0.06)
        left_b = lines("left without\nbuying", 12, PALETTE["miss"], buff=0.03).next_to(crosses[1], DOWN, buff=0.06)

        hint = chip("a hint: maybe no close\nmatch in the range", w=3.5, h=0.75, border=PALETTE["accent"],
                    color=PALETTE["accent"], fs=16).move_to([0, 0.1, 0])
        see = chip("try-on data makes\nit visible", w=3.5, h=0.75, border=PALETTE["good"], color=PALETTE["good"],
                   fs=16).move_to([0, -0.95, 0])

        def info(title, body, col, h):
            b = card_bg(W, h, stroke_color=col)
            inner = VGroup(Text(title, color=col, font_size=15, weight="BOLD"),
                           lines(body, 14, PALETTE["ink"], buff=0.06)).arrange(DOWN, buff=0.1)
            return VGroup(b, fit_in(inner, W - 0.3, h - 0.2).move_to(b.get_center()))
        k1 = info("Arbelle", "shoppers want to see themselves\nin shade ranges", PALETTE["accent"], 1.0).move_to([0, 0.2, 0])
        k2 = info("PwC", "narrow data can make shade\nmatchers miss mid-to-deep tones", PALETTE["good"], 1.0).move_to([0, -1.0, 0])
        k3 = info("so brands", "test across skin tones and\nkeep humans in the loop:\nbeauty advisors, dermatologists",
                  PALETTE["ink"], 1.3).move_to([0, -2.4, 0])
        close = lines("The data raises\nthe question.\nA person decides.", 28, PALETTE["ink"], buff=0.14,
                      weight="BOLD").move_to([0, -0.4, 0])

        self.play(FadeIn(ex), run_time=0.5)
        wait_until(self, 2.7)
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.1) for s in sws], lag_ratio=0.1), run_time=1.6)
        wait_until(self, 5.9)
        self.play(Create(box), FadeIn(tried), run_time=0.6)
        wait_until(self, 6.1)
        self.play(FadeIn(ticks), FadeIn(bought), run_time=0.4)
        self.play(FadeIn(crosses), FadeIn(left_b), run_time=0.5)
        wait_until(self, 8.0)
        self.play(FadeIn(hint, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 12.0)
        self.play(FadeIn(see, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 14.5)
        self.play(FadeOut(hint), FadeOut(see), run_time=0.3)
        reveal(self, k1, t1=0.35, t2=0.35)
        wait_until(self, 18.5)
        reveal(self, k2, t1=0.35, t2=0.35)
        wait_until(self, 23.9)
        reveal(self, k3, t1=0.35, t2=0.35)
        wait_until(self, 30.4)
        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), run_time=0.4)
        self.play(FadeIn(close, shift=UP * 0.1), run_time=0.6)
        wait_until(self, 33.69)


class B07_NeedsCare(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lk = lock_icon(1.0)
        lt = lines("a try-on uses\nyour face", 22, PALETTE["ink"], buff=0.06, weight="BOLD")
        head = VGroup(lk, lt).arrange(RIGHT, buff=0.35).move_to([0, 2.6, 0])

        sens = Text("sensitive information", color=PALETTE["dim"], font_size=13).move_to([0, 1.65, 0])
        c1 = chip("face scans", w=1.5, h=0.42, border=PALETTE["accent"], color=PALETTE["accent"], fs=14)
        c2 = chip("skin condition", w=1.9, h=0.42, border=PALETTE["accent"], color=PALETTE["accent"], fs=14)
        c3 = chip("behavior patterns", w=2.2, h=0.42, border=PALETTE["accent"], color=PALETTE["accent"], fs=14)
        r1 = VGroup(c1, c2).arrange(RIGHT, buff=0.15).move_to([0, 1.15, 0])
        c3.move_to([0, 0.6, 0])
        big = Text("about 7 in 10", color=PALETTE["accent"], font_size=34, weight="BOLD").move_to([0, -0.35, 0])
        dots = VGroup(*[Circle(radius=0.12, fill_color=PALETTE["accent"] if i < 7 else PALETTE["border"], fill_opacity=1,
                               stroke_width=0) for i in range(10)]).arrange(RIGHT, buff=0.1).move_to([0, -0.9, 0])
        apc = lines("in Asia Pacific say they are\nconcerned about how companies\ncollect their information", 14,
                    PALETTE["ink"], buff=0.06).move_to([0, -1.6, 0])
        src = src_chip("PwC Malaysia, 2026", 2.4).move_to([0, -2.4, 0])

        rh = Text("PwC's practical advice", color=PALETTE["good"], font_size=18, weight="BOLD").move_to([0, 1.95, 0])

        def adv(label):
            t = lines(label, 17, PALETTE["ink"], buff=0.05)
            return VGroup(tick(s=1.2), t).arrange(RIGHT, buff=0.25)
        a1 = adv("collect only what's\nnecessary")
        a2 = adv("explain what\nit's for")
        a3 = adv("process on the device\nwhen possible")
        a4 = adv("clear ways to opt out")
        advs = VGroup(a1, a2, a3, a4).arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to([0.1, -0.35, 0])
        tg_off = toggle(False, 1.0)
        tg_label = Text("opt out", color=PALETTE["dim"], font_size=16)
        tg = VGroup(tg_label, tg_off).arrange(RIGHT, buff=0.25).move_to([0, -2.75, 0])
        for r_ in (sens, r1, c3, big, dots, apc, src, rh, a1, a2, a3, a4, tg):
            r_.set_opacity(0)

        wait_until(self, 1.0)
        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.6)
        wait_until(self, 8.4)
        self.play(sens.animate.set_opacity(1), c1.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 9.5)
        self.play(c2.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 10.6)
        self.play(c3.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 12.1)
        self.play(big.animate.set_opacity(1), run_time=0.4)
        self.play(dots.animate.set_opacity(1), apc.animate.set_opacity(1), src.animate.set_opacity(1), run_time=1.0)
        wait_until(self, 16.6)
        self.play(*[FadeOut(m) for m in (sens, c1, c2, c3, big, dots, apc, src)], run_time=0.4)
        self.play(rh.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 18.2)
        self.play(a1.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 19.4)
        self.play(a2.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 21.2)
        self.play(a3.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 25.5)
        self.play(a4.animate.set_opacity(1), tg.animate.set_opacity(1), run_time=0.4)
        tg_on = toggle(True, 1.0).move_to(tg_off.get_center())
        self.play(Transform(tg_off, tg_on), tg_label.animate.set_color(PALETTE["good"]), run_time=0.6)
        wait_until(self, 27.28)


class B08_SameShadeChart(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        nots_l = chip("not a survey", w=1.45, h=0.4, border=PALETTE["dim"], color=PALETTE["dim"], fs=13)
        nots_r = chip("not a review", w=1.45, h=0.4, border=PALETTE["dim"], color=PALETTE["dim"], fs=13)
        nots = VGroup(VGroup(cross(s=1.0), nots_l).arrange(RIGHT, buff=0.1),
                      VGroup(cross(s=1.0), nots_r).arrange(RIGHT, buff=0.1)).arrange(RIGHT, buff=0.2).move_to([0, 3.1, 0])
        strikes = VGroup()

        chart_sw = VGroup(*[swatch(c, 0.62, 0.62, stroke=PALETTE["border"]) for c in SHADES]).arrange_in_grid(
            rows=3, cols=3, buff=0.08)
        chart_t = Text("shade chart", color=PALETTE["dim"], font_size=13)
        c_in = VGroup(chart_sw, chart_t).arrange(DOWN, buff=0.15)
        c_box = card_bg(2.5, 2.9, stroke_color=PALETTE["wood"])
        chart = VGroup(c_box, c_in.move_to(c_box.get_center())).move_to([0, 1.35, 0])

        shopper = person(1.0, PALETTE["accent"]).move_to([-1.1, -0.9, 0])
        sh_l = Text("the shopper", color=PALETTE["ink"], font_size=14, weight="BOLD").next_to(shopper, DOWN, buff=0.15)
        team = VGroup(*[person(0.8, PALETTE["ink"]) for _ in range(3)]).arrange(RIGHT, buff=0.08).move_to([1.0, -0.95, 0])
        tm_l = Text("the product team", color=PALETTE["ink"], font_size=14, weight="BOLD").next_to(team, DOWN, buff=0.15)
        sight_l = DashedLine(shopper.get_top() + UP * 0.08, chart.get_bottom() + DOWN * 0.05 + LEFT * 0.7,
                             color=PALETTE["accent"], stroke_width=3)
        sight_r = DashedLine(team.get_top() + UP * 0.08, chart.get_bottom() + DOWN * 0.05 + RIGHT * 0.7,
                             color=PALETTE["ink"], stroke_width=3)

        m_l = lines("better matches, a wider\nrange that includes them", 15, PALETTE["accent"], buff=0.06,
                    weight="BOLD").move_to([0, -2.65, 0])
        n_l = lines("a clearer idea of what\nto make next", 15, PALETTE["ink"], buff=0.06,
                    weight="BOLD").move_to([0, -3.15, 0])
        n_l.set_opacity(0)

        self.play(FadeIn(chart, shift=UP * 0.1), run_time=0.7)
        wait_until(self, 2.9)
        self.play(FadeIn(shopper), FadeIn(sh_l), run_time=0.5)
        self.play(FadeIn(team), FadeIn(tm_l), run_time=0.5)
        wait_until(self, 5.5)
        self.play(FadeIn(nots), run_time=0.5)
        wait_until(self, 7.8)
        self.play(Create(sight_l), Create(sight_r), run_time=0.8)
        wait_until(self, 12.6)
        self.play(FadeIn(m_l, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 16.5)
        self.play(n_l.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 19.11)


class B09_SourcesCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        def source(name, cite, note, col, h, y):
            hd = lines(name, 17, PALETTE["ink"], buff=0.05, weight="BOLD")
            c = lines(cite, 11, PALETTE["dim"], buff=0.04)
            n = chip(note, w=3.4, h=0.55, border=col, color=col, fs=12)
            inner = VGroup(hd, c, n).arrange(DOWN, buff=0.12)
            b = card_bg(W, h)
            g = VGroup(b, fit_in(inner, W - 0.3, h - 0.2).move_to(b.get_center())).move_to([0, y, 0])
            return g
        s1 = source("Arbelle\n(2026, January 19)", "Beauty consumer trends 2026:\nHow to win the modern beauty consumer",
                    "sells virtual try-on and shade-finder\ntechnology: results are company-reported",
                    PALETTE["miss"], 2.1, 1.45)
        s2 = source("Mani & Narayanan, PwC Malaysia\n(2026, May 19)",
                    "Beauty and the (AI) beast: The makeover of\npersonalisation, simplicity, and trust",
                    "a consulting firm's report focused on\nthe Asia Pacific market", PALETTE["accent"], 2.2, -0.75)
        ill = chip("illustrations, not real cases:\nthe late-night scene and\nthe deep-shade example", w=W, h=0.95,
                   border=PALETTE["ink"], color=PALETTE["ink"], fs=13).move_to([0, -2.6, 0])
        title = Text("A note on sources", color=PALETTE["ink"], font_size=22, weight="BOLD").move_to([0, 3.0, 0])
        s1[1][2].set_opacity(0)
        s2[1][2].set_opacity(0)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 1.7)
        reveal(self, s1, t1=0.4, t2=0.4)
        wait_until(self, 5.6)
        self.play(s1[1][2].animate.set_opacity(1), run_time=0.4)
        wait_until(self, 8.6)
        reveal(self, s2, t1=0.4, t2=0.4)
        self.play(s2[1][2].animate.set_opacity(1), run_time=0.4)
        wait_until(self, 12.3)
        self.play(FadeIn(ill, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 15.91)
