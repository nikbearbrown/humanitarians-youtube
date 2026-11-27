"""
Manim scenes for we-ask-the-ai-now

A warm, fair explainer on how people now split their questions between search and AI
chat, sourced from the user-supplied article "We Ask the AI Now." No footage exists
(per the user's materials note) -- every visual below is a generated Manim graphic with
NO real brand or company logos: the search and chat icons are generic, and source or
product names (Bain & Company, Orbit Media, Future, Google) appear only as plain text.
Every statistic carries its source (Bain, Orbit Media or Future) and the surveys are
never merged into one number; the opening scene and the borrowable observation are
labeled. Built in the house Claude palette. Reveals are timed to the narration (pause
points measured from each beat's mp3).

B00B_AgrimaIntro   -- presenter card: "Hi, I'm Agrima." + lead-in
B01_PlanningATrip  -- illustration: ten tabs years ago vs one AI answer today
B02_SearchSplit    -- split-screen; Bain 56% vs 16%; Orbit 22% -> 29% and 35% -> 28%
B03_HandOver       -- Bain's four uses (bars); Future 55% US / 62% UK (2025); Orbit 24% local
B04_AnswerOnTop    -- a results page with a summary on top; 76%; 70 / 23 / 7; Bain 46%
B05_Generations    -- bars: boomers 76, Gen X 55, millennials 42, Gen Z 42 (Bain)
B06_TrustMeter     -- three gauges: 49%, 36%, 44% (Orbit)
B07_BeingFound     -- the author's observation + what won't change (Orbit's author)
B08_ChooseTheTool  -- a person choosing a tool depending on the question
B09_SourcesCard    -- references + the source-type, date and illustration notes
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
    "blue":   "#5B7FA6",
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


def left_lines(txt, fs, color, buff=0.08):
    return VGroup(*[Text(t, color=color, font_size=fs) for t in txt.split(chr(10))]).arrange(DOWN, buff=buff, aligned_edge=LEFT)


def lines(txt, fs, color, max_w=None, buff=0.1, weight=None):
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


def chip(label, w=2.6, h=0.55, border=None, color=None, fs=16):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(lines(label, fs, color or PALETTE["ink"], buff=0.06), w - 0.3)
    return VGroup(box, txt.move_to(box.get_center()))


def src_chip(label, w=3.4, border=None, color=None):
    return chip(label, w=w, h=0.4, border=border or PALETTE["dim"], color=color or PALETTE["dim"], fs=13)


def meter(w, frac, color, h=0.22):
    track = RoundedRectangle(corner_radius=0.09, width=w, height=h, fill_color=PALETTE["border"],
                             fill_opacity=1, stroke_width=0)
    fill = RoundedRectangle(corner_radius=0.09, width=max(w * frac, 0.2), height=h, fill_color=color,
                            fill_opacity=1, stroke_width=0).align_to(track, LEFT)
    return VGroup(track, fill)


def person(h=1.0, color=None):
    c = color or PALETTE["ink"]
    head = Circle(radius=0.26 * h, color=c, fill_color=c, fill_opacity=1, stroke_width=0)
    body = RoundedRectangle(corner_radius=0.18 * h, width=0.7 * h, height=0.8 * h,
                            fill_color=c, fill_opacity=1, stroke_width=0)
    return VGroup(head, body).arrange(DOWN, buff=0.05)


def search_bar(w=3.4, text=None, fs=16):
    """A GENERIC search bar (no brand): magnifier + field."""
    box = card_bg(w, 0.62, stroke_color=PALETTE["ink"])
    lens = Circle(radius=0.12, color=PALETTE["ink"], stroke_width=3)
    handle = Line([0.09, -0.09, 0], [0.22, -0.22, 0], color=PALETTE["ink"], stroke_width=3.5)
    mag = VGroup(lens, handle).move_to(box.get_left() + RIGHT * 0.38)
    parts = [box, mag]
    if text:
        t = Text(text, color=PALETTE["dim"], font_size=fs)
        fit(t, w - 1.0)
        t.move_to([box.get_left()[0] + 0.75 + t.width / 2, box.get_center()[1], 0])
        parts.append(t)
    return VGroup(*parts)


def chat_bubble(label, w=3.0, h=0.7, fs=15, color=None, fill=None, align=LEFT):
    """A GENERIC chat bubble (no brand)."""
    c = color or PALETTE["accent"]
    box = card_bg(w, h, stroke_color=c, fill=fill)
    t = fit(lines(label, fs, PALETTE["card"] if fill == c else PALETTE["ink"], buff=0.05), w - 0.3)
    return VGroup(box, t.move_to(box.get_center()))


def chat_icon(s=1.0, color=None):
    c = color or PALETTE["accent"]
    box = RoundedRectangle(corner_radius=0.14, width=0.95, height=0.7, fill_color=PALETTE["card"], fill_opacity=1,
                           stroke_color=c, stroke_width=3)
    dots = VGroup(*[Dot(radius=0.05, color=c) for _ in range(3)]).arrange(RIGHT, buff=0.12).move_to(box.get_center())
    tail = Polygon([-0.1, 0, 0], [0.1, 0, 0], [0, -0.16, 0], color=c, fill_color=PALETTE["card"], fill_opacity=1,
                   stroke_width=3).next_to(box, DOWN, buff=-0.02).shift(LEFT * 0.2)
    return VGroup(tail, box, dots).scale(s)


def search_icon(s=1.0, color=None):
    c = color or PALETTE["blue"]
    lens = Circle(radius=0.3, color=c, stroke_width=5)
    handle = Line([0.22, -0.22, 0], [0.5, -0.5, 0], color=c, stroke_width=6)
    return VGroup(lens, handle).scale(s)


def tab_rect(w=0.5, h=0.34, color=None):
    return RoundedRectangle(corner_radius=0.05, width=w, height=h, fill_color=PALETTE["card"], fill_opacity=1,
                            stroke_color=color or PALETTE["dim"], stroke_width=2)


def stat_card(big, label, w=2.6, h=1.5, col=None, bfs=44, lfs=15):
    c = col or PALETTE["accent"]
    b = card_bg(w, h, stroke_color=c)
    t = VGroup(Text(big, color=c, font_size=bfs, weight="BOLD"), lines(label, lfs, PALETTE["ink"], buff=0.05)
               ).arrange(DOWN, buff=0.12)
    return VGroup(b, fit_in(t, w - 0.3, h - 0.25).move_to(b.get_center()))


# --- scenes -----------------------------------------------------------------

class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=40)
        summary = fit(Text(
            "Today: how we now split our questions\nbetween search and AI.",
            color=PALETTE["ink"], font_size=26, line_spacing=1.3, should_center=True), 8.6)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        wait_until(self, 5.35)


class B01_PlanningATrip(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        note = chip("illustration -- not a real case", w=4.4, h=0.45, border=PALETTE["ink"], color=PALETTE["ink"], fs=14)
        note.move_to([0, 3.05, 0])

        # a person planning a trip: phone + a simple map
        mapc = card_bg(1.8, 1.3, stroke_color=PALETTE["wood"], fill=PALETTE["warm"]).move_to([0, 1.0, 0])
        route = VMobject(color=PALETTE["accent"], stroke_width=4).set_points_smoothly(
            [mapc.get_center() + np.array(p) for p in ((-0.6, -0.3, 0), (-0.2, 0.2, 0), (0.2, -0.1, 0), (0.55, 0.3, 0))])
        pn = Circle(radius=0.1, fill_color=PALETTE["accent"], fill_opacity=1, stroke_color=PALETTE["ink"],
                    stroke_width=2).move_to(mapc.get_center() + np.array([0.55, 0.3, 0]))
        trip = Text("weekend trip", color=PALETTE["dim"], font_size=14).next_to(mapc, UP, buff=0.1)
        who = person(1.2, PALETTE["ink"]).move_to([0, -0.7, 0])
        ph = RoundedRectangle(corner_radius=0.06, width=0.38, height=0.62, fill_color=PALETTE["card"], fill_opacity=1,
                              stroke_color=PALETTE["accent"], stroke_width=3).move_to([0.55, -0.55, 0])

        # a few years ago: search, ten tabs
        l_head = chip("a few years ago", w=3.2, h=0.5, border=PALETTE["blue"], color=PALETTE["blue"], fs=18)
        l_head.move_to([-4.0, 2.2, 0])
        l_bar = search_bar(4.4, "best things to do in Lisbon", 15).move_to([-4.0, 1.2, 0])
        tabs = VGroup(*[tab_rect(0.8, 0.5) for _ in range(10)]).arrange_in_grid(rows=2, cols=5, buff=0.1)
        tabs.move_to([-4.0, -0.1, 0])
        l_cap = Text("ten tabs", color=PALETTE["dim"], font_size=20).move_to([-4.0, -1.2, 0])

        # today: AI chat, one answer
        r_head = chip("today", w=3.2, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=18)
        r_head.move_to([4.0, 2.2, 0])
        q1 = chat_bubble("best things to do in Lisbon", w=4.2, h=0.55, fs=15, fill=PALETTE["accent"]).move_to([4.0, 1.4, 0])
        q2 = chat_bubble("I have two kids and a small budget", w=4.2, h=0.55, fs=15, fill=PALETTE["accent"]).move_to(
            [4.0, 0.7, 0])
        ans = VGroup(card_bg(4.2, 1.4, stroke_color=PALETTE["good"]),
                     VGroup(*[Line(LEFT * (1.6 - 0.25 * (i % 3)), RIGHT * (1.6 - 0.25 * (i % 3)), color=PALETTE["dim"],
                                   stroke_width=3, stroke_opacity=0.6) for i in range(4)]).arrange(DOWN, buff=0.2))
        ans[1].move_to(ans[0].get_center())
        ans.move_to([4.0, -0.7, 0])
        r_cap = Text("one answer, in seconds", color=PALETTE["good"], font_size=20, weight="BOLD").move_to([4.0, -1.7, 0])

        real = chip("it matches something real", w=4.6, h=0.6, border=PALETTE["accent"], color=PALETTE["accent"], fs=20)
        real.move_to([0, -2.8, 0])

        self.play(FadeIn(note), run_time=0.5)
        self.play(FadeIn(mapc), Create(route), FadeIn(pn), FadeIn(trip), run_time=0.7)
        self.play(FadeIn(who), FadeIn(ph), run_time=0.5)
        wait_until(self, 1.8)
        self.play(FadeIn(l_head, shift=DOWN * 0.1), FadeIn(l_bar), run_time=0.6)
        wait_until(self, 4.7)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in tabs], lag_ratio=0.12), FadeIn(l_cap), run_time=1.2)
        wait_until(self, 6.6)
        self.play(FadeIn(r_head, shift=DOWN * 0.1), FadeIn(q1, shift=LEFT * 0.1), run_time=0.6)
        wait_until(self, 10.0)
        self.play(FadeIn(q2, shift=LEFT * 0.1), run_time=0.5)
        wait_until(self, 12.7)
        self.play(FadeIn(ans, shift=UP * 0.1), FadeIn(r_cap), run_time=0.6)
        wait_until(self, 17.5)
        self.play(FadeIn(real, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 18.92)


class B02_SearchSplit(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # split-screen header: a generic search bar | a generic chat bubble
        sb = search_bar(3.6, "search", 15).move_to([-3.3, 3.0, 0])
        cb = chat_bubble("ask the AI", w=3.6, h=0.62, fs=16, color=PALETTE["accent"]).move_to([3.3, 3.0, 0])
        mid = Text("two tools", color=PALETTE["dim"], font_size=20).move_to([0, 3.0, 0])
        divider = DashedLine([0, -3.35, 0], [0, 2.6, 0], color=PALETTE["border"], stroke_width=3)

        # left: Bain
        bh = chip("Bain & Company  ·  1,500 US consumers", w=5.6, h=0.5, border=PALETTE["blue"], color=PALETTE["blue"], fs=15)
        bh.move_to([-3.2, 2.15, 0])
        bsub = Text("mostly or always use ... as their default tool", color=PALETTE["dim"], font_size=15)
        fit(bsub, 5.4).move_to([-3.2, 1.55, 0])
        s1 = VGroup(Text("56%", color=PALETTE["blue"], font_size=52, weight="BOLD"),
                    Text("search engines", color=PALETTE["ink"], font_size=18)).arrange(DOWN, buff=0.1)
        m1 = meter(4.8, 0.56, PALETTE["blue"], h=0.28)
        c1 = VGroup(s1, m1).arrange(DOWN, buff=0.25)
        card1 = VGroup(card_bg(5.6, 2.1, stroke_color=PALETTE["blue"]), c1)
        c1.move_to(card1[0].get_center())
        card1.move_to([-3.2, 0.1, 0])
        s2 = VGroup(Text("16%", color=PALETTE["accent"], font_size=52, weight="BOLD"),
                    Text("AI chatbots", color=PALETTE["ink"], font_size=18)).arrange(DOWN, buff=0.1)
        m2 = meter(4.8, 0.16, PALETTE["accent"], h=0.28)
        c2 = VGroup(s2, m2).arrange(DOWN, buff=0.25)
        card2 = VGroup(card_bg(5.6, 2.1, stroke_color=PALETTE["accent"]), c2)
        c2.move_to(card2[0].get_center())
        card2.move_to([-3.2, -2.2, 0])

        # right: Orbit Media
        oh = chip("Orbit Media  ·  March 2026  ·  1,110 US adults", w=5.6, h=0.5, border=PALETTE["good"],
                  color=PALETTE["good"], fs=15).move_to([3.2, 2.15, 0])
        stay = chip("Google use hasn't declined", w=5.6, h=0.5, border=PALETTE["dim"], color=PALETTE["ink"],
                    fs=16).move_to([3.2, 1.5, 0])

        def shift_card(label, a, b, col, y):
            arrow = Arrow([-0.5, 0, 0], [0.5, 0, 0], buff=0, color=col, stroke_width=5, max_tip_length_to_length_ratio=0.5)
            row = VGroup(Text("%d%%" % a, color=PALETTE["dim"], font_size=40, weight="BOLD"), arrow,
                         Text("%d%%" % b, color=col, font_size=46, weight="BOLD")).arrange(RIGHT, buff=0.3)
            lab = lines(label, 15, PALETTE["ink"], buff=0.05)
            inner = VGroup(row, lab).arrange(DOWN, buff=0.15)
            box = card_bg(5.6, 1.7, stroke_color=col)
            return VGroup(box, inner.move_to(box.get_center())).move_to([3.2, y, 0])
        o1 = shift_card("usually use search for research\n(2025 to 2026)", 22, 29, PALETTE["good"], 0.2)
        o2 = shift_card("usually use AI chat\n(2025 to 2026)", 35, 28, PALETTE["accent"], -1.85)
        both = Text("two tools, picked by the question", color=PALETTE["ink"], font_size=19, weight="BOLD")
        both.move_to([3.2, -3.1, 0])

        self.play(FadeIn(mid), run_time=0.4)
        wait_until(self, 1.3)
        self.play(FadeIn(sb, shift=RIGHT * 0.1), FadeIn(cb, shift=LEFT * 0.1), Create(divider), run_time=0.7)
        wait_until(self, 2.8)
        self.play(FadeIn(bh, shift=DOWN * 0.1), FadeIn(bsub), run_time=0.5)
        wait_until(self, 7.0)
        reveal(self, card1, t1=0.4, t2=0.4)
        wait_until(self, 12.8)
        reveal(self, card2, t1=0.4, t2=0.4)
        wait_until(self, 16.1)
        self.play(FadeIn(oh, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 20.1)
        self.play(FadeIn(stay, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 22.1)
        reveal(self, o1, t1=0.4, t2=0.4)
        wait_until(self, 27.3)
        reveal(self, o2, t1=0.4, t2=0.4)
        wait_until(self, 33.0)
        self.play(FadeIn(both), run_time=0.4)
        wait_until(self, 33.9)


class B03_HandOver(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # left: Bain's four uses
        bh = chip("Bain & Company  ·  what chatbot users use it for", w=6.0, h=0.5, border=PALETTE["blue"],
                  color=PALETTE["blue"], fs=15).move_to([-3.4, 3.0, 0])
        items = [("makes complicated topics easier to understand", 53), ("gives step-by-step instructions", 47),
                 ("helps with brainstorming", 45), ("answers quick factual questions", 45)]
        rows = []
        for i, (lab, v) in enumerate(items):
            t = fit(Text(lab, color=PALETTE["ink"], font_size=17), 5.6)
            m = meter(4.6, v / 60.0, PALETTE["blue"], h=0.26)
            n = Text("%d%%" % v, color=PALETTE["blue"], font_size=26, weight="BOLD")
            bar = VGroup(m, n).arrange(RIGHT, buff=0.2)
            rows.append(VGroup(t, bar).arrange(DOWN, buff=0.1, aligned_edge=LEFT))
        stack = VGroup(*rows).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        left_box = card_bg(6.0, 4.6, stroke_color=PALETTE["blue"])
        stack.move_to(left_box.get_center())
        left_box.move_to([-3.4, 0.35, 0])
        stack.move_to(left_box.get_center())

        # right top: Future survey (2025)
        fh = chip("Future (a publisher)  ·  survey from 2025", w=5.6, h=0.5, border=PALETTE["good"],
                  color=PALETTE["good"], fs=15).move_to([3.4, 3.0, 0])
        us = VGroup(Text("55%", color=PALETTE["good"], font_size=46, weight="BOLD"),
                    Text("US", color=PALETTE["ink"], font_size=18)).arrange(DOWN, buff=0.05)
        uk = VGroup(Text("62%", color=PALETTE["good"], font_size=46, weight="BOLD"),
                    Text("UK", color=PALETTE["ink"], font_size=18)).arrange(DOWN, buff=0.05)
        both = VGroup(us, uk).arrange(RIGHT, buff=0.9)
        use = Text("use AI instead of search for some tasks", color=PALETTE["ink"], font_size=16)
        fit(use, 5.0)
        tasks = VGroup(*[chip(t, w=1.75, h=0.4, border=PALETTE["border"], fs=11) for t in
                         ("planning vacations", "fitness plans", "gift ideas", "fixing tech problems",
                          "comparing products", "drafting emails")]).arrange_in_grid(rows=2, cols=3, buff=0.1)
        f_in = VGroup(both, use, tasks).arrange(DOWN, buff=0.18)
        f_box = card_bg(5.6, 3.4, stroke_color=PALETTE["good"])
        fcard = VGroup(f_box, fit_in(f_in, 5.2, 3.0).move_to(f_box.get_center())).move_to([3.4, 1.0, 0])

        # right bottom: Orbit, local searches
        local = VGroup(Text("24%", color=PALETTE["accent"], font_size=40, weight="BOLD"),
                       lines("of Orbit's respondents preferred AI chat\nfor local searches (finding a nearby business)",
                             14, PALETTE["ink"], buff=0.05)).arrange(RIGHT, buff=0.3)
        l_box = card_bg(5.6, 1.35, stroke_color=PALETTE["accent"])
        lcard = VGroup(l_box, fit_in(local, 5.2, 1.1).move_to(l_box.get_center())).move_to([3.4, -1.45, 0])
        orb = src_chip("Orbit Media (March 2026)", 3.0).move_to([3.4, -2.35, 0])
        exc = Text("the exception: local searches still favor search", color=PALETTE["ink"], font_size=17, weight="BOLD")
        fit(exc, 5.6).move_to([3.4, -2.9, 0])
        bsrc = src_chip("Bain & Company (survey in September 2025)", 4.6).move_to([-3.4, -2.3, 0])

        self.play(FadeIn(bh, shift=DOWN * 0.1), FadeIn(left_box), run_time=0.5)
        wait_until(self, 3.9)
        self.play(FadeIn(rows[0], shift=RIGHT * 0.1), run_time=0.5)
        wait_until(self, 8.6)
        self.play(FadeIn(rows[1], shift=RIGHT * 0.1), run_time=0.5)
        wait_until(self, 11.7)
        self.play(FadeIn(rows[2], shift=RIGHT * 0.1), run_time=0.5)
        wait_until(self, 13.2)
        self.play(FadeIn(rows[3], shift=RIGHT * 0.1), FadeIn(bsrc), run_time=0.5)
        wait_until(self, 15.9)
        self.play(FadeIn(fh, shift=DOWN * 0.1), FadeIn(f_box), run_time=0.5)
        wait_until(self, 19.1)
        self.play(FadeIn(us, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 22.1)
        self.play(FadeIn(uk, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 24.4)
        self.play(FadeIn(use), FadeIn(tasks), run_time=0.6)
        wait_until(self, 27.7)
        self.play(FadeIn(exc, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 30.2)
        self.play(FadeIn(l_box), FadeIn(local), FadeIn(orb), run_time=0.6)
        wait_until(self, 34.65)


class B04_AnswerOnTop(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # a generic results page with a summary box on top
        page = card_bg(5.2, 5.2, stroke_color=PALETTE["ink"]).move_to([-3.4, 0.2, 0])
        bar = search_bar(4.6, "a question", 14).move_to([-3.4, 2.25, 0])
        summ = VGroup(card_bg(4.6, 1.5, stroke_color=PALETTE["accent"], fill=PALETTE["warm"]),
                      VGroup(*[Line(LEFT * (1.9 - 0.3 * (i % 2)), RIGHT * (1.9 - 0.3 * (i % 2)), color=PALETTE["dim"],
                                    stroke_width=3, stroke_opacity=0.6) for i in range(4)]).arrange(DOWN, buff=0.17))
        summ[1].move_to(summ[0].get_center())
        summ.move_to([-3.4, 0.95, 0])
        s_lab = Text("AI summary", color=PALETTE["accent"], font_size=15, weight="BOLD").move_to(
            summ[0].get_top() + DOWN * 0.18 + LEFT * 1.6)
        links = VGroup(*[VGroup(Line(LEFT * 2.1, RIGHT * 2.1, color=PALETTE["blue"], stroke_width=3.5),
                                Line(LEFT * 2.1, RIGHT * (2.1 - 0.5 * i), color=PALETTE["border"], stroke_width=3)
                                ).arrange(DOWN, buff=0.1) for i in range(3)]).arrange(DOWN, buff=0.28)
        links.move_to([-3.4, -1.35, 0])
        top_l = Text("the answer is at the top", color=PALETTE["ink"], font_size=17, weight="BOLD").move_to([-3.4, -2.7, 0])

        # right: the numbers
        c76 = VGroup(card_bg(5.4, 1.35, stroke_color=PALETTE["good"]),
                     VGroup(Text("76%", color=PALETTE["good"], font_size=46, weight="BOLD"),
                            lines("of search results pages show\nGoogle's AI Overviews", 15, PALETTE["ink"],
                                  buff=0.05)).arrange(RIGHT, buff=0.35))
        c76[1].move_to(c76[0].get_center())
        c76.move_to([3.3, 2.5, 0])
        tag76 = src_chip("Orbit Media, citing a study it names", 4.0).move_to([3.3, 1.55, 0])

        seg = VGroup(Rectangle(width=0.7 * 5.0, height=0.34, fill_color=PALETTE["good"], fill_opacity=1, stroke_width=0),
                     Rectangle(width=0.23 * 5.0, height=0.34, fill_color=PALETTE["wood"], fill_opacity=1, stroke_width=0),
                     Rectangle(width=0.07 * 5.0, height=0.34, fill_color=PALETTE["miss"], fill_opacity=1, stroke_width=0)
                     ).arrange(RIGHT, buff=0)
        l70 = chip("70%: use AI summaries at least occasionally", w=5.4, h=0.42, border=PALETTE["good"],
                   color=PALETTE["good"], fs=14)
        l23 = chip("about 23%: ignore them", w=5.4, h=0.42, border=PALETTE["wood"], color=PALETTE["ink"], fs=14)
        l7 = chip("7%: have turned them off", w=5.4, h=0.42, border=PALETTE["miss"], color=PALETTE["miss"], fs=14)
        split = VGroup(seg, VGroup(l70, l23, l7).arrange(DOWN, buff=0.08)).arrange(DOWN, buff=0.18)
        sbox = card_bg(5.4, 2.4, stroke_color=PALETTE["good"])
        scard = VGroup(sbox, fit_in(split, 5.0, 2.2).move_to(sbox.get_center())).move_to([3.3, 0.1, 0])
        osrc = src_chip("Orbit Media survey", 2.6).move_to([3.3, -1.3, 0])

        c46 = VGroup(card_bg(5.4, 1.0, stroke_color=PALETTE["blue"]),
                     VGroup(Text("46%", color=PALETTE["blue"], font_size=38, weight="BOLD"),
                            lines("of Bain's respondents use AI overviews\nfrom search engines", 14, PALETTE["ink"],
                                  buff=0.05)).arrange(RIGHT, buff=0.3))
        c46[1].move_to(c46[0].get_center())
        c46.move_to([3.3, -2.05, 0])
        b_src = src_chip("Bain & Company", 2.4).move_to([3.3, -2.8, 0])

        c_sum = chip("search engines now summarize", w=3.6, h=0.5, border=PALETTE["blue"], color=PALETTE["blue"], fs=15)
        c_sea = chip("AI tools now search", w=2.8, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=15)
        blur = VGroup(c_sum, c_sea).arrange(RIGHT, buff=0.2).move_to([0, -3.2, 0])
        blur.set_opacity(1)
        c_sum.move_to([-4.1, -3.2, 0])
        c_sea.move_to([-0.7, -3.2, 0])
        top_l.move_to([-3.4, -0.3, 0])
        top_l.set_opacity(1)

        self.play(FadeIn(page), FadeIn(bar), FadeIn(links), run_time=0.7)
        wait_until(self, 2.5)
        self.play(FadeIn(summ, shift=DOWN * 0.1), FadeIn(s_lab), FadeIn(top_l), run_time=0.6)
        wait_until(self, 4.5)
        reveal(self, c76, t1=0.4, t2=0.4)
        wait_until(self, 8.3)
        self.play(FadeIn(tag76), run_time=0.3)
        wait_until(self, 11.2)
        self.play(FadeIn(sbox), FadeIn(seg[0]), FadeIn(l70), FadeIn(osrc), run_time=0.5)
        wait_until(self, 14.4)
        self.play(FadeIn(seg[1]), FadeIn(l23), run_time=0.4)
        wait_until(self, 16.5)
        self.play(FadeIn(seg[2]), FadeIn(l7), run_time=0.4)
        wait_until(self, 18.6)
        reveal(self, c46, t1=0.4, t2=0.4)
        self.play(FadeIn(b_src), run_time=0.3)
        wait_until(self, 23.0)
        self.play(FadeIn(c_sum, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 25.1)
        self.play(FadeIn(c_sea, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 26.85)


class B05_Generations(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("mostly or always use search engines", color=PALETTE["ink"], font_size=26, weight="BOLD")
        title.move_to([-1.8, 3.0, 0])
        sub = src_chip("Bain & Company survey", 2.9).move_to([4.75, 3.0, 0])

        base_y = -2.0
        maxh = 3.2

        def bar(label, v, col, x):
            h = maxh * v / 80.0
            b = Rectangle(width=1.5, height=h, fill_color=col, fill_opacity=1, stroke_width=0)
            b.move_to([x, base_y + h / 2, 0])
            pct = Text("%d%%" % v, color=col, font_size=34, weight="BOLD").next_to(b, UP, buff=0.12)
            lab = Text(label, color=PALETTE["ink"], font_size=20).next_to(b, DOWN, buff=0.15)
            return VGroup(b, pct, lab)
        b1 = bar("baby boomers", 76, PALETTE["blue"], -4.2)
        b2 = bar("Gen X", 55, PALETTE["blue"], -1.4)
        b3 = bar("millennials", 42, PALETTE["accent"], 1.4)
        b4 = bar("Gen Z", 42, PALETTE["accent"], 4.2)
        axis = Line([-6.0, base_y, 0], [6.0, base_y, 0], color=PALETTE["ink"], stroke_width=3)
        arrow = Arrow([-4.4, 2.2, 0], [4.4, 2.2, 0], buff=0, color=PALETTE["dim"], stroke_width=4,
                      max_tip_length_to_length_ratio=0.1)
        arrow.set_opacity(1)
        arr_l = Text("older", color=PALETTE["dim"], font_size=16).next_to(arrow, UP, buff=0.05).align_to(arrow, LEFT)
        arr_r = Text("younger", color=PALETTE["dim"], font_size=16).next_to(arrow, UP, buff=0.05).align_to(arrow, RIGHT)
        shift = chip("if habits follow age, the mix will keep shifting", w=7.2, h=0.55, border=PALETTE["accent"],
                     color=PALETTE["accent"], fs=18).move_to([0, -3.15, 0])
        b1[2].shift(DOWN * 0.0)

        self.play(FadeIn(title, shift=DOWN * 0.1), FadeIn(sub), run_time=0.5)
        self.play(Create(axis), run_time=0.4)
        wait_until(self, 3.2)
        self.play(FadeIn(b1, shift=UP * 0.2), run_time=0.6)
        wait_until(self, 5.5)
        self.play(FadeIn(b2, shift=UP * 0.2), run_time=0.6)
        wait_until(self, 10.5)
        self.play(FadeIn(b3, shift=UP * 0.2), FadeIn(b4, shift=UP * 0.2), run_time=0.7)
        wait_until(self, 14.6)
        self.play(Create(arrow), FadeIn(arr_l), FadeIn(arr_r), run_time=0.6)
        wait_until(self, 16.0)
        self.play(FadeIn(shift, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 17.27)


class B06_TrustMeter(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("a trust meter", color=PALETTE["ink"], font_size=30, weight="BOLD").move_to([-4.6, 3.05, 0])
        src = src_chip("Orbit Media survey", 2.8).move_to([0.3, 3.05, 0])

        def gauge(pct, label, col, x):
            back = Arc(radius=1.5, start_angle=0, angle=PI, color=PALETTE["border"], stroke_width=22)
            front = Arc(radius=1.5, start_angle=PI, angle=-PI * pct / 100.0, color=col, stroke_width=22)
            big = Text("%d%%" % pct, color=col, font_size=46, weight="BOLD").move_to(back.get_center() + DOWN * 0.15)
            ends = VGroup(Text("0", color=PALETTE["dim"], font_size=14).move_to(back.get_end() + DOWN * 0.3),
                          Text("100", color=PALETTE["dim"], font_size=14).move_to(back.get_start() + DOWN * 0.3))
            lab = lines(label, 18, PALETTE["ink"], buff=0.06).next_to(back, DOWN, buff=0.55)
            g = VGroup(back, front, big, ends, lab)
            box = card_bg(3.9, 4.0, stroke_color=col)
            g.move_to(box.get_center() + DOWN * 0.1)
            return VGroup(box, g).move_to([x, -0.35, 0])
        g1 = gauge(49, "agreed they trust Google's\nresults more than AI chat", PALETTE["blue"], -4.2)
        g2 = gauge(36, "are unlikely to ever trust\nAI chat tools", PALETTE["miss"], 0.0)
        g3 = gauge(44, "say AI has changed how they\nlook for information online", PALETTE["accent"], 4.2)
        adopt = chip("adopting the tools", w=3.4, h=0.55, border=PALETTE["accent"], color=PALETTE["accent"], fs=18)
        doubt = chip("with a healthy amount of doubt", w=4.6, h=0.55, border=PALETTE["good"], color=PALETTE["good"], fs=18)
        foot = VGroup(adopt, doubt).arrange(RIGHT, buff=0.3).move_to([0, -3.1, 0])

        self.play(FadeIn(title), FadeIn(src), run_time=0.5)
        wait_until(self, 3.2)
        reveal(self, g1, t1=0.4, t2=0.5)
        wait_until(self, 7.7)
        reveal(self, g2, t1=0.4, t2=0.5)
        wait_until(self, 12.4)
        reveal(self, g3, t1=0.4, t2=0.5)
        wait_until(self, 17.3)
        self.play(FadeIn(adopt, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 19.0)
        self.play(FadeIn(doubt, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 20.41)


class B07_BeingFound(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("What this means for being found", color=PALETTE["ink"], font_size=26, weight="BOLD")
        title.move_to([-3.0, 3.05, 0])
        obs = chip("my own observation", w=3.2, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=17)
        obs.move_to([4.4, 3.05, 0])

        # left: answer first, websites second
        a1 = VGroup(card_bg(4.6, 0.9, stroke_color=PALETTE["accent"], fill=PALETTE["warm"]),
                    Text("the answer comes first", color=PALETTE["accent"], font_size=20, weight="BOLD"))
        a1[1].move_to(a1[0].get_center())
        a1.move_to([-3.4, 1.8, 0])
        a2 = VGroup(card_bg(4.6, 0.9), Text("the websites come second", color=PALETTE["dim"], font_size=20))
        a2[1].move_to(a2[0].get_center())
        a2.move_to([-3.4, 0.7, 0])
        clear = chip("being clear and easy to find matters more", w=4.6, h=0.6, border=PALETTE["good"],
                     color=PALETTE["good"], fs=16).move_to([-3.4, -0.3, 0])

        def icon_hotel():
            b = Rectangle(width=0.7, height=0.9, fill_color=PALETTE["card"], fill_opacity=1, stroke_color=PALETTE["ink"],
                          stroke_width=2.5)
            w_ = VGroup(*[Square(0.14, fill_color=PALETTE["warm"], fill_opacity=1, stroke_color=PALETTE["wood"],
                                 stroke_width=1.5) for _ in range(6)]).arrange_in_grid(rows=3, cols=2, buff=0.1)
            w_.move_to(b.get_center())
            return VGroup(b, w_)

        def icon_gallery():
            fr = Rectangle(width=0.9, height=0.7, fill_color=PALETTE["wood"], fill_opacity=1, stroke_color=PALETTE["ink"],
                           stroke_width=2.5)
            c = Rectangle(width=0.7, height=0.5, fill_color="#EFE3CC", fill_opacity=1, stroke_width=0).move_to(
                fr.get_center())
            s_ = Circle(radius=0.1, fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0).move_to(
                c.get_center() + UP * 0.08 + LEFT * 0.12)
            return VGroup(fr, c, s_)

        def icon_shelter():
            body = Rectangle(width=0.8, height=0.55, fill_color=PALETTE["card"], fill_opacity=1,
                             stroke_color=PALETTE["ink"], stroke_width=2.5)
            roof = Polygon([-0.5, 0, 0], [0.5, 0, 0], [0, 0.4, 0], fill_color=PALETTE["accent"], fill_opacity=1,
                           stroke_color=PALETTE["ink"], stroke_width=2.5).next_to(body, UP, buff=0)
            door = Rectangle(width=0.2, height=0.3, fill_color=PALETTE["wood"], fill_opacity=1, stroke_width=0).move_to(
                body.get_bottom() + UP * 0.15)
            return VGroup(body, roof, door)

        def icon_shop():
            b = Rectangle(width=0.9, height=0.6, fill_color=PALETTE["card"], fill_opacity=1, stroke_color=PALETTE["ink"],
                          stroke_width=2.5)
            awn = VGroup(*[Rectangle(width=0.18, height=0.2, fill_color=PALETTE["accent"] if i % 2 == 0 else PALETTE["card"],
                                     fill_opacity=1, stroke_color=PALETTE["accent"], stroke_width=1) for i in range(5)]
                         ).arrange(RIGHT, buff=0).next_to(b, UP, buff=0)
            return VGroup(b, awn)
        icons = [("a hotel", icon_hotel()), ("a gallery", icon_gallery()), ("a shelter", icon_shelter()),
                 ("a small shop", icon_shop())]
        tiles = []
        for lab, ic in icons:
            t = Text(lab, color=PALETTE["ink"], font_size=16)
            tiles.append(VGroup(ic, t).arrange(DOWN, buff=0.15))
        tiles_g = VGroup(*tiles).arrange(RIGHT, buff=0.35)
        fit(tiles_g, 4.6).move_to([-3.4, -1.9, 0])

        # right: what won't change
        rh = chip("what won't change (Orbit's author)", w=5.6, h=0.5, border=PALETTE["good"], color=PALETTE["good"], fs=16)
        rh.move_to([3.4, 2.1, 0])
        wont = ["informative websites that help visitors", "original research, genuine points of view",
                "word of mouth", "live events and communities", "email", "influencer marketing"]
        wl = VGroup(*[chip(t, w=5.6, h=0.5, border=PALETTE["border"], fs=15) for t in wont]).arrange(DOWN, buff=0.12)
        wl.move_to([3.4, -0.3, 0])
        tools = chip("the tools change", w=2.7, h=0.5, border=PALETTE["dim"], color=PALETTE["dim"], fs=16)
        goal = chip("the goal stays: helping people who need you", w=5.4, h=0.5, border=PALETTE["accent"],
                    color=PALETTE["accent"], fs=16)
        tg = VGroup(tools, goal).arrange(RIGHT, buff=0.2).move_to([0, -3.15, 0])
        fit(tg, 12.0)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 2.7)
        self.play(FadeIn(obs, shift=DOWN * 0.1), run_time=0.4)
        wait_until(self, 4.5)
        self.play(FadeIn(a1, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 5.8)
        self.play(FadeIn(a2, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 7.2)
        self.play(FadeIn(clear, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 10.2)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in tiles], lag_ratio=0.5), run_time=2.0)
        wait_until(self, 13.6)
        self.play(FadeIn(rh, shift=DOWN * 0.1), run_time=0.4)
        for t, tm in zip(wl, [15.5, 16.9, 18.2, 19.4, 20.6, 21.3]):
            wait_until(self, tm)
            self.play(FadeIn(t, shift=LEFT * 0.1), run_time=0.3)
        wait_until(self, 22.5)
        self.play(FadeIn(tools, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 24.0)
        self.play(FadeIn(goal, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 26.23)


class B08_ChooseTheTool(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        who = person(1.7, PALETTE["ink"]).move_to([0, 0.4, 0])
        s_ic = VGroup(search_icon(1.2), Text("search", color=PALETTE["blue"], font_size=24, weight="BOLD")).arrange(
            DOWN, buff=0.2)
        s_box = card_bg(2.8, 2.2, stroke_color=PALETTE["blue"])
        s_tool = VGroup(s_box, s_ic.move_to(s_box.get_center())).move_to([-4.6, 0.7, 0])
        a_ic = VGroup(chat_icon(1.5), Text("ask the AI", color=PALETTE["accent"], font_size=24, weight="BOLD")).arrange(
            DOWN, buff=0.25)
        a_box = card_bg(2.8, 2.2, stroke_color=PALETTE["accent"])
        a_tool = VGroup(a_box, a_ic.move_to(a_box.get_center())).move_to([4.6, 0.7, 0])
        pick = chip("we choose a tool depending on the question", w=7.4, h=0.6, border=PALETTE["ink"],
                    color=PALETTE["ink"], fs=19).move_to([0, 2.7, 0])

        q1 = chip("directions to a coffee shop?", w=3.4, h=0.55, border=PALETTE["blue"], color=PALETTE["blue"], fs=16)
        q1.move_to([-4.6, -1.0, 0])
        q2 = chip("a complicated idea,\nin plain words", w=3.4, h=0.8, border=PALETTE["accent"], color=PALETTE["accent"],
                  fs=16).move_to([4.6, -1.0, 0])
        q3 = chip("a trip planned around\nyour family", w=3.4, h=0.8, border=PALETTE["accent"], color=PALETTE["accent"],
                  fs=16).move_to([4.6, -2.0, 0])
        a_s = Arrow(q1.get_top(), s_tool.get_bottom(), buff=0.08, color=PALETTE["blue"], stroke_width=4,
                    max_tip_length_to_length_ratio=0.25)
        a_a = Arrow(q2.get_top(), a_tool.get_bottom(), buff=0.08, color=PALETTE["accent"], stroke_width=4,
                    max_tip_length_to_length_ratio=0.25)
        fin = Text("typing keywords and scanning ten blue links: one of several ways we look for answers",
                   color=PALETTE["ink"], font_size=20, weight="BOLD")
        fit(fin, 12.0).move_to([0, -3.1, 0])

        self.play(FadeIn(who), FadeIn(s_tool, shift=RIGHT * 0.2), FadeIn(a_tool, shift=LEFT * 0.2), run_time=0.8)
        wait_until(self, 3.1)
        self.play(FadeIn(pick, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 5.9)
        self.play(FadeIn(q1, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 7.8)
        self.play(GrowArrow(a_s), run_time=0.4)
        wait_until(self, 8.8)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 11.9)
        self.play(FadeIn(q3, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 14.1)
        self.play(GrowArrow(a_a), run_time=0.4)
        wait_until(self, 15.6)
        self.play(FadeIn(fin, shift=UP * 0.1), run_time=0.6)
        wait_until(self, 21.43)


class B09_SourcesCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("A note on sources", color=PALETTE["ink"], font_size=30, weight="BOLD").move_to([0, 3.05, 0])
        NL = chr(10)
        refs = ["Bain & Company (2026)" + NL + "Why consumers choose an AI chatbot" + NL + "over a search engine",
                "Caswell (2025), Tom's Guide" + NL + "on a survey by the publisher Future",
                "Crestodina (2026), Orbit Media Studios" + NL + "The AI-search adoption survey"]
        rt = Text("References", color=PALETTE["accent"], font_size=22, weight="BOLD")
        rl = VGroup(*[left_lines(r, 18, PALETTE["ink"], buff=0.06) for r in refs]).arrange(
            DOWN, buff=0.35, aligned_edge=LEFT)
        r_in = VGroup(rt, rl).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        r_box = card_bg(5.6, 5.0)
        left = VGroup(r_box, fit_in(r_in, 5.2, 4.6).move_to(r_box.get_center())).move_to([-3.45, -0.2, 0])

        def note(txt, col, h=0.78):
            return chip(txt, w=5.9, h=h, border=col, color=col, fs=15)
        n1 = note("Orbit Media is a web design and SEO company\nand ran its own survey", PALETTE["miss"])
        n2 = note("The Future survey is from a media publisher", PALETTE["miss"], 0.55)
        n3 = note("Bain's survey was conducted in September 2025", PALETTE["blue"], 0.55)
        n4 = note("The surveys measure different things:\ndon't compare their numbers directly", PALETTE["accent"])
        n5 = note("The opening scene is an illustration", PALETTE["dim"], 0.55)
        notes = VGroup(n1, n2, n3, n4, n5).arrange(DOWN, buff=0.2).move_to([3.2, -0.2, 0])

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 1.2)
        reveal(self, left, t1=0.4, t2=0.4)
        wait_until(self, 1.7)
        self.play(FadeIn(n1, shift=LEFT * 0.1), run_time=0.4)
        wait_until(self, 7.1)
        self.play(FadeIn(n2, shift=LEFT * 0.1), run_time=0.4)
        wait_until(self, 10.0)
        self.play(FadeIn(n3, shift=LEFT * 0.1), run_time=0.4)
        wait_until(self, 13.9)
        self.play(FadeIn(n4, shift=LEFT * 0.1), run_time=0.4)
        wait_until(self, 18.4)
        self.play(FadeIn(n5, shift=LEFT * 0.1), run_time=0.4)
        wait_until(self, 20.7)
