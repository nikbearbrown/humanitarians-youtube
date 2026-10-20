"""scenes.py — Manim scenes for ab-testing-can-lie-to-you (cli-explainer).
5 Manim beats (B01, B04, B07, B08, B09); the other 7 render via Remotion.
Claude-skin palette: cream ground, warm ink, one terracotta accent. Here the accent
always marks the TEST group (the 16-card carousel), so the flip from "test sinks"
(B04) to "test wins" (B07) reads in the colour alone.
Scene classes must be declared as plain Scene subclasses named B0X_Name — run.sh finds them by regex.
No LaTeX (Text/Pango only) — axes are drawn by hand for the same reason.

THE RECEIPT: every simulated number on screen is parsed at render time from the real
script output in `py/*.out` (ACTUAL-CODE LAW) — nothing typed in by hand. The only
hand-typed numbers are the papers' own (12 → 16 cards, ~6%, 821,588 vs 815,482, > 30%),
each traced in FACTCHECK.md. Simulated numbers carry a "SIMULATION" tag.

Every scene carries the "Supriya" corner handle (PM requirement 4 / LOGO LAW) —
see `handle()`.

TIMING: DUR is read from beat_sheet.json — `actual_duration_s` once audio exists,
`estimated_duration_s` before. Narration cues are placed by the cue phrase's word
position in that beat's narration_text, scaled to DUR, so regenerated audio
re-times the scenes without hand edits. Never hand-trim an mp4.
"""
from manim import *
from pathlib import Path
import json
import re

# The reel folder holds the data (py/*.out) and the timing (beat_sheet.json). Normally
# that is this file's own folder; run.sh's Gate A/W pre-flights execute an ISOLATED COPY
# of scenes.py in a temp dir, so fall back to the reel's real location for those.
_REEL = Path("/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art/projects/2026-10-12-ab-testing-can-lie-to-you")
HERE = Path(__file__).resolve().parent
if not (HERE / "py").is_dir():
    HERE = _REEL
CREAM = "#FAF9F5"; INK = "#3D3929"; TERRACOTTA = "#D97757"
SEC = "#6B6357"; RULE = "#D9D4C7"; PALE = "#E8E3D6"
MONO = "PT Mono"

# ── data: the real script output ──────────────────────────────────────────────

def out_text(name):
    return (HERE / "py" / name).read_text()


def num(pattern, text):
    m = re.search(pattern, text)
    if not m:
        raise ValueError(f"pattern not in output: {pattern!r}")
    return m.group(1)


V1 = out_text("carousel_v1.out")
V2 = out_text("carousel_v2.out")
PK = out_text("peeking.out")

V1_CTRL = float(num(r"control\s+([\d.]+)", V1))
V1_TEST = float(num(r"test\s+([\d.]+)", V1))
V1_Z = num(r"z\s+(-?[\d.]+)", V1)
V1_P = num(r"p\s+(.+)", V1).strip()

V2_NC, V2_NT = (int(x) for x in re.search(r"split (\d+) vs (\d+)", V2).groups())
V2_SRM_P = num(r"SRM p\s+(\S+)", V2)
V2_CTRL = float(num(r"control\s+([\d.]+)", V2))
V2_TEST = float(num(r"test\s+([\d.]+)", V2))

PK_PEEK = float(num(r"peeking\s+([\d.]+)%", PK))
PK_ONCE = float(num(r"once\s+([\d.]+)%", PK))
PK_CURVE = [int(x) for x in num(r"by day (.+)", PK).split()]
PK_TESTS = 1000                                      # TESTS in py/peeking.py
assert abs(PK_CURVE[-1] * 100 / PK_TESTS - PK_PEEK) < 1e-9

# ── timing: from the beat sheet ───────────────────────────────────────────────

BEATS = {b["beat_id"]: b for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}


def dur(bid):
    b = BEATS[bid]
    return float(b.get("actual_duration_s") or b["estimated_duration_s"])


def _w(s):
    return s.strip(".,:;").lower()


