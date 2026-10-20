"""scenes.py — portrait (9:16) Manim scenes for ab-testing-can-lie-to-you/short.
Full-length short (no beats cut): all 5 Manim beats re-laid-out for portrait —
B01, B04, B07, B08, B09. Not shrunk copies of the landscape scenes: the portrait
frame is narrow in x (frame_width=4.5, safe ±1.95) and unchanged in y
(frame_height=8.0, safe ±3.4), so every layout is restacked vertically. The bar
charts (B04, B07) turn horizontal so they fill a tall frame.

DATA + TIMING come from the landscape ../scenes.py (imported, not copied): the
same numbers parsed from ../py/*.out at render time, the same measured audio
durations, the same narration-cue placement. Scene classes must be declared as
plain Scene subclasses named B0X_Name — run.sh finds them by regex.
"""
from manim import *
from pathlib import Path
import importlib.util

# `manim -r 2160,3840` does NOT reset the coordinate frame to portrait — without
# these two lines every scene below renders in the 16:9 default space
# (frame_width=14.222) and shrinks into the center of the canvas.
config.frame_width = 4.5
config.frame_height = 8.0

# Import the landscape module for data/timing. run.sh's Gate A/W pre-flights run an
# ISOLATED COPY of this file in a temp dir, so fall back to the reel's real location.
_REEL = Path("/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art/projects/2026-10-12-ab-testing-can-lie-to-you")
_parent = Path(__file__).resolve().parent.parent / "scenes.py"
if not _parent.is_file() or not (_parent.parent / "py").is_dir():
    _parent = _REEL / "scenes.py"
_spec = importlib.util.spec_from_file_location("landscape_scenes", _parent)
L = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(L)

CREAM, INK, TERRACOTTA, SEC, RULE, PALE, MONO = L.CREAM, L.INK, L.TERRACOTTA, L.SEC, L.RULE, L.PALE, L.MONO
itext = L.itext
SAFE_X = 1.95


def handle(scene):
    """Visible author handle, lower-right inside the portrait safe area."""
    h = Text("Supriya", color=SEC, font_size=20, weight="BOLD").set_opacity(0.8)
    h.move_to([SAFE_X - 0.05, -3.25, 0], aligned_edge=RIGHT)
    scene.add(h)
    return h


class Clock(L.Clock):
    """The landscape clock (same cues, same DUR) with the portrait handle."""

    def __init__(self, scene, bid):
        self.s, self.bid, self.t = scene, bid, 0.0
        self.DUR = L.dur(bid)
        scene.camera.background_color = CREAM
        handle(scene)


def lines(*texts, buff=0.1, edge=None, **kw):
    """Stacked single-line Texts (one Text per line, so the gates measure each)."""
    g = VGroup(*[Text(t, **kw) for t in texts])
    return g.arrange(DOWN, buff=buff, aligned_edge=edge) if edge is not None else g.arrange(DOWN, buff=buff)


def source_lines(*texts, size=16):
    g = VGroup(*[itext(t, size) for t in texts])
    return g.arrange(DOWN, buff=0.06, aligned_edge=LEFT)


def sim_tag(fname, y=3.2):
    f = Text(fname, font=MONO, color=SEC, font_size=16)
    chip = Text("SIMULATION", font=MONO, color=TERRACOTTA, font_size=14, weight="BOLD")
    box = SurroundingRectangle(chip, color=TERRACOTTA, stroke_width=2, buff=0.07, corner_radius=0.04)
    g = VGroup(f, VGroup(box, chip)).arrange(RIGHT, buff=0.2)
    return g.move_to([0, y, 0])


def verdict_card(text, y, w=3.4, h=0.95, size=40):
    card = RoundedRectangle(corner_radius=0.15, width=w, height=h, color=INK, stroke_width=3,
                            fill_color=WHITE, fill_opacity=1).move_to([0, y, 0])
    return VGroup(card, Text(text, color=INK, weight="BOLD", font_size=size).move_to(card))


