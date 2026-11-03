"""
Manim scenes for hotel-phone-helper

A warm, fair explainer on AI voice assistants answering hotel calls, sourced
from the user-supplied article "The Hotel Phone Gets a Helper." No dedicated
footage exists (per the user's materials note) -- every visual below is a
generated Manim graphic, with no real hotel brand logos. The opening Friday
scene is an illustration; the 90% and 30% figures are carried as
company-reported / report-based. Built in the house Claude palette.

B00B_AgrimaIntro      -- presenter card: "Hi, I'm Agrima." + lead-in
B01_FridayAfternoon   -- warm lobby: check-in line, ringing phone, three questions (illustration)
B02_AlwaysOn          -- 24-hour day bar; a helper beside the front desk team
B03_FirstRing         -- call -> assistant -> booking system; overnight messages -> team
B04_WhatItCanDo       -- call-flow graphic + language bubbles + four capabilities
B05_CompanyReported   -- "up to 90%" stat card labeled company-reported
B06_ThirtyPercent     -- ~30% of the day on calls; nine boutique hotels case study
B07_InPerson          -- a team member greeting a guest in person
B08_AfterTheStay      -- the after-stay phone call: problem lane / review lane
B09_DoingItRight      -- call notice, rules differ; assistant vs team
B10_PeopleForPeople   -- the closing lobby and line
B11_SourcesCard       -- six sources + the company-reported note
"""

from manim import *
import numpy as np

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


def lines(txt, fs, color, max_w=None, buff=0.12, weight=None):
    """Centered multi-line label: one Text per line, stacked and centered."""
    kw = {"weight": weight} if weight else {}
    g = VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split("\n")]).arrange(DOWN, buff=buff)
    return fit(g, max_w) if max_w else g


def reveal(scene, card, t1=0.35, t2=0.4):
    """Box grows first, then its contents fade in (no content hanging past a growing box)."""
    box, inner = card[0], card[1]
    w = box.width
    box.stretch(0.01, 0)
    scene.play(box.animate.stretch_to_fit_width(w), run_time=t1)
    scene.play(FadeIn(inner), run_time=t2)


def chip(label, w=2.6, h=0.6, border=None, color=None, fs=16):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(Text(label, color=color or PALETTE["ink"], font_size=fs), w - 0.3)
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


def bubble(text, fs=14, border=None, fill=None, w=None, color=None):
    t = Text(text, color=color or PALETTE["ink"], font_size=fs)
    ww = (w or (t.width + 0.5))
    box = RoundedRectangle(corner_radius=0.16, width=ww, height=0.5, fill_color=fill or PALETTE["card"],
                           fill_opacity=1, stroke_color=border or PALETTE["border"], stroke_width=1.5)
    if w and t.width > w - 0.3:
        t.scale_to_fit_width(w - 0.3)
    return VGroup(box, t.move_to(box.get_center()))


def helper_icon(color=None):
    c = color or PALETTE["accent"]
    box = RoundedRectangle(corner_radius=0.14, width=0.95, height=0.7, fill_color=PALETTE["card"],
                           fill_opacity=1, stroke_color=c, stroke_width=3)
    dots = VGroup(*[Dot(radius=0.05, color=c) for _ in range(3)]).arrange(RIGHT, buff=0.12).move_to(box.get_center())
    tail = Polygon([-0.1, 0, 0], [0.1, 0, 0], [0, -0.16, 0], color=c, fill_color=PALETTE["card"],
                   fill_opacity=1, stroke_width=3).next_to(box, DOWN, buff=-0.02).shift(LEFT * 0.2)
    return VGroup(tail, box, dots)


def db_icon(color=None):
    c = color or PALETTE["ink"]
    body = Rectangle(width=0.75, height=0.7, fill_color=PALETTE["card"], fill_opacity=1, stroke_color=c,
                     stroke_width=2.5)
    top = Ellipse(width=0.75, height=0.22, fill_color=PALETTE["bg"], fill_opacity=1, stroke_color=c,
                  stroke_width=2.5).move_to(body.get_top())
    mid = Arc(radius=0.375, start_angle=PI, angle=PI, color=c, stroke_width=2).stretch(0.3, 1)
    mid.move_to(body.get_center() + UP * 0.02)
    return VGroup(body, top, mid)


def mail_icon(color=None):
    c = color or PALETTE["accent"]
    b = RoundedRectangle(corner_radius=0.05, width=0.8, height=0.55, fill_color=PALETTE["card"], fill_opacity=1,
                         stroke_color=c, stroke_width=2.5)
    f = Polygon(b.get_corner(UL), b.get_corner(UR), b.get_center(), color=c, stroke_width=2.5, fill_opacity=0)
    return VGroup(b, f)


