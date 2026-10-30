# -*- coding: utf-8 -*-
from manim import *

# 16:9 Landscape 4K Canvas
config.pixel_width = 3840
config.pixel_height = 2160
config.frame_rate = 24
config.frame_width = 16
config.frame_height = 9

BG = "#111111"
FG = "#F2EEE8"
ACCENT = "#C46F4B"
MUTED = "#777777"
GOOD = "#78A083"
BAD = "#B65C5C"
BLUE = "#5C8BB6"
BORDER = "#5D584F"


class BrutalistScene(Scene):

    def setup(self):
        self.camera.background_color = BG

    def heading(self, text):
        words = text.split()
        lines = []
        current = []
        for word in words:
            candidate = " ".join(current + [word])
            if len(candidate) > 34 and current:
                lines.append(" ".join(current))
                current = [word]
            else:
                current.append(word)
        if current:
            lines.append(" ".join(current))

        title = VGroup(*[
            Text(line, font="Georgia", font_size=34, color=FG, weight=BOLD)
            for line in lines
        ]).arrange(DOWN, buff=0.10)

        if title.width > 12.4:
            title.scale_to_fit_width(12.4)

        title.move_to(UP * 3.55)

        rule = Line(
            LEFT * 6.2,
            RIGHT * 6.2,
            color=ACCENT,
            stroke_width=5
        ).next_to(title, DOWN, buff=0.16)

        return VGroup(title, rule)

    def caption(self, text, color=MUTED):
        t = Text(text, font="Georgia", font_size=32, color=color, weight=BOLD)
        if t.width > 12.4:
            t.scale_to_fit_width(12.4)
        t.move_to(DOWN * 3.45)
        return t

    def box(self, label, width=2.8, height=1.1, color=FG, border_color=BORDER, font_size=26, fill_color=BG, fill_opacity=0.9):
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
        max_text_width = width - 0.35
        if text.width > max_text_width:
            text.scale_to_fit_width(max_text_width)
        text.move_to(rect)
        return VGroup(rect, text)

    def badge(self, label, color=GOOD, border_color=BORDER, font_size=26, width=2.6, height=0.68):
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
# B00 - FULL TABLE SCAN BOTTLENECK
# ============================================================

class B00_FullTableScanBottleneck(BrutalistScene):

    def construct(self):
        title = self.heading("UNINDEXED QUERIES FORCE FULL TABLE SCANS")

        # Query card
        query_box = self.box("QUERY: SELECT * FROM USERS WHERE ID = 84920", width=8.6, height=0.9, color=ACCENT, font_size=28).move_to(UP * 2.2)

        # Disk blocks row
        b1 = self.box("PAGE 001", width=1.8, height=1.2, color=BAD, font_size=26).move_to(LEFT * 4.5 + DOWN * 0.1)
        b2 = self.box("PAGE 002", width=1.8, height=1.2, color=BAD, font_size=26).move_to(LEFT * 2.25 + DOWN * 0.1)
        b3 = self.box("PAGE 003", width=1.8, height=1.2, color=BAD, font_size=26).move_to(ORIGIN + DOWN * 0.1)
        b_dots = Text("...", font="Georgia", font_size=36, color=MUTED, weight=BOLD).move_to(RIGHT * 1.8 + DOWN * 0.1)
        b_last = self.box("PAGE 500K", width=2.2, height=1.2, color=BAD, font_size=26).move_to(RIGHT * 4.0 + DOWN * 0.1)

        blocks = VGroup(b1, b2, b3, b_dots, b_last)

        self.play(FadeIn(title), FadeIn(query_box), FadeIn(blocks), run_time=1.0)

        # Scan arrow indicating linear disk read
        scan_arrow = Arrow(b1.get_top() + UP * 0.6, b_last.get_top() + UP * 0.6, buff=0.1, color=BAD, stroke_width=5)
        scan_label = Text("SEQUENTIAL DISK READ PASS", font="Georgia", font_size=26, color=BAD, weight=BOLD).next_to(scan_arrow, UP, buff=0.15)
        self.play(Create(scan_arrow), FadeIn(scan_label), run_time=1.2)

        # Flaw badges
        b_cost = self.badge("O(N) LINEAR COMPLEXITY", color=BAD, font_size=26, width=3.4, height=0.68).move_to(LEFT * 3.6 + DOWN * 1.8)
        b_io = self.badge("HIGH DISK I/O LATENCY", color=BAD, font_size=26, width=3.4, height=0.68).move_to(RIGHT * 3.6 + DOWN * 1.8)
        self.play(FadeIn(b_cost), FadeIn(b_io), run_time=1.0)

        cap = self.caption("WITHOUT AN INDEX, THE ENGINE MUST SEQUENTIALLY READ EVERY SINGLE DISK BLOCK")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B01 - THE SOLUTION: B-TREE INDEX HIERARCHY
