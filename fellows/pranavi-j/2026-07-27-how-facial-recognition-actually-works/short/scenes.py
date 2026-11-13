"""
Manim scenes for the 9:16 SHORT derived from
2026-07-27-how-facial-recognition-actually-works.

Built 2026-08-26/28 via runtime/scripts/shorts.py's auto-plan (kept B07, the
NIST evidence beat, protected with --keep — the auto-plan's first choice
was to drop B07 since it's the single longest beat, but that beat is the
video's factual backbone; --keep forced the planner to find its next-best
cut instead, which turned out to be B09 WORKED-EXAMPLE, 26.86s). The result
is 11 of the parent's 12 beats (B09 dropped) at ~170s, under the 180s cap,
with B11's narration rewritten by shorts.py to point viewers at the long.

PORTRAIT FRAME FIX — READ BEFORE TOUCHING ANY NUMBER BELOW:
Manim CE does NOT recompute frame_width when you pass a portrait
`-r WIDTH,HEIGHT` — it leaves frame_width at its 16:9 default (~14.22
units) and GROWS frame_height instead (~25.3 units tall at 2160x3840),
confirmed empirically via `self.camera.frame_width/height` inside a probe
scene. A scene composed for a narrow ~4.5-unit frame would render at a
THIRD its intended size if this were left unpatched — everything clustered
in the top slice of a much taller canvas, which is exactly the "5-8%
canvas fill" GATE V failure a first, unpatched pass produced here (see
BUILD-LOG.md). The toolkit already has the fix and its own name for it —
this is "the bn_layout fix" in runtime/manim/animated_graphics.py's own
header comment — so this file applies the identical patch: keep
frame_height at 8.0, derive frame_width from the real pixel aspect ratio.
That restores the same ~4.5-unit-wide x ~8-unit-tall working frame GATE B's
own `--portrait` mode already assumes (safe half-extents ±1.95 x / ±3.4 y,
confirmed by its own printed report), so every beat below is composed for
THAT frame — matching GATE B and GATE V's shared assumption, not the
raw (unpatched) manim default.
"""

from manim import config

try:
    _pw = getattr(config, "pixel_width", None)
    _ph = getattr(config, "pixel_height", None)
    if _pw and _ph and abs(config.frame_width - config.frame_height * _pw / _ph) > 0.01:
        config.frame_width = config.frame_height * (_pw / _ph)
except Exception:
    pass

from manim import *

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool
    "crimson": "#E4572E", # bad / CVD-safe warm
    "slate":  "#29335C",  # structure
    "gold":   "#F3A712",  # fill only
    "sage":   "#A8C686",  # human / growth
}

MONO = "Courier New"


def fit(mob, max_w):
    """Scale down only if wider than max_w — never scale up short text to an
    artificial fixed width (that starves neighboring elements of room)."""
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card. Same structure as the parent (already a
# vertical stack), just narrowed so the bracketing rules and title fit the
# real ~4.5-unit-wide portrait frame instead of the 16:9 ~14.2-unit one.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(Text(
            "How Facial Recognition Actually Works",
            color=PALETTE["ink"], font_size=34, weight="BOLD",
        ), 3.6)
        title_line2 = fit(Text(
            "(And When It Shouldn't)",
            color=PALETTE["ink"], font_size=34, weight="BOLD",
        ), 3.6)
        title = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.32)

        top_rule = Line(LEFT * 1.75, RIGHT * 1.75, color=PALETTE["gold"], stroke_width=3.5)
        bottom_rule = Line(LEFT * 1.75, RIGHT * 1.75, color=PALETTE["gold"], stroke_width=3.5)
        handle = fit(Text("@HumanitariansAI", color=PALETTE["slate"], font_size=32), 3.4)

        # buff bumped 1.0 -> 1.35: GATE V measured this card at 51% canvas
        # fill (just under the 55% floor) at buff=1.0 — real extracted
        # frame looked fine, just needed a little more of the spacing this
        # card already leans on (same technique as the parent's own B00).
        VGroup(top_rule, title, bottom_rule, handle).arrange(
            DOWN, buff=1.35
        ).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.35)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.8)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.5)
        # silent beat, reuses parent's silent mp3 (4.60s) unchanged.
        self.wait(2.95)


