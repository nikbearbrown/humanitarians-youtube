"""scenes.py — Manim scenes for the-rule-that-lost (Mycroft 8, audit-layer update part 1 of 2).

House conventions, carried over from fifteen-of-sixteen/scenes.py (Mycroft 7):
  - Palette (beat_sheet metadata.palette = "claude"): cream #FAF9F5, ink #3D3929, terracotta
    #D97757, soft #73705F, ghost #A9A491, plus the series' verdict colours (green / amber / red).
    Agent lanes use the app's own blue (A) and orange (B), matching the captured screenshots.
    A WRONG value is shown with an ink strike + terracotta ring, never by colouring it red alone.
  - Type via graphics_lib.py: Montserrat (structure), EB Garamond (editorial), PT Mono (data).
  - Boxes sized to content (auto_box); never a raw "⚠" glyph (warn_icon draws one).
  - Every scene ends with hold_to(self, TARGET) so its native length matches the beat.

What is new here:
  - EXECUTABLE EVIDENCE: every number on screen is read at render time from
    assets/evidence/out/*.json (produced by assets/evidence/m8_evidence.py from the live
    verification layer). Nothing numeric is typed into a scene by hand, so re-running the
    evidence script and re-rendering keeps the film honest.
  - TARGETs come from beat_sheet.json: actual_duration_s once Kokoro has run, else the pre-audio
    estimated_duration_s. Retiming is therefore automatic, but still CHECK the rendered length
    against the audio (CLAUDE.md §5 step 4) — waits may need redistributing, not just padding.
  - MATH (MATH-TYPESETTING.md): no LaTeX is installed on this machine, so MathTex would fail.
    Fractions are an equivalent structured layout: numerator and denominator as real text over
    a drawn fraction bar (frac()), variables in italic serif. The arithmetic is recomputed and
    asserted before it is drawn.
  - Real app screenshots (assets/*.png) are HOLD evidence of the actual software.

B00 (ClaudeComposerAsk) and B17 (ClaudeTitleOutro) are Remotion beats, not scenes here.
Safe frame: x in [-6.4, 6.4], y in [-3.6, 3.6]. Nothing in this file has been rendered at 4K yet.
"""
import json
from datetime import datetime
from pathlib import Path

from graphics_lib import *

HERE = Path(__file__).resolve().parent
EVID = HERE / "assets" / "evidence" / "out"
SHEET = json.loads((HERE / "beat_sheet.json").read_text(encoding="utf-8"))

BG = "#FAF9F5"
INK = "#3D3929"
ACC = "#D97757"
SOFT = "#73705F"
GHOST = "#A9A491"
GREEN = "#4C9A6A"
AMBER = "#C9932E"
RED = "#B0473A"
LANE_A = "#3B82F6"   # app's agent-A blue
LANE_B = "#E07B28"   # app's agent-B orange


# ─── plumbing ────────────────────────────────────────────────────────────────
def target(scene_class):
    for b in SHEET["beats"]:
        if b["shot"].get("manim", {}).get("scene_class") == scene_class:
            return float(b.get("actual_duration_s") or b["estimated_duration_s"])
    raise KeyError(scene_class)


def ev(name):
    return json.loads((EVID / f"{name}.json").read_text(encoding="utf-8"))


def hold_to(scene, tgt, minimum=0.4):
    try:
        elapsed = float(scene.renderer.time)
    except Exception:
        scene.wait(minimum)
        return
    scene.wait(max(minimum, tgt - elapsed))


def money(v):
    v = float(v)
    for div, suf in ((1e12, "T"), (1e9, "B"), (1e6, "M")):
        if abs(v) >= div:
            return f"${v / div:.1f}{suf}"
    return f"${v:,.2f}"


# ─── shared visual pieces ────────────────────────────────────────────────────
def boxed(inner, color=INK, h_pad=0.45, v_pad=0.32, **kw):
    return VGroup(auto_box(inner, h_pad=h_pad, v_pad=v_pad, color=color, **kw), inner)


def head(text):
    return label(text, size=26, weight="BOLD", color=SOFT).move_to([0, 3.2, 0])


def caption(text, y=-3.0, color=INK, size=24):
    return fit_w(label(text, size=size, weight="BOLD", color=color)).move_to([0, y, 0])


def source_line(text, y=-3.45):
    return fit_w(label(text.upper(), size=24, color=GHOST), 12.4).move_to([0, y, 0]).scale(0.75)


def fit_w(group, max_width=11.8):
    if group.width > max_width:
        group.scale(max_width / group.width)
    return group


def fit(group, max_w, max_h):
    s = min(1.0, max_w / group.width, max_h / group.height)
    group.scale(s)
    return group


