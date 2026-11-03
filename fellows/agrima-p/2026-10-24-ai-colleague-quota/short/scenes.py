"""
Portrait (9:16) Manim scenes for ai-colleague-quota-short

Ports of the eight graphic beats kept in the Shorts cut (B00B, B01, B03, B04,
B07, B08, B09, B10). Stacked layouts for a 4.5 x 8.0 frame; same palette and
copy as the 16:9 scenes. Dropped beats (B02, B05, B06) live only in the long
cut. All visuals are generated; no real company logos.
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


def doc_icon(w=0.55, h=0.7, color=None, nlines=3):
    page = RoundedRectangle(corner_radius=0.04, width=w, height=h, fill_color=PALETTE["card"], fill_opacity=1,
                            stroke_color=color or PALETTE["dim"], stroke_width=1.5)
    ln = VGroup(*[Line(LEFT * w * 0.3, RIGHT * w * (0.3 - 0.08 * (i % 2)), color=PALETTE["border"], stroke_width=2)
                  for i in range(nlines)]).arrange(DOWN, buff=h * 0.12).move_to(page.get_center())
    return VGroup(page, ln)


def envelope_icon(w=0.9, color=None, fill=None):
    c = color or PALETTE["dim"]
    b = RoundedRectangle(corner_radius=0.05, width=w, height=w * 0.62, fill_color=fill or PALETTE["card"],
                         fill_opacity=1, stroke_color=c, stroke_width=2)
    f = Polygon(b.get_corner(UL), b.get_corner(UR), b.get_center(), color=c, stroke_width=2, fill_opacity=0)
    return VGroup(b, f)


def tick(color=None, s=1.0, sw=3.5):
    t = VMobject(color=color or PALETTE["good"], stroke_width=sw)
    t.set_points_as_corners([[-0.1, 0.0, 0], [-0.02, -0.1, 0], [0.13, 0.12, 0]])
    return t.scale(s)


def cross(color=None, s=1.0, sw=3):
    c = color or PALETTE["miss"]
    return VGroup(Line([-0.09, -0.09, 0], [0.09, 0.09, 0], color=c, stroke_width=sw),
                  Line([-0.09, 0.09, 0], [0.09, -0.09, 0], color=c, stroke_width=sw)).scale(s)


def flag_icon(color=None):
    c = color or PALETTE["accent"]
    pole = Line(DOWN * 0.18, UP * 0.18, color=PALETTE["ink"], stroke_width=2)
    cloth = Polygon([0, 0.18, 0], [0.24, 0.1, 0], [0, 0.02, 0], fill_color=c, fill_opacity=1, stroke_width=0)
    return VGroup(pole, cloth)


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


def name_rows(n, w, hl=(), gap=0.1, messy=False, seed=0, row_h=0.0):
    rng = np.random.RandomState(seed)
    rows = VGroup()
    for i in range(n):
        dot = Circle(radius=0.05, color=PALETTE["accent"] if i in hl else PALETTE["border"],
                     fill_color=PALETTE["accent"] if i in hl else PALETTE["border"], fill_opacity=1, stroke_width=0)
        bw = (w - 0.3) * (0.55 + 0.4 * ((i * 37) % 10) / 10.0)
        bar = Line(ORIGIN, RIGHT * bw, color=PALETTE["accent"] if i in hl else PALETTE["dim"],
                   stroke_width=3.5 if i in hl else 2.5, stroke_opacity=1 if i in hl else 0.45)
        r = VGroup(dot, bar).arrange(RIGHT, buff=0.08)
        if messy:
            r.shift(RIGHT * float(rng.uniform(-0.15, 0.15)))
            r.rotate(float(rng.uniform(-0.06, 0.06)))
        rows.add(r)
    if messy:
        rows.arrange(DOWN, buff=gap)
    else:
        rows.arrange(DOWN, buff=gap, aligned_edge=LEFT)
    return rows


# --- scenes -----------------------------------------------------------------

class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = fit(Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=38), 3.4)
        summary = lines("Today: AI agents joining\nsales teams. They handle the\nresearch and the first hello,\nso people can spend more time\non the conversations\nthat matter.",
                        21, PALETTE["ink"], max_w=3.4, buff=0.2)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        VGroup(name, rule, summary).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.4)


class B01_MondayMorning(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        panel = RoundedRectangle(corner_radius=0.14, width=3.9, height=6.1, fill_color=PALETTE["warm"],
                                 fill_opacity=1, stroke_color=PALETTE["border"], stroke_width=1.5)
        panel.move_to(UP * 0.25)
        plank = desk_plank(3.5).move_to([0, -0.75, 0])
        top_y = plank.get_top()[1]

        lab1 = Text("a long list of names", color=PALETTE["dim"], font_size=11).move_to([0, 3.07, 0])
        mon = monitor(2.6, 1.7)
        mon.move_to([0, 1.95, 0])
        rows = name_rows(7, 2.3, hl=(2, 5), gap=0.08)
        rows.move_to(mon[0].get_center())

        docs = VGroup()
        for count in (3, 2, 1):
            docs.add(VGroup(*[doc_icon(0.42, 0.34, nlines=2) for _ in range(count)]).arrange(RIGHT, buff=0.03))
        docs.arrange(UP, buff=0.03)
        docs.move_to([-0.95, top_y + docs.height / 2, 0])
        lab2 = lines("a mountain\nof research", 10, PALETTE["dim"], buff=0.03).move_to([-0.95, -1.2, 0])

        envs = VGroup(*[envelope_icon(0.75) for _ in range(4)])
        for i, e in enumerate(envs):
            e.move_to([1.0 + 0.06 * ((-1) ** i), top_y + 0.25 + 0.2 * i, 0])
            e.rotate(0.05 * ((-1) ** i))
        lab3 = lines("first emails\nto write", 10, PALETTE["dim"], buff=0.03).move_to([1.0, -1.2, 0])

        hp = helper_icon(s=0.55).move_to([-1.0, -1.85, 0])
        ht = lines("shows up early,\nreads everything", 11, PALETTE["accent"], buff=0.04).next_to(hp, RIGHT, buff=0.3)
        tks = VGroup(*[tick(PALETTE["good"], 0.55).move_to(rows[i].get_left() + LEFT * 0.14) for i in range(7)])
        note = chip("an illustration, not a reported case", w=3.5, h=0.4, border=PALETTE["ink"], color=PALETTE["ink"],
                    fs=11)
        note.move_to([0, -2.45, 0])

        self.play(FadeIn(panel), FadeIn(plank), run_time=0.6)
        self.play(FadeIn(mon), FadeIn(lab1), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.1) for r in rows], lag_ratio=0.12), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(d, shift=DOWN * 0.2) for row in docs for d in row], lag_ratio=0.1),
                  FadeIn(lab2), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(e, shift=DOWN * 0.2) for e in envs], lag_ratio=0.2), FadeIn(lab3), run_time=1.0)
        self.wait(0.4)
        self.play(FadeIn(hp, shift=LEFT * 0.3), FadeIn(ht), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(t) for t in tks], lag_ratio=0.08), run_time=0.9)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(1.2)


class B03_TheSplit(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        ah = VGroup(helper_icon(s=0.55), Text("the AI agent", color=PALETTE["accent"], font_size=15, weight="BOLD")
                    ).arrange(RIGHT, buff=0.25)
        a_chips = VGroup(chip("early research", w=3.2, h=0.38), chip("finds prospects", w=3.2, h=0.38),
                         chip("writes the first message", w=3.2, h=0.38)).arrange(DOWN, buff=0.1)
        a_inner = VGroup(ah, a_chips).arrange(DOWN, buff=0.2)
        a_box = card_bg(3.7, 2.45, stroke_color=PALETTE["accent"])
        top = VGroup(a_box, a_inner.move_to(a_box.get_center()))
        top.move_to(UP * 2.05)

        mid = VGroup(envelope_icon(0.6, color=PALETTE["accent"]),
                     Text("a reply", color=PALETTE["accent"], font_size=12),
                     Arrow(UP * 0.18, DOWN * 0.18, color=PALETTE["accent"], stroke_width=3, buff=0,
                           max_tip_length_to_length_ratio=0.5)).arrange(RIGHT, buff=0.2)
        mid.move_to(UP * 0.4)

        ph = VGroup(person(0.6, PALETTE["ink"], smile=True), Text("the person", color=PALETTE["ink"], font_size=15,
                                                                 weight="BOLD")).arrange(RIGHT, buff=0.25)
        p_chips = VGroup(chip("builds relationships", w=3.2, h=0.38),
                         chip("handles complex conversations", w=3.2, h=0.38),
                         chip("knows when to slow down", w=3.2, h=0.38)).arrange(DOWN, buff=0.1)
        p_inner = VGroup(ph, p_chips).arrange(DOWN, buff=0.2)
        p_box = card_bg(3.7, 2.45, stroke_color=PALETTE["good"])
        bottom = VGroup(p_box, p_inner.move_to(p_box.get_center()))
        bottom.move_to(DOWN * 1.2)

        n1 = lines("research and first drafts don't\nneed a handshake", 11, PALETTE["dim"], buff=0.04)
        n2 = lines("the conversation after the reply\nis where human skills shine", 12, PALETTE["ink"], buff=0.04,
                   weight="BOLD")
        notes = VGroup(n1, n2).arrange(DOWN, buff=0.1).move_to(DOWN * 2.9)

        reveal(self, top)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in a_chips], lag_ratio=0.3), run_time=1.0)
        self.play(FadeIn(mid, shift=DOWN * 0.15), run_time=0.6)
        reveal(self, bottom)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in p_chips], lag_ratio=0.3), run_time=1.0)
        self.play(FadeIn(n1), run_time=0.4)
        self.play(FadeIn(n2), run_time=0.4)
        self.wait(1.2)


class B04_AlreadyNormal(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        badge = chip("COMPANY-REPORTED", w=3.0, h=0.42, border=PALETTE["miss"], color=PALETTE["miss"], fs=12)
        badge.move_to(UP * 3.1)

        def src():
            return chip("Salesforce, 2026", w=1.7, h=0.3, border=PALETTE["dim"], color=PALETTE["dim"], fs=9)

        def card(num, txt, bar):
            n = Text(num, color=PALETTE["accent"], font_size=40, weight="BOLD")
            t = lines(txt, 11, PALETTE["ink"], buff=0.04)
            right = VGroup(t, bar, src()).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            inner = VGroup(n, right).arrange(RIGHT, buff=0.3)
            box = card_bg(3.7, 1.75)
            return VGroup(box, fit(inner, 3.4).move_to(box.get_center()))

        c1 = card("87%", "of sales organizations\nuse some form of AI", meter(1.9, 0.87, PALETTE["accent"]))
        bars = VGroup(meter(1.9, 1 / 1.7, PALETTE["dim"]), meter(1.9, 1.0, PALETTE["accent"])).arrange(DOWN, buff=0.06)
        c2 = card("1.7x", "top sellers are more likely\nto use AI agents for outreach", bars)
        c3 = card("94%", "of sales leaders with agents\ncall them critical", meter(1.9, 0.94, PALETTE["accent"]))
        VGroup(c1, c2, c3).arrange(DOWN, buff=0.16).move_to(DOWN * 0.15)

        self.play(FadeIn(badge, shift=DOWN * 0.1), run_time=0.5)
        for c in (c1, c2, c3):
            reveal(self, c, t1=0.4, t2=0.5)
        self.wait(1.4)


class B07_TheCatch(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        mh = Text("messy data", color=PALETTE["miss"], font_size=12, weight="BOLD")
        messy = name_rows(6, 1.5, gap=0.14, messy=True, seed=3)
        crosses = VGroup(*[cross(PALETTE["miss"], 0.55).next_to(r, RIGHT, buff=0.08) for r in messy])
        m_col = VGroup(mh, VGroup(messy, crosses)).arrange(DOWN, buff=0.2)
        arr = Arrow(LEFT * 0.2, RIGHT * 0.2, color=PALETTE["accent"], stroke_width=3, buff=0,
                    max_tip_length_to_length_ratio=0.5)
        ch = Text("clean data", color=PALETTE["good"], font_size=12, weight="BOLD")
        clean = name_rows(6, 1.5, gap=0.14)
        ticks = VGroup(*[tick(PALETTE["good"], 0.55).next_to(r, RIGHT, buff=0.08) for r in clean])
        c_col = VGroup(ch, VGroup(clean, ticks)).arrange(DOWN, buff=0.2)
        lists = VGroup(m_col, arr, c_col).arrange(RIGHT, buff=0.2)
        mm = chip("thin data = a mail merge with better manners", w=3.4, h=0.4, border=PALETTE["dim"], fs=10)
        t_inner = VGroup(lists, mm).arrange(DOWN, buff=0.25)
        t_box = card_bg(3.7, 2.9)
        top = VGroup(t_box, fit(t_inner, 3.4).move_to(t_box.get_center()))
        top.move_to(UP * 1.85)

        n = Text("46%", color=PALETTE["accent"], font_size=52, weight="BOLD")
        t = lines("of sales professionals using\nagents said data quality issues\nwere hurting their results", 11,
                  PALETTE["ink"], buff=0.05)
        src = chip("Salesforce survey · company-reported", w=3.3, h=0.36, border=PALETTE["miss"], color=PALETTE["miss"],
                   fs=10)
        tidy = chip("the best-prepared teams tidy up first", w=3.3, h=0.38, border=PALETTE["good"], color=PALETTE["good"],
                    fs=11)
        b_inner = VGroup(n, t, src, tidy).arrange(DOWN, buff=0.16)
        b_box = card_bg(3.7, 3.1, stroke_color=PALETTE["accent"])
        bottom = VGroup(b_box, b_inner.move_to(b_box.get_center()))
        bottom.move_to(DOWN * 1.6)

        reveal(self, top)
        self.play(FadeIn(m_col, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(mm, shift=UP * 0.1), run_time=0.5)
        self.play(GrowArrow(arr), run_time=0.4)
        self.play(FadeIn(c_col, shift=UP * 0.1), run_time=0.8)
        reveal(self, bottom)
        self.play(FadeIn(t), run_time=0.5)
        self.play(FadeIn(src), run_time=0.4)
        self.play(FadeIn(tidy, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)


class B08_AIOperations(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        pr = person(0.95, PALETTE["accent"], smile=True)
        ai = helper_icon(s=0.9)
        guide = Arrow(LEFT * 0.45, RIGHT * 0.45, color=PALETTE["accent"], stroke_width=3, buff=0,
                      max_tip_length_to_length_ratio=0.3)
        gl = Text("guides", color=PALETTE["accent"], font_size=11)
        mid = VGroup(gl, guide).arrange(DOWN, buff=0.08)
        row = VGroup(pr, mid, ai).arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
        cap = Text("someone has to be a good manager", color=PALETTE["ink"], font_size=12)
        t_inner = VGroup(row, cap).arrange(DOWN, buff=0.3)
        t_box = card_bg(3.7, 2.6)
        top = VGroup(t_box, fit(t_inner, 3.4).move_to(t_box.get_center()))
        top.move_to(UP * 2.0)

        rh = Text("AI Operations", color=PALETTE["accent"], font_size=22, weight="BOLD")
        rs = Text("a new role on sales teams", color=PALETTE["dim"], font_size=11)
        cs = VGroup(chip("train and calibrate the agents", w=3.3, h=0.42), chip("keep the data clean", w=3.3, h=0.42),
                    chip("watch performance", w=3.3, h=0.42), chip("coordinate people and AI", w=3.3, h=0.42)
                    ).arrange(DOWN, buff=0.1)
        tag = chip("Outreach, 2026", w=1.8, h=0.32, border=PALETTE["dim"], color=PALETTE["dim"], fs=10)
        b_inner = VGroup(rh, rs, cs, tag).arrange(DOWN, buff=0.18)
        b_box = card_bg(3.7, 3.5, stroke_color=PALETTE["accent"])
        bottom = VGroup(b_box, b_inner.move_to(b_box.get_center()))
        bottom.move_to(DOWN * 1.4)

        reveal(self, top)
        self.play(FadeIn(pr, shift=UP * 0.1), run_time=0.5)
        self.play(GrowArrow(guide), FadeIn(gl), FadeIn(ai), run_time=0.8)
        self.play(FadeIn(cap), run_time=0.5)
        reveal(self, bottom)
        self.play(FadeIn(rs), run_time=0.3)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in cs], lag_ratio=0.3), run_time=1.3)
        self.play(FadeIn(tag), run_time=0.4)
        self.wait(1.2)


class B09_MondayWithATeammate(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        panel = RoundedRectangle(corner_radius=0.14, width=3.9, height=3.8, fill_color=PALETTE["warm"],
                                 fill_opacity=1, stroke_color=PALETTE["border"], stroke_width=1.5)
        panel.move_to(UP * 1.4)
        plank = desk_plank(3.5).move_to([0, 0.0, 0])
        top_y = plank.get_top()[1]

        mon = monitor(1.7, 1.3)
        mon.move_to([-0.95, top_y + 0.28 + 0.65, 0])
        rows = name_rows(6, 1.45, hl=(1, 4), gap=0.07)
        rows.move_to(mon[0].get_center())
        tks = VGroup(*[tick(PALETTE["good"], 0.4).move_to(rows[i].get_left() + LEFT * 0.1) for i in range(6)])
        flags = VGroup(*[flag_icon().scale(0.6).next_to(rows[i], RIGHT, buff=0.06) for i in (1, 4)])

        drafts = VGroup(*[envelope_icon(0.7, color=PALETTE["good"]) for _ in range(3)])
        for i, e in enumerate(drafts):
            e.move_to([0.4 + 0.05 * ((-1) ** i), top_y + 0.22 + 0.2 * i, 0])
        dt = VGroup(*[tick(PALETTE["good"], 0.4).next_to(e, RIGHT, buff=0.04) for e in drafts])

        rep = person(0.95, PALETTE["ink"], smile=True).move_to([1.4, top_y + 0.55, 0])
        ph = phone_icon(h=0.45).move_to([1.7, top_y + 0.3, 0])
        rings = ring_arcs(ph.get_center(), s=0.6)
        reply = envelope_icon(0.6, color=PALETTE["accent"]).move_to([1.2, 2.55, 0])
        rt = Text("interested!", color=PALETTE["accent"], font_size=10).next_to(reply, DOWN, buff=0.05)

        cap = Text("researched list · drafts waiting · warm leads flagged", color=PALETTE["good"], font_size=10)
        fit(cap, 3.6)
        cap.move_to([0, -0.85, 0])
        q1 = lines("The AI colleague\nhas a quota.", 20, PALETTE["ink"], buff=0.08, weight="BOLD").move_to([0, -1.85, 0])
        q2 = lines("The relationship still\nbelongs to the person.", 20, PALETTE["accent"], buff=0.08,
                   weight="BOLD").move_to([0, -3.0, 0])

        self.play(FadeIn(panel), FadeIn(plank), run_time=0.6)
        self.play(FadeIn(mon), run_time=0.5)
        self.play(FadeIn(rows), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(t) for t in tks], lag_ratio=0.08), run_time=0.8)
        self.play(FadeIn(flags), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(e, shift=DOWN * 0.2) for e in drafts], lag_ratio=0.25), FadeIn(dt), run_time=1.0)
        self.play(FadeIn(rep, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(reply, shift=DOWN * 0.2), FadeIn(rt), run_time=0.6)
        self.play(FadeIn(ph), FadeIn(rings), FadeIn(cap), run_time=0.6)
        self.play(FadeIn(q1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


class B10_SourcesCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        sh = Text("Sources", color=PALETTE["ink"], font_size=15, weight="BOLD")
        rows = VGroup()
        for n, t in [("Outreach (Jan 15, 2026)", "Sales 2026: Future trends, tech & strategy guide"),
                     ("Salesforce (2026)", "Newsroom report on AI agents and sales teams"),
                     ("Salesforce (2026)", "15 sales trends for 2026 (State of Sales, ANZ)"),
                     ("Amplemarket (2026)", "AI in sales 2026: what actually works")]:
            a = Text(n, color=PALETTE["accent"], font_size=10, weight="BOLD")
            b = Text(t, color=PALETTE["ink"], font_size=9.5)
            rows.add(VGroup(a, b).arrange(DOWN, buff=0.03, aligned_edge=LEFT))
        rows.arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        t_inner = VGroup(sh, rows).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        t_box = card_bg(3.7, 3.0)
        top = VGroup(t_box, fit(t_inner, 3.3).move_to(t_box.get_center()))
        top.move_to(UP * 1.8)

        nh = Text("A note on sources", color=PALETTE["miss"], font_size=14, weight="BOLD")
        nb = lines("These sources are sales software\ncompanies: Outreach, Salesforce,\nand Amplemarket. So the statistics\nare industry-reported, not\nindependent research.", 11,
                   PALETTE["ink"], buff=0.06)
        badge = chip("INDUSTRY-REPORTED", w=2.8, h=0.4, border=PALETTE["miss"], color=PALETTE["miss"], fs=12)
        ill = lines("The Monday morning scenes are\nillustrations, not reported cases.", 10, PALETTE["ink"], buff=0.04)
        b_inner = VGroup(nh, nb, badge, ill).arrange(DOWN, buff=0.18)
        b_box = card_bg(3.7, 3.1, stroke_color=PALETTE["miss"])
        bottom = VGroup(b_box, fit(b_inner, 3.4).move_to(b_box.get_center()))
        bottom.move_to(DOWN * 1.65)

        reveal(self, top)
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in rows], lag_ratio=0.25), run_time=1.4)
        reveal(self, bottom)
        self.play(FadeIn(nb, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(badge), run_time=0.4)
        self.play(FadeIn(ill), run_time=0.4)
        self.wait(1.3)
