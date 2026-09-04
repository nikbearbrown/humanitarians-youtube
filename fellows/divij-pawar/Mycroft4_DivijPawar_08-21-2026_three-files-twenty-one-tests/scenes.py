"""scenes.py — Manim scenes for three-files-twenty-one-tests (claude-divij, Video 2).

Palette: cream #FAF9F5, ink #3D3929, terracotta #D97757, soft #73705F, ghost #A9A491.
Type: Montserrat (DISPLAY, structural default) / EB Garamond (SERIF, editorial
voice only) / PT Mono (MONO, data+code only) — see graphics_lib.py. Boxes are
sized to their actual content via auto_box, never hand-measured.

Every scene ends with hold_to(self, TARGET) so its NATIVE duration matches the
beat's target length — compile.py then never has to stretch a short clip into
visible slow motion (tips.txt section 8). Re-tune the TARGET constants to
actual_duration_s after audio is generated.

Safe frame: x in [-6.4, 6.4], y in [-3.6, 3.6] (tips.txt section 7).
"""
import numpy as np
from graphics_lib import *

BG = "#FAF9F5"
INK = "#3D3929"
ACC = "#D97757"
SOFT = "#73705F"
GHOST = "#A9A491"

# EB Garamond renders word spaces too narrow to see at font_size <= 26 — verified
# by rendering the same string at 24/26/28/30/32/34/36: broken at 24 and 26,
# correct from 28 up. Montserrat and PT Mono are unaffected. It never errors and
# it is invisible at 480p, so it ships silently. graphics_lib's generic FLOOR=24
# is too low for this one font; shadow serif() here rather than editing the
# shared helper (tips.txt: copy graphics_lib.py reel-to-reel unchanged).
SERIF_FLOOR = 30
_serif = serif


def serif(text, size=34, **kw):  # noqa: F811 — deliberate shadow, see above
    return _serif(text, size=max(size, SERIF_FLOOR), **kw)


def muted_chip(text, size=24):
    """A de-emphasised chip. Never GHOST-filled — label_chip puts WHITE text on
    the fill, and white on #A9A491 is unreadable. SOFT is the muted floor."""
    return label_chip(text, SOFT, size=size)


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


def record_card(w=2.6, h=0.5, color=SOFT):
    """One timestamped record in the audit stack."""
    r = Rectangle(width=w, height=h, color=color, stroke_width=2,
                  fill_opacity=0.05, fill_color=color)
    tick = Line(r.get_left() + RIGHT * 0.22 + UP * 0.0,
                r.get_left() + RIGHT * 1.55, color=color, stroke_width=1.6)
    return VGroup(r, tick)


def num_chip(text, color=INK, size=26):
    t = mono(text, size=size, color=color)
    b = auto_box(t, h_pad=0.22, v_pad=0.16, color=color)
    return VGroup(b, t)


