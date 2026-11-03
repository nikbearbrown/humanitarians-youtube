"""Manim beats for the reel `6g-and-iot`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Every figure on screen carries a source (also in SOURCES.md):
  ITU-R   six IMT-2030 usage scenarios; connection density 10^6-10^8 /km^2
  3GPP    Rel-21 timeline; ambient IoT device 1 (~1 uW) and device 2
  Ericsson  2030 cellular IoT mix -- 60% broadband / 40% NB-IoT+LTE-M, >7bn

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over six previous reels:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * citation beats use fit_src(), which reserves the citation strip
  * never draw a line THROUGH text
  * compose every label INTO the fitted group before fitting
  * _fit scales UP as well as down (FILL-THE-CANVAS)
  * a beat carried by text alone has no shape-state -- give it geometry
"""

import glob
import os

import manimpango
from manim import (
    DOWN, LEFT, RIGHT, UP, Create, FadeIn, LaggedStart, Line, RoundedRectangle,
    Scene, Text, VGroup, Write,
)

_TOOLKIT_FONTS = os.environ.get(
    "ART_FONT_DIR",
    "D:/Projects/brutalist.art/.claude/worktrees/video-creation-setup-4c85fe/runtime/fonts",
)
for _ttf in glob.glob(os.path.join(_TOOLKIT_FONTS, "**", "*.ttf"), recursive=True):
    manimpango.register_font(os.path.abspath(_ttf))

_FAMS = set(manimpango.list_fonts())
SERIF = "EB Garamond" if "EB Garamond" in _FAMS else "Georgia"
SANS = "Inter 28pt" if "Inter 28pt" in _FAMS else "Segoe UI"
MONO = "Consolas" if "Consolas" in _FAMS else "Courier New"

CREAM = "#FAF9F5"
INK = "#3D3929"
INK_SOFT = "#6B6559"
TERRA = "#D97757"

BODY_TOP = 2.25
BODY_BOTTOM = -2.45
BODY_W = 12.0
BODY_H = BODY_TOP - BODY_BOTTOM
SRC_BOTTOM = -1.95


def page(scene):
    scene.camera.background_color = CREAM


def kicker(text, sub=None):
    k = Text(text, font=SANS, font_size=22, color=INK_SOFT).to_edge(UP, buff=0.72)
    k.to_edge(LEFT, buff=0.9)
    rule = Line(k.get_left() + DOWN * 0.28, k.get_left() + RIGHT * 12.0 + DOWN * 0.28,
                stroke_width=1.4, color=INK_SOFT)
    grp = VGroup(k, rule)
    if sub:
        s = Text(sub, font=MONO, font_size=19, color=INK_SOFT)
        s.next_to(rule, DOWN, buff=0.20).align_to(k, LEFT)
        grp.add(s)
    return grp


def spark(text):
    return Text(text, font=SERIF, font_size=37, color=TERRA).to_edge(DOWN, buff=0.62)


def source_line(text):
    return Text(text, font=MONO, font_size=16, color=INK_SOFT).to_edge(DOWN, buff=1.55)


def _fit(group, w, h, centre_y, grow=1.9):
    if group.width <= 0 or group.height <= 0:
        return group
    k = min(w / group.width, h / group.height)
    k = min(k, grow) if k > 1 else k
    group.scale(k)
    group.move_to([0, centre_y, 0])
    return group


def fit(group, w=BODY_W, h=BODY_H):
    return _fit(group, w, h, (BODY_TOP + BODY_BOTTOM) / 2)


def fit_src(group, w=BODY_W):
    return _fit(group, w, BODY_TOP - SRC_BOTTOM, (BODY_TOP + SRC_BOTTOM) / 2)


def chip(label, color, font_size=19, pad=0.32, height=0.36):
    t = Text(label, font=MONO, font_size=font_size, color=color)
    box = RoundedRectangle(width=t.width + pad, height=height, corner_radius=0.07,
                           stroke_width=1.5, stroke_color=color, fill_opacity=0)
    box.move_to(t.get_center())
    return VGroup(box, t)