# ============================================================

class B01_BTreeIndexStructure(BrutalistScene):

    def construct(self):
        title = self.heading("THE SOLUTION: BALANCED B-TREE HIERARCHY")

        # Root Node
        root = self.box("ROOT: [ 25 | 50 | 75 ]", width=4.2, height=0.9, color=ACCENT, font_size=26).move_to(UP * 2.2)

        # Branch Nodes
        br1 = self.box("BRANCH: [ 10 | 20 ]", width=3.2, height=0.85, color=BLUE, font_size=26).move_to(LEFT * 4.2 + UP * 0.7)
        br2 = self.box("BRANCH: [ 35 | 45 ]", width=3.2, height=0.85, color=BLUE, font_size=26).move_to(ORIGIN + UP * 0.7)
        br3 = self.box("BRANCH: [ 60 | 70 ]", width=3.2, height=0.85, color=BLUE, font_size=26).move_to(RIGHT * 4.2 + UP * 0.7)
        branches = VGroup(br1, br2, br3)

        # Leaf Nodes
        lf1 = self.box("LEAF: 1..24", width=2.4, height=0.8, color=GOOD, font_size=26).move_to(LEFT * 4.5 + DOWN * 0.8)
        lf2 = self.box("LEAF: 25..49", width=2.4, height=0.8, color=GOOD, font_size=26).move_to(LEFT * 1.5 + DOWN * 0.8)
        lf3 = self.box("LEAF: 50..74", width=2.4, height=0.8, color=GOOD, font_size=26).move_to(RIGHT * 1.5 + DOWN * 0.8)
        lf4 = self.box("LEAF: 75..99", width=2.4, height=0.8, color=GOOD, font_size=26).move_to(RIGHT * 4.5 + DOWN * 0.8)
        leaves = VGroup(lf1, lf2, lf3, lf4)

        self.play(FadeIn(title), FadeIn(root), FadeIn(branches), FadeIn(leaves), run_time=1.0)

        # Connection lines
        c1 = Line(root.get_bottom(), br1.get_top(), color=BORDER, stroke_width=3)
        c2 = Line(root.get_bottom(), br2.get_top(), color=BORDER, stroke_width=3)
        c3 = Line(root.get_bottom(), br3.get_top(), color=BORDER, stroke_width=3)
        self.play(Create(c1), Create(c2), Create(c3), run_time=1.0)

        # Feature badges
        badge1 = self.badge("O(LOG N) SEARCH TIME", color=GOOD, font_size=26, width=3.2, height=0.68).move_to(LEFT * 3.6 + DOWN * 2.0)
        badge2 = self.badge("BALANCED TREE FANOUT", color=GOOD, font_size=26, width=3.2, height=0.68).move_to(RIGHT * 3.6 + DOWN * 2.0)
        self.play(FadeIn(badge1), FadeIn(badge2), run_time=1.0)

        cap = self.caption("A B-TREE REPLACES LINEAR SCANS WITH A MULTI-LEVEL BALANCED SEARCH HIERARCHY")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B02 - FAST TREE TRAVERSAL: 3 TO 4 HOPS
# ============================================================

