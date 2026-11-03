"""
Portrait (9:16) Manim scenes for tutor-they-never-had-short

Ports of the five graphic beats kept in the Shorts cut (B00B, B01, B04, B07,
B08). Stacked layouts for a 4.5 x 8.0 frame; same palette and copy as the
16:9 scenes. Dropped beats (B02, B03, B05, B06) live only in the long cut.
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


class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = fit(Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=38), 3.4)
        summary = fit(Text(
            "Today: AI tutoring, and\nwhat it could mean for\nkids who have never\nhad extra help. The\nhopeful parts, and the\ncautions too.",
            color=PALETTE["ink"], font_size=24, line_spacing=1.3, should_center=True), 3.4)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.4)


class B01_StuckOnHomework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        kid = person(0.8)
        nb_box = card_bg(2.0, 1.3)
        eq = Text("7 x 8 = ?", color=PALETTE["ink"], font_size=26)
        nb = VGroup(nb_box, eq.move_to(nb_box.get_center()))
        row = VGroup(kid, nb).arrange(RIGHT, buff=0.4).move_to(UP * 1.8)

        bubble_c = Circle(radius=0.28, color=PALETTE["border"], fill_color=PALETTE["card"],
                          fill_opacity=1, stroke_width=1.5)
        bubble_q = Text("?", color=PALETTE["accent"], font_size=24, weight="BOLD")
        bubble = VGroup(bubble_c, bubble_q.move_to(bubble_c.get_center()))
        bubble.next_to(kid, UP, buff=0.15)

        self.play(FadeIn(kid, shift=UP * 0.1), FadeIn(nb), run_time=0.7)
        self.play(FadeIn(bubble, shift=UP * 0.1), run_time=0.5)

        head = Text("what happens next?", color=PALETTE["dim"], font_size=16)
        head.move_to(UP * 0.85)
        self.play(FadeIn(head), run_time=0.4)

        def path_card(title, sub, border):
            box = card_bg(3.5, 1.1, stroke_color=border)
            t = fit(Text(title, color=PALETTE["ink"], font_size=18, weight="BOLD"), 3.1)
            s = fit(Text(sub, color=PALETTE["dim"], font_size=13), 3.1)
            dot = Dot(radius=0.06, color=border)
            inner = VGroup(dot, t, s).arrange(DOWN, buff=0.12)
            return VGroup(box, inner.move_to(box.get_center()))

        p1 = path_card("A parent who can explain", "or a family that can pay a tutor", PALETTE["good"])
        p2 = path_card("No one to ask", "one missed lesson becomes a few", PALETTE["miss"])
        p1.move_to(UP * 0.1)
        p2.move_to(DOWN * 1.95)

        reveal(self, p1)
        o1 = chip("gets unstuck fast", w=2.4, h=0.5, border=PALETTE["good"], color=PALETTE["good"], fs=15)
        o1.move_to(DOWN * 0.75)
        self.play(FadeIn(o1, shift=UP * 0.1), run_time=0.4)

        orr = Text("or", color=PALETTE["dim"], font_size=16)
        orr.move_to(DOWN * 1.3)
        self.play(FadeIn(orr), run_time=0.3)

        reveal(self, p2)
        o2 = chip("\"I'm bad at math\"", w=2.4, h=0.5, border=PALETTE["miss"], color=PALETTE["miss"], fs=15)
        o2.move_to(DOWN * 2.9)
        self.play(FadeIn(o2, shift=UP * 0.1), run_time=0.4)
        self.wait(1.2)


class B04_EarlyResearch(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        chips = VGroup(
            chip("human tutors + AI software", w=3.6, h=0.5, fs=14),
            chip("furthest-behind gained most", w=3.6, h=0.5, fs=14),
            chip("tutors not stretched too thin", w=3.6, h=0.5, fs=14),
        ).arrange(DOWN, buff=0.14)
        chips.move_to(UP * 2.45)
        for c in chips:
            c[0].stretch(0.01, 0)
        self.play(
            LaggedStart(*[c[0].animate.stretch_to_fit_width(3.6) for c in chips], lag_ratio=0.2),
            LaggedStart(*[FadeIn(c[1]) for c in chips], lag_ratio=0.2),
            run_time=1.2,
        )

        title = Text("cost per student, per year", color=PALETTE["dim"], font_size=15)
        title.move_to(UP * 1.1)
        self.play(FadeIn(title), run_time=0.4)

        scale = 1.6 / 4300.0
        x0 = -1.8
        rows = [
            ("AI-assisted tutoring", 700, 700, "about $700", PALETTE["accent"], "one summary reports"),
            ("Private tutoring", 2500, 2500, "$2,500+", PALETTE["dim"], ""),
            ("Traditional intensive tutoring", 3500, 4300, "$3,500 - $4,300", PALETTE["dim"],
             "one summary reports"),
        ]
        y = 0.5
        for name, lo, hi, val, color, flag in rows:
            lbl = fit(Text(name, color=PALETTE["ink"], font_size=16), 3.6)
            lbl.move_to([x0 + lbl.width / 2, y, 0])
            by = y - 0.45
            bar = Rectangle(width=lo * scale, height=0.34, fill_color=color, fill_opacity=1,
                            stroke_width=0)
            bar.move_to([x0 + lo * scale / 2, by, 0])
            parts = [lbl, bar]
            if hi > lo:
                ext = Rectangle(width=(hi - lo) * scale, height=0.34, fill_color=color,
                                fill_opacity=0.35, stroke_width=0)
                ext.move_to([x0 + lo * scale + (hi - lo) * scale / 2, by, 0])
                parts.append(ext)
            end_x = x0 + hi * scale
            vtxt = Text(val, color=color if color == PALETTE["accent"] else PALETTE["ink"],
                        font_size=16, weight="BOLD")
            vtxt.move_to([end_x + 0.15 + vtxt.width / 2, by, 0])
            parts.append(vtxt)
            self.play(FadeIn(VGroup(*parts), shift=RIGHT * 0.15), run_time=0.55)
            if flag:
                ft = Text(flag, color=PALETTE["miss"], font_size=12)
                ft.move_to([x0 + ft.width / 2, by - 0.38, 0])
                self.play(FadeIn(ft), run_time=0.25)
            y -= 1.2

        foot = fit(Text("early results -- not a guarantee", color=PALETTE["dim"], font_size=15), 3.6)
        foot.move_to(DOWN * 3.2)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B07_AFairCaution(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        crowd = VGroup(*[
            Circle(radius=0.09, color=PALETTE["dim"], fill_color=PALETTE["dim"],
                   fill_opacity=0.8, stroke_width=0)
            for _ in range(40)
        ]).arrange_in_grid(rows=4, cols=10, buff=0.12)
        fit(crowd, 2.6)
        n = Text("2,000+", color=PALETTE["ink"], font_size=34, weight="BOLD")
        nl = Text("college students", color=PALETTE["dim"], font_size=17)
        res = fit(Text("AI-tutor group: slightly\nlower grades", color=PALETTE["miss"],
                        font_size=17, line_spacing=1.2, should_center=True), 3.2)
        inner = VGroup(crowd, n, nl, res).arrange(DOWN, buff=0.2)
        box = card_bg(3.7, 3.3, stroke_color=PALETTE["border"])
        study = VGroup(box, inner.move_to(box.get_center()))
        study.move_to(UP * 1.7)
        reveal(self, study)

        head = Text("what to keep in mind", color=PALETTE["accent"], font_size=19, weight="BOLD")
        rows = VGroup()
        for t in ["these were adults, not kids", "the researchers noted limits",
                  "how a tutor is built and used matters"]:
            d = Dot(radius=0.06, color=PALETTE["accent"])
            tx = fit(Text(t, color=PALETTE["ink"], font_size=16), 2.9)
            rows.add(VGroup(d, tx).arrange(RIGHT, buff=0.2))
        rows.arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        inner2 = VGroup(head, rows).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        box2 = card_bg(3.7, 3.0, stroke_color=PALETTE["accent"])
        keep = VGroup(box2, inner2.move_to(box2.get_center()))
        keep.move_to(DOWN * 1.7)
        reveal(self, keep, t2=0.3)
        for r in rows:
            self.play(Indicate(r, color=PALETTE["accent"], scale_factor=1.04), run_time=0.5)
        self.wait(1.2)


class B08_TheClosingIdea(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        gy = 0.9
        ground = Line(LEFT * 1.8, RIGHT * 1.8, color=PALETTE["border"], stroke_width=3)
        ground.move_to(UP * gy)

        desk_top = gy + 0.75
        desk = RoundedRectangle(corner_radius=0.05, width=1.7, height=0.14,
                                 fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0)
        desk.move_to([-0.95, desk_top, 0])
        leg_h = desk_top - gy - 0.07
        legs = VGroup(
            Rectangle(width=0.08, height=leg_h, fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0),
            Rectangle(width=0.08, height=leg_h, fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0),
        )
        legs[0].move_to([-1.7, gy + leg_h / 2, 0])
        legs[1].move_to([-0.2, gy + leg_h / 2, 0])
        kid = person(0.8, PALETTE["ink"])
        kid.move_to([-1.5, gy + kid.height / 2, 0])
        laptop_s = RoundedRectangle(corner_radius=0.05, width=0.7, height=0.45,
                                     fill_color=PALETTE["bg"], fill_opacity=1,
                                     stroke_color=PALETTE["ink"], stroke_width=2)
        laptop_s.move_to([-0.6, desk_top + 0.3, 0])
        glow = Dot(laptop_s.get_center(), radius=0.06, color=PALETTE["accent"])

        self.play(FadeIn(VGroup(ground, legs, desk, kid), shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(VGroup(laptop_s, glow)), run_time=0.5)

        adult = person(1.2, PALETTE["good"])
        adult.move_to([1.2, gy + adult.height / 2, 0])
        halo = RoundedRectangle(corner_radius=0.35, width=3.7, height=2.7,
                                 stroke_color=PALETTE["accent"], stroke_width=2.5,
                                 fill_opacity=0).set_stroke(opacity=0.5)
        halo.move_to([0, gy + 0.85, 0])
        near_l = Text("beside them", color=PALETTE["accent"], font_size=20, weight="BOLD")
        near_l.move_to([0, 0.15, 0])
        roles = fit(Text("teacher  /  volunteer  /  mentor", color=PALETTE["dim"], font_size=15), 3.5)
        roles.move_to([0, -0.3, 0])
        self.play(FadeIn(adult, shift=LEFT * 0.2), run_time=0.7)
        self.play(Create(halo), run_time=0.7)
        self.play(FadeIn(near_l), FadeIn(roles), run_time=0.5)

        q = fit(Text("Can it reach the child\nwho needs it -- and\nwho will be there\nbeside them?",
                     color=PALETTE["ink"], font_size=24, weight="BOLD",
                     line_spacing=1.2, should_center=True), 3.4)
        q.move_to([0, -2.0, 0])
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.7)
        self.wait(1.5)