def panel(title, lines, accent=INK_SOFT, min_w=4.4, fs=20, title_fs=24):
    t = Text(title, font=SANS, font_size=title_fs, color=accent)
    body = VGroup(*[Text(l, font=MONO, font_size=fs, color=INK) for l in lines])
    body.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
    inner = VGroup(t, body).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
    box = RoundedRectangle(width=max(min_w, inner.width + 0.8),
                           height=inner.height + 0.8, corner_radius=0.12,
                           stroke_width=1.8, stroke_color=accent, fill_opacity=0)
    box.move_to(inner.get_center())
    return VGroup(box, inner)


class B01_AdvertisedVsBinding(Scene):
    """BLUF: what is advertised against what actually binds. 17.24s."""

    ADVERTISED = ["peak data rate", "latency", "connection density"]
    BINDING = ["battery life", "coverage where it is", "cost per node"]

    def construct(self):
        page(self)
        head = kicker("TWO LISTS", "and they barely overlap")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        left = panel("WHAT 6G ADVERTISES", self.ADVERTISED, INK_SOFT, min_w=5.0, fs=22)
        right = panel("WHAT ACTUALLY BINDS", self.BINDING, TERRA, min_w=5.0, fs=22)
        fit(VGroup(left, right).arrange(RIGHT, buff=0.9, aligned_edge=UP))

        self.play(Create(left[0]), FadeIn(left[1][0]), run_time=1.3)
        for line in left[1][1]:
            self.play(FadeIn(line, shift=RIGHT * 0.18), run_time=0.75)
        self.wait(0.8)
        self.play(Create(right[0]), FadeIn(right[1][0]), run_time=1.3)
        for line in right[1][1]:
            self.play(FadeIn(line, shift=RIGHT * 0.18), run_time=0.75)
        self.wait(1.2)

        point = spark("Speed was never the constraint")
        self.play(Write(point), run_time=1.9)
        self.wait(3.14)


class B02_ThreeConstraints(Scene):
    """FRAMEWORK: the three constraints, before any 6G claim. 19.52s."""

    CS = [
        ("1", "POWER", "how long before a human\nhas to touch it?"),
        ("2", "COVERAGE", "does it work where the\nthing actually is?"),
        ("3", "COST PER NODE", "can you afford ten\nthousand of them?"),
    ]

    def construct(self):
        page(self)
        head = kicker("THREE CONSTRAINTS", "what decides whether a deployment happens")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = VGroup()
        for num, title, body in self.CS:
            n = Text(num, font=SERIF, font_size=34, color=TERRA)
            t = Text(title, font=SANS, font_size=27, color=INK)
            b = Text(body, font=MONO, font_size=20, color=INK_SOFT, line_spacing=0.7)
            hr = VGroup(n, t).arrange(RIGHT, buff=0.30)
            inner = VGroup(hr, b).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
            box = RoundedRectangle(width=inner.width + 0.85, height=inner.height + 0.85,
                                   corner_radius=0.12, stroke_width=1.8,
                                   stroke_color=INK_SOFT, fill_opacity=0)
            box.move_to(inner.get_center())
            cards.add(VGroup(box, inner))
        fit(cards.arrange(RIGHT, buff=0.45))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1], shift=UP * 0.15), run_time=1.1)
            self.wait(1.5)

        point = spark("Score any generation on these three")
        self.play(Write(point), run_time=2.0)
        self.wait(5.82)


