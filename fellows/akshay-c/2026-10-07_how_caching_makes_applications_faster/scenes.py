# -*- coding: utf-8 -*-
from manim import *

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


class BrutalistScene(Scene):

    def setup(self):
        self.camera.background_color = BG

    def heading(self, text):
        words = text.split()
        lines = []
        current = []

        for word in words:
            candidate = " ".join(current + [word])
            if len(candidate) > 42 and current:
                lines.append(" ".join(current))
                current = [word]
            else:
                current.append(word)

        if current:
            lines.append(" ".join(current))

        title = VGroup(*[
            Text(line, font_size=32, color=FG, weight=BOLD)
            for line in lines
        ]).arrange(DOWN, buff=.08)

        title.move_to(UP * 3.55)

        rule = Line(
            LEFT * 6.8,
            RIGHT * 6.8,
            color=ACCENT,
            stroke_width=5
        ).next_to(title, DOWN, buff=.16)

        return VGroup(title, rule)

    def box(self, label, width=3.0, height=1.05,
            color=FG, font_size=24):

        rect = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=.08,
            stroke_color=color,
            stroke_width=3
        )

        text = Text(
            label,
            font_size=font_size,
            color=color,
            weight=BOLD
        )

        max_text_width = width - .35
        if text.width > max_text_width:
            text.scale_to_fit_width(max_text_width)

        text.move_to(rect)
        return VGroup(rect, text)

    def request(self, label):
        return self.box(
            label,
            width=1.25,
            height=.58,
            color=ACCENT,
            font_size=18
        )

    def caption(self, text, color=MUTED):
        t = Text(
            text,
            font_size=22,
            color=color,
            weight=BOLD
        )

        if t.width > 12.5:
            t.scale_to_fit_width(12.5)

        t.move_to(DOWN * 3.45)
        return t

    def edge_arrow(self, source, target, color=GOOD,
                   stroke_width=5, buff=.14):
        return Arrow(
            source.get_right(),
            target.get_left(),
            buff=buff,
            color=color,
            stroke_width=stroke_width,
            max_tip_length_to_length_ratio=.14
        )

    def reverse_edge_arrow(self, source, target, color=GOOD,
                           stroke_width=5, buff=.14):
        return Arrow(
            source.get_left(),
            target.get_right(),
            buff=buff,
            color=color,
            stroke_width=stroke_width,
            max_tip_length_to_length_ratio=.14
        )

    def app(self):
        return self.box(
            "APPLICATION",
            width=3.0,
            height=1.15,
            color=FG
        )

    def cache(self):
        return self.box(
            "CACHE",
            width=2.7,
            height=1.15,
            color=ACCENT
        )

    def database(self, color=FG):
        return self.box(
            "DATABASE",
            width=2.8,
            height=1.15,
            color=color
        )


# ============================================================
# B00 — REPEATED DATA
# ============================================================

