"""
Portrait (9:16) Manim scenes for weekly-recap-mcphs-short

Ports of the eight graphic beats (B01, B04, B07, B08, B09, B10, B11, B12) --
full parity with the 16:9 cut, no beats dropped. Stacked layouts for a
4.5 x 8.0 frame; same palette and copy as the 16:9 scenes. All visuals are
generated (no slide images, no photos). No personal information about any
individual appears in this file.
"""

from manim import *
import numpy as np

config.frame_width = 4.5
config.frame_height = 8.0

SAFE_W = 3.7

PALETTE = {
    "bg":     "#FAF9F5",
    "ink":    "#3D3929",
    "accent": "#D97757",
    "good":   "#4A7C59",
    "miss":   "#C0392B",
    "card":   "#FFFFFF",
    "border": "#E8E4DA",
    "dim":    "#8B8878",
    "water":  "#DDE8EA",
}


def card_bg(width, height, stroke_color=None):
    return RoundedRectangle(
        corner_radius=0.12, width=width, height=height,
        fill_color=PALETTE["card"], fill_opacity=1,
        stroke_color=stroke_color or PALETTE["border"], stroke_width=1.5,
    )


def grow_in(scene, mob, target_width, run_time=0.5, **kwargs):
    mob.stretch(0.01, 0)
    scene.play(mob.animate.stretch_to_fit_width(target_width), run_time=run_time, **kwargs)


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


def lines(txt, fs, color, max_w=None, buff=0.1, weight=None):
    kw = {"weight": weight} if weight else {}
    g = VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split("\n")]).arrange(DOWN, buff=buff)
    return fit(g, max_w) if max_w else g


def reveal(scene, card, t1=0.35, t2=0.4):
    box, inner = card[0], card[1]
    w = box.width
    box.stretch(0.01, 0)
    scene.play(box.animate.stretch_to_fit_width(w), run_time=t1)
    scene.play(FadeIn(inner), run_time=t2)


def chip(label, w=2.6, h=0.5, border=None, color=None, fs=14):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(Text(label, color=color or PALETTE["ink"], font_size=fs), w - 0.2)
    return VGroup(box, txt.move_to(box.get_center()))


def person(h=1.0, color=None):
    c = color or PALETTE["ink"]
    head = Circle(radius=0.26 * h, color=c, fill_color=c, fill_opacity=1, stroke_width=0)
    body = RoundedRectangle(corner_radius=0.18 * h, width=0.7 * h, height=0.8 * h,
                             fill_color=c, fill_opacity=1, stroke_width=0)
    return VGroup(head, body).arrange(DOWN, buff=0.05)


# --- icons ------------------------------------------------------------------

def article_icon():
    page = RoundedRectangle(corner_radius=0.05, width=0.7, height=0.9,
                             fill_color=PALETTE["bg"], fill_opacity=1,
                             stroke_color=PALETTE["dim"], stroke_width=1.5)
    ln = VGroup(*[Line(LEFT * 0.22, RIGHT * (0.22 - 0.08 * i), color=PALETTE["border"], stroke_width=2)
                  for i in range(4)]).arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to(page.get_center())
    return VGroup(page, ln)


def two_videos_icon():
    def vid(label):
        land = RoundedRectangle(corner_radius=0.04, width=0.9, height=0.52, fill_color=PALETTE["bg"],
                                 fill_opacity=1, stroke_color=PALETTE["dim"], stroke_width=1.5)
        port = RoundedRectangle(corner_radius=0.04, width=0.3, height=0.52, fill_color=PALETTE["bg"],
                                 fill_opacity=1, stroke_color=PALETTE["dim"], stroke_width=1.5)
        tl = Text("16:9", color=PALETTE["dim"], font_size=9).move_to(land.get_center())
        tp = Text("9:16", color=PALETTE["dim"], font_size=8).move_to(port.get_center())
        frames = VGroup(VGroup(land, tl), VGroup(port, tp)).arrange(RIGHT, buff=0.12)
        lab = Text(label, color=PALETTE["ink"], font_size=11)
        return VGroup(lab, frames).arrange(DOWN, buff=0.1)
    return VGroup(vid("AI Done Right"), vid("this recap")).arrange(DOWN, buff=0.22)


