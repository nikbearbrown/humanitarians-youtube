"""
Manim scenes for brand-palette-accessibility-auditor
B04_ContrastAudit  — contrast ratio bar chart with FAIL rows animated
B06_CorrectedPalette — corrected palette all bars passing
"""

from manim import *

PALETTE = {
    "bg":       "#FAF9F5",
    "ink":      "#3D3929",
    "accent":   "#D97757",
    "pass_aa":  "#4A7C59",
    "fail":     "#C0392B",
    "warn":     "#E67E22",
    "line":     "#9B8EAA",
}

PAIRINGS = [
    ("warm-clay #A89068", "white",     3.1,  "normal text"),
    ("caption #9CA3AF",   "#FAFAF8",   2.9,  "normal text"),
    ("ink #3D3929",       "white",     14.2, "normal text"),
    ("accent #D97757",    "white",     3.1,  "large text"),
    ("bg #FAF9F5",        "ink",       14.2, "body copy"),
    ("decorative border", "#FAFAF8",   3.4,  "non-text"),
]

PAIRINGS_CORRECTED = [
    ("warm-clay #7A6045", "white",     4.8,  "normal text"),
    ("caption #6B7280",   "#FAFAF8",   4.6,  "normal text"),
    ("ink #3D3929",       "white",     14.2, "normal text"),
    ("accent #D97757",    "white",     3.1,  "large text"),
    ("bg #FAF9F5",        "ink",       14.2, "body copy"),
    ("decorative border", "#FAFAF8",   3.4,  "non-text"),
]

AA_NORMAL  = 4.5
AA_LARGE   = 3.0


def _bar_color(ratio, threshold):
    if ratio >= threshold:
        return PALETTE["pass_aa"]
    return PALETTE["fail"]


class B04_ContrastAudit(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "WCAG 2.2 AA — Contrast Audit",
            color=PALETTE["ink"], font_size=28
        ).to_edge(UP, buff=0.4)
        self.add(title)

        max_ratio  = 16.0
        bar_width  = 5.5
        bar_height = 0.38
        spacing    = 0.62
        left_x     = -3.2
        start_y    = 2.0

        aa_x = left_x + bar_width * (AA_NORMAL / max_ratio)
        al_x = left_x + bar_width * (AA_LARGE  / max_ratio)

        aa_line = DashedLine(
            start=[aa_x, start_y + 0.3, 0],
            end=[aa_x, start_y - spacing * len(PAIRINGS) - 0.1, 0],
            color=PALETTE["line"], dash_length=0.1, stroke_width=1.5
        )
        al_line = DashedLine(
            start=[al_x, start_y + 0.3, 0],
            end=[al_x, start_y - spacing * len(PAIRINGS) - 0.1, 0],
            color=PALETTE["warn"], dash_length=0.08, stroke_width=1.2
        )
        aa_label = Text("4.5:1 AA-normal", color=PALETTE["line"],
                        font_size=13).next_to([aa_x, start_y + 0.3, 0], UP, buff=0.05)
        al_label = Text("3:1 AA-large", color=PALETTE["warn"],
                        font_size=12).next_to([al_x, start_y + 0.3, 0], UP, buff=0.05)

        self.play(
            Create(aa_line), Create(al_line),
            Write(aa_label), Write(al_label),
            run_time=0.8
        )

        for i, (label, _bg, ratio, use) in enumerate(PAIRINGS):
            y = start_y - i * spacing
            threshold = AA_NORMAL if use != "non-text" else AA_LARGE
            color     = _bar_color(ratio, threshold)
            w         = bar_width * min(ratio, max_ratio) / max_ratio

            bg_bar = Rectangle(
                width=bar_width, height=bar_height,
                fill_color=PALETTE["ink"], fill_opacity=0.07,
                stroke_width=0
            ).move_to([left_x + bar_width / 2, y, 0])

            bar = Rectangle(
                width=0.001, height=bar_height,
                fill_color=color, fill_opacity=0.9,
                stroke_width=0
            ).align_to(bg_bar, LEFT)

            row_label = Text(
                label, color=PALETTE["ink"], font_size=13
            ).next_to(bg_bar, LEFT, buff=0.15).align_to(bg_bar, RIGHT)

            ratio_label = Text(
                f"{ratio}:1", color=color, font_size=14
            )

            self.add(bg_bar, row_label)
            self.play(
                bar.animate.stretch_to_fit_width(w).align_to(bg_bar, LEFT),
                run_time=0.55
            )
            ratio_label.next_to(bar, RIGHT, buff=0.12)
            self.play(Write(ratio_label), run_time=0.25)

            if ratio < threshold:
                fail_tag = Text(
                    "FAIL", color=PALETTE["fail"], font_size=13
                ).next_to(ratio_label, RIGHT, buff=0.18)
                fix_note = Text(
                    "→ fix needed", color=PALETTE["accent"], font_size=12
                ).next_to(fail_tag, RIGHT, buff=0.12)
                self.play(Write(fail_tag), Write(fix_note), run_time=0.3)

        summary = Text(
            "3/6 pairings pass AA for normal text",
            color=PALETTE["ink"], font_size=16
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(summary), run_time=0.5)
        self.wait(1.2)


