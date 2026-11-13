# -*- coding: utf-8 -*-
from manim import *

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


class BrutalistScene(Scene):

    def setup(self):
        self.camera.background_color = BG

    def heading(self, text):
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

        title = VGroup(*[
            Text(line, font_size=31, color=FG, weight=BOLD)
            for line in lines
        ]).arrange(DOWN, buff=.10)

        title.move_to(UP * 6.65)

        rule = Line(
            LEFT * 3.65,
            RIGHT * 3.65,
            color=ACCENT,
            stroke_width=5
        ).next_to(title, DOWN, buff=.20)

        return VGroup(title, rule)

    def box(self, label, width=4.6, height=1.25,
            color=FG, font_size=25):

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

        if text.width > width - .45:
            text.scale_to_fit_width(width - .45)

        text.move_to(rect)
        return VGroup(rect, text)

    def request(self, label):
        return self.box(
            label,
            width=2.15,
            height=.72,
            color=ACCENT,
            font_size=19
        )

    def caption(self, text, color=MUTED):
        words = text.split()
        lines = []
        current = []

        for word in words:
            candidate = " ".join(current + [word])
            if len(candidate) > 31 and current:
                lines.append(" ".join(current))
                current = [word]
            else:
                current.append(word)

        if current:
            lines.append(" ".join(current))

        t = VGroup(*[
            Text(line, font_size=20, color=color, weight=BOLD)
            for line in lines
        ]).arrange(DOWN, buff=.10)

        if t.width > 7.4:
            t.scale_to_fit_width(7.4)

        t.move_to(DOWN * 6.55)
        return t

    def down_arrow(self, source, target, color=GOOD,
                   stroke_width=5, buff=.16):
        return Arrow(
            source.get_bottom(),
            target.get_top(),
            buff=buff,
            color=color,
            stroke_width=stroke_width,
            max_tip_length_to_length_ratio=.14
        )

    def up_arrow(self, source, target, color=GOOD,
                 stroke_width=5, buff=.16):
        return Arrow(
            source.get_top(),
            target.get_bottom(),
            buff=buff,
            color=color,
            stroke_width=stroke_width,
            max_tip_length_to_length_ratio=.14
        )

    def app(self):
        return self.box("APPLICATION", color=FG)

    def cache(self):
        return self.box("CACHE", color=ACCENT)

    def database(self, color=FG):
        return self.box("DATABASE", color=color)


# ============================================================
# B00 — REPEATED DATA
# ============================================================

