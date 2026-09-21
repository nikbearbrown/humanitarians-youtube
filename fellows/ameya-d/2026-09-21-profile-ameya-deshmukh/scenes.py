"""
Manim scenes for profile-ameya-deshmukh (ai-explainer `profile` modifier).
Claude fidelity palette. Evidence beats are Ameya's PROJECTS as illustrations.
Every figure verifiable from his resume + repos. SAFE |x|<=6.0, |y|<=3.3.
"""
from manim import *

BG = "#FAF9F5"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#8A8578"
GOOD = "#4A7C59"; BAD = "#C0392B"; LINE = "#B8B0A0"

TARGET = {"B01_Idea": 17.81, "B02_RAG": 23.13, "B03_Boehringer": 20.33, "B04_Signal": 22.78, "B05_Teaching": 21.01, "B06_Stack": 17.22, "B08_Credit": 14.04}


def _bg(s): s.camera.background_color = BG


def _fill(s, key, tail=1.0):
    try:
        elapsed = s.renderer.time
    except Exception:
        elapsed = 0.0
    s.wait(max(tail, TARGET.get(key, 0.0) - elapsed))


def _title(txt, size=46):
    return Text(txt, color=INK, font_size=size, weight="BOLD").to_edge(UP, buff=0.5)


def _chip(label, w=2.5, h=1.05, fill=INK, op=0.10, fs=30, tcol=INK, mono=False):
    box = RoundedRectangle(width=w, height=h, corner_radius=0.14, fill_color=fill,
                           fill_opacity=op, stroke_color=fill, stroke_width=3)
    t = Text(label, color=tcol, font_size=fs, weight="BOLD",
             font=("monospace" if mono else "sans-serif")).move_to(box.get_center())
    return VGroup(box, t)


class B01_Idea(Scene):
    def construct(self):
        _bg(self)
        name = Text("Ameya Deshmukh", color=INK, font_size=64, weight="BOLD").move_to([0, 2.2, 0])
        role = Text("AI / ML Engineer", color=ACCENT, font_size=34, weight="BOLD").next_to(name, DOWN, buff=0.3)
        sub = Text("MS, Northeastern  ·  Fellow, Humanitarians AI", color=MUTE, font_size=27).next_to(role, DOWN, buff=0.28)
        self.play(Write(name), run_time=1.0)
        self.play(FadeIn(role, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.5); self.wait(0.8)
        rule = Rectangle(width=2.2, height=0.06, color=ACCENT, fill_color=ACCENT, fill_opacity=1, stroke_width=0).move_to([0, -0.4, 0])
        self.play(GrowFromCenter(rule), run_time=0.4)
        thesis = Text("\"Measure, don't guess.\"", color=INK, font_size=46, weight="BOLD").move_to([0, -1.5, 0])
        self.play(Write(thesis), run_time=1.0); self.wait(0.6)
        self.play(Write(Text("the habit under everything he ships", color=MUTE, font_size=26, slant="ITALIC").move_to([0, -2.6, 0])), run_time=0.6)
        _fill(self, "B01_Idea")


class B02_RAG(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Production RAG — Measured"), shift=DOWN * 0.2), run_time=0.6)
        stages = ["chunk", "embed", "retrieve", "rerank"]
        chips = VGroup(*[_chip(s, w=2.2, h=0.85, fill=INK, op=0.10, fs=26) for s in stages])
        chips.arrange(RIGHT, buff=0.4).move_to([0, 1.5, 0])
        arrs = VGroup(*[Arrow(chips[i].get_right(), chips[i + 1].get_left(), color=ACCENT, stroke_width=4, buff=0.1) for i in range(3)])
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.1) for c in chips], lag_ratio=0.25, run_time=1.0),
                  LaggedStart(*[GrowArrow(a) for a in arrs], lag_ratio=0.25, run_time=0.9))
        base = RoundedRectangle(width=3.4, height=0.8, corner_radius=0.1, fill_color=MUTE, fill_opacity=0.8, stroke_width=0).move_to([-2.0, -0.6, 0])
        bt = Text("MRR 0.66", color=BG, font_size=28, weight="BOLD").move_to(base.get_center())
        self.play(GrowFromEdge(base, LEFT), FadeIn(bt), run_time=0.6); self.wait(0.4)
        up = RoundedRectangle(width=4.6, height=0.8, corner_radius=0.1, fill_color=ACCENT, fill_opacity=0.9, stroke_width=0).move_to([-1.4, -1.7, 0])
        ut = Text("MRR 0.81", color=BG, font_size=28, weight="BOLD").move_to(up.get_center())
        self.play(GrowFromEdge(up, LEFT), FadeIn(ut), run_time=0.7)
        self.play(Write(Text("600 docs · a number that moved, not a feeling", color=INK,
                             font_size=26, weight="BOLD").move_to([0, -3.0, 0])), run_time=0.7)
        _fill(self, "B02_RAG")