def slides_icon():
    slide = RoundedRectangle(corner_radius=0.05, width=0.85, height=0.55,
                              fill_color=PALETTE["bg"], fill_opacity=1,
                              stroke_color=PALETTE["accent"], stroke_width=2)
    sl = VGroup(*[Line(LEFT * 0.32, RIGHT * (0.32 - 0.12 * i), color=PALETTE["dim"], stroke_width=1.5)
                  for i in range(2)]).arrange(DOWN, buff=0.09).move_to(slide.get_center())
    podium = Polygon([-0.22, -0.32, 0], [0.22, -0.32, 0], [0.14, 0.0, 0], [-0.14, 0.0, 0],
                     fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0)
    podium.next_to(slide, DOWN, buff=0.02)
    return VGroup(slide, sl, podium)


def blocks_icon(color):
    return VGroup(*[Rectangle(width=0.22, height=h, fill_color=color, fill_opacity=1, stroke_width=0)
                    for h in (0.55, 0.85, 0.65)]).arrange(RIGHT, buff=0.05, aligned_edge=DOWN)


def house_icon(color):
    roof = Triangle(color=color, fill_color=color, fill_opacity=1, stroke_width=0).scale(0.22).stretch(1.5, 0)
    body = Rectangle(width=0.5, height=0.32, fill_color=color, fill_opacity=0.7, stroke_width=0)
    return VGroup(roof, body).arrange(DOWN, buff=0)


def drone_icon(color=None):
    c = color or PALETTE["ink"]
    body = RoundedRectangle(corner_radius=0.06, width=0.5, height=0.18, fill_color=c, fill_opacity=1,
                             stroke_width=0)
    arms = VGroup(Line(LEFT * 0.55, LEFT * 0.25, color=c, stroke_width=3),
                  Line(RIGHT * 0.25, RIGHT * 0.55, color=c, stroke_width=3))
    rotors = VGroup(*[Ellipse(width=0.42, height=0.07, fill_color=PALETTE["accent"], fill_opacity=0.7,
                              stroke_width=0).move_to([x, 0.1, 0]) for x in (-0.55, 0.55)])
    return VGroup(body, arms, rotors)


def loon_icon(scale=1.0):
    body = Ellipse(width=1.0, height=0.38, fill_color=PALETTE["ink"], fill_opacity=1, stroke_width=0)
    neck = Rectangle(width=0.1, height=0.3, fill_color=PALETTE["ink"], fill_opacity=1, stroke_width=0)
    neck.move_to(body.get_right() + LEFT * 0.12 + UP * 0.22)
    head = Circle(radius=0.1, fill_color=PALETTE["ink"], fill_opacity=1, stroke_width=0)
    head.move_to(neck.get_top() + UP * 0.05)
    beak = Triangle(fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0).scale(0.06)
    beak.rotate(-PI / 2).move_to(head.get_right() + RIGHT * 0.07)
    spots = VGroup(*[Dot(body.get_center() + [x, y, 0], radius=0.025, color=PALETTE["card"])
                     for x, y in ((-0.2, 0.05), (0.0, 0.08), (-0.05, -0.04), (0.18, -0.02))])
    return VGroup(body, neck, head, beak, spots).scale(scale)


def hcard(icon, parts, w=3.7, h=1.6, border=None, icon_h=None):
    """Horizontal card: icon left, text lines right. parts = [(text, fs, color, weight)]"""
    box = card_bg(w, h, stroke_color=border)
    icon = icon.copy()
    icon.scale_to_fit_height(icon_h or (h - 0.5))
    if icon.width > 1.15:
        icon.scale_to_fit_width(1.15)
    texts = VGroup(*[lines(t, fs, c, buff=0.04, weight=wt) for (t, fs, c, wt) in parts]).arrange(
        DOWN, buff=0.08, aligned_edge=LEFT)
    inner = VGroup(icon, texts).arrange(RIGHT, buff=0.3)
    fit(inner, w - 0.4)
    return VGroup(box, inner.move_to(box.get_center()))


# --- scenes -----------------------------------------------------------------