class B03_StandardsTimeline(Scene):
    """MECHANISM: the emergence, as a standards calendar. 32.66s."""

    SCENARIOS = [("immersive communication", False), ("massive communication", False),
                 ("hyper-reliable low latency", False), ("ubiquitous connectivity", True),
                 ("AI and communication", True), ("integrated sensing", True)]
    STOPS = [("Rel-21", "normative 6G work begins"),
             ("Dec 2028", "Stage-3 protocol specs"),
             ("Mar 2029", "ASN.1 / OpenAPI freeze"),
             ("~2030", "first commercial systems")]

    def construct(self):
        page(self)
        head = kicker("WHERE 6G ACTUALLY IS", "ITU-R sets the framework · 3GPP writes the spec")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        chips = VGroup(*[chip(name, TERRA if new else INK_SOFT, font_size=17,
                              pad=0.28, height=0.34)
                         for name, new in self.SCENARIOS])
        rows = VGroup(VGroup(*chips[:3]).arrange(RIGHT, buff=0.22),
                      VGroup(*chips[3:]).arrange(RIGHT, buff=0.22)).arrange(DOWN, buff=0.20)
        scen_label = Text("six IMT-2030 usage scenarios  —  three inherited, three new",
                          font=SANS, font_size=21, color=INK_SOFT)
        scenarios = VGroup(scen_label, rows).arrange(DOWN, buff=0.26)

        stops = VGroup()
        for when, what in self.STOPS:
            w = Text(when, font=MONO, font_size=22, color=INK)
            d = Text(what, font=SANS, font_size=19, color=INK_SOFT)
            stops.add(VGroup(w, d).arrange(DOWN, buff=0.16))
        stops.arrange(RIGHT, buff=0.62)
        axis = Line(stops.get_left() + LEFT * 0.25, stops.get_right() + RIGHT * 0.25,
                    stroke_width=2.0, color=INK_SOFT)
        axis.next_to(stops, DOWN, buff=0.26)
        timeline = VGroup(stops, axis)

        body = fit_src(VGroup(scenarios, timeline).arrange(DOWN, buff=0.62))
        src = source_line("ITU-R IMT-2030 framework · 3GPP Release 21 timeline")

        self.play(FadeIn(scen_label), run_time=0.9)
        self.play(LaggedStart(*[Create(c[0]) for c in chips],
                              *[FadeIn(c[1]) for c in chips], lag_ratio=0.25),
                  run_time=4.2)
        self.wait(1.6)
        self.play(Create(axis), run_time=1.2)
        for s in stops:
            self.play(FadeIn(s, shift=UP * 0.15), run_time=1.0)
        self.wait(1.4)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(1.0)

        point = spark("A standards calendar, not a product")
        self.play(Write(point), run_time=2.1)
        self.wait(11.46)


class B04_AmbientDevices(Scene):
    """EVIDENCE: constraint 1 — the battery-less tier. 31.40s."""

    def construct(self):
        page(self)
        head = kicker("CONSTRAINT 1 — POWER", "ambient IoT: devices with no battery")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        d1 = panel("DEVICE 1", ["~1 µW peak", "no amplifier", "no carrier generator",
                                "backscatters an external wave"], TERRA, min_w=5.2)
        d2 = panel("DEVICE 2", ["a few hundred µW peak", "has an amplifier",
                                "own carrier generator", "more range, more complexity"],
                   INK_SOFT, min_w=5.2)
        pair = VGroup(d1, d2).arrange(RIGHT, buff=0.85, aligned_edge=UP)

        harvest = Text("energy harvested from radio, heat or light",
                       font=SANS, font_size=24, color=INK)
        body = fit_src(VGroup(pair, harvest).arrange(DOWN, buff=0.6))
        src = source_line("3GPP ambient IoT study · Release 19, extended in Release 20")

        self.play(Create(d1[0]), FadeIn(d1[1][0]), run_time=1.5)
        for line in d1[1][1]:
            self.play(FadeIn(line, shift=RIGHT * 0.18), run_time=0.9)
        self.wait(1.4)
        self.play(Create(d2[0]), FadeIn(d2[1][0]), run_time=1.5)
        for line in d2[1][1]:
            self.play(FadeIn(line, shift=RIGHT * 0.18), run_time=0.9)
        self.wait(1.4)
        self.play(FadeIn(harvest, shift=UP * 0.15), FadeIn(src), run_time=1.6)
        self.wait(1.4)

        point = spark("No battery, no constraint one")
        self.play(Write(point), run_time=2.0)
        self.wait(8.71)


