"""scenes.py — portrait (9:16) Manim scenes for correlation-is-not-causation/short.
Full-length short (no beats cut): all 5 Manim beats re-laid-out for portrait —
B01, B04, B07, B08, B09. Not shrunk copies of the landscape scenes: the portrait
frame is narrow in x (frame_width=4.5, Gate B safe ±1.95) and unchanged in y
(frame_height=8.0, safe ±3.4), so every layout is restacked vertically. The bar
charts (B04, B07) turn horizontal so they fill a tall frame.

DATA + TIMING come from the landscape ../scenes.py (imported, not copied): the
same numbers parsed from ../sql/*.out at render time, the same measured audio
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
_REEL = Path("/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art/projects/2026-10-05-correlation-is-not-causation")
_parent = Path(__file__).resolve().parent.parent / "scenes.py"
if not _parent.is_file() or not (_parent.parent / "sql").is_dir():
    _parent = _REEL / "scenes.py"
_spec = importlib.util.spec_from_file_location("landscape_scenes", _parent)
L = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(L)

CREAM, INK, TERRACOTTA, SEC, RULE, PALE, MONO = L.CREAM, L.INK, L.TERRACOTTA, L.SEC, L.RULE, L.PALE, L.MONO
SURGERY, KEYHOLE, Q1, Q2, N_PER_ARM = L.SURGERY, L.KEYHOLE, L.Q1, L.Q2, L.N_PER_ARM
ARM_NAME = L.ARM_NAME
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


# ── shared portrait visuals ───────────────────────────────────────────────────

COLS, DOT_GAP, DOT_R = 14, 0.1, 0.036               # 14 × 25 = 350 dots per arm
ARM_X = {SURGERY: -0.95, KEYHOLE: 0.95}
DOT_BASE_Y = -0.35                                  # rows span y -0.35 … 2.05


def patient_column(x):
    dots = VGroup(*[Dot(radius=DOT_R, color=SEC) for _ in range(N_PER_ARM)])
    for k, d in enumerate(dots):
        r, c = divmod(k, COLS)
        d.move_to([x + (c - (COLS - 1) / 2) * DOT_GAP, DOT_BASE_Y + r * DOT_GAP, 0])
    return dots


def arm_label(name, dots):
    return Text(name, color=INK, weight="BOLD", font_size=22).next_to(dots, UP, buff=0.18)


BAR_X0, BAR_L100 = -1.9, 2.8                        # horizontal bars: 100% = 2.8 units


def hbar(y, pct, color, h=0.55):
    w = BAR_L100 * pct / 100
    return Rectangle(width=w, height=h, stroke_width=0, fill_color=color,
                     fill_opacity=1).move_to([BAR_X0 + w / 2, y, 0])


def hbar_value(b, pct, color, size=26):
    return Text(f"{pct:.1f}%", color=color, weight="BOLD", font_size=size).next_to(b, RIGHT, buff=0.1)


def hbar_name(b, name, size=18):
    """Arm name inside the bar's left end, cream on the bar colour."""
    t = Text(name, color=CREAM, weight="BOLD", font_size=size)
    return t.move_to(b.get_left() + RIGHT * (0.1 + t.width / 2))


# ── B01 — PROBLEM ─────────────────────────────────────────────────────────────

class B01_PickOne(Scene):
    """PROBLEM — two treatments, 350 patients each, a real 1986 study: you pick one."""

    def construct(self):
        c = Clock(self, "B01")
        head = Text("Which one works?", color=INK, weight="BOLD", font_size=32).move_to([0, 3.1, 0])
        c.run(Write(head), rt=1.0)

        c.until("open surgery")
        cols = {}
        for arm in (SURGERY, KEYHOLE):
            if arm == KEYHOLE:
                c.until("and a keyhole procedure")
            dots = patient_column(ARM_X[arm])
            lbl = arm_label(ARM_NAME[arm], dots)
            c.run(FadeIn(lbl), LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.004), rt=1.1)
            cols[arm] = (dots, lbl)

        c.until("Three hundred fifty")
        counts = VGroup(*[Text(f"{N_PER_ARM} patients", font=MONO, color=SEC, font_size=14)
                          .next_to(cols[a][0], DOWN, buff=0.15) for a in (SURGERY, KEYHOLE)])
        c.run(FadeIn(counts, shift=UP * 0.05), rt=0.5)

        c.until("The data is real")
        src = lines("Charig et al.", "British Medical Journal, 1986", buff=0.08,
                    color=SEC, font_size=20, slant="ITALIC").move_to([0, -1.25, 0])
        c.run(FadeIn(src, shift=UP * 0.05), rt=0.6)

        c.until("Say you run")
        card = RoundedRectangle(corner_radius=0.14, width=3.7, height=1.0, color=INK, stroke_width=3,
                                fill_color=WHITE, fill_opacity=1).move_to([0, -2.35, 0])
        q = Text("You pick one.", color=INK, weight="BOLD", font_size=36).move_to(card)
        c.run(FadeIn(card, shift=UP * 0.1), Write(q), rt=0.9)
        c.until("You have to")
        c.run(*[Indicate(cols[a][1], color=INK, scale_factor=1.08) for a in (SURGERY, KEYHOLE)], rt=0.8)
        c.pad()


