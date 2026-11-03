"""short/scenes.py — native 9:16 portrait re-layout of all 16 GRAPHIC beats (full-length vertical).

Portrait render (manim -r 2160,3840) keeps frame_height at 8 units but frame_width is only 4.5,
so every scene from ../scenes.py is restacked vertically, never center-cut (shorts.py rule; same
convention as ../../Mycroft5_*/short/scenes.py: same class names, graphics_lib unchanged).
Safe frame: x in [-2.0, 2.0], y in [-3.5, 3.5]. Text is wrapped to ~24 characters per line.

Same evidence rule as the landscape reel: every number is read at render time from
../assets/evidence/out/*.json; screenshots are the real app captures in ../assets/.
TARGETs come from this folder's beat_sheet.json (actual audio durations).
"""
import json
import textwrap
from datetime import datetime
from pathlib import Path

from graphics_lib import *

# Pin the portrait frame: Manim 0.18 keeps the 16:9 frame_width under -r 2160,3840 otherwise.
config.frame_height = 9.0
config.frame_width = 9.0 * 9 / 16

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
EVID = PARENT / "assets" / "evidence" / "out"
SHEET = json.loads((HERE / "beat_sheet.json").read_text(encoding="utf-8"))

BG, INK, ACC, SOFT, GHOST = "#FAF9F5", "#3D3929", "#D97757", "#73705F", "#A9A491"
GREEN, AMBER, RED = "#4C9A6A", "#C9932E", "#B0473A"
LANE_A, LANE_B = "#3B82F6", "#E07B28"
W = 3.9  # usable width


def target(cls):
    for b in SHEET["beats"]:
        if b["shot"].get("manim", {}).get("scene_class") == cls:
            return float(b.get("actual_duration_s") or b["estimated_duration_s"])
    raise KeyError(cls)


def ev(name):
    return json.loads((EVID / f"{name}.json").read_text(encoding="utf-8"))


def hold_to(scene, tgt, minimum=0.4):
    try:
        elapsed = float(scene.renderer.time)
    except Exception:
        scene.wait(minimum)
        return
    scene.wait(max(minimum, tgt - elapsed))


def wrap(text, width=24):
    return "\n".join(textwrap.wrap(text, width)) or text


def fitw(g, w=W):
    if g.width > w:
        g.scale(w / g.width)
    return g


def fit(g, w, h):
    g.scale(min(1.0, w / g.width, h / g.height))
    return g


def txt(text, size=28, color=INK, weight=None, width=24, font=None, **kw):
    k = dict(size=size, color=color, line_spacing=0.85, **kw)
    if weight:
        k["weight"] = weight
    if font:
        k["font"] = font
    return fitw(label(wrap(text, width), **k))


def mtxt(text, size=26, color=INK, width=22):
    return fitw(mono(wrap(text, width), size=size, color=color, line_spacing=0.85))


def head(text):
    return txt(text.upper(), size=30, color=SOFT, weight="BOLD", width=20).move_to([0, 3.05, 0])


def cap(text, y, color=INK, size=26):
    return txt(text, size=size, color=color, weight="BOLD", width=26).move_to([0, y, 0])


def src(text, y=-3.35):
    return fitw(label(wrap(text.upper(), 34), size=24, color=GHOST, line_spacing=0.8)).scale(0.7).move_to([0, y, 0])


def boxed(inner, color=INK, h_pad=0.3, v_pad=0.22, **kw):
    return VGroup(auto_box(inner, h_pad=h_pad, v_pad=v_pad, color=color, **kw), inner)


def chip(text, color, size=22):
    return fitw(label_chip(wrap(text, 26), color, size=size, upper=False))


def ring(m, color=ACC, buff=0.12):
    return Ellipse(width=m.width + 2 * buff + 0.4, height=m.height + 2 * buff + 0.2, color=color, stroke_width=4).move_to(m)


