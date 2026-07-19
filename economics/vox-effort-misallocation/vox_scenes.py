"""vox_scenes.py — Effort Optimization Gone Wrong (vox-effort-misallocation, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'. B02 is the only STILL
(ai media slot) and has no scene here. Durations read from beat_sheet.json
(actuals after audio lock; estimates as fallback).

Color law: TEAL = networking / referral / reallocation / high-return channel;
CRIMSON = cold-application / spray-and-pray / visible-but-low-return.
GOLD = editor's pen, fill only, never text, once per graphic.

Exclusions honored: no ghost-job stats, no ATS rates, no 3-3-2 detail.
Gate B: every zero-width stroke is also zero-opacity.
"""
import sys
import json
import os
import pathlib

# Resolve the shared graphics library wherever this reel lives.
# parents[3] from this file goes up to books/; then into vox/aspects/.../manim.
sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[3]
        / "vox/aspects/explainer/vox-explainer/manim")
)
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ---------------------------------------------------------------- B01_Title

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("Effort Optimization Gone Wrong", font=DISPLAY, color=INK, font_size=26, weight=BOLD)
        t2 = Text("Why More Applications Means Less Progress", font=DISPLAY, color=CRIMSON, font_size=20, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL)+DOWN*0.13, t2.get_corner(DR)+DOWN*0.13, color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ---------------------------------------------------------------- B03_TheQuestion

class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]

        # Question header card
        hdr = Text("THE QUESTION", font=DISPLAY, color=INK, font_size=18, weight=BOLD)
        hdr.to_edge(UP, buff=0.55)

        # Left column: spray-and-pray
        lbl_l = Text("SPRAY-AND-PRAY", font=DISPLAY, color=CRIMSON, font_size=16, weight=BOLD)
        row_l1 = Text("200 applications", font=SERIF, color=INK, font_size=22)
        row_l2 = Text("1 recruiter screen", font=SERIF, color=INK, font_size=22)
        row_l3 = Text("0 referrals", font=SERIF, color=CRIMSON, font_size=22, weight=BOLD)
        col_l = VGroup(lbl_l, row_l1, row_l2, row_l3).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        # Right column: reallocation
        lbl_r = Text("REALLOCATION", font=DISPLAY, color=TEAL, font_size=16, weight=BOLD)
        row_r1 = Text("25 applications", font=SERIF, color=INK, font_size=22)
        row_r2 = Text("2 referrals", font=SERIF, color=TEAL, font_size=22, weight=BOLD)
        row_r3 = Text("4 conversations", font=SERIF, color=TEAL, font_size=22, weight=BOLD)
        col_r = VGroup(lbl_r, row_r1, row_r2, row_r3).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        cols = VGroup(col_l, col_r).arrange(RIGHT, buff=2.2, aligned_edge=UP)
        cols.next_to(hdr, DOWN, buff=0.5)

        # Divider
        div = Line(UP * 1.0, DOWN * 1.2, color=INK, stroke_width=1.5)
        div.move_to(cols.get_center())

        # Why label
        why = Text("Why?", font=SERIF, color=INK, font_size=30, slant=ITALIC)
        why.next_to(cols, DOWN, buff=0.45)

        self.play(FadeIn(hdr), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_l), run_time=0.8)
        self.play(FadeIn(col_r), run_time=0.8)
        self.play(FadeIn(why, shift=UP * 0.12), run_time=0.6)
        self.wait(max(0.3, total - 3.1))


# ---------------------------------------------------------------- B04_TheCounter

