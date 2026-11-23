# -*- coding: utf-8 -*-
from manim import *
import numpy as np

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
            Text(line, font="Georgia", font_size=34, color=FG, weight=BOLD)
            for line in lines
        ]).arrange(DOWN, buff=0.10)

        if title.width > 6.2:
            title.scale_to_fit_width(6.2)

        title.move_to(UP * 6.2)

        rule = Line(
            LEFT * 3.1,
            RIGHT * 3.1,
            color=ACCENT,
            stroke_width=4
        ).next_to(title, DOWN, buff=0.16)

        return VGroup(title, rule)

    def caption(self, text, color=MUTED):
        words = text.split()
        lines = []
        current = []
        for word in words:
            candidate = " ".join(current + [word])
            if len(candidate) > 28 and current:
                lines.append(" ".join(current))
                current = [word]
            else:
                current.append(word)
        if current:
            lines.append(" ".join(current))

        t = VGroup(*[
            Text(line, font="Georgia", font_size=28, color=color, weight=BOLD)
            for line in lines
        ]).arrange(DOWN, buff=0.08)

        if t.width > 6.2:
            t.scale_to_fit_width(6.2)
        t.move_to(DOWN * 4.5)
        return t

    def box(self, label, width=5.6, height=0.88, color=FG, border_color=BORDER, font_size=26, fill_color=BG, fill_opacity=0.9):
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

    def badge(self, label, color=GOOD, border_color=BORDER, font_size=26, width=5.6, height=0.68, fill_color=BG, fill_opacity=0.9):
        rect = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.06,
            stroke_color=border_color,
            stroke_width=2,
            fill_color=fill_color,
            fill_opacity=fill_opacity
        )
        text = Text(label, font="Georgia", font_size=font_size, color=color, weight=BOLD)
        if text.width > width - 0.25:
            text.scale_to_fit_width(width - 0.25)
        text.move_to(rect)
        return VGroup(rect, text)


