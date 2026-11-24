# -*- coding: utf-8 -*-
"""
Manim scenes for "The 99.9% Accuracy Trap" (16:9, 3840x2160) -- Boopesh M.
  B20_Rare        -- 580 dots, 1 red: the real dataset's fraud rate (492 in 284,807)
  B30_Lazy        -- the "always legit" model: accuracy meter 99.8%, 0 of 148 frauds caught
  B40_Scorecard   -- four boxes (confusion matrix) + recall / precision in plain words
  B50_Models      -- lazy vs logistic vs boosted: same accuracy, very different catch
  B60_Threshold   -- precision-recall curve + the threshold dial + the cost rule
  B70_Takeaway    -- takeaway + honest limits
  B90_Outro       -- @HumanitariansAI outro + fellow credit
Every model number is read from code/results.json and code/curves.npz, written by code/fraud_trap.py
(SYNTHETIC data with the real dataset's size and fraud rate). Each scene lands on its beat's measured length.
"""
import json
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"
CODE = HERE / "code"
if not (CODE / "results.json").exists():   # isolated copies (static pre-flight) fall back to the reel's data
    CODE = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-11-01-fraud-accuracy-trap/code")
if not (ASSETS / "hai-logo.svg").exists():
    ASSETS = CODE.parent / "assets"

BG = "#FAF9F5"
INK = "#2B2A26"
ACCENT = "#A64B2A"   # terracotta, WCAG 4.5:1+ on cream and panel
MUTED = "#6F6A5E"
PANEL = "#EEEADF"
LINE = "#D9D3C4"
GHOST = "#A39A88"
TEAL = "#1F4E5F"     # data / caught
GREY = "#8C8578"     # legit dots, lazy model
FRAUD = "#B3261E"    # the fraud dot / missed fraud
DARK = "#2B2A26"
ON_DARK = "#F5F1E8"
ON_DARK_MUTED = "#D8D0C0"

SERIF = "EB Garamond"
SANS = "Inter"
MONO = "DejaVu Sans Mono"

RES = json.loads((CODE / "results.json").read_text())
CUR = np.load(CODE / "curves.npz")
SET = RES["setup"]
LAZY, LOGI, BOOST = RES["always_legit"], RES["logistic"], RES["boosted"]
SWEEP = {r["threshold"]: r for r in RES["threshold_sweep_boosted"]}
BEST = RES["cost_best"]
NF = SET["test_frauds"]          # 148
REAL = SET["real_dataset_reference"]
ONE_IN = int(round(REAL["one_in"], -1))   # 579 -> 580


def _sheet():
    try:
        return {b["beat_id"]: b for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}
    except Exception:
        return {}


BEATS = _sheet()


def beat_len(bid, default=12.0):
    b = BEATS.get(bid, {})
    return float(b.get("render_duration_s") or b.get("actual_duration_s") or default)


def cue(bid, phrase, default):
    """Seconds into the beat when `phrase` is spoken (share of characters + lead silence)."""
    b = BEATS.get(bid)
    if not b:
        return default
    text = b["narration_text"]
    i = text.find(phrase)
    if i < 0:
        return default
    lead = float(b.get("lead_silence_s") or 0)
    return lead + (beat_len(bid) - lead) * i / len(text)


class Clock:
    """Schedules a scene's animations against narration cues and ends it on the beat length."""

    def __init__(self, scene, bid):
        self.scene, self.bid, self.t = scene, bid, 0.0
        scene.camera.background_color = BG

    def play_at(self, at, *anims, run_time=0.8, **kw):
        if at > self.t:
            self.scene.wait(at - self.t)
            self.t = at
        self.scene.play(*anims, run_time=run_time, **kw)
        self.t += run_time

    def finish(self):
        end = beat_len(self.bid)
        if end - self.t > 1 / 24:
            self.scene.wait(end - self.t)


def t(s, size=40, color=INK, font=SANS, weight="NORMAL", **kw):
    return Text(s, font=font, font_size=size, color=color, weight=weight, **kw)


def fit(m, w):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


