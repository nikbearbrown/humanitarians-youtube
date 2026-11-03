"""
Manim scenes for weekly-recap-brand-check

A first-person, professional weekly-progress CLI-explainer. The OUTPUT beats
visualize the REAL output of weekly_recap_v1.py / weekly_recap_v2.py. Every
visual here is a generated graphic: no photos, no children, no people shapes,
no real platform logos. The article is a mock header (a plain-text kicker, no
platform mark); GitHub is a generic code-folder icon and Drive a generic
cloud-folder icon, each with a plain-text label. The Homes of Hope poster is
an abstract frame of geometric blocks with the required label and nothing
about the design itself. Built in the house Claude palette.

B01_FourPartCheck  -- typographic card: "A short, plain recap." + four numbered parts
B04_PartWriting    -- part 1: mock article header
B05_PartVideos     -- part 2: two videos x two formats = four files
B06_PartPoster     -- part 3: abstract poster, labeled, with Yatra
B07_PartSaved      -- part 4: code-folder (GitHub) and cloud-folder (Drive) icons
B10_RoleWeek       -- the four parts with role chips + the count
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


def cloud_folder_icon(s=1.0):
    def shapes(pad, col):
        c1 = Circle(radius=0.62 + pad).move_to([-0.75, -0.1, 0])
        c2 = Circle(radius=0.85 + pad).move_to([0.05, 0.28, 0])
        c3 = Circle(radius=0.62 + pad).move_to([0.85, -0.05, 0])
        base = RoundedRectangle(corner_radius=0.3, width=2.55 + 2 * pad, height=0.9 + 2 * pad).move_to([0.05, -0.37, 0])
        return VGroup(c1, c2, c3, base).set_fill(col, 1).set_stroke(width=0)
    cloud = VGroup(shapes(0.045, PALETTE["ink"]), shapes(0.0, PALETTE["warm"]))
    fb = RoundedRectangle(corner_radius=0.05, width=0.85, height=0.58, fill_color=PALETTE["card"], fill_opacity=1,
                          stroke_color=PALETTE["accent"], stroke_width=3)
    ft = RoundedRectangle(corner_radius=0.04, width=0.38, height=0.15, fill_color=PALETTE["card"], fill_opacity=1,
                          stroke_color=PALETTE["accent"], stroke_width=3).move_to(fb.get_top() + UP * 0.05 + LEFT * 0.2)
    fold = VGroup(ft, fb).move_to([0.05, 0.0, 0])
    return VGroup(cloud, fold).scale(s)


def poster_art(w=3.2, h=4.2):
    frame = RoundedRectangle(corner_radius=0.06, width=w, height=h, fill_color=PALETTE["warm"], fill_opacity=1,
                             stroke_color=PALETTE["ink"], stroke_width=3)
    sun = Circle(radius=w * 0.26, fill_color=PALETTE["accent"], fill_opacity=0.92, stroke_width=0)
    sun.move_to(frame.get_center() + UP * h * 0.2)
    bars = VGroup(
        Rectangle(width=w * 0.2, height=h * 0.2, fill_color=PALETTE["good"], fill_opacity=0.9, stroke_width=0),
        Rectangle(width=w * 0.2, height=h * 0.3, fill_color=PALETTE["wood"], fill_opacity=1, stroke_width=0),
        Rectangle(width=w * 0.2, height=h * 0.14, fill_color=PALETTE["dim"], fill_opacity=0.8, stroke_width=0),
        Rectangle(width=w * 0.2, height=h * 0.24, fill_color=PALETTE["ink"], fill_opacity=0.85, stroke_width=0),
    ).arrange(RIGHT, buff=0.0, aligned_edge=DOWN)
    bars.move_to(frame.get_center() + DOWN * h * 0.06)
    bars.align_to(frame.get_center() + DOWN * h * 0.06 + DOWN * h * 0.15, DOWN)
    t1 = RoundedRectangle(corner_radius=0.04, width=w * 0.62, height=h * 0.05, fill_color=PALETTE["ink"],
                          fill_opacity=0.9, stroke_width=0)
    t2 = RoundedRectangle(corner_radius=0.03, width=w * 0.4, height=h * 0.03, fill_color=PALETTE["dim"],
                          fill_opacity=0.7, stroke_width=0)
    txt = VGroup(t1, t2).arrange(DOWN, buff=h * 0.03, aligned_edge=LEFT)
    txt.move_to(frame.get_bottom() + UP * h * 0.14)
    return VGroup(frame, sun, bars, txt)


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

        labels = ["Writing", "Video production", "Homes of Hope documentary", "Organizing the work"]
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
        wait_until(self, 5.95)


class B04_PartWriting(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(1, "Writing")
        status = status_chip("published")
        tickm = tick(PALETTE["good"], 1.0).next_to(status, LEFT, buff=0.2)

        card = card_bg(11.6, 4.5, stroke_color=PALETTE["border"]).move_to([0, -0.55, 0])
        kicker = Text("SUBSTACK  ·  ARTICLE", color=PALETTE["accent"], font_size=22)
        title = lines("Have You Asked the Chatbot\nAbout Your Brand Lately?", 46, PALETTE["ink"], weight="BOLD",
                      buff=0.12, max_w=10.4)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        l1 = Text("Chatbots have become a first impression for brands.", color=PALETTE["ink"], font_size=28)
        l2 = Text("A five-minute check can catch wrong or outdated information.", color=PALETTE["ink"], font_size=28)
        fit(l1, 10.4)
        fit(l2, 10.4)
        body = VGroup(kicker, title, rule, l1, l2).arrange(DOWN, buff=0.3).move_to(card.get_center())
        mock = Text("mock article header", color=PALETTE["dim"], font_size=18).move_to([0, -3.1, 0])

        wait_until(self, 1.8)
        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 3.6)
        w = card.width
        card.stretch(0.01, 0)
        self.play(FadeIn(card), card.animate.stretch_to_fit_width(w), run_time=0.5)
        self.play(FadeIn(kicker), run_time=0.3)
        wait_until(self, 5.9)
        self.play(FadeIn(status, shift=LEFT * 0.1), FadeIn(tickm), run_time=0.4)
        wait_until(self, 6.9)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.5)
        grow_in(self, rule, 1.8, run_time=0.3)
        wait_until(self, 9.8)
        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 13.2)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(mock), run_time=0.3)
        wait_until(self, 17.15)


class B05_PartVideos(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(2, "Video production")

        stages = ["planning", "review", "approvals", "export"]
        chips = [chip(s, w=2.5, h=0.62, border=PALETTE["accent"], color=PALETTE["ink"], fs=26) for s in stages]
        strip = VGroup(*chips).arrange(RIGHT, buff=0.45).move_to([0, 1.4, 0])
        arrows = VGroup(*[Arrow(chips[i].get_right(), chips[i + 1].get_left(), buff=0.05, color=PALETTE["dim"],
                                stroke_width=3, max_tip_length_to_length_ratio=0.5) for i in range(3)])

        def row(label, y):
            lab = Text(label, color=PALETTE["ink"], font_size=36)
            lab.move_to([-6.1 + lab.width / 2, y, 0])
            t169 = file_tile(2.67, 1.5, "16:9").move_to([-0.7, y, 0])
            t916 = file_tile(0.9, 1.5, "9:16", fs=20).move_to([2.05, y, 0])
            k1 = tick(PALETTE["good"], 1.1).next_to(t169, RIGHT, buff=0.18)
            k1.shift(RIGHT * 0.0)
            k2 = tick(PALETTE["good"], 1.1).next_to(t916, RIGHT, buff=0.18)
            return lab, t169, t916, k1, k2

        r1 = row("AI topic video", -0.1)
        r2 = row("Weekly recap", -2.0)
        count = VGroup(card_bg(3.0, 1.9, stroke_color=PALETTE["accent"]),
                       VGroup(Text("4", color=PALETTE["accent"], font_size=84, weight="BOLD"),
                              Text("video files", color=PALETTE["ink"], font_size=30)).arrange(DOWN, buff=0.05))
        count[1].move_to(count[0].get_center())
        count.move_to([4.75, -1.05, 0])

        wait_until(self, 0.2)
        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 4.3)
        self.play(FadeIn(r1[0], shift=RIGHT * 0.2), run_time=0.4)
        wait_until(self, 6.0)
        self.play(FadeIn(r2[0], shift=RIGHT * 0.2), run_time=0.4)
        wait_until(self, 8.2)
        self.play(FadeIn(chips[0]), run_time=0.3)
        for i, t in enumerate([10.2, 11.0, 11.8]):
            wait_until(self, t)
            self.play(FadeIn(arrows[i]), FadeIn(chips[i + 1]), run_time=0.3)
        wait_until(self, 12.9)
        self.play(FadeIn(r1[1]), FadeIn(r2[1]), run_time=0.4)
        self.play(FadeIn(r1[3]), FadeIn(r2[3]), run_time=0.25)
        wait_until(self, 14.3)
        self.play(FadeIn(r1[2]), FadeIn(r2[2]), run_time=0.4)
        self.play(FadeIn(r1[4]), FadeIn(r2[4]), run_time=0.25)
        wait_until(self, 16.0)
        self.play(FadeIn(count, shift=LEFT * 0.15), run_time=0.5)
        wait_until(self, 17.35)


class B06_PartPoster(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(3, "Homes of Hope documentary")
        poster = poster_art(3.1, 4.0).move_to([-3.6, -0.15, 0])
        cap = lines("Poster design for the Homes of Hope\ndocumentary (with Yatra)", 22, PALETTE["ink"], buff=0.08,
                    max_w=5.2).move_to([-3.6, -2.85, 0])

        kicker = Text("Supports marginalized girls in India with:", color=PALETTE["dim"], font_size=26)
        kicker.move_to([2.95, 2.0, 0])
        fit(kicker, 6.2)
        c1 = chip("a safe home", w=4.6, h=0.8, border=PALETTE["good"], color=PALETTE["ink"], fs=34)
        c2 = chip("education", w=4.6, h=0.8, border=PALETTE["good"], color=PALETTE["ink"], fs=34)
        c3 = chip("support", w=4.6, h=0.8, border=PALETTE["good"], color=PALETTE["ink"], fs=34)
        stack = VGroup(c1, c2, c3).arrange(DOWN, buff=0.25).move_to([2.95, 0.15, 0])
        helped = chip("My part: I helped Yatra with the poster", w=6.2, h=0.9, border=PALETTE["accent"],
                      color=PALETTE["accent"], fs=26)
        helped.move_to([2.95, -2.3, 0])

        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 3.0)
        self.play(FadeIn(poster, shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(kicker), run_time=0.4)
        wait_until(self, 7.6)
        self.play(FadeIn(c1, shift=LEFT * 0.15), run_time=0.35)
        wait_until(self, 8.6)
        self.play(FadeIn(c2, shift=LEFT * 0.15), run_time=0.3)
        wait_until(self, 9.05)
        self.play(FadeIn(c3, shift=LEFT * 0.15), run_time=0.3)
        wait_until(self, 10.0)
        self.play(FadeIn(cap), run_time=0.4)
        self.play(FadeIn(helped, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 12.0)


class B07_PartSaved(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(4, "Organizing the work")

        gh = code_folder_icon(0.95).move_to([-3.4, 0.8, 0])
        dr = cloud_folder_icon(0.95).move_to([3.4, 0.8, 0])
        gl = Text("GitHub", color=PALETTE["ink"], font_size=44, weight="BOLD").move_to([-3.4, -0.65, 0])
        dl = Text("Drive", color=PALETTE["ink"], font_size=44, weight="BOLD").move_to([3.4, -0.65, 0])
        gs = Text("the AI videos' files", color=PALETTE["dim"], font_size=28).move_to([-3.4, -1.3, 0])
        ds = Text("the week's videos", color=PALETTE["dim"], font_size=28).move_to([3.4, -1.3, 0])
        gc = chip("pushed", w=2.4, h=0.62, border=PALETTE["good"], color=PALETTE["good"], fs=26).move_to([-3.4, -2.0, 0])
        dc = chip("attached", w=2.4, h=0.62, border=PALETTE["good"], color=PALETTE["good"], fs=26).move_to([3.4, -2.0, 0])
        gk = tick(PALETTE["good"], 1.0).next_to(gc, LEFT, buff=0.18)
        dk = tick(PALETTE["good"], 1.0).next_to(dc, LEFT, buff=0.18)
        foot = chip("everything saved and shareable", w=7.6, h=0.75, border=PALETTE["accent"],
                    color=PALETTE["accent"], fs=30).move_to([0, -2.95, 0])

        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 2.6)
        self.play(FadeIn(gh, shift=UP * 0.15), FadeIn(gl), FadeIn(gs), run_time=0.5)
        wait_until(self, 5.0)
        self.play(FadeIn(gc), FadeIn(gk), run_time=0.3)
        wait_until(self, 5.8)
        self.play(FadeIn(dr, shift=UP * 0.15), FadeIn(dl), FadeIn(ds), run_time=0.5)
        wait_until(self, 7.8)
        self.play(FadeIn(dc), FadeIn(dk), run_time=0.3)
        wait_until(self, 8.4)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 10.35)


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


class B10_RoleWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        cards = [
            mini_card("AUTHOR", PALETTE["good"], "Writing", "article published", mini_article()),
            mini_card("PRODUCER", PALETTE["good"], "Video\nproduction", "four video files", mini_videos()),
            mini_card("SUPPORT", PALETTE["accent"], "Homes of Hope\ndocumentary", "poster design,\nwith Yatra",
                      poster_art(0.95, 1.2), highlight=True),
            mini_card("ORGANIZER", PALETTE["good"], "Organizing\nthe work", "GitHub and Drive",
                      VGroup(code_folder_icon(0.3), cloud_folder_icon(0.3)).arrange(RIGHT, buff=0.2)),
        ]
        VGroup(*cards).arrange(RIGHT, buff=0.25).move_to([0, 0.5, 0])
        count = chip("4 parts done  ·  1 in a supporting role", w=9.6, h=0.85, border=PALETTE["accent"],
                     color=PALETTE["accent"], fs=34)
        count.move_to([0, -2.8, 0])

        wait_until(self, 2.2)
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.15), run_time=0.35)
        wait_until(self, 7.4)
        self.play(Indicate(cards[2][0], color=PALETTE["accent"], scale_factor=1.03), run_time=0.8)
        wait_until(self, 9.9)
        self.play(FadeIn(count, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 11.45)


class B11_TheLesson(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        k = Text("A real progress update.", color=PALETTE["dim"], font_size=30)
        l1 = Text("Done is done.", color=PALETTE["ink"], font_size=52)
        l2 = Text("Helping is helping.", color=PALETTE["ink"], font_size=52)
        l3 = Text("Said plainly.", color=PALETTE["accent"], font_size=52)
        g = VGroup(l1, l2, l3).arrange(DOWN, buff=0.4)
        VGroup(k, g).arrange(DOWN, buff=0.7).move_to(ORIGIN)

        self.play(FadeIn(k, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 1.5)
        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 2.3)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 3.1)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 3.72)