# ─────────────────────────────────────────────────────────────────────────────
#  B01_PerfectRecordUnknownTruth   (target ~21s)   EXECUTIVE-SUMMARY LAW
#  A perfect audit trail that proves nothing, and the empty slot beside it.
# ─────────────────────────────────────────────────────────────────────────────
class B01_PerfectRecordUnknownTruth(Scene):
    TARGET = 22.1  # actual_duration_s, Kokoro am_onyx

    def construct(self):
        self.camera.background_color = BG

        # ── the immaculate stack ─────────────────────────────────────────────
        stack = VGroup(*[record_card() for _ in range(6)])
        stack.arrange(DOWN, buff=0.22).move_to([-3.3, 0.55, 0])
        stack_lbl = label("THE ACCOUNTABILITY LAYER", size=26, color=INK)
        stack_lbl.next_to(stack, UP, buff=0.4)

        self.play(FadeIn(stack_lbl), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.15) for c in stack],
                              lag_ratio=0.22), run_time=1.9)
        self.wait(1.6)

        self.play(stack.animate.set_opacity(0.30),
                  stack_lbl.animate.set_color(GHOST), run_time=0.7)
        cap = label("PERFECT RECORD.\nUNKNOWN TRUTH.", size=28, weight="BOLD",
                    color=SOFT, line_spacing=0.7)
        cap.next_to(stack, DOWN, buff=0.42)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(2.4)

        # ── the empty slot beside it ─────────────────────────────────────────
        slot_inner = label("CROSS-AGENT\nVALIDATION", size=28, weight="BOLD",
                           color=GHOST, line_spacing=0.7)
        slot_inner.move_to([3.2, 1.0, 0])
        slot = DashedVMobject(
            auto_box(slot_inner, h_pad=0.75, v_pad=0.75, color=GHOST, stroke_width=3),
            num_dashes=42, color=GHOST)
        empty = label("declared · specified · empty", size=24, color=GHOST)
        empty.next_to(slot, DOWN, buff=0.32)

        self.play(Create(slot), FadeIn(slot_inner), run_time=0.8)
        self.play(FadeIn(empty), run_time=0.35)
        self.wait(2.0)

        fill = serif("compare two agents.\nrecord the gap. stop.", size=30,
                     color=ACC, line_spacing=0.75)
        fill.move_to(slot_inner)
        self.play(FadeOut(slot_inner), FadeIn(fill),
                  slot.animate.set_color(ACC), run_time=0.7)
        self.wait(1.8)

        # The row is ~8 units wide: centred on the slot's x=3.2 its right edge
        # lands at 7.2 and "SET ARITHMETIC" is clipped by the frame, while its
        # left end runs into the PERFECT RECORD caption. Centre it and drop it
        # clear of the caption instead.
        chips = VGroup(
            muted_chip("NO JUDGE"), muted_chip("NO MODEL"),
            label_chip("SET ARITHMETIC", ACC, size=24),
        ).arrange(RIGHT, buff=0.34)
        chips.move_to([0, -3.15, 0])
        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in chips],
                              lag_ratio=0.28), run_time=1.0)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_WhatAlreadyExisted   (target ~31s)
