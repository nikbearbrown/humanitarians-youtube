"""
Manim scenes for patent-agent-video11-classifier-eval-harness
B01_EvalHarness              — labeled claims in, accuracy / kappa / baseline / collapse out
B02_OneQueryNotSixteen       — unpartitioned table: 1 patent ~ 160 patents in scan cost
B03_IndependentClaimFinding  — 147 of 160 patents have 1-3 independent claims
B04_WhatsNotDoneYet          — labeling paused for lead review, no accuracy number yet

Every number on screen is from this session's real runs:
  dry runs 127.6 GB ($0.73) single patent, 161.8 GB ($0.92) pool
  (decimal GB, to match the narration; = 118.9 / 150.7 GiB);
  pool distribution 57 / 46 / 44 / 8 / 5; mock "always narrow/defensive"
  run gave kappa 0.00 on both dimensions with both collapse warnings.
"""
from manim import *

PALETTE = {
    "bg":     "#F3EBDD",
    "ink":    "#2F2A26",
    "teal":   "#1F4E5F",
    "crimson": "#E4572E",
    "slate":  "#29335C",
    "gold":   "#F3A712",
    "sage":   "#A8C686",
}

BODY_FONT = "Menlo"


def make_title(line1, line2, font_size=22):
    t1 = Text(line1, color=PALETTE["ink"], font_size=font_size, font=BODY_FONT)
    if line2:
        t2 = Text(line2, color=PALETTE["ink"], font_size=font_size, font=BODY_FONT)
        title = VGroup(t1, t2).arrange(DOWN, buff=0.15)
    else:
        title = VGroup(t1)
    title.to_edge(UP, buff=0.7)
    title.move_to([0, title.get_y(), 0])
    return title


def card(text, color, width, height=0.8, font_size=15, text_color=None):
    box = RoundedRectangle(
        corner_radius=0.1, width=width, height=height,
        fill_color=PALETTE[color], fill_opacity=0.08,
        stroke_color=PALETTE[color], stroke_width=1.5
    )
    label = Text(text, color=PALETTE[text_color or color], font_size=font_size,
                 font=BODY_FONT, line_spacing=1.2).move_to(box.get_center())
    return VGroup(box, label)


