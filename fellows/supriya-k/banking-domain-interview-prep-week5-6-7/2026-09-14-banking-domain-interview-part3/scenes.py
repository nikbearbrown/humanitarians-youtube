"""scenes.py — Manim scenes for banking-domain-star-method-behavioral (deep-explainer) — v3.
11 Manim scenes: 4 act cards (B01, B04, B09, B13) + 7 content beats (B02, B05, B08, B12, B14,
B17, B18). The other 11 beats render via Remotion.

Palette: the humanitarians set used by the shared body cards (QuoteCard / StateCardPair /
LabelChip), for body consistency. Class names are `B0X_Name(Scene)` for run.sh's regex.
No LaTeX. weight/slant passed as strings (Gate A's stub doesn't define the constants).

Book fidelity (v3): on-screen wording follows Ch.12/Ch.14 (see FACTCHECK.md, "v3 corrections").
Daniel's scores are the book's own self-scoring sheet (ch14:83-87). B18's week strip is
illustrative (the book gives no hours) and says so on screen.

Every scene carries the "Supriya" corner handle (PM requirement 4) — `handle()`.
TIMING: DUR from beat_sheet.json (`actual_duration_s`); cues by word position in the narration.
"""
from manim import *
from pathlib import Path
import json
import numpy as np

_REEL = Path("/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art/projects/banking-domain-interview-prep-week5-6-7/2026-09-14-banking-domain-interview-part3")
HERE = Path(__file__).resolve().parent
if not (HERE / "beat_sheet.json").is_file():
    HERE = _REEL

CREAM = "#F3EBDD"; INK = "#2F2A26"; TEAL = "#1F4E5F"
CRIMSON = "#E4572E"; SLATE = "#29335C"; GOLD = "#F3A712"; SEC = "#6B6357"; DIM = "#B9B2A6"

BEATS = {b["beat_id"]: b for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}

# Daniel's self-scoring sheet, verbatim from ch14:83-87 (stage, score, the book's note).
DANIEL = [("Domain vocabulary", 2, "missed the HMDA cross-reference"),
          ("SQL", 2, "correct, but silent"),
          ("Case", 2, "no risk caveat"),
          ("Behavioral", 1, "no named escalation or outcome"),
          ("Systems design", 2, "no named control")]


def dur(bid):
    b = BEATS[bid]
    return float(b.get("actual_duration_s") or b["estimated_duration_s"])


def _norm(w):
    return w.strip(".,:;!?\"'“”").lower()


def cue(bid, phrase):
    words = BEATS[bid]["narration_text"].split()
    target = phrase.split()
    for i in range(len(words) - len(target) + 1):
        if [_norm(w) for w in words[i:i + len(target)]] == [_norm(t) for t in target]:
            return dur(bid) * i / len(words)
    raise ValueError(f"{bid}: cue phrase not in narration: {phrase!r}")


def handle(scene):
    h = Text("Supriya", color=SEC, font_size=26, weight="BOLD").set_opacity(0.8)
    h.to_corner(DR, buff=0.9)
    scene.add(h)
    return h


class Clock:
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
        self.s.wait(max(0.3, self.DUR - self.t - 0.15))


def checkmark(color=TEAL, size=0.4):
    mark = VMobject(color=color, stroke_width=8)
    mark.set_points_as_corners([np.array([-0.5, 0.05, 0]) * size, np.array([-0.1, -0.45, 0]) * size,
                                np.array([0.55, 0.5, 0]) * size])
    return mark


