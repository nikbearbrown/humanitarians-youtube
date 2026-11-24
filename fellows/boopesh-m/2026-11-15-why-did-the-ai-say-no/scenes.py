# -*- coding: utf-8 -*-
"""
Manim scenes for "Why Did the AI Say No?" (16:9, 3840x2160) -- Boopesh M.
  B20_Rule        -- what the rule asks for: Regulation B 1002.9(b)(2); CFPB Circular 2022-03 (withdrawn 2025)
  B30_Models      -- 20,000 synthetic applicants, 5 plain features; scorecard vs boosted "black box"; same AUC
  B40_ApplicantA  -- Applicant A's five values; risk 53 % / 34 % against a 30 % line: both deny
  B50_Scorecard   -- the one formula (push = weight x (A - average)); bars; top 3 reasons
  B60_BlackBox    -- Shapley values (16,000 model runs); top 3; 2 of 3 shared; the list can shift
  B70_Change      -- pay cards down $3,850 -> both approve; limits
  B90_Outro       -- @HumanitariansAI outro + fellow credit
Every number is read from code/results.json, written by code/credit_reasons.py (SYNTHETIC APPLICANTS).
Each scene lands on its beat's measured length.
"""
import json
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"
CODE = HERE / "code"
if not (CODE / "results.json").exists():   # isolated copies (static pre-flight) fall back to the reel's data
    CODE = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-11-15-why-did-the-ai-say-no/code")
if not (ASSETS / "hai-logo.svg").exists():
    ASSETS = CODE.parent / "assets"

BG = "#FAF9F5"
INK = "#2B2A26"
ACCENT = "#A64B2A"   # terracotta, WCAG 4.5:1+ on cream and panel -- "no" / reasons
MUTED = "#6F6A5E"
PANEL = "#EEEADF"
LINE = "#D9D3C4"
GHOST = "#A39A88"
TEAL = "#1F4E5F"     # data / "yes"
DARK = "#2B2A26"
ON_DARK = "#F5F1E8"
ON_DARK_MUTED = "#D8D0C0"
DARK_GHOST = "#5E544C"

SERIF = "EB Garamond"
SANS = "Inter"
MONO = "DejaVu Sans Mono"

RES = json.loads((CODE / "results.json").read_text())
SET = RES["setup"]
FEATS = SET["features"]
AVG = SET["average_applicant"]
A = RES["applicant_a"]
AV = A["values"]
REA = RES["reasons"]
SC = REA["scorecard"]
BB = REA["boosted"]
CF = RES["counterfactual"]
MOD = RES["models"]
CUT = SET["cutoff"]
LABEL = {"income": "income", "dti": "debt-to-income", "missed": "missed payments",
         "history": "credit history", "util": "card use"}


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


KERN = 3   # build text large, then scale down: Pango drops spaces / mis-kerns small text


def t(s, size=40, color=INK, font=SANS, weight="NORMAL", **kw):
    return Text(s, font=font, font_size=size * KERN, color=color, weight=weight, **kw).scale(1 / KERN)


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


def pct(x, nd=0):
    return f"{100 * x:.{nd}f}%"


def a_value(f):
    v = AV[f]
    return {"income": f"${v:.0f}k a year", "dti": f"{v:.0f}% of income", "missed": f"{v:.0f} in 2 years",
            "history": f"{v:.0f} years", "util": f"{v:.0f}% of limit"}[f]


def avg_value(f):
    v = AVG[f]
    return {"income": f"${v:.0f}k", "dti": f"{v:.0f}%", "missed": f"{v:.1f}",
            "history": f"{v:.0f} yrs", "util": f"{v:.0f}%"}[f]


