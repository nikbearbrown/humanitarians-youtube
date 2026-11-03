"""scenes.py — animated Manim scenes for the Banking Domain Data Analyst
Interview Prep whole-book trailer. One Scene per beat (B01..B07).
Newsprint brutalist palette, cream ground, one crimson accent — same
construction as reels/da-interview-trailer/scenes.py (the reference
whole-book-trailer this project clones).
Each scene is padded to its narration duration (dur = estimated_duration_s
from beat_sheet.json until Kokoro audio is locked, then actual_duration_s).
No LaTeX (Text/Pango only). Render each class to manim/<bid>.mp4, then compile.py.
"""
from manim import *

GROUND = "#F3EBDD"; INK = "#2F2A26"; RED = "#BF3339"; OCHRE = "#C8860E"; SEC = "#6B6357"
LEFT_X = -5.6

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

class BeatScene(Scene):
    spec = {}
    def construct(self):
        self.camera.background_color = GROUND
        spec = self.spec
        target = float(spec["dur"])
        elapsed = 0.0

        # ochre corner mark (top-left)
        mark = Rectangle(width=0.9, height=0.09, color=OCHRE, fill_color=OCHRE,
                         fill_opacity=1, stroke_width=0).to_edge(UP, buff=1.1)
        mark.to_edge(LEFT, buff=1.0)
        self.play(GrowFromEdge(mark, LEFT), run_time=0.5); elapsed += 0.5

        kind = spec["kind"]
        copy = spec["copy"]; sub = spec.get("sub", "")

        if kind in ("title", "statement"):
            fs = 60 if kind == "title" else 66
            head = Text(wrap(copy, 22), color=INK, weight=BOLD, font_size=fs,
                        line_spacing=0.9).move_to([0, 0.7, 0])
            head.to_edge(LEFT, buff=1.0)
            self.play(Write(head), run_time=1.6); elapsed += 1.6
            rule = Rectangle(width=1.7, height=0.06, color=RED, fill_color=RED,
                             fill_opacity=1, stroke_width=0)
            rule.next_to(head, DOWN, buff=0.35, aligned_edge=LEFT)
            self.play(GrowFromEdge(rule, LEFT), run_time=0.5); elapsed += 0.5
            subt = Text(wrap(sub, 34), color=SEC, font_size=30,
                        line_spacing=0.9).next_to(rule, DOWN, buff=0.35, aligned_edge=LEFT)
            self.play(FadeIn(subt, shift=UP * 0.2), run_time=0.8); elapsed += 0.8

        else:  # list — heading, then items build in one by one
            head = Text(copy, color=INK, weight=BOLD, font_size=58).move_to([0, 1.3, 0])
            head.to_edge(LEFT, buff=1.0)
            self.play(Write(head), run_time=1.3); elapsed += 1.3
            rule = Rectangle(width=1.5, height=0.06, color=RED, fill_color=RED,
                             fill_opacity=1, stroke_width=0)
            rule.next_to(head, DOWN, buff=0.3, aligned_edge=LEFT)
            self.play(GrowFromEdge(rule, LEFT), run_time=0.4); elapsed += 0.4
            items = spec["items"]
            # scale down font/spacing for longer lists so 6-item beats (B03)
            # still land inside the 16:9 frame the same way 3-5 item beats do
            n = len(items)
            item_fs = 34 if n <= 4 else (30 if n == 5 else 26)
            item_buff = 0.4 if n <= 4 else (0.34 if n == 5 else 0.28)
            texts = VGroup(*[Text(it, color=INK, font_size=item_fs) for it in items])
            texts.arrange(DOWN, aligned_edge=LEFT, buff=item_buff)
            texts.next_to(rule, DOWN, buff=0.5, aligned_edge=LEFT)
            dots = VGroup(*[Dot(color=RED, radius=0.07).next_to(t, LEFT, buff=0.3) for t in texts])
            self.play(LaggedStart(*[FadeIn(VGroup(d, t), shift=RIGHT * 0.3)
                                    for d, t in zip(dots, texts)],
                                  lag_ratio=0.5, run_time=2.4)); elapsed += 2.4

        pad = max(0.4, target - elapsed - 0.2)
        self.wait(pad)


class B01(BeatScene):
    spec = {"kind": "title", "dur": 16.85,
            "copy": "Banking Domain Data Analyst Interview Prep",
            "sub": "The full loop, end to end"}

class B02(BeatScene):
    spec = {"kind": "statement", "dur": 12.59,
            "copy": "You don't fail for lack of skill.",
            "sub": "You fail not knowing the bank's own vocabulary."}

class B03(BeatScene):
    spec = {"kind": "list", "dur": 16.85,
            "copy": "Six parts. One gap closed.",
            "items": ["Regulatory landscape", "Regulation, risk & governance",
                      "Modern banking data stack", "SQL & Python on bank data",
                      "Case, behavioral & systems rounds", "Day-of reference"]}

class B04(BeatScene):
    spec = {"kind": "statement", "dur": 11.5,
            "copy": "Each stage scores a different thing.",
            "sub": "Vocabulary first. Mechanics second."}

class B05(BeatScene):
    spec = {"kind": "list", "dur": 15.7,
            "copy": "Built for 2026",
            "items": ["LCR & CET1 after the regional-bank stress",
                      "CECL reserve modeling",
                      "AML & fraud-analytics growth",
                      "Responsible AI-tool fluency"]}

class B06(BeatScene):
    spec = {"kind": "statement", "dur": 11.67,
            "copy": "Every scenario is original.",
            "sub": "Invented banks. Real skills. No question banks."}

class B07(BeatScene):
    spec = {"kind": "title", "dur": 7.04,
            "copy": "15 chapters. Screen to offer.",
            "sub": "Banking Domain Data Analyst Interview Prep"}