def wrapped(text, n, **kw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= n:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return VGroup(*[Text(l, **kw) for l in lines]).arrange(DOWN, buff=0.12, aligned_edge=LEFT)


# ── act cards (short beats: everything lands in the first ~1s) ────────────────

def act_card(scene, bid, act_label, numeral, headline, color):
    c = Clock(scene, bid)
    big = Text(numeral, color=color, weight="BOLD", font_size=280).set_opacity(0.25)
    big.move_to([6.0 - big.width / 2, -0.1, 0])   # right edge pinned inside SAFE
    bar = Rectangle(width=1.3, height=0.18, fill_color=color, fill_opacity=1, stroke_width=0).move_to([-5.0, 1.2, 0])
    eyebrow = Text(act_label, color=SLATE, weight="BOLD", font_size=36).next_to(bar, RIGHT, buff=0.35)
    head = wrapped(headline, 20, color=INK, weight="BOLD", font_size=58).next_to(bar, DOWN, buff=0.55).align_to(bar, LEFT)
    rule = Rectangle(width=3.0, height=0.08, fill_color=color, fill_opacity=1, stroke_width=0).next_to(head, DOWN, buff=0.45).align_to(bar, LEFT)
    c.run(FadeIn(big), GrowFromEdge(bar, LEFT), FadeIn(eyebrow), FadeIn(head, shift=UP * 0.15), rt=0.5)
    c.run(GrowFromEdge(rule, LEFT), rt=0.3)
    c.pad()


class B01_ActICard(Scene):
    def construct(self):
        act_card(self, "B01", "ACT I", "I", "The STAR Framework", TEAL)


class B04_ActIICard(Scene):
    def construct(self):
        act_card(self, "B04", "ACT II", "II", "What a Banking Panel Listens For", CRIMSON)


class B09_ActIIICard(Scene):
    def construct(self):
        act_card(self, "B09", "ACT III", "III", "Weak Answer, STAR Rewrite", SLATE)


class B13_ActIVCard(Scene):
    def construct(self):
        act_card(self, "B13", "ACT IV", "IV", "Daniel's Full-Loop Mock", GOLD)


# ── content beats ─────────────────────────────────────────────────────────────

class B02_StarFourParts(Scene):
    def construct(self):
        c = Clock(self, "B02")
        head = Text("The four parts", color=INK, weight="BOLD", font_size=46).move_to([-3.6, 2.85, 0])
        c.run(FadeIn(head), rt=0.4)
        parts = [("S", "Situation", "the scenario, briefly", "situation"), ("T", "Task", "your responsibility or goal", "task"),
                 ("A", "Action", "what you specifically did", "action"), ("R", "Result", "the outcome, and what changed because of it", "result")]
        rows = VGroup()
        for k, (letter, label, detail, _) in enumerate(parts):
            y = 1.55 - k * 1.25
            badge = RoundedRectangle(corner_radius=0.14, width=1.0, height=1.0, fill_color=TEAL, fill_opacity=1, stroke_width=0).move_to([-5.2, y, 0])
            lt = Text(letter, color=CREAM, weight="BOLD", font_size=44).move_to(badge)
            lb = Text(label, color=INK, weight="BOLD", font_size=40).move_to([-4.35, y + 0.2, 0], aligned_edge=LEFT)
            dt = Text(detail, color=SLATE, font_size=30).move_to([-4.35, y - 0.28, 0], aligned_edge=LEFT)
            rows.add(VGroup(badge, lt, lb, dt))
        c.run(*[FadeIn(r, shift=RIGHT * 0.15) for r in rows[:1]], rt=0.4)
        for r, w in zip(rows[1:], ["task", "action", "result"]):
            c.until(w)
            c.run(FadeIn(r, shift=RIGHT * 0.15), rt=0.35)
        c.pad()


class B05_ThreeCompetencies(Scene):
    def construct(self):
        c = Clock(self, "B05")
        head = Text("What a banking panel listens for", color=INK, weight="BOLD", font_size=40).move_to([0, 2.9, 0])
        hedge = Text("the book's own framing, not a published rubric", color=SEC, font_size=26, slant="ITALIC").next_to(head, DOWN, buff=0.2)
        c.run(FadeIn(head), FadeIn(hedge), rt=0.5)
        items = [("Risk awareness", "noticed a problem before being told, and acted on it", "risk awareness"),
                 ("Regulatory / control judgment", "understood why a rule or review step existed", "control judgment"),
                 ("Comfort under audit or examiner scrutiny", "defends the work without sounding defensive or evasive", "comfort under audit")]
        cols = VGroup()
        for (label, detail, _), x in zip(items, [-4.15, 0, 4.15]):
            box = RoundedRectangle(corner_radius=0.16, width=3.9, height=3.9, stroke_color=SLATE, stroke_width=3,
                                   fill_color="#FFFFFF", fill_opacity=1).move_to([x, -0.6, 0])
            lb = wrapped(label, 20, color=TEAL, weight="BOLD", font_size=32)
            for t in lb:
                t.set_x(x)
            if lb.width > 3.5:
                lb.scale_to_fit_width(3.5)
            dt = wrapped(detail, 20, color=INK, font_size=28)
            for t in dt:
                t.set_x(x)
            VGroup(lb, dt).arrange(DOWN, buff=0.4).move_to(box)
            cols.add(VGroup(box, lb, dt))
        c.until("on top of")
        c.run(*[FadeIn(col, shift=UP * 0.2) for col in cols], rt=0.6)
        for col, (_, _, w) in zip(cols, items):
            c.until(w)
            ring = SurroundingRectangle(col[0], color=TEAL, buff=0.06, corner_radius=0.2, stroke_width=6)
            c.run(Create(ring), rt=0.35)
        c.pad()


class B08_DeliveryRule(Scene):
    def construct(self):
        c = Clock(self, "B08")
        head = Text("Name the control.", color=INK, weight="BOLD", font_size=50).move_to([0, 2.7, 0])
        c.run(FadeIn(head), rt=0.4)
        weak = Text("“We fixed it.”", color=CRIMSON, font_size=46).move_to([0, 1.3, 0])
        weak_box = SurroundingRectangle(weak, color=CRIMSON, buff=0.3, corner_radius=0.12, stroke_width=4)
        tag = Text("weaker", color=CRIMSON, font_size=26, weight="BOLD").next_to(weak_box, RIGHT, buff=0.3)
        c.until("we fixed it")
        c.run(FadeIn(weak), Create(weak_box), FadeIn(tag), rt=0.5)
        strong = wrapped("“We added a validation check that catches that error before it reaches the report.”", 40,
                         color=TEAL, weight="BOLD", font_size=40).move_to([0, -0.9, 0])
        strong_box = SurroundingRectangle(strong, color=TEAL, buff=0.35, corner_radius=0.14, stroke_width=4)
        c.until("we added")
        c.run(FadeIn(strong, shift=UP * 0.15), Create(strong_box), rt=0.6)
        c.pad()


class B12_ScoredChecklist(Scene):
    def construct(self):
        c = Clock(self, "B12")
        head = Text("What's scored", color=INK, weight="BOLD", font_size=50).move_to([-3.4, 2.8, 0])
        rule = Rectangle(width=2.4, height=0.08, fill_color=TEAL, fill_opacity=1, stroke_width=0).next_to(head, DOWN, buff=0.3).align_to(head, LEFT)
        c.run(FadeIn(head), GrowFromEdge(rule, LEFT), rt=0.4)
        items = [("Risk awareness", "treating “is this plausible?” as a check worth running", "noticing"),
                 ("Escalation", "raising it immediately, to the right people", "escalating"),
                 ("Outcome / control", "naming the specific control that now exists", "naming")]
        rows = VGroup()
        for k, (lb, dt, _) in enumerate(items):
            y = 1.25 - k * 1.45
            ck = checkmark(size=0.55).move_to([-5.6, y, 0])
            t1 = Text(lb, color=INK, weight="BOLD", font_size=38).move_to([-4.9, y + 0.22, 0], aligned_edge=LEFT)
            t2 = Text(dt, color=SLATE, font_size=29).move_to([-4.9, y - 0.3, 0], aligned_edge=LEFT)
            rows.add(VGroup(ck, t1, t2))
        for r, (_, _, w) in zip(rows, items):
            c.until(w)
            c.run(Create(r[0]), FadeIn(r[1]), FadeIn(r[2]), rt=0.4)
        c.pad()


class B14_FiveStageLoop(Scene):
    def construct(self):
        c = Clock(self, "B14")
        head = Text("A full banking loop", color=INK, weight="BOLD", font_size=44).move_to([0, 2.85, 0])
        c.run(FadeIn(head), rt=0.4)
        stages = ["Domain\nvocabulary", "SQL", "Case", "Behavioral", "Systems\ndesign"]
        boxes = VGroup()
        for i, label in enumerate(stages):
            col = CRIMSON if i == 3 else SLATE
            box = RoundedRectangle(corner_radius=0.14, width=2.35, height=2.2, stroke_color=col, stroke_width=4,
                                   fill_color="#FFFFFF", fill_opacity=1)
            num = Text(str(i + 1), color=col, weight="BOLD", font_size=40)
            lb = VGroup(*[Text(x, color=INK, font_size=26, weight="BOLD" if i == 3 else "NORMAL") for x in label.split("\n")]).arrange(DOWN, buff=0.06)
            VGroup(num, lb).arrange(DOWN, buff=0.25).move_to(box)
            boxes.add(VGroup(box, num, lb))
        boxes.arrange(RIGHT, buff=0.18).move_to([0, 0.55, 0])
        c.until("five stages")
        c.run(*[FadeIn(b, shift=DOWN * 0.15) for b in boxes], rt=0.8)
        caveat = Text("not every bank runs all five in one day", color=SEC, font_size=28, slant="ITALIC").next_to(boxes, DOWN, buff=0.4)
        c.until("though not every bank")
        c.run(FadeIn(caveat), rt=0.4)
        who = Text("Daniel · 3½ years in · one timed sitting", color=INK, font_size=32, weight="BOLD").move_to([0, -2.4, 0])
        c.until("daniel")
        ring = SurroundingRectangle(boxes[3], color=CRIMSON, buff=0.12, corner_radius=0.18, stroke_width=6)
        c.run(FadeIn(who, shift=UP * 0.1), Create(ring), rt=0.5)
        c.pad()


class B17_ScoreAndChart(Scene):
    def construct(self):
        c = Clock(self, "B17")
        head = Text("Daniel's self-scoring sheet", color=INK, weight="BOLD", font_size=42).move_to([-2.4, 2.85, 0])
        src = Text("as recorded in the book", color=SEC, font_size=22, slant="ITALIC").next_to(head, RIGHT, buff=0.4).align_to(head, DOWN)
        c.run(FadeIn(head), FadeIn(src), rt=0.4)
        rows = VGroup()
        for k, (stage, score, note) in enumerate(DANIEL):
            y = 1.65 - k * 0.95
            col = CRIMSON if score == 1 else SLATE
            lb = Text(stage, color=INK, font_size=28, weight="BOLD" if score == 1 else "NORMAL").move_to([-2.7, y, 0], aligned_edge=RIGHT)
            bar = Rectangle(width=4.2 * score / 3, height=0.55, fill_color=col, fill_opacity=1, stroke_width=0).move_to([-2.4 + 2.1 * score / 3, y, 0])
            sc = Text(f"{score}/3", color=col, font_size=28, weight="BOLD").next_to(bar, RIGHT, buff=0.2)
            nt = Text(note, color=SEC, font_size=22, slant="ITALIC")
            if nt.width > 3.9:
                nt.scale_to_fit_width(3.9)
            nt.move_to([1.9, y, 0], aligned_edge=LEFT)
            rows.add(VGroup(lb, bar, sc, nt))
        beh = rows[3]
        c.until("he scores that stage")
        c.run(FadeIn(beh[0]), GrowFromEdge(beh[1], LEFT), FadeIn(beh[2]), FadeIn(beh[3]), rt=0.6)
        others = [r for i, r in enumerate(rows) if i != 3]
        c.until("his other four")
        c.run(*[FadeIn(r[0]) for r in others], *[GrowFromEdge(r[1], LEFT) for r in others],
              *[FadeIn(r[2]) for r in others], *[FadeIn(r[3]) for r in others], rt=0.7)
        c.pad()


class B18_TheLesson(Scene):
    def construct(self):
        c = Clock(self, "B18")
        head = Text("Daniel's final week", color=INK, weight="BOLD", font_size=44).move_to([-3.3, 2.85, 0])
        illus = Text("illustrative split — the book gives no hours", color=SEC, font_size=22, slant="ITALIC").move_to([-3.3, 2.3, 0])
        c.run(FadeIn(head), FadeIn(illus), rt=0.4)
        segs = [("Behavioral: re-drill 2–3 STAR stories, name the control", 0.52, CRIMSON),
                ("one light rep each: vocab · SQL · case · systems", 0.2, SLATE),
                ("final 48 hours: cheat sheet + logistics", 0.28, GOLD)]
        total_w, x = 12.0, -6.0
        bars = VGroup()
        for label, frac, col in segs:
            w = total_w * frac
            r = RoundedRectangle(corner_radius=0.12, width=w - 0.12, height=1.9, fill_color=col, fill_opacity=0.92, stroke_width=0).move_to([x + w / 2, 0.55, 0])
            t = wrapped(label, 26 if frac > 0.3 else 16, color="#FFFFFF" if col != GOLD else INK, weight="BOLD", font_size=24)
            for ln in t:
                ln.set_x(0)
            if t.width > w - 0.4:
                t.scale_to_fit_width(w - 0.4)
            t.move_to(r)
            bars.add(VGroup(r, t))
            x += w
        c.until("behavioral gets most")
        c.run(FadeIn(bars[0], shift=UP * 0.15), rt=0.4)
        c.run(FadeIn(bars[1], shift=UP * 0.15), FadeIn(bars[2], shift=UP * 0.15), rt=0.5)
        lesson = Text("Finish the thought out loud.", color=INK, weight="BOLD", font_size=46).move_to([0, -1.75, 0])
        c.until("finish the thought")
        c.run(FadeIn(lesson, shift=UP * 0.15), rt=0.4)
        c.pad()
