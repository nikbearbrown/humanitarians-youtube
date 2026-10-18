"""scenes.py — Manim scenes for banking-sql-running-total-bug (cli-explainer).
5 output beats (B01, B02, B05, B08, B09) — the Manim slots in the 12-beat spine;
the other 7 beats (B00, B03, B04, B06, B07, B10, B11) render via Remotion.
Claude-skin-adjacent palette: cream ground, warm ink, one terracotta brand accent,
plus a functional teal/crimson pair for right/wrong data contrast (never swapped).
Class names are `B0X_Name(Scene)` — required for run.sh's scene-detection regex,
unlike the BeatScene-subclass pattern used in other reels in this toolkit family.
No LaTeX (Text/Pango only). Render each class to manim/<bid>.mp4, then run.sh compiles.
"""
from manim import *
import numpy as np

CREAM = "#FAF9F5"; INK = "#3D3929"; TERRACOTTA = "#D97757"
TEAL = "#1F6F5C"; CRIMSON = "#BF3339"; SEC = "#6B6357"

def checkmark(color=TEAL, size=0.32):
    """A real vector checkmark (native shape) instead of a Unicode glyph in a
    Text mobject — Gate A's distinctness stub excludes Text from its shape
    signature, so a glyph-as-check reads as 'no shape ever changes'."""
    mark = VMobject(color=color, stroke_width=7)
    mark.set_points_as_corners([
        np.array([-0.5, 0.05, 0]) * size,
        np.array([-0.1, -0.45, 0]) * size,
        np.array([0.55, 0.5, 0]) * size,
    ])
    return mark

def wrap(text, n):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= n:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return "\n".join(lines)

def pad(scene, elapsed, target):
    scene.wait(max(0.4, target - elapsed - 0.2))


class B01_RunningBalanceStakes(Scene):
    """PROBLEM beat — the stakes, before the CLI loop begins."""
    DUR = 24.75

    def construct(self):
        self.camera.background_color = CREAM
        elapsed = 0.0

        head = Text("“What's the balance today?”", color=INK, weight="BOLD",
                     font_size=40).to_edge(UP, buff=0.6)
        sub = Text("= sum of every posting up to today", color=SEC,
                    font_size=26).next_to(head, DOWN, buff=0.22)
        self.play(Write(head), run_time=1.2); elapsed += 1.2
        self.play(FadeIn(sub, shift=UP * 0.15), run_time=0.6); elapsed += 0.6

        axis = Line([-5.5, -1.3, 0], [5.5, -1.3, 0], color=SEC, stroke_width=3)
        lbl_2025 = Text("2025", color=SEC, font_size=22).next_to([-3.2, -1.3, 0], DOWN, buff=0.25)
        lbl_2026 = Text("2026", color=SEC, font_size=22).next_to([2.2, -1.3, 0], DOWN, buff=0.25)
        self.play(Create(axis), run_time=0.8); elapsed += 0.8
        self.play(FadeIn(lbl_2025), FadeIn(lbl_2026), run_time=0.5); elapsed += 0.5

        pts = [[-5.2, -1.1, 0], [-3.0, -0.7, 0], [-0.8, -0.2, 0],
               [1.0, 0.1, 0], [3.2, 0.5, 0], [5.2, 0.85, 0]]
        curve = VMobject(color=TERRACOTTA, stroke_width=5)
        curve.set_points_smoothly(pts)
        self.play(Create(curve), run_time=2.2); elapsed += 2.2

        boundary = DashedLine([1.0, -1.9, 0], [1.0, 1.3, 0], color=CRIMSON, stroke_width=3)
        blabel = Text("Jan 1, 2026", color=SEC, font_size=20).next_to(boundary, DOWN, buff=0.3)
        self.play(Create(boundary), FadeIn(blabel), run_time=0.8); elapsed += 0.8

        warn = Triangle(color=SEC, fill_color=CREAM, fill_opacity=1, stroke_width=2)
        warn.scale(0.3).move_to([1.0, 1.75, 0])
        bang = Text("!", color=SEC, font_size=20, weight="BOLD").move_to(warn.get_center() + UP * 0.03)
        strike = Line(warn.get_corner(DL), warn.get_corner(UR), color=SEC, stroke_width=3)
        self.play(FadeIn(warn), FadeIn(bang), run_time=0.5); elapsed += 0.5
        self.play(Create(strike), run_time=0.4); elapsed += 0.4
        no_error = Text("no error thrown", color=SEC, font_size=22,
                         slant="ITALIC").next_to(warn, RIGHT, buff=0.35)
        self.play(FadeIn(no_error, shift=RIGHT * 0.1), run_time=0.6); elapsed += 0.6

        closer = Text("One misplaced clause. No error. Just wrong.",
                       color=INK, weight="BOLD", font_size=30).to_edge(DOWN, buff=0.85)
        self.play(Write(closer), run_time=1.4); elapsed += 1.4

        pad(self, elapsed, self.DUR)