def moon_icon():
    c = Circle(radius=0.3, fill_color=PALETTE["ink"], fill_opacity=1, stroke_width=0)
    cut = Circle(radius=0.26, fill_color=PALETTE["bg"], fill_opacity=1, stroke_width=0).shift(RIGHT * 0.16 + UP * 0.08)
    return VGroup(c, cut)


def hotel_icon(scale=1.0, color=None):
    c = color or PALETTE["dim"]
    body = Rectangle(width=0.9, height=1.2, fill_color=c, fill_opacity=0.85, stroke_width=0)
    wins = VGroup(*[Rectangle(width=0.14, height=0.16, fill_color=PALETTE["warm"], fill_opacity=1, stroke_width=0)
                    for _ in range(9)]).arrange_in_grid(rows=3, cols=3, buff=0.14).move_to(body.get_center() + UP * 0.12)
    door = Rectangle(width=0.2, height=0.24, fill_color=PALETTE["warm"], fill_opacity=1, stroke_width=0)
    door.move_to(body.get_bottom() + UP * 0.12)
    return VGroup(body, wins, door).scale(scale)


def star_icon(color=None, r=0.22):
    return Star(n=5, outer_radius=r, inner_radius=r * 0.45, fill_color=color or PALETTE["accent"], fill_opacity=1,
                stroke_width=0)


def desk(w=3.6, h=0.9):
    top = RoundedRectangle(corner_radius=0.06, width=w, height=h, fill_color=PALETTE["wood"], fill_opacity=1,
                            stroke_width=0)
    trim = Rectangle(width=w, height=0.08, fill_color=PALETTE["ink"], fill_opacity=0.25, stroke_width=0)
    trim.align_to(top, UP)
    return VGroup(top, trim)


def lobby(w, h):
    """Warm lobby panel with floor strip and a window; returns (panel, floor_top_y_offset, group)."""
    panel = RoundedRectangle(corner_radius=0.14, width=w, height=h, fill_color=PALETTE["warm"], fill_opacity=1,
                             stroke_color=PALETTE["border"], stroke_width=1.5)
    floor = Rectangle(width=w - 0.04, height=0.7, fill_color=PALETTE["floor"], fill_opacity=1, stroke_width=0)
    floor.move_to(panel.get_bottom() + UP * 0.37)
    win = VGroup(Rectangle(width=1.5, height=1.0, fill_color="#F6E7C8", fill_opacity=1, stroke_color=PALETTE["wood"],
                           stroke_width=2),
                 Line(UP * 0.5, DOWN * 0.5, color=PALETTE["wood"], stroke_width=2),
                 Line(LEFT * 0.75, RIGHT * 0.75, color=PALETTE["wood"], stroke_width=2))
    win.move_to(panel.get_top() + DOWN * 0.95 + LEFT * (w * 0.3))
    lamp = VGroup(Line(UP * 0.4, ORIGIN, color=PALETTE["dim"], stroke_width=2),
                  Polygon([-0.2, 0, 0], [0.2, 0, 0], [0.12, -0.2, 0], [-0.12, -0.2, 0], fill_color=PALETTE["accent"],
                          fill_opacity=0.7, stroke_width=0))
    lamp.move_to(panel.get_top() + DOWN * 0.45 + RIGHT * (w * 0.12))
    return panel, floor, VGroup(win, lamp)


# --- scenes -----------------------------------------------------------------

class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=40)
        summary = fit(Text(
            "Today: the hotel phone, and the AI helpers\nnow answering it. Not replacing the front\n"
            "desk, but giving it more time for guests.",
            color=PALETTE["ink"], font_size=24, line_spacing=1.3, should_center=True), 8.6)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.4)