# ── B04 — OUTPUT, cycle 1 ─────────────────────────────────────────────────────

B04_Y = {KEYHOLE: 0.75, SURGERY: -0.55}             # bar centres; B07 reuses them as its ghost


class B04_KeyholeWins(Scene):
    """OUTPUT, cycle 1 — the misleading answer: keyhole 82.6 vs surgery 78.0 (horizontal)."""

    def construct(self):
        c = Clock(self, "B04")
        k, s = Q1[KEYHOLE][1], Q1[SURGERY][1]
        ck, cs = L.winner_color(k, s)
        tag = Text("q1_by_treatment.out", font=MONO, color=SEC, font_size=16).move_to([BAR_X0, 1.65, 0],
                                                                                      aligned_edge=LEFT)
        axis = Line([BAR_X0, -1.15, 0], [BAR_X0, 1.35, 0], color=RULE, stroke_width=3)
        c.run(FadeIn(tag), Create(axis), rt=0.5)

        for arm, pct, col in ((KEYHOLE, k, ck), (SURGERY, s, cs)):
            if arm == SURGERY:
                c.until("Open surgery")
            b = hbar(B04_Y[arm], pct, col, h=0.8)
            c.run(GrowFromEdge(b, LEFT), rt=0.9)
            c.run(FadeIn(hbar_name(b, ARM_NAME[arm], 22)), FadeIn(hbar_value(b, pct, col, 30), shift=RIGHT * 0.05), rt=0.3)

        c.until("Keyhole wins")
        gap = round(k - s, 1)
        win = Text("Keyhole wins?", color=INK, weight="BOLD", font_size=40).move_to([0, 3.0, 0])
        gl = Text(f"by {gap} points", color=TERRACOTTA, weight="BOLD", font_size=30).next_to(win, DOWN, buff=0.2)
        c.run(Write(win), FadeIn(gl, shift=UP * 0.05), rt=0.9)

        c.until("Most dashboards")
        stop = lines("most dashboards", "stop here", buff=0.1, color=SEC, font_size=28,
                     slant="ITALIC").move_to([0, -2.2, 0])
        c.run(FadeIn(stop, shift=UP * 0.05), rt=0.6)
        c.pad()


# ── B07 — OUTPUT, cycle 2 ─────────────────────────────────────────────────────

