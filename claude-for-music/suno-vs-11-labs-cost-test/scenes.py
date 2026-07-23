"""scenes.py — Manim scenes for 'Suno vs 11 Labs Cost Test'

GRAPHIC beats: B01, B02, B04, B05, B07, B08, B09, B10 (hero).
Remotion beats: B00, B03, B06, B11, B99.
Palette: teardown — GROUND #FFFFFF, INK #2A1A0E, CRIMSON #C8102E, ACCENT_TEAL #1F6F5C.
B10_TheSplit is the hero beat — dark bg #2A1A0E, white title, teal subtitle.
"""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "runtime" / "manim"))
from animated_graphics import *

ACCENT_TEAL = "#1F6F5C"


def _dur(bid):
    """Return actual_duration_s for bid from this reel's beat_sheet.json."""
    bs = pathlib.Path(__file__).parent / "beat_sheet.json"
    if not bs.exists():
        return 0.0
    for b in json.loads(bs.read_text()).get("beats", []):
        if b["beat_id"] == bid:
            return float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0.0)
    return 0.0


# ──────────────────────────────────────────────────────────
# B00A — ANNOUNCE (both variants, ElevenLabs voiced)
# Title card naming the variant; body voice is the experiment.
# Reads slug from beat_sheet.json to label itself correctly.
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
                     font_size=44, weight="BOLD")
        title.move_to(UP * 0.55)

        sub = Text(variant_lbl, font=SERIF, color=accent,
                   font_size=28, slant=ITALIC)
        sub.move_to(DOWN * 0.12)

        note = Text(other_lbl, font=MONO, color=SLATE, font_size=18)
        note.move_to(DOWN * 0.74)

        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.5, _dur("B00A") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B01 — THE METER (~11s)
