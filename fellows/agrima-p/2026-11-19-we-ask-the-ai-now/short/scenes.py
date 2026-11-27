"""
Portrait (9:16) Manim scenes for we-ask-the-ai-now-short

Ports of the seven graphic beats kept in the Short (B00B, B01, B02, B03, B04, B08, B09).
B00 (cold open), B05 (younger people), B06 (trust) and B07 (being found) are dropped to fit
the 3:00 Shorts cap (see short/FACTCHECK.md). Stacked layouts for a 4.5 x 8.0 frame; same
palette, copy and audio timing as the 16:9 scenes. All visuals are generated with NO brand
logos: generic search and chat icons only. Each survey keeps its own card and source chip;
the numbers of different surveys are never merged.
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
    "blue":   "#5B7FA6",
}

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


def lines(txt, fs, color, max_w=None, buff=0.07, weight=None):
    kw = {"weight": weight} if weight else {}
    g = VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split(chr(10))]).arrange(DOWN, buff=buff)
    return fit(g, max_w) if max_w else g


def wait_until(scene, t):
    d = t - scene.renderer.time
    if d > 0.02:
        scene.wait(d)


def chip(label, w=2.6, h=0.42, border=None, color=None, fs=13):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(lines(label, fs, color or PALETTE["ink"], buff=0.05), w - 0.2)
    return VGroup(box, txt.move_to(box.get_center()))


def src_chip(label, w=3.4, fs=10):
    return chip(label, w=w, h=0.32, border=PALETTE["dim"], color=PALETTE["dim"], fs=fs)


def meter(w, frac, color, h=0.2):
    track = RoundedRectangle(corner_radius=0.08, width=w, height=h, fill_color=PALETTE["border"],
                             fill_opacity=1, stroke_width=0)
    fill = RoundedRectangle(corner_radius=0.08, width=max(w * frac, 0.2), height=h, fill_color=color,
                            fill_opacity=1, stroke_width=0).align_to(track, LEFT)
    return VGroup(track, fill)


def person(h=1.0, color=None):
    c = color or PALETTE["ink"]
    head = Circle(radius=0.26 * h, color=c, fill_color=c, fill_opacity=1, stroke_width=0)
    body = RoundedRectangle(corner_radius=0.18 * h, width=0.7 * h, height=0.8 * h,
                            fill_color=c, fill_opacity=1, stroke_width=0)
    return VGroup(head, body).arrange(DOWN, buff=0.05)


def search_bar(w=3.4, text=None, fs=12):
    """A GENERIC search bar (no brand): magnifier + field."""
    box = card_bg(w, 0.5, stroke_color=PALETTE["ink"])
    lens = Circle(radius=0.1, color=PALETTE["ink"], stroke_width=3)
    handle = Line([0.07, -0.07, 0], [0.18, -0.18, 0], color=PALETTE["ink"], stroke_width=3)
    mag = VGroup(lens, handle).move_to(box.get_left() + RIGHT * 0.3)
    parts = [box, mag]
    if text:
        t = Text(text, color=PALETTE["dim"], font_size=fs)
        fit(t, w - 0.8)
        t.move_to([box.get_left()[0] + 0.6 + t.width / 2, box.get_center()[1], 0])
        parts.append(t)
    return VGroup(*parts)


def bubble(label, w=3.0, h=0.42, fs=11, color=None, filled=False):
    """A GENERIC chat bubble (no brand)."""
    c = color or PALETTE["accent"]
    box = card_bg(w, h, stroke_color=c, fill=c if filled else None)
    t = fit(lines(label, fs, PALETTE["card"] if filled else PALETTE["ink"], buff=0.05), w - 0.2)
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


def tab_rect(w=0.55, h=0.3):
    return RoundedRectangle(corner_radius=0.05, width=w, height=h, fill_color=PALETTE["card"], fill_opacity=1,
                            stroke_color=PALETTE["dim"], stroke_width=2)


def stat(big, label, col, h=1.4, bfs=40, frac=None):
    box = card_bg(W, h, stroke_color=col)
    parts = [Text(big, color=col, font_size=bfs, weight="BOLD"), lines(label, 13, PALETTE["ink"], buff=0.05)]
    if frac is not None:
        parts.append(meter(3.0, frac, col, h=0.2))
    g = VGroup(*parts).arrange(DOWN, buff=0.1)
    return VGroup(box, fit_in(g, W - 0.3, h - 0.2).move_to(box.get_center()))


# --- scenes -----------------------------------------------------------------

class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=34)
        summary = fit(lines("Today: how we now\nsplit our questions\nbetween search\nand AI.", 22, PALETTE["ink"],
                            buff=0.14), W)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        wait_until(self, 5.35)


class B01_PlanningATrip(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        note = chip("illustration -- not a real case", w=3.4, h=0.4, border=PALETTE["ink"], color=PALETTE["ink"], fs=13)
        note.move_to([0, 3.25, 0])
        mapc = card_bg(1.5, 1.0, stroke_color=PALETTE["wood"], fill=PALETTE["warm"]).move_to([-0.8, 2.3, 0])
        route = VMobject(color=PALETTE["accent"], stroke_width=3).set_points_smoothly(
            [mapc.get_center() + np.array(p) for p in ((-0.5, -0.25, 0), (-0.15, 0.15, 0), (0.15, -0.08, 0), (0.45, 0.25, 0))])
        pn = Circle(radius=0.07, fill_color=PALETTE["accent"], fill_opacity=1, stroke_color=PALETTE["ink"],
                    stroke_width=2).move_to(mapc.get_center() + np.array([0.45, 0.25, 0]))
        who = person(0.9, PALETTE["ink"]).move_to([0.75, 2.2, 0])
        ph = RoundedRectangle(corner_radius=0.05, width=0.28, height=0.46, fill_color=PALETTE["card"], fill_opacity=1,
                              stroke_color=PALETTE["accent"], stroke_width=2.5).move_to([1.1, 2.3, 0])
        trip = Text("planning a weekend trip", color=PALETTE["dim"], font_size=12).move_to([0, 1.5, 0])

        # stage A: a few years ago
        a_head = chip("a few years ago", w=2.0, h=0.38, border=PALETTE["blue"], color=PALETTE["blue"], fs=13)
        a_head.move_to([0, 1.15, 0])
        a_bar = search_bar(W, "best things to do in Lisbon", 11).move_to([0, 0.55, 0])
        tabs = VGroup(*[tab_rect() for _ in range(10)]).arrange_in_grid(rows=2, cols=5, buff=0.08).move_to([0, -0.3, 0])
        a_cap = Text("ten tabs", color=PALETTE["dim"], font_size=14).move_to([0, -0.9, 0])

        # stage B: today
        b_head = chip("today", w=1.4, h=0.38, border=PALETTE["accent"], color=PALETTE["accent"], fs=13)
        b_head.move_to([0, 1.15, 0])
        q1 = bubble("best things to do in Lisbon", w=W, h=0.42, fs=11, filled=True).move_to([0, 0.55, 0])
        q2 = bubble("I have two kids and a small budget", w=W, h=0.42, fs=11, filled=True).move_to([0, 0.0, 0])
        ans = VGroup(card_bg(W, 1.1, stroke_color=PALETTE["good"]),
                     VGroup(*[Line(LEFT * (1.4 - 0.25 * (i % 3)), RIGHT * (1.4 - 0.25 * (i % 3)), color=PALETTE["dim"],
                                   stroke_width=3, stroke_opacity=0.6) for i in range(4)]).arrange(DOWN, buff=0.15))
        ans[1].move_to(ans[0].get_center())
        ans.move_to([0, -0.9, 0])
        b_cap = Text("one answer, in seconds", color=PALETTE["good"], font_size=16, weight="BOLD").move_to([0, -1.7, 0])
        real = chip("it matches something real", w=W, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=16)
        real.move_to([0, -2.6, 0])

        self.play(FadeIn(note), run_time=0.5)
        self.play(FadeIn(mapc), Create(route), FadeIn(pn), FadeIn(who), FadeIn(ph), FadeIn(trip), run_time=0.8)
        wait_until(self, 1.8)
        self.play(FadeIn(a_head, shift=DOWN * 0.1), FadeIn(a_bar), run_time=0.6)
        wait_until(self, 4.7)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in tabs], lag_ratio=0.1), FadeIn(a_cap), run_time=1.0)
        wait_until(self, 6.6)
        self.play(FadeOut(a_head), FadeOut(a_bar), FadeOut(tabs), FadeOut(a_cap), run_time=0.3)
        self.play(FadeIn(b_head, shift=DOWN * 0.1), FadeIn(q1, shift=LEFT * 0.1), run_time=0.5)
        wait_until(self, 10.0)
        self.play(FadeIn(q2, shift=LEFT * 0.1), run_time=0.5)
        wait_until(self, 12.7)
        self.play(FadeIn(ans, shift=UP * 0.1), FadeIn(b_cap), run_time=0.6)
        wait_until(self, 17.5)
        self.play(FadeIn(real, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 18.92)


class B02_SearchSplit(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        sb = search_bar(1.75, "search", 11).move_to([-1.0, 3.25, 0])
        cb = bubble("ask the AI", w=1.75, h=0.5, fs=12).move_to([1.0, 3.25, 0])
        two = Text("two tools", color=PALETTE["dim"], font_size=12).move_to([0, 2.8, 0])

        bh = chip("Bain & Company  ·  1,500 US consumers", w=W, h=0.4, border=PALETTE["blue"], color=PALETTE["blue"], fs=11)
        bh.move_to([0, 2.35, 0])
        bsub = Text("mostly or always use ... as their default tool", color=PALETTE["dim"], font_size=10).move_to([0, 1.95, 0])
        card1 = stat("56%", "search engines", PALETTE["blue"], h=1.6, bfs=42, frac=0.56).move_to([0, 0.95, 0])
        card2 = stat("16%", "AI chatbots", PALETTE["accent"], h=1.6, bfs=42, frac=0.16).move_to([0, -0.75, 0])

        oh = chip("Orbit Media  ·  March 2026  ·  1,110 US adults", w=W, h=0.4, border=PALETTE["good"],
                  color=PALETTE["good"], fs=11).move_to([0, 2.35, 0])
        stay = chip("Google use hasn't declined", w=W, h=0.4, border=PALETTE["dim"], fs=12).move_to([0, 1.8, 0])

        def shift_card(label, a, b, col, y):
            arrow = Arrow([-0.3, 0, 0], [0.3, 0, 0], buff=0, color=col, stroke_width=4, max_tip_length_to_length_ratio=0.5)
            row = VGroup(Text("%d%%" % a, color=PALETTE["dim"], font_size=32, weight="BOLD"), arrow,
                         Text("%d%%" % b, color=col, font_size=38, weight="BOLD")).arrange(RIGHT, buff=0.25)
            lab = lines(label, 12, PALETTE["ink"], buff=0.04)
            inner = VGroup(row, lab).arrange(DOWN, buff=0.1)
            box = card_bg(W, 1.4, stroke_color=col)
            return VGroup(box, inner.move_to(box.get_center())).move_to([0, y, 0])
        o1 = shift_card("usually use search for research" + chr(10) + "(2025 to 2026)", 22, 29, PALETTE["good"], 0.55)
        o2 = shift_card("usually use AI chat" + chr(10) + "(2025 to 2026)", 35, 28, PALETTE["accent"], -1.05)
        both = lines("two tools," + chr(10) + "picked by the question", 20, PALETTE["ink"], buff=0.1, weight="BOLD")
        both.move_to([0, -2.4, 0])

        self.play(FadeIn(two), run_time=0.4)
        wait_until(self, 1.3)
        self.play(FadeIn(sb, shift=RIGHT * 0.1), FadeIn(cb, shift=LEFT * 0.1), run_time=0.7)
        wait_until(self, 2.8)
        self.play(FadeIn(bh, shift=DOWN * 0.1), FadeIn(bsub), run_time=0.5)
        wait_until(self, 7.0)
        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.6)
        wait_until(self, 12.8)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.6)
        wait_until(self, 16.1)
        self.play(FadeOut(bh), FadeOut(bsub), FadeOut(card1), FadeOut(card2), run_time=0.3)
        self.play(FadeIn(oh, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 20.1)
        self.play(FadeIn(stay, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 22.1)
        self.play(FadeIn(o1, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 27.3)
        self.play(FadeIn(o2, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 33.0)
        self.play(FadeIn(both), run_time=0.4)
        wait_until(self, 33.9)


class B03_HandOver(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # stage A: Bain
        bh = chip("Bain & Company  ·  what chatbot users use it for", w=W, h=0.4, border=PALETTE["blue"],
                  color=PALETTE["blue"], fs=11).move_to([0, 3.2, 0])
        items = [("makes complicated topics easier to understand", 53), ("gives step-by-step instructions", 47),
                 ("helps with brainstorming", 45), ("answers quick factual questions", 45)]
        rows = []
        for lab, v in items:
            t = fit(Text(lab, color=PALETTE["ink"], font_size=13), W)
            m = meter(2.9, v / 60.0, PALETTE["blue"], h=0.22)
            n = Text("%d%%" % v, color=PALETTE["blue"], font_size=22, weight="BOLD")
            rows.append(VGroup(t, VGroup(m, n).arrange(RIGHT, buff=0.2)).arrange(DOWN, buff=0.08, aligned_edge=LEFT))
        stack = VGroup(*rows).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to([0, 1.4, 0])
        bsrc = src_chip("Bain & Company (survey in September 2025)", W).move_to([0, -0.5, 0])

        # stage B: Future
        fh = chip("Future (a publisher)  ·  survey from 2025", w=W, h=0.4, border=PALETTE["good"], color=PALETTE["good"],
                  fs=11).move_to([0, 3.2, 0])
        us = VGroup(Text("55%", color=PALETTE["good"], font_size=38, weight="BOLD"),
                    Text("US", color=PALETTE["ink"], font_size=14)).arrange(DOWN, buff=0.04)
        uk = VGroup(Text("62%", color=PALETTE["good"], font_size=38, weight="BOLD"),
                    Text("UK", color=PALETTE["ink"], font_size=14)).arrange(DOWN, buff=0.04)
        both = VGroup(us, uk).arrange(RIGHT, buff=0.8).move_to([0, 2.35, 0])
        use = fit(Text("use AI instead of search for some tasks", color=PALETTE["ink"], font_size=13), W).move_to([0, 1.6, 0])
        tasks = VGroup(*[chip(t, w=1.18, h=0.36, border=PALETTE["border"], fs=9) for t in
                         ("planning vacations", "fitness plans", "gift ideas", "fixing tech problems",
                          "comparing products", "drafting emails")]).arrange_in_grid(rows=2, cols=3, buff=0.08)
        tasks.move_to([0, 0.95, 0])

        # stage C: Orbit, local searches
        oh = chip("Orbit Media (March 2026)", w=W, h=0.4, border=PALETTE["accent"], color=PALETTE["accent"],
                  fs=11).move_to([0, 3.2, 0])
        local = VGroup(Text("24%", color=PALETTE["accent"], font_size=44, weight="BOLD"),
                       lines("preferred AI chat for local searches" + chr(10) + "(finding a nearby business)", 12,
                             PALETTE["ink"], buff=0.05)).arrange(DOWN, buff=0.12)
        lcard = VGroup(card_bg(W, 1.5, stroke_color=PALETTE["accent"]), local)
        local.move_to(lcard[0].get_center())
        lcard.move_to([0, 2.2, 0])
        exc = lines("the exception:" + chr(10) + "local searches still favor search", 15, PALETTE["ink"], buff=0.1,
                    weight="BOLD").move_to([0, 0.7, 0])

        self.play(FadeIn(bh, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 3.9)
        self.play(FadeIn(rows[0], shift=RIGHT * 0.1), run_time=0.5)
        wait_until(self, 8.6)
        self.play(FadeIn(rows[1], shift=RIGHT * 0.1), run_time=0.5)
        wait_until(self, 11.7)
        self.play(FadeIn(rows[2], shift=RIGHT * 0.1), run_time=0.5)
        wait_until(self, 13.2)
        self.play(FadeIn(rows[3], shift=RIGHT * 0.1), FadeIn(bsrc), run_time=0.5)
        wait_until(self, 15.9)
        self.play(FadeOut(bh), FadeOut(rows[0]), FadeOut(rows[1]), FadeOut(rows[2]), FadeOut(rows[3]), FadeOut(bsrc),
                  run_time=0.3)
        self.play(FadeIn(fh, shift=DOWN * 0.1), run_time=0.4)
        wait_until(self, 19.1)
        self.play(FadeIn(us, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 22.1)
        self.play(FadeIn(uk, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 24.4)
        self.play(FadeIn(use), FadeIn(tasks), run_time=0.6)
        wait_until(self, 27.7)
        self.play(FadeOut(fh), FadeOut(us), FadeOut(uk), FadeOut(use), FadeOut(tasks), run_time=0.3)
        self.play(FadeIn(oh, shift=DOWN * 0.1), FadeIn(exc, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 30.2)
        self.play(FadeIn(lcard, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 34.65)


class B04_AnswerOnTop(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        page = card_bg(W, 3.0, stroke_color=PALETTE["ink"]).move_to([0, 1.75, 0])
        bar = search_bar(3.3, "a question", 11).move_to([0, 2.85, 0])
        summ = VGroup(card_bg(3.3, 0.85, stroke_color=PALETTE["accent"], fill=PALETTE["warm"]),
                      VGroup(*[Line(LEFT * (1.35 - 0.2 * (i % 2)), RIGHT * (1.35 - 0.2 * (i % 2)), color=PALETTE["dim"],
                                    stroke_width=2.5, stroke_opacity=0.6) for i in range(3)]).arrange(DOWN, buff=0.14))
        summ[1].move_to(summ[0].get_center())
        summ.move_to([0, 2.05, 0])
        s_lab = Text("the answer is at the top", color=PALETTE["accent"], font_size=12, weight="BOLD").move_to([0, 1.45, 0])
        links = VGroup(*[VGroup(Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["blue"], stroke_width=3),
                                Line(LEFT * 1.5, RIGHT * (1.5 - 0.4 * i), color=PALETTE["border"], stroke_width=2.5)
                                ).arrange(DOWN, buff=0.07) for i in range(3)]).arrange(DOWN, buff=0.15)
        links.move_to([0, 0.75, 0])

        c76 = VGroup(card_bg(W, 1.05, stroke_color=PALETTE["good"]),
                     VGroup(Text("76%", color=PALETTE["good"], font_size=34, weight="BOLD"),
                            lines("of search results pages show" + chr(10) + "Google's AI Overviews", 12, PALETTE["ink"],
                                  buff=0.04)).arrange(RIGHT, buff=0.3))
        c76[1].move_to(c76[0].get_center())
        c76.move_to([0, -0.5, 0])
        tag76 = src_chip("Orbit Media, citing a study it names", W).move_to([0, -1.2, 0])

        seg = VGroup(Rectangle(width=0.7 * 3.3, height=0.28, fill_color=PALETTE["good"], fill_opacity=1, stroke_width=0),
                     Rectangle(width=0.23 * 3.3, height=0.28, fill_color=PALETTE["wood"], fill_opacity=1, stroke_width=0),
                     Rectangle(width=0.07 * 3.3, height=0.28, fill_color=PALETTE["miss"], fill_opacity=1, stroke_width=0)
                     ).arrange(RIGHT, buff=0)
        l70 = chip("70%: use AI summaries at least occasionally", w=3.5, h=0.38, border=PALETTE["good"],
                   color=PALETTE["good"], fs=10)
        l23 = chip("about 23%: ignore them", w=3.5, h=0.38, border=PALETTE["wood"], fs=10)
        l7 = chip("7%: have turned them off", w=3.5, h=0.38, border=PALETTE["miss"], color=PALETTE["miss"], fs=10)
        split = VGroup(seg, VGroup(l70, l23, l7).arrange(DOWN, buff=0.07)).arrange(DOWN, buff=0.15)
        sbox = card_bg(W, 1.85, stroke_color=PALETTE["good"])
        scard = VGroup(sbox, split.move_to(sbox.get_center())).move_to([0, -0.9, 0])
        osrc = src_chip("Orbit Media survey", 2.2).move_to([0, -2.0, 0])

        c46 = VGroup(card_bg(W, 1.05, stroke_color=PALETTE["blue"]),
                     VGroup(Text("46%", color=PALETTE["blue"], font_size=34, weight="BOLD"),
                            lines("of Bain's respondents use AI" + chr(10) + "overviews from search engines", 12,
                                  PALETTE["ink"], buff=0.04)).arrange(RIGHT, buff=0.3))
        c46[1].move_to(c46[0].get_center())
        c46.move_to([0, -0.5, 0])
        b_src = src_chip("Bain & Company", 2.0).move_to([0, -1.2, 0])

        c_sum = chip("search engines now summarize", w=3.3, h=0.46, border=PALETTE["blue"], color=PALETTE["blue"], fs=12)
        c_sea = chip("AI tools now search", w=2.4, h=0.46, border=PALETTE["accent"], color=PALETTE["accent"], fs=12)
        c_sum.move_to([0, -2.4, 0])
        c_sea.move_to([0, -3.0, 0])

        self.play(FadeIn(page), FadeIn(bar), FadeIn(links), run_time=0.7)
        wait_until(self, 2.5)
        self.play(FadeIn(summ, shift=DOWN * 0.1), FadeIn(s_lab), run_time=0.6)
        wait_until(self, 4.5)
        self.play(FadeIn(c76, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 8.3)
        self.play(FadeIn(tag76), run_time=0.3)
        wait_until(self, 11.2)
        self.play(FadeOut(c76), FadeOut(tag76), run_time=0.3)
        self.play(FadeIn(sbox), FadeIn(seg[0]), FadeIn(l70), FadeIn(osrc), run_time=0.5)
        wait_until(self, 14.4)
        self.play(FadeIn(seg[1]), FadeIn(l23), run_time=0.4)
        wait_until(self, 16.5)
        self.play(FadeIn(seg[2]), FadeIn(l7), run_time=0.4)
        wait_until(self, 18.6)
        self.play(FadeOut(sbox), FadeOut(seg), FadeOut(l70), FadeOut(l23), FadeOut(l7), FadeOut(osrc), run_time=0.3)
        self.play(FadeIn(c46, shift=UP * 0.1), FadeIn(b_src), run_time=0.5)
        wait_until(self, 23.0)
        self.play(FadeIn(c_sum, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 25.1)
        self.play(FadeIn(c_sea, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 26.85)


class B08_ChooseTheTool(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        pick = chip("we choose a tool depending" + chr(10) + "on the question", w=W, h=0.6, border=PALETTE["ink"], fs=13)
        pick.move_to([0, 3.05, 0])
        s_box = card_bg(1.7, 1.4, stroke_color=PALETTE["blue"])
        s_ic = VGroup(search_icon(0.7), Text("search", color=PALETTE["blue"], font_size=15, weight="BOLD")).arrange(
            DOWN, buff=0.12)
        s_tool = VGroup(s_box, s_ic.move_to(s_box.get_center())).move_to([-1.0, 1.85, 0])
        a_box = card_bg(1.7, 1.4, stroke_color=PALETTE["accent"])
        a_ic = VGroup(chat_icon(0.85), Text("ask the AI", color=PALETTE["accent"], font_size=15, weight="BOLD")).arrange(
            DOWN, buff=0.15)
        a_tool = VGroup(a_box, a_ic.move_to(a_box.get_center())).move_to([1.0, 1.85, 0])
        who = person(0.8, PALETTE["ink"]).move_to([0, 0.4, 0])

        q1 = chip("directions to a" + chr(10) + "coffee shop?", w=1.7, h=0.6, border=PALETTE["blue"], color=PALETTE["blue"], fs=11)
        q1.move_to([-1.0, -0.7, 0])
        q2 = chip("a complicated idea," + chr(10) + "in plain words", w=1.7, h=0.6, border=PALETTE["accent"],
                  color=PALETTE["accent"], fs=11).move_to([1.0, -0.7, 0])
        q3 = chip("a trip planned" + chr(10) + "around your family", w=1.7, h=0.6, border=PALETTE["accent"],
                  color=PALETTE["accent"], fs=11).move_to([1.0, -1.45, 0])
        a_s = Arrow(q1.get_top(), s_tool.get_bottom(), buff=0.06, color=PALETTE["blue"], stroke_width=3,
                    max_tip_length_to_length_ratio=0.1)
        a_a = Arrow(q2.get_top(), a_tool.get_bottom(), buff=0.06, color=PALETTE["accent"], stroke_width=3,
                    max_tip_length_to_length_ratio=0.1)
        fin = lines("typing keywords and scanning" + chr(10) + "ten blue links:" + chr(10) + "one of several ways" + chr(10) +
                    "we look for answers", 16, PALETTE["ink"], buff=0.1, weight="BOLD", max_w=W).move_to([0, -2.7, 0])

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

        title = Text("A note on sources", color=PALETTE["ink"], font_size=22, weight="BOLD").move_to([0, 3.15, 0])
        refs = ["Bain & Company (2026)" + chr(10) + "Why consumers choose an AI chatbot" + chr(10) + "over a search engine",
                "Caswell (2025), Tom's Guide" + chr(10) + "on a survey by the publisher Future",
                "Crestodina (2026), Orbit Media Studios" + chr(10) + "The AI-search adoption survey"]
        rt = Text("References", color=PALETTE["accent"], font_size=14, weight="BOLD")
        rl = VGroup(*[VGroup(*[Text(t, color=PALETTE["ink"], font_size=11) for t in r.split(chr(10))]).arrange(
            DOWN, buff=0.04, aligned_edge=LEFT) for r in refs]).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        r_in = VGroup(rt, rl).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        r_box = card_bg(W, 2.5)
        left = VGroup(r_box, fit_in(r_in, W - 0.3, 2.3).move_to(r_box.get_center())).move_to([0, 1.55, 0])

        n1 = chip("Orbit Media is a web design and SEO" + chr(10) + "company and ran its own survey", w=W, h=0.62,
                  border=PALETTE["miss"], color=PALETTE["miss"], fs=11).move_to([0, -0.3, 0])
        n2 = chip("The Future survey is from a media publisher", w=W, h=0.42, border=PALETTE["miss"],
                  color=PALETTE["miss"], fs=11).move_to([0, -0.95, 0])
        n3 = chip("Bain's survey was conducted in September 2025", w=W, h=0.42, border=PALETTE["blue"],
                  color=PALETTE["blue"], fs=11).move_to([0, -1.5, 0])
        n4 = chip("The surveys measure different things:" + chr(10) + "don't compare their numbers directly", w=W,
                  h=0.62, border=PALETTE["accent"], color=PALETTE["accent"], fs=11).move_to([0, -2.2, 0])
        n5 = chip("The opening scene is an illustration", w=W, h=0.42, border=PALETTE["dim"], color=PALETTE["dim"],
                  fs=11).move_to([0, -2.85, 0])

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 1.2)
        w = r_box.width
        r_box.stretch(0.01, 0)
        self.play(r_box.animate.stretch_to_fit_width(w), run_time=0.4)
        self.play(FadeIn(left[1]), run_time=0.4)
        wait_until(self, 1.7)
        self.play(FadeIn(n1, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 7.1)
        self.play(FadeIn(n2, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 10.0)
        self.play(FadeIn(n3, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 13.9)
        self.play(FadeIn(n4, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 18.4)
        self.play(FadeIn(n5, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 20.7)
