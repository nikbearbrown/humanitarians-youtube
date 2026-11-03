"""
Manim scenes for ai-colleague-quota

A warm, fair explainer on AI agents joining sales teams, sourced from the
user-supplied article "The AI Colleague With a Quota." No dedicated footage
exists (per the user's materials note) -- every visual below is a generated
Manim graphic, with no real company logos (company names appear only as plain
text). Every statistic carries its source and is labeled company-reported; the
Monday-morning scenes are illustrations. Built in the house Claude palette.

B00B_AgrimaIntro          -- presenter card: "Hi, I'm Agrima." + lead-in
B01_MondayMorning         -- desk: list of names, research mountain, first-email stack; the teammate arrives
B02_NotAGadget            -- a grammar tool vs an AI agent seated among people
B03_TheSplit              -- the AI handles research + first draft; the person handles the conversation
B04_AlreadyNormal         -- 87% / 1.7x / 94% stat cards (Salesforce, company-reported)
B05_TwoSurveys            -- 54% / 34% (ANZ survey) and "different surveys, same direction"
B06_TheJobNobodyDreamsOf  -- prospecting tasks, a Siemens example, ~a third less research time
B07_TheCatch              -- messy list -> clean list; 46% data-quality stat
B08_AIOperations          -- a person guiding an AI teammate; four task chips
B09_MondayWithATeammate   -- the same Monday, calm; a rep picks up the phone
B10_SourcesCard           -- four sources + the industry-reported note
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


def meter(w, frac, color, h=0.2):
    track = RoundedRectangle(corner_radius=0.08, width=w, height=h, fill_color=PALETTE["border"],
                              fill_opacity=1, stroke_width=0)
    fill = RoundedRectangle(corner_radius=0.08, width=max(w * frac, 0.2), height=h, fill_color=color,
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


def tick(color=None, s=1.0, sw=4):
    t = VMobject(color=color or PALETTE["good"], stroke_width=sw)
    t.set_points_as_corners([[-0.1, 0.0, 0], [-0.02, -0.1, 0], [0.13, 0.12, 0]])
    return t.scale(s)


def cross(color=None, s=1.0, sw=3.5):
    c = color or PALETTE["miss"]
    return VGroup(Line([-0.09, -0.09, 0], [0.09, 0.09, 0], color=c, stroke_width=sw),
                  Line([-0.09, 0.09, 0], [0.09, -0.09, 0], color=c, stroke_width=sw)).scale(s)


def flag_icon(color=None):
    c = color or PALETTE["accent"]
    pole = Line(DOWN * 0.18, UP * 0.18, color=PALETTE["ink"], stroke_width=2)
    cloth = Polygon([0, 0.18, 0], [0.24, 0.1, 0], [0, 0.02, 0], fill_color=c, fill_opacity=1, stroke_width=0)
    return VGroup(pole, cloth)


def pen_icon():
    body = RoundedRectangle(corner_radius=0.03, width=1.1, height=0.16, fill_color=PALETTE["wood"], fill_opacity=1,
                            stroke_width=0)
    tip = Polygon([0.55, 0.08, 0], [0.55, -0.08, 0], [0.8, 0, 0], fill_color=PALETTE["ink"], fill_opacity=1,
                  stroke_width=0)
    g = VGroup(body, tip).rotate(PI / 4)
    return g


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


def name_rows(n, w, hl=(), start_y=0.0, gap=0.24, messy=False, seed=0):
    rng = np.random.RandomState(seed)
    rows = VGroup()
    for i in range(n):
        dot = Circle(radius=0.06, color=PALETTE["accent"] if i in hl else PALETTE["border"],
                     fill_color=PALETTE["accent"] if i in hl else PALETTE["border"], fill_opacity=1, stroke_width=0)
        bw = (w - 0.4) * (0.55 + 0.4 * ((i * 37) % 10) / 10.0)
        bar = Line(ORIGIN, RIGHT * bw, color=PALETTE["accent"] if i in hl else PALETTE["dim"],
                   stroke_width=4 if i in hl else 3, stroke_opacity=1 if i in hl else 0.45)
        r = VGroup(dot, bar).arrange(RIGHT, buff=0.1)
        if messy:
            r.shift(RIGHT * float(rng.uniform(-0.25, 0.25)))
            r.rotate(float(rng.uniform(-0.06, 0.06)))
        rows.add(r)
    rows.arrange(DOWN, buff=gap, aligned_edge=LEFT) if not messy else rows.arrange(DOWN, buff=gap)
    return rows


# --- scenes -----------------------------------------------------------------

class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=40)
        summary = fit(Text(
            "Today: AI agents joining sales teams.\nThey handle the research and the first hello,\n"
            "so people can spend more time on the\nconversations that matter.",
            color=PALETTE["ink"], font_size=24, line_spacing=1.3, should_center=True), 8.6)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.4)


class B01_MondayMorning(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        panel = RoundedRectangle(corner_radius=0.14, width=12.0, height=5.6, fill_color=PALETTE["warm"],
                                 fill_opacity=1, stroke_color=PALETTE["border"], stroke_width=1.5)
        panel.move_to(DOWN * 0.2)
        plank = desk_plank(11.4).move_to([0, -2.0, 0])
        top_y = plank.get_top()[1]

        mon = monitor(3.4, 2.6)
        mon.move_to([-3.9, top_y + 0.35 + 1.3 + 0.1, 0])
        rows = name_rows(9, 3.0, hl=(2, 6), gap=0.12)
        rows.move_to(mon[0].get_center())
        lab1 = Text("a long list of names", color=PALETTE["dim"], font_size=14).move_to([-3.9, 2.1, 0])

        # research mountain
        docs = VGroup()
        for layer, count in enumerate((4, 3, 2, 1)):
            row = VGroup(*[doc_icon(0.58, 0.46, nlines=2) for _ in range(count)]).arrange(RIGHT, buff=0.04)
            docs.add(row)
        docs.arrange(UP, buff=0.04, aligned_edge=ORIGIN)
        docs.move_to([0.4, top_y + docs.height / 2, 0])
        lab2 = Text("a mountain of research", color=PALETTE["dim"], font_size=14).move_to([0.4, 2.1, 0])

        # first emails
        envs = VGroup(*[envelope_icon(0.95) for _ in range(4)])
        for i, e in enumerate(envs):
            e.move_to([3.6 + 0.08 * ((-1) ** i), top_y + 0.35 + 0.28 * i, 0])
            e.rotate(0.05 * ((-1) ** i))
        lab3 = Text("first emails to write", color=PALETTE["dim"], font_size=14).move_to([3.6, 2.1, 0])

        note = chip("an illustration, not a reported case", w=4.6, h=0.45, border=PALETTE["ink"],
                    color=PALETTE["ink"], fs=13)
        note.move_to([0, -2.75, 0])

        # the new teammate
        hp = helper_icon(s=0.95).move_to([5.2, 0.6, 0])
        ht = lines("shows up early", 13, PALETTE["accent"], buff=0.04).next_to(hp, DOWN, buff=0.18)
        tks = VGroup(*[tick(PALETTE["good"], 0.8).move_to(rows[i].get_left() + LEFT * 0.2) for i in range(9)])

        self.play(FadeIn(panel), run_time=0.5)
        self.play(FadeIn(plank), run_time=0.4)
        self.play(FadeIn(mon), FadeIn(lab1), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.1) for r in rows], lag_ratio=0.12), run_time=1.4)
        self.play(LaggedStart(*[FadeIn(d, shift=DOWN * 0.2) for row in docs for d in row], lag_ratio=0.1),
                  FadeIn(lab2), run_time=1.4)
        self.play(LaggedStart(*[FadeIn(e, shift=DOWN * 0.2) for e in envs], lag_ratio=0.2), FadeIn(lab3), run_time=1.0)
        self.wait(0.5)
        self.play(FadeIn(hp, shift=LEFT * 0.4), FadeIn(ht), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(t) for t in tks], lag_ratio=0.08), run_time=1.0)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(1.2)


class B02_NotAGadget(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lh = Text("a few years ago", color=PALETTE["dim"], font_size=20)
        pen = pen_icon()
        ck = tick(PALETTE["good"], 1.3, 5)
        tool = VGroup(pen, ck).arrange(RIGHT, buff=0.35)
        lt = Text("a tool that fixed your grammar", color=PALETTE["ink"], font_size=17)
        l_inner = VGroup(lh, tool, lt).arrange(DOWN, buff=0.5)
        l_box = card_bg(5.2, 4.2)
        left = VGroup(l_box, fit(l_inner, 4.8).move_to(l_box.get_center()))
        left.move_to(LEFT * 3.5 + UP * 0.1)

        rh = Text("now", color=PALETTE["accent"], font_size=22, weight="BOLD")
        team = VGroup(person(0.9, PALETTE["ink"], smile=True), helper_icon(s=0.9),
                      person(0.9, PALETTE["accent"], smile=True), person(0.9, PALETTE["good"], smile=True)
                      ).arrange(RIGHT, buff=0.35, aligned_edge=DOWN)
        rt = lines("AI agents that work\nlike team members", 18, PALETTE["ink"], buff=0.08)
        tag = chip("in Outreach's description", w=3.4, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=14)
        r_inner = VGroup(rh, team, rt, tag).arrange(DOWN, buff=0.4)
        r_box = card_bg(5.8, 4.6, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, fit(r_inner, 5.3).move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.3 + UP * 0.1)

        arr = Arrow(LEFT * 0.35, RIGHT * 0.35, color=PALETTE["dim"], stroke_width=4, buff=0,
                    max_tip_length_to_length_ratio=0.5).move_to([0.05, 0.1, 0])
        foot = Text("not a gadget anymore -- part of the team", color=PALETTE["dim"], font_size=19)
        foot.move_to(DOWN * 3.0)

        reveal(self, left)
        self.play(FadeIn(tool, shift=UP * 0.1), FadeIn(lt), run_time=0.6)
        self.play(GrowArrow(arr), run_time=0.5)
        reveal(self, right)
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.1) for m in team], lag_ratio=0.25), run_time=1.2)
        self.play(FadeIn(rt), FadeIn(tag), run_time=0.6)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B03_TheSplit(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        ah = VGroup(helper_icon(s=0.9), Text("the AI agent", color=PALETTE["accent"], font_size=22, weight="BOLD")
                    ).arrange(DOWN, buff=0.25)
        a_chips = VGroup(chip("early research", w=3.6, h=0.55, fs=16), chip("finds prospects", w=3.6, h=0.55, fs=16),
                         chip("writes the first message", w=3.6, h=0.55, fs=16)).arrange(DOWN, buff=0.18)
        a_inner = VGroup(ah, a_chips).arrange(DOWN, buff=0.35)
        a_box = card_bg(4.4, 4.6, stroke_color=PALETTE["accent"])
        left = VGroup(a_box, fit(a_inner, 4.0).move_to(a_box.get_center()))
        left.move_to(LEFT * 4.0 + UP * 0.35)

        ph = VGroup(person(0.95, PALETTE["ink"], smile=True), Text("the person", color=PALETTE["ink"], font_size=22,
                                                                  weight="BOLD")).arrange(DOWN, buff=0.25)
        p_chips = VGroup(chip("builds relationships", w=3.8, h=0.55, fs=16),
                         chip("handles complex conversations", w=3.8, h=0.55, fs=15),
                         chip("knows when to slow down", w=3.8, h=0.55, fs=16)).arrange(DOWN, buff=0.18)
        p_inner = VGroup(ph, p_chips).arrange(DOWN, buff=0.35)
        p_box = card_bg(4.6, 4.6, stroke_color=PALETTE["good"])
        right = VGroup(p_box, fit(p_inner, 4.2).move_to(p_box.get_center()))
        right.move_to(RIGHT * 3.9 + UP * 0.35)

        env = envelope_icon(0.8, color=PALETTE["accent"])
        rl = Text("a reply", color=PALETTE["accent"], font_size=16)
        mid = VGroup(env, rl, Arrow(LEFT * 0.4, RIGHT * 0.4, color=PALETTE["accent"], stroke_width=4, buff=0,
                                    max_tip_length_to_length_ratio=0.45)).arrange(DOWN, buff=0.2)
        mid.move_to([0, 0.35, 0])

        n1 = Text("research and first drafts don't need a handshake", color=PALETTE["dim"], font_size=18)
        n2 = Text("the conversation after the reply is where human skills shine", color=PALETTE["ink"], font_size=19,
                  weight="BOLD")
        notes = VGroup(n1, n2).arrange(DOWN, buff=0.15).move_to(DOWN * 3.0)

        reveal(self, left)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in a_chips], lag_ratio=0.3), run_time=1.2)
        self.play(FadeIn(mid, shift=RIGHT * 0.2), run_time=0.7)
        reveal(self, right)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in p_chips], lag_ratio=0.3), run_time=1.2)
        self.play(FadeIn(n1), run_time=0.5)
        self.play(FadeIn(n2), run_time=0.5)
        self.wait(1.2)


class B04_AlreadyNormal(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        badge = chip("COMPANY-REPORTED", w=3.4, h=0.5, border=PALETTE["miss"], color=PALETTE["miss"], fs=16)
        badge.move_to(UP * 3.05)

        def src():
            return chip("Salesforce, 2026", w=2.6, h=0.42, border=PALETTE["dim"], color=PALETTE["dim"], fs=13)

        # 87%
        n1 = Text("87%", color=PALETTE["accent"], font_size=62, weight="BOLD")
        l1 = lines("of sales organizations\nuse some form of AI", 17, PALETTE["ink"], buff=0.08)
        m1 = meter(3.0, 0.87, PALETTE["accent"])
        i1 = VGroup(n1, l1, m1, src()).arrange(DOWN, buff=0.28)
        b1 = card_bg(3.8, 4.6)
        c1 = VGroup(b1, fit(i1, 3.4).move_to(b1.get_center()))

        # 1.7x
        n2 = Text("1.7x", color=PALETTE["accent"], font_size=62, weight="BOLD")
        l2 = lines("top sellers are more likely to\nuse AI agents for outreach", 16, PALETTE["ink"], buff=0.08)
        bar_a = meter(3.0, 1.0 / 1.7, PALETTE["dim"], h=0.2)
        bar_b = meter(3.0, 1.0, PALETTE["accent"], h=0.2)
        ta = Text("other teams", color=PALETTE["dim"], font_size=12)
        tb = Text("top performers", color=PALETTE["accent"], font_size=12)
        bars = VGroup(VGroup(ta, bar_a).arrange(DOWN, buff=0.06, aligned_edge=LEFT),
                      VGroup(tb, bar_b).arrange(DOWN, buff=0.06, aligned_edge=LEFT)).arrange(DOWN, buff=0.14)
        i2 = VGroup(n2, l2, bars, src()).arrange(DOWN, buff=0.28)
        b2 = card_bg(3.8, 4.6)
        c2 = VGroup(b2, fit(i2, 3.4).move_to(b2.get_center()))

        # 94%
        n3 = Text("94%", color=PALETTE["accent"], font_size=62, weight="BOLD")
        l3 = lines("of sales leaders who have\nagents call them critical", 17, PALETTE["ink"], buff=0.08)
        m3 = meter(3.0, 0.94, PALETTE["accent"])
        i3 = VGroup(n3, l3, m3, src()).arrange(DOWN, buff=0.28)
        b3 = card_bg(3.8, 4.6)
        c3 = VGroup(b3, fit(i3, 3.4).move_to(b3.get_center()))

        cards = VGroup(c1, c2, c3).arrange(RIGHT, buff=0.35).move_to(DOWN * 0.35)

        self.play(FadeIn(badge, shift=DOWN * 0.1), run_time=0.5)
        for c in (c1, c2, c3):
            reveal(self, c, t1=0.4, t2=0.5)
        self.wait(1.4)


class B05_TwoSurveys(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        sh = Text("Salesforce survey · Australia and New Zealand", color=PALETTE["dim"], font_size=16)
        n54 = Text("54%", color=PALETTE["accent"], font_size=56, weight="BOLD")
        t54 = Text("already use AI agents", color=PALETTE["ink"], font_size=18)
        n34 = Text("34%", color=PALETTE["good"], font_size=56, weight="BOLD")
        t34 = Text("expect to within two years", color=PALETTE["ink"], font_size=18)
        a = VGroup(n54, t54).arrange(DOWN, buff=0.1)
        b = VGroup(n34, t34).arrange(DOWN, buff=0.1)
        top = VGroup(a, b).arrange(RIGHT, buff=1.0)
        bw = 5.6
        track = RoundedRectangle(corner_radius=0.1, width=bw, height=0.32, fill_color=PALETTE["border"],
                                  fill_opacity=1, stroke_width=0)
        s1 = RoundedRectangle(corner_radius=0.1, width=bw * 0.54, height=0.32, fill_color=PALETTE["accent"],
                              fill_opacity=1, stroke_width=0).align_to(track, LEFT)
        s2 = Rectangle(width=bw * 0.34, height=0.32, fill_color=PALETTE["good"], fill_opacity=0.75,
                       stroke_width=0).next_to(s1, RIGHT, buff=0)
        bar = VGroup(track, s1, s2)
        src = chip("Salesforce, 2026 · company-reported", w=5.0, h=0.5, border=PALETTE["miss"], color=PALETTE["miss"],
                   fs=14)
        l_inner = VGroup(sh, top, bar, src).arrange(DOWN, buff=0.4)
        l_box = card_bg(7.0, 4.6)
        left = VGroup(l_box, fit(l_inner, 6.5).move_to(l_box.get_center()))
        left.move_to(LEFT * 2.8 + UP * 0.1)

        rh = lines("different surveys\ncount different things", 17, PALETTE["ink"], buff=0.08)
        arr1 = Arrow(LEFT * 1.3, RIGHT * 1.3, color=PALETTE["dim"], stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.2)
        arr2 = Arrow(LEFT * 1.3, RIGHT * 1.3, color=PALETTE["accent"], stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.2)
        la = Text("one survey", color=PALETTE["dim"], font_size=13)
        lb = Text("another survey", color=PALETTE["accent"], font_size=13)
        arrows = VGroup(VGroup(la, arr1).arrange(DOWN, buff=0.08), VGroup(lb, arr2).arrange(DOWN, buff=0.08)
                        ).arrange(DOWN, buff=0.3)
        same = Text("the same direction", color=PALETTE["accent"], font_size=18, weight="BOLD")
        r_inner = VGroup(rh, arrows, same).arrange(DOWN, buff=0.4)
        r_box = card_bg(4.4, 4.6, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, fit(r_inner, 3.9).move_to(r_box.get_center()))
        right.move_to(RIGHT * 4.0 + UP * 0.1)

        foot = Text("the numbers don't line up exactly, but they point the same way", color=PALETTE["dim"],
                    font_size=17).move_to(DOWN * 3.0)

        reveal(self, left)
        self.play(FadeIn(top, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(bar), run_time=0.6)
        self.play(FadeIn(src, shift=UP * 0.1), run_time=0.5)
        reveal(self, right)
        self.play(FadeIn(arrows, shift=RIGHT * 0.2), run_time=0.8)
        self.play(FadeIn(same), run_time=0.4)
        self.play(FadeIn(foot), run_time=0.5)
        self.wait(1.2)


class B06_TheJobNobodyDreamsOf(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lh = lines("prospecting: often the least\nenjoyable part of sales", 19, PALETTE["ink"], buff=0.08, weight="BOLD")
        tasks = VGroup()
        for t in ["research companies and decision makers", "draft personalized emails",
                  "set up meetings", "log activity automatically"]:
            tk = tick(PALETTE["good"], 1.0)
            tx = Text(t, color=PALETTE["ink"], font_size=17)
            tasks.add(VGroup(tk, tx).arrange(RIGHT, buff=0.25))
        tasks.arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        agent = VGroup(helper_icon(s=0.6), Text("agents can do it", color=PALETTE["accent"], font_size=15)
                       ).arrange(RIGHT, buff=0.2)
        src = chip("Salesforce, 2026", w=2.6, h=0.42, border=PALETTE["dim"], color=PALETTE["dim"], fs=13)
        l_inner = VGroup(lh, agent, tasks, src).arrange(DOWN, buff=0.35)
        l_box = card_bg(6.0, 5.2)
        left = VGroup(l_box, fit(l_inner, 5.5).move_to(l_box.get_center()))
        left.move_to(LEFT * 3.2)

        sh = Text("Siemens", color=PALETTE["ink"], font_size=24, weight="BOLD")
        sd = lines("uses AI agents to personalize\nfollow-up on every lead", 16, PALETTE["ink"], buff=0.08)
        sn = Text("a human team would love to; rarely has the hours", color=PALETTE["dim"], font_size=12)
        bw = 4.0
        before = meter(bw, 1.0, PALETTE["dim"], h=0.26)
        after = meter(bw, 0.67, PALETTE["accent"], h=0.26)
        bl = Text("research time today", color=PALETTE["dim"], font_size=12)
        al = Text("expected: about a third less", color=PALETTE["accent"], font_size=12)
        bars = VGroup(VGroup(bl, before).arrange(DOWN, buff=0.06, aligned_edge=LEFT),
                      VGroup(al, after).arrange(DOWN, buff=0.06, aligned_edge=LEFT)).arrange(DOWN, buff=0.2)
        back = chip("back into talking to customers", w=4.2, h=0.5, border=PALETTE["good"], color=PALETTE["good"], fs=14)
        r_inner = VGroup(sh, sd, sn, bars, back).arrange(DOWN, buff=0.3)
        r_box = card_bg(5.2, 5.2, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, fit(r_inner, 4.7).move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.5)

        reveal(self, left)
        self.play(LaggedStart(*[FadeIn(t, shift=RIGHT * 0.15) for t in tasks], lag_ratio=0.35), FadeIn(agent),
                  run_time=1.8)
        self.play(FadeIn(src), run_time=0.4)
        reveal(self, right)
        self.play(FadeIn(sd), FadeIn(sn), run_time=0.6)
        self.play(FadeIn(bars), run_time=0.8)
        self.play(FadeIn(back, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)


class B07_TheCatch(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        mh = Text("messy data", color=PALETTE["miss"], font_size=18, weight="BOLD")
        messy = name_rows(7, 2.4, gap=0.2, messy=True, seed=3)
        crosses = VGroup(*[cross(PALETTE["miss"], 0.8).next_to(r, RIGHT, buff=0.15) for r in messy])
        m_col = VGroup(mh, VGroup(messy, crosses)).arrange(DOWN, buff=0.3)
        arr = Arrow(LEFT * 0.4, RIGHT * 0.4, color=PALETTE["accent"], stroke_width=4, buff=0,
                    max_tip_length_to_length_ratio=0.5)
        ch = Text("clean data", color=PALETTE["good"], font_size=18, weight="BOLD")
        clean = name_rows(7, 2.4, gap=0.2)
        ticks = VGroup(*[tick(PALETTE["good"], 0.8).next_to(r, RIGHT, buff=0.15) for r in clean])
        c_col = VGroup(ch, VGroup(clean, ticks)).arrange(DOWN, buff=0.3)
        lists = VGroup(m_col, arr, c_col).arrange(RIGHT, buff=0.5)
        mm = chip("thin data = a mail merge with better manners", w=5.6, h=0.55, border=PALETTE["dim"], fs=14)
        l_inner = VGroup(lists, mm).arrange(DOWN, buff=0.4)
        l_box = card_bg(6.0, 5.2)
        left = VGroup(l_box, fit(l_inner, 5.6).move_to(l_box.get_center()))
        left.move_to(LEFT * 3.2)

        n = Text("46%", color=PALETTE["accent"], font_size=76, weight="BOLD")
        t = lines("of sales professionals using\nagents said data quality issues\nwere hurting their results", 17,
                  PALETTE["ink"], buff=0.08)
        src = chip("Salesforce survey · company-reported", w=4.3, h=0.5, border=PALETTE["miss"], color=PALETTE["miss"],
                   fs=13)
        tidy = chip("the best-prepared teams tidy up first", w=4.3, h=0.55, border=PALETTE["good"], color=PALETTE["good"],
                    fs=15)
        r_inner = VGroup(n, t, src, tidy).arrange(DOWN, buff=0.3)
        r_box = card_bg(4.6, 5.2, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, fit(r_inner, 4.2).move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.8)

        reveal(self, left)
        self.play(FadeIn(m_col, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(mm, shift=UP * 0.1), run_time=0.5)
        self.play(GrowArrow(arr), run_time=0.5)
        self.play(FadeIn(c_col, shift=UP * 0.1), run_time=0.8)
        reveal(self, right)
        self.play(FadeIn(t), run_time=0.5)
        self.play(FadeIn(src), run_time=0.4)
        self.play(FadeIn(tidy, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)


class B08_AIOperations(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        pr = person(1.5, PALETTE["accent"], smile=True)
        ai = helper_icon(s=1.4)
        guide = Arrow(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=4, buff=0,
                      max_tip_length_to_length_ratio=0.3)
        gl = Text("guides", color=PALETTE["accent"], font_size=16)
        mid = VGroup(gl, guide).arrange(DOWN, buff=0.12)
        scene_row = VGroup(pr, mid, ai).arrange(RIGHT, buff=0.45, aligned_edge=DOWN)
        cap = Text("someone has to be a good manager", color=PALETTE["ink"], font_size=18)
        l_inner = VGroup(scene_row, cap).arrange(DOWN, buff=0.5)
        l_box = card_bg(5.6, 4.4)
        left = VGroup(l_box, fit(l_inner, 5.2).move_to(l_box.get_center()))
        left.move_to(LEFT * 3.4 + UP * 0.1)

        rh = Text("AI Operations", color=PALETTE["accent"], font_size=30, weight="BOLD")
        rs = Text("a new role on sales teams", color=PALETTE["dim"], font_size=16)
        cs = VGroup(chip("train and calibrate the agents", w=2.8, h=0.7, fs=14),
                    chip("keep the data clean", w=2.8, h=0.7, fs=14),
                    chip("watch performance", w=2.8, h=0.7, fs=14),
                    chip("coordinate people and AI", w=2.8, h=0.7, fs=14)).arrange_in_grid(rows=2, cols=2, buff=0.2)
        tag = chip("Outreach, 2026", w=2.6, h=0.42, border=PALETTE["dim"], color=PALETTE["dim"], fs=13)
        r_inner = VGroup(rh, rs, cs, tag).arrange(DOWN, buff=0.3)
        r_box = card_bg(5.8, 4.4, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, fit(r_inner, 5.4).move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.3 + UP * 0.1)

        foot = Text("new technology tends to create new roles for the people who guide it", color=PALETTE["dim"],
                    font_size=17).move_to(DOWN * 2.9)

        reveal(self, left)
        self.play(FadeIn(pr, shift=UP * 0.1), run_time=0.5)
        self.play(GrowArrow(guide), FadeIn(gl), FadeIn(ai), run_time=0.8)
        self.play(FadeIn(cap), run_time=0.5)
        reveal(self, right)
        self.play(FadeIn(rs), run_time=0.3)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in cs], lag_ratio=0.3), run_time=1.4)
        self.play(FadeIn(tag), run_time=0.4)
        self.play(FadeIn(foot), run_time=0.5)
        self.wait(1.2)


class B09_MondayWithATeammate(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        panel = RoundedRectangle(corner_radius=0.14, width=12.0, height=5.0, fill_color=PALETTE["warm"],
                                 fill_opacity=1, stroke_color=PALETTE["border"], stroke_width=1.5)
        panel.move_to(UP * 0.55)
        plank = desk_plank(11.4).move_to([0, -1.55, 0])
        top_y = plank.get_top()[1]

        mon = monitor(3.2, 2.3)
        mon.move_to([-4.0, top_y + 0.35 + 1.15 + 0.1, 0])
        rows = name_rows(8, 2.8, hl=(1, 4), gap=0.12)
        rows.move_to(mon[0].get_center())
        tks = VGroup(*[tick(PALETTE["good"], 0.7).move_to(rows[i].get_left() + LEFT * 0.18) for i in range(8)])
        flags = VGroup(*[flag_icon().next_to(rows[i], RIGHT, buff=0.12) for i in (1, 4)])
        lab1 = lines("the list is researched", 13, PALETTE["good"], buff=0.04).move_to([-4.0, 2.55, 0])

        drafts = VGroup(*[envelope_icon(0.95, color=PALETTE["good"]) for _ in range(3)])
        for i, e in enumerate(drafts):
            e.move_to([-0.4 + 0.07 * ((-1) ** i), top_y + 0.35 + 0.3 * i, 0])
        dt = VGroup(*[tick(PALETTE["good"], 0.7).next_to(e, RIGHT, buff=0.08) for e in drafts])
        lab2 = lines("the drafts are waiting", 13, PALETTE["good"], buff=0.04).move_to([-0.4, 2.55, 0])

        rep = person(1.35, PALETTE["ink"], smile=True).move_to([3.0, top_y + 0.75, 0])
        ph = phone_icon(h=0.7).move_to([4.4, top_y + 0.5, 0])
        rings = ring_arcs(ph.get_center(), s=0.9)
        reply = envelope_icon(0.8, color=PALETTE["accent"]).move_to([4.7, 1.9, 0])
        rt = Text("interested!", color=PALETTE["accent"], font_size=14).next_to(reply, DOWN, buff=0.08)
        lab3 = lines("a warm reply", 13, PALETTE["accent"], buff=0.04).move_to([3.4, 2.55, 0])
        hp = helper_icon(s=0.6).move_to([5.3, -0.2, 0])

        q1 = Text("The AI colleague has a quota.", color=PALETTE["ink"], font_size=26, weight="BOLD")
        q2 = Text("The relationship still belongs to the person.", color=PALETTE["accent"], font_size=26,
                  weight="BOLD")
        qs = VGroup(q1, q2).arrange(DOWN, buff=0.15)
        fit(qs, 11.2)
        qs.move_to(DOWN * 2.85)

        self.play(FadeIn(panel), FadeIn(plank), run_time=0.6)
        self.play(FadeIn(mon), run_time=0.5)
        self.play(FadeIn(rows), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(t) for t in tks], lag_ratio=0.08), FadeIn(lab1), run_time=1.0)
        self.play(FadeIn(flags), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(e, shift=DOWN * 0.2) for e in drafts], lag_ratio=0.25), FadeIn(dt),
                  FadeIn(lab2), run_time=1.0)
        self.play(FadeIn(rep, shift=UP * 0.1), FadeIn(hp), run_time=0.7)
        self.play(FadeIn(reply, shift=DOWN * 0.2), FadeIn(rt), FadeIn(lab3), run_time=0.6)
        self.play(FadeIn(ph), FadeIn(rings), run_time=0.5)
        self.play(FadeIn(q1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


class B10_SourcesCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        sh = Text("Sources", color=PALETTE["ink"], font_size=24, weight="BOLD")
        rows = VGroup()
        for n, t in [("Outreach (Jan 15, 2026)", "Sales 2026: Future trends, tech & strategy guide"),
                     ("Salesforce (2026)", "Newsroom report on AI agents and sales teams"),
                     ("Salesforce (2026)", "15 sales trends for 2026 (State of Sales, Australia and New Zealand)"),
                     ("Amplemarket (2026)", "AI in sales 2026: what actually works")]:
            a = Text(n, color=PALETTE["accent"], font_size=15, weight="BOLD")
            b = fit(Text(t, color=PALETTE["ink"], font_size=14), 5.6)
            rows.add(VGroup(a, b).arrange(DOWN, buff=0.04, aligned_edge=LEFT))
        rows.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        l_inner = VGroup(sh, rows).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        l_box = card_bg(6.2, 5.0)
        left = VGroup(l_box, fit(l_inner, 5.7).move_to(l_box.get_center()))
        left.move_to(LEFT * 3.1)

        nh = Text("A note on sources", color=PALETTE["miss"], font_size=22, weight="BOLD")
        nb = lines("These sources are sales software\ncompanies: Outreach, Salesforce, and\nAmplemarket. So the statistics are\nindustry-reported, not independent research.",
                   17, PALETTE["ink"], buff=0.1)
        badge = chip("INDUSTRY-REPORTED", w=3.6, h=0.55, border=PALETTE["miss"], color=PALETTE["miss"], fs=17)
        ill = lines("The Monday morning scenes are\nillustrations, not reported cases.", 15, PALETTE["ink"], buff=0.08)
        r_inner = VGroup(nh, nb, badge, ill).arrange(DOWN, buff=0.4)
        r_box = card_bg(5.2, 5.0, stroke_color=PALETTE["miss"])
        right = VGroup(r_box, fit(r_inner, 4.7).move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.5)

        reveal(self, left)
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in rows], lag_ratio=0.25), run_time=1.5)
        reveal(self, right)
        self.play(FadeIn(nb, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(badge), run_time=0.4)
        self.play(FadeIn(ill), run_time=0.4)
        self.wait(1.3)