class B04_TheCounter(Scene):
    def construct(self):
        total = DUR["B04"]

        # Label
        lbl = Text("APPLICATIONS SENT", font=DISPLAY, color=CRIMSON, font_size=18, weight=BOLD)
        lbl.to_edge(UP, buff=0.6)

        # Build up a row of crimson bars representing applications
        bar_group = VGroup()
        bar_w, bar_h = 0.18, 0.28
        cols = 20
        counts = [10, 20, 40, 100, 200]
        # Draw 20x10 grid of small crimson bars
        for row in range(10):
            for col in range(cols):
                b = Rectangle(width=bar_w, height=bar_h)
                b.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
                b.move_to(RIGHT * col * (bar_w + 0.06) + DOWN * row * (bar_h + 0.06))
                bar_group.add(b)
        bar_group.move_to(ORIGIN + DOWN * 0.2)

        # Counter text — starts at 0, will grow
        counter_val = Text("200", font=MONO, color=CRIMSON, font_size=72, weight=BOLD)
        counter_val.next_to(bar_group, RIGHT, buff=0.6)

        # "feels like progress" label
        progress_lbl = SerifLabel("feels like progress", accent=CRIMSON, size=22)
        progress_lbl.next_to(bar_group, DOWN, buff=0.45)

        self.play(FadeIn(lbl), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(b, scale=0.8) for b in bar_group],
                        lag_ratio=0.012, run_time=2.4)
        )
        self.play(FadeIn(counter_val, shift=LEFT * 0.2), run_time=0.8)
        self.play(Write(progress_lbl[0]), Create(progress_lbl[1]), run_time=0.7)
        self.wait(max(0.3, total - 4.3))


# ---------------------------------------------------------------- B05_ConversionBars

class B05_ConversionBars(Scene):
    def construct(self):
        total = DUR["B05"]

        title = SerifLabel("Conversion rate by channel", accent=INK, size=26)
        title.to_edge(UP, buff=0.55)

        # Three bars on zero baseline
        # cold: 0.2%, referral: 3%, network: 7.5% (mid-range)
        scale = 28.0  # multiply percent by this for height
        channels = [
            ("Cold\nApplication", 0.2, CRIMSON),
            ("Employee\nReferral", 3.0, TEAL),
            ("Network\nIntro", 7.5, TEAL),
        ]

        baseline_y = -1.5
        bar_w = 1.6
        positions = [-3.5, 0.0, 3.5]

        bars = VGroup()
        labels = VGroup()
        pct_labels = VGroup()

        for i, (name, pct, color) in enumerate(channels):
            h = max(pct * scale / 100.0, 0.06)
            bar = Rectangle(width=bar_w, height=h)
            bar.set_fill(color, 1).set_stroke(width=0, opacity=0)
            bar.align_to(UP * baseline_y, DOWN)
            bar.shift(RIGHT * positions[i])
            bars.add(bar)

            # Channel name below baseline
            name_txt = Text(name, font=DISPLAY, color=INK, font_size=15,
                            weight=BOLD)
            name_txt.next_to(bar, DOWN, buff=0.15)
            labels.add(name_txt)

            # Percentage above bar
            pct_str = f"{pct}%" if pct >= 1 else f"~{pct}%"
            pct_txt = Text(pct_str, font=MONO, color=color, font_size=20)
            pct_txt.next_to(bar, UP, buff=0.12)
            pct_labels.add(pct_txt)

        # Baseline
        baseline = Line(LEFT * 5.5 + UP * baseline_y, RIGHT * 5.5 + UP * baseline_y,
                        color=INK, stroke_width=2)

        # Order-of-magnitude annotation
        ann = SerifLabel("25-50x gap", accent=TEAL, size=20)
        ann.move_to(RIGHT * 1.8 + UP * 1.8)

        self.play(Write(title[0]), Create(title[1]), run_time=0.6)
        self.play(Create(baseline), run_time=0.4)
        # Grow crimson bar first (tiny)
        self.play(GrowFromEdge(bars[0], DOWN), FadeIn(labels[0]), run_time=0.8)
        self.play(FadeIn(pct_labels[0]), run_time=0.3)
        # Then grow teal bars
        self.play(
            GrowFromEdge(bars[1], DOWN),
            GrowFromEdge(bars[2], DOWN),
            FadeIn(labels[1]),
            FadeIn(labels[2]),
            run_time=1.4
        )
        self.play(FadeIn(pct_labels[1]), FadeIn(pct_labels[2]), run_time=0.4)
        self.play(Write(ann[0]), Create(ann[1]), run_time=0.6)
        self.wait(max(0.3, total - 4.5))


