import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))

from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {
    "B01": 4.0,
    "B02": 11.0, "B04": 9.0, "B05": 9.0,
    "B07": 9.0,  "B08": 8.0, "B09": 9.0,
    "B10": 7.0,  "B11": 8.0,
    "B12": 18.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ── B01 — Title ───────────────────────────────────────────────────────────────

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("COMPUTATIONAL SKEPTICISM", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why Some Missing Data", font=DISPLAY, color=INK, font_size=36, weight=BOLD)
        t2 = Text("Lies About Itself", font=DISPLAY, color=CRIMSON, font_size=36, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ── Shared bar helper ─────────────────────────────────────────────────────────

_YB = -2.3   # bar baseline y
_BW = 0.85   # bar width

def _bar(x, h, color, opacity=0.75):
    r = Rectangle(width=_BW, height=max(h, 0.05),
                  color=color, fill_color=color, fill_opacity=opacity, stroke_width=0)
    r.move_to([x, _YB + h / 2, 0])
    return r

def _axis(width=9.5):
    return Line([-width / 2, _YB, 0], [width / 2, _YB, 0],
                color=SLATE, stroke_width=1.5)


# ── B02 — IncomeDropout ───────────────────────────────────────────────────────

class B02_IncomeDropout(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Income Survey — Who Filled It In?", font=DISPLAY, font_size=20, color=GOLD).move_to(UP * 3.1)

        ax = _axis()
        labels_txt = ["$20k", "$40k", "$60k", "$80k", "$100k", "$150k+"]
        true_hs = [0.9, 1.4, 1.8, 1.5, 0.8, 0.5]   # true distribution
        miss_hs = [0.9, 1.4, 1.8, 1.5, 0.3, 0.05]  # after high earners drop out

        xs = [-3.75, -2.5, -1.25, 0.0, 1.25, 2.5]
        true_bars = [_bar(x, h, TEAL) for x, h in zip(xs, true_hs)]
        miss_bars = [_bar(x, h, CRIMSON) for x, h in zip(xs, miss_hs)]

        lbl_true = Text("REPORTED (visible)", font=MONO, font_size=12, color=TEAL).move_to([-3.5, 2.8, 0])
        lbl_miss = Text("HIGH EARNERS (missing)", font=MONO, font_size=12, color=CRIMSON).move_to([2.0, 2.8, 0])

        caption = Text("The visible distribution is systematically too low.",
                       font=DISPLAY, font_size=14, color=GOLD).move_to([0, -3.0, 0])

        self.play(Write(title), run_time=0.4)
        self.play(GrowFromCenter(ax), run_time=0.3)
        for b in true_bars:
            self.play(GrowFromEdge(b, DOWN), run_time=0.2)
        self.play(Write(lbl_true), run_time=0.3)
        for b, hm, ht, x in zip(miss_bars, miss_hs, true_hs, xs):
            if abs(hm - ht) > 0.1:
                gap = Rectangle(width=_BW, height=ht - hm,
                                color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.4, stroke_width=0)
                gap.move_to([x, _YB + hm + (ht - hm) / 2, 0])
                self.play(GrowFromCenter(gap), run_time=0.3)
        self.play(Write(lbl_miss), run_time=0.3)
        self.play(Write(caption), run_time=0.4)
        self.wait(DUR["B02"] - 4.5)


# ── B04 — ThreeTypes ──────────────────────────────────────────────────────────

class B04_ThreeTypes(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Three Kinds of Missing", font=DISPLAY, font_size=22, color=GOLD).move_to(UP * 3.1)

        rows = [
            ("MCAR — completely at random", "Sensor failure, random dropout\nSafe to impute; no systematic bias",  TEAL),
            ("MAR — at random given others", "Younger respondents skip income\nConditional on age, manageable",     SLATE),
            ("MNAR — not at random",         "High earners don't report income\nBias in the direction you can't measure", CRIMSON),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, desc, col) in enumerate(rows):
            y = 1.5 - i * 1.5
            box = Rectangle(width=10.5, height=1.2, color=col, fill_color=col,
                            fill_opacity=0.12, stroke_width=1.8).move_to(UP * y)
            t1  = Text(name, font=DISPLAY, font_size=16, color=col).move_to([0.0, y + 0.3,  0])
            t2  = Text(desc, font=MONO,    font_size=13, color=INK).move_to([0.0, y - 0.2, 0])
            self.play(GrowFromCenter(box), run_time=0.35)
            self.play(Write(t1), run_time=0.3)
            self.play(Write(t2), run_time=0.3)

        self.wait(DUR["B04"] - 4.0)


# ── B05 — LooksLikeRandom ─────────────────────────────────────────────────────

class B05_LooksLikeRandom(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("From Inside the Data — All Missing Looks the Same", font=DISPLAY, font_size=17, color=CRIMSON).move_to(UP * 3.1)

        # Three column bars with missing slots
        for i, (label, col, miss_frac) in enumerate([
            ("MCAR", TEAL, 0.2),
            ("MAR",  SLATE, 0.2),
            ("MNAR", CRIMSON, 0.2),
        ]):
            x = (i - 1) * 4.2
            box = Rectangle(width=3.2, height=3.8, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.5).move_to([x, 0.2, 0])
            lbl = Text(label, font=DISPLAY, font_size=17, color=col).move_to([x, 1.7, 0])
            # Present slots
            for j in range(4):
                slot = Rectangle(width=2.6, height=0.5, color=col, fill_color=col,
                                 fill_opacity=0.4, stroke_width=0).move_to([x, 0.5 - j * 0.7, 0])
                self.play(GrowFromCenter(slot), run_time=0.15)
            # Missing slot (hole)
            hole = Rectangle(width=2.6, height=0.5, color=CRIMSON, fill_color=CRIMSON,
                             fill_opacity=0.3, stroke_width=1).move_to([x, -2.3, 0])
            self.play(GrowFromCenter(box), run_time=0.3)
            self.play(Write(lbl), run_time=0.2)
            self.play(GrowFromCenter(hole), run_time=0.2)

        caption = Text("All three show a gap. None tells you why from inside.",
                       font=DISPLAY, font_size=14, color=GOLD).move_to(DOWN * 2.8)
        self.play(Write(caption), run_time=0.4)
        self.wait(DUR["B05"] - 4.5)


# ── B07 — ImputationBias ──────────────────────────────────────────────────────

class B07_ImputationBias(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("What Imputation Does to MNAR Data", font=DISPLAY, font_size=18, color=CRIMSON).move_to(UP * 3.1)

        steps = [
            ("Visible distribution is skewed low",  "high earners absent → visible mean is too small",  CRIMSON),
            ("Impute missing = fill with visible mean", "plug low number into high-income slots",         CRIMSON),
            ("Dataset now systematically wrong",    "in exactly the direction you couldn't see",         CRIMSON),
            ("More data = more confident, more wrong", "the bias bakes in permanently",                  GOLD),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (patch, result, col) in enumerate(steps):
            y = 1.8 - i * 1.3
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.5).move_to(UP * y)
            t1  = Text(patch,  font=DISPLAY, font_size=14, color=col).move_to([0.0, y + 0.22, 0])
            t2  = Text(result, font=MONO,    font_size=13, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.3)
            self.play(Write(t1), run_time=0.3)
            self.play(Write(t2), run_time=0.3)

        self.wait(DUR["B07"] - 4.5)


# ── B08 — QuoteMNAR ───────────────────────────────────────────────────────────

class B08_QuoteMNAR(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Missing not at random: the probability of being missing "
            "depends on the value itself. "
            "Standard imputation produces biased estimates, "
            "and the bias is exactly in the direction you cannot measure.",
            "Computational Skepticism for AI, Chapter 5",
            None,
            "direction you cannot measure",
            DUR["B08"],
        )


# ── B09 — Detection ───────────────────────────────────────────────────────────

class B09_Detection(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("How to Detect MNAR", font=DISPLAY, font_size=22, color=TEAL).move_to(UP * 3.1)

        rows = [
            ("NOT: count the missing values",     "any type looks like this — no signal",                CRIMSON),
            ("NOT: look at missingness patterns",  "standard EDA does not detect MNAR",                  CRIMSON),
            ("YES: reason about who's absent",    "who would not report this? why?",                     TEAL),
            ("YES: think about the mechanism",    "does the value itself determine whether it's there?",  TEAL),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, action, col) in enumerate(rows):
            y = 1.8 - i * 1.3
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.8).move_to(UP * y)
            lbl = Text(name,   font=DISPLAY, font_size=14, color=col).move_to([0.0, y + 0.2,  0])
            act = Text(action, font=MONO,    font_size=13, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.35)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(act), run_time=0.3)

        self.wait(DUR["B09"] - 4.5)


# ── B10 — QuoteDetect ─────────────────────────────────────────────────────────

class B10_QuoteDetect(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Standard EDA does not detect missing not at random. "
            "You detect it by thinking carefully about "
            "who would not report this value and why.",
            "Computational Skepticism for AI, Chapter 5",
            None,
            "who would not report",
            DUR["B10"],
        )


# ── B11 — TheQuestion ─────────────────────────────────────────────────────────

class B11_TheQuestion(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("The Question Tools Skip", font=DISPLAY, font_size=22, color=GOLD).move_to(UP * 3.1)

        rows = [
            ("Tools ask: HOW MANY are missing?",  "18% missing — fill with mean",                          SLATE),
            ("You should ask: WHY are they missing?", "does the value itself determine absence?",             TEAL),
            ("If yes: MNAR",                      "imputing from what you see bakes in the bias",            CRIMSON),
            ("In precisely the direction",         "you cannot measure from inside the data",                 CRIMSON),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, action, col) in enumerate(rows):
            y = 1.8 - i * 1.3
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.8).move_to(UP * y)
            lbl = Text(name,   font=DISPLAY, font_size=14, color=col).move_to([0.0, y + 0.2,  0])
            act = Text(action, font=MONO,    font_size=13, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.35)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(act), run_time=0.3)

        self.wait(DUR["B11"] - 4.5)


# ── B12 — ExampleMNAR ────────────────────────────────────────────────────────

class B12_ExampleMNAR(Scene):
    """THE EXAMPLE — clinical trial: dropouts with severe effects missing, results too optimistic."""
    def construct(self):
        total = DUR["B12"]
        title = Text("Clinical Trial — pain medication", font=DISPLAY,
                     font_size=20, color=GOLD)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.5, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        col_r = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)

        lbl_l = Text("Completers (157)", font=DISPLAY, font_size=22, color=TEAL, weight=BOLD)
        lbl_l.move_to(col_l.get_top() + DOWN * 0.45)
        val_l1 = Text("avg pain reduction: 4.2 pts", font=MONO, font_size=20, color=TEAL)
        val_l1.move_to(col_l.get_center() + UP * 0.2)
        val_l2 = Text("→ model says: effective", font=SERIF, font_size=18, color=TEAL)
        val_l2.move_to(col_l.get_center() + DOWN * 0.7)

        lbl_r = Text("Dropouts (43)", font=DISPLAY, font_size=22, color=CRIMSON, weight=BOLD)
        lbl_r.move_to(col_r.get_top() + DOWN * 0.45)
        val_r1 = Text("severe side effects, week 2", font=MONO, font_size=20, color=CRIMSON)
        val_r1.move_to(col_r.get_center() + UP * 0.2)
        val_r2 = Text("→ missing from data", font=SERIF, font_size=18, color=CRIMSON)
        val_r2.move_to(col_r.get_center() + DOWN * 0.7)

        note_rect = Rectangle(width=9.5, height=0.52, fill_color=CRIMSON, fill_opacity=0.10,
                              stroke_width=1.5, color=CRIMSON).move_to(DOWN * 2.55)
        note_txt = Text("worst responders left — result is systematically too optimistic",
                        font=SERIF, font_size=19, color=CRIMSON)
        note_txt.move_to(note_rect.get_center())

        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(col_l), FadeIn(lbl_l), run_time=0.7)
        self.play(FadeIn(val_l1), FadeIn(val_l2), run_time=0.6)
        self.play(FadeIn(col_r), FadeIn(lbl_r), run_time=0.7)
        self.play(FadeIn(val_r1), FadeIn(val_r2), run_time=0.6)
        self.play(FadeIn(note_rect), FadeIn(note_txt), run_time=0.7)
        self.wait(max(0.5, total - 4.0))