def risk_meter(width, x_left, y, label_size=20):
    """0-100 % default-risk axis with the lender's cutoff line. Returns (group, x-of-risk function)."""
    def px(r):
        return x_left + r * width

    axis = Line([px(0), y, 0], [px(1), y, 0], color=INK, stroke_width=4)
    ticks = VGroup(*[VGroup(Line([px(r), y - 0.08, 0], [px(r), y + 0.08, 0], color=INK, stroke_width=3),
                            t(f"{int(r * 100)}%", 18, MUTED, MONO).move_to([px(r), y - 0.32, 0]))
                     for r in (0, 0.5, 1.0)])
    zone = Rectangle(width=px(1) - px(CUT), height=1.9, fill_color=ACCENT, fill_opacity=0.10,
                     stroke_width=0).move_to([(px(1) + px(CUT)) / 2, y + 0.95, 0])
    cut = DashedLine([px(CUT), y - 0.1, 0], [px(CUT), y + 1.95, 0], color=ACCENT, stroke_width=4,
                     dash_length=0.1)
    cut_l = VGroup(t(f"lender's line: {pct(CUT)}", label_size, ACCENT, weight="BOLD"),
                   t("(my choice)", label_size - 2, MUTED)).arrange(DOWN, buff=0.04)
    cut_l.next_to([px(CUT), y + 1.95, 0], UP, buff=0.1)
    no = t("deny", label_size, ACCENT, weight="BOLD").move_to([px(0.88), y + 1.65, 0])
    yes = t("approve", label_size, TEAL, weight="BOLD").move_to([px(CUT / 2), y + 1.65, 0])
    cap = t("predicted risk of default", 18, MUTED).move_to([px(0.5), y - 0.7, 0])
    return VGroup(zone, axis, ticks, cut, cut_l, no, yes, cap), px


def marker(label, r, px, y, color, row, nd=0):
    """A dot on the risk axis; its label sits beside the stem top, on the side away from the cutoff line
    (row 0 or 1 staggers two labels)."""
    d = Dot([px(r), y, 0], radius=0.13, color=color)
    stem = Line([px(r), y, 0], [px(r), y + 0.45 + 0.5 * row, 0], color=color, stroke_width=3)
    lab = t(f"{label} {pct(r, nd)}", 20, color, weight="BOLD")
    side = RIGHT if r >= CUT else LEFT
    lab.next_to(stem.get_top(), side, buff=0.1)
    return VGroup(stem, d, lab)


def reason_bars(contrib, top, x0, y_top, max_w, row_h=0.62, size=21):
    """Horizontal bars, one per feature, sorted by push toward 'no'. Top-3 in ACCENT."""
    order = sorted(FEATS, key=lambda f: -contrib[f])
    vmax = max(contrib.values())
    rows = VGroup()
    for i, f in enumerate(order):
        v = contrib[f]
        y = y_top - i * row_h
        col = ACCENT if f in top else GHOST
        lab = t(LABEL[f], size, INK if f in top else MUTED, weight="BOLD" if f in top else "NORMAL")
        lab.move_to([x0 - 0.15, y, 0], aligned_edge=RIGHT)
        w = max(abs(v) / vmax * max_w, 0.04)
        bar = Rectangle(width=w, height=row_h * 0.62, fill_color=col, fill_opacity=1, stroke_width=0)
        bar.move_to([x0 + w / 2, y, 0])
        val = t(f"+{v:.2f}" if v >= 0 else f"−{abs(v):.2f}", size - 2, INK if f in top else MUTED, MONO)
        val.next_to(bar, RIGHT, buff=0.12)
        rank = t(str(top.index(f) + 1) if f in top else "", size, ON_DARK, weight="BOLD")
        badge = VGroup()
        if f in top:
            c = Circle(radius=0.19, fill_color=ACCENT, fill_opacity=1, stroke_width=0).next_to(lab, LEFT, buff=0.12)
            badge = VGroup(c, rank.move_to(c))
        rows.add(VGroup(lab, bar, val, badge))
    base = Line([x0, y_top + row_h / 2, 0], [x0, y_top - (len(FEATS) - 0.5) * row_h, 0], color=INK, stroke_width=3)
    return rows, base


