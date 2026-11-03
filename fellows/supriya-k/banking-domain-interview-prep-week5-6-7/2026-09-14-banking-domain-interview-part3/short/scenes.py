"""scenes.py — portrait (9:16) Manim scenes for banking-domain-star-method-behavioral/short.
Full-length short (no beats cut): all 11 Manim beats re-laid-out for portrait — act cards B01,
B04, B09, B13 and content beats B02, B05, B08, B12, B14, B17, B18. Not shrunk copies: the
portrait frame is narrow in x (frame_width=4.5, Gate B safe ±1.95) and unchanged in y
(frame_height=8.0, safe ±3.4), so every layout is restacked vertically.

DATA + TIMING come from the landscape ../scenes.py (imported, not copied): the same palette,
Daniel's self-scoring sheet (ch14:83-87), the same measured audio durations and narration cues.
Scene classes must be plain Scene subclasses named B0X_Name.
"""
from manim import *
from pathlib import Path
import importlib.util

config.frame_width = 4.5
config.frame_height = 8.0

_REEL = Path("/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art/projects/banking-domain-interview-prep-week5-6-7/2026-09-14-banking-domain-interview-part3")
_parent = Path(__file__).resolve().parent.parent / "scenes.py"
if not _parent.is_file() or not (_parent.parent / "beat_sheet.json").is_file():
    _parent = _REEL / "scenes.py"
_spec = importlib.util.spec_from_file_location("landscape_scenes", _parent)
L = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(L)

CREAM, INK, TEAL, CRIMSON, SLATE, GOLD, SEC = L.CREAM, L.INK, L.TEAL, L.CRIMSON, L.SLATE, L.GOLD, L.SEC
DANIEL, checkmark = L.DANIEL, L.checkmark
SAFE_X = 1.95


def handle(scene):
    h = Text("Supriya", color=SEC, font_size=18, weight="BOLD").set_opacity(0.8)
    h.move_to([SAFE_X - 0.05, -3.22, 0], aligned_edge=RIGHT)
    scene.add(h)
    return h


class Clock(L.Clock):
    def __init__(self, scene, bid):
        self.s, self.bid, self.t = scene, bid, 0.0
        self.DUR = L.dur(bid)
        scene.camera.background_color = CREAM
        handle(scene)


def fit(m, w):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


def centered(text, n, **kw):
    g = L.wrapped(text, n, **kw)
    for ln in g:
        ln.set_x(0)
    return g


# ── act cards ─────────────────────────────────────────────────────────────────

def act_card(scene, bid, act_label, numeral, headline, color):
    c = Clock(scene, bid)
    big = Text(numeral, color=color, weight="BOLD", font_size=200).set_opacity(0.25).move_to([0, 1.9, 0])
    fit(big, 3.6)
    bar = Rectangle(width=0.8, height=0.1, fill_color=color, fill_opacity=1, stroke_width=0).move_to([0, 0.35, 0])
    eyebrow = Text(act_label, color=SLATE, weight="BOLD", font_size=26).next_to(bar, DOWN, buff=0.25)
    head = fit(centered(headline, 14, color=INK, weight="BOLD", font_size=40), 3.8).next_to(eyebrow, DOWN, buff=0.35)
    rule = Rectangle(width=1.8, height=0.06, fill_color=color, fill_opacity=1, stroke_width=0).next_to(head, DOWN, buff=0.35)
    c.run(FadeIn(big), GrowFromCenter(bar), FadeIn(eyebrow), FadeIn(head, shift=UP * 0.1), rt=0.5)
    c.run(GrowFromCenter(rule), rt=0.3)
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
        head = Text("The four parts", color=INK, weight="BOLD", font_size=34).move_to([0, 2.9, 0])
        c.run(FadeIn(head), rt=0.4)
        parts = [("S", "Situation", "the scenario, briefly"), ("T", "Task", "your responsibility or goal"),
                 ("A", "Action", "what you specifically did"), ("R", "Result", "the outcome, and what changed because of it")]
        rows = VGroup()
        for k, (letter, label, detail) in enumerate(parts):
            y = 1.75 - k * 1.3
            badge = RoundedRectangle(corner_radius=0.1, width=0.7, height=0.7, fill_color=TEAL, fill_opacity=1, stroke_width=0).move_to([-1.55, y, 0])
            lt = Text(letter, color=CREAM, weight="BOLD", font_size=30).move_to(badge)
            lb = Text(label, color=INK, weight="BOLD", font_size=28).move_to([-1.0, y + 0.18, 0], aligned_edge=LEFT)
            dt = fit(L.wrapped(detail, 26, color=SLATE, font_size=19), 2.95)
            dt.next_to(lb, DOWN, buff=0.08, aligned_edge=LEFT)
            rows.add(VGroup(badge, lt, lb, dt))
        c.run(FadeIn(rows[0], shift=RIGHT * 0.1), rt=0.4)
        for r, w in zip(rows[1:], ["task", "action", "result"]):
            c.until(w)
            c.run(FadeIn(r, shift=RIGHT * 0.1), rt=0.35)
        c.pad()


