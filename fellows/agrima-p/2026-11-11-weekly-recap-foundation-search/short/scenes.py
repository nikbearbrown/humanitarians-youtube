"""
Portrait (9:16) Manim scenes for weekly-recap-foundation-search-short

Ports of the seven graphic beats (B01, B04, B05, B06, B07, B10, B11) -- full
parity with the 16:9 cut, no beats dropped (the whole recap fits under the
3:00 Shorts cap). Stacked layouts for a 4.5 x 8.0 frame; same palette, copy and
audio timing as the 16:9 scenes. All visuals are generated: no photos, no
children, no people shapes, no real platform logos. The outreach graphic is
abstract (connected dots around a megaphone) and carries the required label only.
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
    txt = fit(Text(label, color=color or PALETTE["ink"], font_size=fs), w - 0.2)
    return VGroup(box, txt.move_to(box.get_center()))


def chip2(label, w, h, border, color, fs):
    box = card_bg(w, h, stroke_color=border)
    txt = fit(lines(label, fs, color, buff=0.06), w - 0.2)
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


def left_lines(txt, fs, color, weight=None, buff=0.08):
    kw = {"weight": weight} if weight else {}
    return VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split("\n")]).arrange(
        DOWN, buff=buff, aligned_edge=LEFT)


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
    return VGroup(spokes, ring, nodes, mega).scale(s)


def file_tile(w, h, label, fs=22):
    box = RoundedRectangle(corner_radius=0.08, width=w, height=h, fill_color=PALETTE["card"], fill_opacity=1,
                           stroke_color=PALETTE["good"], stroke_width=3)
    t = fit(Text(label, color=PALETTE["ink"], font_size=fs, weight="BOLD"), w - 0.1).move_to(box.get_center())
    return VGroup(box, t)


# --- scenes -----------------------------------------------------------------

class B01_FourPartCheck(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        phrase = fit(VGroup(*[Text(t, color=PALETTE["ink"], font_size=40) for t in ("A short,", "plain recap.")]
                            ).arrange(DOWN, buff=0.2), W)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        top = VGroup(phrase, rule).arrange(DOWN, buff=0.3).move_to([0, 2.2, 0])

        labels = ["Writing", "Video\nproduction", "Homes of Hope\noutreach", "Organizing\nthe work"]
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
        title = lines("Your Foundation\nSearch Is Doing\nMarket Research", 26, PALETTE["ink"], weight="BOLD",
                      buff=0.1, max_w=3.3)
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)
        l1 = lines("Late-night shade testing and\nvirtual try-on tools", 17, PALETTE["ink"], buff=0.06, max_w=3.3)
        l2 = lines("give beauty brands useful clues\nabout what to make next.", 17, PALETTE["ink"], buff=0.06, max_w=3.3)
        body = VGroup(kicker, title, rule, l1, l2).arrange(DOWN, buff=0.22).move_to(card.get_center())
        mock = Text("mock article header", color=PALETTE["dim"], font_size=13).move_to([0, -3.0, 0])

        wait_until(self, 1.9)
        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 3.6)
        w = card.width
        card.stretch(0.01, 0)
        self.play(FadeIn(card), card.animate.stretch_to_fit_width(w), run_time=0.5)
        self.play(FadeIn(kicker), run_time=0.3)
        wait_until(self, 5.9)
        self.play(FadeIn(pair, shift=RIGHT * 0.1), run_time=0.4)
        wait_until(self, 6.6)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.5)
        grow_in(self, rule, 1.4, run_time=0.3)
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

        r1 = block("AI topic video", "based on the article", 0.9)
        r2 = block("Weekly recap", "this video", -0.9)
        count = chip2("4 video files", W, 0.8, PALETTE["accent"], PALETTE["accent"], 30)
        count.move_to([0, -2.5, 0])

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
        self.play(FadeIn(count, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 14.9)


class B06_PartOutreach(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(3, "Homes of Hope\noutreach")
        kicker = lines("Supports marginalized girls\nin India with:", 15, PALETTE["dim"], buff=0.05).move_to([0, 1.4, 0])
        c1 = chip("a safe home", w=1.4, h=0.5, border=PALETTE["good"], color=PALETTE["ink"], fs=14)
        c2 = chip("education", w=1.25, h=0.5, border=PALETTE["good"], color=PALETTE["ink"], fs=14)
        c3 = chip("support", w=1.0, h=0.5, border=PALETTE["good"], color=PALETTE["ink"], fs=14)
        row = VGroup(c1, c2, c3).arrange(RIGHT, buff=0.1).move_to([0, 0.8, 0])
        art = outreach_art(0.6).move_to([0, -0.6, 0])
        cap = lines("Homes of Hope documentary outreach\n(with Yatra)", 15, PALETTE["ink"], buff=0.07,
                    max_w=W).move_to([0, -1.9, 0])
        goal = chip2("Goal: help the girls' stories\nreach a wider audience", W, 0.9, PALETTE["accent"],
                     PALETTE["accent"], 18).move_to([0, -2.75, 0])
        ongoing = chip("ongoing", w=1.5, h=0.46, border=PALETTE["accent"], color=PALETTE["accent"], fs=18)
        ongoing.move_to([L + W - ongoing.width / 2, 1.9, 0])

        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 3.0)
        self.play(FadeIn(kicker), run_time=0.4)
        wait_until(self, 7.6)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.3)
        wait_until(self, 8.7)
        self.play(FadeIn(c2, shift=UP * 0.1), run_time=0.3)
        wait_until(self, 10.1)
        self.play(FadeIn(c3, shift=UP * 0.1), run_time=0.3)
        wait_until(self, 11.5)
        self.play(FadeIn(art, shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(cap), run_time=0.4)
        wait_until(self, 13.5)
        self.play(FadeIn(goal, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 16.7)
        self.play(FadeIn(ongoing, shift=LEFT * 0.1), run_time=0.4)
        wait_until(self, 18.0)


class B07_PartSaved(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(4, "Organizing\nthe work")

        gh = code_folder_icon(0.8).move_to([0, 0.9, 0])
        gl = Text("GitHub", color=PALETTE["ink"], font_size=34, weight="BOLD").move_to([0, -0.5, 0])
        gs = Text("all of my project files", color=PALETTE["dim"], font_size=17).move_to([0, -1.0, 0])
        gc = chip("pushed", w=1.5, h=0.46, border=PALETTE["good"], color=PALETTE["good"], fs=18).move_to([0.2, -1.6, 0])
        gk = tick(PALETTE["good"], 0.75).next_to(gc, LEFT, buff=0.12)
        c1 = chip("saved", w=1.1, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=14)
        c2 = chip("organized", w=1.25, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=14)
        c3 = chip("easy to find", w=1.3, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=14)
        foot = VGroup(c1, c2, c3).arrange(RIGHT, buff=0.1).move_to([0, -2.6, 0])

        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 2.6)
        self.play(FadeIn(gh, shift=UP * 0.1), FadeIn(gl), FadeIn(gs), run_time=0.5)
        wait_until(self, 4.6)
        self.play(FadeIn(gc), FadeIn(gk), run_time=0.3)
        wait_until(self, 5.1)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.3)
        wait_until(self, 6.8)
        self.play(FadeIn(c2, shift=UP * 0.1), run_time=0.3)
        wait_until(self, 7.8)
        self.play(FadeIn(c3, shift=UP * 0.1), run_time=0.3)
        wait_until(self, 8.6)


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


class B10_StatusWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        cards = [
            hcard(mini_article(), "PUBLISHED", PALETTE["good"], "Writing", "article published"),
            hcard(mini_videos(), "PRODUCED", PALETTE["good"], "Video\nproduction", "four video files"),
            hcard(outreach_art(0.3), "ONGOING", PALETTE["accent"], "Homes of Hope\noutreach",
                  "with Yatra", highlight=True),
            hcard(code_folder_icon(0.3), "SAVED", PALETTE["good"], "Organizing\nthe work", "all files on GitHub"),
        ]
        VGroup(*cards).arrange(DOWN, buff=0.12).move_to([0, 0.5, 0])
        count = chip2("3 parts done\n1 ongoing", W, 0.85, PALETTE["accent"], PALETTE["accent"], 24)
        count.move_to([0, -2.85, 0])

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

        k = lines("A real progress\nupdate.", 24, PALETTE["dim"], buff=0.1)
        l1 = Text("Done is done.", color=PALETTE["ink"], font_size=34)
        l2 = VGroup(*[Text(t, color=PALETTE["accent"], font_size=34) for t in ("Ongoing is", "ongoing.")]
                    ).arrange(DOWN, buff=0.12)
        g = VGroup(l1, l2).arrange(DOWN, buff=0.4)
        fit(g, W)
        VGroup(k, g).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        self.play(FadeIn(k, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 1.8)
        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 2.7)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 3.98)