class B07_TheFlip(Scene):
    """OUTPUT, cycle 2 — split by stone size, surgery wins both; B04's overall bars stay
    as a pale reference strip at the bottom so the reversal reads in one frame."""
    GROUP_Y = {"small": 1.7, "large": -0.35}         # group label y; bars stack beneath
    SIZE_LABEL = {"small": "Small stones (<2 cm)", "large": "Large (≥2 cm or multiple)"}
    NAME = {SURGERY: "Surgery", KEYHOLE: "Keyhole"}

    def construct(self):
        c = Clock(self, "B07")
        tag = Text("q2_by_size.out", font=MONO, color=SEC, font_size=16).move_to([BAR_X0, 2.3, 0],
                                                                                 aligned_edge=LEFT)
        # Open on B04's overall bars (pale), then park them at the bottom as "overall".
        ghost = VGroup(hbar(B04_Y[KEYHOLE], Q1[KEYHOLE][1], PALE, 0.8),
                       hbar(B04_Y[SURGERY], Q1[SURGERY][1], PALE, 0.8))
        c.run(FadeIn(tag), FadeIn(ghost), rt=0.4)
        strip_y = {KEYHOLE: -2.45, SURGERY: -2.8}
        strip = VGroup(*[hbar(strip_y[a], Q1[a][1], PALE, 0.26) for a in (KEYHOLE, SURGERY)])
        strip_lbl = Text("overall", color=SEC, font_size=16, slant="ITALIC").next_to(strip, UP, buff=0.08,
                                                                                   aligned_edge=LEFT)
        strip_txt = VGroup(*[Text(f"{ARM_NAME[a]} {Q1[a][1]:.1f}%", color=SEC, font_size=14)
                             .move_to(strip[i].get_left() + RIGHT * 0.08, aligned_edge=LEFT)
                             for i, a in enumerate((KEYHOLE, SURGERY))])
        c.run(Transform(ghost, strip), FadeIn(strip_lbl), rt=0.6)
        self.add(strip_txt)

        for size, phrase in (("small", "Small stones"), ("large", "Large stones")):
            c.until(phrase)
            gy = self.GROUP_Y[size]
            s, k = Q2[(size, SURGERY)][1], Q2[(size, KEYHOLE)][1]
            cs, ck = L.winner_color(s, k)
            glabel = Text(self.SIZE_LABEL[size], color=INK, weight="BOLD", font_size=22).move_to(
                [BAR_X0, gy, 0], aligned_edge=LEFT)
            bars = []
            for i, (arm, pct, col) in enumerate(((SURGERY, s, cs), (KEYHOLE, k, ck))):
                b = hbar(gy - 0.55 - i * 0.7, pct, col, h=0.6)
                bars.append(VGroup(b, hbar_name(b, self.NAME[arm], 20), hbar_value(b, pct, col, 26)))
            c.run(FadeIn(glabel), GrowFromEdge(bars[0][0], LEFT), GrowFromEdge(bars[1][0], LEFT), rt=1.0)
            c.run(*[FadeIn(m) for bg in bars for m in bg[1:]], rt=0.3)

        c.until("Open surgery wins both")
        verdict = lines("Open surgery", "wins both.", buff=0.08, color=TERRACOTTA, weight="BOLD",
                        font_size=34).move_to([0, 2.92, 0])
        c.run(Write(verdict), rt=1.0)
        c.pad()


# ── B08 — MECHANISM ───────────────────────────────────────────────────────────

class B08_WhoGotWhat(Scene):
    """MECHANISM — B01's dots re-sorted by stone size; stone size → treatment & outcome."""

    def construct(self):
        c = Clock(self, "B08")
        cols = {}
        for arm in (SURGERY, KEYHOLE):
            dots = patient_column(ARM_X[arm])
            cols[arm] = (dots, arm_label(ARM_NAME[arm], dots))
            self.add(dots, cols[arm][1])
        head = Text("Who got which stones?", color=INK, weight="BOLD", font_size=26).move_to([0, 3.15, 0])
        c.run(FadeIn(head), rt=0.5)

        c.until("The hard cases")
        for arm in (SURGERY, KEYHOLE):
            if arm == KEYHOLE:
                c.until("Keyhole got")
            n_large, n_small = Q2[("large", arm)][0], Q2[("small", arm)][0]
            dots, _ = cols[arm]
            c.run(*[d.animate.set_color(INK if i < n_large else PALE) for i, d in enumerate(dots)], rt=1.2)
            lab = VGroup(Text(f"{n_large} large", font=MONO, color=INK, font_size=15, weight="BOLD"),
                         Text(f"{n_small} small", font=MONO, color=SEC, font_size=15)
                         ).arrange(DOWN, buff=0.05).next_to(dots, DOWN, buff=0.12)
            c.run(FadeIn(lab, shift=UP * 0.05), rt=0.4)

        key = VGroup(VGroup(Dot(radius=0.05, color=INK), Text("large (≥2 cm or multiple)", color=INK, font_size=15)
                            ).arrange(RIGHT, buff=0.08),
                     VGroup(Dot(radius=0.05, color=PALE).set_stroke(SEC, 1), Text("small (<2 cm)", color=SEC, font_size=15)
                            ).arrange(RIGHT, buff=0.08)).arrange(DOWN, buff=0.06, aligned_edge=LEFT).move_to([0, -1.22, 0])
        c.run(FadeIn(key), rt=0.4)

        c.until("Stone size drove")

        def node(txt, pos, col=INK, w=1.7):
            box = RoundedRectangle(corner_radius=0.1, width=w, height=0.42, color=col, stroke_width=3,
                                   fill_color=WHITE, fill_opacity=1).move_to(pos)
            return VGroup(box, Text(txt, color=col, weight="BOLD", font_size=18).move_to(box))
        size = node("stone size", [0, -1.72, 0], TERRACOTTA)
        treat = node("treatment", [-0.95, -2.52, 0])
        outc = node("outcome", [0.95, -2.52, 0])
        a1 = Arrow(size.get_bottom(), treat.get_top(), color=TERRACOTTA, stroke_width=4, buff=0.04,
                   max_tip_length_to_length_ratio=0.3)
        a2 = Arrow(size.get_bottom(), outc.get_top(), color=TERRACOTTA, stroke_width=4, buff=0.04,
                   max_tip_length_to_length_ratio=0.3)
        c.run(FadeIn(size, shift=DOWN * 0.05), rt=0.5)
        c.run(GrowArrow(a1), FadeIn(treat), rt=0.6)
        c.run(GrowArrow(a2), FadeIn(outc), rt=0.6)

        c.until("The overall number")
        moral = lines("the overall number measured", "the patients, not the procedure", buff=0.05,
                      edge=LEFT, color=INK, font_size=16, slant="ITALIC").move_to([BAR_X0, -3.08, 0],
                                                                                aligned_edge=LEFT)
        c.run(FadeIn(moral, shift=UP * 0.05), rt=0.8)
        c.pad()