# --------------------------------------------------------------------------- #
# B01 — INTRO: spoken personal-intro card. Same vertical stack as the
# parent, narrowed fit() widths, and the summary re-wrapped from 2 lines to
# 3 shorter ones so no line needs to shrink to an illegibly small font.
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        avatar = Circle(radius=0.85, color=PALETTE["teal"], stroke_width=3,
                         fill_color=PALETTE["teal"], fill_opacity=0.12)
        initials = Text("SPJ", color=PALETTE["teal"], font_size=34).move_to(avatar)
        avatar_group = VGroup(avatar, initials).move_to(UP * 2.1)
        self.play(FadeIn(avatar_group, scale=1.15), run_time=0.6)
        self.wait(0.2)

        name = fit(Text("Sai Pranavi J.", color=PALETTE["ink"],
                         font_size=34, weight="BOLD"), 3.4)
        name.next_to(avatar_group, DOWN, buff=0.35)
        self.play(Write(name), run_time=0.7)

        underline = Line(color=PALETTE["gold"], stroke_width=3)
        underline.put_start_and_end_on(
            name.get_corner(DL) + DOWN * 0.14, name.get_corner(DR) + DOWN * 0.14
        )
        self.play(Create(underline), run_time=0.35)

        role_chip = RoundedRectangle(width=3.0, height=0.55, corner_radius=0.15,
                                      fill_color=PALETTE["slate"], fill_opacity=0.18,
                                      stroke_color=PALETTE["slate"], stroke_width=2)
        role_chip.next_to(underline, DOWN, buff=0.3)
        role_txt = fit(Text("Fellow, Humanitarians AI", color=PALETTE["ink"],
                             font_size=19), 2.8)
        role_txt.move_to(role_chip)
        self.play(FadeIn(role_chip), Write(role_txt), run_time=0.6)
        self.wait(0.2)

        summary_line1 = fit(Text(
            "How facial recognition actually works —",
            color=PALETTE["ink"], font_size=21
        ), 3.5)
        summary_line2 = fit(Text(
            "not a yes-or-no match, but a probability —",
            color=PALETTE["ink"], font_size=21
        ), 3.5)
        summary_line3 = fit(Text(
            "and when it deserves scrutiny.",
            color=PALETTE["ink"], font_size=21
        ), 3.5)
        summary = VGroup(summary_line1, summary_line2, summary_line3).arrange(DOWN, buff=0.2)
        summary.next_to(role_chip, DOWN, buff=0.5)
        self.play(Write(summary), run_time=1.1)
        # retimed 2026-10-20: narration shortened to 11.06s ("Sai Pranavi J."
        # retrofit, was 11.66s) — shifted this hold by the same -0.6s delta
        # (was 7.9s), all preceding play/wait timings unchanged.
        self.wait(7.3)


# --------------------------------------------------------------------------- #
# B02 — HOOK: the 4 context chips (Phone/Airport/Store/Policing) were a
# horizontal row in the parent (arrange(RIGHT), ~11.9 units wide — nearly
# 3x the real portrait frame width). Restacked into a vertical column.
# --------------------------------------------------------------------------- #
class B02_EverywhereHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(Text("Facial recognition is", color=PALETTE["ink"], font_size=28), 3.6)
        title_line2 = fit(Text("everywhere right now", color=PALETTE["ink"], font_size=28), 3.6)
        title = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.18)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.7)
        self.wait(0.3)

        contexts = [
            ("Phone", PALETTE["teal"]),
            ("Airport", PALETTE["slate"]),
            ("Store", PALETTE["gold"]),
            ("Policing", PALETTE["crimson"]),
        ]
        chips = VGroup()
        for label, color in contexts:
            chip = RoundedRectangle(width=3.2, height=0.68, corner_radius=0.14,
                                     fill_color=color, fill_opacity=0.18,
                                     stroke_color=color, stroke_width=2.5)
            txt = Text(label, color=PALETTE["ink"], font_size=24).move_to(chip)
            chips.add(VGroup(chip, txt))
        chips.arrange(DOWN, buff=0.28).next_to(title, DOWN, buff=0.5)

        for c in chips:
            self.play(FadeIn(c, scale=1.08), run_time=0.5)
        self.wait(0.4)

        debate_line1 = fit(Text(
            "There's real, unresolved disagreement",
            color=PALETTE["crimson"], font_size=22
        ), 3.6)
        debate_line2 = fit(Text(
            "about whether that's okay.",
            color=PALETTE["crimson"], font_size=22
        ), 3.6)
        debate = VGroup(debate_line1, debate_line2).arrange(DOWN, buff=0.18)
        debate.next_to(chips, DOWN, buff=0.5)
        self.play(Write(debate), run_time=1.0)
        # tuned close to actual_duration_s (15.48s, reused unchanged).
        self.wait(11.0)


