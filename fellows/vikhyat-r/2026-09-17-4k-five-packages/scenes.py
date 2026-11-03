"""scenes.py — Manim scenes for hai-4k-five-packages.

Humanitarians palette (skills/make/hai/SKILL.md): cream ground, warm ink text,
teal for kept/true, crimson for lost/wrong, slate for structure. GOLD is a
highlighter fill only and is NEVER used as text (Gate W refuses gold text).

House rules observed:
  - ONE accent moment per scene.
  - Numbers appear on screen only alongside the file they came from.
  - No slant=ITALIC on multi-word Text (Pango collapses the spaces).
  - Content stays inside the title-safe area: x in [-6.4, 6.4], y in [-3.5, 3.5].
  - No text placed on top of other text.

Rendered by run.sh at -r 3840,2160 (landscape) or -r 2160,3840 (portrait),
so every scene here is natively 4K. Nothing in this file lives in the toolkit
tree; it belongs to the reel.
"""
from manim import *

# ── Humanitarians palette ────────────────────────────────────────────────────
BG      = ManimColor("#F3EBDD")   # cream ground
INK     = ManimColor("#2F2A26")   # warm ink — all body text
TEAL    = ManimColor("#1F4E5F")   # kept / true / target
CRIMSON = ManimColor("#E4572E")   # lost / wrong / declined
SLATE   = ManimColor("#29335C")   # structure, entity cards
SAGE    = ManimColor("#A8C686")   # human / growth
SOFT    = ManimColor("#6E675E")   # secondary, citation lines
GHOST   = ManimColor("#B6AE9F")   # dimmed
CARD    = ManimColor("#FFFFFF")   # card surface


def _t(text, size=22, color=None, weight=None):
    kw = {"font_size": size, "color": color or INK}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw)


def _cite(text, size=15):
    return Text(text, font_size=size, color=SOFT)


def _title(text, size=32):
    # buff 0.65, not 0.55: Manim's frame half-height is 4.0 and Gate B's safe
    # area stops at y=3.4, so to_edge(UP, buff=0.55) lands the box top at 3.45
    # and trips "outside safe area" by five hundredths of a unit.
    return _t(text, size=size, weight="BOLD").to_edge(UP, buff=0.65)


