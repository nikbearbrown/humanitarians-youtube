"""
Portrait (9:16) Manim scenes for chatbot-brand-check-short

Ports of the eight graphic beats kept in the Shorts cut (B00B, B01, B03, B04,
B05, B08, B09, B10). Stacked layouts for a 4.5 x 8.0 frame; same palette and
copy as the 16:9 scenes. Dropped beats (B02, B06, B07) live only in the long
cut. All visuals are generated; no real brand or company logos.
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


def chip(label, w=2.6, h=0.4, border=None, color=None, fs=11):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(Text(label, color=color or PALETTE["ink"], font_size=fs), w - 0.2)
    return VGroup(box, txt.move_to(box.get_center()))


def meter(w, frac, color, h=0.14):
    track = RoundedRectangle(corner_radius=0.06, width=w, height=h, fill_color=PALETTE["border"],
                              fill_opacity=1, stroke_width=0)
    fill = RoundedRectangle(corner_radius=0.06, width=max(w * frac, 0.15), height=h, fill_color=color,
                             fill_opacity=1, stroke_width=0).align_to(track, LEFT)
    return VGroup(track, fill)


def src_chip(label, w=2.4):
    return chip(label, w=w, h=0.3, border=PALETTE["dim"], color=PALETTE["dim"], fs=9)


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


def tick(color=None, s=1.0, sw=3.5):
    t = VMobject(color=color or PALETTE["good"], stroke_width=sw)
    t.set_points_as_corners([[-0.1, 0.0, 0], [-0.02, -0.1, 0], [0.13, 0.12, 0]])
    return t.scale(s)


def cross(color=None, s=1.0, sw=3):
    c = color or PALETTE["miss"]
    return VGroup(Line([-0.09, -0.09, 0], [0.09, 0.09, 0], color=c, stroke_width=sw),
                  Line([-0.09, 0.09, 0], [0.09, -0.09, 0], color=c, stroke_width=sw)).scale(s)


def star_icon(r=0.1, color=None):
    pts = []
    for i in range(10):
        ang = PI / 2 + i * PI / 5
        rad = r if i % 2 == 0 else r * 0.45
        pts.append([rad * np.cos(ang), rad * np.sin(ang), 0])
    return Polygon(*pts, fill_color=color or PALETTE["wood"], fill_opacity=1, stroke_width=0)


def desk_plank(w, h=0.28):
    return RoundedRectangle(corner_radius=0.05, width=w, height=h, fill_color=PALETTE["wood"], fill_opacity=1,
                            stroke_width=0)


def monitor(w, h):
    screen = RoundedRectangle(corner_radius=0.08, width=w, height=h, fill_color=PALETTE["card"], fill_opacity=1,
                               stroke_color=PALETTE["ink"], stroke_width=2.5)
    stand = Rectangle(width=0.2, height=0.28, fill_color=PALETTE["ink"], fill_opacity=0.8, stroke_width=0)
    stand.next_to(screen, DOWN, buff=0)
    base = RoundedRectangle(corner_radius=0.04, width=0.7, height=0.08, fill_color=PALETTE["ink"], fill_opacity=0.8,
                            stroke_width=0).next_to(stand, DOWN, buff=0)
    return VGroup(screen, stand, base)


def brand_tile(flag, s=1.0):
    col = PALETTE["miss"] if flag else PALETTE["good"]
    box = RoundedRectangle(corner_radius=0.07, width=0.7 * s, height=0.7 * s, fill_color=PALETTE["card"],
                           fill_opacity=1, stroke_color=col, stroke_width=2.2)
    awn = Rectangle(width=0.7 * s, height=0.13 * s, fill_color=col, fill_opacity=0.35, stroke_width=0)
    awn.move_to(box.get_top() + DOWN * 0.13 * s)
    mark = (cross(col, 1.15 * s, 3.5) if flag else tick(col, 1.3 * s, 3.5)).move_to(box.get_center() + DOWN * 0.06 * s)
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

        name = fit(Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=38), 3.4)
        summary = lines("Today: what a chatbot\nsays about your brand.\nIt's the new first impression,\nand it takes five minutes\nto check.",
                        21, PALETTE["ink"], max_w=3.4, buff=0.2)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        VGroup(name, rule, summary).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.4)


class B01_BakeryAsk(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        note = chip("illustration -- not a real case", w=3.2, h=0.4, border=PALETTE["ink"], color=PALETTE["ink"], fs=11)
        note.move_to([0, 3.2, 0])

        shop = storefront(4.8, 3.6).scale(0.62).move_to([0, 1.75, 0])

        phone = RoundedRectangle(corner_radius=0.25, width=2.5, height=2.9, fill_color=PALETTE["card"], fill_opacity=1,
                                 stroke_color=PALETTE["ink"], stroke_width=3).move_to([0, -1.25, 0])
        screen = RoundedRectangle(corner_radius=0.18, width=2.25, height=2.65, fill_color=PALETTE["bg"], fill_opacity=1,
                                  stroke_width=0).move_to(phone.get_center())

        ub = card_bg(2.05, 0.62, stroke_color=PALETTE["accent"], fill=PALETTE["accent"])
        ut = fit(lines("What's good at Maple Street\nBakery, and when is it open?", 8, PALETTE["card"], buff=0.04), 1.85)
        user_bubble = VGroup(ub, ut.move_to(ub.get_center())).move_to(screen.get_top() + DOWN * 0.5)

        typing = VGroup(*[Dot(radius=0.05, color=PALETTE["dim"]) for _ in range(3)]).arrange(RIGHT, buff=0.12)
        typing.move_to(screen.get_center() + DOWN * 0.1 + LEFT * 0.6)

        ab = card_bg(2.05, 1.2, stroke_color=PALETTE["border"])
        bars = VGroup(*[Line(LEFT * (0.8 - 0.1 * (i % 3)), RIGHT * (0.8 - 0.1 * (i % 3)), color=PALETTE["dim"],
                             stroke_width=2.5, stroke_opacity=0.55) for i in range(4)]).arrange(DOWN, buff=0.15)
        answer = VGroup(ab, bars.move_to(ab.get_center())).move_to(screen.get_center() + DOWN * 0.3)

        foot = lines("they decide whether to visit\nbased on the answer", 12, PALETTE["ink"], buff=0.05)
        foot.move_to([0, -3.0, 0])

        self.play(FadeIn(note), run_time=0.4)
        self.play(FadeIn(shop), run_time=0.9)
        self.play(FadeIn(phone), FadeIn(screen), run_time=0.6)
        self.play(FadeIn(user_bubble, shift=LEFT * 0.15), run_time=0.7)
        self.play(FadeIn(typing), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(typing), FadeIn(answer, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)


class B03_NotQuiteRight(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        n = Text("3 in 4", color=PALETTE["accent"], font_size=40, weight="BOLD")
        nl = lines("brands found at least one false fact", 11, PALETTE["ink"], buff=0.04)
        tiles = VGroup(brand_tile(True, 0.8), brand_tile(True, 0.8), brand_tile(True, 0.8),
                       brand_tile(False, 0.8)).arrange(RIGHT, buff=0.18)
        tl = Text("1,704 brands graded 32,556 facts", color=PALETTE["dim"], font_size=9)
        src = chip("Searchable, 2026 -- brands graded their own facts", w=3.4, h=0.3, border=PALETTE["miss"],
                   color=PALETTE["miss"], fs=9)
        a_inner = VGroup(n, nl, tiles, tl, src).arrange(DOWN, buff=0.12)
        a_box = card_bg(3.7, 2.8)
        top = VGroup(a_box, fit_in(a_inner, 3.4, 2.55).move_to(a_box.get_center()))
        top.move_to(UP * 1.85)

        rh = lines("small organizations saw\nfalse facts more often", 11, PALETTE["ink"], buff=0.04, weight="BOLD")
        lg = meter(3.0, 1.0 / 1.5, PALETTE["dim"], h=0.16)
        sm = meter(3.0, 1.0, PALETTE["accent"], h=0.16)
        lgl = Text("large firms", color=PALETTE["dim"], font_size=9)
        sml = Text("small organizations: about 50% more often", color=PALETTE["accent"], font_size=9)
        bars = VGroup(VGroup(lgl, lg).arrange(DOWN, buff=0.04, aligned_edge=LEFT),
                      VGroup(sml, sm).arrange(DOWN, buff=0.04, aligned_edge=LEFT)).arrange(DOWN, buff=0.1)
        mh = Text("most often wrong:", color=PALETTE["miss"], font_size=10, weight="BOLD")
        row1 = VGroup(chip("pricing", w=1.0, h=0.3, fs=9), chip("funding", w=1.0, h=0.3, fs=9),
                      chip("which tools it works with", w=1.7, h=0.3, fs=9)).arrange(RIGHT, buff=0.1)
        s2 = src_chip("Searchable, 2026", 1.8)
        b_inner = VGroup(rh, bars, mh, row1, s2).arrange(DOWN, buff=0.11)
        b_box = card_bg(3.7, 2.8, stroke_color=PALETTE["accent"])
        bottom = VGroup(b_box, fit_in(b_inner, 3.4, 2.55).move_to(b_box.get_center()))
        bottom.move_to(DOWN * 1.2)

        foot = Text("chatbots get a lot right, but not everything", color=PALETTE["dim"], font_size=10)
        fit(foot, 3.6).move_to(DOWN * 3.05)

        reveal(self, top)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in tiles], lag_ratio=0.25), run_time=1.2)
        reveal(self, bottom)
        self.play(FadeIn(bars, shift=UP * 0.1), run_time=0.7)
        self.play(LaggedStart(FadeIn(mh), FadeIn(row1), lag_ratio=0.3), run_time=0.9)
        self.play(FadeIn(foot), run_time=0.5)
        self.wait(1.2)


class B04_TwoNumbers(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        q1 = fit(Text("Did any mistake show up?", color=PALETTE["ink"], font_size=14, weight="BOLD"), 3.3)
        c1t = Text("counts whole brands", color=PALETTE["dim"], font_size=10)
        tiles = VGroup(brand_tile(True, 0.65), brand_tile(True, 0.65), brand_tile(True, 0.65),
                       brand_tile(False, 0.65)).arrange(RIGHT, buff=0.14)
        n1 = Text("3 in 4 brands", color=PALETTE["accent"], font_size=24, weight="BOLD")
        s1 = src_chip("Searchable, 2026", 1.8)
        a_inner = VGroup(q1, c1t, tiles, n1, s1).arrange(DOWN, buff=0.1)
        a_box = card_bg(3.7, 2.5)
        top = VGroup(a_box, fit_in(a_inner, 3.4, 2.3).move_to(a_box.get_center()))
        top.move_to(UP * 1.95)

        q2 = fit(Text("How many statements were wrong?", color=PALETTE["ink"], font_size=14, weight="BOLD"), 3.4)
        c2t = Text("counts individual claims", color=PALETTE["dim"], font_size=10)
        dots = VGroup(*[Circle(radius=0.07, fill_color=PALETTE["accent"] if i == 6 else PALETTE["border"],
                               fill_opacity=1, stroke_width=0) for i in range(20)]).arrange_in_grid(
            rows=2, cols=10, buff=0.09)
        dl = Text("illustrative: 1 wrong claim in 20", color=PALETTE["dim"], font_size=8)
        n2 = Text("4% to 7%", color=PALETTE["good"], font_size=24, weight="BOLD")
        s2 = src_chip("Sanbi, 2026 (a study by Profound)", 2.7)
        b_inner = VGroup(q2, c2t, VGroup(dots, dl).arrange(DOWN, buff=0.06), n2, s2).arrange(DOWN, buff=0.1)
        b_box = card_bg(3.7, 2.5, stroke_color=PALETTE["good"])
        bottom = VGroup(b_box, fit_in(b_inner, 3.4, 2.3).move_to(b_box.get_center()))
        bottom.move_to(DOWN * 0.8)

        f1 = Text("different questions, different numbers", color=PALETTE["dim"], font_size=10)
        f2 = lines("chatbots are mostly right,\nwith mistakes worth catching", 11, PALETTE["good"], buff=0.04, weight="BOLD")
        foot = VGroup(f1, f2).arrange(DOWN, buff=0.08).move_to(DOWN * 2.95)

        reveal(self, top)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in tiles], lag_ratio=0.2), run_time=1.0)
        self.play(FadeIn(n1), run_time=0.4)
        reveal(self, bottom)
        self.play(FadeIn(dots), FadeIn(dl), run_time=0.8)
        self.play(FadeIn(n2), run_time=0.4)
        self.play(FadeIn(f1), run_time=0.5)
        self.play(FadeIn(f2, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)


class B05_WhereMistakesComeFrom(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        def source_card(icon, label):
            t = Text(label, color=PALETTE["ink"], font_size=11)
            tg = Text("OUT OF DATE", color=PALETTE["miss"], font_size=7, weight="BOLD")
            txt = VGroup(t, tg).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
            inner = VGroup(icon, txt).arrange(RIGHT, buff=0.25)
            box = card_bg(3.7, 0.62)
            return VGroup(box, fit_in(inner, 3.4, 0.5).move_to(box.get_center()))

        price_doc = RoundedRectangle(corner_radius=0.03, width=0.34, height=0.44, fill_color=PALETTE["card"],
                                     fill_opacity=1, stroke_color=PALETTE["dim"], stroke_width=1.5)
        price_tag = Text("$", color=PALETTE["accent"], font_size=16, weight="BOLD").move_to(price_doc.get_center())
        icon1 = VGroup(price_doc, price_tag)
        icon2 = VGroup(*[star_icon(0.08) for _ in range(3)]).arrange(RIGHT, buff=0.03)
        icon3 = doc_icon(0.34, 0.44, nlines=3)
        cards = VGroup(source_card(icon1, "an old pricing page"), source_card(icon2, "an outdated review"),
                       source_card(icon3, "an old comparison article")).arrange(DOWN, buff=0.1)
        cards.move_to([0, 2.2, 0])

        arr = Arrow(UP * 0.17, DOWN * 0.17, color=PALETTE["accent"], stroke_width=3, buff=0,
                    max_tip_length_to_length_ratio=0.5).move_to([0, 0.88, 0])
        bot = helper_icon(s=0.5)
        botl = Text("the chatbot's answer", color=PALETTE["accent"], font_size=10)
        wrong = chip("repeats the old detail", w=1.9, h=0.3, border=PALETTE["miss"], color=PALETTE["miss"], fs=9)
        bot_row = VGroup(bot, VGroup(botl, wrong).arrange(DOWN, buff=0.07, aligned_edge=LEFT)).arrange(RIGHT, buff=0.25)
        bot_row.move_to([0, 0.45, 0])

        hn = Text(">50%", color=PALETTE["accent"], font_size=30, weight="BOLD")
        hl = lines("of brands studied: the brand's own\npages were among the sources", 9, PALETTE["ink"], buff=0.04)
        hm = meter(2.6, 0.55, PALETTE["accent"], h=0.12)
        hs = src_chip("Sanbi, 2026", 1.5)
        c1_inner = VGroup(hn, hl, hm, hs).arrange(DOWN, buff=0.07)
        c1_box = card_bg(3.7, 1.55, stroke_color=PALETTE["accent"])
        c1 = VGroup(c1_box, fit_in(c1_inner, 3.4, 1.4).move_to(c1_box.get_center()))
        c1.move_to([0, -0.75, 0])

        tm = chip("memory stops at a training date", w=3.1, h=0.3, border=PALETTE["dim"], fs=9)
        tl = Text("so a new address or price may be missing", color=PALETTE["ink"], font_size=9)
        ts = src_chip("SubscribePR, 2026", 1.7)
        c2_inner = VGroup(tm, tl, ts).arrange(DOWN, buff=0.06)
        c2_box = card_bg(3.7, 1.05, stroke_color=PALETTE["accent"])
        c2 = VGroup(c2_box, fit_in(c2_inner, 3.4, 0.95).move_to(c2_box.get_center()))
        c2.move_to([0, -2.15, 0])

        foot = lines("most errors are not made up --\nthey trace back to real pages", 11, PALETTE["good"], buff=0.04,
                     weight="BOLD")
        foot.move_to([0, -3.05, 0])

        for c in cards:
            self.play(FadeIn(c, shift=DOWN * 0.1), run_time=0.6)
        self.play(GrowArrow(arr), run_time=0.4)
        self.play(FadeIn(bot_row, shift=UP * 0.1), run_time=0.7)
        reveal(self, c1)
        reveal(self, c2)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)


class B08_FiveMinuteCheck(Scene):
    """Rows land on the narration: 'One' ~2.0s, 'Two' ~7.6s, 'Three' ~16.0s, 'Four' ~20.2s, 'Five' ~30.2s."""

    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        CARD_W, CARD_H = 3.9, 6.5
        card = card_bg(CARD_W, CARD_H).move_to([0, -0.05, 0])
        title = Text("The five-minute check", color=PALETTE["ink"], font_size=15, weight="BOLD")
        title.move_to([0, card.get_top()[1] - 0.32, 0])
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=2.5).next_to(title, DOWN, buff=0.08)

        X_NUM, X_TXT = -1.62, -1.3
        heights = [0.7, 1.5, 0.7, 1.3, 0.62]
        gap = 0.12
        y = rule.get_bottom()[1] - 0.2
        rows = []
        for i, h in enumerate(heights):
            top = y
            band = RoundedRectangle(corner_radius=0.07, width=CARD_W - 0.3, height=h, fill_color=PALETTE["bg"],
                                    fill_opacity=1, stroke_color=PALETTE["border"], stroke_width=1.0).move_to(
                [0, top - h / 2, 0])
            circ = Circle(radius=0.15, fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
            num = Text(str(i + 1), color=PALETTE["card"], font_size=12, weight="BOLD").move_to(circ.get_center())
            numg = VGroup(circ, num).move_to([X_NUM, top - 0.25 if len(heights) else 0, 0])
            rows.append({"band": band, "num": numg, "top": top, "h": h})
            y = top - h - gap

        def label(txt, i, fs=12):
            t = lines(txt, fs, PALETTE["ink"], buff=0.04, weight="BOLD")
            t.move_to([0, 0, 0])
            t.align_to([X_TXT, 0, 0], LEFT)
            t.set_y(rows[i]["top"] - 0.2 - t.height / 2 + 0.02)
            return t

        t1 = label("Ask two or three\ndifferent chatbots", 0)
        t2 = label("Ask like a customer would", 1)
        qs = ["what is it?", "what does it cost?", "where and when is it open?", "is it any good?",
              "what are the alternatives?"]
        qw = [0.052 * len(q) + 0.26 for q in qs]
        qchips = [chip(q, w=w, h=0.27, fs=8) for q, w in zip(qs, qw)]
        qrow1 = VGroup(qchips[0], qchips[1]).arrange(RIGHT, buff=0.08)
        qrow2 = VGroup(qchips[2], qchips[3]).arrange(RIGHT, buff=0.08)
        qrow3 = VGroup(qchips[4])
        qgrp = VGroup(qrow1, qrow2, qrow3).arrange(DOWN, buff=0.07, aligned_edge=LEFT)
        qgrp.move_to([X_TXT + qgrp.width / 2, rows[1]["top"] - 0.58 - qgrp.height / 2 + 0.12, 0])
        t3 = label("Note what is right, wrong,\nand missing", 2)
        t4 = label("Fix it at the source", 3)
        fx = ["old pricing pages", "hours", "addresses", "profiles and reviews match your website"]
        fw = [0.052 * len(f) + 0.26 for f in fx]
        fchips = [chip(f, w=w, h=0.27, fs=8, border=PALETTE["good"]) for f, w in zip(fx, fw)]
        frow1 = VGroup(fchips[0], fchips[1], fchips[2]).arrange(RIGHT, buff=0.08)
        frow2 = VGroup(fchips[3])
        fgrp = VGroup(frow1, frow2).arrange(DOWN, buff=0.07, aligned_edge=LEFT)
        fgrp.move_to([X_TXT + fgrp.width / 2, rows[3]["top"] - 0.58 - fgrp.height / 2 + 0.12, 0])
        t5 = label("Check again in a few weeks", 4)

        ticks = [tick(PALETTE["good"], 0.85).move_to([1.65, r["top"] - 0.25, 0]) for r in rows]

        self.play(FadeIn(card), run_time=0.4)
        self.play(FadeIn(title), FadeIn(rule), run_time=0.4)
        for r in rows:
            self.add(r["band"])
            self.add(r["num"])
            r["band"].set_opacity(0)
            r["num"].set_opacity(0)

        def show(i, texts, t_at):
            wait_until(self, t_at)
            self.play(rows[i]["band"].animate.set_fill(opacity=1).set_stroke(opacity=1),
                      rows[i]["num"].animate.set_opacity(1), *[FadeIn(t) for t in texts], run_time=0.5)

        def done(i):
            self.play(FadeIn(ticks[i]), run_time=0.3)

        # q chips in narration order: what is it, what does it cost, where/when, any good, alternatives
        q_order = [qchips[0], qchips[1], qchips[2], qchips[3], qchips[4]]
        f_order = fchips

        show(0, [t1], 2.0)
        wait_until(self, 7.0)
        done(0)
        show(1, [t2], 7.6)
        for k, qc in enumerate(q_order):
            wait_until(self, [9.8, 10.6, 11.6, 13.4, 14.4][k])
            self.play(FadeIn(qc, shift=UP * 0.08), run_time=0.35)
        wait_until(self, 15.6)
        done(1)
        show(2, [t3], 16.0)
        wait_until(self, 19.7)
        done(2)
        show(3, [t4], 20.2)
        for k, fc in enumerate(f_order):
            wait_until(self, [22.5, 23.7, 24.6, 25.9][k])
            self.play(FadeIn(fc, shift=UP * 0.08), run_time=0.35)
        wait_until(self, 29.5)
        done(3)
        show(4, [t5], 30.2)
        wait_until(self, 31.6)
        done(4)
        self.wait(0.5)


class B09_SmallTeamAccurate(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        panel = RoundedRectangle(corner_radius=0.14, width=3.9, height=5.0, fill_color=PALETTE["warm"],
                                 fill_opacity=1, stroke_color=PALETTE["border"], stroke_width=1.5)
        panel.move_to(UP * 0.5)
        plank = desk_plank(3.5).move_to([0, -1.55, 0])
        top_y = plank.get_top()[1]

        ml = Text("an accurate, current profile", color=PALETTE["good"], font_size=10).move_to([-0.55, 2.75, 0])
        note = chip("illustration", w=1.0, h=0.28, border=PALETTE["ink"], color=PALETTE["ink"], fs=8).move_to([1.4, 2.75, 0])

        mon = monitor(3.0, 1.9)
        mon.move_to([0, 1.35, 0])
        scr = mon[0]
        head = RoundedRectangle(corner_radius=0.05, width=2.5, height=0.32, fill_color=PALETTE["accent"], fill_opacity=0.18,
                                stroke_width=0).move_to(scr.get_top() + DOWN * 0.32)
        hbar = Line(LEFT * 0.8, RIGHT * 0.8, color=PALETTE["ink"], stroke_width=4).move_to(head.get_center())
        items = VGroup()
        for lab in ["hours", "address", "prices"]:
            tk = tick(PALETTE["good"], 0.7)
            tx = Text(lab, color=PALETTE["ink"], font_size=13)
            bar = Line(ORIGIN, RIGHT * 1.0, color=PALETTE["border"], stroke_width=3)
            items.add(VGroup(tk, tx, bar).arrange(RIGHT, buff=0.2))
        items.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        items.move_to(scr.get_center() + DOWN * 0.3)

        team = VGroup(person(0.85, PALETTE["ink"], smile=True), person(0.85, PALETTE["accent"], smile=True),
                      person(0.85, PALETTE["good"], smile=True)).arrange(RIGHT, buff=0.25, aligned_edge=DOWN)
        team.move_to([0, top_y + team.height / 2, 0])
        tl = Text("a small team", color=PALETTE["dim"], font_size=10).move_to([0, 0.0, 0])

        q1 = Text("Not about gaming a chatbot.", color=PALETTE["ink"], font_size=14, weight="BOLD")
        q2 = lines("About making accurate, current\ninformation easy to find.", 14, PALETTE["accent"], buff=0.05,
                   weight="BOLD")
        qs = VGroup(q1, q2).arrange(DOWN, buff=0.1)
        fit(qs, 3.6)
        qs.move_to([0, -2.75, 0])

        self.play(FadeIn(panel), FadeIn(plank), run_time=0.6)
        self.play(FadeIn(mon), FadeIn(ml), run_time=0.6)
        self.play(FadeIn(head), FadeIn(hbar), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(it, shift=RIGHT * 0.1) for it in items], lag_ratio=0.35), run_time=1.4)
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.1) for p in team], lag_ratio=0.25), FadeIn(tl), run_time=1.0)
        self.play(FadeIn(note), run_time=0.4)
        self.play(FadeIn(q1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


class B10_SourcesCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        sh = Text("Sources", color=PALETTE["ink"], font_size=14, weight="BOLD")
        rows = VGroup()
        for n, t in [("BrandMentions (2026)", "How to check what ChatGPT says about your brand"),
                     ("CloudNine PR (2026)", "ChatGPT helps consumers discover new brands (press release)"),
                     ("Sanbi (2026)", "Inaccurate AI claims about your brand: causes and fixes"),
                     ("Searchable (July 30, 2026)", "The AI brand misinformation report"),
                     ("SubscribePR (2026)", "ChatGPT says wrong things about your business"),
                     ("Yext (2026)", "Cracking the ChatGPT code: brand visibility in OpenAI")]:
            a = Text(n, color=PALETTE["accent"], font_size=10, weight="BOLD")
            b = fit(Text(t, color=PALETTE["ink"], font_size=8), 3.2)
            rows.add(VGroup(a, b).arrange(DOWN, buff=0.03, aligned_edge=LEFT))
        rows.arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        l_inner = VGroup(sh, rows).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        l_box = card_bg(3.7, 3.5)
        top = VGroup(l_box, fit_in(l_inner, 3.35, 3.25).move_to(l_box.get_center()))
        top.move_to(UP * 1.55)

        nh = Text("A note on sources", color=PALETTE["miss"], font_size=13, weight="BOLD")
        nb = lines("Most of these sources are companies that\nsell marketing, PR, or brand-monitoring\nservices. So the statistics are\nindustry-reported, not independent research.",
                   9, PALETTE["ink"], buff=0.05)
        badge = chip("INDUSTRY-REPORTED", w=2.6, h=0.36, border=PALETTE["miss"], color=PALETTE["miss"], fs=11)
        gr = lines("One study (Searchable) was graded by\nthe brands themselves.", 9, PALETTE["ink"], buff=0.04)
        ill = lines("The bakery scene is an illustration,\nnot a reported case.", 8, PALETTE["dim"], buff=0.04)
        n_inner = VGroup(nh, nb, badge, gr, ill).arrange(DOWN, buff=0.14)
        n_box = card_bg(3.7, 3.0, stroke_color=PALETTE["miss"])
        bottom = VGroup(n_box, fit_in(n_inner, 3.4, 2.75).move_to(n_box.get_center()))
        bottom.move_to(DOWN * 1.8)

        reveal(self, top)
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in rows], lag_ratio=0.2), run_time=1.6)
        reveal(self, bottom)
        self.play(FadeIn(nb, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(badge), run_time=0.4)
        self.play(FadeIn(gr), run_time=0.4)
        self.play(FadeIn(ill), run_time=0.4)
        self.wait(1.3)
