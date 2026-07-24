"""scenes.py — Manim scenes for 'Kokoro: Free Voices (With Names)'

GRAPHIC beats: B01, B02, B03, B05, B06, B07, B08, B09 (hero).
Remotion beats: B00, B04, B99.
Palette: teardown — GROUND #FFFFFF, INK #2A1A0E, CRIMSON #C8102E, ACCENT_TEAL #1F6F5C.
B09_ThreeEngines is the hero beat — dark bg #2A1A0E, EB Garamond display.

Visual signature: each GRAPHIC beat opens with a name card (VOICE_NAME + grade chip),
then the supporting diagram for that voice's lesson.
"""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "runtime" / "manim"))
from animated_graphics import *

ACCENT_TEAL = "#1F6F5C"
DARK_BG = "#2A1A0E"


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
    """Standard name card: big display name + colored grade chip [+ optional flag text]."""
    gc = _grade_color(grade)
    name_t = Text(name.upper(), font=DISPLAY, color=INK, font_size=56, weight="BOLD")

    grade_bg = Rectangle(width=1.5, height=0.62,
                         fill_color=gc, fill_opacity=1, stroke_width=0)
    grade_t = Text(grade, font=DISPLAY, color=WHITE, font_size=30, weight="BOLD")
    grade_t.move_to(grade_bg)
    chip = VGroup(grade_bg, grade_t)

    elems = [name_t, chip]
    if flag:
        flag_t = Text(flag, font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        elems.append(flag_t)

    card = VGroup(*elems)
    card.arrange(DOWN, buff=0.22)
    return card


# ──────────────────────────────────────────────────────────
# B01 — BELLA · grade A- · what Kokoro is  (15.06s)
# Name card top-billed; model card below: 82M params,
# Apache 2.0, local. Three crossed-out lines: API / meter / bill.
# Caption: "what free sounds like."
# ──────────────────────────────────────────────────────────
class B01_MeetBella(Scene):
    def construct(self):
        card = _name_card("Bella", "A-")
        card.move_to(UP * 1.9)

        caption = Text("what free sounds like.", font=SERIF, color=SLATE,
                       font_size=22, slant=ITALIC)
        caption.move_to(DOWN * 3.1)

        # Model stats row
        params = Text("Kokoro-82M", font=DISPLAY, color=INK, font_size=28, weight="BOLD")
        license_t = Text("Apache 2.0", font=MONO, color=ACCENT_TEAL, font_size=22)
        local_t = Text("runs LOCALLY", font=DISPLAY, color=INK, font_size=22)
        model_row = VGroup(params, license_t, local_t)
        model_row.arrange(RIGHT, buff=0.6)
        model_row.move_to(UP * 0.35)

        # Three crossed-out items
        no_api = Text("✗  API", font=DISPLAY, color=CRIMSON, font_size=26)
        no_meter = Text("✗  meter", font=DISPLAY, color=CRIMSON, font_size=26)
        no_bill = Text("✗  bill", font=DISPLAY, color=CRIMSON, font_size=26)
        no_row = VGroup(no_api, no_meter, no_bill)
        no_row.arrange(RIGHT, buff=1.1)
        no_row.move_to(DOWN * 1.2)

        # Rule appears with model row — distinct non-text shape state
        rule = Line(LEFT * 5.5, RIGHT * 5.5, stroke_color=HAIRLINE, stroke_width=1.5)
        rule.move_to(UP * 0.85)

        self.play(FadeIn(card), run_time=0.5)
        self.play(Create(rule), FadeIn(model_row), run_time=0.5)
        self.play(
            LaggedStart(FadeIn(no_api), FadeIn(no_meter), FadeIn(no_bill), lag_ratio=0.3),
            run_time=0.9
        )
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.5, _dur("B01") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B02 — SARAH · grade C+ · the voice is a plug  (14.63s)
# Name card. Three-engine row all feeding one pipeline.
# Caption: "downstream never knows."
# ──────────────────────────────────────────────────────────
class B02_SarahInterface(Scene):
    def construct(self):
        card = _name_card("Sarah", "C+")
        card.move_to(UP * 2.0)

        caption = Text("downstream never knows.", font=SERIF, color=SLATE,
                       font_size=22, slant=ITALIC)
        caption.move_to(DOWN * 3.1)

        # Three engine boxes
        def engine_box(label, sublabel, color):
            bg = Rectangle(width=2.8, height=1.1, fill_color=GROUND,
                           fill_opacity=1, stroke_color=color, stroke_width=2.5)
            lbl = Text(label, font=DISPLAY, color=color, font_size=22, weight="BOLD")
            sub = Text(sublabel, font=MONO, color=SLATE, font_size=16)
            grp = VGroup(lbl, sub)
            grp.arrange(DOWN, buff=0.1)
            grp.move_to(bg)
            return VGroup(bg, grp)

        el_box = engine_box("ElevenLabs", "metered", CRIMSON)
        suno_box = engine_box("Suno", "flat", SLATE)
        kok_box = engine_box("Kokoro", "FREE", ACCENT_TEAL)
        engines = VGroup(el_box, suno_box, kok_box)
        engines.arrange(RIGHT, buff=0.35)
        engines.move_to(UP * 0.45)

        # Pipeline line
        pipe_line = Line(LEFT * 5.5, RIGHT * 5.5, stroke_color=ACCENT_TEAL,
                         stroke_width=3)
        pipe_line.move_to(DOWN * 1.4)
        pipe_label = Text("mp3/beat-*.mp3  ·  render  ·  captions  ·  publish",
                          font=MONO, color=ACCENT_TEAL, font_size=17)
        pipe_label.next_to(pipe_line, DOWN, buff=0.18)

        self.play(FadeIn(card), run_time=0.5)
        self.play(
            LaggedStart(FadeIn(el_box), FadeIn(suno_box), FadeIn(kok_box), lag_ratio=0.25),
            run_time=0.8
        )
        self.play(Create(pipe_line), FadeIn(pipe_label), run_time=0.6)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.5, _dur("B02") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B03 — ADAM · grade F+ · the honest record  (12.74s)
# Name card with F+ in red, styled like a report card.
# Grade scale A→F beside it; a few example voices plotted.
# Caption: "the pack grades its own voices — and it doesn't flatter."
# ──────────────────────────────────────────────────────────
class B03_AdamGradeCard(Scene):
    def construct(self):
        card = _name_card("Adam", "F+")
        card.move_to(UP * 2.0)

        caption = Text("the pack grades its own — and it doesn't flatter.",
                       font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        caption.move_to(DOWN * 3.1)

        # Grade scale row
        grades = [("A-", ACCENT_TEAL), ("B-", ACCENT_TEAL),
                  ("C+", SLATE), ("C", SLATE), ("D-", CRIMSON), ("F+", CRIMSON)]
        chips = []
        for g, c in grades:
            bg = Rectangle(width=0.85, height=0.58, fill_color=c,
                           fill_opacity=1, stroke_width=0)
            t = Text(g, font=DISPLAY, color=WHITE, font_size=22, weight="BOLD")
            t.move_to(bg)
            chips.append(VGroup(bg, t))
        scale_row = VGroup(*chips)
        scale_row.arrange(RIGHT, buff=0.18)
        scale_row.move_to(DOWN * 0.3)

        scale_lbl = Text("pack's own grading scale →", font=MONO, color=SLATE, font_size=17)
        scale_lbl.next_to(scale_row, UP, buff=0.25)

        # Voice examples plotted below
        examples = [("af_bella", "A-", ACCENT_TEAL), ("bf_emma", "B-", ACCENT_TEAL),
                    ("am_adam", "F+", CRIMSON)]
        ex_grp = VGroup()
        for vname, vgrade, vc in examples:
            vt = Text(vname, font=MONO, color=INK, font_size=18)
            vg_bg = Rectangle(width=0.78, height=0.48, fill_color=vc,
                              fill_opacity=1, stroke_width=0)
            vg_t = Text(vgrade, font=DISPLAY, color=WHITE, font_size=18, weight="BOLD")
            vg_t.move_to(vg_bg)
            row = VGroup(vt, VGroup(vg_bg, vg_t))
            row.arrange(RIGHT, buff=0.2)
            ex_grp.add(row)
        ex_grp.arrange(RIGHT, buff=0.6)
        ex_grp.move_to(DOWN * 1.55)

        self.play(FadeIn(card), run_time=0.5)
        self.play(FadeIn(scale_lbl), FadeIn(scale_row), run_time=0.6)
        self.play(FadeIn(ex_grp), run_time=0.5)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.5, _dur("B03") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B05 — EMMA · grade B- · the roster  (12.69s)
# Name card: EMMA, B-, British flag tick.
# Roster grid: 28 English voices (4 rows × 7), grade chips.
# Caption: "casting is taste — and taste is free."
# ──────────────────────────────────────────────────────────
class B05_EmmaRoster(Scene):
    def construct(self):
        card = _name_card("Emma", "B-", "British English")
        card.move_to(UP * 2.15)

        caption = Text("casting is taste — and taste is free.", font=SERIF, color=SLATE,
                       font_size=22, slant=ITALIC)
        caption.move_to(DOWN * 3.1)

        # 28 English voices with grades (from VOICES.md verified 2026-07-13)
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
            stroke_c = ACCENT_TEAL if heard else HAIRLINE
            sw = 2.5 if heard else 0.5
            bg = Rectangle(width=1.68, height=0.52, fill_color=GROUND,
                           fill_opacity=1, stroke_color=stroke_c, stroke_width=sw)
            nm = Text(vname, font=MONO, color=INK, font_size=12)
            gd_bg = Rectangle(width=0.46, height=0.34, fill_color=gc,
                              fill_opacity=1, stroke_width=0)
            gd_t = Text(vgrade, font=DISPLAY, color=WHITE, font_size=11, weight="BOLD")
            gd_t.move_to(gd_bg)
            inner = VGroup(nm, VGroup(gd_bg, gd_t))
            inner.arrange(RIGHT, buff=0.06)
            inner.move_to(bg)
            tiles.append(VGroup(bg, inner))

        # 4 rows × 7
        rows = []
        for i in range(0, 28, 7):
            row = VGroup(*tiles[i:i+7])
            row.arrange(RIGHT, buff=0.1)
            rows.append(row)
        grid = VGroup(*rows)
        grid.arrange(DOWN, buff=0.1)
        grid.move_to(DOWN * 0.95)

        self.play(FadeIn(card), run_time=0.5)
        self.play(FadeIn(grid), run_time=0.7)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.5, _dur("B05") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B06 — GEORGE · grade C · greybox for the ears  (13.67s)
# Name card: GEORGE, C. Two-stage draft → paid flow.
# Caption: "spend taste first, credits last."
# ──────────────────────────────────────────────────────────
class B06_GeorgePreviz(Scene):
    def construct(self):
        card = _name_card("George", "C")
        card.move_to(UP * 2.05)

        caption = Text("spend taste first, credits last.", font=SERIF, color=SLATE,
                       font_size=22, slant=ITALIC)
        caption.move_to(DOWN * 3.1)

        # Stage 1: DRAFT box
        draft_bg = Rectangle(width=3.2, height=1.4, fill_color=GROUND,
                             fill_opacity=1, stroke_color=ACCENT_TEAL, stroke_width=2)
        draft_lbl = Text("DRAFT", font=DISPLAY, color=ACCENT_TEAL,
                         font_size=26, weight="BOLD")
        draft_sub = Text("Kokoro · $0.00", font=MONO, color=SLATE, font_size=18)
        draft_inner = VGroup(draft_lbl, draft_sub)
        draft_inner.arrange(DOWN, buff=0.12)
        draft_inner.move_to(draft_bg)
        draft_box = VGroup(draft_bg, draft_inner)
        draft_box.move_to(LEFT * 3.0 + DOWN * 0.8)

        arrow = Arrow(LEFT * 0.9 + DOWN * 0.8, RIGHT * 0.9 + DOWN * 0.8,
                      stroke_color=INK, stroke_width=3, buff=0.1)

        # Stage 2: PAID box (locked look)
        paid_bg = Rectangle(width=3.2, height=1.4, fill_color=GROUND,
                            fill_opacity=1, stroke_color=SLATE, stroke_width=1.5)
        paid_lbl = Text("PAID VOICE PASS", font=DISPLAY, color=SLATE,
                        font_size=20, weight="BOLD")
        paid_sub = Text("ElevenLabs / Suno", font=MONO, color=SLATE, font_size=18)
        paid_inner = VGroup(paid_lbl, paid_sub)
        paid_inner.arrange(DOWN, buff=0.12)
        paid_inner.move_to(paid_bg)
        paid_box = VGroup(paid_bg, paid_inner)
        paid_box.move_to(RIGHT * 3.0 + DOWN * 0.8)

        # "real timings" annotation above arrow
        timing_lbl = Text("real durations  ·  full conform  ·  watchable review",
                          font=MONO, color=SLATE, font_size=15)
        timing_lbl.move_to(DOWN * 0.18)

        self.play(FadeIn(card), run_time=0.5)
        self.play(FadeIn(draft_box), run_time=0.5)
        self.play(GrowArrow(arrow), FadeIn(timing_lbl), run_time=0.5)
        self.play(FadeIn(paid_box), run_time=0.5)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.5, _dur("B06") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B07 — PUCK · grade C+ · the catch  (11.29s)
# Name card: PUCK, C+. Balance: free advantages LEFT vs
# no cloning RIGHT.
# Caption: "when the video is your name, the voice is yours."
# ──────────────────────────────────────────────────────────
class B07_PuckTradeoff(Scene):
    def construct(self):
        card = _name_card("Puck", "C+")
        card.move_to(UP * 2.0)

        caption = Text("when the video is your name, the voice is yours.",
                       font=SERIF, color=SLATE, font_size=19, slant=ITALIC)
        caption.move_to(DOWN * 3.1)

        # Left: free advantages
        free_hdr = Text("FREE", font=DISPLAY, color=ACCENT_TEAL,
                        font_size=24, weight="BOLD")
        free_pts = ["free", "28 voices", "local · instant"]
        free_lines = VGroup(*[Text(p, font=SERIF, color=INK, font_size=20)
                               for p in free_pts])
        free_lines.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        free_col = VGroup(free_hdr, free_lines)
        free_col.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        free_col.move_to(LEFT * 3.5 + DOWN * 0.9)

        divider = Line(UP * 1.2 + DOWN * 0, DOWN * 2.2, stroke_color=HAIRLINE, stroke_width=1.5)
        divider.move_to(DOWN * 0.8)

        # Right: the catch
        catch_hdr = Text("NO CLONING", font=DISPLAY, color=CRIMSON,
                         font_size=24, weight="BOLD")
        catch_sub = Text("none of us is you", font=SERIF, color=INK, font_size=20)
        catch_col = VGroup(catch_hdr, catch_sub)
        catch_col.arrange(DOWN, buff=0.28)
        catch_col.move_to(RIGHT * 3.0 + DOWN * 0.9)

        self.play(FadeIn(card), run_time=0.5)
        self.play(FadeIn(free_col), run_time=0.5)
        self.play(Create(divider), FadeIn(catch_col), run_time=0.5)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.5, _dur("B07") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B08 — SANTA · grade D- · the wink  (5.85s — short)
# Name card: SANTA, D-. Holly sprig emoji. Played completely
# straight in house style — that IS the joke.
# Caption: "you get what you pay for — except you didn't pay."
# ──────────────────────────────────────────────────────────
class B08_SantaWink(Scene):
    def construct(self):
        card = _name_card("Santa", "D-")
        card.move_to(UP * 1.0)

        caption = Text("you get what you pay for — except you didn't pay.",
                       font=SERIF, color=SLATE, font_size=22, slant=ITALIC)
        caption.move_to(DOWN * 1.8)

        # Thin border rule — distinct non-text shape between card and caption
        rule = Line(LEFT * 3.5, RIGHT * 3.5, stroke_color=HAIRLINE, stroke_width=1.5)
        rule.move_to(DOWN * 0.65)

        self.play(FadeIn(card), run_time=0.5)
        self.play(Create(rule), FadeIn(caption), run_time=0.4)
        self.wait(max(0.3, _dur("B08") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B09 — THREE ENGINES  (16.6s) — HERO BEAT
# Dark bg #2A1A0E. EB Garamond display. Three columns:
# METERED / FLAT / FREE. One teal line at bottom.
# ──────────────────────────────────────────────────────────
class B09_ThreeEngines(Scene):
    def construct(self):
        self.camera.background_color = DARK_BG

        # Hero title
        title = Text("THE ROSTER", font=DISPLAY, color=WHITE,
                     font_size=34, weight="BOLD")
        title.move_to(UP * 3.0)

        # Three columns
        def engine_col(engine_lbl, detail1, detail2, accent):
            hdr = Text(engine_lbl, font=DISPLAY, color=accent,
                       font_size=30, weight="BOLD")
            d1 = Text(detail1, font=SERIF, color=WHITE, font_size=22, slant=ITALIC)
            d2 = Text(detail2, font=SERIF, color=SLATE, font_size=18)
            col = VGroup(hdr, d1, d2)
            col.arrange(DOWN, buff=0.3)
            return col

        metered_col = engine_col("METERED", "the clone, steadiest",
                                 "priced by the character", CRIMSON)
        flat_col = engine_col("FLAT", "your voice through Suno",
                              "one generation per video", WHITE)
        free_col = engine_col("FREE", "the named cast",
                              "twenty-eight voices, $0", ACCENT_TEAL)

        cols = VGroup(metered_col, flat_col, free_col)
        cols.arrange(RIGHT, buff=1.5)
        cols.move_to(DOWN * 0.2)

        # Dividers
        div1 = Line(UP * 1.6, DOWN * 1.8, stroke_color=SLATE, stroke_width=1)
        div1.move_to(metered_col.get_right() + RIGHT * 0.75)
        div2 = Line(UP * 1.6, DOWN * 1.8, stroke_color=SLATE, stroke_width=1)
        div2.move_to(flat_col.get_right() + RIGHT * 0.75)

        # Teal closing line
        close_line = Text("WHO SPEAKS IS TASTE — AND TASTE IS YOURS.",
                          font=SERIF, color=ACCENT_TEAL, font_size=22, slant=ITALIC)
        close_line.move_to(DOWN * 2.8)

        # Title rule appears first — distinct shape state before columns+dividers
        title_rule = Line(LEFT * 5.5, RIGHT * 5.5, stroke_color=SLATE, stroke_width=1)
        title_rule.next_to(title, DOWN, buff=0.3)

        self.play(FadeIn(title), Create(title_rule), run_time=0.5)
        self.play(
            LaggedStart(FadeIn(metered_col), FadeIn(flat_col), FadeIn(free_col),
                        lag_ratio=0.3),
            Create(div1),
            run_time=1.0
        )
        self.play(Create(div2), FadeIn(close_line), run_time=0.6)
        self.wait(max(0.5, _dur("B09") - getattr(self, 'time', 0.0)))
