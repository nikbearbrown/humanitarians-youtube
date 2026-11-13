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

    def badge(self, label, color=GOOD, border_color=BORDER, font_size=26, width=3.4, height=0.68):
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
# B00 - CASCADING FAILURE COLLAPSE
# ============================================================

class B00_CascadingFailureCollapse(BrutalistScene):

    def construct(self):
        title = self.heading("DOWNSTREAM TIMEOUTS TRIGGER CASCADING COLLAPSE")

        # Service chain boxes
        c1 = self.box("CLIENT", width=2.2, height=1.0, color=FG, font_size=26).move_to(LEFT * 5.4 + UP * 0.8)
        c2 = self.box("API GATEWAY", width=2.6, height=1.0, color=BLUE, font_size=26).move_to(LEFT * 2.1 + UP * 0.8)
        c3 = self.box("ORDER SERVICE", width=2.8, height=1.0, color=BLUE, font_size=26).move_to(RIGHT * 1.5 + UP * 0.8)
        c4 = self.box("PAYMENTS [DOWN]", width=3.0, height=1.0, color=BAD, font_size=26).move_to(RIGHT * 5.2 + UP * 0.8)

        chain = VGroup(c1, c2, c3, c4)

        # Flow arrows
        a1 = Arrow(c1.get_right(), c2.get_left(), buff=0.15, color=FG, stroke_width=4)
        a2 = Arrow(c2.get_right(), c3.get_left(), buff=0.15, color=BLUE, stroke_width=4)
        a3 = Arrow(c3.get_right(), c4.get_left(), buff=0.15, color=BAD, stroke_width=4)
        arrows = VGroup(a1, a2, a3)

        self.play(FadeIn(title), FadeIn(chain), Create(arrows), run_time=1.0)

        # Thread pool saturation warning card
        pool_card = self.box("BLOCKED WORKER THREAD POOLS: 100% EXHAUSTED WAITING FOR TIMEOUTS", width=12.0, height=0.95, color=BAD, font_size=26).move_to(DOWN * 0.7)
        self.play(FadeIn(pool_card), run_time=0.8)

        # Badges
        b1 = self.badge("CASCADING TIMEOUTS", color=BAD, font_size=26, width=4.2).move_to(LEFT * 3.2 + DOWN * 2.0)
        b2 = self.badge("CLUSTER-WIDE OUTAGE", color=BAD, font_size=26, width=4.2).move_to(RIGHT * 3.2 + DOWN * 2.0)
        self.play(FadeIn(b1), FadeIn(b2), run_time=0.8)

        cap = self.caption("WHEN A DOWNSTREAM SERVICE DEGRADES, CALLING THREADS BLOCK UNTIL ENTIRE SYSTEMS CRASH")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B01 - THE SOLUTION: CIRCUIT BREAKER WRAPPER
# ============================================================

class B01_CircuitBreakerConcept(BrutalistScene):

    def construct(self):
        title = self.heading("THE SOLUTION: THE CIRCUIT BREAKER WRAPPER")

        # Upstream and downstream
        up_svc = self.box("CALLING SERVICE", width=3.4, height=1.1, color=BLUE, font_size=26).move_to(LEFT * 4.6 + UP * 0.7)
        cb_proxy = self.box("CIRCUIT BREAKER PROXY", width=4.6, height=1.1, color=ACCENT, font_size=26).move_to(ORIGIN + UP * 0.7)
        dn_svc = self.box("REMOTE DEPENDENCY", width=3.4, height=1.1, color=FG, font_size=26).move_to(RIGHT * 4.6 + UP * 0.7)

        # Connectors
        arr1 = Arrow(up_svc.get_right(), cb_proxy.get_left(), buff=0.15, color=ACCENT, stroke_width=4)
        arr2 = Arrow(cb_proxy.get_right(), dn_svc.get_left(), buff=0.15, color=ACCENT, stroke_width=4)

        self.play(FadeIn(title), FadeIn(up_svc), FadeIn(cb_proxy), FadeIn(dn_svc), Create(arr1), Create(arr2), run_time=1.0)

        # Safety architecture card
        safety_box = self.box("AUTOMATIC SAFETY SWITCH: MONITORS LATENCY AND TRIPS ON REPEATED FAILURES", width=12.2, height=0.95, color=GOOD, font_size=26).move_to(DOWN * 0.7)
        self.play(FadeIn(safety_box), run_time=0.8)

        # Badges
        b1 = self.badge("INTERCEPTS CALLS", color=GOOD, font_size=26, width=3.8).move_to(LEFT * 3.2 + DOWN * 2.0)
        b2 = self.badge("FAIL-FAST ISOLATION", color=GOOD, font_size=26, width=3.8).move_to(RIGHT * 3.2 + DOWN * 2.0)
        self.play(FadeIn(b1), FadeIn(b2), run_time=0.8)

        cap = self.caption("A CIRCUIT BREAKER INTERCEPTS REMOTE CALLS TO SHIELD SYSTEMS FROM REPEATED FAILURES")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B02 - STATE 1: CLOSED (NORMAL OPERATION)
