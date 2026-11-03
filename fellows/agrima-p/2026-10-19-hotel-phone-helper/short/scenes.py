"""
Portrait (9:16) Manim scenes for hotel-phone-helper-short

Ports of the eight graphic beats kept in the Shorts cut (B00B, B01, B04, B05,
B06, B09, B10, B11). Stacked layouts for a 4.5 x 8.0 frame; same palette and
copy as the 16:9 scenes. Dropped beats (B02, B03, B07, B08) live only in the
long cut. All visuals are generated; no real hotel brand logos.
"""

from manim import *
import numpy as np

config.frame_width = 4.5
config.frame_height = 8.0

SAFE_W = 3.7

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
    "floor":  "#EADBC6",
}


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


def lines(txt, fs, color, max_w=None, buff=0.1, weight=None):
    kw = {"weight": weight} if weight else {}
    g = VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split("\n")]).arrange(DOWN, buff=buff)
    return fit(g, max_w) if max_w else g


def reveal(scene, card, t1=0.35, t2=0.4):
    box, inner = card[0], card[1]
    w = box.width
    box.stretch(0.01, 0)
    scene.play(box.animate.stretch_to_fit_width(w), run_time=t1)
    scene.play(FadeIn(inner), run_time=t2)


def chip(label, w=2.6, h=0.45, border=None, color=None, fs=12):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(Text(label, color=color or PALETTE["ink"], font_size=fs), w - 0.2)
    return VGroup(box, txt.move_to(box.get_center()))


# --- icons ------------------------------------------------------------------

def person(h=1.0, color=None, smile=False):
    c = color or PALETTE["ink"]
    head = Circle(radius=0.26 * h, color=c, fill_color=c, fill_opacity=1, stroke_width=0)
    body = RoundedRectangle(corner_radius=0.18 * h, width=0.7 * h, height=0.8 * h,
                             fill_color=c, fill_opacity=1, stroke_width=0)
    g = VGroup(head, body).arrange(DOWN, buff=0.05)
    if smile:
        sm = Arc(radius=0.12 * h, start_angle=PI * 1.15, angle=PI * 0.7, color=PALETTE["card"], stroke_width=2)
        sm.move_to(head.get_center() + DOWN * 0.03 * h)
        g.add(sm)
    return g


def suitcase(h=0.4, color=None):
    c = color or PALETTE["wood"]
    body = RoundedRectangle(corner_radius=0.05, width=h * 0.8, height=h, fill_color=c, fill_opacity=1,
                             stroke_width=0)
    handle = Arc(radius=h * 0.18, start_angle=0, angle=PI, color=PALETTE["dim"], stroke_width=2)
    handle.move_to(body.get_top() + UP * h * 0.08)
    return VGroup(body, handle)


def phone_icon(color=None, h=0.9):
    c = color or PALETTE["ink"]
    body = RoundedRectangle(corner_radius=0.08 * h, width=0.5 * h, height=h, fill_color=PALETTE["card"],
                             fill_opacity=1, stroke_color=c, stroke_width=2.5)
    screen = RoundedRectangle(corner_radius=0.04 * h, width=0.36 * h, height=0.62 * h, fill_color=PALETTE["bg"],
                               fill_opacity=1, stroke_width=0).move_to(body.get_center() + UP * 0.04 * h)
    dot = Dot(body.get_bottom() + UP * 0.1 * h, radius=0.03 * h, color=c)
    return VGroup(body, screen, dot)


def ring_arcs(center, color=None, s=0.5):
    c = color or PALETTE["accent"]
    arcs = VGroup()
    for r in (0.35 * s, 0.6 * s):
        arcs.add(Arc(radius=r, start_angle=-PI / 4, angle=PI / 2, color=c, stroke_width=3).move_to(center + RIGHT * r * 0.6))
        arcs.add(Arc(radius=r, start_angle=PI - PI / 4, angle=PI / 2, color=c, stroke_width=3).move_to(center + LEFT * r * 0.6))
    return arcs