class B01_NotAHighlightReel(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        phrase = fit(VGroup(*[Text(t, color=PALETTE["ink"], font_size=40)
                              for t in ("Not a", "highlight", "reel.")]).arrange(DOWN, buff=0.22), 3.4)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        sub = fit(VGroup(*[Text(t, color=PALETTE["dim"], font_size=22)
                           for t in ("A real log", "of the week.")]).arrange(DOWN, buff=0.15), 3.4)
        VGroup(phrase, rule, sub).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.8)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


def _article(h=1.7, icon_h=1.0, tag=None):
    parts = []
    if tag:
        parts.append(tag)
    parts += [("SUBSTACK · ARTICLE", 10, PALETTE["accent"], None),
              ("AI Done\nRight", 17, PALETTE["ink"], "BOLD"),
              ("trust, people, purpose", 10, PALETTE["dim"], None)]
    return hcard(article_icon(), parts, h=h, icon_h=icon_h)


def _videos(h=1.7, icon_h=1.4, tag=None):
    parts = []
    if tag:
        parts.append(tag)
    parts += [("two videos,\nfour files", 15, PALETTE["ink"], None),
              ("16:9 + 9:16 each", 11, PALETTE["dim"], None)]
    return hcard(two_videos_icon(), parts, h=h, icon_h=icon_h)


def _lecture(h=1.7, icon_h=0.95, tag=None, border=None, extra=None):
    parts = []
    if tag:
        parts.append(tag)
    parts += [("Guest lecture\nat MCPHS", 15, PALETTE["ink"], "BOLD"),
              ("with Yatra Rawat", 11, PALETTE["dim"], None)]
    if extra:
        parts.append(extra)
    return hcard(slides_icon(), parts, h=h, icon_h=icon_h, border=border)


class B04_FlatWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        a = _article(h=1.75)
        b = _videos(h=1.75)
        c = _lecture(h=1.75)
        VGroup(a, b, c).arrange(DOWN, buff=0.18).move_to(UP * 0.35)

        reveal(self, a, t1=0.4, t2=0.4)
        reveal(self, b, t1=0.4, t2=0.4)
        reveal(self, c, t1=0.4, t2=0.4)

        footer = lines("Same weight. No sense\nof the biggest piece.", 15, PALETTE["dim"], max_w=3.6, buff=0.08)
        footer.move_to(DOWN * 3.0)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B07_TaggedWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        a = _article(h=1.45, icon_h=0.8, tag=("WRITING", 10, PALETTE["good"], "BOLD"))
        b = _videos(h=1.45, icon_h=1.15, tag=("VIDEO", 10, PALETTE["dim"], "BOLD"))
        c = _lecture(h=1.45, icon_h=0.8, tag=("SPEAKING", 10, PALETTE["accent"], "BOLD"),
                     border=PALETTE["accent"], extra=("took the most time", 10, PALETTE["dim"], None))
        VGroup(a, b, c).arrange(DOWN, buff=0.15).move_to(UP * 0.8)

        reveal(self, a, t1=0.4, t2=0.4)
        reveal(self, b, t1=0.4, t2=0.4)
        reveal(self, c, t1=0.4, t2=0.4)

        count = chip("3 things shipped this week", w=3.6, h=0.8, border=PALETTE["accent"],
                     color=PALETTE["accent"], fs=18)
        count.move_to(DOWN * 2.6)
        self.play(FadeIn(count, shift=UP * 0.1), run_time=0.6)
        self.wait(1.3)


