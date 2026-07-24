"""scenes.py — Manim portrait (9:16) scenes for 'Kokoro: Free Voices (With Names)' short.

GRAPHIC beats: B01, B02, B03, B05, B06, B07, B08, B09.
Remotion beats: B00, B04, B99 (ONDA CHECK → 916 compositions).
Palette: teardown — GROUND #FFFFFF, INK #2A1A0E, CRIMSON #C8102E, ACCENT_TEAL #1F6F5C.

Portrait frame: 1080×1920 (9:16). Coordinate space: x ∈ [-2.25, 2.25], y ∈ [-4.0, 4.0].
Safe area: ±1.9x / ±3.3y. Do NOT set config.frame_width/height inside construct().
"""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "runtime" / "manim"))
from animated_graphics import *

ACCENT_TEAL = "#1F6F5C"
DARK_BG = "#2A1A0E"
SAFE_X = 1.9


def _dur(bid):
    bs = pathlib.Path(__file__).parent / "beat_sheet.json"
    if not bs.exists():
        return 0.0
    for b in json.loads(bs.read_text()).get("beats", []):
        if b["beat_id"] == bid:
            return float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0.0)
    return 0.0


def _grade_color(grade: str) -> str:
    g = grade.strip()[0].upper()
    if g in ("A", "B"):
        return ACCENT_TEAL
    if g == "C":
        return SLATE
    return CRIMSON


def _name_card(name: str, grade: str, flag: str = "") -> VGroup:
    gc = _grade_color(grade)
    name_t = Text(name.upper(), font=DISPLAY, color=INK, font_size=40, weight="BOLD")
    grade_bg = Rectangle(width=1.1, height=0.50, fill_color=gc, fill_opacity=1, stroke_width=0)
    grade_t = Text(grade, font=DISPLAY, color=WHITE, font_size=22, weight="BOLD")
    grade_t.move_to(grade_bg)
    chip = VGroup(grade_bg, grade_t)
    elems = [name_t, chip]
    if flag:
        flag_t = Text(flag, font=SERIF, color=SLATE, font_size=14, slant=ITALIC)
        elems.append(flag_t)
    card = VGroup(*elems)
    card.arrange(DOWN, buff=0.16)
    return card


# ─────────────────────────────────────────────────────────
# B01 — BELLA · A- · what Kokoro is
# ─────────────────────────────────────────────────────────
class B01_MeetBella(Scene):
    def construct(self):
        card = _name_card("Bella", "A-")
        card.move_to(UP * 2.5)

        rule = Line(LEFT * SAFE_X, RIGHT * SAFE_X, stroke_color=HAIRLINE, stroke_width=1.5)
        rule.move_to(UP * 1.6)

        params = Text("Kokoro-82M", font=DISPLAY, color=INK, font_size=20, weight="BOLD")
        license_t = Text("Apache 2.0", font=MONO, color=ACCENT_TEAL, font_size=17)
        local_t = Text("runs LOCALLY", font=DISPLAY, color=INK, font_size=17)
        model_col = VGroup(params, license_t, local_t)
        model_col.arrange(DOWN, buff=0.16)
        model_col.move_to(UP * 0.7)

        no_api = Text("✗  API", font=DISPLAY, color=CRIMSON, font_size=20)
        no_meter = Text("✗  meter", font=DISPLAY, color=CRIMSON, font_size=20)
        no_bill = Text("✗  bill", font=DISPLAY, color=CRIMSON, font_size=20)
        no_col = VGroup(no_api, no_meter, no_bill)
        no_col.arrange(DOWN, buff=0.20)
        no_col.move_to(DOWN * 0.7)

        caption = Text("what free sounds like.", font=SERIF, color=SLATE,
                       font_size=18, slant=ITALIC)
        caption.move_to(DOWN * 2.7)

        self.play(FadeIn(card), run_time=0.5)
        self.play(Create(rule), FadeIn(model_col), run_time=0.5)
        self.play(
            LaggedStart(FadeIn(no_api), FadeIn(no_meter), FadeIn(no_bill), lag_ratio=0.3),
            run_time=0.9
        )
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.5, _dur("B01") - getattr(self, 'time', 0.0)))