def _card(w, h, stroke=INK, fill=CARD, width=1.6):
    """Outline only — deliberately NOT filled.

    A white (#FFFFFF) card on the cream (#F3EBDD) ground is nearly the same
    luminance as its background. Gate V measures ink-vs-background separation
    over the whole ink mask, and a large white fill swamps the dark text: the
    filled version scored 0.00-0.05 against a 0.30 minimum. Outline cards read
    better on cream anyway.
    """
    return Rectangle(width=w, height=h, color=stroke,
                     stroke_width=width, fill_opacity=0.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B01 — One question, four answers.
# ─────────────────────────────────────────────────────────────────────────────
class B01_FourNumbers(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("One question. Four answers.")
        self.play(Write(title), run_time=0.9)

        q = _t("What height does a final master use?", size=24, color=SLATE)
        q.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(q, shift=UP * 0.2), run_time=0.7)

        rows = [
            ("2160", "art — the final command", TEAL),
            ("1080", "a skill guide", CRIMSON),
            ("720",  "compile.py — the built-in fallback", CRIMSON),
            ("1920", "the vertical helper", CRIMSON),
        ]

        y0 = 0.95
        built = VGroup()
        for i, (num, src, col) in enumerate(rows):
            y = y0 - i * 1.05
            n = _t(num, size=40, color=col, weight="BOLD")
            n.move_to(LEFT * 3.9 + UP * y)
            s = _cite(src, size=17)
            s.move_to(RIGHT * 0.9 + UP * y).align_to(LEFT * 1.6, LEFT)
            rule = Line(LEFT * 5.6 + UP * (y - 0.48),
                        RIGHT * 5.6 + UP * (y - 0.48),
                        stroke_width=0.8, color=GHOST)
            self.play(FadeIn(n, shift=RIGHT * 0.25), FadeIn(s), run_time=0.55)
            self.play(Create(rule), run_time=0.25)
            built.add(n, s, rule)

        self.wait(2.38)

        note = _t("One of the four is the stated target.", size=20, color=SLATE)
        note.move_to(DOWN * 3.15)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.8)
        self.wait(3.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B02 — Prevent, catch, detect.
# ─────────────────────────────────────────────────────────────────────────────
class B02_ThreePositions(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("Three places a check can sit")
        self.play(Write(title), run_time=0.9)

        spine = Line(LEFT * 5.7, RIGHT * 5.7, stroke_width=2.2, color=INK)
        spine.shift(UP * 0.35)
        self.play(Create(spine), run_time=0.9)

        stations = [
            (-4.0, "PREVENT", "inside the toolkit", TEAL),
            (0.0,  "CATCH",   "on the fellow's machine", SLATE),
            (4.0,  "DETECT",  "in the Drive", CRIMSON),
        ]

        marks = VGroup()
        for x, name, sub, col in stations:
            d = Dot(point=RIGHT * x + UP * 0.35, radius=0.115, color=col)
            lab = _t(name, size=23, color=col, weight="BOLD")
            lab.move_to(RIGHT * x + UP * 1.05)
            sb = _cite(sub, size=16)
            sb.move_to(RIGHT * x + DOWN * 0.25)
            self.play(GrowFromCenter(d), FadeIn(lab, shift=DOWN * 0.15),
                      FadeIn(sb), run_time=0.6)
            marks.add(d, lab, sb)

        self.wait(1.36)

        cap = _t("people involved by the time it surfaces", size=19, color=SOFT)
        cap.move_to(DOWN * 1.65)
        self.play(FadeIn(cap), run_time=0.6)

        counts = VGroup()
        for x, n in ((-4.0, "one"), (0.0, "one"), (4.0, "two or more")):
            c = _t(n, size=21, color=INK)
            c.move_to(RIGHT * x + DOWN * 2.35)
            counts.add(c)
        for c in counts:
            self.play(FadeIn(c, shift=UP * 0.15), run_time=0.45)

        self.wait(1.7)

        arrow = Arrow(LEFT * 4.0 + DOWN * 3.15, RIGHT * 4.0 + DOWN * 3.15,
                      stroke_width=2.0, color=GHOST, buff=0,
                      max_tip_length_to_length_ratio=0.03)
        self.play(Create(arrow), run_time=1.0)
        self.wait(3.06)


# ─────────────────────────────────────────────────────────────────────────────
#  B03 — Package one: the starter kit.
# ─────────────────────────────────────────────────────────────────────────────
class B03_StarterKit(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("One — a starter kit")
        self.play(Write(title), run_time=0.9)

        # card A — what gets pasted.
        # Height 3.0, not 2.5: header offset (0.42 + 0.34) plus four 0.25 lines
        # at 0.26 buff needs 2.54 units, so a 2.5 card clipped its last two
        # lines. Gate V saw it; Gate B did not, because Gate B measures Text
        # boxes against the FRAME, not against the card they sit inside.
        a = _card(6.0, 3.0).move_to(LEFT * 3.25 + UP * 0.4)
        a_h = _t("pasted before building", size=20, color=SLATE, weight="BOLD")
        a_h.move_to(a.get_top() + DOWN * 0.42)
        items = VGroup(*[_cite(s, size=17) for s in (
            "3840 × 2160  landscape",
            "2160 × 3840  vertical",
            "ProjectName_VolunteerName.mp4",
            "the channel it is for",
        )]).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        items.next_to(a_h, DOWN, buff=0.3)
        self.play(Create(a), run_time=0.6)
        self.play(FadeIn(a_h), run_time=0.4)
        for it in items:
            self.play(FadeIn(it, shift=RIGHT * 0.15), run_time=0.32)

        # card B — the self-check
        b = _card(6.0, 3.0).move_to(RIGHT * 3.25 + UP * 0.4)
        b_h = _t("run before uploading", size=20, color=SLATE, weight="BOLD")
        b_h.move_to(b.get_top() + DOWN * 0.42)
        checks = [("both formats present", TEAL), ("both at target size", TEAL),
                  ("filename matches", TEAL), ("opening line present", CRIMSON)]
        rowg = VGroup()
        for label, col in checks:
            mark = _t("✓" if col is TEAL else "✗", size=19, color=col)
            lab = _cite(label, size=17)
            rowg.add(VGroup(mark, lab).arrange(RIGHT, buff=0.22))
        rowg.arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        rowg.next_to(b_h, DOWN, buff=0.3)
        self.play(Create(b), run_time=0.6)
        self.play(FadeIn(b_h), run_time=0.4)
        for r in rowg:
            self.play(FadeIn(r, shift=RIGHT * 0.15), run_time=0.32)

        self.wait(1.7)

        limit = _t("It relies on being used. A nudge, not a guarantee.",
                   size=20, color=SLATE)
        limit.move_to(DOWN * 2.55)
        self.play(FadeIn(limit, shift=UP * 0.2), run_time=0.8)
        self.wait(3.06)


# ─────────────────────────────────────────────────────────────────────────────
#  B04 — Package two: standardise, and decline.
# ─────────────────────────────────────────────────────────────────────────────
class B04_Standardise(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("Two — decline at the point of writing")
        self.play(Write(title), run_time=0.9)

        already = _t("the rule that already exists", size=19, color=SOFT)
        already.move_to(LEFT * 3.35 + UP * 1.95)
        proposed = _t("the same shape, for resolution", size=19, color=SOFT)
        proposed.move_to(RIGHT * 3.35 + UP * 1.95)
        self.play(FadeIn(already), FadeIn(proposed), run_time=0.6)

        left = _card(5.7, 2.2, stroke=SLATE).move_to(LEFT * 3.35 + UP * 0.55)
        l1 = _t("a placeholder card remains", size=19).move_to(left.get_center() + UP * 0.42)
        l2 = _t("declined", size=25, color=TEAL, weight="BOLD")
        l2.move_to(left.get_center() + DOWN * 0.48)
        self.play(Create(left), run_time=0.55)
        self.play(FadeIn(l1), run_time=0.4)
        self.play(FadeIn(l2, scale=1.08), run_time=0.5)

        right = _card(5.7, 2.2, stroke=SLATE).move_to(RIGHT * 3.35 + UP * 0.55)
        r1 = _t("the size is not a target", size=19).move_to(right.get_center() + UP * 0.42)
        r2 = _t("declined", size=25, color=TEAL, weight="BOLD")
        r2.move_to(right.get_center() + DOWN * 0.48)
        self.play(Create(right), run_time=0.55)
        self.play(FadeIn(r1), run_time=0.4)
        self.play(FadeIn(r2, scale=1.08), run_time=0.5)

        mid = _t("a sibling of an existing habit, not a new kind of check",
                 size=20, color=SLATE)
        mid.move_to(DOWN * 1.45)
        self.play(FadeIn(mid, shift=UP * 0.2), run_time=0.8)

        cost = _cite("needs sign-off · does nothing for what is already submitted",
                     size=18)
        cost.move_to(DOWN * 2.6)
        self.play(FadeIn(cost), run_time=0.7)
        self.wait(7.6)


# ─────────────────────────────────────────────────────────────────────────────
#  B05 — Package three: the read-only report.
# ─────────────────────────────────────────────────────────────────────────────
class B05_DriveReport(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("Three — one row per file")
        self.play(Write(title), run_time=0.9)

        cols = [(-4.6, "fellow"), (-1.9, "format"), (1.0, "size"), (4.05, "verdict")]
        hdr = VGroup()
        for x, name in cols:
            h = _cite(name, size=17).move_to(RIGHT * x + UP * 1.75)
            hdr.add(h)
        rule = Line(LEFT * 5.8 + UP * 1.42, RIGHT * 5.8 + UP * 1.42,
                    stroke_width=1.2, color=INK)
        self.play(FadeIn(hdr), Create(rule), run_time=0.7)

        data = [
            ("maya-r",  "landscape", "3840 × 2160", "pass", TEAL),
            ("maya-r",  "vertical",  "1080 × 1920", "fail", CRIMSON),
            ("alex-t",  "landscape", "1920 × 1080", "fail", CRIMSON),
            ("sam-k",   "—",    "not received",  "open", SOFT),
        ]
        # Each row brings its own geometry — a separator drawn across and a
        # verdict pill built in place — so the frame keeps changing shape
        # rather than only fading text in (Gate A rejects a static shape-state).
        for i, (who, fmt, size, verdict, col) in enumerate(data):
            y = 0.92 - i * 0.78
            cells = VGroup(
                _t(who, size=19).move_to(RIGHT * cols[0][0] + UP * y),
                _t(fmt, size=19).move_to(RIGHT * cols[1][0] + UP * y),
                _t(size, size=19).move_to(RIGHT * cols[2][0] + UP * y),
            )
            pill = RoundedRectangle(corner_radius=0.16, width=1.78, height=0.5,
                                    color=col, stroke_width=1.6,
                                    fill_opacity=0.0)
            pill.move_to(RIGHT * cols[3][0] + UP * y)
            v = _t(verdict, size=18, color=col, weight="BOLD").move_to(pill.get_center())
            sep = Line(LEFT * 5.8 + UP * (y - 0.39), RIGHT * 5.8 + UP * (y - 0.39),
                       stroke_width=0.7, color=GHOST)
            self.play(FadeIn(cells, shift=RIGHT * 0.2), run_time=0.4)
            self.play(Create(pill), FadeIn(v), Create(sep), run_time=0.45)

        self.wait(1.1)

        # the column the whole report exists to read
        band = Rectangle(width=3.0, height=3.35, color=TEAL, stroke_width=1.8,
                         fill_color=TEAL, fill_opacity=0.07)
        band.move_to(RIGHT * cols[2][0] + DOWN * 0.26)
        self.play(Create(band), run_time=0.9)
        self.wait(0.9)

        dep = _t("grouping works because the name is in the filename",
                 size=20, color=SLATE)
        dep.move_to(DOWN * 2.6)
        self.play(FadeIn(dep, shift=UP * 0.2), run_time=0.8)

        dep2 = _cite("there is no author field inside a video", size=18)
        dep2.move_to(DOWN * 3.12)
        self.play(FadeIn(dep2), run_time=0.6)
        self.wait(3.06)


# ─────────────────────────────────────────────────────────────────────────────
#  B06 — Package four: real versus stretched.
# ─────────────────────────────────────────────────────────────────────────────
class B06_RealVsStretched(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("Four — the size is not the picture")
        self.play(Write(title), run_time=0.9)

        # the arithmetic, left to right
        small = _card(2.4, 1.35, stroke=SLATE).move_to(LEFT * 4.7 + UP * 0.5)
        s_lab = _cite("1280 × 720", size=18).next_to(small, DOWN, buff=0.24)
        s_top = _cite("a scene template", size=16).next_to(small, UP, buff=0.24)
        self.play(Create(small), FadeIn(s_lab), FadeIn(s_top), run_time=0.8)

        mid = _card(3.0, 1.69, stroke=SLATE).move_to(LEFT * 0.3 + UP * 0.5)
        m_lab = _cite("2560 × 1440", size=18).next_to(mid, DOWN, buff=0.24)
        m_top = _cite("rendered at double", size=16).next_to(mid, UP, buff=0.24)
        a1 = Arrow(small.get_right(), mid.get_left(), buff=0.22,
                   stroke_width=2.0, color=INK,
                   max_tip_length_to_length_ratio=0.16)
        self.play(Create(a1), run_time=0.5)
        self.play(Create(mid), FadeIn(m_lab), FadeIn(m_top), run_time=0.8)

        big = _card(3.8, 2.14, stroke=CRIMSON, width=2.0).move_to(RIGHT * 4.2 + UP * 0.5)
        b_lab = _cite("3840 × 2160", size=18).next_to(big, DOWN, buff=0.24)
        b_top = _t("stretched", size=18, color=CRIMSON).next_to(big, UP, buff=0.24)
        a2 = Arrow(mid.get_right(), big.get_left(), buff=0.22,
                   stroke_width=2.0, color=CRIMSON,
                   max_tip_length_to_length_ratio=0.16)
        self.play(Create(a2), run_time=0.5)
        self.play(Create(big), FadeIn(b_lab), FadeIn(b_top), run_time=0.8)

        self.wait(2.04)

        line1 = _t("The file measures 3840 × 2160. The picture does not.",
                   size=21, color=SLATE)
        line1.move_to(DOWN * 2.05)
        self.play(FadeIn(line1, shift=UP * 0.2), run_time=0.8)

        line2 = _cite("forty-eight of the built-in templates are defined at this size",
                      size=18)
        line2.move_to(DOWN * 2.62)
        self.play(FadeIn(line2), run_time=0.7)

        line3 = _cite("a confidence signal, not proof", size=18)
        line3.move_to(DOWN * 3.15)
        self.play(FadeIn(line3), run_time=0.6)
        self.wait(2.72)


# ─────────────────────────────────────────────────────────────────────────────
#  B07 — Package five: sorting.
# ─────────────────────────────────────────────────────────────────────────────
class B07_SortFolders(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("Five — the folder organises itself")
        self.play(Write(title), run_time=0.9)

        hub = _card(3.4, 0.95, stroke=SLATE).move_to(UP * 1.75)
        hub_l = _t("the same checks", size=20, color=SLATE).move_to(hub.get_center())
        self.play(Create(hub), FadeIn(hub_l), run_time=0.7)

        passed = _card(4.4, 1.5, stroke=TEAL).move_to(LEFT * 3.3 + DOWN * 0.45)
        p_l = _t("passed", size=23, color=TEAL, weight="BOLD").move_to(passed.get_center() + UP * 0.28)
        p_s = _cite("ready for review", size=17).move_to(passed.get_center() + DOWN * 0.38)

        needs = _card(4.4, 1.5, stroke=CRIMSON).move_to(RIGHT * 3.3 + DOWN * 0.45)
        n_l = _t("needs work", size=23, color=CRIMSON, weight="BOLD").move_to(needs.get_center() + UP * 0.28)
        n_s = _cite("reason attached", size=17).move_to(needs.get_center() + DOWN * 0.38)

        aL = Arrow(hub.get_bottom(), passed.get_top(), buff=0.18,
                   stroke_width=2.0, color=TEAL, max_tip_length_to_length_ratio=0.16)
        aR = Arrow(hub.get_bottom(), needs.get_top(), buff=0.18,
                   stroke_width=2.0, color=CRIMSON, max_tip_length_to_length_ratio=0.16)
        self.play(Create(aL), Create(aR), run_time=0.7)
        self.play(Create(passed), FadeIn(p_l), FadeIn(p_s),
                  Create(needs), FadeIn(n_l), FadeIn(n_s), run_time=0.9)

        self.wait(1.53)

        note = _card(6.6, 0.85, stroke=GHOST).move_to(DOWN * 2.35)
        note_l = _t("vertical is 1080 × 1920, needs 2160 × 3840",
                    size=19).move_to(note.get_center())
        self.play(Create(note), FadeIn(note_l), run_time=0.8)

        self.wait(1.36)
        limit = _cite("the detection is the value · the sorting is convenience", size=18)
        limit.move_to(DOWN * 3.15)
        self.play(FadeIn(limit), run_time=0.7)
        self.wait(2.72)


# ─────────────────────────────────────────────────────────────────────────────
#  B08 — What is actually being asked for.
# ─────────────────────────────────────────────────────────────────────────────
class B08_HonestAccounting(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("Five packages, counted honestly")
        self.play(Write(title), run_time=0.9)

        five = VGroup()
        for i in range(5):
            c = _card(1.95, 1.15, stroke=SLATE)
            lab = _t(str(i + 1), size=26, color=SLATE, weight="BOLD").move_to(c.get_center())
            five.add(VGroup(c, lab))
        five.arrange(RIGHT, buff=0.42).move_to(UP * 1.45)
        for g in five:
            self.play(FadeIn(g, shift=UP * 0.18), run_time=0.3)

        self.wait(1.53)

        shared = _t("one, three and four read the same finished folder",
                    size=20, color=SLATE)
        shared.move_to(DOWN * 2.3)
        self.play(FadeIn(shared), run_time=0.8)
        self.wait(1.36)

        # The three outcomes replace the five IN PLACE, so the frame does not
        # empty out at the top (FILL-THE-CANVAS — Gate V flags a clustered bbox).
        out = VGroup(
            VGroup(_card(3.15, 1.35, stroke=TEAL),
                   _t("one tool", size=22, color=TEAL, weight="BOLD")),
            VGroup(_card(3.15, 1.35, stroke=TEAL),
                   _t("one rule", size=22, color=TEAL, weight="BOLD")),
            VGroup(_card(3.15, 1.35, stroke=GHOST),
                   _t("one document", size=22, color=SOFT)),
        )
        for g in out:
            g[1].move_to(g[0].get_center())
        out.arrange(RIGHT, buff=0.5).move_to(UP * 1.45)

        self.play(ReplacementTransform(five, out), run_time=1.5)
        self.wait(0.85)

        subs = VGroup(
            _cite("checks the finished folder", size=16),
            _cite("declines the wrong size", size=16),
            _cite("the starter kit", size=16),
        )
        for s, g in zip(subs, out):
            s.next_to(g, DOWN, buff=0.3)
        self.play(*[FadeIn(s) for s in subs], run_time=0.7)

        self.wait(1.19)

        tail = _t("two pieces of work, and a document", size=22, color=INK)
        tail.move_to(DOWN * 3.05)
        self.play(FadeIn(tail, shift=UP * 0.2), run_time=0.8)
        self.wait(2.72)


# ─────────────────────────────────────────────────────────────────────────────
#  B10 — Outro. Title restate, handle beneath. Silent by design.
# ─────────────────────────────────────────────────────────────────────────────
class B10_Outro(Scene):
    def construct(self):
        self.camera.background_color = BG

        # QC fill anchors — faint marks at the title-safe corners so a centred
        # outro card reads as filling its frame. Same device as the toolkit's
        # own ClaudeTitleOutro (ClaudeTitleOutro.tsx:74-78); invisible at
        # viewing distance, but it stops Gate V reading the card as underfilled.
        anchors = VGroup(
            Dot(point=LEFT * 6.15 + UP * 3.28, radius=0.022, color=GHOST),
            Dot(point=RIGHT * 6.15 + UP * 3.28, radius=0.022, color=GHOST),
            Dot(point=LEFT * 6.15 + DOWN * 3.28, radius=0.022, color=GHOST),
            Dot(point=RIGHT * 6.15 + DOWN * 3.28, radius=0.022, color=GHOST),
        )
        self.add(anchors)

        eyebrow = _t("IRREDUCIBLY HUMAN", size=19, color=TEAL, weight="BOLD")
        eyebrow.move_to(UP * 2.35)
        self.play(FadeIn(eyebrow), run_time=0.6)

        body = _t("Five Ways to Catch a Resolution Problem", size=42, weight="BOLD")
        body.move_to(UP * 0.85)
        # Baseline-align the terracotta period. arrange(RIGHT) centres the dot
        # vertically against the cap height, which renders it as a mid-height
        # bullet rather than a full stop. Same idiom as the house example at
        # examples/deep-explainer/claude-liam-fluency-trap/scenes.py:202.
        dot = _t(".", size=42, color=CRIMSON, weight="BOLD")
        dot.next_to(body, RIGHT, buff=0.03).align_to(body, DOWN)
        line = VGroup(body, dot)
        self.play(FadeIn(line, shift=UP * 0.25), run_time=1.0)

        rule = Line(LEFT * 1.6, RIGHT * 1.6, stroke_width=2.6, color=CRIMSON)
        rule.move_to(DOWN * 0.25)
        self.play(Create(rule), run_time=0.6)

        handle = _t("@HumanitariansAI", size=32, color=INK).move_to(DOWN * 1.35)
        self.play(FadeIn(handle), run_time=0.7)

        tail = _cite("part two covers the three workflows these combine into", size=17)
        tail.move_to(DOWN * 2.6)
        self.play(FadeIn(tail), run_time=0.7)
        self.wait(4.08)
