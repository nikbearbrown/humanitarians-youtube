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

    def box(self, label, width=6.2, height=0.85, color=FG, border_color=BORDER, font_size=28, fill_color=BG, fill_opacity=0.9):
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

    def badge(self, label, color=GOOD, border_color=BORDER, font_size=28, width=6.2, height=0.75):
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
# B00 - CASCADING FAILURE (PORTRAIT)
# ============================================================

class B00_CascadingFailureCollapse(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("DOWNSTREAM TIMEOUTS TRIGGER CASCADING COLLAPSE")

        c1 = self.box("1. CALLING CLIENT", width=6.2, height=0.75, color=FG, font_size=28).move_to(UP * 4.4)
        c2 = self.box("2. API GATEWAY", width=6.2, height=0.75, color=BLUE, font_size=28).move_to(UP * 3.3)
        c3 = self.box("3. ORDER SERVICE", width=6.2, height=0.75, color=BLUE, font_size=28).move_to(UP * 2.2)
        c4 = self.box("4. PAYMENTS [DOWN / TIMEOUT]", width=6.2, height=0.75, color=BAD, font_size=28).move_to(UP * 1.1)

        a1 = Arrow(c1.get_bottom(), c2.get_top(), buff=0.10, color=FG, stroke_width=3)
        a2 = Arrow(c2.get_bottom(), c3.get_top(), buff=0.10, color=BLUE, stroke_width=3)
        a3 = Arrow(c3.get_bottom(), c4.get_top(), buff=0.10, color=BAD, stroke_width=3)

        self.play(FadeIn(title), FadeIn(c1), FadeIn(c2), FadeIn(c3), FadeIn(c4), Create(a1), Create(a2), Create(a3), run_time=1.0)

        pool = self.box("THREAD POOLS: 100% EXHAUSTED WAITING", width=6.4, height=0.85, color=BAD, font_size=28).move_to(DOWN * 0.4)
        f1 = self.box("CASCADING LATENCY ACROSS TIERS", width=6.4, height=0.75, color=BAD, font_size=28).move_to(DOWN * 1.6)
        f2 = self.box("TOTAL CLUSTER-WIDE OUTAGE", width=6.4, height=0.75, color=BAD, font_size=28).move_to(DOWN * 2.7)

        self.play(FadeIn(pool), FadeIn(f1), FadeIn(f2), run_time=1.0)

        cap = self.caption("WHEN A DOWNSTREAM SERVICE DEGRADES, CALLING THREADS BLOCK UNTIL ENTIRE SYSTEMS CRASH")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B01 - THE SOLUTION (PORTRAIT)
# ============================================================

class B01_CircuitBreakerConcept(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("THE SOLUTION: THE CIRCUIT BREAKER WRAPPER")

        s1 = self.box("UPSTREAM CALLING SERVICE", width=6.2, height=0.8, color=BLUE, font_size=28).move_to(UP * 4.3)
        cb = self.box("CIRCUIT BREAKER PROXY", width=6.4, height=0.9, color=ACCENT, font_size=28).move_to(UP * 2.8)
        s2 = self.box("REMOTE DEPENDENCY", width=6.2, height=0.8, color=FG, font_size=28).move_to(UP * 1.3)

        a1 = Arrow(s1.get_bottom(), cb.get_top(), buff=0.12, color=ACCENT, stroke_width=3)
        a2 = Arrow(cb.get_bottom(), s2.get_top(), buff=0.12, color=ACCENT, stroke_width=3)

        self.play(FadeIn(title), FadeIn(s1), FadeIn(cb), FadeIn(s2), Create(a1), Create(a2), run_time=1.0)

        b1 = self.box("AUTOMATIC SAFETY INTERCEPTOR", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 0.3)
        b2 = self.box("FAIL-FAST FAILURE ISOLATION", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 1.4)
        b3 = self.box("PREVENTS CASCADING THREAD STALLS", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 2.5)

        self.play(FadeIn(b1), FadeIn(b2), FadeIn(b3), run_time=1.0)

        cap = self.caption("A CIRCUIT BREAKER INTERCEPTS REMOTE CALLS TO SHIELD SYSTEMS FROM REPEATED FAILURES")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B02 - CLOSED STATE (PORTRAIT)
# ============================================================

class B02_ClosedStateNormal(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("STATE 1: CLOSED (NORMAL PRODUCTION OPERATION)")

        state_card = self.box("CURRENT STATE: CLOSED [HEALTHY]", width=6.4, height=0.85, color=GOOD, font_size=28).move_to(UP * 4.5)

        c1 = self.box("CALLER INITIATES REQUEST", width=6.2, height=0.75, color=FG, font_size=28).move_to(UP * 3.2)
        c2 = self.box("CLOSED GATE (100% PASS-THROUGH)", width=6.4, height=0.85, color=GOOD, font_size=28).move_to(UP * 1.9)
        c3 = self.box("REMOTE SERVICE EXECUTES", width=6.2, height=0.75, color=FG, font_size=28).move_to(UP * 0.6)

        a1 = Arrow(c1.get_bottom(), c2.get_top(), buff=0.12, color=GOOD, stroke_width=3)
        a2 = Arrow(c2.get_bottom(), c3.get_top(), buff=0.12, color=GOOD, stroke_width=3)

        self.play(FadeIn(title), FadeIn(state_card), FadeIn(c1), FadeIn(c2), FadeIn(c3), Create(a1), Create(a2), run_time=1.0)

        m1 = self.box("ROLLING WINDOW: 100 REQUESTS", width=6.4, height=0.8, color=BLUE, font_size=28).move_to(DOWN * 0.9)
        m2 = self.box("MEASURED ERROR RATE: 0.5%", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 2.0)
        m3 = self.box("CONTINUOUS HEALTH MONITORING", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 3.1)

        self.play(FadeIn(m1), FadeIn(m2), FadeIn(m3), run_time=1.0)

        cap = self.caption("IN THE CLOSED STATE, CALLS FLOW FREELY WHILE SYSTEM HEALTH IS CONTINUOUSLY RECORDED")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B03 - TRIP TRIGGER (PORTRAIT)
# ============================================================

class B03_FailureThresholdTrip(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("TRIP TRIGGER: ERROR THRESHOLD EXCEEDED")

        alert = self.box("FAILURE SPIKE: >50% ERROR RATE", width=6.4, height=0.85, color=BAD, font_size=28).move_to(UP * 4.5)
        m1 = self.box("FAILED CALLS: 58 / 100 (58% ERRORS)", width=6.4, height=0.8, color=BAD, font_size=28).move_to(UP * 3.2)
        m2 = self.box("CONFIGURED TRIP LIMIT: 50.0%", width=6.4, height=0.8, color=MUTED, font_size=28).move_to(UP * 2.1)

        self.play(FadeIn(title), FadeIn(alert), FadeIn(m1), FadeIn(m2), run_time=1.0)

        act = self.box("CIRCUIT TRIPPED -> CLOSED TO OPEN", width=6.4, height=0.85, color=ACCENT, font_size=28).move_to(UP * 0.8)
        p1 = self.box("SEVER ALL OUTBOUND CONNECTIONS", width=6.4, height=0.8, color=BAD, font_size=28).move_to(DOWN * 0.5)
        p2 = self.box("ISOLATE FAILING SERVICE INSTANTLY", width=6.4, height=0.8, color=BAD, font_size=28).move_to(DOWN * 1.6)
        p3 = self.box("PROTECT UPSTREAM THREAD POOLS", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 2.7)

        self.play(FadeIn(act), FadeIn(p1), FadeIn(p2), FadeIn(p3), run_time=1.0)

        cap = self.caption("CROSSING THE THRESHOLD TRIPS THE SWITCH IMMEDIATELY, SEVERING OUTBOUND CONNECTIONS")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B04 - OPEN STATE (PORTRAIT)
# ============================================================

class B04_OpenStateFailFast(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("STATE 2: OPEN (FAIL-FAST DEFLECTION)")

        state_card = self.box("CURRENT STATE: OPEN [TRIPPED]", width=6.4, height=0.85, color=BAD, font_size=28).move_to(UP * 4.5)

        c1 = self.box("INCOMING CLIENT CALL", width=6.2, height=0.75, color=FG, font_size=28).move_to(UP * 3.2)
        cb = self.box("CIRCUIT BREAKER [OPEN / DEFLECT]", width=6.4, height=0.85, color=BAD, font_size=28).move_to(UP * 1.9)
        rem = self.box("REMOTE SERVICE [ISOLATED]", width=6.2, height=0.75, color=MUTED, font_size=28).move_to(UP * 0.6)

        a1 = Arrow(c1.get_bottom(), cb.get_top(), buff=0.12, color=BAD, stroke_width=3)
        x_line = Line(cb.get_bottom(), rem.get_top(), color=MUTED, stroke_width=3)
        x_mark = Text("X", font="Georgia", font_size=56, color=BAD, weight=BOLD).move_to(x_line)

        self.play(FadeIn(title), FadeIn(state_card), FadeIn(c1), FadeIn(cb), FadeIn(rem), Create(a1), Create(x_line), FadeIn(x_mark), run_time=1.0)

        f1 = self.box("INSTANT ZERO-LATENCY FALLBACK", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 0.9)
        f2 = self.box("CACHED DEFAULT DATA RETURNED", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 2.0)
        f3 = self.box("GIVES DOWNSTREAM TIME TO HEAL", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 3.1)

        self.play(FadeIn(f1), FadeIn(f2), FadeIn(f3), run_time=1.0)

        cap = self.caption("WHILE OPEN, REQUESTS RETURN INSTANT FALLBACKS LOCALLY WITHOUT HAMMERING REMOTE SERVERS")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B05 - HALF-OPEN (PORTRAIT)
# ============================================================

class B05_HalfOpenCanaryProbe(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("STATE 3: HALF-OPEN (CANARY HEALTH PROBES)")

        timer_box = self.box("SLEEP WINDOW COMPLETE (30 SECONDS)", width=6.4, height=0.75, color=MUTED, font_size=28).move_to(UP * 4.5)
        state_box = self.box("CURRENT STATE: HALF-OPEN", width=6.4, height=0.85, color=BLUE, font_size=28).move_to(UP * 3.4)

        t1 = self.box("TRIAL TRAFFIC: 5 CANARY PROBES", width=6.4, height=0.8, color=BLUE, font_size=28).move_to(UP * 2.1)
        t2 = self.box("PROBE DISPATCHED TO DOWNSTREAM", width=6.4, height=0.8, color=BLUE, font_size=28).move_to(UP * 0.9)
        arr = Arrow(t1.get_bottom(), t2.get_top(), buff=0.12, color=BLUE, stroke_width=3)

        self.play(FadeIn(title), FadeIn(timer_box), FadeIn(state_box), FadeIn(t1), FadeIn(t2), Create(arr), run_time=1.0)

        v1 = self.box("CONTROLLED EXPERIMENTAL BATCH", width=6.4, height=0.8, color=BLUE, font_size=28).move_to(DOWN * 0.6)
        v2 = self.box("MEASURING LATENCY & ERROR RATE", width=6.4, height=0.8, color=BLUE, font_size=28).move_to(DOWN * 1.7)
        v3 = self.box("SHIELDS FROM TOTAL OVERLOAD", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 2.8)

        self.play(FadeIn(v1), FadeIn(v2), FadeIn(v3), run_time=1.0)

        cap = self.caption("IN HALF-OPEN, A CAREFULLY CONTROLLED SAMPLE OF REQUESTS CHECKS IF THE SERVICE IS HEALTHY")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B06 - DUAL PATH RECOVERY (PORTRAIT)
# ============================================================

class B06_SelfHealingOrRetrip(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("DUAL PATH RECOVERY: RESET VS RE-TRIP")

        p1 = self.box("PATH A: CANARY PROBES SUCCEED", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(UP * 4.3)
        r1 = self.box("ACTION: RESET TO CLOSED (HEALTHY)", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(UP * 3.2)
        arr1 = Arrow(p1.get_bottom(), r1.get_top(), buff=0.12, color=GOOD, stroke_width=3)

        p2 = self.box("PATH B: CANARY PROBES FAIL", width=6.4, height=0.8, color=BAD, font_size=28).move_to(UP * 1.7)
        r2 = self.box("ACTION: RE-TRIP TO OPEN (EXTEND SLEEP)", width=6.4, height=0.8, color=BAD, font_size=28).move_to(UP * 0.6)
        arr2 = Arrow(p2.get_bottom(), r2.get_top(), buff=0.12, color=BAD, stroke_width=3)

        self.play(FadeIn(title), FadeIn(p1), FadeIn(r1), Create(arr1), FadeIn(p2), FadeIn(r2), Create(arr2), run_time=1.2)

        b1 = self.box("AUTOMATIC RECOVERY WITHOUT RESTART", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 0.9)
        b2 = self.box("FAIL-SAFE RESILIENCE PROTECTION", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 2.0)
        b3 = self.box("ZERO HUMAN INTERVENTION NEEDED", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 3.1)

        self.play(FadeIn(b1), FadeIn(b2), FadeIn(b3), run_time=1.0)

        cap = self.caption("HEALTHY PROBES AUTOMATICALLY RESTORE FULL TRAFFIC, WHILE PERSISTENT FAILURES RE-TRIP OPEN")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B07 - RESILIENCE PAYOFF (PORTRAIT)
# ============================================================

class B07_ResilienceArchitecture(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("PRODUCTION RESILIENCE: 4 DEFENSE PILLARS")

        p1 = self.box("1. FAIL-FAST CIRCUIT BREAKERS", width=6.4, height=0.75, color=ACCENT, font_size=28).move_to(UP * 4.4)
        p2 = self.box("2. BULKHEAD THREAD ISOLATION", width=6.4, height=0.75, color=BLUE, font_size=28).move_to(UP * 3.3)
        p3 = self.box("3. GRACEFUL FALLBACK CACHING", width=6.4, height=0.75, color=GOOD, font_size=28).move_to(UP * 2.2)
        p4 = self.box("4. AUTOMATIC SELF-HEALING", width=6.4, height=0.75, color=FG, font_size=28).move_to(UP * 1.1)

        self.play(FadeIn(title), FadeIn(p1), FadeIn(p2), FadeIn(p3), FadeIn(p4), run_time=1.0)

        s1 = self.box("STABILITY UNDER HEAVY LOAD", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 0.5)
        s2 = self.box("MAINTAINING 99.9% SYSTEM UPTIME", width=6.4, height=0.85, color=GOOD, font_size=28).move_to(DOWN * 1.6)
        s3 = self.box("ZERO CASCADING OUTAGES", width=6.4, height=0.8, color=GOOD, font_size=28).move_to(DOWN * 2.7)

        self.play(FadeIn(s1), FadeIn(s2), FadeIn(s3), run_time=1.0)

        cap = self.caption("CIRCUIT BREAKERS PROVIDE DISTRIBUTED FAULT TOLERANCE AND PREVENT CASCADING COLLAPSE")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)
