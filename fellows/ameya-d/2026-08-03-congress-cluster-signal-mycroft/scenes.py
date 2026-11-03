"""
Manim scenes for congress-cluster-signal (cli-explainer, Claude skin).

  B01_StockAct       — the setup: STOCK Act -> public dataset -> the question
  B04_AggregateAlpha — run 1: congressional BUY raw vs SPY, the +0.13% residual
  B07_TierTable      — run 2: alpha + win rate by signal tier (the result)
  B08_Recap          — the lesson: what carries the edge, what doesn't

All numbers sourced in SOURCES.md (RESEARCH_REPORT.md + the pipeline code).
Claude FIDELITY palette — never retint. Coordinates stay inside SAFE (+-6.3, +-3.4).
"""

from manim import *

# Claude fidelity palette (tokens/claude.ts)
BG     = "#FAF9F5"
INK    = "#3D3929"
ACCENT = "#D97757"   # terracotta — the one accent
GOOD   = "#4A7C59"   # positive alpha / pass
BAD    = "#C0392B"   # negative alpha / fail
MUTE   = "#8A8372"   # secondary ink
LINE   = "#C9C2B4"


def _bg(scene):
    scene.camera.background_color = BG


# Narration lengths (measured, mp3/timings.json) — the audio is the master clock,
# so each scene fills to ~its beat length instead of ending early and forcing the
# compiler into extreme slow-motion.
TARGET = {
    "B01_StockAct": 31.3,
    "B04_AggregateAlpha": 21.7,
    "B07_TierTable": 30.8,
    "B08_Recap": 26.8,
}


def _fill(scene, key, tail=1.0):
    """Hold the final composition until the scene reaches its narration length."""
    try:
        elapsed = scene.renderer.time
    except Exception:
        elapsed = 0.0
    remaining = TARGET.get(key, 0.0) - elapsed
    scene.wait(max(tail, remaining))


class B01_StockAct(Scene):
    def construct(self):
        _bg(self)

        title = Text("The STOCK Act, 2012", color=INK, font_size=60, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        sub = Text("disclose every trade within 45 days",
                   color=MUTE, font_size=34).next_to(title, DOWN, buff=0.25)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.7)
        self.play(Write(sub), run_time=0.6)
        self.wait(3.0)

        # arrow: a deterrence law -> a public dataset
        law = Text("a law to deter insider trading", color=INK, font_size=32)
        arrow = Text("becomes", color=ACCENT, font_size=28, slant="ITALIC")
        data = Text("a public dataset of what powerful people buy",
                    color=INK, font_size=32)
        chain = VGroup(law, arrow, data).arrange(DOWN, buff=0.4).move_to([0, 1.15, 0])
        self.play(Write(law), run_time=0.6)
        self.play(FadeIn(arrow), run_time=0.5)
        self.play(Write(data), run_time=0.6)
        self.wait(3.5)

        # stat cards
        cards = VGroup()
        for big, small in [("13,877", "trades"),
                           ("108", "members"),
                           ("2023–26", "3 yrs of filings")]:
            n = Text(big, color=ACCENT, font_size=64, weight="BOLD")
            l = Text(small, color=MUTE, font_size=28)
            box = VGroup(n, l).arrange(DOWN, buff=0.15)
            cards.add(box)
        cards.arrange(RIGHT, buff=1.3).move_to([0, -1.35, 0])
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.15), run_time=0.5)
            self.wait(1.3)
        self.wait(3.0)

        q = Text("Follow every buy — beat the index?",
                 color=INK, font_size=40, weight="BOLD").move_to([0, -3.0, 0])
        underline = Line([-4.7, -3.4, 0], [4.7, -3.4, 0],
                         color=ACCENT, stroke_width=4)
        self.play(Write(q), run_time=0.9)
        self.play(Create(underline), run_time=0.5)
        _fill(self, "B01_StockAct")


