"""
Manim scenes for real-art-new-light

A warm, fair explainer on how museums and artists use AI to bring people closer to
real artworks, sourced from the user-supplied article "Real Art, New Light." No
footage exists and, per the user's materials note, NO real artwork is recreated or
imitated, NO likeness of Salvador Dali or any real person is shown and NO museum or
company logo is used: the paintings are generic abstract shapes, the Dali figure is a
faceless generic silhouette, visitors are plain figures, and source names appear only
as plain text. The Rijksmuseum story is labeled a wire report, the Dali review 2019,
and the opening scene and the borrowable ideas are labeled illustrations and
suggestions. Built in the house Claude palette. Reveals are timed to the narration
(pause points measured from each beat's mp3).

B00B_AgrimaIntro     -- presenter card: "Hi, I'm Agrima." + lead-in
B01_FrontOfAPainting -- illustration: a generic painting, a screen with brushwork, a guide
B02_ThreeHabits      -- the three habits as a numbered checklist
B03_NightWatchEdges  -- generic frame + four dashed extension strips, "3 months"
B04_DaliMuseum       -- faceless silhouette on a screen, speech bubble, sources of the script
B05_MomaWall         -- square wall of flowing colour + 24 x 24 ft / 320,000 / team of 15
B06_HarvardKoblenz   -- two one-sentence panels: Harvard inbox, Koblenz walkable room
B07_IdeasToBorrow    -- six ideas, labeled "my ideas, not rules"
B08_SendThemBack     -- a visitor at a real frame; replace the original vs send people back
B09_SourcesCard      -- references + the wire report / 2019 / illustration notes
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


def chip(label, w=2.6, h=0.55, border=None, color=None, fs=16):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(lines(label, fs, color or PALETTE["ink"], buff=0.06), w - 0.3)
    return VGroup(box, txt.move_to(box.get_center()))


def src_chip(label, w=3.4, border=None, color=None):
    return chip(label, w=w, h=0.4, border=border or PALETTE["dim"], color=color or PALETTE["dim"], fs=13)


def tick(color=None, s=1.0, sw=4):
    t = VMobject(color=color or PALETTE["good"], stroke_width=sw)
    t.set_points_as_corners([[-0.1, 0.0, 0], [-0.02, -0.1, 0], [0.13, 0.12, 0]])
    return t.scale(s)


def cross(color=None, s=1.0, sw=3.5):
    c = color or PALETTE["miss"]
    return VGroup(Line([-0.09, -0.09, 0], [0.09, 0.09, 0], color=c, stroke_width=sw),
                  Line([-0.09, 0.09, 0], [0.09, -0.09, 0], color=c, stroke_width=sw)).scale(s)


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
    fr = Rectangle(width=w + 0.3, height=h + 0.3, fill_color=PALETTE["wood"], fill_opacity=1,
                   stroke_color=PALETTE["ink"], stroke_width=2.5)
    return VGroup(fr, art)


def silhouette(s=1.0, color=None):
    """A faceless, generic silhouette. It depicts no real person."""
    c = color or PALETTE["ink"]
    head = Circle(radius=0.42 * s, fill_color=c, fill_opacity=1, stroke_width=0)
    torso = RoundedRectangle(corner_radius=0.45 * s, width=1.5 * s, height=1.1 * s, fill_color=c, fill_opacity=1,
                             stroke_width=0)
    return VGroup(head, torso).arrange(DOWN, buff=0.08)


def speech_bubble(label, w=2.6, h=0.7, fs=16, color=None):
    c = color or PALETTE["accent"]
    box = card_bg(w, h, stroke_color=c)
    tail = Polygon([-0.12, 0, 0], [0.12, 0, 0], [-0.25, -0.22, 0], fill_color=PALETTE["card"], fill_opacity=1,
                   stroke_color=c, stroke_width=1.5).next_to(box, DOWN, buff=-0.02).shift(LEFT * 0.6)
    t = fit(Text(label, color=PALETTE["ink"], font_size=fs), w - 0.3).move_to(box.get_center())
    return VGroup(tail, box, t)


# --- scenes -----------------------------------------------------------------

class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=40)
        summary = fit(Text(
            "Today: how museums and artists use AI\nto bring people closer to real art.",
            color=PALETTE["ink"], font_size=26, line_spacing=1.3, should_center=True), 8.6)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        wait_until(self, 6.85)


class B01_FrontOfAPainting(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        note = chip("illustration -- not a real case", w=4.4, h=0.45, border=PALETTE["ink"], color=PALETTE["ink"], fs=14)
        note.move_to([0, 3.05, 0])

        wall = Rectangle(width=12.4, height=0.2, fill_color=PALETTE["border"], fill_opacity=1, stroke_width=0)
        wall.move_to([0, -1.75, 0])
        pic = painting(3.2, 2.2).move_to([-3.6, 0.4, 0])
        postcard = VGroup(Rectangle(width=0.9, height=0.62, fill_color=PALETTE["card"], fill_opacity=1,
                                    stroke_color=PALETTE["dim"], stroke_width=2),
                          painting(0.7, 0.42, frame=False))
        postcard[1].move_to(postcard[0].get_center())
        pc_l = Text("only seen on postcards", color=PALETTE["dim"], font_size=16)
        pc = VGroup(postcard, pc_l).arrange(RIGHT, buff=0.2).move_to([-3.6, 2.3, 0])

        screen = card_bg(3.0, 2.0, stroke_color=PALETTE["ink"]).move_to([2.2, 0.75, 0])
        strokes = VGroup(*[Arc(radius=0.5 + 0.12 * (i % 3), start_angle=0.3 * i, angle=PI * 0.55,
                               color=[PALETTE["accent"], PALETTE["good"], PALETTE["wood"], PALETTE["ink"]][i % 4],
                               stroke_width=5 + (i % 3)) for i in range(7)])
        strokes.arrange_in_grid(rows=2, cols=4, buff=0.12)
        fit_in(strokes, 2.5, 1.5).move_to(screen.get_center())
        s_cap = Text("brushwork, up close", color=PALETTE["dim"], font_size=15).next_to(screen, UP, buff=0.12)
        guide = speech_bubble("Ask me anything about it.", w=3.0, h=0.62, fs=16).move_to([2.2, -0.75, 0])

        visitor = person(1.2, PALETTE["ink"]).move_to([-0.2, -0.95, 0])
        sight_p = DashedLine(visitor.get_top() + UP * 0.05 + LEFT * 0.1, pic.get_right() + RIGHT * 0.05 + DOWN * 0.3,
                             color=PALETTE["accent"], stroke_width=3)
        sight_s = DashedLine(visitor.get_top() + UP * 0.05 + RIGHT * 0.1, screen.get_left() + LEFT * 0.05,
                             color=PALETTE["accent"], stroke_width=3)

        same = chip("the painting hasn't changed", w=3.8, h=0.5, border=PALETTE["good"], color=PALETTE["good"], fs=16)
        same.move_to([-3.6, -2.0, 0])
        q1 = chip("not: does AI belong in museums?", w=5.2, h=0.5, border=PALETTE["dim"], color=PALETTE["dim"], fs=17)
        q1.move_to([0, -2.2, 0])
        q2 = chip("but: what do we ask it to do?", w=5.2, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"],
                  fs=17)
        q2.move_to([0, -2.7, 0])
        fin = Text("help people notice the real thing", color=PALETTE["ink"], font_size=22, weight="BOLD")
        fin.move_to([0, -3.15, 0])
        same.move_to([-3.6, -1.35, 0])

        self.play(FadeIn(note), run_time=0.5)
        self.play(FadeIn(wall), FadeIn(pic, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(pc), run_time=0.5)
        wait_until(self, 3.7)
        self.play(FadeIn(screen), FadeIn(strokes), FadeIn(s_cap), run_time=0.7)
        wait_until(self, 6.4)
        self.play(FadeIn(guide, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 8.8)
        self.play(FadeIn(same, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 10.8)
        self.play(FadeIn(visitor), Create(sight_p), Create(sight_s), run_time=0.8)
        wait_until(self, 15.6)
        self.play(FadeIn(q1, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 18.8)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 20.5)
        self.play(FadeIn(fin, shift=UP * 0.1), run_time=0.5)
        wait_until(self, 24.06)


class B02_ThreeHabits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Three habits keep the art authentic", color=PALETTE["ink"], font_size=36, weight="BOLD")
        title.move_to([0, 3.0, 0])

        def num(n, x, y):
            c = VGroup(Circle(radius=0.32, color=PALETTE["accent"], fill_color=PALETTE["accent"], fill_opacity=1,
                              stroke_width=0), Text(str(n), color=PALETTE["card"], font_size=30, weight="BOLD"))
            c[1].move_to(c[0].get_center())
            return c.move_to([x, y, 0])

        def row(n, txt, h, y, ty):
            box = card_bg(11.4, h).move_to([0, y, 0])
            nm = num(n, -5.0, ty)
            t = fit(Text(txt, color=PALETTE["ink"], font_size=30), 9.4)
            t.move_to([-4.4 + t.width / 2, ty, 0])
            return VGroup(box, VGroup(nm, t))

        r1 = row(1, "The original stays untouched, and stays the star.", 1.2, 1.5, 1.5)
        r2 = row(2, "The AI is built from the art's own materials.", 1.9, -0.1, 0.25)
        r3 = row(3, "Visitors are told what is AI, and what is real.", 1.2, -1.8, -1.8)
        fit(r3[1][1], 7.4)
        r3[1][1].move_to([-4.4 + r3[1][1].width / 2, -1.8, 0])
        m1 = chip("the artist's words", w=2.7, h=0.5, border=PALETTE["good"], color=PALETTE["good"], fs=17)
        m2 = chip("scans of the work", w=2.7, h=0.5, border=PALETTE["good"], color=PALETTE["good"], fs=17)
        m3 = chip("the museum's collection", w=3.1, h=0.5, border=PALETTE["good"], color=PALETTE["good"], fs=17)
        mats = VGroup(m1, m2, m3).arrange(RIGHT, buff=0.25).move_to([-0.2, -0.65, 0])
        t1 = tick(PALETTE["good"], 1.5).move_to([5.0, 1.5, 0])
        t2 = tick(PALETTE["good"], 1.5).move_to([5.0, 0.25, 0])
        tags = VGroup(chip("AI", w=0.9, h=0.45, border=PALETTE["accent"], color=PALETTE["accent"], fs=17),
                      chip("real", w=0.9, h=0.45, border=PALETTE["good"], color=PALETTE["good"], fs=17)
                      ).arrange(RIGHT, buff=0.2).move_to([4.6, -1.8, 0])

        wait_until(self, 0.1)
        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 2.4)
        self.play(FadeIn(r1, shift=UP * 0.1), run_time=0.45)
        self.play(FadeIn(t1), run_time=0.2)
        wait_until(self, 6.5)
        self.play(FadeIn(r2, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 10.4)
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.1) for m in mats], lag_ratio=0.5), run_time=1.6)
        self.play(FadeIn(t2), run_time=0.2)
        wait_until(self, 13.9)
        self.play(FadeIn(r3, shift=UP * 0.1), run_time=0.45)
        wait_until(self, 15.8)
        self.play(FadeIn(tags, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 17.4)


class B03_NightWatchEdges(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top = chip("Rembrandt's The Night Watch", w=4.6, h=0.5, border=PALETTE["ink"], color=PALETTE["ink"], fs=17)
        top.move_to([-3.3, 3.05, 0])
        gen = Text("(generic frame -- not the real painting)", color=PALETTE["dim"], font_size=14)
        gen.move_to([-3.3, 2.6, 0])

        cx, cy = -3.3, 0.05
        pic = painting(3.0, 2.1).move_to([cx, cy, 0])
        pw, ph, e = 3.3, 2.4, 0.5

        def strip(w, h, x, y):
            fill = Rectangle(width=w, height=h, fill_color=PALETTE["accent"], fill_opacity=0.28, stroke_width=0)
            out = DashedVMobject(Rectangle(width=w, height=h, color=PALETTE["accent"], stroke_width=3), num_dashes=22)
            return VGroup(fill, out).move_to([x, y, 0])
        strips = VGroup(strip(pw + 2 * e, e, cx, cy + ph / 2 + e / 2), strip(pw + 2 * e, e, cx, cy - ph / 2 - e / 2),
                        strip(e, ph, cx - pw / 2 - e / 2, cy), strip(e, ph, cx + pw / 2 + e / 2, cy))

        y1715 = chip("1715: cut down on all four sides", w=4.6, h=0.5, border=PALETTE["miss"], color=PALETTE["miss"],
                     fs=16).move_to([-3.3, -2.1, 0])
        lost = chip("the strips were never found", w=4.6, h=0.5, border=PALETTE["dim"], color=PALETTE["dim"],
                    fs=16).move_to([-3.3, -2.65, 0])
        months = chip("3 months", w=2.0, h=0.55, border=PALETTE["accent"], color=PALETTE["accent"], fs=22)
        months.move_to([-3.3, -3.2, 0])

        def side(txt, y, col):
            return chip(txt, w=5.6, h=0.7, border=col, color=PALETTE["ink"], fs=17).move_to([3.4, y, 0])
        c1 = side("AI imagined the missing edges", 2.2, PALETTE["accent"])
        c2 = side("a smaller 17th-century copy as the guide", 1.25, PALETTE["accent"])
        c3 = side("three neural networks, matched to Rembrandt's style", 0.3, PALETTE["accent"])
        c4 = side("printed on canvas, mounted on frames around the painting", -0.65, PALETTE["accent"])
        c5 = side("the original was not repainted", -1.6, PALETTE["good"])
        wire = src_chip("wire report (Kemp, 2021) -- restoration project launched 2019", 5.6).move_to([3.4, -2.55, 0])
        ring = SurroundingRectangle(pic, color=PALETTE["good"], buff=0.08, stroke_width=4)
        ok = tick(PALETTE["good"], 1.3).next_to(c5, LEFT, buff=0.1)
        for g in (strips, y1715, lost, months, c1, c2, c3, c4, c5, wire, gen):
            g.set_opacity(0)

        wait_until(self, 1.3)
        self.play(FadeIn(top, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 3.3)
        self.play(FadeIn(pic, shift=UP * 0.1), gen.animate.set_opacity(1), run_time=0.6)
        self.play(y1715.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 5.6)
        self.play(strips.animate.set_opacity(0.0), run_time=0.01)
        self.play(*[s[1].animate.set_opacity(1) for s in strips], run_time=0.5)
        wait_until(self, 10.4)
        self.play(lost.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 12.2)
        self.play(*[s[0].animate.set_opacity(0.28) for s in strips], c1.animate.set_opacity(1), run_time=0.5)
        self.play(c2.animate.set_opacity(1), run_time=0.01)
        wait_until(self, 12.8)
        wait_until(self, 15.9)
        self.play(c3.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 19.3)
        self.play(c4.animate.set_opacity(1), *[s[0].animate.set_fill(PALETTE["wood"], 0.85) for s in strips],
                  run_time=0.6)
        wait_until(self, 25.8)
        self.play(months.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 28.3)
        self.play(c5.animate.set_opacity(1), Create(ring), FadeIn(ok), run_time=0.6)
        wait_until(self, 30.6)
        self.play(wire.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 32.37)


class B04_DaliMuseum(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top = chip("Dalí Museum, Florida", w=3.8, h=0.5, border=PALETTE["ink"], color=PALETTE["ink"], fs=17)
        top.move_to([-3.9, 3.05, 0])

        screen = card_bg(3.8, 3.5, stroke_color=PALETTE["ink"]).move_to([-3.9, 0.25, 0])
        fig = silhouette(1.15, PALETTE["ink"]).move_to(screen.get_center() + DOWN * 0.25)
        ai_tag = chip("AI version", w=1.7, h=0.4, border=PALETTE["accent"], color=PALETTE["accent"], fs=14)
        ai_tag.move_to(screen.get_top() + DOWN * 0.35)
        bubble = speech_bubble("Welcome. Come in.", w=3.0, h=0.7, fs=17).move_to([-3.9, -2.35, 0])
        generic = Text("(a faceless generic silhouette)", color=PALETTE["dim"], font_size=13).move_to([-3.9, -3.2, 0])

        scr = Text("the script is built from his own:", color=PALETTE["dim"], font_size=17).move_to([2.75, 2.45, 0])
        s1 = chip("writings", w=2.5, h=0.5, border=PALETTE["good"], color=PALETTE["ink"], fs=17)
        s2 = chip("quotes", w=2.5, h=0.5, border=PALETTE["good"], color=PALETTE["ink"], fs=17)
        s3 = chip("interviews", w=2.5, h=0.5, border=PALETTE["good"], color=PALETTE["ink"], fs=17)
        s4 = chip("archival footage", w=2.5, h=0.5, border=PALETTE["good"], color=PALETTE["ink"], fs=17)
        grid = VGroup(VGroup(s1, s2).arrange(RIGHT, buff=0.2), VGroup(s3, s4).arrange(RIGHT, buff=0.2)).arrange(
            DOWN, buff=0.2).move_to([2.75, 1.5, 0])
        actor = chip("performed by an actor", w=5.2, h=0.55, border=PALETTE["accent"], color=PALETTE["accent"], fs=18)
        actor.move_to([2.75, 0.35, 0])
        selfie = chip("at the end, he offers a selfie", w=5.2, h=0.55, border=PALETTE["border"], color=PALETTE["ink"],
                      fs=18).move_to([2.75, -0.4, 0])
        rev = chip("a reviewer: complementary to a strong permanent collection", w=5.2, h=0.8, border=PALETTE["good"],
                   color=PALETTE["good"], fs=17).move_to([2.75, -1.35, 0])
        con = chip("seen as controversial by some", w=2.9, h=0.5, border=PALETTE["miss"], color=PALETTE["miss"], fs=15)
        yr = chip("review from 2019", w=2.2, h=0.5, border=PALETTE["miss"], color=PALETTE["miss"], fs=15)
        tags = VGroup(con, yr).arrange(RIGHT, buff=0.15).move_to([2.75, -2.4, 0])
        src = src_chip("Sarmiento, 2019 (Palm Beach ArtsPaper)", 5.2).move_to([2.75, -3.1, 0])
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

        top = chip("MoMA: Refik Anadol's Unsupervised", w=5.4, h=0.5, border=PALETTE["ink"], color=PALETTE["ink"], fs=17)
        top.move_to([-3.3, 3.05, 0])

        S = 3.7
        wall = Rectangle(width=S, height=S, fill_color="#F1E7D6", fill_opacity=1, stroke_color=PALETTE["ink"],
                         stroke_width=3).move_to([-3.3, 0.55, 0])
        rng = np.random.default_rng(7)
        cols = [PALETTE["accent"], PALETTE["good"], PALETTE["wood"], "#7A9CC6", "#C98FB0", "#E3B04B"]
        blobs = VGroup()
        for i in range(22):
            r = rng.uniform(0.25, 0.7)
            x = rng.uniform(-S / 2 + r, S / 2 - r)
            y = rng.uniform(-S / 2 + r, S / 2 - r)
            blobs.add(Circle(radius=r, fill_color=cols[i % len(cols)], fill_opacity=0.5, stroke_width=0).move_to(
                wall.get_center() + np.array([x, y, 0])))
        flows = VGroup()
        for k in range(4):
            ys = -1.3 + 0.9 * k
            pts = [wall.get_center() + np.array([-S / 2 + 0.2 + t * (S - 0.4) / 12,
                                                 ys + 0.28 * np.sin(t * 0.9 + k), 0]) for t in range(13)]
            flows.add(VMobject(color=PALETTE["card"], stroke_width=4, stroke_opacity=0.8).set_points_smoothly(pts))
        gen = Text("(generated abstract colour -- not the real work)", color=PALETTE["dim"], font_size=13)
        gen.move_to([-3.3, -1.5, 0])

        def stat(big, sub, y):
            b = card_bg(5.0, 0.95, stroke_color=PALETTE["accent"])
            t = VGroup(Text(big, color=PALETTE["accent"], font_size=36, weight="BOLD"),
                       Text(sub, color=PALETTE["ink"], font_size=16)).arrange(RIGHT, buff=0.3)
            fit(t, 4.6)
            return VGroup(b, t.move_to(b.get_center())).move_to([3.1, y, 0])
        st1 = stat("24 x 24 ft", "lobby wall", 2.3)
        st2 = stat("320,000", "visual inputs from the collection", 1.2)
        st3 = stat("team of 15", "shaped the results", 0.1)
        sens = VGroup(chip("light", w=1.2, h=0.45, fs=15), chip("visitors' movement", w=2.3, h=0.45, fs=15),
                      chip("weather", w=1.4, h=0.45, fs=15)).arrange(RIGHT, buff=0.12).move_to([-3.3, -2.05, 0])
        sens_l = Text("sensors picked up:", color=PALETTE["dim"], font_size=14).next_to(sens, UP, buff=0.05).shift(DOWN * 0.0)
        sens_l.move_to([-3.3, -1.95, 0])
        sens.move_to([-3.3, -2.4, 0])
        collab = chip("a collaboration between people and machines", w=5.0, h=0.55, border=PALETTE["good"],
                      color=PALETTE["good"], fs=16).move_to([3.1, -1.05, 0])
        first = chip("the first generative AI artwork MoMA acquired", w=5.0, h=0.55, border=PALETTE["accent"],
                     color=PALETTE["accent"], fs=16).move_to([3.1, -1.8, 0])
        raw = Text("the real artworks were the raw material", color=PALETTE["ink"], font_size=22, weight="BOLD")
        fit(raw, 6.0).move_to([0, -3.2, 0])
        src = src_chip("Chan, 2023 (Wallpaper*); Alemdar, n.d. (TRT World, no visible date)", 6.4).move_to([3.1, -2.45, 0])
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
        self.play(collab.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 24.5)
        self.play(first.animate.set_opacity(1), src.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 29.0)
        self.play(raw.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 31.13)


class B06_HarvardKoblenz(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        two = Text("Two more, briefly", color=PALETTE["dim"], font_size=24).move_to([0, 3.0, 0])

        # Harvard: an inbox with a talking portrait silhouette
        hb = card_bg(5.9, 4.7)
        hh = Text("Harvard Art Museums", color=PALETTE["ink"], font_size=24, weight="BOLD")
        env = VGroup(Rectangle(width=1.8, height=1.2, fill_color=PALETTE["warm"], fill_opacity=1,
                               stroke_color=PALETTE["ink"], stroke_width=3),
                     Line([-0.9, 0.6, 0], [0, -0.05, 0], color=PALETTE["ink"], stroke_width=3),
                     Line([0.9, 0.6, 0], [0, -0.05, 0], color=PALETTE["ink"], stroke_width=3))
        port = VGroup(RoundedRectangle(corner_radius=0.05, width=0.95, height=1.15, fill_color=PALETTE["wood"],
                                       fill_opacity=1, stroke_color=PALETTE["ink"], stroke_width=2),
                      silhouette(0.5, PALETTE["ink"]))
        port[1].move_to(port[0].get_center())
        sp = speech_bubble("Hello.", w=1.1, h=0.45, fs=14)
        icon = VGroup(env, port.move_to(env.get_top() + UP * 0.75 + LEFT * 0.45), sp.move_to(env.get_top() + UP * 0.9 + RIGHT * 0.75))
        h1 = chip("sent to the mailing list", w=4.9, h=0.5, fs=16)
        h2 = chip("no original artwork touched", w=4.9, h=0.5, border=PALETTE["good"], color=PALETTE["good"], fs=16)
        h3 = chip("curators first, face to face", w=4.9, h=0.5, border=PALETTE["good"], color=PALETTE["good"], fs=16)
        h4 = chip("an invitation back to the painting", w=4.9, h=0.5, border=PALETTE["accent"],
                  color=PALETTE["accent"], fs=16)
        hchips = VGroup(h1, h2, h3, h4).arrange(DOWN, buff=0.12)
        h_in = VGroup(hh, icon, hchips).arrange(DOWN, buff=0.3)
        left = VGroup(hb, fit_in(h_in, 5.5, 4.4).move_to(hb.get_center())).move_to([-3.2, -0.1, 0])

        # Koblenz: a walkable digital twin with an AI guide
        kb = card_bg(5.9, 4.7)
        kh = Text("Ludwig Museum Koblenz", color=PALETTE["ink"], font_size=24, weight="BOLD")
        room = Rectangle(width=3.4, height=1.5, fill_color=PALETTE["warm"], fill_opacity=1, stroke_color=PALETTE["ink"],
                         stroke_width=3)
        door = Rectangle(width=0.5, height=0.8, fill_color=PALETTE["wood"], fill_opacity=1, stroke_width=0).move_to(
            room.get_bottom() + UP * 0.4 + RIGHT * 1.2)
        frames = VGroup(*[painting(0.55, 0.4, frame=True).move_to(room.get_top() + DOWN * 0.55 + RIGHT * x)
                          for x in (-1.1, -0.4, 0.3)])
        path = VGroup(*[Dot(radius=0.05, color=PALETTE["accent"]).move_to(room.get_center() + np.array([-1.2 + 0.4 * i,
                                                                                                        -0.3, 0]))
                        for i in range(6)])
        guide = VGroup(Circle(radius=0.26, fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0),
                       Text("AI", color=PALETTE["card"], font_size=14, weight="BOLD")).move_to(
            room.get_center() + np.array([1.2, 0.3, 0]))
        guide[1].move_to(guide[0].get_center())
        rm = VGroup(room, door, frames, path, guide)
        k1 = chip("a real exhibition, continued online", w=4.9, h=0.5, fs=16)
        k2 = chip("a walkable digital twin", w=4.9, h=0.5, border=PALETTE["good"], color=PALETTE["good"], fs=16)
        k3 = chip("an AI guide that art professionals can train", w=4.9, h=0.5, border=PALETTE["accent"],
                  color=PALETTE["accent"], fs=16)
        k4 = chip("more than mere documentation", w=4.9, h=0.5, border=PALETTE["dim"], color=PALETTE["dim"],
                  fs=16)
        kchips = VGroup(k1, k2, k3, k4).arrange(DOWN, buff=0.12)
        k_in = VGroup(kh, rm, kchips).arrange(DOWN, buff=0.3)
        right = VGroup(kb, fit_in(k_in, 5.5, 4.4).move_to(kb.get_center())).move_to([3.2, -0.1, 0])
        src = src_chip("Levine, 2026; Kenny, 2026; Ludwig Museum Koblenz, 2026", 7.6).move_to([0, -3.1, 0])
        for g in (hh, icon, h1, h2, h3, h4, kh, rm, k1, k2, k3, k4, src):
            g.set_opacity(0)

        self.play(FadeIn(two), run_time=0.5)
        wait_until(self, 1.7)
        self.play(FadeIn(left[0]), run_time=0.4)
        self.play(hh.animate.set_opacity(1), icon.animate.set_opacity(1), h1.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 5.3)
        self.play(h2.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 7.0)
        self.play(h3.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 10.6)
        self.play(h4.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 13.4)
        self.play(FadeIn(right[0]), run_time=0.4)
        self.play(kh.animate.set_opacity(1), rm.animate.set_opacity(1), k1.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 16.0)
        self.play(k2.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 19.1)
        self.play(k3.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 20.6)
        self.play(k4.animate.set_opacity(1), src.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 22.55)


class B07_IdeasToBorrow(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Ideas anyone could borrow", color=PALETTE["ink"], font_size=32, weight="BOLD").move_to([-3.0, 3.0, 0])
        label = chip("my ideas, not rules", w=3.2, h=0.5, border=PALETTE["accent"], color=PALETTE["accent"], fs=18)
        label.move_to([4.3, 3.0, 0])

        items = ["Let the artist do the talking",
                 "Put AI-made things beside the real work, and say which is which",
                 "Keep it temporary: the AI is a guest",
                 "End with an invitation to see the real thing",
                 "Show your workings, like Anadol sharing his data sources",
                 "Talk to your experts first"]
        rows = []
        for i, txt in enumerate(items):
            box = card_bg(11.6, 0.72)
            n = VGroup(Circle(radius=0.22, color=PALETTE["accent"], fill_color=PALETTE["accent"], fill_opacity=1,
                              stroke_width=0), Text(str(i + 1), color=PALETTE["card"], font_size=22, weight="BOLD"))
            n[1].move_to(n[0].get_center())
            t = fit(Text(txt, color=PALETTE["ink"], font_size=26), 10.3)
            n.move_to(box.get_left() + RIGHT * 0.5)
            t.move_to([box.get_left()[0] + 1.0 + t.width / 2, 0, 0])
            rows.append(VGroup(box, VGroup(n, t)))
        VGroup(*rows).arrange(DOWN, buff=0.14).move_to([0, -0.2, 0])

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 2.1)
        self.play(FadeIn(label, shift=DOWN * 0.1), run_time=0.4)
        for r, t in zip(rows, [4.8, 6.6, 11.0, 13.9, 16.6, 20.3]):
            wait_until(self, t)
            self.play(FadeIn(r, shift=UP * 0.1), run_time=0.4)
        wait_until(self, 21.78)


class B08_SendThemBack(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        pic = painting(3.2, 2.2).move_to([-4.0, 1.0, 0])
        real = Text("the real thing", color=PALETTE["good"], font_size=18, weight="BOLD").next_to(pic, UP, buff=0.15)
        visitor = person(1.2, PALETTE["ink"]).move_to([-4.0, -1.55, 0])
        sight = DashedLine(visitor.get_top() + UP * 0.05, pic.get_bottom() + DOWN * 0.05, color=PALETTE["accent"],
                           stroke_width=3)

        c1 = chip("its missing edges, re-seen", w=5.6, h=0.62, border=PALETTE["accent"], color=PALETTE["ink"], fs=19)
        c2 = chip("an artist, in his own words", w=5.6, h=0.62, border=PALETTE["accent"], color=PALETTE["ink"], fs=19)
        c3 = chip("a collection, as moving light", w=5.6, h=0.62, border=PALETTE["accent"], color=PALETTE["ink"], fs=19)
        caps = VGroup(c1, c2, c3).arrange(DOWN, buff=0.2).move_to([2.7, 2.05, 0])
        tools = chip("always meeting new tools: the camera, the projector", w=5.6, h=0.6, border=PALETTE["dim"],
                     color=PALETTE["dim"], fs=17).move_to([2.7, 0.55, 0])
        rep = chip("replace the original", w=2.7, h=0.8, border=PALETTE["miss"], color=PALETTE["miss"], fs=19)
        back = chip("send people back to it", w=2.8, h=0.8, border=PALETTE["good"], color=PALETTE["good"], fs=19)
        choice = VGroup(rep, back).arrange(RIGHT, buff=0.2).move_to([2.7, -0.55, 0])
        ok = tick(PALETTE["good"], 1.4).next_to(back, LEFT, buff=-0.05).shift(UP * 0.0)
        ok.move_to(back.get_top() + UP * 0.2 + RIGHT * 1.0)
        ring = SurroundingRectangle(back, color=PALETTE["good"], buff=0.08, stroke_width=4, corner_radius=0.1)
        fin = Text("That choice keeps the work authentic.", color=PALETTE["accent"], font_size=26, weight="BOLD")
        fit(fin, 11.0).move_to([0, -2.6, 0])
        for g in (c1, c2, c3, tools, rep, back, fin, real, sight):
            g.set_opacity(0)

        self.play(FadeIn(pic, shift=UP * 0.1), FadeIn(visitor), real.animate.set_opacity(1), sight.animate.set_opacity(1),
                  run_time=0.7)
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
        self.play(fin.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 23.37)


class B09_SourcesCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("A note on sources", color=PALETTE["ink"], font_size=30, weight="BOLD").move_to([0, 3.0, 0])

        refs = ["Kemp (2021), The Jakarta Post", "Sarmiento (2019), Palm Beach ArtsPaper", "Chan (2023), Wallpaper*",
                "Alemdar (n.d.), TRT World", "Donoghue (2025), Whitewall", "Levine (2026), The Boston Globe",
                "Kenny (2026), HBR Cold Call", "Ludwig Museum Koblenz (2026)"]
        rt = Text("References", color=PALETTE["accent"], font_size=20, weight="BOLD")
        rl = VGroup(*[Text(r, color=PALETTE["ink"], font_size=18) for r in refs]).arrange(DOWN, buff=0.17, aligned_edge=LEFT)
        r_in = VGroup(rt, rl).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        r_box = card_bg(5.7, 5.0)
        left = VGroup(r_box, fit_in(r_in, 5.2, 4.6).move_to(r_box.get_center())).move_to([-3.5, -0.2, 0])

        def note(txt, col):
            return chip(txt, w=6.1, h=0.95, border=col, color=col, fs=17)
        n1 = note("The Rijksmuseum story comes from\na wire report (AFP, via The Jakarta Post)", PALETTE["miss"])
        n2 = note("The Dalí Museum story is a 2019 review", PALETTE["miss"])
        n3 = note("The TRT World article\nshows no visible date", PALETTE["dim"])
        n4 = note("The opening scene and the ideas anyone could borrow\nare illustrations and suggestions,\nnot reported cases", PALETTE["accent"])
        n4 = chip("The opening scene and the ideas anyone could borrow\nare illustrations and suggestions, not reported cases",
                  w=6.1, h=1.15, border=PALETTE["accent"], color=PALETTE["accent"], fs=17)
        notes = VGroup(n1, n2, n3, n4).arrange(DOWN, buff=0.22).move_to([3.4, -0.2, 0])
        for g in (n1, n2, n3, n4):
            g.set_opacity(0)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.5)
        wait_until(self, 1.2)
        reveal(self, left, t1=0.4, t2=0.4)
        wait_until(self, 1.8)
        self.play(n1.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 5.2)
        self.play(n2.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 8.3)
        self.play(n3.animate.set_opacity(1), run_time=0.4)
        wait_until(self, 11.2)
        self.play(n4.animate.set_opacity(1), run_time=0.5)
        wait_until(self, 18.02)