def carousel(n, width=3.8, h=1.7, y=1.6):
    gap = 0.05
    w = (width - gap * (n - 1)) / n
    col = TERRACOTTA if n == 16 else INK
    cards = VGroup(*[RoundedRectangle(corner_radius=min(0.05, w / 4), width=w, height=h,
                                      stroke_width=0, fill_color=col, fill_opacity=0.85)
                     for _ in range(n)]).arrange(RIGHT, buff=gap)
    frame = RoundedRectangle(corner_radius=0.1, width=width + 0.25, height=h + 0.25,
                             color=RULE, stroke_width=3)
    return VGroup(frame, cards.move_to(frame)).move_to([0, y, 0])


# horizontal bars: 1 click/user = 0.62 units; bars start at the left safe edge
BAR_X0, UNIT, BAR_H = -1.95, 0.62, 0.62


def hbar(y, v, color):
    w = UNIT * v
    return Rectangle(width=w, height=BAR_H, stroke_width=0, fill_color=color,
                     fill_opacity=1).move_to([BAR_X0 + w / 2, y, 0])


def hbar_value(b, v, color):
    return Text(f"{v:.2f}", color=color, weight="BOLD", font_size=30).next_to(b, RIGHT, buff=0.1)


def hbar_name(b, name):
    t = Text(name, color=CREAM, weight="BOLD", font_size=20)
    return t.move_to(b.get_left() + RIGHT * (0.1 + t.width / 2))


def readout_hbars(ctrl, test, y_ctrl=2.0, y_test=1.2):
    bc, bt = hbar(y_ctrl, ctrl, INK), hbar(y_test, test, TERRACOTTA)
    vals = VGroup(hbar_value(bc, ctrl, INK), hbar_value(bt, test, TERRACOTTA))
    names = VGroup(hbar_name(bc, "control"), hbar_name(bt, "test"))
    unit = itext("clicks per user", 18).move_to([0, y_test - 0.65, 0])
    return VGroup(bc, bt), vals, names, unit


# ── B01 — PROBLEM ─────────────────────────────────────────────────────────────

