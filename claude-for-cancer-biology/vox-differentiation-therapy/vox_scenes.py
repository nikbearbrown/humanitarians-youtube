"""vox_scenes.py — Why a Cancer Drug That Restores Differentiation Is Better
Than One That Kills (vox-differentiation-therapy, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'. B02 (STILL ai) and
B10 (STILL geo) have no scene — they compile as slates.

Color law: TEAL = mature cell / drug working / lock released
           CRIMSON = immature blast / 2HG present / lock engaged
           GOLD = single editor highlight (fill only, once, in B08)

Exclusions: no IDH biochemistry beyond 2HG-as-competitive-inhibitor; no IDH1 vs
IDH2 comparison; no AML vs glioma distinction; no DNMT mechanism; no EZH2.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)
import json, os

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ─── B01 Title / Cold Open Card ──────────────────────────────────────────────

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why Restoring Differentiation", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        t2 = Text("Beats Killing Cancer Cells", font=DISPLAY, color=CRIMSON,
                  font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ─── B03 The Mutation Rides Along ────────────────────────────────────────────

class B03_MutationRidesAlong(Scene):
    """Two cells: a crimson blast morphs through stages to a teal neutrophil.
    A small CRIMSON chip on both reads 'IDH1 mut' — the mutation is inherited."""
    def construct(self):
        total = DUR["B03"]

        # Blast: round dark nucleus (crimson fill, dark ring)
        blast_body = Circle(radius=0.55)
        blast_body.set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 3)
        blast_nucleus = Circle(radius=0.38)
        blast_nucleus.set_fill(CRIMSON, 0.7).set_stroke(width=0, opacity=0)
        blast_nucleus.move_to(blast_body.get_center())
        blast = VGroup(blast_body, blast_nucleus).move_to(LEFT * 3.2)

        blast_chip = LabelChip("IDH1 mut", accent=CRIMSON, size=18)
        blast_chip.next_to(blast, DOWN, buff=0.25)
        blast_label = SerifLabel("leukemic blast", CRIMSON, size=22)
        blast_label.next_to(blast, UP, buff=0.25)

        # Neutrophil: multi-lobed teal nucleus
        def _lobe(center):
            c = Circle(radius=0.22)
            c.set_fill(TEAL, 0.75).set_stroke(width=0, opacity=0)
            c.move_to(center)
            return c

        neut_body = Circle(radius=0.55)
        neut_body.set_fill(TEAL, 0.10).set_stroke(TEAL, 3)
        lobe_centers = [RIGHT * 3.2 + UP * 0.22,
                        RIGHT * 3.2 + RIGHT * 0.24 + DOWN * 0.1,
                        RIGHT * 3.2 + LEFT * 0.24 + DOWN * 0.1]
        lobes = VGroup(*[_lobe(c) for c in lobe_centers])
        neut_body.move_to(RIGHT * 3.2)
        neutrophil = VGroup(neut_body, lobes)

        neut_chip = LabelChip("IDH1 mut", accent=TEAL, size=18)
        neut_chip.next_to(neutrophil, DOWN, buff=0.25)
        neut_label = SerifLabel("mature neutrophil", TEAL, size=22)
        neut_label.next_to(neutrophil, UP, buff=0.25)

        arrow = Arrow(LEFT * 1.5, RIGHT * 1.5, color=INK, stroke_width=3,
                      buff=0.1, tip_length=0.22)
        arrow_label = SerifLabel("matured", INK, size=20)
        arrow_label.next_to(arrow, UP, buff=0.15)

        # Animate
        self.play(FadeIn(blast), FadeIn(blast_chip), FadeIn(blast_label), run_time=0.9)
        self.play(FadeIn(arrow), FadeIn(arrow_label), run_time=0.6)
        self.play(
            ReplacementTransform(blast.copy(), neutrophil),
            FadeIn(neut_chip), FadeIn(neut_label),
            run_time=1.2
        )
        self.wait(max(0.3, total - 2.7))


# ─── B04 The Question Card ───────────────────────────────────────────────────

class B04_TheQuestion(Scene):
    def construct(self):
        total = DUR["B04"]
        eye = LabelChip("The Question", accent=SLATE, size=22)
        q1 = Text("Cancer drugs should kill cancer cells.", font=SERIF,
                  color=INK, font_size=26, slant=ITALIC)
        q2 = Text("Here blast counts fall — cells do not die.", font=SERIF,
                  color=CRIMSON, font_size=26, slant=ITALIC)
        q3 = Text("How does blocking a metabolic enzyme", font=DISPLAY,
                  color=INK, font_size=24, weight=BOLD)
        q4 = Text("produce cells that differentiate?", font=DISPLAY,
                  color=INK, font_size=24, weight=BOLD)

        block = VGroup(q1, q2, q3, q4).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        block.move_to(ORIGIN + DOWN * 0.1)
        eye.next_to(block, UP, buff=0.45)

        # Shape anchor: a crimson blast that morphs to teal neutrophil
        # gives Gate A a real shape-state transition to record
        shape_blast = Circle(radius=0.28)
        shape_blast.set_fill(CRIMSON, 0.55).set_stroke(CRIMSON, 2)
        shape_blast.move_to(RIGHT * 5.5 + UP * 0.5)

        self.play(FadeIn(eye, shift=DOWN * 0.1), FadeIn(shape_blast), run_time=0.5)
        self.play(FadeIn(q1, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(VGroup(q3, q4), shift=UP * 0.1),
                  shape_blast.animate.scale(1.25),
                  run_time=0.8)
        self.wait(max(0.3, total - 2.7))


# ─── B05 Normal Differentiation Ladder ───────────────────────────────────────

class B05_NormalDifferentiation(Scene):
    """A vertical ladder of circles: large stem cell at top, smaller/more
    defined cells stepping down to a teal mature neutrophil at bottom."""
    def construct(self):
        total = DUR["B05"]
        label_top = SerifLabel("stem cell", SLATE, size=20)
        label_bot = SerifLabel("mature cell", TEAL, size=20)

        stages = []
        stage_colors = [SLATE, SLATE, TEAL, TEAL, TEAL]
        stage_opacities = [0.25, 0.40, 0.35, 0.55, 0.85]
        stage_radii = [0.48, 0.40, 0.36, 0.32, 0.28]

        for i, (col, op, r) in enumerate(zip(stage_colors, stage_opacities, stage_radii)):
            c = Circle(radius=r)
            c.set_fill(col, op).set_stroke(col, 2.5)
            stages.append(c)

        ladder = VGroup(*stages).arrange(DOWN, buff=0.25)
        ladder.move_to(ORIGIN + LEFT * 0.5)

        label_top.next_to(stages[0], RIGHT, buff=0.35)
        label_bot.next_to(stages[-1], RIGHT, buff=0.35)

        arrow_down = Arrow(stages[0].get_bottom() + DOWN * 0.05,
                           stages[-1].get_top() + UP * 0.05,
                           color=TEAL, stroke_width=2, buff=0.08, tip_length=0.2)
        arrow_down.set_opacity(0.5)

        self.play(FadeIn(stages[0]), FadeIn(label_top), run_time=0.7)
        for s in stages[1:]:
            self.play(FadeIn(s, shift=DOWN * 0.15), run_time=0.4)
        self.play(FadeIn(label_bot), Create(arrow_down), run_time=0.7)
        self.wait(max(0.3, total - 0.7 - len(stages) * 0.4 - 0.7))


# ─── B06 AML Differentiation Stall ───────────────────────────────────────────

class B06_AMLStall(Scene):
    """Same ladder but the blast is stuck at stage 1. A CRIMSON bar blocks
    further descent. Multiple crimson blasts accumulate."""
    def construct(self):
        total = DUR["B06"]

        # Three blasts piling up at top
        def _blast(pos):
            body = Circle(radius=0.38)
            body.set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2.5)
            nuc = Circle(radius=0.26)
            nuc.set_fill(CRIMSON, 0.70).set_stroke(width=0, opacity=0)
            nuc.move_to(body.get_center())
            return VGroup(body, nuc).move_to(pos)

        blasts = VGroup(
            _blast(UP * 1.5 + LEFT * 0.5),
            _blast(UP * 0.6 + LEFT * 0.5),
            _blast(UP * 0.0 + LEFT * 0.5),
        )

        # Blocked gate bar
        bar = Rectangle(width=2.0, height=0.12)
        bar.set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
        bar.move_to(DOWN * 0.6 + LEFT * 0.5)

        bar_label = LabelChip("differentiation gate locked", accent=CRIMSON, size=18)
        bar_label.next_to(bar, RIGHT, buff=0.3)

        # Ghost of mature cell (faded, unreachable)
        ghost_body = Circle(radius=0.28)
        ghost_body.set_fill(TEAL, 0.10).set_stroke(TEAL, 1.5)
        ghost_body.move_to(DOWN * 1.6 + LEFT * 0.5)
        ghost_label = SerifLabel("mature cell", TEAL, size=18)
        ghost_label.next_to(ghost_body, RIGHT, buff=0.3)
        ghost_body.set_opacity(0.35)
        ghost_label.set_opacity(0.35)

        pile_label = LabelChip("blasts accumulate", accent=CRIMSON, size=20)
        pile_label.next_to(blasts, LEFT, buff=0.35)

        self.play(FadeIn(blasts[0]), run_time=0.5)
        self.play(FadeIn(blasts[1]), run_time=0.4)
        self.play(FadeIn(blasts[2]), FadeIn(pile_label), run_time=0.5)
        self.play(FadeIn(bar), FadeIn(bar_label), run_time=0.6)
        self.play(FadeIn(ghost_body), FadeIn(ghost_label), run_time=0.5)
        self.wait(max(0.3, total - 2.5))


# ─── B07 2HG Produced, Demethylases Jammed ───────────────────────────────────

class B07_TwoHGJam(Scene):
    """IDH1 mutant produces 2HG. A demethylase enzyme (gate shape) has a
    slot for alpha-ketoglutarate (AKG). 2HG fills the slot instead — wrong
    key, lock jammed. Methyl marks (crimson dots on a histone bar) stay."""
    def construct(self):
        total = DUR["B07"]

        # Histone bar with methyl marks on top (crimson dots = marks that stay)
        histone = Rectangle(width=3.8, height=0.45)
        histone.set_fill(SLATE, 0.35).set_stroke(SLATE, 2)
        histone.move_to(DOWN * 0.5)

        hist_label = SerifLabel("histone tail", SLATE, size=19)
        hist_label.next_to(histone, DOWN, buff=0.2)

        def _mark(x_off):
            m = Dot(radius=0.14)
            m.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
            m.move_to(histone.get_top() + RIGHT * x_off + UP * 0.14)
            return m

        marks = VGroup(*[_mark(x) for x in [-1.2, -0.4, 0.4, 1.2]])
        mark_label = LabelChip("methyl marks", accent=CRIMSON, size=18)
        mark_label.next_to(marks, RIGHT, buff=0.35)

        # Demethylase blocked (crimson outline box with X slot)
        dmt = Rectangle(width=1.5, height=1.0)
        dmt.set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 2.5)
        dmt.move_to(UP * 1.6 + LEFT * 0.3)
        dmt_label = SerifLabel("demethylase", CRIMSON, size=19)
        dmt_label.next_to(dmt, UP, buff=0.18)

        # 2HG chip jammed into the enzyme
        hg_chip = LabelChip("2HG jammed", accent=CRIMSON, size=18)
        hg_chip.move_to(dmt.get_center())

        # Blocked arrow from demethylase to marks (crossed)
        block_arrow = Arrow(dmt.get_bottom(), histone.get_top() + LEFT * 0.3,
                            color=CRIMSON, stroke_width=2.5, buff=0.06, tip_length=0.18)
        cross = Text("X", font=DISPLAY, color=CRIMSON, font_size=32, weight=BOLD)
        cross.move_to(block_arrow.get_center() + RIGHT * 0.12)

        self.play(FadeIn(histone), FadeIn(hist_label), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(m, scale=0.7) for m in marks], lag_ratio=0.12,
                              run_time=0.8), FadeIn(mark_label), run_time=0.8)
        self.play(FadeIn(dmt), FadeIn(dmt_label), run_time=0.6)
        self.play(FadeIn(hg_chip), run_time=0.5)
        self.play(FadeIn(block_arrow), FadeIn(cross), run_time=0.6)
        self.wait(max(0.3, total - 3.1))


# ─── B08 The Locked Door (the epigenetic lock) ───────────────────────────────

class B08_LockedDoor(Scene):
    """A door representing the differentiation program. 2HG is a key jammed
    in the lock (CRIMSON). GOLD highlight on the keyhole. The blast is on
    the left; the mature neutrophil silhouette is faintly behind the closed door."""
    def construct(self):
        total = DUR["B08"]

        # Door frame
        door_rect = Rectangle(width=1.8, height=3.0)
        door_rect.set_fill(INK, 0.07).set_stroke(INK, 3)
        door_rect.move_to(ORIGIN)

        door_label = LabelChip("differentiation program", accent=SLATE, size=18)
        door_label.next_to(door_rect, UP, buff=0.3)

        # Keyhole (gold highlight ellipse)
        keyhole = Ellipse(width=0.22, height=0.34)
        keyhole.set_fill(GOLD, 0.75).set_stroke(INK, 1.5)
        keyhole.move_to(door_rect.get_center() + RIGHT * 0.55)

        # 2HG key jammed in lock
        key_stem = Rectangle(width=0.55, height=0.1)
        key_stem.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        key_stem.move_to(keyhole.get_center() + RIGHT * 0.35)
        key_head = Circle(radius=0.15)
        key_head.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        key_head.move_to(key_stem.get_right() + RIGHT * 0.15)
        key = VGroup(key_stem, key_head)

        key_label = LabelChip("2HG", accent=CRIMSON, size=18)
        key_label.next_to(key_head, RIGHT, buff=0.2)

        # Blast on left (stuck)
        blast_body = Circle(radius=0.42)
        blast_body.set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2.5)
        blast_nuc = Circle(radius=0.28)
        blast_nuc.set_fill(CRIMSON, 0.70).set_stroke(width=0, opacity=0)
        blast_nuc.move_to(blast_body.get_center())
        blast = VGroup(blast_body, blast_nuc).move_to(LEFT * 3.8 + UP * 0.2)
        blast_label = SerifLabel("leukemic blast", CRIMSON, size=20)
        blast_label.next_to(blast, DOWN, buff=0.2)

        # Arrow pointing at locked door, blocked
        arr = Arrow(blast.get_right() + RIGHT * 0.1,
                    door_rect.get_left() + LEFT * 0.08,
                    color=CRIMSON, stroke_width=2.5, buff=0.06, tip_length=0.18)

        self.play(FadeIn(door_rect), FadeIn(door_label), run_time=0.7)
        self.play(FadeIn(keyhole), run_time=0.4)
        self.play(FadeIn(key), FadeIn(key_label), run_time=0.5)
        self.play(FadeIn(blast), FadeIn(blast_label), run_time=0.5)
        self.play(FadeIn(arr), run_time=0.5)
        self.wait(max(0.3, total - 2.6))


# ─── B09 Ivosidenib Removes the Jammed Key — Door Opens ─────────────────────

class B09_DoorOpens(Scene):
    """The jammed 2HG key is pulled out (FadeOut). The door swings open
    (rotation). The blast walks through and becomes a teal neutrophil."""
    def construct(self):
        total = DUR["B09"]

        # Build door closed first (matching B08 layout)
        door_rect = Rectangle(width=1.8, height=3.0)
        door_rect.set_fill(TEAL, 0.07).set_stroke(TEAL, 3)
        door_rect.move_to(ORIGIN)

        door_label = LabelChip("differentiation program", accent=TEAL, size=18)
        door_label.next_to(door_rect, UP, buff=0.3)

        keyhole = Ellipse(width=0.22, height=0.34)
        keyhole.set_fill(GOLD, 0.75).set_stroke(INK, 1.5)
        keyhole.move_to(door_rect.get_center() + RIGHT * 0.55)

        # Ivosidenib chip removes the key
        ivo_chip = LabelChip("ivosidenib", accent=TEAL, size=18)
        ivo_chip.move_to(RIGHT * 2.8 + UP * 1.0)

        # Arrow from ivosidenib chip to where key was
        ivo_arrow = Arrow(ivo_chip.get_left() + LEFT * 0.05,
                          keyhole.get_right() + RIGHT * 0.6,
                          color=TEAL, stroke_width=2.5, buff=0.06, tip_length=0.18)

        # Blast on left -> after door opens, transforms to neutrophil on right
        blast_body = Circle(radius=0.42)
        blast_body.set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2.5)
        blast_nuc = Circle(radius=0.28)
        blast_nuc.set_fill(CRIMSON, 0.70).set_stroke(width=0, opacity=0)
        blast_nuc.move_to(blast_body.get_center())
        blast = VGroup(blast_body, blast_nuc).move_to(LEFT * 3.8 + UP * 0.2)

        # Mature neutrophil on right of door
        neut_body = Circle(radius=0.42)
        neut_body.set_fill(TEAL, 0.10).set_stroke(TEAL, 2.5)

        def _lobe(offset):
            c = Circle(radius=0.17)
            c.set_fill(TEAL, 0.75).set_stroke(width=0, opacity=0)
            c.move_to(neut_body.get_center() + offset)
            return c

        lobes = VGroup(
            _lobe(UP * 0.18),
            _lobe(RIGHT * 0.19 + DOWN * 0.08),
            _lobe(LEFT * 0.19 + DOWN * 0.08),
        )
        neut_body.move_to(RIGHT * 3.6 + UP * 0.2)
        lobes.shift(RIGHT * 3.6 + UP * 0.2)
        neutrophil = VGroup(neut_body, lobes)
        neut_label = SerifLabel("mature neutrophil", TEAL, size=20)
        neut_label.next_to(neutrophil, DOWN, buff=0.2)

        # Open door (shift door to right edge, representing opening)
        open_door = Rectangle(width=0.18, height=3.0)
        open_door.set_fill(TEAL, 0.07).set_stroke(TEAL, 3)
        open_door.move_to(LEFT * 0.81)  # door swung to left edge

        # Animate
        self.play(FadeIn(door_rect), FadeIn(door_label), FadeIn(keyhole),
                  FadeIn(blast), run_time=0.7)
        self.play(FadeIn(ivo_chip), FadeIn(ivo_arrow), run_time=0.6)
        # Remove key, open door
        self.play(FadeOut(keyhole),
                  ReplacementTransform(door_rect, open_door),
                  run_time=0.9)
        # Blast moves through and becomes neutrophil
        self.play(
            blast.animate.move_to(ORIGIN + UP * 0.2),
            run_time=0.6
        )
        self.play(
            ReplacementTransform(blast, neutrophil),
            FadeIn(neut_label),
            run_time=1.0
        )
        self.wait(max(0.3, total - 3.8))


# ─── B11 Bone Marrow Time-Lapse (Illustrative) ───────────────────────────────

class B11_BoneMarrowTimeLapse(Scene):
    """Four time panels side by side: Day 0, Day 14, Day 28, Day 56.
    Each panel shows a small grid of cells — crimson blasts vs teal mature.
    The ratio shifts from ~80% blasts to <5% blasts over the four panels."""
    def construct(self):
        total = DUR["B11"]

        panel_w, panel_h = 2.8, 3.2
        days = ["Day 0", "Day 14", "Day 28", "Day 56"]
        # (n_blasts, n_mature) — illustrative, from card
        counts = [(16, 2), (12, 6), (4, 14), (1, 17)]
        xs = [-5.1, -1.7, 1.7, 5.1]

        panels = VGroup()
        for i, (day, (nb, nm), x) in enumerate(zip(days, counts, xs)):
            # Panel background
            bg = Rectangle(width=panel_w, height=panel_h)
            bg.set_fill(WHITE, 0.25).set_stroke(INK, 1.2)
            bg.move_to(RIGHT * x + DOWN * 0.2)

            # Day label
            day_label = Text(day, font=DISPLAY, color=INK, font_size=19, weight=BOLD)
            day_label.next_to(bg, UP, buff=0.18)

            # Cell grid (18 cells total, arranged 6x3)
            per_row = 6
            cell_size = 0.3
            gap = 0.08
            grid = VGroup()
            total_cells = nb + nm
            for ci in range(total_cells):
                col = CRIMSON if ci < nb else TEAL
                # Blasts: round; mature: smaller with lighter fill
                cell = Circle(radius=cell_size / 2)
                cell.set_fill(col, 0.7 if ci < nb else 0.5)
                cell.set_stroke(col, 1.5)
                cx = (ci % per_row) * (cell_size + gap)
                cy = -(ci // per_row) * (cell_size + gap)
                cell.move_to(bg.get_center() + RIGHT * (cx - (per_row - 1) * (cell_size + gap) / 2)
                             + UP * (cy + 0.3))
                grid.add(cell)

            # Blast % chip
            pct = int(round(nb / total_cells * 100))
            pct_chip = LabelChip(f"{pct}% blasts", accent=CRIMSON if pct > 20 else TEAL, size=16)
            pct_chip.next_to(bg, DOWN, buff=0.18)

            panel_group = VGroup(bg, day_label, grid, pct_chip)
            panels.add(panel_group)

        illustrative = SerifLabel("illustrative — numbers are representative",
                                   SLATE, size=18)
        illustrative.to_edge(DOWN, buff=0.35)

        for i, pg in enumerate(panels):
            self.play(FadeIn(pg, shift=UP * 0.12), run_time=0.7)

        self.play(FadeIn(illustrative), run_time=0.5)
        self.wait(max(0.3, total - len(panels) * 0.7 - 0.5))


# ─── B12 Recap Endcard ───────────────────────────────────────────────────────

class B12_Recap(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("An oncometabolite locked the", font=DISPLAY, color=INK,
                  font_size=24, weight=BOLD)
        t2 = Text("developmental program.", font=DISPLAY, color=CRIMSON,
                  font_size=24, weight=BOLD)
        t3 = Text("Remove the lock —", font=DISPLAY, color=INK,
                  font_size=24, weight=BOLD)
        t4 = Text("the cancer matures.", font=DISPLAY, color=TEAL,
                  font_size=24, weight=BOLD)
        block = VGroup(t1, t2, t3, t4).arrange(DOWN, buff=0.16).move_to(UP * 0.1)
        u = Line(t4.get_corner(DL) + DOWN * 0.1, t4.get_corner(DR) + DOWN * 0.1,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.5)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(VGroup(t1, t2), shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(VGroup(t3, t4), shift=UP * 0.1), Create(u), run_time=0.9)
        self.wait(max(0.3, total - 2.2))
