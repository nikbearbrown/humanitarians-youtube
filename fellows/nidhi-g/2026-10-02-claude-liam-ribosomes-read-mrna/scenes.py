"""
Manim scenes for claude-liam-ribosomes-read-mrna  (body beats B02-B08)

One shared machine, drawn the same way in every beat:
  mRNA tape   5'-AUG GCU GGC UAA-3'  (Met-Ala-Gly-stop, standard genetic code)
  ribosome    large + small subunit, slots E | P | A left to right (A is on the 3' side)
  tRNA        body + anticodon (written 3'->5' so each letter sits over its codon partner)
              + amino-acid bead

Claude palette: cream ground, warm ink, terracotta as the one accent (shapes only -
terracotta never carries text, it fails AA contrast on cream).
Run times are fitted to the measured Kokoro audio (generated at --speed 1.1).
"""

import os

import numpy as np
from manim import *

try:  # make the bundled faces resolvable by Pango even if not installed system-wide
    import manimpango
    _home = os.environ.get("ART_HOME", "")
    for _rel in ("runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf",
                 "runtime/fonts/PT_Mono/PTMono-Regular.ttf"):
        _p = os.path.join(_home, _rel)
        if _home and os.path.isfile(_p):
            manimpango.register_font(_p)
except Exception:
    pass

PAGE = "#FAF9F5"
INK = "#3D3929"
INK_SOFT = "#73705F"
SPARK = "#D97757"
SERIF = "EB Garamond"
MONO = "PT Mono"

SEQ = "AUGGCUGGCUAA"
PAIR = {"A": "U", "U": "A", "G": "C", "C": "G"}

TAPE_Y = -1.2
STEP = 0.75                      # one nucleotide
CODON = 3 * STEP                 # one codon = one ribosome slot


def letter_x(j):
    return -3.3 + STEP * j


def codon_x(k):
    return letter_x(3 * k + 1)


def serif(s, size=36, color=INK):
    return Text(s, font=SERIF, font_size=size, color=color)


def mono(s, size=46, color=INK):
    return Text(s, font=MONO, font_size=size, color=color)


def spark_line(words):
    """The spark + one short serif line, top-left (SPARK-LINE LAW)."""
    c = np.array([-5.9, 3.0, 0])
    arms = VGroup(*[
        Line(c + 0.2 * np.array([np.cos(a), np.sin(a), 0]),
             c - 0.2 * np.array([np.cos(a), np.sin(a), 0]),
             color=SPARK, stroke_width=6)
        for a in (0, np.pi / 3, 2 * np.pi / 3)])
    label = serif(words, 40).next_to(arms, RIGHT, buff=0.3)
    return VGroup(arms, label)


def logo_bug():
    """NBB mark, small and low-opacity, lower-right inside title-safe (LOGO LAW)."""
    try:
        bug = SVGMobject("nbb-logo.svg")
        bug.set_fill(INK, opacity=0.4).set_stroke(width=0)
        bug.height = 0.5
    except Exception:
        bug = serif("@NikBearBrown", 24, INK_SOFT)
    return bug.move_to(np.array([5.75, -3.05, 0]))


def tape(seq=SEQ):
    letters = VGroup(*[mono(ch).move_to([letter_x(j), TAPE_Y, 0]) for j, ch in enumerate(seq)])
    backbone = Line([letter_x(0) - 0.4, TAPE_Y - 0.42, 0], [letter_x(11) + 0.4, TAPE_Y - 0.42, 0],
                    color=INK, stroke_width=4)
    five = serif("5'", 34, INK_SOFT).move_to([letter_x(0) - 0.85, TAPE_Y, 0])
    three = serif("3'", 34, INK_SOFT).move_to([letter_x(11) + 0.85, TAPE_Y, 0])
    return VGroup(backbone, letters, five, three)