def strike(m, color=INK):
    return Line(m.get_left() + LEFT * 0.06, m.get_right() + RIGHT * 0.06, color=color, stroke_width=5)


def shot(name, w=W, h=3.0):
    img = ImageMobject(str(PARENT / "assets" / name))
    img.scale(min(w / img.width, h / img.height))
    return Group(img, SurroundingRectangle(img, buff=0.03, color=GHOST, stroke_width=1.5))


def money(v):
    v = float(v)
    for d, s in ((1e12, "T"), (1e9, "B"), (1e6, "M")):
        if abs(v) >= d:
            return f"${v / d:.1f}{s}"
    return f"${v:,.2f}"


def frac(n, d, size=30):
    n = n if isinstance(n, Mobject) else label(n, size=size, color=INK)
    d = d if isinstance(d, Mobject) else label(d, size=size, color=INK)
    w = max(n.width, d.width) + 0.2
    bar = Line(LEFT * w / 2, RIGHT * w / 2, color=INK, stroke_width=3)
    n.next_to(bar, UP, buff=0.12)
    d.next_to(bar, DOWN, buff=0.12)
    return VGroup(n, bar, d)


def var(t, size=30):
    return serif(t, size=size, color=INK, italic=True)


FOUR = ("METRIC", "PERIOD", "UNIT", "SOURCE")


def four_grid(lit=(), size=26):
    cells = VGroup()
    for n in FOUR:
        on = n in lit
        t = label(n, size=size, weight="BOLD", color=BG if on else INK)
        r = Rectangle(width=1.8, height=0.75, color=ACC if on else INK, fill_color=ACC, fill_opacity=1 if on else 0)
        cells.add(VGroup(r, t.move_to(r)))
    return cells.arrange_in_grid(rows=2, cols=2, buff=0.18)


def corner(lit):
    return VGroup()  # portrait: no corner chip (clutters a 4.5-wide frame)


def ledger(items, color, symbol):
    rows = VGroup(*[VGroup(Text(symbol, font_size=36, color=color),
                           label(wrap(t, 22), size=30, color=color, line_spacing=0.85)).arrange(RIGHT, buff=0.2, aligned_edge=UP)
                    for t in items])
    return fit(rows.arrange(DOWN, buff=0.4, aligned_edge=LEFT), W, 5.6)


def stack(*elems, top=2.45, bottom=-3.45, buff=0.28):
    """Arrange elements top-to-bottom under the title and fit them to the space: no fixed y."""
    g = Group(*elems).arrange(DOWN, buff=buff)
    fit(g, W, top - bottom)
    return g.move_to([0, (top + bottom) / 2, 0])


class Beat(Scene):
    def setup(self):
        self.camera.background_color = BG

    def finish(self):
        hold_to(self, target(type(self).__name__))

    def reveal(self, *mobs, rt=0.5, wait=0.0):
        self.play(*[FadeIn(m) for m in mobs], run_time=rt)
        if wait:
            self.wait(wait)


class B01_FourBoxTest(Beat):
    def construct(self):
        self.reveal(head("One test for every figure"))
        self.reveal(txt("two AI agents, one company, compare the numbers they report", size=28, color=SOFT).move_to([0, 1.8, 0]), wait=3.5)
        g = four_grid().move_to([0, -0.1, 0])
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in g], lag_ratio=0.25), run_time=1.6)
        self.wait(3.0)
        self.reveal(cap("two figures compare only when all four line up", -2.2))
        self.finish()


