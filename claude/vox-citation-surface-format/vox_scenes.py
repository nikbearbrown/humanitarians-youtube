"""vox_scenes.py — Why Claude Can't Write Your Literature Review
(vox-citation-surface-format, slate cut, 16:9)

Color law (teardown):
  INK     = real/verified sources
  CRIMSON = hallucinated citations (identical surface format, no source)
  SLATE   = plausible-but-unverified (lead status)

Exclusions: no semantic entropy, no RAG, no model-version comparison.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 9.0, "B03": 9.0, "B04": 12.0, "B05": 11.0, "B06": 11.0,
    "B07": 10.0, "B08": 12.0, "B09": 11.0, "B10": 12.0, "B11": 12.0,
    "B12": 11.0, "B13": 10.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


def _label(text, color=INK, size=26):
    return Text(text, font=SERIF, color=color, font_size=size)


def _chip(text, accent=SLATE, size=20):
    return LabelChip(text, accent=accent, size=size)


def _cite_row(author, journal, year, status_color, size=21):
    """A fake citation row in a consistent format, colored by status."""
    text = f"{author} ({year}). Finding on topic. {journal}, 12(3), 44–58."
    return _label(text, status_color, size)


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("PROMPT ENGINEERING", font=DISPLAY, color=CRIMSON,
                   font_size=22, weight=BOLD)
        t1 = Text("Why Claude can't write", font=SERIF, color=INK, font_size=56, weight=BOLD)
        t2 = Text("your literature review", font=SERIF, color=INK, font_size=56, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        sub = _label("citations from Claude are leads — not evidence", SLATE, 26)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text("Why did the format", font=SERIF, color=INK, font_size=52, weight=BOLD)
        q2 = Text("give no signal?", font=SERIF, color=INK, font_size=52, weight=BOLD)
        block = VGroup(q1, q2).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.14, q2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q1), run_time=0.6)
        self.play(FadeIn(q2), Create(u), run_time=0.8)
        self.wait(max(0.5, total - 1.4))


class B04_GenerateNotRetrieve(Scene):
    """Claude generates citation-shaped text — does not retrieve from database."""
    def construct(self):
        total = DUR["B04"]
        title = _label("Claude generates. It does not retrieve.", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Two tracks
        gen_chip = _chip("CLAUDE", accent=CRIMSON, size=20)
        gen_step1 = _label("statistical pattern", CRIMSON, 22)
        gen_arr = Text("→", font=SERIF, color=SLATE, font_size=22)
        gen_step2 = _label("citation-shaped text", CRIMSON, 22)
        gen_row = VGroup(gen_chip, gen_step1, gen_arr, gen_step2).arrange(RIGHT, buff=0.25)
        gen_row.move_to(UP * 0.4)

        db_chip = _chip("DATABASE", accent=INK, size=20)
        db_step1 = _label("search query", INK, 22)
        db_arr = Text("→", font=SERIF, color=SLATE, font_size=22)
        db_step2 = _label("verified source record", INK, 22)
        db_row = VGroup(db_chip, db_step1, db_arr, db_step2).arrange(RIGHT, buff=0.25)
        db_row.move_to(DOWN * 0.3)

        note = SerifLabel("a citation from Claude is a hypothesis about what might exist", CRIMSON, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(gen_row, shift=LEFT * 0.2), run_time=0.7)
        self.play(FadeIn(db_row, shift=LEFT * 0.2), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B05_SamePattern(Scene):
    """Real citation vs. hallucinated: same fields, same format, identical surface."""
    def construct(self):
        total = DUR["B05"]
        title = _label("Same six fields — same statistical process", INK, 28)
        title.to_edge(UP, buff=0.6)

        fields = ["Author", "Journal", "Year", "Volume", "Pages", "Finding"]
        # Real (INK)
        real_chip = _chip("REAL SOURCE", accent=INK, size=18)
        real_fields = VGroup(*[_chip(f, accent=INK, size=16) for f in fields])
        real_fields.arrange(RIGHT, buff=0.18)
        real_row = VGroup(real_chip, real_fields).arrange(RIGHT, buff=0.3)
        real_row.move_to(UP * 0.4)

        # Hallucinated (CRIMSON)
        hall_chip = _chip("HALLUCINATED", accent=CRIMSON, size=18)
        hall_fields = VGroup(*[_chip(f, accent=CRIMSON, size=16) for f in fields])
        hall_fields.arrange(RIGHT, buff=0.18)
        hall_row = VGroup(hall_chip, hall_fields).arrange(RIGHT, buff=0.3)
        hall_row.move_to(DOWN * 0.2)

        note = SerifLabel("no internal flag marks one as real — the pattern is the same", CRIMSON, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(real_row, shift=LEFT * 0.2), run_time=0.8)
        self.play(FadeIn(hall_row, shift=LEFT * 0.2), run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.7))


class B06_FluencyNotAccuracy(Scene):
    """Fluency is not accuracy — voice of scholarship ≠ substance."""
    def construct(self):
        total = DUR["B06"]
        title = _label("Fluency is not accuracy", INK, 28)
        title.to_edge(UP, buff=0.6)

        # A fluent-sounding citation row
        cite = _label('"Johnson et al. (2021). Green infrastructure cooling effects.', SLATE, 22)
        cite2 = _label('Urban Climate, 38(2), 101-114. doi:10.1016/j.uclim.2021.100901"', SLATE, 22)
        cite_block = VGroup(cite, cite2).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        cite_block.move_to(UP * 0.4)

        chip_real = _chip("SOUNDS AUTHORITATIVE", accent=SLATE, size=18)
        chip_real.next_to(cite_block, DOWN, buff=0.3)

        # The check
        check_chip = _chip("CHECKED", accent=CRIMSON, size=18)
        check_txt = _label("doi returns no result — paper does not exist", CRIMSON, 23)
        check_row = VGroup(check_chip, check_txt).arrange(RIGHT, buff=0.3)
        check_row.move_to(DOWN * 0.6)

        note = SerifLabel("the voice of scholarship does not prove the substance", CRIMSON, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(cite_block), run_time=0.7)
        self.play(FadeIn(chip_real), run_time=0.5)
        self.play(FadeIn(check_row, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.0))


class B07_SectionCard(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("Claude provides leads.", font=DISPLAY, color=INK,
                  font_size=46, weight=BOLD)
        t2 = Text("You produce the evidence.", font=DISPLAY, color=CRIMSON,
                  font_size=46, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2, scale=0.95), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B08_LeadsFirstPrompt(Scene):
    """Leads-first prompt: search terms + framework names, no citations."""
    def construct(self):
        total = DUR["B08"]
        title = _label("Ask for search terms — not citations", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Bad prompt
        bad_chip = _chip("BAD PROMPT", accent=CRIMSON, size=18)
        bad_txt = _label('"Find me papers on green roof cooling with citations."', CRIMSON, 22)
        bad_row = VGroup(bad_chip, bad_txt).arrange(RIGHT, buff=0.3)
        bad_row.move_to(UP * 0.6)

        cross = Line(bad_txt.get_corner(UL), bad_txt.get_corner(DR),
                     color=CRIMSON, stroke_width=2)
        cross._qc_intentional = True

        # Good prompt
        good_chip = _chip("LEADS-FIRST", accent=INK, size=18)
        good_t1 = _label('"Give me 8 search terms for green roof cooling.', INK, 22)
        good_t2 = _label('Name relevant frameworks — no citations."', INK, 22)
        good_block = VGroup(good_t1, good_t2).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        good_row = VGroup(good_chip, good_block).arrange(RIGHT, buff=0.3)
        good_row.move_to(DOWN * 0.35)

        note = SerifLabel("leads are cheap and useful — verification is yours", INK, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(bad_row), run_time=0.6)
        self.play(Create(cross), run_time=0.4)
        self.play(FadeIn(good_row, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.8))


class B09_RicherOutput(Scene):
    """Richer output = more verification needed."""
    def construct(self):
        total = DUR["B09"]
        title = _label("Richer output = verification more critical, not less", INK, 28)
        title.to_edge(UP, buff=0.6)

        rows_data = [
            ("SPARSE output", "easy to flag as incomplete", INK),
            ("FLUENT output", "feels authoritative — still needs verification", SLATE),
            ("RICH output", "most likely to be accepted unchecked", CRIMSON),
        ]
        rows = VGroup()
        for label, desc, color in rows_data:
            chip = _chip(label, accent=color, size=18)
            desc_lbl = _label(desc, color, 23)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.4).move_to(UP * 0.1)

        note = SerifLabel("fluency is the signal that makes the check feel unnecessary", CRIMSON, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.25),
                  run_time=1.1)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B10_MarcoChecks(Scene):
    """12 citations: 4 INK (real), 3 SLATE (wrong finding), 5 CRIMSON (nonexistent)."""
    def construct(self):
        total = DUR["B10"]
        title = _label("12 citations verified — three outcome categories", INK, 26)
        title.to_edge(UP, buff=0.6)

        outcomes = [
            ("4 CITATIONS", "real source · claim matches", INK),
            ("3 CITATIONS", "real journal · finding reversed", SLATE),
            ("5 CITATIONS", "source does not exist", CRIMSON),
        ]
        rows = VGroup()
        for label, desc, color in outcomes:
            chip = _chip(label, accent=color, size=20)
            desc_lbl = _label(desc, color, 24)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.4).move_to(UP * 0.1)

        note = SerifLabel("all 12 had identical format — only 4 were evidence", CRIMSON, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.25),
                  run_time=1.1)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B11_MarcoFixed(Scene):
    """Leads-first workflow: terms → database → abstracts to Claude → matrix."""
    def construct(self):
        total = DUR["B11"]
        title = _label("Leads-first workflow — 11 real papers in 40 minutes", INK, 28)
        title.to_edge(UP, buff=0.6)

        steps = [
            ("STEP 1", "ask Claude for search terms and framework names", INK),
            ("STEP 2", "run terms in Google Scholar and PubMed", INK),
            ("STEP 3", "paste 3 verified abstracts to Claude", INK),
            ("STEP 4", "ask for literature matrix from provided text only", INK),
        ]
        rows = VGroup()
        for label, desc, color in steps:
            chip = _chip(label, accent=color, size=18)
            desc_lbl = _label(desc, color, 23)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.35).move_to(UP * 0.0)

        result = SerifLabel("Claude works only from what Marco provided", INK, size=25)
        result.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.2),
                  run_time=1.1)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B12_Practice(Scene):
    """Two rules for every research prompt."""
    def construct(self):
        total = DUR["B12"]
        title = _label("Two rules for every research prompt:", INK, 28)
        title.to_edge(UP, buff=0.6)

        rules = [
            ("RULE 1", "never ask Claude for citations directly", INK),
            ("", "ask for search terms and framework names", INK),
            ("RULE 2", "if you paste sources, ask Claude to work from those only", INK),
            ("", "and flag anything it cannot find in your text", INK),
        ]
        rows = VGroup()
        for i, (label, desc, color) in enumerate(rules):
            if label:
                chip = _chip(label, accent=color, size=20)
                desc_lbl = _label(desc, color, 23)
                row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            else:
                indent = Text("  →", font=SERIF, font_size=22, color=SLATE)
                desc_lbl = _label(desc, SLATE, 22)
                row = VGroup(indent, desc_lbl).arrange(RIGHT, buff=0.1)
            rows.add(row)
        rows.arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(DOWN * 0.1)

        note = SerifLabel("leads are directions — evidence requires your verification", INK, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.15), run_time=1.2)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B13_End(Scene):
    def construct(self):
        total = DUR["B13"]
        t1 = Text("Leads to verify.", font=SERIF,
                  color=INK, font_size=48, weight=BOLD)
        t2 = Text("Not evidence to cite.", font=SERIF,
                  color=INK, font_size=48, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        sub = _label("the voice of scholarship does not prove the substance", SLATE, 26)
        sub.next_to(u, DOWN, buff=0.4)
        topic = Text("PROMPT ENGINEERING", font=DISPLAY, color=SLATE,
                     font_size=22, weight=BOLD)
        topic.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(topic, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.6))