# --------------------------------------------------------------------------- #
# B03 — FRAMEWORK: the 3 lens-question rows were left-anchored at LEFT*4.6 —
# off the real ~2.25-unit portrait half-width entirely. Recentered as
# balanced badge+label row-groups; the stakes gradient bar shrunk from
# width 8.4 (nearly 2x the real frame width) to 3.0 and centered.
# --------------------------------------------------------------------------- #
class B03_FrameworkLens(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text("The lens", color=PALETTE["ink"], font_size=32), 3.4)
        title.move_to(UP * 3.1)
        self.play(Write(title), run_time=0.6)
        self.wait(0.2)

        questions = [
            "What's it used for?",
            "What happens if it's wrong?",
            "How confident is the claim, really?",
        ]
        y = 2.15
        for i, q in enumerate(questions, start=1):
            badge = Circle(radius=0.26, color=PALETTE["slate"], stroke_width=2.2,
                            fill_color=PALETTE["slate"], fill_opacity=0.15)
            num = Text(str(i), color=PALETTE["ink"], font_size=20).move_to(badge)
            label = fit(Text(q, color=PALETTE["ink"], font_size=20), 2.6)
            label.next_to(badge, RIGHT, buff=0.3)
            row = VGroup(badge, num, label)
            row.move_to(UP * y)
            self.play(FadeIn(badge, scale=1.2), FadeIn(num), Write(label), run_time=0.7)
            self.wait(0.2)
            y -= 1.05
        self.wait(0.3)

        track = RoundedRectangle(width=3.0, height=0.4, corner_radius=0.18,
                                  fill_color=PALETTE["ink"], fill_opacity=0.07,
                                  stroke_color=PALETTE["slate"], stroke_width=1.4)
        track.move_to(DOWN * 1.55)
        self.play(FadeIn(track), run_time=0.4)

        fill_tracker = ValueTracker(0.01)
        fill = always_redraw(lambda: Rectangle(
            width=max(0.02, 3.0 * 0.98 * fill_tracker.get_value()), height=0.4,
            fill_opacity=0.9, stroke_width=0
        ).set_fill(color=[PALETTE["sage"], PALETTE["gold"], PALETTE["crimson"]])
         .move_to(track.get_left() + RIGHT * (3.0 * 0.98 * fill_tracker.get_value()) / 2))
        self.add(fill)
        self.play(fill_tracker.animate.set_value(1.0), run_time=1.0)

        low = Text("low-stakes", color=PALETTE["sage"], font_size=15).next_to(track, DOWN, buff=0.2).align_to(track, LEFT)
        high = Text("high-stakes", color=PALETTE["crimson"], font_size=15).next_to(track, DOWN, buff=0.2).align_to(track, RIGHT)
        self.play(FadeIn(low), FadeIn(high), run_time=0.5)

        thesis_line1 = fit(Text("Scrutiny should scale", color=PALETTE["ink"], font_size=22), 3.4)
        thesis_line2 = fit(Text("with those answers.", color=PALETTE["ink"], font_size=22), 3.4)
        thesis = VGroup(thesis_line1, thesis_line2).arrange(DOWN, buff=0.18)
        thesis.move_to(DOWN * 2.75)
        # FadeIn (not Write) — same fix as the parent's B04: this scene's
        # native runtime places this animation's midpoint right at the
        # GATE V 50% sample point, and Write()'s letter-by-letter trace
        # reads as a garbled/overlapping-glyph defect at exactly that
        # frame (confirmed by direct extraction — see BUILD-LOG.md).
        self.play(FadeIn(thesis), run_time=0.8)
        # tuned close to actual_duration_s (11.81s, reused unchanged).
        self.wait(5.3)


