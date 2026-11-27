"""
Manim scenes for weekly-recap-we-ask

A first-person, professional weekly-progress CLI-explainer. The OUTPUT beats
visualize the REAL output of weekly_recap_v1.py / weekly_recap_v2.py. Every visual
here is a generated graphic: no photos of children or real people, no real platform
or company logos. The article is a mock header (a plain-text kicker, a generic search
bar and chat bubble); the meeting is a generic calendar icon; the Homes of Hope work
is an abstract graphic (connected dots around a megaphone) with the required label
and nothing about the work itself beyond "ongoing". Built in the house Claude palette.
Reveals are timed to the narration (pause points measured from each beat's mp3).

B03_PartWriting       -- part 1: mock article header + the summary as short chips
B04_PartVideos        -- part 2: two videos x two formats = four files; prompt, plan, final check
B05_PartMeeting       -- part 3: a calendar icon + share progress / stay in sync / plan next
B06_PartHomesOfHope   -- part 4: abstract outreach graphic, labeled, with Yatra; ongoing
B09_StatusWeek        -- the four parts with status chips + the count
B10_WeekInOneLine     -- the closing line, one short line at a time
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


def lines(txt, fs, color, max_w=None, buff=0.12, weight=None):
    kw = {"weight": weight} if weight else {}
    g = VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split(chr(10))]).arrange(DOWN, buff=buff)
    return fit(g, max_w) if max_w else g


def wait_until(scene, t):
    d = t - scene.renderer.time
    if d > 0.02:
        scene.wait(d)


def chip(label, w=2.6, h=0.6, border=None, color=None, fs=16):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(lines(label, fs, color or PALETTE["ink"], buff=0.06), w - 0.3)
    return VGroup(box, txt.move_to(box.get_center()))


def tick(color=None, s=1.0, sw=5):
    t = VMobject(color=color or PALETTE["good"], stroke_width=sw)
    t.set_points_as_corners([[-0.1, 0.0, 0], [-0.02, -0.1, 0], [0.13, 0.12, 0]])
    return t.scale(s)


def header(n, name, color=None):
    kick = Text("PART %d OF 4" % n, color=PALETTE["accent"], font_size=24)
    head = fit(Text(name, color=PALETTE["ink"], font_size=50, weight="BOLD"), 8.2)
    g = VGroup(kick, head).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
    g.move_to([-6.1 + g.width / 2, 3.2 - g.height / 2, 0])
    return g


def status_chip(label, color=None, w=2.5):
    c = color or PALETTE["good"]
    ch = chip(label, w=w, h=0.62, border=c, color=c, fs=24)
    ch.move_to([6.1 - ch.width / 2, 2.88, 0])
    return ch


# --- icons ------------------------------------------------------------------

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


def chat_bubble(label, w=3.0, h=0.62, fs=16, color=None):
    """A GENERIC chat bubble (no brand)."""
    c = color or PALETTE["accent"]
    box = card_bg(w, h, stroke_color=c)
    t = fit(Text(label, color=PALETTE["ink"], font_size=fs), w - 0.3)
    return VGroup(box, t.move_to(box.get_center()))


def calendar_icon(s=1.0):
    """A generic calendar icon (no brand)."""
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
    t = fit(Text(label, color=PALETTE["ink"], font_size=fs, weight="BOLD"), w - 0.2).move_to(box.get_center())
    return VGroup(box, t)


# --- scenes -----------------------------------------------------------------

class B03_PartWriting(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(1, "Writing")
        status = status_chip("published")
        tickm = tick(PALETTE["good"], 1.0).next_to(status, LEFT, buff=0.2)

        card = card_bg(5.6, 4.6, stroke_color=PALETTE["border"])
        kicker = Text("SUBSTACK  ·  ARTICLE", color=PALETTE["accent"], font_size=18)
        title = Text("We Ask the AI Now", color=PALETTE["ink"], font_size=40, weight="BOLD")
        fit(title, 5.0)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        l1 = lines("People are splitting their questions" + chr(10) + "between search and AI.", 20, PALETTE["ink"],
                   buff=0.08, max_w=5.0)
        sbar = search_bar(4.6, "search", 15)
        cbub = chat_bubble("ask the AI", w=4.6, h=0.62, fs=16)
        mock = Text("mock article header", color=PALETTE["dim"], font_size=15)
        body = VGroup(kicker, title, rule, l1, sbar, cbub, mock).arrange(DOWN, buff=0.2)
        card.move_to([-3.3, -0.45, 0])
        body.move_to(card.get_center())

        def side(txt, y, col, h=0.62):
            return chip(txt, w=5.6, h=h, border=col, color=PALETTE["ink"], fs=15).move_to([3.4, y, 0])
        c1 = side("most still use search as their default", 1.4, PALETTE["blue"])
        c2 = side("many turn to AI chat for hard topics, step-by-step" + chr(10) + "help, brainstorming and trips", 0.5,
                  PALETTE["accent"], 0.85)
        c3 = side("search now shows AI answers at the top;" + chr(10) + "AI tools now search: the two are blending",
                  -0.45, PALETTE["good"], 0.85)
        c4 = side("younger people lead the shift", -1.3, PALETTE["blue"])
        c5 = side("people use AI, with some doubt", -2.05, PALETTE["dim"])
        take = chip("takeaway: clear, helpful information matters more than ever for being found", w=11.6, h=0.62,
                    border=PALETTE["accent"], color=PALETTE["accent"], fs=19).move_to([0, -3.1, 0])

        wait_until(self, 1.8)
        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 3.4)
        w = card.width
        card.stretch(0.01, 0)
        self.play(FadeIn(card), card.animate.stretch_to_fit_width(w), run_time=0.5)
        self.play(FadeIn(kicker), run_time=0.3)
        wait_until(self, 5.6)
        self.play(FadeIn(status, shift=LEFT * 0.1), FadeIn(tickm), run_time=0.4)
        wait_until(self, 5.9)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.5)
        grow_in(self, rule, 1.8, run_time=0.3)
        wait_until(self, 7.8)
        self.play(FadeIn(l1, shift=UP * 0.1), FadeIn(sbar, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 9.9)
        self.play(FadeIn(cbub, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 13.0)
        self.play(FadeIn(c1, shift=LEFT * 0.1), run_time=0.4)
        wait_until(self, 15.6)
        self.play(FadeIn(c2, shift=LEFT * 0.1), run_time=0.4)
        wait_until(self, 22.2)
        self.play(FadeIn(c3, shift=LEFT * 0.1), run_time=0.4)
        wait_until(self, 28.8)
        self.play(FadeIn(c4, shift=LEFT * 0.1), run_time=0.4)
        wait_until(self, 30.6)
        self.play(FadeIn(c5, shift=LEFT * 0.1), run_time=0.4)
        wait_until(self, 33.3)
        self.play(FadeIn(take, shift=UP * 0.1), FadeIn(mock), run_time=0.5)
        wait_until(self, 37.8)


class B04_PartVideos(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(2, "Video production")
        tool = chip("made with Brutalist, our video-creation tool", w=6.4, h=0.55, border=PALETTE["dim"],
                    color=PALETTE["dim"], fs=17)
        tool.move_to([-6.1 + 3.2, 1.6, 0])

        def row(label, sub, y):
            lab = VGroup(Text(label, color=PALETTE["ink"], font_size=36),
                         Text(sub, color=PALETTE["dim"], font_size=22)).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            lab.move_to([-6.1 + lab.width / 2, y, 0])
            t169 = file_tile(2.67, 1.3, "16:9").move_to([-0.7, y, 0])
            t916 = file_tile(0.9, 1.3, "9:16", fs=20).move_to([2.05, y, 0])
            k1 = tick(PALETTE["good"], 1.1).next_to(t169, RIGHT, buff=0.18)
            k2 = tick(PALETTE["good"], 1.1).next_to(t916, RIGHT, buff=0.18)
            return lab, t169, t916, k1, k2

        r1 = row("AI topic video", "based on the article", 0.4)
        r2 = row("Weekly recap", "this video", -1.35)
        count = VGroup(card_bg(3.0, 1.9, stroke_color=PALETTE["accent"]),
                       VGroup(Text("4", color=PALETTE["accent"], font_size=84, weight="BOLD"),
                              Text("video files", color=PALETTE["ink"], font_size=30)).arrange(DOWN, buff=0.05))
        count[1].move_to(count[0].get_center())
        count.move_to([4.75, -0.5, 0])
        p1 = chip("I wrote the prompt", w=3.6, h=0.6, border=PALETTE["accent"], color=PALETTE["accent"], fs=18)
        p2 = chip("I reviewed and approved the plan", w=3.9, h=0.6, border=PALETTE["accent"], color=PALETTE["accent"], fs=18)
        p3 = chip("I checked the final result", w=3.6, h=0.6, border=PALETTE["accent"], color=PALETTE["accent"], fs=18)
        steps = VGroup(p1, p2, p3).arrange(RIGHT, buff=0.25).move_to([0, -3.05, 0])
        each = Text("for each video:", color=PALETTE["dim"], font_size=18).move_to([-5.0, -2.55, 0])

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
        self.play(FadeIn(count, shift=LEFT * 0.15), run_time=0.5)
        wait_until(self, 16.3)
        self.play(FadeIn(each), FadeIn(p1, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 18.2)
        self.play(FadeIn(p2, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 20.0)
        self.play(FadeIn(p3, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 21.55)


class B05_PartMeeting(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(3, "Weekly meeting")
        cal = calendar_icon(1.25).move_to([-3.4, -0.2, 0])
        cal_l = Text("the weekly team meeting", color=PALETTE["dim"], font_size=22).move_to([-3.4, -2.35, 0])
        att = status_chip("attended")
        attk = tick(PALETTE["good"], 1.0).next_to(att, LEFT, buff=0.2)

        def purpose(txt, y):
            b = card_bg(5.8, 0.95, stroke_color=PALETTE["accent"])
            t = Text(txt, color=PALETTE["ink"], font_size=32)
            return VGroup(b, fit(t, 5.2).move_to(b.get_center())).move_to([3.3, y, 0])
        s1 = purpose("share progress", 1.1)
        s2 = purpose("stay in sync with the team", -0.1)
        s3 = purpose("plan what comes next", -1.3)

        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 2.2)
        self.play(FadeIn(cal, shift=UP * 0.15), FadeIn(cal_l), run_time=0.6)
        wait_until(self, 4.4)
        self.play(FadeIn(att, shift=LEFT * 0.1), FadeIn(attk), run_time=0.4)
        wait_until(self, 6.3)
        self.play(FadeIn(s1, shift=LEFT * 0.15), run_time=0.35)
        wait_until(self, 7.4)
        self.play(FadeIn(s2, shift=LEFT * 0.15), run_time=0.35)
        wait_until(self, 8.4)
        self.play(FadeIn(s3, shift=LEFT * 0.15), run_time=0.35)
        wait_until(self, 9.34)


class B06_PartHomesOfHope(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(4, "Homes of Hope")
        art = outreach_art(1.0).move_to([-3.6, 0.0, 0])
        cap = lines("Homes of Hope documentary outreach" + chr(10) + "(with Yatra)", 22, PALETTE["ink"], buff=0.08,
                    max_w=5.4).move_to([-3.6, -2.4, 0])

        kicker = Text("Supports marginalized girls in India with:", color=PALETTE["dim"], font_size=24)
        fit(kicker, 6.2).move_to([3.1, 2.0, 0])
        c1 = chip("a safe home", w=4.6, h=0.62, border=PALETTE["good"], fs=26)
        c2 = chip("education", w=4.6, h=0.62, border=PALETTE["good"], fs=26)
        c3 = chip("support", w=4.6, h=0.62, border=PALETTE["good"], fs=26)
        stack = VGroup(c1, c2, c3).arrange(DOWN, buff=0.15).move_to([3.1, 0.5, 0])
        mine = chip("My work with Yatra: promotion and outreach", w=6.2, h=0.8, border=PALETTE["accent"],
                    color=PALETTE["accent"], fs=21).move_to([3.1, -1.25, 0])
        goal = chip("to help the girls' stories reach a wider audience", w=6.2, h=0.8, border=PALETTE["good"],
                    color=PALETTE["good"], fs=20).move_to([3.1, -2.35, 0])
        ongoing = status_chip("ongoing", PALETTE["accent"])

        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 2.1)
        self.play(FadeIn(art, shift=UP * 0.15), FadeIn(cap), run_time=0.6)
        wait_until(self, 5.3)
        self.play(FadeIn(kicker), run_time=0.4)
        wait_until(self, 9.8)
        self.play(FadeIn(c1, shift=LEFT * 0.15), run_time=0.3)
        wait_until(self, 10.8)
        self.play(FadeIn(c2, shift=LEFT * 0.15), run_time=0.3)
        wait_until(self, 12.1)
        self.play(FadeIn(c3, shift=LEFT * 0.15), run_time=0.3)
        wait_until(self, 13.3)
        self.play(FadeIn(mine, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 15.6)
        self.play(FadeIn(goal, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 18.8)
        self.play(FadeIn(ongoing, shift=LEFT * 0.1), run_time=0.4)
        wait_until(self, 20.05)


def mini_card(role, role_color, title, detail, icon, highlight=False):
    box = card_bg(2.9, 4.4, stroke_color=PALETTE["accent"] if highlight else PALETTE["border"])
    rc = chip(role, w=2.3, h=0.46, border=role_color, color=role_color, fs=20)
    t = lines(title, 26, PALETTE["ink"], weight="BOLD", buff=0.06, max_w=2.5)
    d = lines(detail, 20, PALETTE["dim"], buff=0.05, max_w=2.5)
    inner = VGroup(rc, icon, t, d).arrange(DOWN, buff=0.25)
    fit_in(inner, 2.6, 4.0)
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
            mini_card("PUBLISHED", PALETTE["good"], "Writing", "article published", mini_article()),
            mini_card("PRODUCED", PALETTE["good"], "Video\nproduction".replace(chr(92) + "n", chr(10)), "four video files",
                      mini_videos()),
            mini_card("ATTENDED", PALETTE["good"], "Weekly\nmeeting".replace(chr(92) + "n", chr(10)), "team meeting",
                      calendar_icon(0.32)),
            mini_card("ONGOING", PALETTE["accent"], "Homes of Hope", "with Yatra", outreach_art(0.4), highlight=True),
        ]
        VGroup(*cards).arrange(RIGHT, buff=0.25).move_to([0, 0.5, 0])
        count = chip("3 parts done  ·  1 ongoing", w=9.6, h=0.85, border=PALETTE["accent"],
                     color=PALETTE["accent"], fs=34)
        count.move_to([0, -2.8, 0])

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

        k = Text("A real progress update.", color=PALETTE["dim"], font_size=30)
        l1 = Text("An article published.", color=PALETTE["ink"], font_size=44)
        l2 = Text("Videos made in two formats.", color=PALETTE["ink"], font_size=44)
        l3 = Text("A team meeting attended.", color=PALETTE["ink"], font_size=44)
        l4 = Text("Steady progress on Homes of Hope.", color=PALETTE["accent"], font_size=44)
        g = VGroup(l1, l2, l3, l4).arrange(DOWN, buff=0.34)
        VGroup(k, g).arrange(DOWN, buff=0.6).move_to(ORIGIN)

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
