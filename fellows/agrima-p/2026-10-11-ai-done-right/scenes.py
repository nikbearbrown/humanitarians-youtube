"""
Manim scenes for ai-done-right

A calm, neutral explainer on nonprofits built around AI, sourced from the
user-supplied article "AI Done Right: What Nonprofits Built Around AI Can
Teach Us About Trust, People, and Purpose." No dedicated footage exists (per
the user's materials note) -- every visual below is a generated Manim
graphic. Every stat is self-reported by nonprofits that already use AI (Fast
Forward, 2026) and is carried as such. Built in the house Claude palette.

B00B_AgrimaIntro        -- presenter card: "Hi, I'm Agrima." + lead-in
B01_TheCommonStory      -- time-saving chips + 98-of-100 dot grid
B02_TheDifferentGroup   -- AI on the side vs built around AI (courts + WhatsApp planner)
B03_AdalatAI            -- courtroom with paperwork -> simple stenography tool; 5,500 / 11
B04_TheResearch         -- 119 nonprofits / 20 countries / 20 leaders
B05_HelpsAndWorries     -- 92% more efficient; 88% / 84% worries
B06_PeopleInTheLoop     -- 76% / 51% / 85%; designing for vs with
B07_MoneyIsTheHardPart  -- 90% plan to grow vs ~24% have the resources
B08_FairLimits          -- what this research is / Bridgespan's note
B09_AtTheTable          -- people around a table with a screen; closing question
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


def meter(w, frac, color):
    track = RoundedRectangle(corner_radius=0.08, width=w, height=0.2,
                              fill_color=PALETTE["border"], fill_opacity=1, stroke_width=0)
    fill = RoundedRectangle(corner_radius=0.08, width=max(w * frac, 0.2), height=0.2,
                             fill_color=color, fill_opacity=1, stroke_width=0)
    fill.align_to(track, LEFT)
    return VGroup(track, fill)


def stat_row(num, label, frac, color, w, num_fs=38, label_fs=16):
    n = Text(num, color=color, font_size=num_fs, weight="BOLD")
    lab = fit(Text(label, color=PALETTE["ink"], font_size=label_fs), w - n.width - 0.4)
    top = VGroup(n, lab).arrange(RIGHT, buff=0.3)
    bar = meter(w, frac, color)
    return VGroup(top, bar).arrange(DOWN, buff=0.16, aligned_edge=LEFT)


class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=40)
        summary = fit(Text(
            "Today: nonprofits built around AI, and\nwhat they can teach us about trust,\n"
            "people, and purpose. What seems to\nwork, and the fair limits too.",
            color=PALETTE["ink"], font_size=24, line_spacing=1.3, should_center=True), 8.6)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.4)


class B01_TheCommonStory(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # left: the usual story
        head = Text("the usual story", color=PALETTE["dim"], font_size=19)
        chips = VGroup(
            chip("faster emails", w=3.8, h=0.7, fs=19),
            chip("quicker grant drafts", w=3.8, h=0.7, fs=19),
            chip("less time on paperwork", w=3.8, h=0.7, fs=19),
        ).arrange(DOWN, buff=0.3)
        l_inner = VGroup(head, chips).arrange(DOWN, buff=0.4)
        l_box = card_bg(4.6, 4.6)
        left = VGroup(l_box, l_inner.move_to(l_box.get_center()))
        left.move_to(LEFT * 3.9 + DOWN * 0.1)

        # right: 98 of 100 dots
        dots = VGroup(*[
            Circle(radius=0.1, color=PALETTE["accent"] if i < 98 else PALETTE["border"],
                   fill_color=PALETTE["accent"] if i < 98 else PALETTE["border"],
                   fill_opacity=1, stroke_width=0)
            for i in range(100)
        ]).arrange_in_grid(rows=10, cols=10, buff=0.12)
        big = Text("98%", color=PALETTE["accent"], font_size=44, weight="BOLD")
        sm = lines("of 917 nonprofit staff and leaders\nuse AI in some way (2026 survey)",
                   16, PALETTE["dim"], max_w=4.6)
        r_inner = VGroup(dots, big, sm).arrange(DOWN, buff=0.22)
        r_box = card_bg(5.4, 5.7)
        right = VGroup(r_box, r_inner.move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.4 + DOWN * 0.1)

        reveal(self, left)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in chips], lag_ratio=0.3), run_time=1.0)
        reveal(self, right, t2=0.3)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.01), run_time=1.6)
        self.wait(1.2)


class B02_TheDifferentGroup(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # left: AI on the side
        env_box = RoundedRectangle(corner_radius=0.05, width=0.9, height=0.6,
                                    fill_color=PALETTE["bg"], fill_opacity=1,
                                    stroke_color=PALETTE["dim"], stroke_width=2)
        flap = Polygon(env_box.get_corner(UL), env_box.get_corner(UR), env_box.get_center(),
                       color=PALETTE["dim"], stroke_width=2, fill_opacity=0)
        envelope = VGroup(env_box, flap)
        doc = RoundedRectangle(corner_radius=0.05, width=0.6, height=0.8,
                                fill_color=PALETTE["bg"], fill_opacity=1,
                                stroke_color=PALETTE["dim"], stroke_width=2)
        doc_lines = VGroup(*[Line(LEFT * 0.18, RIGHT * 0.18, color=PALETTE["border"], stroke_width=2)
                              for _ in range(3)]).arrange(DOWN, buff=0.12).move_to(doc.get_center())
        docg = VGroup(doc, doc_lines)
        icons = VGroup(envelope, docg).arrange(RIGHT, buff=0.4)
        l_title = Text("AI on the side", color=PALETTE["ink"], font_size=22, weight="BOLD")
        l_sub = fit(Text("saves time on tasks", color=PALETTE["dim"], font_size=16), 2.9)
        l_inner = VGroup(l_title, icons, l_sub).arrange(DOWN, buff=0.4)
        l_box = card_bg(3.3, 3.8)
        left = VGroup(l_box, l_inner.move_to(l_box.get_center()))
        left.move_to(LEFT * 4.6 + DOWN * 0.4)

        # middle: courts card
        roof = Triangle(color=PALETTE["accent"], fill_color=PALETTE["accent"], fill_opacity=0.15,
                        stroke_width=2).scale(0.45).stretch(1.6, 0)
        pillars = VGroup(*[Rectangle(width=0.14, height=0.5, fill_color=PALETTE["dim"], fill_opacity=1,
                                       stroke_width=0) for _ in range(4)]).arrange(RIGHT, buff=0.18)
        base = Rectangle(width=1.3, height=0.1, fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0)
        court = VGroup(roof, pillars, base).arrange(DOWN, buff=0.04)
        c_title = lines("helps courts record\nwhat is said", 18, PALETTE["ink"], max_w=2.9)
        c_tag = chip("cases move faster", w=2.6, h=0.5, border=PALETTE["good"], color=PALETTE["good"], fs=15)
        c_inner = VGroup(court, c_title, c_tag).arrange(DOWN, buff=0.3)
        c_box = card_bg(3.4, 3.8, stroke_color=PALETTE["accent"])
        courts = VGroup(c_box, c_inner.move_to(c_box.get_center()))
        courts.move_to(LEFT * 0.4 + DOWN * 0.4)

        # right: WhatsApp-style lesson planner chat (illustrative)
        def bub(text, side):
            t = Text(text, color=PALETTE["ink"], font_size=14)
            b = RoundedRectangle(corner_radius=0.14, width=t.width + 0.4, height=0.5,
                                  fill_color="#DCF1DC" if side == "me" else PALETTE["bg"],
                                  fill_opacity=1, stroke_color=PALETTE["border"], stroke_width=1.2)
            return VGroup(b, t.move_to(b.get_center()))
        m1 = bub("Plan tomorrow's lesson", "me")
        m2 = bub("Here's a draft plan.", "bot")
        chat = VGroup(m1, m2).arrange(DOWN, buff=0.18)
        m1.align_to(chat, RIGHT)
        m2.align_to(chat, LEFT)
        w_title = lines("a lesson planner\ninside WhatsApp", 18, PALETTE["ink"], max_w=3.0)
        w_tag = chip("evenings back for teachers", w=3.1, h=0.5, border=PALETTE["good"],
                     color=PALETTE["good"], fs=14)
        w_note = Text("illustrative chat", color=PALETTE["dim"], font_size=12)
        w_inner = VGroup(chat, w_title, w_tag, w_note).arrange(DOWN, buff=0.28)
        w_box = card_bg(3.6, 3.8, stroke_color=PALETTE["accent"])
        wa = VGroup(w_box, w_inner.move_to(w_box.get_center()))
        wa.move_to(RIGHT * 3.6 + DOWN * 0.4)

        h_right = Text("built around AI", color=PALETTE["accent"], font_size=20, weight="BOLD")
        h_right.move_to([1.6, 1.95, 0])

        reveal(self, left)
        self.play(FadeIn(h_right), run_time=0.4)
        reveal(self, courts)
        reveal(self, wa)
        self.wait(1.3)


class B03_AdalatAI(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        room = card_bg(6.6, 5.2)
        room.move_to(LEFT * 2.9 + DOWN * 0.1)
        rc = room.get_center()

        bench = RoundedRectangle(corner_radius=0.06, width=3.4, height=0.5,
                                  fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0)
        bench.move_to(rc + UP * 1.55)
        judge = person(0.8, PALETTE["ink"])
        judge.move_to(bench.get_top() + UP * (judge.height / 2 + 0.02))

        def pile(n):
            sheets = VGroup(*[
                Rectangle(width=0.9, height=0.1, fill_color=PALETTE["card"], fill_opacity=1,
                          stroke_color=PALETTE["dim"], stroke_width=1.2).shift(UP * 0.11 * i + RIGHT * 0.04 * ((-1) ** i))
                for i in range(n)
            ])
            return sheets
        piles = VGroup(pile(7), pile(10), pile(5)).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        piles.move_to(rc + DOWN * 0.15)
        lbl1 = Text("slow paperwork, clogged courtrooms", color=PALETTE["miss"], font_size=18)
        lbl1.move_to(rc + DOWN * 1.9)

        reveal(self, VGroup(room, VGroup(bench, judge)))
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.1) for p in piles], lag_ratio=0.25), run_time=1.0)
        self.play(FadeIn(lbl1), run_time=0.4)
        self.wait(0.8)

        # the simple tool: speech -> clean text
        mic_body = RoundedRectangle(corner_radius=0.15, width=0.3, height=0.55,
                                     fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
        mic_stand = Arc(radius=0.28, start_angle=PI, angle=PI, color=PALETTE["accent"], stroke_width=3)
        mic_stand.rotate(PI).move_to(mic_body.get_bottom() + UP * 0.05)
        mic = VGroup(mic_body, mic_stand)
        lines = VGroup(*[
            Line(LEFT * (1.1 - 0.25 * (i % 2)), RIGHT * (1.1 - 0.25 * (i % 2)),
                 color=PALETTE["good"], stroke_width=4)
            for i in range(4)
        ]).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        tool = VGroup(mic, lines).arrange(RIGHT, buff=0.6).move_to(rc + DOWN * 0.15)
        lbl2 = Text("a simple stenography tool", color=PALETTE["good"], font_size=18, weight="BOLD")
        lbl2.move_to(rc + DOWN * 1.9)
        self.play(FadeOut(piles), FadeOut(lbl1), run_time=0.6)
        self.play(FadeIn(tool, shift=UP * 0.1), FadeIn(lbl2), run_time=0.7)

        # right: the numbers
        def stat(num, lab):
            n = Text(num, color=PALETTE["accent"], font_size=44, weight="BOLD")
            l = Text(lab, color=PALETTE["dim"], font_size=19)
            inner = VGroup(n, l).arrange(DOWN, buff=0.15)
            box = card_bg(3.9, 2.3)
            return VGroup(box, inner.move_to(box.get_center()))
        s1 = stat("5,500", "courtrooms")
        s2 = stat("11", "states")
        stats = VGroup(s1, s2).arrange(DOWN, buff=0.25)
        stats.move_to(RIGHT * 4.2 + DOWN * 0.1)
        reveal(self, s1)
        reveal(self, s2)

        foot = Text("Start with the real problem, not the impressive technology.",
                    color=PALETTE["accent"], font_size=20)
        foot.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B04_TheResearch(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        src = chip("Fast Forward  ·  September 2026 report", w=6.4, h=0.7, border=PALETTE["accent"],
                   color=PALETTE["accent"], fs=19)
        src.move_to(UP * 2.6)
        self.play(FadeIn(src, shift=DOWN * 0.1), run_time=0.5)

        def stat(num, lab):
            n = Text(num, color=PALETTE["ink"], font_size=60, weight="BOLD")
            l = lines(lab, 20, PALETTE["dim"], max_w=3.2)
            inner = VGroup(n, l).arrange(DOWN, buff=0.3)
            box = card_bg(3.8, 3.2)
            return VGroup(box, inner.move_to(box.get_center()))
        cards = VGroup(
            stat("119", "AI-powered\nnonprofits surveyed"),
            stat("20", "countries"),
            stat("20", "leaders\ninterviewed"),
        ).arrange(RIGHT, buff=0.4)
        cards.move_to(DOWN * 0.3)
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.12), run_time=0.6)

        foot = Text("what stood out: four things", color=PALETTE["dim"], font_size=19)
        foot.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B05_HelpsAndWorries(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # left: it seems to help
        lh = Text("it seems to help", color=PALETTE["good"], font_size=23, weight="BOLD")
        r1 = stat_row("92%", "said AI made services\nmore efficient", 0.92, PALETTE["good"], 4.5)
        none_chip = chip("not one said the risks outweigh the benefits", w=4.6, h=0.9,
                         border=PALETTE["good"], color=PALETTE["good"], fs=16)
        l_inner = VGroup(lh, r1, none_chip).arrange(DOWN, buff=0.55)
        l_box = card_bg(5.5, 5.0, stroke_color=PALETTE["good"])
        left = VGroup(l_box, l_inner.move_to(l_box.get_center()))
        left.move_to(LEFT * 3.45)

        # right: honest about worries
        rh = Text("honest about their worries", color=PALETTE["accent"], font_size=23, weight="BOLD")
        w1 = stat_row("88%", "worry about sharing\nwrong information", 0.88, PALETTE["accent"], 4.5)
        w2 = stat_row("84%", "worry about misusing\npersonal data", 0.84, PALETTE["accent"], 4.5)
        r_inner = VGroup(rh, w1, w2).arrange(DOWN, buff=0.5)
        r_box = card_bg(5.5, 5.0, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, r_inner.move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.45)

        reveal(self, left)
        reveal(self, right)
        foot = Text("a lot of caution from people who believe in the tool", color=PALETTE["dim"],
                    font_size=18)
        foot.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B06_PeopleInTheLoop(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        def stat(num, lab):
            n = Text(num, color=PALETTE["accent"], font_size=46, weight="BOLD")
            l = lines(lab, 17, PALETTE["ink"], max_w=3.4)
            inner = VGroup(n, l).arrange(DOWN, buff=0.2)
            box = card_bg(3.9, 2.5)
            return VGroup(box, inner.move_to(box.get_center()))
        cards = VGroup(
            stat("76%", "keep asking for feedback\nfrom the people they help"),
            stat("51%", "invite community members\nto help shape the tools"),
            stat("85%", "say they are very open\nabout using AI"),
        ).arrange(RIGHT, buff=0.3)
        cards.move_to(UP * 1.45)
        for c in cards:
            reveal(self, c, t1=0.3, t2=0.3)

        # designing for you  vs  designing with you
        def panel(label, color):
            box = card_bg(5.6, 2.4, stroke_color=color)
            return VGroup(box, label)
        # for: a box passes something to a person
        src_box = RoundedRectangle(corner_radius=0.06, width=0.7, height=0.55,
                                    fill_color=PALETTE["bg"], fill_opacity=1,
                                    stroke_color=PALETTE["dim"], stroke_width=2)
        arr = Arrow(LEFT * 0.5, RIGHT * 0.5, color=PALETTE["dim"], stroke_width=3, buff=0,
                    max_tip_length_to_length_ratio=0.3)
        p_for = person(0.7, PALETTE["ink"])
        for_icon = VGroup(src_box, arr, p_for).arrange(RIGHT, buff=0.25)
        for_txt = Text("designing for you", color=PALETTE["dim"], font_size=20)
        for_in = VGroup(for_icon, for_txt).arrange(DOWN, buff=0.3)
        for_box = card_bg(5.6, 2.4)
        for_card = VGroup(for_box, for_in.move_to(for_box.get_center()))
        for_card.move_to(LEFT * 3.2 + DOWN * 1.9)

        tbl = RoundedRectangle(corner_radius=0.05, width=1.3, height=0.14,
                                fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0)
        ppl = VGroup(person(0.55, PALETTE["good"]), person(0.55, PALETTE["accent"]),
                     person(0.55, PALETTE["ink"])).arrange(RIGHT, buff=0.2)
        with_icon = VGroup(ppl, tbl).arrange(DOWN, buff=-0.05)
        with_txt = Text("designing with you", color=PALETTE["accent"], font_size=20, weight="BOLD")
        with_in = VGroup(with_icon, with_txt).arrange(DOWN, buff=0.3)
        with_box = card_bg(5.6, 2.4, stroke_color=PALETTE["accent"])
        with_card = VGroup(with_box, with_in.move_to(with_box.get_center()))
        with_card.move_to(RIGHT * 3.2 + DOWN * 1.9)

        reveal(self, for_card)
        reveal(self, with_card)
        self.wait(1.3)


class B07_MoneyIsTheHardPart(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        bar_w = 4.6
        x0 = -2.5

        def row(label, num, frac, color, y):
            lab = Text(label, color=PALETTE["ink"], font_size=22)
            lab.move_to([-6.0 + lab.width / 2, y, 0])
            bar = meter(bar_w, frac, color)
            bar.move_to([x0 + bar_w / 2, y, 0])
            n = Text(num, color=color, font_size=40, weight="BOLD")
            n.move_to([x0 + bar_w + 0.5 + n.width / 2, y, 0])
            return VGroup(lab, bar, n)

        title = Text("growing a good project", color=PALETTE["dim"], font_size=19)
        title.move_to(UP * 2.7)
        self.play(FadeIn(title), run_time=0.4)

        r1 = row("have a plan to grow", "90%", 0.90, PALETTE["good"], 1.5)
        r2 = row("have what it takes", "about 24%", 0.24, PALETTE["accent"], 0.0)
        self.play(FadeIn(r1, shift=RIGHT * 0.15), run_time=0.7)
        self.play(FadeIn(r2, shift=RIGHT * 0.15), run_time=0.7)

        gap_end = x0 + bar_w * 0.90
        gap_start = x0 + bar_w * 0.24
        gap = Arrow([gap_start, -0.75, 0], [gap_end, -0.75, 0], color=PALETTE["miss"], stroke_width=3,
                    buff=0, max_tip_length_to_length_ratio=0.08)
        gap_l = Text("the gap", color=PALETTE["miss"], font_size=19)
        gap_l.next_to(gap, DOWN, buff=0.15)
        self.play(GrowArrow(gap), FadeIn(gap_l), run_time=0.7)

        pref = chip("most say steady, flexible funding would help more than short project grants",
                    w=10.6, h=0.8, border=PALETTE["good"], color=PALETTE["good"], fs=19)
        pref.move_to(DOWN * 2.6)
        self.play(FadeIn(pref, shift=UP * 0.1), run_time=0.6)
        self.wait(1.3)


class B08_FairLimits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = Text("what this research is", color=PALETTE["ink"], font_size=24, weight="BOLD")
        rows = VGroup()
        for t in ["answers from the nonprofits themselves",
                  "from nonprofits that already use AI",
                  "so it doesn't describe every nonprofit",
                  "report supported by Google.org"]:
            d = Dot(radius=0.07, color=PALETTE["dim"])
            tx = Text(t, color=PALETTE["ink"], font_size=18)
            rows.add(VGroup(d, tx).arrange(RIGHT, buff=0.25))
        rows.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        l_inner = VGroup(head, rows).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        l_box = card_bg(5.6, 5.0)
        left = VGroup(l_box, l_inner.move_to(l_box.get_center()))
        left.move_to(LEFT * 3.4 + DOWN * 0.2)

        head2 = Text("another view", color=PALETTE["accent"], font_size=24, weight="BOLD")
        who = Text("Bridgespan", color=PALETTE["ink"], font_size=34, weight="BOLD")
        body = fit(Text("skipping AI can be the\nright choice for some\norganizations", color=PALETTE["ink"],
                         font_size=21, line_spacing=1.3), 4.6)
        r_inner = VGroup(head2, who, body).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        r_box = card_bg(5.4, 5.0, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, r_inner.move_to(r_box.get_center()))
        right.move_to(RIGHT * 3.4 + DOWN * 0.2)

        reveal(self, left)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.4)
        reveal(self, right, t2=0.3)
        foot = Text("a fair thing to say out loud", color=PALETTE["dim"], font_size=18)
        foot.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B09_AtTheTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        ty = 0.45  # table top
        people = VGroup(
            person(1.0, PALETTE["ink"]).move_to([-3.4, ty + 0.65, 0]),
            person(1.0, PALETTE["good"]).move_to([-1.9, ty + 0.65, 0]),
            person(1.0, PALETTE["accent"]).move_to([1.9, ty + 0.65, 0]),
            person(1.0, PALETTE["dim"]).move_to([3.4, ty + 0.65, 0]),
        )
        table = RoundedRectangle(corner_radius=0.05, width=8.6, height=0.18,
                                  fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0)
        table.move_to([0, ty, 0])
        legs = VGroup(*[Rectangle(width=0.12, height=1.2, fill_color=PALETTE["dim"], fill_opacity=1,
                                   stroke_width=0) for _ in range(2)])
        legs[0].move_to([-3.9, ty - 0.69, 0])
        legs[1].move_to([3.9, ty - 0.69, 0])
        screen = RoundedRectangle(corner_radius=0.08, width=1.9, height=1.2,
                                   fill_color=PALETTE["bg"], fill_opacity=1,
                                   stroke_color=PALETTE["ink"], stroke_width=2.5)
        screen.move_to([0, ty + 0.09 + 0.6 + 0.12, 0])
        stand = Rectangle(width=0.3, height=0.12, fill_color=PALETTE["ink"], fill_opacity=1, stroke_width=0)
        stand.move_to([0, ty + 0.09 + 0.06, 0])
        glow = Dot(screen.get_center(), radius=0.1, color=PALETTE["accent"])

        self.play(FadeIn(VGroup(people, table, legs), shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(VGroup(screen, stand, glow)), run_time=0.6)

        chips = VGroup(
            chip("start with a real problem", w=3.6, h=0.7, border=PALETTE["good"], color=PALETTE["good"], fs=17),
            chip("keep people involved", w=3.6, h=0.7, border=PALETTE["good"], color=PALETTE["good"], fs=17),
            chip("be open about AI", w=3.6, h=0.7, border=PALETTE["good"], color=PALETTE["good"], fs=17),
        ).arrange(RIGHT, buff=0.35)
        chips.move_to(DOWN * 1.35)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in chips], lag_ratio=0.3), run_time=1.2)

        note = Text("none of it needs a big budget. It mostly needs attention.",
                    color=PALETTE["dim"], font_size=19)
        note.move_to(DOWN * 2.15)
        self.play(FadeIn(note), run_time=0.5)

        q = fit(Text("Who is at the table with us?", color=PALETTE["ink"], font_size=30, weight="BOLD"), 11.0)
        q.move_to(DOWN * 2.95)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.7)
        self.wait(1.5)
