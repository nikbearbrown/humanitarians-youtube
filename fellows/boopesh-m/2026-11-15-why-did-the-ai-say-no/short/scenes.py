# -*- coding: utf-8 -*-
"""
Manim scenes for the 9:16 Short of "Why Did the AI Say No?" (2160x3840) -- Boopesh M.
  B10_Denied   -- the rule (Regulation B: specific principal reasons) + Applicant A denied by both models
  B20_Reasons  -- top 3 reasons: scorecard (exact) vs black box (Shapley, 16,000 runs); 2 of 3 shared
  B30_Change   -- pay cards down $3,850 -> both models say yes; limits
  B90_Outro    -- @HumanitariansAI outro + fellow credit
Native portrait layouts (frame 4.5 x 8 units). Numbers read from ../code/results.json (SYNTHETIC APPLICANTS).
"""
import json
from pathlib import Path

from manim import *

config.frame_width = 4.5
config.frame_height = 8.0

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"
CODE = HERE.parent / "code"
if not (CODE / "results.json").exists():   # isolated copies (static pre-flight) fall back to the reel's data
    CODE = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-11-15-why-did-the-ai-say-no/code")
if not (ASSETS / "hai-logo.svg").exists():
    ASSETS = CODE.parent / "short" / "assets"

BG = "#FAF9F5"
INK = "#2B2A26"
ACCENT = "#A64B2A"
MUTED = "#6F6A5E"
PANEL = "#EEEADF"
LINE = "#D9D3C4"
GHOST = "#A39A88"
TEAL = "#1F4E5F"
DARK = "#2B2A26"
ON_DARK = "#F5F1E8"
ON_DARK_MUTED = "#D8D0C0"

SERIF = "EB Garamond"
SANS = "Inter"
MONO = "DejaVu Sans Mono"

CX = -0.15
SAFE_W = 3.7

RES = json.loads((CODE / "results.json").read_text())
SET = RES["setup"]
A = RES["applicant_a"]
AV = A["values"]
REA = RES["reasons"]
SC = REA["scorecard"]
BB = REA["boosted"]
CF = RES["counterfactual"]
CUT = SET["cutoff"]
LABEL = {"income": "income", "dti": "debt-to-income", "missed": "missed payments",
         "history": "credit history", "util": "card use"}


def _sheet():
    try:
        return {b["beat_id"]: b for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}
    except Exception:
        return {}


BEATS = _sheet()


def beat_len(bid, default=8.0):
    b = BEATS.get(bid, {})
    return float(b.get("render_duration_s") or b.get("actual_duration_s") or default)


def cue(bid, phrase, default):
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

    def play_at(self, at, *anims, run_time=0.7, **kw):
        if at > self.t:
            self.scene.wait(at - self.t)
            self.t = at
        self.scene.play(*anims, run_time=run_time, **kw)
        self.t += run_time

    def finish(self):
        end = beat_len(self.bid)
        if end - self.t > 1 / 24:
            self.scene.wait(end - self.t)


TYPE_SCALE = 0.72
KERN = 4


def t(s, size=24, color=INK, font=SANS, weight="NORMAL", **kw):
    m = Text(s, font=font, font_size=size * TYPE_SCALE * KERN, color=color, weight=weight, **kw)
    return m.scale(1 / KERN)


def fit(m, w=SAFE_W):
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


def card(w, h, fill=PANEL):
    return RoundedRectangle(width=w, height=h, corner_radius=0.08, fill_color=fill,
                            fill_opacity=1, stroke_width=0)


def ghost_of(m, color=GHOST):
    return m.copy().set_fill(opacity=0).set_stroke(color, 2)


def pct(x, nd=0):
    return f"{100 * x:.{nd}f}%"


def header(kicker, title):
    k = fit(t(kicker.upper(), 13, MUTED, MONO))
    h = fit(t(title, 34, INK, SERIF, weight="BOLD", line_spacing=0.9))
    g = VGroup(k, h).arrange(DOWN, buff=0.12)
    g.move_to([CX, 3.1 - g.height / 2, 0])
    return g