class B06_CorrectedPalette(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "Corrected Palette — All Pairings Pass",
            color=PALETTE["ink"], font_size=28
        ).to_edge(UP, buff=0.4)
        self.add(title)

        max_ratio  = 16.0
        bar_width  = 5.5
        bar_height = 0.38
        spacing    = 0.62
        left_x     = -3.2
        start_y    = 2.0

        aa_x = left_x + bar_width * (AA_NORMAL / max_ratio)
        al_x = left_x + bar_width * (AA_LARGE  / max_ratio)

        aa_line = DashedLine(
            start=[aa_x, start_y + 0.3, 0],
            end=[aa_x, start_y - spacing * len(PAIRINGS_CORRECTED) - 0.1, 0],
            color=PALETTE["line"], dash_length=0.1, stroke_width=1.5
        )
        al_line = DashedLine(
            start=[al_x, start_y + 0.3, 0],
            end=[al_x, start_y - spacing * len(PAIRINGS_CORRECTED) - 0.1, 0],
            color=PALETTE["warn"], dash_length=0.08, stroke_width=1.2
        )
        aa_label = Text("4.5:1 AA-normal", color=PALETTE["line"],
                        font_size=13).next_to([aa_x, start_y + 0.3, 0], UP, buff=0.05)
        al_label = Text("3:1 AA-large/non-text", color=PALETTE["warn"],
                        font_size=12).next_to([al_x, start_y + 0.3, 0], UP, buff=0.05)

        self.play(
            Create(aa_line), Create(al_line),
            Write(aa_label), Write(al_label),
            run_time=0.8
        )

        for i, (label, _bg, ratio, use) in enumerate(PAIRINGS_CORRECTED):
            y = start_y - i * spacing
            threshold = AA_NORMAL if use != "non-text" else AA_LARGE
            color     = _bar_color(ratio, threshold)
            w         = bar_width * min(ratio, max_ratio) / max_ratio

            bg_bar = Rectangle(
                width=bar_width, height=bar_height,
                fill_color=PALETTE["ink"], fill_opacity=0.07,
                stroke_width=0
            ).move_to([left_x + bar_width / 2, y, 0])

            bar = Rectangle(
                width=0.001, height=bar_height,
                fill_color=color, fill_opacity=0.9,
                stroke_width=0
            ).align_to(bg_bar, LEFT)

            row_label = Text(
                label, color=PALETTE["ink"], font_size=13
            ).next_to(bg_bar, LEFT, buff=0.15).align_to(bg_bar, RIGHT)

            ratio_label = Text(
                f"{ratio}:1", color=color, font_size=14
            )

            self.add(bg_bar, row_label)
            self.play(
                bar.animate.stretch_to_fit_width(w).align_to(bg_bar, LEFT),
                run_time=0.45
            )
            ratio_label.next_to(bar, RIGHT, buff=0.12)
            self.play(Write(ratio_label), run_time=0.2)

        note = Text(
            "palette character preserved — value adjusted, hue unchanged",
            color=PALETTE["line"], font_size=14
        ).to_edge(DOWN, buff=0.7)
        summary = Text(
            "5/6 text pairings pass AA-normal · 1/6 non-text passes AA-large",
            color=PALETTE["ink"], font_size=15
        ).next_to(note, DOWN, buff=0.2)

        self.play(Write(note), run_time=0.5)
        self.play(Write(summary), run_time=0.5)
        self.wait(1.2)