def cue(bid, phrase):
    """Seconds into the beat where `phrase` starts, by word position in the narration."""
    words = BEATS[bid]["narration_text"].split()
    target = phrase.split()
    for i in range(len(words) - len(target) + 1):
        if [_w(w) for w in words[i:i + len(target)]] == [_w(t) for t in target]:
            return dur(bid) * i / len(words)
    raise ValueError(f"{bid}: cue phrase not in narration: {phrase!r}")


class Clock:
    """A beat's running clock. Scenes stay plain `(Scene)` subclasses — run.sh finds them
    by regex on the class line — and each opens with `c = Clock(self, "B0X")`.
    `until(phrase)` waits to that cue; `pad()` holds to the end of the beat's audio."""

    def __init__(self, scene, bid):
        self.s, self.bid, self.t = scene, bid, 0.0
        self.DUR = dur(bid)
        scene.camera.background_color = CREAM
        handle(scene)

    def run(self, *anims, rt=0.6):
        self.s.play(*anims, run_time=rt); self.t += rt

    def until(self, phrase):
        at = cue(self.bid, phrase)
        if at > self.t:
            self.s.wait(at - self.t); self.t = at

    def pad(self):
        self.s.wait(max(0.4, self.DUR - self.t - 0.2))


def handle(scene):
    """Visible author handle, lower-right inside the safe area, on from frame 0."""
    h = Text("Supriya", color=SEC, font_size=26, weight="BOLD").set_opacity(0.8)
    h.to_corner(DR, buff=0.9)
    scene.add(h)
    return h


# ── shared visuals ────────────────────────────────────────────────────────────

def sim_tag(fname):
    """Upper-left receipt: which output file, and that it is a simulation."""
    f = Text(fname, font=MONO, color=SEC, font_size=26)
    chip = Text("SIMULATION", font=MONO, color=TERRACOTTA, font_size=22, weight="BOLD")
    box = SurroundingRectangle(chip, color=TERRACOTTA, stroke_width=3, buff=0.1, corner_radius=0.06)
    g = VGroup(f, VGroup(box, chip)).arrange(RIGHT, buff=0.3)
    return g.to_corner(UL, buff=0.9)


def itext(s, size, color=SEC):
    """Italic Text built at 3× and scaled down — see source_line()."""
    return Text(s, color=color, font_size=size * 3, slant="ITALIC").scale(1 / 3)


def source_line(*lines, size=24):
    """Small italic citation. Built at 3× and scaled down: Pango drops word spacing in
    small italic Text (seen at 4K: "SRMsarethis"), and large-then-scale renders clean."""
    t = VGroup(*[itext(l, size) for l in lines])
    return t.arrange(DOWN, buff=0.08, aligned_edge=LEFT)


def carousel(n, width=5.9, h=2.6, x=-3.0, y=0.35):
    """A carousel strip: n rounded cards filling `width`. The 16-card version is the TEST."""
    gap = 0.08
    w = (width - gap * (n - 1)) / n
    col = TERRACOTTA if n == 16 else INK
    cards = VGroup(*[RoundedRectangle(corner_radius=min(0.08, w / 4), width=w, height=h,
                                      stroke_width=0, fill_color=col, fill_opacity=0.85)
                     for _ in range(n)]).arrange(RIGHT, buff=gap)
    frame = RoundedRectangle(corner_radius=0.15, width=width + 0.4, height=h + 0.4,
                             color=RULE, stroke_width=4)
    return VGroup(frame, cards.move_to(frame)).move_to([x, y, 0])


BASE_Y, BAR_W = -2.1, 1.9
UNIT = 0.85                                          # 1 click/user = 0.85 units tall


def bar(x, v, color, w=BAR_W):
    h = UNIT * v
    return Rectangle(width=w, height=h, stroke_width=0, fill_color=color,
                     fill_opacity=1).move_to([x, BASE_Y + h / 2, 0])


def bar_value(b, v, color):
    return Text(f"{v:.2f}", color=color, weight="BOLD", font_size=40).next_to(b, UP, buff=0.15)


def bar_name(x, name, size=32):
    t = Text(name, color=INK, font_size=size)
    return t.move_to([x, BASE_Y - 0.2 - t.height / 2, 0])


CTRL_X, TEST_X = -4.2, -1.6


