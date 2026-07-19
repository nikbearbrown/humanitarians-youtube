import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
PASS_CLR="#2A7A2A"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_SolveVerify(Scene):
    def construct(self):
        def lbl_bg(txt, pos, fontsize=20, color=INK, bw=None, bh=0.36):
            t = Text(txt, font_size=fontsize, color=color)
            t.move_to(pos)
            w = bw if bw else max(t.width + 0.2, 0.4)
            bg = Rectangle(
                width=w, height=bh,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            ).move_to(pos)
            return VGroup(bg, t)

        # ---- Title ----
        title = Text(
            "The Solve-Verify Gap: Speed Widens the Asymmetry",
            font_size=27, color=INK, weight=BOLD
        ).move_to((0, 3.2, 0))

        # ---- X-axis (hours) ----
        X_START = -4.5
        HOUR_UNIT = 0.75
        axis_y = -2.5
        x_axis = Line(
            (X_START - 0.1, axis_y, 0),
            (X_START + 4 * HOUR_UNIT + 0.2, axis_y, 0),
            color=SLATE, stroke_width=2
        )
        tick_marks = VGroup()
        tick_labels_grp = VGroup()
        for i, lbl in enumerate(["0", "1h", "2h", "3h", "4h"]):
            tx = X_START + i * HOUR_UNIT
            tick = Line((tx, axis_y - 0.1, 0), (tx, axis_y + 0.1, 0),
                        color=SLATE, stroke_width=1.5)
            tick_marks.add(tick)
            tl = lbl_bg(lbl, (tx, axis_y - 0.35, 0), fontsize=17, color=SLATE, bh=0.30)
            tick_labels_grp.add(tl)
        axis_group = VGroup(x_axis, tick_marks, tick_labels_grp)

        # ---- Domain data ----
        # (domain, verify_units, fail_pct, ratio_label, produce_label)
        DOMAINS = [
            ("LEGAL",   1.5,  40, "72000x", "~0s"),
            ("MEDICAL", 3.0,  25, "7200x",  "~2s"),
            ("FINANCE", 2.25, 30, "10800x", "~1s"),
        ]
        GROUP_Y = [1.5, 0.0, -1.5]
        BAR_H = 0.35
        PRODUCE_W = 0.10
        # Failure rate bar label placed to the RIGHT of the chart area (x=2.0+)
        FAIL_LABEL_X = 1.8

        domain_groups = []
        for (dom, verify_u, fail_pct, ratio, prod_lbl), gy in zip(DOMAINS, GROUP_Y):
            # Domain label
            dom_lbl = lbl_bg(dom, (-5.05, gy, 0), fontsize=22, color=INK, bw=1.3, bh=0.40)

            # Produce bar (tiny teal)
            prod_bar = Rectangle(
                width=PRODUCE_W, height=BAR_H,
                fill_color=PASS_CLR, fill_opacity=0.9,
                stroke_width=0, stroke_opacity=0
            ).move_to((X_START + PRODUCE_W / 2, gy, 0))

            # Verify bar (crimson)
            verify_x_start = X_START + PRODUCE_W + 0.15
            verify_center = verify_x_start + verify_u / 2
            verify_bar = Rectangle(
                width=verify_u, height=BAR_H,
                fill_color=CRIMSON, fill_opacity=0.85,
                stroke_width=0, stroke_opacity=0
            ).move_to((verify_center, gy, 0))
            verify_end_x = verify_x_start + verify_u

            # Ratio label — right of verify bar, in safe zone
            ratio_lbl = lbl_bg(ratio, (verify_end_x + 0.55, gy, 0),
                               fontsize=21, color=CRIMSON, bw=1.1, bh=0.34)

            # Produce header
            prod_hdr = lbl_bg("PRODUCE", (X_START + PRODUCE_W / 2, gy + 0.42, 0),
                              fontsize=14, color=PASS_CLR, bh=0.26)
            # Verify header
            verify_hdr = lbl_bg("VERIFY", (verify_center, gy + 0.42, 0),
                                fontsize=14, color=CRIMSON, bh=0.26)

            # Failure rate bar (below, at gy - 0.52)
            fail_w = fail_pct / 100.0 * 2.5
            fail_bar = Rectangle(
                width=fail_w, height=0.20,
                fill_color=GOLD, fill_opacity=1,
                stroke_color=SLATE, stroke_width=1,
                stroke_opacity=0.7
            ).move_to((X_START + fail_w / 2, gy - 0.52, 0))

            # Failure rate label at fixed right position (away from bar charts)
            fail_lbl = lbl_bg(
                f"{fail_pct}% fail if skipped",
                (FAIL_LABEL_X, gy - 0.52, 0),
                fontsize=17, color=SLATE, bh=0.28
            )

            grp = VGroup(
                dom_lbl,
                prod_hdr, prod_bar,
                verify_hdr, verify_bar, ratio_lbl,
                fail_bar, fail_lbl
            )
            domain_groups.append(grp)

        # ---- Bonus annotation ----
        bonus_bg = Rectangle(
            width=9.5, height=0.36,
            fill_color=CREAM, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, -3.1, 0))
        bonus_t = Text(
            "Exception: code with test suite — verify < produce (proves the rule)",
            font_size=19, color=SLATE
        ).move_to((0, -3.1, 0))
        bonus = VGroup(bonus_bg, bonus_t)

        # ---- Animate (7 play calls) ----
        self.play(Write(title))
        self.play(Create(axis_group))
        self.play(FadeIn(domain_groups[0]))
        self.play(FadeIn(domain_groups[1]))
        self.play(FadeIn(domain_groups[2]))
        self.play(FadeIn(bonus))
        self.wait(1)