class B02_FastTreeTraversal(BrutalistScene):

    def construct(self):
        title = self.heading("FAST TREE TRAVERSAL: 3 TO 4 DISK HOPS")

        # Search Query Target
        target = self.box("LOOKUP: ID = 42", width=3.6, height=0.85, color=ACCENT, font_size=28).move_to(UP * 2.2)

        # Traversal Nodes
        hop1 = self.box("HOP 1: ROOT PAGE (25 < 42 < 50)", width=5.2, height=0.85, color=FG, font_size=26).move_to(UP * 0.9)
        hop2 = self.box("HOP 2: BRANCH PAGE (35 < 42 < 45)", width=5.2, height=0.85, color=FG, font_size=26).move_to(DOWN * 0.3)
        hop3 = self.box("HOP 3: LEAF PAGE (FOUND ROW ID 42)", width=5.2, height=0.85, color=GOOD, font_size=26).move_to(DOWN * 1.5)

        self.play(FadeIn(title), FadeIn(target), FadeIn(hop1), run_time=1.0)

        arr1 = Arrow(hop1.get_bottom(), hop2.get_top(), buff=0.12, color=ACCENT, stroke_width=4)
        self.play(Create(arr1), FadeIn(hop2), run_time=1.0)

        arr2 = Arrow(hop2.get_bottom(), hop3.get_top(), buff=0.12, color=GOOD, stroke_width=4)
        self.play(Create(arr2), FadeIn(hop3), run_time=1.0)

        # Performance summary pill
        pill = self.badge("1,000,000 ROWS -> ONLY 3 DISK READS", color=GOOD, font_size=26, width=5.4, height=0.72).move_to(DOWN * 2.45)
        self.play(FadeIn(pill), run_time=0.8)

        cap = self.caption("POINT LOOKUPS TRAVERSE FROM ROOT TO LEAF IN MILLISECONDS RATHER THAN SECONDS")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B03 - DOUBLY LINKED LEAVES POWER RANGE SCANS
# ============================================================

class B03_DoublyLinkedLeafChain(BrutalistScene):

    def construct(self):
        title = self.heading("DOUBLY LINKED LEAVES POWER RANGE SCANS")

        # Range Query
        query = self.box("RANGE QUERY: WHERE ID BETWEEN 25 AND 70", width=7.2, height=0.85, color=ACCENT, font_size=28).move_to(UP * 2.2)

        # Linked Leaf Pages
        p1 = self.box("LEAF A: 1..24", width=2.4, height=1.1, color=FG, font_size=26).move_to(LEFT * 4.2 + DOWN * 0.1)
        p2 = self.box("LEAF B: 25..49", width=2.4, height=1.1, color=GOOD, font_size=26).move_to(LEFT * 1.4 + DOWN * 0.1)
        p3 = self.box("LEAF C: 50..74", width=2.4, height=1.1, color=GOOD, font_size=26).move_to(RIGHT * 1.4 + DOWN * 0.1)
        p4 = self.box("LEAF D: 75..99", width=2.4, height=1.1, color=FG, font_size=26).move_to(RIGHT * 4.2 + DOWN * 0.1)

        self.play(FadeIn(title), FadeIn(query), FadeIn(p1), FadeIn(p2), FadeIn(p3), FadeIn(p4), run_time=1.0)

        # Bidirectional arrows connecting leaves
        l1 = DoubleArrow(p1.get_right(), p2.get_left(), buff=0.1, color=ACCENT, stroke_width=3)
        l2 = DoubleArrow(p2.get_right(), p3.get_left(), buff=0.1, color=GOOD, stroke_width=4)
        l3 = DoubleArrow(p3.get_right(), p4.get_left(), buff=0.1, color=ACCENT, stroke_width=3)
        self.play(Create(l1), Create(l2), Create(l3), run_time=1.0)

        # Scan path bracket / badge
        scan_badge = self.badge("SEQUENTIAL LEAF SCAN (NO TREE RE-TRAVERSAL)", color=GOOD, font_size=26, width=6.2, height=0.72).move_to(DOWN * 1.6)
        self.play(FadeIn(scan_badge), run_time=0.8)

        cap = self.caption("HORIZONTAL LEAF LINKS ENABLE FAST RANGE QUERIES WITHOUT RE-TRAVERSING THE TREE")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B04 - CLUSTERED VS SECONDARY INDEXES
# ============================================================