def readout_bars(ctrl, test):
    """Control (ink) and test (terracotta) bars + values + names; returns (bars, extras)."""
    bc, bt = bar(CTRL_X, ctrl, INK), bar(TEST_X, test, TERRACOTTA)
    extras = VGroup(bar_value(bc, ctrl, INK), bar_value(bt, test, TERRACOTTA),
                    bar_name(CTRL_X, "control"), bar_name(TEST_X, "test"))
    return VGroup(bc, bt), extras


def axis():
    return Line([-5.7, BASE_Y, 0], [-0.1, BASE_Y, 0], color=RULE, stroke_width=4)


def unit_label():
    return itext("clicks per user", 26, SEC).move_to([(CTRL_X + TEST_X) / 2, BASE_Y - 1.0, 0])


RIGHT_X = 3.5                                        # centre of the right-hand text column


# ── B01 — PROBLEM ─────────────────────────────────────────────────────────────

class B01_DontShip(Scene):
    """PROBLEM — MSN went from 12 to 16 carousel cards; the test said 'significant drop'."""

    def construct(self):
        c = Clock(self, "B01")
        head = Text("MSN's carousel", color=INK, weight="BOLD", font_size=48).move_to([-3.0, 2.6, 0])
        twelve = carousel(12)
        n12 = Text("12 cards", font=MONO, color=SEC, font_size=30).next_to(twelve, DOWN, buff=0.3)
        c.run(Write(head), FadeIn(twelve, shift=RIGHT * 0.3), FadeIn(n12), rt=1.2)

        c.until("sixteen rotating cards")
        sixteen = carousel(16)
        n16 = Text("16 cards", font=MONO, color=TERRACOTTA, font_size=30, weight="BOLD").move_to(n12)
        c.run(ReplacementTransform(twelve, sixteen), ReplacementTransform(n12, n16), rt=1.2)

        c.until("They expected")
        hope = VGroup(Arrow(DOWN * 0.8, UP * 0.8, color=RULE, stroke_width=10, buff=0),
                      itext("expected: more clicks", 32, SEC)
                      ).arrange(RIGHT, buff=0.3).move_to([RIGHT_X, 2.2, 0])
        c.run(FadeIn(hope, shift=UP * 0.2), rt=0.7)

        c.until("The test said")
        drop = VGroup(Arrow(UP * 0.8, DOWN * 0.8, color=INK, stroke_width=10, buff=0),
                      VGroup(Text("significant drop", color=INK, weight="BOLD", font_size=40),
                             Text("p < 0.05", font=MONO, color=INK, font_size=30)
                             ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
                      ).arrange(RIGHT, buff=0.3).move_to([RIGHT_X, 0.4, 0])
        c.run(FadeIn(drop, shift=DOWN * 0.2), hope.animate.set_opacity(0.35), rt=0.8)

        c.until("On that result")
        card = RoundedRectangle(corner_radius=0.2, width=4.6, height=1.5, color=INK, stroke_width=4,
                                fill_color=WHITE, fill_opacity=1).move_to([RIGHT_X, -1.45, 0])
        verdict = Text("Don't ship.", color=INK, weight="BOLD", font_size=56).move_to(card)
        c.run(FadeIn(card, shift=UP * 0.2), Write(verdict), rt=0.9)

        c.until("This is real")
        src = source_line("Fabijan et al., KDD 2019", "MSN carousel experiment", size=28)
        src.move_to([-3.0, -2.75, 0])
        c.run(FadeIn(src, shift=UP * 0.1), rt=0.6)
        c.pad()


# ── B04 — OUTPUT, cycle 1 ─────────────────────────────────────────────────────

class B04_LooksWorse(Scene):
    """OUTPUT, cycle 1 — the misleading readout: control 3.89 vs test 3.20."""

    def construct(self):
        c = Clock(self, "B04")
        c.run(FadeIn(sim_tag("carousel_v1.out")), Create(axis()), FadeIn(unit_label()), rt=0.6)
        bars, extras = readout_bars(V1_CTRL, V1_TEST)

        c.until("Control")
        c.run(GrowFromEdge(bars[0], DOWN), FadeIn(extras[2]), rt=0.8)
        c.run(FadeIn(extras[0], shift=UP * 0.1), rt=0.3)
        c.until("Test")
        c.run(GrowFromEdge(bars[1], DOWN), FadeIn(extras[3]), rt=0.8)
        c.run(FadeIn(extras[1], shift=UP * 0.1), rt=0.3)

        c.until("A z score")
        stats = VGroup(Text(f"z  {V1_Z.replace('-', '−')}", font=MONO, color=INK, font_size=52, weight="BOLD"),
                       Text(f"p  {V1_P}", font=MONO, color=INK, font_size=40)
                       ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to([RIGHT_X, 1.4, 0])
        c.run(FadeIn(stats, shift=UP * 0.1), rt=0.6)

        c.until("Significant")
        worse = Text("Significant. Worse.", color=INK, weight="BOLD", font_size=50).move_to([RIGHT_X, -0.3, 0])
        c.run(Write(worse), rt=0.8)

        c.until("Don't ship")
        card = RoundedRectangle(corner_radius=0.2, width=4.6, height=1.4, color=INK, stroke_width=4,
                                fill_color=WHITE, fill_opacity=1).move_to([RIGHT_X, -1.8, 0])
        verdict = Text("Don't ship.", color=INK, weight="BOLD", font_size=54).move_to(card)
        c.run(FadeIn(card, shift=UP * 0.2), Write(verdict), rt=0.7)
        c.pad()


# ── B07 — OUTPUT, cycle 2 ─────────────────────────────────────────────────────

class B07_TheFlip(Scene):
    """OUTPUT, cycle 2 — the split is off (SRM), then the bars flip once the filter is fixed.
    Flag C (approved): the paper's own real SRM example as a source line."""

    def construct(self):
        c = Clock(self, "B07")
        c.run(FadeIn(sim_tag("carousel_v2.out")), rt=0.4)

        # Phase 1 — the split. Two user counts; the missing users are the story.
        def count_row(label, n, col, y):
            return VGroup(Text(label, color=INK, font_size=34),
                          Text(f"{n:,}", font=MONO, color=col, font_size=64, weight="BOLD")
                          ).arrange(RIGHT, buff=0.5).move_to([-3.0, y, 0])
        r1 = count_row("control", V2_NC, INK, 0.9)
        r2 = count_row("test", V2_NT, TERRACOTTA, -0.5)
        r2[0].align_to(r1[0], LEFT); r2[1].align_to(r1[1], RIGHT)
        head = itext("users after the bot filter", 32, SEC).move_to([-3.0, 2.0, 0])
        c.run(FadeIn(head), FadeIn(r1), FadeIn(r2), rt=0.8)

        c.until("three thousand users short")
        miss = Text(f"−{V2_NC - V2_NT:,} missing", font=MONO, color=TERRACOTTA, font_size=44,
                    weight="BOLD").next_to(r2, DOWN, buff=0.45).align_to(r2[1], RIGHT)
        c.run(FadeIn(miss, shift=UP * 0.1), Indicate(r2[1], color=TERRACOTTA, scale_factor=1.06), rt=0.8)

        c.until("The odds")
        p = float(V2_SRM_P)
        odds = VGroup(Text(f"SRM p  {V2_SRM_P}", font=MONO, color=INK, font_size=48, weight="BOLD"),
                      Text(f"≈ {round(p * 1e6)} in a million by chance", color=INK, font_size=34)
                      ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to([RIGHT_X, 1.9, 0])
        c.run(FadeIn(odds, shift=UP * 0.1), rt=0.7)

        c.until("That's a sample ratio mismatch")
        srm = Text("Sample ratio mismatch.", color=TERRACOTTA, weight="BOLD", font_size=38).move_to([RIGHT_X - 0.1, 0.7, 0])
        src = source_line("Real SRMs are this subtle — Fabijan et al.'s example:",
                          "821,588 vs 815,482 users, < 1 in 500k by chance.", size=18)
        src.move_to([RIGHT_X - 0.2, -2.05, 0])
        c.run(Write(srm), FadeIn(src, shift=UP * 0.1), rt=0.9)

        # Phase 2 — fix the filter: the readout flips.
        c.until("Fix the filter")
        bars, extras = readout_bars(V2_CTRL, V2_TEST)
        ghost = VGroup(bar(CTRL_X, V1_CTRL, PALE), bar(TEST_X, V1_TEST, PALE))
        ax, ul = axis(), unit_label()
        c.run(FadeOut(VGroup(head, r1, r2, miss)), FadeIn(ax), FadeIn(ul), FadeIn(ghost), rt=0.6)
        c.run(GrowFromEdge(bars[0], DOWN), GrowFromEdge(bars[1], DOWN), FadeIn(extras[2:]), rt=1.0)
        c.run(FadeIn(extras[0], shift=UP * 0.1), FadeIn(extras[1], shift=UP * 0.1), rt=0.4)

        c.until("The loss was a win")
        flip = VGroup(Arrow(DOWN * 0.7, UP * 0.7, color=TERRACOTTA, stroke_width=10, buff=0),
                      Text("The loss was a win.", color=TERRACOTTA, weight="BOLD", font_size=44)
                      ).arrange(RIGHT, buff=0.3).move_to([RIGHT_X, -0.6, 0])
        c.run(FadeOut(ghost), FadeIn(flip, shift=UP * 0.2), rt=0.8)
        c.pad()


# ── B08 — SECOND LIE: PEEKING ─────────────────────────────────────────────────

class B08_Peeking(Scene):
    """Peeking, one beat — 1,000 A/A tests, false winners by day vs the 5% line."""
    X0, X1, Y0, Y1 = -5.2, 1.6, -2.15, 1.95          # plot box
    YMAX = 30.0                                      # % at the top of the plot

    def px(self, day):                               # day 1..20
        return self.X0 + (day - 1) / 19 * (self.X1 - self.X0)

    def py(self, pct):
        return self.Y0 + pct / self.YMAX * (self.Y1 - self.Y0)

    def construct(self):
        c = Clock(self, "B08")
        head = Text("The second lie: peeking", color=INK, weight="BOLD", font_size=46).to_edge(UP, buff=0.75)
        c.run(Write(head), rt=0.9)

        c.until("I ran a thousand")
        tag = sim_tag("peeking.out").to_corner(DL, buff=0.9).shift(RIGHT * 0.3)
        sub = itext("1,000 A/A tests · both groups identical", 28, SEC).next_to(head, DOWN, buff=0.2)
        xa = Line([self.X0, self.Y0, 0], [self.X1, self.Y0, 0], color=RULE, stroke_width=4)
        ya = Line([self.X0, self.Y0, 0], [self.X0, self.Y1, 0], color=RULE, stroke_width=4)
        xt = VGroup(*[Text(str(d), font=MONO, color=SEC, font_size=22).move_to([self.px(d), self.Y0 - 0.3, 0])
                      for d in (1, 5, 10, 15, 20)])
        xl = Text("day", color=SEC, font_size=24).move_to([self.X1 + 0.6, self.Y0 - 0.3, 0])
        yt = VGroup(*[Text(f"{p}%", font=MONO, color=SEC, font_size=22).next_to([self.X0, self.py(p), 0], LEFT, buff=0.15)
                      for p in (0, 10, 20, 30)])
        five = DashedLine([self.X0, self.py(5), 0], [self.X1, self.py(5), 0], color=SEC, stroke_width=3)
        five_l = Text("5% — what you signed up for", color=SEC, font_size=22).next_to(five, DOWN, buff=0.1).align_to(five, LEFT).shift(RIGHT * 1.6)
        c.run(FadeIn(sub), Create(xa), Create(ya), FadeIn(xt), FadeIn(xl), FadeIn(yt), FadeIn(tag), rt=0.9)
        c.run(Create(five), FadeIn(five_l), rt=0.5)

        # The curve: share of tests that have "won" at least once by each day.
        pts = [[self.px(d + 1), self.py(n * 100 / PK_TESTS), 0] for d, n in enumerate(PK_CURVE)]
        curve = VMobject(color=TERRACOTTA, stroke_width=7).set_points_as_corners(pts)
        c.until("checking every day")
        span = max(1.5, cue("B08", "and a quarter") - c.t)
        c.run(Create(curve, rate_func=linear), rt=span)
        end = Dot(pts[-1], color=TERRACOTTA, radius=0.1)
        peek_l = Text(f"{PK_PEEK:.1f}% crown a winner", color=TERRACOTTA, weight="BOLD", font_size=34
                      ).next_to(end, UP, buff=0.25).align_to(end, RIGHT)
        c.run(FadeIn(end), FadeIn(peek_l, shift=LEFT * 0.1), rt=0.5)

        c.until("Look once")
        once = Dot([self.px(20), self.py(PK_ONCE), 0], color=INK, radius=0.1)
        once_l = Text(f"look once: {PK_ONCE:.1f}%", color=INK, weight="BOLD", font_size=30
                      ).next_to(once, RIGHT, buff=0.2).shift(DOWN * 0.15)
        c.run(FadeIn(once, scale=0.5), FadeIn(once_l), rt=0.6)

        c.until("Researchers at Stanford")
        box = RoundedRectangle(corner_radius=0.15, width=3.9, height=1.9, color=INK, stroke_width=4,
                               fill_color=WHITE, fill_opacity=1).move_to([4.3, 1.0, 0])
        big = VGroup(Text("checking nonstop", color=INK, font_size=30),
                     Text("> 30%", color=INK, weight="BOLD", font_size=60)).arrange(DOWN, buff=0.12).move_to(box)
        src = source_line("Johari, Pekelis & Walsh, 2015", "(continuous monitoring, 10,000 obs.)", size=18)
        src.next_to(box, DOWN, buff=0.2).align_to(box, LEFT)
        c.run(FadeIn(box, shift=UP * 0.2), FadeIn(big), FadeIn(src), rt=0.8)
        c.pad()


# ── B09 — SUMMARY ─────────────────────────────────────────────────────────────

class B09_ThreeChecks(Scene):
    """SUMMARY — MSN resolved (flipped, shipped), ~6% of experiments, three checks."""

    def construct(self):
        c = Clock(self, "B09")
        car = carousel(16, width=4.6, h=1.0, x=-3.6, y=2.3)
        c.run(FadeIn(car, shift=RIGHT * 0.2), rt=0.7)

        c.until("The bot filter")
        why = itext("the bot filter dropped its most engaged users", 28, SEC).next_to(car, DOWN, buff=0.25).align_to(car, LEFT)
        c.run(FadeIn(why, shift=UP * 0.1), rt=0.6)

        c.until("Once that was fixed")
        up = VGroup(Arrow(DOWN * 0.6, UP * 0.6, color=TERRACOTTA, stroke_width=10, buff=0),
                    Text("flipped. shipped.", color=TERRACOTTA, weight="BOLD", font_size=40)
                    ).arrange(RIGHT, buff=0.25).next_to(car, RIGHT, buff=0.5)
        c.run(FadeIn(up, shift=UP * 0.2), rt=0.7)

        c.until("about six percent")
        six = VGroup(Text("~6%", color=INK, weight="BOLD", font_size=60),
                     VGroup(Text("of Microsoft experiments", color=INK, font_size=28),
                            itext("had an SRM · Fabijan et al. 2019", 24, SEC)
                            ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
                     ).arrange(RIGHT, buff=0.3).move_to([2.9, 0.35, 0])
        c.run(FadeIn(six, shift=UP * 0.1), rt=0.6)

        checks = [("check the split first", "Check the split first."),
                  ("fix your sample size", "Fix the sample size in advance."),
                  ("if you must peek", "Must peek? Use a test built for it.")]
        rows = VGroup()
        for i, (_, txt) in enumerate(checks, 1):
            y = -0.8 - (i - 1) * 0.92
            n = Text(str(i), color=TERRACOTTA, weight="BOLD", font_size=44).move_to([-5.0, y, 0])
            badge = Circle(radius=0.36, color=TERRACOTTA, stroke_width=5).move_to(n)
            t = Text(txt, color=INK, font_size=42).move_to([-4.4, y, 0], aligned_edge=LEFT)
            rows.add(VGroup(badge, n, t))
        for (phrase, _), r in zip(checks, rows):
            c.until(phrase)
            c.run(Create(r[0]), FadeIn(r[1], scale=0.8), FadeIn(r[2], shift=RIGHT * 0.15), rt=0.6)
        c.pad()