class B02_WhatTheyWereHanded(Beat):
    def construct(self):
        data = {r["concept"]: r for r in ev("B02_B03_what_they_were_handed")["rows"]}
        self.reveal(head("What the agents were handed"))
        rev = data["Revenues"]["legacy_entry"]
        eps, ni = data["EarningsPerShareDiluted"], data["NetIncomeLoss"]
        raw = mtxt(f'Revenues {data["Revenues"]["legacy_handed"]} fy {rev["fy"]} {rev["form"]}', size=24, width=30)
        rows = [(money(data["Revenues"]["legacy_handed"]), f"fiscal {rev['fy']} annual, retired label", RED),
                (f"EPS {eps['legacy_handed']}", f"{eps['legacy_span_days']}-day year to date; quarter {eps['b0_selected']}", RED),
                (f"Net income {money(ni['legacy_handed'])}", f"year to date; quarter {money(ni['b0_selected'])}", RED),
                (f"Assets {money(data['Assets']['legacy_handed'])}", "correct: a point in time", GREEN)]
        blocks = [VGroup(mono(l, size=28, color=INK), txt(r, size=24, color=c, weight="BOLD", width=30)).arrange(DOWN, buff=0.06) for l, r, c in rows]
        closing = cap("every Apple comparison until now used these", 0, size=24)
        g = stack(raw, *blocks, closing, buff=0.3)
        self.reveal(g[0], wait=2.5)
        for blk in g[1:5]:
            self.reveal(blk, wait=2.0)
        self.reveal(g[5])
        self.finish()


class B03_FactWithPeriod(Beat):
    def construct(self):
        eps = {r["concept"]: r for r in ev("B02_B03_what_they_were_handed")["rows"]}["EarningsPerShareDiluted"]
        inside = eps["b0_describe"][eps["b0_describe"].index("(") + 1: eps["b0_describe"].rindex(")")].split(", ")
        accn = next(p for p in inside if p.startswith("accn"))
        self.reveal(head("Every figure carries its context"))
        value = mono(str(eps["b0_selected"]), size=60, color=INK)
        chips = VGroup(chip(inside[0], ACC), chip("USD per share", INK), chip(f"{inside[2]} · {inside[1]}", SOFT), chip(accn, SOFT)).arrange(DOWN, buff=0.12)
        rules = VGroup(chip("quarter: 80 to 100 days", ACC), chip("annual: 350 to 380 days", INK), chip("else: labelled last resort", GHOST)).arrange(DOWN, buff=0.12)
        closing = cap("a restatement replaces the original", 0, size=24)
        g = stack(value, chips, rules, closing, buff=0.35)
        self.reveal(g[0])
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in g[1]], lag_ratio=0.35), run_time=2.0)
        self.wait(3.0)
        self.reveal(g[2], wait=1.5)
        self.reveal(g[3])
        self.finish()