# --------------------------------------------------------------------------- #
# B04 — MECHANISM: the detect->embed->compare->score pipeline was 4 boxes
# arranged RIGHT (a wide horizontal flow, face icon further left still) —
# the single beat the task brief calls out by name. Fully restacked into a
# vertical column: face icon on top, arrows pointing DOWN instead of RIGHT.
# --------------------------------------------------------------------------- #
class B04_PipelineMechanism(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text("What it actually does", color=PALETTE["ink"], font_size=26), 3.6)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.6)

        tag = Text("Q3: how confident?", color=PALETTE["slate"], font_size=15, font=MONO)
        tag.next_to(title, DOWN, buff=0.18)
        self.play(FadeIn(tag), run_time=0.3)
        self.wait(0.2)

        face = Circle(radius=0.34, color=PALETTE["slate"], stroke_width=2.2,
                      fill_color=PALETTE["slate"], fill_opacity=0.08)
        eye_l = Dot(face.get_center() + LEFT * 0.12 + UP * 0.08, radius=0.03, color=PALETTE["ink"])
        eye_r = Dot(face.get_center() + RIGHT * 0.12 + UP * 0.08, radius=0.03, color=PALETTE["ink"])
        smile = Arc(radius=0.14, start_angle=-2.6, angle=1.2, color=PALETTE["ink"], stroke_width=2)
        smile.move_to(face.get_center() + DOWN * 0.08)
        face_icon = VGroup(face, eye_l, eye_r, smile)
        face_icon.next_to(tag, DOWN, buff=0.28)
        self.play(Create(face), FadeIn(eye_l), FadeIn(eye_r), Create(smile), run_time=0.7)

        stages = ["Detect", "Embedding", "Compare\nto DB", "Score"]
        boxes = VGroup(*[
            RoundedRectangle(width=2.9, height=0.56, corner_radius=0.1,
                              fill_color=PALETTE["teal"], fill_opacity=0.15,
                              stroke_color=PALETTE["teal"], stroke_width=2)
            for _ in stages
        ])
        boxes.arrange(DOWN, buff=0.26)
        boxes.next_to(face_icon, DOWN, buff=0.38)
        labels = VGroup(*[
            Text(s, color=PALETTE["ink"], font_size=18, line_spacing=0.9).move_to(b)
            for s, b in zip(stages, boxes)
        ])

        entry_arrow = Arrow(face_icon.get_bottom(), boxes[0].get_top(), buff=0.08,
                             color=PALETTE["ink"], stroke_width=2, max_tip_length_to_length_ratio=0.35)
        self.play(GrowArrow(entry_arrow), run_time=0.4)

        arrows = VGroup()
        for i in range(len(boxes) - 1):
            arrows.add(Arrow(boxes[i].get_bottom(), boxes[i + 1].get_top(), buff=0.05,
                              color=PALETTE["ink"], stroke_width=2, max_tip_length_to_length_ratio=0.4))

        for i, (box, label) in enumerate(zip(boxes, labels)):
            self.play(Create(box), Write(label), run_time=0.45)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.25)
        self.wait(0.1)

        gauge_bg = RoundedRectangle(width=3.0, height=0.42, corner_radius=0.2,
                                     fill_color=PALETTE["ink"], fill_opacity=0.08,
                                     stroke_color=PALETTE["slate"], stroke_width=1.5)
        gauge_bg.next_to(boxes, DOWN, buff=0.4)
        self.play(FadeIn(gauge_bg), run_time=0.4)

        gauge_tracker = ValueTracker(0.01)
        gauge_fill = always_redraw(lambda: Rectangle(
            width=max(0.02, 3.0 * 0.98 * gauge_tracker.get_value()), height=0.42,
            fill_color=PALETTE["crimson"], fill_opacity=0.9, stroke_width=0
        ).move_to(gauge_bg.get_left() + RIGHT * (3.0 * 0.98 * gauge_tracker.get_value()) / 2))
        self.add(gauge_fill)
        self.play(gauge_tracker.animate.set_value(1.0), run_time=1.0)

        pct = Text("98%", color=PALETTE["bg"], font_size=18).move_to(gauge_bg.get_left() + RIGHT * 0.48)
        self.play(FadeIn(pct), run_time=0.4)

        caption_line1 = fit(Text(
            "A 98% match is a probability,", color=PALETTE["crimson"], font_size=19
        ), 3.6)
        caption_line2 = fit(Text(
            "not a certainty.", color=PALETTE["crimson"], font_size=19
        ), 3.6)
        caption = VGroup(caption_line1, caption_line2).arrange(DOWN, buff=0.14)
        caption.next_to(gauge_bg, DOWN, buff=0.28)
        # FadeIn (not Write) — same fix as the parent's B04: a whole-string
        # opacity fade settles instantly, never straddling a mid-Write
        # glyph-trace across the GATE V 50% sample point.
        self.play(FadeIn(caption), run_time=0.3)
        # tuned close to actual_duration_s (21.12s, reused unchanged); the
        # caption above finishes at native ~6.95s, well under the 50% mark
        # (~10.55s of this scene's ~21.1s native total).
        self.wait(14.15)