# ============================================================
# Beat B00: Monolithic Database Bottleneck (12.69s)
# ============================================================
class B00_MonolithicDatabaseBottleneck(BrutalistPortraitScene):
    def construct(self):
        hdr = self.heading("MONOLITHIC DB\nBOTTLENECK")
        cap = self.caption("Single-node architectures collapse when traffic exceeds vertical hardware limits", color=BAD)
        self.add(hdr, cap)

        client_box = self.box("APPLICATION TRAFFIC (500k QPS)", width=6.2, height=0.9, color=BLUE, font_size=24).move_to(UP * 4.2)

        arrow_down = Arrow(client_box.get_bottom(), UP * 2.8, color=BAD, stroke_width=4, buff=0.15)

        db_card = RoundedRectangle(
            width=6.2, height=4.8, corner_radius=0.12,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(DOWN * 0.1)
        db_title = Text("MONOLITHIC DATABASE", font="Georgia", font_size=26, color=ACCENT, weight=BOLD).next_to(db_card.get_top(), DOWN, buff=0.25)

        m1 = self.badge("CPU: 99% (SATURATED)", color=BAD, font_size=24, width=5.4, height=0.65).move_to(db_card.get_center() + UP * 1.0)
        m2 = self.badge("DISK IOPS: 100% QUEUE", color=BAD, font_size=24, width=5.4, height=0.65).move_to(db_card.get_center() + UP * 0.2)
        m3 = self.badge("MEMORY: 98% THRASHING", color=BAD, font_size=24, width=5.4, height=0.65).move_to(db_card.get_center() - UP * 0.6)
        limit_lbl = Text("HARD PHYSICAL CEILING", font="Georgia", font_size=24, color=MUTED, weight=BOLD).next_to(db_card.get_bottom(), UP, buff=0.25)

        self.play(FadeIn(client_box), FadeIn(db_card), FadeIn(db_title), FadeIn(VGroup(m1, m2, m3)), FadeIn(limit_lbl))
        self.wait(3.5)
        self.play(GrowArrow(arrow_down))
        self.wait(8.0)


# ============================================================
# Beat B01: Horizontal Sharding Architecture (13.48s)
# ============================================================
class B01_HorizontalShardingArchitecture(BrutalistPortraitScene):
    def construct(self):
        hdr = self.heading("HORIZONTAL SHARDING\nARCHITECTURE")
        cap = self.caption("Data splits horizontally across independent nodes with dedicated resources", color=GOOD)
        self.add(hdr, cap)

        top_bar = self.box("ORIGINAL MONOLITHIC DATASET", width=6.2, height=0.85, color=FG, font_size=24).move_to(UP * 4.4)
        down_arrow = Arrow(top_bar.get_bottom(), UP * 3.3, color=ACCENT, stroke_width=4, buff=0.12)
        part_tag = self.badge("ROW-BY-ROW HORIZONTAL SPLIT", color=ACCENT, font_size=24, width=5.8, height=0.55).move_to(UP * 3.3)

        s0 = self.box("SHARD 0: ROWS 1 - 250M", width=6.0, height=0.8, color=BLUE, font_size=24).move_to(UP * 2.1)
        s1 = self.box("SHARD 1: ROWS 251M - 500M", width=6.0, height=0.8, color=GOOD, font_size=24).move_to(UP * 0.9)
        s2 = self.box("SHARD 2: ROWS 501M - 750M", width=6.0, height=0.8, color=ACCENT, font_size=24).move_to(DOWN * 0.3)
        s3 = self.box("SHARD 3: ROWS 751M - 1B", width=6.0, height=0.8, color=BLUE, font_size=24).move_to(DOWN * 1.5)

        note = self.badge("DEDICATED CPU · RAM · DISK", color=MUTED, font_size=24, width=6.0, height=0.6).move_to(DOWN * 2.7)

        self.play(FadeIn(top_bar))
        self.wait(3.0)
        self.play(GrowArrow(down_arrow), FadeIn(part_tag))
        self.wait(1.5)
        self.play(FadeIn(VGroup(s0, s1, s2, s3)), FadeIn(note))
        self.wait(8.0)


# ============================================================
# Beat B02: Shard Key Selection (11.33s)
# ============================================================
class B02_ShardKeySelection(BrutalistPortraitScene):
    def construct(self):
        hdr = self.heading("SHARD KEY SELECTION")
        cap = self.caption("The shard key determines deterministic placement across the cluster", color=GOOD)
        self.add(hdr, cap)

        top_card = RoundedRectangle(
            width=6.2, height=3.0, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(UP * 2.6)
        t_title = Text("TABLE: ACCOUNTS", font="Georgia", font_size=24, color=FG, weight=BOLD).next_to(top_card.get_top(), DOWN, buff=0.18)
        r1 = self.box("id: BIGINT", width=5.6, height=0.58, font_size=24, color=MUTED).move_to(top_card.get_center() + UP * 0.45)
        r2 = self.box("user_id: UUID [SHARD KEY]", width=5.6, height=0.62, font_size=24, color=ACCENT, border_color=ACCENT).move_to(top_card.get_center() - UP * 0.25)
        r3 = self.box("email: VARCHAR", width=5.6, height=0.58, font_size=24, color=MUTED).move_to(top_card.get_center() - UP * 0.95)

        arrow = Arrow(top_card.get_bottom(), UP * 0.6, color=ACCENT, stroke_width=4, buff=0.15)

        bot_card = RoundedRectangle(
            width=6.2, height=3.2, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(DOWN * 1.3)
        b_title = Text("KEY REQUIREMENTS", font="Georgia", font_size=24, color=ACCENT, weight=BOLD).next_to(bot_card.get_top(), DOWN, buff=0.18)
        k1 = self.badge("HIGH CARDINALITY: Millions of keys", color=GOOD, font_size=24, width=5.6, height=0.6).move_to(bot_card.get_center() + UP * 0.45)
        k2 = self.badge("UNIFORM FREQUENCY: Avoid hotspots", color=BLUE, font_size=24, width=5.6, height=0.6).move_to(bot_card.get_center() - UP * 0.25)
        k3 = self.badge("IMMUTABLE: Values never change", color=ACCENT, font_size=24, width=5.6, height=0.6).move_to(bot_card.get_center() - UP * 0.95)

        self.play(FadeIn(top_card), FadeIn(t_title), FadeIn(VGroup(r1, r2, r3)))
        self.wait(3.5)
        self.play(GrowArrow(arrow), FadeIn(bot_card), FadeIn(b_title), FadeIn(VGroup(k1, k2, k3)))
        self.wait(7.0)


# ============================================================
# Beat B03: Range vs Hash Partitioning (13.76s)
# ============================================================
class B03_RangeVsHashPartitioning(BrutalistPortraitScene):
    def construct(self):
        hdr = self.heading("RANGE VS HASH\nPARTITIONING")
        cap = self.caption("Range scans need sequential keys; hash partitioning balances writes", color=FG)
        self.add(hdr, cap)

        # Card 1: Range
        c1 = RoundedRectangle(
            width=6.2, height=2.5, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(UP * 2.4)
        c1_t = Text("1. RANGE PARTITIONING", font="Georgia", font_size=26, color=BLUE, weight=BOLD).next_to(c1.get_top(), DOWN, buff=0.18)
        rg_pro = self.badge("PRO: Fast Range Queries", color=GOOD, font_size=26, width=5.6, height=0.6).next_to(c1_t, DOWN, buff=0.2)
        rg_con = self.badge("CON: Sequential Hotspot Risk", color=BAD, font_size=26, width=5.6, height=0.6).next_to(rg_pro, DOWN, buff=0.18)

        # Card 2: Hash
        c2 = RoundedRectangle(
            width=6.2, height=2.5, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(DOWN * 0.7)
        c2_t = Text("2. HASH PARTITIONING", font="Georgia", font_size=26, color=ACCENT, weight=BOLD).next_to(c2.get_top(), DOWN, buff=0.18)
        hs_pro = self.badge("PRO: Balanced Write Traffic", color=GOOD, font_size=26, width=5.6, height=0.6).next_to(c2_t, DOWN, buff=0.2)
        hs_con = self.badge("CON: Range Queries Scatter", color=BAD, font_size=26, width=5.6, height=0.6).next_to(hs_pro, DOWN, buff=0.18)

        self.play(FadeIn(c1), FadeIn(c1_t), FadeIn(VGroup(rg_pro, rg_con)))
        self.wait(5.0)
        self.play(FadeIn(c2), FadeIn(c2_t), FadeIn(VGroup(hs_pro, hs_con)))
        self.wait(7.5)


# ============================================================
# Beat B04: Query Routing Layer (12.69s)
# ============================================================
class B04_QueryRoutingCoordinator(BrutalistPortraitScene):
    def construct(self):
        hdr = self.heading("QUERY ROUTING LAYER")
        cap = self.caption("Targeted queries hit single shards with single-millisecond latency", color=GOOD)
        self.add(hdr, cap)

        # Top: App Query
        app = self.box("QUERY: WHERE user_id = 42", width=6.2, height=0.8, color=BLUE, font_size=24).move_to(UP * 4.3)

        arrow1 = Arrow(app.get_bottom(), UP * 2.9, color=BLUE, stroke_width=4, buff=0.12)

        # Middle: Router
        router = RoundedRectangle(
            width=6.2, height=1.7, corner_radius=0.1,
            stroke_color=ACCENT, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(UP * 1.7)
        r_title = Text("QUERY ROUTER", font="Georgia", font_size=24, color=ACCENT, weight=BOLD).next_to(router.get_top(), DOWN, buff=0.18)
        r_eval = Text("hash(42) % 3 = 1 -> SHARD 1", font="Georgia", font_size=24, color=GOOD).next_to(r_title, DOWN, buff=0.2)

        arrow2 = Arrow(router.get_bottom(), DOWN * 0.2, color=GOOD, stroke_width=5, buff=0.12)

        # Bottom: Shards
        s0 = self.box("SHARD 0 (IDLE)", width=5.8, height=0.7, color=MUTED, font_size=24).move_to(DOWN * 0.4)
        s1 = self.box("SHARD 1 (TARGET MATCH)", width=5.8, height=0.75, color=GOOD, border_color=GOOD, font_size=24).move_to(DOWN * 1.4)
        s2 = self.box("SHARD 2 (IDLE)", width=5.8, height=0.7, color=MUTED, font_size=24).move_to(DOWN * 2.4)

        self.play(FadeIn(app))
        self.wait(2.5)
        self.play(GrowArrow(arrow1), FadeIn(router), FadeIn(r_title), FadeIn(r_eval))
        self.wait(3.0)
        self.play(GrowArrow(arrow2), FadeIn(VGroup(s0, s1, s2)))
        self.wait(6.0)


# ============================================================
# Beat B05: Cross-Shard Scatter-Gather (12.84s)
# ============================================================
class B05_CrossShardScatterGather(BrutalistPortraitScene):
    def construct(self):
        hdr = self.heading("CROSS-SHARD\nSCATTER-GATHER")
        cap = self.caption("Queries lacking shard keys fan out across all nodes, multiplying network latency", color=BAD)
        self.add(hdr, cap)

        q_box = self.box("NON-KEY QUERY: WHERE email = '...'", width=6.2, height=0.85, color=BAD, font_size=24).move_to(UP * 4.3)
        a_in = Arrow(q_box.get_bottom(), UP * 3.1, color=BAD, stroke_width=4, buff=0.12)

        coord = RoundedRectangle(
            width=6.2, height=1.65, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(UP * 2.0)
        c_title = Text("COORDINATOR (BROADCAST)", font="Georgia", font_size=24, color=FG, weight=BOLD).next_to(coord.get_top(), DOWN, buff=0.18)
        c_desc = Text("Scatter query to all 3 Shards", font="Georgia", font_size=24, color=ACCENT).next_to(c_title, DOWN, buff=0.18)

        # 3 Shards below
        sh0 = self.box("SHARD 0: Scan local partition", width=5.8, height=0.72, color=FG, font_size=24).move_to(UP * 0.4)
        sh1 = self.box("SHARD 1: Scan local partition", width=5.8, height=0.72, color=FG, font_size=24).move_to(DOWN * 0.45)
        sh2 = self.box("SHARD 2: Scan local partition", width=5.8, height=0.72, color=FG, font_size=24).move_to(DOWN * 1.3)

        penalty = self.badge("GATHER: Bound by slowest shard", color=BAD, font_size=24, width=6.0, height=0.68).move_to(DOWN * 2.4)

        self.play(FadeIn(q_box), FadeIn(coord), FadeIn(c_title), FadeIn(c_desc))
        self.wait(3.0)
        self.play(GrowArrow(a_in))
        self.wait(1.5)
        self.play(FadeIn(VGroup(sh0, sh1, sh2)), FadeIn(penalty))
        self.wait(7.0)


# ============================================================
# Beat B06: Shard Splitting & Rebalancing (13.46s)
# ============================================================
class B06_ShardSplittingRebalance(BrutalistPortraitScene):
    def construct(self):
        hdr = self.heading("LIVE SHARD SPLITTING\n& REBALANCING")
        cap = self.caption("Partitions split and migrate without stopping live database writes", color=GOOD)
        self.add(hdr, cap)

        # Overloaded shard
        hot = RoundedRectangle(
            width=6.2, height=1.65, corner_radius=0.1,
            stroke_color=BAD, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(UP * 3.4)
        hot_t = Text("HOT SHARD 2 (95% IOPS)", font="Georgia", font_size=26, color=BAD, weight=BOLD).next_to(hot.get_top(), DOWN, buff=0.18)
        hot_k = Text("250M Rows at Threshold", font="Georgia", font_size=26, color=FG).next_to(hot_t, DOWN, buff=0.16)

        split_arr = Arrow(hot.get_bottom(), UP * 1.8, color=ACCENT, stroke_width=4, buff=0.12)

        # 2 New split shards
        s2a = RoundedRectangle(
            width=6.2, height=1.6, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(UP * 0.8)
        s2a_t = Text("NEW SHARD 2A: 0x00-0x7F", font="Georgia", font_size=26, color=ACCENT, weight=BOLD).next_to(s2a.get_top(), DOWN, buff=0.16)
        s2a_b = self.badge("50% Load | Replicated Live", color=GOOD, font_size=26, width=5.6, height=0.58).next_to(s2a_t, DOWN, buff=0.16)

        s2b = RoundedRectangle(
            width=6.2, height=1.6, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(DOWN * 1.2)
        s2b_t = Text("NEW SHARD 2B: 0x80-0xFF", font="Georgia", font_size=26, color=GOOD, weight=BOLD).next_to(s2b.get_top(), DOWN, buff=0.16)
        s2b_b = self.badge("50% Load | Live Cutover", color=GOOD, font_size=26, width=5.6, height=0.58).next_to(s2b_t, DOWN, buff=0.16)

        self.play(FadeIn(hot), FadeIn(hot_t), FadeIn(hot_k))
        self.wait(4.0)
        self.play(GrowArrow(split_arr))
        self.wait(1.5)
        self.play(FadeIn(s2a), FadeIn(s2a_t), FadeIn(s2a_b),
                  FadeIn(s2b), FadeIn(s2b_t), FadeIn(s2b_b))
        self.wait(6.5)


# ============================================================
# Beat B07: High Availability Sharded Topology (12.54s)
# ============================================================
class B07_HighAvailabilityShardedTopology(BrutalistPortraitScene):
    def construct(self):
        hdr = self.heading("PRODUCTION SHARDED\nTOPOLOGY")
        cap = self.caption("Production sharding pairs horizontal scale with full primary-replica fault tolerance", color=GOOD)
        self.add(hdr, cap)

        # Router
        router = self.box("QUERY ROUTER CLUSTER (STATELESS)", width=6.2, height=0.8, color=BLUE, font_size=24).move_to(UP * 4.3)

        arrow_top = Arrow(router.get_bottom(), UP * 3.3, color=ACCENT, stroke_width=4, buff=0.12)

        # 3 Shard Groups
        s1 = RoundedRectangle(width=6.2, height=1.2, corner_radius=0.08, stroke_color=BORDER, stroke_width=2, fill_color=BG, fill_opacity=0.95).move_to(UP * 2.3)
        s1_t = Text("SHARD 1: Primary + 2 Replicas", font="Georgia", font_size=24, color=ACCENT, weight=BOLD).move_to(s1)

        s2 = RoundedRectangle(width=6.2, height=1.2, corner_radius=0.08, stroke_color=BORDER, stroke_width=2, fill_color=BG, fill_opacity=0.95).move_to(UP * 0.8)
        s2_t = Text("SHARD 2: Primary + 2 Replicas", font="Georgia", font_size=24, color=ACCENT, weight=BOLD).move_to(s2)

        s3 = RoundedRectangle(width=6.2, height=1.2, corner_radius=0.08, stroke_color=BORDER, stroke_width=2, fill_color=BG, fill_opacity=0.95).move_to(DOWN * 0.7)
        s3_t = Text("SHARD 3: Primary + 2 Replicas", font="Georgia", font_size=24, color=ACCENT, weight=BOLD).move_to(s3)

        summary = self.badge("INFINITE SCALE · ZERO SPOFs", color=GOOD, font_size=24, width=6.2, height=0.68).move_to(DOWN * 2.1)

        self.play(FadeIn(router))
        self.wait(2.5)
        self.play(GrowArrow(arrow_top), FadeIn(VGroup(s1, s1_t, s2, s2_t, s3, s3_t)))
        self.wait(3.5)
        self.play(FadeIn(summary))
        self.wait(5.5)