class B04_ClusteredVsSecondary(BrutalistScene):

    def construct(self):
        title = self.heading("CLUSTERED VS SECONDARY INDEXES")

        # Column 1: Clustered Index
        c_title = Text("CLUSTERED INDEX (PRIMARY KEY)", font="Georgia", font_size=26, color=ACCENT, weight=BOLD).move_to(LEFT * 3.6 + UP * 2.0)
        c_box1 = self.box("PHYSICAL ROW ORDER", width=4.6, height=0.85, color=FG, font_size=26).move_to(LEFT * 3.6 + UP * 1.0)
        c_box2 = self.box("TABLE DATA STORED IN LEAVES", width=4.6, height=0.85, color=FG, font_size=26).move_to(LEFT * 3.6 + DOWN * 0.1)
        c_badge = self.badge("1 DIRECT DISK LOOKUP", color=GOOD, font_size=26, width=4.0, height=0.70).move_to(LEFT * 3.6 + DOWN * 1.3)
        col1 = VGroup(c_title, c_box1, c_box2, c_badge)

        # Column 2: Secondary Index
        s_title = Text("SECONDARY INDEX (E.G. EMAIL)", font="Georgia", font_size=26, color=BLUE, weight=BOLD).move_to(RIGHT * 3.6 + UP * 2.0)
        s_box1 = self.box("INDEXED COLUMN VALUE", width=4.6, height=0.85, color=FG, font_size=26).move_to(RIGHT * 3.6 + UP * 1.0)
        s_box2 = self.box("POINTS TO PRIMARY KEY ID", width=4.6, height=0.85, color=FG, font_size=26).move_to(RIGHT * 3.6 + DOWN * 0.1)
        s_badge = self.badge("2-STEP LOOKUP TRAVERSAL", color=BLUE, font_size=26, width=4.0, height=0.70).move_to(RIGHT * 3.6 + DOWN * 1.3)
        col2 = VGroup(s_title, s_box1, s_box2, s_badge)

        # Divider line
        div = Line(UP * 2.2, DOWN * 1.8, color=BORDER, stroke_width=3)

        self.play(FadeIn(title), FadeIn(col1), FadeIn(col2), Create(div), run_time=1.2)

        cap = self.caption("CLUSTERED INDEX ORDERS PHYSICAL DATA WHILE SECONDARY INDEXES POINT TO PRIMARY KEYS")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B05 - COMPOSITE INDEXES & LEFTMOST PREFIX RULE
# ============================================================

class B05_CompositeIndexPrefix(BrutalistScene):

    def construct(self):
        title = self.heading("COMPOSITE INDEXES & LEFTMOST PREFIX RULE")

        # Composite Index Definition
        def_box = self.box("INDEX DEFINITION: ( TENANT_ID, STATUS, CREATED_AT )", width=9.2, height=0.85, color=ACCENT, font_size=26).move_to(UP * 2.1)

        # Case 1: Valid Prefix Match
        case1 = self.box("WHERE TENANT_ID = 4 AND STATUS = 'ACTIVE'", width=6.8, height=0.8, color=FG, font_size=26).move_to(LEFT * 1.0 + UP * 0.9)
        hit1 = self.badge("INDEX USED", color=GOOD, font_size=26, width=2.4, height=0.7).move_to(RIGHT * 4.4 + UP * 0.9)

        # Case 2: Leftmost Column Only
        case2 = self.box("WHERE TENANT_ID = 4", width=6.8, height=0.8, color=FG, font_size=26).move_to(LEFT * 1.0 + DOWN * 0.2)
        hit2 = self.badge("INDEX USED", color=GOOD, font_size=26, width=2.4, height=0.7).move_to(RIGHT * 4.4 + DOWN * 0.2)

        # Case 3: Missing Leftmost Column
        case3 = self.box("WHERE STATUS = 'ACTIVE'", width=6.8, height=0.8, color=FG, font_size=26).move_to(LEFT * 1.0 + DOWN * 1.3)
        miss = self.badge("FULL SCAN", color=BAD, font_size=26, width=2.4, height=0.7).move_to(RIGHT * 4.4 + DOWN * 1.3)

        self.play(FadeIn(title), FadeIn(def_box), run_time=1.0)
        self.play(FadeIn(case1), FadeIn(hit1), FadeIn(case2), FadeIn(hit2), FadeIn(case3), FadeIn(miss), run_time=1.2)

        cap = self.caption("COMPOSITE INDEXES ONLY ACCELERATE QUERIES THAT FILTER BY THE FIRST COLUMN FIRST")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B06 - THE WRITE PENALTY & TREE REBALANCING
