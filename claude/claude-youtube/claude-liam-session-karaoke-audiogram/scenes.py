"""scenes.py — Manim scenes for 'Session, Karaoke & Audiogram'

Five GRAPHIC beats: B01, B04, B07, B09 (hero), B10 (hero split).
Palette: teardown — flat white GROUND, ink INK, with newsprint-style
ACCENT_TEAL = #1F6F5C for the teal accent (tool / good state).
B09 and B10 are hero beats on a dark #2A1A0E canvas.
"""
import sys, pathlib
import numpy as np
# locate brutalist-art/runtime/manim by walking up (layout-proof)
for _a in pathlib.Path(__file__).resolve().parents:
    _m = _a / "brutalist-art" / "runtime" / "manim"
    if (_m / "animated_graphics.py").is_file():
        sys.path.insert(0, str(_m)); break
from animated_graphics import *

ACCENT_TEAL = "#1F6F5C"


# ──────────────────────────────────────────────────────────
# B01 — THE SPOKEN WORD ERA (13s)
# Mock Suno lyrics box: one [spoken word] tag at the very top,
# three stanzas with no further tags. A red musical note creeps
# into the second stanza — Suno decided that line got a melody.
# Caption: "a stop sign is not a direction."
# ──────────────────────────────────────────────────────────
class B01_TheSpokenWordEra(Scene):
    def construct(self):
        section = LabelChip("THE [SPOKEN WORD] ERA", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # Lyrics box — white panel with teal border
        tag_line = Text("[spoken word]", font=MONO, color=ACCENT_TEAL,
                        font_size=18, weight=BOLD)
        blank = Text("", font=MONO, color=INK, font_size=14)

        stanza_1 = VGroup(
            Text("She walks in beauty, like the night", font=SERIF, color=INK, font_size=16),
            Text("Of cloudless climes and starry skies,", font=SERIF, color=INK, font_size=16),
        ).arrange(DOWN, buff=0.06, aligned_edge=LEFT)

        stanza_2 = VGroup(
            Text("Thus mellowed to that tender light", font=SERIF, color=INK, font_size=16),
            Text("Which heaven to gaudy day denies,", font=SERIF, color=INK, font_size=16),
        ).arrange(DOWN, buff=0.06, aligned_edge=LEFT)

        stanza_3 = VGroup(
            Text("And on that cheek, and o'er that brow,", font=SERIF, color=INK, font_size=16),
            Text("So soft, so calm, yet eloquent,", font=SERIF, color=INK, font_size=16),
        ).arrange(DOWN, buff=0.06, aligned_edge=LEFT)

        lyrics_content = VGroup(tag_line, stanza_1, stanza_2, stanza_3).arrange(
            DOWN, buff=0.22, aligned_edge=LEFT
        )
        lyrics_box = surround_box(lyrics_content, buff=0.35,
                                  fill_color=GROUND, stroke_color=SLATE, stroke_width=1.5)
        lyrics_grp = VGroup(lyrics_box, lyrics_content)
        if lyrics_grp.width > 9.0:
            lyrics_grp.scale_to_fit_width(9.0)
        lyrics_grp.move_to(UP * 0.2 + LEFT * 0.5)

        self.play(FadeIn(lyrics_grp, scale=0.95), run_time=0.7)
        self.wait(0.4)

        # Musical note creeps into stanza_2 — Suno decided to sing it
        note = Text("♪", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        note.next_to(stanza_2, RIGHT, buff=0.25)
        note_label = Text("Suno decided that line\ndeserved a melody.",
                          font=SERIF, color=CRIMSON, font_size=15, slant=ITALIC)
        note_label.next_to(note, RIGHT, buff=0.2)
        if note_label.width > 3.5:
            note_label.scale_to_fit_width(3.5)

        self.play(FadeIn(note, scale=1.4), run_time=0.6)
        self.play(FadeIn(note_label, shift=LEFT * 0.1), run_time=0.5)
        self.wait(0.4)

        # Caption
        caption = SerifLabel("a stop sign is not a direction.",
                             accent=CRIMSON, size=22)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.6)
        self.wait(9.3)


# ──────────────────────────────────────────────────────────
# B04 — THE WORD CLOCK (16s)
# Three-column diagram:
#   LEFT:   KNOWN TEXT — words stacked (She / walks / in / beauty…)
#   CENTER: TIMING — faster-whisper timestamps in teal
#   RIGHT:  words.json output — matched words in teal
# Arrow from LEFT+CENTER → RIGHT, label 'SequenceMatcher'.
# Caption: "text already known → timing, not transcription."
# ──────────────────────────────────────────────────────────
class B04_TheWordClock(Scene):
    def construct(self):
        section = LabelChip("THE WORD CLOCK", accent=ACCENT_TEAL, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # ---- LEFT column: KNOWN TEXT
        left_hdr = Text("KNOWN TEXT", font=DISPLAY, color=INK, font_size=17, weight=BOLD)
        words_known = ["She", "walks", "in", "beauty…"]
        left_words = VGroup(*[
            Text(w, font=SERIF, color=INK, font_size=18)
            for w in words_known
        ]).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        left_col = VGroup(left_hdr, left_words).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        left_box = surround_box(left_col, buff=0.28, fill_color=GROUND,
                                stroke_color=SLATE, stroke_width=1.5)
        left_grp = VGroup(left_box, left_col).move_to(LEFT * 4.5 + UP * 0.2)

        # ---- CENTER column: TIMING (faster-whisper timestamps)
        ctr_hdr = Text("TIMING", font=DISPLAY, color=ACCENT_TEAL, font_size=17, weight=BOLD)
        timestamps = ["0.17s", "0.42s", "0.51s", "0.60s"]
        ctr_times = VGroup(*[
            Text(t, font=MONO, color=ACCENT_TEAL, font_size=17)
            for t in timestamps
        ]).arrange(DOWN, buff=0.14)
        whisper_lbl = Text("faster-whisper", font=SERIF, color=SLATE, font_size=13, slant=ITALIC)
        ctr_col = VGroup(ctr_hdr, ctr_times, whisper_lbl).arrange(DOWN, buff=0.18)
        ctr_box = surround_box(ctr_col, buff=0.28, fill_color=GROUND,
                               stroke_color=ACCENT_TEAL, stroke_width=1.5)
        ctr_grp = VGroup(ctr_box, ctr_col).move_to(ORIGIN + UP * 0.2)

        # ---- RIGHT column: words.json output
        right_hdr = Text("words.json", font=MONO, color=ACCENT_TEAL, font_size=17, weight=BOLD)
        json_lines = [
            '{"text": "She",     sf:4,  ef:9}',
            '{"text": "walks",   sf:10, ef:17}',
            '{"text": "in",      sf:18, ef:21}',
            '{"text": "beauty,", sf:22, ef:32}',
        ]
        right_lines = VGroup(*[
            Text(line, font=MONO, color=ACCENT_TEAL, font_size=13)
            for line in json_lines
        ]).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        right_col = VGroup(right_hdr, right_lines).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        right_box = surround_box(right_col, buff=0.28, fill_color=GROUND,
                                 stroke_color=ACCENT_TEAL, stroke_width=2)
        right_grp = VGroup(right_box, right_col).move_to(RIGHT * 4.3 + UP * 0.2)
        if right_grp.width > 4.8:
            right_grp.scale_to_fit_width(4.8)

        self.play(FadeIn(left_grp, scale=0.9), run_time=0.5)
        self.play(FadeIn(ctr_grp, scale=0.9), run_time=0.5)
        self.wait(0.2)

        # Arrow: LEFT+CENTER → RIGHT with "SequenceMatcher" label
        arr_start = ctr_box.get_right() + RIGHT * 0.1
        arr_end   = right_box.get_left() + LEFT * 0.1
        seq_arrow = Arrow(arr_start, arr_end, stroke_color=ACCENT_TEAL,
                          stroke_width=2.5, tip_length=0.2, buff=0)
        seq_lbl = Text("SequenceMatcher", font=MONO, color=ACCENT_TEAL, font_size=13)
        seq_lbl.next_to(seq_arrow, UP, buff=0.1)

        self.play(GrowArrow(seq_arrow), FadeIn(seq_lbl), run_time=0.6)
        self.play(FadeIn(right_grp, scale=0.9), run_time=0.5)
        self.wait(0.3)

        caption = SerifLabel("text already known → timing, not transcription.",
                             accent=ACCENT_TEAL, size=20)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.6)
        self.wait(11.8)


# ──────────────────────────────────────────────────────────
# B07 — AUDIOGRAM LAYERS (14s)
# Exploded layer stack, bottom to top:
#   1. SOURCE VIDEO FRAME  — labeled 'already rendered'
#   2. OSCILLOSCOPE WAVEFORM — teal line
#   3. KARAOKE WORD LAYER  — 'She walks in beauty' current word bright
#   4. AUDIO (dashed) — extracted from the source frame
# Caption: "decorate the finished frame — never re-render."
# ──────────────────────────────────────────────────────────
class B07_AudiogramLayers(Scene):
    def construct(self):
        section = LabelChip("AUDIOGRAM LAYERS", accent=ACCENT_TEAL, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        layer_w = 7.0
        layer_h = 0.65

        def make_layer(label, sublabel, stroke_color, fill_color=None, y_pos=0.0):
            fill_color = fill_color or GROUND
            rect = Rectangle(width=layer_w, height=layer_h,
                             fill_color=fill_color, fill_opacity=1,
                             stroke_color=stroke_color, stroke_width=2)
            lbl = Text(label, font=DISPLAY, color=stroke_color, font_size=15, weight=BOLD)
            sub = Text(sublabel, font=SERIF, color=SLATE, font_size=13, slant=ITALIC)
            lbl_grp = VGroup(lbl, sub).arrange(RIGHT, buff=0.3)
            lbl_grp.move_to(rect.get_center())
            grp = VGroup(rect, lbl_grp)
            grp.move_to([0, y_pos, 0])
            return grp

        # Layers bottom → top (rendered bottom to top in screen space, staggered y)
        layer_source = make_layer("SOURCE VIDEO FRAME", "already rendered",
                                  SLATE, fill_color="#F7F7F7", y_pos=-1.8)
        layer_wave   = make_layer("OSCILLOSCOPE WAVEFORM", "teal amplitude bar",
                                  ACCENT_TEAL, fill_color="#EFF9F5", y_pos=-0.8)
        layer_karaoke= make_layer("KARAOKE WORD LAYER", "'She walks in beauty' — current word bright",
                                  ACCENT_TEAL, fill_color="#EFF9F5", y_pos=0.2)
        layer_audio  = make_layer("AUDIO", "extracted from source — waveform & picture locked",
                                  CRIMSON, fill_color="#FFF5F5", y_pos=1.2)

        # Dashed line from source to audio (showing extraction)
        dash_line = DashedLine(
            layer_source.get_right() + RIGHT * 0.15 + UP * 0.0,
            layer_audio.get_right()  + RIGHT * 0.15 + DOWN * 0.0,
            dash_length=0.18, dashed_ratio=0.5,
            stroke_color=CRIMSON, stroke_width=2,
        )

        layers = [layer_source, layer_wave, layer_karaoke, layer_audio]
        self.play(LaggedStart(*[FadeIn(l, shift=UP * 0.15) for l in layers],
                              lag_ratio=0.2), run_time=1.2)
        self.play(Create(dash_line), run_time=0.5)
        self.wait(0.3)

        caption = SerifLabel("decorate the finished frame — never re-render.",
                             accent=CRIMSON, size=21)
        caption.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.6)
        self.wait(10.9)


# ──────────────────────────────────────────────────────────
# B09 — THE OVERLAY HERO (13s)  — HERO BEAT, most visual care
# Dark canvas #2A1A0E.
# Center: teal oscilloscope waveform pulsing across full width.
# Below: "SHE WALKS IN BEAUTY" in EB Garamond white 80px.
# Smaller teal: "ONE COMMAND · ONE EXTRACT · ONE RENDER".
# No caption — the visual is the statement.
# ──────────────────────────────────────────────────────────
class B09_TheOverlayHero(Scene):
    def construct(self):
        self.camera.background_color = "#2A1A0E"

        # Teal oscilloscope waveform — sine curve across full width
        wave = ParametricFunction(
            lambda t: np.array([t, 0.55 * np.sin(2.2 * t + 0.3), 0]),
            t_range=[-6.8, 6.8, 0.04],
            color=ACCENT_TEAL,
            stroke_width=5,
        )
        wave.move_to(UP * 0.9)

        # Second harmonic for richness
        wave2 = ParametricFunction(
            lambda t: np.array([t, 0.22 * np.sin(4.4 * t + 1.1), 0]),
            t_range=[-6.8, 6.8, 0.04],
            color=ACCENT_TEAL,
            stroke_width=2.5,
            stroke_opacity=0.5,
        )
        wave2.move_to(UP * 0.9)

        # Title — EB Garamond large
        title = Text("SHE WALKS IN BEAUTY", font=SERIF, color=WHITE,
                     font_size=52, weight=BOLD)
        title.move_to(DOWN * 0.4)
        if title.width > 12.5:
            title.scale_to_fit_width(12.5)

        # Subtitle — three tools condensed
        subtitle = Text("ONE COMMAND  ·  ONE EXTRACT  ·  ONE RENDER",
                        font=MONO, color=ACCENT_TEAL, font_size=20)
        subtitle.move_to(DOWN * 1.5)
        if subtitle.width > 12.5:
            subtitle.scale_to_fit_width(12.5)

        self.play(Create(wave), Create(wave2), run_time=1.0)
        self.play(Write(title), run_time=0.9)
        self.play(FadeIn(subtitle, shift=UP * 0.1), run_time=0.7)
        self.wait(10.4)


# ──────────────────────────────────────────────────────────
# B10 — THE CHOICE (18s)  — HERO SPLIT, most care
# Dark canvas #2A1A0E.
# Vertical divider.
# LEFT: 'POEM' label in teal; "burned-in words / compete with listening" white;
#        "you cannot be moved / and read at the same time" in red.
# RIGHT: 'PROMO AUDIOGRAM' in teal; "words / are the visual" white;
#         "there is no film / to protect" in teal.
# Bottom full-width: "THE MACHINE SYNCS EVERY WORD — YOU DECIDE WHAT THE VIEWER READS"
# ──────────────────────────────────────────────────────────
class B10_TheChoice(Scene):
    def construct(self):
        self.camera.background_color = "#2A1A0E"

        # Vertical divider
        divider = Line(UP * 3.4, DOWN * 2.2,
                       stroke_color=WHITE, stroke_width=1.5, stroke_opacity=0.25)
        divider.move_to(ORIGIN)
        self.play(Create(divider), run_time=0.4)

        # ---- LEFT: POEM
        poem_lbl = Text("POEM", font=DISPLAY, color=ACCENT_TEAL, font_size=24, weight=BOLD)
        poem_lbl.move_to(LEFT * 3.2 + UP * 2.6)

        poem_body = VGroup(
            Text("burned-in words", font=SERIF, color=WHITE, font_size=20),
            Text("compete with listening.", font=SERIF, color=WHITE, font_size=20),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        poem_body.move_to(LEFT * 3.2 + UP * 1.3)

        poem_warning = VGroup(
            Text("you cannot be moved", font=SERIF, color=CRIMSON, font_size=18, slant=ITALIC),
            Text("and read at the same time.", font=SERIF, color=CRIMSON, font_size=18, slant=ITALIC),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        poem_warning.move_to(LEFT * 3.2 + DOWN * 0.1)

        self.play(FadeIn(poem_lbl, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(poem_body, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(poem_warning, shift=DOWN * 0.1), run_time=0.5)
        self.wait(0.3)

        # ---- RIGHT: PROMO AUDIOGRAM
        promo_lbl = Text("PROMO AUDIOGRAM", font=DISPLAY, color=ACCENT_TEAL,
                         font_size=20, weight=BOLD)
        promo_lbl.move_to(RIGHT * 3.2 + UP * 2.6)
        if promo_lbl.width > 5.5:
            promo_lbl.scale_to_fit_width(5.5)

        promo_body = VGroup(
            Text("words", font=SERIF, color=WHITE, font_size=20),
            Text("are the visual.", font=SERIF, color=WHITE, font_size=20),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        promo_body.move_to(RIGHT * 3.2 + UP * 1.3)

        promo_note = VGroup(
            Text("there is no film", font=SERIF, color=ACCENT_TEAL, font_size=18, slant=ITALIC),
            Text("to protect.", font=SERIF, color=ACCENT_TEAL, font_size=18, slant=ITALIC),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        promo_note.move_to(RIGHT * 3.2 + DOWN * 0.1)

        self.play(FadeIn(promo_lbl, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(promo_body, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(promo_note, shift=DOWN * 0.1), run_time=0.5)
        self.wait(0.4)

        # Bottom full-width statement
        bottom = Text(
            "THE MACHINE SYNCS EVERY WORD — YOU DECIDE WHAT THE VIEWER READS",
            font=DISPLAY, color=WHITE, font_size=18, weight=BOLD
        )
        if bottom.width > 12.5:
            bottom.scale_to_fit_width(12.5)
        bottom.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(bottom, shift=UP * 0.1), run_time=0.8)
        self.wait(13.1)