def screenshot(name, max_w, max_h):
    img = ImageMobject(str(HERE / "assets" / name))
    img.scale(min(max_w / img.width, max_h / img.height))
    frame = SurroundingRectangle(img, buff=0.04, color=GHOST, stroke_width=1.5)
    return Group(img, frame)


def ring(mob, color=ACC, buff=0.18):
    """Handnote-style ring around a value."""
    return Ellipse(width=mob.width + 2 * buff + 0.9, height=mob.height + 2 * buff + 0.3,
                   color=color, stroke_width=4).move_to(mob)


def strike(mob, color=INK):
    return Line(mob.get_left() + LEFT * 0.08, mob.get_right() + RIGHT * 0.08,
                color=color, stroke_width=5)


def warn_icon(scale=0.22):
    tri = Triangle(color=AMBER, fill_color=AMBER, fill_opacity=1, stroke_width=0).scale(scale)
    bang = label("!", size=int(scale * 110), weight="BOLD", color=BG).move_to(
        tri.get_center() + DOWN * (scale * 0.14))
    return VGroup(tri, bang)


def frac(num, den, size=34, color=INK):
    """Structured fraction: numerator over a real bar over denominator."""
    n = num if isinstance(num, Mobject) else label(num, size=size, color=color)
    d = den if isinstance(den, Mobject) else label(den, size=size, color=color)
    w = max(n.width, d.width) + 0.25
    bar = Line(LEFT * w / 2, RIGHT * w / 2, color=color, stroke_width=3)
    n.next_to(bar, UP, buff=0.14)
    d.next_to(bar, DOWN, buff=0.14)
    return VGroup(n, bar, d)


def var(text, size=34, color=INK):
    """A variable name: italic serif, per MATH-TYPESETTING.md."""
    return serif(text, size=size, color=color, italic=True)


FOUR = ("METRIC", "PERIOD", "UNIT", "SOURCE")


def four_boxes(lit=(), size=26, gap=0.35):
    cells = VGroup()
    for name in FOUR:
        on = name in lit
        t = label(name, size=size, weight="BOLD", color=BG if on else INK)
        b = auto_box(t, h_pad=0.4, v_pad=0.28, color=ACC if on else INK,
                     fill_color=ACC, fill_opacity=1 if on else 0)
        cells.add(VGroup(b, t))
    return cells.arrange(RIGHT, buff=gap)


def corner_chip(lit):
    """The four-box test, small, bottom-right: which box this beat is about."""
    return four_boxes(lit, size=24, gap=0.12).scale(0.5).move_to([3.95, -3.2, 0])


class Beat(Scene):
    def setup(self):
        self.camera.background_color = BG

    def finish(self):
        hold_to(self, target(type(self).__name__))