class B04_AggregateAlpha(Scene):
    def construct(self):
        _bg(self)

        title = Text("Run 1 — the aggregate", color=INK, font_size=40, weight="BOLD")
        title.to_edge(UP, buff=0.55)
        n = Text("5,162 priced BUY events", color=MUTE, font_size=24)
        n.next_to(title, DOWN, buff=0.18)
        self.play(FadeIn(title, shift=DOWN * 0.2), Write(n), run_time=0.8)

        # two bars, near-identical: raw +2.23 vs SPY +2.10
        base_y = -2.2
        scale = 0.95   # units per % point
        raw_v, spy_v = 2.23, 2.10

        def bar(x, val, color, label, pct):
            h = val * scale
            rect = Rectangle(width=1.4, height=h, fill_color=color,
                             fill_opacity=0.9, stroke_width=0)
            rect.move_to([x, base_y + h / 2, 0])
            cap = Text(label, color=INK, font_size=24).next_to(
                [x, base_y, 0], DOWN, buff=0.2)
            v = Text(pct, color=color, font_size=26, weight="BOLD").next_to(rect, UP, buff=0.15)
            return rect, cap, v

        raw_rect, raw_cap, raw_v_t = bar(-2.6, raw_v, INK, "Congress BUY", "+2.23%")
        spy_rect, spy_cap, spy_v_t = bar(0.2, spy_v, MUTE, "SPY (same windows)", "+2.10%")

        self.add(raw_cap, spy_cap)
        self.play(GrowFromEdge(raw_rect, DOWN), run_time=0.8)
        self.play(Write(raw_v_t), run_time=0.4)
        self.wait(2.5)
        self.play(GrowFromEdge(spy_rect, DOWN), run_time=0.8)
        self.play(Write(spy_v_t), run_time=0.4)
        self.wait(2.5)

        # the residual = alpha
        brace = Text("alpha = +0.13%", color=ACCENT, font_size=30, weight="BOLD")
        brace.move_to([3.9, base_y + 1.4, 0])
        sliver = Rectangle(width=0.5, height=0.13 * scale * 4, fill_color=ACCENT,
                           fill_opacity=1.0, stroke_width=0)
        sliver.move_to([3.9, base_y + 0.25, 0])
        self.play(FadeIn(sliver, scale=1.2), Write(brace), run_time=0.8)
        self.wait(2.5)

        verdict = Text("Congress rides the market.", color=INK,
                       font_size=30, slant="ITALIC").move_to([0, base_y - 0.95, 0])
        sell = Text("(SELL alpha: -0.01%)", color=MUTE, font_size=20).next_to(
            verdict, DOWN, buff=0.15)
        self.play(Write(verdict), run_time=0.8)
        self.play(FadeIn(sell), run_time=0.4)
        _fill(self, "B04_AggregateAlpha")


