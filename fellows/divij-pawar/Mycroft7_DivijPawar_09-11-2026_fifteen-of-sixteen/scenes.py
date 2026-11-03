"""scenes.py — Manim scenes for fifteen-of-sixteen (claude-divij, Cross-Agent Validation video 5).

Palette: cream #FAF9F5, ink #3D3929, terracotta #D97757, soft #73705F, ghost #A9A491,
plus three verdict colors carried over from the series' Chapter-3/4 scorecard
convention: green #4C9A6A (worked / resolved), amber #C9932E (a real but informative
gap), red #B0473A (a real, unresolved flaw). Type: Montserrat (DISPLAY, structural
default) / EB Garamond (SERIF, editorial voice only) / PT Mono (MONO, data+code
only) — see graphics_lib.py. Boxes are sized to their actual content via auto_box,
never hand-measured.

Every scene ends with hold_to(self, TARGET) so its NATIVE duration matches the
beat's target length — compile.py then never has to stretch a short clip into
visible slow motion. TARGET constants below are the PRE-AUDIO estimated_duration_s
from beat_sheet.json — RETIME against actual Kokoro output per BUILD-PROMPT.md
Step 3 before final render. Nothing in this file has been rendered yet.

Safe frame: x in [-6.4, 6.4], y in [-3.6, 3.6].

Never a raw Text("✓")/Text("✕")/Text("⚠") — Montserrat AND Manim's own default font
have no glyph for some of these on this machine (confirmed the hard way building
zero-for-sixteen/scenes.py: ⚠ silently rendered as its raw hex codepoint). Use
checked() from graphics_lib for ✓/✕ (confirmed working), and a drawn Triangle()+"!"
for any warning glyph rather than a raw emoji Text().

B00 (cold open + title, Remotion ClaudeComposerAsk) and B17 (outro, Remotion
ClaudeTitleOutro) are not Manim scenes — see beat_sheet.json. B01 through B16 below
are the 16 GRAPHIC beats, one class each, named to match beat_sheet.json's
shot.manim.scene_class exactly.
"""
from graphics_lib import *

BG = "#FAF9F5"
INK = "#3D3929"
ACC = "#D97757"
SOFT = "#73705F"
GHOST = "#A9A491"

GREEN = "#4C9A6A"
AMBER = "#C9932E"
RED = "#B0473A"


def hold_to(scene, target, minimum=0.4):
    """Pad the scene out to `target` seconds of native runtime."""
    try:
        elapsed = float(scene.renderer.time)
    except Exception:
        scene.wait(minimum)
        return
    scene.wait(max(minimum, target - elapsed))


def boxed(inner, color=INK, h_pad=0.45, v_pad=0.32, **kw):
    """content -> VGroup(box, content), box sized to the content."""
    b = auto_box(inner, h_pad=h_pad, v_pad=v_pad, color=color, **kw)
    return VGroup(b, inner)


def muted_chip(text, size=24):
    return label_chip(text, SOFT, size=size)


def num_chip(text, color=INK, size=26):
    t = mono(text, size=size, color=color)
    b = auto_box(t, h_pad=0.22, v_pad=0.16, color=color)
    return VGroup(b, t)


def warn_icon(scale=0.22):
    """A drawn triangle + '!' — never a raw ⚠ Text() glyph, which silently
    fails to render on this machine (see module docstring)."""
    tri = Triangle(color=AMBER, fill_color=AMBER, fill_opacity=1,
                    stroke_width=0).scale(scale)
    bang = label("!", size=int(scale * 90), weight="BOLD", color=BG).move_to(
        tri.get_center() + DOWN * (scale * 0.14))
    return VGroup(tri, bang)


def fit_w(group, max_width=11.5, max_scale=1.0):
    if group.width > max_width:
        group.scale(min(max_scale, max_width / group.width))
    return group


