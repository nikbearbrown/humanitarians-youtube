"""
Portrait (9:16) Manim scenes for weekly-recap-we-ask-short

Ports of the six graphic beats (B03, B04, B05, B06, B09, B10) -- full parity with the
16:9 cut, no beats dropped (the whole recap fits under the 3:00 limit). Stacked layouts
for a 4.5 x 8.0 frame; same palette, copy and audio timing as the 16:9 scenes. All
visuals are generated: no photos of children or real people, no real platform or
company logos. The Homes of Hope graphic is abstract and carries the required label.
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

L = -1.85   # left edge of the content column
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


def lines(txt, fs, color, max_w=None, buff=0.1, weight=None):
    kw = {"weight": weight} if weight else {}
    g = VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split(chr(10))]).arrange(DOWN, buff=buff)
    return fit(g, max_w) if max_w else g


def left_lines(txt, fs, color, weight=None, buff=0.08):
    kw = {"weight": weight} if weight else {}
    return VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split(chr(10))]).arrange(
        DOWN, buff=buff, aligned_edge=LEFT)


def wait_until(scene, t):
    d = t - scene.renderer.time
    if d > 0.02:
        scene.wait(d)


def chip(label, w=2.6, h=0.5, border=None, color=None, fs=14):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(lines(label, fs, color or PALETTE["ink"], buff=0.05), w - 0.2)
    return VGroup(box, txt.move_to(box.get_center()))


def tick(color=None, s=1.0, sw=4):
    t = VMobject(color=color or PALETTE["good"], stroke_width=sw)
    t.set_points_as_corners([[-0.1, 0.0, 0], [-0.02, -0.1, 0], [0.13, 0.12, 0]])
    return t.scale(s)


def header(n, name, top=3.3):
    kick = Text("PART %d OF 4" % n, color=PALETTE["accent"], font_size=16)
    head = fit(left_lines(name, 32, PALETTE["ink"], weight="BOLD", buff=0.08), W)
    g = VGroup(kick, head).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
    g.move_to([L + g.width / 2, top - g.height / 2, 0])
    return g


# --- icons ------------------------------------------------------------------

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


def chat_bubble(label, w=3.0, h=0.5, fs=12, color=None):
    c = color or PALETTE["accent"]
    box = card_bg(w, h, stroke_color=c)
    t = fit(Text(label, color=PALETTE["ink"], font_size=fs), w - 0.2)
    return VGroup(box, t.move_to(box.get_center()))


def calendar_icon(s=1.0):
    body = RoundedRectangle(corner_radius=0.12, width=3.0, height=2.6, fill_color=PALETTE["card"], fill_opacity=1,
                            stroke_color=PALETTE["ink"], stroke_width=3)
    bar = Rectangle(width=3.0, height=0.55, fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
    bar.move_to(body.get_top() + DOWN * 0.275)
    rings = VGroup(*[RoundedRectangle(corner_radius=0.04, width=0.12, height=0.4, fill_color=PALETTE["ink"],
                                      fill_opacity=1, stroke_width=0).move_to(body.get_top() + RIGHT * x)
                     for x in (-0.8, 0.8)])
    dots = VGroup(*[Dot(radius=0.07, color=PALETTE["border"]) for _ in range(15)]).arrange_in_grid(rows=3, cols=5,
                                                                                                  buff=0.38)
    dots.move_to(body.get_center() + DOWN * 0.35)
    dots[7].set_color(PALETTE["accent"]).scale(1.9)
    return VGroup(body, bar, rings, dots).scale(s)


def outreach_art(s=1.0):
    """Abstract outreach graphic: a megaphone with connected dots around it. No people, no photos."""
    cone = Polygon([-0.32, 0.2, 0], [0.34, 0.6, 0], [0.34, -0.6, 0], [-0.32, -0.2, 0],
                   fill_color=PALETTE["accent"], fill_opacity=1, stroke_color=PALETTE["ink"], stroke_width=3)
    cap = RoundedRectangle(corner_radius=0.05, width=0.3, height=0.46, fill_color=PALETTE["ink"], fill_opacity=1,
                           stroke_width=0).next_to(cone, LEFT, buff=-0.02)
    grip = RoundedRectangle(corner_radius=0.05, width=0.2, height=0.3, fill_color=PALETTE["ink"], fill_opacity=1,
                            stroke_width=0).move_to(cone.get_bottom() + UP * 0.12 + LEFT * 0.12)
    waves = VGroup(*[Arc(radius=r, start_angle=-PI / 5, angle=2 * PI / 5, color=PALETTE["ink"], stroke_width=3)
                     .move_to(cone.get_right() + RIGHT * (r * 0.95 - 0.02) + UP * 0.0) for r in (0.3, 0.52)])
    mega = VGroup(cap, cone, grip, waves).move_to(ORIGIN)
    R = 1.55
    pts = [np.array([R * np.cos(a), R * np.sin(a), 0]) for a in np.linspace(PI / 2, PI / 2 + 2 * PI, 7)[:-1]]
    cols = [PALETTE["good"], PALETTE["wood"], PALETTE["accent"], PALETTE["good"], PALETTE["wood"], PALETTE["accent"]]
    spokes = VGroup(*[Line(ORIGIN, p, color=PALETTE["border"], stroke_width=3) for p in pts])
    ring = VGroup(*[Line(pts[i], pts[(i + 1) % 6], color=PALETTE["dim"], stroke_width=2, stroke_opacity=0.6)
                    for i in range(6)])
    nodes = VGroup(*[Dot(p, radius=0.17, color=c) for p, c in zip(pts, cols)])
    return VGroup(spokes, ring, nodes, mega).scale(s)


def file_tile(w, h, label, fs=22):
    box = RoundedRectangle(corner_radius=0.08, width=w, height=h, fill_color=PALETTE["card"], fill_opacity=1,
                           stroke_color=PALETTE["good"], stroke_width=3)
    t = fit(Text(label, color=PALETTE["ink"], font_size=fs, weight="BOLD"), w - 0.1).move_to(box.get_center())
    return VGroup(box, t)


# --- scenes -----------------------------------------------------------------

class B03_PartWriting(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(1, "Writing")
        status = chip("published", w=1.8, h=0.46, border=PALETTE["good"], color=PALETTE["good"], fs=18)
        tk = tick(PALETTE["good"], 0.8)
        pair = VGroup(tk, status).arrange(RIGHT, buff=0.15)
        pair.move_to([L + pair.width / 2, 2.15, 0])

        card = card_bg(W, 3.9)
        kicker = Text("SUBSTACK  ·  ARTICLE", color=PALETTE["accent"], font_size=13)
        title = lines("We Ask the" + chr(10) + "AI Now", 32, PALETTE["ink"], weight="BOLD", buff=0.08, max_w=3.2)
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)
        l1 = lines("People are splitting their" + chr(10) + "questions between search and AI.", 15, PALETTE["ink"],
                   buff=0.06, max_w=3.3)
        sbar = search_bar(3.2, "search", 11)
        cbub = chat_bubble("ask the AI", w=3.2, h=0.5, fs=12)
        mock = Text("mock article header", color=PALETTE["dim"], font_size=11)
        body = VGroup(kicker, title, rule, l1, sbar, cbub, mock).arrange(DOWN, buff=0.17)
        card.move_to([0, 0.1, 0])
        body.move_to(card.get_center())

        def side(txt, y, col, h=0.55):
            return chip(txt, w=W, h=h, border=col, color=PALETTE["ink"], fs=13).move_to([0, y, 0])
        c1 = side("most still use search as their default", 1.7, PALETTE["blue"])
        c2 = side("many turn to AI chat for hard topics," + chr(10) + "step-by-step help, brainstorming, trips",
                  0.85, PALETTE["accent"], 0.75)
        c3 = side("search now shows AI answers at the top;" + chr(10) + "AI tools now search: the two blend",
                  -0.05, PALETTE["good"], 0.75)
        c4 = side("younger people lead the shift", -0.85, PALETTE["blue"])
        c5 = side("people use AI, with some doubt", -1.5, PALETTE["dim"])
        take = chip("takeaway: clear, helpful information" + chr(10) + "matters more than ever for being found",
                    w=W, h=0.8, border=PALETTE["accent"], color=PALETTE["accent"], fs=13).move_to([0, -2.55, 0])

        wait_until(self, 1.8)
        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 3.4)
        w = card.width
        card.stretch(0.01, 0)
        self.play(FadeIn(card), card.animate.stretch_to_fit_width(w), run_time=0.5)
        self.play(FadeIn(kicker), run_time=0.3)
        wait_until(self, 5.6)
        self.play(FadeIn(pair, shift=RIGHT * 0.1), run_time=0.4)
        wait_until(self, 5.9)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.5)
        grow_in(self, rule, 1.4, run_time=0.3)
        wait_until(self, 7.8)
        self.play(FadeIn(l1, shift=UP * 0.1), FadeIn(sbar, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 9.9)
        self.play(FadeIn(cbub, shift=UP * 0.1), FadeIn(mock), run_time=0.5)
        wait_until(self, 12.7)
        self.play(FadeOut(card), FadeOut(kicker), FadeOut(title), FadeOut(rule), FadeOut(l1), FadeOut(sbar),
                  FadeOut(cbub), FadeOut(mock), run_time=0.3)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 15.6)
        self.play(FadeIn(c2, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 22.2)
        self.play(FadeIn(c3, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 28.8)
        self.play(FadeIn(c4, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 30.6)
        self.play(FadeIn(c5, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 33.3)
        self.play(FadeIn(take, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 37.8)


class B04_PartVideos(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(2, "Video production")
        tool = chip("made with Brutalist," + chr(10) + "our video-creation tool", w=W, h=0.6, border=PALETTE["dim"],
                    color=PALETTE["dim"], fs=13).move_to([0, 2.0, 0])

        def block(label, sub, y):
            lab = Text(label, color=PALETTE["ink"], font_size=24)
            sb = Text(sub, color=PALETTE["dim"], font_size=15)
            col = VGroup(lab, sb).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
            col.move_to([L + col.width / 2, y + 0.65, 0])
            t169 = file_tile(1.5, 0.8, "16:9", fs=17).move_to([-0.95, y - 0.1, 0])
            t916 = file_tile(0.62, 0.9, "9:16", fs=13).move_to([0.55, y - 0.1, 0])
            k1 = tick(PALETTE["good"], 0.75).next_to(t169, RIGHT, buff=0.12)
            k2 = tick(PALETTE["good"], 0.75).next_to(t916, RIGHT, buff=0.12)
            return col, t169, t916, k1, k2

        r1 = block("AI topic video", "based on the article", 0.5)
        r2 = block("Weekly recap", "this video", -0.95)
        count = chip("4 video files", w=W, h=0.6, border=PALETTE["accent"], color=PALETTE["accent"], fs=24)
        count.move_to([0, -1.95, 0])
        each = Text("for each video:", color=PALETTE["dim"], font_size=12).move_to([L + 0.55, -2.4, 0])
        p1 = chip("I wrote the prompt", w=W, h=0.42, border=PALETTE["accent"], color=PALETTE["accent"], fs=13)
        p2 = chip("I reviewed and approved the plan", w=W, h=0.42, border=PALETTE["accent"], color=PALETTE["accent"], fs=13)
        p3 = chip("I checked the final result", w=W, h=0.42, border=PALETTE["accent"], color=PALETTE["accent"], fs=13)
        p1.move_to([0, -2.75, 0])
        p2.move_to([0, -3.22, 0])
        p3.move_to([0, -3.22, 0])
        p2.move_to([0, -3.2, 0])
        p3.move_to([0, -3.2, 0])
        p1.move_to([0, -2.72, 0])

        wait_until(self, 0.2)
        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 2.2)
        self.play(FadeIn(tool, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 5.7)
        self.play(FadeIn(r1[0], shift=RIGHT * 0.2), run_time=0.4)
        wait_until(self, 8.5)
        self.play(FadeIn(r2[0], shift=RIGHT * 0.2), run_time=0.4)
        wait_until(self, 10.4)
        self.play(FadeIn(r1[1]), FadeIn(r2[1]), run_time=0.4)
        self.play(FadeIn(r1[3]), FadeIn(r2[3]), run_time=0.25)
        wait_until(self, 12.0)
        self.play(FadeIn(r1[2]), FadeIn(r2[2]), run_time=0.4)
        self.play(FadeIn(r1[4]), FadeIn(r2[4]), run_time=0.25)
        wait_until(self, 14.2)
        self.play(FadeIn(count, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 16.3)
        self.play(FadeIn(each), FadeIn(p1, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 18.2)
        self.play(FadeOut(p1), FadeIn(p2, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 20.0)
        self.play(FadeOut(p2), FadeIn(p3, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 21.55)


class B05_PartMeeting(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(3, "Weekly meeting")
        att = chip("attended", w=1.7, h=0.46, border=PALETTE["good"], color=PALETTE["good"], fs=18)
        attk = tick(PALETTE["good"], 0.8)
        pair = VGroup(attk, att).arrange(RIGHT, buff=0.15)
        pair.move_to([L + pair.width / 2, 2.15, 0])
        cal = calendar_icon(0.8).move_to([0, 0.55, 0])
        cal_l = Text("the weekly team meeting", color=PALETTE["dim"], font_size=15).move_to([0, -0.8, 0])

        def purpose(txt, y):
            b = card_bg(W, 0.6, stroke_color=PALETTE["accent"])
            t = Text(txt, color=PALETTE["ink"], font_size=19)
            return VGroup(b, fit(t, W - 0.3).move_to(b.get_center())).move_to([0, y, 0])
        s1 = purpose("share progress", -1.5)
        s2 = purpose("stay in sync with the team", -2.2)
        s3 = purpose("plan what comes next", -2.9)

        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 2.2)
        self.play(FadeIn(cal, shift=UP * 0.1), FadeIn(cal_l), run_time=0.6)
        wait_until(self, 4.4)
        self.play(FadeIn(pair, shift=RIGHT * 0.1), run_time=0.4)
        wait_until(self, 6.3)
        self.play(FadeIn(s1, shift=UP * 0.1), run_time=0.35)
        wait_until(self, 7.4)
        self.play(FadeIn(s2, shift=UP * 0.1), run_time=0.35)
        wait_until(self, 8.4)
        self.play(FadeIn(s3, shift=UP * 0.1), run_time=0.35)
        wait_until(self, 9.34)


class B06_PartHomesOfHope(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(4, "Homes of Hope")
        ongoing = chip("ongoing", w=1.5, h=0.46, border=PALETTE["accent"], color=PALETTE["accent"], fs=18)
        ongoing.move_to([L + W - ongoing.width / 2, 2.15, 0])
        kicker = lines("Supports marginalized girls" + chr(10) + "in India with:", 14, PALETTE["dim"], buff=0.05)
        kicker.move_to([0, 1.65, 0])
        c1 = chip("a safe home", w=1.4, h=0.5, border=PALETTE["good"], fs=14)
        c2 = chip("education", w=1.25, h=0.5, border=PALETTE["good"], fs=14)
        c3 = chip("support", w=1.0, h=0.5, border=PALETTE["good"], fs=14)
        row = VGroup(c1, c2, c3).arrange(RIGHT, buff=0.1).move_to([0, 1.05, 0])
        art = outreach_art(0.55).move_to([0, -0.15, 0])
        cap = lines("Homes of Hope documentary outreach" + chr(10) + "(with Yatra)", 14, PALETTE["ink"], buff=0.06,
                    max_w=W).move_to([0, -1.35, 0])
        mine = chip("My work with Yatra:" + chr(10) + "promotion and outreach", w=W, h=0.65, border=PALETTE["accent"],
                    color=PALETTE["accent"], fs=13).move_to([0, -2.1, 0])
        goal = chip("to help the girls' stories" + chr(10) + "reach a wider audience", w=W, h=0.65,
                    border=PALETTE["good"], color=PALETTE["good"], fs=13).move_to([0, -2.85, 0])

        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 2.1)
        self.play(FadeIn(art, shift=UP * 0.1), FadeIn(cap), run_time=0.6)
        wait_until(self, 5.3)
        self.play(FadeIn(kicker), run_time=0.4)
        wait_until(self, 9.8)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.3)
        wait_until(self, 10.8)
        self.play(FadeIn(c2, shift=UP * 0.1), run_time=0.3)
        wait_until(self, 12.1)
        self.play(FadeIn(c3, shift=UP * 0.1), run_time=0.3)
        wait_until(self, 13.3)
        self.play(FadeIn(mine, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 15.6)
        self.play(FadeIn(goal, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 18.8)
        self.play(FadeIn(ongoing, shift=LEFT * 0.1), run_time=0.4)
        wait_until(self, 20.05)


def hcard(icon, role, role_color, title, detail, h=1.25, highlight=False, icon_w=1.1):
    box = card_bg(W, h, stroke_color=PALETTE["accent"] if highlight else PALETTE["border"])
    icon = icon.copy()
    fit_in(icon, icon_w, h - 0.3)
    r = Text(role, color=role_color, font_size=13, weight="BOLD")
    t = left_lines(title, 19, PALETTE["ink"], weight="BOLD", buff=0.03)
    d = left_lines(detail, 14, PALETTE["dim"], buff=0.03)
    texts = VGroup(r, t, d).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
    inner = VGroup(icon, texts).arrange(RIGHT, buff=0.25)
    fit(inner, W - 0.3)
    inner.move_to(box.get_center())
    return VGroup(box, inner)


def mini_article():
    box = RoundedRectangle(corner_radius=0.06, width=1.5, height=1.2, fill_color=PALETTE["bg"], fill_opacity=1,
                           stroke_color=PALETTE["dim"], stroke_width=2)
    k = Text("ARTICLE", color=PALETTE["accent"], font_size=14)
    ls = VGroup(*[Line(LEFT * 0.5, RIGHT * (0.5 - 0.15 * (i % 2)), color=PALETTE["border"], stroke_width=3)
                  for i in range(3)]).arrange(DOWN, buff=0.12)
    VGroup(k, ls).arrange(DOWN, buff=0.14).move_to(box.get_center())
    return VGroup(box, k, ls)


def mini_videos():
    def pair():
        a = file_tile(0.95, 0.5, "16:9", fs=14)
        b = file_tile(0.36, 0.5, "", fs=10)
        c = Text("9:16", color=PALETTE["ink"], font_size=10, weight="BOLD")
        return VGroup(a, VGroup(b, c.move_to(b.get_center()))).arrange(RIGHT, buff=0.1)
    return VGroup(pair(), pair()).arrange(DOWN, buff=0.12)


class B09_StatusWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        cards = [
            hcard(mini_article(), "PUBLISHED", PALETTE["good"], "Writing", "article published"),
            hcard(mini_videos(), "PRODUCED", PALETTE["good"], "Video" + chr(10) + "production", "four video files"),
            hcard(calendar_icon(0.3), "ATTENDED", PALETTE["good"], "Weekly" + chr(10) + "meeting", "team meeting"),
            hcard(outreach_art(0.3), "ONGOING", PALETTE["accent"], "Homes of Hope", "with Yatra", highlight=True),
        ]
        VGroup(*cards).arrange(DOWN, buff=0.12).move_to([0, 0.5, 0])
        count = chip("3 parts done" + chr(10) + "1 ongoing", w=W, h=0.85, border=PALETTE["accent"],
                     color=PALETTE["accent"], fs=24)
        count.move_to([0, -2.85, 0])

        wait_until(self, 2.4)
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.15), run_time=0.3)
        wait_until(self, 5.8)
        self.play(FadeIn(count, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 7.6)
        self.play(Indicate(cards[3][0], color=PALETTE["accent"], scale_factor=1.03), run_time=0.8)
        wait_until(self, 8.36)


class B10_WeekInOneLine(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        k = lines("A real progress" + chr(10) + "update.", 24, PALETTE["dim"], buff=0.1)
        l1 = lines("An article" + chr(10) + "published.", 28, PALETTE["ink"], buff=0.06)
        l2 = lines("Videos made in" + chr(10) + "two formats.", 28, PALETTE["ink"], buff=0.06)
        l3 = lines("A team meeting" + chr(10) + "attended.", 28, PALETTE["ink"], buff=0.06)
        l4 = lines("Steady progress on" + chr(10) + "Homes of Hope.", 28, PALETTE["accent"], buff=0.06)
        g = VGroup(l1, l2, l3, l4).arrange(DOWN, buff=0.32)
        VGroup(k, g).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        fit(VGroup(k, g), W)

        self.play(FadeIn(k, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 1.9)
        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 3.3)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 5.3)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 7.0)
        self.play(FadeIn(l4, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 8.82)
