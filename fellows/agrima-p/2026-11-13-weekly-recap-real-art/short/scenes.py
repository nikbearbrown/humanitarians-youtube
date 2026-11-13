"""
Portrait (9:16) Manim scenes for weekly-recap-real-art-short

Ports of the eight graphic beats (B01, B04, B05, B06, B07, B08, B11, B12) -- full
parity with the 16:9 cut, no beats dropped (the whole recap fits under the 3:00
Shorts cap). Stacked layouts for a 4.5 x 8.0 frame; same palette, copy and audio
timing as the 16:9 scenes. All visuals are generated: no photos of animals, shelters
or people, no real platform logos. The CatBot and DogBot section is labeled
"Early-stage plan" and never says the demo is built or that any shelter has agreed.
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
    g = VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split("\n")]).arrange(DOWN, buff=buff)
    return fit(g, max_w) if max_w else g


def wait_until(scene, t):
    d = t - scene.renderer.time
    if d > 0.02:
        scene.wait(d)


def chip(label, w=2.6, h=0.5, border=None, color=None, fs=14):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(lines(label, fs, color or PALETTE["ink"], buff=0.05), w - 0.2)
    return VGroup(box, txt.move_to(box.get_center()))


def chip2(label, w, h, border, color, fs):
    box = card_bg(w, h, stroke_color=border)
    txt = fit(lines(label, fs, color, buff=0.06), w - 0.2)
    return VGroup(box, txt.move_to(box.get_center()))


def tick(color=None, s=1.0, sw=4):
    t = VMobject(color=color or PALETTE["good"], stroke_width=sw)
    t.set_points_as_corners([[-0.1, 0.0, 0], [-0.02, -0.1, 0], [0.13, 0.12, 0]])
    return t.scale(s)


def left_lines(txt, fs, color, weight=None, buff=0.08):
    kw = {"weight": weight} if weight else {}
    return VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split("\n")]).arrange(
        DOWN, buff=buff, aligned_edge=LEFT)


def header(n, name, top=3.3):
    kick = Text("PART %d OF 4" % n, color=PALETTE["accent"], font_size=16)
    head = fit(left_lines(name, 32, PALETTE["ink"], weight="BOLD", buff=0.08), W)
    g = VGroup(kick, head).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
    g.move_to([L + g.width / 2, top - g.height / 2, 0])
    return g


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
    t = fit(Text(label, color=PALETTE["ink"], font_size=fs, weight="BOLD"), w - 0.1).move_to(box.get_center())
    return VGroup(box, t)


def plan_chip():
    ch = chip("Early-stage plan", w=1.75, h=0.4, border=PALETTE["accent"], color=PALETTE["accent"], fs=12)
    ch.move_to([L + W - ch.width / 2, 3.1, 0])
    return ch


# --- scenes -----------------------------------------------------------------

class B01_FourPartCheck(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        phrase = fit(VGroup(*[Text(t, color=PALETTE["ink"], font_size=40) for t in ("A short,", "plain recap.")]
                            ).arrange(DOWN, buff=0.2), W)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        top = VGroup(phrase, rule).arrange(DOWN, buff=0.3).move_to([0, 2.2, 0])

        labels = ["Writing", "Video\nproduction", "Organizing\nthe work", "A new\nproject"]
        rows = []
        for i, lab in enumerate(labels):
            num = VGroup(Circle(radius=0.24, color=PALETTE["accent"], fill_color=PALETTE["accent"], fill_opacity=1,
                                stroke_width=0),
                         Text(str(i + 1), color=PALETTE["card"], font_size=24, weight="BOLD"))
            num[1].move_to(num[0].get_center())
            t = left_lines(lab, 28, PALETTE["ink"], buff=0.05)
            rows.append(VGroup(num, t).arrange(RIGHT, buff=0.35))
        stack = VGroup(*rows).arrange(DOWN, buff=0.38, aligned_edge=LEFT).move_to([0, -0.7, 0])
        stack.shift(RIGHT * (L + 0.1 - stack.get_left()[0]))

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        for r, t in zip(rows, [3.0, 3.9, 4.6, 5.2]):
            wait_until(self, t)
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.4)
        wait_until(self, 5.99)


class B04_PartWriting(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(1, "Writing")
        status = chip("published", w=1.8, h=0.46, border=PALETTE["good"], color=PALETTE["good"], fs=18)
        tk = tick(PALETTE["good"], 0.8)
        pair = VGroup(tk, status).arrange(RIGHT, buff=0.15)
        pair.move_to([L + pair.width / 2, 2.15, 0])

        card = card_bg(W, 4.4).move_to([0, -0.55, 0])
        kicker = Text("SUBSTACK  ·  ARTICLE", color=PALETTE["accent"], font_size=14)
        title = lines("Real Art,\nNew Light", 34, PALETTE["ink"], weight="BOLD", buff=0.1, max_w=3.3)
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)
        l1 = lines("How AI can be used to\npromote real artwork,", 17, PALETTE["ink"], buff=0.06, max_w=3.3)
        l2 = lines("while keeping the original\nat the center.", 17, PALETTE["ink"], buff=0.06, max_w=3.3)
        body = VGroup(kicker, title, rule, l1, l2).arrange(DOWN, buff=0.24).move_to(card.get_center())
        mock = Text("mock article header", color=PALETTE["dim"], font_size=13).move_to([0, -3.0, 0])

        wait_until(self, 1.9)
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
        tool = chip2("made with Brutalist,\nour video-creation tool", W, 0.6, PALETTE["dim"], PALETTE["dim"], 13)
        tool.move_to([0, 2.0, 0])

        def block(label, sub, y):
            lab = Text(label, color=PALETTE["ink"], font_size=24)
            sb = Text(sub, color=PALETTE["dim"], font_size=15)
            col = VGroup(lab, sb).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
            col.move_to([L + col.width / 2, y + 0.7, 0])
            t169 = file_tile(1.5, 0.85, "16:9", fs=17).move_to([-0.95, y - 0.15, 0])
            t916 = file_tile(0.62, 0.95, "9:16", fs=13).move_to([0.55, y - 0.15, 0])
            k1 = tick(PALETTE["good"], 0.75).next_to(t169, RIGHT, buff=0.12)
            k2 = tick(PALETTE["good"], 0.75).next_to(t916, RIGHT, buff=0.12)
            return col, t169, t916, k1, k2

        r1 = block("AI topic video", "based on the article", 0.6)
        r2 = block("Weekly recap", "this video", -1.0)
        count = chip2("4 video files", W, 0.8, PALETTE["accent"], PALETTE["accent"], 30)
        count.move_to([0, -2.6, 0])

        wait_until(self, 0.2)
        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 4.8)
        self.play(FadeIn(tool, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(count, shift=UP * 0.1), run_time=0.5)
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

        head = header(3, "Organizing\nthe work")

        gh = code_folder_icon(0.8).move_to([0, 0.95, 0])
        gl = Text("GitHub", color=PALETTE["ink"], font_size=34, weight="BOLD").move_to([0, -0.5, 0])
        gs = Text("my files", color=PALETTE["dim"], font_size=17).move_to([0, -1.0, 0])
        gc = chip("pushed", w=1.5, h=0.46, border=PALETTE["good"], color=PALETTE["good"], fs=18).move_to([0.2, -1.6, 0])
        gk = tick(PALETTE["good"], 0.75).next_to(gc, LEFT, buff=0.12)
        c1 = chip("saved", w=1.4, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=16)
        c2 = chip("easy to share", w=2.1, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=16)
        foot = VGroup(c1, c2).arrange(RIGHT, buff=0.15).move_to([0, -2.6, 0])

        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 2.4)
        self.play(FadeIn(gh, shift=UP * 0.1), FadeIn(gl), FadeIn(gs), run_time=0.5)
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

        head = header(4, "A new\nproject")
        plan = plan_chip()

        cat = cat_icon(0.6).move_to([-0.95, 1.55, 0])
        dog = dog_icon(0.6).move_to([0.95, 1.55, 0])
        plus = Text("+", color=PALETTE["dim"], font_size=28).move_to([0, 1.5, 0])
        cl = Text("CatBot", color=PALETTE["ink"], font_size=17, weight="BOLD").move_to([-0.95, 1.0, 0])
        dl = Text("DogBot", color=PALETTE["ink"], font_size=17, weight="BOLD").move_to([0.95, 1.0, 0])
        listing = chip2("each animal's\nlisting", 1.35, 0.6, PALETTE["border"], PALETTE["ink"], 12).move_to([-1.2, 0.4, 0])
        a1 = Arrow([-0.45, 0.4, 0], [-0.1, 0.4, 0], buff=0, color=PALETTE["accent"], stroke_width=4,
                   max_tip_length_to_length_ratio=0.9)
        market = chip2("marketing that helps\nthem get adopted", 1.9, 0.6, PALETTE["good"], PALETTE["good"], 12).move_to(
            [0.95, 0.4, 0])
        for_s = Text("for cat and dog shelters", color=PALETTE["dim"], font_size=12).move_to([0, -0.05, 0])

        step = Text("First step: a small proof of concept", color=PALETTE["dim"], font_size=13).move_to([0, -0.5, 0])
        notes = VGroup(card_bg(1.05, 0.85), lines("quick\nnotes", 14, PALETTE["ink"], buff=0.05))
        notes[1].move_to(notes[0].get_center())
        notes.move_to([-1.4, -1.25, 0])
        a2 = Arrow([-0.82, -1.25, 0], [-0.62, -1.25, 0], buff=0, color=PALETTE["accent"], stroke_width=3,
                   max_tip_length_to_length_ratio=1.0)
        bio = VGroup(card_bg(1.05, 0.85, stroke_color=PALETTE["good"]), lines("a warm\nbio", 14, PALETTE["ink"], buff=0.05))
        bio[1].move_to(bio[0].get_center())
        bio.move_to([-0.05, -1.25, 0])
        posts = VGroup(*[chip("post %d" % (i + 1), w=1.05, h=0.26, border=PALETTE["good"], fs=10) for i in range(3)]
                       ).arrange(DOWN, buff=0.06).move_to([1.4, -1.25, 0])
        plat = Text("platform-ready", color=PALETTE["dim"], font_size=10).move_to([1.4, -1.82, 0])
        appr = VGroup(tick(PALETTE["good"], 1.0), Text("a person approves everything", color=PALETTE["good"],
                                                       font_size=14)).arrange(RIGHT, buff=0.15)
        appr_c = VGroup(card_bg(W, 0.6, stroke_color=PALETTE["good"]), appr)
        appr.move_to(appr_c[0].get_center())
        appr_c.move_to([0, -2.35, 0])
        cam = VGroup(card_bg(W, 0.7, stroke_color=PALETTE["accent"]),
                     VGroup(camera_icon(0.4), Text("volunteer photo days", color=PALETTE["ink"], font_size=14)).arrange(
                         RIGHT, buff=0.2))
        cam[1].move_to(cam[0].get_center())
        cam.move_to([0, -3.1, 0])

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

        head = header(4, "A new\nproject")
        plan = plan_chip()
        nxt = Text("What comes next (planned)", color=PALETTE["dim"], font_size=14).move_to([0, 1.7, 0])

        def step(n, txt, y, h=0.55):
            num = VGroup(Circle(radius=0.17, color=PALETTE["accent"], fill_color=PALETTE["accent"], fill_opacity=1,
                                stroke_width=0), Text(str(n), color=PALETTE["card"], font_size=15, weight="BOLD"))
            num[1].move_to(num[0].get_center())
            t = lines(txt, 15, PALETTE["ink"], buff=0.04)
            row = VGroup(num, t).arrange(RIGHT, buff=0.2)
            box = card_bg(W, h)
            row.move_to(box.get_center() + LEFT * 0.5)
            tag = chip("planned", w=0.85, h=0.28, border=PALETTE["dim"], color=PALETTE["dim"], fs=10)
            tag.move_to(box.get_right() + LEFT * 0.55)
            return VGroup(box, VGroup(row, tag)).move_to([0, y, 0])
        s1 = step(1, "build the demo", 1.2)
        s2 = step(2, "reach out to shelters", 0.55)
        s3 = step(3, "one pilot shelter\nin each region", -0.2, h=0.7)
        s4 = chip("to help shape the next version", w=W, h=0.4, border=PALETTE["good"], color=PALETTE["good"], fs=12)
        s4.move_to([0, -0.9, 0])
        one = chip("one pilot shelter in each region", w=W, h=0.4, border=PALETTE["accent"], color=PALETTE["accent"],
                   fs=12).move_to([0, -1.42, 0])

        panel = card_bg(W, 1.75, stroke_color=PALETTE["border"], fill=PALETTE["warm"]).move_to([0, -2.45, 0])
        mn = RoundedRectangle(corner_radius=0.18, width=1.05, height=1.0, fill_color="#E9D9BE", fill_opacity=1,
                              stroke_color=PALETTE["wood"], stroke_width=2).move_to([-0.95, -2.4, 0])
        bos = RoundedRectangle(corner_radius=0.18, width=0.85, height=0.7, fill_color="#E9D9BE", fill_opacity=1,
                               stroke_color=PALETTE["wood"], stroke_width=2).move_to([0.95, -2.2, 0])
        link = DashedLine(mn.get_right() + RIGHT * 0.05, bos.get_left() + LEFT * 0.05, color=PALETTE["dim"], stroke_width=2)
        mn_l = Text("Minnesota", color=PALETTE["ink"], font_size=12, weight="BOLD").next_to(mn, DOWN, buff=0.06)
        bos_l = Text("Boston area", color=PALETTE["ink"], font_size=12, weight="BOLD").next_to(bos, DOWN, buff=0.06)
        p1 = pin(0.75).move_to(mn.get_center() + UP * 0.1)
        p2 = pin(0.75).move_to(bos.get_center() + UP * 0.08)
        cap = Text("generic map -- not to scale", color=PALETTE["dim"], font_size=9).move_to([0, -3.22, 0])

        self.play(FadeIn(head, shift=UP * 0.1), FadeIn(plan, shift=LEFT * 0.1), run_time=0.5)
        wait_until(self, 0.9)
        self.play(FadeIn(nxt), run_time=0.3)
        wait_until(self, 1.4)
        self.play(FadeIn(s1), run_time=0.4)
        wait_until(self, 3.4)
        self.play(FadeIn(s2), FadeIn(panel), FadeIn(cap), run_time=0.5)
        wait_until(self, 5.0)
        self.play(FadeIn(mn), FadeIn(mn_l), run_time=0.4)
        wait_until(self, 6.0)
        self.play(FadeIn(bos), FadeIn(bos_l), FadeIn(link), run_time=0.4)
        wait_until(self, 7.3)
        self.play(FadeIn(s3), FadeIn(p1), FadeIn(p2), FadeIn(one), run_time=0.5)
        wait_until(self, 10.7)
        self.play(FadeIn(s4), run_time=0.4)
        wait_until(self, 11.64)


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


class B11_StatusWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        cards = [
            hcard(mini_article(), "PUBLISHED", PALETTE["good"], "Writing", "article published"),
            hcard(mini_videos(), "PRODUCED", PALETTE["good"], "Video\nproduction", "four video files"),
            hcard(code_folder_icon(0.3), "SAVED", PALETTE["good"], "Organizing\nthe work", "files on GitHub"),
            hcard(VGroup(cat_icon(0.4), dog_icon(0.4)).arrange(RIGHT, buff=0.1), "PLANNING", PALETTE["accent"],
                  "A new project", "CatBot and DogBot,\nearly-stage plan", highlight=True),
        ]
        VGroup(*cards).arrange(DOWN, buff=0.12).move_to([0, 0.5, 0])
        count = chip2("3 parts done\n1 in planning", W, 0.85, PALETTE["accent"], PALETTE["accent"], 24)
        count.move_to([0, -2.85, 0])

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

        k = lines("A real progress\nupdate.", 24, PALETTE["dim"], buff=0.1)
        l1 = Text("Done is done.", color=PALETTE["ink"], font_size=34)
        l2 = VGroup(*[Text(t, color=PALETTE["accent"], font_size=34) for t in ("Planned is", "planned.")]
                    ).arrange(DOWN, buff=0.12)
        g = VGroup(l1, l2).arrange(DOWN, buff=0.4)
        fit(g, W)
        VGroup(k, g).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        self.play(FadeIn(k, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 1.7)
        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 2.6)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 3.7)
