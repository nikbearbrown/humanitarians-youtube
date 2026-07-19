"""vox_scenes.py — The Wrong Job: Why the Silent SOC Mismatch Is the Costliest Error
(vox-soc-mismatch, slate cut, 16:9)

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat.
B02 is a STILL · ai beat and has no scene class here.

Color law:
  TEAL   = correct SOC / confirmed match / right wages
  CRIMSON= wrong SOC / silent mismatch / mispriced role
  GOLD   = fill highlight only, never text

Exclusions honored: no OEWS survey methodology, no job zone detail,
no BLS pipeline build instructions — just the confirm/reject check and consequences.
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


def _row_line(label_txt, value_txt, label_color=INK, value_color=INK, size=24):
    """A label + value pair arranged left-right."""
    lbl = Text(label_txt, font=SERIF, color=label_color, font_size=size)
    val = Text(value_txt, font=MONO, color=value_color,
               font_size=int(size * 0.95), weight=BOLD)
    grp = VGroup(lbl, val).arrange(RIGHT, buff=0.4)
    return grp


# ================================================================ B01 Title

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("The Wrong Job", font=DISPLAY, color=INK, font_size=34, weight=BOLD)
        t2 = Text("Why the Silent SOC Mismatch Costs the Most", font=DISPLAY, color=CRIMSON, font_size=20, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ================================================================ B03 TheQuestion

class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        line1 = Text("Mapping a title should attach the right wages.",
                     font=SERIF, color=INK, font_size=26, weight=BOLD)
        line2 = Text("Here is the case where the mapping is wrong",
                     font=SERIF, color=INK, font_size=24)
        line3 = Text("and nothing in the output says so.", font=SERIF, color=INK, font_size=24)
        line4 = Text("Why?", font=DISPLAY, color=CRIMSON, font_size=50, weight=BOLD)
        block = VGroup(line1, line2, line3, line4).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        hl = Rectangle(width=line4.width + 0.3, height=line4.height + 0.15)
        hl.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        hl.move_to(line4.get_center())
        self.play(FadeIn(line1), run_time=0.7)
        self.play(FadeIn(line2), FadeIn(line3), run_time=0.7)
        self.play(FadeIn(hl), FadeIn(line4, scale=1.05), run_time=0.9)
        self.wait(max(0.3, total - 2.3))


# ================================================================ B04 TitleAmbiguity

class B04_TitleAmbiguity(Scene):
    def construct(self):
        total = DUR["B04"]
        lx = LEFT * 3.2
        rx = RIGHT * 3.2
        panel_w, panel_h = 3.4, 3.2

        # Left panel: dashboard Growth Analyst
        lbox = Rectangle(width=panel_w, height=panel_h)
        lbox.set_fill(SLATE, 0.1).set_stroke(SLATE, 1.6)
        lbox.move_to(lx)
        ltitle = LabelChip("Growth Analyst", accent=SLATE, size=20)
        ltitle.next_to(lbox, UP, buff=0.18)
        ldesc1 = Text("builds dashboards", font=SERIF, color=INK, font_size=22)
        ldesc2 = Text("runs reports", font=SERIF, color=INK, font_size=22)
        VGroup(ldesc1, ldesc2).arrange(DOWN, buff=0.28).move_to(lx)

        # Right panel: ML Growth Analyst
        rbox = Rectangle(width=panel_w, height=panel_h)
        rbox.set_fill(SLATE, 0.1).set_stroke(SLATE, 1.6)
        rbox.move_to(rx)
        rtitle = LabelChip("Growth Analyst", accent=SLATE, size=20)
        rtitle.next_to(rbox, UP, buff=0.18)
        rdesc1 = Text("deploys ML models", font=SERIF, color=CRIMSON, font_size=22)
        rdesc2 = Text("product usage data", font=SERIF, color=CRIMSON, font_size=22)
        VGroup(rdesc1, rdesc2).arrange(DOWN, buff=0.28).move_to(rx)

        # divider label
        div = SerifLabel("same title", INK, size=24)
        div.move_to(ORIGIN + UP * 2.2)
        sub = Text("opposite work", font=SERIF, color=CRIMSON, font_size=22)
        sub.next_to(div, DOWN, buff=0.18)

        self.play(FadeIn(lbox), FadeIn(ltitle), FadeIn(rbox), FadeIn(rtitle), run_time=0.8)
        self.play(FadeIn(ldesc1), FadeIn(ldesc2), run_time=0.5)
        self.play(FadeIn(rdesc1), FadeIn(rdesc2), run_time=0.5)
        self.play(FadeIn(div), FadeIn(sub, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.3, total - 2.5))


# ================================================================ B05 SOCIsPivot

class B05_SOCIsPivot(Scene):
    def construct(self):
        total = DUR["B05"]

        # Central pivot marker — LabelChip gives white text on accent box (Gate W safe)
        pivot_chip = LabelChip("SOC code", accent=SLATE, size=26)
        pivot_chip.move_to(ORIGIN)

        # Arrows from title -> SOC -> features (drawn)
        title_chip = LabelChip("job title", accent=SLATE, size=22)
        title_chip.move_to(LEFT * 4.5)

        wages_chip = LabelChip("wages", accent=TEAL, size=22)
        trend_chip = LabelChip("trend", accent=TEAL, size=22)
        wages_chip.move_to(RIGHT * 4.5 + UP * 0.6)
        trend_chip.move_to(RIGHT * 4.5 + DOWN * 0.6)

        arr_in = Arrow(title_chip.get_right() + RIGHT * 0.1,
                       pivot_chip.get_left() + LEFT * 0.1,
                       color=INK, stroke_width=2, buff=0.1)
        arr_wages = Arrow(pivot_chip.get_right() + RIGHT * 0.1,
                          wages_chip.get_left() + LEFT * 0.1,
                          color=TEAL, stroke_width=2, buff=0.1)
        arr_trend = Arrow(pivot_chip.get_right() + RIGHT * 0.1,
                          trend_chip.get_left() + LEFT * 0.1,
                          color=TEAL, stroke_width=2, buff=0.1)

        # "wrong code -> wrong data" annotation
        ann = SerifLabel("wrong code = wrong data, silently", CRIMSON, size=22)
        ann.move_to(DOWN * 2.5)

        self.play(FadeIn(title_chip), run_time=0.4)
        self.play(FadeIn(pivot_chip), GrowArrow(arr_in), run_time=0.8)
        self.play(GrowArrow(arr_wages), FadeIn(wages_chip),
                  GrowArrow(arr_trend), FadeIn(trend_chip), run_time=0.8)
        self.play(FadeIn(ann, shift=UP * 0.2), run_time=0.6)
        self.wait(max(0.3, total - 2.6))


# ================================================================ B06 TheMapping

class B06_TheMapping(Scene):
    def construct(self):
        total = DUR["B06"]

        # Title posting label
        posting = LabelChip("Growth Analyst posting", accent=SLATE, size=22)
        posting.move_to(UP * 3.2 + LEFT * 0.0)

        # Arrow down to proposed SOC box
        arr1 = Arrow(posting.get_bottom() + DOWN * 0.1,
                     posting.get_bottom() + DOWN * 1.2,
                     color=INK, stroke_width=2, buff=0.05)

        # Proposed SOC box (CRIMSON — wrong)
        soc_box = Rectangle(width=5.0, height=1.1)
        soc_box.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 1.8)
        soc_box.move_to(UP * 1.6)
        soc_label = Text("13-1161  Market Research Analysts", font=MONO,
                         color=CRIMSON, font_size=22, weight=BOLD)
        soc_label.move_to(soc_box)

        # Alternate-title list
        alt_header = SerifLabel("alternate-title list:", INK, size=22)
        alt_header.move_to(UP * 0.4 + LEFT * 2.5)
        alt1 = Text("Market Research Analyst", font=SERIF, color=INK, font_size=20)
        alt2 = Text("Consumer Insights Analyst", font=SERIF, color=INK, font_size=20)
        alt3 = Text("Survey Researcher", font=SERIF, color=INK, font_size=20)
        alts = VGroup(alt1, alt2, alt3).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        alts.next_to(alt_header, DOWN, buff=0.2, aligned_edge=LEFT)

        # No match annotation
        no_ml = SerifLabel("no ML   no modeling   no data science", CRIMSON, size=22)
        no_ml.move_to(DOWN * 2.8)

        self.play(FadeIn(posting), run_time=0.5)
        self.play(GrowArrow(arr1), run_time=0.5)
        self.play(FadeIn(soc_box), FadeIn(soc_label), run_time=0.7)
        self.play(FadeIn(alt_header), FadeIn(alts), run_time=0.8)
        self.play(FadeIn(no_ml, shift=UP * 0.2), run_time=0.6)
        self.wait(max(0.3, total - 3.1))


# ================================================================ B07 TheCheck

class B07_TheCheck(Scene):
    def construct(self):
        total = DUR["B07"]

        # Rule statement
        rule1 = Text("The alternate-title list is the only check.",
                     font=SERIF, color=INK, font_size=28, weight=BOLD)
        rule1.move_to(UP * 2.4)

        rule2 = Text("If the posting's work is not there:", font=SERIF,
                     color=INK, font_size=24)
        rule2.next_to(rule1, DOWN, buff=0.4)

        rule3 = Text("the match is unconfirmed.", font=DISPLAY,
                     color=CRIMSON, font_size=30, weight=BOLD)
        rule3.next_to(rule2, DOWN, buff=0.25)

        # Gold highlight behind the key phrase
        hl = Rectangle(width=rule3.width + 0.35, height=rule3.height + 0.16)
        hl.set_fill(GOLD, 0.5).set_stroke(width=0, opacity=0)
        hl.move_to(rule3.get_center())

        # Regardless sub-note
        sub = SerifLabel("regardless of how plausible the code seemed", INK, size=22)
        sub.next_to(rule3, DOWN, buff=0.5)

        # Flow chips at bottom
        chip_prop = LabelChip("model proposes", accent=SLATE, size=22)
        chip_check = LabelChip("data confirms", accent=TEAL, size=22)
        chip_you = LabelChip("you judge", accent=INK, size=22)
        flow = VGroup(chip_prop, chip_check, chip_you).arrange(RIGHT, buff=0.5)
        flow.move_to(DOWN * 2.8)

        self.play(FadeIn(rule1), run_time=0.6)
        self.play(FadeIn(rule2), run_time=0.5)
        self.play(FadeIn(hl), FadeIn(rule3, scale=1.04), run_time=0.8)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(FadeIn(flow), run_time=0.6)
        self.wait(max(0.3, total - 3.0))


# ================================================================ B08 RejectAndRetry

class B08_RejectAndRetry(Scene):
    def construct(self):
        total = DUR["B08"]
        lx = LEFT * 3.2
        rx = RIGHT * 3.2

        # Left panel: REJECTED SOC (CRIMSON)
        lbox = Rectangle(width=3.4, height=3.8)
        lbox.set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.8)
        lbox.move_to(lx)
        lchip = LabelChip("rejected", accent=CRIMSON, size=22)
        lchip.next_to(lbox, UP, buff=0.18)

        lsoc = Text("13-1161", font=MONO, color=CRIMSON, font_size=28, weight=BOLD)
        lsoc_name = Text("Market Research", font=SERIF, color=CRIMSON, font_size=20)
        lsoc_grp = VGroup(lsoc, lsoc_name).arrange(DOWN, buff=0.12)
        lsoc_grp.move_to(lx + UP * 0.7)

        lno = SerifLabel("no ML in alt-titles", CRIMSON, size=20)
        lno.move_to(lx + DOWN * 0.9)

        # Right panel: CONFIRMED SOC (TEAL)
        rbox = Rectangle(width=3.4, height=3.8)
        rbox.set_fill(TEAL, 0.08).set_stroke(TEAL, 1.8)
        rbox.move_to(rx)
        rchip = LabelChip("confirmed", accent=TEAL, size=22)
        rchip.next_to(rbox, UP, buff=0.18)

        rsoc = Text("15-2051", font=MONO, color=TEAL, font_size=28, weight=BOLD)
        rsoc_name = Text("Data Scientists", font=SERIF, color=TEAL, font_size=20)
        rsoc_grp = VGroup(rsoc, rsoc_name).arrange(DOWN, buff=0.12)
        rsoc_grp.move_to(rx + UP * 0.7)

        ralt1 = Text("Machine Learning Engineer", font=SERIF, color=TEAL, font_size=19)
        ralt2 = Text("Predictive Analytics Engineer", font=SERIF, color=TEAL, font_size=19)
        ralt_grp = VGroup(ralt1, ralt2).arrange(DOWN, buff=0.16)
        ralt_grp.move_to(rx + DOWN * 0.9)

        self.play(FadeIn(lbox), FadeIn(lchip), FadeIn(lsoc_grp), FadeIn(lno), run_time=0.8)
        self.play(FadeIn(rbox), FadeIn(rchip), FadeIn(rsoc_grp), run_time=0.8)
        self.play(FadeIn(ralt_grp), run_time=0.6)
        self.wait(max(0.3, total - 2.2))


# ================================================================ B09 TheGap

class B09_TheGap(Scene):
    def construct(self):
        total = DUR["B09"]
        baseline = DOWN * 1.8
        max_h = 3.8
        bar_w = 1.8

        # bar heights proportional to wages (68 and 108, scaled to max_h at 120)
        h_mra = max_h * (68 / 120)
        h_ds  = max_h * (108 / 120)

        lx = LEFT * 2.8
        rx = RIGHT * 2.8

        b_mra = _bar(bar_w, h_mra, CRIMSON)
        b_mra.move_to(baseline + UP * h_mra / 2 + lx)
        b_ds = _bar(bar_w, h_ds, TEAL)
        b_ds.move_to(baseline + UP * h_ds / 2 + rx)

        bl = Line(LEFT * 5.0 + baseline, RIGHT * 5.0 + baseline,
                  color=INK, stroke_width=1.5)

        # wage labels
        w_mra = Text("$68K", font=MONO, color=CRIMSON, font_size=34, weight=BOLD)
        w_mra.next_to(b_mra, UP, buff=0.18)
        w_ds = Text("$108K", font=MONO, color=TEAL, font_size=34, weight=BOLD)
        w_ds.next_to(b_ds, UP, buff=0.18)

        # occupation chips below
        chip_mra = LabelChip("market research analyst", accent=CRIMSON, size=18)
        chip_mra.next_to(b_mra, DOWN, buff=0.22)
        chip_ds = LabelChip("data scientist", accent=TEAL, size=18)
        chip_ds.next_to(b_ds, DOWN, buff=0.22)

        # gap annotation between the two top lines
        top_mra_y = baseline + UP * h_mra
        top_ds_y  = baseline + UP * h_ds
        # vertical gap line on the right edge of the CRIMSON bar
        gap_v = DashedLine(
            lx + RIGHT * bar_w / 2 + top_mra_y,
            lx + RIGHT * bar_w / 2 + top_ds_y,
            color=GOLD, stroke_width=2, dash_length=0.12
        )
        gap_label = SerifLabel("$40K gap", GOLD, size=24)
        gap_label.next_to(gap_v, RIGHT, buff=0.2)
        # gold fill highlight behind gap label
        hl = Rectangle(width=gap_label.width + 0.2, height=gap_label.height + 0.1)
        hl.set_fill(GOLD, 0.4).set_stroke(width=0, opacity=0)
        hl.move_to(gap_label.get_center())

        sub = SerifLabel("the cost of skipping the check  (illustrative)", INK, size=20)
        sub.move_to(DOWN * 3.0)

        self.play(Create(bl), run_time=0.4)
        self.play(FadeIn(b_mra, shift=UP * 0.3), FadeIn(w_mra), FadeIn(chip_mra),
                  run_time=0.8)
        self.play(FadeIn(b_ds, shift=UP * 0.3), FadeIn(w_ds), FadeIn(chip_ds),
                  run_time=0.8)
        self.play(Create(gap_v), FadeIn(hl), FadeIn(gap_label), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(max(0.3, total - 3.2))


# ================================================================ B10 WalkThrough

class B10_WalkThrough(Scene):
    def construct(self):
        total = DUR["B10"]

        # Step-by-step walk: left side is CRIMSON path (wrong), right is TEAL path (correct)
        lx = LEFT * 3.4
        rx = RIGHT * 3.4
        panel_w, panel_h = 3.2, 5.2

        # Posting label at top center
        posting = LabelChip("Growth Analyst — build + deploy ML models", accent=SLATE, size=18)
        posting.move_to(UP * 3.3)

        # Left panel: rejected path
        lbox = Rectangle(width=panel_w, height=panel_h)
        lbox.set_fill(CRIMSON, 0.07).set_stroke(CRIMSON, 1.6)
        lbox.move_to(lx + DOWN * 0.2)
        lchip = LabelChip("wrong path", accent=CRIMSON, size=20)
        lchip.next_to(lbox, UP, buff=0.18)

        l1 = Text("propose: 13-1161", font=MONO, color=CRIMSON, font_size=20, weight=BOLD)
        l2 = SerifLabel("alt-titles: no ML", CRIMSON, size=20)
        l3 = LabelChip("rejected", accent=CRIMSON, size=20)
        l4 = Text("wage: $68K", font=MONO, color=CRIMSON, font_size=22, weight=BOLD)
        lsteps = VGroup(l1, l2, l3, l4).arrange(DOWN, buff=0.28)
        lsteps.move_to(lx + DOWN * 0.2)

        # Right panel: confirmed path
        rbox = Rectangle(width=panel_w, height=panel_h)
        rbox.set_fill(TEAL, 0.07).set_stroke(TEAL, 1.6)
        rbox.move_to(rx + DOWN * 0.2)
        rchip = LabelChip("correct path", accent=TEAL, size=20)
        rchip.next_to(rbox, UP, buff=0.18)

        r1 = Text("propose: 15-2051", font=MONO, color=TEAL, font_size=20, weight=BOLD)
        r2 = SerifLabel("ML Engineer in alt-titles", TEAL, size=20)
        r3 = LabelChip("confirmed", accent=TEAL, size=20)
        r4 = Text("wage: $108K", font=MONO, color=TEAL, font_size=22, weight=BOLD)
        rsteps = VGroup(r1, r2, r3, r4).arrange(DOWN, buff=0.28)
        rsteps.move_to(rx + DOWN * 0.2)

        # illustrative note
        illus = SerifLabel("illustrative — same mechanism", INK, size=19)
        illus.move_to(DOWN * 3.1)

        self.play(FadeIn(posting), run_time=0.5)
        self.play(FadeIn(lbox), FadeIn(lchip), FadeIn(rbox), FadeIn(rchip), run_time=0.7)
        # reveal steps sequentially
        for ls, rs in zip(lsteps, rsteps):
            self.play(FadeIn(ls), FadeIn(rs), run_time=0.55)
        self.play(FadeIn(illus), run_time=0.5)
        self.wait(max(0.3, total - 0.55 * 4 - 2.2))


# ================================================================ B11 Endcard

class B11_Endcard(Scene):
    def construct(self):
        total = DUR["B11"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("The numbers were real.", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("They described the wrong occupation.", font=DISPLAY, color=CRIMSON, font_size=26, weight=BOLD)
        t3 = Text("The only check: the alternate-title list.", font=DISPLAY, color=INK, font_size=24, weight=BOLD)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.20).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        sub = Text("from The Reallocation Engine", font=SERIF, color=INK, font_size=20)
        sub.next_to(block, DOWN, buff=0.45)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.1)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 2.1))
