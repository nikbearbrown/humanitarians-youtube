# -*- coding: utf-8 -*-
from manim import *
import numpy as np

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
            if len(candidate) > 36 and current:
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
        t = Text(text, font="Georgia", font_size=30, color=color, weight=BOLD)
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

    def badge(self, label, color=GOOD, border_color=BORDER, font_size=24, width=3.4, height=0.68, fill_color=BG, fill_opacity=0.9):
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
class B00_MonolithicDatabaseBottleneck(BrutalistScene):
    def construct(self):
        hdr = self.heading("MONOLITHIC DATABASE BOTTLENECK")
        cap = self.caption("Single-node architectures collapse when traffic exceeds vertical hardware limits", color=BAD)
        self.add(hdr, cap)

        # Monolith DB Center Box
        db_card = RoundedRectangle(
            width=6.4, height=4.4, corner_radius=0.12,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(RIGHT * 2.8 + DOWN * 0.1)
        db_title = Text("MONOLITHIC PRIMARY DATABASE", font="Georgia", font_size=26, color=ACCENT, weight=BOLD).next_to(db_card.get_top(), DOWN, buff=0.25)

        # Bottleneck metric cards inside monolith
        m1 = self.badge("CPU UTILIZATION: 99% (SATURATED)", color=BAD, font_size=22, width=5.6, height=0.62).move_to(db_card.get_center() + UP * 0.8)
        m2 = self.badge("DISK IOPS: 100% (QUEUE OVERFLOW)", color=BAD, font_size=22, width=5.6, height=0.62).move_to(db_card.get_center() + UP * 0.0)
        m3 = self.badge("BUFFER POOL: 98% (CACHE THRASHING)", color=BAD, font_size=22, width=5.6, height=0.62).move_to(db_card.get_center() + DOWN * 0.8)
        limit_lbl = Text("PHYSICAL VERTICAL CEILING", font="Georgia", font_size=22, color=MUTED, weight=BOLD).next_to(db_card.get_bottom(), UP, buff=0.22)

        # Left side: Application cluster
        client_box = self.box("APPLICATION\nCLUSTER", width=2.8, height=2.6, color=BLUE, font_size=24).move_to(LEFT * 5.6 + DOWN * 0.1)
        
        # Inbound traffic badges placed cleanly above respective arrows (zero arrow obstruction)
        q1 = self.badge("500k QPS TRAFFIC", color=ACCENT, font_size=20, width=2.6, height=0.46).move_to(LEFT * 2.3 + UP * 1.36)
        q2 = self.badge("WRITE LOCKS", color=BAD, font_size=20, width=2.6, height=0.46).move_to(LEFT * 2.3 + UP * 0.26)
        q3 = self.badge("INDEX STALLS", color=BAD, font_size=20, width=2.6, height=0.46).move_to(LEFT * 2.3 + DOWN * 0.84)

        # Three distinct, unobstructed inbound traffic arrows
        a1 = Arrow(LEFT * 4.2 + UP * 0.95, LEFT * 0.4 + UP * 0.95, color=ACCENT, stroke_width=4, buff=0.08)
        a2 = Arrow(LEFT * 4.2 + DOWN * 0.15, LEFT * 0.4 + DOWN * 0.15, color=BAD, stroke_width=4, buff=0.08)
        a3 = Arrow(LEFT * 4.2 + DOWN * 1.25, LEFT * 0.4 + DOWN * 1.25, color=BAD, stroke_width=4, buff=0.08)

        self.play(FadeIn(client_box), FadeIn(db_card), FadeIn(db_title), FadeIn(VGroup(m1, m2, m3)), FadeIn(limit_lbl))
        self.wait(3.5)
        self.play(GrowArrow(a1), GrowArrow(a2), GrowArrow(a3), FadeIn(q1), FadeIn(q2), FadeIn(q3))
        self.wait(7.19)


# ============================================================
# Beat B01: Horizontal Sharding Architecture (13.48s)
# ============================================================
class B01_HorizontalShardingArchitecture(BrutalistScene):
    def construct(self):
        hdr = self.heading("HORIZONTAL SHARDING ARCHITECTURE")
        cap = self.caption("Data splits horizontally across independent nodes with dedicated resources", color=GOOD)
        self.add(hdr, cap)

        # Top banner: Original dataset
        top_bar = RoundedRectangle(
            width=11.2, height=1.0, corner_radius=0.08,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9
        ).move_to(UP * 2.1)
        top_txt = Text("TOTAL DATASET (BILLIONS OF ROWS)", font="Georgia", font_size=26, color=FG, weight=BOLD).move_to(top_bar)
        
        # Horizontal Partition Arrow
        down_arrow = Arrow(UP * 1.5, UP * 0.75, color=ACCENT, stroke_width=5, buff=0.1)
        part_tag = self.badge("ROW-BY-ROW HORIZONTAL PARTITIONING", color=ACCENT, font_size=20, width=5.6, height=0.55).move_to(UP * 1.1)

        # 4 Independent Shards
        shards = VGroup()
        shard_data = [
            ("SHARD 0", "Rows 1 - 250M", BLUE, LEFT * 4.65),
            ("SHARD 1", "Rows 251M - 500M", GOOD, LEFT * 1.55),
            ("SHARD 2", "Rows 501M - 750M", ACCENT, RIGHT * 1.55),
            ("SHARD 3", "Rows 751M - 1B", BLUE, RIGHT * 4.65),
        ]

        for title, rows, col, pos in shard_data:
            card = RoundedRectangle(
                width=2.85, height=2.6, corner_radius=0.1,
                stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9
            ).move_to(pos + DOWN * 0.95)
            s_title = Text(title, font="Georgia", font_size=24, color=col, weight=BOLD).next_to(card.get_top(), DOWN, buff=0.2)
            s_rows = Text(rows, font="Georgia", font_size=20, color=FG).next_to(s_title, DOWN, buff=0.2)
            s_res = self.badge("DEDICATED\nCPU / RAM / DISK", color=MUTED, font_size=18, width=2.45, height=0.75).next_to(s_rows, DOWN, buff=0.2)
            shards.add(VGroup(card, s_title, s_rows, s_res))

        self.play(FadeIn(top_bar), FadeIn(top_txt))
        self.wait(3.0)
        self.play(GrowArrow(down_arrow), FadeIn(part_tag))
        self.wait(1.5)
        self.play(FadeIn(shards))
        self.wait(8.0)


# ============================================================
# Beat B02: Shard Key Selection (11.33s)
# ============================================================
class B02_ShardKeySelection(BrutalistScene):
    def construct(self):
        hdr = self.heading("SHARD KEY SELECTION")
        cap = self.caption("The shard key determines deterministic placement across the cluster", color=GOOD)
        self.add(hdr, cap)

        # Left Card: Schema Table
        schema_card = RoundedRectangle(
            width=5.6, height=4.2, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(LEFT * 3.4 + DOWN * 0.2)
        schema_title = Text("TABLE: ACCOUNTS", font="Georgia", font_size=26, color=FG, weight=BOLD).next_to(schema_card.get_top(), DOWN, buff=0.25)

        r1 = self.box("id: BIGINT (Primary Key)", width=5.0, height=0.55, font_size=22, color=MUTED).move_to(schema_card.get_center() + UP * 0.8)
        r2 = self.box("user_id: UUID [SHARD KEY]", width=5.0, height=0.65, font_size=22, color=ACCENT, border_color=ACCENT).move_to(schema_card.get_center() + UP * 0.05)
        r3 = self.box("email: VARCHAR(255)", width=5.0, height=0.55, font_size=22, color=MUTED).move_to(schema_card.get_center() - UP * 0.65)
        r4 = self.box("created_at: TIMESTAMP", width=5.0, height=0.55, font_size=22, color=MUTED).move_to(schema_card.get_center() - UP * 1.35)

        # Right Card: Shard Key Requirements
        req_card = RoundedRectangle(
            width=5.6, height=4.2, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(RIGHT * 3.4 + DOWN * 0.2)
        req_title = Text("SHARD KEY CRITERIA", font="Georgia", font_size=26, color=ACCENT, weight=BOLD).next_to(req_card.get_top(), DOWN, buff=0.25)

        k1 = self.badge("HIGH CARDINALITY\nMillions of distinct values", color=GOOD, font_size=20, width=5.0, height=0.8).move_to(req_card.get_center() + UP * 0.7)
        k2 = self.badge("UNIFORM FREQUENCY\nPrevents celebrity hotspots", color=BLUE, font_size=20, width=5.0, height=0.8).move_to(req_card.get_center() - UP * 0.2)
        k3 = self.badge("IMMUTABLE VALUE\nKey value must never mutate", color=ACCENT, font_size=20, width=5.0, height=0.8).move_to(req_card.get_center() - UP * 1.1)

        arrow_connect = Arrow(r2.get_right(), req_card.get_left(), color=ACCENT, stroke_width=4, buff=0.2)

        self.play(FadeIn(schema_card), FadeIn(schema_title), FadeIn(VGroup(r1, r2, r3, r4)))
        self.wait(3.5)
        self.play(GrowArrow(arrow_connect), FadeIn(req_card), FadeIn(req_title), FadeIn(VGroup(k1, k2, k3)))
        self.wait(7.0)


# ============================================================
# Beat B03: Range vs Hash Partitioning (13.76s)
# ============================================================
class B03_RangeVsHashPartitioning(BrutalistScene):
    def construct(self):
        hdr = self.heading("RANGE VS HASH PARTITIONING")
        cap = self.caption("Range partitioning optimizes sequential scans; hash partitioning guarantees balance", color=FG)
        self.add(hdr, cap)

        # Left Card: Range Partitioning
        left_card = RoundedRectangle(
            width=5.8, height=4.4, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(LEFT * 3.3 + DOWN * 0.2)
        left_title = Text("RANGE PARTITIONING", font="Georgia", font_size=26, color=BLUE, weight=BOLD).next_to(left_card.get_top(), DOWN, buff=0.25)
        left_sub = Text("Contiguous key ranges", font="Georgia", font_size=20, color=MUTED).next_to(left_title, DOWN, buff=0.12)

        rg1 = self.box("Shard 1: User IDs 1 - 1,000,000", width=5.2, height=0.55, font_size=20, color=FG).move_to(left_card.get_center() + UP * 0.4)
        rg2 = self.box("Shard 2: User IDs 1,000,001 - 2M", width=5.2, height=0.55, font_size=20, color=FG).move_to(left_card.get_center() - UP * 0.25)
        rg_pro = self.badge("PRO: Fast Range Scans (BETWEEN)", color=GOOD, font_size=19, width=5.2, height=0.55).move_to(left_card.get_center() - UP * 0.95)
        rg_con = self.badge("CON: Hotspots on Sequential IDs", color=BAD, font_size=19, width=5.2, height=0.55).move_to(left_card.get_center() - UP * 1.6)

        # Right Card: Hash Partitioning
        right_card = RoundedRectangle(
            width=5.8, height=4.4, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(RIGHT * 3.3 + DOWN * 0.2)
        right_title = Text("HASH PARTITIONING", font="Georgia", font_size=26, color=ACCENT, weight=BOLD).next_to(right_card.get_top(), DOWN, buff=0.25)
        right_sub = Text("hash(shard_key) % N", font="Georgia", font_size=20, color=MUTED).next_to(right_title, DOWN, buff=0.12)

        hs1 = self.box("Uniform pseudo-random scatter", width=5.2, height=0.55, font_size=20, color=FG).move_to(right_card.get_center() + UP * 0.4)
        hs2 = self.box("Even traffic distribution across all nodes", width=5.2, height=0.55, font_size=20, color=FG).move_to(right_card.get_center() - UP * 0.25)
        hs_pro = self.badge("PRO: Zero Write Hotspots", color=GOOD, font_size=19, width=5.2, height=0.55).move_to(right_card.get_center() - UP * 0.95)
        hs_con = self.badge("CON: Range Queries Require Scatter", color=BAD, font_size=19, width=5.2, height=0.55).move_to(right_card.get_center() - UP * 1.6)

        self.play(FadeIn(left_card), FadeIn(left_title), FadeIn(left_sub), FadeIn(VGroup(rg1, rg2, rg_pro, rg_con)))
        self.wait(5.0)
        self.play(FadeIn(right_card), FadeIn(right_title), FadeIn(right_sub), FadeIn(VGroup(hs1, hs2, hs_pro, hs_con)))
        self.wait(7.5)


# ============================================================
# Beat B04: Query Routing Layer (12.69s)
# ============================================================
class B04_QueryRoutingCoordinator(BrutalistScene):
    def construct(self):
        hdr = self.heading("QUERY ROUTING LAYER")
        cap = self.caption("Targeted queries hit single shards with single-millisecond latency", color=GOOD)
        self.add(hdr, cap)

        # Left: Application Query Box
        app_box = self.box("APPLICATION\nCLIENT", width=2.8, height=1.5, color=BLUE, font_size=24).move_to(LEFT * 5.0 + UP * 0.0)
        q_text = self.badge("SELECT * WHERE\nuser_id = 42", color=FG, font_size=19, width=2.8, height=0.75).next_to(app_box, DOWN, buff=0.35)

        # Middle: Query Coordinator / Router
        router_card = RoundedRectangle(
            width=3.6, height=3.6, corner_radius=0.1,
            stroke_color=ACCENT, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(LEFT * 0.2 + UP * 0.0)
        r_title = Text("QUERY ROUTER\n(COORDINATOR)", font="Georgia", font_size=24, color=ACCENT, weight=BOLD).next_to(router_card.get_top(), DOWN, buff=0.25)
        r_eval = Text("hash(42) % 3 = 1", font="Georgia", font_size=22, color=FG).next_to(r_title, DOWN, buff=0.35)
        r_target = self.badge("ROUTE -> SHARD 1", color=GOOD, font_size=20, width=3.0, height=0.6).next_to(r_eval, DOWN, buff=0.35)

        # Right: 3 Shards
        s0 = self.box("SHARD 0 (IDLE)", width=3.0, height=0.9, color=MUTED, font_size=22).move_to(RIGHT * 4.6 + UP * 1.4)
        s1 = self.box("SHARD 1 (TARGET)", width=3.0, height=0.9, color=GOOD, border_color=GOOD, font_size=22).move_to(RIGHT * 4.6 + UP * 0.0)
        s2 = self.box("SHARD 2 (IDLE)", width=3.0, height=0.9, color=MUTED, font_size=22).move_to(RIGHT * 4.6 - UP * 1.4)

        # Arrows
        arrow_to_router = Arrow(app_box.get_right(), router_card.get_left(), color=BLUE, stroke_width=4, buff=0.15)
        arrow_to_shard = Arrow(router_card.get_right(), s1.get_left(), color=GOOD, stroke_width=5, buff=0.15)

        self.play(FadeIn(app_box), FadeIn(q_text))
        self.wait(2.5)
        self.play(GrowArrow(arrow_to_router), FadeIn(router_card), FadeIn(r_title), FadeIn(r_eval), FadeIn(r_target))
        self.wait(3.0)
        self.play(GrowArrow(arrow_to_shard), FadeIn(s0), FadeIn(s1), FadeIn(s2))
        self.wait(6.0)


# ============================================================
# Beat B05: Cross-Shard Scatter-Gather (12.84s)
# ============================================================
class B05_CrossShardScatterGather(BrutalistScene):
    def construct(self):
        hdr = self.heading("CROSS-SHARD SCATTER-GATHER")
        cap = self.caption("Queries lacking shard keys fan out across all nodes, multiplying network latency", color=BAD)
        self.add(hdr, cap)

        # Left query without shard key
        q_box = self.box("NON-KEY QUERY\nWHERE email = '...' ", width=3.2, height=1.4, color=BAD, font_size=22).move_to(LEFT * 5.0 + UP * 0.0)

        # Coordinator
        coord_card = RoundedRectangle(
            width=3.6, height=3.6, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(LEFT * 0.6 + UP * 0.0)
        c_title = Text("COORDINATOR", font="Georgia", font_size=26, color=FG, weight=BOLD).next_to(coord_card.get_top(), DOWN, buff=0.25)
        c_step1 = Text("1. Scatter to All Shards", font="Georgia", font_size=20, color=ACCENT).next_to(c_title, DOWN, buff=0.3)
        c_step2 = Text("2. Parallel Execution", font="Georgia", font_size=20, color=BLUE).next_to(c_step1, DOWN, buff=0.2)
        c_step3 = Text("3. In-Memory Sort & Merge", font="Georgia", font_size=20, color=BAD).next_to(c_step2, DOWN, buff=0.2)

        # Right 3 Shards
        sh0 = self.box("SHARD 0\nPartial Result 1", width=3.0, height=0.95, color=FG, font_size=20).move_to(RIGHT * 4.4 + UP * 1.45)
        sh1 = self.box("SHARD 1\nPartial Result 2", width=3.0, height=0.95, color=FG, font_size=20).move_to(RIGHT * 4.4 + UP * 0.0)
        sh2 = self.box("SHARD 2\nPartial Result 3", width=3.0, height=0.95, color=FG, font_size=20).move_to(RIGHT * 4.4 - UP * 1.45)

        # Fan-out scatter arrows
        a_in = Arrow(q_box.get_right(), coord_card.get_left(), color=BAD, stroke_width=4, buff=0.15)
        a_out0 = Arrow(coord_card.get_right() + UP * 0.7, sh0.get_left(), color=ACCENT, stroke_width=4, buff=0.15)
        a_out1 = Arrow(coord_card.get_right(), sh1.get_left(), color=ACCENT, stroke_width=4, buff=0.15)
        a_out2 = Arrow(coord_card.get_right() - UP * 0.7, sh2.get_left(), color=ACCENT, stroke_width=4, buff=0.15)

        self.play(FadeIn(q_box), FadeIn(coord_card), FadeIn(c_title), FadeIn(VGroup(c_step1, c_step2, c_step3)))
        self.wait(3.0)
        self.play(GrowArrow(a_in))
        self.wait(1.5)
        self.play(GrowArrow(a_out0), GrowArrow(a_out1), GrowArrow(a_out2), FadeIn(VGroup(sh0, sh1, sh2)))
        self.wait(7.0)


# ============================================================
# Beat B06: Shard Splitting & Rebalancing (13.46s)
# ============================================================
class B06_ShardSplittingRebalance(BrutalistScene):
    def construct(self):
        hdr = self.heading("LIVE SHARD SPLITTING & REBALANCING")
        cap = self.caption("Partitions split and migrate without stopping live database writes", color=GOOD)
        self.add(hdr, cap)

        # Top: Overloaded Hot Shard
        hot_shard = RoundedRectangle(
            width=5.6, height=1.35, corner_radius=0.1,
            stroke_color=BAD, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(UP * 1.6)
        hot_title = Text("SHARD 2 (HOTSPOT: 95% DISK / CPU)", font="Georgia", font_size=24, color=BAD, weight=BOLD).next_to(hot_shard.get_top(), DOWN, buff=0.2)
        hot_keys = Text("Key Space: 0x5000 - 0x7FFF (250 Million Rows)", font="Georgia", font_size=20, color=FG).next_to(hot_title, DOWN, buff=0.15)

        # Splitting Arrows
        arr_left = Arrow(hot_shard.get_bottom() + LEFT * 1.4, LEFT * 3.4 + UP * 0.1, color=ACCENT, stroke_width=4, buff=0.15)
        arr_right = Arrow(hot_shard.get_bottom() + RIGHT * 1.4, RIGHT * 3.4 + UP * 0.1, color=GOOD, stroke_width=4, buff=0.15)

        # Two New Balanced Shards
        new_s1 = RoundedRectangle(
            width=5.2, height=2.2, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(LEFT * 3.4 + DOWN * 1.1)
        s1_t = Text("NEW SHARD 2A", font="Georgia", font_size=24, color=ACCENT, weight=BOLD).next_to(new_s1.get_top(), DOWN, buff=0.2)
        s1_k = Text("Keys: 0x5000 - 0x67FF", font="Georgia", font_size=20, color=FG).next_to(s1_t, DOWN, buff=0.15)
        s1_b = self.badge("50% Load | Healthy", color=GOOD, font_size=19, width=4.4, height=0.55).next_to(s1_k, DOWN, buff=0.2)

        new_s2 = RoundedRectangle(
            width=5.2, height=2.2, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(RIGHT * 3.4 + DOWN * 1.1)
        s2_t = Text("NEW SHARD 2B", font="Georgia", font_size=24, color=GOOD, weight=BOLD).next_to(new_s2.get_top(), DOWN, buff=0.2)
        s2_k = Text("Keys: 0x6800 - 0x7FFF", font="Georgia", font_size=20, color=FG).next_to(s2_t, DOWN, buff=0.15)
        s2_b = self.badge("50% Load | Healthy", color=GOOD, font_size=19, width=4.4, height=0.55).next_to(s2_k, DOWN, buff=0.2)

        self.play(FadeIn(hot_shard), FadeIn(hot_title), FadeIn(hot_keys))
        self.wait(4.0)
        self.play(GrowArrow(arr_left), GrowArrow(arr_right))
        self.wait(1.5)
        self.play(FadeIn(new_s1), FadeIn(s1_t), FadeIn(s1_k), FadeIn(s1_b),
                  FadeIn(new_s2), FadeIn(s2_t), FadeIn(s2_k), FadeIn(s2_b))
        self.wait(6.5)


# ============================================================
# Beat B07: High Availability Sharded Topology (12.54s)
# ============================================================
class B07_HighAvailabilityShardedTopology(BrutalistScene):
    def construct(self):
        hdr = self.heading("PRODUCTION SHARDED TOPOLOGY")
        cap = self.caption("Production sharding pairs horizontal scale with full primary-replica fault tolerance", color=GOOD)
        self.add(hdr, cap)

        # Top: Stateless Router Pool
        router_pool = RoundedRectangle(
            width=11.2, height=1.0, corner_radius=0.08,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
        ).move_to(UP * 2.1)
        router_txt = Text("STATELESS QUERY ROUTER CLUSTER (VTGate / Mongos)", font="Georgia", font_size=24, color=BLUE, weight=BOLD).move_to(router_pool)

        # 3 Shard Replica Sets
        shards = VGroup()
        sets = [
            ("SHARD 1 REPLICA SET", LEFT * 4.0),
            ("SHARD 2 REPLICA SET", ORIGIN),
            ("SHARD 3 REPLICA SET", RIGHT * 4.0),
        ]

        for s_title, pos in sets:
            set_box = RoundedRectangle(
                width=3.6, height=2.6, corner_radius=0.1,
                stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.95
            ).move_to(pos + DOWN * 0.25)
            t = Text(s_title, font="Georgia", font_size=20, color=ACCENT, weight=BOLD).next_to(set_box.get_top(), DOWN, buff=0.2)
            p = self.badge("PRIMARY (Writes)", color=GOOD, font_size=18, width=3.1, height=0.5).next_to(t, DOWN, buff=0.18)
            r = self.badge("2x REPLICAS (Reads)", color=FG, font_size=18, width=3.1, height=0.5).next_to(p, DOWN, buff=0.15)
            shards.add(VGroup(set_box, t, p, r))

        # Connecting vertical arrows
        a1 = Arrow(router_pool.get_bottom() + LEFT * 4.0, shards[0][0].get_top(), color=ACCENT, stroke_width=4, buff=0.12)
        a2 = Arrow(router_pool.get_bottom(), shards[1][0].get_top(), color=ACCENT, stroke_width=4, buff=0.12)
        a3 = Arrow(router_pool.get_bottom() + RIGHT * 4.0, shards[2][0].get_top(), color=ACCENT, stroke_width=4, buff=0.12)

        # Bottom payoff banner
        summary = self.badge("UNLIMITED HORIZONTAL CAPACITY · ZERO SINGLE POINTS OF FAILURE", color=GOOD, font_size=22, width=11.2, height=0.68).move_to(DOWN * 2.15)

        self.play(FadeIn(router_pool), FadeIn(router_txt))
        self.wait(2.5)
        self.play(GrowArrow(a1), GrowArrow(a2), GrowArrow(a3), FadeIn(shards))
        self.wait(3.5)
        self.play(FadeIn(summary))
        self.wait(5.5)