class B08_WhatItIs(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Humanitarians AI", color=PALETTE["ink"], font_size=20, weight="BOLD")
        badge = chip("501(c)(3) nonprofit", w=2.6, h=0.4, border=PALETTE["accent"], color=PALETTE["accent"], fs=13)
        idea = Text("one idea: AI for real-world good", color=PALETTE["dim"], font_size=12)
        focus = VGroup(chip("education", w=1.6, h=0.4, fs=12), chip("healthcare", w=1.6, h=0.4, fs=12),
                       chip("nonprofits", w=1.6, h=0.4, fs=12), chip("the arts", w=1.6, h=0.4, fs=12)
                       ).arrange_in_grid(rows=2, cols=2, buff=0.12)
        need = lines("real needs, no budget for a tech team", 11, PALETTE["ink"], max_w=3.3)
        l_inner = VGroup(title, badge, idea, focus, need).arrange(DOWN, buff=0.17)
        l_box = card_bg(3.7, 3.1)
        top = VGroup(l_box, l_inner.move_to(l_box.get_center()))
        top.move_to(UP * 1.8)

        mh = Text("The mission", color=PALETTE["accent"], font_size=17, weight="BOLD")
        ai = chip("AI", w=0.9, h=0.4, border=PALETTE["accent"], color=PALETTE["accent"], fs=15)
        big = VGroup(blocks_icon(PALETTE["dim"]).scale(0.8),
                     lines("big companies,\nbig budgets", 10, PALETTE["dim"], buff=0.04)).arrange(DOWN, buff=0.1)
        small = VGroup(VGroup(person(0.35, PALETTE["good"]), person(0.35, PALETTE["accent"]),
                              house_icon(PALETTE["ink"]).scale(0.8)).arrange(RIGHT, buff=0.1),
                       lines("small nonprofits,\nschools, causes", 10, PALETTE["accent"], buff=0.04)
                       ).arrange(DOWN, buff=0.1)
        groups = VGroup(big, small).arrange(RIGHT, buff=0.7)
        cant = lines("can't afford a developer\nor a marketing team", 11, PALETTE["ink"], buff=0.04)
        gap = Text("the gap we exist to fill", color=PALETTE["accent"], font_size=14, weight="BOLD")
        r_inner = VGroup(mh, ai, groups, cant, gap).arrange(DOWN, buff=0.2)
        r_box = card_bg(3.7, 3.3, stroke_color=PALETTE["accent"])
        bottom = VGroup(r_box, r_inner.move_to(r_box.get_center()))
        bottom.move_to(DOWN * 1.6)
        a1 = Arrow(ai.get_bottom(), big.get_top() + UP * 0.03, color=PALETTE["dim"], stroke_width=2, buff=0.05,
                   max_tip_length_to_length_ratio=0.3)
        a2 = Arrow(ai.get_bottom(), small.get_top() + UP * 0.03, color=PALETTE["accent"], stroke_width=3.5,
                   buff=0.05, max_tip_length_to_length_ratio=0.3)

        reveal(self, top)
        self.play(FadeIn(focus, shift=UP * 0.1), run_time=0.6)
        reveal(self, bottom, t2=0.3)
        self.play(GrowArrow(a1), run_time=0.5)
        self.play(GrowArrow(a2), run_time=0.7)
        self.wait(1.4)


class B09_HowItWorks(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        vol = VGroup(VGroup(person(0.4, PALETTE["good"]), person(0.4, PALETTE["accent"]),
                            person(0.4, PALETTE["ink"])).arrange(RIGHT, buff=0.08),
                     lines("graduate student\nvolunteers", 9, PALETTE["ink"], buff=0.03)).arrange(DOWN, buff=0.1)
        tb = RoundedRectangle(corner_radius=0.08, width=0.65, height=0.5, fill_color=PALETTE["bg"],
                               fill_opacity=1, stroke_color=PALETTE["accent"], stroke_width=2)
        tl = VGroup(*[Line(LEFT * 0.2, RIGHT * 0.2, color=PALETTE["dim"], stroke_width=2)
                      for _ in range(3)]).arrange(DOWN, buff=0.08).move_to(tb.get_center())
        tools = VGroup(VGroup(tb, tl), lines("real tools", 9, PALETTE["ink"], buff=0.03)).arrange(DOWN, buff=0.1)
        orgs = VGroup(house_icon(PALETTE["ink"]).scale(0.9), lines("real\norganizations", 9, PALETTE["ink"], buff=0.03)
                      ).arrange(DOWN, buff=0.1)
        arr = Arrow(LEFT * 0.2, RIGHT * 0.2, color=PALETTE["dim"], stroke_width=2.5, buff=0,
                    max_tip_length_to_length_ratio=0.4)
        flow = VGroup(vol, arr, tools, arr.copy(), orgs).arrange(RIGHT, buff=0.18)
        fit(flow, 3.4)
        benefits = VGroup(
            chip("hands-on AI experience beyond a class project", w=3.45, h=0.4, border=PALETTE["good"],
                 color=PALETTE["good"], fs=11),
            chip("real project work to point to", w=3.45, h=0.4, border=PALETTE["good"],
                 color=PALETTE["good"], fs=11),
            chip("a place to build skills between jobs", w=3.45, h=0.4, border=PALETTE["good"],
                 color=PALETTE["good"], fs=11),
        ).arrange(DOWN, buff=0.12)
        t_inner = VGroup(flow, benefits).arrange(DOWN, buff=0.3)
        t_box = card_bg(3.7, 3.2)
        top = VGroup(t_box, t_inner.move_to(t_box.get_center()))
        top.move_to(UP * 1.75)

        mh = Text("The Madison Project", color=PALETTE["ink"], font_size=17, weight="BOLD")
        ms = Text("named after Madison Avenue", color=PALETTE["dim"], font_size=11)
        lic = VGroup(chip("open source", w=3.0, h=0.36, fs=12), chip("MIT licensed", w=3.0, h=0.36, fs=12),
                     chip("free for anyone", w=3.0, h=0.36, fs=12)).arrange(DOWN, buff=0.1)
        d_box = card_bg(3.0, 0.7, stroke_color=PALETTE["accent"])
        d_t = Text("Substack · developer diary", color=PALETTE["accent"], font_size=12)
        d_l = Line(LEFT * 1.0, RIGHT * 1.0, color=PALETTE["border"], stroke_width=2)
        diary = VGroup(d_box, VGroup(d_t, d_l).arrange(DOWN, buff=0.1).move_to(d_box.get_center()))
        b_inner = VGroup(mh, ms, lic, diary).arrange(DOWN, buff=0.15)
        b_box = card_bg(3.7, 3.2, stroke_color=PALETTE["accent"])
        bottom = VGroup(b_box, b_inner.move_to(b_box.get_center()))
        bottom.move_to(DOWN * 1.65)

        reveal(self, top)
        self.play(FadeIn(flow, shift=UP * 0.1), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.1) for b in benefits], lag_ratio=0.3), run_time=1.2)
        reveal(self, bottom)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in lic], lag_ratio=0.3), run_time=1.0)
        self.play(FadeIn(diary, shift=UP * 0.1), run_time=0.6)
        self.wait(1.3)


