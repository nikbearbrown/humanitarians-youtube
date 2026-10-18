"""scenes.py — PORTRAIT (9:16) Manim scenes for the Banking Domain Data
Analyst Interview Prep whole-book trailer. One Scene per beat (B01..B07),
same content/copy as ../scenes.py, but reflowed for a 4.5x8 portrait frame
per skills/make/sketch-explainer/reference/reframing-16x9-to-9x16.md:
every line is centered (never left-ragged), font sizes are picked so the
widest line clears the portrait safe width, and elements are chained with
next_to() down the tall axis (never a fixed landscape y-coordinate) so the
layout is correct regardless of how many lines any given beat wraps to.
No LaTeX (Text/Pango only).
"""
from manim import *

GROUND = "#F3EBDD"; INK = "#2F2A26"; RED = "#BF3339"; OCHRE = "#C8860E"; SEC = "#6B6357"

# matches qc/manim_layout_audit.py's --portrait safe box (half-extents 1.95 x 3.4)
TOP_Y = 3.15

def wrap(text, n):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= n:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


def centered(text, n, **kw):
    """Wrap text to n chars/line and return a Paragraph with every line
    x-centered (Text with an embedded '\\n' only centers the whole block,
    leaving lines left-ragged inside it — wrong for a portrait column)."""
    lines = wrap(text, n)
    return Paragraph(*lines, alignment="center", line_spacing=1.0, **kw)


class BeatScene916(Scene):
    spec = {}
    def construct(self):
        self.camera.background_color = GROUND
        spec = self.spec
        target = float(spec["dur"])
        elapsed = 0.0

        # ochre mark: centered top bar (was a top-left corner mark in landscape —
        # recomputed for the portrait band, never a reused landscape coordinate)
        mark = Rectangle(width=0.6, height=0.07, color=OCHRE, fill_color=OCHRE,
                         fill_opacity=1, stroke_width=0).move_to([0, TOP_Y, 0])
        self.play(GrowFromCenter(mark), run_time=0.5); elapsed += 0.5

        kind = spec["kind"]
        copy = spec["copy"]; sub = spec.get("sub", "")

        if kind in ("title", "statement"):
            fs, wrap_n = (34, 15) if kind == "title" else (36, 16)
            head = centered(copy, wrap_n, color=INK, weight=BOLD, font_size=fs)
            head.next_to(mark, DOWN, buff=0.8)
            self.play(Write(head), run_time=1.6); elapsed += 1.6
            rule = Rectangle(width=1.2, height=0.055, color=RED, fill_color=RED,
                             fill_opacity=1, stroke_width=0)
            rule.next_to(head, DOWN, buff=0.5)
            self.play(GrowFromCenter(rule), run_time=0.5); elapsed += 0.5
            subt = centered(sub, 20, color=SEC, font_size=28)
            subt.next_to(rule, DOWN, buff=0.55)
            self.play(FadeIn(subt, shift=UP * 0.2), run_time=0.8); elapsed += 0.8

        else:  # list — heading, then items build in one by one, stacked & centered
            head = centered(copy, 16, color=INK, weight=BOLD, font_size=32)
            head.next_to(mark, DOWN, buff=0.7)
            self.play(Write(head), run_time=1.3); elapsed += 1.3
            rule = Rectangle(width=1.0, height=0.05, color=RED, fill_color=RED,
                             fill_opacity=1, stroke_width=0)
            rule.next_to(head, DOWN, buff=0.45)
            self.play(GrowFromCenter(rule), run_time=0.4); elapsed += 0.4
            items = spec["items"]
            n = len(items)
            # font/wrap picked so the widest line clears the portrait safe width
            # (measured directly against Text.width — see PLAN notes) rather than
            # shrinking the landscape tiering to fit a narrower box
            if n <= 4:
                item_fs, wrap_n, item_buff = 24, 21, 0.5
            elif n == 5:
                item_fs, wrap_n, item_buff = 20, 26, 0.4
            else:
                item_fs, wrap_n, item_buff = 16, 48, 0.34
            rows = VGroup()
            for it in items:
                txt = centered(it, wrap_n, color=INK, font_size=item_fs)
                dot = Dot(color=RED, radius=0.06).next_to(txt, LEFT, buff=0.18)
                rows.add(VGroup(dot, txt))
            rows.arrange(DOWN, buff=item_buff)
            rows.next_to(rule, DOWN, buff=0.6)
            self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.2) for r in rows],
                                  lag_ratio=0.5, run_time=2.4)); elapsed += 2.4

        pad = max(0.4, target - elapsed - 0.2)
        self.wait(pad)


class B01(BeatScene916):
    spec = {"kind": "title", "dur": 16.85,
            "copy": "Banking Domain Data Analyst Interview Prep",
            "sub": "The full loop, end to end"}

class B02(BeatScene916):
    spec = {"kind": "statement", "dur": 12.59,
            "copy": "You don't fail for lack of skill.",
            "sub": "You fail not knowing the bank's own vocabulary."}

class B03(BeatScene916):
    spec = {"kind": "list", "dur": 16.85,
            "copy": "Six parts. One gap closed.",
            "items": ["Regulatory landscape", "Regulation, risk & governance",
                      "Modern banking data stack", "SQL & Python on bank data",
                      "Case, behavioral & systems rounds", "Day-of reference"]}

class B04(BeatScene916):
    spec = {"kind": "statement", "dur": 11.5,
            "copy": "Each stage scores a different thing.",
            "sub": "Vocabulary first. Mechanics second."}

class B05(BeatScene916):
    spec = {"kind": "list", "dur": 15.7,
            "copy": "Built for 2026",
            "items": ["LCR & CET1 after the regional-bank stress",
                      "CECL reserve modeling",
                      "AML & fraud-analytics growth",
                      "Responsible AI-tool fluency"]}

class B06(BeatScene916):
    spec = {"kind": "statement", "dur": 11.67,
            "copy": "Every scenario is original.",
            "sub": "Invented banks. Real skills. No question banks."}

class B07(BeatScene916):
    spec = {"kind": "title", "dur": 7.04,
            "copy": "15 chapters. Screen to offer.",
            "sub": "Banking Domain Data Analyst Interview Prep"}