def svg(name, height=None, width=None):
    m = SVGMobject(str(ASSETS / name))
    if height:
        m.scale_to_fit_height(height)
    if width:
        m.scale_to_fit_width(width)
    return m


def header(kicker, title):
    k = t(kicker.upper(), 22, MUTED, MONO)
    h = t(title, 58, INK, SERIF, weight="BOLD")
    g = VGroup(k, h).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
    g.to_corner(UL, buff=0.85)
    return g


def card(w, h, fill=PANEL):
    return RoundedRectangle(width=w, height=h, corner_radius=0.12, fill_color=fill,
                            fill_opacity=1, stroke_width=0)


def ghost_of(m, color=GHOST):
    return m.copy().set_fill(opacity=0).set_stroke(color, 3)


def pct(x, nd=1):
    return f"{100 * x:.{nd}f}%"


def comma(n):
    return f"{n:,}"


class Frame:
    """Maps data coordinates onto a rectangle of the scene."""

    def __init__(self, x0, x1, y0, y1, box):
        self.x0, self.x1, self.y0, self.y1 = x0, x1, y0, y1
        self.L, self.R, self.B, self.T = box

    def p(self, x, y):
        return np.array([self.L + (x - self.x0) / (self.x1 - self.x0) * (self.R - self.L),
                         self.B + (y - self.y0) / (self.y1 - self.y0) * (self.T - self.B), 0.0])

    def axes(self, color=INK):
        return VGroup(Line([self.L, self.B, 0], [self.R + 0.1, self.B, 0], color=color, stroke_width=3),
                      Line([self.L, self.B, 0], [self.L, self.T + 0.1, 0], color=color, stroke_width=3))


def stat_card(big, small, w=5.4, h=1.05, big_color=INK):
    c = card(w, h)
    lab = VGroup(t(big, 40, big_color, SERIF, weight="BOLD"), t(small, 21, MUTED)).arrange(RIGHT, buff=0.3)
    fit(lab, w - 0.4).move_to(c)
    return VGroup(c, lab)


# ======================================================================== B20 =
class B20_Rare(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        hd = header("real card data · ULB Machine Learning Group + Worldline", "How rare is card fraud?")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        cols, rows, sp = 29, 20, 0.225
        dots = VGroup(*[Circle(radius=0.075, stroke_width=0, fill_color=GREY, fill_opacity=1)
                        for _ in range(rows * cols)]).arrange_in_grid(rows=rows, cols=cols, buff=sp - 0.15)
        dots.move_to([-2.85, -0.5, 0])
        k = 12 * cols + 17                       # the one fraud, somewhere off-centre
        red = dots[k]
        ghosts = dots.copy().set_fill(opacity=0).set_stroke(GHOST, 1.5)
        grid_cap = VGroup(t(f"{cols * rows} transactions ·", 22, MUTED), t("1 fraud (red)", 22, FRAUD, weight="BOLD")).arrange(RIGHT, buff=0.15).next_to(dots, DOWN, buff=0.15)

        s1 = stat_card(comma(REAL["rows"]), "card transactions")
        s2 = stat_card(comma(REAL["frauds"]), "of them fraud", big_color=FRAUD)
        s3 = stat_card(f"1 in {ONE_IN}", f"= {int(REAL['rate'] * 1e5) / 1e3:.3f}% of all", big_color=FRAUD)
        stats = VGroup(s1, s2, s3).arrange(DOWN, buff=0.22).move_to([3.55, -0.35, 0])
        src = VGroup(t("European cardholders, two days in Sept 2013", 18, MUTED),
                     t("Kaggle dataset from ULB + Worldline", 18, MUTED)).arrange(DOWN, buff=0.08)
        src.next_to(stats, DOWN, buff=0.25)

        ring = Circle(radius=0.26, color=FRAUD, stroke_width=6).move_to(red)

        clock.play_at(0.4, FadeIn(ghosts), FadeIn(VGroup(*[ghost_of(s[0]) for s in stats])), run_time=0.6)
        clock.play_at(cue("B20", "real card", 2.5), FadeIn(s1, shift=LEFT * 0.2), run_time=0.6)
        clock.play_at(cue("B20", "four hundred ninety-two", 5.0), FadeIn(s2, shift=LEFT * 0.2), FadeIn(src),
                      run_time=0.6)
        clock.play_at(cue("B20", "About one in", 9.0), FadeIn(s3, shift=LEFT * 0.2), run_time=0.6)
        clock.play_at(cue("B20", "Here are", 12.0),
                      LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.004), FadeIn(grid_cap[0]), run_time=1.6)
        clock.play_at(cue("B20", "Just one", 14.5), red.animate.set_fill(FRAUD).scale(1.4), Create(ring),
                      FadeIn(grid_cap[1]), run_time=0.7)
        clock.finish()