class B10_CaseStudies(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lh = Text("Homes of Hope India", color=PALETTE["ink"], font_size=17, weight="BOLD")
        ls = Text("AI storytelling tool: Wilkes", color=PALETTE["dim"], font_size=11)
        frame = RoundedRectangle(corner_radius=0.06, width=0.8, height=0.55, fill_color=PALETTE["bg"],
                                  fill_opacity=1, stroke_color=PALETTE["dim"], stroke_width=2)
        play = Triangle(color=PALETTE["accent"], fill_color=PALETTE["accent"], fill_opacity=1,
                        stroke_width=0).scale(0.1).rotate(-PI / 2).move_to(frame.get_center())
        footage = VGroup(VGroup(frame, play), Text("interview footage", color=PALETTE["ink"], font_size=10)
                         ).arrange(DOWN, buff=0.08)
        arrow = Arrow(LEFT * 0.3, RIGHT * 0.3, color=PALETTE["accent"], stroke_width=3, buff=0,
                      max_tip_length_to_length_ratio=0.35)
        doc = article_icon().scale(0.7)
        story = VGroup(doc, Text("written story", color=PALETTE["ink"], font_size=10)).arrange(DOWN, buff=0.08)
        flow = VGroup(footage, arrow, story).arrange(RIGHT, buff=0.3)
        reviewed = chip("reviewed by people, then published", w=3.3, h=0.4, border=PALETTE["good"],
                        color=PALETTE["good"], fs=11)
        amp = lines("to amplify real voices,\nnot invent them", 13, PALETTE["accent"], buff=0.05, weight="BOLD")
        t_inner = VGroup(lh, ls, flow, reviewed, amp).arrange(DOWN, buff=0.16)
        t_box = card_bg(3.7, 3.3)
        top = VGroup(t_box, t_inner.move_to(t_box.get_center()))
        top.move_to(UP * 1.7)

        rh = fit(Text("Drone Documentary Initiative", color=PALETTE["ink"], font_size=15, weight="BOLD"), 3.4)
        rs = Text("a drone photography program for nonprofits", color=PALETTE["dim"], font_size=9)
        drone = drone_icon().scale(0.6)
        sb = RoundedRectangle(corner_radius=0.06, width=2.4, height=0.95, fill_color=PALETTE["water"],
                               fill_opacity=0.6, stroke_color=PALETTE["dim"], stroke_width=2)
        face = Circle(radius=0.15, fill_color=PALETTE["dim"], fill_opacity=0.8, stroke_width=0)
        face.move_to(sb.get_center() + LEFT * 0.6 + UP * 0.05)
        plate = Rectangle(width=0.42, height=0.15, fill_color=PALETTE["dim"], fill_opacity=0.8, stroke_width=0)
        plate.move_to(sb.get_center() + RIGHT * 0.6 + DOWN * 0.2)
        frame_g = VGroup(sb, face, plate)
        tags = VGroup(chip("auto-tagged footage", w=3.3, h=0.36, fs=11),
                      chip("faces and license plates auto-blurred", w=3.3, h=0.36, border=PALETTE["accent"],
                           color=PALETTE["accent"], fs=11)).arrange(DOWN, buff=0.1)
        b_inner = VGroup(rh, rs, drone, frame_g, tags).arrange(DOWN, buff=0.12)
        b_box = card_bg(3.7, 3.3, stroke_color=PALETTE["accent"])
        bottom = VGroup(b_box, b_inner.move_to(b_box.get_center()))
        bottom.move_to(DOWN * 1.7)
        blur1 = DashedVMobject(Circle(radius=0.25, color=PALETTE["accent"], stroke_width=2.5), num_dashes=12)
        blur1.move_to(face.get_center())
        blur2 = DashedVMobject(Rectangle(width=0.6, height=0.3, color=PALETTE["accent"], stroke_width=2.5),
                               num_dashes=14)
        blur2.move_to(plate.get_center())

        reveal(self, top)
        self.play(FadeIn(flow, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(reviewed, shift=UP * 0.1), FadeIn(amp, shift=UP * 0.1), run_time=0.7)
        reveal(self, bottom)
        self.play(FadeIn(drone, shift=DOWN * 0.1), FadeIn(frame_g), run_time=0.7)
        self.play(Create(blur1), Create(blur2), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in tags], lag_ratio=0.3), run_time=0.9)
        self.wait(1.3)


