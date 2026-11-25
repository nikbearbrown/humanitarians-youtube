"""
Manim scenes for weekly-recap-real-art

A first-person, professional weekly-progress CLI-explainer. The OUTPUT beats
visualize the REAL output of weekly_recap_v1.py / weekly_recap_v2.py. Every
visual here is a generated graphic: no photos of animals, shelters or people, no
real platform logos. The article is a mock header (a plain-text kicker, no
platform mark); GitHub is a generic code-folder icon with a plain-text label.
The CatBot and DogBot section is an EARLY-STAGE PLAN and is labeled so on screen:
an illustrated cat and dog, quick notes turning into a bio and posts, a person
approving everything, a camera icon for volunteer photo days, and a generic map
panel with one pin each for Minnesota and the Boston area. It never says the demo
is built and never says any shelter has agreed. Built in the house Claude palette.

B01_FourPartCheck    -- typographic card: "A short, plain recap." + four numbered parts
B04_PartWriting      -- part 1: mock article header
B05_PartVideos       -- part 2: two videos x two formats = four files
B06_PartSaved        -- part 3: code-folder (GitHub) icon + saved / easy to share
B07_PartNewProject   -- part 4: CatBot and DogBot, the plan and the first step
B08_PartNextSteps    -- part 4: what comes next, planned (map with one pin each)
B11_StatusWeek       -- the four parts with status chips + the count
B12_TheLesson        -- closing typographic beat
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
    g.move_to(ORIGIN).to_corner(UL, buff=0.0)
    g.move_to([-6.1 + g.width / 2, 3.2 - g.height / 2, 0])
    return g


def status_chip(label, color=None, w=2.5):
    c = color or PALETTE["good"]
    ch = chip(label, w=w, h=0.62, border=c, color=c, fs=24)
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


def cat_icon(s=1.0):
    """A friendly illustrated cat face (generic cartoon, not a real animal)."""
    head = Circle(radius=0.5, fill_color="#E8B07A", fill_opacity=1, stroke_color=PALETTE["ink"], stroke_width=3)
    ear_l = Polygon([-0.48, 0.18, 0], [-0.4, 0.68, 0], [-0.06, 0.42, 0], fill_color="#E8B07A", fill_opacity=1,
                    stroke_color=PALETTE["ink"], stroke_width=3)
    ear_r = Polygon([0.48, 0.18, 0], [0.4, 0.68, 0], [0.06, 0.42, 0], fill_color="#E8B07A", fill_opacity=1,
                    stroke_color=PALETTE["ink"], stroke_width=3)
    eyes = VGroup(Dot([-0.18, 0.08, 0], radius=0.05, color=PALETTE["ink"]), Dot([0.18, 0.08, 0], radius=0.05,
                                                                                  color=PALETTE["ink"]))
    nose = Triangle(fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0).scale(0.06).rotate(PI).move_to(
        [0, -0.04, 0])
    mouth = Arc(radius=0.12, start_angle=PI * 1.15, angle=PI * 0.7, color=PALETTE["ink"], stroke_width=2.5).move_to(
        [0, -0.16, 0])
    whisk = VGroup(*[Line([sx * 0.18, -0.1 + dy, 0], [sx * 0.62, -0.1 + dy * 2.2, 0], color=PALETTE["ink"],
                          stroke_width=1.8) for sx in (-1, 1) for dy in (0.04, -0.06)])
    ear_l.set_z_index(0)
    ear_r.set_z_index(0)
    head.set_z_index(1)
    return VGroup(ear_l, ear_r, head, eyes, nose, mouth, whisk).scale(s)


def dog_icon(s=1.0):
    """A friendly illustrated dog face (generic cartoon, not a real animal)."""
    head = Circle(radius=0.5, fill_color="#D8B07A", fill_opacity=1, stroke_color=PALETTE["ink"], stroke_width=3)
    ear_l = Ellipse(width=0.34, height=0.66, fill_color="#9A6A3C", fill_opacity=1, stroke_color=PALETTE["ink"],
                    stroke_width=3).move_to([-0.5, 0.05, 0]).rotate(0.2)
    ear_r = Ellipse(width=0.34, height=0.66, fill_color="#9A6A3C", fill_opacity=1, stroke_color=PALETTE["ink"],
                    stroke_width=3).move_to([0.5, 0.05, 0]).rotate(-0.2)
    eyes = VGroup(Dot([-0.18, 0.1, 0], radius=0.05, color=PALETTE["ink"]), Dot([0.18, 0.1, 0], radius=0.05,
                                                                                  color=PALETTE["ink"]))
    muzzle = Ellipse(width=0.42, height=0.3, fill_color="#F3E3C8", fill_opacity=1, stroke_width=0).move_to([0, -0.14, 0])
    nose = Ellipse(width=0.16, height=0.1, fill_color=PALETTE["ink"], fill_opacity=1, stroke_width=0).move_to(
        [0, -0.06, 0])
    mouth = Arc(radius=0.1, start_angle=PI * 1.15, angle=PI * 0.7, color=PALETTE["ink"], stroke_width=2.5).move_to(
        [0, -0.22, 0])
    ear_l.set_z_index(2)
    ear_r.set_z_index(2)
    head.set_z_index(1)
    muzzle.set_z_index(3)
    nose.set_z_index(4)
    return VGroup(head, ear_l, ear_r, eyes, muzzle, nose, mouth).scale(s)


def camera_icon(s=1.0):
    body = RoundedRectangle(corner_radius=0.1, width=1.0, height=0.7, fill_color=PALETTE["card"], fill_opacity=1,
                            stroke_color=PALETTE["ink"], stroke_width=3)
    bump = RoundedRectangle(corner_radius=0.05, width=0.36, height=0.14, fill_color=PALETTE["card"], fill_opacity=1,
                            stroke_color=PALETTE["ink"], stroke_width=3).next_to(body, UP, buff=-0.02).shift(LEFT * 0.2)
    lens = Circle(radius=0.2, fill_color=PALETTE["bg"], fill_opacity=1, stroke_color=PALETTE["accent"], stroke_width=3)
    dot = Dot(lens.get_center(), radius=0.06, color=PALETTE["accent"])
    return VGroup(bump, body, lens, dot).scale(s)


def pin(s=1.0, color=None):
    c = color or PALETTE["accent"]
    head = Circle(radius=0.17, fill_color=c, fill_opacity=1, stroke_color=PALETTE["ink"], stroke_width=2)
    tipp = Polygon([-0.12, -0.1, 0], [0.12, -0.1, 0], [0, -0.38, 0], fill_color=c, fill_opacity=1,
                   stroke_color=PALETTE["ink"], stroke_width=2)
    dot = Dot(head.get_center(), radius=0.05, color=PALETTE["card"])
    head.set_z_index(2)
    dot.set_z_index(3)
    return VGroup(tipp, head, dot).scale(s)


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

        labels = ["Writing", "Video production", "Organizing the work", "A new project"]
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
        title = Text("Real Art, New Light", color=PALETTE["ink"], font_size=60, weight="BOLD")
        fit(title, 10.4)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        l1 = Text("How AI can be used to promote real artwork,", color=PALETTE["ink"], font_size=30)
        l2 = Text("while keeping the original at the center.", color=PALETTE["ink"], font_size=30)
        fit(l1, 10.4)
        fit(l2, 10.4)
        body = VGroup(kicker, title, rule, l1, l2).arrange(DOWN, buff=0.34).move_to(card.get_center())
        mock = Text("mock article header", color=PALETTE["dim"], font_size=18).move_to([0, -3.1, 0])

        wait_until(self, 1.9)
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
        wait_until(self, 7.7)
        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 10.9)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(mock), run_time=0.3)
        wait_until(self, 12.77)


class B05_PartVideos(Scene):
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
            t169 = file_tile(2.67, 1.5, "16:9").move_to([-0.7, y, 0])
            t916 = file_tile(0.9, 1.5, "9:16", fs=20).move_to([2.05, y, 0])
            k1 = tick(PALETTE["good"], 1.1).next_to(t169, RIGHT, buff=0.18)
            k2 = tick(PALETTE["good"], 1.1).next_to(t916, RIGHT, buff=0.18)
            return lab, t169, t916, k1, k2

        r1 = row("AI topic video", "based on the article", 0.2)
        r2 = row("Weekly recap", "this video", -1.95)
        count = VGroup(card_bg(3.0, 1.9, stroke_color=PALETTE["accent"]),
                       VGroup(Text("4", color=PALETTE["accent"], font_size=84, weight="BOLD"),
                              Text("video files", color=PALETTE["ink"], font_size=30)).arrange(DOWN, buff=0.05))
        count[1].move_to(count[0].get_center())
        count.move_to([4.75, -0.85, 0])

        wait_until(self, 0.2)
        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 4.8)
        self.play(FadeIn(tool, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(count, shift=LEFT * 0.15), run_time=0.5)
        wait_until(self, 8.1)
        self.play(FadeIn(r1[0], shift=RIGHT * 0.2), run_time=0.4)
        wait_until(self, 10.8)
        self.play(FadeIn(r2[0], shift=RIGHT * 0.2), run_time=0.4)
        wait_until(self, 13.2)
        self.play(FadeIn(r1[1]), FadeIn(r2[1]), run_time=0.4)
        self.play(FadeIn(r1[3]), FadeIn(r2[3]), run_time=0.25)
        wait_until(self, 14.7)
        self.play(FadeIn(r1[2]), FadeIn(r2[2]), run_time=0.4)
        self.play(FadeIn(r1[4]), FadeIn(r2[4]), run_time=0.25)
        wait_until(self, 16.2)


class B06_PartSaved(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(3, "Organizing the work")

        gh = code_folder_icon(1.15).move_to([0, 0.7, 0])
        gl = Text("GitHub", color=PALETTE["ink"], font_size=48, weight="BOLD").move_to([0, -0.8, 0])
        gs = Text("my files", color=PALETTE["dim"], font_size=30).move_to([0, -1.4, 0])
        gc = chip("pushed", w=2.4, h=0.62, border=PALETTE["good"], color=PALETTE["good"], fs=26).move_to([0.25, -2.05, 0])
        gk = tick(PALETTE["good"], 1.0).next_to(gc, LEFT, buff=0.18)
        c1 = chip("saved", w=2.4, h=0.7, border=PALETTE["accent"], color=PALETTE["accent"], fs=28)
        c2 = chip("easy to share", w=3.4, h=0.7, border=PALETTE["accent"], color=PALETTE["accent"], fs=28)
        foot = VGroup(c1, c2).arrange(RIGHT, buff=0.3).move_to([0, -3.0, 0])

        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 2.4)
        self.play(FadeIn(gh, shift=UP * 0.15), FadeIn(gl), FadeIn(gs), run_time=0.5)
        wait_until(self, 3.4)
        self.play(FadeIn(gc), FadeIn(gk), run_time=0.3)
        wait_until(self, 4.2)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.3)
        wait_until(self, 5.2)
        self.play(FadeIn(c2, shift=UP * 0.1), run_time=0.3)
        wait_until(self, 6.37)


class B07_PartNewProject(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(4, "A new project")
        plan = status_chip("Early-stage plan", PALETTE["accent"], w=3.6)

        # top row: CatBot + DogBot, and the listing -> marketing idea
        cat = cat_icon(1.2).move_to([-5.0, 1.0, 0])
        dog = dog_icon(1.2).move_to([-2.9, 1.0, 0])
        cl = Text("CatBot", color=PALETTE["ink"], font_size=24, weight="BOLD").move_to([-5.0, 0.2, 0])
        dl = Text("DogBot", color=PALETTE["ink"], font_size=24, weight="BOLD").move_to([-2.9, 0.2, 0])
        plus = Text("+", color=PALETTE["dim"], font_size=36).move_to([-3.95, 1.0, 0])
        listing = chip("each animal's\nlisting", w=2.3, h=0.95, border=PALETTE["border"], fs=20).move_to([0.0, 1.0, 0])
        a1 = Arrow([1.2, 1.0, 0], [1.9, 1.0, 0], buff=0, color=PALETTE["accent"], stroke_width=5,
                   max_tip_length_to_length_ratio=0.8)
        market = chip("marketing that helps\nthem get adopted", w=3.4, h=0.95, border=PALETTE["good"],
                      color=PALETTE["good"], fs=20).move_to([3.9, 1.0, 0])
        for_s = Text("for cat and dog shelters", color=PALETTE["dim"], font_size=20).move_to([1.95, 0.0, 0])

        # bottom row: the first step, a small proof of concept
        step = Text("First step: a small proof of concept", color=PALETTE["dim"], font_size=24).move_to([-2.3, -0.72, 0])
        notes = VGroup(card_bg(1.5, 1.6), lines("quick\nnotes", 24, PALETTE["ink"], buff=0.08))
        notes[1].move_to(notes[0].get_center())
        notes.move_to([-5.5, -2.0, 0])
        a2 = Arrow([-4.7, -2.0, 0], [-4.2, -2.0, 0], buff=0, color=PALETTE["accent"], stroke_width=5,
                   max_tip_length_to_length_ratio=0.8)
        bio = VGroup(card_bg(1.7, 1.6, stroke_color=PALETTE["good"]), lines("a warm\nbio", 22, PALETTE["ink"], buff=0.08))
        bio[1].move_to(bio[0].get_center())
        bio.move_to([-3.2, -2.0, 0])
        posts = VGroup(*[chip("post %d" % (i + 1), w=1.5, h=0.45, border=PALETTE["good"], fs=16) for i in range(3)]
                       ).arrange(DOWN, buff=0.1).move_to([-1.2, -2.0, 0])
        plat = Text("platform-ready", color=PALETTE["dim"], font_size=15).next_to(posts, DOWN, buff=0.08)
        appr = VGroup(tick(PALETTE["good"], 1.6), lines("a person\napproves everything", 20, PALETTE["good"],
                                                         buff=0.06)).arrange(RIGHT, buff=0.2)
        appr_c = VGroup(card_bg(3.0, 1.2, stroke_color=PALETTE["good"]), appr)
        appr.move_to(appr_c[0].get_center())
        appr_c.move_to([1.65, -2.0, 0])
        cam = VGroup(card_bg(2.2, 1.6, stroke_color=PALETTE["accent"]),
                     VGroup(camera_icon(0.75), lines("volunteer\nphoto days", 18, PALETTE["ink"], buff=0.05)).arrange(
                         DOWN, buff=0.12))
        cam[1].move_to(cam[0].get_center())
        cam.move_to([4.85, -2.0, 0])

        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 1.7)
        self.play(FadeIn(plan, shift=LEFT * 0.1), run_time=0.4)
        wait_until(self, 9.9)
        self.play(FadeIn(cat), FadeIn(cl), run_time=0.4)
        wait_until(self, 11.3)
        self.play(FadeIn(plus), FadeIn(dog), FadeIn(dl), run_time=0.4)
        wait_until(self, 13.2)
        self.play(FadeIn(listing), FadeIn(for_s), run_time=0.4)
        self.play(FadeIn(a1), FadeIn(market), run_time=0.5)
        wait_until(self, 18.8)
        self.play(FadeIn(step), run_time=0.4)
        wait_until(self, 21.7)
        self.play(FadeIn(notes), run_time=0.4)
        wait_until(self, 23.4)
        self.play(FadeIn(a2), FadeIn(bio), run_time=0.4)
        self.play(FadeIn(posts), FadeIn(plat), run_time=0.5)
        wait_until(self, 27.0)
        self.play(FadeIn(appr_c), run_time=0.4)
        wait_until(self, 29.4)
        self.play(FadeIn(cam), run_time=0.4)
        wait_until(self, 32.37)


class B08_PartNextSteps(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(4, "A new project")
        plan = status_chip("Early-stage plan", PALETTE["accent"], w=3.6)
        nxt = Text("What comes next (planned)", color=PALETTE["dim"], font_size=26).move_to([-3.2, 1.55, 0])

        def step(n, txt, y):
            num = VGroup(Circle(radius=0.26, color=PALETTE["accent"], fill_color=PALETTE["accent"], fill_opacity=1,
                                stroke_width=0), Text(str(n), color=PALETTE["card"], font_size=24, weight="BOLD"))
            num[1].move_to(num[0].get_center())
            t = lines(txt, 22, PALETTE["ink"], buff=0.06)
            tag = chip("planned", w=1.2, h=0.4, border=PALETTE["dim"], color=PALETTE["dim"], fs=14)
            row = VGroup(num, t).arrange(RIGHT, buff=0.3)
            box = card_bg(6.0, 1.15)
            row.move_to(box.get_center() + LEFT * 0.7)
            tag.move_to(box.get_right() + LEFT * 0.8)
            return VGroup(box, VGroup(row, tag)).move_to([-3.2, y, 0])
        s1 = step(1, "build the demo", 0.65)
        s2 = step(2, "reach out to shelters", -0.65)
        s3 = step(3, "one pilot shelter\nin each region", -1.95)
        s4 = chip("to help shape the next version", w=6.0, h=0.6, border=PALETTE["good"], color=PALETTE["good"], fs=19)
        s4.move_to([-3.2, -2.95, 0])

        # a simple map panel (generic, not to scale) with one pin in each region
        panel = card_bg(5.6, 4.2, stroke_color=PALETTE["border"], fill=PALETTE["warm"]).move_to([3.35, -0.35, 0])
        grid = VGroup(*[Line([panel.get_left()[0] + 0.15, y, 0], [panel.get_right()[0] - 0.15, y, 0],
                             color=PALETTE["border"], stroke_width=1.5) for y in np.linspace(-2.1, 1.7, 6)])
        mn = RoundedRectangle(corner_radius=0.25, width=1.9, height=2.0, fill_color="#E9D9BE", fill_opacity=1,
                              stroke_color=PALETTE["wood"], stroke_width=2).move_to([1.8, 0.1, 0])
        bos = RoundedRectangle(corner_radius=0.25, width=1.5, height=1.2, fill_color="#E9D9BE", fill_opacity=1,
                               stroke_color=PALETTE["wood"], stroke_width=2).move_to([4.75, 0.6, 0])
        link = DashedLine(mn.get_right() + RIGHT * 0.05, bos.get_left() + LEFT * 0.05, color=PALETTE["dim"], stroke_width=2)
        mn_l = Text("Minnesota", color=PALETTE["ink"], font_size=22, weight="BOLD").next_to(mn, DOWN, buff=0.15)
        bos_l = Text("Boston area", color=PALETTE["ink"], font_size=22, weight="BOLD").next_to(bos, DOWN, buff=0.15)
        p1 = pin(1.2).move_to(mn.get_center() + UP * 0.2)
        p2 = pin(1.2).move_to(bos.get_center() + UP * 0.15)
        cap = Text("generic map -- not to scale", color=PALETTE["dim"], font_size=14).move_to([3.35, -2.25, 0])
        one = chip("one pilot shelter in each region", w=5.0, h=0.55, border=PALETTE["accent"], color=PALETTE["accent"],
                   fs=17).move_to([3.35, 2.15, 0])

        self.play(FadeIn(head, shift=UP * 0.1), FadeIn(plan, shift=LEFT * 0.1), run_time=0.5)
        wait_until(self, 0.9)
        self.play(FadeIn(nxt), run_time=0.3)
        wait_until(self, 1.4)
        self.play(FadeIn(s1), run_time=0.4)
        wait_until(self, 3.4)
        self.play(FadeIn(s2), FadeIn(panel), FadeIn(grid),
                  FadeIn(cap), run_time=0.5)
        wait_until(self, 5.0)
        self.play(FadeIn(mn), FadeIn(mn_l), run_time=0.4)
        wait_until(self, 6.0)
        self.play(FadeIn(bos), FadeIn(bos_l), FadeIn(link), run_time=0.4)
        wait_until(self, 7.3)
        self.play(FadeIn(s3), FadeIn(p1), FadeIn(p2),
                  FadeIn(one), run_time=0.5)
        wait_until(self, 10.7)
        self.play(FadeIn(s4), run_time=0.4)
        wait_until(self, 11.64)


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


def mini_pets():
    return VGroup(cat_icon(0.5), dog_icon(0.5)).arrange(RIGHT, buff=0.15)


class B11_StatusWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        cards = [
            mini_card("PUBLISHED", PALETTE["good"], "Writing", "article published", mini_article()),
            mini_card("PRODUCED", PALETTE["good"], "Video\nproduction", "four video files", mini_videos()),
            mini_card("SAVED", PALETTE["good"], "Organizing\nthe work", "files on GitHub", code_folder_icon(0.45)),
            mini_card("PLANNING", PALETTE["accent"], "A new project", "CatBot and DogBot,\nearly-stage plan", mini_pets(),
                      highlight=True),
        ]
        VGroup(*cards).arrange(RIGHT, buff=0.25).move_to([0, 0.5, 0])
        count = chip("3 parts done  ·  1 in planning", w=9.6, h=0.85, border=PALETTE["accent"],
                     color=PALETTE["accent"], fs=34)
        count.move_to([0, -2.8, 0])

        wait_until(self, 2.5)
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.15), run_time=0.35)
        wait_until(self, 5.9)
        self.play(FadeIn(count, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 8.0)
        self.play(Indicate(cards[3][0], color=PALETTE["accent"], scale_factor=1.03), run_time=0.8)
        wait_until(self, 10.68)


class B12_TheLesson(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        k = Text("A real progress update.", color=PALETTE["dim"], font_size=30)
        l1 = Text("Done is done.", color=PALETTE["ink"], font_size=52)
        l2 = Text("Planned is planned.", color=PALETTE["accent"], font_size=52)
        g = VGroup(l1, l2).arrange(DOWN, buff=0.4)
        VGroup(k, g).arrange(DOWN, buff=0.7).move_to(ORIGIN)

        self.play(FadeIn(k, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 1.7)
        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 2.6)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 3.7)