class B05_ThreeCompetencies(Scene):
    def construct(self):
        c = Clock(self, "B05")
        head = fit(centered("What a banking panel listens for", 18, color=INK, weight="BOLD", font_size=30), 3.8).move_to([0, 2.85, 0])
        hedge = fit(Text("the book's own framing, not a published rubric", color=SEC, font_size=17, slant="ITALIC"), 3.8)
        hedge.next_to(head, DOWN, buff=0.18)
        c.run(FadeIn(head), FadeIn(hedge), rt=0.5)
        items = [("Risk awareness", "noticed a problem before being told, and acted on it", "risk awareness"),
                 ("Regulatory / control judgment", "understood why a rule or review step existed", "control judgment"),
                 ("Comfort under audit or examiner scrutiny", "defends the work without sounding defensive or evasive", "comfort under audit")]
        cols = VGroup()
        for k, (label, detail, _) in enumerate(items):
            box = RoundedRectangle(corner_radius=0.12, width=3.7, height=1.5, stroke_color=SLATE, stroke_width=3,
                                   fill_color="#FFFFFF", fill_opacity=1).move_to([0, 1.15 - k * 1.7, 0])
            lb = fit(centered(label, 24, color=TEAL, weight="BOLD", font_size=24), 3.4)
            dt = fit(centered(detail, 30, color=INK, font_size=19), 3.4)
            VGroup(lb, dt).arrange(DOWN, buff=0.14).move_to(box)
            cols.add(VGroup(box, lb, dt))
        c.until("on top of")
        c.run(*[FadeIn(col, shift=UP * 0.15) for col in cols], rt=0.6)
        for col, (_, _, w) in zip(cols, items):
            c.until(w)
            ring = SurroundingRectangle(col[0], color=TEAL, buff=0.05, corner_radius=0.15, stroke_width=6)
            c.run(Create(ring), rt=0.35)
        c.pad()


class B08_DeliveryRule(Scene):
    def construct(self):
        c = Clock(self, "B08")
        head = Text("Name the control.", color=INK, weight="BOLD", font_size=34).move_to([0, 2.8, 0])
        c.run(FadeIn(head), rt=0.4)
        weak = Text("“We fixed it.”", color=CRIMSON, font_size=34).move_to([0, 1.5, 0])
        weak_box = SurroundingRectangle(weak, color=CRIMSON, buff=0.22, corner_radius=0.1, stroke_width=4)
        tag = Text("weaker", color=CRIMSON, font_size=20, weight="BOLD").next_to(weak_box, DOWN, buff=0.18)
        c.until("we fixed it")
        c.run(FadeIn(weak), Create(weak_box), FadeIn(tag), rt=0.5)
        strong = fit(centered("“We added a validation check that catches that error before it reaches the report.”", 18,
                              color=TEAL, weight="BOLD", font_size=28), 3.4).move_to([0, -0.9, 0])
        strong_box = SurroundingRectangle(strong, color=TEAL, buff=0.25, corner_radius=0.12, stroke_width=4)
        c.until("we added")
        c.run(FadeIn(strong, shift=UP * 0.1), Create(strong_box), rt=0.6)
        c.pad()


class B12_ScoredChecklist(Scene):
    def construct(self):
        c = Clock(self, "B12")
        head = Text("What's scored", color=INK, weight="BOLD", font_size=36).move_to([0, 2.85, 0])
        rule = Rectangle(width=1.6, height=0.06, fill_color=TEAL, fill_opacity=1, stroke_width=0).next_to(head, DOWN, buff=0.22)
        c.run(FadeIn(head), GrowFromCenter(rule), rt=0.4)
        items = [("Risk awareness", "treating “is this plausible?” as a check worth running", "noticing"),
                 ("Escalation", "raising it immediately, to the right people", "escalating"),
                 ("Outcome / control", "naming the specific control that now exists", "naming")]
        rows = VGroup()
        for k, (lb, dt, _) in enumerate(items):
            y = 1.6 - k * 1.6
            ck = checkmark(size=0.4).move_to([-1.65, y + 0.05, 0])
            t1 = fit(Text(lb, color=INK, weight="BOLD", font_size=28), 3.2).move_to([-1.25, y + 0.15, 0], aligned_edge=LEFT)
            t2 = fit(L.wrapped(dt, 27, color=SLATE, font_size=19), 3.2).next_to(t1, DOWN, buff=0.1, aligned_edge=LEFT)
            rows.add(VGroup(ck, t1, t2))
        for r, (_, _, w) in zip(rows, items):
            c.until(w)
            c.run(Create(r[0]), FadeIn(r[1]), FadeIn(r[2]), rt=0.4)
        c.pad()


