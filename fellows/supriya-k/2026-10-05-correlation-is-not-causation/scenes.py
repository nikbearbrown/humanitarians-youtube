"""scenes.py — Manim scenes for correlation-is-not-causation (cli-explainer).
5 Manim beats (B01, B04, B07, B08, B09); the other 7 render via Remotion.
Claude-skin palette: cream ground, warm ink, one terracotta accent. Here the accent
always marks "the winner", so the flip from keyhole (B04) to surgery (B07) is
visible in the colour alone.
Scene classes must be declared as plain Scene subclasses named B0X_Name — run.sh finds them by regex.
No LaTeX (Text/Pango only).

THE RECEIPT: every number on screen is parsed at render time from the real query
output in `sql/*.out` (ACTUAL-CODE LAW) — nothing is typed in by hand. If the
data or queries change, re-run them and re-render; the scenes follow.

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
import numpy as np

# The reel folder holds the data (sql/*.out) and the timing (beat_sheet.json). Normally
# that is this file's own folder; run.sh's Gate A/W pre-flights execute an ISOLATED COPY
# of scenes.py in a temp dir, so fall back to the reel's real location for those.
_REEL = Path("/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art/projects/2026-10-05-correlation-is-not-causation")
HERE = Path(__file__).resolve().parent
if not (HERE / "sql").is_dir():
    HERE = _REEL
CREAM = "#FAF9F5"; INK = "#3D3929"; TERRACOTTA = "#D97757"
SEC = "#6B6357"; RULE = "#D9D4C7"; PALE = "#E8E3D6"
MONO = "PT Mono"

SURGERY, KEYHOLE = "open surgery", "keyhole (PCNL)"
SIZE_LABEL = {"small": "Small stones (<2 cm)", "large": "Large (≥2 cm or multiple)"}

# ── data: the real query output ───────────────────────────────────────────────

def read_out(name):
    """Parse a sqlite3 `-header -column` .out file into a list of dicts."""
    lines = [l for l in (HERE / "sql" / name).read_text().splitlines() if l.strip()]
    rule = lines[1]                                   # the "----  ----" line gives column spans
    spans, i = [], 0
    while i < len(rule):
        if rule[i] == "-":
            j = i
            while j < len(rule) and rule[j] == "-":
                j += 1
            spans.append((i, j)); i = j
        else:
            i += 1
    cut = lambda l: [l[a:(spans[k + 1][0] if k + 1 < len(spans) else None)].strip()
                     for k, (a, _) in enumerate(spans)]
    head = cut(lines[0])
    return [dict(zip(head, cut(l))) for l in lines[2:]]


Q1 = {r["treatment"]: (int(r["patients"]), float(r["success_pct"])) for r in read_out("q1_by_treatment.out")}
Q2 = {(r["stone_size"], r["treatment"]): (int(r["patients"]), float(r["success_pct"]))
      for r in read_out("q2_by_size.out")}
N_PER_ARM = Q1[SURGERY][0]                            # 350 — both arms are the same size
assert Q1[KEYHOLE][0] == N_PER_ARM

# ── timing: from the beat sheet ───────────────────────────────────────────────

BEATS = {b["beat_id"]: b for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}


def dur(bid):
    b = BEATS[bid]
    return float(b.get("actual_duration_s") or b["estimated_duration_s"])


def cue(bid, phrase):
    """Seconds into the beat where `phrase` starts, by word position in the narration."""
    words = BEATS[bid]["narration_text"].split()
    target = phrase.split()
    for i in range(len(words) - len(target) + 1):
        if [w.strip(".,:;") for w in words[i:i + len(target)]] == [t.strip(".,:;") for t in target]:
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

COLS, DOT_GAP, DOT_R = 14, 0.2, 0.068               # 14 × 25 = 350 dots per arm
ARM_X = {SURGERY: -4.6, KEYHOLE: -1.2}
ARM_NAME = {SURGERY: "Open surgery", KEYHOLE: "Keyhole"}


def patient_column(x):
    """350 patient dots, filled bottom-up, row-major."""
    dots = VGroup(*[Dot(radius=DOT_R, color=SEC) for _ in range(N_PER_ARM)])
    rows = N_PER_ARM // COLS
    for k, d in enumerate(dots):
        r, c = divmod(k, COLS)
        d.move_to([x + (c - (COLS - 1) / 2) * DOT_GAP, -2.4 + r * DOT_GAP, 0])
    assert rows * COLS == N_PER_ARM
    return dots


def arm_label(name, dots):
    return Text(name, color=INK, weight="BOLD", font_size=34).next_to(dots, UP, buff=0.3)


BASE_Y, BAR_H100, BAR_W = -2.0, 4.3, 1.15            # 100% = 4.3 units tall


def bar(x, pct, color, w=BAR_W):
    h = BAR_H100 * pct / 100
    return Rectangle(width=w, height=h, stroke_width=0, fill_color=color,
                     fill_opacity=1).move_to([x, BASE_Y + h / 2, 0])


def bar_value(b, pct, color):
    return Text(f"{pct:.1f}%", color=color, weight="BOLD", font_size=38).next_to(b, UP, buff=0.15)


def bar_name(x, name, size=28):
    """`name` may be a tuple of lines; each is its own Text (Gate W measures per Text)."""
    names = name if isinstance(name, tuple) else (name,)
    t = VGroup(*[Text(n, color=INK, font_size=size) for n in names]).arrange(DOWN, buff=0.08)
    return t.move_to([x, BASE_Y - 0.15 - t.height / 2, 0])


def winner_color(a, b):
    return (TERRACOTTA, INK) if a > b else (INK, TERRACOTTA)


# ── B01 — PROBLEM ─────────────────────────────────────────────────────────────

class B01_PickOne(Scene):
    """PROBLEM — two treatments, 350 patients each, a real 1986 study: you pick one."""

    def construct(self):
        c = Clock(self, "B01")
        head = VGroup(Text("Two treatments.", color=INK, weight="BOLD", font_size=46),
                      Text("Which one works?", color=INK, weight="BOLD", font_size=46)
                      ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to([3.4, 2.3, 0])
        c.run(Write(head), rt=1.2)

        c.until("open surgery")
        cols = {}
        for arm in (SURGERY, KEYHOLE):
            if arm == KEYHOLE:
                c.until("and a keyhole procedure")
            dots = patient_column(ARM_X[arm])
            lbl = arm_label(ARM_NAME[arm], dots)
            c.run(FadeIn(lbl), LaggedStart(*[FadeIn(d, scale=0.5) for d in dots],
                                              lag_ratio=0.004), rt=1.1)
            cols[arm] = (dots, lbl)

        c.until("Three hundred fifty")
        counts = VGroup(*[Text(f"{N_PER_ARM} patients", font=MONO, color=SEC, font_size=26)
                          .next_to(cols[a][0], DOWN, buff=0.25) for a in (SURGERY, KEYHOLE)])
        c.run(FadeIn(counts, shift=UP * 0.1), rt=0.5)

        c.until("The data is real")
        src = VGroup(Text("Charig et al.", color=SEC, font_size=28, slant="ITALIC"),
                     Text("British Medical Journal, 1986", color=SEC, font_size=28, slant="ITALIC")
                     ).arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to([3.4, 0.7, 0])
        c.run(FadeIn(src, shift=UP * 0.1), rt=0.6)

        c.until("Say you run")
        card = RoundedRectangle(corner_radius=0.2, width=5.6, height=2.0, color=INK,
                                stroke_width=4, fill_color=WHITE, fill_opacity=1).move_to([3.4, -1.1, 0])
        q = Text("You pick one.", color=INK, weight="BOLD", font_size=52).move_to(card)
        c.run(FadeIn(card, shift=UP * 0.2), Write(q), rt=0.9)
        c.until("You have to")
        c.run(*[Indicate(cols[a][1], color=INK, scale_factor=1.08) for a in (SURGERY, KEYHOLE)], rt=0.8)
        c.pad()


# ── B04 — OUTPUT, cycle 1 ─────────────────────────────────────────────────────

class B04_KeyholeWins(Scene):
    """OUTPUT, cycle 1 — the misleading answer: keyhole 82.6 vs surgery 78.0.
    Chart on the left two-thirds; the reading of it on the right."""
    X = {KEYHOLE: -4.0, SURGERY: -1.4}
    W = 1.9

    def construct(self):
        c = Clock(self, "B04")
        k, s = Q1[KEYHOLE][1], Q1[SURGERY][1]
        ck, cs = winner_color(k, s)
        tag = Text("q1_by_treatment.out", font=MONO, color=SEC, font_size=26).to_corner(UL, buff=0.9)
        axis = Line([-5.6, BASE_Y, 0], [0.4, BASE_Y, 0], color=RULE, stroke_width=4)
        c.run(FadeIn(tag), Create(axis), rt=0.5)

        bars = {}
        for arm, pct, col in ((KEYHOLE, k, ck), (SURGERY, s, cs)):
            if arm == SURGERY:
                c.until("Open surgery")
            x = self.X[arm]
            b = bar(x, pct, col, self.W)
            c.run(GrowFromEdge(b, DOWN), FadeIn(bar_name(x, ARM_NAME[arm], 32)), rt=0.9)
            c.run(FadeIn(bar_value(b, pct, col), shift=UP * 0.1), rt=0.3)
            bars[arm] = b

        # The gap is too thin to brace at this scale (4.6 pts), so it is stated, not drawn.
        c.until("Keyhole wins")
        gap = round(k - s, 1)
        win = Text("Keyhole wins?", color=INK, weight="BOLD", font_size=62).move_to([3.4, 1.3, 0])
        gl = Text(f"by {gap} points", color=TERRACOTTA, weight="BOLD", font_size=44).next_to(win, DOWN, buff=0.35)
        c.run(Write(win), FadeIn(gl, shift=UP * 0.1), rt=0.9)

        c.until("Most dashboards")
        stop = VGroup(Text("most dashboards", color=SEC, font_size=38, slant="ITALIC"),
                      Text("stop here", color=SEC, font_size=38, slant="ITALIC")
                      ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(gl, DOWN, buff=0.5)
        c.run(FadeIn(stop, shift=UP * 0.1), rt=0.6)
        c.pad()


# ── B07 — OUTPUT, cycle 2 ─────────────────────────────────────────────────────

class B07_TheFlip(Scene):
    """OUTPUT, cycle 2 — the same two bars split by stone size; surgery wins both."""
    GROUP_X = {"small": -3.3, "large": 2.3}
    OFF = {SURGERY: -0.95, KEYHOLE: 0.95}
    W = 1.55
    NAME = {SURGERY: ("Open", "surgery"), KEYHOLE: "Keyhole"}

    def construct(self):
        c = Clock(self, "B07")
        tag = Text("q2_by_size.out", font=MONO, color=SEC, font_size=26).to_corner(UL, buff=0.9)
        axis = Line([-5.6, BASE_Y, 0], [4.6, BASE_Y, 0], color=RULE, stroke_width=4)
        # Open on B04's overall bars (pale), so the split reads as the same data re-cut.
        ghost = VGroup(bar(B04_KeyholeWins.X[KEYHOLE], Q1[KEYHOLE][1], PALE, B04_KeyholeWins.W),
                       bar(B04_KeyholeWins.X[SURGERY], Q1[SURGERY][1], PALE, B04_KeyholeWins.W))
        self.add(axis)
        c.run(FadeIn(tag), FadeIn(ghost), rt=0.4)

        for size, phrase in (("small", "Small stones"), ("large", "Large stones")):
            c.until(phrase)
            gx = self.GROUP_X[size]
            s, k = Q2[(size, SURGERY)][1], Q2[(size, KEYHOLE)][1]
            cs, ck = winner_color(s, k)
            pair = VGroup()
            for arm, pct, col in ((SURGERY, s, cs), (KEYHOLE, k, ck)):
                x = gx + self.OFF[arm]
                b = bar(x, pct, col, self.W)
                pair.add(VGroup(b, bar_value(b, pct, col), bar_name(x, self.NAME[arm], 26)))
            glabel = Text(SIZE_LABEL[size], color=INK, weight="BOLD", font_size=28).move_to([gx, BASE_Y - 1.2, 0])
            src = ghost[0] if size == "small" else ghost[1]
            c.run(ReplacementTransform(src.copy(), pair[0][0]), GrowFromEdge(pair[1][0], DOWN),
                     FadeIn(glabel), FadeIn(pair[0][2]), FadeIn(pair[1][2]), rt=1.0)
            c.run(FadeIn(pair[0][1], shift=UP * 0.1), FadeIn(pair[1][1], shift=UP * 0.1), rt=0.3)
            if size == "large":
                c.run(FadeOut(ghost), rt=0.4)

        c.until("Open surgery wins both")
        verdict = Text("Open surgery wins both.", color=TERRACOTTA, weight="BOLD",
                       font_size=52).to_edge(UP, buff=0.6).shift(RIGHT * 1.4)
        c.run(Write(verdict), rt=1.0)
        c.pad()


# ── B08 — MECHANISM ───────────────────────────────────────────────────────────

class B08_WhoGotWhat(Scene):
    """MECHANISM — B01's dots re-sorted by stone size: the hard cases went to surgery."""

    def construct(self):
        c = Clock(self, "B08")
        cols = {}
        for arm in (SURGERY, KEYHOLE):
            dots = patient_column(ARM_X[arm])
            cols[arm] = (dots, arm_label(ARM_NAME[arm], dots))
            self.add(dots, cols[arm][1])
        head = Text("Who got which stones?", color=INK, weight="BOLD", font_size=40).move_to([3.4, 2.9, 0])
        c.run(FadeIn(head), rt=0.5)

        # Large stones fill each column from the bottom: dark ink = large, pale = small.
        c.until("The hard cases")
        for arm in (SURGERY, KEYHOLE):
            if arm == KEYHOLE:
                c.until("Keyhole got")
            n_large = Q2[("large", arm)][0]
            n_small = Q2[("small", arm)][0]
            dots, _ = cols[arm]
            c.run(*[d.animate.set_color(INK if i < n_large else PALE) for i, d in enumerate(dots)], rt=1.2)
            lab = VGroup(Text(f"{n_large} large", font=MONO, color=INK, font_size=24, weight="BOLD"),
                         Text(f"{n_small} small", font=MONO, color=SEC, font_size=24)
                         ).arrange(DOWN, buff=0.08).next_to(dots, DOWN, buff=0.15)
            c.run(FadeIn(lab, shift=UP * 0.1), rt=0.4)

        key = VGroup(VGroup(Dot(radius=0.09, color=INK), Text("large (≥2 cm or multiple)", color=INK, font_size=24)
                            ).arrange(RIGHT, buff=0.15),
                     VGroup(Dot(radius=0.09, color=PALE).set_stroke(SEC, 1), Text("small (<2 cm)", color=SEC, font_size=24)
                            ).arrange(RIGHT, buff=0.15)).arrange(DOWN, buff=0.15, aligned_edge=LEFT).move_to([3.4, 2.0, 0])
        c.run(FadeIn(key), rt=0.4)

        # The confounder: stone size → treatment, stone size → outcome.
        c.until("Stone size drove")
        def node(txt, pos, col=INK, w=3.0):
            box = RoundedRectangle(corner_radius=0.15, width=w, height=0.95, color=col, stroke_width=4,
                                   fill_color=WHITE, fill_opacity=1).move_to(pos)
            return VGroup(box, Text(txt, color=col, weight="BOLD", font_size=32).move_to(box))
        size = node("stone size", [3.4, 0.85, 0], TERRACOTTA)
        treat = node("treatment", [1.9, -0.85, 0], w=2.8)
        outc = node("outcome", [4.9, -0.85, 0], w=2.6)
        a1 = Arrow(size.get_bottom(), treat.get_top(), color=TERRACOTTA, stroke_width=6, buff=0.1)
        a2 = Arrow(size.get_bottom(), outc.get_top(), color=TERRACOTTA, stroke_width=6, buff=0.1)
        c.run(FadeIn(size, shift=DOWN * 0.1), rt=0.5)
        c.run(GrowArrow(a1), FadeIn(treat), rt=0.6)
        c.run(GrowArrow(a2), FadeIn(outc), rt=0.6)

        c.until("The overall number")
        moral = VGroup(Text("the overall number measured", color=INK, font_size=28, slant="ITALIC"),
                       Text("the patients, not the procedure", color=INK, font_size=28, slant="ITALIC")
                       ).arrange(DOWN, buff=0.12).move_to([3.4, -2.0, 0])
        c.run(FadeIn(moral, shift=UP * 0.1), rt=0.8)
        c.pad()