# ============================================================

class B06_TheWriteTradeoff(BrutalistScene):

    def construct(self):
        title = self.heading("THE WRITE PENALTY & TREE REBALANCING")

        # Left Card: Read Acceleration
        r_head = Text("READ OPERATIONS", font="Georgia", font_size=26, color=GOOD, weight=BOLD).move_to(LEFT * 3.6 + UP * 1.9)
        r_box1 = self.box("INSTANT B-TREE TRAVERSAL", width=4.6, height=0.85, color=FG, font_size=26).move_to(LEFT * 3.6 + UP * 0.9)
        r_box2 = self.box("O(LOG N) POINT LOOKUP", width=4.6, height=0.85, color=FG, font_size=26).move_to(LEFT * 3.6 + DOWN * 0.2)
        r_badge = self.badge("ACCELERATED READS", color=GOOD, font_size=26, width=4.0, height=0.70).move_to(LEFT * 3.6 + DOWN * 1.4)
        reads = VGroup(r_head, r_box1, r_box2, r_badge)

        # Right Card: Write Penalty
        w_head = Text("WRITE OPERATIONS", font="Georgia", font_size=26, color=BAD, weight=BOLD).move_to(RIGHT * 3.6 + UP * 1.9)
        w_box1 = self.box("INSERT / UPDATE / DELETE", width=4.6, height=0.85, color=FG, font_size=26).move_to(RIGHT * 3.6 + UP * 0.9)
        w_box2 = self.box("PAGE SPLIT REBALANCING", width=4.6, height=0.85, color=FG, font_size=26).move_to(RIGHT * 3.6 + DOWN * 0.2)
        w_badge = self.badge("WRITE OVERHEAD & LOCKS", color=BAD, font_size=26, width=4.0, height=0.70).move_to(RIGHT * 3.6 + DOWN * 1.4)
        writes = VGroup(w_head, w_box1, w_box2, w_badge)

        div = Line(UP * 2.2, DOWN * 1.9, color=BORDER, stroke_width=3)

        self.play(FadeIn(title), FadeIn(reads), FadeIn(writes), Create(div), run_time=1.2)

        cap = self.caption("EVERY INDEX SPEEDS UP READS BUT ADDS MAINTENANCE OVERHEAD TO WRITES")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B07 - PRODUCTION DATABASE INDEXING STRATEGY
# ============================================================

class B07_ArchitecturePayoff(BrutalistScene):

    def construct(self):
        title = self.heading("PRODUCTION DATABASE INDEXING STRATEGY")

        p1 = self.box("1. SELECTIVE INDEXING\nIndex high-cardinality search columns", width=5.6, height=1.1, color=FG, font_size=26).move_to(LEFT * 3.2 + UP * 1.2)
        p2 = self.box("2. COVERING INDEXES\nInclude all query columns to skip heap", width=5.6, height=1.1, color=FG, font_size=26).move_to(RIGHT * 3.2 + UP * 1.2)
        p3 = self.box("3. LEFTMOST ALIGNMENT\nOrder multi-columns by query frequency", width=5.6, height=1.1, color=FG, font_size=26).move_to(LEFT * 3.2 + DOWN * 0.4)
        p4 = self.box("4. PRUNE REDUNDANT\nDrop unused indexes to protect writes", width=5.6, height=1.1, color=FG, font_size=26).move_to(RIGHT * 3.2 + DOWN * 0.4)

        pillars = VGroup(p1, p2, p3, p4)

        self.play(FadeIn(title), FadeIn(pillars), run_time=1.2)

        summary = self.badge("SUB-MILLISECOND QUERIES WITH BALANCED WRITE PERFORMANCE", color=GOOD, font_size=26, width=8.2, height=0.72).move_to(DOWN * 1.8)
        self.play(FadeIn(summary), run_time=0.8)

        cap = self.caption("TARGETED INDEXING DELIVERS FAST QUERIES WHILE PRESERVING WRITE THROUGHPUT")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)