class B01_DontShip(Scene):
    """PROBLEM — MSN went from 12 to 16 carousel cards; the test said 'significant drop'."""

    def construct(self):
        c = Clock(self, "B01")
        head = Text("MSN's carousel", color=INK, weight="BOLD", font_size=34).move_to([0, 3.0, 0])
        twelve = carousel(12)
        n12 = Text("12 cards", font=MONO, color=SEC, font_size=22).next_to(twelve, DOWN, buff=0.2)
        c.run(Write(head), FadeIn(twelve, shift=RIGHT * 0.2), FadeIn(n12), rt=1.2)

        c.until("sixteen rotating cards")
        sixteen = carousel(16)
        n16 = Text("16 cards", font=MONO, color=TERRACOTTA, font_size=22, weight="BOLD").move_to(n12)
        c.run(ReplacementTransform(twelve, sixteen), ReplacementTransform(n12, n16), rt=1.2)

        c.until("They expected")
        hope = VGroup(Arrow(DOWN * 0.45, UP * 0.45, color=RULE, stroke_width=8, buff=0),
                      itext("expected: more clicks", 24)).arrange(RIGHT, buff=0.2).move_to([0, -0.3, 0])
        c.run(FadeIn(hope, shift=UP * 0.15), rt=0.7)

        c.until("The test said")
        drop = VGroup(Arrow(UP * 0.4, DOWN * 0.4, color=INK, stroke_width=8, buff=0),
                      VGroup(Text("significant drop", color=INK, weight="BOLD", font_size=30),
                             Text("p < 0.05", font=MONO, color=INK, font_size=24)
                             ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
                      ).arrange(RIGHT, buff=0.2).move_to([0, -1.2, 0])
        c.run(FadeIn(drop, shift=DOWN * 0.15), hope.animate.set_opacity(0.35), rt=0.8)

        c.until("On that result")
        card = verdict_card("Don't ship.", -2.2)
        c.run(FadeIn(card[0], shift=UP * 0.15), Write(card[1]), rt=0.9)

        c.until("This is real")
        src = source_lines("Fabijan et al., KDD 2019", "MSN carousel experiment", size=18)
        src.move_to([-1.95, -3.0, 0], aligned_edge=LEFT)
        c.run(FadeIn(src, shift=UP * 0.1), rt=0.6)
        c.pad()


# ── B04 — OUTPUT, cycle 1 ─────────────────────────────────────────────────────

class B04_LooksWorse(Scene):
    """OUTPUT, cycle 1 — the misleading readout: control 3.89 vs test 3.20."""

    def construct(self):
        c = Clock(self, "B04")
        bars, vals, names, unit = readout_hbars(L.V1_CTRL, L.V1_TEST)
        c.run(FadeIn(sim_tag("carousel_v1.out")), FadeIn(unit), rt=0.6)

        c.until("Control")
        c.run(GrowFromEdge(bars[0], LEFT), rt=0.8)
        c.run(FadeIn(names[0]), FadeIn(vals[0], shift=LEFT * 0.1), rt=0.3)
        c.until("Test")
        c.run(GrowFromEdge(bars[1], LEFT), rt=0.8)
        c.run(FadeIn(names[1]), FadeIn(vals[1], shift=LEFT * 0.1), rt=0.3)

        c.until("A z score")
        stats = VGroup(Text(f"z  {L.V1_Z.replace('-', '−')}", font=MONO, color=INK, font_size=40, weight="BOLD"),
                       Text(f"p  {L.V1_P}", font=MONO, color=INK, font_size=30)
                       ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).move_to([0, -0.3, 0])
        c.run(FadeIn(stats, shift=UP * 0.1), rt=0.6)

        c.until("Significant")
        worse = Text("Significant. Worse.", color=INK, weight="BOLD", font_size=34).move_to([0, -1.35, 0])
        c.run(Write(worse), rt=0.8)

        c.until("Don't ship")
        card = verdict_card("Don't ship.", -2.4)
        c.run(FadeIn(card[0], shift=UP * 0.15), Write(card[1]), rt=0.7)
        c.pad()


# ── B07 — OUTPUT, cycle 2 ─────────────────────────────────────────────────────

class B07_TheFlip(Scene):
    """OUTPUT, cycle 2 — the split is off (SRM), then the bars flip once the filter is fixed.
    Flag C (approved): the paper's own real SRM example as a source line."""

    def construct(self):
        c = Clock(self, "B07")
        c.run(FadeIn(sim_tag("carousel_v2.out")), rt=0.4)

        head = itext("users after the bot filter", 22).move_to([0, 2.65, 0])

        def count_row(label, n, col, y):
            lab = Text(label, color=INK, font_size=24)
            num = Text(f"{n:,}", font=MONO, color=col, font_size=46, weight="BOLD")
            lab.move_to([-1.95, y, 0], aligned_edge=LEFT)
            num.move_to([1.95, y, 0], aligned_edge=RIGHT)
            return VGroup(lab, num)
        r1 = count_row("control", L.V2_NC, INK, 2.0)
        r2 = count_row("test", L.V2_NT, TERRACOTTA, 1.25)
        c.run(FadeIn(head), FadeIn(r1), FadeIn(r2), rt=0.8)

        c.until("three thousand users short")
        miss = Text(f"−{L.V2_NC - L.V2_NT:,} missing", font=MONO, color=TERRACOTTA, font_size=32,
                    weight="BOLD").move_to([1.95, 0.55, 0], aligned_edge=RIGHT)
        c.run(FadeIn(miss, shift=UP * 0.1), Indicate(r2[1], color=TERRACOTTA, scale_factor=1.06), rt=0.8)

        c.until("The odds")
        p = float(L.V2_SRM_P)
        odds = VGroup(Text(f"SRM p  {L.V2_SRM_P}", font=MONO, color=INK, font_size=36, weight="BOLD"),
                      Text(f"≈ {round(p * 1e6)} in a million by chance", color=INK, font_size=24)
                      ).arrange(DOWN, buff=0.12).move_to([0, -0.95, 0])
        c.run(FadeIn(odds, shift=UP * 0.1), rt=0.7)

        c.until("That's a sample ratio mismatch")
        srm = Text("Sample ratio mismatch.", color=TERRACOTTA, weight="BOLD", font_size=26).move_to([0, -1.75, 0])
        src = source_lines("Real SRMs are this subtle —",
                           "Fabijan et al.'s example: 821,588",
                           "vs 815,482 users, < 1 in 500k.", size=17)
        src.move_to([-1.95, -2.6, 0], aligned_edge=LEFT)
        c.run(Write(srm), FadeIn(src, shift=UP * 0.1), rt=0.9)

        # Phase 2 — fix the filter: the readout flips (top block is replaced by bars).
        c.until("Fix the filter")
        bars, vals, names, unit = readout_hbars(L.V2_CTRL, L.V2_TEST, y_ctrl=2.25, y_test=1.45)
        ghost = VGroup(hbar(2.25, L.V1_CTRL, PALE), hbar(1.45, L.V1_TEST, PALE))
        c.run(FadeOut(VGroup(head, r1, r2, miss)), FadeIn(ghost), FadeIn(unit), rt=0.6)
        c.run(GrowFromEdge(bars[0], LEFT), GrowFromEdge(bars[1], LEFT), rt=1.0)
        c.run(FadeIn(names), FadeIn(vals), rt=0.4)

        c.until("The loss was a win")
        flip = VGroup(Arrow(DOWN * 0.4, UP * 0.4, color=TERRACOTTA, stroke_width=8, buff=0),
                      Text("The loss was a win.", color=TERRACOTTA, weight="BOLD", font_size=30)
                      ).arrange(RIGHT, buff=0.2).move_to([0, 0.2, 0])
        c.run(FadeOut(ghost), FadeIn(flip, shift=UP * 0.15), rt=0.8)
        c.pad()


# ── B08 — SECOND LIE: PEEKING ─────────────────────────────────────────────────

class B08_Peeking(Scene):
    """Peeking, one beat — 1,000 A/A tests, false winners by day vs the 5% line."""
    X0, X1, Y0, Y1 = -1.45, 1.75, -0.4, 2.0          # plot box
    YMAX = 30.0

    def px(self, day):
        return self.X0 + (day - 1) / 19 * (self.X1 - self.X0)

    def py(self, pct):
        return self.Y0 + pct / self.YMAX * (self.Y1 - self.Y0)

    def construct(self):
        c = Clock(self, "B08")
        head = Text("The second lie:", color=INK, weight="BOLD", font_size=32).move_to([0, 3.2, 0])
        head2 = Text("peeking", color=TERRACOTTA, weight="BOLD", font_size=32).next_to(head, DOWN, buff=0.08)
        c.run(Write(head), Write(head2), rt=0.9)

        c.until("I ran a thousand")
        sub = itext("1,000 A/A tests · both groups identical", 17).move_to([0, 2.35, 0])
        xa = Line([self.X0, self.Y0, 0], [self.X1, self.Y0, 0], color=RULE, stroke_width=3)
        ya = Line([self.X0, self.Y0, 0], [self.X0, self.Y1, 0], color=RULE, stroke_width=3)
        xt = VGroup(*[Text(str(d), font=MONO, color=SEC, font_size=16).move_to([self.px(d), self.Y0 - 0.2, 0])
                      for d in (1, 5, 10, 15, 20)])
        xl = Text("day", color=SEC, font_size=16).move_to([0.15, self.Y0 - 0.45, 0])
        yt = VGroup(*[Text(f"{p}%", font=MONO, color=SEC, font_size=16).next_to([self.X0, self.py(p), 0], LEFT, buff=0.08)
                      for p in (0, 10, 20)])
        five = DashedLine([self.X0, self.py(5), 0], [self.X1, self.py(5), 0], color=SEC, stroke_width=2)
        five_l = Text("5% — what you signed up for", color=SEC, font_size=15).next_to(five, UP, buff=0.06).align_to(five, RIGHT)
        tag = sim_tag("peeking.out", y=-1.2)
        c.run(FadeIn(sub), Create(xa), Create(ya), FadeIn(xt), FadeIn(xl), FadeIn(yt), FadeIn(tag), rt=0.9)
        c.run(Create(five), FadeIn(five_l), rt=0.5)

        pts = [[self.px(d + 1), self.py(n * 100 / L.PK_TESTS), 0] for d, n in enumerate(L.PK_CURVE)]
        curve = VMobject(color=TERRACOTTA, stroke_width=5).set_points_as_corners(pts)
        c.until("checking every day")
        span = max(1.5, L.cue("B08", "and a quarter") - c.t)
        c.run(Create(curve, rate_func=linear), rt=span)
        end = Dot(pts[-1], color=TERRACOTTA, radius=0.07)
        peek_l = Text(f"{L.PK_PEEK:.1f}% crown a winner", color=TERRACOTTA, weight="BOLD", font_size=21
                      ).next_to(end, UP, buff=0.15).align_to(end, RIGHT)
        c.run(FadeIn(end), FadeIn(peek_l, shift=DOWN * 0.1), rt=0.5)

        c.until("Look once")
        once = Dot([self.px(20), self.py(L.PK_ONCE), 0], color=INK, radius=0.07)
        once_l = Text(f"look once: {L.PK_ONCE:.1f}%", color=INK, weight="BOLD", font_size=18
                      ).next_to(once, LEFT, buff=0.12).shift(DOWN * 0.17)
        c.run(FadeIn(once, scale=0.5), FadeIn(once_l), rt=0.6)

        c.until("Researchers at Stanford")
        box = RoundedRectangle(corner_radius=0.12, width=3.2, height=1.05, color=INK, stroke_width=3,
                               fill_color=WHITE, fill_opacity=1).move_to([0, -2.05, 0])
        big = VGroup(Text("checking nonstop", color=INK, font_size=20),
                     Text("> 30%", color=INK, weight="BOLD", font_size=36)).arrange(DOWN, buff=0.04).move_to(box)
        src = source_lines("Johari, Pekelis & Walsh, 2015 ·", "continuous checks, 10,000 obs.", size=15)
        src.move_to([-1.95, -2.92, 0], aligned_edge=LEFT)
        c.run(FadeIn(box, shift=UP * 0.15), FadeIn(big), FadeIn(src), rt=0.8)
        c.pad()


# ── B09 — SUMMARY ─────────────────────────────────────────────────────────────

class B09_ThreeChecks(Scene):
    """SUMMARY — MSN resolved (flipped, shipped), ~6% of experiments, three checks."""

    def construct(self):
        c = Clock(self, "B09")
        car = carousel(16, width=3.6, h=0.95, y=3.0)
        c.run(FadeIn(car, shift=RIGHT * 0.15), rt=0.7)

        c.until("The bot filter")
        why = VGroup(itext("the bot filter dropped", 20), itext("its most engaged users", 20)
                     ).arrange(DOWN, buff=0.05).next_to(car, DOWN, buff=0.2)
        c.run(FadeIn(why, shift=UP * 0.1), rt=0.6)

        c.until("Once that was fixed")
        up = VGroup(Arrow(DOWN * 0.4, UP * 0.4, color=TERRACOTTA, stroke_width=8, buff=0),
                    Text("flipped. shipped.", color=TERRACOTTA, weight="BOLD", font_size=32)
                    ).arrange(RIGHT, buff=0.2).move_to([0, 1.25, 0])
        c.run(FadeIn(up, shift=UP * 0.15), rt=0.7)

        c.until("about six percent")
        six = VGroup(Text("~6%", color=INK, weight="BOLD", font_size=36),
                     VGroup(Text("of Microsoft experiments", color=INK, font_size=16),
                            itext("had an SRM · Fabijan et al. 2019", 13)
                            ).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
                     ).arrange(RIGHT, buff=0.2).move_to([0, 0.25, 0])
        c.run(FadeIn(six, shift=UP * 0.1), rt=0.6)

        checks = [("check the split first", ("Check the split first.",)),
                  ("fix your sample size", ("Fix the sample size", "in advance.")),
                  ("if you must peek", ("Must peek? Use a", "test built for it."))]
        rows = VGroup()
        ys = (-0.75, -1.65, -2.65)
        for (_, txt), y in zip(checks, ys):
            n = Text(str(len(rows) + 1), color=TERRACOTTA, weight="BOLD", font_size=30).move_to([-1.65, y, 0])
            badge = Circle(radius=0.25, color=TERRACOTTA, stroke_width=4).move_to(n)
            t = lines(*txt, buff=0.06, edge=LEFT, color=INK, font_size=28)
            t.move_to([-1.25, y, 0], aligned_edge=LEFT)
            rows.add(VGroup(badge, n, t))
        for (phrase, _), r in zip(checks, rows):
            c.until(phrase)
            c.run(Create(r[0]), FadeIn(r[1], scale=0.8), FadeIn(r[2], shift=RIGHT * 0.1), rt=0.6)
        c.pad()