# ─────────────────────────────────────────────────────────────────────────────
#  B01_OpenThreads   (target ~36s)   Figure 3
#  Two paths branching from last week's closing card.
# ─────────────────────────────────────────────────────────────────────────────
class B01_OpenThreads(Scene):
    TARGET = 27.84  # retimed to actual Kokoro duration (was 28.05)

    def construct(self):
        self.camera.background_color = BG

        head = label("WHAT LAST WEEK LEFT UNRESOLVED", size=27, weight="BOLD",
                    color=SOFT).move_to([0, 3.2, 0])
        self.play(FadeIn(head), run_time=0.4)

        recap = label_chip("16 / 31 FALSE POSITIVES -- 0 REAL CONFLICTS", ACC, size=22)
        recap.move_to([0, 2.2, 0])
        self.play(FadeIn(recap), run_time=0.5)
        self.wait(1.2)

        last_week = boxed(label("LAST WEEK", size=22, weight="BOLD", color=INK),
                         color=SOFT).move_to([0, 0.8, 0])
        self.play(FadeIn(last_week), run_time=0.5)
        self.wait(0.6)

        left = boxed(label("LINK\nCONCEPTS", size=22, weight="BOLD", color=INK,
                           line_spacing=0.8), color=ACC).move_to([-2.6, -1.2, 0])
        right = boxed(label("TEST\nOVERLAP", size=22, weight="BOLD", color=INK,
                            line_spacing=0.8), color=ACC).move_to([2.6, -1.2, 0])
        lineL = Line(last_week.get_bottom(), left.get_top(), color=SOFT, stroke_width=2)
        lineR = Line(last_week.get_bottom(), right.get_top(), color=SOFT, stroke_width=2)
        self.play(Create(lineL), Create(lineR), run_time=0.5)
        self.play(FadeIn(left), FadeIn(right), run_time=0.6)
        self.wait(1.4)

        cap = label("one day, both threads, in that order", size=22, weight="BOLD",
                   color=INK).move_to([0, -3.0, 0])
        self.play(FadeIn(cap), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_NumberTagging   (target ~32s)   Figure 4
#  A conclusion sentence with numbers getting colored concept tags.
# ─────────────────────────────────────────────────────────────────────────────
class B02_NumberTagging(Scene):
    TARGET = 25.77  # retimed to actual Kokoro duration (was 25.88)

    def construct(self):
        self.camera.background_color = BG

        head = label("TAG THE NUMBER, NOT JUST THE DIGITS", size=26, weight="BOLD",
                    color=SOFT).move_to([0, 3.2, 0])
        self.play(FadeIn(head), run_time=0.4)

        sentence = label("\"Assets of $383.266 billion, revenue of $391.0 billion,\ndebt-to-equity near 0.34.\"",
                        size=24, color=INK, line_spacing=0.85)
        sentence.move_to([0, 1.6, 0])
        self.play(FadeIn(sentence), run_time=0.6)
        self.wait(1.2)

        tagA = label_chip("ASSETS", GREEN, size=16).move_to([-3.6, 0.5, 0])
        tagB = label_chip("REVENUE", GREEN, size=16).move_to([-0.3, 0.5, 0])
        tagC = label_chip("UNTAGGED", GHOST, size=16).move_to([3.4, 0.5, 0])
        self.play(FadeIn(tagA), run_time=0.35)
        self.play(FadeIn(tagB), run_time=0.35)
        self.wait(0.5)
        self.play(FadeIn(tagC), run_time=0.4)
        self.wait(1.4)

        chip = label_chip("TAGGED NUMBERS -- EXCLUDED FROM\nCOMPARISON ENTIRELY", ACC, size=24)
        chip.move_to([0, -1.4, 0])
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(1.6)

        cap = label("only the untagged ones still get\ncompared the old way", size=20,
                   color=SOFT, line_spacing=0.75).move_to([0, -2.7, 0])
        self.play(FadeIn(cap), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B03_ThreeBugs   (target ~40s)   Figure 5
#  Three bug cards, each struck through FIXED.
# ─────────────────────────────────────────────────────────────────────────────
class B03_ThreeBugs(Scene):
    TARGET = 33.05  # retimed to actual Kokoro duration (was 32.66)

    def construct(self):
        self.camera.background_color = BG

        head = label("THREE BUGS, CAUGHT BEFORE TRUST", size=27, weight="BOLD",
                    color=SOFT).move_to([0, 3.2, 0])
        self.play(FadeIn(head), run_time=0.4)

        bugs = [
            "decimal point mistaken\nfor end of sentence",
            "tagger missed the raw echo:\nEarningsPerShareDiluted",
            "distance measured from\nlabel start, not end",
        ]
        cards = VGroup()
        for i, t in enumerate(bugs):
            inner = label(t, size=24, color=INK, line_spacing=0.8)
            card = boxed(inner, color=GHOST, h_pad=0.6, v_pad=0.4)
            cards.add(card)
        cards.arrange(DOWN, buff=0.4)
        cards.move_to([0, -0.35, 0])
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.08) for c in cards],
                              lag_ratio=0.35), run_time=1.8)
        self.wait(1.4)

        strikes = VGroup()
        stamps = VGroup()
        for c in cards:
            s = Line(c.get_corner(DL), c.get_corner(UR), color=RED, stroke_width=3)
            strikes.add(s)
        self.play(LaggedStart(*[Create(s) for s in strikes], lag_ratio=0.3), run_time=1.0)
        self.wait(0.6)

        for c in cards:
            st = label_chip("FIXED", GREEN, size=20)
            st.next_to(c, RIGHT, buff=0.3)
            stamps.add(st)
        self.play(LaggedStart(*[FadeIn(s, scale=1.1) for s in stamps], lag_ratio=0.3),
                  run_time=0.9)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_ReplayThroughGate   (target ~17s)   Figure 6