# ---------------------------------------------------------------- B06_EffortMismatch

class B06_EffortMismatch(Scene):
    def construct(self):
        total = DUR["B06"]

        # Header
        hdr = SerifLabel("Where the effort goes vs where the hires come from", accent=INK, size=22)
        hdr.to_edge(UP, buff=0.55)

        # Left: effort column
        effort_lbl = Text("EFFORT", font=DISPLAY, color=CRIMSON, font_size=18, weight=BOLD)
        effort_bar = Rectangle(width=1.8, height=4.0)
        effort_bar.set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
        effort_pct = Text("100%", font=MONO, color=WHITE, font_size=28, weight=BOLD)
        effort_type = Text("Cold Applications", font=DISPLAY, color=INK, font_size=14)
        effort_col = VGroup(effort_lbl, effort_bar)
        effort_col.arrange(DOWN, buff=0.2)
        effort_pct.move_to(effort_bar)
        effort_type.next_to(effort_bar, DOWN, buff=0.15)

        # Right: hires column — split teal (54%+ from connections) vs crimson (rest)
        hires_lbl = Text("HIRES", font=DISPLAY, color=INK, font_size=18, weight=BOLD)
        teal_h = 4.0 * 0.54
        crim_h = 4.0 * 0.46
        teal_bar = Rectangle(width=1.8, height=teal_h)
        teal_bar.set_fill(TEAL, 0.85).set_stroke(width=0, opacity=0)
        crim_bar = Rectangle(width=1.8, height=crim_h)
        crim_bar.set_fill(CRIMSON, 0.45).set_stroke(width=0, opacity=0)
        hire_stack = VGroup(teal_bar, crim_bar).arrange(DOWN, buff=0)
        hires_col = VGroup(hires_lbl, hire_stack)
        hires_col.arrange(DOWN, buff=0.2)
        teal_pct = Text("54%+", font=MONO, color=WHITE, font_size=22, weight=BOLD)
        teal_pct.move_to(teal_bar)
        teal_ann = Text("via connections", font=DISPLAY, color=WHITE, font_size=12)
        teal_ann.next_to(teal_pct, DOWN, buff=0.1)
        crim_pct_lbl = Text("<46%", font=MONO, color=INK, font_size=18)
        crim_pct_lbl.move_to(crim_bar)

        # Layout
        main = VGroup(
            VGroup(effort_col, VGroup(effort_pct, effort_type)),
            VGroup(hires_col, teal_pct, teal_ann, crim_pct_lbl)
        )
        effort_group = VGroup(effort_col, effort_pct, effort_type)
        hires_group = VGroup(hires_col, teal_pct, teal_ann, crim_pct_lbl)
        all_cols = VGroup(effort_group, hires_group).arrange(RIGHT, buff=3.0)
        all_cols.next_to(hdr, DOWN, buff=0.4)

        # Arrow pointing left effort -> cold apps (tiny return)
        arrow_lbl = SerifLabel("all effort here", accent=CRIMSON, size=18)
        arrow_lbl.next_to(effort_bar, LEFT, buff=0.4)

        self.play(Write(hdr[0]), Create(hdr[1]), run_time=0.6)
        self.play(
            FadeIn(effort_lbl),
            GrowFromEdge(effort_bar, DOWN),
            run_time=1.0
        )
        self.play(FadeIn(effort_pct), FadeIn(effort_type), run_time=0.5)
        self.play(
            FadeIn(hires_lbl),
            GrowFromEdge(teal_bar, UP),
            GrowFromEdge(crim_bar, UP),
            run_time=1.2
        )
        self.play(FadeIn(teal_pct), FadeIn(teal_ann), FadeIn(crim_pct_lbl), run_time=0.5)
        self.play(Write(arrow_lbl[0]), Create(arrow_lbl[1]), run_time=0.5)
        self.wait(max(0.3, total - 4.3))