# --------------------------------------------------------------------------- #
# B05 — BENEFITS: same vertical checklist as the parent, re-indented
# (LEFT*4.5 -> LEFT*1.5) and each item's label re-wrapped to 2 short lines
# so it doesn't need to shrink to an illegible font at ~2.5 units wide.
# --------------------------------------------------------------------------- #
class B05_LegitimateUses(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text("The low-stakes side", color=PALETTE["ink"], font_size=25), 3.5)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.6)

        badge_bg = RoundedRectangle(width=2.3, height=0.48, corner_radius=0.14,
                                     fill_color=PALETTE["sage"], fill_opacity=0.25,
                                     stroke_color=PALETTE["sage"], stroke_width=2)
        badge_bg.next_to(title, DOWN, buff=0.28)
        badge_txt = Text("LOW-STAKES", color=PALETTE["ink"], font_size=15).move_to(badge_bg)
        self.play(FadeIn(badge_bg), Write(badge_txt), run_time=0.5)
        self.wait(0.2)

        items = [
            "Assistive tools for\nvisually impaired users",
            "Unlocking your\nown phone",
            "Reuniting missing people\nwith family",
            "Supporting medical\ndiagnosis",
        ]
        y = 1.55
        for it in items:
            dot = Dot(radius=0.1, color=PALETTE["sage"])
            check = Text("✓", color=PALETTE["bg"], font_size=13).move_to(dot)
            label = fit(Text(it, color=PALETTE["ink"], font_size=19, line_spacing=0.9), 2.5)
            dot.move_to(LEFT * 1.5 + UP * y)
            check.move_to(dot)
            label.next_to(dot, RIGHT, buff=0.3)
            self.play(FadeIn(dot, scale=1.3), FadeIn(check), Write(label), run_time=0.7)
            y -= 1.2
        # tuned close to actual_duration_s (15.14s, reused unchanged).
        self.wait(11.0)


# --------------------------------------------------------------------------- #
# B06 — HARMS: same re-indent treatment as B05.
# --------------------------------------------------------------------------- #
class B06_HarmfulUses(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text("The high-stakes side", color=PALETTE["ink"], font_size=26), 3.5)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.6)

        badge_bg = RoundedRectangle(width=2.6, height=0.48, corner_radius=0.14,
                                     fill_color=PALETTE["crimson"], fill_opacity=0.2,
                                     stroke_color=PALETTE["crimson"], stroke_width=2)
        badge_bg.next_to(title, DOWN, buff=0.28)
        badge_txt = Text("HIGH-STAKES", color=PALETTE["ink"], font_size=15).move_to(badge_bg)
        self.play(FadeIn(badge_bg), Write(badge_txt), run_time=0.5)
        self.wait(0.2)

        items = [
            "Mass surveillance\nwithout consent",
            "Tracking shoppers who\nnever agreed to it",
            "Biometric data can't be\nreset like a password",
        ]
        # y-start/decrement bumped (1.35/1.3 -> 1.6/1.65): GATE V measured
        # this scene at 52% canvas fill (just under the 55% floor) — real
        # extracted frame showed a well-composed list with empty space
        # below the last item, so items are simply spread a bit further.
        y = 1.6
        for it in items:
            dot = Dot(radius=0.1, color=PALETTE["crimson"])
            cross = Text("✗", color=PALETTE["bg"], font_size=13).move_to(dot)
            label = fit(Text(it, color=PALETTE["ink"], font_size=19, line_spacing=0.9), 2.5)
            dot.move_to(LEFT * 1.5 + UP * y)
            cross.move_to(dot)
            label.next_to(dot, RIGHT, buff=0.3)
            self.play(FadeIn(dot, scale=1.3), FadeIn(cross), Write(label), run_time=0.7)
            y -= 1.65
        # tuned close to actual_duration_s (12.38s, reused unchanged).
        self.wait(8.95)