def ribosome(p_k):
    """Ribosome with slot P over codon p_k."""
    cx = codon_x(p_k)
    large = RoundedRectangle(corner_radius=0.5, width=7.2, height=3.6)
    large.set_fill(INK, opacity=0.05).set_stroke(INK, width=3)
    large.move_to([cx, 0.85, 0])
    small = RoundedRectangle(corner_radius=0.4, width=6.0, height=1.05)
    small.set_fill(INK, opacity=0.05).set_stroke(INK, width=3)
    small.move_to([cx, -2.05, 0])
    slots, labels = VGroup(), VGroup()
    for name, dk in (("E", -1), ("P", 0), ("A", 1)):
        r = Rectangle(width=2.05, height=2.9).set_stroke(INK_SOFT, width=2)
        r.move_to([cx + dk * CODON, 0.5, 0])
        slots.add(r)
        labels.add(serif(name, 40).move_to([cx + dk * CODON, 2.25, 0]))
    return VGroup(large, small, slots, labels)


def bead(name, x, y=1.2, r=0.42):
    c = Circle(radius=r).set_fill(PAGE, opacity=1).set_stroke(INK, width=3)
    c.move_to([x, y, 0])
    return VGroup(c, serif(name, 28 if r >= 0.42 else 25).move_to(c))


def link(b1, b2, color=INK, width=6):
    """Bond drawn edge-to-edge between two beads, so it never crosses a label."""
    c1, c2 = np.array(b1[0].get_center(), dtype=float), np.array(b2[0].get_center(), dtype=float)
    u = (c2 - c1) / np.linalg.norm(c2 - c1)
    return Line(c1 + u * b1[0].width / 2, c2 - u * b2[0].width / 2, color=color, stroke_width=width)


def trna(anticodon, aa, k, empty=False):
    """tRNA standing over codon k: anticodon letters, body, optional amino-acid bead."""
    cx = codon_x(k)
    letters = VGroup(*[mono(ch, 44).move_to([cx + (i - 1) * STEP, -0.62, 0])
                       for i, ch in enumerate(anticodon)])
    body = RoundedRectangle(corner_radius=0.25, width=1.9, height=1.0)
    body.set_fill(PAGE, opacity=1).set_stroke(INK, width=3).move_to([cx, 0.2, 0])
    stem = Line([cx, 0.7, 0], [cx, 0.8, 0], color=INK, stroke_width=3)
    g = VGroup(letters, body, stem)
    if not empty:
        g.add(bead(aa, cx))
    return g


def pair_lines(k, wobble_last=False):
    """Short base-pair ticks between codon k and the anticodon above it."""
    out = VGroup()
    for i in range(3):
        x = letter_x(3 * k + i)
        top, bot = np.array([x, -0.85, 0]), np.array([x, -0.97, 0])
        if wobble_last and i == 2:
            out.add(ArcBetweenPoints(top + LEFT * 0.12, bot + RIGHT * 0.12, angle=PI / 2,
                                     color=SPARK, stroke_width=5))
        else:
            out.add(Line(top, bot, color=INK, stroke_width=5))
    return out