class B00_RepeatedData(BrutalistScene):

    def construct(self):
        title = self.heading("THE SAME DATA. AGAIN AND AGAIN.")

        user = self.box(
            "USER",
            width=2.0,
            color=ACCENT
        ).move_to(LEFT * 5.4)

        app = self.app().move_to(ORIGIN)

        db = self.database().move_to(RIGHT * 5.2)

        a1 = self.edge_arrow(user, app)
        a2 = self.edge_arrow(app, db)

        self.play(FadeIn(title), run_time=.6)
        self.play(
            FadeIn(user),
            FadeIn(app),
            FadeIn(db),
            run_time=.7
        )

        self.play(Create(a1), run_time=.6)
        self.play(Create(a2), run_time=.6)

        repeated = VGroup(
            self.request("REQ 1"),
            self.request("REQ 2"),
            self.request("REQ 3")
        ).arrange(DOWN, buff=.18)

        repeated.move_to(LEFT * 3.55 + DOWN * 1.45)

        self.play(
            LaggedStart(
                *[FadeIn(r) for r in repeated],
                lag_ratio=.15
            ),
            run_time=.8
        )

        cap = self.caption(
            "EVERY REQUEST TRAVELS ALL THE WAY TO THE DATABASE"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B01 — DATABASE LOAD
# ============================================================

class B01_DatabaseLoad(BrutalistScene):

    def construct(self):
        title = self.heading("REPEATED QUERIES ADD UP")

        requests = VGroup(*[
            self.request(f"REQ {i}")
            for i in range(1, 6)
        ])

        requests.arrange(DOWN, buff=.18)
        requests.move_to(LEFT * 5.0)

        db = self.database(BAD).move_to(RIGHT * 4.7)

        self.play(FadeIn(title), FadeIn(db), run_time=.7)

        self.play(
            LaggedStart(
                *[FadeIn(r) for r in requests],
                lag_ratio=.10
            ),
            run_time=.8
        )

        arrows = VGroup(*[
            self.edge_arrow(r, db, BAD, 3)
            for r in requests
        ])

        self.play(
            LaggedStart(
                *[Create(a) for a in arrows],
                lag_ratio=.08
            ),
            run_time=1.3
        )

        load = Text(
            "DATABASE LOAD ↑",
            font_size=28,
            color=BAD,
            weight=BOLD
        ).next_to(db, DOWN, buff=.45)

        self.play(FadeIn(load), run_time=.5)

        cap = self.caption(
            "MORE TRAFFIC MEANS MORE DATABASE WORK"
        )
        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B02 — ADD A CACHE
# ============================================================

class B02_AddCache(BrutalistScene):

    def construct(self):
        title = self.heading("ADD A CACHE")

        app = self.app().move_to(LEFT * 4.7)
        cache = self.cache().move_to(ORIGIN)
        db = self.database().move_to(RIGHT * 4.7)

        self.play(
            FadeIn(title),
            FadeIn(app),
            FadeIn(db),
            run_time=.7
        )

        self.play(FadeIn(cache), run_time=.6)

        a1 = self.edge_arrow(app, cache)
        a2 = self.edge_arrow(cache, db)

        self.play(Create(a1), Create(a2), run_time=.9)

        cap = self.caption(
            "KEEP FREQUENTLY USED DATA CLOSER TO THE APPLICATION"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B03 — CACHE MISS
# ============================================================

class B03_CacheMiss(BrutalistScene):

    def construct(self):
        title = self.heading("CACHE MISS")

        app = self.app().move_to(LEFT * 4.7)
        cache = self.cache().move_to(ORIGIN)
        db = self.database().move_to(RIGHT * 4.7)

        self.play(
            FadeIn(title),
            FadeIn(app),
            FadeIn(cache),
            FadeIn(db),
            run_time=.7
        )

        lookup = self.edge_arrow(app, cache)

        self.play(Create(lookup), run_time=.7)

        miss = Text(
            "MISS",
            font_size=30,
            color=BAD,
            weight=BOLD
        ).next_to(cache, DOWN, buff=.45)

        self.play(FadeIn(miss), run_time=.5)

        db_lookup = self.edge_arrow(cache, db, BAD)

        self.play(Create(db_lookup), run_time=.8)

        cap = self.caption(
            "NOT IN CACHE → FETCH IT FROM THE DATABASE"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B04 — STORE RESULT
# ============================================================

class B04_StoreResult(BrutalistScene):

    def construct(self):
        title = self.heading("STORE THE RESULT")

        cache = self.cache().move_to(LEFT * 2.6)
        db = self.database().move_to(RIGHT * 3.2)

        self.play(
            FadeIn(title),
            FadeIn(cache),
            FadeIn(db),
            run_time=.7
        )

        returned = self.reverse_edge_arrow(db, cache)

        self.play(Create(returned), run_time=.9)

        stored = Text(
            "STORED",
            font_size=29,
            color=GOOD,
            weight=BOLD
        ).next_to(cache, DOWN, buff=.48)

        self.play(FadeIn(stored), run_time=.5)

        item = self.box(
            "DATA",
            width=1.5,
            height=.62,
            color=GOOD,
            font_size=19
        ).next_to(cache, UP, buff=.45)

        self.play(FadeIn(item), run_time=.5)

        cap = self.caption(
            "SAVE A COPY FOR THE NEXT REQUEST"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B05 — CACHE HIT
# ============================================================

class B05_CacheHit(BrutalistScene):

    def construct(self):
        title = self.heading("CACHE HIT")

        app = self.app().move_to(LEFT * 4.7)
        cache = self.cache().move_to(ORIGIN)
        db = self.database(MUTED).move_to(RIGHT * 4.7)

        self.play(
            FadeIn(title),
            FadeIn(app),
            FadeIn(cache),
            FadeIn(db),
            run_time=.7
        )

        lookup = self.edge_arrow(app, cache, GOOD)

        self.play(Create(lookup), run_time=.7)

        hit = Text(
            "HIT",
            font_size=32,
            color=GOOD,
            weight=BOLD
        ).next_to(cache, DOWN, buff=.45)

        self.play(FadeIn(hit), run_time=.5)

        response = self.reverse_edge_arrow(cache, app, GOOD)

        self.play(Create(response), run_time=.7)

        bypassed = Text(
            "NO QUERY",
            font_size=21,
            color=MUTED,
            weight=BOLD
        ).next_to(db, DOWN, buff=.45)

        self.play(FadeIn(bypassed), run_time=.4)

        cap = self.caption(
            "THE DATABASE DOESN'T NEED TO DO THE WORK AGAIN"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B06 — TTL
# ============================================================

class B06_TTL(BrutalistScene):

    def construct(self):
        title = self.heading("CACHE ENTRIES EXPIRE")

        cache = self.box(
            "CACHED DATA",
            width=4.3,
            height=1.45,
            color=ACCENT,
            font_size=27
        ).move_to(UP * .35)

        ttl = Text(
            "TTL: 60s",
            font_size=31,
            color=GOOD,
            weight=BOLD
        ).next_to(cache, DOWN, buff=.55)

        self.play(FadeIn(title), FadeIn(cache), run_time=.7)
        self.play(FadeIn(ttl), run_time=.5)

        ttl30 = Text(
            "TTL: 30s",
            font_size=31,
            color=GOOD,
            weight=BOLD
        ).move_to(ttl)

        ttl0 = Text(
            "TTL: 1s",
            font_size=31,
            color=BAD,
            weight=BOLD
        ).move_to(ttl)

        self.play(Transform(ttl, ttl30), run_time=.7)
        self.play(Transform(ttl, ttl0), run_time=.7)

        expired = Text(
            "EXPIRED",
            font_size=28,
            color=BAD,
            weight=BOLD
        ).next_to(ttl, DOWN, buff=.45)

        self.play(FadeIn(expired), run_time=.5)

        cap = self.caption(
            "EXPIRATION HELPS LIMIT HOW LONG STALE DATA IS KEPT"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B07 — PAYOFF
# ============================================================

class B07_CachingPayoff(BrutalistScene):

    def construct(self):
        title = self.heading("LESS WORK. FASTER RESPONSES.")

        requests = VGroup(*[
            self.request(f"REQ {i}")
            for i in range(1, 5)
        ])

        requests.arrange(DOWN, buff=.18)
        requests.move_to(LEFT * 5.3)

        cache = self.cache().move_to(ORIGIN)
        db = self.database().move_to(RIGHT * 5.0)

        self.play(
            FadeIn(title),
            FadeIn(cache),
            FadeIn(db),
            run_time=.7
        )

        self.play(
            LaggedStart(
                *[FadeIn(r) for r in requests],
                lag_ratio=.10
            ),
            run_time=.7
        )

        hit_arrows = VGroup(*[
            self.edge_arrow(r, cache, GOOD, 3)
            for r in requests
        ])

        self.play(
            LaggedStart(
                *[Create(a) for a in hit_arrows],
                lag_ratio=.08
            ),
            run_time=1.1
        )

        db_arrow = self.edge_arrow(cache, db, MUTED, 3)
        self.play(Create(db_arrow), run_time=.5)

        benefits = VGroup(
            Text(
                "FASTER RESPONSES",
                font_size=25,
                color=GOOD,
                weight=BOLD
            ),
            Text(
                "LESS DATABASE LOAD",
                font_size=25,
                color=GOOD,
                weight=BOLD
            )
        ).arrange(RIGHT, buff=1.5)

        benefits.move_to(DOWN * 2.15)

        self.play(FadeIn(benefits), run_time=.7)

        cap = self.caption(
            "SERVE MORE REQUESTS WITH LESS BACKEND WORK"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(1)