class B03_Boehringer(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Boehringer Ingelheim — Data Scientist"), shift=DOWN * 0.2), run_time=0.6)
        a = _chip("2M+ records\nconnected", w=4.4, h=1.6, fill=INK, op=0.09, fs=30).move_to([-3.1, 0.8, 0])
        b = _chip("data quality\n+40%", w=4.4, h=1.6, fill=GOOD, op=0.13, fs=30, tcol=GOOD).move_to([3.1, 0.8, 0])
        self.play(FadeIn(a, shift=RIGHT * 0.1), run_time=0.6); self.wait(0.5)
        self.play(GrowArrow(Arrow(a.get_right(), b.get_left(), color=ACCENT, stroke_width=5, buff=0.15)), FadeIn(b), run_time=0.7); self.wait(0.6)
        ml = _chip("LangChain multi-agent system on the healthcare data", w=9.4, h=1.1, fill=ACCENT, op=0.12, fs=27).move_to([0, -1.3, 0])
        self.play(FadeIn(ml, shift=UP * 0.1), run_time=0.7); self.wait(0.6)
        self.play(Write(Text("big, regulated data — made usable, then made to reason", color=MUTE,
                             font_size=25, slant="ITALIC").move_to([0, -3.0, 0])), run_time=0.7)
        _fill(self, "B03_Boehringer")


class B04_Signal(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Congressional Signal — Honest"), shift=DOWN * 0.2), run_time=0.6)
        steps = ["market-adjust\nevery trade", "significance\ntest", "backtest\nthe signal"]
        chips = VGroup(*[_chip(s, w=3.0, h=1.4, fill=INK, op=0.10, fs=25) for s in steps])
        chips.arrange(RIGHT, buff=0.5).move_to([0, 1.2, 0])
        for i, c in enumerate(chips):
            self.play(FadeIn(c, shift=RIGHT * 0.1), run_time=0.45)
            if i < len(chips) - 1:
                self.play(GrowArrow(Arrow(chips[i].get_right(), chips[i + 1].get_left(), color=ACCENT, stroke_width=4, buff=0.1)), run_time=0.25)
        self.play(Write(Text("finding: no individual edge — only clusters show a small, real one", color=INK,
                             font_size=25, weight="BOLD").move_to([0, -1.0, 0])), run_time=0.8)
        self.wait(0.5)
        self.play(Write(Text("he let the data say no", color=ACCENT, font_size=34, weight="BOLD").move_to([0, -2.4, 0])), run_time=0.7)
        _fill(self, "B04_Signal")


class B05_Teaching(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("And He Teaches It"), shift=DOWN * 0.2), run_time=0.6)
        eps = ["First Principles", "Reranking", "Vector Search", "LLM Inference",
               "Quantization", "Caching", "Chunking", "Tokenization"]
        cards = VGroup(*[_chip(e, w=4.3, h=0.85, fill=INK, op=0.09, fs=25) for e in eps])
        cards.arrange_in_grid(rows=4, cols=2, buff=(0.5, 0.3)).move_to([0, -0.1, 0])
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in cards], lag_ratio=0.12, run_time=2.0))
        self.play(Write(Text("a full RAG explainer series · every number traceable", color=ACCENT,
                             font_size=26, weight="BOLD").move_to([0, -3.0, 0])), run_time=0.8)
        _fill(self, "B05_Teaching")


class B06_Stack(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("The Toolkit"), shift=DOWN * 0.2), run_time=0.6)
        skills = ["Python", "PyTorch", "RAG", "LangChain", "multi-agent", "SQL & pipelines"]
        chips = VGroup(*[_chip(s, w=3.5, h=1.0, fill=ACCENT, op=0.12, fs=28) for s in skills])
        chips.arrange_in_grid(rows=2, cols=3, buff=(0.5, 0.5)).move_to([0, 0.4, 0])
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in chips], lag_ratio=0.12, run_time=1.6))
        self.play(Write(Text("baseline  →  change one thing  →  measure whether it helped", color=INK,
                             font_size=28, weight="BOLD").move_to([0, -2.6, 0])), run_time=0.8)
        _fill(self, "B06_Stack")


class B08_Credit(Scene):
    def construct(self):
        _bg(self)
        panel = RoundedRectangle(width=10.4, height=5.0, corner_radius=0.2, fill_color=INK,
                                 fill_opacity=0.05, stroke_color=INK, stroke_width=3).move_to([0, 0.1, 0])
        self.play(FadeIn(panel), run_time=0.5)
        name = Text("Ameya Deshmukh", color=INK, font_size=52, weight="BOLD").move_to([0, 1.6, 0])
        role = Text("AI / ML Engineer  ·  Humanitarians AI  ·  MS Northeastern", color=MUTE, font_size=26).next_to(name, DOWN, buff=0.3)
        self.play(Write(name), run_time=0.8)
        self.play(FadeIn(role), run_time=0.5); self.wait(0.5)
        rule = Rectangle(width=2.0, height=0.05, color=ACCENT, fill_color=ACCENT, fill_opacity=1, stroke_width=0).next_to(role, DOWN, buff=0.4)
        self.play(GrowFromCenter(rule), run_time=0.3)
        li = VGroup(Text("LinkedIn", color=ACCENT, font_size=26, weight="BOLD"),
                    Text("linkedin.com/in/ameya-deshmukh-179945a4", color=INK, font_size=26, font="monospace")).arrange(RIGHT, buff=0.35)
        gh = VGroup(Text("GitHub", color=ACCENT, font_size=26, weight="BOLD"),
                    Text("github.com/Ameya-Deshmukh26", color=INK, font_size=26, font="monospace")).arrange(RIGHT, buff=0.35)
        links = VGroup(li, gh).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to([0, -1.4, 0])
        for l in links:
            self.play(FadeIn(l, shift=RIGHT * 0.1), run_time=0.6); self.wait(0.5)
        _fill(self, "B08_Credit")