class B11_LoonProject(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = lines("Goal: conserve Minnesota's\nstate bird, the common loon", 15, PALETTE["ink"],
                     max_w=3.7, buff=0.06, weight="BOLD")
        head.move_to(UP * 3.0)

        lake = card_bg(3.7, 2.7)
        lake.move_to(UP * 1.1)
        lc = lake.get_center()
        water = Rectangle(width=3.4, height=1.4, fill_color=PALETTE["water"], fill_opacity=0.8, stroke_width=0)
        water.move_to(lc + DOWN * 0.55)
        waves = VGroup(*[Line(LEFT * 0.25, RIGHT * 0.25, color=PALETTE["card"], stroke_width=2).shift(
            lc + [x, y, 0]) for x, y in ((-1.2, -1.05), (0.1, -1.1), (1.2, -1.0))])
        drone = drone_icon().scale(0.7).move_to(lc + UP * 0.95)
        scan = DashedVMobject(Line(drone.get_bottom(), lc + DOWN * 0.15, color=PALETTE["accent"], stroke_width=2),
                              num_dashes=6)
        loons = VGroup(loon_icon(0.5).move_to(lc + [-1.05, -0.35, 0]),
                       loon_icon(0.5).move_to(lc + [0.1, -0.7, 0]),
                       loon_icon(0.5).move_to(lc + [1.1, -0.3, 0]))
        marks = VGroup(*[VGroup(Circle(radius=0.14, color=PALETTE["accent"], stroke_width=2.5),
                                Text(str(i + 1), color=PALETTE["accent"], font_size=11, weight="BOLD")
                                ).move_to(l.get_center() + UP * 0.38) for i, l in enumerate(loons)])
        for m in marks:
            m[1].move_to(m[0].get_center())

        th = Text("what it tracks", color=PALETTE["accent"], font_size=12, weight="BOLD")
        tracks = VGroup(chip("counts loons", w=1.65, h=0.38, fs=11), chip("habitat change", w=1.65, h=0.38, fs=11),
                        chip("shoreline erosion", w=1.65, h=0.38, fs=11)).arrange(DOWN, buff=0.12)
        left_c = VGroup(th, tracks).arrange(DOWN, buff=0.2)
        sh = Text("status", color=PALETTE["accent"], font_size=12, weight="BOLD")
        status = VGroup(chip("drone acquired", w=1.65, h=0.38, border=PALETTE["good"], color=PALETTE["good"], fs=11),
                        chip("one FAA exam", w=1.65, h=0.38, border=PALETTE["accent"], color=PALETTE["accent"], fs=11),
                        chip("certified flights", w=1.65, h=0.38, fs=11, color=PALETTE["dim"])).arrange(DOWN, buff=0.12)
        right_c = VGroup(sh, status).arrange(DOWN, buff=0.2)
        i_inner = VGroup(left_c, right_c).arrange(RIGHT, buff=0.2, aligned_edge=UP)
        i_box = card_bg(3.7, 2.2)
        info = VGroup(i_box, i_inner.move_to(i_box.get_center()))
        info.move_to(DOWN * 2.2)

        self.play(FadeIn(head, shift=DOWN * 0.1), run_time=0.5)
        reveal(self, VGroup(lake, VGroup(water, waves)))
        self.play(FadeIn(loons), run_time=0.7)
        self.play(FadeIn(drone, shift=DOWN * 0.1), Create(scan), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(m) for m in marks], lag_ratio=0.4), run_time=1.2)
        reveal(self, info)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in tracks], lag_ratio=0.3), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.1) for s in status], lag_ratio=0.3), run_time=0.9)
        self.wait(1.2)


