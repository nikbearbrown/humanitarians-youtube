"""
Manim scenes for rag-eval-production (RAG series — offline vs online eval + tracing).
Claude fidelity palette. Grounded in PRODUCTION_NOTES.md §6/§7. SAFE |x|<=6.0, |y|<=3.3.
"""
from manim import *

BG = "#FAF9F5"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#8A8578"
GOOD = "#4A7C59"; BAD = "#C0392B"; LINE = "#B8B0A0"

TARGET = {"B01_TwoJobs": 17.41, "B02_Offline": 18.39, "B03_CIGate": 18.28, "B04_OnlineProblem": 17.75, "B05_Proxies": 19.16, "B06_Trace": 18.13, "B08_Together": 19.11}


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


class B01_TwoJobs(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Two Different Jobs"), shift=DOWN * 0.2), run_time=0.6)

        def panel(x, head, lines, col):
            box = RoundedRectangle(width=5.4, height=3.1, corner_radius=0.16, fill_color=col,
                                   fill_opacity=0.10, stroke_color=col, stroke_width=3).move_to([x, 0.0, 0])
            h = Text(head, color=col, font_size=32, weight="BOLD").move_to([x, 1.1, 0])
            body = VGroup(*[Text(l, color=INK, font_size=24) for l in lines]).arrange(DOWN, buff=0.3).move_to([x, -0.3, 0])
            return VGroup(box, h, body)
        left = panel(-3.1, "OFFLINE", ["before deploy", "known answers", "measure correctness"], INK)
        right = panel(3.1, "ONLINE", ["in production", "no labels", "watch proxies"], ACCENT)
        self.play(FadeIn(left, shift=RIGHT * 0.1), run_time=0.7); self.wait(2.0)
        self.play(FadeIn(right, shift=LEFT * 0.1), run_time=0.7); self.wait(2.0)
        self.play(Write(Text("same word — two completely different problems", color=MUTE,
                             font_size=27, slant="ITALIC").to_edge(DOWN, buff=0.55)), run_time=0.7)
        _fill(self, "B01_TwoJobs")


class B02_Offline(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Offline — You Know the Truth"), shift=DOWN * 0.2), run_time=0.6)
        gs = _chip("golden set\nQ + known answer", w=4.6, h=1.6, fill=INK, op=0.09, fs=26).move_to([-3.2, 0.9, 0])
        self.play(FadeIn(gs, shift=RIGHT * 0.1), run_time=0.6)
        score = _chip("score the system", w=4.4, h=1.6, fill=ACCENT, op=0.12, fs=27).move_to([3.1, 0.9, 0])
        self.play(GrowArrow(Arrow(gs.get_right(), score.get_left(), color=ACCENT, stroke_width=5, buff=0.15)), FadeIn(score), run_time=0.7)
        self.wait(0.6)
        metrics = VGroup(
            Text("retrieval:  hit@k · MRR", color=INK, font_size=28),
            Text("generation:  faithfulness", color=INK, font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to([0, -1.4, 0])
        for m in metrics:
            self.play(FadeIn(m, shift=RIGHT * 0.1), run_time=0.5); self.wait(0.6)
        self.play(Write(Text("you know the truth — the numbers mean what they say", color=GOOD,
                             font_size=26, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.7)
        _fill(self, "B02_Offline")


class B03_CIGate(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Make It a CI Gate"), shift=DOWN * 0.2), run_time=0.6)
        gs = _chip("golden set\non every deploy", w=4.2, h=1.5, fill=INK, op=0.09, fs=25).move_to([-4.0, 0.6, 0])
        cmp = _chip("vs baseline", w=3.0, h=1.5, fill=MUTE, op=0.16, fs=26).move_to([-0.2, 0.6, 0])
        self.play(FadeIn(gs), run_time=0.5)
        self.play(GrowArrow(Arrow(gs.get_right(), cmp.get_left(), color=ACCENT, stroke_width=5, buff=0.12)), FadeIn(cmp), run_time=0.6)
        ok = _chip("PASS → deploy", w=3.4, h=1.0, fill=GOOD, op=0.14, fs=26, tcol=GOOD).move_to([3.6, 1.2, 0])
        bad = _chip("DROP → blocked", w=3.6, h=1.0, fill=BAD, op=0.12, fs=26, tcol=BAD).move_to([3.6, -0.1, 0])
        self.play(GrowArrow(Arrow(cmp.get_right(), ok.get_left(), color=GOOD, stroke_width=4, buff=0.12)), FadeIn(ok), run_time=0.5)
        self.play(GrowArrow(Arrow(cmp.get_right(), bad.get_left(), color=BAD, stroke_width=4, buff=0.12)), FadeIn(bad), run_time=0.5)
        self.wait(0.8)
        self.play(Write(Text("a failing quality test stops the release — before any user sees it", color=INK,
                             font_size=25, weight="BOLD").to_edge(DOWN, buff=0.55)), run_time=0.8)
        _fill(self, "B03_CIGate")


class B04_OnlineProblem(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("In Production, Truth Disappears"), shift=DOWN * 0.2), run_time=0.6)
        q = _chip("unseen question", w=4.2, h=1.1, fill=INK, op=0.09, fs=27).move_to([-3.4, 0.7, 0])
        a = _chip("an answer", w=3.2, h=1.1, fill=ACCENT, op=0.12, fs=27).move_to([0.6, 0.7, 0])
        qm = Text("?", color=BAD, font_size=72, weight="BOLD").move_to([4.4, 0.7, 0])
        self.play(FadeIn(q, shift=RIGHT * 0.1), run_time=0.5)
        self.play(GrowArrow(Arrow(q.get_right(), a.get_left(), color=ACCENT, stroke_width=5, buff=0.15)), FadeIn(a), run_time=0.6)
        self.play(GrowArrow(Arrow(a.get_right(), qm.get_left() + [-0.1, 0, 0], color=BAD, stroke_width=5, buff=0.2)), FadeIn(qm, scale=1.2), run_time=0.6)
        self.wait(0.6)
        self.play(Write(Text("nobody labels it — you can't compute correctness live", color=BAD,
                             font_size=27, weight="BOLD").move_to([0, -1.3, 0])), run_time=0.8)
        self.play(Write(Text("new question: is the system behaving like it did when healthy?", color=INK,
                             font_size=25, weight="BOLD").to_edge(DOWN, buff=0.55)), run_time=0.8)
        _fill(self, "B04_OnlineProblem")


class B05_Proxies(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Watch the Proxies"), shift=DOWN * 0.2), run_time=0.6)
        items = [("score distribution", "mean top-1 ↓ = drift alert"),
                 ("refusal rate", "answering less?"),
                 ("latency · cost", "per request"),
                 ("user feedback", "thumbs, follow-ups")]
        cards = VGroup()
        for head, sub in items:
            box = RoundedRectangle(width=5.4, height=1.5, corner_radius=0.14, fill_color=INK,
                                   fill_opacity=0.08, stroke_color=INK, stroke_width=3)
            h = Text(head, color=ACCENT, font_size=28, weight="BOLD").move_to(box.get_center() + UP * 0.32)
            s = Text(sub, color=INK, font_size=23).move_to(box.get_center() + DOWN * 0.32)
            cards.add(VGroup(box, h, s))
        cards.arrange_in_grid(rows=2, cols=2, buff=(0.6, 0.55)).move_to([0, -0.15, 0])
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.1), run_time=0.45); self.wait(0.7)
        self.play(Write(Text("none is correctness — together they tell you when to look", color=MUTE,
                             font_size=25, slant="ITALIC").to_edge(DOWN, buff=0.45)), run_time=0.7)
        _fill(self, "B05_Proxies")


class B06_Trace(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("The Trace — Why It Broke"), shift=DOWN * 0.2), run_time=0.6)
        rows = ["retrieved chunks + scores", "the exact prompt sent", "the response", "latency per stage", "tokens + cost"]
        grp = VGroup()
        for r in rows:
            dot = Square(side_length=0.22, fill_color=ACCENT, fill_opacity=0.9, stroke_width=0)
            t = Text(r, color=INK, font_size=28)
            grp.add(VGroup(dot, t).arrange(RIGHT, buff=0.3))
        grp.arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to([0, 0.2, 0])
        for row in grp:
            self.play(GrowFromCenter(row[0]), FadeIn(row[1], shift=RIGHT * 0.1), run_time=0.4); self.wait(0.4)
        self.play(Write(Text("one span per request — when a proxy alerts, this is where you look", color=INK,
                             font_size=25, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.8)
        _fill(self, "B06_Trace")


class B08_Together(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Two Loops, One Rule"), shift=DOWN * 0.2), run_time=0.6)
        offline = _chip("OFFLINE gate\n(pre-deploy CI)", w=4.6, h=1.5, fill=INK, op=0.10, fs=26).move_to([-3.2, 1.2, 0])
        ship = _chip("ship", w=2.0, h=1.0, fill=GOOD, op=0.14, fs=26, tcol=GOOD).move_to([0.5, 1.2, 0])
        online = _chip("ONLINE monitor\n+ trace", w=4.6, h=1.5, fill=ACCENT, op=0.12, fs=26).move_to([3.0, -0.4, 0])
        self.play(FadeIn(offline, shift=RIGHT * 0.1), run_time=0.5)
        self.play(GrowArrow(Arrow(offline.get_right(), ship.get_left(), color=ACCENT, stroke_width=4, buff=0.12)), FadeIn(ship), run_time=0.5)
        self.play(GrowArrow(Arrow(ship.get_bottom(), online.get_top(), color=ACCENT, stroke_width=4, buff=0.15)), FadeIn(online), run_time=0.6)
        self.play(Create(CurvedArrow(online.get_left(), offline.get_bottom(), color=MUTE, stroke_width=3, angle=1.0)), run_time=0.6)
        self.wait(0.6)
        self.play(Write(Text("debug retrieval first — look at the chunks before the prompt", color=ACCENT,
                             font_size=27, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.8)
        _fill(self, "B08_Together")