# ---------------------------------------------------------------- B07_FeedbackGap

class B07_FeedbackGap(Scene):
    def construct(self):
        total = DUR["B07"]

        hdr = Text("Feedback vs Return", font=DISPLAY, color=INK, font_size=20, weight=BOLD)
        hdr.to_edge(UP, buff=0.55)

        # Two timelines side by side
        tl_y = 0.3
        tl_len = 5.0

        # Left: cold apps — immediate feedback (counter climbs)
        lbl_l = Text("COLD APPLYING", font=DISPLAY, color=CRIMSON, font_size=15, weight=BOLD)
        line_l = Line(LEFT * tl_len / 2, RIGHT * tl_len / 2, color=CRIMSON, stroke_width=2)

        # Dots rising from timeline (the counter going up)
        dot_xs = [-2.2, -1.5, -0.8, -0.1, 0.6, 1.3]
        dots_l = VGroup(*[
            Dot(radius=0.08, color=CRIMSON).move_to(
                RIGHT * x + UP * (tl_y + 0.05 + i * 0.28)
            )
            for i, x in enumerate(dot_xs)
        ])

        now_lbl = Text("NOW", font=DISPLAY, color=CRIMSON, font_size=13)
        now_lbl.next_to(line_l, DOWN, buff=0.2)

        feedback_lbl = SerifLabel("immediate feedback", accent=CRIMSON, size=17)
        feedback_lbl.next_to(dots_l, RIGHT, buff=0.2)

        left_group = VGroup(lbl_l, line_l, dots_l, now_lbl, feedback_lbl)

        # Right: networking — flat then spike
        lbl_r = Text("NETWORKING", font=DISPLAY, color=TEAL, font_size=15, weight=BOLD)
        line_r = Line(LEFT * tl_len / 2, RIGHT * tl_len / 2, color=TEAL, stroke_width=2)

        # Flat for a while, then spike
        spike_dot = Dot(radius=0.14, color=TEAL)

        later_lbl = Text("DAYS LATER", font=DISPLAY, color=TEAL, font_size=13)
        return_lbl = SerifLabel("delayed return", accent=TEAL, size=17)

        right_group = VGroup(lbl_r, line_r, spike_dot, later_lbl, return_lbl)

        # Position the two groups
        left_group_pos = VGroup(lbl_l, line_l, now_lbl).move_to(LEFT * 3.2 + UP * tl_y)
        lbl_l.next_to(line_l, UP, buff=0.18)
        now_lbl.next_to(line_l.get_end(), DOWN, buff=0.15)
        dots_l.move_to(line_l.get_center() + UP * 0.5)
        feedback_lbl.next_to(line_l, DOWN, buff=0.55)

        line_r.move_to(RIGHT * 3.2 + UP * tl_y)
        lbl_r.next_to(line_r, UP, buff=0.18)
        spike_dot.move_to(line_r.get_end() + UP * 1.1)
        later_lbl.next_to(line_r.get_end(), DOWN, buff=0.15)
        return_lbl.next_to(line_r, DOWN, buff=0.55)

        # Vertical divider
        div = Line(UP * 1.8 + ORIGIN, DOWN * 0.5 + ORIGIN, color=SLATE, stroke_width=1.5)

        # Instinct arrow
        instinct = Text("instinct chooses", font=DISPLAY, color=CRIMSON, font_size=14)
        instinct.next_to(line_l, DOWN, buff=1.1)

        self.play(FadeIn(hdr), run_time=0.4)
        self.play(Create(div), run_time=0.3)
        self.play(
            FadeIn(lbl_l), Create(line_l),
            FadeIn(lbl_r), Create(line_r),
            run_time=0.8
        )
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.7) for d in dots_l],
                        lag_ratio=0.12, run_time=1.4)
        )
        self.play(FadeIn(now_lbl), FadeIn(later_lbl), run_time=0.4)
        self.play(
            Write(feedback_lbl[0]), Create(feedback_lbl[1]),
            run_time=0.5
        )
        # Spike appears on teal timeline
        self.play(FadeIn(spike_dot, scale=0.5), run_time=0.6)
        self.play(Write(return_lbl[0]), Create(return_lbl[1]), run_time=0.5)
        self.play(FadeIn(instinct), run_time=0.5)
        self.wait(max(0.3, total - 5.4))


