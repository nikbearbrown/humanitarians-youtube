"""scenes.py — Manim portrait (9:16) scenes for 'Suno vs 11 Labs Cost Test' short.

GRAPHIC beats: B00A, B01, B02, B04, B05, B08 (Suno short) / B10 (11labs short).
Remotion beats: B00, B03, B06, B11, B99.
Palette: teardown — GROUND #FFFFFF, INK #2A1A0E, CRIMSON #C8102E, ACCENT_TEAL #1F6F5C.
B10_TheSplit is the hero beat — dark bg #2A1A0E, white title, teal subtitle.

Portrait coordinate system: x ∈ [-2.25, 2.25], y ∈ [-4.0, 4.0].
Safe area: x ±1.95, y ±3.4. All elements stay within safe area.
No two-column left/right layouts — everything stacked vertically.
"""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "runtime" / "manim"))
from animated_graphics import *

ACCENT_TEAL = "#1F6F5C"


def _dur(bid):
    bs = pathlib.Path(__file__).parent / "beat_sheet.json"
    if not bs.exists():
        return 0.0
    for b in json.loads(bs.read_text()).get("beats", []):
        if b["beat_id"] == bid:
            return float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0.0)
    return 0.0


# ──────────────────────────────────────────────────────────
# B00A — ANNOUNCE
# Reads slug from this short's beat_sheet.json to label
# variant correctly: SUNO VOICE or ELEVENLABS VOICE.
# Portrait: title top, variant label middle, note lower.
# ──────────────────────────────────────────────────────────
class B00A_Announce(Scene):
    def construct(self):
        bs_path = pathlib.Path(__file__).parent / "beat_sheet.json"
        slug = json.loads(bs_path.read_text()).get("metadata", {}).get("slug", "") if bs_path.exists() else ""
        if "11labs" in slug:
            variant_lbl = "ELEVENLABS VOICE"
            other_lbl   = "Suno version in description"
            accent      = CRIMSON
        else:
            variant_lbl = "SUNO VOICE"
            other_lbl   = "ElevenLabs version in description"
            accent      = ACCENT_TEAL

        title = Text("SUNO VS 11 LABS", font=DISPLAY, color=INK,
                     font_size=38, weight="BOLD")
        title.move_to(UP * 1.6)

        sub = Text(variant_lbl, font=SERIF, color=accent,
                   font_size=24, slant=ITALIC)
        sub.move_to(UP * 0.6)

        note = Text(other_lbl, font=MONO, color=SLATE, font_size=16)
        note.move_to(DOWN * 0.3)

        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.5, _dur("B00A") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B01 — THE METER (~11s)
