"""scenes.py — Manim scenes for one-run-still-open (Mycroft 9, audit-layer update part 2 of 2).

Same conventions and helpers as ../Mycroft8_DivijPawar_09-18-2026_the-rule-that-lost/scenes.py
(copied, not imported, so each reel folder is self-contained):
  - "claude" palette, graphics_lib type system, content-fitted boxes, hold_to() timing
  - EXECUTABLE EVIDENCE: numbers and refusal text are read at render time from
    assets/evidence/out/*.json (assets/evidence/m9_evidence.py, read-only, records no decision)
  - TARGETs come from beat_sheet.json (actual_duration_s once Kokoro has run)
  - structured math without LaTeX (none installed): sub() gives real lowered subscripts and
    operators render in Manim's default font, per MATH-TYPESETTING.md
  - real app screenshots of run ec1a3b44 are HOLD evidence

[verify] beats B14-B16 describe roadmap features that are not in the checkout yet. Each carries an
on-screen "ILLUSTRATIVE · NOT BUILT YET" chip until the feature exists; replace
them with real captures then, or cut them to the coda (see PEDAGOGY.md).

B00 (ClaudeComposerAsk) and B20 (ClaudeTitleOutro) are Remotion beats. Safe frame: x in
[-6.4, 6.4], y in [-3.6, 3.6]. Nothing in this file has been rendered at 4K yet.
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


def fit_w(group, max_width=11.0):
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


def export_lines(n=7):
    md = (EVID / "B16_export_8ecb0922_auditor.md").read_text(encoding="utf-8").splitlines()
    keep = [l.replace("\u2014", "-").replace("**", "") for l in md if l.strip() and not l.startswith("|")]
    return keep[:n]


class Beat(Scene):
    def setup(self):
        self.camera.background_color = BG

    def finish(self):
        hold_to(self, target(type(self).__name__))


def op(sym, size=34, color=INK):
    """Math operators in Manim's default font: Montserrat lacks some glyphs (see graphics_lib)."""
    return Text(sym, font_size=size, color=color)


def sub(base, subscript, size=34, color=INK):
    """Base with a real, lowered subscript (MATH-TYPESETTING.md)."""
    b = label(base, size=size, color=color)
    s = label(subscript, size=24, color=color)
    s.next_to(b, RIGHT, buff=0.04).align_to(b, DOWN).shift(DOWN * 0.14)
    return VGroup(b, s)


GATE = ("TRIGGER", "STOP", "DECIDER", "RECORD")


def gate_boxes(lit=(), size=26, gap=0.35):
    cells = VGroup()
    for name in GATE:
        on = name in lit
        t = label(name, size=size, weight="BOLD", color=BG if on else INK)
        b = auto_box(t, h_pad=0.4, v_pad=0.28, color=ACC if on else INK, fill_color=ACC, fill_opacity=1 if on else 0)
        cells.add(VGroup(b, t))
    return cells.arrange(RIGHT, buff=gap)


def gate_chip(lit):
    return gate_boxes(lit, size=24, gap=0.12).scale(0.5).move_to([3.95, -3.2, 0])


def row_chip(name, status, verdict, vcolor):
    n = label(name, size=26, weight="BOLD", color=INK)
    s = mono(status, size=26, color=SOFT)
    v = label(verdict, size=24, weight="BOLD", color=vcolor)
    return VGroup(n, s, v)