class B01_FridayAfternoon(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        panel, floor, deco = lobby(12.0, 5.6)
        panel.move_to(DOWN * 0.2)
        floor.move_to(panel.get_bottom() + UP * 0.37)
        deco.move_to(deco.get_center() + [0, 0, 0])
        ft = floor.get_top()[1]

        dk = desk(3.6, 0.9)
        dk.move_to([0.8, ft + 0.45, 0])
        t1 = person(1.1, PALETTE["ink"], smile=True)
        t2 = person(1.1, PALETTE["accent"], smile=True)
        t1.move_to([-0.1, dk.get_top()[1] + 0.62, 0])
        t2.move_to([1.5, dk.get_top()[1] + 0.62, 0])
        guests = VGroup(*[person(0.95, c) for c in (PALETTE["dim"], PALETTE["good"], PALETTE["ink"], PALETTE["accent"])])
        for i, g in enumerate(guests):
            g.move_to([-4.9 + 0.95 * i, ft + 0.7, 0])
        cases = VGroup(*[suitcase(0.38).move_to([-4.9 + 0.95 * i + 0.4, ft + 0.28, 0]) for i in range(4)])
        ph = phone_icon(h=0.7).move_to([2.55, dk.get_top()[1] + 0.4, 0])
        rings = ring_arcs(ph.get_center(), s=0.9)

        q1 = bubble("What time does the pool close?", fs=14, w=3.2)
        q2 = bubble("Can I get a late checkout?", fs=14, w=3.2)
        q3 = bubble("Is there a table free tonight?", fs=14, w=3.2)
        qs = VGroup(q1, q2, q3).arrange(DOWN, buff=0.22)
        qs.move_to([4.3, 0.55, 0])
        note = chip("an illustration, not a reported case", w=4.6, h=0.45, border=PALETTE["ink"],
                    color=PALETTE["ink"], fs=13)
        note.move_to([-3.4, floor.get_center()[1], 0])

        reveal(self, VGroup(panel, VGroup(floor, deco)))
        self.play(FadeIn(VGroup(dk, t1, t2), shift=UP * 0.1), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(g, shift=RIGHT * 0.2) for g in guests], lag_ratio=0.3),
                  FadeIn(cases), run_time=1.4)
        self.play(FadeIn(ph), run_time=0.4)
        self.play(FadeIn(rings), run_time=0.4)
        for q in (q1, q2, q3):
            self.play(FadeIn(q, shift=LEFT * 0.2), run_time=0.5)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(1.2)