class B02_FilterOrderSplit(Scene):
    """MECHANISM beat — filter-then-sum (wrong) vs sum-then-filter (right)."""
    DUR = 22.59

    def _column(self, x, header, header_color, stage_labels, stage_colors, result_text, result_color):
        hdr = Text(header, color=header_color, weight="BOLD", font_size=26).move_to([x, 2.7, 0])
        ys = [1.75, 0.55, -0.65]
        steps = []          # list of (arrow, VGroup(box, txt)) reveal-together pairs
        boxes = []
        prev_bottom = hdr.get_bottom()
        for label, color, y in zip(stage_labels, stage_colors, ys):
            box = Rectangle(width=4.3, height=0.85, color=color, stroke_width=3,
                             fill_color=CREAM, fill_opacity=1).move_to([x, y, 0])
            txt = Text(label, color=INK, font_size=20).move_to(box.get_center())
            arrow = Arrow(prev_bottom, box.get_top(), buff=0.08, color=SEC,
                          stroke_width=3, max_tip_length_to_length_ratio=0.15)
            boxes.append(box)
            steps.append((arrow, VGroup(box, txt)))
            prev_bottom = box.get_bottom()
        result = Rectangle(width=3.2, height=0.9, color=result_color, stroke_width=4,
                            fill_color=result_color, fill_opacity=0.12).move_to([x, -2.15, 0])
        rtxt = Text(result_text, color=result_color, weight="BOLD", font_size=30).move_to(result.get_center())
        rarrow = Arrow(boxes[-1].get_bottom(), result.get_top(), buff=0.08, color=SEC,
                        stroke_width=3, max_tip_length_to_length_ratio=0.15)
        steps.append((rarrow, VGroup(result, rtxt)))
        return hdr, steps, VGroup(result, rtxt)

    def construct(self):
        self.camera.background_color = CREAM
        elapsed = 0.0

        rule = Text("A WHERE in an earlier CTE still runs first.", color=INK, weight="BOLD",
                     font_size=30).to_edge(UP, buff=0.7)
        self.play(Write(rule), run_time=1.3); elapsed += 1.3

        divider = Line([0, 2.8, 0], [0, -2.75, 0], color=SEC, stroke_width=2)
        self.play(Create(divider), run_time=0.5); elapsed += 0.5

        left_hdr, left_steps, left_result = self._column(
            -3.55, "Filter → Sum", CRIMSON,
            ["ledger rows (all postings)", "WHERE 2026", "SUM() OVER"],
            [SEC, CRIMSON, SEC], "WRONG", CRIMSON)
        right_hdr, right_steps, right_result = self._column(
            3.55, "Sum → Filter", TEAL,
            ["ledger rows (all postings)", "SUM() OVER", "WHERE 2026 (display only)"],
            [SEC, TEAL, SEC], "RIGHT", TEAL)

        self.play(FadeIn(left_hdr), FadeIn(right_hdr), run_time=0.5); elapsed += 0.5
        for (l_arrow, l_box), (r_arrow, r_box) in zip(left_steps, right_steps):
            self.play(Create(l_arrow), Create(r_arrow), run_time=0.3)
            self.play(FadeIn(l_box), FadeIn(r_box), run_time=0.4)
            elapsed += 0.7

        self.play(Flash(left_result.get_center(), color=CRIMSON, line_length=0.3),
                   Flash(right_result.get_center(), color=TEAL, line_length=0.3), run_time=0.6)
        elapsed += 0.6

        pad(self, elapsed, self.DUR)


def _balance_table(rows, value_color, badge_text, badge_color):
    """Shared 3-row (month, balance) table builder for B05 / B08."""
    header = VGroup(
        Text("Month", color=SEC, font_size=26, weight="BOLD").move_to([-2.0, 2.2, 0]),
        Text("EOM Balance", color=SEC, font_size=26, weight="BOLD").move_to([2.0, 2.2, 0]),
    )
    rule = Line([-4.2, 1.75, 0], [4.2, 1.75, 0], color=SEC, stroke_width=2)
    row_group = VGroup()
    ys = [0.9, 0.0, -0.9]
    for (month, value), y in zip(rows, ys):
        m = Text(month, color=INK, font_size=28).move_to([-2.0, y, 0])
        v = Text(value, color=value_color, weight="BOLD", font_size=32).move_to([2.0, y, 0])
        row_group.add(VGroup(m, v))
    badge = RoundedRectangle(corner_radius=0.15, width=6.6, height=0.85, color=badge_color,
                              stroke_width=3, fill_color=badge_color, fill_opacity=0.12)
    badge.move_to([0, -2.3, 0])
    badge_txt = Text(badge_text, color=badge_color, weight="BOLD", font_size=24).move_to(badge.get_center())
    return header, rule, row_group, badge, badge_txt