# ── B09 — SUMMARY ─────────────────────────────────────────────────────────────

class B09_ThreeQuestions(Scene):
    """SUMMARY — real correlation, wrong cause; three questions; the observational caveat."""

    def construct(self):
        c = Clock(self, "B09")
        head = Text("A real correlation. Not the cause.", color=INK, weight="BOLD",
                    font_size=48).to_edge(UP, buff=0.7)
        c.run(Write(head), rt=1.2)
        c.until("The gap came")
        sub = Text("the gap came from the patient mix", color=SEC, font_size=32,
                   slant="ITALIC").next_to(head, DOWN, buff=0.25)
        c.run(FadeIn(sub, shift=UP * 0.1), rt=0.6)

        qs = [("who got which", "Who got which option?"),
              ("what else drives", "What else drives the outcome?"),
              ("does the gap survive", "Does the gap survive a split?")]
        rows = VGroup()
        for i, (_, q) in enumerate(qs, 1):
            y = 1.0 - (i - 1) * 1.05
            num = Text(str(i), color=TERRACOTTA, weight="BOLD", font_size=50).move_to([-4.6, y, 0])
            badge = Circle(radius=0.42, color=TERRACOTTA, stroke_width=5).move_to(num)
            txt = Text(q, color=INK, font_size=46).move_to([-3.9, y, 0], aligned_edge=LEFT)
            rows.add(VGroup(badge, num, txt))
        for (phrase, _), r in zip(qs, rows):
            c.until(phrase)
            c.run(Create(r[0]), FadeIn(r[1], scale=0.8), FadeIn(r[2], shift=RIGHT * 0.15), rt=0.6)

        c.until("And even the split")
        rule = Line(LEFT * 5.0, RIGHT * 4.2, color=RULE, stroke_width=3).next_to(rows, DOWN, buff=0.4)
        cav1 = Text("A split is still observational.", color=INK, font_size=36, slant="ITALIC")
        cav1.next_to(rule, DOWN, buff=0.3).align_to(rule, LEFT)
        c.run(GrowFromEdge(rule, LEFT), FadeIn(cav1), rt=0.7)
        c.until("Only randomizing")
        cav2 = Text("Only randomizing rules out what nobody measured.", color=SEC, font_size=32,
                    slant="ITALIC").next_to(cav1, DOWN, buff=0.2, aligned_edge=LEFT)
        c.run(FadeIn(cav2, shift=UP * 0.1), rt=0.7)
        c.pad()