class B02_AlwaysOn(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = Text("hotels never really close", color=PALETTE["ink"], font_size=26, weight="BOLD")
        head.move_to(UP * 3.0)
        cells = VGroup(*[Rectangle(width=0.44, height=0.5, fill_color=PALETTE["accent"], fill_opacity=0.9,
                                   stroke_color=PALETTE["card"], stroke_width=1.5) for _ in range(24)]
                       ).arrange(RIGHT, buff=0)
        cells.move_to(UP * 2.0)
        hrs = VGroup(*[Text(t, color=PALETTE["dim"], font_size=12) for t in ("12am", "6am", "12pm", "6pm")])
        for i, t in enumerate(hrs):
            t.move_to(cells[i * 6].get_bottom() + LEFT * 0.22 + DOWN * 0.25)
        def cx(i):
            return cells[i].get_center()[0]
        tags = VGroup(
            chip("late night", w=1.8, h=0.45, fs=13).move_to([cx(1), 0.9, 0]),
            chip("early morning", w=2.2, h=0.45, fs=13).move_to([cx(7), 0.9, 0]),
            chip("evening", w=1.8, h=0.45, fs=13).move_to([cx(20), 0.9, 0]),
        )
        tz = chip("callers planning trips in other time zones", w=5.4, h=0.45, border=PALETTE["dim"],
                  color=PALETTE["dim"], fs=13).move_to([0, 0.25, 0])

        team = VGroup(VGroup(person(0.8, PALETTE["ink"], smile=True), person(0.8, PALETTE["accent"], smile=True)
                             ).arrange(RIGHT, buff=0.15),
                      Text("front desk team", color=PALETTE["ink"], font_size=16)).arrange(DOWN, buff=0.2)
        plus = Text("+", color=PALETTE["dim"], font_size=40)
        helper = VGroup(helper_icon(), Text("AI voice assistant", color=PALETTE["ink"], font_size=16)).arrange(DOWN, buff=0.28)
        pair = VGroup(team, plus, helper).arrange(RIGHT, buff=0.8)
        box = card_bg(8.4, 2.5)
        pcard = VGroup(box, pair.move_to(box.get_center()))
        pcard.move_to(DOWN * 1.6)
        tm = Text("a teammate, not a replacement", color=PALETTE["accent"], font_size=22, weight="BOLD")
        tm.move_to(DOWN * 3.15)

        self.play(FadeIn(head, shift=DOWN * 0.1), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.04), FadeIn(hrs), run_time=1.6)
        self.play(FadeIn(tags), FadeIn(tz), run_time=0.7)
        reveal(self, pcard)
        self.play(FadeIn(tm, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B03_FirstRing(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        def node(icon, label, w=2.5, h=1.9, border=None):
            box = card_bg(w, h, stroke_color=border)
            lab = lines(label, 14, PALETTE["ink"], max_w=w - 0.3, buff=0.05)
            inner = VGroup(icon, lab).arrange(DOWN, buff=0.18)
            return VGroup(box, inner.move_to(box.get_center()))

        def arrow(c=None):
            return Arrow(LEFT * 0.25, RIGHT * 0.25, color=c or PALETTE["dim"], stroke_width=3, buff=0,
                         max_tip_length_to_length_ratio=0.45)

        # lane 1
        n1 = node(VGroup(phone_icon(h=0.7)), "a call comes in")
        n2 = node(helper_icon(), "the assistant picks up\non the first ring", border=PALETTE["accent"])
        n3 = node(db_icon(), "checks the booking\nsystem in real time")
        n4 = node(VGroup(chip("what's available", w=1.9, h=0.4, fs=12),
                         chip("the price", w=1.9, h=0.4, fs=12)).arrange(DOWN, buff=0.12), "shared with the caller",
                  border=PALETTE["good"])
        l1 = VGroup(n1, arrow(), n2, arrow(PALETTE["accent"]), n3, arrow(), n4).arrange(RIGHT, buff=0.22)
        l1.move_to(UP * 1.75)
        l1h = Text("any hour", color=PALETTE["dim"], font_size=14).next_to(l1, UP, buff=0.15)

        # lane 2
        m1 = node(moon_icon(), "busy check-in time\nor overnight", h=1.7)
        m2 = node(mail_icon(), "takes a message", h=1.7, border=PALETTE["accent"])
        m3 = node(person(0.6, PALETTE["accent"], smile=True), "the team reads it\nin the morning", h=1.7)
        l2 = VGroup(m1, arrow(), m2, arrow(PALETTE["accent"]), m3).arrange(RIGHT, buff=0.22)
        l2.move_to(DOWN * 0.35)

        guest = chip("guest: a quick answer, not a busy signal", w=6.2, h=0.6, border=PALETTE["good"],
                     color=PALETTE["good"], fs=15)
        hotel = chip("hotel: fewer missed bookings", w=4.2, h=0.6, border=PALETTE["good"], color=PALETTE["good"],
                     fs=15)
        res = VGroup(guest, hotel).arrange(RIGHT, buff=0.35)
        res.move_to(DOWN * 2.65)

        self.play(FadeIn(l1h), run_time=0.3)
        for part in l1:
            self.play(FadeIn(part, shift=RIGHT * 0.15), run_time=0.5)
        self.wait(0.4)
        for part in l2:
            self.play(FadeIn(part, shift=RIGHT * 0.15), run_time=0.45)
        self.play(FadeIn(guest, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(hotel, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B04_WhatItCanDo(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # call flow card
        fh = Text("the call flow", color=PALETTE["dim"], font_size=16)
        ph = VGroup(phone_icon(h=0.8), Text("call comes in", color=PALETTE["ink"], font_size=14)).arrange(DOWN, buff=0.15)
        ai = VGroup(helper_icon(), Text("AI answers", color=PALETTE["accent"], font_size=14, weight="BOLD")
                    ).arrange(DOWN, buff=0.25)
        done = chip("handled: booking or question", w=3.0, h=0.5, border=PALETTE["good"], color=PALETTE["good"], fs=13)
        team = VGroup(person(0.6, PALETTE["accent"], smile=True),
                      Text("tricky call: a team member", color=PALETTE["ink"], font_size=13)).arrange(RIGHT, buff=0.2)
        right = VGroup(done, team).arrange(DOWN, buff=0.7, aligned_edge=LEFT)
        flow = VGroup(ph, ai, right).arrange(RIGHT, buff=0.85)
        a1 = Arrow(ph.get_right(), ai.get_left(), color=PALETTE["dim"], stroke_width=3, buff=0.1,
                   max_tip_length_to_length_ratio=0.2)
        c_inner = VGroup(fh, flow).arrange(DOWN, buff=0.35)
        c_box = card_bg(7.7, 3.5)
        call = VGroup(c_box, c_inner.move_to(c_box.get_center()))
        call.move_to(LEFT * 2.2 + UP * 1.1)
        a1 = Arrow(ph.get_right() + RIGHT * 0.05, ai.get_left() + LEFT * 0.05, color=PALETTE["dim"], stroke_width=3,
                   buff=0.05, max_tip_length_to_length_ratio=0.25)
        a2 = Arrow(ai.get_right() + RIGHT * 0.05, done.get_left() + LEFT * 0.05, color=PALETTE["good"], stroke_width=3,
                   buff=0.05, max_tip_length_to_length_ratio=0.2)
        a3 = Arrow(ai.get_right() + RIGHT * 0.05, team.get_left() + LEFT * 0.05, color=PALETTE["accent"],
                   stroke_width=3, buff=0.05, max_tip_length_to_length_ratio=0.2)

        # language bubbles card
        lh = Text("switches to the caller's language", color=PALETTE["dim"], font_size=15)
        bubs = VGroup(*[bubble(t, fs=16, w=1.6) for t in ("Hello", "Hola", "Bonjour", "Hallo", "Ciao", "Olá")]
                      ).arrange_in_grid(rows=3, cols=2, buff=0.18)
        l_inner = VGroup(lh, bubs).arrange(DOWN, buff=0.3)
        l_box = card_bg(4.1, 3.5)
        lang = VGroup(l_box, fit(l_inner, 3.9).move_to(l_box.get_center()))
        lang.move_to(RIGHT * 4.1 + UP * 1.1)

        caps = VGroup(
            chip("take, confirm, change, or cancel a booking", w=5.8, h=0.55, fs=15),
            chip("answer common questions about the hotel", w=5.8, h=0.55, fs=15),
            chip("switch languages to match the caller", w=5.8, h=0.55, fs=15),
            chip("pass the call to a person when one is needed", w=5.8, h=0.55, fs=15),
        ).arrange_in_grid(rows=2, cols=2, buff=0.25)
        caps.move_to(DOWN * 2.35)

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

        hotel = hotel_icon(1.3)
        loc = lines("a hotel in the\nCzech Republic\n2026", 16, PALETTE["dim"], buff=0.08)
        left = VGroup(hotel, loc).arrange(DOWN, buff=0.35)

        upto = Text("up to", color=PALETTE["dim"], font_size=24)
        big = Text("90%", color=PALETTE["accent"], font_size=96, weight="BOLD")
        sub = Text("of repetitive front-office requests", color=PALETTE["ink"], font_size=22)
        bar_w = 5.4
        track = RoundedRectangle(corner_radius=0.1, width=bar_w, height=0.28, fill_color=PALETTE["border"],
                                  fill_opacity=1, stroke_width=0)
        fill = RoundedRectangle(corner_radius=0.1, width=bar_w * 0.9, height=0.28, fill_color=PALETTE["accent"],
                                 fill_opacity=0.55, stroke_width=0).align_to(track, LEFT)
        bar = VGroup(track, fill)
        mid = VGroup(upto, big, sub, bar).arrange(DOWN, buff=0.22)
        body = VGroup(left, mid).arrange(RIGHT, buff=0.9)

        badge = chip("COMPANY-REPORTED", w=3.6, h=0.6, border=PALETTE["miss"], color=PALETTE["miss"], fs=20)
        goal = chip("best read as a goal, not a promise", w=6.0, h=0.6, border=PALETTE["dim"], color=PALETTE["ink"],
                    fs=18)
        inner = VGroup(badge, body, goal).arrange(DOWN, buff=0.4)
        box = card_bg(11.2, 5.4)
        card = VGroup(box, fit(inner, 10.6).move_to(box.get_center()))
        card.move_to(DOWN * 0.1)

        reveal(self, card)
        self.play(FadeIn(left, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(upto), FadeIn(big, scale=0.9), run_time=0.7)
        self.play(FadeIn(sub), FadeIn(bar), run_time=0.5)
        self.play(FadeIn(badge, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(goal, shift=UP * 0.1), run_time=0.5)
        self.wait(1.3)


class B06_ThirtyPercent(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # left: about 30% of the day
        lh = Text("a front desk day", color=PALETTE["dim"], font_size=16)
        ring = Annulus(inner_radius=0.9, outer_radius=1.45, color=PALETTE["border"], fill_opacity=1, stroke_width=0)
        part = AnnularSector(inner_radius=0.9, outer_radius=1.45, angle=0.3 * TAU, start_angle=PI / 2,
                             color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
        pct = Text("~30%", color=PALETTE["accent"], font_size=34, weight="BOLD")
        pct.move_to(ring.get_center())
        donut = VGroup(ring, part, pct)
        cap = lines("on phone calls,\nmany of them routine", 17, PALETTE["ink"], buff=0.08)
        hint = Text("reports suggest", color=PALETTE["dim"], font_size=14)
        l_inner = VGroup(lh, donut, cap, hint).arrange(DOWN, buff=0.3)
        l_box = card_bg(5.4, 5.7)
        left = VGroup(l_box, l_inner.move_to(l_box.get_center()))
        left.move_to(LEFT * 3.5 + DOWN * 0.1)

        # right: nine boutique hotels
        rh = Text("one case study", color=PALETTE["dim"], font_size=16)
        grid = VGroup(*[VGroup(hotel_icon(0.38), VGroup(person(0.2, PALETTE["ink"]), person(0.2, PALETTE["accent"])
                                                          ).arrange(RIGHT, buff=0.04)).arrange(DOWN, buff=0.05)
                        for _ in range(9)]).arrange_in_grid(rows=3, cols=3, buff=0.2)
        r_chips = VGroup(
            chip("9 boutique hotels, two-person front desks", w=5.0, h=0.5, fs=13),
            chip("an assistant handled the after-hours calls", w=5.0, h=0.5, fs=13, border=PALETTE["accent"],
                 color=PALETTE["accent"]),
            chip("busy mornings changed: more time for guests", w=5.0, h=0.5, fs=13, border=PALETTE["good"],
                 color=PALETTE["good"]),
        ).arrange(DOWN, buff=0.12)
        r_inner = VGroup(rh, grid, r_chips).arrange(DOWN, buff=0.25)
        r_box = card_bg(5.7, 5.7)
        right = VGroup(r_box, fit(r_inner, 5.3).move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.4 + DOWN * 0.1)

        reveal(self, left)
        self.play(FadeIn(ring), run_time=0.4)
        self.play(FadeIn(part), FadeIn(pct), run_time=0.8)
        reveal(self, right)
        self.play(LaggedStart(*[FadeIn(g) for g in grid], lag_ratio=0.1), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in r_chips], lag_ratio=0.3), run_time=1.2)
        self.wait(1.2)


class B07_InPerson(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        panel, floor, deco = lobby(6.6, 4.9)
        panel.move_to(LEFT * 3.0 + DOWN * 0.1)
        floor.move_to(panel.get_bottom() + UP * 0.37)
        deco.shift(LEFT * 3.0 + DOWN * 0.1 - deco.get_center() + deco.get_center())
        ft = floor.get_top()[1]
        dk = desk(3.0, 0.9).move_to([-3.3, ft + 0.45, 0])
        team = person(1.3, PALETTE["accent"], smile=True).move_to([-3.3, dk.get_top()[1] + 0.75, 0])
        guest = person(1.15, PALETTE["ink"]).move_to([-1.2, ft + 0.9, 0])
        case = suitcase(0.45).move_to([-0.6, ft + 0.32, 0])
        hi = bubble("Welcome!", fs=17, border=PALETTE["accent"], w=1.6).move_to([-3.3, dk.get_top()[1] + 2.15, 0])

        hd = Text("the part only people can do", color=PALETTE["accent"], font_size=22, weight="BOLD")
        cs = VGroup(chip("welcome you", w=4.6, h=0.65, fs=18), chip("notice when something's wrong", w=4.6, h=0.65, fs=18),
                    chip("make you feel looked after", w=4.6, h=0.65, fs=18)).arrange(DOWN, buff=0.25)
        r_inner = VGroup(hd, cs).arrange(DOWN, buff=0.45)
        r_box = card_bg(5.4, 4.9, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, r_inner.move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.4 + DOWN * 0.1)
        foot = chip("the repeat tasks go to the helper", w=5.4, h=0.5, border=PALETTE["dim"], color=PALETTE["dim"], fs=14)
        foot.move_to(DOWN * 3.15)

        reveal(self, VGroup(panel, VGroup(floor, deco)))
        self.play(FadeIn(VGroup(dk, team), shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(VGroup(guest, case), shift=RIGHT * 0.3), run_time=0.8)
        self.play(FadeIn(hi, shift=DOWN * 0.1), run_time=0.5)
        reveal(self, right)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in cs], lag_ratio=0.3), run_time=1.2)
        self.play(FadeIn(foot), run_time=0.5)
        self.wait(1.2)


class B08_AfterTheStay(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        ph = phone_icon(h=1.4)
        ring = ring_arcs(ph.get_center(), s=1.0)
        q = bubble("How was your stay?", fs=18, border=PALETTE["accent"], w=3.3)
        l_inner = VGroup(VGroup(ph, ring), q, Text("a call after checkout", color=PALETTE["dim"], font_size=15)
                         ).arrange(DOWN, buff=0.35)
        l_box = card_bg(4.4, 4.6)
        left = VGroup(l_box, l_inner.move_to(l_box.get_center()))
        left.move_to(LEFT * 4.1 + UP * 0.2)

        def lane(tag, tagc, mid, end, endc):
            t = chip(tag, w=2.3, h=0.55, border=tagc, color=tagc, fs=15)
            m = lines(mid, 13, PALETTE["ink"], buff=0.05)
            e = end
            a = Arrow(LEFT * 0.22, RIGHT * 0.22, color=PALETTE["dim"], stroke_width=3, buff=0,
                      max_tip_length_to_length_ratio=0.45)
            a2 = a.copy()
            return VGroup(t, a, m, a2, e).arrange(RIGHT, buff=0.18)
        fix = VGroup(person(0.5, PALETTE["accent"], smile=True), Text("the team fixes it", color=PALETTE["ink"], font_size=13)
                     ).arrange(RIGHT, buff=0.12)
        rev = VGroup(star_icon(), Text("pointed toward a review", color=PALETTE["ink"], font_size=13)
                     ).arrange(RIGHT, buff=0.12)
        lane1 = lane("a problem", PALETTE["miss"], "reaches the hotel\nquickly and privately", fix, None)
        lane2 = lane("loved the stay", PALETTE["good"], "the assistant\ncan point the way", rev, None)
        lanes = VGroup(lane1, lane2).arrange(DOWN, buff=0.9, aligned_edge=LEFT)
        lanes.scale(1.15)
        r_box = card_bg(7.6, 4.6)
        right = VGroup(r_box, fit(lanes, 7.1).move_to(r_box.get_center()))
        right.move_to(RIGHT * 2.55 + UP * 0.2)

        foot = Text("Guests get heard. Hotels learn what to improve.", color=PALETTE["accent"], font_size=22)
        foot.move_to(DOWN * 3.0)

        reveal(self, left)
        self.play(FadeIn(ring), run_time=0.4)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.5)
        reveal(self, right)
        for part in lane1:
            self.play(FadeIn(part, shift=RIGHT * 0.1), run_time=0.35)
        for part in lane2:
            self.play(FadeIn(part, shift=RIGHT * 0.1), run_time=0.35)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B09_DoingItRight(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lh = Text("being upfront", color=PALETTE["ink"], font_size=22, weight="BOLD")
        banner_box = RoundedRectangle(corner_radius=0.14, width=5.2, height=1.1, fill_color=PALETTE["ink"],
                                       fill_opacity=1, stroke_width=0)
        banner_t = lines("This call may be recorded\nor handled by AI.", 17, PALETTE["bg"], buff=0.08)
        banner = VGroup(banner_box, banner_t.move_to(banner_box.get_center()))
        c1 = chip("rules differ from place to place", w=4.8, h=0.55, fs=15)
        c2 = chip("check what applies to you", w=4.8, h=0.55, fs=15, border=PALETTE["good"], color=PALETTE["good"])
        fo = Text("good hospitality, too", color=PALETTE["accent"], font_size=18)
        l_inner = VGroup(lh, banner, c1, c2, fo).arrange(DOWN, buff=0.3)
        l_box = card_bg(6.2, 5.2)
        left = VGroup(l_box, fit(l_inner, 5.7).move_to(l_box.get_center()))
        left.move_to(LEFT * 3.3)

        a_h = VGroup(helper_icon(), Text("the assistant", color=PALETTE["accent"], font_size=18, weight="BOLD")
                     ).arrange(DOWN, buff=0.25)
        a_l = VGroup(*[Text(t, color=PALETTE["ink"], font_size=15) for t in ("pool hours", "late checkout", "repeat questions")]
                     ).arrange(DOWN, buff=0.15)
        col_a = VGroup(a_h, a_l).arrange(DOWN, buff=0.3)
        t_h = VGroup(person(0.7, PALETTE["accent"], smile=True), Text("the team", color=PALETTE["ink"], font_size=18,
                                                                       weight="BOLD")).arrange(DOWN, buff=0.25)
        t_l = Text("the welcome", color=PALETTE["ink"], font_size=15)
        col_t = VGroup(t_h, t_l).arrange(DOWN, buff=0.3)
        cols = VGroup(col_a, col_t).arrange(RIGHT, buff=0.9, aligned_edge=UP)
        r_head = Text("routine tasks, with people at the center", color=PALETTE["dim"], font_size=15)
        r_inner = VGroup(r_head, cols).arrange(DOWN, buff=0.4)
        r_box = card_bg(5.5, 5.2, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, fit(r_inner, 5.0).move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.4)

        reveal(self, left)
        self.play(FadeIn(banner, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(c2, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(fo), run_time=0.4)
        reveal(self, right)
        self.play(FadeIn(col_a, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(col_t, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)


class B10_PeopleForPeople(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        panel, floor, deco = lobby(11.4, 4.4)
        panel.move_to(UP * 0.8)
        floor.move_to(panel.get_bottom() + UP * 0.37)
        ft = floor.get_top()[1]
        dk = desk(4.2, 0.9).move_to([0.8, ft + 0.45, 0])
        t1 = person(1.15, PALETTE["ink"], smile=True).move_to([-0.3, dk.get_top()[1] + 0.65, 0])
        t2 = person(1.15, PALETTE["accent"], smile=True).move_to([1.9, dk.get_top()[1] + 0.65, 0])
        gs = VGroup(person(1.0, PALETTE["dim"]).move_to([-3.2, ft + 0.72, 0]),
                    person(1.0, PALETTE["good"]).move_to([-2.2, ft + 0.72, 0]),
                    person(1.0, PALETTE["ink"]).move_to([4.2, ft + 0.72, 0]))
        cases = VGroup(suitcase(0.4).move_to([-2.65, ft + 0.3, 0]), suitcase(0.4).move_to([-1.65, ft + 0.3, 0]))
        ph = phone_icon(h=0.7).move_to([2.9, dk.get_top()[1] + 0.4, 0])
        tick = VMobject(color=PALETTE["good"], stroke_width=5).set_points_as_corners(
            [ph.get_center() + [-0.1, 0.0, 0], ph.get_center() + [-0.02, -0.1, 0], ph.get_center() + [0.13, 0.12, 0]])

        q = fit(Text("A hotel where the people have more time for people.", color=PALETTE["ink"], font_size=30,
                     weight="BOLD"), 11.2)
        q.move_to(DOWN * 2.1)
        sub = Text("guests get quick answers  ·  teams get time back", color=PALETTE["dim"], font_size=19)
        sub.move_to(DOWN * 2.85)

        reveal(self, VGroup(panel, VGroup(floor, deco)))
        self.play(FadeIn(VGroup(dk, t1, t2), shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(gs, shift=UP * 0.1), FadeIn(cases), run_time=0.8)
        self.play(FadeIn(ph), Create(tick), run_time=0.7)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(1.5)


class B11_SourcesCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        sh = Text("Sources", color=PALETTE["ink"], font_size=24, weight="BOLD")
        rows = VGroup()
        for n, t in [("SendSquared (2026)", "Hotel AI 2026: The Automation Stack"),
                     ("Omnidim (2026)", "Voice AI for Hotels"),
                     ("Travel Daily News (July 2026)", "AI phone guest service in a Czech hotel"),
                     ("GrowwStacks (2026)", "Voice Agents in Hotels"),
                     ("RaftLabs (2026)", "Voice AI Agents for Hospitality in 2026"),
                     ("AI Agent Rank (May 23, 2026)", "AI for Hospitality & Restaurants 2026")]:
            a = Text(n, color=PALETTE["accent"], font_size=15, weight="BOLD")
            b = Text(t, color=PALETTE["ink"], font_size=14)
            rows.add(VGroup(a, b).arrange(DOWN, buff=0.04, aligned_edge=LEFT))
        rows.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        l_inner = VGroup(sh, rows).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        l_box = card_bg(6.2, 5.4)
        left = VGroup(l_box, fit(l_inner, 5.6).move_to(l_box.get_center()))
        left.move_to(LEFT * 3.3)

        nh = Text("A note on sources", color=PALETTE["miss"], font_size=22, weight="BOLD")
        nb = lines("Most sources are companies that\nbuild hotel AI tools. So the\npercentages are company-reported\nfigures, not independent research.",
                   18, PALETTE["ink"], buff=0.1)
        badge = chip("COMPANY-REPORTED", w=3.4, h=0.55, border=PALETTE["miss"], color=PALETTE["miss"], fs=17)
        ill = lines("The Friday scene is an\nillustration, not a reported case.", 15, PALETTE["ink"], buff=0.08)
        r_inner = VGroup(nh, nb, badge, ill).arrange(DOWN, buff=0.4)
        r_box = card_bg(5.4, 5.4, stroke_color=PALETTE["miss"])
        right = VGroup(r_box, fit(r_inner, 4.9).move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.5)

        reveal(self, left)
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in rows], lag_ratio=0.2), run_time=1.4)
        reveal(self, right)
        self.play(FadeIn(nb, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(badge), run_time=0.4)
        self.play(FadeIn(ill), run_time=0.4)
        self.wait(1.3)