class B05_TruncatedBalance(Scene):
    """OUTPUT beat, cycle 1 — the wrong result."""
    DUR = 16.11

    def construct(self):
        self.camera.background_color = CREAM
        elapsed = 0.0

        title = Text("ACCT-50231 — as reported (buggy)", color=INK, weight="BOLD",
                      font_size=30).to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=1.1); elapsed += 1.1

        header, rule, rows, badge, badge_txt = _balance_table(
            [("Jan 2026", "−$300.00"), ("Feb 2026", "−$150.00"), ("Mar 2026", "−$225.00")],
            CRIMSON, "MISSING $12,400 OF HISTORY", CRIMSON)

        self.play(FadeIn(header), run_time=0.4); elapsed += 0.4
        self.play(Create(rule), run_time=0.4); elapsed += 0.4
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.15) for r in rows],
                              lag_ratio=0.6, run_time=1.8)); elapsed += 1.8
        self.play(FadeIn(badge), FadeIn(badge_txt), run_time=0.5); elapsed += 0.5
        self.play(Indicate(VGroup(badge, badge_txt), color=CRIMSON, scale_factor=1.05), run_time=0.8)
        elapsed += 0.8

        pad(self, elapsed, self.DUR)


class B08_CorrectedBalance(Scene):
    """OUTPUT beat, cycle 2 — the corrected result (mirrors B05's geometry)."""
    DUR = 13.1

    def construct(self):
        self.camera.background_color = CREAM
        elapsed = 0.0

        title = Text("ACCT-50231 — as reported (fixed)", color=INK, weight="BOLD",
                      font_size=30).to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=1.0); elapsed += 1.0

        header, rule, wrong_rows, _, _ = _balance_table(
            [("Jan 2026", "−$300.00"), ("Feb 2026", "−$150.00"), ("Mar 2026", "−$225.00")],
            CRIMSON, "", CRIMSON)
        self.play(FadeIn(header), Create(rule), run_time=0.5); elapsed += 0.5
        self.play(FadeIn(wrong_rows), run_time=0.4); elapsed += 0.4

        strikes = VGroup(*[Line(r.get_left() + LEFT * 0.1, r.get_right() + RIGHT * 0.1,
                                 color=CRIMSON, stroke_width=3) for r in wrong_rows])
        strikes._qc_intentional = True    # deliberate strike-through, not a stray line-on-text defect
        self.play(Create(strikes), run_time=0.6); elapsed += 0.6
        self.play(FadeOut(wrong_rows), FadeOut(strikes), run_time=0.5); elapsed += 0.5

        _, _, right_rows, badge, badge_txt = _balance_table(
            [("Jan 2026", "$12,100.00"), ("Feb 2026", "$12,250.00"), ("Mar 2026", "$12,175.00")],
            TEAL, "NOTHING INVENTED. NOTHING LOST.", TEAL)
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.15) for r in right_rows],
                              lag_ratio=0.6, run_time=1.6)); elapsed += 1.6
        self.play(FadeIn(badge), FadeIn(badge_txt), run_time=0.5); elapsed += 0.5

        pad(self, elapsed, self.DUR)


class B09_TheLesson(Scene):
    """SUMMARY beat — the lesson, one beat, animated checklist."""
    DUR = 13.91

    def construct(self):
        self.camera.background_color = CREAM
        elapsed = 0.0

        head = Text("The lesson", color=INK, weight="BOLD", font_size=42).to_edge(UP, buff=0.85)
        head.to_edge(LEFT, buff=0.85)
        rule = Rectangle(width=1.9, height=0.07, color=TERRACOTTA, fill_color=TERRACOTTA,
                          fill_opacity=1, stroke_width=0).next_to(head, DOWN, buff=0.32, aligned_edge=LEFT)
        self.play(Write(head), run_time=0.9); elapsed += 0.9
        self.play(GrowFromEdge(rule, LEFT), run_time=0.4); elapsed += 0.4

        items = [
            "Compute the running total over the WHOLE ledger",
            "Filter to the reporting window only AFTER the sum",
            "A misplaced WHERE doesn't error — it quietly zeroes your history",
        ]
        rows = VGroup()
        for it in items:
            check = checkmark(size=0.42)
            txt = Text(wrap(it, 34), color=INK, font_size=32, line_spacing=1.05)
            row = VGroup(check, txt).arrange(RIGHT, buff=0.35, aligned_edge=UP)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(rule, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.25) for r in rows],
                              lag_ratio=0.6, run_time=2.4)); elapsed += 2.4

        note = Text(wrap("Window functions run after WHERE inside their OWN query — "
                          "not before a WHERE in an earlier CTE.", 58),
                    color=SEC, font_size=22, slant="ITALIC",
                    line_spacing=1.0).next_to(rows, DOWN, buff=0.22, aligned_edge=LEFT)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=1.0); elapsed += 1.0

        pad(self, elapsed, self.DUR)