# ─────────────────────────────────────────────────────────
# B02 — SARAH · C+ · the voice is a plug
# ─────────────────────────────────────────────────────────
class B02_SarahInterface(Scene):
    def construct(self):
        card = _name_card("Sarah", "C+")
        card.move_to(UP * 2.5)

        def engine_box(label, sublabel, color):
            bg = Rectangle(width=3.6, height=0.82,
                           fill_color=GROUND, fill_opacity=1,
                           stroke_color=color, stroke_width=2)
            lbl = Text(label, font=DISPLAY, color=color, font_size=17, weight="BOLD")
            sub = Text(sublabel, font=MONO, color=SLATE, font_size=13)
            inner = VGroup(lbl, sub)
            inner.arrange(DOWN, buff=0.08)
            inner.move_to(bg)
            return VGroup(bg, inner)

        el_box = engine_box("ElevenLabs", "metered", CRIMSON)
        suno_box = engine_box("Suno", "flat", SLATE)
        kok_box = engine_box("Kokoro", "FREE", ACCENT_TEAL)
        engines = VGroup(el_box, suno_box, kok_box)
        engines.arrange(DOWN, buff=0.16)
        engines.move_to(DOWN * 0.1)

        pipe_line = Line(LEFT * SAFE_X, RIGHT * SAFE_X,
                         stroke_color=ACCENT_TEAL, stroke_width=2.5)
        pipe_line.move_to(DOWN * 2.1)
        pipe_label = Text("mp3/ → render → publish",
                          font=MONO, color=ACCENT_TEAL, font_size=13)
        pipe_label.next_to(pipe_line, DOWN, buff=0.12)

        caption = Text("downstream never knows.", font=SERIF, color=SLATE,
                       font_size=17, slant=ITALIC)
        caption.move_to(DOWN * 3.0)

        self.play(FadeIn(card), run_time=0.5)
        self.play(
            LaggedStart(FadeIn(el_box), FadeIn(suno_box), FadeIn(kok_box), lag_ratio=0.25),
            run_time=0.8
        )
        self.play(Create(pipe_line), FadeIn(pipe_label), run_time=0.6)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.5, _dur("B02") - getattr(self, 'time', 0.0)))


# ─────────────────────────────────────────────────────────
# B03 — ADAM · F+ · the honest record
# ─────────────────────────────────────────────────────────
class B03_AdamGradeCard(Scene):
    def construct(self):
        card = _name_card("Adam", "F+")
        card.move_to(UP * 2.5)

        def chip_row(grades_list):
            chips = []
            for g, c in grades_list:
                bg = Rectangle(width=0.72, height=0.46,
                               fill_color=c, fill_opacity=1, stroke_width=0)
                t = Text(g, font=DISPLAY, color=WHITE, font_size=18, weight="BOLD")
                t.move_to(bg)
                chips.append(VGroup(bg, t))
            row = VGroup(*chips)
            row.arrange(RIGHT, buff=0.12)
            return row

        row1 = chip_row([("A-", ACCENT_TEAL), ("B-", ACCENT_TEAL), ("C+", SLATE)])
        row2 = chip_row([("C", SLATE), ("D-", CRIMSON), ("F+", CRIMSON)])
        scale = VGroup(row1, row2)
        scale.arrange(DOWN, buff=0.14)
        scale.move_to(UP * 0.65)

        scale_lbl = Text("pack's grading scale", font=MONO, color=SLATE, font_size=15)
        scale_lbl.next_to(scale, UP, buff=0.18)

        examples = [("af_bella", "A-", ACCENT_TEAL),
                    ("bf_emma", "B-", ACCENT_TEAL),
                    ("am_adam", "F+", CRIMSON)]
        ex_grp = VGroup()
        for vname, vgrade, vc in examples:
            vt = Text(vname, font=MONO, color=INK, font_size=15)
            vg_bg = Rectangle(width=0.68, height=0.40,
                              fill_color=vc, fill_opacity=1, stroke_width=0)
            vg_t = Text(vgrade, font=DISPLAY, color=WHITE, font_size=14, weight="BOLD")
            vg_t.move_to(vg_bg)
            row = VGroup(vt, VGroup(vg_bg, vg_t))
            row.arrange(RIGHT, buff=0.18)
            ex_grp.add(row)
        ex_grp.arrange(DOWN, buff=0.22)
        ex_grp.move_to(DOWN * 0.9)

        caption = Text("the pack grades its own —\nand it doesn't flatter.",
                       font=SERIF, color=SLATE, font_size=17, slant=ITALIC)
        caption.move_to(DOWN * 2.8)

        self.play(FadeIn(card), run_time=0.5)
        self.play(FadeIn(scale_lbl), FadeIn(scale), run_time=0.6)
        self.play(FadeIn(ex_grp), run_time=0.5)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.5, _dur("B03") - getattr(self, 'time', 0.0)))


