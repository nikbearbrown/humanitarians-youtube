"""short/scenes.py — 9:16 portrait re-layout of the three GRAPHIC beats kept
in the Short (B12, B13, B14). B00 and B15 are Remotion (ClaudeComposerAsk916,
ClaudeTitleOutro916) and are not Manim scenes.

Portrait rendering (manim -r 1080,1920) keeps frame_height at 8 units but
shrinks frame_width to ~4.5 (half-width ~2.25) — every horizontal
arrangement in the parent reel's scenes.py assumed the 16:9 frame_width
(~14.2) and would clip off-frame here. Every beat below is restacked
vertically instead, never a center-cut of the 16:9 version, per shorts.py's
"Manim GRAPHIC beats are re-laid-out for portrait" rule and the precedent
in ../../Mycroft5_DivijPawar_08-28-2026_the-number-that-wasnt-there/short/scenes.py
(same convention: BID_Name916, graphics_lib imported unchanged, frame_width
~4.5 assumed throughout).

Safe frame used throughout: x in [-2.0, 2.0], y in [-3.4, 3.4] (a slightly
tighter margin than the 16:9 parent's [-6.4,6.4]/[-3.6,3.6] — portrait's
narrow width leaves much less room for anything to drift before it bleeds
off the side edge). Vertical budget is nearly unchanged from the 16:9
parent (frame_height stays 8 units either way), so content that was
already vertically-stacked in the parent (B12, B13, B14 all were) mostly
needs re-wrapping long single lines into two lines, not a full re-design.

fit_v() is this file's version of the parent's fit_fields() — scales a
group down (never up) to guarantee it fits a vertical band, since portrait's
narrow width makes several of this reel's longer chip/line strings wrap to
more lines here than they did at 16:9, and a fixed guessed scale would
silently collide with whatever sits below it.
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
    try:
        elapsed = float(scene.renderer.time)
    except Exception:
        scene.wait(minimum)
        return
    scene.wait(max(minimum, target - elapsed))


def boxed(inner, color=INK, h_pad=0.3, v_pad=0.2, **kw):
    b = auto_box(inner, h_pad=h_pad, v_pad=v_pad, color=color, **kw)
    return VGroup(b, inner)


def fit_v(group, top, bottom, x=0, max_scale=1.0):
    """Scale `group` down (never up) so its height fits between `top` and
    `bottom`, then center it at that x in the middle of the band."""
    avail_h = top - bottom
    if group.height > 0:
        scale_factor = min(max_scale, (avail_h / group.height) * 0.96)
        if scale_factor < 1.0:
            group.scale(scale_factor)
    group.move_to([x, (top + bottom) / 2, 0])
    return group


def fit_w(group, max_width=3.9, max_scale=1.0):
    if group.width > max_width:
        group.scale(min(max_scale, max_width / group.width))
    return group


# ─────────────────────────────────────────────────────────────────────────────
#  B12_TrueNowList916   (target ~33s)
# ─────────────────────────────────────────────────────────────────────────────
class B12_TrueNowList916(Scene):
    TARGET = 33.26

    def construct(self):
        self.camera.background_color = BG

        head = label("TRUE NOW\nTHAT WASN'T", size=24, weight="BOLD",
                    color=SOFT, line_spacing=0.85).move_to([0, 3.1, 0])
        self.play(FadeIn(head), run_time=0.5)
        self.wait(0.5)

        items = [
            "interface calls the\ncomparison route",
            "one-fetch, two-lenses\ndesign rendered honestly",
            "retry path visible\noutside the test suite",
            "fabricated number findable\nwithout a raw log",
            "code sits in enforced\nlayers, enforcement can fail",
            "over-flagging is now a\nversioned corpus + 8 tests",
            "224 tests, up from 169,\ngreen at every step",
        ]
        lines = VGroup(*[
            checked(t, size=15, color=INK, line_spacing=0.72) for t in items
        ]).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        fit_w(lines, max_width=3.9)
        fit_v(lines, top=2.35, bottom=-3.3)

        for ln in lines:
            self.play(FadeIn(ln, shift=RIGHT * 0.06), run_time=0.3)
            self.wait(0.2)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B13_StillNotTrueAndUncommitted916   (target ~60s)
#  The reel's longest, densest beat — never trimmed for time, so it gets
#  the most careful fit-to-frame treatment here.
# ─────────────────────────────────────────────────────────────────────────────
class B13_StillNotTrueAndUncommitted916(Scene):
    TARGET = 60.39

    def construct(self):
        self.camera.background_color = BG

        head = label("STILL NOT\nTRUE", size=24, weight="BOLD", color=RED,
                    line_spacing=0.85).move_to([0, 3.1, 0])
        self.play(FadeIn(head), run_time=0.5)
        self.wait(0.4)

        items = [
            "zero tests — compare route,\ntrace module, all JS",
            "no UI work exercised\nagainst a real model",
            "retry/halt only proven\nagainst mock failures",
            "over-flagging not fixed",
            "suppressed true positive\nunresolved — needs a human call",
            "regex bug still corrupting\na real figure",
            "14 ledger entries, 12\nopen/unverified, 1 critical",
        ]
        lines = VGroup(*[
            label(t, size=12, color=INK, line_spacing=0.65) for t in items
        ]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        fit_w(lines, max_width=3.9)
        fit_v(lines, top=2.5, bottom=0.15)

        for ln in lines:
            self.play(FadeIn(ln, shift=RIGHT * 0.05), run_time=0.25)
            self.wait(0.15)
        self.wait(0.4)

        # The list holds, uncleared, while the uncommitted-state reveal
        # builds beneath it — stacked (not side-by-side, unlike the 16:9
        # parent) since portrait's ~4-unit width can't hold both at once.
        # Positioned with next_to() chains, not hand-guessed y-coordinates —
        # a fixed-coordinate first pass here left "CHANGED OR NEW FILES"
        # overlapping the closing caption (caught in visual QC); next_to()
        # guarantees clearance regardless of exact font-metric height.
        git_panel = boxed(mono("c53746a", size=15, color=INK), color=SOFT,
                         h_pad=0.22, v_pad=0.14)
        git_lbl = label("last commit", size=10, color=SOFT).next_to(
            git_panel, LEFT, buff=0.18)
        git_row = VGroup(git_lbl, git_panel).next_to(lines, DOWN, buff=0.3)
        self.play(FadeIn(git_row), run_time=0.5)
        self.wait(0.5)

        counter = mono("56", size=26, weight="BOLD", color=RED)
        counter_lbl = label("CHANGED OR NEW FILES", size=10, color=SOFT)
        counter_group = VGroup(counter, counter_lbl).arrange(
            DOWN, buff=0.06).next_to(git_row, DOWN, buff=0.3)
        self.play(FadeIn(counter_group, scale=1.05), run_time=0.5)
        self.wait(0.8)

        cap = label("named after the previous\nperiod's check — still true,\nand now bigger", size=12,
                   weight="BOLD", color=INK, line_spacing=0.65)
        cap.next_to(counter_group, DOWN, buff=0.3)
        self.play(FadeIn(cap), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B14_SixteenZeroReprise916   (target ~18s)   OUTRO-LAW second-to-last beat
# ─────────────────────────────────────────────────────────────────────────────
class B14_SixteenZeroReprise916(Scene):
    TARGET = 17.98

    def construct(self):
        self.camera.background_color = BG

        closer = serif("the smallest true claim\nI can make about this week",
                      size=18, color=INK, line_spacing=0.8).move_to([0, 3.0, 0])
        self.play(FadeIn(closer), run_time=0.5)
        self.wait(0.8)

        flagged = label("16 FLAGGED", size=30, weight="BOLD", color=ACC)
        conflicts = label("0 GENUINE\nCONFLICTS", size=22, weight="BOLD",
                         color=INK, line_spacing=0.8)
        counter = VGroup(flagged, conflicts).arrange(DOWN, buff=0.2).move_to([0, 1.3, 0])
        self.play(FadeIn(counter), run_time=0.6)
        self.wait(1.0)

        cursor_lbl = mono("tests/fixtures/\ncross_agent_real_runs_corpus.json",
                         size=10, color=SOFT, line_spacing=0.7).move_to([0, -0.2, 0])
        self.play(FadeIn(cursor_lbl), run_time=0.4)
        self.wait(0.6)

        self.play(FadeOut(VGroup(closer, counter, cursor_lbl)), run_time=0.4)

        bullets = [
            ("16 of 31 stored runs are\nfalse positives — 0 genuine", INK),
            ("the one confirmed true positive\nwould not flag today", INK),
            ("/api/compare + step_trace.py +\nall JS: zero automated tests", INK),
            ("no UI work this period has run\nagainst a live model", INK),
            ("12 of 14 ledger entries open\nor unverified — 1 critical", INK),
            ("nothing described here is\ncommitted (last commit c53746a)", RED),
            ("corpus labels are AI-assigned,\nnot yet human-reviewed", SOFT),
        ]
        lines = VGroup(*[
            mono(t, size=11, color=c, line_spacing=0.7) for t, c in bullets
        ]).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        fit_w(lines, max_width=3.9)
        fit_v(lines, top=3.3, bottom=-3.3)

        for ln in lines:
            self.play(FadeIn(ln, shift=RIGHT * 0.04), run_time=0.25)
            self.wait(0.12)
        hold_to(self, self.TARGET)
