import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))

from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {
    "B01": 4.0,
    "B02": 11.0, "B04": 9.0, "B05": 9.0,
    "B07": 9.0,  "B08": 8.0, "B09": 9.0,
    "B10": 7.0,  "B11": 8.0, "B12": 14.0,
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
        t1 = Text("Why Deleting the Race Column", font=DISPLAY, color=INK, font_size=36, weight=BOLD)
        t2 = Text("Doesn't Delete Race", font=DISPLAY, color=CRIMSON, font_size=36, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ── B02 — GhostColumn ─────────────────────────────────────────────────────────

class B02_GhostColumn(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Feature Set — Race Column Removed", font=DISPLAY, font_size=18, color=GOLD).move_to(UP * 3.1)

        # Present columns
        col_data = [
            ("INCOME",     TEAL),
            ("DEBT RATIO", TEAL),
            ("ZIP CODE",   CRIMSON),
            ("SURNAME",    CRIMSON),
            ("OCCUPATION", CRIMSON),
        ]
        xs = [-4.0, -2.0, 0.0, 2.0, 4.0]
        cols = []
        for (label, col), x in zip(col_data, xs):
            box = Rectangle(width=1.6, height=3.8, color=col, fill_color=col,
                            fill_opacity=0.15, stroke_width=1.5).move_to([x, 0.3, 0])
            lbl = Text(label, font=MONO, font_size=11, color=col).move_to([x, 1.7, 0])
            cols.append((box, lbl, col, x))

        # Ghost — deleted race column (shown as struck-through slate)
        ghost_box = Rectangle(width=1.6, height=3.8, color=SLATE, fill_color=SLATE,
                              fill_opacity=0.08, stroke_width=1.5, stroke_opacity=0.4).move_to([6.0, 0.3, 0])
        ghost_lbl = Text("RACE\n(deleted)", font=MONO, font_size=11, color=SLATE).move_to([6.0, 1.7, 0])
        ghost_cross = Line([5.2, -1.6, 0], [6.8, 2.0, 0], color=SLATE, stroke_width=1.5, stroke_opacity=0.5)

        # Arrows from proxy columns to ghost
        arrows = [
            Line([x + 0.8, 0.3, 0], [5.15, 0.3, 0], color=CRIMSON, stroke_width=1.5)
            for x in [0.0, 2.0, 4.0]
        ]

        caption = Text("Proxies reconstruct the deleted column inside the model.",
                       font=DISPLAY, font_size=13, color=GOLD).move_to(DOWN * 2.5)

        self.play(Write(title), run_time=0.4)
        for box, lbl, col, x in cols:
            self.play(GrowFromCenter(box), run_time=0.25)
            self.play(Write(lbl), run_time=0.2)
        self.play(GrowFromCenter(ghost_box), run_time=0.4)
        self.play(Write(ghost_lbl), run_time=0.3)
        self.play(Create(ghost_cross), run_time=0.3)
        for arr in arrows:
            self.play(GrowFromEdge(arr, LEFT), run_time=0.3)
        self.play(Write(caption), run_time=0.4)
        self.wait(DUR["B02"] - 5.0)


# ── B04 — Correlations ────────────────────────────────────────────────────────

class B04_Correlations(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("The Sensitive Attribute Isn't One Column", font=DISPLAY, font_size=18, color=CRIMSON).move_to(UP * 3.1)

        proxies = [
            ("ZIP CODE",   "encodes neighborhood demographics\nhistorically segregated by race",   CRIMSON),
            ("SURNAME",    "carries ancestry signals\ncorrelated with ethnic group",                CRIMSON),
            ("OCCUPATION", "reflects historical access patterns\ncorrelated with race in training data", CRIMSON),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, desc, col) in enumerate(proxies):
            x = (i - 1) * 4.3
            box = Rectangle(width=3.8, height=2.8, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.8).move_to([x, 0.4, 0])
            lbl = Text(name, font=DISPLAY, font_size=15, color=col).move_to([x, 1.4, 0])
            desc_txt = Text(desc, font=MONO, font_size=12, color=INK).move_to([x, 0.0, 0])
            self.play(GrowFromCenter(box), run_time=0.4)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(desc_txt), run_time=0.3)

        note = Text("Remove the column — the signal stays in the correlations.",
                    font=DISPLAY, font_size=14, color=GOLD).move_to(DOWN * 2.3)
        self.play(Write(note), run_time=0.4)
        self.wait(DUR["B04"] - 4.3)


# ── B05 — DirectVsIndirect ────────────────────────────────────────────────────

class B05_DirectVsIndirect(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        hdr_dir = Rectangle(width=5.5, height=0.6, color=TEAL,   fill_color=TEAL,
                            fill_opacity=0.20, stroke_width=1.5).move_to(LEFT * 3.2 + UP * 2.8)
        hdr_ind = Rectangle(width=5.5, height=0.6, color=CRIMSON, fill_color=CRIMSON,
                            fill_opacity=0.20, stroke_width=1.5).move_to(RIGHT * 3.2 + UP * 2.8)
        t_dir   = Text("DIRECT PATH", font=DISPLAY, font_size=17, color=TEAL).move_to(hdr_dir)
        t_ind   = Text("INDIRECT PATH", font=DISPLAY, font_size=17, color=CRIMSON).move_to(hdr_ind)

        body_dir = Rectangle(width=5.5, height=3.8, color=TEAL, fill_opacity=0,
                             stroke_width=1.5).move_to(LEFT * 3.2 + DOWN * 0.6)
        body_ind = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_opacity=0,
                             stroke_width=1.5).move_to(RIGHT * 3.2 + DOWN * 0.6)

        c1 = Text("Race column →\nModel", font=MONO, font_size=15, color=INK).move_to(LEFT * 3.2 + UP * 0.5)
        c2 = Text("→ FTU BLOCKS THIS", font=DISPLAY, font_size=14, color=TEAL).move_to(LEFT * 3.2 + DOWN * 1.5)

        f1 = Text("Zip code + surname →\nModel (race implicit)", font=MONO, font_size=14, color=INK).move_to(RIGHT * 3.2 + UP * 0.5)
        f2 = Text("→ FTU DOES NOTHING\nABOUT THIS", font=DISPLAY, font_size=14, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 1.5)

        self.play(GrowFromCenter(hdr_dir), GrowFromCenter(hdr_ind), run_time=0.5)
        self.play(Write(t_dir), Write(t_ind), run_time=0.5)
        self.play(GrowFromCenter(body_dir), GrowFromCenter(body_ind), run_time=0.5)
        self.play(Write(c1), Write(f1), run_time=0.5)
        self.play(Write(c2), Write(f2), run_time=0.5)
        self.wait(DUR["B05"] - 3.5)


# ── B07 — ProxyPaths ──────────────────────────────────────────────────────────

class B07_ProxyPaths(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("What FTU Does and Doesn't Close", font=DISPLAY, font_size=18, color=GOLD).move_to(UP * 3.1)

        steps = [
            ("Race column removed",           "FTU closes this direct input path",        TEAL),
            ("Zip code remains → model",       "correlated with race — indirect path open", CRIMSON),
            ("Surname remains → model",        "ancestry signal — indirect path open",      CRIMSON),
            ("Model learns race from proxies", "inside learned weights, not the column",    CRIMSON),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (patch, result, col) in enumerate(steps):
            y = 1.8 - i * 1.3
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.5).move_to(UP * y)
            t1  = Text(patch,  font=DISPLAY, font_size=15, color=col).move_to([0.0, y + 0.22, 0])
            t2  = Text(result, font=MONO,    font_size=13, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.3)
            self.play(Write(t1), run_time=0.3)
            self.play(Write(t2), run_time=0.3)

        self.wait(DUR["B07"] - 4.5)


# ── B08 — QuoteFTU ────────────────────────────────────────────────────────────

class B08_QuoteFTU(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Fairness through unawareness is not a fairness guarantee. "
            "It is a documentation choice that looks like one.",
            "Computational Skepticism for AI, Chapter 7",
            None,
            "documentation choice",
            DUR["B08"],
        )


# ── B09 — WhatWorks ───────────────────────────────────────────────────────────

class B09_WhatWorks(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("What Actually Audits Fairness", font=DISPLAY, font_size=20, color=TEAL).move_to(UP * 3.1)

        rows = [
            ("NOT: confirm column is absent",    "that's a documentation audit, not a fairness audit", CRIMSON),
            ("YES: audit proxy correlations",    "do remaining features correlate with the sensitive attribute?", TEAL),
            ("YES: measure outcomes by group",   "compare model outputs across demographic groups",     TEAL),
            ("YES: test for reconstruction",     "can you predict the deleted column from remaining ones?", TEAL),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, action, col) in enumerate(rows):
            y = 1.8 - i * 1.3
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.8).move_to(UP * y)
            lbl = Text(name,   font=DISPLAY, font_size=14, color=col).move_to([0.0, y + 0.2,  0])
            act = Text(action, font=MONO,    font_size=12, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.35)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(act), run_time=0.3)

        self.wait(DUR["B09"] - 4.5)


# ── B10 — QuoteProxy ──────────────────────────────────────────────────────────

class B10_QuoteProxy(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Sensitive attributes reconstruct from proxies — "
            "zip code, surname, occupation — that correlate with group membership. "
            "Omit race but keep zip code and the model may be using race anyway.",
            "Computational Skepticism for AI, Chapter 7",
            None,
            "reconstruct from proxies",
            DUR["B10"],
        )


# ── B11 — AuditOutcomes ───────────────────────────────────────────────────────

class B11_AuditOutcomes(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Documentation vs Fairness Audit", font=DISPLAY, font_size=20, color=GOLD).move_to(UP * 3.1)

        rows = [
            ("Documentation audit",    "race column absent → ✓",                           SLATE),
            ("Fairness audit",         "outcomes by group → gap still there",               CRIMSON),
            ("The gap is real",        "the column's absence didn't close it",               CRIMSON),
            ("Auditing fairness means", "measuring what the model does, not what it sees",  TEAL),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, action, col) in enumerate(rows):
            y = 1.8 - i * 1.3
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.8).move_to(UP * y)
            lbl = Text(name,   font=DISPLAY, font_size=15, color=col).move_to([0.0, y + 0.2,  0])
            act = Text(action, font=MONO,    font_size=13, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.35)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(act), run_time=0.3)

        self.wait(DUR["B11"] - 4.5)


# ── B12 — ExampleRace ─────────────────────────────────────────────────────────

class B12_ExampleRace(Scene):
    def construct(self):
        total = DUR["B12"]
        title = Text("Hiring Model — name column removed", font=DISPLAY, font_size=20, color=GOLD)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.5, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        col_r = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)

        lbl_l = Text("Column removed", font=DISPLAY, font_size=16, color=TEAL).move_to(LEFT * 3.2 + UP * 1.55)
        lbl_r = Text("Proxy features remain", font=DISPLAY, font_size=16, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 1.55)

        val_l = Text('Name: [DELETED]', font=MONO, font_size=14, color=SLATE).move_to(LEFT * 3.2 + UP * 0.5)

        val_r1 = Text("University → race  ρ=0.19", font=MONO, font_size=13, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 0.75)
        val_r2 = Text("ZIP code → demographics", font=MONO, font_size=13, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 0.05)
        val_r3 = Text("Prior employer → segregation", font=MONO, font_size=13, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 0.85)

        note_rect = Rectangle(width=9.5, height=0.52, fill_color=CRIMSON, fill_opacity=0.10,
                              stroke_width=1.5, color=CRIMSON).move_to(DOWN * 2.55)
        note_txt = Text("hiring rates unchanged — signal reconstructed from proxies (illustrative)",
                        font=MONO, font_size=11, color=CRIMSON).move_to(DOWN * 2.55)

        self.play(Write(title), run_time=0.5)
        self.play(GrowFromCenter(col_l), GrowFromCenter(col_r), run_time=0.6)
        self.play(Write(lbl_l), Write(lbl_r), run_time=0.5)
        self.play(FadeIn(val_l), run_time=0.4)
        self.play(Write(val_r1), run_time=0.4)
        self.play(Write(val_r2), run_time=0.4)
        self.play(Write(val_r3), run_time=0.4)
        self.play(GrowFromCenter(note_rect), run_time=0.4)
        self.play(Write(note_txt), run_time=0.4)
        self.wait(max(0.5, total - 4.5))