class B05_DensityAndSensing(Scene):
    """EVIDENCE: constraint 2 — density and the sensing scenario. 22.10s."""

    def construct(self):
        page(self)
        head = kicker("CONSTRAINT 2 — COVERAGE", "ubiquitous connectivity, by name")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        big = Text("10⁶ – 10⁸", font=SERIF, font_size=74, color=TERRA)
        unit = Text("devices per km²", font=SANS, font_size=25, color=INK)
        mult = Text("1–100× IMT-2020", font=MONO, font_size=21, color=INK_SOFT)
        dens_inner = VGroup(big, unit, mult).arrange(DOWN, buff=0.20)
        dens_box = RoundedRectangle(width=dens_inner.width + 1.1,
                                    height=dens_inner.height + 0.85, corner_radius=0.14,
                                    stroke_width=1.9, stroke_color=TERRA, fill_opacity=0)
        dens_box.move_to(dens_inner.get_center())
        density = VGroup(dens_box, dens_inner)

        sensing = panel("INTEGRATED SENSING", ["the same radio that carries",
                                               "your data detects what",
                                               "moves through it"], INK_SOFT, min_w=5.0)
        pair = VGroup(density, sensing).arrange(RIGHT, buff=0.9, aligned_edge=UP)
        body = fit_src(pair)
        src = source_line("ITU-R IMT-2030 framework · connection density target")

        self.play(Create(dens_box), FadeIn(dens_inner), run_time=2.0)
        self.wait(1.8)
        self.play(Create(sensing[0]), FadeIn(sensing[1]), run_time=1.9)
        self.wait(1.6)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(1.2)

        point = spark("Also not a speed feature")
        self.play(Write(point), run_time=1.9)
        self.wait(5.91)


class B06_TheBill(Scene):
    """EVIDENCE: the cons, each mapped to a constraint. 22.04s."""

    COSTS = [
        ("THE CALENDAR", "nothing you deploy before 2030 is 6G"),
        ("NETWORK ENERGY", "denser cells, more radio chains"),
        ("THE READER", "the tag is cheap; the reader is not"),
    ]

    def construct(self):
        page(self)
        head = kicker("THE BILL", "what each promise costs")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = VGroup()
        for title, detail in self.COSTS:
            t = Text(title, font=SANS, font_size=25, color=TERRA)
            d = Text(detail, font=MONO, font_size=22, color=INK)
            cell = RoundedRectangle(width=d.width + 0.65, height=0.74,
                                    corner_radius=0.09, stroke_width=1.8,
                                    stroke_color=TERRA, fill_opacity=0)
            cell.move_to(d.get_center())
            rows.add(VGroup(t, VGroup(cell, d)))
        lw = max(r[0].width for r in rows)
        for r in rows:
            r[1].next_to(r[0], RIGHT, buff=0.6 + (lw - r[0].width))
        rows.arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        fit(rows)

        self.play(LaggedStart(*[FadeIn(r[0], shift=RIGHT * 0.18) for r in rows],
                              lag_ratio=0.2), run_time=1.1)
        for r in rows:
            self.play(Create(r[1][0]), FadeIn(r[1][1], shift=RIGHT * 0.18), run_time=1.5)
        self.wait(1.6)

        point = spark("The device gets cheaper. The infrastructure does not.")
        self.play(Write(point), run_time=2.2)
        self.wait(7.84)