#  The four components that were already there, then the probe aimed at itself.
# ─────────────────────────────────────────────────────────────────────────────
class B02_WhatAlreadyExisted(Scene):
    TARGET = 34.73  # actual_duration_s, Kokoro am_onyx

    def construct(self):
        self.camera.background_color = BG

        head = label("ALREADY BUILT", size=28, weight="BOLD", color=SOFT)
        head.move_to([0, 3.3, 0])
        self.play(FadeIn(head), run_time=0.4)

        # NOTE: written "Reasoning Object", never through an uppercase chip —
        # .upper() smashes the compound to REASONINGOBJECT (tips.txt section 9).
        specs = [
            ("Reasoning Object", ["frozen after write",
                                  "conclusion · steps · confidence"], [-3.4, 1.35, 0]),
            ("Validation Loop",  ["parse, one retry, then halt",
                                  "both attempts recorded"],          [3.4, 1.35, 0]),
            ("The Store",        ["SQLite, append-only triggers",
                                  "RAISE(ABORT) on update"],          [-3.4, -1.55, 0]),
            ("Consistency Probe", ["0.6 numbers · 0.4 words",
                                   "0.70 / 0.40 thresholds"],         [3.4, -1.55, 0]),
        ]
        cards, boxes = [], []
        for name, lines, pos in specs:
            t = label(name, size=28, weight="BOLD", color=INK)
            subs = VGroup(*[mono(s, size=24, color=SOFT) if any(ch.isdigit() for ch in s)
                            else label(s, size=24, color=SOFT) for s in lines])
            subs.arrange(DOWN, buff=0.18)
            inner = VGroup(t, subs).arrange(DOWN, buff=0.26)
            g = boxed(inner, color=GHOST, h_pad=0.5, v_pad=0.34).move_to(pos)
            cards.append(g)
            boxes.append(g[0])

        for g in cards:
            self.play(FadeIn(g, scale=0.94), run_time=0.5)
            self.wait(1.9)

        self.wait(1.2)
        # the fourth card is the hinge — it already had the scoring
        self.play(boxes[3].animate.set_stroke(color=ACC, width=4), run_time=0.5)
        self.wait(2.2)

        self.play(*[FadeOut(g) for g in cards], FadeOut(head), run_time=0.6)

        # ── pointed at itself ────────────────────────────────────────────────
        node = Circle(radius=0.55, color=INK, stroke_width=3,
                      fill_opacity=0.06, fill_color=INK).move_to([0, 0.55, 0])
        loop = Arc(radius=1.35, start_angle=-PI / 2.2, angle=1.75 * PI,
                   color=ACC, stroke_width=4).move_arc_center_to([0, 0.55, 0])
        loop.add_tip(tip_length=0.28)
        # The label must clear the ARC, not just the circle — at buff from the
        # node it lands inside the loop and the arrow tip strikes the first glyph.
        node_lbl = label("ONE AGENT", size=26, color=INK).next_to(loop, DOWN, buff=0.34)
        self.play(FadeIn(node), FadeIn(node_lbl), run_time=0.5)
        self.play(Create(loop), run_time=1.0)
        self.wait(1.4)

        cap = label("COMPARED AGAINST A REPEAT OF ITSELF", size=28,
                    weight="BOLD", color=SOFT).move_to([0, -2.6, 0])
        self.play(FadeIn(cap), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B03_TheOrphan   (target ~34s)
#  The declared-but-empty orchestration layer, the counters, the node-layer gap.
# ─────────────────────────────────────────────────────────────────────────────
class B03_TheOrphan(Scene):
    TARGET = 43.09  # actual_duration_s, Kokoro am_onyx

    def construct(self):
        self.camera.background_color = BG

        head = label("THE DECLARED ARCHITECTURE", size=28, weight="BOLD",
                     color=SOFT).move_to([0, 3.3, 0])
        self.play(FadeIn(head), run_time=0.4)

        # ── orchestration layer: three mechanisms, all empty ─────────────────
        # Labels wrapped to two lines — at floor size the one-line forms collide
        # (tips.txt section 6).
        mechs = [("Cross-Agent\nValidation", -4.0),
                 ("Dynamic Task\nAllocation", 0.0),
                 ("Pattern\nRecognition", 4.0)]
        mgroups, mboxes = [], []
        for name, x in mechs:
            t = label(name, size=26, weight="BOLD", color=INK, line_spacing=0.7)
            g = boxed(t, color=GHOST, h_pad=0.42, v_pad=0.3).move_to([x, 1.55, 0])
            mgroups.append(g)
            mboxes.append(g[0])
        # Band is tall enough to hold the boxes AND their per-box stamp, so the
        # stamp never crosses the dashed edge.
        band = DashedVMobject(
            Rectangle(width=12.4, height=2.9, color=GHOST, stroke_width=2.5)
            .move_to([0, 1.45, 0]), num_dashes=76, color=GHOST)
        band_lbl = label("ORCHESTRATION LAYER", size=24, color=SOFT)
        band_lbl.move_to([0, 2.55, 0])

        self.play(Create(band), FadeIn(band_lbl), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(g) for g in mgroups], lag_ratio=0.3),
                  run_time=1.2)
        self.wait(1.6)

        # "ZERO IMPLEMENTATION" under each box measures ~4.1 units at size 24 —
        # wider than the 4.0 node pitch, so three of them merge into one
        # unreadable smear. Short per-box stamp + one shared line underneath.
        stamps = VGroup(*[label("EMPTY", size=24, weight="BOLD", color=GHOST)
                          .next_to(g, DOWN, buff=0.24) for g in mgroups])
        stamp_line = label("three declared mechanisms · zero implementation",
                           size=26, color=SOFT).move_to([0, -0.6, 0])
        self.play(LaggedStart(*[FadeIn(s) for s in stamps], lag_ratio=0.25),
                  run_time=1.0)
        self.play(FadeIn(stamp_line), run_time=0.4)
        self.wait(2.0)

        self.play(mboxes[0].animate.set_stroke(color=ACC, width=4),
                  mgroups[1].animate.set_opacity(0.28),
                  mgroups[2].animate.set_opacity(0.28),
                  stamps[1].animate.set_opacity(0.28),
                  stamps[2].animate.set_opacity(0.28),
                  stamp_line.animate.set_opacity(0.28),
                  run_time=0.7)
        self.wait(2.0)
        self.play(FadeOut(VGroup(head, band, band_lbl, *mgroups, stamps,
                                 stamp_line)), run_time=0.6)

        # ── the counters ─────────────────────────────────────────────────────
        head2 = label("THE BEST-SPECIFIED ORPHAN", size=28, weight="BOLD",
                      color=SOFT).move_to([0, 3.3, 0])
        self.play(FadeIn(head2), run_time=0.35)

        rows = [("specification", "21,824 bytes", SOFT),
                ("conductor documents", "1", SOFT),
                ("scaffolded node scripts", "16", SOFT),
                ("shared logic wiring it together", "0", ACC)]
        ys = [1.85, 0.95, 0.05, -0.95]
        drawn = VGroup()
        for (k, v, col), y in zip(rows, ys):
            kk = label(k, size=26, color=INK if col is SOFT else ACC)
            kk.move_to([0.2, y, 0], aligned_edge=RIGHT)
            vv = mono(v, size=30 if col is SOFT else 40, color=col)
            vv.move_to([0.8, y, 0], aligned_edge=LEFT)
            drawn.add(kk, vv)
            self.play(FadeIn(kk), FadeIn(vv), run_time=0.45)
            self.wait(1.9 if col is ACC else 0.75)
        self.wait(1.6)
        self.play(FadeOut(drawn), FadeOut(head2), run_time=0.55)

        # ── the node-layer gap ───────────────────────────────────────────────
        head3 = label("THE NODE LAYER", size=28, weight="BOLD",
                      color=SOFT).move_to([0, 3.3, 0])
        self.play(FadeIn(head3), run_time=0.35)

        x0, sc = -5.0, 10.0 / 30497.0
        b1 = Rectangle(width=30497 * sc, height=0.75, color=GHOST, stroke_width=2,
                       fill_opacity=0.3, fill_color=GHOST)
        b1.move_to([x0, 1.15, 0], aligned_edge=LEFT)
        l1 = label("30,497 lines total", size=26, color=SOFT).next_to(b1, DOWN, buff=0.22)
        l1.align_to(b1, LEFT)

        b2 = Rectangle(width=max(1276 * sc, 0.06), height=0.75, color=ACC,
                       stroke_width=2, fill_opacity=0.85, fill_color=ACC)
        b2.move_to([x0, -0.85, 0], aligned_edge=LEFT)
        l2 = label("1,276 lines of real logic", size=26, color=ACC)
        l2.next_to(b2, RIGHT, buff=0.3)

        self.play(GrowFromEdge(b1, LEFT), run_time=0.7)
        self.play(FadeIn(l1), run_time=0.35)
        self.wait(1.2)
        self.play(GrowFromEdge(b2, LEFT), run_time=0.5)
        self.play(FadeIn(l2), run_time=0.35)
        self.wait(2.0)

        tests = muted_chip("TESTS IN THE NODE LAYER: 0").move_to([0, -2.7, 0])
        self.play(FadeIn(tests), run_time=0.4)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_CutsAreTheDesign   (target ~35s)