def bubble(text, fs=12, border=None, fill=None, w=None, color=None):
    t = Text(text, color=color or PALETTE["ink"], font_size=fs)
    ww = (w or (t.width + 0.4))
    box = RoundedRectangle(corner_radius=0.14, width=ww, height=0.42, fill_color=fill or PALETTE["card"],
                           fill_opacity=1, stroke_color=border or PALETTE["border"], stroke_width=1.5)
    if w and t.width > w - 0.2:
        t.scale_to_fit_width(w - 0.2)
    return VGroup(box, t.move_to(box.get_center()))


def helper_icon(color=None, s=1.0):
    c = color or PALETTE["accent"]
    box = RoundedRectangle(corner_radius=0.14, width=0.95, height=0.7, fill_color=PALETTE["card"],
                           fill_opacity=1, stroke_color=c, stroke_width=3)
    dots = VGroup(*[Dot(radius=0.05, color=c) for _ in range(3)]).arrange(RIGHT, buff=0.12).move_to(box.get_center())
    tail = Polygon([-0.1, 0, 0], [0.1, 0, 0], [0, -0.16, 0], color=c, fill_color=PALETTE["card"],
                   fill_opacity=1, stroke_width=3).next_to(box, DOWN, buff=-0.02).shift(LEFT * 0.2)
    return VGroup(tail, box, dots).scale(s)


def hotel_icon(scale=1.0, color=None):
    c = color or PALETTE["dim"]
    body = Rectangle(width=0.9, height=1.2, fill_color=c, fill_opacity=0.85, stroke_width=0)
    wins = VGroup(*[Rectangle(width=0.14, height=0.16, fill_color=PALETTE["warm"], fill_opacity=1, stroke_width=0)
                    for _ in range(9)]).arrange_in_grid(rows=3, cols=3, buff=0.14).move_to(body.get_center() + UP * 0.12)
    door = Rectangle(width=0.2, height=0.24, fill_color=PALETTE["warm"], fill_opacity=1, stroke_width=0)
    door.move_to(body.get_bottom() + UP * 0.12)
    return VGroup(body, wins, door).scale(scale)


def desk(w=3.6, h=0.9):
    top = RoundedRectangle(corner_radius=0.06, width=w, height=h, fill_color=PALETTE["wood"], fill_opacity=1,
                            stroke_width=0)
    trim = Rectangle(width=w, height=0.08, fill_color=PALETTE["ink"], fill_opacity=0.25, stroke_width=0)
    trim.align_to(top, UP)
    return VGroup(top, trim)


def lobby_panel(w, h):
    panel = RoundedRectangle(corner_radius=0.14, width=w, height=h, fill_color=PALETTE["warm"], fill_opacity=1,
                             stroke_color=PALETTE["border"], stroke_width=1.5)
    floor = Rectangle(width=w - 0.04, height=0.7, fill_color=PALETTE["floor"], fill_opacity=1, stroke_width=0)
    floor.move_to(panel.get_bottom() + UP * 0.37)
    lamp = VGroup(Line(UP * 0.35, ORIGIN, color=PALETTE["dim"], stroke_width=2),
                  Polygon([-0.18, 0, 0], [0.18, 0, 0], [0.1, -0.18, 0], [-0.1, -0.18, 0], fill_color=PALETTE["accent"],
                          fill_opacity=0.7, stroke_width=0))
    lamp.move_to(panel.get_top() + DOWN * 0.3 + LEFT * (w * 0.32))
    return panel, floor, lamp


# --- scenes -----------------------------------------------------------------

class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = fit(Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=38), 3.4)
        summary = lines("Today: the hotel phone,\nand the AI helpers now\nanswering it. Not replacing\nthe front desk, but giving it\nmore time for guests.",
                        22, PALETTE["ink"], max_w=3.4, buff=0.2)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        VGroup(name, rule, summary).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.4)