# ======================================================================== B30 =
class B30_Lazy(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        hd = header(f"synthetic test set · {comma(SET['test_rows'])} transactions · {NF} frauds",
                    "The laziest fraud model")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        code_box = card(5.2, 1.75, fill=DARK).move_to([-3.45, 0.55, 0])
        code = VGroup(t("def is_fraud(transaction):", 24, ON_DARK, MONO),
                      t("return False  # always legit", 24, ON_DARK_MUTED, MONO)).arrange(
            DOWN, aligned_edge=LEFT, buff=0.18)
        code[1].shift(RIGHT * 0.6)
        fit(code, 4.8).move_to(code_box)
        note_box = card(5.2, 1.55).move_to([-3.45, -1.75, 0])
        note = VGroup(t("synthetic data", 26, INK, weight="BOLD"),
                      t("same size and fraud rate", 21, MUTED),
                      t("as the real dataset", 21, MUTED)).arrange(DOWN, buff=0.1).move_to(note_box)

        # accuracy meter
        mx0, mx1, my = 0.35, 6.0, 0.25
        acc_lab = t("accuracy", 26, MUTED).move_to([mx0, 1.25, 0], aligned_edge=LEFT)
        acc_big = t(pct(LAZY["accuracy"]), 72, TEAL, SERIF, weight="BOLD")
        acc_big.next_to(acc_lab, RIGHT, buff=0.35).align_to(acc_lab, DOWN).shift(DOWN * 0.08)
        track = RoundedRectangle(width=mx1 - mx0, height=0.5, corner_radius=0.08, fill_color=PANEL,
                                 fill_opacity=1, stroke_color=GHOST, stroke_width=2).move_to([(mx0 + mx1) / 2, my, 0])
        fill_w = (mx1 - mx0) * LAZY["accuracy"]
        bar = Rectangle(width=fill_w, height=0.5, fill_color=TEAL, fill_opacity=1, stroke_width=0)
        bar.move_to([mx0 + fill_w / 2, my, 0])
        ticks = VGroup(t("0%", 18, MUTED, MONO).move_to([mx0, my - 0.45, 0], aligned_edge=LEFT),
                       t("100%", 18, MUTED, MONO).move_to([mx1, my - 0.45, 0], aligned_edge=RIGHT))

        # 148 hollow circles: every fraud missed
        circ = VGroup(*[Circle(radius=0.055, stroke_color=FRAUD, stroke_width=2.5, fill_opacity=0)
                        for _ in range(NF)]).arrange_in_grid(rows=4, cols=37, buff=0.095)
        circ.scale_to_fit_width(mx1 - mx0).move_to([(mx0 + mx1) / 2, -1.85, 0])
        caught_lab = t("frauds caught", 26, MUTED).move_to([mx0, -0.85, 0], aligned_edge=LEFT)
        caught_big = t(f"{LAZY['caught']} of {NF}", 60, FRAUD, SERIF, weight="BOLD")
        caught_big.next_to(caught_lab, RIGHT, buff=0.35).align_to(caught_lab, DOWN).shift(DOWN * 0.06)
        circ_cap = t("every one of the 148 frauds is missed", 20, FRAUD).next_to(circ, DOWN, buff=0.2)
        verdict = fit(t("a great score for a model that does nothing", 24, ACCENT, weight="BOLD"), mx1 - mx0)
        verdict.move_to([(mx0 + mx1) / 2, -3.05, 0])

        clock.play_at(0.4, FadeIn(ghost_of(code_box)), FadeIn(ghost_of(note_box)), FadeIn(ghost_of(track)),
                      FadeIn(circ.copy().set_stroke(GHOST, 2)), run_time=0.6)
        clock.play_at(cue("B30", "It says legit", 2.3), FadeIn(code_box), FadeIn(code, shift=UP * 0.1), run_time=0.6)
        clock.play_at(cue("B30", "synthetic data", 4.5), FadeIn(note_box), FadeIn(note), run_time=0.6)
        clock.play_at(cue("B30", "its accuracy", 6.5), FadeIn(track), FadeIn(ticks), FadeIn(acc_lab), run_time=0.4)
        clock.play_at(clock.t, GrowFromEdge(bar, LEFT), FadeIn(acc_big, scale=0.9), run_time=1.0)
        clock.play_at(cue("B30", "Frauds caught", 10.0), FadeIn(caught_lab), FadeIn(caught_big, scale=0.9),
                      FadeIn(circ), FadeIn(circ_cap), run_time=0.7)
        clock.play_at(clock.t + 0.8, FadeIn(verdict, shift=UP * 0.1), run_time=0.6)
        clock.finish()


# ======================================================================== B40 =
class B40_Scorecard(Scene):
    def construct(self):
        clock = Clock(self, "B40")
        hd = header("a better scorecard · lazy model's test results", "Four boxes, two questions")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        bw, bh = 2.75, 1.55
        specs = [("fraud caught", LAZY["caught"], TEAL, ON_DARK, ON_DARK_MUTED),
                 ("false alarm", LAZY["false_alarms"], PANEL, INK, MUTED),
                 ("fraud missed", LAZY["missed"], FRAUD, ON_DARK, ON_DARK_MUTED),
                 ("legit, let through", LAZY["true_legit"], PANEL, INK, MUTED)]
        boxes = VGroup()
        for name, n, fill, c1, c2 in specs:
            r = RoundedRectangle(width=bw, height=bh, corner_radius=0.1, fill_color=fill, fill_opacity=1,
                                 stroke_width=0)
            lab = VGroup(t(comma(n), 48, c1, SERIF, weight="BOLD"), t(name, 21, c2)).arrange(DOWN, buff=0.1)
            lab.move_to(r)
            boxes.add(VGroup(r, lab))
        boxes.arrange_in_grid(rows=2, cols=2, buff=0.18).move_to([-2.85, -0.95, 0])
        col_h = VGroup(t("really fraud", 20, MUTED).next_to(boxes[0], UP, buff=0.15),
                       t("really legit", 20, MUTED).next_to(boxes[1], UP, buff=0.15))

        rc = card(5.9, 1.9).move_to([3.25, 0.55, 0])
        rec = VGroup(svg("eq_recall_ink.svg", height=1.0),
                     t("of all real frauds, how many did we catch?", 21, MUTED)).arrange(DOWN, buff=0.18)
        fit(rec, 5.5).move_to(rc)
        pc = card(5.9, 1.9).move_to([3.25, -1.55, 0])
        pre = VGroup(svg("eq_precision_ink.svg", height=1.0),
                     t("of all alarms raised, how many were real fraud?", 21, MUTED)).arrange(DOWN, buff=0.18)
        fit(pre, 5.5).move_to(pc)
        verdict = t(f"lazy model: recall = {LAZY['caught']} / {NF} = 0", 26, ACCENT, weight="BOLD")
        verdict.move_to([3.25, -3.0, 0])

        clock.play_at(0.4, FadeIn(VGroup(*[ghost_of(b[0]) for b in boxes])), FadeIn(ghost_of(rc)),
                      FadeIn(ghost_of(pc)), run_time=0.6)
        clock.play_at(cue("B40", "four boxes", 2.5), FadeIn(col_h), run_time=0.5)
        order = [("fraud caught", 0), ("fraud missed", 2), ("false alarm", 1), ("legit, correctly", 3)]
        for i, (p, j) in enumerate(order):
            clock.play_at(max(clock.t, cue("B40", p, 3.5 + i)), FadeIn(boxes[j], scale=0.95), run_time=0.45)
        clock.play_at(cue("B40", "Recall asks", 8.0), FadeIn(rc), FadeIn(rec, shift=UP * 0.1), run_time=0.6)
        clock.play_at(cue("B40", "Precision asks", 11.5), FadeIn(pc), FadeIn(pre, shift=UP * 0.1), run_time=0.6)
        clock.play_at(cue("B40", "For the lazy", 15.0), FadeIn(verdict, shift=UP * 0.1),
                      Indicate(boxes[2], color=FRAUD, scale_factor=1.05), run_time=0.7)
        clock.finish()


# ======================================================================== B50 =
class B50_Models(Scene):
    def construct(self):
        clock = Clock(self, "B50")
        hd = header(f"synthetic test set · {NF} frauds · cutoff 0.5", "Same accuracy, different catch")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        models = [("always legit", LAZY, GREY), ("logistic regression", LOGI, TEAL),
                  ("gradient boosting", BOOST, TEAL)]
        xs = [-4.5, -0.45, 3.6]
        bb, bt = -2.35, 0.0         # bar bottom / top (top = all 148 caught)
        cols = []
        for (name, r, col), x in zip(models, xs):
            nm = t(name, 26, INK, weight="BOLD").move_to([x, 1.45, 0])
            acc = VGroup(t(pct(r["accuracy"], 2), 40, INK, SERIF, weight="BOLD"),
                         t("accurate", 20, MUTED)).arrange(RIGHT, buff=0.15).move_to([x, 0.85, 0])
            frame = Rectangle(width=1.3, height=bt - bb, stroke_color=GHOST, stroke_width=3,
                              fill_opacity=0).move_to([x, (bb + bt) / 2, 0])
            h = max((bt - bb) * r["caught"] / NF, 0.02)
            bar = Rectangle(width=1.3, height=h, fill_color=col, fill_opacity=1, stroke_width=0)
            bar.move_to([x, bb + h / 2, 0])
            num = t(f"{r['caught']}", 40, col if r["caught"] else FRAUD, SERIF, weight="BOLD")
            num.next_to(frame, RIGHT, buff=0.15).align_to(bar, UP)
            if r["caught"] == 0:
                num.move_to([x + 1.05, bb + 0.25, 0])
            cap = t(f"caught of {NF}", 18, MUTED).next_to(num, DOWN, buff=0.05).align_to(num, LEFT)
            fa = t(f"false alarms: {r['false_alarms']}", 20, INK).move_to([x, -2.75, 0])
            prec = pct(r["precision"], 0) if r["flagged"] else "n/a"
            rp = t(f"recall {pct(r['recall'], 0)} · precision {prec}", 18, MUTED)
            rp.move_to([x, -3.12, 0])
            cols.append(dict(nm=nm, acc=acc, frame=frame, bar=bar, num=num, cap=cap, fa=fa, rp=rp))
        brace_line = RoundedRectangle(width=11.4, height=0.68, corner_radius=0.1, stroke_color=ACCENT,
                                      stroke_width=3, fill_opacity=0).move_to([-0.45, 0.85, 0])
        same = t("accuracy: almost identical", 20, ACCENT, weight="BOLD").move_to([-0.45, 0.3, 0])
        same_bg = BackgroundRectangle(same, color=BG, fill_opacity=1, buff=0.05)
        twice = VGroup(t(f"{BOOST['caught'] / LOGI['caught']:.1f}×", 34, ON_DARK, SERIF, weight="BOLD"),
                       t("logistic's catch", 16, ON_DARK_MUTED)).arrange(DOWN, buff=0.04)
        twice.move_to(cols[2]["bar"].get_top() + DOWN * 0.55)

        def show(c, extra=()):
            return [FadeIn(c["nm"]), FadeIn(c["acc"], shift=UP * 0.1), GrowFromEdge(c["bar"], DOWN),
                    FadeIn(c["num"]), FadeIn(c["cap"]), FadeIn(c["fa"]), FadeIn(c["rp"]), *extra]

        clock.play_at(0.4, *[FadeIn(c["frame"]) for c in cols],
                      *[FadeIn(c["nm"].copy().set_opacity(0.3)) for c in cols], run_time=0.6)
        clock.play_at(0.9, *show(cols[0]), run_time=0.7)
        clock.play_at(cue("B50", "A logistic regression", 3.0), *show(cols[1]), run_time=0.8)
        clock.play_at(cue("B50", "A small gradient", 9.0), *show(cols[2]), run_time=0.8)
        clock.play_at(cue("B50", "Nearly twice", 15.0), FadeIn(twice), run_time=0.6)
        clock.play_at(cue("B50", "accuracy can't", 17.0), Create(brace_line), FadeIn(same_bg), FadeIn(same),
                      run_time=0.6)
        clock.play_at(cue("B50", "Recall can", 19.0),
                      *[Indicate(c["rp"], color=ACCENT, scale_factor=1.12) for c in cols], run_time=0.8)
        clock.finish()


# ======================================================================== B60 =
class B60_Threshold(Scene):
    def construct(self):
        clock = Clock(self, "B60")
        hd = header("gradient-boosted model · synthetic test set", "The threshold dial")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        # precision-recall curve (boosted, teal; logistic, grey)
        fr = Frame(0, 1, 0, 1, (-5.6, -0.95, -2.5, 1.35))
        ax = fr.axes()
        xl = VGroup(t("0", 18, MUTED, MONO).move_to(fr.p(0, 0) + DOWN * 0.25),
                    t("1", 18, MUTED, MONO).move_to(fr.p(1, 0) + DOWN * 0.25),
                    t("recall: share of fraud caught →", 18, MUTED).move_to(fr.p(0.5, 0) + DOWN * 0.5))
        yl = VGroup(t("1", 18, MUTED, MONO).next_to(fr.p(0, 1), LEFT, buff=0.12),
                    t("0", 18, MUTED, MONO).next_to(fr.p(0, 0), LEFT, buff=0.12),
                    t("precision: alarms that are real →", 18, MUTED).rotate(PI / 2).next_to(fr.p(0, 0.5), LEFT, buff=0.35))

        def curve(key, color, width):
            p, r = CUR[f"{key}_precision"], CUR[f"{key}_recall"]
            step = max(1, len(p) // 400)
            pts = [fr.p(r[i], p[i]) for i in range(0, len(p), step)] + [fr.p(r[-1], p[-1])]
            return VMobject(color=color, stroke_width=width).set_points_as_corners(pts)

        c_lr = curve("logistic", GREY, 3)
        c_hgb = curve("boosted", TEAL, 5)
        leg = VGroup(VGroup(Line(ORIGIN, RIGHT * 0.4, color=TEAL, stroke_width=5), t("gradient boosting", 18, INK)).arrange(RIGHT, buff=0.12),
                     VGroup(Line(ORIGIN, RIGHT * 0.4, color=GREY, stroke_width=3), t("logistic regression", 18, INK)).arrange(RIGHT, buff=0.12))
        leg.arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(fr.p(0.03, 0.12), aligned_edge=DL)

        # the dial (right)
        dial_box = card(6.3, 3.4).move_to([2.95, 0.1, 0])
        th_list = [0.9, 0.5, 0.1, 0.01]
        sx0, sx1, sy = 1.55, 5.5, 1.05
        slider = Line([sx0, sy, 0], [sx1, sy, 0], color=INK, stroke_width=4)
        tick_x = {th: sx1 - (sx1 - sx0) * i / (len(th_list) - 1) for i, th in enumerate(th_list)}
        ticks = VGroup()
        for th, x in tick_x.items():
            ticks.add(VGroup(Line([x, sy - 0.1, 0], [x, sy + 0.1, 0], color=INK, stroke_width=3),
                             t(f"{th:g}", 18, MUTED, MONO).move_to([x, sy + 0.32, 0])))
        dial_lab = t("cutoff", 22, INK, weight="BOLD").move_to([0.15, sy, 0], aligned_edge=LEFT)
        knob = Circle(radius=0.16, fill_color=ACCENT, fill_opacity=1, stroke_color=BG, stroke_width=3)

        def readout(r):
            a = VGroup(t(f"{r['caught']}", 54, TEAL, SERIF, weight="BOLD"),
                       t(f"frauds caught of {NF}", 20, MUTED)).arrange(DOWN, buff=0.05)
            b = VGroup(t(f"{r['false_alarms']}", 54, ACCENT, SERIF, weight="BOLD"),
                       t("false alarms", 20, MUTED)).arrange(DOWN, buff=0.05)
            g = VGroup(a, b).arrange(RIGHT, buff=1.1).move_to([2.95, -0.7, 0])
            return g

        def dot_at(r):
            return Dot(fr.p(r["recall"], r["precision"]), radius=0.11, color=ACCENT)

        r9, r01 = SWEEP[0.9], SWEEP[0.01]
        ro = readout(r9)
        knob.move_to([tick_x[0.9], sy, 0])
        dot = dot_at(r9)
        lower = t("← lower it: more caught, more false alarms", 20, MUTED).move_to([2.95, 0.5, 0])

        cost_box = card(6.3, 1.25, fill=DARK).move_to([2.95, -2.35, 0])
        cost = VGroup(t("if a miss costs 50× a false alarm (assumption):", 19, ON_DARK_MUTED),
                      t(f"cheapest cutoff {BEST['threshold']:g} → catches {BEST['caught']}, "
                        f"{BEST['false_alarms']} false alarms", 22, ON_DARK, weight="BOLD")).arrange(DOWN, buff=0.12)
        fit(cost, 5.9).move_to(cost_box)
        star = Circle(radius=0.2, color=INK, stroke_width=4).move_to(fr.p(BEST["recall"], BEST["precision"]))

        clock.play_at(0.4, FadeIn(ax.copy().set_color(GHOST)), FadeIn(ghost_of(dial_box)),
                      FadeIn(ghost_of(cost_box)), run_time=0.6)
        clock.play_at(0.9, Create(ax), FadeIn(xl), FadeIn(yl), run_time=0.6)
        clock.play_at(cue("B60", "fraud score", 2.0), Create(c_lr), Create(c_hgb), FadeIn(leg), run_time=1.4)
        clock.play_at(cue("B60", "Lower it", 4.5), FadeIn(dial_box), Create(slider), FadeIn(ticks), FadeIn(dial_lab),
                      FadeIn(lower), run_time=0.7)
        clock.play_at(cue("B60", "At point nine", 8.0), FadeIn(knob), FadeIn(ro), FadeIn(dot, scale=0.5),
                      run_time=0.6)
        ro2 = readout(r01)
        clock.play_at(cue("B60", "At point zero one", 13.5), knob.animate.move_to([tick_x[0.01], sy, 0]),
                      dot.animate.move_to(fr.p(r01["recall"], r01["precision"])), Transform(ro, ro2), run_time=1.2)
        clock.play_at(cue("B60", "Say a miss", 17.0), FadeIn(cost_box), FadeIn(cost, shift=UP * 0.1),
                      FadeIn(star, scale=0.5), run_time=0.7)
        clock.finish()


# ======================================================================== B70 =
class B70_Takeaway(Scene):
    def construct(self):
        clock = Clock(self, "B70")
        hd = header("takeaway + honest limits", "When it's rare, don't trust accuracy")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        L = card(5.9, 4.5, fill=DARK).move_to([-3.1, -0.75, 0])
        R = card(5.9, 4.5).move_to([3.1, -0.75, 0])
        lt = t("Check these instead", 28, ON_DARK, weight="BOLD").move_to(L.get_top() + DOWN * 0.5)
        tk = [("recall", "how much fraud you catch"), ("precision", "how many alarms are real"),
              ("cost", "what each mistake costs")]
        items_l = VGroup()
        for a, b in tk:
            items_l.add(VGroup(t(a, 30, ON_DARK, SERIF, weight="BOLD"), t(b, 21, ON_DARK_MUTED)).arrange(
                DOWN, aligned_edge=LEFT, buff=0.06))
        items_l.arrange(DOWN, aligned_edge=LEFT, buff=0.32).move_to(L.get_center() + DOWN * 0.3)

        rt = t("Honest limits", 28, INK, weight="BOLD").move_to(R.get_top() + DOWN * 0.5)
        lims = ["synthetic data, not real transactions",
                "built to match the real fraud rate",
                "real systems use far more signals",
                "fraudsters change their tricks"]
        items_r = VGroup()
        for s in lims:
            items_r.add(VGroup(Dot(radius=0.06, color=INK), t(s, 21, INK)).arrange(RIGHT, buff=0.2))
        items_r.arrange(DOWN, aligned_edge=LEFT, buff=0.38).move_to(R.get_center() + DOWN * 0.3)
        items_r[0][1].set_color(ACCENT)

        clock.play_at(0.3, FadeIn(ghost_of(L, "#5E544C")), FadeIn(ghost_of(R)), run_time=0.5)
        clock.play_at(cue("B70", "accuracy is the wrong", 1.5), FadeIn(L), FadeIn(lt), run_time=0.6)
        for i, p in enumerate(["recall", "precision", "cost of each"]):
            clock.play_at(max(clock.t, cue("B70", p, 4.0 + i)), FadeIn(items_l[i], shift=RIGHT * 0.15), run_time=0.45)
        clock.play_at(cue("B70", "honest limits", 8.0), FadeIn(R), FadeIn(rt), run_time=0.5)
        for i, p in enumerate(["synthetic", "built to match", "far more signals", "fraudsters"]):
            clock.play_at(max(clock.t, cue("B70", p, 9.0 + 1.5 * i)), FadeIn(items_r[i], shift=LEFT * 0.15),
                          run_time=0.45)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = t("The 99.9% Accuracy Trap", 80, INK, SERIF)
        title.scale_to_fit_width(min(title.width, 11.0))
        pill_lab = t("SUBSCRIBE", 32, ON_DARK, SANS, weight="BOLD")
        pill = RoundedRectangle(width=pill_lab.width + 0.8, height=0.74, corner_radius=0.37,
                                fill_color=DARK, fill_opacity=1, stroke_width=0)
        pill_lab.move_to(pill)
        hai = svg("hai-logo.svg", height=0.52).set_color(INK)
        handle = t("@HumanitariansAI", 38, INK, SANS, weight="BOLD")
        row = VGroup(VGroup(pill, pill_lab), hai, handle).arrange(RIGHT, buff=0.3)
        main = VGroup(title, row).arrange(DOWN, buff=0.55).move_to(UP * 1.45)
        clock.play_at(0.2, FadeIn(title, shift=UP * 0.15), run_time=0.8)
        clock.play_at(clock.t + 0.1, FadeIn(row, shift=UP * 0.1), run_time=0.6)

        rule = Line(LEFT * 3.4, RIGHT * 3.4, color=LINE, stroke_width=3).next_to(main, DOWN, buff=0.6)
        c1 = t("Boopesh M.", 46, INK, SERIF, weight="BOLD")
        c2 = t("Humanitarians AI Fellow · Brutalist team", 32, MUTED)
        c3 = t("Data: synthetic, with the fraud rate of the ULB + Worldline card dataset (Dal Pozzolo et al., 2015)",
               20, MUTED)
        c3.scale_to_fit_width(min(c3.width, 11.8))
        c4 = t("Narration: AI voice (Kokoro am_onyx) reading Boopesh's script", 24, MUTED)
        credit = VGroup(c1, c2, c3, c4).arrange(DOWN, buff=0.2).next_to(rule, DOWN, buff=0.45)
        dim = VGroup(rule, credit).copy().set_opacity(0.18)
        clock.play_at(clock.t, FadeIn(dim), run_time=0.3)
        clock.play_at(max(clock.t, cue("B90", "With Boopesh", 1.5)), FadeOut(dim), Create(rule),
                      FadeIn(credit, shift=UP * 0.1), run_time=0.7)
        clock.finish()
