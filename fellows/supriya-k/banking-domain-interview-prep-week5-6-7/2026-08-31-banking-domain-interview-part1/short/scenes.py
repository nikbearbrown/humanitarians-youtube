"""scenes.py — portrait (9:16) Manim scenes for banking-domain-interview-end-to-end-v2/short — v3.
Full-length short (no beats cut — v2's short dropped B06–B08): all 5 Manim beats re-laid-out for
portrait — B01, B02, B05, B08, B09. Portrait frame: frame_width=4.5 (Gate B safe ±1.95),
frame_height=8.0 (safe ±3.4); every layout is restacked vertically.

DATA + TIMING come from the landscape ../scenes.py (imported, not copied): the same balances and
cohort mix parsed from ../sql/*.out, the same measured audio durations and narration cues.
Scene classes must be plain Scene subclasses named B0X_Name.
"""
from manim import *
from pathlib import Path
import importlib.util

config.frame_width = 4.5
config.frame_height = 8.0

_REEL = Path("/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art/projects/banking-domain-interview-prep-week5-6-7/2026-08-31-banking-domain-interview-part1")
_parent = Path(__file__).resolve().parent.parent / "scenes.py"
if not _parent.is_file() or not (_parent.parent / "sql").is_dir():
    _parent = _REEL / "scenes.py"
_spec = importlib.util.spec_from_file_location("landscape_scenes", _parent)
L = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(L)

CREAM, INK, TERRACOTTA, TEAL, CRIMSON, SEC, RULE, MONO = L.CREAM, L.INK, L.TERRACOTTA, L.TEAL, L.CRIMSON, L.SEC, L.RULE, L.MONO
BALANCES, CARRIED, ACCOUNT, BUCKETS, VINTAGE, MOBS, TOTALS, COHORT_N = L.BALANCES, L.CARRIED, L.ACCOUNT, L.BUCKETS, L.VINTAGE, L.MOBS, L.TOTALS, L.COHORT_N
mon, money = L.mon, L.money
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


def chip(label, color, size=20, fill=0.12, w=None):
    t = Text(label, color=color, weight="BOLD", font_size=size)
    box = RoundedRectangle(corner_radius=0.2, width=w or t.width + 0.4, height=t.height + 0.3,
                           stroke_color=color, stroke_width=3, fill_color=color, fill_opacity=fill)
    if w:
        fit(t, w - 0.25)
    return VGroup(box, t.move_to(box))


def lines(texts, size, color=INK, bold=True, buff=0.08):
    return VGroup(*[Text(t, color=color, font_size=size, weight="BOLD" if bold else "NORMAL") for t in texts]).arrange(DOWN, buff=buff)


def disclosure():
    return fit(Text("real run: sql/ · SQLite (MySQL-only functions swapped)", font=MONO, color=SEC, font_size=13), 3.8).move_to([0, -2.85, 0])


class B01_TheSecondLanguage(Scene):
    def construct(self):
        c = Clock(self, "B01")
        head = Text("You already have this.", color=INK, weight="BOLD", font_size=28).move_to([0, 3.05, 0])
        c.run(FadeIn(head), rt=0.5)
        base = VGroup(*[chip(s, TEAL, 20, 0.0) for s in ["joins", "cohorts", "dashboards"]]).arrange(RIGHT, buff=0.15)
        fit(base, 3.8).move_to([0, 2.35, 0])
        c.until("skills you already have")
        c.run(LaggedStart(*[FadeIn(b, shift=UP * 0.1) for b in base], lag_ratio=0.25), rt=0.8)
        layer = Text("+ the layer banking adds", color=TERRACOTTA, weight="BOLD", font_size=22).move_to([0, 1.55, 0])
        regs = VGroup(*[chip(s, TERRACOTTA, 24) for s in ["OCC", "CFPB"]]).arrange(RIGHT, buff=0.2).move_to([0, 0.8, 0])
        regl = Text("regulators", color=SEC, font_size=16).next_to(regs, DOWN, buff=0.1)
        ratios = VGroup(*[chip(s, TERRACOTTA, 24) for s in ["CET1", "LCR"]]).arrange(RIGHT, buff=0.2).move_to([0, -0.3, 0])
        ratl = Text("ratios", color=SEC, font_size=16).next_to(ratios, DOWN, buff=0.1)
        c.until("second language")
        c.run(FadeIn(layer), rt=0.4)
        c.until("regulators like")
        c.run(FadeIn(regs, shift=DOWN * 0.2), FadeIn(regl), rt=0.5)
        c.until("ratios like")
        c.run(FadeIn(ratios, shift=DOWN * 0.2), FadeIn(ratl), rt=0.5)
        qs = VGroup(chip("regulatory-reportable?", INK, 20, 0.06, w=3.6), chip("could it be fraud?", INK, 20, 0.06, w=3.6)).arrange(DOWN, buff=0.2).move_to([0, -1.95, 0])
        c.until("regulatory-reportable")
        c.run(FadeIn(qs[0], shift=UP * 0.1), FadeIn(qs[1], shift=UP * 0.1), rt=0.5)
        c.pad()


