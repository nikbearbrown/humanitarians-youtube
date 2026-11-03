# -*- coding: utf-8 -*-
from manim import *

# 9:16 Portrait 4K Canvas
config.pixel_width = 2160
config.pixel_height = 3840
config.frame_rate = 24
config.frame_width = 9
config.frame_height = 16

BG = "#111111"
FG = "#F2EEE8"
ACCENT = "#C46F4B"
MUTED = "#777777"
GOOD = "#78A083"
BAD = "#B65C5C"
BLUE = "#5C8BB6"
BORDER = "#5D584F"


class BrutalistPortraitScene(Scene):

    def setup(self):
        self.camera.background_color = BG

    def heading(self, text):
        words = text.split()
        lines = []
        current = []
        for word in words:
            candidate = " ".join(current + [word])
            if len(candidate) > 20 and current:
                lines.append(" ".join(current))
                current = [word]
            else:
                current.append(word)
        if current:
            lines.append(" ".join(current))

        title = VGroup(*[
            Text(line, font="Georgia", font_size=36, color=FG, weight=BOLD)
            for line in lines
        ]).arrange(DOWN, buff=0.12)

        if title.width > 6.4:
            title.scale_to_fit_width(6.4)

        title.move_to(UP * 6.2)

        rule = Line(
            LEFT * 3.2,
            RIGHT * 3.2,
            color=ACCENT,
            stroke_width=4
        ).next_to(title, DOWN, buff=0.18)

        return VGroup(title, rule)

    def caption(self, text, color=MUTED):
        words = text.split()
        lines = []
        current = []
        for word in words:
            candidate = " ".join(current + [word])
            if len(candidate) > 22 and current:
                lines.append(" ".join(current))
                current = [word]
            else:
                current.append(word)
        if current:
            lines.append(" ".join(current))

        t = VGroup(*[
            Text(line, font="Georgia", font_size=32, color=color, weight=BOLD)
            for line in lines
        ]).arrange(DOWN, buff=0.10)

        if t.width > 6.4:
            t.scale_to_fit_width(6.4)

        t.move_to(DOWN * 5.2)
        return t

    def box(self, label, width=6.2, height=1.1, color=FG, border_color=BORDER, font_size=32, fill_color=BG, fill_opacity=0.9):
        rect = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.08,
            stroke_color=border_color,
            stroke_width=3,
            fill_color=fill_color,
            fill_opacity=fill_opacity
        )
        text = Text(label, font="Georgia", font_size=font_size, color=color, weight=BOLD)
        max_text_width = width - 0.4
        if text.width > max_text_width:
            text.scale_to_fit_width(max_text_width)
        text.move_to(rect)
        return VGroup(rect, text)

    def badge(self, label, color=GOOD, border_color=BORDER, font_size=32, width=2.4, height=0.75):
        rect = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.06,
            stroke_color=border_color,
            stroke_width=2,
            fill_color=BG,
            fill_opacity=0.9
        )
        text = Text(label, font="Georgia", font_size=font_size, color=color, weight=BOLD)
        if text.width > width - 0.25:
            text.scale_to_fit_width(width - 0.25)
        text.move_to(rect)
        return VGroup(rect, text)


# ============================================================
# B00 - FULL TABLE SCAN (PORTRAIT)
# ============================================================

