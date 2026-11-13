"""
Portrait (9:16) Manim scenes for ai-done-right-short

Ports of the six graphic beats kept in the Shorts cut (B00B, B03, B05, B06,
B08, B09). Stacked layouts for a 4.5 x 8.0 frame; same palette and copy as the
16:9 scenes. Dropped beats (B01, B02, B04, B07) live only in the long cut.
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


def lines(txt, fs, color, max_w=None, buff=0.12, weight=None):
    """Centered multi-line label: one Text per line, stacked and centered."""
    kw = {"weight": weight} if weight else {}
    g = VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split("\n")]).arrange(DOWN, buff=buff)
    return fit(g, max_w) if max_w else g


def reveal(scene, card, t1=0.35, t2=0.4):
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


def meter(w, frac, color):
    track = RoundedRectangle(corner_radius=0.08, width=w, height=0.18,
                              fill_color=PALETTE["border"], fill_opacity=1, stroke_width=0)
    fill = RoundedRectangle(corner_radius=0.08, width=max(w * frac, 0.2), height=0.18,
                             fill_color=color, fill_opacity=1, stroke_width=0)
    fill.align_to(track, LEFT)
    return VGroup(track, fill)


def stat_row(num, label, frac, color, w, num_fs=32, label_fs=13):
    n = Text(num, color=color, font_size=num_fs, weight="BOLD")
    lab = lines(label, label_fs, PALETTE["ink"], max_w=w - n.width - 0.3, buff=0.06)
    top = VGroup(n, lab).arrange(RIGHT, buff=0.25)
    bar = meter(w, frac, color)
    return VGroup(top, bar).arrange(DOWN, buff=0.14, aligned_edge=LEFT)


class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = fit(Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=38), 3.4)
        summary = lines("Today: nonprofits built\naround AI, and what they\ncan teach us about trust,\n"
                        "people, and purpose.\nWhat seems to work, and\nthe fair limits too.",
                        22, PALETTE["ink"], max_w=3.4, buff=0.2)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.4)


class B03_AdalatAI(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        room = card_bg(3.7, 3.3)
        room.move_to(UP * 1.7)
        rc = room.get_center()

        bench = RoundedRectangle(corner_radius=0.06, width=2.0, height=0.4,
                                  fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0)
        bench.move_to(rc + UP * 0.5)
        judge = person(0.6, PALETTE["ink"])
        judge.move_to(bench.get_top() + UP * (judge.height / 2 + 0.02))

        def pile(n):
            return VGroup(*[
                Rectangle(width=0.9, height=0.1, fill_color=PALETTE["card"], fill_opacity=1,
                          stroke_color=PALETTE["dim"], stroke_width=1.2).shift(UP * 0.11 * i + RIGHT * 0.04 * ((-1) ** i))
                for i in range(n)
            ])
        piles = VGroup(pile(7), pile(10), pile(5)).arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
        fit(piles, 3.0)
        piles.move_to(rc + DOWN * 0.55)
        lbl1 = lines("slow paperwork,\nclogged courtrooms", 15, PALETTE["miss"], max_w=3.2, buff=0.06)
        lbl1.move_to(rc + DOWN * 1.3)

        reveal(self, VGroup(room, VGroup(bench, judge)))
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.1) for p in piles], lag_ratio=0.25), run_time=1.0)
        self.play(FadeIn(lbl1), run_time=0.4)
        self.wait(0.8)

        mic_body = RoundedRectangle(corner_radius=0.15, width=0.3, height=0.55,
                                     fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
        mic_stand = Arc(radius=0.28, start_angle=PI, angle=PI, color=PALETTE["accent"], stroke_width=3)
        mic_stand.rotate(PI).move_to(mic_body.get_bottom() + UP * 0.05)
        mic = VGroup(mic_body, mic_stand)
        tlines = VGroup(*[
            Line(LEFT * (1.0 - 0.25 * (i % 2)), RIGHT * (1.0 - 0.25 * (i % 2)),
                 color=PALETTE["good"], stroke_width=4)
            for i in range(4)
        ]).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        tool = VGroup(mic, tlines).arrange(RIGHT, buff=0.45).move_to(rc + DOWN * 0.45)
        lbl2 = lines("a simple\nstenography tool", 15, PALETTE["good"], max_w=3.2, buff=0.06, weight="BOLD")
        lbl2.move_to(rc + DOWN * 1.3)
        self.play(FadeOut(piles), FadeOut(lbl1), run_time=0.6)
        self.play(FadeIn(tool, shift=UP * 0.1), FadeIn(lbl2), run_time=0.7)

        def stat(num, lab):
            n = Text(num, color=PALETTE["accent"], font_size=28, weight="BOLD")
            l = Text(lab, color=PALETTE["dim"], font_size=14)
            inner = VGroup(n, l).arrange(DOWN, buff=0.1)
            box = card_bg(1.8, 1.25)
            return VGroup(box, inner.move_to(box.get_center()))
        s1 = stat("5,500", "courtrooms")
        s2 = stat("11", "states")
        stats = VGroup(s1, s2).arrange(RIGHT, buff=0.1)
        stats.move_to(DOWN * 0.95)
        reveal(self, s1)
        reveal(self, s2)

        foot = lines("Start with the real\nproblem, not the\nimpressive technology.", 19,
                     PALETTE["accent"], max_w=3.5, buff=0.1)
        foot.move_to(DOWN * 2.55)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B05_HelpsAndWorries(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lh = Text("it seems to help", color=PALETTE["good"], font_size=19, weight="BOLD")
        r1 = stat_row("92%", "said AI made\nservices more\nefficient", 0.92, PALETTE["good"], 3.2)
        none_chip = chip("not one said the risks outweigh the benefits", w=3.4, h=0.5,
                         border=PALETTE["good"], color=PALETTE["good"], fs=12)
        l_inner = VGroup(lh, r1, none_chip).arrange(DOWN, buff=0.28)
        l_box = card_bg(3.7, 2.8, stroke_color=PALETTE["good"])
        top = VGroup(l_box, l_inner.move_to(l_box.get_center()))
        top.move_to(UP * 1.95)

        rh = fit(Text("honest about their worries", color=PALETTE["accent"], font_size=19, weight="BOLD"), 3.2)
        w1 = stat_row("88%", "worry about sharing\nwrong information", 0.88, PALETTE["accent"], 3.2)
        w2 = stat_row("84%", "worry about misusing\npersonal data", 0.84, PALETTE["accent"], 3.2)
        r_inner = VGroup(rh, w1, w2).arrange(DOWN, buff=0.35)
        r_box = card_bg(3.7, 3.3, stroke_color=PALETTE["accent"])
        bottom = VGroup(r_box, r_inner.move_to(r_box.get_center()))
        bottom.move_to(DOWN * 1.45)

        reveal(self, top)
        reveal(self, bottom)
        self.wait(1.3)


class B06_PeopleInTheLoop(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        def hstat(num, lab):
            n = Text(num, color=PALETTE["accent"], font_size=32, weight="BOLD")
            l = lines(lab, 13, PALETTE["ink"], max_w=2.2, buff=0.06)
            inner = VGroup(n, l).arrange(RIGHT, buff=0.3)
            box = card_bg(3.7, 1.05)
            return VGroup(box, fit(inner, 3.3).move_to(box.get_center()))
        cards = VGroup(
            hstat("76%", "keep asking for feedback\nfrom the people they help"),
            hstat("51%", "invite community members\nto help shape the tools"),
            hstat("85%", "say they are very open\nabout using AI"),
        ).arrange(DOWN, buff=0.15)
        cards.move_to(UP * 1.575)
        for c in cards:
            reveal(self, c, t1=0.3, t2=0.3)

        src_box = RoundedRectangle(corner_radius=0.06, width=0.55, height=0.42,
                                    fill_color=PALETTE["bg"], fill_opacity=1,
                                    stroke_color=PALETTE["dim"], stroke_width=2)
        arr = Arrow(LEFT * 0.35, RIGHT * 0.35, color=PALETTE["dim"], stroke_width=3, buff=0,
                    max_tip_length_to_length_ratio=0.35)
        p_for = person(0.5, PALETTE["ink"])
        for_icon = VGroup(src_box, arr, p_for).arrange(RIGHT, buff=0.15)
        for_txt = Text("designing for you", color=PALETTE["dim"], font_size=17)
        for_in = VGroup(for_icon, for_txt).arrange(DOWN, buff=0.15)
        for_box = card_bg(3.7, 1.35)
        for_card = VGroup(for_box, for_in.move_to(for_box.get_center()))
        for_card.move_to(DOWN * 1.03)

        tbl = RoundedRectangle(corner_radius=0.05, width=1.0, height=0.1,
                                fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0)
        ppl = VGroup(person(0.45, PALETTE["good"]), person(0.45, PALETTE["accent"]),
                     person(0.45, PALETTE["ink"])).arrange(RIGHT, buff=0.15)
        with_icon = VGroup(ppl, tbl).arrange(DOWN, buff=-0.04)
        with_txt = Text("designing with you", color=PALETTE["accent"], font_size=17, weight="BOLD")
        with_in = VGroup(with_icon, with_txt).arrange(DOWN, buff=0.15)
        with_box = card_bg(3.7, 1.35, stroke_color=PALETTE["accent"])
        with_card = VGroup(with_box, with_in.move_to(with_box.get_center()))
        with_card.move_to(DOWN * 2.55)

        reveal(self, for_card)
        reveal(self, with_card)
        self.wait(1.3)


class B08_FairLimits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = Text("what this research is", color=PALETTE["ink"], font_size=19, weight="BOLD")
        rows = VGroup()
        for t in ["answers from the\nnonprofits themselves",
                  "from nonprofits that\nalready use AI",
                  "so it doesn't describe\nevery nonprofit",
                  "report supported\nby Google.org"]:
            d = Dot(radius=0.06, color=PALETTE["dim"])
            tx = VGroup(*[Text(s, color=PALETTE["ink"], font_size=14) for s in t.split("\n")]
                        ).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
            rows.add(VGroup(d, tx).arrange(RIGHT, buff=0.2))
        rows.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        l_inner = VGroup(head, rows).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        l_box = card_bg(3.7, 3.6)
        top = VGroup(l_box, l_inner.move_to(l_box.get_center()))
        top.move_to(UP * 1.55)

        head2 = Text("another view", color=PALETTE["accent"], font_size=16, weight="BOLD")
        who = Text("Bridgespan", color=PALETTE["ink"], font_size=26, weight="BOLD")
        body = VGroup(*[Text(s, color=PALETTE["ink"], font_size=15)
                        for s in ("skipping AI can be the", "right choice for some", "organizations")]
                      ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        r_inner = VGroup(head2, who, body).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        r_box = card_bg(3.7, 2.6, stroke_color=PALETTE["accent"])
        bottom = VGroup(r_box, r_inner.move_to(r_box.get_center()))
        bottom.move_to(DOWN * 1.95)

        reveal(self, top)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.4)
        reveal(self, bottom, t2=0.3)
        self.wait(1.2)


class B09_AtTheTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        ty = 1.75
        people = VGroup(
            person(0.8, PALETTE["ink"]).move_to([-1.6, ty + 0.55, 0]),
            person(0.8, PALETTE["good"]).move_to([-0.95, ty + 0.55, 0]),
            person(0.8, PALETTE["accent"]).move_to([0.95, ty + 0.55, 0]),
            person(0.8, PALETTE["dim"]).move_to([1.6, ty + 0.55, 0]),
        )
        table = RoundedRectangle(corner_radius=0.05, width=3.7, height=0.14,
                                  fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0)
        table.move_to([0, ty, 0])
        legs = VGroup(*[Rectangle(width=0.09, height=0.8, fill_color=PALETTE["dim"], fill_opacity=1,
                                   stroke_width=0) for _ in range(2)])
        legs[0].move_to([-1.7, ty - 0.47, 0])
        legs[1].move_to([1.7, ty - 0.47, 0])
        screen = RoundedRectangle(corner_radius=0.06, width=0.95, height=0.65,
                                   fill_color=PALETTE["bg"], fill_opacity=1,
                                   stroke_color=PALETTE["ink"], stroke_width=2.5)
        screen.move_to([0, ty + 0.07 + 0.33 + 0.08, 0])
        stand = Rectangle(width=0.2, height=0.08, fill_color=PALETTE["ink"], fill_opacity=1, stroke_width=0)
        stand.move_to([0, ty + 0.07 + 0.04, 0])
        glow = Dot(screen.get_center(), radius=0.07, color=PALETTE["accent"])

        self.play(FadeIn(VGroup(people, table, legs), shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(VGroup(screen, stand, glow)), run_time=0.6)

        chips = VGroup(
            chip("start with a real problem", w=3.4, h=0.55, border=PALETTE["good"], color=PALETTE["good"], fs=14),
            chip("keep people involved", w=3.4, h=0.55, border=PALETTE["good"], color=PALETTE["good"], fs=14),
            chip("be open about AI", w=3.4, h=0.55, border=PALETTE["good"], color=PALETTE["good"], fs=14),
        ).arrange(DOWN, buff=0.18)
        chips.move_to(DOWN * 0.35)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in chips], lag_ratio=0.3), run_time=1.2)

        note = lines("none of it needs a big budget.\nIt mostly needs attention.", 14,
                     PALETTE["dim"], max_w=3.6, buff=0.08)
        note.move_to(DOWN * 1.75)
        self.play(FadeIn(note), run_time=0.5)

        q = lines("Who is at the\ntable with us?", 26, PALETTE["ink"], max_w=3.4, buff=0.12, weight="BOLD")
        q.move_to(DOWN * 2.75)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.7)
        self.wait(1.5)