# ─────────────────────────────────────────────────────────
# B05 — EMMA · B- · the roster
# ─────────────────────────────────────────────────────────
class B05_EmmaRoster(Scene):
    def construct(self):
        card = _name_card("Emma", "B-", "British English")
        card.move_to(UP * 2.3)

        ROSTER = [
            ("af_alloy", "C+"), ("af_aoede", "B-"), ("af_bella", "A-"),
            ("af_heart", "A-"), ("af_jessica", "B+"), ("af_kore", "B"),
            ("af_nicole", "B-"), ("af_nova", "B"), ("af_river", "C+"),
            ("af_sarah", "C+"), ("af_sky", "C"),
            ("am_adam", "F+"), ("am_echo", "C"), ("am_eric", "C+"),
            ("am_fenrir", "B+"), ("am_liam", "C+"), ("am_michael", "C+"),
            ("af_kore", "C"), ("am_puck", "C+"), ("am_santa", "D-"),
            ("bf_alice", "B"), ("bf_emma", "B-"), ("bf_isabella", "C+"),
            ("bf_lily", "B-"),
            ("bm_daniel", "B+"), ("bm_fable", "B"), ("bm_george", "C"),
            ("bm_lewis", "C+"),
        ]
        HEARD = {"af_bella", "af_sarah", "am_adam", "bf_emma"}

        tiles = []
        for vname, vgrade in ROSTER:
            gc = _grade_color(vgrade)
            heard = vname in HEARD
            sw = 2.0 if heard else 0.5
            sc = ACCENT_TEAL if heard else HAIRLINE
            bg = Rectangle(width=0.88, height=0.40,
                           fill_color=GROUND, fill_opacity=1,
                           stroke_color=sc, stroke_width=sw)
            nm = Text(vname, font=MONO, color=INK, font_size=9)
            gd_bg = Rectangle(width=0.24, height=0.20,
                              fill_color=gc, fill_opacity=1, stroke_width=0)
            gd_t = Text(vgrade, font=DISPLAY, color=WHITE, font_size=8, weight="BOLD")
            gd_t.move_to(gd_bg)
            # force name to fit inside tile (leave room for grade chip + buff)
            if nm.width > 0.54:
                nm.scale_to_fit_width(0.54)
            inner = VGroup(nm, VGroup(gd_bg, gd_t))
            inner.arrange(RIGHT, buff=0.06)
            inner.move_to(bg)
            tiles.append(VGroup(bg, inner))

        rows = []
        for i in range(0, 28, 4):
            row = VGroup(*tiles[i:i+4])
            row.arrange(RIGHT, buff=0.07)
            rows.append(row)
        grid = VGroup(*rows)
        grid.arrange(DOWN, buff=0.07)
        grid.move_to(DOWN * 0.7)

        caption = Text("casting is taste — and taste is free.", font=SERIF, color=SLATE,
                       font_size=16, slant=ITALIC)
        caption.move_to(DOWN * 3.0)

        self.play(FadeIn(card), run_time=0.5)
        self.play(FadeIn(grid), run_time=0.7)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.5, _dur("B05") - getattr(self, 'time', 0.0)))