# ============================================================

class B02_ClosedStateNormal(BrutalistScene):

    def construct(self):
        title = self.heading("STATE 1: CLOSED (NORMAL PRODUCTION OPERATION)")

        # State banner
        state_banner = self.box("CURRENT STATE: CLOSED [HEALTHY FLOW]", width=8.8, height=0.85, color=GOOD, font_size=28).move_to(UP * 1.9)

        # Call flow
        caller = self.box("CALLER", width=2.4, height=1.0, color=FG, font_size=26).move_to(LEFT * 4.6 + UP * 0.4)
        gate = self.box("CLOSED GATE (100% PASS)", width=4.4, height=1.0, color=GOOD, font_size=26).move_to(ORIGIN + UP * 0.4)
        remote = self.box("REMOTE SERVICE", width=2.8, height=1.0, color=FG, font_size=26).move_to(RIGHT * 4.6 + UP * 0.4)

        a1 = Arrow(caller.get_right(), gate.get_left(), buff=0.15, color=GOOD, stroke_width=4)
        a2 = Arrow(gate.get_right(), remote.get_left(), buff=0.15, color=GOOD, stroke_width=4)

        self.play(FadeIn(title), FadeIn(state_banner), FadeIn(caller), FadeIn(gate), FadeIn(remote), Create(a1), Create(a2), run_time=1.0)

        # Rolling metric window card
        metric_card = self.box("ROLLING STATISTICAL WINDOW: 100 CALLS EVALUATED | ERROR RATE: 0.5%", width=12.2, height=0.90, color=BLUE, font_size=26).move_to(DOWN * 0.8)
        self.play(FadeIn(metric_card), run_time=0.8)

        # Badges
        b1 = self.badge("UNIMPEDED TRAFFIC", color=GOOD, font_size=26, width=3.8).move_to(LEFT * 3.2 + DOWN * 2.0)
        b2 = self.badge("CONTINUOUS TELEMETRY", color=GOOD, font_size=26, width=3.8).move_to(RIGHT * 3.2 + DOWN * 2.0)
        self.play(FadeIn(b1), FadeIn(b2), run_time=0.8)

        cap = self.caption("IN THE CLOSED STATE, CALLS FLOW FREELY WHILE SYSTEM HEALTH IS CONTINUOUSLY RECORDED")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B03 - TRIP TRIGGER: ERROR THRESHOLD EXCEEDED
# ============================================================

class B03_FailureThresholdTrip(BrutalistScene):

    def construct(self):
        title = self.heading("TRIP TRIGGER: ERROR THRESHOLD EXCEEDED")

        # Threshold alarm box
        alarm = self.box("FAILURE SPIKE: ERROR RATE EXCEEDS 50% SAFETY THRESHOLD", width=11.6, height=0.85, color=BAD, font_size=28).move_to(UP * 2.0)

        # Metric comparison boxes
        err_box = self.box("FAILED CALLS: 58 / 100 (58% ERRORS)", width=5.6, height=1.05, color=BAD, font_size=26).move_to(LEFT * 3.2 + UP * 0.6)
        thr_box = self.box("CONFIGURED TRIP LIMIT: 50.0%", width=5.6, height=1.05, color=MUTED, font_size=26).move_to(RIGHT * 3.2 + UP * 0.6)

        self.play(FadeIn(title), FadeIn(alarm), FadeIn(err_box), FadeIn(thr_box), run_time=1.0)

        # Transition action box
        action = self.box("SWITCH TRIP TRIGGERED -> TRANSITION FROM CLOSED TO OPEN", width=12.0, height=0.95, color=ACCENT, font_size=26).move_to(DOWN * 0.7)
        self.play(FadeIn(action), run_time=0.8)

        # Badges
        b1 = self.badge("SEVER NETWORK CALLS", color=BAD, font_size=26, width=4.0).move_to(LEFT * 3.2 + DOWN * 2.0)
        b2 = self.badge("ISOLATE FAILURE DOMAIN", color=BAD, font_size=26, width=4.0).move_to(RIGHT * 3.2 + DOWN * 2.0)
        self.play(FadeIn(b1), FadeIn(b2), run_time=0.8)

        cap = self.caption("CROSSING THE THRESHOLD TRIPS THE SWITCH IMMEDIATELY, SEVERING OUTBOUND CONNECTIONS")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B04 - STATE 2: OPEN (FAIL-FAST DEFLECTION)