# ---------------------------------------------------------------- B08_Misallocated

class B08_Misallocated(Scene):
    def construct(self):
        total = DUR["B08"]

        # Two-column layout: optimizing for vs actually gets
        col_hdr_l = Text("OPTIMIZING FOR", font=DISPLAY, color=INK, font_size=18, weight=BOLD)
        col_hdr_r = Text("ACTUALLY GETS", font=DISPLAY, color=INK, font_size=18, weight=BOLD)

        val_l = Text("Application count", font=SERIF, color=CRIMSON, font_size=26)
        val_r = Text("Lowest-return channel", font=SERIF, color=CRIMSON, font_size=26)

        col_l = VGroup(col_hdr_l, val_l).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        col_r = VGroup(col_hdr_r, val_r).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        cols = VGroup(col_l, col_r).arrange(RIGHT, buff=2.5, aligned_edge=UP)
        cols.move_to(UP * 0.4)

        # Rule
        rule = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.5)
        rule.next_to(cols, DOWN, buff=0.5)

        # Result line
        result = Text("Result: mathematically misallocated.", font=SERIF, color=INK, font_size=24,
                      slant=ITALIC)
        result.next_to(rule, DOWN, buff=0.4)

        # Small chips
        chip_l = LabelChip("visible", accent=CRIMSON, size=18)
        chip_l.next_to(val_l, RIGHT, buff=0.25)
        chip_r = LabelChip("lowest return", accent=CRIMSON, size=18)
        chip_r.next_to(val_r, RIGHT, buff=0.25)

        self.play(
            FadeIn(col_hdr_l), FadeIn(col_hdr_r),
            run_time=0.6
        )
        self.play(
            FadeIn(val_l, shift=UP * 0.12),
            FadeIn(val_r, shift=UP * 0.12),
            run_time=0.8
        )
        self.play(FadeIn(chip_l), FadeIn(chip_r), run_time=0.5)
        self.play(Create(rule), run_time=0.4)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.3, total - 3.0))


# ---------------------------------------------------------------- B09_TwoWeeks

