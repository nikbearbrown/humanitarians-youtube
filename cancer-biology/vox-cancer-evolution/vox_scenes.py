"""vox_scenes.py — Why Cancer Is Evolution Running Inside the Body
(vox-cancer-evolution, slate cut, 16:9).

One Scene per GRAPHIC / CARD beat whose source is own.
B02 is the only STILL (ai media slot) — no scene here.
Durations read from beat_sheet.json (actuals after audio lock; estimates as fallback).

Color law: TEAL = winning / selected clone (the expanding lineage)
           CRIMSON = mutation / selection event (the driver)
           GOLD = editor's pen (fill only, at most once per graphic)
           SLATE = structural scaffolding
NO driver vs passenger statistics, NO Lynch/MSI, NO chromothripsis,
NO mutation rate/signatures, NO synthetic lethality (card exclusions).

Gate B: every zero-width stroke is also zero-opacity.
Single-method .animate only — no chained .animate calls.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403

_bs = pathlib.Path(__file__).with_name("beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 15)}


# ---------------------------------------------------------------- helpers

def _fan(width, height, color=TEAL, opacity=0.82):
    """A right-pointing triangle representing a clonal expansion fan."""
    pts = [ORIGIN, UP * (height / 2), RIGHT * width + UP * (height / 6),
           RIGHT * width + DOWN * (height / 6), DOWN * (height / 2)]
    poly = Polygon(*pts)
    poly.set_fill(color, opacity).set_stroke(width=0, opacity=0)
    return poly


def _stage_arrow(length=1.2):
    return Arrow(ORIGIN, RIGHT * length, color=INK, stroke_width=3,
                 tip_length=0.18, buff=0.0)


def _mutation_chip(label, size=22):
    return LabelChip(label, accent=CRIMSON, size=size)


def _baseline(y=-3.2, width=12.0):
    """Horizontal baseline for timelines."""
    return Line(LEFT * (width / 2), RIGHT * (width / 2),
                color=INK, stroke_width=1.8).shift(UP * y)


# ================================================================ scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why Cancer Is Evolution", font=DISPLAY, color=INK,
                  font_size=30, weight=BOLD)
        t2 = Text("Running Inside the Body", font=DISPLAY, color=CRIMSON,
                  font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13,
                 t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B03_StageTimeline(Scene):
    """Four stage labels connected by arrows; CRIMSON mutation chips drop in sequence."""
    def construct(self):
        total = DUR["B03"]
        stages = ["NORMAL", "SMALL\nADENOMA", "LARGE\nADENOMA", "CARCINOMA"]
        mutations = ["APC", "KRAS", "18q loss", "TP53"]
        stage_colors = [INK, TEAL, TEAL, CRIMSON]

        # Build stage nodes
        nodes = []
        for label, col in zip(stages, stage_colors):
            t = Text(label, font=DISPLAY, color=col, font_size=16, weight=BOLD)
            nodes.append(t)

        node_x = [-5.2, -1.8, 1.5, 4.8]
        for node, x in zip(nodes, node_x):
            node.move_to(RIGHT * x + UP * 0.5)

        # Arrows between stages
        arrows = []
        for i in range(3):
            ax = (node_x[i] + node_x[i + 1]) / 2
            a = _stage_arrow(length=node_x[i + 1] - node_x[i] - 1.2)
            a.move_to(RIGHT * ax + UP * 0.5)
            arrows.append(a)

        # Mutation chips above arrows
        chip_x = [(node_x[i] + node_x[i + 1]) / 2 for i in range(3)]
        # TP53 chip sits on the last arrow but we only have 3 arrows for 4 stages
        # Actually 4 mutations map to transitions: APC, KRAS, 18q, TP53 on 3 arrows
        # We compress: put APC and KRAS on first two arrows, 18q+TP53 on third
        # Better: use 3 transitions, label APC/KRAS/TP53 (drop 18q per exclusion note
        # — 18q is fine to include but we only have 3 arrows)
        # Per beat sheet, all 4 appear — add a 4th label on the 3rd arrow stacked
        chip_labels = [["APC"], ["KRAS"], ["18q", "TP53"]]
        chips = []
        for cx, lbls in zip(chip_x, chip_labels):
            grp = VGroup()
            for j, lbl in enumerate(lbls):
                c = _mutation_chip(lbl, size=18)
                c.move_to(RIGHT * cx + UP * (1.15 - j * 0.42))
                grp.add(c)
            chips.append(grp)

        # Stage dots
        dots = [Dot(radius=0.14, color=col).move_to(RIGHT * x + UP * 0.5)
                for x, col in zip(node_x, stage_colors)]

        self.play(LaggedStart(*[FadeIn(n, shift=UP * 0.12) for n in nodes],
                              lag_ratio=0.15, run_time=1.0))
        self.play(LaggedStart(*[FadeIn(d, scale=0.8) for d in dots],
                              lag_ratio=0.15, run_time=0.6))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows],
                              lag_ratio=0.25, run_time=1.0))
        for chip_grp in chips:
            self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.18) for c in chip_grp],
                                  lag_ratio=0.2, run_time=0.6))
        self.wait(max(0.3, total - 3.2))


class B04_QuestionCard(Scene):
    def construct(self):
        total = DUR["B04"]
        eye = Text("THE QUESTION", font=DISPLAY, color=SLATE, font_size=16)
        q = Text("Why do independent cancers", font=DISPLAY, color=INK,
                 font_size=26, weight=BOLD)
        q2 = Text("converge on the same mutations", font=DISPLAY, color=INK,
                  font_size=26, weight=BOLD)
        q3 = Text("in the same order?", font=DISPLAY, color=CRIMSON,
                  font_size=26, weight=BOLD)
        block = VGroup(q, q2, q3).arrange(DOWN, buff=0.15).move_to(UP * 0.3)
        u = Line(q3.get_corner(DL) + DOWN * 0.12,
                 q3.get_corner(DR) + DOWN * 0.12,
                 color=GOLD, stroke_width=2)
        sub = Text("if mutation is random, why does the path repeat?",
                   font=SERIF, color=INK, font_size=20, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.45)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), run_time=1.0)
        self.play(Create(u), FadeIn(sub, shift=UP * 0.1), run_time=0.9)
        self.wait(max(0.3, total - 2.4))


class B05_RandomExpectation(Scene):
    """Three tumors each hit random different genes — no pattern."""
    def construct(self):
        total = DUR["B05"]
        import random
        random.seed(42)

        n_rows, n_cols = 5, 10
        dot_size = 0.22
        gap = 0.12

        def _gene_grid(highlights, x_offset):
            g = VGroup()
            for r in range(n_rows):
                for c in range(n_cols):
                    sq = Square(dot_size).set_fill(SLATE, 0.25).set_stroke(width=0, opacity=0)
                    sq.move_to(RIGHT * (c * (dot_size + gap) + x_offset) +
                               DOWN * (r * (dot_size + gap)))
                    g.add(sq)
            for idx in highlights:
                g[idx].set_fill(CRIMSON, 0.85)
            return g

        # Three tumor panels, each with different random highlights
        highlight_sets = [
            random.sample(range(50), 5),
            random.sample(range(50), 5),
            random.sample(range(50), 5),
        ]
        labels = ["tumor 1", "tumor 2", "tumor 3"]
        x_offsets = [-5.4, -0.3, 4.8]
        col_width = n_cols * (dot_size + gap)

        grids = []
        for hl, x_off in zip(highlight_sets, x_offsets):
            grid = _gene_grid(hl, x_off - col_width / 2 + dot_size / 2)
            grids.append(grid)

        tumor_labels = []
        for lbl, x_off in zip(labels, x_offsets):
            tl = SerifLabel(lbl, accent=SLATE, size=22)
            tl.move_to(RIGHT * x_off + UP * 1.8)
            tumor_labels.append(tl)

        eye = Text("random expectation", font=DISPLAY, color=SLATE,
                   font_size=16).to_edge(UP, buff=0.5)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(tl) for tl in tumor_labels],
                              lag_ratio=0.2, run_time=0.8))
        for grid in grids:
            self.play(LaggedStart(*[FadeIn(sq, scale=0.85) for sq in grid],
                                  lag_ratio=0.01, run_time=0.7))
        self.wait(max(0.4, total - 2.0 - 0.5 - 0.8))


class B06_ConsistentPath(Scene):
    """Three tumor rows each carry the identical ordered driver sequence."""
    def construct(self):
        total = DUR["B06"]
        driver_seq = ["APC", "KRAS", "18q", "TP53"]
        row_labels = ["tumor 1", "tumor 2", "tumor 3"]
        row_y = [1.2, 0.0, -1.2]

        eye = Text("what Vogelstein found", font=DISPLAY, color=TEAL,
                   font_size=16).to_edge(UP, buff=0.5)
        all_chips = []
        row_label_mobs = []
        for y, rl in zip(row_y, row_labels):
            rlabel = SerifLabel(rl, accent=SLATE, size=20)
            rlabel.move_to(LEFT * 5.8 + UP * y)
            row_label_mobs.append(rlabel)
            row_chips = []
            for j, drv in enumerate(driver_seq):
                c = _mutation_chip(drv, size=20)
                c.move_to(RIGHT * (-2.0 + j * 2.5) + UP * y)
                row_chips.append(c)
            all_chips.append(row_chips)

        # Column alignment lines (thin vertical lines between columns)
        col_lines = []
        for j in range(4):
            xl = -2.0 + j * 2.5
            ln = DashedLine(UP * 1.8, DOWN * 1.8, color=SLATE,
                            stroke_width=1.0, dash_length=0.12)
            ln.move_to(RIGHT * xl)
            col_lines.append(ln)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(rl) for rl in row_label_mobs],
                              lag_ratio=0.2, run_time=0.6))
        self.play(LaggedStart(*[FadeIn(ln) for ln in col_lines],
                              lag_ratio=0.15, run_time=0.5))
        for row_chips in all_chips:
            self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.15) for c in row_chips],
                                  lag_ratio=0.12, run_time=0.7))
        self.wait(max(0.4, total - 2.3))


class B07_SectionCard(Scene):
    def construct(self):
        total = DUR["B07"]
        eye = Text("THE MECHANISM", font=DISPLAY, color=SLATE, font_size=16)
        title = Text("Selection, not randomness", font=DISPLAY, color=INK,
                     font_size=34, weight=BOLD)
        block = VGroup(title).move_to(UP * 0.1)
        u = Line(title.get_corner(DL) + DOWN * 0.13,
                 title.get_corner(DR) + DOWN * 0.13,
                 color=TEAL, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(title), Create(u), run_time=1.0)
        self.wait(max(0.3, total - 1.5))


class B08_CloneFan1(Scene):
    """Stage 1: APC mutation — first expansion fan."""
    def construct(self):
        total = DUR["B08"]

        baseline = _baseline(y=-2.8, width=12.0)
        time_label = Text("time", font=SERIF, color=INK, font_size=18, slant=ITALIC)
        time_label.move_to(RIGHT * 5.5 + DOWN * 2.8)

        # One normal cell dot at left
        start_dot = Dot(radius=0.2, color=INK).move_to(LEFT * 5.0 + DOWN * 2.0)
        normal_lbl = SerifLabel("1 normal crypt cell", accent=SLATE, size=18)
        normal_lbl.next_to(start_dot, UP, buff=0.2)

        # APC chip
        apc_chip = _mutation_chip("APC", size=22)
        apc_chip.move_to(LEFT * 3.0 + UP * 0.6)

        # Fan growing rightward from APC event
        fan1 = _fan(width=6.0, height=2.8, color=TEAL, opacity=0.72)
        fan1.move_to(RIGHT * 0.5 + DOWN * 1.0)

        clone_lbl = SerifLabel("APC clone", accent=TEAL, size=22)
        clone_lbl.move_to(RIGHT * 1.2 + UP * 0.5)

        self.play(Create(baseline), FadeIn(time_label), run_time=0.6)
        self.play(FadeIn(start_dot), FadeIn(normal_lbl), run_time=0.6)
        self.play(FadeIn(apc_chip, shift=DOWN * 0.25, scale=0.85), run_time=0.7)
        self.play(GrowFromPoint(fan1, fan1.get_left()), run_time=1.2)
        self.play(FadeIn(clone_lbl, shift=LEFT * 0.15), run_time=0.6)
        self.wait(max(0.3, total - 3.7))


class B09_CloneFan2(Scene):
    """Stage 2: KRAS mutation — second fan within the APC fan."""
    def construct(self):
        total = DUR["B09"]

        baseline = _baseline(y=-2.8, width=12.0)
        time_label = Text("time", font=SERIF, color=INK, font_size=18, slant=ITALIC)
        time_label.move_to(RIGHT * 5.5 + DOWN * 2.8)

        # APC fan (dim — already established)
        fan1 = _fan(width=8.0, height=3.4, color=TEAL, opacity=0.38)
        fan1.move_to(RIGHT * 0.5 + DOWN * 0.8)
        apc_lbl = SerifLabel("APC clone", accent=TEAL, size=18)
        apc_lbl.move_to(LEFT * 1.5 + DOWN * 0.3)

        # KRAS chip — inside the fan
        kras_chip = _mutation_chip("KRAS", size=22)
        kras_chip.move_to(LEFT * 0.5 + UP * 1.0)

        # Second, brighter fan inside the first
        fan2 = _fan(width=4.0, height=2.0, color=TEAL, opacity=0.85)
        fan2.move_to(RIGHT * 2.5 + DOWN * 1.1)

        clone2_lbl = SerifLabel("KRAS sub-clone", accent=TEAL, size=22)
        clone2_lbl.move_to(RIGHT * 3.2 + UP * 0.2)

        polyp_lbl = Text("small polyp", font=SERIF, color=INK,
                         font_size=18, slant=ITALIC)
        polyp_lbl.move_to(RIGHT * 3.6 + UP * -0.8)

        self.play(Create(baseline), FadeIn(time_label), run_time=0.5)
        self.play(FadeIn(fan1), FadeIn(apc_lbl), run_time=0.7)
        self.play(FadeIn(kras_chip, shift=DOWN * 0.25, scale=0.85), run_time=0.7)
        self.play(GrowFromPoint(fan2, fan2.get_left()), run_time=1.1)
        self.play(FadeIn(clone2_lbl), run_time=0.5)
        self.play(FadeIn(polyp_lbl, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 4.0))


class B10_CloneFan3(Scene):
    """Stages 3 and 4: TP53 loss then invasion — fan complete."""
    def construct(self):
        total = DUR["B10"]

        baseline = _baseline(y=-2.8, width=12.0)
        time_label = Text("time", font=SERIF, color=INK, font_size=18, slant=ITALIC)
        time_label.move_to(RIGHT * 6.0 + DOWN * 2.8)

        # Fan 1 (APC, dim)
        fan1 = _fan(width=9.5, height=3.8, color=TEAL, opacity=0.28)
        fan1.move_to(RIGHT * 0.5 + DOWN * 0.7)
        # Fan 2 (KRAS, medium)
        fan2 = _fan(width=6.0, height=2.6, color=TEAL, opacity=0.50)
        fan2.move_to(RIGHT * 1.5 + DOWN * 0.9)
        # TP53 chip
        tp53_chip = _mutation_chip("TP53", size=22)
        tp53_chip.move_to(RIGHT * 1.2 + UP * 1.1)
        # Fan 3 (TP53, bright)
        fan3 = _fan(width=3.2, height=1.8, color=TEAL, opacity=0.88)
        fan3.move_to(RIGHT * 3.5 + DOWN * 1.2)

        clone3_lbl = SerifLabel("TP53 sub-clone", accent=TEAL, size=20)
        clone3_lbl.move_to(RIGHT * 4.0 + UP * 0.2)

        # Basement membrane dashed line
        bm = DashedLine(LEFT * 6.0 + DOWN * 2.0, RIGHT * 6.0 + DOWN * 2.0,
                        color=SLATE, stroke_width=2, dash_length=0.2)
        bm_lbl = SerifLabel("basement membrane", accent=SLATE, size=16)
        bm_lbl.move_to(RIGHT * 4.5 + DOWN * 1.65)

        # Carcinoma tip breaching membrane
        breach = Triangle().scale(0.22).set_fill(CRIMSON, 0.9).set_stroke(width=0, opacity=0)
        breach.move_to(RIGHT * 4.6 + DOWN * 2.25)

        carcinoma_lbl = LabelChip("carcinoma", accent=CRIMSON, size=18)
        carcinoma_lbl.move_to(RIGHT * 3.8 + DOWN * 3.2)

        self.play(Create(baseline), FadeIn(time_label), run_time=0.5)
        self.play(FadeIn(fan1), FadeIn(fan2), run_time=0.7)
        self.play(FadeIn(tp53_chip, shift=DOWN * 0.25, scale=0.85), run_time=0.6)
        self.play(GrowFromPoint(fan3, fan3.get_left()), FadeIn(clone3_lbl), run_time=1.0)
        self.play(Create(bm), FadeIn(bm_lbl), run_time=0.7)
        self.play(FadeIn(breach, scale=0.6), FadeIn(carcinoma_lbl), run_time=0.7)
        self.wait(max(0.3, total - 4.2))


class B11_SelectionLogic(Scene):
    """Three-row selection logic: gene chip, growth advantage text, TEAL arrow."""
    def construct(self):
        total = DUR["B11"]

        eye = Text("why the order is fixed", font=DISPLAY, color=TEAL,
                   font_size=16).to_edge(UP, buff=0.5)

        rows_data = [
            ("APC", "activates Wnt — strongest growth lever in the colon", 4.0),
            ("KRAS", "locks RAS on — continuous proliferation signal", 2.8),
            ("TP53", "removes damage checkpoint — bypasses death signals", 1.8),
        ]
        row_y = [1.0, 0.0, -1.0]

        gene_chips = []
        advantage_labels = []
        advantage_arrows = []

        for (gene, advantage, arrow_len), y in zip(rows_data, row_y):
            chip = _mutation_chip(gene, size=22)
            chip.move_to(LEFT * 5.0 + UP * y)
            gene_chips.append(chip)

            adv = Text(advantage, font=SERIF, color=INK, font_size=18)
            adv.move_to(LEFT * 1.2 + UP * y)
            advantage_labels.append(adv)

            arr = Arrow(RIGHT * 1.8, RIGHT * (1.8 + arrow_len),
                        color=TEAL, stroke_width=4, tip_length=0.18, buff=0.0)
            arr.move_to(RIGHT * (1.8 + arrow_len / 2) + UP * y)
            advantage_arrows.append(arr)

        self.play(FadeIn(eye), run_time=0.5)
        for chip, adv, arr in zip(gene_chips, advantage_labels, advantage_arrows):
            self.play(FadeIn(chip, shift=RIGHT * 0.15), run_time=0.5)
            self.play(FadeIn(adv, shift=LEFT * 0.1), run_time=0.5)
            self.play(GrowArrow(arr), run_time=0.6)
        self.wait(max(0.4, total - 0.5 - 3 * 1.6))


class B12_AgeRisk(Scene):
    """Horizontal 0-60 yr timeline; four mutation chips drop at spaced intervals."""
    def construct(self):
        total = DUR["B12"]

        # Timeline axis
        axis = Arrow(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=3,
                     tip_length=0.22, buff=0.0)
        axis.move_to(DOWN * 0.5)
        yr_label = Text("years", font=SERIF, color=INK, font_size=18, slant=ITALIC)
        yr_label.next_to(axis, RIGHT, buff=0.2)

        # Year tick labels
        year_ticks = [0, 15, 30, 45, 60]
        tick_mobs = []
        axis_left = -5.2
        axis_right = 5.2
        for yr in year_ticks:
            frac = yr / 60.0
            x = axis_left + frac * (axis_right - axis_left)
            tick = Line(UP * 0.12, DOWN * 0.12, color=INK, stroke_width=2).move_to(
                RIGHT * x + DOWN * 0.5)
            lbl = Text(str(yr), font=MONO, color=INK, font_size=16)
            lbl.next_to(tick, DOWN, buff=0.1)
            tick_mobs.append(VGroup(tick, lbl))

        # Four mutations at approximate years 0, 15, 30, 45
        mutation_data = [
            ("APC", 0),
            ("KRAS", 15),
            ("TP53", 30),
            ("invasion", 45),
        ]
        chips = []
        fans = []
        for gene, yr in mutation_data:
            frac = yr / 60.0
            x = axis_left + frac * (axis_right - axis_left)
            c = _mutation_chip(gene, size=18)
            c.move_to(RIGHT * x + UP * 0.8)
            chips.append(c)
            # Small TEAL wedge below the axis at each stage
            remaining_frac = (60 - yr) / 60.0
            fan_w = remaining_frac * 3.0 + 0.5
            fan_h = remaining_frac * 1.2 + 0.3
            f = _fan(width=fan_w, height=fan_h, color=TEAL, opacity=0.65)
            f.move_to(RIGHT * (x + fan_w / 2) + DOWN * 1.5)
            fans.append(f)

        carcinoma_chip = LabelChip("carcinoma", accent=CRIMSON, size=18)
        carcinoma_chip.move_to(RIGHT * 5.0 + DOWN * 2.1)

        self.play(GrowArrow(axis), FadeIn(yr_label), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(t) for t in tick_mobs], lag_ratio=0.12,
                              run_time=0.6))
        for chip, fan in zip(chips, fans):
            self.play(FadeIn(chip, shift=DOWN * 0.2), run_time=0.45)
            self.play(GrowFromPoint(fan, fan.get_left()), run_time=0.45)
        self.play(FadeIn(carcinoma_chip, scale=0.85), run_time=0.6)
        self.wait(max(0.3, total - 0.7 - 0.6 - 4 * 0.9 - 0.6))


class B13_WorkedExample(Scene):
    """Illustrative single-patient timeline with four milestones."""
    def construct(self):
        total = DUR["B13"]

        eye = Text("illustrative", font=MONO, color=SLATE,
                   font_size=14, slant=ITALIC).to_corner(UR, buff=0.5)

        # Horizontal timeline
        axis = Arrow(LEFT * 5.8, RIGHT * 5.8, color=INK, stroke_width=3,
                     tip_length=0.2, buff=0.0)
        axis.move_to(DOWN * 2.4)

        # Milestone data: (year, mutation label, description, x-position)
        milestones = [
            (0,  "APC",     "1 crypt cell",         -5.2),
            (5,  "KRAS",    "small polyp",          -1.8),
            (13, "TP53",    "large adenoma",          1.6),
            (17, "invasion","carcinoma",              4.8),
        ]

        # Pre-build all objects
        tick_groups = []
        chip_mobs = []
        fan_mobs = []
        desc_mobs = []
        yr_mobs = []

        for yr, mut, desc, x in milestones:
            tick = Line(UP * 0.15, DOWN * 0.15, color=INK, stroke_width=2)
            tick.move_to(RIGHT * x + DOWN * 2.4)

            yr_t = Text(str(yr), font=MONO, color=INK, font_size=18)
            yr_t.next_to(tick, DOWN, buff=0.12)
            yr_mobs.append(yr_t)
            tick_groups.append(VGroup(tick))

            accent = CRIMSON if mut != "invasion" else CRIMSON
            c = LabelChip(mut, accent=accent, size=18)
            c.move_to(RIGHT * x + UP * 0.2)
            chip_mobs.append(c)

            d = Text(desc, font=SERIF, color=INK, font_size=16, slant=ITALIC)
            d.move_to(RIGHT * x + UP * 1.0)
            desc_mobs.append(d)

            # Fan widens across milestones
            stage_idx = milestones.index((yr, mut, desc, x))
            fan_w = 0.8 + stage_idx * 0.9
            fan_h = 0.5 + stage_idx * 0.45
            fan_color = TEAL if mut != "invasion" else CRIMSON
            f = _fan(width=fan_w, height=fan_h, color=fan_color, opacity=0.78)
            f.move_to(RIGHT * (x + fan_w / 2 - 0.3) + DOWN * 1.6)
            fan_mobs.append(f)

        illus_note = Text("(numbers illustrative)", font=MONO, color=SLATE,
                          font_size=13, slant=ITALIC)
        illus_note.to_edge(DOWN, buff=0.3)

        self.play(GrowArrow(axis), FadeIn(eye), run_time=0.6)
        self.play(FadeIn(illus_note), run_time=0.4)

        for i, (tg, yr_t, chip, desc, fan) in enumerate(
                zip(tick_groups, yr_mobs, chip_mobs, desc_mobs, fan_mobs)):
            self.play(FadeIn(tg), FadeIn(yr_t), run_time=0.4)
            self.play(FadeIn(chip, shift=DOWN * 0.2), run_time=0.5)
            self.play(GrowFromPoint(fan, fan.get_left()), run_time=0.7)
            self.play(FadeIn(desc, shift=DOWN * 0.1), run_time=0.4)
            if i < 3:
                self.wait(0.5)

        self.wait(max(0.5, total - (0.6 + 0.4 + 4 * (0.4 + 0.5 + 0.7 + 0.4 + 0.5))))


class B14_EndCard(Scene):
    def construct(self):
        total = DUR["B14"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        answer = Text("Cancer finds the same path because", font=DISPLAY, color=INK,
                      font_size=24, weight=BOLD)
        answer2 = Text("selection keeps finding the same advantages.", font=DISPLAY,
                       color=INK, font_size=24, weight=BOLD)
        block = VGroup(answer, answer2).arrange(DOWN, buff=0.16).move_to(UP * 0.2)
        u = Line(answer2.get_corner(DL) + DOWN * 0.12,
                 answer2.get_corner(DR) + DOWN * 0.12,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), run_time=1.0)
        self.play(Create(u), run_time=0.7)
        self.wait(max(0.5, total - 2.2))
