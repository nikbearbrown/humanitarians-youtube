"""
PORTRAIT (9:16) Manim scenes for the rag-eval-production Short.
Claude palette. |x|<=1.86, |y|<=3.3. Facts per ../FACTCHECK.md.
"""
from manim import *

BG = "#FAF9F5"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#8A8578"
TAG = "RAG SERIES · EVAL IN PRODUCTION"
PANEL_W = 3.62


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


def _panel(h, y=-0.1):
    return RoundedRectangle(width=PANEL_W, height=h, corner_radius=0.28, fill_color=INK,
                           fill_opacity=0.10, stroke_color=INK, stroke_width=3).move_to([0, y, 0])


def _chip(label, wrap_n, fs, fill=INK, op=0.12, tcol=INK, w=PANEL_W - 0.3, h=1.0):
    box = RoundedRectangle(width=w, height=h, corner_radius=0.18, fill_color=fill,
                           fill_opacity=op, stroke_color=fill, stroke_width=2.5)
    t = centered(label, wrap_n, color=tcol, weight=BOLD, font_size=fs).move_to(box.get_center())
    return VGroup(box, t)


class BeatScene916(Scene):
    spec = {}

    def construct(self):
        self.camera.background_color = BG
        spec = self.spec; target = float(spec["dur"]); elapsed = 0.0
        band = RoundedRectangle(width=PANEL_W, height=0.9, corner_radius=0.2, fill_color=ACCENT,
                                fill_opacity=0.14, stroke_color=ACCENT, stroke_width=3).move_to([0, 3.0, 0])
        tag = Text(TAG, color=INK, font_size=21, weight="BOLD").move_to(band.get_center())
        self.play(GrowFromCenter(band), FadeIn(tag), run_time=0.6); elapsed += 0.6
        kind = spec["kind"]; copy = spec["copy"]; sub = spec.get("sub", "")
        if kind in ("title", "statement"):
            panel = _panel(4.9, y=-0.35); self.play(FadeIn(panel), run_time=0.5); elapsed += 0.5
            head = centered(copy, 15, color=INK, weight=BOLD, font_size=46 if kind == "title" else 44).move_to([0, 0.75, 0])
            self.play(Write(head), run_time=1.4); elapsed += 1.4
            rule = Rectangle(width=1.4, height=0.07, color=ACCENT, fill_color=ACCENT, fill_opacity=1, stroke_width=0).next_to(head, DOWN, buff=0.55)
            self.play(GrowFromCenter(rule), run_time=0.4); elapsed += 0.4
            if sub:
                subt = _chip(sub, 22, 29, fill=INK, op=0.10, h=1.8).next_to(rule, DOWN, buff=0.55)
                self.play(FadeIn(subt, shift=UP * 0.2), run_time=0.8); elapsed += 0.8
        else:
            items = spec["items"]; panel = _panel(5.6, y=-0.35); self.play(FadeIn(panel), run_time=0.5); elapsed += 0.5
            head = centered(copy, 16, color=INK, weight=BOLD, font_size=38).move_to([0, 1.95, 0])
            self.play(Write(head), run_time=1.1); elapsed += 1.1
            chips = VGroup(*[_chip(it, 26, 23, fill=ACCENT, op=0.16, h=0.98) for it in items])
            chips.arrange(DOWN, buff=0.3).next_to(head, DOWN, buff=0.5)
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in chips], lag_ratio=0.5, run_time=2.4)); elapsed += 2.4
        if spec.get("handle"):
            self.play(FadeIn(Text("@HumanitariansAI", color=INK, font_size=26, weight="BOLD").move_to([0, -3.05, 0])), run_time=0.5); elapsed += 0.5
        self.wait(max(0.4, target - elapsed - 0.2))


class B01(BeatScene916):
    spec = {"kind": "title", "dur": 7.55, "copy": "Eval in Production", "sub": "offline vs online", "handle": True}

class B02(BeatScene916):
    spec = {"kind": "statement", "dur": 7.51, "copy": "Two different jobs.", "sub": "offline: known answers · online: no labels"}

class B03(BeatScene916):
    spec = {"kind": "statement", "dur": 8.21, "copy": "Offline = a golden set.", "sub": "score hit@k / MRR / faithfulness before deploy"}

class B04(BeatScene916):
    spec = {"kind": "statement", "dur": 9.13, "copy": "Gate the deploy.", "sub": "MRR drops in CI → release blocked"}

class B05(BeatScene916):
    spec = {"kind": "list", "dur": 7.45, "copy": "Online: watch proxies",
            "items": ["score distribution (mean top-1 ↓)", "refusal rate", "latency + cost"]}

class B06(BeatScene916):
    spec = {"kind": "statement", "dur": 8.21, "copy": "The trace says why.", "sub": "chunks · prompt · latency · cost, per request"}

class B07(BeatScene916):
    spec = {"kind": "title", "dur": 4.29, "copy": "Gate before, watch after.", "sub": "@HumanitariansAI", "handle": True}