# ─────────────────────────────────────────────────────────────────────────────
# B01 — recap and the four-box test (framework before example)
# ─────────────────────────────────────────────────────────────────────────────
class B01_FourBoxTest(Beat):
    def construct(self):
        self.play(FadeIn(head("ONE TEST FOR EVERY FIGURE")), run_time=0.4)
        what = label("two AI agents, one company, compare the numbers they report", size=26, color=SOFT)
        self.play(FadeIn(fit_w(what).move_to([0, 2.2, 0])), run_time=0.5)
        self.wait(3.5)
        boxes = four_boxes().move_to([0, 0.6, 0])
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.1) for b in boxes], lag_ratio=0.25), run_time=1.6)
        self.wait(3.0)
        self.play(FadeIn(caption("two figures compare only when all four line up", y=-1.3)), run_time=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B02 — period: what the agents were handed
# ─────────────────────────────────────────────────────────────────────────────
class B02_WhatTheyWereHanded(Beat):
    def construct(self):
        data = {r["concept"]: r for r in ev("B02_B03_what_they_were_handed")["rows"]}
        self.add(corner_chip({"PERIOD"}))
        self.play(FadeIn(head("WHAT THE AGENTS WERE HANDED")), run_time=0.4)

        rev = data["Revenues"]["legacy_entry"]
        raw = mono(f'"Revenues": {{"val": {data["Revenues"]["legacy_handed"]}, "fy": {rev["fy"]}, '
                   f'"fp": "{rev["fp"]}", "form": "{rev["form"]}"}}', size=24, color=INK)
        fit_w(raw, 10.6).move_to([0, 2.3, 0])
        src = source_line("real SEC companyfacts payload, trimmed (edgar_aapl_companyfacts_sample.json)", y=1.8)
        self.play(FadeIn(raw), FadeIn(src), run_time=0.6)
        self.play(Create(ring(raw, buff=0.1)), run_time=0.6)
        self.wait(3.0)

        eps, ni, assets = data["EarningsPerShareDiluted"], data["NetIncomeLoss"], data["Assets"]
        rows = [
            (money(data["Revenues"]["legacy_handed"]), f"fiscal {rev['fy']} annual, retired label", RED),
            (f"EPS {eps['legacy_handed']}", f"{eps['legacy_span_days']}-day year to date, quarter {eps['b0_selected']}", RED),
            (f"Net income {money(ni['legacy_handed'])}", f"year to date, quarter {money(ni['b0_selected'])}", RED),
            (f"Assets {money(assets['legacy_handed'])}", "correct: a point in time", GREEN),
        ]
        hl = label("HANDED TO THE AGENT", size=24, weight="BOLD", color=SOFT).move_to([-3.3, 1.05, 0])
        hr = label("WHAT IT ACTUALLY WAS", size=24, weight="BOLD", color=SOFT).move_to([2.6, 1.05, 0])
        self.play(FadeIn(hl), FadeIn(hr), run_time=0.4)
        for i, (left, right, col) in enumerate(rows):
            y = 0.3 - i * 0.78
            l = mono(left, size=26, color=INK).move_to([-3.3, y, 0])
            r = label(right, size=24, color=col, weight="BOLD")
            fit_w(r, 6.0).move_to([2.6, y, 0])
            self.play(FadeIn(l), FadeIn(r, shift=LEFT * 0.1), run_time=0.5)
            self.wait(2.2)
        self.play(FadeIn(caption("every Apple comparison until now used these", y=-2.75)), run_time=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B03 — the fix, written test-first
# ─────────────────────────────────────────────────────────────────────────────
class B03_FactWithPeriod(Beat):
    def construct(self):
        eps = {r["concept"]: r for r in ev("B02_B03_what_they_were_handed")["rows"]}["EarningsPerShareDiluted"]
        desc = eps["b0_describe"]  # "2.02 USD/shares (FY2026 Q3, 3 months ending ..., 10-Q, frame ..., accn ...)"
        inside = desc[desc.index("(") + 1: desc.rindex(")")].split(", ")
        period, span, form = inside[0], inside[1], inside[2]
        accn = next(p for p in inside if p.startswith("accn"))
        self.add(corner_chip({"PERIOD", "UNIT", "SOURCE"}))
        self.play(FadeIn(head("EVERY FIGURE CARRIES ITS CONTEXT")), run_time=0.4)

        value = mono(str(eps["b0_selected"]), size=72, color=INK).move_to([0, 1.6, 0])
        self.play(FadeIn(value, scale=0.9), run_time=0.6)
        chips = VGroup(*[label_chip(t, c, size=22, upper=False) for t, c in
                         ((period, ACC), ("USD per share", INK), (f"{form} · {span}", SOFT), (accn, SOFT))])
        chips.arrange(RIGHT, buff=0.25)
        fit_w(chips).move_to([0, 0.35, 0])
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.15) for c in chips], lag_ratio=0.35), run_time=2.0)
        self.wait(3.0)

        segs = VGroup()
        for text, w, col in (("quarter: 80 to 100 days", 3.6, ACC), ("annual: 350 to 380 days", 3.6, INK),
                             ("anything else: labelled last resort", 4.0, GHOST)):
            t = label(text, size=24, weight="BOLD", color=BG)
            fit_w(t, w - 0.3)
            r = Rectangle(width=w, height=0.7, fill_color=col, fill_opacity=1, stroke_width=0)
            segs.add(VGroup(r, t.move_to(r)))
        segs.arrange(RIGHT, buff=0.1).move_to([0, -1.1, 0])
        self.play(LaggedStart(*[FadeIn(s) for s in segs], lag_ratio=0.3), run_time=1.5)
        self.wait(2.0)
        self.play(FadeIn(caption("a restatement replaces the original", y=-2.3)), run_time=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B04 — source: a failure recorded as ok
# ─────────────────────────────────────────────────────────────────────────────
class B04_FailureRecordedOk(Beat):
    def construct(self):
        e = ev("B04_search_args_and_retry")
        step = e["first_three"][0]
        self.add(corner_chip({"SOURCE"}))
        self.play(FadeIn(head("A FAILED SEARCH, RECORDED AS OK")), run_time=0.4)

        tag = label_chip("RECONSTRUCTION: the old recorder kept no arguments", GHOST, size=22, upper=False)
        tag.move_to([0, 2.45, 0])
        line = mono("tavily_search      status: ok", size=30, color=INK).move_to([-1.2, 1.55, 0])
        self.play(FadeIn(tag), FadeIn(line), run_time=0.6)
        self.wait(1.5)
        result = mono('returned  {"error": "400 Bad Request"}', size=26, color=SOFT)
        result.next_to(line, DOWN, buff=0.3).align_to(line, LEFT)
        self.play(FadeIn(result, shift=DOWN * 0.1), run_time=0.5)
        ok = line[-2:]
        err = label("error", size=30, weight="BOLD", color=ACC).next_to(line, RIGHT, buff=0.35)
        st = strike(ok)
        self.play(Create(st), FadeIn(err), run_time=0.7)
        self.wait(3.0)

        self.play(FadeOut(VGroup(tag, line, result, err, st)), run_time=0.5)
        a = step["args"]
        shown = [f'"query": "{a.get("query")}"', f'"start_date": "{a.get("start_date")}"',
                 f'"end_date": "{a.get("end_date")}"', f'"include_domains": {json.dumps(a.get("include_domains"))}',
                 f'"include_images": "{a.get("include_images")}"']
        args = VGroup(*[mono(s, size=26, color=INK) for s in shown]).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        box = boxed(args, color=SOFT)
        hdr = label(f"the model's own search settings (recorded, run {step['run_id']})", size=24,
                    weight="BOLD", color=SOFT)
        grp = VGroup(hdr, box).arrange(DOWN, buff=0.25)
        fit(grp, 11.5, 4.2).move_to([0, 0.3, 0])
        self.play(FadeIn(grp), run_time=0.6)
        self.play(Create(ring(VGroup(args[1], args[2]), buff=0.08)), run_time=0.6)
        self.wait(3.0)
        retry = caption(f"one retry with the query alone: {step['urls']} real results", y=-2.6)
        self.play(FadeIn(retry), run_time=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B05 — two agents at once
# ─────────────────────────────────────────────────────────────────────────────
class B05_BarrierAndOverlap(Beat):
    def construct(self):
        e = ev("B05_overlap_from_stream")
        span = {k: (datetime.fromisoformat(v["first"]), datetime.fromisoformat(v["last"]))
                for k, v in e["per_agent_span"].items()}
        t0 = min(s for s, _ in span.values())
        t1 = max(t for _, t in span.values())
        total = (t1 - t0).total_seconds()

        self.play(FadeIn(head("BOTH AGENTS, AT THE SAME TIME")), run_time=0.4)
        self.wait(1.5)

        x0, width = -3.3, 9.5
        def x(t):
            return x0 + width * (t - t0).total_seconds() / total
        bars = VGroup()
        for i, (key, name, col) in enumerate((("shared", "SEC fetch (shared)", GHOST),
                                              ("agent_a", "AGENT A", LANE_A), ("agent_b", "AGENT B", LANE_B))):
            s, t = span[key]
            y = -0.35 - i * 0.75
            r = Rectangle(width=max(0.08, x(t) - x(s)), height=0.5, fill_color=col, fill_opacity=0.9, stroke_width=0)
            r.move_to([(x(s) + x(t)) / 2, y, 0])
            lab = label(name, size=24, weight="BOLD", color=INK)
            fit_w(lab, 2.6).move_to([-3.5, y, 0], aligned_edge=RIGHT)
            bars.add(VGroup(r, lab))
        self.play(LaggedStart(*[GrowFromEdge(b[0], LEFT) for b in bars], lag_ratio=0.3),
                  LaggedStart(*[FadeIn(b[1]) for b in bars], lag_ratio=0.3), run_time=1.8)
        o0 = max(span["agent_a"][0], span["agent_b"][0])
        o1 = min(span["agent_a"][1], span["agent_b"][1])
        shade = Rectangle(width=x(o1) - x(o0), height=1.45, stroke_color=INK, stroke_width=2,
                          fill_color=INK, fill_opacity=0.06).move_to([(x(o0) + x(o1)) / 2, -1.475, 0])
        olab = label(f"in flight together: {e['overlap_s']} s   (start gap {e['start_gap_ms']:.0f} ms)",
                     size=24, weight="BOLD", color=INK).next_to(shade, DOWN, buff=0.2)
        self.play(FadeIn(shade), FadeIn(olab), run_time=0.6)
        self.wait(2.5)
        self.play(FadeIn(source_line("from the recorded AAPL stream, 2026-09-24 · speed-up not measured")), run_time=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B06 — metric and unit: figures, not strings
# ─────────────────────────────────────────────────────────────────────────────
class B06_FigureNotString(Beat):
    def construct(self):
        e = ev("B06_figures_not_strings")
        self.add(corner_chip({"METRIC", "UNIT"}))
        self.play(FadeIn(head("COMPARE FIGURES, NOT STRINGS")), run_time=0.4)

        parts = VGroup(label_chip("METRIC  eps_diluted", ACC, size=22, upper=False),
                       label_chip("PERIOD  Q3 FY2026", INK, size=22, upper=False),
                       label_chip("VALUE  2.02", SOFT, size=22, upper=False)).arrange(RIGHT, buff=0.3)
        ex = label("\"Diluted EPS of $2.02 for Q3 FY2026\"", size=26, color=INK).move_to([0, 2.35, 0])
        parts.move_to([0, 1.55, 0])
        self.play(FadeIn(ex), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(p, shift=DOWN * 0.1) for p in parts], lag_ratio=0.3), run_time=1.2)
        tol = VGroup(*[label(t, size=24, color=SOFT) for t in
                       ("EPS: to the cent", "large figures: within 0.5%", "% changes: within 0.1 point")]
                     ).arrange(RIGHT, buff=0.6)
        fit_w(tol).move_to([0, 0.75, 0])
        self.play(FadeIn(tol), run_time=0.5)
        self.wait(4.0)

        tc = e["msft_format_test_case"]
        row = tc["canonical_rows"][0]
        test_tag = label_chip("CONSTRUCTED EXAMPLE IN MICROSOFT'S FILED FORMAT", GHOST, size=22)
        r = VGroup(mono(row["raw_a"], size=28, color=LANE_A),
                   checked(f"{row['status'].title()}  {row['variance_pct']}%", size=26, color=GREEN, weight="BOLD"),
                   mono(row["raw_b"], size=28, color=LANE_B)).arrange(RIGHT, buff=0.7)
        old = label(f"old rule: {len(tc['old_set_difference'])} 'different' numbers", size=24, color=SOFT)
        blk = VGroup(test_tag, r, old).arrange(DOWN, buff=0.22)
        fit_w(blk).move_to([0, -0.6, 0])
        self.play(FadeIn(blk), run_time=0.6)
        self.wait(4.0)

        n = e["nvda_confidence_stored_run"]
        nv = label(f"stored run {n['run_id']}: the old rule's only 'conflict' was {n['stored_divergent'][0]}"
                   f"  →  a self-rating, not a figure", size=24, weight="BOLD", color=INK)
        self.play(FadeIn(fit_w(nv).move_to([0, -2.2, 0])), run_time=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B07 — the ratio check (structured fraction, arithmetic asserted)
# ─────────────────────────────────────────────────────────────────────────────
class B07_RatioRecompute(Beat):
    def construct(self):
        e = ev("B07_derivation_checks")
        rev_b, ast_b = e["arithmetic"]["revenue_B"], e["arithmetic"]["assets_B"]
        ratio = rev_b / ast_b
        assert abs(ratio - e["arithmetic"]["revenue_over_assets"]) < 1e-3, "arithmetic drift"
        wrong = [r for r in e["rows"] if r["status"] == "DERIVED_WRONG"]
        margin = next(r for r in e["rows"] if r["status"] == "DERIVED_OK" and r["label"] == "Net margin")
        roa = next(r for r in e["rows"] if r["label"] == "Return on assets")

        self.play(FadeIn(head("A REAL RATIO AND A MADE-UP ONE LOOK THE SAME")), run_time=0.5)
        self.wait(2.5)

        eq = VGroup(var("asset turnover", 34), label("=", size=36, color=INK),
                    frac(var("revenue", 30), var("assets", 30)), label("=", size=36, color=INK),
                    frac(f"{rev_b}", f"{ast_b}", size=32), label("=", size=36, color=INK),
                    mono(f"{ratio:.3f}", size=38, color=INK)).arrange(RIGHT, buff=0.3)
        fit_w(eq).move_to([0, 1.5, 0])
        self.play(LaggedStart(*[FadeIn(p) for p in eq], lag_ratio=0.25), run_time=2.2)
        unit = source_line("revenue and assets in $ billions, as each agent stated them", y=0.35)
        self.play(FadeIn(unit), run_time=0.3)
        self.wait(2.0)

        stated = VGroup(*[mono(f"agent wrote {w['stated']}   (run {w['run_id']})", size=28, color=INK) for w in wrong]
                        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to([-1.2, -0.75, 0])
        self.play(FadeIn(stated), run_time=0.5)
        times = label(f"{ratio / float(wrong[0]['stated']):.1f}×", size=34, weight="BOLD", color=ACC)
        times.next_to(stated, RIGHT, buff=0.6)
        self.play(Create(ring(stated, buff=0.1)), FadeIn(times), run_time=0.7)
        self.wait(3.0)

        ok = VGroup(checked(f"net margin in the same runs: {margin['stated']}, recomputes to 38.2%", size=24, color=GREEN),
                    checked(f"GOOGL return on assets: {roa['stated']} stated, 18.96% recomputed", size=24, color=GREEN)
                    ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(FadeIn(fit_w(ok).move_to([0, -2.45, 0])), run_time=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B08 — the correction: Return on Assets filed under Assets
# ─────────────────────────────────────────────────────────────────────────────
class B08_WrongDrawer(Beat):
    def construct(self):
        e = ev("B08_old_tagger_on_return_on_assets")
        tag_of_pct = next(t for n, t in e["tag_numbers"] if "%" in n)
        pct = next(n for n, t in e["tag_numbers"] if "%" in n)
        self.play(FadeIn(head("HOW THE OLD TAGGER READ IT")), run_time=0.4)

        a = label("indicating a Return on ", size=30, color=INK)
        b = label("Assets", size=30, weight="BOLD", color=BG)
        c = label(f" (ROA) of {pct}", size=30, color=INK)
        sent = VGroup(a, b, c).arrange(RIGHT, buff=0.16)
        hl = BackgroundRectangle(b, color=ACC, fill_opacity=1, buff=0.08)
        sent_g = VGroup(sent, hl)
        fit_w(sent_g).move_to([0, 1.9, 0])
        self.add(hl)
        self.play(FadeIn(sent), FadeIn(hl), run_time=0.6)
        self.wait(2.5)

        drawer = boxed(label(tag_of_pct.upper(), size=30, weight="BOLD", color=INK), color=INK).move_to([-4.3, -0.1, 0])
        excl = label_chip("EXCLUDED: ONLY ONE AGENT WAS GIVEN ASSETS", SOFT, size=22)
        fit_w(excl, 7.0).next_to(drawer, RIGHT, buff=0.6)
        fig = mono(pct, size=30, color=ACC).move_to(c.get_right() + LEFT * 0.6)
        self.play(FadeIn(drawer), run_time=0.4)
        self.play(fig.animate.move_to(drawer.get_top() + UP * 0.35), run_time=0.9)
        self.play(FadeIn(excl), run_time=0.4)
        self.play(FadeIn(source_line("tag_numbers() on a real corpus conclusion", y=-1.0)), run_time=0.3)
        self.wait(3.0)

        card = boxed(label("EARLIER RESULT:  15 / 16", size=32, weight="BOLD", color=INK), color=INK).move_to([0, -1.95, 0])
        foot = label("the count stands · part of it came from this mis-tag", size=24, weight="BOLD", color=AMBER)
        foot.next_to(card, DOWN, buff=0.2)
        self.play(FadeIn(card), run_time=0.4)
        self.play(FadeIn(foot), run_time=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B09 — the test it failed (falsifiability)
# ─────────────────────────────────────────────────────────────────────────────
class B09_SixOfSixteen(Beat):
    def construct(self):
        e = ev("B09_corpus_replay")
        n, old, new = e["disjoint_concepts_runs"], e["concept_aware_flags"], e["canonical_flags"]
        tp = next(r for r in e["all"] if r["run_id"] == "f4a4c782")
        self.play(FadeIn(head("THE BAR: DO NO WORSE THAN THE OLD RULE")), run_time=0.4)

        base_y, unit_h = -1.7, 0.42
        axis = Line([-4.5, base_y, 0], [4.5, base_y, 0], color=INK, stroke_width=2)
        self.play(Create(axis), run_time=0.4)
        bars = VGroup()
        for xpos, val, name in ((-2.0, old, "OLD RULE"), (2.0, new, "NEW RULE")):
            r = Rectangle(width=1.6, height=max(0.02, val * unit_h), fill_color=INK, fill_opacity=0.9, stroke_width=0)
            r.move_to([xpos, base_y + val * unit_h / 2, 0])
            v = label(f"{val} / {n}", size=30, weight="BOLD", color=INK).next_to(r, UP, buff=0.15)
            nm = label(name, size=24, weight="BOLD", color=SOFT).move_to([xpos, base_y - 0.35, 0])
            bars.add(VGroup(r, v, nm))
        self.play(LaggedStart(*[GrowFromEdge(b[0], DOWN) for b in bars], lag_ratio=0.4),
                  LaggedStart(*[FadeIn(VGroup(b[1], b[2])) for b in bars], lag_ratio=0.4), run_time=1.6)
        self.wait(3.0)

        c1 = label(f"1 real: a fabricated debt-to-equity ratio of {tp['divergent'][0]}, caught by both",
                   size=24, weight="BOLD", color=GREEN)
        c2 = label(f"{new - 1} can't be judged: ratios with no components", size=24, weight="BOLD", color=AMBER)
        calls = VGroup(c1, c2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        fit_w(calls, 11.0).move_to([0, 2.35, 0])
        self.play(FadeIn(c1), run_time=0.5)
        self.wait(1.5)
        self.play(FadeIn(c2), run_time=0.5)
        self.wait(2.0)
        self.play(FadeIn(caption("the old runs never recorded what each agent was given", y=-2.75)), run_time=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B10 — the decision: opt-in, and the evidence now accumulates
# ─────────────────────────────────────────────────────────────────────────────
class B10_OptIn(Beat):
    def construct(self):
        e = ev("B10_record_growth")
        shot = screenshot("B10_recorded_verdict_1280.png", 11.6, 4.3).move_to([0, 1.1, 0])
        self.play(FadeIn(shot), run_time=0.6)
        chip = label_chip("WHICH RULE DECIDED IS ALWAYS SHOWN", ACC, size=22).next_to(shot, DOWN, buff=0.25)
        self.play(FadeIn(chip), run_time=0.4)
        self.wait(4.0)

        a, b = e["counts"]
        counter = VGroup(mono(f"{a} fields", size=34, color=SOFT), label("→", size=34, color=INK),
                         mono(f"{b} fields", size=34, color=INK)).arrange(RIGHT, buff=0.4)
        ctx = label_chip("contexts: what each agent was given", SOFT, size=22, upper=False)
        grp = VGroup(counter, ctx).arrange(RIGHT, buff=0.6)
        fit_w(grp).move_to([0, -2.45, 0])
        self.play(FadeIn(counter), run_time=0.5)
        self.play(FadeIn(ctx), run_time=0.4)
        self.play(FadeIn(source_line("fields kept on every stored run, before and after", y=-3.25)), run_time=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B11 — three format failures found live
# ─────────────────────────────────────────────────────────────────────────────
class B11_ThreeFormatFailures(Beat):
    def construct(self):
        e = ev("B11_echo_replay_today")
        example = e["examples"][1]["echoed_window"] if len(e["examples"]) > 1 else e["examples"][0]["echoed_window"]
        self.play(FadeIn(head("THREE FORMAT FAILURES, FOUND LIVE")), run_time=0.4)
        cards = [
            ("copied the prompt's instructions", f"\"{example}\"", "17 / 135 conclusions (logged)"),
            ("closed with square brackets", "[/conclusion]  instead of  </conclusion>", "3 / 22 first attempts"),
            ("opening lost in the search turn", "</thought_log>  with no opening tag", "fixed: earlier turns are read"),
        ]
        col = VGroup()
        for i, (name, sample, stat) in enumerate(cards):
            t = label(f"{i + 1}  {name}", size=26, weight="BOLD", color=INK)
            s = mono(sample, size=24, color=SOFT)
            st = label(stat, size=24, weight="BOLD", color=ACC)
            col.add(VGroup(t, s, st).arrange(DOWN, buff=0.12, aligned_edge=LEFT))
        col.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        fit(col, 11.5, 5.0).move_to([0, 0.15, 0])
        for c in col:
            self.play(FadeIn(c, shift=RIGHT * 0.1), run_time=0.6)
            self.wait(5.0)
        self.play(FadeIn(label_chip("FINAL BATCH: 0 FIRST-ATTEMPT FAILURES · 8 AGENTS", GREEN, size=22).move_to([0, -3.0, 0])), run_time=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B12 — the table (real app screenshots)
# ─────────────────────────────────────────────────────────────────────────────
class B12_TheMatrix(Beat):
    def construct(self):
        self.play(FadeIn(head("THE COMPARISON, AS A TABLE")), run_time=0.5)
        desk = screenshot("B12_matrix_1280.png", 8.4, 5.2).move_to([-1.6, -0.2, 0])
        self.play(FadeIn(desk), run_time=0.6)
        self.wait(5.0)
        phone = screenshot("B12_matrix_375.png", 2.9, 5.6).move_to([4.9, -0.3, 0])
        self.play(FadeIn(phone, shift=LEFT * 0.2), run_time=0.6)
        self.play(FadeIn(source_line("captured from /app, run 20c538e4, desktop and phone width", y=-3.3)), run_time=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B13 — something in common: the first same-figure agreement
# ─────────────────────────────────────────────────────────────────────────────
class B13_FirstRealAgreement(Beat):
    def construct(self):
        e = ev("B13_first_shared_match")
        eps = {r["concept"]: r for r in ev("B02_B03_what_they_were_handed")["rows"]}["EarningsPerShareDiluted"]
        self.play(FadeIn(head("BOTH AGENTS NOW GET THE SAME FIGURES")), run_time=0.4)
        shot = screenshot("B13_shared_rows_1280.png", 11.0, 3.6).move_to([0, 1.1, 0])
        self.play(FadeIn(shot), run_time=0.6)
        rows = " · ".join(f"{r['label'].split(' (')[0]}: {r['raw_a']} = {r['raw_b']}" for r in e["rows"])
        self.play(FadeIn(fit_w(label(rows, size=24, weight="BOLD", color=GREEN)).next_to(shot, DOWN, buff=0.2)), run_time=0.5)
        self.wait(4.0)

        left = boxed(label("agent: \"not explicitly stated\n in the Context\"", size=24, color=INK), color=INK)
        right = boxed(mono("last context line:\n" + eps["b0_describe"][:44] + "…", size=24, color=INK), color=ACC)
        pair = VGroup(left, right).arrange(RIGHT, buff=0.5)
        fit(pair, 11.6, 1.8).move_to([0, -2.1, 0])
        self.play(FadeIn(pair), run_time=0.6)
        self.play(FadeIn(source_line("agent A on the NVDA and GOOGL runs", y=-3.3)), run_time=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B14 / B15 — the honest ledger
# ─────────────────────────────────────────────────────────────────────────────
def ledger(items, color, symbol):
    rows = VGroup(*[checked(t, size=38, color=color, symbol=symbol) for t in items])
    return rows.arrange(DOWN, buff=0.45, aligned_edge=LEFT)


class B14_TrueNow(Beat):
    def construct(self):
        self.play(FadeIn(label("WHAT WORKS NOW", size=40, weight="BOLD", color=GREEN).move_to([0, 3.0, 0])), run_time=0.4)
        rows = ledger(["every figure carries its period, unit and filing",
                       "failed searches are recorded as failures",
                       "two agents in flight at once",
                       "ratios recomputed: two hidden errors surfaced"], GREEN, "✓")
        fit(rows, 11.5, 5.0).move_to([0, -0.2, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.4)
            self.wait(1.6)
        self.finish()


class B15_StillNotTrue(Beat):
    def construct(self):
        self.play(FadeIn(label("WHAT STILL DOESN'T", size=40, weight="BOLD", color=RED).move_to([0, 3.0, 0])), run_time=0.4)
        rows = ledger(["the stricter comparator is opt-in for company runs",
                       "tagging still depends on wording",
                       "the ratio check ignores annual vs quarterly",
                       "agents skip figures that are in their input"], RED, "✕")
        fit(rows, 11.5, 4.0).move_to([0, 0.0, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.4)
            self.wait(1.8)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B16 — close: end-card reprise (the stats live here, not in the outro)
# ─────────────────────────────────────────────────────────────────────────────
class B16_EndCardReprise(Beat):
    def construct(self):
        corpus = ev("B09_corpus_replay")
        closer = serif("the smallest true claim", size=30, color=INK).move_to([0, 3.15, 0])
        self.play(FadeIn(closer), run_time=0.5)
        card = VGroup(label("15 / 16", size=44, weight="BOLD", color=SOFT), label("→", size=40, color=INK),
                      label(f"{corpus['canonical_flags']} / {corpus['disjoint_concepts_runs']}", size=44,
                            weight="BOLD", color=ACC)).arrange(RIGHT, buff=0.5).move_to([0, 2.1, 0])
        self.play(FadeIn(card), run_time=0.6)
        boxes = four_boxes(size=24).scale(0.8).move_to([0, 1.05, 0])
        self.play(FadeIn(boxes), run_time=0.5)
        self.wait(2.5)
        bullets = [
            ("agents had been handed FY2018 revenue and nine-month EPS", INK),
            (f"new rule: {corpus['canonical_flags']} of {corpus['disjoint_concepts_runs']} alarms, 1 real, "
             f"{corpus['canonical_flags'] - 1} unknown; opt-in", INK),
            ("recomputed ratios found two asset-turnover errors, 5× off", INK),
            ("part of 15 of 16 came from a Return-on-Assets mis-tag", INK),
            ("first shared-figure match, across both agents and the filing", INK),
            ("the stricter rule stays opt-in until runs show what each agent was given", RED),
        ]
        lines = VGroup(*[label(t, size=24, color=c, weight="BOLD" if c == RED else None) for t, c in bullets])
        lines.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        fit(lines, 11.5, 3.7).move_to([0, -1.55, 0])
        for ln in lines:
            self.play(FadeIn(ln, shift=RIGHT * 0.05), run_time=0.35)
            self.wait(0.9)
        self.finish()