# --------------------------------------------------------------------------- #
# B07 — EVIDENCE: the NIST FRVT chart was two vertical bars side-by-side
# (LEFT*2.3/RIGHT*2.3, ~6.6 units wide total — well over the real portrait
# frame). Redesigned as two horizontal bars (rightward fill = magnitude of
# the demographic gap) stacked vertically — portrait's natural comparison
# layout, reads top-to-bottom as "most algorithms" then "best-performing".
# --------------------------------------------------------------------------- #
class B07_NistEvidence(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(Text("NIST FRVT — Demographic", color=PALETTE["ink"], font_size=21), 3.6)
        title_line2 = fit(Text("Effects (2019)", color=PALETTE["ink"], font_size=21), 3.6)
        title = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.1)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.6)

        cite = fit(Text(
            "189 algorithms - 18.27M images", color=PALETTE["ink"], font_size=14, font=MONO
        ), 3.4)
        cite.next_to(title, DOWN, buff=0.22)
        self.play(FadeIn(cite), run_time=0.5)
        self.wait(0.3)

        bar_w, bar_h = 3.0, 0.48

        def make_row(label_text, ratio, fill_color, tag_text):
            lbl = fit(Text(label_text, color=PALETTE["ink"], font_size=18), 3.2)
            track = RoundedRectangle(width=bar_w, height=bar_h, corner_radius=0.08,
                                      stroke_color=PALETTE["ink"], stroke_width=1.2, fill_opacity=0.0)
            track.next_to(lbl, DOWN, buff=0.16)
            tracker = ValueTracker(0.01)
            fill_mob = always_redraw(lambda: Rectangle(
                width=max(0.02, bar_w * 0.95 * ratio * tracker.get_value()), height=bar_h,
                fill_color=fill_color, fill_opacity=0.85, stroke_width=0
            ).move_to(track.get_left() + RIGHT * (bar_w * 0.95 * ratio * tracker.get_value()) / 2))
            tag = fit(Text(tag_text, color=fill_color, font_size=15), 3.2)
            tag.next_to(track, DOWN, buff=0.12).align_to(track, LEFT)
            return lbl, track, tracker, fill_mob, tag

        lbl1, track1, t1, fill1, tag1 = make_row(
            "Most algorithms", 0.88, PALETTE["crimson"], "real gap")
        lbl2, track2, t2, fill2, tag2 = make_row(
            "Best-performing algorithms", 0.10, PALETTE["sage"], "~near zero")

        group1 = VGroup(lbl1, track1, tag1)
        group1.next_to(cite, DOWN, buff=0.5)
        group2 = VGroup(lbl2, track2, tag2)
        group2.next_to(group1, DOWN, buff=0.42)

        self.play(FadeIn(lbl1), FadeIn(track1), run_time=0.5)
        self.add(fill1)
        self.play(t1.animate.set_value(1.0), run_time=1.1)
        self.play(FadeIn(tag1), run_time=0.4)
        self.wait(0.2)

        self.play(FadeIn(lbl2), FadeIn(track2), run_time=0.5)
        self.add(fill2)
        self.play(t2.animate.set_value(1.0), run_time=1.1)
        self.play(FadeIn(tag2), run_time=0.4)
        self.wait(0.5)

        dissent_line1 = fit(Text(
            "Security Industry Association:", color=PALETTE["gold"], font_size=17
        ), 3.6)
        dissent_line2 = fit(Text(
            "this is overstated.", color=PALETTE["gold"], font_size=17
        ), 3.6)
        dissent = VGroup(dissent_line1, dissent_line2).arrange(DOWN, buff=0.1)
        dissent.next_to(group2, DOWN, buff=0.5)
        self.play(FadeIn(dissent), run_time=0.6)
        # tuned close to actual_duration_s (31.27s, the longest kept beat —
        # protected from the auto-plan's drop via --keep B07; this is the
        # video's factual backbone, so it stays even though it's the
        # single longest beat). Everything settles by native ~6.7s, far
        # under the 50% mark (~15.6s of ~31.2s native total).
        self.wait(24.5)


