"""
Manim scenes for weekly-recap-foundation-search

A first-person, professional weekly-progress CLI-explainer. The OUTPUT beats
visualize the REAL output of weekly_recap_v1.py / weekly_recap_v2.py. Every
visual here is a generated graphic: no photos, no children, no people shapes,
no real platform logos. The article is a mock header (a plain-text kicker, no
platform mark); GitHub is a generic code-folder icon with a plain-text label.
The Homes of Hope outreach is an abstract graphic (connected dots around a
megaphone) with the required label and nothing about the outreach itself beyond
"ongoing". Built in the house Claude palette.

B01_FourPartCheck  -- typographic card: "A short, plain recap." + four numbered parts
B04_PartWriting    -- part 1: mock article header
B05_PartVideos     -- part 2: two videos x two formats = four files
B06_PartOutreach   -- part 3: abstract outreach graphic, labeled, with Yatra; ongoing
B07_PartSaved      -- part 4: code-folder (GitHub) icon + saved / organized / easy to find
B10_StatusWeek     -- the four parts with status chips + the count
B11_TheLesson      -- closing typographic beat
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
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    if mob.height > max_h:
        mob.scale_to_fit_height(max_h)
    return mob


def lines(txt, fs, color, max_w=None, buff=0.12, weight=None):
    kw = {"weight": weight} if weight else {}
    g = VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split("\n")]).arrange(DOWN, buff=buff)
    return fit(g, max_w) if max_w else g


def wait_until(scene, t):
    d = t - scene.renderer.time
    if d > 0.02:
        scene.wait(d)


def chip(label, w=2.6, h=0.6, border=None, color=None, fs=16):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(Text(label, color=color or PALETTE["ink"], font_size=fs), w - 0.3)
    return VGroup(box, txt.move_to(box.get_center()))


def tick(color=None, s=1.0, sw=5):
    t = VMobject(color=color or PALETTE["good"], stroke_width=sw)
    t.set_points_as_corners([[-0.1, 0.0, 0], [-0.02, -0.1, 0], [0.13, 0.12, 0]])
    return t.scale(s)


def header(n, name, color=None):
    kick = Text("PART %d OF 4" % n, color=PALETTE["accent"], font_size=24)
    head = fit(Text(name, color=PALETTE["ink"], font_size=50, weight="BOLD"), 8.2)
    g = VGroup(kick, head).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
    g.move_to(ORIGIN).to_corner(UL, buff=0.0)
    g.move_to([-6.1 + g.width / 2, 3.2 - g.height / 2, 0])
    return g


def status_chip(label, color=None):
    c = color or PALETTE["good"]
    ch = chip(label, w=2.5, h=0.62, border=c, color=c, fs=24)
    ch.move_to([6.1 - ch.width / 2, 2.88, 0])
    return ch


# --- icons ------------------------------------------------------------------

def code_folder_icon(s=1.0):
    body = RoundedRectangle(corner_radius=0.1, width=2.4, height=1.7, fill_color=PALETTE["warm"], fill_opacity=1,
                            stroke_color=PALETTE["ink"], stroke_width=3)
    tab = RoundedRectangle(corner_radius=0.08, width=0.95, height=0.34, fill_color=PALETTE["warm"], fill_opacity=1,
                           stroke_color=PALETTE["ink"], stroke_width=3)
    tab.move_to(body.get_top() + UP * 0.12 + LEFT * 0.7)
    body.set_z_index(1)
    glyph = Text("</>", color=PALETTE["accent"], font_size=44, weight="BOLD").move_to(body.get_center())
    glyph.set_z_index(2)
    return VGroup(tab, body, glyph).scale(s)


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
    mega.scale(1.0)
    return VGroup(spokes, ring, nodes, mega).scale(s)


def file_tile(w, h, label, fs=22):
    box = RoundedRectangle(corner_radius=0.08, width=w, height=h, fill_color=PALETTE["card"], fill_opacity=1,
                           stroke_color=PALETTE["good"], stroke_width=3)
    t = fit(Text(label, color=PALETTE["ink"], font_size=fs, weight="BOLD"), w - 0.2).move_to(box.get_center())
    return VGroup(box, t)


# --- scenes -----------------------------------------------------------------

class B01_FourPartCheck(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        phrase = Text("A short, plain recap.", color=PALETTE["ink"], font_size=54)
        rule = Line(LEFT * 1.1, RIGHT * 1.1, color=PALETTE["accent"], stroke_width=3)
        top = VGroup(phrase, rule).arrange(DOWN, buff=0.3).move_to([0, 2.3, 0])

        labels = ["Writing", "Video production", "Homes of Hope outreach", "Organizing the work"]
        rows = []
        for i, lab in enumerate(labels):
            num = VGroup(Circle(radius=0.3, color=PALETTE["accent"], fill_color=PALETTE["accent"], fill_opacity=1,
                                stroke_width=0),
                         Text(str(i + 1), color=PALETTE["card"], font_size=30, weight="BOLD"))
            num[1].move_to(num[0].get_center())
            t = Text(lab, color=PALETTE["ink"], font_size=38)
            rows.append(VGroup(num, t).arrange(RIGHT, buff=0.45))
        stack = VGroup(*rows).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to([0, -0.55, 0])
        for r in rows:
            r.shift(RIGHT * (-r.get_left()[0] - 3.4))

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 2.2, run_time=0.4)
        for r, t in zip(rows, [3.0, 3.9, 4.6, 5.2]):
            wait_until(self, t)
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.4)
        wait_until(self, 5.99)


class B04_PartWriting(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(1, "Writing")
        status = status_chip("published")
        tickm = tick(PALETTE["good"], 1.0).next_to(status, LEFT, buff=0.2)

        card = card_bg(11.6, 4.5, stroke_color=PALETTE["border"]).move_to([0, -0.55, 0])
        kicker = Text("SUBSTACK  ·  ARTICLE", color=PALETTE["accent"], font_size=22)
        title = lines("Your Foundation Search\nIs Doing Market Research", 46, PALETTE["ink"], weight="BOLD",
                      buff=0.12, max_w=10.4)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        l1 = Text("Late-night shade testing and virtual try-on tools", color=PALETTE["ink"], font_size=28)
        l2 = Text("give beauty brands useful clues about what to make next.", color=PALETTE["ink"], font_size=28)
        fit(l1, 10.4)
        fit(l2, 10.4)
        body = VGroup(kicker, title, rule, l1, l2).arrange(DOWN, buff=0.3).move_to(card.get_center())
        mock = Text("mock article header", color=PALETTE["dim"], font_size=18).move_to([0, -3.1, 0])

        wait_until(self, 1.9)
        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 3.6)
        w = card.width
        card.stretch(0.01, 0)
        self.play(FadeIn(card), card.animate.stretch_to_fit_width(w), run_time=0.5)
        self.play(FadeIn(kicker), run_time=0.3)
        wait_until(self, 5.9)
        self.play(FadeIn(status, shift=LEFT * 0.1), FadeIn(tickm), run_time=0.4)
        wait_until(self, 6.6)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.5)
        grow_in(self, rule, 1.8, run_time=0.3)
        wait_until(self, 9.9)
        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 13.0)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(mock), run_time=0.3)
        wait_until(self, 16.95)


class B05_PartVideos(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(2, "Video production")

        def row(label, sub, y):
            lab = VGroup(Text(label, color=PALETTE["ink"], font_size=36),
                         Text(sub, color=PALETTE["dim"], font_size=22)).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            lab.move_to([-6.1 + lab.width / 2, y, 0])
            t169 = file_tile(2.67, 1.5, "16:9").move_to([-0.7, y, 0])
            t916 = file_tile(0.9, 1.5, "9:16", fs=20).move_to([2.05, y, 0])
            k1 = tick(PALETTE["good"], 1.1).next_to(t169, RIGHT, buff=0.18)
            k2 = tick(PALETTE["good"], 1.1).next_to(t916, RIGHT, buff=0.18)
            return lab, t169, t916, k1, k2

        r1 = row("AI topic video", "based on the article", 0.9)
        r2 = row("Weekly recap", "this video", -1.4)
        count = VGroup(card_bg(3.0, 1.9, stroke_color=PALETTE["accent"]),
                       VGroup(Text("4", color=PALETTE["accent"], font_size=84, weight="BOLD"),
                              Text("video files", color=PALETTE["ink"], font_size=30)).arrange(DOWN, buff=0.05))
        count[1].move_to(count[0].get_center())
        count.move_to([4.75, -0.25, 0])

        wait_until(self, 0.2)
        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 7.4)
        self.play(FadeIn(r1[0], shift=RIGHT * 0.2), run_time=0.4)
        wait_until(self, 9.4)
        self.play(FadeIn(r2[0], shift=RIGHT * 0.2), run_time=0.4)
        wait_until(self, 11.0)
        self.play(FadeIn(r1[1]), FadeIn(r2[1]), run_time=0.4)
        self.play(FadeIn(r1[3]), FadeIn(r2[3]), run_time=0.25)
        wait_until(self, 12.0)
        self.play(FadeIn(r1[2]), FadeIn(r2[2]), run_time=0.4)
        self.play(FadeIn(r1[4]), FadeIn(r2[4]), run_time=0.25)
        wait_until(self, 13.5)
        self.play(FadeIn(count, shift=LEFT * 0.15), run_time=0.5)
        wait_until(self, 14.9)


class B06_PartOutreach(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(3, "Homes of Hope outreach")
        art = outreach_art(1.05).move_to([-3.6, -0.05, 0])
        cap = lines("Homes of Hope documentary outreach\n(with Yatra)", 22, PALETTE["ink"], buff=0.08,
                    max_w=5.4).move_to([-3.6, -2.45, 0])

        kicker = Text("Supports marginalized girls in India with:", color=PALETTE["dim"], font_size=26)
        kicker.move_to([2.95, 1.7, 0])
        fit(kicker, 6.2)
        c1 = chip("a safe home", w=4.6, h=0.8, border=PALETTE["good"], color=PALETTE["ink"], fs=34)
        c2 = chip("education", w=4.6, h=0.8, border=PALETTE["good"], color=PALETTE["ink"], fs=34)
        c3 = chip("support", w=4.6, h=0.8, border=PALETTE["good"], color=PALETTE["ink"], fs=34)
        stack = VGroup(c1, c2, c3).arrange(DOWN, buff=0.25).move_to([2.95, 0.0, 0])
        goal = lines("Goal: help the girls' stories\nreach a wider audience", 24, PALETTE["accent"], buff=0.08)
        goal_chip = VGroup(card_bg(6.2, 1.1, stroke_color=PALETTE["accent"]), goal)
        goal.move_to(goal_chip[0].get_center())
        goal_chip.move_to([2.95, -2.3, 0])
        ongoing = status_chip("ongoing", PALETTE["accent"])

        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 3.0)
        self.play(FadeIn(kicker), run_time=0.4)
        wait_until(self, 7.6)
        self.play(FadeIn(c1, shift=LEFT * 0.15), run_time=0.35)
        wait_until(self, 8.7)
        self.play(FadeIn(c2, shift=LEFT * 0.15), run_time=0.3)
        wait_until(self, 10.1)
        self.play(FadeIn(c3, shift=LEFT * 0.15), run_time=0.3)
        wait_until(self, 11.5)
        self.play(FadeIn(art, shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(cap), run_time=0.4)
        wait_until(self, 13.5)
        self.play(FadeIn(goal_chip, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 16.7)
        self.play(FadeIn(ongoing, shift=LEFT * 0.1), run_time=0.4)
        wait_until(self, 18.0)


class B07_PartSaved(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(4, "Organizing the work")

        gh = code_folder_icon(1.15).move_to([0, 0.7, 0])
        gl = Text("GitHub", color=PALETTE["ink"], font_size=48, weight="BOLD").move_to([0, -0.8, 0])
        gs = Text("all of my project files", color=PALETTE["dim"], font_size=30).move_to([0, -1.4, 0])
        gc = chip("pushed", w=2.4, h=0.62, border=PALETTE["good"], color=PALETTE["good"], fs=26).move_to([0.25, -2.05, 0])
        gk = tick(PALETTE["good"], 1.0).next_to(gc, LEFT, buff=0.18)
        c1 = chip("saved", w=2.4, h=0.7, border=PALETTE["accent"], color=PALETTE["accent"], fs=28)
        c2 = chip("organized", w=2.8, h=0.7, border=PALETTE["accent"], color=PALETTE["accent"], fs=28)
        c3 = chip("easy to find", w=3.2, h=0.7, border=PALETTE["accent"], color=PALETTE["accent"], fs=28)
        foot = VGroup(c1, c2, c3).arrange(RIGHT, buff=0.3).move_to([0, -3.0, 0])

        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 2.6)
        self.play(FadeIn(gh, shift=UP * 0.15), FadeIn(gl), FadeIn(gs), run_time=0.5)
        wait_until(self, 4.6)
        self.play(FadeIn(gc), FadeIn(gk), run_time=0.3)
        wait_until(self, 5.1)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.3)
        wait_until(self, 6.8)
        self.play(FadeIn(c2, shift=UP * 0.1), run_time=0.3)
        wait_until(self, 7.8)
        self.play(FadeIn(c3, shift=UP * 0.1), run_time=0.3)
        wait_until(self, 8.6)


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


class B10_StatusWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        cards = [
            mini_card("PUBLISHED", PALETTE["good"], "Writing", "article published", mini_article()),
            mini_card("PRODUCED", PALETTE["good"], "Video\nproduction", "four video files", mini_videos()),
            mini_card("ONGOING", PALETTE["accent"], "Homes of Hope\noutreach", "with Yatra",
                      outreach_art(0.4), highlight=True),
            mini_card("SAVED", PALETTE["good"], "Organizing\nthe work", "all files on GitHub", code_folder_icon(0.45)),
        ]
        VGroup(*cards).arrange(RIGHT, buff=0.25).move_to([0, 0.5, 0])
        count = chip("3 parts done  ·  1 ongoing", w=9.6, h=0.85, border=PALETTE["accent"],
                     color=PALETTE["accent"], fs=34)
        count.move_to([0, -2.8, 0])

        wait_until(self, 2.5)
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.15), run_time=0.35)
        wait_until(self, 5.9)
        self.play(FadeIn(count, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 7.9)
        self.play(Indicate(cards[2][0], color=PALETTE["accent"], scale_factor=1.03), run_time=0.8)
        wait_until(self, 10.0)


class B11_TheLesson(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        k = Text("A real progress update.", color=PALETTE["dim"], font_size=30)
        l1 = Text("Done is done.", color=PALETTE["ink"], font_size=52)
        l2 = Text("Ongoing is ongoing.", color=PALETTE["accent"], font_size=52)
        g = VGroup(l1, l2).arrange(DOWN, buff=0.4)
        VGroup(k, g).arrange(DOWN, buff=0.7).move_to(ORIGIN)

        self.play(FadeIn(k, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 1.8)
        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 2.7)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 3.98)