class B00_FullTableScanBottleneck(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("UNINDEXED QUERIES FORCE FULL TABLE SCANS")

        q_box = self.box("QUERY: WHERE ID = 84920", width=6.2, height=0.9, color=ACCENT, font_size=30).move_to(UP * 4.6)

        b1 = self.box("PAGE 001 (MISS)", width=5.6, height=0.8, color=BAD, font_size=28).move_to(UP * 3.1)
        b2 = self.box("PAGE 002 (MISS)", width=5.6, height=0.8, color=BAD, font_size=28).move_to(UP * 2.0)
        b3 = self.box("PAGE 003 (MISS)", width=5.6, height=0.8, color=BAD, font_size=28).move_to(UP * 0.9)
        dots = Text("...", font="Georgia", font_size=36, color=MUTED, weight=BOLD).move_to(DOWN * 0.1)
        b_last = self.box("PAGE 500,000 (MISS)", width=5.6, height=0.8, color=BAD, font_size=28).move_to(DOWN * 1.1)

        blocks = VGroup(b1, b2, b3, dots, b_last)

        self.play(FadeIn(title), FadeIn(q_box), FadeIn(blocks), run_time=1.0)

        f1 = self.box("O(N) LINEAR SCAN TIME", width=6.2, height=0.8, color=BAD, font_size=28).move_to(DOWN * 2.4)
        f2 = self.box("STORAGE I/O BOTTLENECK", width=6.2, height=0.8, color=BAD, font_size=28).move_to(DOWN * 3.5)

        self.play(FadeIn(f1), FadeIn(f2), run_time=1.0)

        cap = self.caption("WITHOUT AN INDEX, THE ENGINE MUST SEQUENTIALLY READ EVERY SINGLE DISK BLOCK")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B01 - B-TREE INDEX STRUCTURE (PORTRAIT)
# ============================================================

class B01_BTreeIndexStructure(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("BALANCED B-TREE HIERARCHY")

        root = self.box("ROOT PAGE: [ 25 | 50 | 75 ]", width=6.2, height=0.9, color=ACCENT, font_size=28).move_to(UP * 4.5)

        br1 = self.box("BRANCH A: [ 10 | 20 ]", width=6.0, height=0.8, color=BLUE, font_size=28).move_to(UP * 3.0)
        br2 = self.box("BRANCH B: [ 35 | 45 ]", width=6.0, height=0.8, color=BLUE, font_size=28).move_to(UP * 1.9)
        br3 = self.box("BRANCH C: [ 60 | 70 ]", width=6.0, height=0.8, color=BLUE, font_size=28).move_to(UP * 0.8)

        lf1 = self.box("LEAF 1: ROWS 1..24", width=5.8, height=0.75, color=GOOD, font_size=28).move_to(DOWN * 0.4)
        lf2 = self.box("LEAF 2: ROWS 25..49", width=5.8, height=0.75, color=GOOD, font_size=28).move_to(DOWN * 1.4)
        lf3 = self.box("LEAF 3: ROWS 50..74", width=5.8, height=0.75, color=GOOD, font_size=28).move_to(DOWN * 2.4)

        tree = VGroup(root, br1, br2, br3, lf1, lf2, lf3)

        self.play(FadeIn(title), FadeIn(tree), run_time=1.2)

        badge = self.box("O(LOG N) SEARCH COMPLEXITY", width=6.2, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 3.6)
        self.play(FadeIn(badge), run_time=0.8)

        cap = self.caption("A B-TREE REPLACES LINEAR SCANS WITH A MULTI-LEVEL BALANCED SEARCH HIERARCHY")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B02 - FAST TREE TRAVERSAL (PORTRAIT)
# ============================================================

class B02_FastTreeTraversal(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("FAST TREE TRAVERSAL: 3 HOPS")

        target = self.box("LOOKUP: ID = 42", width=6.2, height=0.85, color=ACCENT, font_size=30).move_to(UP * 4.6)

        hop1 = self.box("HOP 1: ROOT (25 < 42 < 50)", width=6.0, height=0.85, color=FG, font_size=28).move_to(UP * 3.1)
        hop2 = self.box("HOP 2: BRANCH (35 < 42 < 45)", width=6.0, height=0.85, color=FG, font_size=28).move_to(UP * 1.4)
        hop3 = self.box("HOP 3: LEAF (ROW 42 FOUND)", width=6.0, height=0.85, color=GOOD, font_size=28).move_to(DOWN * 0.3)

        self.play(FadeIn(title), FadeIn(target), FadeIn(hop1), run_time=1.0)

        a1 = Arrow(hop1.get_bottom(), hop2.get_top(), buff=0.15, color=ACCENT, stroke_width=4)
        self.play(Create(a1), FadeIn(hop2), run_time=0.9)

        a2 = Arrow(hop2.get_bottom(), hop3.get_top(), buff=0.15, color=GOOD, stroke_width=4)
        self.play(Create(a2), FadeIn(hop3), run_time=0.9)

        stat = self.box("1,000,000 ROWS -> 3 DISK READS", width=6.2, height=0.9, color=GOOD, font_size=28).move_to(DOWN * 2.0)
        sub = self.box("QUERY TIME: 1.2 MILLISECONDS", width=6.2, height=0.8, color=FG, font_size=28).move_to(DOWN * 3.1)

        self.play(FadeIn(stat), FadeIn(sub), run_time=1.0)

        cap = self.caption("POINT LOOKUPS TRAVERSE FROM ROOT TO LEAF IN MILLISECONDS RATHER THAN SECONDS")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B03 - DOUBLY LINKED LEAVES (PORTRAIT)
# ============================================================

class B03_DoublyLinkedLeafChain(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("DOUBLY LINKED LEAF CHAIN")

        query = self.box("RANGE: WHERE ID BETWEEN 25 AND 70", width=6.2, height=0.85, color=ACCENT, font_size=28).move_to(UP * 4.6)

        p1 = self.box("LEAF A: KEYS 1..24", width=5.6, height=0.8, color=FG, font_size=28).move_to(UP * 3.1)
        p2 = self.box("LEAF B: KEYS 25..49 (MATCH)", width=5.6, height=0.8, color=GOOD, font_size=28).move_to(UP * 1.6)
        p3 = self.box("LEAF C: KEYS 50..74 (MATCH)", width=5.6, height=0.8, color=GOOD, font_size=28).move_to(UP * 0.1)
        p4 = self.box("LEAF D: KEYS 75..99", width=5.6, height=0.8, color=FG, font_size=28).move_to(DOWN * 1.4)

        self.play(FadeIn(title), FadeIn(query), FadeIn(p1), FadeIn(p2), FadeIn(p3), FadeIn(p4), run_time=1.0)

        a1 = DoubleArrow(p1.get_bottom(), p2.get_top(), buff=0.1, color=ACCENT, stroke_width=3)
        a2 = DoubleArrow(p2.get_bottom(), p3.get_top(), buff=0.1, color=GOOD, stroke_width=4)
        a3 = DoubleArrow(p3.get_bottom(), p4.get_top(), buff=0.1, color=ACCENT, stroke_width=3)
        self.play(Create(a1), Create(a2), Create(a3), run_time=1.0)

        badge = self.box("SEQUENTIAL HORIZONTAL SCAN", width=6.2, height=0.85, color=GOOD, font_size=28).move_to(DOWN * 2.8)
        self.play(FadeIn(badge), run_time=0.8)

        cap = self.caption("HORIZONTAL LEAF LINKS ENABLE FAST RANGE QUERIES WITHOUT RE-TRAVERSING THE TREE")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B04 - CLUSTERED VS SECONDARY (PORTRAIT)
# ============================================================

class B04_ClusteredVsSecondary(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("CLUSTERED VS SECONDARY INDEXES")

        c_tag = Text("CLUSTERED INDEX (PRIMARY KEY)", font="Georgia", font_size=28, color=ACCENT, weight=BOLD).move_to(UP * 4.6)
        c1 = self.box("PHYSICAL ROW ORDER ON DISK", width=6.0, height=0.75, color=FG, font_size=28).move_to(UP * 3.7)
        c2 = self.box("LEAF STORES COMPLETE ROW DATA", width=6.0, height=0.75, color=FG, font_size=28).move_to(UP * 2.7)
        c_badge = self.box("1 DIRECT DISK READ", width=6.0, height=0.75, color=GOOD, font_size=28).move_to(UP * 1.7)

        s_tag = Text("SECONDARY INDEX (E.G. EMAIL)", font="Georgia", font_size=28, color=BLUE, weight=BOLD).move_to(UP * 0.4)
        s1 = self.box("INDEXED COLUMN KEY + PK POINTER", width=6.0, height=0.75, color=FG, font_size=28).move_to(DOWN * 0.5)
        s2 = self.box("REQUIRES 2ND LOOKUP TO TABLE", width=6.0, height=0.75, color=FG, font_size=28).move_to(DOWN * 1.5)
        s_badge = self.box("2-STEP POINTER TRAVERSAL", width=6.0, height=0.75, color=BLUE, font_size=28).move_to(DOWN * 2.5)

        self.play(FadeIn(title), FadeIn(c_tag), FadeIn(c1), FadeIn(c2), FadeIn(c_badge), run_time=1.0)
        self.play(FadeIn(s_tag), FadeIn(s1), FadeIn(s2), FadeIn(s_badge), run_time=1.0)

        cap = self.caption("CLUSTERED INDEX ORDERS PHYSICAL DATA WHILE SECONDARY INDEXES POINT TO PRIMARY KEYS")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B05 - COMPOSITE INDEX PREFIX (PORTRAIT)
# ============================================================

class B05_CompositeIndexPrefix(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("LEFTMOST PREFIX RULE")

        idx_def = self.box("INDEX: (TENANT_ID, STATUS, CREATED)", width=6.4, height=0.85, color=ACCENT, font_size=28).move_to(UP * 4.6)

        c1 = self.box("WHERE TENANT_ID = 4 AND STATUS = 'OK'", width=6.4, height=0.75, color=FG, font_size=28).move_to(UP * 3.3)
        h1 = self.box("INDEX USED (PREFIX MATCH)", width=6.2, height=0.70, color=GOOD, font_size=28).move_to(UP * 2.4)

        c2 = self.box("WHERE TENANT_ID = 4", width=6.4, height=0.75, color=FG, font_size=28).move_to(UP * 1.3)
        h2 = self.box("INDEX USED (FIRST COLUMN)", width=6.2, height=0.70, color=GOOD, font_size=28).move_to(UP * 0.4)

        c3 = self.box("WHERE STATUS = 'OK'", width=6.4, height=0.75, color=FG, font_size=28).move_to(DOWN * 0.7)
        h3 = self.box("FULL SCAN (NO PREFIX)", width=6.2, height=0.70, color=BAD, font_size=28).move_to(DOWN * 1.6)

        self.play(FadeIn(title), FadeIn(idx_def), run_time=1.0)
        self.play(FadeIn(c1), FadeIn(h1), FadeIn(c2), FadeIn(h2), FadeIn(c3), FadeIn(h3), run_time=1.2)

        cap = self.caption("COMPOSITE INDEXES ONLY ACCELERATE QUERIES THAT FILTER BY THE FIRST COLUMN FIRST")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B06 - WRITE PENALTY (PORTRAIT)
# ============================================================

class B06_TheWriteTradeoff(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("THE WRITE PENALTY & TRADEOFF")

        r_tag = Text("READS: SUB-MILLISECOND LOOKUPS", font="Georgia", font_size=28, color=GOOD, weight=BOLD).move_to(UP * 4.6)
        r1 = self.box("O(LOG N) TRAVERSAL SPEED", width=6.0, height=0.75, color=FG, font_size=28).move_to(UP * 3.7)
        r2 = self.box("FAST POINT AND RANGE QUERIES", width=6.0, height=0.75, color=FG, font_size=28).move_to(UP * 2.7)

        w_tag = Text("WRITES: MAINTENANCE OVERHEAD", font="Georgia", font_size=28, color=BAD, weight=BOLD).move_to(UP * 1.4)
        w1 = self.box("PAGE SPLIT TREE REBALANCING", width=6.0, height=0.75, color=FG, font_size=28).move_to(UP * 0.5)
        w2 = self.box("INDEX LOCK CONTENTION", width=6.0, height=0.75, color=FG, font_size=28).move_to(DOWN * 0.5)
        w3 = self.box("STORAGE & MEMORY BLOAT", width=6.0, height=0.75, color=FG, font_size=28).move_to(DOWN * 1.5)

        self.play(FadeIn(title), FadeIn(r_tag), FadeIn(r1), FadeIn(r2), run_time=1.0)
        self.play(FadeIn(w_tag), FadeIn(w1), FadeIn(w2), FadeIn(w3), run_time=1.0)

        cap = self.caption("EVERY INDEX SPEEDS UP READS BUT ADDS MAINTENANCE OVERHEAD TO WRITES")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B07 - INDEXING STRATEGY PAYOFF (PORTRAIT)
# ============================================================

class B07_ArchitecturePayoff(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("DATABASE INDEXING STRATEGY")

        p1 = self.box("1. SELECTIVE INDEXING", width=6.2, height=0.70, color=FG, font_size=30).move_to(UP * 4.4)
        s1 = self.box("INDEX HIGH-CARDINALITY KEYS", width=6.2, height=0.60, color=MUTED, font_size=28).move_to(UP * 3.6)

        p2 = self.box("2. COVERING INDEXES", width=6.2, height=0.70, color=FG, font_size=30).move_to(UP * 2.7)
        s2 = self.box("SKIP TABLE HEAP LOOKUPS", width=6.2, height=0.60, color=MUTED, font_size=28).move_to(UP * 1.9)

        p3 = self.box("3. LEFTMOST ALIGNMENT", width=6.2, height=0.70, color=FG, font_size=30).move_to(UP * 1.0)
        s3 = self.box("ORDER BY FILTER FREQUENCY", width=6.2, height=0.60, color=MUTED, font_size=28).move_to(UP * 0.2)

        p4 = self.box("4. PRUNE REDUNDANT", width=6.2, height=0.70, color=FG, font_size=30).move_to(DOWN * 0.7)
        s4 = self.box("DROP UNUSED INDEXES", width=6.2, height=0.60, color=MUTED, font_size=28).move_to(DOWN * 1.5)

        pillars = VGroup(p1, s1, p2, s2, p3, s3, p4, s4)

        self.play(FadeIn(title), FadeIn(pillars), run_time=1.2)

        badge = self.box("SUB-MILLISECOND QUERIES AT SCALE", width=6.2, height=0.85, color=GOOD, font_size=30).move_to(DOWN * 2.6)
        self.play(FadeIn(badge), run_time=0.8)

        cap = self.caption("TARGETED INDEXING DELIVERS FAST QUERIES WHILE PRESERVING WRITE THROUGHPUT")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)