class B02_SixPartMap(Scene):
    def construct(self):
        c = Clock(self, "B02")
        head = Text("Six parts", color=INK, weight="BOLD", font_size=32).move_to([0, 3.05, 0])
        c.run(FadeIn(head), rt=0.5)
        boxes = VGroup()
        for num, label, _ in L.PARTS:
            box = RoundedRectangle(corner_radius=0.1, width=3.8, height=0.68, color=TEAL, stroke_width=3,
                                   fill_color="#FFFFFF", fill_opacity=1)
            n = Text(num, color=TERRACOTTA, weight="BOLD", font_size=22).move_to(box.get_left() + RIGHT * 0.4)
            lb = fit(Text(label.replace("\n", " "), color=INK, font_size=20), 2.9).move_to(box).align_to(box, LEFT).shift(RIGHT * 0.8)
            boxes.add(VGroup(box, n, lb))
        boxes.arrange(DOWN, buff=0.14).move_to([0, 0.3, 0])
        sub = fit(chip("Part IV: 40+ SQL problems · Python for banking", TERRACOTTA, 17, w=3.8), 3.8).move_to([0, -2.45, 0])
        for k, ((_, _, word), b) in enumerate(zip(L.PARTS[:4], boxes[:4])):
            c.until(word)
            c.run(FadeIn(b, shift=LEFT * 0.15), *([FadeIn(sub)] if k == 3 else []), rt=0.4)
        c.until(L.PARTS[4][2])
        c.run(FadeIn(boxes[4], shift=LEFT * 0.15), FadeIn(boxes[5], shift=LEFT * 0.15), rt=0.5)
        c.pad()


class B05_CorrectBalance(Scene):
    def construct(self):
        c = Clock(self, "B05")
        head = lines(["Cascade Savings", f"account {ACCOUNT}"], 24).move_to([0, 2.9, 0])
        c.run(FadeIn(head), FadeIn(disclosure()), rt=0.5)
        carried = fit(Text(f"carried into January: {money(CARRIED)}", color=TEAL, font_size=18), 3.8).move_to([0, 2.05, 0])
        c.until("twelve thousand")
        c.run(FadeIn(carried), rt=0.4)
        hdr = VGroup(Text("Month", color=SEC, font_size=18).move_to([-1.0, 1.35, 0]), Text("EOM balance", color=SEC, font_size=18).move_to([0.95, 1.35, 0]))
        rule = Line([-1.9, 1.12, 0], [1.9, 1.12, 0], color=RULE, stroke_width=2)
        body = VGroup(*[VGroup(Text(mon(m), color=INK, font_size=22).move_to([-1.0, 0.7 - k * 0.62, 0]),
                               Text(money(v), font=MONO, color=TEAL, font_size=24, weight="BOLD").move_to([0.95, 0.7 - k * 0.62, 0]))
                        for k, (m, v) in enumerate(BALANCES)])
        c.until("month-end balances")
        c.run(FadeIn(hdr), Create(rule), LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in body], lag_ratio=0.3), rt=1.0)
        c.until("true ones")
        c.run(FadeIn(chip("Sum first. Filter after.", TEAL, 22, 0.08).move_to([0, -1.75, 0]), scale=0.95), rt=0.4)
        c.pad()


