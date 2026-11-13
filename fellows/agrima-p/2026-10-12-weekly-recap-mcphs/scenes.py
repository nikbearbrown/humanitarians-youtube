"""
Manim scenes for weekly-recap-mcphs

A first-person, honest weekly-progress CLI-explainer. The two OUTPUT beats
visualize the REAL output of weekly_recap_v1.py / weekly_recap_v2.py. About
half of the runtime summarizes the Humanitarians AI guest-lecture
presentation; every visual here is a generated graphic (no slide images, no
photos). No personal information about any individual appears in this file.
Built in the house Claude palette.

B01_NotAHighlightReel   -- typographic card: "Not a highlight reel."
B04_FlatWeek            -- three same-weight cards: article / two videos / lecture
B07_TaggedWeek          -- the same three, tagged WRITING / VIDEO / SPEAKING + count
B08_WhatItIs            -- organization card + the mission (big budgets vs left behind)
B09_HowItWorks          -- volunteers -> tools -> organizations; the Madison Project
B10_CaseStudies         -- Homes of Hope India (footage -> reviewed stories); drone documentary
B11_LoonProject         -- lake, loons, drone; what it tracks; status track
B12_WhyNowAndInvolved   -- why it matters now + how to get involved
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


def lines(txt, fs, color, max_w=None, buff=0.12, weight=None):
    """Centered multi-line label: one Text per line, stacked and centered."""
    kw = {"weight": weight} if weight else {}
    g = VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split("\n")]).arrange(DOWN, buff=buff)
    return fit(g, max_w) if max_w else g


def reveal(scene, card, t1=0.35, t2=0.4):
    """Box grows first, then its contents fade in (no content hanging past a growing box)."""
    box, inner = card[0], card[1]
    w = box.width
    box.stretch(0.01, 0)
    scene.play(box.animate.stretch_to_fit_width(w), run_time=t1)
    scene.play(FadeIn(inner), run_time=t2)


def chip(label, w=2.6, h=0.6, border=None, color=None, fs=16):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(Text(label, color=color or PALETTE["ink"], font_size=fs), w - 0.3)
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
    bs = VGroup(*[Rectangle(width=0.22, height=h, fill_color=color, fill_opacity=1, stroke_width=0)
                  for h in (0.55, 0.85, 0.65)]).arrange(RIGHT, buff=0.05, aligned_edge=DOWN)
    return bs


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
    g = VGroup(body, neck, head, beak, spots)
    return g.scale(scale)


# --- scenes -----------------------------------------------------------------

class B01_NotAHighlightReel(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        phrase = Text("Not a highlight reel.", color=PALETTE["ink"], font_size=40)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        sub = Text("A real log of the week.", color=PALETTE["dim"], font_size=20)

        VGroup(phrase, rule, sub).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.8)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


def _article_card(w=3.8, h=3.6, tag=None):
    box = card_bg(w, h)
    dots = VGroup(*[Circle(radius=0.045, color=PALETTE["border"], fill_color=PALETTE["border"],
                           fill_opacity=1, stroke_width=0) for _ in range(3)]).arrange(RIGHT, buff=0.09)
    rule = Line(LEFT * (w * 0.32), RIGHT * (w * 0.32), color=PALETTE["border"], stroke_width=1.5)
    header = VGroup(dots, rule).arrange(DOWN, buff=0.1)
    kicker = Text("SUBSTACK · ARTICLE", color=PALETTE["accent"], font_size=11)
    title = lines("AI Done\nRight", 22, PALETTE["ink"], weight="BOLD", buff=0.08)
    by = fit(Text("trust, people, purpose", color=PALETTE["dim"], font_size=12), w - 0.4)
    parts = [header, kicker, title, by]
    if tag:
        parts.insert(0, tag)
    inner = VGroup(*parts).arrange(DOWN, buff=0.2)
    return VGroup(box, inner.move_to(box.get_center()))


def _videos_card(w=3.8, h=3.6, tag=None):
    box = card_bg(w, h)
    icon = two_videos_icon()
    t = Text("two videos · four files", color=PALETTE["ink"], font_size=14)
    parts = [icon, fit(t, w - 0.4)]
    if tag:
        parts.insert(0, tag)
    inner = VGroup(*parts).arrange(DOWN, buff=0.22)
    return VGroup(box, inner.move_to(box.get_center()))


def _lecture_card(w=3.8, h=3.6, tag=None, border=None):
    box = card_bg(w, h, stroke_color=border)
    icon = slides_icon()
    t1 = fit(Text("Guest lecture at MCPHS", color=PALETTE["ink"], font_size=16, weight="BOLD"), w - 0.4)
    t2 = Text("with Yatra Rawat", color=PALETTE["dim"], font_size=13)
    t3 = lines("Massachusetts College of Pharmacy\nand Health Sciences", 9, PALETTE["dim"], max_w=w - 0.4,
               buff=0.04)
    parts = [icon, t1, t2, t3]
    if tag:
        parts.insert(0, tag)
    inner = VGroup(*parts).arrange(DOWN, buff=0.18)
    return VGroup(box, inner.move_to(box.get_center()))


class B04_FlatWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        a = _article_card()
        b = _videos_card()
        c = _lecture_card()
        VGroup(a, b, c).arrange(RIGHT, buff=0.4).move_to(UP * 0.1)

        reveal(self, a, t1=0.4, t2=0.4)
        reveal(self, b, t1=0.4, t2=0.4)
        reveal(self, c, t1=0.4, t2=0.4)

        footer = Text("Same weight. No sense of the biggest piece.", color=PALETTE["dim"],
                      font_size=17).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B07_TaggedWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        def tag(label, color):
            return chip(label, w=1.7, h=0.4, border=color, color=color, fs=12)

        a = _article_card(h=3.4, tag=tag("WRITING", PALETTE["good"]))
        b = _videos_card(h=3.4, tag=tag("VIDEO", PALETTE["dim"]))
        c = _lecture_card(h=3.4, tag=tag("SPEAKING", PALETTE["accent"]), border=PALETTE["accent"])
        VGroup(a, b, c).arrange(RIGHT, buff=0.4).move_to(UP * 0.55)

        reveal(self, a, t1=0.4, t2=0.4)
        reveal(self, b, t1=0.4, t2=0.4)
        reveal(self, c, t1=0.4, t2=0.4)

        count = chip("3 things shipped this week", w=5.2, h=0.8, border=PALETTE["accent"],
                     color=PALETTE["accent"], fs=22)
        count.move_to(DOWN * 2.45)
        self.play(FadeIn(count, shift=UP * 0.1), run_time=0.6)
        note = Text("the lecture took the most time", color=PALETTE["dim"], font_size=16)
        note.next_to(c, DOWN, buff=0.25)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.3)


class B08_WhatItIs(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # left: the organization
        title = Text("Humanitarians AI", color=PALETTE["ink"], font_size=26, weight="BOLD")
        badge = chip("501(c)(3) nonprofit", w=3.0, h=0.5, border=PALETTE["accent"],
                     color=PALETTE["accent"], fs=16)
        idea = Text("one idea: AI for real-world good", color=PALETTE["dim"], font_size=17)
        focus = VGroup(
            chip("education", w=2.3, h=0.5, fs=16), chip("healthcare", w=2.3, h=0.5, fs=16),
            chip("nonprofits", w=2.3, h=0.5, fs=16), chip("the arts", w=2.3, h=0.5, fs=16),
        ).arrange_in_grid(rows=2, cols=2, buff=0.2)
        need = lines("real needs, no budget\nfor a tech team", 16, PALETTE["ink"], buff=0.08)
        l_inner = VGroup(title, badge, idea, focus, need).arrange(DOWN, buff=0.3)
        l_box = card_bg(5.6, 5.4)
        left = VGroup(l_box, l_inner.move_to(l_box.get_center()))
        left.move_to(LEFT * 3.4)

        # right: the mission
        mh = Text("The mission", color=PALETTE["accent"], font_size=22, weight="BOLD")
        ai = chip("AI", w=1.2, h=0.55, border=PALETTE["accent"], color=PALETTE["accent"], fs=20)
        big = VGroup(blocks_icon(PALETTE["dim"]), lines("big companies,\nbig budgets", 13, PALETTE["dim"], buff=0.05)
                     ).arrange(DOWN, buff=0.15)
        small = VGroup(VGroup(person(0.4, PALETTE["good"]), person(0.4, PALETTE["accent"]),
                              house_icon(PALETTE["ink"])).arrange(RIGHT, buff=0.12),
                       lines("small nonprofits,\nschools, causes", 13, PALETTE["accent"], buff=0.05)
                       ).arrange(DOWN, buff=0.15)
        groups = VGroup(big, small).arrange(RIGHT, buff=1.1)
        a1 = Arrow(ai.get_bottom(), big.get_top() + UP * 0.05, color=PALETTE["dim"], stroke_width=2.5,
                   buff=0.1, max_tip_length_to_length_ratio=0.2)
        a2 = Arrow(ai.get_bottom(), small.get_top() + UP * 0.05, color=PALETTE["accent"], stroke_width=4,
                   buff=0.1, max_tip_length_to_length_ratio=0.2)
        cant = lines("can't afford a developer\nor a marketing team", 14, PALETTE["ink"], buff=0.06)
        gap = Text("the gap we exist to fill", color=PALETTE["accent"], font_size=18, weight="BOLD")
        r_inner = VGroup(mh, ai, groups, cant, gap).arrange(DOWN, buff=0.35)
        r_box = card_bg(5.6, 5.4, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, r_inner.move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.4)
        # arrows depend on final positions
        ai_c = ai.get_bottom()
        a1 = Arrow(ai_c, big.get_top() + UP * 0.05, color=PALETTE["dim"], stroke_width=2.5, buff=0.08,
                   max_tip_length_to_length_ratio=0.25)
        a2 = Arrow(ai_c, small.get_top() + UP * 0.05, color=PALETTE["accent"], stroke_width=4, buff=0.08,
                   max_tip_length_to_length_ratio=0.25)

        reveal(self, left)
        self.play(FadeIn(focus, shift=UP * 0.1), run_time=0.6)
        reveal(self, right, t2=0.3)
        self.play(GrowArrow(a1), run_time=0.5)
        self.play(GrowArrow(a2), run_time=0.7)
        self.wait(1.4)


class B09_HowItWorks(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # left: volunteers -> tools -> organizations
        vol = VGroup(VGroup(person(0.5, PALETTE["good"]), person(0.5, PALETTE["accent"]),
                            person(0.5, PALETTE["ink"])).arrange(RIGHT, buff=0.1),
                     lines("graduate student\nvolunteers", 12, PALETTE["ink"], buff=0.04)).arrange(DOWN, buff=0.15)
        tool_box = RoundedRectangle(corner_radius=0.08, width=0.8, height=0.6, fill_color=PALETTE["bg"],
                                     fill_opacity=1, stroke_color=PALETTE["accent"], stroke_width=2)
        tool_ln = VGroup(*[Line(LEFT * 0.25, RIGHT * 0.25, color=PALETTE["dim"], stroke_width=2)
                           for _ in range(3)]).arrange(DOWN, buff=0.1).move_to(tool_box.get_center())
        tools = VGroup(VGroup(tool_box, tool_ln), lines("real tools", 12, PALETTE["ink"], buff=0.04)
                       ).arrange(DOWN, buff=0.15)
        orgs = VGroup(house_icon(PALETTE["ink"]), lines("real\norganizations", 12, PALETTE["ink"], buff=0.04)
                      ).arrange(DOWN, buff=0.15)
        arr_a = Arrow(LEFT * 0.3, RIGHT * 0.3, color=PALETTE["dim"], stroke_width=3, buff=0,
                      max_tip_length_to_length_ratio=0.35)
        arr_b = arr_a.copy()
        flow = VGroup(vol, arr_a, tools, arr_b, orgs).arrange(RIGHT, buff=0.3)
        benefits = VGroup(
            chip("hands-on AI experience beyond a class project", w=5.4, h=0.5, border=PALETTE["good"],
                 color=PALETTE["good"], fs=14),
            chip("real project work to point to", w=5.4, h=0.5, border=PALETTE["good"],
                 color=PALETTE["good"], fs=14),
            chip("a place to build skills between jobs", w=5.4, h=0.5, border=PALETTE["good"],
                 color=PALETTE["good"], fs=14),
        ).arrange(DOWN, buff=0.18)
        l_inner = VGroup(flow, benefits).arrange(DOWN, buff=0.5)
        l_box = card_bg(6.1, 5.2)
        left = VGroup(l_box, l_inner.move_to(l_box.get_center()))
        left.move_to(LEFT * 3.15)

        # right: the Madison Project
        mh = Text("The Madison Project", color=PALETTE["ink"], font_size=22, weight="BOLD")
        ms = Text("named after Madison Avenue", color=PALETTE["dim"], font_size=14)
        lic = VGroup(
            chip("open source", w=3.8, h=0.5, fs=15), chip("MIT licensed", w=3.8, h=0.5, fs=15),
            chip("free for anyone", w=3.8, h=0.5, fs=15),
        ).arrange(DOWN, buff=0.15)
        dry_box = card_bg(3.8, 1.1, stroke_color=PALETTE["accent"])
        dry_t = Text("Substack · developer diary", color=PALETTE["accent"], font_size=14)
        dry_l = VGroup(*[Line(LEFT * (1.3 - 0.4 * i), RIGHT * (1.3 - 0.4 * i), color=PALETTE["border"],
                              stroke_width=2) for i in range(2)]).arrange(DOWN, buff=0.1)
        diary = VGroup(dry_box, VGroup(dry_t, dry_l).arrange(DOWN, buff=0.15).move_to(dry_box.get_center()))
        r_inner = VGroup(mh, ms, lic, diary).arrange(DOWN, buff=0.3)
        r_box = card_bg(5.0, 5.2, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, r_inner.move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.6)

        reveal(self, left)
        self.play(FadeIn(flow, shift=UP * 0.1), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.1) for b in benefits], lag_ratio=0.3), run_time=1.2)
        reveal(self, right)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in lic], lag_ratio=0.3), run_time=1.0)
        self.play(FadeIn(diary, shift=UP * 0.1), run_time=0.6)
        self.wait(1.3)


class B10_CaseStudies(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # left: Homes of Hope India (icons only -- no photos)
        lh = Text("Homes of Hope India", color=PALETTE["ink"], font_size=22, weight="BOLD")
        ls = Text("AI storytelling tool: Wilkes", color=PALETTE["dim"], font_size=14)
        frame = RoundedRectangle(corner_radius=0.06, width=1.0, height=0.7, fill_color=PALETTE["bg"],
                                  fill_opacity=1, stroke_color=PALETTE["dim"], stroke_width=2)
        play = Triangle(color=PALETTE["accent"], fill_color=PALETTE["accent"], fill_opacity=1,
                        stroke_width=0).scale(0.12).rotate(-PI / 2).move_to(frame.get_center())
        footage = VGroup(VGroup(frame, play), Text("interview footage", color=PALETTE["ink"], font_size=12)
                         ).arrange(DOWN, buff=0.12)
        arrow = Arrow(LEFT * 0.4, RIGHT * 0.4, color=PALETTE["accent"], stroke_width=3, buff=0,
                      max_tip_length_to_length_ratio=0.3)
        doc = article_icon()
        story = VGroup(doc, Text("written story", color=PALETTE["ink"], font_size=12)).arrange(DOWN, buff=0.12)
        flow = VGroup(footage, arrow, story).arrange(RIGHT, buff=0.35)
        reviewed = chip("reviewed by people, then published", w=4.6, h=0.55, border=PALETTE["good"],
                        color=PALETTE["good"], fs=14)
        amp = lines("to amplify real voices,\nnot invent them", 17, PALETTE["accent"], buff=0.08,
                    weight="BOLD")
        l_inner = VGroup(lh, ls, flow, reviewed, amp).arrange(DOWN, buff=0.3)
        l_box = card_bg(5.6, 5.4)
        left = VGroup(l_box, l_inner.move_to(l_box.get_center()))
        left.move_to(LEFT * 3.4)

        # right: Drone Documentary Initiative
        rh = Text("Drone Documentary Initiative", color=PALETTE["ink"], font_size=20, weight="BOLD")
        rs = Text("a drone photography program for nonprofits", color=PALETTE["dim"], font_size=13)
        drone = drone_icon()
        scene_box = RoundedRectangle(corner_radius=0.06, width=3.4, height=1.7, fill_color=PALETTE["water"],
                                      fill_opacity=0.6, stroke_color=PALETTE["dim"], stroke_width=2)
        face = Circle(radius=0.22, fill_color=PALETTE["dim"], fill_opacity=0.8, stroke_width=0)
        face.move_to(scene_box.get_center() + LEFT * 0.8 + UP * 0.1)
        plate = Rectangle(width=0.6, height=0.22, fill_color=PALETTE["dim"], fill_opacity=0.8, stroke_width=0)
        plate.move_to(scene_box.get_center() + RIGHT * 0.8 + DOWN * 0.3)
        blur1 = DashedVMobject(Circle(radius=0.36, color=PALETTE["accent"], stroke_width=3), num_dashes=14)
        blur1.move_to(face.get_center())
        blur2 = DashedVMobject(Rectangle(width=0.85, height=0.45, color=PALETTE["accent"], stroke_width=3),
                               num_dashes=16)
        blur2.move_to(plate.get_center())
        frame_g = VGroup(scene_box, face, plate)
        tags = VGroup(
            chip("auto-tagged footage", w=4.2, h=0.5, fs=14),
            chip("faces and license plates auto-blurred", w=4.2, h=0.5, border=PALETTE["accent"],
                 color=PALETTE["accent"], fs=14),
        ).arrange(DOWN, buff=0.15)
        r_inner = VGroup(rh, rs, drone, frame_g, tags).arrange(DOWN, buff=0.2)
        r_box = card_bg(5.6, 5.4, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, r_inner.move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.4)
        # blur outlines follow the final positions
        blur1.move_to(face.get_center())
        blur2.move_to(plate.get_center())

        reveal(self, left)
        self.play(FadeIn(flow, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(reviewed, shift=UP * 0.1), FadeIn(amp, shift=UP * 0.1), run_time=0.7)
        reveal(self, right)
        self.play(FadeIn(drone, shift=DOWN * 0.1), FadeIn(frame_g), run_time=0.7)
        self.play(Create(blur1), Create(blur2), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in tags], lag_ratio=0.3), run_time=0.9)
        self.wait(1.3)


class B11_LoonProject(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = Text("Goal: conserve Minnesota's state bird, the common loon", color=PALETTE["ink"],
                    font_size=20, weight="BOLD")
        head.move_to(UP * 3.0)

        # left: lake scene
        lake = card_bg(7.2, 5.0)
        lake.move_to(LEFT * 2.5 + DOWN * 0.3)
        lc = lake.get_center()
        water = Rectangle(width=6.8, height=2.5, fill_color=PALETTE["water"], fill_opacity=0.8, stroke_width=0)
        water.move_to(lc + DOWN * 0.95)
        waves = VGroup(*[Line(LEFT * 0.4, RIGHT * 0.4, color=PALETTE["card"], stroke_width=2).shift(
            lc + [x, y, 0]) for x, y in ((-2.7, -1.9), (-0.5, -2.0), (2.2, -1.85), (0.9, -1.6), (-2.2, -1.4))])
        drone = drone_icon().move_to(lc + UP * 1.55)
        scan = DashedVMobject(Line(drone.get_bottom(), lc + DOWN * 0.6, color=PALETTE["accent"], stroke_width=2),
                              num_dashes=8)
        loons = VGroup(loon_icon(0.75).move_to(lc + [-1.9, -0.7, 0]),
                       loon_icon(0.75).move_to(lc + [0.2, -1.15, 0]),
                       loon_icon(0.75).move_to(lc + [2.0, -0.6, 0]))
        marks = VGroup(*[VGroup(Circle(radius=0.2, color=PALETTE["accent"], stroke_width=3),
                                Text(str(i + 1), color=PALETTE["accent"], font_size=16, weight="BOLD")
                                ).move_to(l.get_center() + UP * 0.55) for i, l in enumerate(loons)])
        for m in marks:
            m[1].move_to(m[0].get_center())
        shore = Text("lakes, from above", color=PALETTE["dim"], font_size=13).move_to(lc + DOWN * 2.05)

        # right: what it tracks + status
        th = Text("what it tracks", color=PALETTE["accent"], font_size=18, weight="BOLD")
        tracks = VGroup(chip("counts loons", w=3.3, h=0.5, fs=15),
                        chip("habitat change", w=3.3, h=0.5, fs=15),
                        chip("shoreline erosion", w=3.3, h=0.5, fs=15)).arrange(DOWN, buff=0.15)
        sh = Text("status", color=PALETTE["accent"], font_size=18, weight="BOLD")
        s1 = chip("drone acquired", w=3.3, h=0.5, border=PALETTE["good"], color=PALETTE["good"], fs=15)
        s2 = chip("one FAA exam to go", w=3.3, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=15)
        s3 = chip("certified flights", w=3.3, h=0.5, fs=15, color=PALETTE["dim"])
        status = VGroup(s1, s2, s3).arrange(DOWN, buff=0.15)
        r_inner = VGroup(th, tracks, sh, status).arrange(DOWN, buff=0.24)
        r_box = card_bg(4.1, 5.0)
        right = VGroup(r_box, r_inner.move_to(r_box.get_center()))
        right.move_to(RIGHT * 4.1 + DOWN * 0.3)

        self.play(FadeIn(head, shift=DOWN * 0.1), run_time=0.5)
        reveal(self, VGroup(lake, VGroup(water, waves, shore)))
        self.play(FadeIn(loons), run_time=0.7)
        self.play(FadeIn(drone, shift=DOWN * 0.1), Create(scan), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(m) for m in marks], lag_ratio=0.4), run_time=1.2)
        reveal(self, right)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in tracks], lag_ratio=0.3), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.1) for s in status], lag_ratio=0.3), run_time=0.9)
        self.wait(1.2)


class B12_WhyNowAndInvolved(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lh = Text("Why it matters now", color=PALETTE["ink"], font_size=24, weight="BOLD")

        def row(icon, txt):
            t = lines(txt, 17, PALETTE["ink"], max_w=3.8, buff=0.08)
            return VGroup(icon, t).arrange(RIGHT, buff=0.35)
        badge_c = Circle(radius=0.3, color=PALETTE["good"], fill_color=PALETTE["good"], fill_opacity=0.15,
                         stroke_width=3)
        tick = VMobject(color=PALETTE["good"], stroke_width=4).set_points_as_corners(
            [badge_c.get_center() + [-0.12, -0.0, 0], badge_c.get_center() + [-0.03, -0.1, 0],
             badge_c.get_center() + [0.13, 0.12, 0]])
        r1 = row(VGroup(badge_c, tick), "real, verified content\ngains value as AI content\nfloods every platform")
        r2 = row(house_icon(PALETTE["ink"]), "small nonprofits need tech\nthey can't afford to build")
        l_inner = VGroup(lh, r1, r2).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        l_box = card_bg(5.9, 4.6)
        left = VGroup(l_box, l_inner.move_to(l_box.get_center()))
        left.move_to(LEFT * 3.3 + UP * 0.2)

        rh = Text("How to get involved", color=PALETTE["accent"], font_size=24, weight="BOLD")
        vol = chip("all volunteers  ·  never about profit", w=4.6, h=0.55, border=PALETTE["good"],
                   color=PALETTE["good"], fs=15)
        acts = VGroup(chip("reach out", w=4.2, h=0.55, fs=16), chip("follow along on Substack", w=4.2, h=0.55, fs=16),
                      chip("or just come say hi", w=4.2, h=0.55, fs=16)).arrange(DOWN, buff=0.18)
        r_inner = VGroup(rh, vol, acts).arrange(DOWN, buff=0.4)
        r_box = card_bg(5.6, 4.6, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, r_inner.move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.4 + UP * 0.2)

        reveal(self, left)
        self.play(FadeIn(r1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(r2, shift=UP * 0.1), run_time=0.6)
        reveal(self, right)
        self.play(FadeIn(vol, shift=UP * 0.1), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(a, shift=UP * 0.1) for a in acts], lag_ratio=0.3), run_time=1.0)
        foot = Text("volunteers filling the gap, tool by tool", color=PALETTE["dim"], font_size=18)
        foot.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)
