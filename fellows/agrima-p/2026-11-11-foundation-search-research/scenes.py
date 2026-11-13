"""
Manim scenes for foundation-search-research

A warm, fair explainer on what a late-night virtual shade try-on tells a beauty
brand, sourced from the user-supplied article "Your Foundation Search Is Doing
Market Research." No dedicated footage exists (per the user's materials note) --
every visual below is a generated Manim graphic: no real brand or company logos
(source names appear only as plain text) and no photos of real people (faces are
an abstract outline with shade swatches). The cosnova results are labeled
company-reported; the late-night scene and the deep-shade example are labeled
illustrations. Built in the house Claude palette.

Reveals are timed to the narration: each beat's pause points were measured from
its mp3 (silencedetect) and the scene waits to those absolute times.

B00B_AgrimaIntro   -- presenter card: "Hi, I'm Agrima." + lead-in
B01_LateNightTryOn -- 11 p.m., phone + face outline, three shades, a text, tab closed (illustration)
B02_QuietConversation -- shopper <-> brand exchange; three insight rows; what people do vs say
B03_TapToProduct   -- taps and swatches -> make / stock / say; PwC data point + local trends
B04_CosnovaExample -- over 90% / 20%+ / tens of thousands of sessions, all company-reported
B05_GapVisible     -- swatch bar, deepest shades tried but not bought (example); inclusion cards
B06_BackToTheShelf -- near-duplicate shelf trimmed; shopper benefits
B07_NeedsCare      -- lock + toggle; sensitive data; 7 in 10; four advice rows
B08_SameShadeChart -- a shopper and a product team look at one shade chart
B09_SourcesCard    -- two sources + the company-reported / Asia Pacific / illustration notes
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

# foundation shades, light -> deep (illustrative swatches, not real products)
SHADES = ["#F6E0CE", "#EFCDAE", "#E3B792", "#D49F78", "#BD8559", "#9A6840", "#744A2E", "#573622", "#3F2618"]


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
    """Scale down (never up) so the group fits inside max_w x max_h."""
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    if mob.height > max_h:
        mob.scale_to_fit_height(max_h)
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


def wait_until(scene, t):
    d = t - scene.renderer.time
    if d > 0.02:
        scene.wait(d)


def chip(label, w=2.6, h=0.6, border=None, color=None, fs=16):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(Text(label, color=color or PALETTE["ink"], font_size=fs), w - 0.3)
    return VGroup(box, txt.move_to(box.get_center()))


def meter(w, frac, color, h=0.2):
    track = RoundedRectangle(corner_radius=0.08, width=w, height=h, fill_color=PALETTE["border"],
                              fill_opacity=1, stroke_width=0)
    fill = RoundedRectangle(corner_radius=0.08, width=max(w * frac, 0.2), height=h, fill_color=color,
                             fill_opacity=1, stroke_width=0).align_to(track, LEFT)
    return VGroup(track, fill)


def src_chip(label, w=3.4, border=None, color=None):
    return chip(label, w=w, h=0.42, border=border or PALETTE["dim"], color=color or PALETTE["dim"], fs=12)


# --- icons ------------------------------------------------------------------

def person(h=1.0, color=None):
    c = color or PALETTE["ink"]
    head = Circle(radius=0.26 * h, color=c, fill_color=c, fill_opacity=1, stroke_width=0)
    body = RoundedRectangle(corner_radius=0.18 * h, width=0.7 * h, height=0.8 * h,
                             fill_color=c, fill_opacity=1, stroke_width=0)
    return VGroup(head, body).arrange(DOWN, buff=0.05)


def tick(color=None, s=1.0, sw=4):
    t = VMobject(color=color or PALETTE["good"], stroke_width=sw)
    t.set_points_as_corners([[-0.1, 0.0, 0], [-0.02, -0.1, 0], [0.13, 0.12, 0]])
    return t.scale(s)


def cross(color=None, s=1.0, sw=3.5):
    c = color or PALETTE["miss"]
    return VGroup(Line([-0.09, -0.09, 0], [0.09, 0.09, 0], color=c, stroke_width=sw),
                  Line([-0.09, 0.09, 0], [0.09, -0.09, 0], color=c, stroke_width=sw)).scale(s)


def swatch(color, w=0.9, h=0.9, stroke=None):
    return RoundedRectangle(corner_radius=0.1, width=w, height=h, fill_color=color, fill_opacity=1,
                            stroke_color=stroke or PALETTE["ink"], stroke_width=1.5)


def face(r=1.0, tone="#D7AA8A", strips=None):
    """An abstract illustrated face outline (no photo): head, two eye dots, a smile; optional shade strips on a cheek."""
    head = Ellipse(width=1.5 * r, height=1.9 * r, fill_color=tone, fill_opacity=1,
                   stroke_color=PALETTE["ink"], stroke_width=2.5)
    eyes = VGroup(*[Dot(radius=0.06 * r, color=PALETTE["ink"]) for _ in range(2)]).arrange(RIGHT, buff=0.5 * r)
    eyes.move_to(head.get_center() + UP * 0.25 * r)
    smile = Arc(radius=0.32 * r, start_angle=PI * 1.2, angle=PI * 0.6, color=PALETTE["ink"], stroke_width=2.5)
    smile.move_to(head.get_center() + DOWN * 0.42 * r)
    g = VGroup(head, eyes, smile)
    if strips:
        st = VGroup(*[Rectangle(width=0.5 * r, height=0.2 * r, fill_color=c, fill_opacity=1, stroke_width=0)
                      for c in strips]).arrange(DOWN, buff=0)
        st.move_to(head.get_center() + RIGHT * 0.2 * r + DOWN * 0.05 * r)
        g.add(st)
    return g


def phone(w=3.0, h=5.0):
    body = RoundedRectangle(corner_radius=0.3, width=w, height=h, fill_color=PALETTE["card"], fill_opacity=1,
                            stroke_color=PALETTE["ink"], stroke_width=3)
    screen = RoundedRectangle(corner_radius=0.2, width=w - 0.3, height=h - 0.4, fill_color=PALETTE["bg"],
                              fill_opacity=1, stroke_width=0).move_to(body.get_center())
    return VGroup(body, screen)


def bottle(color, s=1.0):
    body = RoundedRectangle(corner_radius=0.08 * s, width=0.46 * s, height=0.78 * s, fill_color=color,
                            fill_opacity=1, stroke_color=PALETTE["ink"], stroke_width=1.5)
    cap = Rectangle(width=0.22 * s, height=0.22 * s, fill_color=PALETTE["ink"], fill_opacity=1, stroke_width=0)
    cap.next_to(body, UP, buff=0)
    return VGroup(body, cap)


def lock_icon(s=1.0, color=None):
    c = color or PALETTE["ink"]
    shackle = Arc(radius=0.3 * s, start_angle=0, angle=PI, color=c, stroke_width=6 * s)
    body = RoundedRectangle(corner_radius=0.08 * s, width=0.8 * s, height=0.62 * s, fill_color=c,
                            fill_opacity=1, stroke_width=0)
    shackle.next_to(body, UP, buff=-0.02)
    keyhole = Dot(radius=0.07 * s, color=PALETTE["card"]).move_to(body.get_center())
    return VGroup(shackle, body, keyhole)


def toggle(on=True, s=1.0):
    col = PALETTE["good"] if on else PALETTE["dim"]
    track = RoundedRectangle(corner_radius=0.25 * s, width=1.0 * s, height=0.5 * s, fill_color=col,
                             fill_opacity=1, stroke_width=0)
    knob = Circle(radius=0.19 * s, fill_color=PALETTE["card"], fill_opacity=1, stroke_width=0)
    knob.move_to(track.get_right() + LEFT * 0.25 * s if on else track.get_left() + RIGHT * 0.25 * s)
    return VGroup(track, knob)


# --- scenes -----------------------------------------------------------------

class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=40)
        summary = fit(Text(
            "Today: how late-night shade testing helps\nbeauty brands decide what to make next.",
            color=PALETTE["ink"], font_size=26, line_spacing=1.3, should_center=True), 8.6)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        wait_until(self, 6.7)


class B01_LateNightTryOn(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # persistent illustration label
        note = chip("illustration -- not a real case", w=4.4, h=0.45, border=PALETTE["ink"], color=PALETTE["ink"], fs=14)
        note.move_to([0, 3.05, 0])

        # 11 p.m.: moon + clock
        moon = VGroup(Circle(radius=0.34, fill_color=PALETTE["wood"], fill_opacity=1, stroke_width=0),
                      Circle(radius=0.3, fill_color=PALETTE["bg"], fill_opacity=1, stroke_width=0).shift(RIGHT * 0.2 + UP * 0.1))
        clock = chip("11:00 p.m.", w=2.0, h=0.55, border=PALETTE["ink"], color=PALETTE["ink"], fs=18)
        night = VGroup(moon, clock).arrange(RIGHT, buff=0.3).move_to([-4.6, 2.35, 0])

        # desk + snack
        plank = desk = RoundedRectangle(corner_radius=0.05, width=4.6, height=0.3, fill_color=PALETTE["wood"],
                                        fill_opacity=1, stroke_width=0).move_to([-4.0, -1.75, 0])
        cookie = Circle(radius=0.42, fill_color="#D8B07A", fill_opacity=1, stroke_color=PALETTE["wood"], stroke_width=2)
        chips = VGroup(*[Dot(radius=0.05, color=PALETTE["ink"]).move_to(cookie.get_center() + np.array(p))
                         for p in ((-0.15, 0.12, 0), (0.17, 0.05, 0), (0.0, -0.2, 0), (-0.2, -0.12, 0))])
        snack = VGroup(cookie, chips).next_to(plank, UP, buff=0).shift(LEFT * 0.9)
        snack_l = Text("a snack", color=PALETTE["dim"], font_size=15).next_to(snack, UP, buff=0.12)

        # phone with a face + swatches
        ph = phone(3.0, 5.0).move_to([0.6, -0.1, 0])
        screen = ph[1]
        fc = face(0.95, tone="#D7AA8A").move_to(screen.get_center() + UP * 0.5)
        tab = chip("try on", w=1.3, h=0.4, border=PALETTE["accent"], color=PALETTE["accent"], fs=14)
        tab.move_to(screen.get_top() + DOWN * 0.35)
        pale, orange, almost = "#F7E3D3", "#E0944F", "#D9AE8E"
        sw = VGroup(*[swatch(c, 0.62, 0.62) for c in (pale, orange, almost)]).arrange(RIGHT, buff=0.22)
        sw.move_to(screen.get_center() + DOWN * 1.35)

        # verdict rows on the right
        def row(col, label, mark, mcol):
            s = swatch(col, 0.5, 0.5)
            t = Text(label, color=PALETTE["ink"], font_size=22)
            m = mark.copy().set_color(mcol)
            return VGroup(s, t, m).arrange(RIGHT, buff=0.3)
        r1 = row(pale, "too pale", cross(s=1.4), PALETTE["miss"])
        r2 = row(orange, "too orange", cross(s=1.4), PALETTE["miss"])
        r3 = row(almost, "almost right", tick(s=1.6), PALETTE["good"])
        rows = VGroup(r1, r2, r3).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to([4.5, 0.3, 0])

        # a text arrives, the tab closes
        ding = VGroup(card_bg(2.3, 0.5, stroke_color=PALETTE["accent"]),
                      Text("new text", color=PALETTE["accent"], font_size=16))
        ding[1].move_to(ding[0].get_center())
        ding.move_to(tab.get_center())
        closed = chip("tab closed", w=1.9, h=0.45, border=PALETTE["dim"], color=PALETTE["dim"], fs=15)
        closed.move_to(screen.get_center())

        nothing = VGroup(cross(s=1.4), Text("bought nothing", color=PALETTE["ink"], font_size=22)).arrange(RIGHT, buff=0.2)
        nothing.move_to([-4.0, 0.55, 0])

        clue = Dot(radius=0.16, color=PALETTE["accent"])
        clue_ring = Circle(radius=0.4, color=PALETTE["accent"], stroke_width=3)
        clue_txt = Text("a small clue just arrived", color=PALETTE["accent"], font_size=24, weight="BOLD")
        clue_row = VGroup(VGroup(clue_ring, clue), clue_txt).arrange(RIGHT, buff=0.3).move_to([0, -3.05, 0])

        self.play(FadeIn(night, shift=DOWN * 0.1), FadeIn(note), run_time=0.7)
        wait_until(self, 1.6)
        self.play(FadeIn(plank), FadeIn(snack), FadeIn(snack_l), run_time=0.6)
        self.play(FadeIn(ph), FadeIn(fc), FadeIn(tab), run_time=0.8)
        wait_until(self, 5.9)
        self.play(FadeIn(sw, shift=UP * 0.1), run_time=0.6)
        wait_until(self, 8.9)
        self.play(FadeIn(r1, shift=LEFT * 0.15), run_time=0.45)
        wait_until(self, 10.1)
        self.play(FadeIn(r2, shift=LEFT * 0.15), run_time=0.45)
        wait_until(self, 11.7)
        self.play(FadeIn(r3, shift=LEFT * 0.15), run_time=0.45)
        wait_until(self, 13.2)
        self.play(FadeOut(tab), FadeIn(ding, shift=DOWN * 0.1), run_time=0.45)
        self.play(FadeOut(fc), FadeOut(sw), FadeOut(ding), FadeIn(closed), run_time=0.7)
        wait_until(self, 15.4)
        self.play(FadeIn(nothing, shift=RIGHT * 0.1), run_time=0.5)
        wait_until(self, 19.0)
        self.play(FadeIn(clue_row, shift=UP * 0.1), run_time=0.6)
        self.play(clue_ring.animate.scale(1.5).set_stroke(opacity=0.2), run_time=0.9)
        wait_until(self, 24.27)


class B02_QuietConversation(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # left: the shopper
        sp = phone(1.9, 3.0)
        sf = face(0.62, strips=("#E8C4A6", "#D9AE8E", "#C99572")).move_to(sp[1].get_center() + UP * 0.1)
        sl = Text("the shopper", color=PALETTE["ink"], font_size=20, weight="BOLD")
        l_in = VGroup(VGroup(sp, sf), sl).arrange(DOWN, buff=0.3)
        l_box = card_bg(3.1, 4.5)
        left = VGroup(l_box, fit_in(l_in, 2.7, 4.1).move_to(l_box.get_center())).move_to([-4.6, 0.25, 0])

        # right: the brand's insight panel
        bl = Text("the brand", color=PALETTE["ink"], font_size=20, weight="BOLD")

        def insight(label, frac):
            return VGroup(Text(label, color=PALETTE["ink"], font_size=16), meter(3.2, frac, PALETTE["accent"], h=0.18)
                          ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        i1 = insight("which products are tried most", 0.85)
        i2 = insight("where customers hesitate", 0.55)
        i3 = insight("how personalization affects confidence to buy", 0.7)
        i3[0].scale_to_fit_width(3.2) if i3[0].width > 3.2 else None
        irows = VGroup(i1, i2, i3).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        r_in = VGroup(bl, irows).arrange(DOWN, buff=0.35)
        r_box = card_bg(4.3, 4.5, stroke_color=PALETTE["accent"])
        right = VGroup(r_box, fit_in(r_in, 3.9, 4.1).move_to(r_box.get_center())).move_to([4.2, 0.25, 0])

        # arrows both ways
        a_to_shopper = Arrow([1.6, 1.05, 0], [-2.7, 1.05, 0], buff=0, color=PALETTE["dim"], stroke_width=5,
                             max_tip_length_to_length_ratio=0.12)
        a_to_brand = Arrow([-2.7, -0.55, 0], [1.9, -0.55, 0], buff=0, color=PALETTE["accent"], stroke_width=5,
                           max_tip_length_to_length_ratio=0.12)
        a1l = Text("the try-on helps the shopper", color=PALETTE["dim"], font_size=17).next_to(a_to_shopper, UP, buff=0.12)
        a2l = Text("it also works the other way around", color=PALETTE["accent"], font_size=17).next_to(a_to_brand, UP, buff=0.12)

        arb = src_chip("Arbelle, 2026", 2.2).move_to([4.2, -2.4, 0])
        ins = chip("every interaction creates insight", w=4.4, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=16)
        ins.move_to([0.1, 2.95, 0])

        do = chip("what people DO", w=2.6, h=0.55, border=PALETTE["accent"], color=PALETTE["accent"], fs=17)
        say = chip("what they say", w=2.6, h=0.55, border=PALETTE["dim"], color=PALETTE["dim"], fs=17)
        norev = chip("no review needed", w=2.6, h=0.55, border=PALETTE["good"], color=PALETTE["good"], fs=17)
        bottom = VGroup(do, say, norev).arrange(RIGHT, buff=0.3).move_to([-0.6, -3.0, 0])

        for r_ in (i1, i2, i3):
            r_.set_opacity(0)
        reveal(self, left)
        wait_until(self, 3.7)
        self.play(GrowArrow(a_to_shopper), FadeIn(a1l), run_time=0.7)
        wait_until(self, 5.8)
        self.play(GrowArrow(a_to_brand), FadeIn(a2l), run_time=0.7)
        wait_until(self, 7.2)
        self.play(FadeIn(ins, shift=DOWN * 0.1), run_time=0.5)
        reveal(self, right, t1=0.4, t2=0.4)
        self.play(FadeIn(arb), run_time=0.3)
        wait_until(self, 13.0)
        self.play(i1.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 13.9)
        self.play(i2.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 15.6)
        self.play(i3.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 19.0)
        self.play(FadeIn(do, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 20.6)
        self.play(FadeIn(say, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 22.0)
        self.play(FadeIn(norev, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 24.27)


class B03_TapToProduct(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # taps + swatches
        taps = VGroup(*[VGroup(swatch(c, 0.55, 0.55), Circle(radius=0.38, color=PALETTE["accent"], stroke_width=2.5))
                        for c in ("#EFCDAE", "#D49F78", "#9A6840")])
        for t in taps:
            t[1].move_to(t[0].get_center())
        taps.arrange(DOWN, buff=0.35)
        tl = Text("taps and swatches", color=PALETTE["ink"], font_size=17)
        t_in = VGroup(taps, tl).arrange(DOWN, buff=0.3)
        t_box = card_bg(2.5, 4.4)
        tcard = VGroup(t_box, fit_in(t_in, 2.2, 4.0).move_to(t_box.get_center())).move_to([-5.0, 0.15, 0])

        def label_card(big, small, col):
            b = card_bg(3.9, 1.2, stroke_color=col)
            inner = VGroup(Text(big, color=PALETTE["ink"], font_size=26, weight="BOLD"),
                           Text(small, color=PALETTE["dim"], font_size=16)).arrange(DOWN, buff=0.1)
            return VGroup(b, fit(inner, 3.5).move_to(b.get_center()))
        c1 = label_card("what to make", "product development", PALETTE["accent"])
        c2 = label_card("what to stock and show", "merchandising", PALETTE["accent"])
        c3 = label_card("what to say", "marketing", PALETTE["accent"])
        labels = VGroup(c1, c2, c3).arrange(DOWN, buff=0.3).move_to([-1.1, 0.15, 0])
        arb = src_chip("Arbelle, 2026", 2.2).move_to([-1.1, -2.95, 0])
        arrow = Arrow([-3.55, 0.15, 0], [-3.15, 0.15, 0], buff=0, color=PALETTE["accent"], stroke_width=5,
                      max_tip_length_to_length_ratio=0.9)

        # PwC card
        ph = Text("PwC Malaysia", color=PALETTE["ink"], font_size=19, weight="BOLD")
        dp = lines("every interaction is a data point\nthat improves the model\nand the product", 16, PALETTE["ink"], buff=0.08)
        lt = Text("small local trends", color=PALETTE["dim"], font_size=16)
        g1 = chip("glass skin -- Korea", w=3.4, h=0.5, fs=16)
        g2 = chip("no-makeup -- Japan", w=3.4, h=0.5, fs=16)
        src = src_chip("PwC Malaysia, 2026", 2.8)
        p_in = VGroup(ph, dp, lt, VGroup(g1, g2).arrange(DOWN, buff=0.18), src).arrange(DOWN, buff=0.25)
        p_box = card_bg(4.2, 4.9, stroke_color=PALETTE["good"])
        pcard = VGroup(p_box, fit_in(p_in, 3.8, 4.5).move_to(p_box.get_center())).move_to([4.0, 0.0, 0])

        for r_ in (dp, lt, g1, g2, src):
            r_.set_opacity(0)

        wait_until(self, 1.6)
        reveal(self, tcard)
        wait_until(self, 2.9)
        self.play(GrowArrow(arrow), run_time=0.4)
        wait_until(self, 4.6)
        reveal(self, c1, t1=0.3, t2=0.3)
        wait_until(self, 5.9)
        reveal(self, c2, t1=0.3, t2=0.3)
        wait_until(self, 6.9)
        reveal(self, c3, t1=0.3, t2=0.3)
        self.play(FadeIn(arb), run_time=0.3)
        wait_until(self, 8.6)
        reveal(self, pcard, t1=0.4, t2=0.4)
        wait_until(self, 11.5)
        self.play(dp.animate.set_opacity(1), run_time=0.6)
        wait_until(self, 17.3)
        self.play(lt.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 20.1)
        self.play(g1.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 22.3)
        self.play(g2.animate.set_opacity(1), src.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 24.16)


class B04_CosnovaExample(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        head = chip("cosnova -- AI shade matching", w=4.6, h=0.5, border=PALETTE["ink"], color=PALETTE["ink"], fs=17)
        head.move_to(UP * 3.0)
        badge = chip("COMPANY-REPORTED", w=3.4, h=0.5, border=PALETTE["miss"], color=PALETTE["miss"], fs=16)
        badge.move_to(UP * 2.35)

        def stat(n, fs, label, col):
            return VGroup(Text(n, color=col, font_size=fs, weight="BOLD"),
                          lines(label, 16, PALETTE["ink"], buff=0.06)).arrange(DOWN, buff=0.2)

        s1 = stat("over 90%", 46, "consumer satisfaction", PALETTE["accent"])
        m1 = meter(2.9, 0.9, PALETTE["accent"], h=0.2)
        i1 = VGroup(s1, m1).arrange(DOWN, buff=0.4)
        b1 = card_bg(3.8, 3.0)
        c1 = VGroup(b1, fit_in(i1, 3.4, 2.7).move_to(b1.get_center()))

        s2 = stat("20%+", 46, "increase in add-to-cart rates", PALETTE["good"])
        up = Arrow([0, -0.3, 0], [0, 0.3, 0], buff=0, color=PALETTE["good"], stroke_width=6,
                   max_tip_length_to_length_ratio=0.8)
        i2 = VGroup(s2, up).arrange(DOWN, buff=0.35)
        b2 = card_bg(3.8, 3.0)
        c2 = VGroup(b2, fit_in(i2, 3.4, 2.7).move_to(b2.get_center()))

        dots = VGroup(*[Dot(radius=0.07, color=PALETTE["accent"]) for _ in range(30)]).arrange_in_grid(
            rows=3, cols=10, buff=0.14)
        s3 = stat("tens of thousands", 28, "of shopper sessions", PALETTE["ink"])
        i3 = VGroup(s3, dots).arrange(DOWN, buff=0.3)
        b3 = card_bg(3.8, 3.0)
        c3 = VGroup(b3, fit_in(i3, 3.4, 2.7).move_to(b3.get_center()))

        cards = VGroup(c1, c2, c3).arrange(RIGHT, buff=0.35).move_to(DOWN * 0.5)
        src = src_chip("Arbelle, 2026 -- reporting on cosnova", 4.4).move_to([0, -2.4, 0])
        foot = Text("Arbelle sells this kind of technology: company-reported, not independent research",
                    color=PALETTE["miss"], font_size=19, weight="BOLD")
        fit(foot, 11.5).move_to([0, -3.05, 0])

        wait_until(self, 1.7)
        self.play(FadeIn(head, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 6.7)
        self.play(FadeIn(badge, shift=DOWN * 0.1), run_time=0.4)
        reveal(self, c1, t1=0.4, t2=0.4)
        wait_until(self, 10.7)
        reveal(self, c2, t1=0.4, t2=0.4)
        wait_until(self, 14.4)
        reveal(self, c3, t1=0.4, t2=0.4)
        self.play(FadeIn(src), run_time=0.3)
        wait_until(self, 18.1)
        self.play(FadeIn(foot, shift=UP * 0.1), run_time=0.6)
        wait_until(self, 24.1)


class B05_GapVisible(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        ex = chip("EXAMPLE -- not a real case", w=4.4, h=0.45, border=PALETTE["ink"], color=PALETTE["ink"], fs=14)
        ex.move_to([-3.9, 3.05, 0])

        # swatch bar, light -> deep
        sws = VGroup(*[swatch(c, 1.1, 1.0, stroke=PALETTE["border"]) for c in SHADES]).arrange(RIGHT, buff=0.12)
        sws.move_to([0, 1.55, 0])
        deep = VGroup(*sws[-3:])
        box = SurroundingRectangle(deep, color=PALETTE["accent"], buff=0.08, stroke_width=4, corner_radius=0.1)
        tried = Text("tried again and again", color=PALETTE["accent"], font_size=18, weight="BOLD")
        tried.next_to(box, UP, buff=0.1)

        ticks = VGroup(*[tick(s=1.3).move_to(sws[i].get_bottom() + DOWN * 0.3) for i in range(6)])
        crosses = VGroup(*[cross(s=1.3).move_to(sws[i].get_bottom() + DOWN * 0.3) for i in range(6, 9)])
        bought = Text("bought", color=PALETTE["good"], font_size=15).next_to(ticks[2], DOWN, buff=0.08)
        left_b = Text("left without buying", color=PALETTE["miss"], font_size=15).next_to(crosses[1], DOWN, buff=0.08)

        hint = chip("a hint: maybe no close match in the range", w=5.6, h=0.55, border=PALETTE["accent"],
                    color=PALETTE["accent"], fs=17).move_to([-2.0, -0.35, 0])
        see = chip("try-on data makes it visible", w=4.2, h=0.55, border=PALETTE["good"], color=PALETTE["good"],
                   fs=17).move_to([3.6, -0.35, 0])

        def info(title, body, col, w=3.9, h=1.8):
            b = card_bg(w, h, stroke_color=col)
            inner = VGroup(Text(title, color=col, font_size=17, weight="BOLD"),
                           lines(body, 16, PALETTE["ink"], buff=0.07)).arrange(DOWN, buff=0.14)
            return VGroup(b, fit_in(inner, w - 0.4, h - 0.3).move_to(b.get_center()))
        k1 = info("Arbelle", "shoppers want to see\nthemselves in shade ranges", PALETTE["accent"])
        k2 = info("PwC", "narrow data can make shade\nmatchers miss mid-to-deep tones", PALETTE["good"])
        k3 = info("so brands", "test across skin tones\nand keep humans in the loop:\nbeauty advisors, dermatologists",
                  PALETTE["ink"])
        cards = VGroup(k1, k2, k3).arrange(RIGHT, buff=0.25).move_to([0, -1.9, 0])
        close = Text("The data raises the question. A person decides.", color=PALETTE["ink"], font_size=22,
                     weight="BOLD").move_to([0, -3.15, 0])

        self.play(FadeIn(ex), run_time=0.5)
        wait_until(self, 2.7)
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.1) for s in sws], lag_ratio=0.1), run_time=1.6)
        wait_until(self, 5.9)
        self.play(Create(box), FadeIn(tried), run_time=0.6)
        wait_until(self, 6.1)
        self.play(FadeIn(ticks), FadeIn(bought), run_time=0.4)
        self.play(FadeIn(crosses), FadeIn(left_b), run_time=0.5)
        wait_until(self, 8.0)
        self.play(FadeIn(hint, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 12.0)
        self.play(FadeIn(see, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 14.5)
        reveal(self, k1, t1=0.35, t2=0.35)
        wait_until(self, 18.5)
        reveal(self, k2, t1=0.35, t2=0.35)
        wait_until(self, 23.9)
        reveal(self, k3, t1=0.35, t2=0.35)
        wait_until(self, 30.4)
        self.play(FadeIn(close, shift=UP * 0.1), run_time=0.6)
        wait_until(self, 33.69)


class B06_BackToTheShelf(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # a shelf of near-duplicate shades
        tones = ["#E3B792", "#E0B38C", "#DDAE88", "#E3B792", "#D8A982", "#D49F78", "#D9A57D", "#D2A079", "#DDAE88", "#D49F78"]
        bots = VGroup(*[bottle(c, 1.15) for c in tones]).arrange(RIGHT, buff=0.35)
        bots.move_to([0, 1.35, 0])
        plank = Rectangle(width=bots.width + 0.8, height=0.14, fill_color=PALETTE["wood"], fill_opacity=1,
                          stroke_width=0).next_to(bots, DOWN, buff=0)
        shelf_l = Text("near-duplicate shades", color=PALETTE["dim"], font_size=17).next_to(plank, DOWN, buff=0.12)
        pwc = src_chip("PwC Malaysia, 2026", 2.8).move_to([3.7, 0.32, 0])

        trim_idx = (1, 3, 6, 8)
        keep_idx = (0, 5, 9)
        trim_note = chip("trim the long tail", w=3.0, h=0.5, border=PALETTE["miss"], color=PALETTE["miss"], fs=16)
        trim_note.move_to([-3.6, 2.95, 0])
        best_note = chip("the best get more attention", w=3.8, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=16)
        best_note.move_to([3.4, 2.95, 0])
        yours = Text("yours", color=PALETTE["good"], font_size=20, weight="BOLD")

        # shopper benefits
        def ben(label, col):
            b = card_bg(3.9, 0.85, stroke_color=col)
            t = fit(Text(label, color=PALETTE["ink"], font_size=20), 3.5)
            return VGroup(b, t.move_to(b.get_center()))
        b1 = ben("fewer returns", PALETTE["good"])
        b2 = ben("bigger basket", PALETTE["good"])
        b3 = ben("less sampling waste\nand over-ordering".replace("\n", " "), PALETTE["good"])
        bens = VGroup(b1, b2, b3).arrange(RIGHT, buff=0.25).move_to([0, -2.1, 0])
        arb = src_chip("Arbelle, 2026", 2.2).move_to([0, -2.95, 0])
        shopper = Text("for the shopper: fewer near-duplicates, an easier time finding yours", color=PALETTE["dim"],
                       font_size=17).move_to([0, -0.85, 0])

        wait_until(self, 1.4)
        self.play(FadeIn(plank), LaggedStart(*[FadeIn(b, shift=UP * 0.1) for b in bots], lag_ratio=0.08), run_time=1.6)
        self.play(FadeIn(shelf_l), FadeIn(pwc), run_time=0.4)
        wait_until(self, 5.8)
        self.play(FadeIn(trim_note, shift=DOWN * 0.1), *[bots[i].animate.set_opacity(0.22) for i in trim_idx], run_time=0.8)
        crs = VGroup(*[cross(s=1.5).move_to(bots[i].get_center()) for i in trim_idx])
        self.play(FadeIn(crs), run_time=0.4)
        wait_until(self, 8.5)
        rings = VGroup(*[SurroundingRectangle(bots[i], color=PALETTE["accent"], buff=0.08, stroke_width=3,
                                              corner_radius=0.08) for i in keep_idx])
        self.play(Create(rings), FadeIn(best_note, shift=DOWN * 0.1), run_time=0.7)
        wait_until(self, 11.8)
        self.play(FadeIn(shopper, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 14.4)
        yours.move_to(bots[5].get_top() + UP * 0.55)
        your_ring = SurroundingRectangle(bots[5], color=PALETTE["good"], buff=0.12, stroke_width=4, corner_radius=0.1)
        self.play(FadeOut(rings[1]), Create(your_ring), FadeIn(yours, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 16.8)
        reveal(self, b1, t1=0.3, t2=0.3)
        wait_until(self, 19.8)
        reveal(self, b2, t1=0.3, t2=0.3)
        wait_until(self, 21.6)
        reveal(self, b3, t1=0.3, t2=0.3)
        self.play(FadeIn(arb), run_time=0.3)
        wait_until(self, 23.86)


class B07_NeedsCare(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # left card: what a try-on uses + 7 in 10
        lk = lock_icon(1.2)
        lt = Text("a try-on uses your face", color=PALETTE["ink"], font_size=22, weight="BOLD")
        head = VGroup(lk, lt).arrange(RIGHT, buff=0.35)
        c1 = chip("face scans", w=1.9, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=16)
        c2 = chip("skin condition", w=2.2, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=16)
        c3 = chip("behavior patterns", w=2.5, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=16)
        chips_row = VGroup(c1, c2, c3).arrange(RIGHT, buff=0.15)
        sens = Text("sensitive information", color=PALETTE["dim"], font_size=15)
        dots = VGroup(*[Circle(radius=0.14, fill_color=PALETTE["accent"] if i < 7 else PALETTE["border"], fill_opacity=1,
                               stroke_width=0) for i in range(10)]).arrange(RIGHT, buff=0.16)
        big = Text("about 7 in 10", color=PALETTE["accent"], font_size=40, weight="BOLD")
        apc = lines("in Asia Pacific say they are concerned about\nhow companies collect their information", 16,
                    PALETTE["ink"], buff=0.07)
        src = src_chip("PwC Malaysia, 2026", 2.8)
        l_in = VGroup(head, VGroup(sens, chips_row).arrange(DOWN, buff=0.15), VGroup(big, dots, apc).arrange(DOWN, buff=0.18),
                      src).arrange(DOWN, buff=0.3)
        l_box = card_bg(6.2, 5.6)
        left = VGroup(l_box, fit_in(l_in, 5.7, 5.2).move_to(l_box.get_center())).move_to([-3.35, 0.0, 0])

        # right card: the advice, tick by tick
        rh = Text("PwC's practical advice", color=PALETTE["good"], font_size=20, weight="BOLD")

        def adv(label):
            t = Text(label, color=PALETTE["ink"], font_size=20)
            return VGroup(tick(s=1.4), fit(t, 4.3)).arrange(RIGHT, buff=0.3)
        a1 = adv("collect only what's necessary")
        a2 = adv("explain what it's for")
        a3 = adv("process on the device when possible")
        a4 = adv("clear ways to opt out")
        advs = VGroup(a1, a2, a3, a4).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        tg_off = toggle(False, 1.1)
        tg_label = Text("opt out", color=PALETTE["dim"], font_size=17)
        tg = VGroup(tg_label, tg_off).arrange(RIGHT, buff=0.25)
        r_in = VGroup(rh, advs, tg).arrange(DOWN, buff=0.4)
        r_box = card_bg(5.6, 5.6, stroke_color=PALETTE["good"])
        right = VGroup(r_box, fit_in(r_in, 5.2, 5.2).move_to(r_box.get_center())).move_to([3.6, 0.0, 0])

        for r_ in (sens, c1, c2, c3, big, dots, apc, src, a1, a2, a3, a4, tg):
            r_.set_opacity(0)
        wait_until(self, 1.0)
        reveal(self, left, t1=0.4, t2=0.5)
        wait_until(self, 8.4)
        self.play(sens.animate.set_opacity(1), c1.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 9.5)
        self.play(c2.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 10.6)
        self.play(c3.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 12.1)
        self.play(big.animate.set_opacity(1), run_time=0.4)
        self.play(dots.animate.set_opacity(1), apc.animate.set_opacity(1), src.animate.set_opacity(1), run_time=1.0)
        wait_until(self, 16.8)
        reveal(self, right, t1=0.4, t2=0.4)
        wait_until(self, 18.2)
        self.play(a1.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 19.4)
        self.play(a2.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 21.2)
        self.play(a3.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 25.5)
        self.play(a4.animate.set_opacity(1), tg.animate.set_opacity(1), run_time=0.4)
        tg_on = toggle(True, 1.1).move_to(tg_off.get_center())
        self.play(Transform(tg_off, tg_on), tg_label.animate.set_color(PALETTE["good"]), run_time=0.6)
        wait_until(self, 27.28)


class B08_SameShadeChart(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        chart_sw = VGroup(*[swatch(c, 0.9, 0.9, stroke=PALETTE["border"]) for c in SHADES]).arrange_in_grid(
            rows=3, cols=3, buff=0.12)
        chart_t = Text("shade chart", color=PALETTE["dim"], font_size=18)
        c_in = VGroup(chart_sw, chart_t).arrange(DOWN, buff=0.25)
        c_box = card_bg(3.7, 4.1, stroke_color=PALETTE["wood"])
        chart = VGroup(c_box, c_in.move_to(c_box.get_center())).move_to([0, 0.35, 0])

        shopper = person(1.5, PALETTE["accent"]).move_to([-4.6, 0.2, 0])
        sh_l = Text("the shopper", color=PALETTE["ink"], font_size=20, weight="BOLD").next_to(shopper, DOWN, buff=0.25)
        team = VGroup(*[person(1.25, PALETTE["ink"]) for _ in range(3)]).arrange(RIGHT, buff=0.3).move_to([4.7, 0.2, 0])
        tm_l = Text("the product team", color=PALETTE["ink"], font_size=20, weight="BOLD").next_to(team, DOWN, buff=0.25)

        sight_l = DashedLine(shopper.get_right() + RIGHT * 0.1, chart.get_left() + LEFT * 0.05,
                             color=PALETTE["accent"], stroke_width=3)
        sight_r = DashedLine(team.get_left() + LEFT * 0.1, chart.get_right() + RIGHT * 0.05,
                             color=PALETTE["ink"], stroke_width=3)

        s_chip = chip("not a survey", w=2.4, h=0.5, border=PALETTE["dim"], color=PALETTE["dim"], fs=16)
        r_chip = chip("not a review", w=2.4, h=0.5, border=PALETTE["dim"], color=PALETTE["dim"], fs=16)
        nots = VGroup(s_chip, r_chip).arrange(RIGHT, buff=0.3).move_to([0, 3.05, 0])
        strikes = VGroup(*[cross(s=1.6).move_to(c.get_left() + RIGHT * 0.3) for c in (s_chip, r_chip)])
        m_l = Text("better matches, a wider range that includes them", color=PALETTE["accent"], font_size=19,
                   weight="BOLD")
        fit(m_l, 5.6).move_to([-3.4, -2.95, 0])
        n_l = Text("a clearer idea of what to make next", color=PALETTE["ink"], font_size=19, weight="BOLD")
        fit(n_l, 5.6).move_to([3.4, -2.95, 0])

        self.play(FadeIn(chart, shift=UP * 0.1), run_time=0.7)
        wait_until(self, 2.9)
        self.play(FadeIn(shopper), FadeIn(sh_l), run_time=0.5)
        self.play(FadeIn(team), FadeIn(tm_l), run_time=0.5)
        wait_until(self, 5.5)
        self.play(FadeIn(nots), run_time=0.4)
        self.play(FadeIn(strikes), run_time=0.3)
        wait_until(self, 7.8)
        self.play(Create(sight_l), Create(sight_r), run_time=0.8)
        wait_until(self, 12.6)
        self.play(FadeIn(m_l, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 16.5)
        self.play(FadeIn(n_l, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 19.11)


class B09_SourcesCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        def source(name, cite, note, col):
            h = Text(name, color=PALETTE["ink"], font_size=24, weight="BOLD")
            c = fit(Text(cite, color=PALETTE["dim"], font_size=15), 10.4)
            n = chip(note, w=9.8, h=0.5, border=col, color=col, fs=17)
            inner = VGroup(h, c, n).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
            n.align_to(h, LEFT)
            b = card_bg(11.4, 1.95)
            return VGroup(b, inner.move_to(b.get_center()))
        s1 = source("Arbelle (2026, January 19)",
                    "Beauty consumer trends 2026: How to win the modern beauty consumer",
                    "sells virtual try-on and shade-finder technology: customer results are company-reported",
                    PALETTE["miss"])
        s2 = source("Mani & Narayanan, PwC Malaysia (2026, May 19)",
                    "Beauty and the (AI) beast: The makeover of personalisation, simplicity, and trust",
                    "a consulting firm's report that focuses on the Asia Pacific market",
                    PALETTE["accent"])
        ill = chip("illustrations, not real cases: the late-night scene and the deep-shade example", w=11.4, h=0.6,
                   border=PALETTE["ink"], color=PALETTE["ink"], fs=19)
        stack = VGroup(s1, s2, ill).arrange(DOWN, buff=0.3).move_to(DOWN * 0.15)
        s1[1][2].set_opacity(0)
        s2[1][2].set_opacity(0)
        title = Text("A note on sources", color=PALETTE["ink"], font_size=26, weight="BOLD").move_to([0, 3.0, 0])

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 1.7)
        reveal(self, s1, t1=0.4, t2=0.4)
        wait_until(self, 5.6)
        self.play(s1[1][2].animate.set_opacity(1), run_time=0.4)
        wait_until(self, 8.6)
        reveal(self, s2, t1=0.4, t2=0.4)
        self.play(s2[1][2].animate.set_opacity(1), run_time=0.4)
        wait_until(self, 12.3)
        self.play(FadeIn(ill, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 15.91)