class B09_TwoWeeks(Scene):
    def construct(self):
        total = DUR["B09"]

        hdr = Text("Same week. Two strategies.", font=DISPLAY, color=INK, font_size=20, weight=BOLD)
        hdr.to_edge(UP, buff=0.5)

        # Column headers
        hdr_l = Text("SPRAY-AND-PRAY", font=DISPLAY, color=CRIMSON, font_size=16, weight=BOLD)
        hdr_r = Text("REALLOCATION", font=DISPLAY, color=TEAL, font_size=16, weight=BOLD)

        # Rows: metric, left-val, right-val
        rows_data = [
            ("Applications sent",    "200",       "25"),
            ("Recruiter screens",    "1",         "(rolling)"),
            ("Referrals generated",  "0",         "2"),
            ("Conversations",        "0",         "4"),
        ]

        row_groups = VGroup()
        for metric, l_val, r_val in rows_data:
            m = Text(metric, font=SERIF, color=INK, font_size=18)
            lv = Text(l_val, font=MONO, color=CRIMSON, font_size=22, weight=BOLD)
            rv = Text(r_val, font=MONO, color=TEAL, font_size=22, weight=BOLD)
            row_groups.add(VGroup(m, lv, rv))

        # Bottom "winner" rows
        spread_lbl = SerifLabel("Spreadsheet winner", accent=INK, size=18)
        spread_val_l = LabelChip("spray-and-pray", accent=CRIMSON, size=16)
        spread_val_r = Text("--", font=MONO, color=INK, font_size=20)

        move_lbl = SerifLabel("Movement winner", accent=TEAL, size=18)
        move_val_l = Text("--", font=MONO, color=INK, font_size=20)
        move_val_r = LabelChip("reallocation", accent=TEAL, size=16)

        # Layout
        col_l_x = -1.8
        col_r_x = 1.8
        col_m_x = -4.2

        # Position header row
        hdr_l.move_to(RIGHT * col_l_x + UP * 1.8)
        hdr_r.move_to(RIGHT * col_r_x + UP * 1.8)

        # Rule under headers
        rule_top = Line(LEFT * 5.5 + UP * 1.45, RIGHT * 5.5 + UP * 1.45,
                        color=INK, stroke_width=1.5)

        # Position data rows
        start_y = 1.1
        row_height = 0.48
        row_mob_list = []
        for i, (rg, (metric, l_val, r_val)) in enumerate(zip(row_groups, rows_data)):
            y = start_y - i * row_height
            rg[0].move_to(RIGHT * col_m_x + UP * y, aligned_edge=LEFT)
            rg[1].move_to(RIGHT * col_l_x + UP * y)
            rg[2].move_to(RIGHT * col_r_x + UP * y)
            row_mob_list.append(rg)

        # Rule before winner rows
        rule_mid = Line(LEFT * 5.5 + UP * (start_y - 4 * row_height - 0.12),
                        RIGHT * 5.5 + UP * (start_y - 4 * row_height - 0.12),
                        color=INK, stroke_width=1.2)

        # Winner rows
        w_y1 = start_y - 4 * row_height - 0.4
        w_y2 = w_y1 - 0.48

        spread_lbl.move_to(RIGHT * col_m_x + UP * w_y1, aligned_edge=LEFT)
        spread_val_l.move_to(RIGHT * col_l_x + UP * w_y1)
        spread_val_r.move_to(RIGHT * col_r_x + UP * w_y1)

        move_lbl.move_to(RIGHT * col_m_x + UP * w_y2, aligned_edge=LEFT)
        move_val_l.move_to(RIGHT * col_l_x + UP * w_y2)
        move_val_r.move_to(RIGHT * col_r_x + UP * w_y2)

        self.play(FadeIn(hdr), run_time=0.4)
        self.play(FadeIn(hdr_l), FadeIn(hdr_r), run_time=0.5)
        self.play(Create(rule_top), run_time=0.3)

        # Reveal rows one by one
        for rg in row_mob_list:
            self.play(FadeIn(rg[0]), FadeIn(rg[1]), FadeIn(rg[2]), run_time=0.55)

        self.play(Create(rule_mid), run_time=0.3)
        self.play(
            Write(spread_lbl[0]), Create(spread_lbl[1]),
            FadeIn(spread_val_l), FadeIn(spread_val_r),
            run_time=0.7
        )
        self.play(
            Write(move_lbl[0]), Create(move_lbl[1]),
            FadeIn(move_val_l), FadeIn(move_val_r),
            run_time=0.7
        )
        self.wait(max(0.3, total - 7.2))


# ---------------------------------------------------------------- B10_Endcard

class B10_Endcard(Scene):
    def construct(self):
        total = DUR["B10"]

        topic = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        line1 = Text("Spend effort where the return is,", font=SERIF, color=INK,
                     font_size=30, weight=BOLD)
        line2 = Text("not where the feedback is.", font=SERIF, color=INK,
                     font_size=30, weight=BOLD)
        block = VGroup(line1, line2).arrange(DOWN, buff=0.15)
        u = Line(block.get_corner(DL)+DOWN*0.15, block.get_corner(DR)+DOWN*0.15,
                 color=GOLD, stroke_width=2)
        topic.next_to(block, UP, buff=0.5)

        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.1)
        self.wait(max(0.3, total - 1.6))