# ======================================================================== B20 =
class B20_Rule(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        hd = header("what the rule asks for · US lending · not legal advice", "A denial needs specific reasons")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        # left: Regulation B
        L = card(6.4, 4.5).move_to([-2.95, -0.75, 0])
        law = VGroup(t("Equal Credit Opportunity Act", 26, INK, weight="BOLD"),
                     t("Regulation B · 12 CFR 1002.9(b)(2)", 20, MUTED, MONO)).arrange(DOWN, aligned_edge=LEFT,
                                                                                       buff=0.08)
        quote = VGroup(t("reasons “must be specific and indicate", 26, INK, SERIF),
                       t("the principal reason(s)” for a denial", 26, INK, SERIF)).arrange(DOWN, aligned_edge=LEFT,
                                                                                           buff=0.06)
        ok_mark = t("✓", 30, TEAL, weight="BOLD")
        no_mark = t("✗", 30, ACCENT, weight="BOLD")
        ok = VGroup(ok_mark, VGroup(t("“debt payments too high for income”", 21, INK, weight="BOLD"),
                                    t("specific", 18, TEAL)).arrange(DOWN, aligned_edge=LEFT, buff=0.03)
                    ).arrange(RIGHT, buff=0.2, aligned_edge=UP)
        bad = VGroup(no_mark, VGroup(t("“you failed to reach our score”", 21, INK, weight="BOLD"),
                                     t("named in the rule as not enough", 18, ACCENT)).arrange(
            DOWN, aligned_edge=LEFT, buff=0.03)).arrange(RIGHT, buff=0.2, aligned_edge=UP)
        body = VGroup(law, quote, ok, bad).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        fit(body, 5.8).move_to(L)

        # right: the circular on a short timeline
        R = card(4.9, 4.5, fill=DARK).move_to([3.75, -0.75, 0])

        def event(year, a, b):
            return VGroup(t(year, 26, ON_DARK, SERIF, weight="BOLD"),
                          VGroup(t(a, 20, ON_DARK, weight="BOLD"), t(b, 18, ON_DARK_MUTED)).arrange(
                              DOWN, aligned_edge=LEFT, buff=0.04)).arrange(DOWN, aligned_edge=LEFT, buff=0.06)

        e1 = event("2022", "CFPB Circular 2022-03", "same duty for complex algorithms")
        e2 = event("2025", "circular withdrawn", "with dozens of other guidance papers")
        e3 = event("2026", "Regulation B wording", "still in the rule book")
        ev = VGroup(e1, e2, e3).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        fit(ev, 4.3).move_to(R)
        foot = t("what the rule asks for, not legal advice", 20, MUTED).move_to([0, -3.13, 0])

        clock.play_at(0.3, FadeIn(ghost_of(L)), FadeIn(ghost_of(R, DARK_GHOST)), run_time=0.5)
        clock.play_at(cue("B20", "In the US", 2.0), FadeIn(L), FadeIn(law, shift=UP * 0.1), run_time=0.6)
        clock.play_at(cue("B20", "says a denied", 5.0), FadeIn(quote, shift=UP * 0.1), FadeIn(ok), run_time=0.6)
        clock.play_at(cue("B20", "You failed", 9.0), FadeIn(bad, shift=UP * 0.1), run_time=0.6)
        clock.play_at(cue("B20", "In twenty twenty-two", 12.0), FadeIn(R), FadeIn(e1, shift=UP * 0.1), run_time=0.6)
        clock.play_at(cue("B20", "It was withdrawn", 16.0), FadeIn(e2, shift=UP * 0.1), run_time=0.5)
        clock.play_at(cue("B20", "but the regulation", 18.0), FadeIn(e3, shift=UP * 0.1), run_time=0.5)
        clock.play_at(cue("B20", "That's what", 20.0), FadeIn(foot), run_time=0.5)
        clock.finish()


# ======================================================================== B30 =
class B30_Models(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        hd = header("my experiment · synthetic applicants, made up in code",
                    f"{SET['n_applicants']:,} synthetic applicants")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        # left: the five features with the average applicant
        L = card(5.3, 4.5).move_to([-3.45, -0.75, 0])
        lt = VGroup(t("5 plain features", 24, INK, weight="BOLD"),
                    t("average applicant", 18, MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.04)
        rows = VGroup()
        for f in FEATS:
            rows.add(VGroup(t(LABEL[f], 24, INK, weight="BOLD"), t(avg_value(f), 22, TEAL, MONO)))
        for r in rows:
            r[1].move_to([0, 0, 0])
        col = VGroup(*[r[0] for r in rows]).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        for r in rows:
            r[1].next_to(r[0], RIGHT, buff=0.3).set_x(1.9, direction=LEFT)
        hint = t("no protected traits · fairness: another video", 18, MUTED)
        lbody = VGroup(lt, VGroup(*rows), hint).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        fit(lbody, 4.8).move_to(L)

        # right: two model cards
        def model_card(title, sub, art, fill, ink, ink2):
            c = card(3.15, 3.15, fill=fill)
            g = VGroup(art, t(title, 26, ink, SERIF, weight="BOLD"), t(sub, 17, ink2)).arrange(DOWN, buff=0.18)
            return VGroup(c, fit(g, 2.8).move_to(c))

        ws = MOD["scorecard"]["weights_per_sd"]   # |weight| per standard deviation, from the fitted scorecard
        wmax = max(abs(v) for v in ws.values())
        wbars = VGroup(*[Rectangle(width=0.32, height=0.12 + 1.0 * abs(ws[f]) / wmax, fill_color=TEAL,
                                   fill_opacity=1, stroke_width=0) for f in FEATS]).arrange(RIGHT, buff=0.1,
                                                                                            aligned_edge=DOWN)
        sc_art = VGroup(wbars, t("one weight per feature", 17, MUTED)).arrange(DOWN, buff=0.1)

        def tree(s=0.32):
            n0 = Dot([0, 0, 0], radius=0.06, color=ON_DARK)
            pts = [[-s, -s, 0], [s, -s, 0], [-1.5 * s, -2 * s, 0], [-0.5 * s, -2 * s, 0], [0.5 * s, -2 * s, 0],
                   [1.5 * s, -2 * s, 0]]
            ds = VGroup(*[Dot(p, radius=0.05, color=ON_DARK) for p in pts])
            ls = VGroup(Line(n0.get_center(), pts[0], color=ON_DARK, stroke_width=2),
                        Line(n0.get_center(), pts[1], color=ON_DARK, stroke_width=2),
                        *[Line(pts[0], pts[k], color=ON_DARK, stroke_width=2) for k in (2, 3)],
                        *[Line(pts[1], pts[k], color=ON_DARK, stroke_width=2) for k in (4, 5)])
            return VGroup(ls, n0, ds)

        trees = VGroup(*[tree() for _ in range(3)]).arrange(RIGHT, buff=0.18)
        bb_art = VGroup(trees, t("300 trees, added up", 17, ON_DARK_MUTED)).arrange(DOWN, buff=0.3)
        m1 = model_card("Scorecard", "logistic regression", sc_art, PANEL, INK, MUTED)
        m2 = model_card("Black box", "gradient-boosted trees", bb_art, DARK, ON_DARK, ON_DARK_MUTED)
        models = VGroup(m1, m2).arrange(RIGHT, buff=0.3).move_to([2.95, -0.1, 0])
        auc = VGroup(t(f"test AUC {MOD['scorecard']['test_auc']:.2f}", 22, TEAL, MONO, weight="BOLD")
                     .next_to(m1, DOWN, buff=0.22),
                     t(f"test AUC {MOD['boosted']['test_auc']:.2f}", 22, TEAL, MONO, weight="BOLD")
                     .next_to(m2, DOWN, buff=0.22))
        auc_c = t("AUC: how well risky applicants rank above safe ones (1 = perfect)", 18, MUTED)
        fit(auc_c, 6.6).next_to(models, DOWN, buff=0.75)

        clock.play_at(0.3, FadeIn(ghost_of(L)), FadeIn(ghost_of(m1[0])), FadeIn(ghost_of(m2[0], GHOST)),
                      run_time=0.5)
        clock.play_at(cue("B30", "I made twenty", 1.5), FadeIn(L), FadeIn(lt), run_time=0.5)
        clock.play_at(cue("B30", "income", 4.0), LaggedStart(*[FadeIn(r, shift=RIGHT * 0.1) for r in rows],
                                                              lag_ratio=0.35), run_time=2.4)
        clock.play_at(cue("B30", "No protected", 10.0), FadeIn(hint), run_time=0.5)
        clock.play_at(cue("B30", "a simple scorecard", 13.0), FadeIn(m1, shift=UP * 0.1), run_time=0.6)
        clock.play_at(cue("B30", "gradient-boosted", 15.0), FadeIn(m2, shift=UP * 0.1), run_time=0.6)
        clock.play_at(cue("B30", "On test data", 17.0), FadeIn(auc), FadeIn(auc_c), run_time=0.6)
        clock.finish()


# ======================================================================== B40 =
class B40_ApplicantA(Scene):
    def construct(self):
        clock = Clock(self, "B40")
        hd = header("applicant A · also made up", "Meet Applicant A")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        L = card(5.0, 4.6).move_to([-3.6, -0.7, 0])
        tag = VGroup(t("A", 40, ON_DARK, SERIF, weight="BOLD"))
        disc = Circle(radius=0.36, fill_color=DARK, fill_opacity=1, stroke_width=0)
        badge = VGroup(disc, tag.move_to(disc))
        name = t("Applicant A", 28, INK, SERIF, weight="BOLD")
        top = VGroup(badge, name).arrange(RIGHT, buff=0.25)
        rows = VGroup()
        order = ["dti", "util", "missed", "history", "income"]
        for f in order:
            rows.add(VGroup(t(LABEL[f], 21, MUTED), t(a_value(f), 25, INK, weight="BOLD")).arrange(
                DOWN, aligned_edge=LEFT, buff=0.12))
        grid = VGroup(*rows).arrange_in_grid(rows=3, cols=2, buff=(0.45, 0.28), flow_order="dr",
                                             col_alignments="ll")
        lbody = VGroup(top, grid).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        fit(lbody, 4.5).move_to(L)

        meter, px = risk_meter(5.0, 0.55, -2.15)
        rsc = A["risk_scorecard"]
        rbb = A["risk_boosted"]
        m_sc = marker("scorecard", rsc, px, -2.15, INK, 0)
        m_bb = marker("black box", rbb, px, -2.15, DARK, 1)
        stamp_t = t("BOTH SAY NO", 34, ON_DARK, weight="BOLD")
        stamp = VGroup(RoundedRectangle(width=stamp_t.width + 0.6, height=0.8, corner_radius=0.1, fill_color=ACCENT,
                                        fill_opacity=1, stroke_width=0), stamp_t)
        stamp_t.move_to(stamp[0])
        stamp.move_to([3.05, 1.25, 0])

        clock.play_at(0.3, FadeIn(ghost_of(L)), FadeIn(meter[1].copy().set_color(GHOST)), run_time=0.5)
        clock.play_at(0.6, FadeIn(L), FadeIn(top), run_time=0.5)
        for i, p in enumerate(["Debt payments", "Cards are", "One missed", "four years", "One missed"]):
            if i == 4:
                continue
            clock.play_at(max(clock.t, cue("B40", p, 2.0 + 2 * i)), FadeIn(rows[i], shift=UP * 0.08), run_time=0.4)
        clock.play_at(clock.t, FadeIn(rows[4], shift=UP * 0.08), run_time=0.4)
        clock.play_at(cue("B40", "My chosen line", 10.0), FadeIn(meter), run_time=0.7)
        clock.play_at(cue("B40", "The scorecard puts", 14.0), FadeIn(m_sc, shift=DOWN * 0.1), run_time=0.6)
        clock.play_at(cue("B40", "the black box", 16.5), FadeIn(m_bb, shift=DOWN * 0.1), run_time=0.6)
        clock.play_at(cue("B40", "Both say no", 18.5), FadeIn(stamp, scale=1.15), run_time=0.5)
        clock.finish()


# ======================================================================== B50 =
class B50_Scorecard(Scene):
    def construct(self):
        clock = Clock(self, "B50")
        hd = header("the scorecard · exact reasons", "Five multiplications")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        form = svg("eq_push_ink.svg", width=7.6)
        form.move_to([-1.85, 1.0, 0])
        form_box = SurroundingRectangle(form, color=GHOST, buff=0.2, corner_radius=0.1, stroke_width=3)
        rows, base = reason_bars(SC["contrib"], SC["top3"], -3.0, 0.0, 3.6)
        cap = t("push toward “no” (log-odds) · applicant A vs the average applicant", 18, MUTED)
        fit(cap, 6.0).move_to([-3.1, -3.13, 0])
        ghosts = VGroup(*[ghost_of(r[1]) for r in rows])

        R = card(4.3, 3.9, fill=DARK).move_to([4.05, -1.25, 0])
        rt = t("reasons on the notice", 21, ON_DARK_MUTED)
        wrap = {"dti": "debt payments too high\nfor income", "util": "card balances near\ntheir limits",
                "missed": "recent missed\npayments"}
        items = VGroup(*[VGroup(t(str(i + 1), 32, ON_DARK, SERIF, weight="BOLD"),
                                t(wrap[f], 22, ON_DARK, weight="BOLD", line_spacing=0.9)).arrange(
            RIGHT, buff=0.22, aligned_edge=UP) for i, f in enumerate(SC["top3"])]).arrange(DOWN, aligned_edge=LEFT,
                                                                                         buff=0.3)
        rbody = VGroup(rt, items).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        fit(rbody, 3.8).move_to(R)

        clock.play_at(0.3, FadeIn(form_box), FadeIn(ghosts), FadeIn(ghost_of(R, DARK_GHOST)), run_time=0.5)
        clock.play_at(cue("B50", "Each feature's push", 2.5), FadeIn(form), FadeOut(form_box), run_time=0.7)
        clock.play_at(cue("B50", "Five multiplications", 7.0), Create(base),
                      LaggedStart(*[AnimationGroup(FadeIn(r[0]), GrowFromEdge(r[1], LEFT), FadeIn(r[2]))
                                    for r in rows], lag_ratio=0.25), FadeOut(ghosts), FadeIn(cap), run_time=1.6)
        clock.play_at(cue("B50", "The top three", 10.0), FadeIn(R), FadeIn(rt),
                      LaggedStart(*[FadeIn(r[3], scale=0.6) for r in rows], lag_ratio=0.2), run_time=0.7)
        for i, p in enumerate(["debt payments too", "cards near", "and a recent"]):
            clock.play_at(max(clock.t, cue("B50", p, 11.0 + 1.5 * i)), FadeIn(items[i], shift=RIGHT * 0.1),
                          run_time=0.45)
        clock.finish()


# ======================================================================== B60 =
class B60_BlackBox(Scene):
    def construct(self):
        clock = Clock(self, "B60")
        hd = header("the black box · Shapley values", f"{BB['model_runs']:,} model runs for one person")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        # left: how + the bars
        how = VGroup(t(f"{2 ** len(FEATS)} combinations of A's features", 21, INK, weight="BOLD"),
                     t(f"× {SET['n_background']} other applicants", 21, INK, weight="BOLD"),
                     t(f"= {BB['model_runs']:,} runs of the model", 21, ACCENT, weight="BOLD")).arrange(
            DOWN, aligned_edge=LEFT, buff=0.06)
        how.move_to([-3.4, 1.15, 0])
        rows, base = reason_bars(BB["contrib"], BB["top3"], -3.0, -0.3, 2.6, row_h=0.55, size=20)
        ghosts = VGroup(*[ghost_of(r[1]) for r in rows])
        cite = t("method: Lundberg & Lee, NeurIPS 2017", 18, MUTED).move_to([-3.1, -3.13, 0])

        # right: compare the two top-3 lists
        R = card(5.0, 3.0).move_to([3.55, 0.45, 0])

        def col(title, top, other, color):
            items = VGroup(t(title, 22, color, weight="BOLD"))
            for i, f in enumerate(top):
                shared = f in other
                items.add(t(f"{i + 1}  {LABEL[f]}", 21, INK if shared else MUTED,
                            weight="BOLD" if shared else "NORMAL"))
            return items.arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        c1 = col("scorecard", SC["top3"], BB["top3"], TEAL)
        c2 = col("black box", BB["top3"], SC["top3"], ACCENT)
        cols = VGroup(c1, c2).arrange(RIGHT, buff=0.5, aligned_edge=UP)
        n = REA["agreement"]["n_shared"]
        verdict = t(f"{n} of 3 reasons shared", 28, INK, SERIF, weight="BOLD")
        rbody = VGroup(cols, verdict).arrange(DOWN, buff=0.4)
        fit(rbody, 4.5).move_to(R)

        sh = REA["boosted_vs_approved_background"]["top3"]
        rt = REA["boosted_retrained_other_split"]["top3"]
        assert "dti" in sh and "dti" in rt
        shift = VGroup(t("the black box's list can shift", 22, ACCENT, weight="BOLD"),
                       t("vs approved applicants only:", 20, MUTED),
                       t(f"debt-to-income back in top 3 (#{sh.index('dti') + 1})", 21, INK, weight="BOLD"),
                       t("retrained on another 70% of the data:", 20, MUTED),
                       t(f"debt-to-income back in top 3 (#{rt.index('dti') + 1})", 21, INK, weight="BOLD")).arrange(
            DOWN, aligned_edge=LEFT, buff=0.06)
        shift[3].shift(DOWN * 0.12)
        shift[4].shift(DOWN * 0.12)
        fit(shift, 5.0).next_to(R, DOWN, buff=0.3).align_to(R, LEFT).shift(RIGHT * 0.2)

        clock.play_at(0.3, FadeIn(ghosts), FadeIn(ghost_of(R)), run_time=0.5)
        clock.play_at(cue("B60", "So I computed", 2.5), FadeIn(how[0]), run_time=0.5)
        clock.play_at(cue("B60", "against five", 5.0), FadeIn(how[1]), run_time=0.4)
        clock.play_at(cue("B60", "Sixteen thousand", 7.5), FadeIn(how[2], scale=1.1), FadeIn(cite), run_time=0.5)
        clock.play_at(cue("B60", "Its top three", 10.0), Create(base),
                      LaggedStart(*[AnimationGroup(FadeIn(r[0]), GrowFromEdge(r[1], LEFT), FadeIn(r[2]),
                                                   FadeIn(r[3])) for r in rows], lag_ratio=0.25),
                      FadeOut(ghosts), run_time=1.5)
        clock.play_at(cue("B60", "Two of three", 15.0), FadeIn(R), FadeIn(cols), run_time=0.6)
        clock.play_at(clock.t + 0.3, FadeIn(verdict, shift=UP * 0.1), run_time=0.5)
        clock.play_at(cue("B60", "And the list", 18.0), FadeIn(shift[0]), run_time=0.4)
        clock.play_at(cue("B60", "compare A with", 19.5), FadeIn(shift[1:3], shift=UP * 0.08), run_time=0.4)
        clock.play_at(cue("B60", "or retrain", 21.0), FadeIn(shift[3:], shift=UP * 0.08), run_time=0.4)
        clock.finish()


# ======================================================================== B70 =
class B70_Change(Scene):
    def construct(self):
        clock = Clock(self, "B70")
        hd = header("what would change the answer · one change, all else equal", "Pay the cards down")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        lim = SET["card_limit"]
        u0 = AV["util"] / 100
        u1 = CF["both_approve_util"] / 100
        pay = CF["both_approve_paydown"]
        # left: card balance bar
        x0, w, y = -6.0, 5.4, -0.35
        frame = Rectangle(width=w, height=0.8, stroke_color=INK, stroke_width=3, fill_opacity=0).move_to(
            [x0 + w / 2, y, 0])
        fill0 = Rectangle(width=w * u0, height=0.8, fill_color=ACCENT, fill_opacity=1, stroke_width=0).move_to(
            [x0 + w * u0 / 2, y, 0])
        fill1 = Rectangle(width=w * u1, height=0.8, fill_color=TEAL, fill_opacity=1, stroke_width=0).move_to(
            [x0 + w * u1 / 2, y, 0])
        ttl = VGroup(t("card balances", 24, INK, weight="BOLD"),
                     t(f"limit ${lim:,} (assumed)", 18, MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.04)
        ttl.next_to(frame, UP, buff=0.25).align_to(frame, LEFT)
        lab0 = t(f"${lim * u0:,.0f} · {AV['util']:.0f}%", 24, ACCENT, MONO, weight="BOLD")
        lab0.next_to(frame, DOWN, buff=0.2).align_to(frame, LEFT)
        lab1 = t(f"${lim * u1:,.0f} · {CF['both_approve_util']:.0f}%", 24, TEAL, MONO, weight="BOLD")
        lab1.next_to(frame, DOWN, buff=0.2).align_to(frame, LEFT)
        payl = VGroup(t(f"pay down ${pay:,}", 34, INK, SERIF, weight="BOLD"),
                      t("keep everything else the same", 19, MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.05)
        payl.next_to(lab1, DOWN, buff=0.35).align_to(frame, LEFT)

        my = -1.85
        meter, px = risk_meter(5.0, 0.9, my)
        ra = CF["risk_after"]
        m_sc0 = marker("scorecard", A["risk_scorecard"], px, my, INK, 0)
        m_bb0 = marker("black box", A["risk_boosted"], px, my, DARK, 1)
        # after the change both sit left of the line: the one nearer the line gets the higher label
        m_sc1 = marker("scorecard", ra["scorecard"], px, my, TEAL, int(ra["scorecard"] > ra["boosted"]), nd=1)
        m_bb1 = marker("black box", ra["boosted"], px, my, TEAL, int(ra["boosted"] >= ra["scorecard"]), nd=1)
        yes_t = t("BOTH SAY YES", 30, ON_DARK, weight="BOLD")
        yes = VGroup(RoundedRectangle(width=yes_t.width + 0.6, height=0.72, corner_radius=0.1, fill_color=TEAL,
                                      fill_opacity=1, stroke_width=0), yes_t)
        yes_t.move_to(yes[0])
        yes.move_to([px(0.5), 1.45, 0])
        limits = VGroup(t("limits:", 19, MUTED, weight="BOLD"),
                        t("synthetic applicants · a cutoff I chose · Shapley values are one method of several",
                          19, MUTED)).arrange(RIGHT, buff=0.15)
        fit(limits, 12.4).move_to([0, -3.13, 0])

        clock.play_at(0.3, FadeIn(frame.copy().set_stroke(GHOST)), FadeIn(meter[1].copy().set_color(GHOST)),
                      run_time=0.5)
        clock.play_at(0.8, Create(frame), FadeIn(ttl), FadeIn(fill0), FadeIn(lab0), FadeIn(meter), FadeIn(m_sc0),
                      FadeIn(m_bb0), run_time=0.8)
        clock.play_at(cue("B70", "pay card balances", 3.0), Transform(fill0, fill1), Transform(lab0, lab1),
                      FadeIn(payl, shift=UP * 0.1), run_time=1.4)
        clock.play_at(cue("B70", "Both models now", 8.0), Transform(m_sc0, m_sc1), Transform(m_bb0, m_bb1),
                      run_time=1.0)
        clock.play_at(clock.t, FadeIn(yes, scale=1.1), run_time=0.5)
        clock.play_at(cue("B70", "Limits", 14.0), FadeIn(limits, shift=UP * 0.1), run_time=0.5)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = t("Why Did the AI Say No?", 80, INK, SERIF)
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
        c3 = t("Data: synthetic applicants made in code · Rule: Regulation B, 12 CFR 1002.9 · "
               "Method: Shapley values (Lundberg & Lee, 2017)", 20, MUTED)
        c3.scale_to_fit_width(min(c3.width, 11.8))
        c4 = t("Narration: AI voice (Kokoro am_onyx) reading Boopesh's script · not legal advice", 24, MUTED)
        c4.scale_to_fit_width(min(c4.width, 11.8))
        credit = VGroup(c1, c2, c3, c4).arrange(DOWN, buff=0.2).next_to(rule, DOWN, buff=0.45)
        dim = VGroup(rule, credit).copy().set_opacity(0.18)
        clock.play_at(clock.t, FadeIn(dim), run_time=0.3)
        clock.play_at(max(clock.t, cue("B90", "With Boopesh", 1.5)), FadeOut(dim), Create(rule),
                      FadeIn(credit, shift=UP * 0.1), run_time=0.7)
        clock.finish()