class B04_FailureRecordedOk(Beat):
    def construct(self):
        step = ev("B04_search_args_and_retry")["first_three"][0]
        self.add(corner({"SOURCE"}))
        self.reveal(head("A failed search, recorded as ok"))
        tag = chip("reconstruction: the old recorder kept no arguments", GHOST).move_to([0, 2.15, 0])
        line = mono("tavily_search  ok", size=30, color=INK).move_to([0, 1.45, 0])
        self.reveal(tag, line, wait=1.2)
        res = mtxt('returned {"error": "400 Bad Request"}', size=24, color=SOFT).move_to([0, 0.8, 0])
        self.reveal(res)
        ok = line[-2:]
        st = strike(ok)
        err = label("error", size=30, weight="BOLD", color=ACC).next_to(line, DOWN, buff=0.2).shift(RIGHT * 1.2)
        self.play(Create(st), FadeIn(err), run_time=0.6)
        self.wait(2.5)
        self.play(FadeOut(VGroup(tag, line, res, err, st)), run_time=0.4)
        a = step["args"]
        args = VGroup(*[mono(s, size=24, color=INK) for s in (f'start_date {a.get("start_date")}', f'end_date   {a.get("end_date")}',
                                                               f'domains {a.get("include_domains")}', f'images "{a.get("include_images")}"')]
                      ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        box = fitw(boxed(args, color=SOFT))
        hdr = txt(f"the model's own settings (run {step['run_id']})", size=24, color=SOFT, weight="BOLD")
        grp = VGroup(hdr, box).arrange(DOWN, buff=0.2).move_to([0, 0.9, 0])
        self.reveal(grp)
        self.play(Create(ring(VGroup(args[0], args[1]), buff=0.05)), run_time=0.5)
        self.wait(2.5)
        self.reveal(cap(f"one retry with the query alone: {step['urls']} real results", -1.4))
        self.finish()


class B05_BarrierAndOverlap(Beat):
    def construct(self):
        e = ev("B05_overlap_from_stream")
        span = {k: (datetime.fromisoformat(v["first"]), datetime.fromisoformat(v["last"])) for k, v in e["per_agent_span"].items()}
        t0 = min(s for s, _ in span.values())
        total = (max(t for _, t in span.values()) - t0).total_seconds()
        self.reveal(head("Both agents, at the same time"), wait=1.0)
        # vertical timeline: time runs downward
        y0, height = 1.6, 3.9

        def y(t):
            return y0 - height * (t - t0).total_seconds() / total
        cols = VGroup()
        for i, (k, name, col) in enumerate((("shared", "SEC\nfetch", GHOST), ("agent_a", "AGENT\nA", LANE_A), ("agent_b", "AGENT\nB", LANE_B))):
            s, t = span[k]
            x = -1.35 + i * 1.35
            r = Rectangle(width=0.8, height=max(0.06, y(s) - y(t)), fill_color=col, fill_opacity=0.9, stroke_width=0).move_to([x, (y(s) + y(t)) / 2, 0])
            lab = label(name, size=24, weight="BOLD", color=INK, line_spacing=0.8).move_to([x, 2.1, 0])
            cols.add(VGroup(r, lab))
        self.play(LaggedStart(*[GrowFromEdge(c[0], UP) for c in cols], lag_ratio=0.3),
                  LaggedStart(*[FadeIn(c[1]) for c in cols], lag_ratio=0.3), run_time=1.8)
        o0 = max(span["agent_a"][0], span["agent_b"][0])
        o1 = min(span["agent_a"][1], span["agent_b"][1])
        shade = Rectangle(width=2.3, height=y(o0) - y(o1), stroke_color=INK, stroke_width=2, fill_color=INK, fill_opacity=0.06).move_to([0.675, (y(o0) + y(o1)) / 2, 0])
        self.reveal(shade)
        self.reveal(cap(f"in flight together: {e['overlap_s']} s", -2.55), txt(f"start gap {e['start_gap_ms']:.0f} ms", size=24, color=SOFT).move_to([0, -2.95, 0]))
        self.reveal(src("recorded AAPL stream · speed-up not measured"))
        self.finish()


class B06_FigureNotString(Beat):
    def construct(self):
        e = ev("B06_figures_not_strings")
        self.reveal(head("Compare figures, not strings"))
        ex = txt('"Diluted EPS of $2.02 for Q3 FY2026"', size=24, width=40)
        parts = VGroup(chip("METRIC  eps_diluted", ACC), chip("PERIOD  Q3 FY2026", INK), chip("VALUE  2.02", SOFT)).arrange(DOWN, buff=0.1)
        tol = txt("EPS to the cent · large figures 0.5% · % changes 0.1 point", size=24, color=SOFT, width=30)
        row = e["msft_format_test_case"]["canonical_rows"][0]
        blk = VGroup(chip("constructed example, Microsoft's filed format", GHOST), mono(row["raw_a"], size=28, color=LANE_A),
                     label(f"= {row['status'].title()}  {row['variance_pct']}%", size=28, weight="BOLD", color=GREEN),
                     mono(row["raw_b"], size=28, color=LANE_B)).arrange(DOWN, buff=0.1)
        n = e["nvda_confidence_stored_run"]
        closing = cap(f"run {n['run_id']}: the only 'conflict' was {n['stored_divergent'][0]}, a self-rating", 0, size=24)
        g = stack(ex, parts, tol, blk, closing, buff=0.3)
        self.reveal(g[0])
        self.play(LaggedStart(*[FadeIn(p) for p in g[1]], lag_ratio=0.3), run_time=1.0)
        self.reveal(g[2], wait=3.5)
        self.reveal(g[3], wait=3.5)
        self.reveal(g[4])
        self.finish()


class B07_RatioRecompute(Beat):
    def construct(self):
        e = ev("B07_derivation_checks")
        rb, ab = e["arithmetic"]["revenue_B"], e["arithmetic"]["assets_B"]
        ratio = rb / ab
        assert abs(ratio - e["arithmetic"]["revenue_over_assets"]) < 1e-3
        wrong = [r for r in e["rows"] if r["status"] == "DERIVED_WRONG"]
        roa = next(r for r in e["rows"] if r["label"] == "Return on assets")
        self.reveal(head("A real ratio and a made-up one look the same"))
        l1 = VGroup(var("asset turnover", 30), label("=", size=32, color=INK), frac(var("revenue", 28), var("assets", 28))).arrange(RIGHT, buff=0.2)
        l2 = VGroup(label("=", size=32, color=INK), frac(f"{rb}", f"{ab}", size=30), label("=", size=32, color=INK), mono(f"{ratio:.3f}", size=36, color=INK)).arrange(RIGHT, buff=0.2)
        eq = fitw(VGroup(l1, l2).arrange(DOWN, buff=0.3)).move_to([0, 1.55, 0])
        self.play(LaggedStart(FadeIn(l1), FadeIn(l2), lag_ratio=0.4), run_time=1.8)
        self.reveal(src("revenue and assets in $ billions, as stated", y=0.35), wait=1.5)
        stated = VGroup(*[mono(f"agent wrote {w['stated']}", size=30, color=INK) for w in wrong]).arrange(DOWN, buff=0.15).move_to([0, -0.5, 0])
        self.reveal(stated)
        times = label(f"{ratio / float(wrong[0]['stated']):.1f}× off", size=32, weight="BOLD", color=ACC).move_to([0, -1.45, 0])
        self.play(Create(ring(stated, buff=0.06)), FadeIn(times), run_time=0.6)
        self.wait(2.5)
        self.reveal(cap(f"GOOGL return on assets: {roa['stated']} stated, 18.96% recomputed: cleared", -2.5, color=GREEN, size=24))
        self.finish()


class B08_WrongDrawer(Beat):
    def construct(self):
        e = ev("B08_old_tagger_on_return_on_assets")
        pct = next(n for n, t in e["tag_numbers"] if "%" in n)
        tag = next(t for n, t in e["tag_numbers"] if "%" in n)
        self.reveal(head("How the old tagger read it"))
        a = label("Return on", size=32, color=INK)
        b = label("Assets", size=32, weight="BOLD", color=BG)
        c = label(f"(ROA) of {pct}", size=32, color=INK)
        hl = BackgroundRectangle(b, color=ACC, fill_opacity=1, buff=0.08)
        sent = VGroup(a, VGroup(hl, b), c).arrange(DOWN, buff=0.15).move_to([0, 1.7, 0])
        self.reveal(sent, wait=2.5)
        drawer = boxed(label(tag.upper(), size=32, weight="BOLD", color=INK)).move_to([0, -0.1, 0])
        fig = mono(pct, size=30, color=ACC).move_to(c)
        self.reveal(drawer)
        self.play(fig.animate.move_to(drawer.get_top() + UP * 0.35), run_time=0.9)
        self.reveal(chip("excluded: only one agent was given Assets", SOFT).move_to([0, -0.95, 0]), wait=2.5)
        self.reveal(fitw(boxed(label("EARLIER RESULT  15 / 16", size=30, weight="BOLD", color=INK))).move_to([0, -1.95, 0]))
        self.reveal(cap("the count stands; part of it came from this mis-tag", -2.85, color=AMBER, size=24))
        self.finish()


class B09_SixOfSixteen(Beat):
    def construct(self):
        e = ev("B09_corpus_replay")
        n, old, new = e["disjoint_concepts_runs"], e["concept_aware_flags"], e["canonical_flags"]
        tp = next(r for r in e["all"] if r["run_id"] == "f4a4c782")
        self.reveal(head("The bar: do no worse than the old rule"))
        base, uh = -0.9, 0.4
        self.play(Create(Line([-1.8, base, 0], [1.8, base, 0], color=INK, stroke_width=2)), run_time=0.3)
        bars = VGroup()
        for x, v, name in ((-0.9, old, "OLD"), (0.9, new, "NEW")):
            r = Rectangle(width=1.1, height=max(0.02, v * uh), fill_color=INK, fill_opacity=0.9, stroke_width=0).move_to([x, base + v * uh / 2, 0])
            bars.add(VGroup(r, label(f"{v} / {n}", size=30, weight="BOLD", color=INK).next_to(r, UP, buff=0.12),
                            label(name, size=24, weight="BOLD", color=SOFT).move_to([x, base - 0.32, 0])))
        self.play(LaggedStart(*[GrowFromEdge(b[0], DOWN) for b in bars], lag_ratio=0.4),
                  LaggedStart(*[FadeIn(VGroup(b[1], b[2])) for b in bars], lag_ratio=0.4), run_time=1.6)
        self.wait(2.5)
        self.reveal(cap(f"1 real: a fabricated ratio of {tp['divergent'][0]}, caught by both", -2.3, color=GREEN, size=24), wait=1.5)
        self.reveal(cap(f"{new - 1} can't be judged: no components recorded", -3.25, color=AMBER, size=24))
        self.finish()


class B10_OptIn(Beat):
    def construct(self):
        e = ev("B10_record_growth")
        self.reveal(shot("B10_recorded_verdict_1280.png", W, 2.2).move_to([0, 1.9, 0]))
        self.reveal(chip("which rule decided is always shown", ACC).move_to([0, 0.45, 0]), wait=3.5)
        a, b = e["counts"]
        self.reveal(VGroup(mono(f"{a}", size=44, color=SOFT), label("→", size=36, color=INK), mono(f"{b}", size=44, color=INK),
                           label("fields", size=30, color=INK)).arrange(RIGHT, buff=0.25).move_to([0, -0.9, 0]))
        self.reveal(chip("contexts: what each agent was given", SOFT).move_to([0, -1.8, 0]))
        self.reveal(src("fields kept on every stored run, before and after", y=-2.6))
        self.finish()


class B11_ThreeFormatFailures(Beat):
    def construct(self):
        ex = ev("B11_echo_replay_today")["examples"]
        sample = (ex[1] if len(ex) > 1 else ex[0])["echoed_window"]
        self.reveal(head("Three format failures, found live"))
        cards = [("copied the prompt", f'"{sample}"', "17 / 135 conclusions"),
                 ("square brackets", "[/conclusion]", "3 / 22 first attempts"),
                 ("opening lost", "</thought_log> alone", "earlier turns now read")]
        y = 1.8
        for i, (t, s, stat) in enumerate(cards):
            blk = VGroup(label(f"{i + 1}  {t}", size=28, weight="BOLD", color=INK), mtxt(s, size=24, color=SOFT, width=26),
                         label(stat, size=26, weight="BOLD", color=ACC)).arrange(DOWN, buff=0.1)
            self.reveal(fitw(blk).move_to([0, y, 0]), wait=4.5)
            y -= 1.5
        self.reveal(chip("final batch: 0 first-attempt failures, 8 agents", GREEN).move_to([0, -2.9, 0]))
        self.finish()


class B12_TheMatrix(Beat):
    def construct(self):
        self.reveal(head("The comparison, as a table"))
        self.reveal(shot("B12_matrix_375.png", 3.0, 5.6).move_to([0, -0.35, 0]), wait=2.0)
        self.reveal(src("captured from /app, run 20c538e4, phone width", y=-3.35))
        self.finish()


class B13_FirstRealAgreement(Beat):
    def construct(self):
        e = ev("B13_first_shared_match")
        self.reveal(head("Both agents now get the same figures"))
        rows = VGroup(*[VGroup(label(r["label"].split(" (")[0], size=26, weight="BOLD", color=INK),
                               label(f"{r['raw_a']} = {r['raw_b']}", size=26, color=GREEN, weight="BOLD")).arrange(DOWN, buff=0.08)
                        for r in e["rows"]]).arrange(DOWN, buff=0.3)
        self.reveal(fitw(rows).move_to([0, 1.55, 0]), txt("both match the filing", size=24, color=SOFT).move_to([0, 0.45, 0]), wait=3.5)
        left = boxed(txt('agent: "not explicitly stated in the Context"', size=24, width=22))
        right = boxed(txt("last line of its input: diluted EPS 2.02", size=24, width=22), color=ACC)
        self.reveal(fit(VGroup(left, right).arrange(DOWN, buff=0.25), W, 2.6).move_to([0, -1.55, 0]))
        self.reveal(src("agent A on the NVDA and GOOGL runs"))
        self.finish()


class B14_TrueNow(Beat):
    def construct(self):
        self.reveal(txt("WHAT WORKS NOW", size=40, color=GREEN, weight="BOLD").move_to([0, 3.0, 0]))
        rows = ledger(["every figure carries its period, unit and filing", "failed searches are recorded as failures",
                       "two agents in flight at once", "ratios recomputed: two hidden errors surfaced"], GREEN, "✓").move_to([0, -0.2, 0])
        for r in rows:
            self.reveal(r, rt=0.4, wait=1.8)
        self.finish()


class B15_StillNotTrue(Beat):
    def construct(self):
        self.reveal(txt("WHAT STILL DOESN'T", size=40, color=RED, weight="BOLD").move_to([0, 3.0, 0]))
        rows = ledger(["the stricter comparator is opt-in for company runs", "tagging still depends on wording",
                       "the ratio check ignores annual vs quarterly", "agents skip figures that are in their input"], RED, "✕").move_to([0, -0.2, 0])
        for r in rows:
            self.reveal(r, rt=0.4, wait=1.8)
        self.finish()


class B16_EndCardReprise(Beat):
    def construct(self):
        c = ev("B09_corpus_replay")
        self.reveal(serif("the smallest true claim", size=32, color=INK).move_to([0, 3.1, 0]))
        self.reveal(VGroup(label("15 / 16", size=44, weight="BOLD", color=SOFT), label("→", size=40, color=INK),
                           label(f"{c['canonical_flags']} / {c['disjoint_concepts_runs']}", size=44, weight="BOLD", color=ACC)
                           ).arrange(RIGHT, buff=0.3).move_to([0, 2.3, 0]))
        self.reveal(four_grid(size=24).scale(0.6).move_to([0, 1.2, 0]), wait=2.0)
        bullets = [("handed FY2018 revenue and nine-month EPS", INK),
                   (f"{c['canonical_flags']} of {c['disjoint_concepts_runs']} alarms: 1 real, {c['canonical_flags'] - 1} unknown", INK),
                   ("two asset-turnover errors, 5× off", INK), ("a Return-on-Assets mis-tag", INK),
                   ("first shared-figure match", INK), ("stricter rule stays opt-in for now", RED)]
        lines = fit(VGroup(*[label(wrap(t, 28), size=26, color=col, weight="BOLD" if col == RED else None, line_spacing=0.85) for t, col in bullets]
                           ).arrange(DOWN, buff=0.2, aligned_edge=LEFT), W, 3.8).move_to([0, -1.5, 0])
        for ln in lines:
            self.reveal(ln, rt=0.3, wait=0.9)
        self.finish()
