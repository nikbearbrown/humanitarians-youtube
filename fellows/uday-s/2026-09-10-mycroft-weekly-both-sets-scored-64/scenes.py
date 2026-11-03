"""Manim beats for the reel `mycroft-weekly-both-sets-scored-64`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: mycroft @ 253ee74 (2026-09-10), episode 3. Every number was taken from
a live run of steps 4 and 5, not from the commit message; see SOURCES.md.

NO LaTeX anywhere (dvisvgm absent).

Layout lessons carried from the previous three reels — all of them cost a
re-render to learn, so they are stated rather than rediscovered:
  * kicker at buff 0.72 — 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * beats carrying a citation use fit_src(), which reserves the citation strip
  * never draw a line THROUGH text — mark the connector, not the label
  * compose every label INTO the fitted group; anything positioned relative to
    a group after fit() can land on the citation
  * _fit scales UP as well as down (FILL-THE-CANVAS): a helper that only shrinks
    silently leaves sparse beats half empty
"""

import glob
import os

import manimpango
from manim import (
    DOWN, LEFT, RIGHT, UP, Create, FadeIn, LaggedStart, Line, RoundedRectangle,
    Scene, Text, VGroup, Write,
)

_TOOLKIT_FONTS = os.environ.get(
    "ART_FONT_DIR",
    "D:/Projects/brutalist.art/.claude/worktrees/video-creation-setup-4c85fe/runtime/fonts",
)
for _ttf in glob.glob(os.path.join(_TOOLKIT_FONTS, "**", "*.ttf"), recursive=True):
    manimpango.register_font(os.path.abspath(_ttf))

_FAMS = set(manimpango.list_fonts())
SERIF = "EB Garamond" if "EB Garamond" in _FAMS else "Georgia"
SANS = "Inter 28pt" if "Inter 28pt" in _FAMS else "Segoe UI"
MONO = "Consolas" if "Consolas" in _FAMS else "Courier New"

CREAM = "#FAF9F5"
INK = "#3D3929"
INK_SOFT = "#6B6559"
TERRA = "#D97757"

BODY_TOP = 2.25
BODY_BOTTOM = -2.45
BODY_W = 12.0
BODY_H = BODY_TOP - BODY_BOTTOM
SRC_BOTTOM = -1.95


def page(scene):
    scene.camera.background_color = CREAM


def kicker(text, sub=None):
    k = Text(text, font=SANS, font_size=22, color=INK_SOFT).to_edge(UP, buff=0.72)
    k.to_edge(LEFT, buff=0.9)
    rule = Line(k.get_left() + DOWN * 0.28, k.get_left() + RIGHT * 12.0 + DOWN * 0.28,
                stroke_width=1.4, color=INK_SOFT)
    grp = VGroup(k, rule)
    if sub:
        s = Text(sub, font=MONO, font_size=19, color=INK_SOFT)
        s.next_to(rule, DOWN, buff=0.20).align_to(k, LEFT)
        grp.add(s)
    return grp


def spark(text):
    return Text(text, font=SERIF, font_size=37, color=TERRA).to_edge(DOWN, buff=0.62)


def source_line(text):
    return Text(text, font=MONO, font_size=16, color=INK_SOFT).to_edge(DOWN, buff=1.55)


def _fit(group, w, h, centre_y, grow=1.9):
    if group.width <= 0 or group.height <= 0:
        return group
    k = min(w / group.width, h / group.height)
    k = min(k, grow) if k > 1 else k
    group.scale(k)
    group.move_to([0, centre_y, 0])
    return group


def fit(group, w=BODY_W, h=BODY_H):
    return _fit(group, w, h, (BODY_TOP + BODY_BOTTOM) / 2)


def fit_src(group, w=BODY_W):
    return _fit(group, w, BODY_TOP - SRC_BOTTOM, (BODY_TOP + SRC_BOTTOM) / 2)


def tick(color=INK):
    """A drawn check mark. Sits BESIDE a label, never across it."""
    return VGroup(
        Line([-0.10, 0.02, 0], [-0.02, -0.09, 0], stroke_width=3.2, color=color),
        Line([-0.02, -0.09, 0], [0.13, 0.13, 0], stroke_width=3.2, color=color),
    )


