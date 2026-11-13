"""
Portrait (9:16) Manim scenes for real-art-new-light-short

Ports of the seven graphic beats kept in the Short (B00B, B01, B03, B04, B05, B08,
B09). B00 (cold open), B02 (three habits), B06 (Harvard and Koblenz) and B07 (ideas
anyone could borrow) are dropped to fit the 3:00 Shorts cap (see short/FACTCHECK.md).
Stacked layouts for a 4.5 x 8.0 frame; same palette, copy and audio timing as the
16:9 scenes. All visuals are generated: no real artwork, no likeness of Salvador Dali
or any real person, no museum or company logos. The Rijksmuseum story is labeled a
wire report, the Dali review 2019, and the opening scene an illustration.
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


def lines(txt, fs, color, max_w=None, buff=0.07, weight=None):
    kw = {"weight": weight} if weight else {}
    g = VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split("\n")]).arrange(DOWN, buff=buff)
    return fit(g, max_w) if max_w else g


def wait_until(scene, t):
    d = t - scene.renderer.time
    if d > 0.02:
        scene.wait(d)


def chip(label, w=2.6, h=0.42, border=None, color=None, fs=13):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(lines(label, fs, color or PALETTE["ink"], buff=0.05), w - 0.2)
    return VGroup(box, txt.move_to(box.get_center()))


def src_chip(label, w=3.6, fs=10):
    return chip(label, w=w, h=0.34, border=PALETTE["dim"], color=PALETTE["dim"], fs=fs)


def tick(color=None, s=1.0, sw=4):
    t = VMobject(color=color or PALETTE["good"], stroke_width=sw)
    t.set_points_as_corners([[-0.1, 0.0, 0], [-0.02, -0.1, 0], [0.13, 0.12, 0]])
    return t.scale(s)


def person(h=1.0, color=None):
    c = color or PALETTE["ink"]
    head = Circle(radius=0.26 * h, color=c, fill_color=c, fill_opacity=1, stroke_width=0)
    body = RoundedRectangle(corner_radius=0.18 * h, width=0.7 * h, height=0.8 * h,
                            fill_color=c, fill_opacity=1, stroke_width=0)
    return VGroup(head, body).arrange(DOWN, buff=0.05)


def painting(w=3.2, h=2.2, frame=True):
    """A GENERIC abstract painting (sun + two hills). Not a copy or imitation of any real artwork."""
    canvas = Rectangle(width=w, height=h, fill_color="#EFE3CC", fill_opacity=1, stroke_width=0)
    sun = Circle(radius=h * 0.17, fill_color=PALETTE["accent"], fill_opacity=0.9, stroke_width=0)
    sun.move_to(canvas.get_center() + np.array([-w * 0.22, h * 0.2, 0]))
    hill1 = Polygon([-w / 2, -h / 2, 0], [-w / 2, -h * 0.12, 0], [-w * 0.05, h * 0.02, 0], [w / 2, -h * 0.22, 0],
                    [w / 2, -h / 2, 0], fill_color=PALETTE["good"], fill_opacity=0.85, stroke_width=0)
    hill2 = Polygon([-w / 2, -h / 2, 0], [-w / 2, -h * 0.34, 0], [-w * 0.3, -h * 0.2, 0], [w * 0.25, -h * 0.42, 0],
                    [w * 0.25, -h / 2, 0], fill_color=PALETTE["wood"], fill_opacity=0.9, stroke_width=0)
    for m in (hill1, hill2):
        m.shift(canvas.get_center())
    art = VGroup(canvas, sun, hill1, hill2)
    if not frame:
        return art
    fr = Rectangle(width=w + 0.25, height=h + 0.25, fill_color=PALETTE["wood"], fill_opacity=1,
                   stroke_color=PALETTE["ink"], stroke_width=2.5)
    return VGroup(fr, art)


def silhouette(s=1.0, color=None):
    """A faceless, generic silhouette. It depicts no real person."""
    c = color or PALETTE["ink"]
    head = Circle(radius=0.42 * s, fill_color=c, fill_opacity=1, stroke_width=0)
    torso = RoundedRectangle(corner_radius=0.45 * s, width=1.5 * s, height=1.1 * s, fill_color=c, fill_opacity=1,
                             stroke_width=0)
    return VGroup(head, torso).arrange(DOWN, buff=0.08)


def speech_bubble(label, w=2.6, h=0.5, fs=13, color=None):
    c = color or PALETTE["accent"]
    box = card_bg(w, h, stroke_color=c)
    tail = Polygon([-0.1, 0, 0], [0.1, 0, 0], [-0.2, -0.18, 0], fill_color=PALETTE["card"], fill_opacity=1,
                   stroke_color=c, stroke_width=1.5).next_to(box, DOWN, buff=-0.02).shift(LEFT * 0.5)
    t = fit(Text(label, color=PALETTE["ink"], font_size=fs), w - 0.2).move_to(box.get_center())
    return VGroup(tail, box, t)


# --- scenes -----------------------------------------------------------------

class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=34)
        summary = fit(lines("Today: how museums\nand artists use AI\nto bring people closer\nto real art.", 22,
                            PALETTE["ink"], buff=0.14), W)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        wait_until(self, 6.85)


class B01_FrontOfAPainting(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        note = chip("illustration -- not a real case", w=3.4, h=0.4, border=PALETTE["ink"], color=PALETTE["ink"], fs=13)
        note.move_to([0, 3.25, 0])
        pic = painting(2.3, 1.55).move_to([0, 1.45, 0])
        postcard = VGroup(Rectangle(width=0.7, height=0.5, fill_color=PALETTE["card"], fill_opacity=1,
                                    stroke_color=PALETTE["dim"], stroke_width=2),
                          painting(0.55, 0.34, frame=False))
        postcard[1].move_to(postcard[0].get_center())
        pc = VGroup(postcard, Text("only seen on postcards", color=PALETTE["dim"], font_size=13)).arrange(RIGHT,
                                                                                                         buff=0.15)
        pc.move_to([0, 2.8, 0])
        same = chip("the painting hasn't changed", w=3.2, h=0.4, border=PALETTE["good"], color=PALETTE["good"], fs=13)
        same.move_to([0, 0.3, 0])

        screen = card_bg(2.1, 1.25, stroke_color=PALETTE["ink"]).move_to([0.75, -0.75, 0])
        strokes = VGroup(*[Arc(radius=0.4 + 0.1 * (i % 3), start_angle=0.3 * i, angle=PI * 0.55,
                               color=[PALETTE["accent"], PALETTE["good"], PALETTE["wood"], PALETTE["ink"]][i % 4],
                               stroke_width=4 + (i % 3)) for i in range(7)])
        strokes.arrange_in_grid(rows=2, cols=4, buff=0.1)
        fit_in(strokes, 1.7, 0.9).move_to(screen.get_center())
        guide = speech_bubble("Ask me anything about it.", w=2.4, h=0.42, fs=12).move_to([0.75, -1.8, 0])
        visitor = person(0.95, PALETTE["ink"]).move_to([-1.3, -0.95, 0])

        q1 = chip("not: does AI belong in museums?", w=3.6, h=0.4, border=PALETTE["dim"], color=PALETTE["dim"], fs=13)
        q1.move_to([0, -2.4, 0])
        q2 = chip("but: what do we ask it to do?", w=3.6, h=0.4, border=PALETTE["accent"], color=PALETTE["accent"],
                  fs=13).move_to([0, -2.85, 0])
        fin = fit(Text("help people notice the real thing", color=PALETTE["ink"], font_size=17, weight="BOLD"), W)
        fin.move_to([0, -3.25, 0])

        self.play(FadeIn(note), run_time=0.5)
        self.play(FadeIn(pic, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(pc), run_time=0.5)
        wait_until(self, 3.7)
        self.play(FadeIn(screen), FadeIn(strokes), run_time=0.7)
        wait_until(self, 6.4)
        self.play(FadeIn(guide, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 8.8)
        self.play(FadeIn(same, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 10.8)
        self.play(FadeIn(visitor), run_time=0.6)
        wait_until(self, 15.6)
        self.play(FadeIn(q1, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 18.8)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 20.5)
        self.play(FadeIn(fin, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 24.06)


class B03_NightWatchEdges(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top = chip("Rembrandt's The Night Watch", w=3.6, h=0.4, border=PALETTE["ink"], color=PALETTE["ink"], fs=13)
        top.move_to([0, 3.25, 0])
        gen = Text("(generic frame -- not the real painting)", color=PALETTE["dim"], font_size=10)
        gen.move_to([0, 2.9, 0])

        cx, cy = 0.0, 1.5
        pic = painting(1.9, 1.3).move_to([cx, cy, 0])
        pw, ph, e = 2.1, 1.5, 0.33

        def strip(w, h, x, y):
            fill = Rectangle(width=w, height=h, fill_color=PALETTE["accent"], fill_opacity=0.28, stroke_width=0)
            out = DashedVMobject(Rectangle(width=w, height=h, color=PALETTE["accent"], stroke_width=3), num_dashes=18)
            return VGroup(fill, out).move_to([x, y, 0])
        strips = VGroup(strip(pw + 2 * e, e, cx, cy + ph / 2 + e / 2), strip(pw + 2 * e, e, cx, cy - ph / 2 - e / 2),
                        strip(e, ph, cx - pw / 2 - e / 2, cy), strip(e, ph, cx + pw / 2 + e / 2, cy))

        months = chip("3 months", w=1.5, h=0.4, border=PALETTE["accent"], color=PALETTE["accent"], fs=16)
        months.move_to([0, 0.32, 0])
        y1715 = chip("1715: cut down on all four sides;\nthe strips were never found", w=3.6, h=0.55,
                     border=PALETTE["miss"], color=PALETTE["miss"], fs=12).move_to([0, -0.45, 0])

        def side(txt, y, col=PALETTE["accent"]):
            return chip(txt, w=3.6, h=0.42, border=col, color=PALETTE["ink"], fs=12).move_to([0, y, 0])
        c2 = side("a smaller 17th-century copy as the guide", -1.0)
        c3 = side("three neural networks, Rembrandt's style", -1.5)
        c4 = side("printed on canvas, mounted around it", -2.0)
        c5 = side("the original was not repainted", -2.5, PALETTE["good"])
        wire = src_chip("wire report (Kemp, 2021); restoration project launched 2019", 3.6).move_to([0, -3.05, 0])
        ring = SurroundingRectangle(pic, color=PALETTE["good"], buff=0.06, stroke_width=3)
        for g in (strips, y1715, months, c2, c3, c4, c5, wire, gen):
            g.set_opacity(0)

        wait_until(self, 1.3)
        self.play(FadeIn(top, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 3.3)
        self.play(FadeIn(pic, shift=UP * 0.1), gen.animate.set_opacity(1), run_time=0.6)
        self.play(y1715.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 5.6)
        self.play(*[s[1].animate.set_opacity(1) for s in strips], run_time=0.5)
        wait_until(self, 12.2)
        self.play(*[s[0].animate.set_opacity(0.28) for s in strips], run_time=0.5)
        wait_until(self, 12.8)
        self.play(c2.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 15.9)
        self.play(c3.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 19.3)
        self.play(c4.animate.set_opacity(1), *[s[0].animate.set_fill(PALETTE["wood"], 0.85) for s in strips],
                  run_time=0.6)
        wait_until(self, 25.8)
        self.play(months.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 28.3)
        self.play(c5.animate.set_opacity(1), Create(ring), run_time=0.6)
        wait_until(self, 30.6)
        self.play(wire.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 32.37)


class B04_DaliMuseum(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top = chip("Dalí Museum, Florida", w=3.2, h=0.4, border=PALETTE["ink"], color=PALETTE["ink"], fs=13)
        top.move_to([0, 3.25, 0])
        screen = card_bg(2.0, 1.9, stroke_color=PALETTE["ink"]).move_to([-0.85, 2.0, 0])
        fig = silhouette(0.6, PALETTE["ink"]).move_to(screen.get_center() + DOWN * 0.15)
        ai_tag = chip("AI version", w=1.2, h=0.3, border=PALETTE["accent"], color=PALETTE["accent"], fs=11)
        ai_tag.move_to(screen.get_top() + DOWN * 0.25)
        bubble = speech_bubble("Welcome. Come in.", w=1.5, h=0.42, fs=11).move_to([1.2, 2.4, 0])
        generic = Text("(a faceless generic silhouette)", color=PALETTE["dim"], font_size=10).move_to([-0.85, 0.9, 0])

        scr = Text("the script is built from his own:", color=PALETTE["dim"], font_size=12).move_to([0, 0.55, 0])
        s1 = chip("writings", w=1.8, h=0.4, border=PALETTE["good"], fs=13)
        s2 = chip("quotes", w=1.8, h=0.4, border=PALETTE["good"], fs=13)
        s3 = chip("interviews", w=1.8, h=0.4, border=PALETTE["good"], fs=13)
        s4 = chip("archival footage", w=1.8, h=0.4, border=PALETTE["good"], fs=13)
        grid = VGroup(VGroup(s1, s2).arrange(RIGHT, buff=0.1), VGroup(s3, s4).arrange(RIGHT, buff=0.1)).arrange(
            DOWN, buff=0.1).move_to([0, -0.05, 0])
        actor = chip("performed by an actor", w=3.7, h=0.42, border=PALETTE["accent"], color=PALETTE["accent"], fs=13)
        actor.move_to([0, -0.8, 0])
        selfie = chip("at the end, he offers a selfie", w=3.7, h=0.42, fs=13).move_to([0, -1.3, 0])
        rev = chip("a reviewer: complementary to a\nstrong permanent collection", w=3.7, h=0.62, border=PALETTE["good"],
                   color=PALETTE["good"], fs=12).move_to([0, -2.0, 0])
        con = chip("seen as controversial by some", w=2.2, h=0.4, border=PALETTE["miss"], color=PALETTE["miss"], fs=11)
        yr = chip("review from 2019", w=1.4, h=0.4, border=PALETTE["miss"], color=PALETTE["miss"], fs=11)
        tags = VGroup(con, yr).arrange(RIGHT, buff=0.1).move_to([0, -2.7, 0])
        src = src_chip("Sarmiento, 2019 (Palm Beach ArtsPaper)", 3.7).move_to([0, -3.2, 0])
        for g in (scr, s1, s2, s3, s4, actor, selfie, rev, con, yr, src, generic):
            g.set_opacity(0)

        wait_until(self, 1.2)
        self.play(FadeIn(top, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 3.2)
        self.play(FadeIn(screen), FadeIn(fig), FadeIn(ai_tag), run_time=0.6)
        self.play(FadeIn(bubble, shift=UP * 0.1), generic.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 8.0)
        self.play(scr.animate.set_opacity(1), s1.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 10.2)
        self.play(s2.animate.set_opacity(1), run_time=0.3)
        wait_until(self, 10.9)
        self.play(s3.animate.set_opacity(1), run_time=0.3)
        wait_until(self, 12.7)
        self.play(s4.animate.set_opacity(1), run_time=0.3)
        wait_until(self, 14.5)
        self.play(actor.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 15.4)
        self.play(selfie.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 17.3)
        self.play(rev.animate.set_opacity(1), src.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 21.2)
        self.play(con.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 24.9)
        self.play(yr.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 27.15)


class B05_MomaWall(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top = chip("MoMA: Refik Anadol's Unsupervised", w=3.7, h=0.4, border=PALETTE["ink"], color=PALETTE["ink"], fs=13)
        top.move_to([0, 3.25, 0])
        S = 2.3
        wall = Rectangle(width=S, height=S, fill_color="#F1E7D6", fill_opacity=1, stroke_color=PALETTE["ink"],
                         stroke_width=3).move_to([0, 1.75, 0])
        rng = np.random.default_rng(7)
        cols = [PALETTE["accent"], PALETTE["good"], PALETTE["wood"], "#7A9CC6", "#C98FB0", "#E3B04B"]
        blobs = VGroup()
        for i in range(18):
            r = rng.uniform(0.15, 0.42)
            x = rng.uniform(-S / 2 + r, S / 2 - r)
            y = rng.uniform(-S / 2 + r, S / 2 - r)
            blobs.add(Circle(radius=r, fill_color=cols[i % len(cols)], fill_opacity=0.5, stroke_width=0).move_to(
                wall.get_center() + np.array([x, y, 0])))
        flows = VGroup()
        for k in range(4):
            ys = -0.8 + 0.55 * k
            pts = [wall.get_center() + np.array([-S / 2 + 0.12 + t * (S - 0.24) / 12,
                                                 ys + 0.17 * np.sin(t * 0.9 + k), 0]) for t in range(13)]
            flows.add(VMobject(color=PALETTE["card"], stroke_width=3, stroke_opacity=0.8).set_points_smoothly(pts))
        gen = Text("(generated abstract colour -- not the real work)", color=PALETTE["dim"], font_size=10)
        gen.move_to([0, 0.45, 0])

        def stat(big, sub, y):
            b = card_bg(3.7, 0.72, stroke_color=PALETTE["accent"])
            t = VGroup(Text(big, color=PALETTE["accent"], font_size=24, weight="BOLD"),
                       Text(sub, color=PALETTE["ink"], font_size=11)).arrange(RIGHT, buff=0.2)
            fit(t, 3.4)
            return VGroup(b, t.move_to(b.get_center())).move_to([0, y, 0])
        st1 = stat("24 x 24 ft", "lobby wall", -0.15)
        st2 = stat("320,000", "visual inputs from the collection", -0.95)
        st3 = stat("team of 15", "shaped the results", -1.75)
        sens_l = Text("sensors picked up:", color=PALETTE["dim"], font_size=11).move_to([0, -2.35, 0])
        sens = VGroup(chip("light", w=0.9, h=0.38, fs=11), chip("visitors' movement", w=1.7, h=0.38, fs=11),
                      chip("weather", w=1.0, h=0.38, fs=11)).arrange(RIGHT, buff=0.1).move_to([0, -2.75, 0])
        collab = chip("a collaboration between\npeople and machines", w=3.7, h=0.55, border=PALETTE["good"],
                      color=PALETTE["good"], fs=12).move_to([0, -2.55, 0])
        first = chip("the first generative AI artwork\nMoMA acquired", w=3.7, h=0.55, border=PALETTE["accent"],
                     color=PALETTE["accent"], fs=12).move_to([0, -3.15, 0])
        raw = lines("the real artworks were\nthe raw material", 22, PALETTE["ink"], buff=0.1, weight="BOLD",
                    max_w=W).move_to([0, -2.72, 0])
        src = src_chip("Chan, 2023; Alemdar, n.d. (TRT World, no visible date)", 3.7).move_to([0, -3.3, 0])
        for g in (st1, st2, st3, sens, sens_l, collab, first, raw, src, gen):
            g.set_opacity(0)

        wait_until(self, 0.9)
        self.play(FadeIn(top, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 2.6)
        self.play(FadeIn(VGroup(wall, blobs, flows)), gen.animate.set_opacity(1), run_time=0.8)
        wait_until(self, 5.0)
        self.play(st1.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 9.6)
        self.play(st2.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 14.1)
        self.play(sens_l.animate.set_opacity(1), sens[0].animate.set_opacity(1), run_time=0.4)
        wait_until(self, 15.7)
        self.play(sens[1].animate.set_opacity(1), run_time=0.3)
        wait_until(self, 17.0)
        self.play(sens[2].animate.set_opacity(1), run_time=0.3)
        wait_until(self, 18.4)
        self.play(st3.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 20.6)
        self.play(sens_l.animate.set_opacity(0), sens.animate.set_opacity(0), run_time=0.3)
        self.play(collab.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 24.5)
        self.play(first.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 28.9)
        self.play(collab.animate.set_opacity(0), first.animate.set_opacity(0), run_time=0.3)
        self.play(raw.animate.set_opacity(1), src.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 31.13)


class B08_SendThemBack(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        real = Text("the real thing", color=PALETTE["good"], font_size=15, weight="BOLD").move_to([0, 3.2, 0])
        pic = painting(2.2, 1.5).move_to([0, 2.1, 0])
        visitor = person(0.9, PALETTE["ink"]).move_to([0, 0.55, 0])
        sight = DashedLine(visitor.get_top() + UP * 0.04, pic.get_bottom() + DOWN * 0.04, color=PALETTE["accent"],
                           stroke_width=3)

        c1 = chip("its missing edges, re-seen", w=3.6, h=0.42, border=PALETTE["accent"], fs=13)
        c2 = chip("an artist, in his own words", w=3.6, h=0.42, border=PALETTE["accent"], fs=13)
        c3 = chip("a collection, as moving light", w=3.6, h=0.42, border=PALETTE["accent"], fs=13)
        caps = VGroup(c1, c2, c3).arrange(DOWN, buff=0.12).move_to([0, -0.75, 0])
        tools = chip("always meeting new tools:\nthe camera, the projector", w=3.6, h=0.55, border=PALETTE["dim"],
                     color=PALETTE["dim"], fs=12).move_to([0, -1.78, 0])
        rep = chip("replace the original", w=1.75, h=0.5, border=PALETTE["miss"], color=PALETTE["miss"], fs=12)
        back = chip("send people back to it", w=1.85, h=0.5, border=PALETTE["good"], color=PALETTE["good"], fs=12)
        choice = VGroup(rep, back).arrange(RIGHT, buff=0.1).move_to([0, -2.55, 0])
        ring = SurroundingRectangle(back, color=PALETTE["good"], buff=0.05, stroke_width=3, corner_radius=0.1)
        fin = lines("That choice keeps\nthe work authentic.", 24, PALETTE["accent"], buff=0.12, weight="BOLD",
                    max_w=W).move_to([0, -0.9, 0])
        for g in (c1, c2, c3, tools, rep, back, fin):
            g.set_opacity(0)

        self.play(FadeIn(pic, shift=UP * 0.1), FadeIn(visitor), FadeIn(real), Create(sight), run_time=0.7)
        self.play(c1.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 2.7)
        self.play(c2.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 5.1)
        self.play(c3.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 8.0)
        self.play(tools.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 12.1)
        self.play(rep.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 15.8)
        self.play(back.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 17.8)
        self.play(Create(ring), run_time=0.5)
        wait_until(self, 20.0)
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(tools), run_time=0.3)
        self.play(fin.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 23.37)


class B09_SourcesCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("A note on sources", color=PALETTE["ink"], font_size=22, weight="BOLD").move_to([0, 3.15, 0])
        refs = ["Kemp (2021), The Jakarta Post", "Sarmiento (2019), Palm Beach ArtsPaper", "Chan (2023), Wallpaper*",
                "Alemdar (n.d.), TRT World", "Donoghue (2025), Whitewall", "Levine (2026), The Boston Globe",
                "Kenny (2026), HBR Cold Call", "Ludwig Museum Koblenz (2026)"]
        rt = Text("References", color=PALETTE["accent"], font_size=14, weight="BOLD")
        rl = VGroup(*[Text(r, color=PALETTE["ink"], font_size=12) for r in refs]).arrange(DOWN, buff=0.1,
                                                                                         aligned_edge=LEFT)
        r_in = VGroup(rt, rl).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        r_box = card_bg(W, 2.5)
        left = VGroup(r_box, fit_in(r_in, W - 0.3, 2.3).move_to(r_box.get_center())).move_to([0, 1.55, 0])

        n1 = chip("The Rijksmuseum story comes from\na wire report (AFP, via The Jakarta Post)", w=W, h=0.7,
                  border=PALETTE["miss"], color=PALETTE["miss"], fs=11).move_to([0, -0.3, 0])
        n2 = chip("The Dalí Museum story is a 2019 review", w=W, h=0.5, border=PALETTE["miss"],
                  color=PALETTE["miss"], fs=11).move_to([0, -1.05, 0])
        n3 = chip("The TRT World article shows no visible date", w=W, h=0.5, border=PALETTE["dim"],
                  color=PALETTE["dim"], fs=11).move_to([0, -1.65, 0])
        n4 = chip("The opening scene and the ideas\nanyone could borrow are illustrations\nand suggestions, not reported cases",
                  w=W, h=0.95, border=PALETTE["accent"], color=PALETTE["accent"], fs=11).move_to([0, -2.55, 0])
        for g in (n1, n2, n3, n4):
            g.set_opacity(0)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 1.2)
        reveal_box, reveal_in = left[0], left[1]
        w = reveal_box.width
        reveal_box.stretch(0.01, 0)
        self.play(reveal_box.animate.stretch_to_fit_width(w), run_time=0.4)
        self.play(FadeIn(reveal_in), run_time=0.4)
        wait_until(self, 1.8)
        self.play(n1.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 5.2)
        self.play(n2.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 8.3)
        self.play(n3.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 11.2)
        self.play(n4.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 18.02)