class B07_Mix2030(Scene):
    """FALSIFIABILITY: what the 2030 forecast says. 32.29s."""

    def construct(self):
        page(self)
        head = kicker("WHAT THE FRAMEWORK PREDICTS",
                      "a generation should not displace what already satisfies the three")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        year = Text("2030  —  6G's launch year", font=SANS, font_size=26, color=INK)
        broad = RoundedRectangle(width=6.0, height=0.8, corner_radius=0.09,
                                 stroke_width=2.0, stroke_color=INK, fill_opacity=0)
        legacy = RoundedRectangle(width=4.0, height=0.8, corner_radius=0.09,
                                  stroke_width=2.0, stroke_color=TERRA, fill_opacity=0)
        b_lab = Text("60%  4G/5G broadband IoT", font=MONO, font_size=20, color=INK)
        b_lab.move_to(broad.get_center())
        l_lab = Text("40%  NB-IoT + LTE-M", font=MONO, font_size=20, color=TERRA)
        l_lab.move_to(legacy.get_center())
        bar = VGroup(VGroup(broad, b_lab), VGroup(legacy, l_lab)).arrange(RIGHT, buff=0.14)

        total = Text("over 7 billion cellular IoT connections", font=SANS,
                     font_size=22, color=INK_SOFT)
        punch = Text("NB-IoT and LTE-M were introduced 2015–2017",
                     font=SANS, font_size=26, color=TERRA)
        body = fit_src(VGroup(year, bar, total, punch).arrange(DOWN, buff=0.42))
        src = source_line("Ericsson Mobility Report · IoT connections forecast to 2030")

        self.play(FadeIn(year), run_time=1.0)
        self.play(Create(broad), FadeIn(b_lab), run_time=1.8)
        self.wait(1.2)
        self.play(Create(legacy), FadeIn(l_lab), run_time=1.8)
        self.wait(1.4)
        self.play(FadeIn(total), run_time=1.1)
        self.wait(1.4)
        self.play(Write(punch), run_time=2.4)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(1.4)

        point = spark("Fifteen-year-old tech, four in ten connections")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.9)
        self.wait(13.09)


class B08_Verdict(Scene):
    """VERDICT: the three constraints scored, and what to do now. 22.42s."""

    SCORES = [
        ("POWER", "genuinely improved — ambient tier only", TERRA),
        ("COVERAGE", "improved on paper; depends on build-out", INK),
        ("COST PER NODE", "cheaper device, dearer infrastructure", INK),
    ]

    def construct(self):
        page(self)
        head = kicker("SCORED", "the three constraints, after the evidence")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = VGroup()
        for axis, answer, color in self.SCORES:
            a = Text(axis, font=SANS, font_size=25, color=INK_SOFT)
            v = Text(answer, font=MONO, font_size=21, color=color)
            cell = RoundedRectangle(width=v.width + 0.6, height=0.7, corner_radius=0.09,
                                    stroke_width=1.7, stroke_color=color, fill_opacity=0)
            cell.move_to(v.get_center())
            rows.add(VGroup(a, VGroup(cell, v)))
        lw = max(r[0].width for r in rows)
        for r in rows:
            r[1].next_to(r[0], RIGHT, buff=0.6 + (lw - r[0].width))
        rows.arrange(DOWN, buff=0.32, aligned_edge=LEFT)

        use = Text("USE IT FOR:  the battery-less tier — nothing before it did that",
                   font=SANS, font_size=22, color=INK)
        wait_not = Text("DO NOT WAIT:  an ordinary sensor network — that answer already ships",
                        font=SANS, font_size=22, color=TERRA)
        tail = VGroup(use, wait_not).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        fit(VGroup(rows, tail).arrange(DOWN, buff=0.55))

        self.play(LaggedStart(*[FadeIn(r[0], shift=RIGHT * 0.18) for r in rows],
                              lag_ratio=0.2), run_time=1.0)
        for r in rows:
            self.play(Create(r[1][0]), FadeIn(r[1][1], shift=RIGHT * 0.18), run_time=1.15)
        self.wait(1.2)
        self.play(FadeIn(use, shift=UP * 0.15), run_time=1.2)
        self.play(FadeIn(wait_not, shift=UP * 0.15), run_time=1.2)
        self.wait(1.4)

        point = spark("Find the binding constraint first")
        self.play(Write(point), run_time=2.0)
        self.wait(8.13)