# ── B09 — SUMMARY ─────────────────────────────────────────────────────────────

class B09_ThreeQuestions(Scene):
    """SUMMARY — real correlation, wrong cause; three questions; the observational caveat."""

    def construct(self):
        c = Clock(self, "B09")
        head = lines("A real correlation.", "Not the cause.", buff=0.08, edge=LEFT, color=INK,
                     weight="BOLD", font_size=32).move_to([BAR_X0, 2.85, 0], aligned_edge=LEFT)
        c.run(Write(head), rt=1.2)
        c.until("The gap came")
        sub = Text("the gap came from the patient mix", color=SEC, font_size=19,
                   slant="ITALIC").next_to(head, DOWN, buff=0.2, aligned_edge=LEFT)
        c.run(FadeIn(sub, shift=UP * 0.05), rt=0.6)

        qs = [("who got which", ("Who got which", "option?")),
              ("what else drives", ("What else drives", "the outcome?")),
              ("does the gap survive", ("Does the gap", "survive a split?"))]
        rows = VGroup()
        for i, (_, q) in enumerate(qs, 1):
            y = 1.05 - (i - 1) * 1.15
            badge = Circle(radius=0.27, color=TERRACOTTA, stroke_width=4).move_to([BAR_X0 + 0.27, y, 0])
            num = Text(str(i), color=TERRACOTTA, weight="BOLD", font_size=30).move_to(badge)
            txt = lines(*q, buff=0.06, edge=LEFT, color=INK, font_size=26).move_to(
                [BAR_X0 + 0.75, y, 0], aligned_edge=LEFT)
            rows.add(VGroup(badge, num, txt))
        for (phrase, _), r in zip(qs, rows):
            c.until(phrase)
            c.run(Create(r[0]), FadeIn(r[1], scale=0.8), FadeIn(r[2], shift=RIGHT * 0.05), rt=0.6)

        c.until("And even the split")
        rule = Line([BAR_X0, -2.05, 0], [1.6, -2.05, 0], color=RULE, stroke_width=2)
        cav1 = Text("A split is still observational.", color=INK, font_size=21, slant="ITALIC"
                    ).move_to([BAR_X0, -2.35, 0], aligned_edge=LEFT)
        c.run(GrowFromEdge(rule, LEFT), FadeIn(cav1), rt=0.7)
        c.until("Only randomizing")
        cav2 = lines("Only randomizing rules out", "what nobody measured.", buff=0.05, edge=LEFT,
                     color=SEC, font_size=19, slant="ITALIC").next_to(cav1, DOWN, buff=0.12, aligned_edge=LEFT)
        c.run(FadeIn(cav2, shift=UP * 0.05), rt=0.7)
        c.pad()
