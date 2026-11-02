"""
Portrait (9:16) Manim scenes for weekly-recap-brand-check-short

Ports of the seven graphic beats (B01, B04, B05, B06, B07, B10, B11) -- full
parity with the 16:9 cut, no beats dropped (the whole recap fits under the
3:00 Shorts cap). Stacked layouts for a 4.5 x 8.0 frame; same palette, copy and
audio timing as the 16:9 scenes. All visuals are generated: no photos, no
children, no people shapes, no real platform logos. The poster is abstract and
carries the required label only.
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

        labels = ["Writing", "Video\nproduction", "Homes of Hope\ndocumentary", "Organizing\nthe work"]
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
        wait_until(self, 5.95)


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
        title = lines("Have You Asked\nthe Chatbot About\nYour Brand Lately?", 26, PALETTE["ink"], weight="BOLD",
                      buff=0.1, max_w=3.3)
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)
        l1 = lines("Chatbots are a first\nimpression for brands.", 17, PALETTE["ink"], buff=0.06, max_w=3.3)
        l2 = lines("A five-minute check catches\nwrong or outdated info.", 17, PALETTE["ink"], buff=0.06, max_w=3.3)
        body = VGroup(kicker, title, rule, l1, l2).arrange(DOWN, buff=0.22).move_to(card.get_center())
        mock = Text("mock article header", color=PALETTE["dim"], font_size=13).move_to([0, -3.0, 0])

        wait_until(self, 1.8)
        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 3.6)
        w = card.width
        card.stretch(0.01, 0)
        self.play(FadeIn(card), card.animate.stretch_to_fit_width(w), run_time=0.5)
        self.play(FadeIn(kicker), run_time=0.3)
        wait_until(self, 5.9)
        self.play(FadeIn(pair, shift=RIGHT * 0.1), run_time=0.4)
        wait_until(self, 6.9)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.5)
        grow_in(self, rule, 1.4, run_time=0.3)
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
        chips = [chip(s, w=1.75, h=0.48, border=PALETTE["accent"], color=PALETTE["ink"], fs=19) for s in stages]
        strip = VGroup(VGroup(chips[0], chips[1]).arrange(RIGHT, buff=0.2),
                       VGroup(chips[2], chips[3]).arrange(RIGHT, buff=0.2)).arrange(DOWN, buff=0.15)
        strip.move_to([0, 1.55, 0])

        def block(label, y):
            lab = Text(label, color=PALETTE["ink"], font_size=24)
            lab.move_to([L + lab.width / 2, y + 0.65, 0])
            t169 = file_tile(1.5, 0.85, "16:9", fs=17).move_to([-0.95, y - 0.1, 0])
            t916 = file_tile(0.62, 0.95, "9:16", fs=13).move_to([0.55, y - 0.1, 0])
            k1 = tick(PALETTE["good"], 0.75).next_to(t169, RIGHT, buff=0.12)
            k2 = tick(PALETTE["good"], 0.75).next_to(t916, RIGHT, buff=0.12)
            return lab, t169, t916, k1, k2

        r1 = block("AI topic video", -0.05)
        r2 = block("Weekly recap", -1.6)
        count = chip2("4 video files", W, 0.8, PALETTE["accent"], PALETTE["accent"], 30)
        count.move_to([0, -2.85, 0])

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
            self.play(FadeIn(chips[i + 1]), run_time=0.3)
        wait_until(self, 12.9)
        self.play(FadeIn(r1[1]), FadeIn(r2[1]), run_time=0.4)
        self.play(FadeIn(r1[3]), FadeIn(r2[3]), run_time=0.25)
        wait_until(self, 14.3)
        self.play(FadeIn(r1[2]), FadeIn(r2[2]), run_time=0.4)
        self.play(FadeIn(r1[4]), FadeIn(r2[4]), run_time=0.25)
        wait_until(self, 16.0)
        self.play(FadeIn(count, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 17.35)


class B06_PartPoster(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = header(3, "Homes of Hope\ndocumentary")
        poster = poster_art(1.8, 2.5).move_to([-1.0, 0.5, 0])
        cap = lines("Poster design for the Homes of Hope\ndocumentary (with Yatra)", 16, PALETTE["ink"], buff=0.07,
                    max_w=W).move_to([0, -1.1, 0])

        kicker = lines("Supports marginalized\ngirls in India with:", 14, PALETTE["dim"], buff=0.05).move_to([0.95, 1.6, 0])
        c1 = chip("a safe home", w=1.6, h=0.55, border=PALETTE["good"], color=PALETTE["ink"], fs=17)
        c2 = chip("education", w=1.6, h=0.55, border=PALETTE["good"], color=PALETTE["ink"], fs=17)
        c3 = chip("support", w=1.6, h=0.55, border=PALETTE["good"], color=PALETTE["ink"], fs=17)
        stack = VGroup(c1, c2, c3).arrange(DOWN, buff=0.18).move_to([1.0, 0.25, 0])
        helped = chip2("My part:\nI helped Yatra with the poster", W, 1.0, PALETTE["accent"], PALETTE["accent"], 19)
        helped.move_to([0, -2.25, 0])

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

        head = header(4, "Organizing\nthe work")

        def block(icon, name, sub, status, y):
            icon.move_to([-1.2, y, 0])
            nm = Text(name, color=PALETTE["ink"], font_size=34, weight="BOLD")
            sb = fit(Text(sub, color=PALETTE["dim"], font_size=18), 2.2)
            ch = chip(status, w=1.5, h=0.46, border=PALETTE["good"], color=PALETTE["good"], fs=18)
            tk = tick(PALETTE["good"], 0.75)
            row = VGroup(tk, ch).arrange(RIGHT, buff=0.12)
            col = VGroup(nm, sb, row).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            col.move_to([-0.4 + col.width / 2, y, 0])
            return icon, nm, sb, row

        gh = block(code_folder_icon(0.52), "GitHub", "the AI videos' files", "pushed", 0.75)
        dr = block(cloud_folder_icon(0.5), "Drive", "the week's videos", "attached", -1.0)
        foot = chip2("everything saved\nand shareable", W, 0.95, PALETTE["accent"], PALETTE["accent"], 21)
        foot.move_to([0, -2.7, 0])

        self.play(FadeIn(head, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 2.6)
        self.play(FadeIn(gh[0], shift=UP * 0.1), FadeIn(gh[1]), FadeIn(gh[2]), run_time=0.5)
        wait_until(self, 5.0)
        self.play(FadeIn(gh[3]), run_time=0.3)
        wait_until(self, 5.8)
        self.play(FadeIn(dr[0], shift=UP * 0.1), FadeIn(dr[1]), FadeIn(dr[2]), run_time=0.5)
        wait_until(self, 7.8)
        self.play(FadeIn(dr[3]), run_time=0.3)
        wait_until(self, 8.4)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 10.35)


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


class B10_RoleWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        cards = [
            hcard(mini_article(), "AUTHOR", PALETTE["good"], "Writing", "article published"),
            hcard(mini_videos(), "PRODUCER", PALETTE["good"], "Video\nproduction", "four video files"),
            hcard(poster_art(0.95, 1.2), "SUPPORT", PALETTE["accent"], "Homes of Hope\ndocumentary",
                  "poster, with Yatra", highlight=True),
            hcard(VGroup(code_folder_icon(0.3), cloud_folder_icon(0.3)).arrange(DOWN, buff=0.1), "ORGANIZER",
                  PALETTE["good"], "Organizing\nthe work", "GitHub and Drive"),
        ]
        VGroup(*cards).arrange(DOWN, buff=0.12).move_to([0, 0.5, 0])
        count = chip2("4 parts done\n1 in a supporting role", W, 0.85, PALETTE["accent"], PALETTE["accent"], 21)
        count.move_to([0, -2.85, 0])

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

        k = lines("A real progress\nupdate.", 24, PALETTE["dim"], buff=0.1)
        l1 = Text("Done is done.", color=PALETTE["ink"], font_size=34)
        l2 = VGroup(*[Text(t, color=PALETTE["ink"], font_size=34) for t in ("Helping is", "helping.")]
                    ).arrange(DOWN, buff=0.12)
        l3 = Text("Said plainly.", color=PALETTE["accent"], font_size=34)
        g = VGroup(l1, l2, l3).arrange(DOWN, buff=0.4)
        fit(g, W)
        VGroup(k, g).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        self.play(FadeIn(k, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 1.5)
        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 2.3)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 3.1)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 3.72)