# --------------------------------------------------------------------------- #
# B08 — FRAMEWORK-CALLBACK: the fluency-trap split panel was two boxes
# side-by-side at LEFT*3.0/RIGHT*3.0, width 4.4 each — nearly the ENTIRE
# 16:9 frame width on its own. Restacked top/bottom, each box narrowed to
# ~3.3 units so both fit, one above the other, on the real portrait canvas.
# --------------------------------------------------------------------------- #
class B08_FluencyTrap(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(Text("The same trap as a", color=PALETTE["ink"], font_size=23), 3.6)
        title_line2 = fit(Text("fluent AI paragraph", color=PALETTE["ink"], font_size=23), 3.6)
        title = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.1)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.6)
        self.wait(0.3)

        top_box = RoundedRectangle(width=3.3, height=1.2, corner_radius=0.12,
                                    fill_color=PALETTE["slate"], fill_opacity=0.08,
                                    stroke_color=PALETTE["slate"], stroke_width=2)
        top_box.next_to(title, DOWN, buff=0.55)
        lines = VGroup(*[
            Line(LEFT * (1.25 - 0.12 * i), RIGHT * 1.25, color=PALETTE["ink"], stroke_width=2.5)
            for i in range(4)
        ]).arrange(DOWN, buff=0.16).move_to(top_box)
        top_label = Text("A fluent paragraph", color=PALETTE["ink"], font_size=16)
        top_label.next_to(top_box, DOWN, buff=0.16)
        tag1 = Text("looks certain", color=PALETTE["crimson"], font_size=15)
        tag1.next_to(top_box, UP, buff=0.12)

        bottom_box = RoundedRectangle(width=3.3, height=1.2, corner_radius=0.12,
                                       fill_color=PALETTE["teal"], fill_opacity=0.08,
                                       stroke_color=PALETTE["teal"], stroke_width=2)
        bottom_box.next_to(top_label, DOWN, buff=0.55)
        score = Text("98% match", color=PALETTE["teal"], font_size=30).move_to(bottom_box)
        bottom_label = Text("A match score", color=PALETTE["ink"], font_size=16)
        bottom_label.next_to(bottom_box, DOWN, buff=0.16)
        tag2 = Text("looks certain", color=PALETTE["crimson"], font_size=15)
        tag2.next_to(bottom_box, UP, buff=0.12)

        self.play(FadeIn(top_box), Create(lines), Write(top_label), run_time=0.8)
        self.play(FadeIn(tag1), run_time=0.4)
        self.wait(0.2)
        self.play(FadeIn(bottom_box), Write(score), Write(bottom_label), run_time=0.8)
        self.play(FadeIn(tag2), run_time=0.4)
        self.wait(0.4)

        banner = RoundedRectangle(width=3.6, height=0.85, corner_radius=0.12,
                                   fill_color=PALETTE["crimson"], fill_opacity=0.92, stroke_width=0)
        banner.next_to(bottom_label, DOWN, buff=0.45)
        banner_line1 = Text("Both are a probability —", color=PALETTE["bg"], font_size=18)
        banner_line2 = Text("not a fact.", color=PALETTE["bg"], font_size=18)
        banner_txt = VGroup(banner_line1, banner_line2).arrange(DOWN, buff=0.08)
        banner_txt.move_to(banner)
        self.play(FadeIn(banner), Write(banner_txt), run_time=0.9)
        # tuned close to actual_duration_s (12.77s, reused unchanged); the
        # banner settles at native ~4.8s, safely under the 50% mark (~6.35s
        # of ~12.7s native total).
        self.wait(7.9)