def stamp(text, fill):
    lab = t(text, 26, ON_DARK, weight="BOLD")
    box = RoundedRectangle(width=lab.width + 0.4, height=0.55, corner_radius=0.08, fill_color=fill, fill_opacity=1,
                           stroke_width=0)
    return VGroup(box, lab.move_to(box))


def risk_tile(title, r, color, w=1.75, h=1.2, nd=0):
    c = card(w, h)
    g = VGroup(t(title, 16, MUTED), t(pct(r, nd), 40, color, SERIF, weight="BOLD")).arrange(DOWN, buff=0.04)
    return VGroup(c, fit(g, w - 0.2).move_to(c))


# ======================================================================== B10 =
class B10_Denied(Scene):
    def construct(self):
        clock = Clock(self, "B10")
        hd = header("the rule · US lending · not legal advice", "A denial needs\nspecific reasons")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        rule = card(SAFE_W, 1.25, fill=DARK).move_to([CX, 1.35, 0])
        rq = VGroup(t("reasons “must be specific and", 19, ON_DARK, SERIF),
                    t("indicate the principal reason(s)”", 19, ON_DARK, SERIF),
                    t("Regulation B · 12 CFR 1002.9(b)(2)", 13, ON_DARK_MUTED, MONO)).arrange(DOWN, buff=0.05)
        fit(rq, SAFE_W - 0.3).move_to(rule)
        no = VGroup(t("✗", 22, ACCENT, weight="BOLD"), t("“the model said no”", 20, INK, weight="BOLD")).arrange(
            RIGHT, buff=0.12)
        no.next_to(rule, DOWN, buff=0.18).set_x(CX)

        # Applicant A
        a_card = card(SAFE_W, 1.35).move_to([CX, -0.45, 0])
        a_t = t("Applicant A (made up)", 19, INK, SERIF, weight="BOLD")
        a_l = VGroup(t(f"debt {AV['dti']:.0f}% of income · cards {AV['util']:.0f}% used", 16, INK),
                     t(f"{AV['missed']:.0f} missed payment · {AV['history']:.0f} yrs history · "
                       f"${AV['income']:.0f}k", 16, INK)).arrange(DOWN, buff=0.06)
        a_g = VGroup(a_t, a_l).arrange(DOWN, buff=0.12)
        fit(a_g, SAFE_W - 0.3).move_to(a_card)

        t1 = risk_tile("scorecard risk", A["risk_scorecard"], ACCENT)
        t2 = risk_tile("black box risk", A["risk_boosted"], ACCENT)
        tiles = VGroup(t1, t2).arrange(RIGHT, buff=0.2).move_to([CX, -1.95, 0])
        line = t(f"lender's line {pct(CUT)} (my choice)", 15, MUTED).next_to(tiles, DOWN, buff=0.12).set_x(CX)
        st = stamp("BOTH SAY NO", ACCENT).move_to([CX, 2.6, 0])

        clock.play_at(0.3, FadeIn(ghost_of(rule, "#5E544C")), FadeIn(ghost_of(a_card)),
                      FadeIn(ghost_of(VGroup(t1[0], t2[0]))), run_time=0.4)
        clock.play_at(0.6, FadeIn(rule), FadeIn(rq), run_time=0.5)
        clock.play_at(cue("B10", "The model said", 3.0), FadeIn(no, shift=UP * 0.08), run_time=0.4)
        clock.play_at(cue("B10", "My made-up", 5.0), FadeIn(a_card), FadeIn(a_g), run_time=0.5)
        clock.play_at(cue("B10", "a simple scorecard", 8.0), FadeIn(t1), FadeIn(line), run_time=0.4)
        clock.play_at(cue("B10", "and a black box", 9.3), FadeIn(t2), run_time=0.4)
        clock.play_at(clock.t + 0.1, FadeOut(hd), FadeIn(st, scale=1.1), run_time=0.4)
        clock.finish()