#  Why a fixture is a discipline, and the scope list.
# ─────────────────────────────────────────────────────────────────────────────
class B04_CutsAreTheDesign(Scene):
    TARGET = 39.96  # actual_duration_s, Kokoro am_onyx

    IN_SCOPE = ["one real agent (live EDGAR)",
                "one hand-written fixture",
                "numeric divergence only",
                "one shared run ID",
                "write a record, then stop"]
    DEFERRED = [("a real second agent", "blocked"),
                ("claim decomposition", "scope"),
                ("authority weighting", "-0.006"),
                ("a debate loop", "cost"),
                ("pattern recognition", "unverifiable"),
                ("SQL-queryable column", "premature"),
                ("any new HTTP route", "exposure")]

    def construct(self):
        self.camera.background_color = BG

        # ── the two producers ────────────────────────────────────────────────
        pa_t = VGroup(mono("AgentID.FINANCIAL", size=26, color=INK),
                      label("live SEC EDGAR", size=24, color=SOFT)
                      ).arrange(DOWN, buff=0.22)
        pa = boxed(pa_t, color=INK).move_to([-3.3, 2.2, 0])
        pb_t = VGroup(mono("AgentID.EARNINGS", size=26, color=INK),
                      label("hand-written fixture", size=24, color=SOFT)
                      ).arrange(DOWN, buff=0.22)
        pb = boxed(pb_t, color=ACC).move_to([3.3, 2.2, 0])

        self.play(FadeIn(pa), run_time=0.45)
        self.play(FadeIn(pb), run_time=0.45)
        self.wait(1.8)

        # ── two hypotheses you cannot separate ───────────────────────────────
        cnode_t = label("CONTRADICTION", size=26, weight="BOLD", color=INK)
        cnode = boxed(cnode_t, color=INK).move_to([0, 0.35, 0])
        self.play(FadeIn(cnode), run_time=0.45)

        h1_t = label("they genuinely\ndisagree", size=26, color=INK, line_spacing=0.7)
        h1 = boxed(h1_t, color=GHOST).move_to([-3.0, -1.85, 0])
        h2_t = label("your comparator\nis broken", size=26, color=INK, line_spacing=0.7)
        h2 = boxed(h2_t, color=GHOST).move_to([3.0, -1.85, 0])
        e1 = Line(cnode[0].get_bottom(), h1[0].get_top(), color=GHOST, stroke_width=2.5)
        e2 = Line(cnode[0].get_bottom(), h2[0].get_top(), color=GHOST, stroke_width=2.5)

        self.play(Create(e1), Create(e2), run_time=0.5)
        self.play(FadeIn(h1), FadeIn(h2), run_time=0.5)
        self.wait(1.4)

        both = label("with two real producers, neither can be eliminated",
                     size=24, color=SOFT).move_to([0, -3.2, 0])
        self.play(FadeIn(both), run_time=0.4)
        self.wait(2.2)

        # the fixture kills one branch
        self.play(h2.animate.set_opacity(0.18), e2.animate.set_opacity(0.18),
                  h1[0].animate.set_stroke(color=ACC, width=4),
                  e1.animate.set_stroke(color=ACC, width=3.5),
                  FadeOut(both), run_time=0.7)
        kill = label("a wrong result can only be the comparator's fault",
                     size=24, color=ACC).move_to([0, -3.2, 0])
        self.play(FadeIn(kill), run_time=0.4)
        self.wait(2.4)

        self.play(FadeOut(VGroup(pa, pb, cnode, h1, h2, e1, e2, kill)), run_time=0.6)

        # ── the scope list, two columns (never one 12-row stack) ─────────────
        # 12 rows in a single column runs past y = -3.6 at floor type size
        # (tips.txt section 7), so IN SCOPE and DEFERRED sit side by side.
        h_in = label("IN SCOPE", size=28, weight="BOLD", color=INK)
        h_in.move_to([-3.5, 2.75, 0])
        h_de = label("DEFERRED", size=28, weight="BOLD", color=GHOST)
        h_de.move_to([2.6, 2.75, 0])
        self.play(FadeIn(h_in), FadeIn(h_de), run_time=0.4)

        in_rows = VGroup(*[checked(t, size=24, color=INK) for t in self.IN_SCOPE])
        in_rows.arrange(DOWN, buff=0.34, aligned_edge=LEFT)
        in_rows.next_to(h_in, DOWN, buff=0.45).align_to(h_in, LEFT).shift(LEFT * 1.5)

        de_rows = VGroup()
        for t, why in self.DEFERRED:
            row = VGroup(checked(t, size=24, color=GHOST, symbol="✕"),
                         label(why, size=24, color=GHOST))
            de_rows.add(row)
        for r in de_rows:
            r.arrange(RIGHT, buff=0.3)
        de_rows.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        de_rows.next_to(h_de, DOWN, buff=0.45).align_to(h_de, LEFT).shift(LEFT * 0.9)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.1) for r in in_rows],
                              lag_ratio=0.3), run_time=1.6)
        self.wait(1.0)
        self.play(LaggedStart(*[FadeIn(r) for r in de_rows], lag_ratio=0.22),
                  run_time=1.8)
        self.wait(1.8)

        self.play(de_rows[6].animate.set_color(ACC), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B05_SymmetricDifference   (target ~35s)   the visual spine of the reel
# ─────────────────────────────────────────────────────────────────────────────
class B05_SymmetricDifference(Scene):
    TARGET = 38.36  # actual_duration_s, Kokoro am_onyx

    def construct(self):
        self.camera.background_color = BG

        # ── three files ──────────────────────────────────────────────────────
        head = label("THREE FILES", size=28, weight="BOLD", color=SOFT)
        head.move_to([0, 3.3, 0])
        self.play(FadeIn(head), run_time=0.4)

        files = [("cross_validation.py", 331, ACC),
                 ("adapters/fixture_adapter.py", 81, SOFT),
                 ("tests/test_cross_validation.py", 375, ACC)]
        rows = VGroup()
        for nm, n, col in files:
            t = mono(nm, size=26, color=INK)
            bar = Rectangle(width=n / 375.0 * 3.2, height=0.32, color=col,
                            stroke_width=1.5, fill_opacity=0.5, fill_color=col)
            cnt = mono("%d lines" % n, size=24, color=SOFT)
            r = VGroup(t, bar, cnt).arrange(RIGHT, buff=0.4)
            rows.add(r)
        for r in rows:
            r[0].align_to(rows[2][0], LEFT)
        rows.arrange(DOWN, buff=0.42, aligned_edge=LEFT).move_to([0, 1.6, 0])

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.12) for r in rows],
                              lag_ratio=0.3), run_time=1.5)
        self.wait(2.2)

        sig = label("each agent gets its own context", size=26, color=INK)
        sig_chip = label_chip("ASYMMETRY, IN THE SIGNATURE", ACC, size=24)
        sigg = VGroup(sig, sig_chip).arrange(DOWN, buff=0.34).move_to([0, -1.4, 0])
        self.play(FadeIn(sigg), run_time=0.5)
        self.wait(2.2)
        self.play(FadeOut(rows), FadeOut(sigg), FadeOut(head), run_time=0.55)

        # ── the halt handler, real source ────────────────────────────────────
        code = VGroup(
            mono("except HaltError as exc:", size=26, color=INK),
            mono("    # The halt is the evidence.", size=26, color=ACC),
            mono("    return None, list(exc.reasoning_objects), True", size=26, color=INK),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        cbox = auto_box(code, h_pad=0.55, v_pad=0.42, color=GHOST, fill_opacity=0.05)
        cunit = VGroup(cbox, code).move_to([0, 0.6, 0])
        ctag = mono("cross_validation.py", size=24, color=SOFT)
        ctag.next_to(cbox, UP, buff=0.26)

        self.play(Create(cbox), FadeIn(ctag), run_time=0.5)
        self.play(FadeIn(code[0]), run_time=0.4)
        self.play(FadeIn(code[1]), run_time=0.4)
        self.play(FadeIn(code[2]), run_time=0.4)
        self.wait(3.0)
        self.play(FadeOut(cunit), FadeOut(ctag), run_time=0.5)

        # ── the symmetric difference ─────────────────────────────────────────
        self._set_pass(["12%", "4.2B", "0.91"], ["8%", "4.2B", "0.91"],
                       {"12%", "8%"}, "DIFFERENT VALUE")
        self._set_pass(["12%", "4.2B"], ["4.2B"],
                       {"12%"}, "MISSING ENTIRELY")

        cap = label("SAME RULE. NO SPECIAL CASE.", size=34, weight="BOLD", color=ACC)
        cap.move_to([0, 0.4, 0])
        chips = VGroup(muted_chip("NO MODEL"), muted_chip("NO JUDGE"),
                       label_chip("SET ARITHMETIC", ACC, size=24)
                       ).arrange(RIGHT, buff=0.34).move_to([0, -1.3, 0])
        self.play(FadeIn(cap), run_time=0.45)
        self.play(FadeIn(chips), run_time=0.45)
        hold_to(self, self.TARGET)

    def _set_pass(self, a_vals, b_vals, divergent, tag):
        """One run of the comparison: shared numbers cancel, the rest lift out."""
        head = label("conclusion A", size=24, color=SOFT).move_to([-3.4, 2.9, 0])
        head_b = label("conclusion B", size=24, color=SOFT).move_to([3.4, 2.9, 0])

        a_chips = VGroup(*[num_chip(v) for v in a_vals]).arrange(DOWN, buff=0.28)
        a_box = auto_box(a_chips, h_pad=0.5, v_pad=0.4, color=GHOST) if a_vals else None
        a_unit = VGroup(a_box, a_chips) if a_box else VGroup(a_chips)
        a_unit.move_to([-3.4, 1.15, 0])

        if b_vals:
            b_chips = VGroup(*[num_chip(v) for v in b_vals]).arrange(DOWN, buff=0.28)
            b_box = auto_box(b_chips, h_pad=0.5, v_pad=0.4, color=GHOST)
            b_unit = VGroup(b_box, b_chips)
        else:
            b_chips = VGroup()
            b_unit = VGroup()
        b_unit.move_to([3.4, 1.15, 0])

        self.play(FadeIn(head), FadeIn(head_b), FadeIn(a_unit), FadeIn(b_unit),
                  run_time=0.6)
        self.wait(1.0)

        # shared values cancel
        shared_a = [c for c, v in zip(a_chips, a_vals) if v not in divergent]
        shared_b = [c for c, v in zip(b_chips, b_vals) if v not in divergent]
        if shared_a or shared_b:
            self.play(*[c.animate.set_opacity(0.16) for c in shared_a + shared_b],
                      run_time=0.6)
            self.wait(0.9)

        # what's left in exactly one set lifts out
        keep = [c for c, v in zip(a_chips, a_vals) if v in divergent]
        keep += [c for c, v in zip(b_chips, b_vals) if v in divergent]
        targets = VGroup(*[c.copy() for c in keep])
        targets.arrange(RIGHT, buff=0.5).move_to([0, -1.55, 0])
        for c in targets:
            c[0].set_stroke(color=ACC, width=4)
            c[1].set_color(ACC)

        out_lbl = label("DIVERGENT", size=26, weight="BOLD", color=ACC)
        out_lbl.move_to([0, -0.65, 0])
        tag_lbl = label(tag, size=24, color=SOFT).move_to([0, -2.6, 0])

        self.play(FadeIn(out_lbl), run_time=0.3)
        self.play(*[ReplacementTransform(c.copy(), t) for c, t in zip(keep, targets)],
                  run_time=0.9)
        self.play(FadeIn(tag_lbl), run_time=0.3)
        self.wait(2.2)

        self.play(FadeOut(VGroup(head, head_b, a_unit, b_unit, out_lbl,
                                 targets, tag_lbl)), run_time=0.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B06_RunIdAndMutation   (target ~40s)
#  Two halves with a hard cut: the integration, then breaking it on purpose.
# ─────────────────────────────────────────────────────────────────────────────
class B06_RunIdAndMutation(Scene):
    TARGET = 41.77  # actual_duration_s, Kokoro am_onyx

    def construct(self):
        self.camera.background_color = BG

        # ── HALF ONE: one run ID ─────────────────────────────────────────────
        head = label("ONE RUN ID", size=28, weight="BOLD", color=SOFT)
        head.move_to([0, 3.3, 0])
        self.play(FadeIn(head), run_time=0.4)

        sa = VGroup(*[record_card(w=2.3, h=0.42, color=INK) for _ in range(3)])
        sa.arrange(DOWN, buff=0.18).move_to([-3.6, 1.05, 0])
        sb = VGroup(*[record_card(w=2.3, h=0.42, color=INK) for _ in range(3)])
        sb.arrange(DOWN, buff=0.18).move_to([3.6, 1.05, 0])
        la = label("agent A", size=24, color=SOFT).next_to(sa, UP, buff=0.24)
        lb = label("agent B", size=24, color=SOFT).next_to(sb, UP, buff=0.24)

        self.play(FadeIn(sa), FadeIn(sb), FadeIn(la), FadeIn(lb), run_time=0.6)
        self.wait(1.2)

        self.play(sa.animate.move_to([-1.35, 1.05, 0]),
                  sb.animate.move_to([1.35, 1.05, 0]),
                  FadeOut(la), FadeOut(lb), run_time=0.9)
        container = DashedVMobject(
            Rectangle(width=6.4, height=2.5, color=ACC, stroke_width=3)
            .move_to([0, 1.05, 0]), num_dashes=48, color=ACC)
        cid = mono("run_id: 7f3a…", size=28, color=ACC).next_to(container, UP, buff=0.22)
        self.play(Create(container), FadeIn(cid), run_time=0.7)
        self.wait(1.0)

        chip = label_chip("THE COMPARISON IS THE EVIDENCE", ACC, size=24)
        chip.move_to([0, -1.15, 0])
        self.play(FadeIn(chip), run_time=0.4)
        self.wait(2.2)
        self.play(FadeOut(VGroup(sa, sb, container, cid, chip, head)), run_time=0.55)

        # ── the payload: one new key ─────────────────────────────────────────
        keys = ["run_id", "subject", "scope", "halted",
                "reasoning_objects", "session", "cross_agent_comparison"]
        klines = VGroup(*[mono('"%s": …' % k, size=26,
                               color=ACC if k == "cross_agent_comparison" else GHOST)
                          for k in keys])
        klines.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        kbox = auto_box(klines, h_pad=0.55, v_pad=0.42, color=GHOST, fill_opacity=0.04)
        kunit = VGroup(kbox, klines).move_to([0, 0.5, 0])
        ktag = mono("payload", size=24, color=SOFT).next_to(kbox, UP, buff=0.24)

        self.play(Create(kbox), FadeIn(ktag), FadeIn(klines), run_time=0.8)
        self.wait(1.6)
        onekey = label_chip("ONE NEW KEY", ACC, size=24).move_to([0, -2.55, 0])
        self.play(klines[6].animate.scale(1.06), FadeIn(onekey), run_time=0.5)
        self.wait(2.2)
        self.play(FadeOut(kunit), FadeOut(ktag), FadeOut(onekey), run_time=0.5)

        # ── inherited for free ───────────────────────────────────────────────
        inh = VGroup(
            muted_chip("APPEND-ONLY"), muted_chip("IMMUTABLE RECORDS"),
            muted_chip("TIERED DISCLOSURE"),
        ).arrange(RIGHT, buff=0.4).move_to([0, 0.9, 0])
        inh_cap = label("NONE OF THIS WAS WRITTEN\nFOR CROSS-AGENT VALIDATION",
                        size=28, weight="BOLD", color=INK, line_spacing=0.7)
        inh_cap.move_to([0, -1.1, 0])
        self.play(LaggedStart(*[FadeIn(c) for c in inh], lag_ratio=0.28), run_time=1.0)
        self.play(FadeIn(inh_cap), run_time=0.5)
        self.wait(2.6)
        self.play(FadeOut(inh), FadeOut(inh_cap), run_time=0.5)

        # ── HARD CUT: HALF TWO — green is a claim ────────────────────────────
        green = mono("129 / 129", size=84, color=INK).move_to([0, 0.9, 0])
        gsub = label("all passing", size=26, color=SOFT).next_to(green, DOWN, buff=0.3)
        self.play(FadeIn(green, scale=1.08), FadeIn(gsub), run_time=0.6)
        self.wait(1.4)
        q = Text("?", font_size=110, color=ACC).next_to(green, RIGHT, buff=0.6)
        self.play(FadeIn(q, scale=0.8), run_time=0.5)
        self.wait(2.0)
        self.play(FadeOut(green), FadeOut(gsub), FadeOut(q), run_time=0.5)

        # ── the mutation table ───────────────────────────────────────────────
        head3 = label("SO I BROKE IT ON PURPOSE", size=28, weight="BOLD",
                      color=SOFT).move_to([0, 3.3, 0])
        self.play(FadeIn(head3), run_time=0.35)

        muts = [("symmetric_difference -> intersection", "7 tests failed", ACC),
                ("contradiction_flag None -> False", "3 tests failed", ACC),
                ("file restored byte-identical", "129 / 129", SOFT)]
        ys = [1.85, 0.85, -0.15]
        drawn = VGroup()
        for (m, r, col), y in zip(muts, ys):
            mm = mono(m, size=24, color=INK)
            mm.move_to([0.15, y, 0], aligned_edge=RIGHT)
            rr = label(r, size=26, weight="BOLD", color=col)
            rr.move_to([0.75, y, 0], aligned_edge=LEFT)
            drawn.add(mm, rr)
            self.play(FadeIn(mm), FadeIn(rr), run_time=0.45)
            self.wait(1.5)
        self.wait(1.2)
        self.play(FadeOut(drawn), FadeOut(head3), run_time=0.5)

        # ── the sharpest idea in the reel gets the last frames ───────────────
        f_t = VGroup(mono("false", size=36, color=INK),
                     label("CHECKED.\nFOUND NOTHING.", size=26, color=SOFT,
                           line_spacing=0.7)).arrange(DOWN, buff=0.32)
        f_g = boxed(f_t, color=GHOST, h_pad=0.6, v_pad=0.44).move_to([-3.2, 0.4, 0])

        n_t = VGroup(mono("null", size=36, color=ACC),
                     label("NO CHECK WAS\nPOSSIBLE.", size=26, color=INK,
                           line_spacing=0.7)).arrange(DOWN, buff=0.32)
        n_g = boxed(n_t, color=ACC, h_pad=0.6, v_pad=0.44, stroke_width=4)
        n_g.move_to([3.2, 0.4, 0])

        self.play(FadeIn(f_g), run_time=0.5)
        self.play(FadeIn(n_g), run_time=0.5)
        self.wait(1.6)
        tail = label("these are different statements", size=26, color=SOFT)
        tail.move_to([0, -2.5, 0])
        self.play(FadeIn(tail), run_time=0.45)
        hold_to(self, self.TARGET)