class B02_ThreeParts(Scene):
    """FRAMEWORK: tape, carrier, ribosome + slots, listed on screen in narration order (5.5 s)."""

    def construct(self):
        self.camera.background_color = PAGE
        self.add(logo_bug())
        self.play(FadeIn(spark_line("Three parts.")), run_time=0.3)

        t = tape()
        legend = VGroup(
            serif("1   mRNA — the tape", 32),
            serif("2   tRNA — the carrier", 32),
            serif("3   ribosome — E, P, A slots", 32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).move_to([3.75, 1.5, 0])

        self.play(Create(t[0]), FadeIn(t[1], lag_ratio=0.1), FadeIn(t[2:]),
                  FadeIn(legend[0]), run_time=1.1)

        carrier = trna("UAC", "Met", 0)
        carrier.shift(UP * 3)
        self.play(carrier.animate.shift(DOWN * 3), FadeIn(legend[1]), run_time=1.0)

        rib = ribosome(0)
        large, small, slots, labels = rib
        large.shift(UP * 4)
        small.shift(DOWN * 3)
        self.add(large, small)
        self.bring_to_back(large, small)
        self.play(large.animate.shift(DOWN * 4), small.animate.shift(UP * 3),
                  FadeIn(legend[2]), run_time=1.1)

        self.play(Create(slots), FadeIn(labels, lag_ratio=0.3),
                  slots[1].animate.set_stroke(SPARK, width=4), run_time=1.0)
        self.wait(1.1)


class B03_Codons(Scene):
    """Read in threes from the AUG start; AUG brings Met (4.9 s)."""

    def construct(self):
        self.camera.background_color = PAGE
        self.add(logo_bug())
        step = 0.9
        xs = [-4.95 + step * j for j in range(12)]
        letters = VGroup(*[mono(ch, 70).move_to([xs[j], -0.4, 0]) for j, ch in enumerate(SEQ)])
        five = serif("5'", 40, INK_SOFT).move_to([-5.75, -0.4, 0])
        three = serif("3'", 40, INK_SOFT).move_to([5.75, -0.4, 0])
        direction = Arrow([-4.8, -2.45, 0], [4.8, -2.45, 0], color=INK, stroke_width=4, buff=0)
        dir_label = serif("read this way", 34, INK_SOFT).next_to(direction, DOWN, buff=0.2)

        self.play(FadeIn(spark_line("Read in threes.")), FadeIn(letters, lag_ratio=0.05),
                  FadeIn(five), FadeIn(three), GrowArrow(direction), FadeIn(dir_label),
                  run_time=0.8)

        frame = SurroundingRectangle(letters[0:3], color=INK, buff=0.15, stroke_width=4)
        self.play(Create(frame), run_time=0.35)
        for k in range(1, 4):
            self.play(frame.animate.move_to(letters[3 * k:3 * k + 3]), run_time=0.4)
        start = SurroundingRectangle(letters[0:3], buff=0.15, stroke_width=4)
        start.set_stroke(SPARK).set_fill(SPARK, opacity=0.25)
        self.play(Transform(frame, start), run_time=0.5)

        tag = serif("start codon", 36).next_to(frame, DOWN, buff=0.25)
        met = bead("Met", xs[1], -0.4)
        self.add(met)
        self.bring_to_back(met)
        self.play(FadeIn(tag), met.animate.move_to([xs[1], 1.6, 0]), run_time=0.8)
        aa = serif("methionine — the first amino acid", 38).move_to([1.6, 1.6, 0])
        self.play(FadeIn(aa, shift=LEFT * 0.3), run_time=0.5)
        self.wait(1.0)


class B04_Decoding(Scene):
    """WORKED EXAMPLE: wrong anticodon rejected, matching one stays in slot A (4.6 s)."""

    def construct(self):
        self.camera.background_color = PAGE
        self.add(logo_bug())
        rib = ribosome(0)
        p_trna = trna("UAC", "Met", 0)
        self.add(rib, tape(), p_trna, spark_line("Fit decides."))
        note = serif("codon GCU in slot A", 34, INK_SOFT).move_to([codon_x(1), -3.05, 0])
        self.play(FadeIn(note), run_time=0.3)

        wrong = trna("UAC", "Met", 1).shift(UP * 3)
        self.play(wrong.animate.shift(DOWN * 3), run_time=0.7)
        crosses = VGroup(*[Cross(scale_factor=0.16, stroke_color=INK, stroke_width=5)
                           .move_to([letter_x(3 + i), -0.92, 0]) for i in range(3)])
        self.play(FadeIn(crosses), run_time=0.3)
        self.play(wrong.animate.shift(UP * 3.5).set_opacity(0), FadeOut(crosses), run_time=0.6)

        right = trna("CGA", "Ala", 1).shift(UP * 3)
        self.play(right.animate.shift(DOWN * 3), run_time=0.7)
        self.play(Create(pair_lines(1)), run_time=0.35)
        self.play(rib[2][2].animate.set_stroke(SPARK, width=6), run_time=0.4)
        self.wait(1.2)


class B05_PeptideBond(Scene):
    """Peptidyl transfer: Met moves onto Ala; catalyst is ribosomal RNA (4.3 s)."""

    def construct(self):
        self.camera.background_color = PAGE
        self.add(logo_bug())
        p_trna = trna("UAC", "Met", 0, empty=True)
        a_trna = trna("CGA", "Ala", 1)
        met = bead("Met", codon_x(0))
        self.add(ribosome(0), tape(), p_trna, a_trna, met, pair_lines(0), pair_lines(1))
        self.play(FadeIn(spark_line("RNA makes the bond.")), run_time=0.3)

        target = np.array([codon_x(1) - 0.9, 2.2, 0])
        self.play(met.animate.move_to(target), run_time=1.0)
        bond = link(met, a_trna[3], color=SPARK, width=8)
        self.play(Create(bond), run_time=0.4)

        label = serif("catalyst: ribosomal RNA,", 34).move_to([3.8, 2.45, 0])
        label2 = serif("not a protein", 34).next_to(label, DOWN, buff=0.2)
        pointer = Arrow(label2.get_left() + LEFT * 0.1, bond.get_center() + UP * 0.1,
                        color=INK, stroke_width=4, buff=0.15)
        self.play(FadeIn(label), FadeIn(label2), GrowArrow(pointer), run_time=0.7)
        self.wait(1.4)


class B06_Shift(Scene):
    """Translocation: ribosome moves one codon toward 3'; empty tRNA exits from E (4.6 s)."""

    def construct(self):
        self.camera.background_color = PAGE
        self.add(logo_bug())
        rib = ribosome(0)
        empty = trna("UAC", "", 0, empty=True)
        carrier = trna("CGA", "Ala", 1)
        met = bead("Met", codon_x(1) - 0.9, 2.2)
        bond = link(met, carrier[3])
        e_ticks = pair_lines(0)
        self.add(rib, tape(), empty, carrier, met, bond, e_ticks, pair_lines(1))
        self.play(FadeIn(spark_line("One codon on.")), run_time=0.3)

        move = Arrow([codon_x(0), 2.95, 0], [codon_x(1), 2.95, 0], color=INK,
                     stroke_width=5, buff=0)
        move_label = serif("one codon", 34, INK_SOFT).next_to(move, RIGHT, buff=0.25)
        self.play(rib.animate.shift(RIGHT * CODON), GrowArrow(move), FadeIn(move_label),
                  run_time=1.3)
        exit_note = serif("exits from E", 34, INK_SOFT).move_to([codon_x(0), -3.05, 0])
        self.play(FadeOut(empty, shift=UP * 2.2 + LEFT * 0.6), FadeOut(e_ticks),
                  FadeIn(exit_note), run_time=0.9)
        open_note = serif("slot A open over GGC", 34, INK_SOFT).move_to([codon_x(2), -3.05, 0])
        self.play(rib[2][2].animate.set_stroke(SPARK, width=6), FadeIn(open_note), run_time=0.5)
        self.play(Indicate(rib[2][2], color=SPARK, scale_factor=1.04), run_time=0.8)
        self.wait(0.8)


class B07_Wobble(Scene):
    """FALSIFIABILITY: one Gly tRNA reads GGC strictly and GGU by G-U wobble (4.8 s)."""

    def construct(self):
        self.camera.background_color = PAGE
        self.add(logo_bug())
        step = 0.95

        def codon(word, cx):
            return VGroup(*[mono(ch, 76).move_to([cx + (i - 1) * step, -1.6, 0])
                            for i, ch in enumerate(word)])

        left, right = codon("GGC", -3.3), codon("GGU", 3.3)
        third_bg = VGroup(*[
            RoundedRectangle(corner_radius=0.12, width=0.8, height=2.7)
            .set_fill(SPARK, opacity=0.22).set_stroke(width=0)
            .move_to([cx + step, -0.75, 0]) for cx in (-3.3, 3.3)])
        cap_l = serif("GGC", 34, INK_SOFT).next_to(left, DOWN, buff=0.35)
        cap_r = serif("GGU", 34, INK_SOFT).next_to(right, DOWN, buff=0.35)
        self.add(third_bg, left, right, cap_l, cap_r)
        self.play(FadeIn(spark_line("Loose at letter three.")), run_time=0.3)

        def adapter(cx):
            letters = VGroup(*[mono(ch, 60).move_to([cx + (i - 1) * step, 0.1, 0])
                               for i, ch in enumerate("CCG")])
            body = RoundedRectangle(corner_radius=0.25, width=2.6, height=1.1)
            body.set_fill(PAGE, opacity=1).set_stroke(INK, width=3).move_to([cx, 1.25, 0])
            return VGroup(letters, body, bead("Gly", cx, 2.45))

        def ticks(cx, wobble):
            out = VGroup()
            for i in range(3):
                x = cx + (i - 1) * step
                top, bot = np.array([x, -0.35, 0]), np.array([x, -1.0, 0])
                if wobble and i == 2:
                    out.add(ArcBetweenPoints(top, bot + RIGHT * 0.25, angle=-PI / 2,
                                             color=INK, stroke_width=6))
                else:
                    out.add(Line(top, bot, color=INK, stroke_width=6))
            return out

        g = adapter(-3.3).shift(UP * 2.5)
        self.play(g.animate.shift(DOWN * 2.5), run_time=0.7)
        strict = ticks(-3.3, wobble=False)
        self.play(Create(strict), run_time=0.4)
        self.wait(0.4)

        self.play(FadeOut(strict), g.animate.shift(RIGHT * 6.6), run_time=1.0)
        wob = ticks(3.3, wobble=True)
        wob_label = serif("wobble pair G·U", 36).move_to([3.3, -3.1, 0])
        self.play(Create(wob), FadeIn(wob_label), run_time=0.5)
        same = serif("same tRNA, both mean glycine", 40).move_to([-2.6, 2.45, 0])
        self.play(FadeIn(same, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(1.0)


class B08_Stop(Scene):
    """Termination: no tRNA for UAA; release factor docks; chain released (5.0 s)."""

    def construct(self):
        self.camera.background_color = PAGE
        self.add(logo_bug())
        rib = ribosome(2)
        p_trna = trna("CCG", "Gly", 2, empty=True)
        gly = bead("Gly", codon_x(2), 1.2)
        ala = bead("Ala", codon_x(2) - 0.9, 2.2)
        met = bead("Met", codon_x(2) - 1.75, 1.4)
        chain_bonds = VGroup(link(met, ala), link(ala, gly))
        self.add(rib, tape(), p_trna, chain_bonds, met, ala, gly, pair_lines(2))

        stops = VGroup(serif("stop codons", 40),
                       mono("UAA", 52), mono("UAG", 52), mono("UGA", 52))
        stops.arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([-4.9, 1.0, 0])
        self.play(FadeIn(spark_line("Stop codons.")), FadeIn(stops, lag_ratio=0.2), run_time=0.5)

        # a mismatched carrier tries UAA and is rejected (no tRNA pairs with a stop codon)
        probe = trna("CGA", "Ala", 3)
        crosses = VGroup(*[Cross(scale_factor=0.16, stroke_color=INK, stroke_width=5)
                           .move_to([letter_x(9 + i), -0.92, 0]) for i in range(3)])
        self.play(FadeIn(probe, shift=DOWN * 3), run_time=0.45)
        self.play(FadeIn(crosses), run_time=0.2)
        self.play(FadeOut(probe, shift=UP * 3), FadeOut(crosses), run_time=0.45)

        rf = RoundedRectangle(corner_radius=0.25, width=1.9, height=2.2)
        rf.set_fill(SPARK, opacity=0.3).set_stroke(INK, width=3)
        rf_label = VGroup(serif("release", 30), serif("factor", 30)).arrange(DOWN, buff=0.08)
        rf_group = VGroup(rf, rf_label.move_to(rf)).move_to([codon_x(3), 0.45, 0])
        self.play(FadeIn(rf_group, shift=DOWN * 3), run_time=0.8)

        chain = VGroup(met, ala, gly, chain_bonds)
        r_met, r_ala, r_gly = (bead(n, x, 3.0, r=0.36) for n, x in (("Met", 2.9), ("Ala", 3.8), ("Gly", 4.7)))
        released = VGroup(r_met, r_ala, r_gly, VGroup(link(r_met, r_ala), link(r_ala, r_gly)))
        free = serif("chain released", 36).move_to([codon_x(2), -3.05, 0])
        self.play(Transform(chain, released), FadeIn(free), run_time=1.0)
        self.wait(1.3)