# ─────────────────────────────────────────────────────────
# B06 — GEORGE · C · greybox for the ears
# ─────────────────────────────────────────────────────────
class B06_GeorgePreviz(Scene):
    def construct(self):
        card = _name_card("George", "C")
        card.move_to(UP * 2.5)

        draft_bg = Rectangle(width=3.6, height=0.82,
                             fill_color=GROUND, fill_opacity=1,
                             stroke_color=ACCENT_TEAL, stroke_width=2)
        draft_lbl = Text("DRAFT", font=DISPLAY, color=ACCENT_TEAL, font_size=22, weight="BOLD")
        draft_sub = Text("Kokoro · $0.00", font=MONO, color=SLATE, font_size=15)
        draft_inner = VGroup(draft_lbl, draft_sub)
        draft_inner.arrange(DOWN, buff=0.10)
        draft_inner.move_to(draft_bg)
        draft_box = VGroup(draft_bg, draft_inner)
        draft_box.move_to(UP * 1.2)

        arrow = Arrow(UP * 0.3, DOWN * 0.3,
                      stroke_color=INK, stroke_width=2.5, buff=0.1)

        timing_lbl = Text("real durations\nwatchable review", font=MONO, color=SLATE, font_size=12)
        timing_lbl.next_to(arrow, RIGHT, buff=0.14)

        paid_bg = Rectangle(width=3.6, height=0.82,
                            fill_color=GROUND, fill_opacity=1,
                            stroke_color=SLATE, stroke_width=1.5)
        paid_lbl = Text("PAID VOICE PASS", font=DISPLAY, color=SLATE, font_size=17, weight="BOLD")
        paid_sub = Text("ElevenLabs / Suno", font=MONO, color=SLATE, font_size=15)
        paid_inner = VGroup(paid_lbl, paid_sub)
        paid_inner.arrange(DOWN, buff=0.10)
        paid_inner.move_to(paid_bg)
        paid_box = VGroup(paid_bg, paid_inner)
        paid_box.move_to(DOWN * 1.0)

        caption = Text("spend taste first, credits last.", font=SERIF, color=SLATE,
                       font_size=17, slant=ITALIC)
        caption.move_to(DOWN * 2.5)

        self.play(FadeIn(card), run_time=0.5)
        self.play(FadeIn(draft_box), run_time=0.5)
        self.play(GrowArrow(arrow), FadeIn(timing_lbl), run_time=0.5)
        self.play(FadeIn(paid_box), run_time=0.5)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.5, _dur("B06") - getattr(self, 'time', 0.0)))


# ─────────────────────────────────────────────────────────
# B07 — PUCK · C+ · the catch
# ─────────────────────────────────────────────────────────
class B07_PuckTradeoff(Scene):
    def construct(self):
        card = _name_card("Puck", "C+")
        card.move_to(UP * 2.5)

        rule = Line(LEFT * SAFE_X, RIGHT * SAFE_X, stroke_color=HAIRLINE, stroke_width=1.5)
        rule.move_to(UP * 1.6)

        free_hdr = Text("FREE", font=DISPLAY, color=ACCENT_TEAL, font_size=22, weight="BOLD")
        free_pts = ["✓  free", "✓  28 voices", "✓  local · instant"]
        free_lines = VGroup(*[Text(p, font=SERIF, color=INK, font_size=17)
                               for p in free_pts])
        free_lines.arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        free_col = VGroup(free_hdr, free_lines)
        free_col.arrange(DOWN, buff=0.20, aligned_edge=LEFT)
        free_col.move_to(UP * 0.5)

        divider = Line(LEFT * SAFE_X, RIGHT * SAFE_X, stroke_color=HAIRLINE, stroke_width=1.0)
        divider.move_to(DOWN * 0.7)

        catch_hdr = Text("NO CLONING", font=DISPLAY, color=CRIMSON, font_size=20, weight="BOLD")
        catch_sub = Text("none of us is you", font=SERIF, color=INK, font_size=17)
        catch_col = VGroup(catch_hdr, catch_sub)
        catch_col.arrange(DOWN, buff=0.18)
        catch_col.move_to(DOWN * 1.55)

        caption = Text("when the video is your name,\nthe voice is yours.",
                       font=SERIF, color=SLATE, font_size=17, slant=ITALIC)
        caption.move_to(DOWN * 2.8)

        self.play(FadeIn(card), run_time=0.5)
        self.play(Create(rule), FadeIn(free_col), run_time=0.5)
        self.play(Create(divider), FadeIn(catch_col), run_time=0.5)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.5, _dur("B07") - getattr(self, 'time', 0.0)))


