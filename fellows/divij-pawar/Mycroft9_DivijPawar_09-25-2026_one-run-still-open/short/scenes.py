"""short/scenes.py (Mycroft 9) — native 9:16 portrait re-layout of all 19 GRAPHIC beats (full-length vertical).

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


def stack(*elems, top=2.45, bottom=-3.45, buff=0.28, grow=False):
    """Arrange elements top-to-bottom under the title and fit them to the space: no fixed y.
    grow=True also scales UP to fill the space (Gate V underfill)."""
    g = Group(*elems).arrange(DOWN, buff=buff)
    if grow:
        g.scale(min(W / g.width, (top - bottom) / g.height))
    else:
        fit(g, W, top - bottom)
    return g.move_to([0, (top + bottom) / 2, 0])


def export_lines(n=7):
    md = (EVID / "B16_export_8ecb0922_auditor.md").read_text(encoding="utf-8").splitlines()
    keep = [l.replace("\u2014", "-").replace("**", "") for l in md if l.strip() and not l.startswith("|")]
    return keep[:n]


class Beat(Scene):
    def setup(self):
        self.camera.background_color = BG

    def finish(self):
        hold_to(self, target(type(self).__name__))

    def reveal(self, *mobs, rt=0.5, wait=0.0):
        self.play(*[FadeIn(m) for m in mobs], run_time=rt)
        if wait:
            self.wait(wait)


GATE = ("TRIGGER", "STOP", "DECIDER", "RECORD")


def gate_grid(size=26):
    cells = VGroup()
    for n in GATE:
        t = label(n, size=size, weight="BOLD", color=INK)
        r = Rectangle(width=1.8, height=0.75, color=INK)
        cells.add(VGroup(r, t.move_to(r)))
    return cells.arrange_in_grid(rows=2, cols=2, buff=0.18)


def op(sym, size=32):
    return Text(sym, font_size=size, color=INK)


def sub(base, s, size=32):
    b = label(base, size=size, color=INK)
    t = label(s, size=24, color=INK)
    t.next_to(b, RIGHT, buff=0.03).align_to(b, DOWN).shift(DOWN * 0.12)
    return VGroup(b, t)


def illustrative():
    return chip("ILLUSTRATIVE · NOT BUILT YET", AMBER)


class B01_FourPartsOfAGate(Beat):
    def construct(self):
        self.reveal(head("When the agents disagree"))
        g = stack(chip("PART 1: METRIC · PERIOD · UNIT · SOURCE", SOFT),
                  serif(wrap("a flagged contradiction is only useful if something happens next", 22), size=32, color=INK),
                  gate_grid(), cap("without all four, it's only a warning", 0))
        self.reveal(g[0])
        self.reveal(g[1], wait=5.0)
        self.play(LaggedStart(*[FadeIn(c) for c in g[2]], lag_ratio=0.3), run_time=1.8)
        self.wait(4.0)
        self.reveal(g[3])
        self.finish()


class B02_Trigger(Beat):
    def construct(self):
        e = ev("B02_trigger")
        g_, one = e["gated_run"], e["one_sided_run"]
        unc = next(r for r in one["rows"] if r[1] == "UNCORROBORATED")
        self.reveal(head("What opens the gate"))

        def card(title, status, verdict, col):
            return VGroup(txt(title, size=26, weight="BOLD"), mono(status, size=24, color=SOFT),
                          txt(verdict, size=26, color=col, weight="BOLD")).arrange(DOWN, buff=0.08)
        g = stack(card(f"{g_['rows'][0][0]} (run {g_['id']})", g_["rows"][0][1], "→ awaiting decision", ACC),
                  card(f"{unc[0]} (run {one['id']})", unc[1], "→ shown for review, no gate", SOFT),
                  card("a run stored before the gate", "any status", f"→ {e['pre_gate_run_status']}", SOFT),
                  cap("only a two-sided mismatch stops a run", 0), buff=0.45)
        for m in g[:3]:
            self.reveal(m, wait=4.5)
        self.reveal(g[3])
        self.finish()


class B03_DecisionForm(Beat):
    def construct(self):
        e = ev("B03_B04_decision_rules")
        g = stack(shot("B03_gate_open_1280.png", W, 3.6), txt(f"5 outcomes · reason of at least {e['min_rationale']} characters", size=26, weight="BOLD"),
                  txt('"looks good" is 10 characters: refused', size=26, color=ACC, weight="BOLD"), top=3.4, buff=0.3)
        self.reveal(g[0], rt=0.7, wait=4.0)
        self.reveal(g[1], wait=4.0)
        self.reveal(g[2])
        self.finish()


class B04_SmallPrint(Beat):
    def construct(self):
        t = ev("B03_B04_decision_rules")["trials"]

        def card(k, v):
            return boxed(VGroup(txt(k, size=24, color=SOFT, weight="BOLD"), txt(v.replace("refused: ", ""), size=24, width=26)
                                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT), color=ACC)
        g = stack(serif(wrap('"Recorded as entered; not verified."', 20), size=36, color=INK),
                  chip("the login carries a permission level, not a person", SOFT),
                  card("reason too short", t["looks good (10 chars)"]),
                  card("an undisputed figure", t["cites an undisputed figure"]),
                  card("a value without the override", t["value without override"]), top=3.4, buff=0.3)
        self.reveal(g[0])
        self.reveal(g[1], wait=3.5)
        for c in g[2:]:
            self.reveal(c, rt=0.4, wait=1.4)
        self.finish()


class B05_Supersede(Beat):
    def construct(self):
        def card(t):
            return boxed(label(t, size=28, weight="BOLD", color=INK), fill_color=BG, fill_opacity=1)
        c1, c2 = card("decision 1"), card("decision 2 (newer)")
        g = stack(c1, c2, txt("superseded, still on record", size=26, color=SOFT, weight="BOLD"),
                  chip("UPDATE / DELETE → blocked by a database trigger", RED), top=3.4, bottom=-3.4, buff=1.1, grow=True)
        self.reveal(g[0])
        self.play(FadeIn(g[1], shift=DOWN * 0.2), g[0].animate.set_opacity(0.45), run_time=0.6)
        self.reveal(g[2])
        self.reveal(g[3])
        self.finish()


class B06_InvestorView(Beat):
    def construct(self):
        aud = Group(txt("AUDITOR", size=24, color=SOFT, weight="BOLD"), shot("B06_auditor_1280.png", W, 2.5)).arrange(DOWN, buff=0.1)
        inv = Group(txt("INVESTOR", size=24, color=SOFT, weight="BOLD"), shot("B06_investor_1280.png", W, 2.5)).arrange(DOWN, buff=0.1)
        pair = Group(aud, inv).arrange(DOWN, buff=0.3)
        pair.scale(min(W / pair.width, 6.8 / pair.height)).move_to([0, 0.0, 0])
        self.reveal(pair, rt=0.7, wait=6.0)
        self.play(FadeOut(pair), run_time=0.4)
        g = stack(txt("FOUND: '1998' once, in a trace search result", size=26, color=ACC, weight="BOLD"),
                  shot("B06_investor_trace_leak_1280.png", W, 1.0),
                  txt("FIXED: the trace withholds search results while the gate is open", size=26, color=GREEN, weight="BOLD"),
                  mtxt("after the fix: 1998 → 0, 1996 → 0", size=26),
                  txt("still: a read without a token is served at the run's stored level", size=24, weight="BOLD"),
                  top=3.4, bottom=-3.4, buff=0.6, grow=True)
        for m in g:
            self.reveal(m, rt=0.3, wait=0.9)
        self.finish()


class B07_StillOpen(Beat):
    def construct(self):
        e = ev("B00_B07_gated_run_now")
        g = stack(shot("B07_gate_closed_1280.png", W, 1.4), chip(e["gate_status_now"].replace("_", " "), ACC),
                  txt("decisions recorded", size=30, color=SOFT, weight="BOLD"), mono(str(e["decisions_recorded"]), size=72, color=INK),
                  txt("nobody has decided yet: the gate is for a person", size=30, weight="BOLD", width=20),
                  top=3.4, bottom=-3.4, buff=0.9, grow=True)
        for m in g:
            self.reveal(m, rt=0.3, wait=0.2)
        self.finish()


class B08_HardRules(Beat):
    def construct(self):
        self.reveal(head("Hard rules: identities that gate"))
        r1 = VGroup(sub("EPS", "basic"), op("≥"), sub("EPS", "diluted")).arrange(RIGHT, buff=0.2)
        r2 = VGroup(label("FCF", size=32, color=INK), op("="), label("OCF", size=32, color=INK), op("−"), label("CapEx", size=32, color=INK)).arrange(RIGHT, buff=0.18)
        r3 = VGroup(label("Assets", size=32, color=INK), op("="), label("Liabilities", size=32, color=INK)).arrange(RIGHT, buff=0.18)
        r3b = VGroup(op("+"), label("Equity", size=32, color=INK)).arrange(RIGHT, buff=0.18)
        g = stack(r1, r2, VGroup(r3, r3b).arrange(DOWN, buff=0.12), chip("HARD: opens the gate", ACC),
                  txt("assets check allows 2%: stated equity often excludes noncontrolling interest", size=24, color=SOFT),
                  cap("the reviewer can confirm the error instead of picking an agent", 0, size=24), buff=0.4)
        for m in g:
            self.reveal(m, wait=1.6)
        self.finish()


class B09_ClaimVsSource(Beat):
    def construct(self):
        slip = ev("B08_B11_checks")["msft_slip"][0]
        self.reveal(head("Each cited figure vs the filing"))
        given = boxed(VGroup(txt("GIVEN", size=24, color=SOFT, weight="BOLD"), mono("revenue $82.9B", size=30, color=INK)).arrange(DOWN, buff=0.1))
        wrote = boxed(VGroup(txt("WROTE", size=24, color=SOFT, weight="BOLD"), mono("$828,860,000,000", size=30, color=INK)).arrange(DOWN, buff=0.1), color=ACC)
        g = stack(txt("rounding to the digits written is not misquoting", size=26, color=SOFT), given, wrote,
                  label("10×", size=40, weight="BOLD", color=ACC),
                  txt("that attempt halted on format first: this check never ran on it live", size=24, color=AMBER, weight="BOLD"),
                  src(f"stored MSFT run {slip['run_id']}", y=0), buff=0.35)
        self.reveal(g[0], wait=1.5)
        self.reveal(g[1], g[2])
        self.play(Create(ring(g[2][1][1], buff=0.05)), FadeIn(g[3]), run_time=0.6)
        self.wait(2.5)
        self.reveal(g[4], g[5])
        self.finish()


class B10_SoftRules(Beat):
    def construct(self):
        e = ev("B08_B11_checks")
        un = e["googl_unusual"]
        self.reveal(head("Soft rules: usually true, never gate"))
        rule = VGroup(label("net income", size=30, color=INK), op("≤"), label("operating", size=30, color=INK)).arrange(RIGHT, buff=0.15)
        rows = VGroup(*[VGroup(txt(c["who"], size=26, weight="BOLD"), mtxt(c["math"].split(" (")[0], size=24)).arrange(DOWN, buff=0.06) for c in un]).arrange(DOWN, buff=0.2)
        g = stack(rule, txt("(usually)", size=24, color=SOFT), rows,
                  boxed(txt("unusual, worth a look · does not gate", size=26, color=AMBER, weight="BOLD"), color=AMBER),
                  cap("part 1's 'unrecognised $9.11' was Google's filed EPS", 0, size=24), buff=0.4)
        for m in g:
            self.reveal(m, wait=1.4)
        self.finish()


class B11_FilingAndTimeout(Beat):
    def construct(self):
        e = ev("B08_B11_checks")
        led = {i["id"]: i for i in ev("B18_ledger")}
        bal = next(c for c in e["aapl_checks"] if c["rule"] == "balance_sheet_filed")
        self.reveal(head("The filing gets the same checks"))
        g = stack(VGroup(Text("✓", font_size=32, color=GREEN), txt(bal["plain"], size=28, color=GREEN, weight="BOLD", width=20)).arrange(RIGHT, buff=0.15), mtxt(bal["math"], size=24),
                  mtxt("model: no reply to a 5-token request within 60 s", size=26),
                  boxed(VGroup(txt(f"OPEN ISSUE · {led['ollama-hangs-under-compare']['severity'].upper()}", size=24, color=RED, weight="BOLD"),
                               txt("no timeout on model calls: a stuck model holds a comparison forever", size=24)).arrange(DOWN, buff=0.1), color=RED),
                  buff=0.45)
        for m in g:
            self.reveal(m, wait=2.0)
        self.finish()


class B12_SourceExcerpt(Beat):
    def construct(self):
        e = ev("B12_filing_excerpt")
        self.reveal(head("Found in the filing itself"))
        items = [VGroup(mono(c, size=24, color=SOFT), mtxt(f"'{r['row_label']}' | {r['displayed']} as filed", size=24)).arrange(DOWN, buff=0.06)
                 for c, r in e["found"].items()]
        g = stack(chip("recorded output · find_in_document() on the real Apple 10-Q", GHOST), *items,
                  chip("last batch: 24 / 24 figures found, every filed value equal", GREEN),
                  chip("in the review: every figure has a Source button", ACC), buff=0.35)
        for m in g:
            self.reveal(m, wait=1.8)
        self.finish()


class B13_LiveLanes(Beat):
    def construct(self):
        e = ev("B13_stream_events")
        ph = e["steps_by_phase"]

        def lane(name, col, lines):
            hdr = label(name, size=26, weight="BOLD", color=BG)
            hb = auto_box(hdr, h_pad=0.4, v_pad=0.15, color=col, fill_color=col, fill_opacity=1)
            body = VGroup(*[txt(l, size=24) for l in lines]).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
            fr = SurroundingRectangle(body, buff=0.2, color=col, stroke_width=3)
            return VGroup(VGroup(hb, hdr), VGroup(fr, body)).arrange(DOWN, buff=0)
        shared = chip(f"{len(ph['shared'])} shared steps: fetch once, summarise for each agent", GHOST)
        g = stack(txt("ONE SEC FETCH, BOTH AGENTS", size=30, color=SOFT, weight="BOLD"), shared,
                  lane("AGENT A", LANE_A, [ph["agent_a"][0], "thinking… (live timer)", "citations become links"]),
                  lane("AGENT B", LANE_B, [ph["agent_b"][0], "searching: <query>…", "finished"]),
                  src("diagram of a real captured event stream (AAPL run)", y=0), top=3.4, buff=0.3)
        for m in g:
            self.reveal(m, wait=1.0)
        self.finish()


class B14_Assessment(Beat):
    def construct(self):
        self.reveal(head("A second call reads the answer"))
        g = stack(shot("B14_grades_1280.png", W, 2.4), chip("labelled model judgment", SOFT),
                  chip("quotes not in the answer or inputs are dropped", SOFT), chip("extraction fails: the run carries on and says so", SOFT),
                  src("run 8ecb0922, AAPL · captured from /app", y=0), buff=0.35)
        self.reveal(g[0], rt=0.7, wait=4.0)
        for m in g[1:]:
            self.reveal(m, rt=0.4, wait=1.2)
        self.finish()


class B15_DivergenceAndConsensus(Beat):
    def construct(self):
        bins = VGroup(*[boxed(VGroup(label(x, size=28, weight="BOLD", color=INK), txt(d, size=24, color=SOFT)).arrange(DOWN, buff=0.08))
                        for x, d in (("DATA", "different figures or periods"), ("ASSUMPTION", "same figures, other assumptions"), ("WEIGHTING", "same evidence, weighed differently"))]).arrange(DOWN, buff=0.15)
        rule = VGroup(txt("grade AND direction agree", size=26, weight="BOLD"), txt("AND no hard rule failed", size=26, weight="BOLD", color=ACC),
                      txt("→ consensus", size=26, weight="BOLD", color=GREEN)).arrange(DOWN, buff=0.06)
        g = stack(bins, rule, shot("B15_grade_gate_1280.png", W, 1.0),
                  cap("accept A, accept B, or set the grade; investors see none until then", 0, size=24), top=3.4, buff=0.5)
        self.play(LaggedStart(*[FadeIn(b) for b in g[0]], lag_ratio=0.3), run_time=1.2)
        self.wait(3.0)
        for m in g[1:]:
            self.reveal(m, wait=1.5)
        self.finish()


class B16_AnswerFirst(Beat):
    def construct(self):
        self.reveal(head("Answer first, then export"))
        parts = ["the answer, and any failed check", "the decision", "the evidence", "the agents", "the machinery (folded)"]
        order = VGroup(*[txt(f"{i + 1}  {p}", size=24, weight="BOLD" if i == 0 else None, color=INK if i < 4 else SOFT, width=30) for i, p in enumerate(parts)]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        md = boxed(VGroup(*[mtxt(l[:40], size=24, width=40) for l in export_lines(5)]).arrange(DOWN, buff=0.1, aligned_edge=LEFT), color=SOFT)
        g = stack(order, txt("review-8ecb0922.md (recorded export)", size=24, color=SOFT, weight="BOLD"), md, buff=0.35)
        self.play(LaggedStart(*[FadeIn(x) for x in g[0]], lag_ratio=0.25), run_time=1.4)
        self.reveal(g[1], g[2])
        self.finish()


class B17_TrueNow(Beat):
    def construct(self):
        self.reveal(txt("WHAT WORKS NOW", size=40, color=GREEN, weight="BOLD").move_to([0, 3.0, 0]))
        rows = ledger(["a mismatch, failed check or grade split stops the run", "decisions need a reason and can't be edited",
                       "investors get no disputed value, answer or search result", "every review exports as a plain document"], GREEN, "✓").move_to([0, -0.3, 0])
        for r in rows:
            self.reveal(r, rt=0.4, wait=1.8)
        self.finish()


class B18_StillNotTrue(Beat):
    def construct(self):
        self.reveal(txt("WHAT STILL DOESN'T", size=40, color=RED, weight="BOLD").move_to([0, 3.0, 0]))
        rows = ledger(["the decider's name is typed, never verified", "anyone can mint a reviewer token",
                       "storage holds everything; withheld only when read", "the grade is the same model judging itself",
                       "model calls have no timeout"], RED, "✕").move_to([0, -0.3, 0])
        for r in rows:
            self.reveal(r, rt=0.35, wait=1.6)
        self.finish()


class B19_EndCardReprise(Beat):
    def construct(self):
        e = ev("B00_B07_gated_run_now")
        a, b = e["rows"][0][2], e["rows"][0][3]
        card = VGroup(VGroup(mono(a, size=40, color=LANE_A), label("2 years", size=28, weight="BOLD", color=INK), mono(b, size=40, color=LANE_B)).arrange(RIGHT, buff=0.3),
                      chip(e["gate_status_now"].replace("_", " "), ACC)).arrange(DOWN, buff=0.15)
        bullets = ["a mismatch now stops the run for a named person", "20+ character reason; superseded, never edited",
                   "disputed values, answers and searches withheld", "hard rules gate; soft rules inform",
                   "identity self-declared; no model-call timeout", "the grade is model judgment until a person sets it"]
        lines = VGroup(*[label(wrap(t, 28), size=26, color=RED if i == 5 else INK, weight="BOLD" if i == 5 else None, line_spacing=0.85)
                         for i, t in enumerate(bullets)]).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        g = stack(serif("the smallest true claim", size=32, color=INK), card, gate_grid(24).scale(0.6), lines, top=3.5, buff=0.3)
        self.reveal(g[0], g[1])
        self.reveal(g[2], wait=2.5)
        for ln in g[3]:
            self.reveal(ln, rt=0.3, wait=1.0)
        self.finish()