# ============================================================

class B04_OpenStateFailFast(BrutalistScene):

    def construct(self):
        title = self.heading("STATE 2: OPEN (FAIL-FAST DEFLECTION)")

        # State banner
        state_banner = self.box("CURRENT STATE: OPEN [TRIPPED / DEFLECTING]", width=9.2, height=0.85, color=BAD, font_size=28).move_to(UP * 2.0)

        # Flow components
        caller = self.box("INCOMING CALL", width=2.8, height=1.0, color=FG, font_size=26).move_to(LEFT * 4.6 + UP * 0.6)
        breaker = self.box("CIRCUIT OPEN [BLOCK]", width=4.2, height=1.0, color=BAD, font_size=26).move_to(ORIGIN + UP * 0.6)
        remote = self.box("REMOTE [ISOLATED]", width=3.0, height=1.0, color=MUTED, font_size=26).move_to(RIGHT * 4.6 + UP * 0.6)

        a1 = Arrow(caller.get_right(), breaker.get_left(), buff=0.15, color=BAD, stroke_width=4)
        # Blocked line to remote
        x_line = Line(breaker.get_right(), remote.get_left(), color=MUTED, stroke_width=3)
        x_mark = Text("X", font="Georgia", font_size=32, color=BAD, weight=BOLD).move_to(x_line)

        self.play(FadeIn(title), FadeIn(state_banner), FadeIn(caller), FadeIn(breaker), FadeIn(remote), Create(a1), Create(x_line), FadeIn(x_mark), run_time=1.0)

        # Instant fallback return card
        fallback_card = self.box("INSTANT 0ms FALLBACK RESPONSE: LOCAL CACHE OR DEGRADED DEFAULT", width=12.2, height=0.95, color=GOOD, font_size=26).move_to(DOWN * 0.7)
        self.play(FadeIn(fallback_card), run_time=0.8)

        # Badges
        b1 = self.badge("ZERO NETWORK WAIT", color=GOOD, font_size=26, width=3.8).move_to(LEFT * 3.2 + DOWN * 2.0)
        b2 = self.badge("ALLOWS DOWNSTREAM HEALING", color=GOOD, font_size=26, width=4.2).move_to(RIGHT * 3.2 + DOWN * 2.0)
        self.play(FadeIn(b1), FadeIn(b2), run_time=0.8)

        cap = self.caption("WHILE OPEN, REQUESTS RETURN INSTANT FALLBACKS LOCALLY WITHOUT HAMMERING REMOTE SERVERS")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B05 - STATE 3: HALF-OPEN (CANARY PROBES)
# ============================================================

class B05_HalfOpenCanaryProbe(BrutalistScene):

    def construct(self):
        title = self.heading("STATE 3: HALF-OPEN (CANARY HEALTH PROBES)")

        # Timeout info and state
        timer_box = self.box("SLEEP WINDOW COMPLETE (30 SECONDS COOLDOWN)", width=9.6, height=0.75, color=MUTED, font_size=26).move_to(UP * 2.1)
        state_box = self.box("CURRENT STATE: HALF-OPEN [TRIAL PROBE TESTING]", width=9.6, height=0.80, color=BLUE, font_size=28).move_to(UP * 1.15)

        self.play(FadeIn(title), FadeIn(timer_box), FadeIn(state_box), run_time=1.0)

        # Canary flow
        calls = self.box("CLIENT TRAFFIC", width=2.8, height=1.0, color=FG, font_size=26).move_to(LEFT * 4.6 + DOWN * 0.3)
        canary = self.box("CANARY FILTER [5 PROBES]", width=4.2, height=1.0, color=BLUE, font_size=26).move_to(ORIGIN + DOWN * 0.3)
        target = self.box("REMOTE SERVICE", width=2.8, height=1.0, color=FG, font_size=26).move_to(RIGHT * 4.6 + DOWN * 0.3)

        a1 = Arrow(calls.get_right(), canary.get_left(), buff=0.15, color=BLUE, stroke_width=4)
        a2 = Arrow(canary.get_right(), target.get_left(), buff=0.15, color=BLUE, stroke_width=4)

        self.play(FadeIn(calls), FadeIn(canary), FadeIn(target), Create(a1), Create(a2), run_time=1.0)

        # Badges
        b1 = self.badge("LIMITED TRIAL BATCH", color=BLUE, font_size=26, width=4.0).move_to(LEFT * 3.2 + DOWN * 1.8)
        b2 = self.badge("VERIFY DEPENDENCY HEALTH", color=BLUE, font_size=26, width=4.2).move_to(RIGHT * 3.2 + DOWN * 1.8)
        self.play(FadeIn(b1), FadeIn(b2), run_time=0.8)

        cap = self.caption("IN HALF-OPEN, A CAREFULLY CONTROLLED SAMPLE OF REQUESTS CHECKS IF THE SERVICE IS HEALTHY")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B06 - DUAL PATH RECOVERY: RESET VS RE-TRIP
