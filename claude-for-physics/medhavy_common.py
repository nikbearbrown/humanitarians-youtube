"""medhavy_common.py — shared infrastructure for every Physics_textbook
medhavy-palette Manim video (see memory: project_physics_textbook_video_pipeline).

Import from a <slug>.py script like:

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # .../vids/videos/
    from medhavy_common import *

Provides: palette constants, safe-area helpers, portrait detection, the
caption-schedule builder, and MedhavyScene (a Scene subclass that fixes the
frozen-frame caption bug and provides question_card()/init_captions() so
subclasses don't re-implement them).
"""
import textwrap

from manim import *

# ---- medhavy palette (Okabe-Ito, colorblind-safe) ----
# CREAM overridden to pure white per professor feedback — stock medhavy
# cream (#F0EAD6) read as "dirty brown" on screen.
CREAM = "#FFFFFF"
INK = "#000000"
TEAL = "#009E73"
CRIMSON = "#D55E00"
SLATE = "#4D4D4D"
GOLD = "#F0E442"

CAPTION_FONT = 15
# PT Sans, not Open Sans: Open Sans renders mid-word gaps in Manim/Pango
# captions at this size (confirmed bug); PT Sans fixed it.
CAPTION_STYLE = "PT Sans"
CAPTION_WRAP = 30
# No separate title card: question_card() is the sole opening card for shorts
# and starts at t=0, voiced by beat B00Q (first in the beat sheet), so the
# caption schedule needs no offset before it.
TITLE_DURATION = 0.0
CAPTION_WORDS_PER_CHUNK = 7
SAFE_MARGIN = 0.6


def is_portrait():
    """Call once at module level. config.frame_width does NOT auto-recompute
    from -r's aspect ratio in this Manim version (confirmed bug) — detect
    orientation from pixel dims instead and force frame_width ourselves."""
    portrait = config.pixel_width < config.pixel_height
    if portrait:
        config.frame_width = config.frame_height * config.pixel_width / config.pixel_height
    config.background_color = CREAM
    return portrait


def safe_half_w():
    return config.frame_width / 2 - SAFE_MARGIN


def safe_half_h():
    return config.frame_height / 2 - SAFE_MARGIN


def crisp_text(text, font_size, **kwargs):
    """Text rendered at 4x size then scaled back down. At small font_size
    Manim/Pango kerning drops or inserts gaps mid-word (confirmed:
    "centripetalforce", "trace s naps" even in PT Sans); rendering large and
    scaling fixes it with identical on-screen size. Use for every small label."""
    return Text(text, font_size=font_size * 4, **kwargs).scale(0.25)


def build_caption_schedule(sheet, durs, narr, title_duration=TITLE_DURATION,
                           words_per_chunk=CAPTION_WORDS_PER_CHUNK):
    """(start_s, end_s, text) for every short caption chunk across the whole
    video, in absolute self.time coordinates. Chunked ~7 words at a time, not
    a whole beat's narration at once — that overflows the frame (confirmed
    bug)."""
    schedule = []
    t = title_duration
    for b in sheet["beats"]:
        bid = b["beat_id"]
        dur = durs[bid]
        words = narr[bid].split()
        chunks = [
            " ".join(words[i:i + words_per_chunk])
            for i in range(0, len(words), words_per_chunk)
        ] or [""]
        chunk_dur = dur / len(chunks)
        for c in chunks:
            schedule.append((t, t + chunk_dur, c))
            t += chunk_dur
    return schedule


class MedhavyScene(Scene):
    """Base class for every Physics_textbook medhavy video.

    Subclass, set self.PORTRAIT (from is_portrait()) at the top of
    construct(), then call self.init_captions(schedule, caption_y) and
    self.question_card(NARR["B00Q"], DURS["B00Q"]) when self.PORTRAIT — self.wait()
    already disables Manim's frozen-frame optimization automatically
    whenever PORTRAIT, so scene-time-driven captions never silently freeze
    during a long wait (confirmed bug, fixed here once for every video).
    """

    PORTRAIT = False

    @property
    def time(self):
        # Scene itself has no elapsed-time attribute in this Manim version
        # (only self.renderer.time does) — confirmed bug, proxy it here so
        # caption updaters (which read self.time) don't crash with
        # AttributeError on the very first frame.
        return self.renderer.time

    def wait(self, duration=1.0, stop_condition=None, frozen_frame=None):
        if self.PORTRAIT and frozen_frame is None:
            frozen_frame = False
        return super().wait(duration, stop_condition=stop_condition, frozen_frame=frozen_frame)

    def question_card(self, question_text, duration):
        """Sole opening card for shorts: the driving question styled as a
        title (voiced by beat B00Q). Total run time == duration, the B00Q
        audio's measured length, so B00's visuals start when B00's audio does."""
        wrapped = "\n".join(textwrap.wrap(question_text, width=22))
        question = Text(wrapped, font_size=30, color=INK, line_spacing=1.3).move_to(ORIGIN)
        max_w = 2 * safe_half_w()
        if question.width > max_w:
            question.scale_to_fit_width(max_w)
        underline = Line(
            question.get_corner(DOWN + LEFT) + DOWN * 0.25,
            question.get_corner(DOWN + RIGHT) + DOWN * 0.25,
            color=CRIMSON, stroke_width=5,
        )
        self.play(Write(question), Create(underline), run_time=1.0)
        self.wait(max(duration - 1.6, 0.5))
        self.play(FadeOut(question), FadeOut(underline), run_time=0.6)

    def init_captions(self, schedule, caption_y):
        self.caption_schedule = schedule
        self.caption_idx = -1
        caption_mobj = VGroup()

        def updater(m):
            t = self.time
            idx = self.caption_idx
            for i, (start, end, _text) in enumerate(self.caption_schedule):
                if start <= t < end:
                    idx = i
                    break
            if idx == self.caption_idx or idx >= len(self.caption_schedule):
                return
            self.caption_idx = idx
            _, _, chunk_text = self.caption_schedule[idx]
            if not chunk_text:
                m.become(VGroup())
                return
            wrapped = "\n".join(textwrap.wrap(chunk_text, width=CAPTION_WRAP))
            text = crisp_text(
                wrapped, CAPTION_FONT, color=INK, line_spacing=1.15, font=CAPTION_STYLE
            ).move_to([0, caption_y, 0])
            backing = SurroundingRectangle(
                text, color=SLATE, fill_color=CREAM, fill_opacity=0.92, buff=0.2, corner_radius=0.08,
            )
            m.become(VGroup(backing, text))

        caption_mobj.add_updater(updater)
        self.add(caption_mobj)
