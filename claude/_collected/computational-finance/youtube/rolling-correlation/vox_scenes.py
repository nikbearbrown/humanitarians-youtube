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


class B04_CorrelationHeatmap(Scene):
    def construct(self):
        # 5x5 correlation matrix heatmap
        # Cell size: 1.6 wide x 0.8 tall
        # Grid total: 8.0 wide x 4.0 tall
        # Centered: top-left at (-4.0, 2.0), grid center at (0,0)
        n = 5
        cell_w = 1.6
        cell_h = 0.8
        grid_left = -4.0
        grid_top = 2.0

        LABELS = ["A1", "A2", "A3", "A4", "A5"]

        def cell_center(i, j):
            # i=row (0=top), j=col (0=left)
            x = grid_left + j * cell_w + cell_w / 2
            y = grid_top - i * cell_h - cell_h / 2
            return [x, y, 0]

        def cream_label_small(txt, pos, font_size=16, txt_color=INK):
            t = Text(txt, color=txt_color, font_size=font_size)
            t.move_to(pos)
            bg = Rectangle(
                width=t.width + 0.10, height=t.height + 0.06,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            )
            bg.move_to(pos)
            return VGroup(bg, t)

        # ---- Title ----
        title = Text("ROLLING CORRELATION — NORMAL vs CRISIS", color=INK, font_size=28, weight=BOLD)
        title.move_to([0, 3.2, 0])

        # ---- Build all cells ----
        all_cells = VGroup()
        diagonal_cells = []
        offdiag_cells = []

        for i in range(n):
            for j in range(n):
                pos = cell_center(i, j)
                rect = Rectangle(
                    width=cell_w - 0.04, height=cell_h - 0.04,
                    stroke_width=0.5, stroke_color=INK,
                )
                rect.move_to(pos)
                if i == j:
                    rect.set_fill(CRIMSON, opacity=0.9)
                    diagonal_cells.append(rect)
                else:
                    rect.set_fill(GOLD, opacity=0.85)
                    offdiag_cells.append(rect)
                all_cells.add(rect)

        # ---- Header labels ----
        header_labels = VGroup()
        # Column headers (top)
        for j in range(n):
            pos = [grid_left + j * cell_w + cell_w / 2, grid_top + 0.45, 0]
            header_labels.add(cream_label_small(LABELS[j], pos, font_size=18))
        # Row headers (left)
        for i in range(n):
            pos = [grid_left - 0.45, grid_top - i * cell_h - cell_h / 2, 0]
            header_labels.add(cream_label_small(LABELS[i], pos, font_size=18))

        # ---- Diagonal value texts "1.0" ----
        diag_value_texts = VGroup()
        for i in range(n):
            pos = cell_center(i, i)
            diag_value_texts.add(cream_label_small("1.0", pos, font_size=15, txt_color=CREAM))

        # ---- Off-diagonal sample texts: show "0.30" on all off-diag cells ----
        offdiag_sample_texts = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    pos = cell_center(i, j)
                    offdiag_sample_texts.append(
                        cream_label_small("0.30", pos, font_size=13, txt_color=INK)
                    )

        # ---- Crisis value texts "0.85" ----
        crisis_value_texts = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    pos = cell_center(i, j)
                    crisis_value_texts.append(
                        cream_label_small("0.85", pos, font_size=13, txt_color=CREAM)
                    )

        normal_regime_label = Text("NORMAL REGIME (corr ~0.30)", color=SLATE, font_size=22)
        normal_regime_label.move_to([0, -2.7, 0])

        crisis_regime_label = Text("CRISIS REGIME (corr ~0.85)", color=CRIMSON, font_size=22, weight=BOLD)
        crisis_regime_label.move_to([0, -2.7, 0])

        verdict_text = Text("Diversification fails when correlations spike",
                            color=CRIMSON, font_size=24, weight=BOLD)
        verdict_text.move_to([0, -3.2, 0])

        # ---- Sequence (7 play() calls) ----
        self.play(Write(title))
        self.play(*[FadeIn(r) for r in all_cells], *[Write(l) for l in header_labels])
        self.play(*[Write(v) for v in diag_value_texts])
        self.play(*[Write(v) for v in offdiag_sample_texts], Write(normal_regime_label))
        self.play(*[cell.animate.set_fill(CRIMSON, opacity=0.85) for cell in offdiag_cells])
        self.play(FadeOut(normal_regime_label), FadeIn(crisis_regime_label),
                  *[Transform(v, cv) for v, cv in zip(offdiag_sample_texts, crisis_value_texts)])
        self.play(Write(verdict_text))