# Portrait: tank centered in top half, beat counter below,
# bill line below that, caption at bottom.
# Caption: "metered: the more you talk, the more you pay."
# ──────────────────────────────────────────────────────────
class B01_TheMeter(Scene):
    def construct(self):
        chip = LabelChip("THE ITCH", accent=CRIMSON, size=17)
        chip.to_corner(UL, buff=0.55)
        self.play(FadeIn(chip), run_time=0.4)

        # Tank label + rectangle centered in top half
        tank_label = Text("ELEVENLABS CREDITS", font=DISPLAY, color=INK,
                          font_size=18, weight="MEDIUM")
        tank_label.move_to(UP * 2.6)

        tank_bg = Rectangle(width=2.6, height=2.0, fill_color=GROUND,
                            fill_opacity=1, stroke_color=INK, stroke_width=2)
        tank_bg.move_to(UP * 1.4)

        fill_full = Rectangle(width=2.4, height=1.8, fill_color=ACCENT_TEAL,
                               fill_opacity=0.35, stroke_width=0)
        fill_full.move_to(tank_bg).align_to(tank_bg, DOWN).shift(UP * 0.1)

        fill_drain = Rectangle(width=2.4, height=0.25, fill_color=ACCENT_TEAL,
                                fill_opacity=0.35, stroke_width=0)
        fill_drain.move_to(tank_bg).align_to(tank_bg, DOWN).shift(UP * 0.1)

        self.play(FadeIn(tank_label), FadeIn(tank_bg), FadeIn(fill_full), run_time=0.5)
        self.play(Transform(fill_full, fill_drain), run_time=1.5)

        # Beat counter ticking up — below the tank
        beats = ["B00", "B01", "B02", "…", "B99"]
        counter_lbl = Text("beats voiced:", font=MONO, color=INK, font_size=20)
        counter_lbl.move_to(DOWN * 0.4)
        self.play(FadeIn(counter_lbl), run_time=0.3)

        prev = None
        for i, bid in enumerate(beats):
            t = Text(bid, font=MONO, color=CRIMSON if bid == "B99" else INK, font_size=26)
            t.next_to(counter_lbl, DOWN, buff=0.28)
            if prev:
                self.play(ReplacementTransform(prev, t), run_time=0.22)
            else:
                self.play(FadeIn(t), run_time=0.22)
            prev = t

        # Bill line — below counter
        bill_lbl = Text("bill", font=MONO, color=CRIMSON, font_size=18)
        bill_lbl.move_to(DOWN * 1.8)
        bill_line = Line(
            LEFT * 1.2 + DOWN * 2.1,
            LEFT * 1.2 + DOWN * 2.1,
            stroke_color=CRIMSON, stroke_width=3,
        )
        self.play(FadeIn(bill_lbl), run_time=0.3)
        self.play(
            bill_line.animate.put_start_and_end_on(
                LEFT * 1.4 + DOWN * 2.2, RIGHT * 1.4 + DOWN * 1.6
            ),
            run_time=1.0,
        )
        self.add(bill_line)

        caption = SerifLabel("metered: the more you talk, the more you pay.",
                             accent=CRIMSON, size=19)
        caption.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(max(0.5, _dur("B01") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B02 — THE CHALLENGER (~15s)
# Portrait: SUNO card centered, all elements stacked vertically.
# Title → subtitle → 3 waveform bars → stamp → footnote.
# Caption: "flat: the bill doesn't scale with the word count."
# ──────────────────────────────────────────────────────────
class B02_TheChallenger(Scene):
    def construct(self):
        chip = LabelChip("THE CHALLENGER", accent=ACCENT_TEAL, size=17)
        chip.to_corner(UL, buff=0.55)
        self.play(FadeIn(chip), run_time=0.4)

        # Card background — tall portrait card
        card = Rectangle(width=3.4, height=5.0, fill_color=GROUND,
                         fill_opacity=1, stroke_color=ACCENT_TEAL, stroke_width=2)
        card.move_to(UP * 0.6)

        # Title
        title = Text("SUNO", font=DISPLAY, color=INK, font_size=40, weight="BOLD")
        title.move_to(UP * 2.6)

        subtitle = Text("your voice, uploaded once", font=SERIF, color=SLATE,
                        font_size=19, slant=ITALIC)
        subtitle.next_to(title, DOWN, buff=0.2)

        self.play(FadeIn(card), FadeIn(title), run_time=0.6)
        self.play(FadeIn(subtitle), run_time=0.4)

        # Waveform hint — three bars centered
        bar_h = [0.55, 0.82, 0.48]
        bars = VGroup(*[
            Rectangle(width=0.22, height=h, fill_color=ACCENT_TEAL,
                      fill_opacity=0.7, stroke_width=0).move_to(
                          (LEFT * 0.38 + RIGHT * i * 0.40) + UP * 1.5
                      )
            for i, h in enumerate(bar_h)
        ])
        self.play(FadeIn(bars), run_time=0.5)

        # Flat-rate stamp — sized from text, centered
        stamp_txt = Text("ONE GEN ≈ ONE VIDEO'S NARRATION",
                         font=DISPLAY, color=WHITE, font_size=14, weight="MEDIUM")
        stamp_txt.move_to(UP * 0.6)
        stamp_bg = Rectangle(
            width=stamp_txt.width + 0.5,
            height=stamp_txt.height + 0.38,
            fill_color=ACCENT_TEAL, fill_opacity=1, stroke_width=0,
        )
        stamp_bg.move_to(stamp_txt)
        stamp_bg._qc_intentional = True
        self.play(FadeIn(stamp_bg), FadeIn(stamp_txt), run_time=0.6)

        # Honest footnote in red — below stamp
        note = Text("leans speak-song — clear for spoken word",
                    font=SERIF, color=CRIMSON, font_size=15)
        note.move_to(UP * 0.0)
        self.play(FadeIn(note), run_time=0.4)

        caption = SerifLabel("flat: the bill doesn't scale with the word count.",
                             accent=ACCENT_TEAL, size=19)
        caption.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(max(0.5, _dur("B02") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B04 — THE [SPOKEN WORD] TAG (~12s)
# Portrait: CORRECT (tag per beat) in top half, horizontal
# rule dividing, WRONG (tag once) in bottom half.
# No side-by-side — top/bottom split.
# Caption: "one style note is not enough — tag rides above every beat."
# ──────────────────────────────────────────────────────────
class B04_SpokenWordTag(Scene):
    def construct(self):
        chip = LabelChip("THE TAG", accent=ACCENT_TEAL, size=17)
        chip.to_corner(UL, buff=0.55)
        self.play(FadeIn(chip), run_time=0.4)

        # TOP HALF: CORRECT — tag above every beat
        correct_lbl = Text("✓  tag per beat", font=DISPLAY, color=ACCENT_TEAL,
                           font_size=18, weight="MEDIUM")
        correct_lbl.move_to(UP * 2.8)
        self.play(FadeIn(correct_lbl), run_time=0.4)

        tag = "[spoken word]"
        beat_texts = ["Every beat, every word…", "No drift, no melody…", "Stays speaking."]
        for i, bt in enumerate(beat_texts):
            row_tag = Text(tag, font=MONO, color=ACCENT_TEAL, font_size=15)
            row_beat = Text(bt, font=SERIF, color=INK, font_size=16)
            row = VGroup(row_tag, row_beat).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
            row.move_to(LEFT * 0.1 + UP * (2.2 - i * 0.56))
            self.play(FadeIn(row), run_time=0.25)

        # Horizontal divider rule
        div = Line(LEFT * 1.9 + UP * 0.4, RIGHT * 1.9 + UP * 0.4,
                   stroke_color=HAIRLINE, stroke_width=1.5)
        div._qc_intentional = True
        self.play(Create(div), run_time=0.35)

        # BOTTOM HALF: WRONG — tag only once
        wrong_lbl = Text("✗  tag once = not enough", font=DISPLAY, color=CRIMSON,
                         font_size=18, weight="MEDIUM")
        wrong_lbl.move_to(UP * 0.05)
        self.play(FadeIn(wrong_lbl), run_time=0.35)

        top_tag = Text(tag, font=MONO, color=SLATE, font_size=15)
        top_tag.move_to(LEFT * 0.1 + DOWN * 0.5)
        wbeat1 = Text("Every beat, every word…", font=SERIF, color=INK, font_size=16)
        wbeat1.move_to(LEFT * 0.1 + DOWN * 0.95)
        # Musical note creeping in (the problem)
        wbeat2 = Text("No drift, no ♪ melody…", font=SERIF, color=CRIMSON, font_size=16)
        wbeat2.move_to(LEFT * 0.1 + DOWN * 1.4)

        self.play(FadeIn(top_tag), FadeIn(wbeat1), run_time=0.3)
        self.play(FadeIn(wbeat2), run_time=0.4)

        caption = SerifLabel("one style note is not enough — the tag rides above every beat.",
                             accent=ACCENT_TEAL, size=17)
        caption.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(max(0.5, _dur("B04") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B05 — THE PANTRY DROP (~13s)
# Three-step flow is vertical — fits portrait naturally.
# Steps centered at x=0, numbers at x≈-1.8, text at x≈0.2.
# Pantry box below step 3.
# Caption: "pantry/ is where human-made media always lands."
# ──────────────────────────────────────────────────────────
class B05_PantryDrop(Scene):
    def construct(self):
        chip = LabelChip("THE HUMAN LOOP", accent=ACCENT_TEAL, size=17)
        chip.to_corner(UL, buff=0.55)
        self.play(FadeIn(chip), run_time=0.4)

        steps = [
            ("1", "paste .suno.N.txt", "into Suno's lyrics box"),
            ("2", "generate + download", "vocal-only stem (no music bed)"),
            ("3", "drop into pantry/", "toolkit's human-media shelf"),
        ]
        y_positions = [2.0, 0.7, -0.6]

        step_grps = []
        for (num, head, sub), y in zip(steps, y_positions):
            num_t = Text(num, font=DISPLAY, color=CRIMSON, font_size=34, weight="BOLD")
            num_t.move_to(LEFT * 1.8 + UP * y)

            head_t = Text(head, font=DISPLAY, color=INK, font_size=20, weight="MEDIUM")
            head_t.move_to(RIGHT * 0.2 + UP * y)

            sub_t = Text(sub, font=SERIF, color=SLATE, font_size=16, slant=ITALIC)
            sub_t.move_to(RIGHT * 0.2 + UP * (y - 0.36))

            grp = VGroup(num_t, head_t, sub_t)
            step_grps.append(grp)
            self.play(FadeIn(grp), run_time=0.45)

        # Arrows between steps — on number column
        for i in range(len(y_positions) - 1):
            arr = Arrow(
                LEFT * 1.8 + UP * (y_positions[i] - 0.42),
                LEFT * 1.8 + UP * (y_positions[i + 1] + 0.42),
                stroke_color=INK, stroke_width=2, buff=0,
            )
            arr._qc_intentional = True
            self.play(GrowArrow(arr), run_time=0.28)

        # Pantry box — below step 3
        pantry_path = Text("pantry/<slug>-vocals-1.wav",
                           font=MONO, color=ACCENT_TEAL, font_size=16)
        pantry_path.move_to(DOWN * 1.75)
        pantry_box = auto_box(pantry_path, h_pad=0.26, v_pad=0.20,
                              stroke_color=ACCENT_TEAL, stroke_width=2)
        self.play(FadeIn(pantry_box), FadeIn(pantry_path), run_time=0.5)

        caption = SerifLabel("pantry/ is where human-made media always lands.",
                             accent=ACCENT_TEAL, size=19)
        caption.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(max(0.5, _dur("B05") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B08 — THE NUMBERS (~17s)
# Portrait: single stacked card, no two-column layout.
# Header row "ElevenLabs | Suno" at top, then 6 metric rows.
# Left-justify EL value, center label, right-justify Suno value.
# Caption: "metered scales with the word count; flat doesn't."
# ──────────────────────────────────────────────────────────
class B08_TheNumbers(Scene):
    def construct(self):
        chip = LabelChip("THE NUMBERS", accent=CRIMSON, size=17)
        chip.to_corner(UL, buff=0.55)
        self.play(FadeIn(chip), run_time=0.4)

        # Card background
        card = Rectangle(width=3.7, height=5.6, fill_color=GROUND,
                         fill_opacity=1, stroke_color=INK, stroke_width=1.5)
        card.move_to(UP * 0.5)

        # Header row
        el_hdr = Text("ElevenLabs", font=DISPLAY, color=CRIMSON,
                      font_size=17, weight="BOLD")
        el_hdr.move_to(LEFT * 1.1 + UP * 3.0)

        slash = Text("|", font=DISPLAY, color=HAIRLINE, font_size=17)
        slash.move_to(UP * 3.0)

        suno_hdr = Text("Suno", font=DISPLAY, color=ACCENT_TEAL,
                        font_size=17, weight="BOLD")
        suno_hdr.move_to(RIGHT * 1.1 + UP * 3.0)

        self.play(FadeIn(card), FadeIn(el_hdr), FadeIn(slash), FadeIn(suno_hdr),
                  run_time=0.6)

        # Horizontal rule under header
        hdr_rule = Line(LEFT * 1.75 + UP * 2.72, RIGHT * 1.75 + UP * 2.72,
                        stroke_color=HAIRLINE, stroke_width=1)
        hdr_rule._qc_intentional = True
        self.play(Create(hdr_rule), run_time=0.2)

        # Rows: (label, el_value, suno_value)
        rows = [
            ("characters", "3,108", "1 gen"),
            ("wall time", "42s/13 calls", "<5s"),
            ("human steps", "0", "3"),
            ("retakes", "0", "0"),
            ("cost / min", "~$0.28", "1 gen"),
            ("scales?", "YES", "NO"),
        ]
        row_start_y = 2.35
        row_gap = 0.52

        for i, (lbl, el_v, suno_v) in enumerate(rows):
            y = row_start_y - i * row_gap

            lbl_t = Text(lbl, font=SERIF, color=SLATE, font_size=14, slant=ITALIC)
            lbl_t.move_to(UP * y)

            el_color = CRIMSON if "YES" in el_v else INK
            el_t = Text(el_v, font=MONO, color=el_color, font_size=15)
            el_t.move_to(LEFT * 1.3 + UP * y)

            suno_color = ACCENT_TEAL if "NO" in suno_v else INK
            suno_t = Text(suno_v, font=MONO, color=suno_color, font_size=15)
            suno_t.move_to(RIGHT * 1.3 + UP * y)

            self.play(FadeIn(lbl_t), FadeIn(el_t), FadeIn(suno_t), run_time=0.32)

        caption = SerifLabel("metered scales with the word count; flat doesn't.",
                             accent=CRIMSON, size=18)
        caption.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(max(0.5, _dur("B08") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B10 — THE SPLIT / HERO (~19s)
# Dark bg #2A1A0E. Portrait: hero lines stacked center,
# "both paths equal" below, "you listened / ✓ this one" at bottom.
# White/teal colors same as parent.
# Gate W WARNING expected — white text on dark bg, intentional.
# ──────────────────────────────────────────────────────────
class B10_TheSplit(Scene):
    def construct(self):
        self.camera.background_color = "#2A1A0E"

        # Section chip — crimson bg, white text
        chip_bg = Rectangle(width=2.6, height=0.5, fill_color=CRIMSON,
                            fill_opacity=1, stroke_width=0)
        chip_bg.to_corner(UL, buff=0.55)
        chip_txt = Text("THE SPLIT", font=DISPLAY, color=WHITE, font_size=17,
                        weight="MEDIUM")
        chip_txt.move_to(chip_bg)
        self.play(FadeIn(chip_bg), FadeIn(chip_txt), run_time=0.4)

        # Hero lines stacked center (top half)
        hero_line1 = Text("THE MACHINE VOICES", font=SERIF, color=WHITE, font_size=28)
        hero_line1.move_to(UP * 2.4)
        hero_line2 = Text("EVERY BEAT.", font=SERIF, color=WHITE, font_size=28)
        hero_line2.move_to(UP * 1.85)
        hero_line3 = Text("YOU CHOOSE WHOSE", font=SERIF, color=ACCENT_TEAL, font_size=28)
        hero_line3.move_to(UP * 1.2)
        hero_line4 = Text("VOICE SHIPS.", font=SERIF, color=ACCENT_TEAL, font_size=28)
        hero_line4.move_to(UP * 0.65)

        self.play(FadeIn(hero_line1), FadeIn(hero_line2), run_time=0.7)
        self.play(FadeIn(hero_line3), FadeIn(hero_line4), run_time=0.7)

        # Crimson divider rule (center)
        rule = Line(LEFT * 1.6 + UP * 0.1, RIGHT * 1.6 + UP * 0.1,
                    stroke_color=CRIMSON, stroke_width=2)
        rule._qc_intentional = True
        self.play(Create(rule), run_time=0.4)

        # "both paths equal" — centered below rule
        both_lbl = Text("both paths, equal", font=DISPLAY, color=WHITE,
                        font_size=18, weight="MEDIUM")
        both_lbl.move_to(DOWN * 0.35)

        el_tag = Text("EL ——————", font=MONO, color=SLATE, font_size=17)
        el_tag.move_to(DOWN * 0.85)
        suno_tag = Text("SUNO —————", font=MONO, color=SLATE, font_size=17)
        suno_tag.move_to(DOWN * 1.25)

        self.play(FadeIn(both_lbl), FadeIn(el_tag), FadeIn(suno_tag), run_time=0.5)

        # "you listened / checkmark" — stacked below
        ear_lbl = Text("you listened.", font=SERIF, color=WHITE, font_size=20, slant=ITALIC)
        ear_lbl.move_to(DOWN * 1.9)

        check_line = Text("✓  this one.", font=DISPLAY, color=ACCENT_TEAL,
                          font_size=24, weight="BOLD")
        check_line.move_to(DOWN * 2.45)

        self.play(FadeIn(ear_lbl), run_time=0.4)
        self.play(FadeIn(check_line), run_time=0.5)

        caption_txt = Text("you listened to both — one of them is playing right now.",
                           font=SERIF, color=SLATE, font_size=16, slant=ITALIC)
        caption_txt.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(caption_txt), run_time=0.6)
        self.wait(max(0.5, _dur("B10") - getattr(self, 'time', 0.0)))