class B01_FridayAfternoon(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        panel, floor, lamp = lobby_panel(3.9, 5.4)
        panel.move_to(UP * 0.5)
        floor.move_to(panel.get_bottom() + UP * 0.37)
        ft = floor.get_top()[1]

        dk = desk(2.0, 0.8).move_to([0.8, ft + 0.4, 0])
        t1 = person(0.85, PALETTE["ink"], smile=True).move_to([0.3, dk.get_top()[1] + 0.5, 0])
        t2 = person(0.85, PALETTE["accent"], smile=True).move_to([1.1, dk.get_top()[1] + 0.5, 0])
        guests = VGroup(*[person(0.62, c) for c in (PALETTE["dim"], PALETTE["good"], PALETTE["accent"])])
        for i, g in enumerate(guests):
            g.move_to([-1.6 + 0.5 * i, ft + 0.5, 0])
        cases = VGroup(*[suitcase(0.26).move_to([-1.6 + 0.5 * i + 0.22, ft + 0.2, 0]) for i in range(3)])
        ph = phone_icon(h=0.5).move_to([1.7, dk.get_top()[1] + 0.3, 0])
        rings = ring_arcs(ph.get_center(), s=0.7)

        qs = VGroup(bubble("What time does the pool close?", fs=12, w=3.3),
                    bubble("Can I get a late checkout?", fs=12, w=3.3),
                    bubble("Is there a table free tonight?", fs=12, w=3.3)).arrange(DOWN, buff=0.2)
        qs.move_to([0, 1.7, 0])
        note = chip("an illustration, not a reported case", w=3.5, h=0.4, border=PALETTE["ink"],
                    color=PALETTE["ink"], fs=11)
        note.move_to([0, floor.get_center()[1], 0])

        reveal(self, VGroup(panel, VGroup(floor, lamp)))
        self.play(FadeIn(VGroup(dk, t1, t2), shift=UP * 0.1), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(g, shift=RIGHT * 0.2) for g in guests], lag_ratio=0.3),
                  FadeIn(cases), run_time=1.2)
        self.play(FadeIn(ph), run_time=0.4)
        self.play(FadeIn(rings), run_time=0.4)
        for q in qs:
            self.play(FadeIn(q, shift=DOWN * 0.15), run_time=0.5)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(1.2)


class B04_WhatItCanDo(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        fh = Text("the call flow", color=PALETTE["dim"], font_size=11)
        ph = VGroup(phone_icon(h=0.6), Text("call comes in", color=PALETTE["ink"], font_size=10)).arrange(DOWN, buff=0.1)
        ai = VGroup(helper_icon(s=0.7), Text("AI answers", color=PALETTE["accent"], font_size=11, weight="BOLD")
                    ).arrange(DOWN, buff=0.15)
        top_row = VGroup(ph, ai).arrange(RIGHT, buff=0.6)
        done = chip("handled: booking\nor question".replace("\n", " "), w=1.6, h=0.5, border=PALETTE["good"],
                    color=PALETTE["good"], fs=9)
        team = VGroup(person(0.4, PALETTE["accent"], smile=True),
                      lines("tricky call:\na team member", 9, PALETTE["ink"], buff=0.03)).arrange(RIGHT, buff=0.1)
        bot_row = VGroup(done, team).arrange(RIGHT, buff=0.35)
        inner = VGroup(fh, top_row, bot_row).arrange(DOWN, buff=0.45)
        box = card_bg(3.7, 2.9)
        call = VGroup(box, inner.move_to(box.get_center()))
        call.move_to(UP * 1.9)
        a1 = Arrow(ph.get_right() + RIGHT * 0.03, ai.get_left() + LEFT * 0.03, color=PALETTE["dim"], stroke_width=2.5,
                   buff=0.04, max_tip_length_to_length_ratio=0.3)
        a2 = Arrow(ai.get_bottom() + DOWN * 0.03, done.get_top() + UP * 0.03, color=PALETTE["good"], stroke_width=2,
                   buff=0.04, tip_length=0.1, max_tip_length_to_length_ratio=1)
        a3 = Arrow(ai.get_bottom() + DOWN * 0.03, team.get_top() + UP * 0.03, color=PALETTE["accent"], stroke_width=2,
                   buff=0.04, tip_length=0.1, max_tip_length_to_length_ratio=1)

        lh = Text("switches to the caller's language", color=PALETTE["dim"], font_size=11)
        bubs = VGroup(*[bubble(t, fs=12, w=1.05) for t in ("Hello", "Hola", "Bonjour", "Hallo", "Ciao", "Olá")]
                      ).arrange_in_grid(rows=2, cols=3, buff=0.12)
        l_inner = VGroup(lh, bubs).arrange(DOWN, buff=0.2)
        l_box = card_bg(3.7, 1.75)
        lang = VGroup(l_box, fit(l_inner, 3.4).move_to(l_box.get_center()))
        lang.move_to(DOWN * 0.55)

        caps = VGroup(chip("take, confirm, change, or cancel a booking", w=3.7, h=0.36, fs=10),
                      chip("answer common questions about the hotel", w=3.7, h=0.36, fs=10),
                      chip("switch languages to match the caller", w=3.7, h=0.36, fs=10),
                      chip("pass the call to a person when needed", w=3.7, h=0.36, fs=10)).arrange(DOWN, buff=0.08)
        caps.move_to(DOWN * 2.45)

        reveal(self, call)
        self.play(FadeIn(ph), run_time=0.4)
        self.play(GrowArrow(a1), FadeIn(ai), run_time=0.6)
        self.play(GrowArrow(a2), FadeIn(done), run_time=0.5)
        self.play(GrowArrow(a3), FadeIn(team), run_time=0.5)
        reveal(self, lang)
        self.play(LaggedStart(*[FadeIn(b) for b in bubs], lag_ratio=0.15), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in caps], lag_ratio=0.25), run_time=1.4)
        self.wait(1.2)