# --------------------------------------------------------------------------- #
# B10 — CTA: same vertical checklist pattern as B05/B06, re-indented and
# with the 2nd/3rd questions wrapped to 2 lines so they fit ~2.6 units wide.
# --------------------------------------------------------------------------- #
class B10_YourTurn(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text("YOUR TURN", color=PALETTE["slate"], font_size=30), 3.4)
        title.move_to(UP * 3.15)
        self.play(Write(title), run_time=0.6)

        sub1 = fit(Text("Pick one AI system you", color=PALETTE["ink"], font_size=19), 3.5)
        sub2 = fit(Text("used this week.", color=PALETTE["ink"], font_size=19), 3.5)
        subgroup = VGroup(sub1, sub2).arrange(DOWN, buff=0.1)
        subgroup.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subgroup), run_time=0.5)
        self.wait(0.3)

        questions = [
            "What's it used for?",
            "What happens if\nit's wrong?",
            "How confident is the\nclaim, really?",
        ]
        y = 1.15
        for q in questions:
            box = Square(side_length=0.3, color=PALETTE["slate"], stroke_width=2.2,
                         fill_color=PALETTE["bg"], fill_opacity=1.0)
            label = fit(Text(q, color=PALETTE["ink"], font_size=19, line_spacing=0.9), 2.6)
            box.move_to(LEFT * 1.5 + UP * y)
            label.next_to(box, RIGHT, buff=0.3)
            self.play(Create(box), Write(label), run_time=0.6)
            self.wait(0.2)
            y -= 1.15
        self.wait(0.3)

        verdict_line1 = fit(Text(
            "Low-stakes on all three? Let it go.", color=PALETTE["crimson"], font_size=18
        ), 3.6)
        verdict_line2 = fit(Text(
            "High-stakes on any? Scrutinize it.", color=PALETTE["crimson"], font_size=18
        ), 3.6)
        verdict = VGroup(verdict_line1, verdict_line2).arrange(DOWN, buff=0.12)
        verdict.move_to(DOWN * 3.0)
        self.play(Write(verdict), run_time=0.9)
        # tuned close to actual_duration_s (17.30s, reused unchanged).
        self.wait(12.3)


# --------------------------------------------------------------------------- #
# B11 — SIGN-OFF: same brand card as the parent (already a centered
# vertical stack — no structural change needed), just narrowed. Its
# narration was REWRITTEN by shorts.py (B09 was dropped, so this outro
# now tells viewers what's missing and points them at the long) — new
# measured duration is 11.95s vs. the parent's 4.92s, so self.wait() is
# re-tuned to that new length instead of copied from the parent.
# --------------------------------------------------------------------------- #
class B11_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(Text("@HumanitariansAI", color=PALETTE["slate"], font_size=36), 3.6)
        accent = Line(LEFT * 1.9, RIGHT * 1.9, color=PALETTE["gold"], stroke_width=3.5)
        tagline = fit(Text("In for Sai Pranavi J.", color=PALETTE["ink"], font_size=22), 3.6)
        # buff bumped 0.4 -> 1.9 (first pass at 1.7 measured 54%, just
        # under the 55% floor — one more small bump for margin), accent
        # widened 2.4 -> 3.8: GATE V measured this card at only 16% canvas
        # fill originally (this beat has the least "content" of any kept
        # beat, and its rewritten outro narration now holds this card for
        # 11.95s — plenty of screen time to spend on generous spacing
        # rather than a tiny cluster of text).
        VGroup(handle, accent, tagline).arrange(DOWN, buff=1.9).move_to(ORIGIN)

        tagline_underline = Line(color=PALETTE["sage"], stroke_width=1)

        self.play(FadeIn(handle, shift=UP * 0.2), run_time=0.6)
        self.play(Create(accent), run_time=0.4)
        self.play(FadeIn(tagline), run_time=0.5)
        tagline_underline.put_start_and_end_on(
            tagline.get_corner(DL) + DOWN * 0.12, tagline.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(tagline_underline), run_time=0.3)
        # re-tuned to the REWRITTEN outro's measured duration (11.95s, not
        # the parent's 4.92s) — see the class docstring above.
        self.wait(10.15)