class B14_FiveStageLoop(Scene):
    def construct(self):
        c = Clock(self, "B14")
        head = Text("A full banking loop", color=INK, weight="BOLD", font_size=32).move_to([0, 2.95, 0])
        c.run(FadeIn(head), rt=0.4)
        stages = ["Domain vocabulary", "SQL", "Case", "Behavioral", "Systems design"]
        boxes = VGroup()
        for i, label in enumerate(stages):
            col = CRIMSON if i == 3 else SLATE
            box = RoundedRectangle(corner_radius=0.1, width=3.7, height=0.66, stroke_color=col, stroke_width=4,
                                   fill_color="#FFFFFF", fill_opacity=1)
            num = Text(str(i + 1), color=col, weight="BOLD", font_size=28).move_to(box.get_left() + RIGHT * 0.35)
            lb = fit(Text(label, color=INK, font_size=22, weight="BOLD" if i == 3 else "NORMAL"), 2.8).next_to(num, RIGHT, buff=0.3)
            boxes.add(VGroup(box, num, lb))
        boxes.arrange(DOWN, buff=0.16).move_to([0, 0.5, 0])
        c.until("five stages")
        c.run(*[FadeIn(b, shift=RIGHT * 0.1) for b in boxes], rt=0.8)
        caveat = fit(Text("not every bank runs all five in one day", color=SEC, font_size=19, slant="ITALIC"), 3.8)
        caveat.next_to(boxes, DOWN, buff=0.3)
        c.until("though not every bank")
        c.run(FadeIn(caveat), rt=0.4)
        who = fit(centered("Daniel · 3½ years in · one timed sitting", 22, color=INK, font_size=22, weight="BOLD"), 3.8).move_to([0, -2.5, 0])
        c.until("daniel")
        ring = SurroundingRectangle(boxes[3], color=CRIMSON, buff=0.08, corner_radius=0.14, stroke_width=6)
        c.run(FadeIn(who, shift=UP * 0.1), Create(ring), rt=0.5)
        c.pad()


class B17_ScoreAndChart(Scene):
    def construct(self):
        c = Clock(self, "B17")
        head = Text("Daniel's self-scoring sheet", color=INK, weight="BOLD", font_size=28).move_to([0, 3.0, 0])
        fit(head, 3.8)
        src = Text("as recorded in the book", color=SEC, font_size=18, slant="ITALIC").next_to(head, DOWN, buff=0.15)
        c.run(FadeIn(head), FadeIn(src), rt=0.4)
        rows = VGroup()
        for k, (stage, score, note) in enumerate(DANIEL):
            y = 1.85 - k * 1.05
            col = CRIMSON if score == 1 else SLATE
            lb = Text(stage, color=INK, font_size=21, weight="BOLD" if score == 1 else "NORMAL").move_to([-1.9, y + 0.28, 0], aligned_edge=LEFT)
            bar = Rectangle(width=2.6 * score / 3, height=0.3, fill_color=col, fill_opacity=1, stroke_width=0)
            bar.move_to([-1.9, y - 0.06, 0], aligned_edge=LEFT)
            sc = Text(f"{score}/3", color=col, font_size=21, weight="BOLD").next_to(bar, RIGHT, buff=0.15)
            nt = fit(Text(note, color=SEC, font_size=16, slant="ITALIC"), 3.8).move_to([-1.9, y - 0.38, 0], aligned_edge=LEFT)
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
        head = Text("Daniel's final week", color=INK, weight="BOLD", font_size=32).move_to([0, 3.0, 0])
        illus = fit(Text("illustrative split — the book gives no hours", color=SEC, font_size=17, slant="ITALIC"), 3.8)
        illus.next_to(head, DOWN, buff=0.15)
        c.run(FadeIn(head), FadeIn(illus), rt=0.4)
        segs = [("Behavioral: re-drill 2–3 STAR stories, name the control", 0.52, CRIMSON),
                ("one light rep each: vocab · SQL · case · systems", 0.2, SLATE),
                ("final 48 hours: cheat sheet + logistics", 0.28, GOLD)]
        total_h, y = 3.9, 2.2
        bars = VGroup()
        for label, frac, col in segs:
            h = total_h * frac
            r = RoundedRectangle(corner_radius=0.1, width=3.8, height=h - 0.1, fill_color=col, fill_opacity=0.92,
                                 stroke_width=0).move_to([0, y - h / 2, 0])
            t = fit(centered(label, 22 if frac > 0.25 else 28, color="#FFFFFF" if col != GOLD else INK, weight="BOLD",
                              font_size=21 if frac > 0.25 else 18), 3.4)
            if t.height > h - 0.2:
                t.scale_to_fit_height(h - 0.2)
            t.move_to(r)
            bars.add(VGroup(r, t))
            y -= h
        c.until("behavioral gets most")
        c.run(FadeIn(bars[0], shift=UP * 0.1), rt=0.4)
        c.run(FadeIn(bars[1], shift=UP * 0.1), FadeIn(bars[2], shift=UP * 0.1), rt=0.5)
        lesson = fit(centered("Finish the thought out loud.", 20, color=INK, weight="BOLD", font_size=30), 3.8).move_to([0, -2.45, 0])
        c.until("finish the thought")
        c.run(FadeIn(lesson, shift=UP * 0.1), rt=0.4)
        c.pad()