# Tank draining as beat counter ticks up; red bill line rises.
# Caption: "metered: the more you talk, the more you pay."
# ──────────────────────────────────────────────────────────
class B01_TheMeter(Scene):
    def construct(self):
        chip = LabelChip("THE ITCH", accent=CRIMSON, size=17)
        chip.to_corner(UL, buff=0.55)
        self.play(FadeIn(chip), run_time=0.4)

        # Tank rectangle (draining ELEVENLABS CREDITS)
        tank_label = Text("ELEVENLABS CREDITS", font=DISPLAY, color=INK,
                          font_size=20, weight="MEDIUM")
        tank_label.move_to(UP * 1.8 + LEFT * 2.4)

        tank_bg = Rectangle(width=2.0, height=2.4, fill_color=GROUND,
                            fill_opacity=1, stroke_color=INK, stroke_width=2)
        tank_bg.move_to(LEFT * 2.4 + UP * 0.2)

        fill_full = Rectangle(width=1.8, height=2.2, fill_color=ACCENT_TEAL,
                               fill_opacity=0.35, stroke_width=0)
        fill_full.move_to(tank_bg).align_to(tank_bg, DOWN).shift(UP * 0.1)

        fill_drain = Rectangle(width=1.8, height=0.4, fill_color=ACCENT_TEAL,
                               fill_opacity=0.35, stroke_width=0)
        fill_drain.move_to(tank_bg).align_to(tank_bg, DOWN).shift(UP * 0.1)

        self.play(FadeIn(tank_label), FadeIn(tank_bg), FadeIn(fill_full), run_time=0.5)
        self.play(Transform(fill_full, fill_drain), run_time=1.5)

        # Beat counter ticking up
        beats = ["B00", "B01", "B02", "…", "B99"]
        counter_lbl = Text("beats voiced:", font=MONO, color=INK, font_size=22)
        counter_lbl.move_to(RIGHT * 1.6 + UP * 1.6)
        self.play(FadeIn(counter_lbl), run_time=0.3)

        prev = None
        for i, bid in enumerate(beats):
            t = Text(bid, font=MONO, color=CRIMSON if bid == "B99" else INK, font_size=28)
            t.next_to(counter_lbl, DOWN, buff=0.3)
            if prev:
                self.play(ReplacementTransform(prev, t), run_time=0.25)
            else:
                self.play(FadeIn(t), run_time=0.25)
            prev = t

        # Bill line rising
        bill_lbl = Text("bill", font=MONO, color=CRIMSON, font_size=20)
        bill_lbl.move_to(RIGHT * 1.6 + DOWN * 0.2)
        bill_line = Line(
            RIGHT * 1.6 + DOWN * 0.6,
            RIGHT * 1.6 + DOWN * 0.6,
            stroke_color=CRIMSON, stroke_width=3,
        )
        self.play(FadeIn(bill_lbl), run_time=0.3)
        self.play(
            bill_line.animate.put_start_and_end_on(
                RIGHT * 0.8 + DOWN * 0.6, RIGHT * 2.4 + UP * 0.0
            ),
            run_time=1.0,
        )
        self.add(bill_line)

        caption = SerifLabel("metered: the more you talk, the more you pay.",
                             accent=CRIMSON, size=22)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(max(0.5, _dur("B01") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B02 — THE CHALLENGER (~15s)
# Suno card: voice waveform, flat-rate stamp, honest footnote.
# Caption: "flat: the bill doesn't scale with the word count."
# ──────────────────────────────────────────────────────────
class B02_TheChallenger(Scene):
    def construct(self):
        chip = LabelChip("THE CHALLENGER", accent=ACCENT_TEAL, size=17)
        chip.to_corner(UL, buff=0.55)
        self.play(FadeIn(chip), run_time=0.4)

        # Card background
        card = Rectangle(width=6.4, height=3.4, fill_color=GROUND,
                         fill_opacity=1, stroke_color=ACCENT_TEAL, stroke_width=2)
        card.move_to(UP * 0.4)

        # Title
        title = Text("SUNO", font=DISPLAY, color=INK, font_size=40, weight="BOLD")
        title.move_to(UP * 1.8)

        subtitle = Text("your voice, uploaded once", font=SERIF, color=SLATE,
                        font_size=22, slant=ITALIC)
        subtitle.next_to(title, DOWN, buff=0.18)

        self.play(FadeIn(card), FadeIn(title), run_time=0.6)
        self.play(FadeIn(subtitle), run_time=0.4)

        # Waveform hint — three bars
        bar_h = [0.6, 0.9, 0.5]
        bars = VGroup(*[
            Rectangle(width=0.18, height=h, fill_color=ACCENT_TEAL,
                      fill_opacity=0.7, stroke_width=0).move_to(LEFT * (0.4 - i * 0.32) + UP * 0.35)
            for i, h in enumerate(bar_h)
        ])
        self.play(FadeIn(bars), run_time=0.5)

        # Flat-rate stamp — size bg from text, not a guessed width
        stamp_txt = Text("ONE GENERATION ≈ ONE VIDEO'S NARRATION",
                         font=DISPLAY, color=WHITE, font_size=13, weight="MEDIUM")
        stamp_txt.move_to(DOWN * 0.22)
        stamp_bg = Rectangle(
            width=stamp_txt.width + 0.56,
            height=stamp_txt.height + 0.38,
            fill_color=ACCENT_TEAL, fill_opacity=1, stroke_width=0,
        )
        stamp_bg.move_to(stamp_txt)
        stamp_bg._qc_intentional = True
        self.play(FadeIn(stamp_bg), FadeIn(stamp_txt), run_time=0.6)

        # Honest footnote in red
        note = Text("leans speak-song — clear for spoken word",
                    font=SERIF, color=CRIMSON, font_size=18)
        note.move_to(DOWN * 0.88)
        self.play(FadeIn(note), run_time=0.4)

        caption = SerifLabel("flat: the bill doesn't scale with the word count.",
                             accent=ACCENT_TEAL, size=22)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(max(0.5, _dur("B02") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B04 — THE [SPOKEN WORD] TAG (~12s)
# .suno.txt mock: three beats, each with [spoken word] above.
# Side-by-side: correct (tag per beat) vs wrong (once at top).
# Caption: "one style note is not enough; the tag rides above every beat."
# ──────────────────────────────────────────────────────────
class B04_SpokenWordTag(Scene):
    def construct(self):
        chip = LabelChip("THE TAG", accent=ACCENT_TEAL, size=17)
        chip.to_corner(UL, buff=0.55)
        self.play(FadeIn(chip), run_time=0.4)

        # LEFT: CORRECT — tag above every beat
        correct_lbl = Text("✓  tag per beat", font=DISPLAY, color=ACCENT_TEAL,
                           font_size=20, weight="MEDIUM")
        correct_lbl.move_to(LEFT * 3.2 + UP * 2.1)

        tag = "[spoken word]"
        beat_texts = ["Every beat, every word…", "No drift, no melody…", "Stays speaking."]
        lines = []
        for i, bt in enumerate(beat_texts):
            row_tag = Text(tag, font=MONO, color=ACCENT_TEAL, font_size=17)
            row_beat = Text(bt, font=SERIF, color=INK, font_size=18)
            row = VGroup(row_tag, row_beat).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            row.move_to(LEFT * 3.2 + UP * (1.2 - i * 0.72))
            lines.append(row)

        self.play(FadeIn(correct_lbl), run_time=0.4)
        for row in lines:
            self.play(FadeIn(row), run_time=0.3)

        # Divider
        div = Line(UP * 2.5, DOWN * 1.8, stroke_color=HAIRLINE, stroke_width=1.5)
        div.move_to(ORIGIN)
        self.play(Create(div), run_time=0.4)

        # RIGHT: WRONG — tag only once
        wrong_lbl = Text("✗  tag once = not enough", font=DISPLAY, color=CRIMSON,
                         font_size=20, weight="MEDIUM")
        wrong_lbl.move_to(RIGHT * 3.2 + UP * 2.1)

        top_tag = Text(tag, font=MONO, color=SLATE, font_size=17)
        top_tag.move_to(RIGHT * 3.2 + UP * 1.35)
        wbeat1 = Text("Every beat, every word…", font=SERIF, color=INK, font_size=18)
        wbeat1.move_to(RIGHT * 3.2 + UP * 0.72)
        # Musical note creeping in (the problem)
        wbeat2 = Text("No drift, no ♪ melody…", font=SERIF, color=CRIMSON, font_size=18)
        wbeat2.move_to(RIGHT * 3.2 + UP * 0.08)

        self.play(FadeIn(wrong_lbl), run_time=0.4)
        self.play(FadeIn(top_tag), FadeIn(wbeat1), run_time=0.3)
        self.play(FadeIn(wbeat2), run_time=0.4)

        caption = SerifLabel("one style note is not enough — the tag rides above every beat.",
                             accent=ACCENT_TEAL, size=20)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(max(0.5, _dur("B04") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B05 — THE PANTRY DROP (~13s)
# Three-step flow: paste → generate+download → drop in pantry/.
# Caption: "pantry/<slug>-vocals-N.wav — where human-made media lands."
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
        y_positions = [1.2, 0.18, -0.85]

        step_grps = []
        for (num, head, sub), y in zip(steps, y_positions):
            num_t = Text(num, font=DISPLAY, color=CRIMSON, font_size=36, weight="BOLD")
            num_t.move_to(LEFT * 5.2 + UP * y)

            head_t = Text(head, font=DISPLAY, color=INK, font_size=24, weight="MEDIUM")
            head_t.move_to(LEFT * 2.0 + UP * y)

            sub_t = Text(sub, font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
            sub_t.move_to(LEFT * 2.0 + UP * (y - 0.38))

            grp = VGroup(num_t, head_t, sub_t)
            step_grps.append(grp)
            self.play(FadeIn(grp), run_time=0.45)

        # Arrow between steps (step 1 → 2 → 3), carefully placed away from text
        for i in range(len(y_positions) - 1):
            arr_y = (y_positions[i] + y_positions[i + 1]) / 2
            arr = Arrow(
                LEFT * 5.2 + UP * (y_positions[i] - 0.45),
                LEFT * 5.2 + UP * (y_positions[i + 1] + 0.45),
                stroke_color=INK, stroke_width=2, buff=0,
            )
            arr._qc_intentional = True
            self.play(GrowArrow(arr), run_time=0.3)

        # Pantry label on the right — positioned below step-2 zone to avoid collision
        pantry_path = Text("pantry/<slug>-vocals-1.wav",
                           font=MONO, color=ACCENT_TEAL, font_size=18)
        pantry_path.move_to(RIGHT * 3.2 + DOWN * 0.55)
        pantry_box = auto_box(pantry_path, h_pad=0.28, v_pad=0.22,
                              stroke_color=ACCENT_TEAL, stroke_width=2)
        self.play(FadeIn(pantry_box), FadeIn(pantry_path), run_time=0.5)

        caption = SerifLabel("pantry/ is where human-made media always lands.",
                             accent=ACCENT_TEAL, size=22)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(max(0.5, _dur("B05") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B07 — THE SAME INTERFACE (~17s)
# Two engines → same beat slots → one unbroken pipeline.
# Caption: "same files, same durations, same beat sheet — downstream never knows."
# ──────────────────────────────────────────────────────────
class B07_SameInterface(Scene):
    def construct(self):
        chip = LabelChip("THE PLUG", accent=ACCENT_TEAL, size=17)
        chip.to_corner(UL, buff=0.55)
        self.play(FadeIn(chip), run_time=0.4)

        # Two engine labels (top)
        el_lbl = Text("ELEVENLABS", font=DISPLAY, color=INK, font_size=26, weight="BOLD")
        el_lbl.move_to(LEFT * 4.2 + UP * 2.5)
        el_sub = Text("metered", font=SERIF, color=CRIMSON, font_size=20, slant=ITALIC)
        el_sub.next_to(el_lbl, DOWN, buff=0.1)

        suno_lbl = Text("SUNO", font=DISPLAY, color=INK, font_size=26, weight="BOLD")
        suno_lbl.move_to(RIGHT * 4.2 + UP * 2.5)
        suno_sub = Text("flat", font=SERIF, color=ACCENT_TEAL, font_size=20, slant=ITALIC)
        suno_sub.next_to(suno_lbl, DOWN, buff=0.1)

        self.play(FadeIn(el_lbl), FadeIn(el_sub), run_time=0.5)
        self.play(FadeIn(suno_lbl), FadeIn(suno_sub), run_time=0.5)

        # Beat slot row (center)
        slots = ["B00", "B01", "B02", "…", "B99"]
        slot_grp = VGroup(*[
            Text(s, font=MONO, color=INK, font_size=20) for s in slots
        ]).arrange(RIGHT, buff=0.5)
        slot_grp.move_to(UP * 0.4)

        slot_boxes = VGroup(*[
            auto_box(t, h_pad=0.18, v_pad=0.14, stroke_color=SLATE, stroke_width=1)
            for t in slot_grp
        ])
        self.play(FadeIn(slot_boxes), FadeIn(slot_grp), run_time=0.6)

        # Duration stamp under each slot
        durs = ["13.8s", "11.1s", "14.7s", "…", "15.2s"]
        dur_grp = VGroup(*[
            Text(d, font=MONO, color=SLATE, font_size=16) for d in durs
        ]).arrange(RIGHT, buff=0.5)
        dur_grp.move_to(UP * 0.0)
        # align each dur under its slot
        for d_t, s_t in zip(dur_grp, slot_grp):
            d_t.move_to(s_t.get_center() + DOWN * 0.52)
        self.play(FadeIn(dur_grp), run_time=0.4)

        # Arrows from engines to slots
        el_arr = Arrow(
            el_lbl.get_bottom() + DOWN * 0.1,
            slot_grp[0].get_top() + UP * 0.1,
            stroke_color=INK, stroke_width=2, buff=0.05,
        )
        el_arr._qc_intentional = True
        suno_arr = Arrow(
            suno_lbl.get_bottom() + DOWN * 0.1,
            slot_grp[-1].get_top() + UP * 0.1,
            stroke_color=INK, stroke_width=2, buff=0.05,
        )
        suno_arr._qc_intentional = True
        self.play(GrowArrow(el_arr), GrowArrow(suno_arr), run_time=0.5)

        # Pipeline line below slots
        pipe_lbl = Text("render  ·  captions  ·  shorts  ·  publish",
                        font=DISPLAY, color=ACCENT_TEAL, font_size=22, weight="MEDIUM")
        pipe_lbl.move_to(DOWN * 1.4)
        pipe_line = Line(
            LEFT * 5.0 + DOWN * 1.1,
            RIGHT * 5.0 + DOWN * 1.1,
            stroke_color=ACCENT_TEAL, stroke_width=3,
        )
        pipe_line._qc_intentional = True
        pipe_arr = Arrow(
            LEFT * 5.0 + DOWN * 1.1,
            RIGHT * 5.0 + DOWN * 1.1,
            stroke_color=ACCENT_TEAL, stroke_width=3, buff=0,
        )
        pipe_arr._qc_intentional = True
        self.play(Create(pipe_arr), FadeIn(pipe_lbl), run_time=0.6)

        caption = SerifLabel("same files, same durations — downstream never knows.",
                             accent=ACCENT_TEAL, size=22)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(max(0.5, _dur("B07") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B08 — THE NUMBERS (~17s)
# Two-column comparison card from COST-LOG.md.
# Real measured values only — Suno credit $ marked TBD.
# Caption: "metered scales with word count; flat doesn't."
# ──────────────────────────────────────────────────────────
class B08_TheNumbers(Scene):
    def construct(self):
        chip = LabelChip("THE NUMBERS", accent=CRIMSON, size=17)
        chip.to_corner(UL, buff=0.55)
        self.play(FadeIn(chip), run_time=0.4)

        # Column headers
        el_hdr = Text("ElevenLabs", font=DISPLAY, color=INK, font_size=26, weight="BOLD")
        el_hdr.move_to(LEFT * 3.0 + UP * 2.1)
        suno_hdr = Text("Suno", font=DISPLAY, color=INK, font_size=26, weight="BOLD")
        suno_hdr.move_to(RIGHT * 3.0 + UP * 2.1)

        el_sub = Text("metered", font=SERIF, color=CRIMSON, font_size=20, slant=ITALIC)
        el_sub.next_to(el_hdr, DOWN, buff=0.08)
        suno_sub = Text("flat", font=SERIF, color=ACCENT_TEAL, font_size=20, slant=ITALIC)
        suno_sub.next_to(suno_hdr, DOWN, buff=0.08)

        self.play(FadeIn(el_hdr), FadeIn(el_sub), FadeIn(suno_hdr), FadeIn(suno_sub),
                  run_time=0.6)

        # Divider — intentional; row labels sit on it by design
        vdiv = Line(UP * 2.6, DOWN * 1.6, stroke_color=HAIRLINE, stroke_width=1.5)
        vdiv.move_to(ORIGIN)
        vdiv._qc_intentional = True
        self.play(Create(vdiv), run_time=0.3)

        # Rows: (label, el_value, suno_value)
        rows = [
            ("characters", "3,108 chars", "1 generation"),
            ("wall time", "42s (13 calls)", "<5s (slice only)"),
            ("human steps", "0", "3"),
            ("retakes", "0", "0"),
            ("cost / narr. min", "~$0.28 (overage)", "1 gen (see log)"),
            ("scales w/ words?", "YES", "NO"),
        ]
        row_y = 1.2
        for i, (lbl, el_v, suno_v) in enumerate(rows):
            y = row_y - i * 0.56
            lbl_t = Text(lbl, font=SERIF, color=SLATE, font_size=19, slant=ITALIC)
            lbl_t.move_to(ORIGIN + UP * y)

            el_t = Text(el_v, font=MONO, color=CRIMSON if "YES" in el_v else INK,
                        font_size=20)
            el_t.move_to(LEFT * 3.0 + UP * y)

            suno_t = Text(suno_v, font=MONO,
                          color=ACCENT_TEAL if "NO" in suno_v else INK, font_size=20)
            suno_t.move_to(RIGHT * 3.0 + UP * y)

            self.play(FadeIn(lbl_t), FadeIn(el_t), FadeIn(suno_t), run_time=0.35)

        caption = SerifLabel("metered scales with the word count; flat doesn't.",
                             accent=CRIMSON, size=22)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(max(0.5, _dur("B08") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B09 — THE TRADEOFF (~18s)
# Two-pan balance: EL (steady) vs Suno (can drift + workflow tax).
# Caption: "cheap has a workflow tax — is the tax smaller than the bill?"
# ──────────────────────────────────────────────────────────
class B09_TheTradeoff(Scene):
    def construct(self):
        chip = LabelChip("NO FREE LUNCH", accent=CRIMSON, size=17)
        chip.to_corner(UL, buff=0.55)
        self.play(FadeIn(chip), run_time=0.4)

        # Balance beam
        pivot = Dot(ORIGIN + DOWN * 0.1, radius=0.12, color=INK)
        beam = Line(LEFT * 3.8 + DOWN * 0.1, RIGHT * 3.8 + DOWN * 0.1,
                    stroke_color=INK, stroke_width=3)
        beam._qc_intentional = True
        self.play(FadeIn(pivot), Create(beam), run_time=0.5)

        # Left pan — ElevenLabs (steady)
        el_pan_lbl = Text("ElevenLabs", font=DISPLAY, color=INK,
                          font_size=24, weight="BOLD")
        el_pan_lbl.move_to(LEFT * 3.8 + UP * 1.6)
        el_steady = Text("steadier", font=SERIF, color=ACCENT_TEAL,
                         font_size=22, slant=ITALIC)
        el_steady.move_to(LEFT * 3.8 + UP * 1.1)
        el_detail = Text("every retake sounds the same", font=SERIF, color=SLATE,
                         font_size=18)
        el_detail.move_to(LEFT * 3.8 + UP * 0.68)

        self.play(FadeIn(el_pan_lbl), FadeIn(el_steady), FadeIn(el_detail), run_time=0.55)

        # Right pan — Suno (can drift + workflow tax)
        suno_pan_lbl = Text("Suno", font=DISPLAY, color=INK,
                            font_size=24, weight="BOLD")
        suno_pan_lbl.move_to(RIGHT * 3.8 + UP * 1.6)
        suno_drift = Text("can drift musical", font=SERIF, color=CRIMSON,
                          font_size=22, slant=ITALIC)
        suno_drift.move_to(RIGHT * 3.8 + UP * 1.1)

        tax_items = ["retakes  ·  vocal-only dl",
                     "pantry drop  ·  slicing"]
        tax_stack = VGroup(*[
            Text(t, font=MONO, color=SLATE, font_size=17) for t in tax_items
        ]).arrange(DOWN, buff=0.18)
        tax_stack.move_to(RIGHT * 3.8 + UP * 0.52)

        self.play(FadeIn(suno_pan_lbl), FadeIn(suno_drift), FadeIn(tax_stack),
                  run_time=0.55)

        # Tilt beam: Suno has workflow tax → right side tips slightly down
        self.play(
            beam.animate.put_start_and_end_on(
                LEFT * 3.8 + UP * 0.22, RIGHT * 3.8 + DOWN * 0.42
            ),
            run_time=0.8,
        )

        caption = SerifLabel(
            "cheap has a workflow tax — is the tax smaller than the bill?",
            accent=CRIMSON, size=20,
        )
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(max(0.5, _dur("B09") - getattr(self, 'time', 0.0)))


# ──────────────────────────────────────────────────────────
# B10 — THE SPLIT / HERO (~19s)
# Dark bg. Centre: "THE MACHINE VOICES EVERY BEAT." / "YOU CHOOSE WHOSE VOICE SHIPS."
# Left: both engine paths, equal. Right: human ear + checkmark on one take.
# Caption: "you listened to both — one of them is playing right now."
# Gate W WARNING expected (white text on dark bg — intentional hero beat).
# ──────────────────────────────────────────────────────────
class B10_TheSplit(Scene):
    def construct(self):
        self.camera.background_color = "#2A1A0E"

        # Section chip — in white so it reads on dark bg
        chip_bg = Rectangle(width=2.4, height=0.5, fill_color=CRIMSON,
                            fill_opacity=1, stroke_width=0)
        chip_bg.to_corner(UL, buff=0.55)
        chip_txt = Text("THE SPLIT", font=DISPLAY, color=WHITE, font_size=17,
                        weight="MEDIUM")
        chip_txt.move_to(chip_bg)
        self.play(FadeIn(chip_bg), FadeIn(chip_txt), run_time=0.4)

        # Centre title (hero statement)
        hero_line1 = Text("THE MACHINE VOICES EVERY BEAT.",
                          font=SERIF, color=WHITE, font_size=36)
        hero_line1.move_to(UP * 0.85)
        hero_line2 = Text("YOU CHOOSE WHOSE VOICE SHIPS.",
                          font=SERIF, color=ACCENT_TEAL, font_size=36)
        hero_line2.move_to(UP * 0.25)

        self.play(FadeIn(hero_line1), run_time=0.7)
        self.play(FadeIn(hero_line2), run_time=0.7)

        # Left: two engine paths, drawn equal
        left_lbl = Text("both paths, equal", font=DISPLAY, color=WHITE,
                        font_size=20, weight="MEDIUM")
        left_lbl.move_to(LEFT * 4.2 + DOWN * 0.7)

        el_tag = Text("EL   ──────", font=MONO, color=SLATE, font_size=19)
        el_tag.move_to(LEFT * 4.2 + DOWN * 1.18)
        suno_tag = Text("SUNO  ──────", font=MONO, color=SLATE, font_size=19)
        suno_tag.move_to(LEFT * 4.2 + DOWN * 1.58)

        self.play(FadeIn(left_lbl), FadeIn(el_tag), FadeIn(suno_tag), run_time=0.5)

        # Right: human ear + checkmark on one take
        ear_lbl = Text("you listened.", font=SERIF, color=WHITE, font_size=22, slant=ITALIC)
        ear_lbl.move_to(RIGHT * 4.0 + DOWN * 0.7)

        check_line = Text("✓  this one.", font=DISPLAY, color=ACCENT_TEAL,
                          font_size=26, weight="BOLD")
        check_line.move_to(RIGHT * 4.0 + DOWN * 1.28)

        self.play(FadeIn(ear_lbl), run_time=0.4)
        self.play(FadeIn(check_line), run_time=0.5)

        # Crimson divider rule
        rule = Line(LEFT * 1.2 + DOWN * 1.9, RIGHT * 1.2 + DOWN * 1.9,
                    stroke_color=CRIMSON, stroke_width=2)
        rule._qc_intentional = True
        self.play(Create(rule), run_time=0.4)

        caption_txt = Text("you listened to both — one of them is playing right now.",
                           font=SERIF, color=SLATE, font_size=21, slant=ITALIC)
        caption_txt.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption_txt), run_time=0.6)
        self.wait(max(0.5, _dur("B10") - getattr(self, 'time', 0.0)))