# ======================================================================== B20 =
class B20_Reasons(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        hd = header("applicant A · top 3 reasons", "Two models,\ntwo lists")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        def block(title, sub, top, other, contrib, color, y):
            c = card(SAFE_W, 1.75).move_to([CX, y, 0])
            head = VGroup(t(title, 22, color, weight="BOLD"), t(sub, 14, MUTED)).arrange(RIGHT, buff=0.15,
                                                                                         aligned_edge=DOWN)
            vmax = max(contrib[f] for f in top)
            rows = VGroup()
            for i, f in enumerate(top):
                shared = f in other
                lab = t(f"{i + 1}  {LABEL[f]}", 19, INK if shared else MUTED,
                        weight="BOLD" if shared else "NORMAL")
                bar = Rectangle(width=1.1 * contrib[f] / vmax, height=0.16, fill_color=ACCENT if shared else GHOST,
                                fill_opacity=1, stroke_width=0)
                rows.add(VGroup(lab, bar))
            for r in rows:
                r[0].move_to([0, 0, 0], aligned_edge=LEFT)
                r[1].move_to([2.35, 0, 0], aligned_edge=LEFT)
            rows.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
            body = VGroup(head, rows).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
            fit(body, SAFE_W - 0.3).move_to(c)
            return VGroup(c, body)

        b1 = block("scorecard", "exact · 5 multiplications", SC["top3"], BB["top3"], SC["contrib"], TEAL, 0.75)
        b2 = block("black box", f"Shapley · {BB['model_runs']:,} model runs", BB["top3"], SC["top3"],
                   BB["contrib"], ACCENT, -1.15)
        n = REA["agreement"]["n_shared"]
        verdict = t(f"{n} of 3 reasons shared", 28, INK, SERIF, weight="BOLD").move_to([CX, -2.35, 0])

        clock.play_at(0.3, FadeIn(ghost_of(b1[0])), FadeIn(ghost_of(b2[0])), run_time=0.4)
        clock.play_at(cue("B20", "The scorecard", 0.6), FadeIn(b1, shift=UP * 0.08), run_time=0.5)
        clock.play_at(cue("B20", "The black box", 4.5), FadeIn(b2, shift=UP * 0.08), run_time=0.5)
        clock.play_at(cue("B20", "and shares only", 7.5), FadeIn(verdict, shift=UP * 0.08), run_time=0.4)
        clock.finish()


# ======================================================================== B30 =
class B30_Change(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        pay = CF["both_approve_paydown"]
        hd = header("what would change it · all else equal", f"Pay the cards\ndown ${pay:,}")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        lim = SET["card_limit"]
        u0, u1 = AV["util"] / 100, CF["both_approve_util"] / 100
        w, y = SAFE_W - 0.2, 1.05
        x0 = CX - w / 2
        cap = t(f"card balances · limit ${lim:,} (assumed)", 16, MUTED).move_to([CX, y + 0.62, 0])
        frame = Rectangle(width=w, height=0.6, stroke_color=INK, stroke_width=3, fill_opacity=0).move_to([CX, y, 0])
        f0 = Rectangle(width=w * u0, height=0.6, fill_color=ACCENT, fill_opacity=1, stroke_width=0).move_to(
            [x0 + w * u0 / 2, y, 0])
        f1 = Rectangle(width=w * u1, height=0.6, fill_color=TEAL, fill_opacity=1, stroke_width=0).move_to(
            [x0 + w * u1 / 2, y, 0])
        l0 = t(f"${lim * u0:,.0f} · {AV['util']:.0f}%", 22, ACCENT, MONO, weight="BOLD").move_to([CX, y - 0.6, 0])
        l1 = t(f"${lim * u1:,.0f} · {CF['both_approve_util']:.0f}%", 22, TEAL, MONO, weight="BOLD").move_to(
            [CX, y - 0.6, 0])

        ra = CF["risk_after"]
        a1 = risk_tile("scorecard risk", A["risk_scorecard"], ACCENT, nd=1)
        a2 = risk_tile("black box risk", A["risk_boosted"], ACCENT, nd=1)
        b1 = risk_tile("scorecard risk", ra["scorecard"], TEAL, nd=1)
        b2 = risk_tile("black box risk", ra["boosted"], TEAL, nd=1)
        VGroup(a1, a2).arrange(RIGHT, buff=0.2).move_to([CX, -0.75, 0])
        VGroup(b1, b2).arrange(RIGHT, buff=0.2).move_to([CX, -0.75, 0])
        line = t(f"lender's line {pct(CUT)} (my choice)", 15, MUTED).move_to([CX, -1.55, 0])
        st = stamp("BOTH SAY YES", TEAL).move_to([CX, -2.05, 0])
        lim_t = t("synthetic applicants · not legal advice", 14, MUTED).move_to([CX, -2.55, 0])

        clock.play_at(0.3, Create(frame), FadeIn(cap), FadeIn(f0), FadeIn(l0), FadeIn(a1), FadeIn(a2), FadeIn(line),
                      FadeIn(lim_t), run_time=0.5)
        clock.play_at(cue("B30", "Pay card balances", 1.5), Transform(f0, f1), Transform(l0, l1), run_time=1.2)
        clock.play_at(cue("B30", "and both models", 4.5), Transform(a1, b1), Transform(a2, b2), run_time=0.6)
        clock.play_at(clock.t, FadeIn(st, scale=1.1), run_time=0.4)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = fit(VGroup(t("Why Did the", 46, INK, SERIF), t("AI Say No?", 46, INK, SERIF)).arrange(DOWN, buff=0.12))
        pill_lab = t("SUBSCRIBE", 20, ON_DARK, SANS, weight="BOLD")
        pill = RoundedRectangle(width=pill_lab.width + 0.5, height=0.5, corner_radius=0.25,
                                fill_color=DARK, fill_opacity=1, stroke_width=0)
        pill_lab.move_to(pill)
        hai = svg("hai-logo.svg", height=0.42).set_color(INK)
        handle = t("@HumanitariansAI", 24, INK, SANS, weight="BOLD")
        row = VGroup(hai, handle).arrange(RIGHT, buff=0.2)
        main = VGroup(title, VGroup(pill, pill_lab), row).arrange(DOWN, buff=0.45).move_to([CX, 1.85, 0])
        clock.play_at(0.2, FadeIn(title, shift=UP * 0.1), FadeIn(ghost_of(VGroup(pill))), run_time=0.6)
        clock.play_at(clock.t, FadeIn(VGroup(pill, pill_lab)), FadeIn(row), run_time=0.5)
        rule = Line(LEFT * 1.4, RIGHT * 1.4, color=LINE, stroke_width=2).next_to(main, DOWN, buff=0.55).set_x(CX)
        credit = VGroup(t("Boopesh M.", 36, INK, SERIF, weight="BOLD"),
                        t("Humanitarians AI Fellow", 22, MUTED), t("Brutalist team", 22, MUTED),
                        fit(t("Narration: AI voice", 18, MUTED)), t("(Kokoro am_onyx)", 18, MUTED),
                        t("Data: synthetic applicants", 16, MUTED),
                        t("Rule: Regulation B · not legal advice", 16, MUTED)).arrange(DOWN, buff=0.17)
        credit.next_to(rule, DOWN, buff=0.3).set_x(CX)
        dim = VGroup(rule, credit).copy().set_opacity(0.18)
        clock.play_at(clock.t, FadeIn(dim), run_time=0.3)
        clock.play_at(max(clock.t, min(cue("B90", "With Boopesh", 1.5), 1.8)), FadeOut(dim), Create(rule),
                      FadeIn(credit), run_time=0.6)
        clock.finish()
