"""vox_scenes.py — Why the 90-Day Clock Is a Gate, Not a Tiebreaker
(vox-ninety-day-gate, slate cut, 16:9)

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat.
B02 is a STILL · ai beat and has no scene class here.

Color law:
  TEAL   = within-authorization / reachable roles / factor near 1
  CRIMSON= past-authorization / timeline gate zeroed / skip-regardless
  GOLD   = fill highlight only, never text
  INK    = body text, neutral labels
  SLATE  = structural entity chips

Exclusions honored: no STEM OPT eligibility specifics, no H-1B lottery
timing detail, no FICA/tax discussion, no immigration-law advice.

Gate B convention: every zero-width stroke is also zero-opacity.
"""
import sys
import json
import pathlib

# Resolve the shared graphics library wherever this reel lives.
# parents[3] from this file goes up to books/; then into vox/aspects/.../manim.
sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[3]
        / "vox/aspects/explainer/vox-explainer/manim")
)
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)
from vox_graphics import _quote_scene

_bs = pathlib.Path(__file__).with_name("beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ---------------------------------------------------------------- helpers

def _bar(width, height, color, alpha=1.0):
    r = Rectangle(width=width, height=height)
    r.set_fill(color, alpha).set_stroke(width=0, opacity=0)
    return r


def _chip(label, color):
    return LabelChip(label, accent=color, size=20)


# ================================================================ B01 Title

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("Why the 90-Day Clock", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("Is a Gate, Not a Tiebreaker", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ================================================================ B03 TheCliff

class B03_TheCliff(Scene):
    """Horizontal timeline: apply → screen → tech → panel → |AUTH END| → offer (unreachable)"""
    def construct(self):
        total = DUR["B03"]

        # Timeline baseline
        baseline_y = DOWN * 0.2
        tl = Line(LEFT * 5.8 + baseline_y, RIGHT * 5.8 + baseline_y,
                  color=INK, stroke_width=2)

        # Stage labels (dots on the line)
        stages = ["apply", "screen", "tech", "panel", "offer"]
        xs = [-5.0, -2.8, -0.6, 1.6, 4.2]
        dots = VGroup()
        labels = VGroup()
        for name, x in zip(stages, xs):
            d = Dot(radius=0.09, color=INK)
            d.move_to(RIGHT * x + baseline_y)
            dots.add(d)
            lbl = Text(name, font=DISPLAY, color=INK, font_size=16)
            lbl.next_to(d, DOWN, buff=0.22)
            labels.add(lbl)

        # Authorization-end vertical cliff line (CRIMSON)
        cliff_x = 2.9
        cliff_top = baseline_y + UP * 2.0
        cliff_bot = baseline_y + DOWN * 1.2
        cliff = Line(RIGHT * cliff_x + cliff_bot, RIGHT * cliff_x + cliff_top,
                     color=CRIMSON, stroke_width=3)

        cliff_label = Text("auth end", font=DISPLAY, color=CRIMSON, font_size=18, weight=BOLD)
        cliff_label.next_to(cliff, UP, buff=0.18)

        # "offer" dot is past the cliff — mark it unreachable
        offer_cross_a = Line(RIGHT * (xs[-1] - 0.15) + baseline_y + UP * 0.15,
                             RIGHT * (xs[-1] + 0.15) + baseline_y + DOWN * 0.15,
                             color=CRIMSON, stroke_width=2.5)
        offer_cross_b = Line(RIGHT * (xs[-1] + 0.15) + baseline_y + UP * 0.15,
                             RIGHT * (xs[-1] - 0.15) + baseline_y + DOWN * 0.15,
                             color=CRIMSON, stroke_width=2.5)

        unreachable_lbl = SerifLabel("unreachable", CRIMSON, size=20)
        unreachable_lbl.next_to(labels[-1], DOWN, buff=0.15)

        self.play(Create(tl), run_time=0.5)
        self.play(FadeIn(dots), FadeIn(labels), run_time=0.8)
        self.play(Create(cliff), FadeIn(cliff_label), run_time=0.8)
        self.play(Create(offer_cross_a), Create(offer_cross_b),
                  FadeIn(unreachable_lbl), run_time=0.7)
        self.wait(max(0.3, total - 2.8))


# ================================================================ B04 TheQuestion

class B04_TheQuestion(Scene):
    def construct(self):
        total = DUR["B04"]
        line1 = Text("A strong role should close before authorization ends.",
                     font=SERIF, color=INK, font_size=24, weight=BOLD)
        line2 = Text("Here is the case where a perfect role became unreachable",
                     font=SERIF, color=INK, font_size=22)
        line3 = Text("before the first interview.", font=SERIF, color=INK, font_size=22)
        line4 = Text("Why?", font=DISPLAY, color=CRIMSON, font_size=52, weight=BOLD)

        block = VGroup(line1, line2, line3, line4).arrange(DOWN, buff=0.22).move_to(ORIGIN)

        # Gold highlight behind "Why?"
        hl = Rectangle(width=line4.width + 0.3, height=line4.height + 0.14)
        hl.set_fill(GOLD, 0.5).set_stroke(width=0, opacity=0)
        hl.move_to(line4.get_center())

        self.play(FadeIn(line1), run_time=0.7)
        self.play(FadeIn(line2), FadeIn(line3), run_time=0.6)
        self.play(FadeIn(hl), FadeIn(line4, scale=1.05), run_time=0.9)
        self.wait(max(0.3, total - 2.2))


# ================================================================ B05 TheScoringProblem

class B05_TheScoringProblem(Scene):
    """Four score bars all looking strong — the naive expectation."""
    def construct(self):
        total = DUR["B05"]
        baseline = DOWN * 1.9
        max_h = 3.2
        bar_w = 1.2

        factors = [
            ("sponsorship", 0.90, TEAL),
            ("liveness", 0.85, TEAL),
            ("fit", 0.88, TEAL),
            ("quality", 0.91, TEAL),
        ]
        xs = [-4.0, -1.35, 1.3, 3.95]

        bl = Line(LEFT * 5.5 + baseline, RIGHT * 5.5 + baseline,
                  color=INK, stroke_width=1.5)

        bars = VGroup()
        pcts = VGroup()
        chips = VGroup()
        for (name, val, color), x in zip(factors, xs):
            h = max_h * val
            b = _bar(bar_w, h, color)
            b.move_to(baseline + UP * h / 2 + RIGHT * x)
            bars.add(b)

            pct_str = f"{int(val * 100)}%"
            p = Text(pct_str, font=MONO, color=color, font_size=26, weight=BOLD)
            p.next_to(b, UP, buff=0.14)
            pcts.add(p)

            c = _chip(name, SLATE)
            c.next_to(b, DOWN, buff=0.2)
            chips.add(c)

        # Header
        header = SerifLabel("composite: everything says apply", TEAL, size=22)
        header.to_edge(UP, buff=0.5)

        self.play(Create(bl), run_time=0.4)
        self.play(FadeIn(bars, shift=UP * 0.3), run_time=0.9)
        self.play(FadeIn(pcts), FadeIn(chips), run_time=0.7)
        self.play(FadeIn(header), run_time=0.5)
        self.wait(max(0.3, total - 2.5))


# ================================================================ B06 TheHiddenConstraint

class B06_TheHiddenConstraint(Scene):
    """Two-column: what the scorer sees vs what is yours alone."""
    def construct(self):
        total = DUR["B06"]

        lx = LEFT * 2.9
        rx = RIGHT * 2.9
        panel_w, panel_h = 3.4, 3.6

        # Left panel: scorer's view
        lbox = Rectangle(width=panel_w, height=panel_h)
        lbox.set_fill(TEAL, 0.07).set_stroke(TEAL, 1.6)
        lbox.move_to(lx + UP * 0.1)
        lchip = _chip("scorer sees", TEAL)
        lchip.next_to(lbox, UP, buff=0.18)

        l1 = SerifLabel("sponsorship tier", TEAL, size=20)
        l2 = SerifLabel("posting liveness", TEAL, size=20)
        l3 = SerifLabel("fit score", TEAL, size=20)
        l4 = SerifLabel("role quality", TEAL, size=20)
        litems = VGroup(l1, l2, l3, l4).arrange(DOWN, buff=0.28)
        litems.move_to(lx + UP * 0.15)

        # Right panel: yours alone
        rbox = Rectangle(width=panel_w, height=panel_h)
        rbox.set_fill(CRIMSON, 0.07).set_stroke(CRIMSON, 1.6)
        rbox.move_to(rx + UP * 0.1)
        rchip = _chip("invisible to scorer", CRIMSON)
        rchip.next_to(rbox, UP, buff=0.18)

        r1 = SerifLabel("authorization end date", CRIMSON, size=20)
        r2 = SerifLabel("process length vs runway", CRIMSON, size=20)
        ritems = VGroup(r1, r2).arrange(DOWN, buff=0.38)
        ritems.move_to(rx + UP * 0.15)

        self.play(FadeIn(lbox), FadeIn(lchip), run_time=0.6)
        self.play(FadeIn(litems), run_time=0.7)
        self.play(FadeIn(rbox), FadeIn(rchip), run_time=0.6)
        self.play(FadeIn(ritems), run_time=0.7)
        self.wait(max(0.3, total - 2.6))


# ================================================================ B07 ProcessTimeline

class B07_ProcessTimeline(Scene):
    """Horizontal timeline with cumulative process stages, duration labels."""
    def construct(self):
        total = DUR["B07"]

        baseline_y = DOWN * 0.4
        tl = Line(LEFT * 6.0 + baseline_y, RIGHT * 6.0 + baseline_y,
                  color=INK, stroke_width=2)

        stages = [
            ("apply", -5.5),
            ("screen", -3.5),
            ("tech", -1.0),
            ("panel", 1.5),
            ("offer", 4.0),
        ]

        dots = VGroup()
        labels = VGroup()
        for name, x in stages:
            d = Dot(radius=0.10, color=INK)
            d.move_to(RIGHT * x + baseline_y)
            dots.add(d)
            lbl = Text(name, font=DISPLAY, color=INK, font_size=17)
            lbl.next_to(d, DOWN, buff=0.24)
            labels.add(lbl)

        # Duration bracket: "weeks of process" below
        bracket_start = RIGHT * stages[0][1] + baseline_y + DOWN * 0.75
        bracket_end   = RIGHT * stages[-1][1] + baseline_y + DOWN * 0.75
        brace_line = Line(bracket_start, bracket_end, color=INK, stroke_width=1.4)
        dur_lbl = SerifLabel("weeks of calendar time add up", INK, size=21)
        dur_lbl.next_to(brace_line, DOWN, buff=0.2)

        # Header
        header = Text("The hiring process is a pipeline, not a handshake.",
                      font=DISPLAY, color=INK, font_size=19)
        header.to_edge(UP, buff=0.5)

        self.play(FadeIn(header), run_time=0.5)
        self.play(Create(tl), run_time=0.6)
        self.play(
            AnimationGroup(*[FadeIn(d, scale=0.8) for d in dots], lag_ratio=0.18),
            AnimationGroup(*[FadeIn(l) for l in labels], lag_ratio=0.18),
            run_time=1.2
        )
        self.play(Create(brace_line), FadeIn(dur_lbl), run_time=0.8)
        self.wait(max(0.3, total - 3.1))


# ================================================================ B08 TheGateLine

class B08_TheGateLine(Scene):
    """Timeline with bold CRIMSON authorization cliff — offer on the wrong side."""
    def construct(self):
        total = DUR["B08"]

        baseline_y = DOWN * 0.35
        tl = Line(LEFT * 6.0 + baseline_y, RIGHT * 6.0 + baseline_y,
                  color=INK, stroke_width=2)

        stages = [
            ("apply", -5.2),
            ("screen", -3.2),
            ("tech", -0.8),
            ("panel", 1.6),
            ("offer", 4.4),
        ]

        dots = VGroup()
        labels = VGroup()
        for name, x in stages:
            d = Dot(radius=0.10, color=INK)
            d.move_to(RIGHT * x + baseline_y)
            dots.add(d)
            lbl = Text(name, font=DISPLAY, color=INK, font_size=17)
            lbl.next_to(d, DOWN, buff=0.24)
            labels.add(lbl)

        # Authorization cliff
        cliff_x = 2.8
        cliff_top = baseline_y + UP * 2.4
        cliff_bot = baseline_y + DOWN * 1.4
        cliff = Line(RIGHT * cliff_x + cliff_bot, RIGHT * cliff_x + cliff_top,
                     color=CRIMSON, stroke_width=4)
        cliff_label = Text("authorization end", font=DISPLAY, color=CRIMSON,
                           font_size=18, weight=BOLD)
        cliff_label.next_to(RIGHT * cliff_x + cliff_top, UP, buff=0.12)

        # Shade region past cliff = unreachable
        shade = Rectangle(width=6.0 - cliff_x + 0.2, height=4.0)
        shade.set_fill(CRIMSON, 0.07).set_stroke(width=0, opacity=0)
        shade.move_to(RIGHT * (cliff_x + (6.0 - cliff_x) / 2) + baseline_y)

        # "offer" dot cross-out
        ox = stages[-1][1]
        cross_a = Line(RIGHT * (ox - 0.18) + baseline_y + UP * 0.18,
                       RIGHT * (ox + 0.18) + baseline_y + DOWN * 0.18,
                       color=CRIMSON, stroke_width=2.5)
        cross_b = Line(RIGHT * (ox + 0.18) + baseline_y + UP * 0.18,
                       RIGHT * (ox - 0.18) + baseline_y + DOWN * 0.18,
                       color=CRIMSON, stroke_width=2.5)

        unreachable = SerifLabel("unreachable — calendar already ruled it out", CRIMSON, size=20)
        unreachable.next_to(labels[-1], DOWN, buff=0.15)

        self.play(Create(tl), FadeIn(dots), FadeIn(labels), run_time=0.8)
        self.play(Create(cliff), FadeIn(cliff_label), run_time=0.9)
        self.play(FadeIn(shade), run_time=0.5)
        self.play(Create(cross_a), Create(cross_b), FadeIn(unreachable), run_time=0.8)
        self.wait(max(0.3, total - 3.0))


# ================================================================ B09 MultiplierNotAddend

class B09_MultiplierNotAddend(Scene):
    """Show contrast: addend (averages in) vs multiplier (zeroes out)."""
    def construct(self):
        total = DUR["B09"]

        # ---- LEFT: the addend failure mode (dimmed)
        lx = LEFT * 3.2
        wrong_header = Text("if it were an addend...", font=DISPLAY, color=INK,
                            font_size=18)
        wrong_header.move_to(lx + UP * 2.8)

        # stacked bars averaging in
        bar_w = 1.0
        bar_baseline = DOWN * 1.2
        b_spon = _bar(bar_w, 1.5, TEAL, alpha=0.5)
        b_spon.move_to(lx + LEFT * 1.1 + bar_baseline + UP * 0.75)
        b_tl   = _bar(bar_w, 0.0, CRIMSON, alpha=0.5)   # zero height = 0 factor
        b_tl.move_to(lx + RIGHT * 0.1 + bar_baseline + UP * 0.0)

        # composite: still positive (the failure)
        comp_lbl_wrong = Text("composite still > 0", font=DISPLAY,
                              color=INK, font_size=18)
        comp_lbl_wrong.move_to(lx + DOWN * 2.3)
        comp_warn = SerifLabel("wrong — apply on a doomed role", CRIMSON, size=19)
        comp_warn.next_to(comp_lbl_wrong, DOWN, buff=0.18)

        # ---- RIGHT: the multiplier (correct)
        rx = RIGHT * 2.8
        right_header = Text("the gate multiplies", font=DISPLAY, color=CRIMSON,
                            font_size=18, weight=BOLD)
        right_header.move_to(rx + UP * 2.8)

        eq_line1 = Text("composite x timeline factor", font=DISPLAY, color=INK, font_size=22)
        eq_line2 = Text("= any score x 0", font=DISPLAY, color=CRIMSON, font_size=24)
        eq_line3 = Text("= 0", font=MONO, color=CRIMSON, font_size=38, weight=BOLD)
        eq_block = VGroup(eq_line1, eq_line2, eq_line3).arrange(DOWN, buff=0.22)
        eq_block.move_to(rx + DOWN * 0.2)

        # Divider
        divider = Line(ORIGIN + UP * 2.8, ORIGIN + DOWN * 2.8,
                       color=INK, stroke_width=1.2)

        self.play(FadeIn(wrong_header), FadeIn(right_header), Create(divider), run_time=0.7)
        self.play(FadeIn(b_spon), FadeIn(b_tl), FadeIn(comp_lbl_wrong),
                  FadeIn(comp_warn), run_time=0.9)
        self.play(FadeIn(eq_line1), run_time=0.5)
        self.play(FadeIn(eq_line2), run_time=0.5)
        self.play(FadeIn(eq_line3, scale=1.1), run_time=0.6)
        self.wait(max(0.3, total - 3.2))


# ================================================================ B10 TheCostOfWaiting

class B10_TheCostOfWaiting(Scene):
    """Buffer bar with a HandRing showing the consumed chunk."""
    def construct(self):
        total = DUR["B10"]

        # Horizontal buffer bar: total runway = 4 months
        bar_total_w = 9.0
        bar_h = 0.9
        bar_y = ORIGIN

        full_bar = Rectangle(width=bar_total_w, height=bar_h)
        full_bar.set_fill(TEAL, 0.18).set_stroke(INK, 1.4)
        full_bar.move_to(bar_y)

        # Four-month partition marks
        month_w = bar_total_w / 4
        marks = VGroup()
        mark_labels = VGroup()
        for i in range(1, 4):
            mx = full_bar.get_left() + RIGHT * month_w * i
            mk = Line(mx + DOWN * bar_h / 2, mx + UP * bar_h / 2,
                      color=INK, stroke_width=1.0)
            marks.add(mk)
            ml = Text(f"mo {i}", font=MONO, color=INK, font_size=15)
            ml.next_to(mx + UP * bar_h / 2, UP, buff=0.12)
            mark_labels.add(ml)

        # End label
        end_lbl = Text("auth end", font=DISPLAY, color=CRIMSON, font_size=17, weight=BOLD)
        end_lbl.next_to(full_bar.get_right() + UP * bar_h / 2, UP, buff=0.12)

        # "Consumed" block — 4 months chasing Role A
        consumed_bar = Rectangle(width=bar_total_w, height=bar_h)
        consumed_bar.set_fill(CRIMSON, 0.28).set_stroke(width=0, opacity=0)
        consumed_bar.move_to(bar_y)
        ring = HandRing(consumed_bar, color=CRIMSON)

        consumed_lbl = SerifLabel("four months consumed chasing Role A", CRIMSON, size=21)
        consumed_lbl.next_to(full_bar, DOWN, buff=0.48)

        could_have = SerifLabel("buffer needed for reachable roles: gone", CRIMSON, size=21)
        could_have.next_to(consumed_lbl, DOWN, buff=0.22)

        header = Text("A zero-factor role doesn't just waste effort — it steals buffer.",
                      font=DISPLAY, color=INK, font_size=18)
        header.to_edge(UP, buff=0.45)

        self.play(FadeIn(header), run_time=0.5)
        self.play(FadeIn(full_bar), FadeIn(marks), FadeIn(mark_labels),
                  FadeIn(end_lbl), run_time=0.9)
        self.play(FadeIn(consumed_bar), run_time=0.5)
        self.play(Create(ring), run_time=1.0)
        self.play(FadeIn(consumed_lbl), run_time=0.5)
        self.play(FadeIn(could_have), run_time=0.5)
        self.wait(max(0.3, total - 3.9))


# ================================================================ B11 ThreeRoles

class B11_ThreeRoles(Scene):
    """Horizontal bar chart: Role A (CRIMSON, past cliff), Role B (TEAL, safe).
    Authorization cliff line separates reachable from unreachable."""
    def construct(self):
        total = DUR["B11"]

        # Layout: two role bars, horizontal, against a shared timeline x-axis
        lx_origin = LEFT * 5.5
        bar_h = 0.65
        y_a = UP * 1.0
        y_b = DOWN * 0.6

        # x-axis: today -> 6 months (each "month" = 1.5 units)
        month_unit = 1.7
        n_months = 6
        axis_len = month_unit * n_months
        axis_y = DOWN * 1.8

        axis = Line(lx_origin + axis_y,
                    lx_origin + RIGHT * axis_len + axis_y,
                    color=INK, stroke_width=1.5)

        # Month tick marks
        ticks = VGroup()
        tick_labels = VGroup()
        for m in range(n_months + 1):
            tx = lx_origin + RIGHT * month_unit * m + axis_y
            tk = Line(tx, tx + UP * 0.15, color=INK, stroke_width=1.2)
            ticks.add(tk)
            if m > 0:
                tl = Text(f"mo {m}", font=MONO, color=INK, font_size=14)
                tl.next_to(tx + UP * 0.15, UP, buff=0.08)
                tick_labels.add(tl)

        # "today" label
        today_lbl = Text("today", font=MONO, color=INK, font_size=14)
        today_lbl.next_to(lx_origin + axis_y + UP * 0.15, UP, buff=0.08)

        # Auth end: at month 4
        auth_x = lx_origin + RIGHT * month_unit * 4
        cliff = Line(auth_x + DOWN * 1.9 + axis_y,
                     auth_x + UP * 2.8 + axis_y,
                     color=CRIMSON, stroke_width=3.5)
        cliff_lbl = Text("auth end", font=DISPLAY, color=CRIMSON,
                         font_size=17, weight=BOLD)
        cliff_lbl.next_to(auth_x + UP * 2.8 + axis_y, UP, buff=0.1)

        # Buffer dotted line at month 3 (80-day target approx.)
        buf_x = lx_origin + RIGHT * month_unit * 3
        buf_line = DashedLine(buf_x + DOWN * 0.5 + axis_y,
                              buf_x + UP * 2.5 + axis_y,
                              color=INK, stroke_width=1.5, dash_length=0.14)
        buf_lbl = Text("buffer target", font=MONO, color=INK, font_size=13)
        buf_lbl.next_to(buf_x + UP * 2.5 + axis_y, UP, buff=0.08)

        # Role A: 5-month process => past cliff (CRIMSON)
        role_a_len = month_unit * 5
        bar_a = Rectangle(width=role_a_len, height=bar_h)
        bar_a.set_fill(CRIMSON, 0.82).set_stroke(width=0, opacity=0)
        bar_a.move_to(lx_origin + RIGHT * role_a_len / 2 + y_a + axis_y)

        chip_a = _chip("Role A  MegaCorp", CRIMSON)
        chip_a.next_to(bar_a, LEFT, buff=0.22)

        factor_a = Text("factor = 0", font=MONO, color=CRIMSON, font_size=20, weight=BOLD)
        factor_a.next_to(bar_a, RIGHT, buff=0.22)

        # Role B: 6-week process (~1.5 months) => well inside (TEAL)
        role_b_len = month_unit * 1.5
        bar_b = Rectangle(width=role_b_len, height=bar_h)
        bar_b.set_fill(TEAL, 0.82).set_stroke(width=0, opacity=0)
        bar_b.move_to(lx_origin + RIGHT * role_b_len / 2 + y_b + axis_y)

        chip_b = _chip("Role B  startup", TEAL)
        chip_b.next_to(bar_b, LEFT, buff=0.22)

        factor_b = Text("factor ~ 1", font=MONO, color=TEAL, font_size=20, weight=BOLD)
        factor_b.next_to(bar_b, RIGHT, buff=0.22)

        # Illustrative note
        illus = SerifLabel("illustrative numbers", INK, size=18)
        illus.to_edge(DOWN, buff=0.3)

        self.play(Create(axis), FadeIn(ticks), FadeIn(tick_labels),
                  FadeIn(today_lbl), run_time=0.7)
        self.play(Create(cliff), FadeIn(cliff_lbl),
                  Create(buf_line), FadeIn(buf_lbl), run_time=0.8)
        self.play(FadeIn(bar_a), FadeIn(chip_a), run_time=0.7)
        self.play(FadeIn(factor_a), run_time=0.5)
        self.play(FadeIn(bar_b), FadeIn(chip_b), run_time=0.7)
        self.play(FadeIn(factor_b), run_time=0.5)
        self.play(FadeIn(illus), run_time=0.4)
        self.wait(max(0.3, total - 4.3))


# ================================================================ B12 Endcard

class B12_Endcard(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("The gate doesn't vote.", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("It multiplies.", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        sub = Text("from The Reallocation Engine", font=SERIF, color=INK, font_size=20)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 2.0))
