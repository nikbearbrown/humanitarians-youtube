"""
Manim scenes for tutor-they-never-had

A warm, neutral, personal explainer on AI tutoring for kids who have never had
extra help, sourced from the user-supplied article "The Tutor They Never Had:
What AI Tutoring Could Mean for Kids Who Have Never Had Extra Help." No
dedicated footage exists (per the user's materials note) -- every visual below
is a generated Manim graphic. Built in the house Claude palette.

B00B_AgrimaIntro        -- presenter card: "Hi, I'm Agrima." + lead-in
B01_StuckOnHomework     -- a kid stuck on math, two paths (help vs. no one to ask)
B02_TheAccessGap        -- $2,500+ per student; ~16 million children waiting
B03_ThePatientTutor     -- a patient tutor that never minds the same question twice
B04_EarlyResearch       -- hybrid human+AI findings and the cost comparison bars
B05_GhanaWhatsApp       -- simplified map, Ghana highlighted, WhatsApp-style tutor
B06_ReachingTheChild    -- a device is not time, a quiet space, a reason to continue
B07_AFairCaution        -- the college-student study and its limits
B08_TheClosingIdea      -- a child with a device and a caring adult nearby
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

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=40)
        summary = Text(
            "Today: AI tutoring, and what it\ncould mean for kids who have\n"
            "never had extra help. The hopeful\nparts, and the cautions too.",
            color=PALETTE["ink"], font_size=24, line_spacing=1.3, should_center=True)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.4)


class B01_StuckOnHomework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        kid = person(1.0)
        nb_box = card_bg(2.5, 1.7)
        eq = Text("7 x 8 = ?", color=PALETTE["ink"], font_size=30)
        nb = VGroup(nb_box, eq.move_to(nb_box.get_center()))
        left = VGroup(kid, nb).arrange(RIGHT, buff=0.5).move_to(LEFT * 4.0 + DOWN * 0.3)

        bubble_c = Circle(radius=0.32, color=PALETTE["border"], fill_color=PALETTE["card"],
                          fill_opacity=1, stroke_width=1.5)
        bubble_q = Text("?", color=PALETTE["accent"], font_size=28, weight="BOLD")
        bubble = VGroup(bubble_c, bubble_q.move_to(bubble_c.get_center()))
        bubble.next_to(kid, UP, buff=0.3)

        self.play(FadeIn(kid, shift=UP * 0.1), FadeIn(nb), run_time=0.7)
        self.play(FadeIn(bubble, shift=UP * 0.1), run_time=0.5)

        def path_card(title, sub, border):
            box = card_bg(3.7, 1.25, stroke_color=border)
            t = fit(Text(title, color=PALETTE["ink"], font_size=19, weight="BOLD"), 3.3)
            s = fit(Text(sub, color=PALETTE["dim"], font_size=14), 3.3)
            dot = Dot(radius=0.06, color=border)
            inner = VGroup(dot, t, s).arrange(DOWN, buff=0.14)
            return VGroup(box, inner.move_to(box.get_center()))

        p1 = path_card("A parent who can explain", "or a family that can pay a tutor", PALETTE["good"])
        p2 = path_card("No one to ask", "one missed lesson becomes a few", PALETTE["miss"])
        p1.move_to(RIGHT * 1.7 + UP * 1.5)
        p2.move_to(RIGHT * 1.7 + DOWN * 1.9)

        a1 = Arrow(left.get_right() + RIGHT * 0.1, p1.get_left(), color=PALETTE["good"],
                   stroke_width=3, buff=0.15, max_tip_length_to_length_ratio=0.12)
        a2 = Arrow(left.get_right() + RIGHT * 0.1, p2.get_left(), color=PALETTE["miss"],
                   stroke_width=3, buff=0.15, max_tip_length_to_length_ratio=0.12)

        self.play(GrowArrow(a1), run_time=0.4)
        reveal(self, p1)
        o1 = chip("gets unstuck fast", w=2.4, border=PALETTE["good"], color=PALETTE["good"], fs=16)
        o1.next_to(p1, RIGHT, buff=0.3)
        self.play(FadeIn(o1, shift=LEFT * 0.1), run_time=0.4)

        self.play(GrowArrow(a2), run_time=0.4)
        reveal(self, p2)
        o2 = chip("\"I'm bad at math\"", w=2.4, border=PALETTE["miss"], color=PALETTE["miss"], fs=16)
        o2.next_to(p2, RIGHT, buff=0.3)
        self.play(FadeIn(o2, shift=LEFT * 0.1), run_time=0.4)

        note = Text("not a lack of ability -- a lack of help", color=PALETTE["dim"], font_size=17)
        note.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B02_TheAccessGap(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # left: private tutoring cost
        cost_box = card_bg(4.8, 4.3, stroke_color=PALETTE["border"])
        coin = Circle(radius=0.38, color=PALETTE["accent"], fill_color=PALETTE["accent"],
                      fill_opacity=0.15, stroke_width=2.5)
        coin_s = Text("$", color=PALETTE["accent"], font_size=30, weight="BOLD")
        coin_g = VGroup(coin, coin_s.move_to(coin.get_center()))
        big = Text("$2,500+", color=PALETTE["ink"], font_size=50, weight="BOLD")
        lbl = fit(Text("private tutoring,\nper student", color=PALETTE["dim"], font_size=19,
                        line_spacing=1.25, should_center=True), 4.2)
        cost_inner = VGroup(coin_g, big, lbl).arrange(DOWN, buff=0.3)
        cost = VGroup(cost_box, cost_inner.move_to(cost_box.get_center()))
        cost.move_to(LEFT * 3.4 + UP * 0.2)

        # right: 16 dots = 16 million children
        dots_box = card_bg(5.4, 4.3, stroke_color=PALETTE["border"])
        dots = VGroup(*[
            Circle(radius=0.17, color=PALETTE["accent"], fill_color=PALETTE["accent"],
                   fill_opacity=0.85, stroke_width=0)
            for _ in range(16)
        ]).arrange_in_grid(rows=4, cols=4, buff=0.2)
        dlbl = fit(Text("about 16 million low-income children\nwaiting for afterschool spots",
                         color=PALETTE["dim"], font_size=17, line_spacing=1.25,
                         should_center=True), 4.9)
        key = Text("each dot = 1 million", color=PALETTE["dim"], font_size=14)
        dots_inner = VGroup(dots, dlbl, key).arrange(DOWN, buff=0.25)
        dots_card = VGroup(dots_box, dots_inner.move_to(dots_box.get_center()))
        dots_card.move_to(RIGHT * 3.3 + UP * 0.2)

        reveal(self, cost)
        reveal(self, dots_card, t2=0.3)
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.06),
            run_time=1.2,
        )

        foot = Text("for a lot of families, extra help is out of reach", color=PALETTE["accent"],
                    font_size=19)
        foot.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B03_ThePatientTutor(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        panel = card_bg(7.4, 4.1, stroke_color=PALETTE["border"])
        panel.move_to(UP * 0.6)

        def bubble(text, side, fs=17):
            t = Text(text, color=PALETTE["ink"] if side == "tutor" else PALETTE["card"], font_size=fs)
            w = t.width + 0.6
            fillc = PALETTE["bg"] if side == "tutor" else PALETTE["accent"]
            strokec = PALETTE["border"] if side == "tutor" else PALETTE["accent"]
            box = RoundedRectangle(corner_radius=0.18, width=w, height=0.62,
                                    fill_color=fillc, fill_opacity=1,
                                    stroke_color=strokec, stroke_width=1.5)
            return VGroup(box, t.move_to(box.get_center()))

        b1 = bubble("How do I do this one?", "kid")
        b2 = bubble("Sure! Here's one way to think about it.", "tutor")
        b3 = bubble("Wait... how do I do this one?", "kid")
        b4 = bubble("Happy to go again. Take your time.", "tutor")
        left_x, right_x = panel.get_left()[0] + 0.45, panel.get_right()[0] - 0.45
        ys = [1.9, 1.0, 0.1, -0.8]
        for b, y, side in zip([b1, b2, b3, b4], ys, ["kid", "tutor", "kid", "tutor"]):
            b.move_to(UP * y)
            if side == "kid":
                b.align_to(panel, RIGHT).shift(LEFT * 0.45)
            else:
                b.align_to(panel, LEFT).shift(RIGHT * 0.45)

        grow_in(self, panel, 7.4, run_time=0.5)
        for b in (b1, b2, b3, b4):
            self.play(FadeIn(b, shift=UP * 0.1), run_time=0.45)

        traits = VGroup(
            chip("patient", w=2.4, border=PALETTE["good"], color=PALETTE["good"]),
            chip("always available", w=3.0, border=PALETTE["good"], color=PALETTE["good"]),
            chip("never embarrassed", w=3.2, border=PALETTE["good"], color=PALETTE["good"]),
        ).arrange(RIGHT, buff=0.35)
        traits.to_edge(DOWN, buff=0.85)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in traits], lag_ratio=0.3),
                  run_time=1.2)
        self.wait(1.2)


class B04_EarlyResearch(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        chips = VGroup(
            chip("human tutors + AI software", w=4.1, fs=15),
            chip("furthest-behind gained most", w=4.1, fs=15),
            chip("tutors not stretched too thin", w=4.1, fs=15),
        ).arrange(RIGHT, buff=0.3)
        chips.move_to(UP * 2.55)
        for c in chips:
            c[0].stretch(0.01, 0)
        self.play(
            LaggedStart(*[c[0].animate.stretch_to_fit_width(4.1) for c in chips], lag_ratio=0.2),
            LaggedStart(*[FadeIn(c[1]) for c in chips], lag_ratio=0.2),
            run_time=1.2,
        )

        title = Text("cost per student, per year", color=PALETTE["dim"], font_size=17)
        title.move_to(UP * 1.45)
        self.play(FadeIn(title), run_time=0.4)

        scale = 6.0 / 4300.0
        rows = [
            ("AI-assisted tutoring", 700, 700, "about $700", PALETTE["accent"], "one summary reports"),
            ("Private tutoring", 2500, 2500, "$2,500+", PALETTE["dim"], ""),
            ("Traditional intensive tutoring", 3500, 4300, "$3,500 - $4,300", PALETTE["dim"],
             "one summary reports"),
        ]
        y = 0.55
        bar_x0 = -2.6
        for name, lo, hi, val, color, flag in rows:
            lbl = Text(name, color=PALETTE["ink"], font_size=17)
            lbl.move_to([bar_x0 - 0.35 - lbl.width / 2, y, 0])
            bar = Rectangle(width=lo * scale, height=0.5, fill_color=color, fill_opacity=1,
                            stroke_width=0)
            bar.move_to([bar_x0 + lo * scale / 2, y, 0])
            parts = [lbl, bar]
            if hi > lo:
                ext = Rectangle(width=(hi - lo) * scale, height=0.5, fill_color=color,
                                fill_opacity=0.35, stroke_width=0)
                ext.move_to([bar_x0 + lo * scale + (hi - lo) * scale / 2, y, 0])
                parts.append(ext)
            end_x = bar_x0 + hi * scale
            vtxt = Text(val, color=color if color == PALETTE["accent"] else PALETTE["ink"],
                        font_size=18, weight="BOLD")
            vtxt.move_to([end_x + 0.2 + vtxt.width / 2, y, 0])
            parts.append(vtxt)
            row = VGroup(*parts)
            self.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.55)
            if flag:
                ft = Text(flag, color=PALETTE["miss"], font_size=13)
                ft.move_to([end_x + 0.2 + vtxt.width / 2, y - 0.42, 0])
                self.play(FadeIn(ft), run_time=0.25)
            y -= 1.15

        foot = Text("early results -- not a guarantee, and only if it holds up",
                    color=PALETTE["dim"], font_size=17)
        foot.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


# simplified Africa outline (lon, lat) -- hand-drawn for illustration only
_AFRICA = [
    (-5.9, 35.8), (-1.9, 35.1), (3.0, 36.8), (10.2, 37.3), (11.1, 33.3), (15.2, 32.3),
    (20.0, 31.0), (25.0, 32.6), (32.0, 31.2), (32.5, 29.9), (34.0, 27.0), (35.5, 23.0),
    (37.2, 18.5), (39.5, 15.5), (43.1, 12.7), (51.3, 11.8), (49.0, 6.0), (46.0, 2.0),
    (42.5, -1.0), (39.2, -6.5), (40.5, -10.5), (40.5, -15.0), (35.0, -19.8), (35.5, -24.0),
    (32.9, -26.0), (30.0, -31.0), (27.0, -33.8), (22.0, -34.2), (18.4, -34.3), (17.0, -29.0),
    (14.5, -22.5), (11.8, -17.0), (13.5, -12.0), (12.3, -6.0), (9.5, 0.5), (9.8, 3.5),
    (6.0, 4.3), (4.0, 6.3), (1.0, 6.0), (-2.0, 4.8), (-4.5, 5.2), (-7.5, 4.4), (-11.5, 6.8),
    (-13.0, 8.5), (-15.0, 11.0), (-17.2, 14.6), (-16.5, 19.5), (-17.0, 21.0), (-13.0, 27.5),
    (-9.8, 30.0), (-9.7, 32.5), (-6.8, 34.0),
]


class B05_GhanaWhatsApp(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        k = 0.062
        lon0, lat0 = 17.0, 2.0  # map center in degrees
        def proj(lon, lat):
            return np.array([(lon - lon0) * k, (lat - lat0) * k, 0])

        frame = card_bg(5.6, 5.4, stroke_color=PALETTE["border"])
        frame.move_to(LEFT * 3.4 + DOWN * 0.1)
        origin = frame.get_center()

        africa = Polygon(*[proj(lo, la) + origin for lo, la in _AFRICA],
                         color=PALETTE["dim"], stroke_width=2,
                         fill_color=PALETTE["dim"], fill_opacity=0.18)
        tag = Text("simplified map", color=PALETTE["dim"], font_size=12)
        tag.move_to(frame.get_bottom() + UP * 0.25)

        reveal(self, VGroup(frame, tag))
        self.play(FadeIn(africa), run_time=0.7)

        gpt = proj(-1.0, 7.9) + origin
        ring = Circle(radius=0.34, color=PALETTE["accent"], stroke_width=3).move_to(gpt)
        dot = Dot(gpt, radius=0.1, color=PALETTE["accent"])
        gl = Text("Ghana", color=PALETTE["accent"], font_size=22, weight="BOLD")
        gl.move_to(ring.get_center() + RIGHT * 0.85 + UP * 0.62)
        self.play(GrowFromCenter(ring), FadeIn(dot), run_time=0.5)
        self.play(FadeIn(gl, shift=RIGHT * 0.1), run_time=0.4)

        # right side: phone with a chat bubble + three facts
        phone = RoundedRectangle(corner_radius=0.25, width=1.5, height=2.6,
                                  fill_color=PALETTE["card"], fill_opacity=1,
                                  stroke_color=PALETTE["ink"], stroke_width=2.5)
        b_a = RoundedRectangle(corner_radius=0.12, width=1.05, height=0.42,
                                fill_color=PALETTE["good"], fill_opacity=0.9, stroke_width=0)
        b_b = RoundedRectangle(corner_radius=0.12, width=0.85, height=0.42,
                                fill_color=PALETTE["border"], fill_opacity=1, stroke_width=0)
        b_c = RoundedRectangle(corner_radius=0.12, width=1.05, height=0.42,
                                fill_color=PALETTE["good"], fill_opacity=0.9, stroke_width=0)
        bubbles = VGroup(b_a, b_b, b_c).arrange(DOWN, buff=0.22)
        b_a.align_to(phone, LEFT).shift(RIGHT * 0.2)
        b_b.align_to(phone, RIGHT).shift(LEFT * 0.2)
        bubbles.move_to(phone.get_center())
        phone_g = VGroup(phone, bubbles)
        phone_g.move_to(RIGHT * 0.9 + UP * 0.9)
        plabel = Text("a math tutor\non WhatsApp", color=PALETTE["ink"], font_size=19, line_spacing=1.2, should_center=True)
        plabel.next_to(phone_g, DOWN, buff=0.3)

        self.play(FadeIn(phone_g, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(plabel), run_time=0.4)

        facts = VGroup(
            chip("strong progress over 8 months", w=3.5, border=PALETTE["good"], color=PALETTE["good"], fs=15),
            chip("ran on phones people already had", w=3.5, fs=15),
            chip("few had ever had a tutor before", w=3.5, fs=15),
        ).arrange(DOWN, buff=0.22)
        facts.move_to(RIGHT * 4.35 + DOWN * 0.1)
        for f in facts:
            self.play(FadeIn(f, shift=LEFT * 0.1), run_time=0.45)
        self.wait(1.2)


class B06_ReachingTheChild(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        stat_box = card_bg(9.4, 1.2, stroke_color=PALETTE["border"])
        big = Text("~9 million", color=PALETTE["accent"], font_size=34, weight="BOLD")
        small = Text("US students without reliable home internet", color=PALETTE["ink"], font_size=19)
        stat_inner = VGroup(big, small).arrange(RIGHT, buff=0.35)
        stat = VGroup(stat_box, stat_inner.move_to(stat_box.get_center()))
        stat.move_to(UP * 2.6)
        reveal(self, stat)

        # a laptop with wifi arcs
        screen = RoundedRectangle(corner_radius=0.08, width=1.5, height=0.95,
                                   fill_color=PALETTE["bg"], fill_opacity=1,
                                   stroke_color=PALETTE["ink"], stroke_width=2.5)
        base = RoundedRectangle(corner_radius=0.05, width=1.9, height=0.12,
                                 fill_color=PALETTE["ink"], fill_opacity=1, stroke_width=0)
        base.next_to(screen, DOWN, buff=0.04)
        arcs = VGroup(*[
            Arc(radius=0.18 + 0.16 * i, start_angle=PI / 4, angle=PI / 2,
                color=PALETTE["good"], stroke_width=3)
            for i in range(3)
        ])
        arcs.move_to(screen.get_center() + DOWN * 0.1)
        laptop = VGroup(screen, base, arcs)
        lap_lbl = Text("free laptop + Wi-Fi", color=PALETTE["ink"], font_size=18)
        lap = VGroup(laptop, lap_lbl).arrange(DOWN, buff=0.3)
        lap_box = card_bg(3.4, 2.7, stroke_color=PALETTE["border"])
        lap_card = VGroup(lap_box, lap.move_to(lap_box.get_center()))
        lap_card.move_to(LEFT * 4.2 + DOWN * 0.7)
        reveal(self, lap_card)

        note = Text("still, many students did not take part", color=PALETTE["miss"], font_size=17)
        note.next_to(lap_card, DOWN, buff=0.3)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.4)

        mid = Text("is not the same as", color=PALETTE["dim"], font_size=17)
        mid.move_to(LEFT * 1.3 + DOWN * 0.7)
        self.play(FadeIn(mid), run_time=0.4)

        needs = ["the time", "a quiet space", "a reason to keep going"]
        stack = VGroup()
        for n in needs:
            ring_ic = Circle(radius=0.14, color=PALETTE["accent"], stroke_width=2.5)
            txt = Text(n, color=PALETTE["ink"], font_size=19)
            row = VGroup(ring_ic, txt).arrange(RIGHT, buff=0.25)
            box = card_bg(4.3, 0.75, stroke_color=PALETTE["accent"])
            stack.add(VGroup(box, row.move_to(box.get_center())))
        stack.arrange(DOWN, buff=0.2)
        stack.move_to(RIGHT * 3.3 + DOWN * 0.7)
        for s in stack:
            reveal(self, s, t1=0.3, t2=0.3)
        self.wait(1.3)


class B07_AFairCaution(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # left card: the study
        crowd = VGroup(*[
            Circle(radius=0.09, color=PALETTE["dim"], fill_color=PALETTE["dim"],
                   fill_opacity=0.8, stroke_width=0)
            for _ in range(40)
        ]).arrange_in_grid(rows=4, cols=10, buff=0.14)
        n = Text("2,000+", color=PALETTE["ink"], font_size=40, weight="BOLD")
        nl = Text("college students", color=PALETTE["dim"], font_size=19)
        res = fit(Text("AI-tutor group: slightly\nlower grades", color=PALETTE["miss"],
                        font_size=19, line_spacing=1.25, should_center=True), 4.4)
        inner = VGroup(crowd, n, nl, res).arrange(DOWN, buff=0.28)
        box = card_bg(5.6, 5.0, stroke_color=PALETTE["border"])
        study = VGroup(box, inner.move_to(box.get_center()))
        study.move_to(LEFT * 3.4 + DOWN * 0.2)
        reveal(self, study)

        # right card: what to keep in mind
        head = Text("what to keep in mind", color=PALETTE["accent"], font_size=22, weight="BOLD")
        rows = VGroup()
        for t in ["these were adults, not kids", "the researchers noted limits",
                  "how a tutor is built and used matters"]:
            d = Dot(radius=0.07, color=PALETTE["accent"])
            tx = fit(Text(t, color=PALETTE["ink"], font_size=19), 4.4)
            rows.add(VGroup(d, tx).arrange(RIGHT, buff=0.25))
        rows.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        inner2 = VGroup(head, rows).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        box2 = card_bg(6.0, 5.0, stroke_color=PALETTE["accent"])
        keep = VGroup(box2, inner2.move_to(box2.get_center()))
        keep.move_to(RIGHT * 3.4 + DOWN * 0.2)
        reveal(self, keep, t2=0.3)
        for r in rows:
            self.play(Indicate(r, color=PALETTE["accent"], scale_factor=1.04), run_time=0.5)
        self.wait(1.2)


class B08_TheClosingIdea(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        gy = -1.2
        ground = Line(LEFT * 4.6, RIGHT * 4.6, color=PALETTE["border"], stroke_width=3)
        ground.move_to(UP * gy)

        desk_top = -0.35
        desk = RoundedRectangle(corner_radius=0.05, width=3.0, height=0.16,
                                 fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0)
        desk.move_to([-1.6, desk_top, 0])
        leg_h = desk_top - gy - 0.08
        legs = VGroup(
            Rectangle(width=0.1, height=leg_h, fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0),
            Rectangle(width=0.1, height=leg_h, fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0),
        )
        legs[0].move_to([-3.0, gy + leg_h / 2, 0])
        legs[1].move_to([-0.2, gy + leg_h / 2, 0])
        kid = person(1.1, PALETTE["ink"])
        kid.move_to([-2.6, -0.5 + kid.height / 2, 0])
        laptop_s = RoundedRectangle(corner_radius=0.05, width=0.95, height=0.6,
                                     fill_color=PALETTE["bg"], fill_opacity=1,
                                     stroke_color=PALETTE["ink"], stroke_width=2)
        laptop_s.move_to([-1.3, desk_top + 0.38, 0])
        glow = Dot(laptop_s.get_center(), radius=0.07, color=PALETTE["accent"])

        self.play(FadeIn(VGroup(ground, legs, desk, kid), shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(VGroup(laptop_s, glow)), run_time=0.5)

        adult = person(1.5, PALETTE["good"])
        adult.move_to([1.2, gy + adult.height / 2, 0])
        halo = RoundedRectangle(corner_radius=0.4, width=6.3, height=3.6,
                                 stroke_color=PALETTE["accent"], stroke_width=2.5,
                                 fill_opacity=0).set_stroke(opacity=0.5)
        halo.move_to([-1.0, 0.25, 0])
        near_l = Text("beside them", color=PALETTE["accent"], font_size=20, weight="BOLD")
        near_l.move_to([-1.0, -1.85, 0])
        roles = Text("teacher  /  volunteer  /  mentor", color=PALETTE["dim"], font_size=17)
        roles.move_to([-1.0, -2.25, 0])
        self.play(FadeIn(adult, shift=LEFT * 0.2), run_time=0.7)
        self.play(Create(halo), run_time=0.7)
        self.play(FadeIn(near_l), FadeIn(roles), run_time=0.5)

        q = fit(Text("Can it reach the child who needs it -- and who will be there beside them?",
                     color=PALETTE["ink"], font_size=24, weight="BOLD"), 11.6)
        q.move_to([0, -3.1, 0])
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.7)
        self.wait(1.5)