class B00_RepeatedData(BrutalistScene):

    def construct(self):
        title = self.heading("THE SAME DATA. AGAIN AND AGAIN.")

        user = self.box(
            "USER",
            width=3.3,
            color=ACCENT
        ).move_to(UP * 3.8)

        app = self.app().move_to(UP * .9)
        db = self.database().move_to(DOWN * 2.3)

        a1 = self.down_arrow(user, app)
        a2 = self.down_arrow(app, db)

        self.play(FadeIn(title), run_time=.6)
        self.play(FadeIn(user), FadeIn(app), FadeIn(db), run_time=.7)
        self.play(Create(a1), run_time=.6)
        self.play(Create(a2), run_time=.6)

        repeated = VGroup(
            self.request("REQ 1"),
            self.request("REQ 2"),
            self.request("REQ 3")
        ).arrange(RIGHT, buff=.25)

        repeated.move_to(UP * 2.35 + LEFT * .85)

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
        ]).arrange(RIGHT, buff=.06)

        requests.scale(.82)
        requests.move_to(UP * 3.8)

        db = self.database(FG).move_to(DOWN * .8)

        self.play(FadeIn(title), FadeIn(db), run_time=.7)

        self.play(
            LaggedStart(
                *[FadeIn(r) for r in requests],
                lag_ratio=.10
            ),
            run_time=.8
        )

        arrows = VGroup(*[
            Arrow(
                r.get_bottom(),
                db.get_top(),
                buff=.14,
                color=FG,
                stroke_width=3,
                max_tip_length_to_length_ratio=.12
            )
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
            font_size=29,
            color=BAD,
            weight=BOLD
        ).next_to(db, DOWN, buff=.55)

        self.play(FadeIn(load), run_time=.5)

        cap = self.caption(
            "MORE TRAFFIC MEANS MORE DATABASE WORK"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B02 — ADD CACHE
# ============================================================

class B02_AddCache(BrutalistScene):

    def construct(self):
        title = self.heading("ADD A CACHE")

        app = self.app().move_to(UP * 3.5)
        cache = self.cache().move_to(UP * .2)
        db = self.database().move_to(DOWN * 3.1)

        self.play(
            FadeIn(title),
            FadeIn(app),
            FadeIn(db),
            run_time=.7
        )

        self.play(FadeIn(cache), run_time=.6)

        a1 = self.down_arrow(app, cache)
        a2 = self.down_arrow(cache, db)

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

        app = self.app().move_to(UP * 3.5)
        cache = self.cache().move_to(UP * .2)
        db = self.database().move_to(DOWN * 3.1)

        self.play(
            FadeIn(title),
            FadeIn(app),
            FadeIn(cache),
            FadeIn(db),
            run_time=.7
        )

        lookup = self.down_arrow(app, cache)
        self.play(Create(lookup), run_time=.7)

        miss = Text(
            "MISS",
            font_size=30,
            color=BAD,
            weight=BOLD
        ).next_to(cache, RIGHT, buff=.35)

        self.play(FadeIn(miss), run_time=.5)

        db_lookup = self.down_arrow(cache, db, BAD)
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

        db = self.database().move_to(UP * 2.6)
        cache = self.cache().move_to(DOWN * 1.5)

        self.play(
            FadeIn(title),
            FadeIn(cache),
            FadeIn(db),
            run_time=.7
        )

        returned = self.down_arrow(db, cache)
        self.play(Create(returned), run_time=.9)

        item = self.box(
            "DATA",
            width=2.3,
            height=.75,
            color=GOOD,
            font_size=20
        ).move_to(UP * .55 + RIGHT * 1.65)

        self.play(FadeIn(item), run_time=.5)

        stored = Text(
            "STORED",
            font_size=29,
            color=GOOD,
            weight=BOLD
        ).next_to(cache, DOWN, buff=.55)

        self.play(FadeIn(stored), run_time=.5)

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

        app = self.app().move_to(UP * 3.5)
        cache = self.cache().move_to(UP * .1)
        db = self.database(MUTED).move_to(DOWN * 3.3)

        self.play(
            FadeIn(title),
            FadeIn(app),
            FadeIn(cache),
            FadeIn(db),
            run_time=.7
        )

        lookup = self.down_arrow(app, cache, GOOD)
        self.play(Create(lookup), run_time=.7)

        hit = Text(
            "HIT",
            font_size=32,
            color=GOOD,
            weight=BOLD
        ).next_to(cache, RIGHT, buff=.4)

        self.play(FadeIn(hit), run_time=.5)

        response = self.up_arrow(cache, app, GOOD)
        response.shift(RIGHT * .55)

        self.play(Create(response), run_time=.7)

        bypassed = Text(
            "NO QUERY",
            font_size=21,
            color=MUTED,
            weight=BOLD
        ).next_to(db, RIGHT, buff=.35)

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
            width=5.3,
            height=1.5,
            color=ACCENT,
            font_size=27
        ).move_to(UP * 1.7)

        ttl60 = Text(
            "TTL: 60s",
            font_size=31,
            color=GOOD,
            weight=BOLD
        ).move_to(DOWN * .2)

        ttl30 = Text(
            "TTL: 30s",
            font_size=31,
            color=GOOD,
            weight=BOLD
        ).move_to(ttl60)

        ttl1 = Text(
            "TTL: 1s",
            font_size=31,
            color=BAD,
            weight=BOLD
        ).move_to(ttl60)

        expired = Text(
            "EXPIRED",
            font_size=30,
            color=BAD,
            weight=BOLD
        ).move_to(ttl60)

        self.play(FadeIn(title), FadeIn(cache), run_time=.7)
        self.play(FadeIn(ttl60), run_time=.5)

        self.play(
            FadeOut(ttl60),
            FadeIn(ttl30),
            run_time=.5
        )

        self.play(
            FadeOut(ttl30),
            FadeIn(ttl1),
            run_time=.5
        )

        self.play(
            FadeOut(ttl1),
            FadeIn(expired),
            run_time=.5
        )

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
        ]).arrange(RIGHT, buff=.18)

        requests.scale(.82)
        requests.move_to(UP * 4.0)

        cache = self.cache().move_to(UP * .9)
        db = self.database().move_to(DOWN * 3.0)

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
            Arrow(
                r.get_bottom(),
                cache.get_top(),
                buff=.14,
                color=GOOD,
                stroke_width=3,
                max_tip_length_to_length_ratio=.12
            )
            for r in requests
        ])

        self.play(
            LaggedStart(
                *[Create(a) for a in hit_arrows],
                lag_ratio=.08
            ),
            run_time=1.1
        )

        db_arrow = self.down_arrow(cache, db, MUTED, 3)
        self.play(Create(db_arrow), run_time=.5)

        benefits = VGroup(
            Text(
                "FASTER RESPONSES",
                font_size=23,
                color=GOOD,
                weight=BOLD
            ),
            Text(
                "LESS DATABASE LOAD",
                font_size=23,
                color=GOOD,
                weight=BOLD
            )
        ).arrange(DOWN, buff=.22)

        benefits.move_to(DOWN * 1.25 + LEFT * 1.75)

        self.play(FadeIn(benefits), run_time=.7)

        cap = self.caption(
            "SERVE MORE REQUESTS WITH LESS BACKEND WORK"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(1)