class B05_CompanyReported(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        badge = chip("COMPANY-REPORTED", w=3.0, h=0.5, border=PALETTE["miss"], color=PALETTE["miss"], fs=14)
        hotel = hotel_icon(0.55)
        loc = lines("a hotel in the\nCzech Republic, 2026", 11, PALETTE["dim"], buff=0.05)
        row = VGroup(hotel, loc).arrange(RIGHT, buff=0.3)
        upto = Text("up to", color=PALETTE["dim"], font_size=18)
        big = Text("90%", color=PALETTE["accent"], font_size=72, weight="BOLD")
        sub = lines("of repetitive\nfront-office requests", 16, PALETTE["ink"], buff=0.06)
        bar_w = 3.0
        track = RoundedRectangle(corner_radius=0.08, width=bar_w, height=0.2, fill_color=PALETTE["border"],
                                  fill_opacity=1, stroke_width=0)
        fill = RoundedRectangle(corner_radius=0.08, width=bar_w * 0.9, height=0.2, fill_color=PALETTE["accent"],
                                 fill_opacity=0.55, stroke_width=0).align_to(track, LEFT)
        bar = VGroup(track, fill)
        goal = chip("best read as a goal, not a promise", w=3.3, h=0.55, border=PALETTE["dim"], fs=12)
        inner = VGroup(badge, row, upto, big, sub, bar, goal).arrange(DOWN, buff=0.2)
        box = card_bg(3.7, 5.6)
        card = VGroup(box, inner.move_to(box.get_center()))
        card.move_to(ORIGIN)

        reveal(self, card)
        self.play(FadeIn(row, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(upto), FadeIn(big, scale=0.9), run_time=0.7)
        self.play(FadeIn(sub), FadeIn(bar), run_time=0.5)
        self.play(FadeIn(badge, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(goal, shift=UP * 0.1), run_time=0.5)
        self.wait(1.3)


class B06_ThirtyPercent(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        ring = Annulus(inner_radius=0.5, outer_radius=0.8, color=PALETTE["border"], fill_opacity=1, stroke_width=0)
        part = AnnularSector(inner_radius=0.5, outer_radius=0.8, angle=0.3 * TAU, start_angle=PI / 2,
                             color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
        pct = Text("~30%", color=PALETTE["accent"], font_size=17, weight="BOLD").move_to(ring.get_center())
        donut = VGroup(ring, part, pct)
        cap = VGroup(lines("of a front desk\nday on phone calls,\nmany of them routine", 12, PALETTE["ink"],
                           buff=0.05),
                     Text("reports suggest", color=PALETTE["dim"], font_size=10)).arrange(DOWN, buff=0.12)
        t_inner = VGroup(donut, cap).arrange(RIGHT, buff=0.35)
        t_box = card_bg(3.7, 2.6)
        top = VGroup(t_box, fit(t_inner, 3.4).move_to(t_box.get_center()))
        top.move_to(UP * 2.05)

        rh = Text("one case study", color=PALETTE["dim"], font_size=11)
        cells = [VGroup(hotel_icon(0.28), VGroup(person(0.15, PALETTE["ink"]), person(0.15, PALETTE["accent"])
                                                  ).arrange(RIGHT, buff=0.03)).arrange(DOWN, buff=0.04)
                 for _ in range(9)]
        grid = VGroup(*cells).arrange_in_grid(rows=2, cols=5, buff=0.14)
        chips = VGroup(chip("9 boutique hotels, two-person front desks", w=3.4, h=0.38, fs=10),
                       chip("an assistant handled the after-hours calls", w=3.4, h=0.38, fs=10,
                            border=PALETTE["accent"], color=PALETTE["accent"]),
                       chip("busy mornings changed: more time for guests", w=3.4, h=0.38, fs=10,
                            border=PALETTE["good"], color=PALETTE["good"])).arrange(DOWN, buff=0.1)
        b_inner = VGroup(rh, grid, chips).arrange(DOWN, buff=0.22)
        b_box = card_bg(3.7, 3.5)
        bottom = VGroup(b_box, b_inner.move_to(b_box.get_center()))
        bottom.move_to(DOWN * 1.2)

        reveal(self, top)
        self.play(FadeIn(ring), run_time=0.4)
        self.play(FadeIn(part), FadeIn(pct), run_time=0.8)
        reveal(self, bottom)
        self.play(LaggedStart(*[FadeIn(g) for g in grid], lag_ratio=0.1), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in chips], lag_ratio=0.3), run_time=1.2)
        self.wait(1.2)


class B09_DoingItRight(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lh = Text("being upfront", color=PALETTE["ink"], font_size=15, weight="BOLD")
        banner_box = RoundedRectangle(corner_radius=0.12, width=3.3, height=0.85, fill_color=PALETTE["ink"],
                                       fill_opacity=1, stroke_width=0)
        banner_t = lines("This call may be recorded\nor handled by AI.", 12, PALETTE["bg"], buff=0.05)
        banner = VGroup(banner_box, banner_t.move_to(banner_box.get_center()))
        c1 = chip("rules differ from place to place", w=3.3, h=0.38, fs=11)
        c2 = chip("check what applies to you", w=3.3, h=0.38, fs=11, border=PALETTE["good"], color=PALETTE["good"])
        fo = Text("good hospitality, too", color=PALETTE["accent"], font_size=12)
        t_inner = VGroup(lh, banner, c1, c2, fo).arrange(DOWN, buff=0.17)
        t_box = card_bg(3.7, 3.0)
        top = VGroup(t_box, t_inner.move_to(t_box.get_center()))
        top.move_to(UP * 1.85)

        a_h = VGroup(helper_icon(s=0.6), Text("the assistant", color=PALETTE["accent"], font_size=13, weight="BOLD")
                     ).arrange(DOWN, buff=0.15)
        a_l = VGroup(*[Text(t, color=PALETTE["ink"], font_size=11) for t in ("pool hours", "late checkout", "repeat questions")]
                     ).arrange(DOWN, buff=0.08)
        col_a = VGroup(a_h, a_l).arrange(DOWN, buff=0.18)
        t_h = VGroup(person(0.5, PALETTE["accent"], smile=True), Text("the team", color=PALETTE["ink"], font_size=13,
                                                                       weight="BOLD")).arrange(DOWN, buff=0.15)
        t_l = Text("the welcome", color=PALETTE["ink"], font_size=11)
        col_t = VGroup(t_h, t_l).arrange(DOWN, buff=0.18)
        cols = VGroup(col_a, col_t).arrange(RIGHT, buff=0.7, aligned_edge=UP)
        r_head = lines("routine tasks, with\npeople at the center", 11, PALETTE["dim"], buff=0.04)
        b_inner = VGroup(r_head, cols).arrange(DOWN, buff=0.25)
        b_box = card_bg(3.7, 3.0, stroke_color=PALETTE["accent"])
        bottom = VGroup(b_box, b_inner.move_to(b_box.get_center()))
        bottom.move_to(DOWN * 1.65)

        reveal(self, top)
        self.play(FadeIn(banner, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(c2, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(fo), run_time=0.4)
        reveal(self, bottom)
        self.play(FadeIn(col_a, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(col_t, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)


class B10_PeopleForPeople(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        panel, floor, lamp = lobby_panel(3.9, 4.0)
        panel.move_to(UP * 1.35)
        floor.move_to(panel.get_bottom() + UP * 0.37)
        ft = floor.get_top()[1]
        dk = desk(2.0, 0.8).move_to([0.5, ft + 0.4, 0])
        t1 = person(0.85, PALETTE["ink"], smile=True).move_to([0.0, dk.get_top()[1] + 0.5, 0])
        t2 = person(0.85, PALETTE["accent"], smile=True).move_to([0.9, dk.get_top()[1] + 0.5, 0])
        gs = VGroup(person(0.65, PALETTE["dim"]).move_to([-1.55, ft + 0.5, 0]),
                    person(0.65, PALETTE["good"]).move_to([-1.1, ft + 0.5, 0]),
                    person(0.65, PALETTE["ink"]).move_to([1.7, ft + 0.5, 0]))
        cases = VGroup(suitcase(0.26).move_to([-1.33, ft + 0.2, 0]))
        ph = phone_icon(h=0.5).move_to([1.2, dk.get_top()[1] + 0.3, 0])
        tick = VMobject(color=PALETTE["good"], stroke_width=4).set_points_as_corners(
            [ph.get_center() + [-0.07, 0.0, 0], ph.get_center() + [-0.01, -0.07, 0], ph.get_center() + [0.09, 0.08, 0]])

        q = lines("A hotel where the\npeople have more\ntime for people.", 22, PALETTE["ink"], max_w=3.5,
                  buff=0.12, weight="BOLD")
        q.move_to(DOWN * 1.8)
        sub = lines("guests get quick answers\nteams get time back", 13, PALETTE["dim"], buff=0.06)
        sub.move_to(DOWN * 3.0)

        reveal(self, VGroup(panel, VGroup(floor, lamp)))
        self.play(FadeIn(VGroup(dk, t1, t2), shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(gs, shift=UP * 0.1), FadeIn(cases), run_time=0.8)
        self.play(FadeIn(ph), Create(tick), run_time=0.7)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(1.5)


class B11_SourcesCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        sh = Text("Sources", color=PALETTE["ink"], font_size=16, weight="BOLD")
        rows = VGroup()
        for n, t in [("SendSquared (2026)", "Hotel AI 2026: The Automation Stack"),
                     ("Omnidim (2026)", "Voice AI for Hotels"),
                     ("Travel Daily News (July 2026)", "AI phone guest service in a Czech hotel"),
                     ("GrowwStacks (2026)", "Voice Agents in Hotels"),
                     ("RaftLabs (2026)", "Voice AI Agents for Hospitality in 2026"),
                     ("AI Agent Rank (May 23, 2026)", "AI for Hospitality & Restaurants 2026")]:
            a = Text(n, color=PALETTE["accent"], font_size=10, weight="BOLD")
            b = Text(t, color=PALETTE["ink"], font_size=9.5)
            rows.add(VGroup(a, b).arrange(DOWN, buff=0.03, aligned_edge=LEFT))
        rows.arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        t_inner = VGroup(sh, rows).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        t_box = card_bg(3.7, 3.6)
        top = VGroup(t_box, fit(t_inner, 3.3).move_to(t_box.get_center()))
        top.move_to(UP * 1.55)

        nh = Text("A note on sources", color=PALETTE["miss"], font_size=14, weight="BOLD")
        nb = lines("Most sources are companies that\nbuild hotel AI tools. So the\npercentages are company-reported\nfigures, not independent research.",
                   11, PALETTE["ink"], buff=0.06)
        badge = chip("COMPANY-REPORTED", w=2.6, h=0.4, border=PALETTE["miss"], color=PALETTE["miss"], fs=12)
        ill = lines("The Friday scene is an illustration,\nnot a reported case.", 10, PALETTE["ink"], buff=0.04)
        b_inner = VGroup(nh, nb, badge, ill).arrange(DOWN, buff=0.2)
        b_box = card_bg(3.7, 2.9, stroke_color=PALETTE["miss"])
        bottom = VGroup(b_box, fit(b_inner, 3.4).move_to(b_box.get_center()))
        bottom.move_to(DOWN * 1.8)

        reveal(self, top)
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in rows], lag_ratio=0.2), run_time=1.4)
        reveal(self, bottom)
        self.play(FadeIn(nb, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(badge), run_time=0.4)
        self.play(FadeIn(ill), run_time=0.4)
        self.wait(1.3)