# ============================================================

class B06_SelfHealingOrRetrip(BrutalistScene):

    def construct(self):
        title = self.heading("DUAL PATH RECOVERY: RESET VS RE-TRIP")

        # Success path (left)
        p1 = self.box("PROBE OUTCOME: 100% SUCCESS", width=5.8, height=0.9, color=GOOD, font_size=26).move_to(LEFT * 3.3 + UP * 1.2)
        r1 = self.box("ACTION: RESET TO CLOSED (HEALTHY)", width=5.8, height=0.9, color=GOOD, font_size=26).move_to(LEFT * 3.3 + DOWN * 0.3)
        arr_ok = Arrow(p1.get_bottom(), r1.get_top(), buff=0.15, color=GOOD, stroke_width=4)

        # Failure path (right)
        p2 = self.box("PROBE OUTCOME: TIMEOUT OR ERROR", width=5.8, height=0.9, color=BAD, font_size=26).move_to(RIGHT * 3.3 + UP * 1.2)
        r2 = self.box("ACTION: RE-TRIP TO OPEN (EXTEND SLEEP)", width=5.8, height=0.9, color=BAD, font_size=26).move_to(RIGHT * 3.3 + DOWN * 0.3)
        arr_fail = Arrow(p2.get_bottom(), r2.get_top(), buff=0.15, color=BAD, stroke_width=4)

        self.play(FadeIn(title), FadeIn(p1), FadeIn(r1), Create(arr_ok), FadeIn(p2), FadeIn(r2), Create(arr_fail), run_time=1.2)

        # Badges
        b1 = self.badge("AUTOMATIC RECOVERY", color=GOOD, font_size=26, width=3.8).move_to(LEFT * 3.2 + DOWN * 1.8)
        b2 = self.badge("FAIL-SAFE PROTECTION", color=BAD, font_size=26, width=3.8).move_to(RIGHT * 3.2 + DOWN * 1.8)
        self.play(FadeIn(b1), FadeIn(b2), run_time=0.8)

        cap = self.caption("HEALTHY PROBES AUTOMATICALLY RESTORE FULL TRAFFIC, WHILE PERSISTENT FAILURES RE-TRIP OPEN")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B07 - RESILIENCE ARCHITECTURE PAYOFF
# ============================================================

class B07_ResilienceArchitecture(BrutalistScene):

    def construct(self):
        title = self.heading("PRODUCTION RESILIENCE: 4 DEFENSE PILLARS")

        # 4 Pillars
        p1 = self.box("1. FAIL-FAST ISOLATION", width=5.8, height=0.95, color=ACCENT, font_size=26).move_to(LEFT * 3.3 + UP * 1.4)
        p2 = self.box("2. BULKHEAD PARTITIONING", width=5.8, height=0.95, color=BLUE, font_size=26).move_to(RIGHT * 3.3 + UP * 1.4)
        p3 = self.box("3. GRACEFUL FALLBACK DEFAULTS", width=5.8, height=0.95, color=GOOD, font_size=26).move_to(LEFT * 3.3 + UP * 0.1)
        p4 = self.box("4. AUTOMATIC SELF-HEALING", width=5.8, height=0.95, color=FG, font_size=26).move_to(RIGHT * 3.3 + UP * 0.1)

        pillars = VGroup(p1, p2, p3, p4)

        self.play(FadeIn(title), FadeIn(pillars), run_time=1.0)

        # Bottom summary card
        summary = self.box("STABILITY UNDER LOAD: MAINTAINING 99.9% UPTIME ACROSS SERVICES", width=12.2, height=0.95, color=GOOD, font_size=26).move_to(DOWN * 1.3)
        self.play(FadeIn(summary), run_time=0.8)

        # Badges
        b1 = self.badge("ZERO CASCADING CRASHES", color=GOOD, font_size=26, width=4.0).move_to(LEFT * 3.2 + DOWN * 2.3)
        b2 = self.badge("HIGH AVAILABILITY", color=GOOD, font_size=26, width=3.8).move_to(RIGHT * 3.2 + DOWN * 2.3)
        self.play(FadeIn(b1), FadeIn(b2), run_time=0.8)

        cap = self.caption("CIRCUIT BREAKERS PROVIDE DISTRIBUTED FAULT TOLERANCE AND PREVENT CASCADING COLLAPSE")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)
