"""
Manim scenes for chatbot-brand-check

A warm, fair explainer on checking what AI chatbots say about your brand,
sourced from the user-supplied article "Have You Asked the Chatbot About Your
Brand Lately?" No dedicated footage exists (per the user's materials note) --
every visual below is a generated Manim graphic, with no real brand or company
logos (source names appear only as plain text). Every statistic carries its
source and is labeled industry-reported; the bakery scenes are illustrations.
Built in the house Claude palette.

B00B_AgrimaIntro          -- presenter card: "Hi, I'm Agrima." + lead-in
B01_BakeryAsk             -- bakery storefront + a phone chat (illustration)
B02_NewFrontDoor          -- 900 million / 49% / 78% + 52% stat cards (sourced)
B03_NotQuiteRight         -- 3 in 4 brands; small organizations; most-often-wrong facts
B04_TwoNumbers            -- "did any mistake show up?" vs "how many statements were wrong?"
B05_WhereMistakesComeFrom -- old pages feed the chatbot's answer; own pages; training date
B06_WhatOthersSay         -- 25M+ links; 53% managed listings vs 40% brand websites
B07_PeopleDoubleCheck     -- 95% take an extra step; 4% buy from an unfamiliar brand
B08_FiveMinuteCheck       -- the five-step checklist, built row by row on the narration
B09_SmallTeamAccurate     -- a small team looks at an accurate profile
B10_SourcesCard           -- six sources + the industry-reported note
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


def fit_in(mob, max_w, max_h):
    """Scale down (never up) so the group fits inside max_w x max_h."""
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    if mob.height > max_h:
        mob.scale_to_fit_height(max_h)
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


def wait_until(scene, t):
    d = t - scene.renderer.time
    if d > 0.02:
        scene.wait(d)


def chip(label, w=2.6, h=0.6, border=None, color=None, fs=16):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(Text(label, color=color or PALETTE["ink"], font_size=fs), w - 0.3)
    return VGroup(box, txt.move_to(box.get_center()))


def meter(w, frac, color, h=0.2):
    track = RoundedRectangle(corner_radius=0.08, width=w, height=h, fill_color=PALETTE["border"],
                              fill_opacity=1, stroke_width=0)
    fill = RoundedRectangle(corner_radius=0.08, width=max(w * frac, 0.2), height=h, fill_color=color,
                             fill_opacity=1, stroke_width=0).align_to(track, LEFT)
    return VGroup(track, fill)


def src_chip(label, w=3.4, border=None, color=None):
    return chip(label, w=w, h=0.42, border=border or PALETTE["dim"], color=color or PALETTE["dim"], fs=12)


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


def helper_icon(color=None, s=1.0):
    c = color or PALETTE["accent"]
    box = RoundedRectangle(corner_radius=0.14, width=0.95, height=0.7, fill_color=PALETTE["card"],
                           fill_opacity=1, stroke_color=c, stroke_width=3)
    dots = VGroup(*[Dot(radius=0.05, color=c) for _ in range(3)]).arrange(RIGHT, buff=0.12).move_to(box.get_center())
    tail = Polygon([-0.1, 0, 0], [0.1, 0, 0], [0, -0.16, 0], color=c, fill_color=PALETTE["card"],
                   fill_opacity=1, stroke_width=3).next_to(box, DOWN, buff=-0.02).shift(LEFT * 0.2)
    return VGroup(tail, box, dots).scale(s)


def doc_icon(w=0.55, h=0.7, color=None, nlines=3):
    page = RoundedRectangle(corner_radius=0.04, width=w, height=h, fill_color=PALETTE["card"], fill_opacity=1,
                            stroke_color=color or PALETTE["dim"], stroke_width=1.5)
    ln = VGroup(*[Line(LEFT * w * 0.3, RIGHT * w * (0.3 - 0.08 * (i % 2)), color=PALETTE["border"], stroke_width=2)
                  for i in range(nlines)]).arrange(DOWN, buff=h * 0.12).move_to(page.get_center())
    return VGroup(page, ln)


def tick(color=None, s=1.0, sw=4):
    t = VMobject(color=color or PALETTE["good"], stroke_width=sw)
    t.set_points_as_corners([[-0.1, 0.0, 0], [-0.02, -0.1, 0], [0.13, 0.12, 0]])
    return t.scale(s)


def cross(color=None, s=1.0, sw=3.5):
    c = color or PALETTE["miss"]
    return VGroup(Line([-0.09, -0.09, 0], [0.09, 0.09, 0], color=c, stroke_width=sw),
                  Line([-0.09, 0.09, 0], [0.09, -0.09, 0], color=c, stroke_width=sw)).scale(s)


def star_icon(r=0.13, color=None):
    pts = []
    for i in range(10):
        ang = PI / 2 + i * PI / 5
        rad = r if i % 2 == 0 else r * 0.45
        pts.append([rad * np.cos(ang), rad * np.sin(ang), 0])
    return Polygon(*pts, fill_color=color or PALETTE["wood"], fill_opacity=1, stroke_width=0)


def desk_plank(w, h=0.32):
    return RoundedRectangle(corner_radius=0.05, width=w, height=h, fill_color=PALETTE["wood"], fill_opacity=1,
                            stroke_width=0)


def monitor(w=3.4, h=2.5):
    screen = RoundedRectangle(corner_radius=0.1, width=w, height=h, fill_color=PALETTE["card"], fill_opacity=1,
                               stroke_color=PALETTE["ink"], stroke_width=2.5)
    stand = Rectangle(width=0.25, height=0.35, fill_color=PALETTE["ink"], fill_opacity=0.8, stroke_width=0)
    stand.next_to(screen, DOWN, buff=0)
    base = RoundedRectangle(corner_radius=0.04, width=1.0, height=0.1, fill_color=PALETTE["ink"], fill_opacity=0.8,
                            stroke_width=0).next_to(stand, DOWN, buff=0)
    return VGroup(screen, stand, base)


def brand_tile(flag, s=1.0):
    """A small 'brand' tile: a mini storefront outline with a cross (false fact found) or a tick (clear)."""
    col = PALETTE["miss"] if flag else PALETTE["good"]
    box = RoundedRectangle(corner_radius=0.08, width=0.85 * s, height=0.85 * s, fill_color=PALETTE["card"],
                           fill_opacity=1, stroke_color=col, stroke_width=2.5)
    awn = Rectangle(width=0.85 * s, height=0.16 * s, fill_color=col, fill_opacity=0.35, stroke_width=0)
    awn.move_to(box.get_top() + DOWN * 0.16 * s)
    mark = (cross(col, 1.4 * s, 4) if flag else tick(col, 1.6 * s, 4)).move_to(box.get_center() + DOWN * 0.08 * s)
    return VGroup(box, awn, mark)


def storefront(W=4.8, H=3.6):
    body = RoundedRectangle(corner_radius=0.08, width=W, height=H, fill_color=PALETTE["warm"], fill_opacity=1,
                            stroke_color=PALETTE["wood"], stroke_width=2.5)
    n = 6
    sw = (W + 0.2) / n
    stripes = VGroup(*[Rectangle(width=sw, height=0.7, fill_color=PALETTE["accent"] if i % 2 == 0 else PALETTE["card"],
                                 fill_opacity=1, stroke_color=PALETTE["accent"], stroke_width=1)
                       for i in range(n)]).arrange(RIGHT, buff=0)
    stripes.move_to(body.get_top() + DOWN * 0.35)
    sign = card_bg(3.3, 0.5, stroke_color=PALETTE["wood"], fill=PALETTE["card"])
    sign.move_to(body.get_top() + DOWN * 1.15)
    sign_t = fit(Text("Maple Street Bakery", color=PALETTE["ink"], font_size=20, weight="BOLD"), 3.0)
    sign_t.move_to(sign.get_center())
    win = RoundedRectangle(corner_radius=0.06, width=1.9, height=1.4, fill_color=PALETTE["bg"], fill_opacity=1,
                           stroke_color=PALETTE["ink"], stroke_width=2).move_to(body.get_center() + LEFT * 1.2 + DOWN * 0.55)
    loaf1 = Ellipse(width=0.62, height=0.36, fill_color=PALETTE["wood"], fill_opacity=1, stroke_width=0)
    loaf2 = Ellipse(width=0.62, height=0.36, fill_color=PALETTE["accent"], fill_opacity=0.7, stroke_width=0)
    loaf3 = Ellipse(width=0.9, height=0.3, fill_color=PALETTE["wood"], fill_opacity=1, stroke_width=0)
    bread = VGroup(VGroup(loaf1, loaf2).arrange(RIGHT, buff=0.12), loaf3).arrange(DOWN, buff=0.12)
    bread.move_to(win.get_center() + DOWN * 0.1)
    door = RoundedRectangle(corner_radius=0.06, width=1.2, height=2.0, fill_color=PALETTE["wood"], fill_opacity=1,
                            stroke_color=PALETTE["ink"], stroke_width=2).move_to(body.get_center() + RIGHT * 1.4 + DOWN * 0.8)
    knob = Dot(door.get_center() + RIGHT * 0.35, radius=0.05, color=PALETTE["ink"])
    return VGroup(body, stripes, sign, sign_t, win, bread, door, knob)


# --- scenes -----------------------------------------------------------------

class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=40)
        summary = fit(Text(
            "Today: what a chatbot says about your brand.\nIt's the new first impression,\n"
            "and it takes five minutes to check.",
            color=PALETTE["ink"], font_size=26, line_spacing=1.3, should_center=True), 8.6)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.4)


class B01_BakeryAsk(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        shop = storefront(4.8, 3.6).move_to([-3.55, 0.15, 0])
        ground = Line([-6.0, -1.65 + 0.15, 0], [-1.1, -1.65 + 0.15, 0], color=PALETTE["wood"], stroke_width=4)
        friend = Text("a friend mentions it", color=PALETTE["dim"], font_size=15).move_to([-3.55, 2.3, 0])

        phone = RoundedRectangle(corner_radius=0.3, width=3.0, height=5.0, fill_color=PALETTE["card"], fill_opacity=1,
                                 stroke_color=PALETTE["ink"], stroke_width=3).move_to([3.6, 0.1, 0])
        screen = RoundedRectangle(corner_radius=0.2, width=2.7, height=4.6, fill_color=PALETTE["bg"], fill_opacity=1,
                                  stroke_width=0).move_to(phone.get_center())

        ub = card_bg(2.4, 0.9, stroke_color=PALETTE["accent"], fill=PALETTE["accent"])
        ut = lines("What's good at Maple Street\nBakery, and when is it open?", 13, PALETTE["card"], buff=0.05)
        fit(ut, 2.2)
        user_bubble = VGroup(ub, ut.move_to(ub.get_center())).move_to(screen.get_top() + DOWN * 0.95 + RIGHT * 0.1)

        typing = VGroup(*[Dot(radius=0.06, color=PALETTE["dim"]) for _ in range(3)]).arrange(RIGHT, buff=0.14)
        typing.move_to(screen.get_center() + DOWN * 0.1 + LEFT * 0.7)

        ab = card_bg(2.4, 1.9, stroke_color=PALETTE["border"])
        bars = VGroup(*[Line(LEFT * (0.95 - 0.12 * (i % 3)), RIGHT * (0.95 - 0.12 * (i % 3)), color=PALETTE["dim"],
                             stroke_width=3, stroke_opacity=0.55) for i in range(5)]).arrange(DOWN, buff=0.2)
        answer = VGroup(ab, bars.move_to(ab.get_center())).move_to(screen.get_center() + DOWN * 0.45)

        cap = Text("a friendly, confident paragraph", color=PALETTE["dim"], font_size=14).next_to(phone, DOWN, buff=0.12)
        note = chip("illustration -- not a real case", w=4.4, h=0.45, border=PALETTE["ink"], color=PALETTE["ink"], fs=14)
        note.move_to([0, 3.0, 0])
        foot = Text("they decide whether to visit based on the answer", color=PALETTE["ink"], font_size=19)
        foot.move_to([0, -3.05, 0])

        self.play(FadeIn(shop), FadeIn(ground), run_time=0.9)
        self.play(FadeIn(friend, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(phone), FadeIn(screen), run_time=0.6)
        self.play(FadeIn(user_bubble, shift=LEFT * 0.2), run_time=0.7)
        self.play(FadeIn(typing), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(typing), FadeIn(answer, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(cap), run_time=0.4)
        self.play(FadeIn(note), run_time=0.5)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)


class B02_NewFrontDoor(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        badge = chip("INDUSTRY-REPORTED", w=3.4, h=0.5, border=PALETTE["miss"], color=PALETTE["miss"], fs=16)
        badge.move_to(UP * 3.0)

        def stat(n, fs, label, frac=None, color=None):
            col = color or PALETTE["accent"]
            parts = [Text(n, color=col, font_size=fs, weight="BOLD"), lines(label, 14, PALETTE["ink"], buff=0.06)]
            if frac is not None:
                parts.append(meter(2.9, frac, col, h=0.16))
            return VGroup(*parts).arrange(DOWN, buff=0.16)

        # 900 million
        s1 = stat("900 million", 40, "weekly ChatGPT users\nFebruary 2026")
        ic = helper_icon(s=0.9)
        i1 = VGroup(ic, s1, src_chip("OpenAI figure, via BrandMentions, 2026", 3.5)).arrange(DOWN, buff=0.4)
        b1 = card_bg(3.8, 5.0)
        c1 = VGroup(b1, fit_in(i1, 3.4, 4.6).move_to(b1.get_center()))

        # 49% + 42%
        s2 = stat("49%", 52, "of U.S. adults have\nused an AI chatbot", 0.49)
        s2b = stat("42%", 30, "use one to look\nup information", 0.42, PALETTE["good"])
        i2 = VGroup(s2, s2b, src_chip("Pew Research Center, via BrandMentions", 3.5)).arrange(DOWN, buff=0.3)
        b2 = card_bg(3.8, 5.0)
        c2 = VGroup(b2, fit_in(i2, 3.4, 4.6).move_to(b2.get_center()))

        # 78% + 52%
        s3 = stat("78%", 52, "use AI chat tools\nUK survey, 2,564 consumers", 0.78)
        s3b = stat("52%", 30, "of those users say it helps them\nfind brands they would not\nhave discovered otherwise", 0.52,
                   PALETTE["good"])
        i3 = VGroup(s3, s3b, src_chip("CloudNine PR, April 2026", 3.5)).arrange(DOWN, buff=0.3)
        b3 = card_bg(3.8, 5.0)
        c3 = VGroup(b3, fit_in(i3, 3.4, 4.6).move_to(b3.get_center()))

        cards = VGroup(c1, c2, c3).arrange(RIGHT, buff=0.35).move_to(DOWN * 0.3)
        foot = Text("for many brands, the chatbot is now a first impression", color=PALETTE["dim"], font_size=19)
        foot.move_to(DOWN * 3.15)

        self.play(FadeIn(badge, shift=DOWN * 0.1), run_time=0.5)
        for c in (c1, c2, c3):
            reveal(self, c, t1=0.4, t2=0.5)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.5)
        self.wait(1.4)


class B03_NotQuiteRight(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        n = Text("3 in 4", color=PALETTE["accent"], font_size=64, weight="BOLD")
        nl = lines("brands found at least\none false fact", 17, PALETTE["ink"], buff=0.08)
        tiles = VGroup(brand_tile(True), brand_tile(True), brand_tile(True), brand_tile(False)).arrange(RIGHT, buff=0.25)
        tl = Text("1,704 brands graded 32,556 facts", color=PALETTE["dim"], font_size=14)
        src = src_chip("Searchable, 2026 -- brands graded their own facts", 5.0, border=PALETTE["miss"],
                       color=PALETTE["miss"])
        l_inner = VGroup(n, nl, tiles, tl, src).arrange(DOWN, buff=0.25)
        l_box = card_bg(5.8, 5.0)
        left = VGroup(l_box, fit_in(l_inner, 5.3, 4.6).move_to(l_box.get_center()))
        left.move_to(LEFT * 3.2 + UP * 0.15)

        rh = lines("small organizations\nsaw false facts more often", 17, PALETTE["ink"], buff=0.08, weight="BOLD")
        bw = 3.8
        lg = meter(bw, 1.0 / 1.5, PALETTE["dim"], h=0.26)
        sm = meter(bw, 1.0, PALETTE["accent"], h=0.26)
        lgl = Text("large firms", color=PALETTE["dim"], font_size=13)
        sml = Text("small organizations: about 50% more often", color=PALETTE["accent"], font_size=13)
        bars = VGroup(VGroup(lgl, lg).arrange(DOWN, buff=0.06, aligned_edge=LEFT),
                      VGroup(sml, sm).arrange(DOWN, buff=0.06, aligned_edge=LEFT)).arrange(DOWN, buff=0.2)
        mh = Text("most often wrong:", color=PALETTE["miss"], font_size=15, weight="BOLD")
        mc = VGroup(chip("pricing", w=1.4, h=0.5, fs=14), chip("funding", w=1.4, h=0.5, fs=14),
                    chip("which tools it works with", w=3.0, h=0.5, fs=13))
        mc[2].next_to(VGroup(mc[0], mc[1]).arrange(RIGHT, buff=0.15), DOWN, buff=0.15)
        mc_row = VGroup(VGroup(mc[0], mc[1]).arrange(RIGHT, buff=0.15), mc[2]).arrange(DOWN, buff=0.15)
        r_inner = VGroup(rh, bars, mh, mc_row, src_chip("Searchable, 2026", 2.6)).arrange(DOWN, buff=0.3)
        r_box = card_bg(5.2, 5.0, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, fit_in(r_inner, 4.7, 4.6).move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.5 + UP * 0.15)

        foot = Text("chatbots get a lot right, but not everything", color=PALETTE["dim"], font_size=19)
        foot.move_to(DOWN * 3.05)

        reveal(self, left)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in tiles], lag_ratio=0.25), run_time=1.2)
        reveal(self, right)
        self.play(FadeIn(bars, shift=UP * 0.1), run_time=0.7)
        self.play(LaggedStart(FadeIn(mh), FadeIn(mc_row), lag_ratio=0.3), run_time=0.9)
        self.play(FadeIn(foot), run_time=0.5)
        self.wait(1.2)


class B04_TwoNumbers(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # left: counts brands
        q1 = Text("Did any mistake show up?", color=PALETTE["ink"], font_size=22, weight="BOLD")
        c1t = Text("counts whole brands", color=PALETTE["dim"], font_size=15)
        tiles = VGroup(brand_tile(True, 0.9), brand_tile(True, 0.9), brand_tile(True, 0.9),
                       brand_tile(False, 0.9)).arrange(RIGHT, buff=0.22)
        n1 = Text("3 in 4 brands", color=PALETTE["accent"], font_size=34, weight="BOLD")
        s1 = src_chip("Searchable, 2026", 2.6)
        l_inner = VGroup(q1, c1t, tiles, n1, s1).arrange(DOWN, buff=0.3)
        l_box = card_bg(5.5, 4.9)
        left = VGroup(l_box, fit_in(l_inner, 5.0, 4.5).move_to(l_box.get_center()))
        left.move_to(LEFT * 3.2 + UP * 0.35)

        # right: counts claims
        q2 = Text("How many statements were wrong?", color=PALETTE["ink"], font_size=22, weight="BOLD")
        c2t = Text("counts individual claims", color=PALETTE["dim"], font_size=15)
        dots = VGroup(*[Circle(radius=0.11, fill_color=PALETTE["accent"] if i == 6 else PALETTE["border"],
                               fill_opacity=1, stroke_width=0) for i in range(20)]).arrange_in_grid(
            rows=2, cols=10, buff=0.14)
        dl = Text("illustrative: 1 wrong claim in 20", color=PALETTE["dim"], font_size=12)
        n2 = Text("4% to 7%", color=PALETTE["good"], font_size=34, weight="BOLD")
        s2 = src_chip("Sanbi, 2026 (a study by Profound)", 3.6)
        r_inner = VGroup(q2, c2t, VGroup(dots, dl).arrange(DOWN, buff=0.15), n2, s2).arrange(DOWN, buff=0.3)
        r_box = card_bg(5.5, 4.9, stroke_color=PALETTE["good"])
        right = VGroup(r_box, fit_in(r_inner, 5.0, 4.5).move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.2 + UP * 0.35)

        f1 = Text("different questions, different numbers -- they do not conflict", color=PALETTE["dim"], font_size=18)
        f2 = Text("chatbots are mostly right, with mistakes worth catching", color=PALETTE["good"], font_size=20,
                  weight="BOLD")
        foot = VGroup(f1, f2).arrange(DOWN, buff=0.15).move_to(DOWN * 3.0)

        reveal(self, left)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in tiles], lag_ratio=0.2), run_time=1.0)
        self.play(FadeIn(n1), run_time=0.4)
        reveal(self, right)
        self.play(FadeIn(dots), FadeIn(dl), run_time=0.8)
        self.play(FadeIn(n2), run_time=0.4)
        self.play(FadeIn(f1), run_time=0.5)
        self.play(FadeIn(f2, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)


class B05_WhereMistakesComeFrom(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        def source_card(icon, label, tag):
            t = lines(label, 16, PALETTE["ink"], buff=0.05)
            tg = Text(tag, color=PALETTE["miss"], font_size=12, weight="BOLD")
            txt = VGroup(t, tg).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            inner = VGroup(icon, txt).arrange(RIGHT, buff=0.3)
            box = card_bg(4.1, 1.25)
            return VGroup(box, fit_in(inner, 3.8, 1.05).move_to(box.get_center()))

        price_doc = RoundedRectangle(corner_radius=0.04, width=0.7, height=0.9, fill_color=PALETTE["card"],
                                     fill_opacity=1, stroke_color=PALETTE["dim"], stroke_width=1.5)
        price_tag = Text("$", color=PALETTE["accent"], font_size=30, weight="BOLD").move_to(price_doc.get_center())
        icon1 = VGroup(price_doc, price_tag)
        icon2 = VGroup(*[star_icon(0.13) for _ in range(3)]).arrange(RIGHT, buff=0.04)
        icon3 = doc_icon(0.7, 0.9, nlines=4)
        cards = VGroup(source_card(icon1, "an old\npricing page", "OUT OF DATE"),
                       source_card(icon2, "an outdated\nreview", "OUT OF DATE"),
                       source_card(icon3, "an old comparison\narticle", "OUT OF DATE")).arrange(DOWN, buff=0.25)
        cards.move_to([-4.0, 0.25, 0])

        bot = helper_icon(s=1.4).move_to([-0.35, 0.4, 0])
        botl = Text("the chatbot's answer", color=PALETTE["accent"], font_size=15).next_to(bot, DOWN, buff=0.3)
        wrong = chip("repeats the old detail", w=2.6, h=0.45, border=PALETTE["miss"], color=PALETTE["miss"], fs=13)
        wrong.next_to(botl, DOWN, buff=0.2)
        arrows = VGroup(*[Arrow(c.get_right() + RIGHT * 0.05, bot.get_center() + LEFT * 0.75 + UP * (0.18 * k), color=PALETTE["accent"],
                                 stroke_width=3.5, buff=0.08, max_tip_length_to_length_ratio=0.2)
                          for c, k in zip(cards, (1, 0, -1))])

        hn = Text(">50%", color=PALETTE["accent"], font_size=52, weight="BOLD")
        hl = lines("of brands studied: the brand's\nown pages were among the\nsources behind the mistake", 14,
                   PALETTE["ink"], buff=0.06)
        hm = meter(3.4, 0.55, PALETTE["accent"], h=0.16)
        hs = src_chip("Sanbi, 2026", 2.2)
        div = Line(LEFT * 1.8, RIGHT * 1.8, color=PALETTE["border"], stroke_width=2)
        tm = chip("memory stops at a training date", w=3.8, h=0.5, border=PALETTE["dim"], fs=13)
        tl = lines("so a new address or\nprice may be missing", 14, PALETTE["ink"], buff=0.06)
        ts = src_chip("SubscribePR, 2026", 2.4)
        r_inner = VGroup(hn, hl, hm, hs, div, tm, tl, ts).arrange(DOWN, buff=0.2)
        r_box = card_bg(4.6, 5.2, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, fit_in(r_inner, 4.1, 4.9).move_to(r_box.get_center()))
        right.move_to([3.85, 0.15, 0])

        foot = Text("most errors are not made up -- they trace back to real pages", color=PALETTE["good"],
                    font_size=19, weight="BOLD").move_to(DOWN * 3.1)

        for c in cards:
            self.play(FadeIn(c, shift=RIGHT * 0.2), run_time=0.6)
        self.play(FadeIn(bot), FadeIn(botl), run_time=0.6)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.25), run_time=1.0)
        self.play(FadeIn(wrong, shift=UP * 0.1), run_time=0.5)
        reveal(self, right)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)


class B06_WhatOthersSay(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        n1 = Text("25 million+", color=PALETTE["accent"], font_size=48, weight="BOLD")
        l1 = lines("AI-cited links analyzed", 17, PALETTE["ink"], buff=0.08)
        srcs = VGroup(chip("news", w=1.5, h=0.5, fs=14), chip("reviews", w=1.5, h=0.5, fs=14),
                      chip("others' coverage", w=2.2, h=0.5, fs=14)).arrange(RIGHT, buff=0.15)
        arr = Arrow(UP * 0.35, DOWN * 0.35, color=PALETTE["accent"], stroke_width=4, buff=0,
                    max_tip_length_to_length_ratio=0.45)
        most = lines("coverage written by others\nmade up most of the citations", 17, PALETTE["accent"], buff=0.08,
                     weight="BOLD")
        s1 = src_chip("BrandMentions, 2026", 2.8)
        l_inner = VGroup(n1, l1, srcs, arr, most, s1).arrange(DOWN, buff=0.28)
        l_box = card_bg(5.8, 5.0)
        left = VGroup(l_box, fit_in(l_inner, 5.3, 4.6).move_to(l_box.get_center()))
        left.move_to(LEFT * 3.2 + UP * 0.15)

        rh = lines("share of ChatGPT's citations\nin another analysis", 16, PALETTE["ink"], buff=0.08)
        a_n = Text("about 53%", color=PALETTE["accent"], font_size=40, weight="BOLD")
        a_l = Text("managed listings, like business profiles", color=PALETTE["ink"], font_size=14)
        a_m = meter(4.0, 0.53, PALETTE["accent"], h=0.24)
        b_n = Text("about 40%", color=PALETTE["dim"], font_size=40, weight="BOLD")
        b_l = Text("brand websites", color=PALETTE["ink"], font_size=14)
        b_m = meter(4.0, 0.40, PALETTE["dim"], h=0.24)
        ga = VGroup(a_n, a_l, a_m).arrange(DOWN, buff=0.1)
        gb = VGroup(b_n, b_l, b_m).arrange(DOWN, buff=0.1)
        s2 = src_chip("Yext, 2026", 2.2)
        r_inner = VGroup(rh, ga, gb, s2).arrange(DOWN, buff=0.3)
        r_box = card_bg(5.4, 5.0, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, fit_in(r_inner, 4.9, 4.6).move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.4 + UP * 0.15)

        foot = Text("profiles and reviews can matter as much as your own website", color=PALETTE["dim"], font_size=19)
        foot.move_to(DOWN * 3.05)

        reveal(self, left)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in srcs], lag_ratio=0.3), run_time=1.0)
        self.play(GrowArrow(arr), FadeIn(most), run_time=0.7)
        reveal(self, right)
        self.play(FadeIn(ga, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(gb, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(foot), run_time=0.5)
        self.wait(1.2)


class B07_PeopleDoubleCheck(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        n1 = Text("95%", color=PALETTE["accent"], font_size=60, weight="BOLD")
        l1 = lines("took at least one extra step before\nacting on an AI recommendation", 16, PALETTE["ink"], buff=0.08)
        m1 = meter(3.6, 0.95, PALETTE["accent"], h=0.2)
        chips = VGroup(chip("visit the website", w=2.0, h=0.48, fs=13), chip("read reviews", w=1.7, h=0.48, fs=13),
                       chip("check a profile", w=1.9, h=0.48, fs=13)).arrange(RIGHT, buff=0.12)
        sv = Text("survey of 3,848 people", color=PALETTE["dim"], font_size=13)
        s1 = src_chip("Yext, 2026", 2.2)
        l_inner = VGroup(n1, l1, m1, chips, sv, s1).arrange(DOWN, buff=0.26)
        l_box = card_bg(5.8, 4.9)
        left = VGroup(l_box, fit_in(l_inner, 5.4, 4.5).move_to(l_box.get_center()))
        left.move_to(LEFT * 3.3 + UP * 0.35)

        n2 = Text("4%", color=PALETTE["good"], font_size=60, weight="BOLD")
        l2 = lines("of U.K. AI users would buy from\nan unfamiliar brand right away", 16, PALETTE["ink"], buff=0.08)
        m2 = meter(3.6, 0.04, PALETTE["good"], h=0.2)
        s2 = src_chip("CloudNine PR, 2026", 2.8)
        r_inner = VGroup(n2, l2, m2, s2).arrange(DOWN, buff=0.3)
        r_box = card_bg(5.2, 4.9, stroke_color=PALETTE["good"])
        right = VGroup(r_box, fit_in(r_inner, 4.7, 4.5).move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.5 + UP * 0.35)

        f1 = Text("The chatbot opens the door. Your website and reviews do the rest.", color=PALETTE["ink"],
                  font_size=19, weight="BOLD")
        f2 = Text("If they disagree, a visitor may wonder which to believe.", color=PALETTE["dim"], font_size=17)
        foot = VGroup(f1, f2).arrange(DOWN, buff=0.15).move_to(DOWN * 3.0)

        reveal(self, left)
        self.play(FadeIn(m1), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in chips], lag_ratio=0.3), run_time=1.0)
        reveal(self, right)
        self.play(FadeIn(f1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(f2), run_time=0.5)
        self.wait(1.2)


class B08_FiveMinuteCheck(Scene):
    """Rows land on the narration: 'One' ~2.0s, 'Two' ~7.6s, 'Three' ~16.0s, 'Four' ~20.2s, 'Five' ~30.2s."""

    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        CARD_W, CARD_H = 11.6, 6.3
        card = card_bg(CARD_W, CARD_H).move_to([0, -0.05, 0])
        title = Text("The five-minute check", color=PALETTE["ink"], font_size=26, weight="BOLD")
        title.move_to([0, card.get_top()[1] - 0.45, 0])
        rule = Line(LEFT * 1.0, RIGHT * 1.0, color=PALETTE["accent"], stroke_width=3).next_to(title, DOWN, buff=0.12)

        X_NUM, X_TXT = -5.1, -4.5
        heights = [0.7, 1.3, 0.7, 1.3, 0.7]
        gap = 0.14
        y = rule.get_bottom()[1] - 0.2
        rows = []
        for i, h in enumerate(heights):
            top = y
            ctr = top - h / 2
            band = RoundedRectangle(corner_radius=0.08, width=CARD_W - 0.5, height=h, fill_color=PALETTE["bg"],
                                    fill_opacity=1, stroke_color=PALETTE["border"], stroke_width=1.2).move_to([0, ctr, 0])
            circ = Circle(radius=0.22, fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
            num = Text(str(i + 1), color=PALETTE["card"], font_size=20, weight="BOLD").move_to(circ.get_center())
            numg = VGroup(circ, num).move_to([X_NUM, top - 0.4, 0])
            rows.append({"band": band, "num": numg, "top": top, "h": h})
            y = top - h - gap

        def label(txt, i, fs=20, color=None, bold=False):
            t = Text(txt, color=color or PALETTE["ink"], font_size=fs, weight="BOLD" if bold else "NORMAL")
            t = fit(t, 9.6)
            t.move_to([X_TXT, rows[i]["top"] - 0.4, 0], aligned_edge=LEFT)
            t.align_to([X_TXT, 0, 0], LEFT)
            return t

        t1 = label("Ask two or three different chatbots", 0, bold=True)
        t1s = label("the same mistake rarely shows up everywhere", 0, fs=14, color=PALETTE["dim"])
        t1s.next_to(t1, RIGHT, buff=0.3)
        t2 = label("Ask like a customer would", 1, bold=True)
        qs = ["what is it?", "what does it cost?", "where and when is it open?", "is it any good?", "what are the alternatives?"]
        qchips = VGroup(*[
            chip(q, w=max(1.1, 0.072 * len(q) + 0.4), h=0.42, fs=12) for q in qs]).arrange(RIGHT, buff=0.12)
        qchips.move_to([X_TXT + qchips.width / 2, rows[1]["top"] - 0.95, 0])
        t3 = label("Note what is right, wrong, and missing", 2, bold=True)
        t3s = label("and any sources the chatbot names", 2, fs=14, color=PALETTE["dim"])
        t3s.next_to(t3, RIGHT, buff=0.3)
        t4 = label("Fix it at the source", 3, bold=True)
        fx = ["old pricing pages", "hours", "addresses", "profiles and reviews match your website"]
        fchips = VGroup(*[chip(f, w=max(1.1, 0.072 * len(f) + 0.4), h=0.42, fs=12,
                               border=PALETTE["good"]) for f in fx]).arrange(RIGHT, buff=0.12)
        fchips.move_to([X_TXT + fchips.width / 2, rows[3]["top"] - 0.95, 0])
        t5 = label("Check again in a few weeks", 4, bold=True)
        t5s = label("answers can change, so a quick repeat helps", 4, fs=14, color=PALETTE["dim"])
        t5s.next_to(t5, RIGHT, buff=0.3)

        ticks = [tick(PALETTE["good"], 1.1).move_to([5.1, r["top"] - 0.4, 0]) for r in rows]

        self.play(FadeIn(card), run_time=0.4)
        self.play(FadeIn(title), FadeIn(rule), run_time=0.4)
        for r in rows:
            self.add(r["band"])
            self.add(r["num"])
        for r in rows:
            r["band"].set_opacity(0)
            r["num"].set_opacity(0)

        def show(i, texts, t_at):
            wait_until(self, t_at)
            self.play(rows[i]["band"].animate.set_fill(opacity=1).set_stroke(opacity=1),
                      rows[i]["num"].animate.set_opacity(1), *[FadeIn(t) for t in texts], run_time=0.5)

        def done(i):
            self.play(FadeIn(ticks[i]), run_time=0.3)

        show(0, [t1, t1s], 2.0)
        wait_until(self, 7.0)
        done(0)
        show(1, [t2], 7.6)
        for k, qc in enumerate(qchips):
            wait_until(self, [9.8, 10.6, 11.6, 13.4, 14.4][k])
            self.play(FadeIn(qc, shift=UP * 0.1), run_time=0.35)
        wait_until(self, 15.6)
        done(1)
        show(2, [t3, t3s], 16.0)
        wait_until(self, 19.7)
        done(2)
        show(3, [t4], 20.2)
        for k, fc in enumerate(fchips):
            wait_until(self, [22.5, 23.7, 24.6, 25.9][k])
            self.play(FadeIn(fc, shift=UP * 0.1), run_time=0.35)
        wait_until(self, 29.5)
        done(3)
        show(4, [t5, t5s], 30.2)
        wait_until(self, 31.6)
        done(4)
        self.wait(0.5)


class B09_SmallTeamAccurate(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        panel = RoundedRectangle(corner_radius=0.14, width=12.0, height=5.0, fill_color=PALETTE["warm"],
                                 fill_opacity=1, stroke_color=PALETTE["border"], stroke_width=1.5)
        panel.move_to(UP * 0.55)
        plank = desk_plank(11.4).move_to([0, -1.55, 0])
        top_y = plank.get_top()[1]

        team = VGroup(person(1.35, PALETTE["ink"], smile=True), person(1.35, PALETTE["accent"], smile=True),
                      person(1.35, PALETTE["good"], smile=True)).arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
        team.move_to([-3.6, top_y + team.height / 2, 0])
        tl = Text("a small team", color=PALETTE["dim"], font_size=15).move_to([-3.6, 2.55, 0])

        mon = monitor(4.6, 3.0)
        mon.move_to([2.3, top_y + 0.35 + 0.1 + 1.5, 0])
        scr = mon[0]
        head = RoundedRectangle(corner_radius=0.06, width=3.8, height=0.5, fill_color=PALETTE["accent"], fill_opacity=0.18,
                                stroke_width=0).move_to(scr.get_top() + DOWN * 0.5)
        hbar = Line(LEFT * 1.2, RIGHT * 1.2, color=PALETTE["ink"], stroke_width=5).move_to(head.get_center())
        items = VGroup()
        for lab in ["hours", "address", "prices"]:
            tk = tick(PALETTE["good"], 1.0)
            tx = Text(lab, color=PALETTE["ink"], font_size=20)
            bar = Line(ORIGIN, RIGHT * 1.6, color=PALETTE["border"], stroke_width=4)
            items.add(VGroup(tk, tx, bar).arrange(RIGHT, buff=0.3))
        items.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        items.move_to(scr.get_center() + DOWN * 0.45)
        ml = Text("an accurate, current profile", color=PALETTE["good"], font_size=15).move_to([2.3, 2.55, 0])

        note = chip("illustration", w=1.8, h=0.4, border=PALETTE["ink"], color=PALETTE["ink"], fs=12)
        note.move_to([5.0, 2.55, 0])

        q1 = Text("Not about gaming a chatbot.", color=PALETTE["ink"], font_size=26, weight="BOLD")
        q2 = Text("About making accurate, current information easy to find.", color=PALETTE["accent"], font_size=26,
                  weight="BOLD")
        qs = VGroup(q1, q2).arrange(DOWN, buff=0.15)
        fit(qs, 11.2)
        qs.move_to(DOWN * 2.85)

        self.play(FadeIn(panel), FadeIn(plank), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.1) for p in team], lag_ratio=0.25), FadeIn(tl), run_time=1.0)
        self.play(FadeIn(mon), FadeIn(ml), run_time=0.6)
        self.play(FadeIn(head), FadeIn(hbar), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(it, shift=RIGHT * 0.1) for it in items], lag_ratio=0.35), run_time=1.4)
        self.play(FadeIn(note), run_time=0.4)
        self.play(FadeIn(q1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


class B10_SourcesCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        sh = Text("Sources", color=PALETTE["ink"], font_size=24, weight="BOLD")
        rows = VGroup()
        for n, t in [("BrandMentions (2026)", "How to check what ChatGPT says about your brand"),
                     ("CloudNine PR (2026)", "ChatGPT helps consumers discover new brands (press release)"),
                     ("Sanbi (2026)", "Inaccurate AI claims about your brand: causes and fixes"),
                     ("Searchable (July 30, 2026)", "The AI brand misinformation report"),
                     ("SubscribePR (2026)", "ChatGPT says wrong things about your business"),
                     ("Yext (2026)", "Cracking the ChatGPT code: brand visibility in OpenAI")]:
            a = Text(n, color=PALETTE["accent"], font_size=15, weight="BOLD")
            b = fit(Text(t, color=PALETTE["ink"], font_size=13), 5.4)
            rows.add(VGroup(a, b).arrange(DOWN, buff=0.04, aligned_edge=LEFT))
        rows.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        l_inner = VGroup(sh, rows).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        l_box = card_bg(6.2, 5.4)
        left = VGroup(l_box, fit_in(l_inner, 5.7, 5.0).move_to(l_box.get_center()))
        left.move_to(LEFT * 3.1)

        nh = Text("A note on sources", color=PALETTE["miss"], font_size=22, weight="BOLD")
        nb = lines("Most of these sources are companies\nthat sell marketing, PR, or\nbrand-monitoring services. So the\nstatistics are industry-reported,\nnot independent research.",
                   16, PALETTE["ink"], buff=0.08)
        badge = chip("INDUSTRY-REPORTED", w=3.6, h=0.55, border=PALETTE["miss"], color=PALETTE["miss"], fs=17)
        gr = lines("One study (Searchable) was graded by\nthe brands themselves.", 14, PALETTE["ink"], buff=0.06)
        ill = lines("The bakery scene is an illustration,\nnot a reported case.", 14, PALETTE["dim"], buff=0.06)
        r_inner = VGroup(nh, nb, badge, gr, ill).arrange(DOWN, buff=0.3)
        r_box = card_bg(5.4, 5.4, stroke_color=PALETTE["miss"])
        right = VGroup(r_box, fit_in(r_inner, 4.9, 5.0).move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.5)

        reveal(self, left)
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in rows], lag_ratio=0.2), run_time=1.6)
        reveal(self, right)
        self.play(FadeIn(nb, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(badge), run_time=0.4)
        self.play(FadeIn(gr), run_time=0.4)
        self.play(FadeIn(ill), run_time=0.4)
        self.wait(1.3)