#  The sixteen labeled record tiles filing through a concept_aware gate.
# ─────────────────────────────────────────────────────────────────────────────
class B04_ReplayThroughGate(Scene):
    TARGET = 12.97  # retimed to actual Kokoro duration (was 13.33)

    def construct(self):
        self.camera.background_color = BG

        chip = label_chip("NOT A NEW EXAMPLE -- THE SAME 16 REAL RUNS", ACC, size=20)
        chip.move_to([0, 3.1, 0])
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(0.8)

        tiles = VGroup(*[Rectangle(width=0.5, height=0.34, color=GHOST, stroke_width=1.6,
                                   fill_opacity=0.15, fill_color=GHOST) for _ in range(16)])
        tiles.arrange(RIGHT, buff=0.12).move_to([0, 1.4, 0])
        self.play(LaggedStart(*[FadeIn(t) for t in tiles], lag_ratio=0.05), run_time=0.9)
        self.wait(0.5)

        gate = boxed(mono("concept_aware", size=20, color=INK), color=INK,
                    h_pad=0.35, v_pad=0.22).move_to([0, 0.0, 0])
        self.play(FadeIn(gate), run_time=0.5)
        self.wait(0.4)

        self.play(*[t.animate.move_to(gate.get_bottom() + DOWN * 0.6).scale(0.4)
                    for t in tiles], run_time=1.4)
        self.wait(0.8)

        cap = label("replay all sixteen, count what's left", size=22, weight="BOLD",
                   color=INK).move_to([0, -2.4, 0])
        self.play(FadeIn(cap), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B05_CheckedTwice   (target ~27s)   Figure 7
#  Two check panels landing on the same number.
# ─────────────────────────────────────────────────────────────────────────────
class B05_CheckedTwice(Scene):
    TARGET = 19.8  # retimed to actual Kokoro duration (was 20.48)

    def construct(self):
        self.camera.background_color = BG

        stop = label("15 STOP FLAGGING", size=37, weight="BOLD", color=GREEN)
        stop.move_to([0, 2.75, 0])
        self.play(FadeIn(stop), run_time=0.5)
        self.wait(1.0)

        still = label_chip("THE SIXTEENTH DOESN'T --\nREALLY FABRICATED, SUPPOSED TO STILL FLAG",
                          RED, size=18)
        still.move_to([0, 1.45, 0])
        self.play(FadeIn(still), run_time=0.5)
        self.wait(1.2)

        panelA = boxed(mono("MODULE, DIRECT:\n15/16", size=23, color=INK, line_spacing=0.8),
                      color=SOFT).move_to([-2.95, -0.65, 0])
        panelB = boxed(mono("PRODUCTION API:\n15/16", size=23, color=INK, line_spacing=0.8),
                      color=SOFT).move_to([2.95, -0.65, 0])
        self.play(FadeIn(panelA), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(panelB), run_time=0.5)
        self.wait(0.8)

        line = Line(panelA.get_right(), panelB.get_left(), color=GREEN, stroke_width=2.5)
        self.play(Create(line), run_time=0.5)
        self.wait(1.0)

        cap = label("checked twice, not once", size=22, color=SOFT).move_to([0, -2.85, 0])
        self.play(FadeIn(cap), run_time=0.4)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B06_TruePositivePreserved   (target ~11s)   Figure 8
#  Chapter 2 closer — deliberately the shortest beat, recaps not introduces.
# ─────────────────────────────────────────────────────────────────────────────
class B06_TruePositivePreserved(Scene):
    TARGET = 10.6  # retimed to actual Kokoro duration (was 10.13)

    def construct(self):
        self.camera.background_color = BG

        killed = label("15 KILLED", size=66, weight="BOLD", color=ACC)
        one = label("1", size=66, weight="BOLD", color=INK)
        card = VGroup(killed, one).arrange(RIGHT, buff=5.4).move_to([0, 2.35, 0])
        self.play(FadeIn(card), run_time=0.5)
        self.wait(0.6)

        stamp = label_chip("TRUE POSITIVE, PRESERVED", GREEN, size=34)
        stamp.move_to([0, 0.1, 0])
        self.play(FadeIn(stamp, scale=1.05), run_time=0.5)
        self.wait(0.8)

        cap = label("the one confirmed real catch on record", size=30,
                   color=SOFT).move_to([0, -2.85, 0])
        self.play(FadeIn(cap), run_time=0.4)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B07_SharedContextFork   (target ~28s)   Figure 9
#  One shared context block forking into two model icons.
# ─────────────────────────────────────────────────────────────────────────────
class B07_SharedContextFork(Scene):
    TARGET = 20.16  # retimed to actual Kokoro duration (was 20.93)

    def construct(self):
        self.camera.background_color = BG

        chip = label_chip("SAME DATA. TWO MODELS.", ACC, size=24)
        chip.move_to([0, 3.1, 0])
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(0.8)

        ctx = boxed(mono("shared context: real SEC data", size=18, color=INK),
                   color=INK).move_to([0, 1.6, 0])
        self.play(FadeIn(ctx), run_time=0.5)
        self.wait(0.6)

        modelA = boxed(mono("qwen2.5:7b", size=22, color=INK), color=SOFT).move_to([-3.4, 0.0, 0])
        modelB = boxed(mono("mistral-7b", size=22, color=INK), color=SOFT).move_to([3.4, 0.0, 0])
        lineA = Line(ctx.get_bottom(), modelA.get_top(), color=SOFT, stroke_width=2)
        lineB = Line(ctx.get_bottom(), modelB.get_top(), color=SOFT, stroke_width=2)
        self.play(Create(lineA), Create(lineB), run_time=0.5)
        self.play(FadeIn(modelA), FadeIn(modelB), run_time=0.6)
        self.wait(1.0)

        runs = VGroup(*[
            mono(t, size=16, color=SOFT) for t in
            ("AAPL", "AAPL (swapped)", "MSFT", "NVDA")
        ]).arrange(RIGHT, buff=0.4).move_to([0, -1.6, 0])
        self.play(LaggedStart(*[FadeIn(r) for r in runs], lag_ratio=0.2), run_time=1.0)
        self.wait(1.0)

        cap = label("a role effect, ruled out", size=20, color=INK,
                   weight="BOLD").move_to([0, -2.7, 0])
        self.play(FadeIn(cap), run_time=0.4)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B08_ZeroRealNumbers   (target ~24s)   Figure 10 (+ B00's deferred figure 2)
#  Real vs fabricated context, red 0 REAL NUMBERS CITED stamp.
# ─────────────────────────────────────────────────────────────────────────────
class B08_ZeroRealNumbers(Scene):
    TARGET = 17.62  # retimed to actual Kokoro duration (was 17.19)

    def construct(self):
        self.camera.background_color = BG

        head = label("4 FOR 4, FLAGGED", size=34, weight="BOLD", color=INK)
        head.move_to([0, 3.0, 0])
        self.play(FadeIn(head), run_time=0.5)
        self.wait(0.6)

        cap1 = label("first time on evidence both sides actually saw", size=18,
                   color=SOFT).move_to([0, 2.1, 0])
        self.play(FadeIn(cap1), run_time=0.4)
        self.wait(1.0)

        real = VGroup(
            label("REAL CONTEXT", size=16, weight="BOLD", color=SOFT),
            mono("Assets: 383266000000.0", size=16, color=INK),
        ).arrange(DOWN, buff=0.15)
        realbox = boxed(real, color=GREEN)

        # Real output, not invented placeholder text -- queried directly from
        # web/data/accountability.db (run 09cc72b6, MSFT, 2026-09-11T17:42:37Z),
        # the same run RUN_LOG.md describes narratively as "invented an
        # unrelated historical fiscal quarter and a fabricated source URL"
        # without quoting the exact string. EXECUTABLE-EVIDENCE (CLAUDE.md
        # SS4): the real text was one query away and should be shown, not
        # stood in for.
        fake_q = mono("\"Q2 FY 2021\" -- doesn't exist", size=15, color=RED)
        fake_url = mono("https://www.sec.gov/", size=14, color=GHOST)
        fake_strike = Line(fake_url.get_left(), fake_url.get_right(), color=RED, stroke_width=2)
        fake = VGroup(
            label("FABRICATED", size=16, weight="BOLD", color=SOFT),
            fake_q, VGroup(fake_url, fake_strike),
        ).arrange(DOWN, buff=0.15)
        fakebox = boxed(fake, color=RED)

        # arrange(RIGHT, buff=...), not hand-guessed x-coordinates — a
        # fixed-coordinate first pass here left the two boxes overlapping
        # (each box's actual content width, especially the mono figures,
        # was wider than assumed), caught in visual QC. arrange() guarantees
        # clearance regardless of exact text width.
        pair = VGroup(realbox, fakebox).arrange(RIGHT, buff=0.5).move_to([0, 0.2, 0])

        self.play(FadeIn(realbox), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(fakebox), run_time=0.5)
        self.wait(1.2)

        stamp = label_chip("0 REAL NUMBERS CITED", RED, size=22)
        stamp.move_to([0, -2.2, 0])
        self.play(FadeIn(stamp, scale=1.1), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B09_SignAndMagnitude   (target ~24s)   Figure 11
#  Real $101B income vs the mislabeled "-$101M loss".
# ─────────────────────────────────────────────────────────────────────────────
class B09_SignAndMagnitude(Scene):
    TARGET = 16.79  # retimed to actual Kokoro duration (was 16.9)

    def construct(self):
        self.camera.background_color = BG

        chip = label_chip("ROLES SWAPPED -- NOT A SEAT EFFECT", ACC, size=28)
        chip.move_to([0, 3.1, 0])
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(1.0)

        real = mono("$101,464,000,000\nnet income", size=24, color=GREEN, line_spacing=0.8)
        real.move_to([0, 1.5, 0])
        self.play(FadeIn(real), run_time=0.6)
        self.wait(1.2)

        arrow = Arrow([0, 0.7, 0], [0, -0.2, 0], color=RED, stroke_width=3)
        self.play(Create(arrow), run_time=0.5)

        wrong = mono("\"-$101,000,000\nnet income loss\"", size=24, color=RED, line_spacing=0.8)
        wrong.move_to([0, -1.2, 0])
        self.play(FadeIn(wrong), run_time=0.6)
        self.wait(1.4)

        stamp = label_chip("WRONG SIGN. WRONG BY 1000x.", RED, size=27)
        stamp.move_to([0, -2.7, 0])
        self.play(FadeIn(stamp, scale=1.05), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B10_ModelScoreboard   (target ~19s)   Figure 12
#  Split scoreboard: 4/4+1 unsupported vs 0/4 grounded.
# ─────────────────────────────────────────────────────────────────────────────
class B10_ModelScoreboard(Scene):
    TARGET = 13.85  # retimed to actual Kokoro duration (was 13.97)

    def construct(self):
        self.camera.background_color = BG

        rowA = VGroup(
            label("MODEL A", size=22, weight="BOLD", color=SOFT),
            label("4/4 correct, +1 unsupported ROE", size=22, color=INK),
        ).arrange(RIGHT, buff=0.9)
        rowB = VGroup(
            label("MODEL B", size=22, weight="BOLD", color=SOFT),
            label("0/4 grounded", size=22, color=RED),
        ).arrange(RIGHT, buff=0.9)
        board = VGroup(rowA, rowB).arrange(DOWN, buff=0.6).move_to([0, 2.55, 0])
        self.play(FadeIn(rowA), run_time=0.5)
        self.wait(0.6)
        self.play(FadeIn(rowB), run_time=0.5)
        self.wait(1.2)

        cap1 = label("the mechanism works. it found a real problem.", size=27,
                   weight="BOLD", color=INK).move_to([0, -0.5, 0])
        self.play(FadeIn(cap1), run_time=0.5)
        self.wait(1.0)
        cap2 = label("just not the one it was built to find", size=27,
                   weight="BOLD", color=SOFT).move_to([0, -2.9, 0])
        self.play(FadeIn(cap2), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B11_RouteRewire   (target ~14s)   Figure 13
#  /api/compare route diagram, old rule struck, new rule wired in.
# ─────────────────────────────────────────────────────────────────────────────
class B11_RouteRewire(Scene):
    TARGET = 11.09  # retimed to actual Kokoro duration (was 11.09)

    def construct(self):
        self.camera.background_color = BG

        head = label("WIRING THE FIX IN -- SAME DAY", size=38, weight="BOLD",
                    color=SOFT).move_to([0, 3.15, 0])
        self.play(FadeIn(head), run_time=0.4)

        route = boxed(mono("/api/compare", size=30, color=INK), color=INK).move_to([0, 1.5, 0])
        self.play(FadeIn(route), run_time=0.5)
        self.wait(0.6)

        old = mono("old rule", size=24, color=SOFT).move_to([0, -0.1, 0])
        strike = Line(old.get_left(), old.get_right(), color=RED, stroke_width=3)
        self.play(FadeIn(old), run_time=0.4)
        self.play(Create(strike), run_time=0.4)
        self.wait(0.6)

        new = label_chip("concept_aware -- DEFAULT NOW", GREEN, size=32)
        new.move_to([0, -2.85, 0])
        self.play(FadeIn(new, scale=1.05), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B12_RegexFix   (target ~45s)   Figure 14 + the old-gate quiet-failure fix
# ─────────────────────────────────────────────────────────────────────────────
class B12_RegexFix(Scene):
    TARGET = 35.63  # retimed to actual Kokoro duration (was 36.63)

    def construct(self):
        self.camera.background_color = BG

        chip1 = label_chip("FIX #1 -- THE OLD GATE'S QUIET FAILURE", ACC, size=20)
        chip1.move_to([0, 3.1, 0])
        self.play(FadeIn(chip1), run_time=0.5)
        self.wait(0.8)

        cap1 = label("required both sides non-empty --\nsuppressed the true positive", size=19,
                   color=INK, line_spacing=0.75).move_to([0, 1.9, 0])
        self.play(FadeIn(cap1), run_time=0.5)
        self.wait(1.2)

        stamp1 = label_chip("NEW RULE: NO SUCH GATE", GREEN, size=20)
        stamp1.move_to([0, 0.8, 0])
        self.play(FadeIn(stamp1), run_time=0.5)
        self.wait(1.4)

        self.play(FadeOut(VGroup(chip1, cap1, stamp1)), run_time=0.5)

        chip2 = label_chip("FIX #2 -- A REAL EXTRACTION BUG", ACC, size=32)
        chip2.move_to([0, 3.15, 0])
        self.play(FadeIn(chip2), run_time=0.5)
        self.wait(0.8)

        big = mono("13,971,000,000.0", size=40, color=INK).move_to([0, 0.9, 0])
        self.play(FadeIn(big), run_time=0.5)
        self.wait(1.0)

        discard = mono("13,971,000,", size=40, color=INK).move_to(big, aligned_edge=LEFT)
        keep = mono("000.0", size=40, color=RED)
        keep.next_to(discard, RIGHT, buff=0.0)
        self.remove(big)
        self.add(discard, keep)
        self.play(discard.animate.set_opacity(0.2), run_time=0.8)
        self.wait(1.0)

        self.play(FadeOut(VGroup(discard, keep)), run_time=0.4)
        fixed = mono("13,971,000,000.0", size=40, color=GREEN).move_to([0, 0.9, 0])
        self.play(FadeIn(fixed), run_time=0.5)
        self.wait(1.2)

        cap2 = label("confirmed against the real historical case", size=32,
                   color=SOFT).move_to([0, -2.9, 0])
        self.play(FadeIn(cap2), run_time=0.4)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B13_VerificationRateZero   (target ~31s)   Figure 15
#  The real thought log, citation highlighted, VERIFICATION RATE: 0.0 stamp.
# ─────────────────────────────────────────────────────────────────────────────
class B13_VerificationRateZero(Scene):
    TARGET = 24.81  # retimed to actual Kokoro duration (was 23.03)

    def construct(self):
        self.camera.background_color = BG

        head = label("CLAIM VERIFICATION, WIRED IN\nFOR THE FIRST TIME", size=35, weight="BOLD",
                    color=SOFT, line_spacing=0.8).move_to([0, 2.9, 0])
        self.play(FadeIn(head), run_time=0.5)
        self.wait(0.8)

        quote = serif("\"Calculated the debt-to-equity\nratio as 0.34\"", size=34,
                    color=INK, italic=True, line_spacing=0.8)
        src = mono("[SOURCE: SEC Filings]", size=24, color=ACC)
        group = VGroup(quote, src).arrange(DOWN, buff=0.28).move_to([0, 0.9, 0])
        self.play(FadeIn(group), run_time=0.6)
        self.wait(1.4)

        stamp = label_chip("VERIFICATION RATE: 0.0", RED, size=37)
        stamp.next_to(group, DOWN, buff=0.6)
        self.play(FadeIn(stamp, scale=1.05), run_time=0.5)
        self.wait(1.4)

        chip = label_chip("A REAL SIGNAL, NOT A GUESS", ACC, size=36)
        chip.move_to([0, -2.9, 0])
        self.play(FadeIn(chip), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B14_TrueNowList   (target ~44s)
#  Chapter 5, first half — the script's own direction: "List one, building
#  line by line."
# ─────────────────────────────────────────────────────────────────────────────
class B14_TrueNowList(Scene):
    TARGET = 34.37  # retimed to actual Kokoro duration (was 34.71)

    def construct(self):
        self.camera.background_color = BG

        head = label("TRUE NOW THAT WASN'T", size=28, weight="BOLD",
                    color=SOFT).move_to([0, 3.2, 0])
        self.play(FadeIn(head), run_time=0.5)
        self.wait(0.6)

        items = [
            "fifteen of sixteen false positives gone -- measured on all sixteen, not four",
            "the suppressed true positive fires again",
            "comma-formatted numbers extract correctly",
            "claim verification runs on this route for the first time",
            "four ledger issues closed in one day",
            "242 tests, up from 224, green at every step",
        ]
        lines = VGroup(*[
            checked(t, size=19, color=INK) for t in items
        ]).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        fit_w(lines, max_width=11.5)
        lines.move_to([0, 0.2, 0])

        for ln in lines:
            self.play(FadeIn(ln, shift=RIGHT * 0.08), run_time=0.35)
            self.wait(0.25)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B15_StillNotTrueAndUncommitted   (target ~57s)   Figure 16
#  Chapter 5, second half — the script's own direction: "List two, in
#  warning color, held on screen. Do not clear it." The reel's longest,
#  most protected beat by design — never trim this per the script's own
#  production notes.
# ─────────────────────────────────────────────────────────────────────────────
class B15_StillNotTrueAndUncommitted(Scene):
    TARGET = 43.69  # retimed to actual Kokoro duration (was 43.16)

    def construct(self):
        self.camera.background_color = BG

        head = label("STILL NOT TRUE", size=28, weight="BOLD",
                    color=RED).move_to([0, 3.25, 0])
        self.play(FadeIn(head), run_time=0.5)
        self.wait(0.4)

        items = [
            "a real ratio and a fabricated one still look identical",
            "narrowed the gap, did not close it",
            "one local model's grounding failure -- flagged, not fixed",
            "comparison route: 3 tests. every other route, all interface code: 0",
            "4 critical security findings -- exactly as open as before",
        ]
        lines = VGroup(*[label(t, size=17, color=INK) for t in items])
        lines.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        fit_w(lines, max_width=11.0)
        lines.move_to([0, 1.5, 0])

        for ln in lines:
            self.play(FadeIn(ln, shift=RIGHT * 0.06), run_time=0.3)
            self.wait(0.2)
        self.wait(0.6)

        # the list holds, uncleared, while the uncommitted-state reveal builds beneath it
        git_panel = boxed(mono("c53746a", size=22, color=INK), color=SOFT,
                         h_pad=0.35, v_pad=0.22).move_to([-2.4, -2.0, 0])
        git_lbl = label("last commit -- unchanged", size=14, color=SOFT).next_to(
            git_panel, UP, buff=0.1)
        self.play(FadeIn(git_panel), FadeIn(git_lbl), run_time=0.5)
        self.wait(0.8)

        counter = label_chip("+11 MORE FILES", RED, size=22).move_to([2.4, -1.9, 0])
        self.play(FadeIn(counter, scale=1.1), run_time=0.6)
        self.wait(1.2)

        cap = label("the pile outside version control\ngot bigger again", size=18,
                   weight="BOLD", color=INK, line_spacing=0.7).move_to([0, -3.15, 0])
        self.play(FadeIn(cap), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B16_FifteenKilledReprise   (target ~41s)   Figure 1 reprise + END CARD
#  Second-to-last beat, OUTRO-LAW: dense factual callouts land here, never
#  on the truly final Remotion outro (B17).
# ─────────────────────────────────────────────────────────────────────────────
class B16_FifteenKilledReprise(Scene):
    TARGET = 32.68  # retimed to actual Kokoro duration (was 31.49)

    def construct(self):
        self.camera.background_color = BG

        closer = serif("the smallest true claim", size=28,
                      color=INK).move_to([0, 3.1, 0])
        self.play(FadeIn(closer), run_time=0.5)
        self.wait(1.0)

        killed = label("15 KILLED", size=36, weight="BOLD", color=ACC)
        one = label("1 TRUE POSITIVE", size=28, weight="BOLD", color=INK)
        card = VGroup(killed, one).arrange(DOWN, buff=0.2).move_to([0, 1.4, 0])
        self.play(FadeIn(card), run_time=0.6)
        self.wait(1.2)

        cap = label("better at not crying wolf.\nnot better at spotting a convincing fake.",
                   size=18, color=SOFT, line_spacing=0.75).move_to([0, -0.2, 0])
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(VGroup(closer, card, cap)), run_time=0.5)

        bullets = [
            ("15 of 16 false positives killed -- the 1 remaining is the confirmed true positive", INK),
            ("a real number and a fabricated one still look alike, untagged", INK),
            ("1 of 2 tested local models did not ground its answers, in 3 of 4 live runs", INK),
            ("claim verification now runs on the comparison route", INK),
            ("/api/compare has 3 tests now; every other route and all interface code: 0", INK),
            ("4 critical security findings remain exactly as open as before", INK),
            ("nothing described here is committed (same commit as last video, +11 files)", RED),
        ]
        lines = VGroup(*[mono(t, size=14, color=c) for t, c in bullets])
        lines.arrange(DOWN, buff=0.92, aligned_edge=LEFT)
        fit_w(lines, max_width=11.5)
        lines.move_to([0, 0.1, 0])

        for ln in lines:
            self.play(FadeIn(ln, shift=RIGHT * 0.05), run_time=0.3)
            self.wait(0.15)
        hold_to(self, self.TARGET)