class B01_EvalHarness(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Evaluation", "Harness")
        self.add(title)

        # State 1 — the pipeline: labeled claims -> classifier -> compare
        steps = VGroup(
            card("labeled\nclaims", "slate", 2.2, 1.0),
            card("classifier", "teal", 2.2, 1.0),
            card("compare\nwith labels", "slate", 2.2, 1.0),
        ).arrange(RIGHT, buff=0.7).move_to([0, 1.0, 0])
        arrows = VGroup(
            Arrow(steps[0].get_right(), steps[1].get_left(), buff=0.1, color=PALETTE["ink"], stroke_width=2),
            Arrow(steps[1].get_right(), steps[2].get_left(), buff=0.1, color=PALETTE["ink"], stroke_width=2),
        )
        for i, s in enumerate(steps):
            self.play(Create(s[0]), Write(s[1]), run_time=0.8)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.4)
        self.wait(3.9)

        # State 2 — accuracy alone isn't enough: four measurements
        metrics = VGroup(
            card("accuracy", "teal", 3.6, 0.75),
            card("Cohen's kappa", "teal", 3.6, 0.75),
            card("majority baseline", "teal", 3.6, 0.75),
            card("collapse check (>= 80%)", "crimson", 3.6, 0.75, font_size=14),
        ).arrange_in_grid(rows=2, cols=2, buff=(0.4, 0.3)).move_to([0, -1.1, 0])
        for m in metrics:
            self.play(Create(m[0]), Write(m[1]), run_time=0.7)
            self.wait(2.1)
        self.wait(1.9)

        # State 3 — what kappa means
        self.play(FadeOut(steps), FadeOut(arrows), run_time=0.6)
        self.play(metrics.animate.move_to([0, 1.0, 0]), run_time=0.8)
        self.play(Indicate(metrics[1], color=PALETTE["gold"]), run_time=1.0)
        kappa_note = card("kappa = agreement beyond chance\nsame answer every time  ->  kappa = 0",
                          "gold", 7.6, 1.2, font_size=15, text_color="ink").move_to([0, -1.0, 0])
        self.play(Create(kappa_note[0]), Write(kappa_note[1]), run_time=1.2)
        self.wait(8.4)

        # State 4 — the offline test with a fake "always narrow/defensive" classifier
        self.play(FadeOut(metrics), FadeOut(kappa_note), run_time=0.6)
        mock = card("fake classifier: always narrow / defensive", "slate", 7.6, 0.8,
                    font_size=15).move_to([0, 1.1, 0])
        self.play(Create(mock[0]), Write(mock[1]), run_time=1.0)
        self.wait(1.2)
        results = VGroup(
            card("breadth   kappa 0.00   collapse warning", "crimson", 7.6, 0.75, font_size=15),
            card("posture   kappa 0.00   collapse warning", "crimson", 7.6, 0.75, font_size=15),
        ).arrange(DOWN, buff=0.25).move_to([0, -0.5, 0])
        for r in results:
            self.play(Create(r[0]), Write(r[1]), run_time=0.9)
            self.wait(1.2)

        bottom = Text(
            "tested offline: no API calls, no cost",
            color=PALETTE["slate"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.0)
        self.wait(1.0)


class B02_OneQueryNotSixteen(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("One Query,", "Not Sixteen")
        self.add(title)

        # State 1 — why: billed per column scanned, not per row returned
        why = card("table is not partitioned\nbilled per column scanned, not per row",
                   "slate", 7.6, 1.2, font_size=15).move_to([0, 1.2, 0])
        self.play(Create(why[0]), Write(why[1]), run_time=1.2)
        self.wait(7.6)

        # State 2 — real dry-run sizes as proportional bars
        max_w = 6.0
        rows = VGroup()
        for label, gb, cost, color in [
            ("1 patent", 127.6, "$0.73", "teal"),
            ("160 patents", 161.8, "$0.92", "gold"),
        ]:
            name = Text(label, color=PALETTE["ink"], font_size=15, font=BODY_FONT)
            bar = Rectangle(width=max_w * gb / 161.8, height=0.5,
                            fill_color=PALETTE[color], fill_opacity=0.7,
                            stroke_color=PALETTE[color], stroke_width=1)
            value = Text(f"{gb} GB  {cost}", color=PALETTE["ink"], font_size=14, font=BODY_FONT)
            rows.add(VGroup(name, bar, value))
        for row in rows:
            row[0].move_to([-4.6, 0, 0])
            row[1].move_to([-3.3 + row[1].width / 2, 0, 0])
        for row in rows:
            row[2].next_to(row[1], RIGHT, buff=0.25)
        rows[0].shift(DOWN * 0.3)
        rows[1].shift(DOWN * 1.1)
        for row in rows:
            self.play(Write(row[0]), GrowFromEdge(row[1], LEFT), run_time=1.0)
            self.play(Write(row[2]), run_time=0.6)
            self.wait(1.2)
        self.wait(0.7)

        # State 3 — the flow: one query, 160 candidates, picked locally for free
        self.play(FadeOut(why), FadeOut(rows), run_time=0.6)
        flow = VGroup(
            card("1 query", "teal", 2.0, 0.9),
            card("160\ncandidates", "teal", 2.0, 0.9, font_size=14),
            card("pick locally\n(free)", "sage", 2.0, 0.9, font_size=14, text_color="teal"),
            card("16\npatents", "slate", 2.0, 0.9, font_size=14),
        ).arrange(RIGHT, buff=0.35).move_to([0, 0.6, 0])
        for i, f in enumerate(flow):
            self.play(Create(f[0]), Write(f[1]), run_time=0.8)
            self.wait(2.2)
        self.wait(1.8)

        # State 4 — dry run first, then the real scan
        check = VGroup(
            card("dry run (free): 161.8 GB predicted", "sage", 7.0, 0.7, font_size=14, text_color="teal"),
            card("real query:     161.8 GB billed", "gold", 7.0, 0.7, font_size=14, text_color="ink"),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.3, 0])
        for c in check:
            self.play(Create(c[0]), Write(c[1]), run_time=0.8)
            self.wait(2.25)

        bottom = Text(
            "~$0.92 at list price, one query",
            color=PALETTE["slate"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.0)
        self.wait(1.0)


class B03_IndependentClaimFinding(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Most Patents Have", "1-3 Independent Claims")
        self.add(title)

        # State 1 — the assumption
        plan = card("plan assumed ~5 independent claims per patent\n50 claims from 8-10 patents",
                    "crimson", 8.0, 1.2, font_size=15).move_to([0, 1.2, 0])
        self.play(Create(plan[0]), Write(plan[1]), run_time=1.2)
        self.wait(4.7)

        # State 2 — the real distribution across 160 candidate patents
        self.play(FadeOut(plan), run_time=0.6)
        counts = [("1", 57), ("2", 46), ("3", 44), ("4", 8), ("5+", 5)]
        base_y, max_h, bar_w, gap = -2.0, 3.0, 0.9, 0.45
        x0 = -(len(counts) * bar_w + (len(counts) - 1) * gap) / 2 + bar_w / 2
        bars, labels = VGroup(), VGroup()
        for i, (k, n) in enumerate(counts):
            color = PALETTE["teal"] if i < 3 else PALETTE["crimson"]
            h = max(max_h * n / 57, 0.08)
            x = x0 + i * (bar_w + gap) - 1.6
            bar = Rectangle(width=bar_w, height=h, fill_color=color, fill_opacity=0.75,
                            stroke_color=color, stroke_width=1).move_to([x, base_y + h / 2, 0])
            num = Text(str(n), color=PALETTE["ink"], font_size=14, font=BODY_FONT).next_to(bar, UP, buff=0.1)
            tick = Text(k, color=PALETTE["ink"], font_size=14, font=BODY_FONT).move_to([x, base_y - 0.3, 0])
            bars.add(bar)
            labels.add(VGroup(num, tick))
        axis_note = Text("independent claims per patent", color=PALETTE["ink"],
                         font_size=13, font=BODY_FONT).move_to([-1.6, base_y - 0.7, 0])
        self.play(Write(axis_note), run_time=0.6)
        for bar, lab in zip(bars, labels):
            self.play(GrowFromEdge(bar, DOWN), Write(lab), run_time=0.6)
        self.wait(1.5)

        tally = VGroup(
            card("147 of 160\nhave 1-3", "teal", 2.6, 1.0, font_size=15),
            card("13 of 160\nhave 4+", "crimson", 2.6, 1.0, font_size=15),
        ).arrange(DOWN, buff=0.3).move_to([4.2, -0.6, 0])
        for t in tally:
            self.play(Create(t[0]), Write(t[1]), run_time=0.8)
            self.wait(2.0)
        self.wait(4.7)

        # State 3 — how the 16 patents were picked
        self.play(FadeOut(bars), FadeOut(labels), FadeOut(axis_note), FadeOut(tally), run_time=0.6)
        rules = VGroup(
            card("US grants, 2020-2024", "slate", 7.6, 0.6, font_size=14),
            card("20 per CPC section, picked by hash, not by hand", "slate", 7.6, 0.6, font_size=14),
            card("skip patents with fewer than 3 independent", "slate", 7.6, 0.6, font_size=14),
            card("2 patents per section, at most 4 claims each", "slate", 7.6, 0.6, font_size=14),
        ).arrange(DOWN, buff=0.18).move_to([0, 0.4, 0])
        for r in rules:
            self.play(Create(r[0]), Write(r[1]), run_time=0.8)
            self.wait(3.6)

        result = card("50 claims  ·  16 patents  ·  all 8 CPC sections", "sage", 7.6, 0.75,
                      font_size=15, text_color="teal").move_to([0, -1.9, 0])
        self.play(Create(result[0]), Write(result[1]), run_time=1.0)
        self.play(Indicate(result, color=PALETTE["gold"]), run_time=1.0)
        self.wait(1.0)


class B04_WhatsNotDoneYet(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("What's", "Not Done Yet")
        self.add(title)

        rows = VGroup(
            card("harness          built, tested offline", "sage", 7.6, 0.7, text_color="teal"),
            card("50 claims        pulled, real data", "sage", 7.6, 0.7, text_color="teal"),
            card("hand labeling    paused for lead review", "gold", 7.6, 0.7, text_color="ink"),
            card("accuracy number  not measured yet", "crimson", 7.6, 0.7),
        ).arrange(DOWN, buff=0.22).move_to([0, 0.4, 0])
        for r in rows:
            self.play(Create(r[0]), Write(r[1]), run_time=0.8)
            self.wait(2.2)

        self.play(Indicate(rows[2], color=PALETTE["gold"]), run_time=1.0)
        self.wait(3.4)

        bottom = Text(
            "stuck on narrow / defensive? still an open question",
            color=PALETTE["slate"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.0)