class B08_VintageCurve(Scene):
    def construct(self):
        c = Clock(self, "B08")
        head = lines(["Harborline Card Co.", "Jan 2025 sample cohort"], 22).move_to([0, 2.95, 0])
        c.run(FadeIn(head), FadeIn(disclosure()), rt=0.5)
        colors = [interpolate_color(ManimColor(TEAL), ManimColor(CRIMSON), i / (len(BUCKETS) - 1)) for i in range(len(BUCKETS))]
        bar_h, bar_w, base_y = 3.2, 1.05, -1.3
        xs = [-1.35, 0.0, 1.35]
        cols, labels, notes = VGroup(), VGroup(), VGroup()
        for x, m in zip(xs, MOBS):
            segs, y = VGroup(), base_y
            for b, col in zip(BUCKETS, colors):
                n, _ = VINTAGE[m].get(b, (0, 0.0))
                if n == 0:
                    continue
                h = bar_h * n / COHORT_N
                segs.add(Rectangle(width=bar_w, height=h, stroke_width=1, stroke_color=CREAM, fill_color=col,
                                   fill_opacity=0.95).move_to([x, y + h / 2, 0]))
                y += h
            cols.add(segs)
            labels.add(Text(f"month {m}", color=INK, weight="BOLD", font_size=18).move_to([x, base_y - 0.25, 0]))
            cur = VINTAGE[m]["current"][1]
            p90, pco = (VINTAGE[m].get(b, (0, 0.0))[1] for b in ("90+", "charge_off"))
            notes.add(VGroup(*[Text(s, color=SEC, font_size=13) for s in (f"{cur:g}% cur", f"{p90:g}% 90+", f"{pco:g}% c-o")]
                             ).arrange(DOWN, buff=0.04).move_to([x, base_y + bar_h + 0.38, 0]))
        c.until("month three")
        c.run(GrowFromEdge(cols[0], DOWN), FadeIn(labels[0]), FadeIn(notes[0]), rt=0.6)
        c.run(GrowFromEdge(cols[1], DOWN), FadeIn(labels[1]), FadeIn(notes[1]), rt=0.6)
        c.until("month nine")
        c.run(GrowFromEdge(cols[2], DOWN), FadeIn(labels[2]), FadeIn(notes[2]), rt=0.6)
        legend = VGroup(*[VGroup(Square(side_length=0.18, fill_color=col, fill_opacity=0.95, stroke_width=0),
                                 Text(b, color=SEC, font_size=13)).arrange(RIGHT, buff=0.06) for b, col in zip(BUCKETS, colors)]
                        ).arrange(RIGHT, buff=0.14)
        fit(legend, 3.8).move_to([0, base_y - 0.65, 0])
        c.run(FadeIn(legend), rt=0.4)
        c.until("each column adds back")
        ns = Text(f"each column: n = {COHORT_N}", color=TEAL, font_size=20, weight="BOLD").move_to([0, base_y - 1.1, 0])
        c.run(FadeIn(ns), rt=0.5)
        c.pad()


class B09_TwoMoves(Scene):
    def construct(self):
        c = Clock(self, "B09")
        head = Text("Two moves", color=INK, weight="BOLD", font_size=34).move_to([0, 2.95, 0])
        bar = Line(head.get_corner(DL) + DOWN * 0.1, head.get_corner(DR) + DOWN * 0.1, color=TERRACOTTA, stroke_width=5)
        c.run(FadeIn(head), Create(bar), rt=0.5)
        rows = VGroup()
        for ls in (["Get the SQL", "evaluation order right"], ["Never lose", "the cohort"]):
            t = VGroup(*[Text(x, color=INK, font_size=24) for x in ls]).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
            rows.add(VGroup(L.checkmark(size=0.3).next_to(t, LEFT, buff=0.18).align_to(t, UP), t))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.45).move_to([0.0, 1.2, 0])
        for r, w in zip(rows, ["evaluation order", "never lose the cohort"]):
            c.until(w)
            c.run(Create(r[0]), FadeIn(r[1], shift=RIGHT * 0.1), rt=0.5)
        rest = Text("the rest of the book →", color=SEC, font_size=20, slant="ITALIC").move_to([0, -0.4, 0])
        chips = VGroup(*[chip(s, TEAL, 20, 0.0, w=3.4) for s in ["regulatory metrics", "data stack", "behavioral & case rounds"]]
                       ).arrange(DOWN, buff=0.15).move_to([0, -1.6, 0])
        c.until("the rest of the book")
        c.run(FadeIn(rest), LaggedStart(*[FadeIn(x, shift=UP * 0.1) for x in chips], lag_ratio=0.25), rt=0.9)
        c.pad()