class B12_WhyNowAndInvolved(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lh = Text("Why it matters now", color=PALETTE["ink"], font_size=18, weight="BOLD")
        badge_c = Circle(radius=0.22, color=PALETTE["good"], fill_color=PALETTE["good"], fill_opacity=0.15,
                         stroke_width=3)
        tick = VMobject(color=PALETTE["good"], stroke_width=3).set_points_as_corners(
            [badge_c.get_center() + [-0.09, 0, 0], badge_c.get_center() + [-0.02, -0.08, 0],
             badge_c.get_center() + [0.1, 0.09, 0]])
        r1 = VGroup(VGroup(badge_c, tick),
                    lines("real, verified content\ngains value as AI content\nfloods every platform", 12,
                          PALETTE["ink"], buff=0.05)).arrange(RIGHT, buff=0.25)
        r2 = VGroup(house_icon(PALETTE["ink"]).scale(0.8),
                    lines("small nonprofits need tech\nthey can't afford to build", 12,
                          PALETTE["ink"], buff=0.05)).arrange(RIGHT, buff=0.25)
        t_inner = VGroup(lh, r1, r2).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        t_box = card_bg(3.7, 2.8)
        top = VGroup(t_box, t_inner.move_to(t_box.get_center()))
        top.move_to(UP * 1.95)

        rh = Text("How to get involved", color=PALETTE["accent"], font_size=18, weight="BOLD")
        vol = chip("all volunteers · never about profit", w=3.4, h=0.42, border=PALETTE["good"],
                   color=PALETTE["good"], fs=12)
        acts = VGroup(chip("reach out", w=3.0, h=0.42, fs=13), chip("follow along on Substack", w=3.0, h=0.42, fs=13),
                      chip("or just come say hi", w=3.0, h=0.42, fs=13)).arrange(DOWN, buff=0.14)
        b_inner = VGroup(rh, vol, acts).arrange(DOWN, buff=0.24)
        b_box = card_bg(3.7, 3.0, stroke_color=PALETTE["accent"])
        bottom = VGroup(b_box, b_inner.move_to(b_box.get_center()))
        bottom.move_to(DOWN * 1.15)

        foot = lines("volunteers filling the gap,\ntool by tool", 13, PALETTE["dim"], max_w=3.6, buff=0.06)
        foot.move_to(DOWN * 3.07)

        reveal(self, top)
        self.play(FadeIn(r1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(r2, shift=UP * 0.1), run_time=0.6)
        reveal(self, bottom)
        self.play(FadeIn(vol, shift=UP * 0.1), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(a, shift=UP * 0.1) for a in acts], lag_ratio=0.3), run_time=1.0)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)