# ─────────────────────────────────────────────────────────────────────────────
# B01 — recap and the four parts of a gate (framework before example)
# ─────────────────────────────────────────────────────────────────────────────
class B01_FourPartsOfAGate(Beat):
    def construct(self):
        recap = label_chip("PART 1: METRIC · PERIOD · UNIT · SOURCE", SOFT, size=22).move_to([0, 3.05, 0])
        self.play(FadeIn(recap), run_time=0.4)
        q = serif("a flagged contradiction is only useful\nif something happens next", size=44, color=INK)
        self.play(FadeIn(fit_w(q).move_to([0, 1.55, 0])), run_time=0.6)
        self.wait(5.5)
        boxes = gate_boxes(size=34, gap=0.45).move_to([0, -0.45, 0])
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.1) for b in boxes], lag_ratio=0.3), run_time=1.8)
        self.wait(4.0)
        self.play(FadeIn(caption("without all four, it's only a warning", y=-2.2, size=32)), run_time=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B02 — trigger
# ─────────────────────────────────────────────────────────────────────────────
class B02_Trigger(Beat):
    def construct(self):
        e = ev("B02_trigger")
        self.add(gate_chip({"TRIGGER"}))
        self.play(FadeIn(head("WHAT OPENS THE GATE")), run_time=0.4)
        g = e["gated_run"]
        one = e["one_sided_run"]
        unc = next(r for r in one["rows"] if r[1] == "UNCORROBORATED")
        rows = [
            row_chip(f"{g['rows'][0][0]}  (run {g['id']})", g["rows"][0][1], "→  AWAITING DECISION", ACC),
            row_chip(f"{unc[0]}  (run {one['id']})", unc[1], "→  shown for review, no gate", SOFT),
            row_chip("a run stored before the gate", "any status", f"→  {e['pre_gate_run_status']}", SOFT),
        ]
        for i, r in enumerate(rows):
            y = 1.6 - i * 1.35
            r[0].move_to([-5.9, y + 0.25, 0], aligned_edge=LEFT)
            r[1].move_to([-5.9, y - 0.25, 0], aligned_edge=LEFT)
            r[2].move_to([1.2, y, 0], aligned_edge=LEFT)
            fit_w(r, 12.2)
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.6)
            self.wait(4.5)
        self.play(FadeIn(caption("only a two-sided mismatch stops a run", y=-2.6)), run_time=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B03 — the decision form (real screenshot of run ec1a3b44)
# ─────────────────────────────────────────────────────────────────────────────
class B03_DecisionForm(Beat):
    def construct(self):
        e = ev("B03_B04_decision_rules")
        self.add(gate_chip({"DECIDER"}))
        shot = screenshot("B03_gate_open_1280.png", 7.2, 6.6).move_to([-2.55, 0.15, 0])
        self.play(FadeIn(shot), run_time=0.7)
        self.wait(2.0)
        notes = VGroup(
            label("opens in place,", size=26, weight="BOLD", color=INK),
            label("the evidence stays visible", size=26, weight="BOLD", color=INK),
            label("5 outcomes", size=26, color=INK),
            label(f"reason: at least {e['min_rationale']} characters", size=26, color=INK),
            label("\"looks good\" is 10 characters:", size=24, color=SOFT),
            label("refused: " + e["trials"]["looks good (10 chars)"].replace("refused: ", "").replace(" in at least", "\nin at least"),
                  size=24, color=ACC, line_spacing=0.8),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        fit(notes, 4.9, 5.6).move_to([3.75, 0.2, 0])
        for n in notes:
            self.play(FadeIn(n, shift=LEFT * 0.1), run_time=0.35)
            self.wait(1.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B04 — identity and refusals (the server's own refusal text)
# ─────────────────────────────────────────────────────────────────────────────
class B04_SmallPrint(Beat):
    def construct(self):
        e = ev("B03_B04_decision_rules")["trials"]
        self.add(gate_chip({"DECIDER"}))
        q = serif("\"Recorded as entered; not verified.\"", size=40, color=INK).move_to([0, 2.5, 0])
        self.play(FadeIn(q), run_time=0.6)
        chip = label_chip("the login carries a permission level, not a person", SOFT, size=22, upper=False)
        self.play(FadeIn(chip.move_to([0, 1.5, 0])), run_time=0.4)
        self.wait(3.5)
        cards = VGroup(*[
            boxed(VGroup(label(k, size=24, weight="BOLD", color=SOFT),
                         label(v.replace("refused: ", ""), size=24, color=INK)).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
                  color=ACC)
            for k, v in (("reason too short", e["looks good (10 chars)"]),
                         ("an undisputed figure", e["cites an undisputed figure"]),
                         ("a value without the override", e["value without override"]))
        ]).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        fit(cards, 11.5, 3.3).move_to([0, -1.05, 0])
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.1), run_time=0.4)
            self.wait(1.4)
        src = source_line("refusal text: validate_decision() on the real payload, nothing recorded")
        fit_w(src, 7.4).move_to([-2.2, -3.45, 0])
        self.play(FadeIn(src), run_time=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B05 — the record: supersede, never edit
# ─────────────────────────────────────────────────────────────────────────────
class B05_Supersede(Beat):
    def construct(self):
        self.add(gate_chip({"RECORD"}))

        def card(t):
            return boxed(label(t, size=26, weight="BOLD", color=INK), color=INK, fill_color=BG, fill_opacity=1)

        c1 = card("decision 1").move_to([-2.4, 1.2, 0])
        c2 = card("decision 2 (newer)").move_to([1.6, 0.2, 0])
        self.play(FadeIn(c1), run_time=0.4)
        self.play(FadeIn(c2, shift=DOWN * 0.2), c1.animate.set_opacity(0.45), run_time=0.6)
        tag = label("superseded, still on record", size=24, weight="BOLD", color=SOFT).next_to(c1, UP, buff=0.2)
        self.play(FadeIn(tag), run_time=0.3)
        blocked = label_chip("UPDATE / DELETE  →  BLOCKED BY A DATABASE TRIGGER", RED, size=22).move_to([0, -1.5, 0])
        self.play(FadeIn(blocked), run_time=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B06 — what an investor sees, and the hole (falsifiability)
# ─────────────────────────────────────────────────────────────────────────────
class B06_InvestorView(Beat):
    def construct(self):
        aud = screenshot("B06_auditor_1280.png", 5.9, 4.6)
        inv = screenshot("B06_investor_1280.png", 5.9, 4.6)
        pair = Group(aud, inv).arrange(RIGHT, buff=0.4).move_to([0, 0.6, 0])
        la = label("AUDITOR", size=24, weight="BOLD", color=SOFT).next_to(aud, UP, buff=0.15)
        li = label("INVESTOR", size=24, weight="BOLD", color=SOFT).next_to(inv, UP, buff=0.15)
        self.play(FadeIn(pair), FadeIn(la), FadeIn(li), run_time=0.7)
        self.wait(6.0)
        self.play(FadeOut(Group(pair, la, li)), run_time=0.5)
        found = label("FOUND: '1998' once, in a search result in the trace", size=28, weight="BOLD", color=ACC).move_to([0, 2.7, 0])
        leak = screenshot("B06_investor_trace_leak_1280.png", 11.8, 1.3).move_to([0, 1.7, 0])
        self.play(FadeIn(fit_w(found)), FadeIn(leak), run_time=0.6)
        self.play(Create(ring(leak[0], buff=0.05)), run_time=0.5)
        self.wait(3.0)
        fixed = VGroup(label("FIXED: the trace withholds what each search returned while the gate is open", size=26, weight="BOLD", color=GREEN),
                       mono("investor read after the fix:  '1998' 0   '1996' 0", size=28, color=INK)).arrange(DOWN, buff=0.2)
        self.play(FadeIn(fit_w(fixed).move_to([0, 0.1, 0])), run_time=0.6)
        self.wait(3.0)
        lim = label("still: a read without a token is served at the run's stored level", size=24, weight="BOLD", color=INK)
        self.play(FadeIn(fit_w(lim).move_to([0, -1.4, 0])), run_time=0.5)
        self.play(FadeIn(source_line("found, fixed, and verified on a restarted server, 2026-09-26")), run_time=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B07 — the gate the builder didn't clear
# ─────────────────────────────────────────────────────────────────────────────
class B07_StillOpen(Beat):
    def construct(self):
        e = ev("B00_B07_gated_run_now")
        shot = screenshot("B07_gate_closed_1280.png", 11.8, 2.4).move_to([0, 1.9, 0])
        self.play(FadeIn(shot), run_time=0.6)
        facts = VGroup(label_chip(e["gate_status_now"].replace("_", " "), ACC, size=24),
                       mono(f"decisions recorded: {e['decisions_recorded']}", size=30, color=INK)
                       ).arrange(RIGHT, buff=0.6).scale(1.15).move_to([0, -0.2, 0])
        self.play(FadeIn(facts), run_time=0.5)
        self.play(FadeIn(caption("nobody has decided yet: the gate is for a person", y=-2.1, size=36)), run_time=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B08 — rules that stop a run (structured math, no LaTeX needed)
# ─────────────────────────────────────────────────────────────────────────────
class B08_HardRules(Beat):
    def construct(self):
        self.play(FadeIn(head("HARD RULES: IDENTITIES THAT GATE")), run_time=0.4)
        r1 = VGroup(sub("EPS", "basic"), op("≥"), sub("EPS", "diluted")).arrange(RIGHT, buff=0.3)
        r2 = VGroup(label("FCF", size=34, color=INK), op("="), label("OCF", size=34, color=INK), op("−"),
                    label("CapEx", size=34, color=INK)).arrange(RIGHT, buff=0.3)
        r3 = VGroup(label("Assets", size=34, color=INK), op("="), label("Liabilities", size=34, color=INK), op("+"),
                    label("Equity", size=34, color=INK)).arrange(RIGHT, buff=0.3)
        rules = VGroup(r1, r2, r3).arrange(DOWN, buff=0.55, aligned_edge=LEFT).move_to([-2.2, 0.7, 0])
        for r in rules:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.5)
            self.wait(1.8)
        tags = VGroup(*[label_chip("HARD: OPENS THE GATE", ACC, size=20).next_to(r, RIGHT, buff=0.5) for r in rules])
        for t in tags:
            t.set_x(3.75)
        self.play(FadeIn(tags), run_time=0.5)
        tol = label("assets check allows 2%: stated equity often excludes noncontrolling interest", size=24, color=SOFT)
        self.play(FadeIn(fit_w(tol).move_to([0, -1.3, 0])), run_time=0.4)
        self.wait(2.0)
        self.play(FadeIn(caption("the reviewer can confirm the error instead of picking an agent", y=-2.3)), run_time=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B09 — claim versus source: the 10x slip
# ─────────────────────────────────────────────────────────────────────────────
class B09_ClaimVsSource(Beat):
    def construct(self):
        e = ev("B08_B11_checks")
        slip = e["msft_slip"][0]
        self.play(FadeIn(head("EACH CITED FIGURE vs THE FILING IT WAS GIVEN")), run_time=0.4)
        rule = label("rounding to the digits written is not misquoting", size=26, color=SOFT).move_to([0, 2.4, 0])
        self.play(FadeIn(rule), run_time=0.4)
        self.wait(2.0)
        given = boxed(VGroup(label("GIVEN", size=24, weight="BOLD", color=SOFT), mono("revenue $82.9B", size=32, color=INK)
                             ).arrange(DOWN, buff=0.15), color=INK)
        wrote = boxed(VGroup(label("WROTE", size=24, weight="BOLD", color=SOFT), mono("$828,860,000,000", size=32, color=INK)
                             ).arrange(DOWN, buff=0.15), color=ACC)
        pair = VGroup(given, wrote).arrange(RIGHT, buff=1.0).move_to([0, 0.6, 0])
        self.play(FadeIn(pair), run_time=0.6)
        x10 = label("10×", size=40, weight="BOLD", color=ACC).next_to(wrote, DOWN, buff=0.2)
        self.play(Create(ring(wrote[1][1], buff=0.08)), FadeIn(x10), run_time=0.6)
        self.wait(3.0)
        note = label("that attempt halted on format first: this check never ran on it live",
                     size=24, weight="BOLD", color=AMBER)
        self.play(FadeIn(fit_w(note).move_to([0, -1.7, 0])), run_time=0.5)
        self.play(FadeIn(source_line(f"stored MSFT run {slip['run_id']}: \"revenue was $828,860,000,000 USD\"", y=-2.5)), run_time=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B10 — rules that only inform
# ─────────────────────────────────────────────────────────────────────────────
class B10_SoftRules(Beat):
    def construct(self):
        e = ev("B08_B11_checks")
        un = e["googl_unusual"]
        self.play(FadeIn(head("SOFT RULES: USUALLY TRUE, NEVER GATE")), run_time=0.4)
        rule = VGroup(label("net income", size=32, color=INK), op("≤"), label("operating income", size=32, color=INK),
                      label("(usually)", size=26, color=SOFT)).arrange(RIGHT, buff=0.3).move_to([0, 2.2, 0])
        self.play(FadeIn(rule), run_time=0.5)
        self.wait(2.0)
        rows = VGroup(*[
            VGroup(label(c["who"], size=26, weight="BOLD", color=INK), mono(c["math"], size=24, color=INK)).arrange(RIGHT, buff=0.4)
            for c in un
        ]).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        fit_w(rows).move_to([0, 0.9, 0])
        self.play(FadeIn(rows), run_time=0.6)
        call = boxed(label("unusual, worth a look  ·  does not gate", size=26, weight="BOLD", color=AMBER), color=AMBER)
        reason = label(un[0]["reason"], size=24, color=SOFT)
        blk = VGroup(call, fit_w(reason)).arrange(DOWN, buff=0.2).move_to([0, -0.8, 0])
        self.play(FadeIn(blk), run_time=0.5)
        self.wait(2.0)
        self.play(FadeIn(caption("part 1's 'unrecognised $9.11' was Google's filed EPS", y=-2.4)), run_time=0.5)
        self.play(FadeIn(source_line(f"stored GOOGL run {e['googl_run']}")), run_time=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B11 — the filing, and an honest gap
# ─────────────────────────────────────────────────────────────────────────────
class B11_FilingAndTimeout(Beat):
    def construct(self):
        e = ev("B08_B11_checks")
        led = {i["id"]: i for i in ev("B18_ledger")}
        bal = next(c for c in e["aapl_checks"] if c["rule"] == "balance_sheet_filed")
        self.play(FadeIn(head("THE FILING GETS THE SAME CHECKS")), run_time=0.4)
        ok = VGroup(checked(bal["plain"], size=28, color=GREEN, weight="BOLD"), mono(bal["math"], size=24, color=INK)
                    ).arrange(DOWN, buff=0.15)
        self.play(FadeIn(fit_w(ok).move_to([0, 1.9, 0])), run_time=0.5)
        self.wait(3.0)
        status = mono("model: no reply to a 5-token request within 60 s", size=28, color=INK).move_to([0, 0.5, 0])
        self.play(FadeIn(fit_w(status)), run_time=0.5)
        h = led["ollama-hangs-under-compare"]
        card = boxed(VGroup(label(f"OPEN ISSUE · {h['severity'].upper()}", size=24, weight="BOLD", color=RED),
                            label("no timeout on model calls: a stuck model holds a comparison forever",
                                  size=24, color=INK)).arrange(DOWN, buff=0.15, aligned_edge=LEFT), color=RED)
        self.play(FadeIn(fit_w(card).move_to([0, -1.2, 0])), run_time=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B12 — show me where it says that (recorded output; no UI exists yet)
# ─────────────────────────────────────────────────────────────────────────────
class B12_SourceExcerpt(Beat):
    def construct(self):
        e = ev("B12_filing_excerpt")
        self.play(FadeIn(head("FOUND IN THE FILING ITSELF")), run_time=0.4)
        tag = label_chip("RECORDED OUTPUT · find_in_document() on the real Apple 10-Q", GHOST, size=22, upper=False)
        self.play(FadeIn(fit_w(tag).move_to([0, 2.45, 0])), run_time=0.4)
        lines = VGroup(*[VGroup(mono(c, size=24, color=SOFT),
                                mono(f"row '{r['row_label']}'  |  '{r['displayed']}' as filed  =  {r['value']:,.2f}", size=26, color=INK)
                                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT) for c, r in e["found"].items()]).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        term = boxed(lines, color=SOFT, h_pad=0.4, v_pad=0.3)
        fit(term, 11.8, 3.3).move_to([0, 0.35, 0])
        self.play(FadeIn(term), run_time=0.6)
        self.wait(4.0)
        tally = label_chip("LAST BATCH: 24 / 24 FIGURES FOUND · EVERY FILED VALUE EQUAL", GREEN, size=22)
        self.play(FadeIn(fit_w(tally).move_to([0, -1.75, 0])), run_time=0.5)
        self.play(FadeIn(label_chip("IN THE REVIEW: EVERY FIGURE HAS A SOURCE BUTTON", ACC, size=22).move_to([0, -2.5, 0])), run_time=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B13 — watching it run (diagram driven by the recorded stream's events)
# ─────────────────────────────────────────────────────────────────────────────
class B13_LiveLanes(Beat):
    def construct(self):
        e = ev("B13_stream_events")
        phases = e["steps_by_phase"]
        shared = VGroup(*[label_chip(s.replace("_", " "), GHOST, size=20, upper=False) for s in phases["shared"]]
                        ).arrange(RIGHT, buff=0.15)
        bar_lab = label("ONE SEC FETCH, BOTH AGENTS", size=24, weight="BOLD", color=SOFT)
        top = VGroup(bar_lab, fit_w(shared, 11.5)).arrange(DOWN, buff=0.15).move_to([0, 2.5, 0])
        self.play(FadeIn(top), run_time=0.6)

        def lane(name, color, steps, x):
            hdr = label(name, size=26, weight="BOLD", color=BG)
            hb = auto_box(hdr, h_pad=0.5, v_pad=0.2, color=color, fill_color=color, fill_opacity=1)
            body = VGroup(*[label(s, size=24, color=INK) for s in steps]).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
            frame = Rectangle(width=5.4, height=2.6, color=color, stroke_width=3)
            g = VGroup(VGroup(hb, hdr), frame).arrange(DOWN, buff=0)
            body.move_to(frame)
            return VGroup(g, body).move_to([x, -0.35, 0])

        la = lane("AGENT A", LANE_A, [f"{phases['agent_a'][0]}", "thinking… (live timer)", "citations resolve into links"], -2.9)
        lb = lane("AGENT B", LANE_B, [f"{phases['agent_b'][0]}", "searching: <query>…", "finished"], 2.9)
        self.play(FadeIn(la), FadeIn(lb), run_time=0.7)
        counts = e["event_counts"]
        cap = label(f"recorded stream: {counts.get('step_started', 0)} steps started · {counts.get('step_finished', 0)} finished · "
                    f"{counts.get('agent_finished', 0)} agents done", size=24, color=SOFT)
        self.play(FadeIn(fit_w(cap).move_to([0, -2.4, 0])), run_time=0.4)
        self.play(FadeIn(source_line("diagram of a real captured event stream (AAPL run)")), run_time=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B14–B16 — [verify] roadmap beats: labelled on screen until the code is logged
# ─────────────────────────────────────────────────────────────────────────────
def illustrative():
    return label_chip("ILLUSTRATIVE · NOT BUILT YET", AMBER, size=20).move_to([0, 3.25, 0])


class B14_Assessment(Beat):
    def construct(self):
        self.play(FadeIn(head("A SECOND CALL READS THE ANSWER FOR A GRADE")), run_time=0.4)
        shot_ = screenshot("B14_grades_1280.png", 11.6, 3.6).move_to([0, 0.9, 0])
        self.play(FadeIn(shot_), run_time=0.7)
        self.wait(4.0)
        chips = VGroup(label_chip("labelled model judgment", SOFT, size=22, upper=False),
                       label_chip("quotes not in the answer or inputs are dropped", SOFT, size=22, upper=False),
                       label_chip("extraction fails: the run carries on and says so", SOFT, size=22, upper=False)
                       ).arrange(DOWN, buff=0.18)
        self.play(FadeIn(fit_w(chips).move_to([0, -2.0, 0])), run_time=0.6)
        self.play(FadeIn(source_line("run 8ecb0922, AAPL · captured from /app")), run_time=0.3)
        self.finish()


class B15_DivergenceAndConsensus(Beat):
    def construct(self):
        bins = VGroup(*[boxed(VGroup(label(t, size=28, weight="BOLD", color=INK), label(d, size=24, color=SOFT)).arrange(DOWN, buff=0.12), color=INK)
                        for t, d in (("DATA", "different figures or periods"), ("ASSUMPTION", "same figures, other assumptions"),
                                     ("WEIGHTING", "same evidence, weighed differently"))]).arrange(RIGHT, buff=0.35)
        self.play(LaggedStart(*[FadeIn(b) for b in fit_w(bins).move_to([0, 2.55, 0])], lag_ratio=0.3), run_time=1.2)
        rule = VGroup(label("grade AND direction agree", size=26, weight="BOLD", color=INK), label("AND no hard rule failed", size=26, weight="BOLD", color=ACC),
                      op("→"), label("consensus", size=26, weight="BOLD", color=GREEN)).arrange(RIGHT, buff=0.3)
        self.play(FadeIn(fit_w(rule).move_to([0, 1.35, 0])), run_time=0.5)
        self.wait(3.0)
        g = screenshot("B15_grade_gate_1280.png", 11.6, 1.8).move_to([0, -0.2, 0])
        self.play(FadeIn(g), run_time=0.6)
        self.play(FadeIn(caption("accept A's grade, accept B's, or set the grade · investors see none until then", y=-1.7, size=24)), run_time=0.4)
        self.play(FadeIn(source_line("run 8ecb0922: AAA vs A, driver: assumption (stable vs expanding margins)", y=-2.5)), run_time=0.3)
        self.finish()


class B16_AnswerFirst(Beat):
    def construct(self):
        self.play(FadeIn(head("ANSWER FIRST, THEN EXPORT")), run_time=0.4)
        parts = ["the answer, and any failed check", "the decision", "the evidence, figure by figure", "the agents", "the machinery (folded)"]
        stack_ = VGroup(*[label(f"{i + 1}  {p}", size=24, weight="BOLD" if i == 0 else None, color=INK if i < 4 else SOFT) for i, p in enumerate(parts)]
                        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        fit(stack_, 4.6, 4.5).move_to([-3.1, 0.3, 0])
        self.play(LaggedStart(*[FadeIn(x) for x in stack_], lag_ratio=0.25), run_time=1.4)
        md = VGroup(*[mono(l[:40], size=26, color=INK) for l in export_lines(8)]).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        box = boxed(md, color=SOFT, h_pad=0.3, v_pad=0.25)
        tag = label("review-8ecb0922.md  (recorded export)", size=24, weight="BOLD", color=SOFT)
        grp = VGroup(tag, box).arrange(DOWN, buff=0.15)
        fit(grp, 6.2, 5.4).move_to([2.55, 0.1, 0])
        self.play(FadeIn(grp), run_time=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B17 / B18 — the honest ledger
# ─────────────────────────────────────────────────────────────────────────────
def ledger(items, color, symbol):
    return VGroup(*[checked(t, size=36, color=color, symbol=symbol) for t in items]).arrange(DOWN, buff=0.42, aligned_edge=LEFT)


class B17_TrueNow(Beat):
    def construct(self):
        self.play(FadeIn(label("WHAT WORKS NOW", size=40, weight="BOLD", color=GREEN).move_to([0, 3.0, 0])), run_time=0.4)
        rows = ledger(["a mismatch, failed check or grade split stops the run", "decisions need a reason and can't be edited",
                       "investors get no disputed value, answer or search result", "every review exports as a plain document"], GREEN, "✓")
        fit(rows, 11.5, 4.6).move_to([0, -0.1, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.4)
            self.wait(1.8)
        self.finish()


class B18_StillNotTrue(Beat):
    def construct(self):
        self.play(FadeIn(label("WHAT STILL DOESN'T", size=40, weight="BOLD", color=RED).move_to([0, 3.05, 0])), run_time=0.4)
        rows = ledger(["the decider's name is typed, never verified", "anyone can mint a reviewer token",
                       "storage holds everything; withheld only when read", "the grade is the same model judging itself",
                       "model calls have no timeout"], RED, "✕")
        fit(rows, 11.5, 4.6).move_to([0, -0.1, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.35)
            self.wait(1.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
# B19 — close: end-card reprise with the takeaway
# ─────────────────────────────────────────────────────────────────────────────
class B19_EndCardReprise(Beat):
    def construct(self):
        e = ev("B00_B07_gated_run_now")
        a, b = e["rows"][0][2], e["rows"][0][3]
        closer = serif("the smallest true claim", size=30, color=INK).move_to([0, 3.15, 0])
        self.play(FadeIn(closer), run_time=0.5)
        card = VGroup(mono(a, size=40, color=LANE_A), label("2 years", size=30, weight="BOLD", color=INK),
                      mono(b, size=40, color=LANE_B), label_chip(e["gate_status_now"].replace("_", " "), ACC, size=22)
                      ).arrange(RIGHT, buff=0.5).move_to([0, 2.2, 0])
        self.play(FadeIn(card), run_time=0.6)
        boxes = gate_boxes(size=24).scale(0.8).move_to([0, 1.15, 0])
        self.play(FadeIn(boxes), run_time=0.5)
        self.wait(3.0)
        bullets = [
            ("a mismatch now stops the run for a named person", INK),
            ("reason of 20+ characters; decisions superseded, never edited", INK),
            ("disputed values, answers and search results withheld", INK),
            ("hard accounting rules gate; soft rules inform", INK),
            ("identity self-declared; no model-call timeout", INK),
            ("the grade is model judgment until a person sets it", RED),
        ]
        lines = VGroup(*[label(t, size=24, color=c, weight="BOLD" if c == RED else None) for t, c in bullets])
        lines.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        fit(lines, 11.5, 3.6).move_to([0, -1.55, 0])
        for ln in lines:
            self.play(FadeIn(ln, shift=RIGHT * 0.05), run_time=0.35)
            self.wait(1.1)
        self.finish()