# ─────────────────────────────────────────────────────────
# B08 — SANTA · D- · the wink  (5.85s)
# ─────────────────────────────────────────────────────────
class B08_SantaWink(Scene):
    def construct(self):
        card = _name_card("Santa", "D-")
        card.move_to(UP * 1.5)

        rule = Line(LEFT * SAFE_X, RIGHT * SAFE_X, stroke_color=HAIRLINE, stroke_width=1.5)
        rule.move_to(DOWN * 0.2)

        caption = Text("you get what you pay for —\nexcept you didn't pay.",
                       font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        caption.move_to(DOWN * 1.4)

        self.play(FadeIn(card), run_time=0.5)
        self.play(Create(rule), FadeIn(caption), run_time=0.4)
        self.wait(max(0.3, _dur("B08") - getattr(self, 'time', 0.0)))


# ─────────────────────────────────────────────────────────
# B09 — THREE ENGINES (portrait, hero, dark bg)
# ─────────────────────────────────────────────────────────
class B09_ThreeEngines(Scene):
    def construct(self):
        self.camera.background_color = DARK_BG

        title = Text("THE ROSTER", font=DISPLAY, color=WHITE, font_size=24, weight="BOLD")
        title.move_to(UP * 3.0)

        title_rule = Line(LEFT * SAFE_X, RIGHT * SAFE_X, stroke_color=SLATE, stroke_width=1)
        title_rule.next_to(title, DOWN, buff=0.2)

        def engine_col(engine_lbl, detail1, detail2, accent):
            hdr = Text(engine_lbl, font=DISPLAY, color=accent, font_size=20, weight="BOLD")
            d1 = Text(detail1, font=SERIF, color=WHITE, font_size=15, slant=ITALIC)
            d2 = Text(detail2, font=SERIF, color=SLATE, font_size=13)
            col = VGroup(hdr, d1, d2)
            col.arrange(DOWN, buff=0.18)
            return col

        metered = engine_col("METERED", "the clone, steadiest", "priced by character", CRIMSON)
        flat = engine_col("FLAT", "your voice, Suno", "one generation per video", WHITE)
        free = engine_col("FREE", "the named cast", "twenty-eight · $0", ACCENT_TEAL)

        cols = VGroup(metered, flat, free)
        cols.arrange(DOWN, buff=0.55)
        cols.move_to(ORIGIN)

        div1 = Line(LEFT * SAFE_X, RIGHT * SAFE_X, stroke_color=SLATE, stroke_width=0.8)
        div1.move_to(metered.get_bottom() + DOWN * 0.28)
        div2 = Line(LEFT * SAFE_X, RIGHT * SAFE_X, stroke_color=SLATE, stroke_width=0.8)
        div2.move_to(flat.get_bottom() + DOWN * 0.28)

        close_line = Text("WHO SPEAKS IS TASTE —\nAND TASTE IS YOURS.",
                          font=SERIF, color=ACCENT_TEAL, font_size=17, slant=ITALIC)
        close_line.move_to(DOWN * 2.9)

        self.play(FadeIn(title), Create(title_rule), run_time=0.5)
        self.play(FadeIn(metered), Create(div1), run_time=0.6)
        self.play(FadeIn(flat), Create(div2), run_time=0.5)
        self.play(FadeIn(free), run_time=0.5)
        self.play(FadeIn(close_line), run_time=0.6)
        self.wait(max(0.5, _dur("B09") - getattr(self, 'time', 0.0)))