def chip(label, color, font_size=19, pad=0.32, height=0.36):
    t = Text(label, font=MONO, font_size=font_size, color=color)
    box = RoundedRectangle(width=t.width + pad, height=height, corner_radius=0.07,
                           stroke_width=1.5, stroke_color=color, fill_opacity=0)
    box.move_to(t.get_center())
    return VGroup(box, t)


def panel(title, lines, accent=INK_SOFT, min_w=4.4, fs=21, title_fs=24):
    t = Text(title, font=SANS, font_size=title_fs, color=accent)
    body = VGroup(*[Text(l, font=MONO, font_size=fs, color=INK) for l in lines])
    body.arrange(DOWN, buff=0.24, aligned_edge=LEFT)
    inner = VGroup(t, body).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
    box = RoundedRectangle(width=max(min_w, inner.width + 0.8),
                           height=inner.height + 0.8, corner_radius=0.12,
                           stroke_width=1.8, stroke_color=accent, fill_opacity=0)
    box.move_to(inner.get_center())
    return VGroup(box, inner)


class B01_LedgerSteps(Scene):
    """PROBLEM: the six-step ledger, two more closing. 12.59s."""

    STEPS = [
        ("1", "verify-provenance", "done"),
        ("2", "ingest-inputs", "done"),
        ("3", "validate-data-shape", "done"),
        ("4", "transform-quality-check", "closing"),
        ("5", "run-approved-tools", "closing"),
        ("6", "produce-human-report", "open"),
    ]

    def construct(self):
        page(self)
        head = kicker("THE RECIPE", "six declared steps · episode 3")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows, closing = VGroup(), []
        for num, name, state in self.STEPS:
            done = state == "done"
            color = INK if done else TERRA
            n = Text(num, font=SERIF, font_size=30, color=INK_SOFT)
            box = RoundedRectangle(width=0.34, height=0.34, corner_radius=0.06,
                                   stroke_width=2.0, stroke_color=color, fill_opacity=0)
            label = Text(name, font=MONO, font_size=26, color=color)
            box.next_to(n, RIGHT, buff=0.38)
            label.next_to(box, RIGHT, buff=0.38)
            row = VGroup(n, box, label)
            rows.add(row)
            if done:
                row.add(tick(INK).move_to(box.get_center()))
            elif state == "closing":
                closing.append(row)
        rows.arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        fit(rows)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.25) for r in rows],
                              lag_ratio=0.28), run_time=2.4)
        self.wait(1.0)

        anims = []
        for row in closing:
            mark = tick(INK).move_to(row[1].get_center())
            anims += [row[1].animate.set_stroke(INK), row[2].animate.set_color(INK),
                      Create(mark)]
        self.play(*anims, run_time=2.3)
        self.wait(0.9)

        point = spark("Five of six")
        self.play(Write(point), run_time=1.6)
        self.wait(2.49)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: three questions about any emitted number. 16.68s."""

    QS = [
        ("1", "MEASURED OR\nSUBSTITUTED?", "did data produce it,\nor did a fallback?"),
        ("2", "DOES THE OUTPUT\nSAY WHICH?", "is the substitution\nnamed in the record?"),
        ("3", "CAN YOU WALK\nIT BACK?", "is there a chain to\nthe source bytes?"),
    ]

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS", "ask these of any number a pipeline hands you")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = VGroup()
        for num, title, body in self.QS:
            n = Text(num, font=SERIF, font_size=32, color=TERRA)
            t = Text(title, font=SANS, font_size=25, color=INK, line_spacing=0.7)
            b = Text(body, font=MONO, font_size=19, color=INK_SOFT, line_spacing=0.7)
            hr = VGroup(n, t).arrange(RIGHT, buff=0.28, aligned_edge=UP)
            inner = VGroup(hr, b).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
            box = RoundedRectangle(width=inner.width + 0.8, height=inner.height + 0.8,
                                   corner_radius=0.12, stroke_width=1.8,
                                   stroke_color=INK_SOFT, fill_opacity=0)
            box.move_to(inner.get_center())
            cards.add(VGroup(box, inner))
        fit(cards.arrange(RIGHT, buff=0.42))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1], shift=UP * 0.15), run_time=1.0)
            self.wait(1.3)

        point = spark("Most dashboards answer none of the three")
        self.play(Write(point), run_time=1.9)
        self.wait(4.99)


class B05_DedupePasses(Scene):
    """OUTPUT 1: two independent dedupe passes, and the overlap. 22.89s."""

    def construct(self):
        page(self)
        head = kicker("STEP 4 — QUALITY CHECK", "defective set · two dedupe passes")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        id_pass = panel("ID PASS", ["news  records[2]", "price records[4]",
                                    "reddit children[1]"], INK_SOFT, min_w=4.8)
        hl_pass = panel("HEADLINE PASS", ["news  records[1]  ← syndicated",
                                          "news  records[2]  ← also id-dup"],
                        TERRA, min_w=5.4)
        pair = VGroup(id_pass, hl_pass).arrange(RIGHT, buff=0.8, aligned_edge=UP)

        tally = Text("5 findings across 4 rows — one row trips both passes",
                     font=SANS, font_size=24, color=INK)
        flags = Text("6 flags:  3 stale  ·  3 wrong type  —  all KEPT",
                     font=SANS, font_size=24, color=TERRA)
        body = fit_src(VGroup(pair, tally, flags).arrange(DOWN, buff=0.45))
        src = source_line("live run · transform-quality-check.py --fixture-set defective")

        self.play(Create(id_pass[0]), FadeIn(id_pass[1]), run_time=1.8)
        self.wait(1.2)
        self.play(Create(hl_pass[0]), FadeIn(hl_pass[1]), run_time=1.8)
        self.wait(1.4)
        self.play(Write(tally), run_time=2.2)
        self.wait(1.0)
        self.play(FadeIn(flags, shift=UP * 0.15), FadeIn(src), run_time=1.5)
        self.wait(1.0)

        point = spark("An id-only dedupe double-weights the story")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.7)
        self.wait(6.39)


class B08_BothScored64(Scene):
    """OUTPUT 2: the centrepiece — clean and defective both report 64. 21.59s."""

    def construct(self):
        page(self)
        head = kicker("STEP 5 — THE SCORE", "same arithmetic, two very different inputs")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        def score_panel(title, flags_line, accent):
            t = Text(title, font=SANS, font_size=24, color=accent)
            big = Text("64", font=SERIF, font_size=86, color=INK)
            f = Text(flags_line, font=MONO, font_size=20, color=accent)
            inner = VGroup(t, big, f).arrange(DOWN, buff=0.26)
            box = RoundedRectangle(width=inner.width + 1.1, height=inner.height + 0.85,
                                   corner_radius=0.14, stroke_width=1.9,
                                   stroke_color=accent, fill_opacity=0)
            box.move_to(inner.get_center())
            return VGroup(box, inner)

        clean = score_panel("CLEAN SET", "3 flags", INK_SOFT)
        defect = score_panel("DEFECTIVE SET", "8 flags", TERRA)
        pair = VGroup(clean, defect).arrange(RIGHT, buff=1.0, aligned_edge=UP)

        note = Text("5 duplicates removed · 6 rows rejected · 6 quality flags — score unchanged",
                    font=SANS, font_size=23, color=TERRA)
        body = fit_src(VGroup(pair, note).arrange(DOWN, buff=0.55))
        src = source_line("live run · run-approved-tools.py --no-write · overall_score")

        self.play(Create(clean[0]), FadeIn(clean[1]), run_time=1.9)
        self.wait(1.3)
        self.play(Create(defect[0]), FadeIn(defect[1]), run_time=1.9)
        self.wait(1.6)
        self.play(Write(note), run_time=2.4)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(1.2)

        point = spark("The number is the same. The record is not.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.8)
        self.wait(5.89)


class B09_FlagCatalogue(Scene):
    """FALSIFIABILITY: half the catalogue is unreachable by the corpus. 28.99s."""

    FIRES = ["multi_quote_first_wins", "scored_row_carries_quality_flag",
             "ticker_not_derived_from_question", "untested_threshold_path",
             "scoring_params_unattributed"]
    NEVER = ["coerced_missing_field_to_zero", "coerced_non_numeric_to_zero",
             "score_is_no_data_default", "denominator_exceeds_scored_rows",
             "js_undefined_concatenated"]

    def construct(self):
        page(self)
        head = kicker("WHAT THE CORPUS CANNOT REACH",
                      "10 flags in the catalogue")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        def column(title, names, color):
            t = Text(title, font=SANS, font_size=24, color=color)
            rows = VGroup(*[chip(n, color, font_size=17, pad=0.28, height=0.34)
                            for n in names])
            rows.arrange(DOWN, buff=0.16, aligned_edge=LEFT)
            col = VGroup(t, rows).arrange(DOWN, buff=0.32)
            t.align_to(col, LEFT)
            rows.align_to(col, LEFT)
            return col

        left = column("FIRES ON THE CORPUS  ·  5", self.FIRES, INK_SOFT)
        right = column("NEVER FIRES  ·  5", self.NEVER, TERRA)
        pair = VGroup(left, right).arrange(RIGHT, buff=0.8, aligned_edge=UP)

        note = Text("the five it cannot reach are the substitution paths",
                    font=SANS, font_size=24, color=TERRA)
        body = fit_src(VGroup(pair, note).arrange(DOWN, buff=0.5))
        src = source_line("FLAG_CATALOGUE vs both fixture sets · exercised in isolation instead")

        self.play(FadeIn(left[0]), run_time=0.8)
        self.play(LaggedStart(*[Create(c[0]) for c in left[1]],
                              *[FadeIn(c[1]) for c in left[1]], lag_ratio=0.3),
                  run_time=3.4)
        self.wait(1.4)
        self.play(FadeIn(right[0]), run_time=0.8)
        self.play(LaggedStart(*[Create(c[0]) for c in right[1]],
                              *[FadeIn(c[1]) for c in right[1]], lag_ratio=0.3),
                  run_time=3.4)
        self.wait(1.6)
        self.play(Write(note), run_time=2.2)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(1.2)

        point = spark("A suite that cannot trip half your alarms proves nothing")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.9)
        self.wait(8.69)


class B10_WeekLedger(Scene):
    """SUMMARY: what closed, what is still open. 19.65s."""

    CLOSED = ["5 of 6 steps written", "18/18 defects at exact locators",
              "scores_digest stable across runs", "--no-write writes nothing"]
    OPEN = ["step 6 — the report", "scoring weights unattributed",
            "5 flags untestable by the corpus"]

    def construct(self):
        page(self)
        head = kicker("THE WEEK", "mycroft · commit 253ee74")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        def column(title, items, color):
            t = Text(title, font=SANS, font_size=25, color=INK_SOFT)
            body = VGroup(*[Text(i, font=MONO, font_size=22, color=color)
                            for i in items])
            body.arrange(DOWN, buff=0.32, aligned_edge=LEFT)
            rule = Line(LEFT * (max(body.width, t.width) / 2),
                        RIGHT * (max(body.width, t.width) / 2),
                        stroke_width=1.3, color=INK_SOFT)
            col = VGroup(t, rule, body).arrange(DOWN, buff=0.26)
            for part in (t, rule, body):
                part.align_to(col, LEFT)
            return col

        left = column("CLOSED THIS WEEK", self.CLOSED, INK)
        right = column("STILL OPEN", self.OPEN, TERRA)
        fit(VGroup(left, right).arrange(RIGHT, buff=1.4, aligned_edge=UP))

        self.play(FadeIn(left, shift=UP * 0.2), run_time=1.7)
        self.wait(1.8)
        self.play(FadeIn(right, shift=UP * 0.2), run_time=1.7)
        self.wait(1.6)

        point = spark("Five of six. Openly.")
        self.play(Write(point), run_time=1.8)
        self.wait(8.15)
