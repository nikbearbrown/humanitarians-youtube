"""
PORTRAIT (9:16) Manim scenes — Short. One Scene per beat, reflowed for a 4.5x8
portrait frame: centered lines, font sizes clearing the safe width, elements
chained with next_to() down the tall axis. Claude palette. |x|<=1.86, |y|<=3.3.
Generated from gen_vertical.py.
"""
from manim import *

BG = "#FAF9F5"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#8A8578"
TAG = 'THIS WEEK · RAG SYSTEM'

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
    return Paragraph(*wrap(text, n), alignment="center", line_spacing=1.0, **kw)

PANEL_W = 3.62

def _panel(h, y=-0.1):
    return RoundedRectangle(width=PANEL_W, height=h, corner_radius=0.28,
                            fill_color=INK, fill_opacity=0.10,
                            stroke_color=INK, stroke_width=3).move_to([0, y, 0])

def _chip(label, wrap_n, fs, fill=INK, op=0.12, tcol=INK, w=PANEL_W - 0.3, h=1.0):
    box = RoundedRectangle(width=w, height=h, corner_radius=0.18, fill_color=fill,
                           fill_opacity=op, stroke_color=fill, stroke_width=2.5)
    t = centered(label, wrap_n, color=tcol, weight=BOLD, font_size=fs).move_to(box.get_center())
    return VGroup(box, t)

class BeatScene916(Scene):
    spec = {}
    def construct(self):
        self.camera.background_color = BG
        spec = self.spec
        target = float(spec["dur"]); elapsed = 0.0
        kind = spec["kind"]; copy = spec["copy"]; sub = spec.get("sub", "")
        band = RoundedRectangle(width=PANEL_W, height=0.9, corner_radius=0.2,
                                fill_color=ACCENT, fill_opacity=0.14,
                                stroke_color=ACCENT, stroke_width=3).move_to([0, 3.0, 0])
        tag = Text(TAG, color=INK, font_size=24, weight="BOLD").move_to(band.get_center())
        self.play(GrowFromCenter(band), FadeIn(tag), run_time=0.6); elapsed += 0.6
        if kind in ("title", "statement"):
            panel = _panel(4.9, y=-0.35)
            self.play(FadeIn(panel), run_time=0.5); elapsed += 0.5
            fs = 46 if kind == "title" else 44
            head = centered(copy, 15, color=INK, weight=BOLD, font_size=fs).move_to([0, 0.75, 0])
            self.play(Write(head), run_time=1.4); elapsed += 1.4
            rule = Rectangle(width=1.4, height=0.07, color=ACCENT, fill_color=ACCENT,
                             fill_opacity=1, stroke_width=0).next_to(head, DOWN, buff=0.55)
            self.play(GrowFromCenter(rule), run_time=0.4); elapsed += 0.4
            if sub:
                subt = _chip(sub, 22, 30, fill=INK, op=0.10, tcol=INK, h=1.7)
                subt.next_to(rule, DOWN, buff=0.55)
                self.play(FadeIn(subt, shift=UP * 0.2), run_time=0.8); elapsed += 0.8
        else:
            items = spec["items"]; n = len(items)
            panel = _panel(5.6, y=-0.35)
            self.play(FadeIn(panel), run_time=0.5); elapsed += 0.5
            head = centered(copy, 16, color=INK, weight=BOLD, font_size=40).move_to([0, 1.95, 0])
            self.play(Write(head), run_time=1.1); elapsed += 1.1
            if n <= 3:
                item_fs, wrap_n, ch_h, buff = 28, 24, 1.15, 0.32
            elif n == 4:
                item_fs, wrap_n, ch_h, buff = 25, 26, 0.98, 0.28
            else:
                item_fs, wrap_n, ch_h, buff = 21, 32, 0.82, 0.24
            chips = VGroup(*[_chip(it, wrap_n, item_fs, fill=ACCENT, op=0.16, h=ch_h) for it in items])
            chips.arrange(DOWN, buff=buff).next_to(head, DOWN, buff=0.5)
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in chips],
                                  lag_ratio=0.5, run_time=2.4)); elapsed += 2.4
            foot = spec.get("foot", "")
            if foot:
                ft = centered(foot, 26, color=INK, weight=BOLD, font_size=28)
                ft.next_to(chips, DOWN, buff=0.4)
                self.play(FadeIn(ft, shift=UP * 0.2), run_time=0.6); elapsed += 0.6
        if spec.get("handle"):
            h = Text("@HumanitariansAI", color=INK, font_size=26, weight="BOLD").move_to([0, -3.05, 0])
            self.play(FadeIn(h), run_time=0.5); elapsed += 0.5
        self.wait(max(0.4, target - elapsed - 0.2))

class B01(BeatScene916):
    spec = {'kind': 'title', 'dur': 9.81, 'copy': 'The RAG System I Built', 'sub': '600 disclosures, measured end to end', 'handle': True}

class B02(BeatScene916):
    spec = {'kind': 'statement', 'dur': 10.54, 'copy': 'Chunking moved quality most.', 'sub': 'naive → recursive: MRR 0.833 → 1.000'}

class B03(BeatScene916):
    spec = {'kind': 'list', 'dur': 10.45, 'copy': 'Three surprises', 'items': ['384-dim beat 768-dim (88% vs 76%)', 'hit rate saturates — MRR still discriminates', 'vector search is 0.2% of latency']}

class B04(BeatScene916):
    spec = {'kind': 'statement', 'dur': 8.96, 'copy': 'Hybrid beats either half.', 'sub': 'dense + BM25, fused by rank: MRR 0.655 → 0.810'}

class B05(BeatScene916):
    spec = {'kind': 'list', 'dur': 8.68, 'copy': 'Where the time goes', 'items': ['search — 4 ms', 'rerank — 301 ms', 'the model — 1288 ms'], 'foot': 'cache first, not vector math'}

class B06(BeatScene916):
    spec = {'kind': 'statement', 'dur': 5.82, 'copy': 'Measure before you optimise.', 'sub': 'the surprises are where the wins are'}

class B07(BeatScene916):
    spec = {'kind': 'title', 'dur': 7.25, 'copy': 'Measured, not guessed.', 'sub': 'full cut on the channel', 'handle': True}