class B07_TierTable(Scene):
    def construct(self):
        _bg(self)

        title = Text("Run 2 — by signal tier", color=INK, font_size=52, weight="BOLD")
        title.to_edge(UP, buff=0.45)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.6)

        # column headers
        cols = ["TIER", "n", "alpha", "win%"]
        xs = [-4.6, -1.6, 1.1, 4.0]
        header = VGroup(*[
            Text(c, color=MUTE, font_size=30, weight="BOLD").move_to([x, 2.35, 0])
            for c, x in zip(cols, xs)])
        self.play(FadeIn(header), run_time=0.4)
        hline = Line([-6.0, 2.0, 0], [5.4, 2.0, 0], color=LINE, stroke_width=2.5)
        self.play(Create(hline), run_time=0.3)

        rows = [
            ("STRONG", "815",   "+0.23%", "50.3%", GOOD, True),
            ("WATCH",  "1,212", "+0.54%", "50.6%", GOOD, True),
            ("SKIP",   "132",   "-0.04%", "44.7%", BAD,  False),
            ("SOLO",   "3,003", "-0.05%", "44.9%", BAD,  False),
        ]
        y = 1.4
        clustered_boxes = []
        for i, (name, nn, a, w, col, clustered) in enumerate(rows):
            # colored swatch — a distinct non-text shape per row (sized by |alpha|)
            mag = 0.24 + i * 0.08
            swatch = Rectangle(width=mag, height=0.46, fill_color=col,
                               fill_opacity=0.95, stroke_width=0).move_to([-5.9, y, 0])
            cells = [
                Text(name, color=INK, font_size=34, weight="BOLD").move_to([xs[0], y, 0]),
                Text(nn,   color=INK, font_size=32).move_to([xs[1], y, 0]),
                Text(a,    color=col, font_size=34, weight="BOLD").move_to([xs[2], y, 0]),
                Text(w,    color=col, font_size=34, weight="BOLD").move_to([xs[3], y, 0]),
            ]
            self.play(GrowFromEdge(swatch, LEFT),
                      *[FadeIn(c, shift=RIGHT * 0.15) for c in cells], run_time=0.5)
            self.wait(2.6)
            if clustered:
                box = SurroundingRectangle(VGroup(swatch, *cells), color=ACCENT,
                                           buff=0.16, stroke_width=3,
                                           corner_radius=0.08)
                clustered_boxes.append(box)
            y -= 0.88

        if clustered_boxes:
            self.play(*[Create(b) for b in clustered_boxes], run_time=0.8)
            self.wait(2.5)

        note = Text("~5-point win gap across 5,162 events",
                    color=INK, font_size=34, weight="BOLD").move_to([0, -2.75, 0])
        money = Text("$10k in STRONG → $10,247   vs   $10,224 in SPY",
                     color=MUTE, font_size=28).next_to(note, DOWN, buff=0.22)
        self.play(Write(note), run_time=0.8)
        self.play(FadeIn(money), run_time=0.5)
        _fill(self, "B07_TierTable")


class B08_Recap(Scene):
    def construct(self):
        _bg(self)

        title = Text("What the build showed", color=INK, font_size=52, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.6)

        rows = [
            (True,  "Cluster membership carries the edge",
                    "independent members converge on one ticker"),
            (False, "The conviction score does NOT rank",
                    "WATCH +0.54% beat STRONG +0.23% — not monotone"),
            (False, "Small samples lie",
                    "64 members looked inverted; stable only at 108"),
        ]
        y = 1.7
        for i, (ok, head, tail) in enumerate(rows):
            col = GOOD if ok else BAD
            # a distinct non-text glyph per verdict: check = up-triangle, cross = square
            glyph = (Triangle(color=col, fill_color=col, fill_opacity=1.0,
                              stroke_width=0).scale(0.38)
                     if ok else
                     Square(side_length=0.56, color=col, fill_color=col,
                            fill_opacity=1.0, stroke_width=0).rotate(PI / 4))
            glyph.move_to([-5.5, y, 0])
            mark = Text("PASS" if ok else "FAIL", color=col,
                        font_size=28, weight="BOLD").move_to([-4.35, y, 0])
            h = Text(head, color=INK, font_size=36, weight="BOLD")
            t = Text(tail, color=MUTE, font_size=27)
            txt = VGroup(h, t).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
            txt.next_to(mark, RIGHT, buff=0.45)
            self.play(GrowFromCenter(glyph), FadeIn(mark, scale=1.2), run_time=0.4)
            self.play(Write(h), run_time=0.5)
            self.play(FadeIn(t), run_time=0.4)
            self.wait(3.4)
            y -= 1.5

        closing = Text("A noise filter — not a profit engine.",
                       color=ACCENT, font_size=42, weight="BOLD").move_to([0, -2.8, 0])
        note = Text("research & education only — not financial advice",
                    color=MUTE, font_size=26, slant="ITALIC").next_to(
            closing, DOWN, buff=0.18)
        self.play(Write(closing), run_time=0.9)
        self.play(FadeIn(note), run_time=0.5)
        _fill(self, "B08_Recap")
