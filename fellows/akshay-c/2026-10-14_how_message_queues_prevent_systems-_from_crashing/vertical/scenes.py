# -*- coding: utf-8 -*-
from manim import *

# Native 4K portrait.
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
            if len(candidate) > 25 and current:
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

        if title.width > 7.0:
            title.scale_to_fit_width(7.0)

        title.move_to(UP * 6.55)

        rule = Line(
            LEFT * 3.35,
            RIGHT * 3.35,
            color=ACCENT,
            stroke_width=5
        ).next_to(title, DOWN, buff=.18)

        return VGroup(title, rule)

    def box(self, label, width=5.7, height=1.10,
            color=FG, font_size=27):
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

    def message(self, label):
        return self.box(
            label,
            width=1.75,
            height=.68,
            color=ACCENT,
            font_size=19
        )

    def caption(self, text, color=MUTED):
        t = Text(
            text,
            font_size=23,
            color=color,
            weight=BOLD
        )

        if t.width > 7.0:
            t.scale_to_fit_width(7.0)

        t.move_to(DOWN * 6.45)
        return t

    def vertical_arrow(self, source, target, color=GOOD,
                       stroke_width=5, buff=.16):
        return Arrow(
            source.get_bottom(),
            target.get_top(),
            buff=buff,
            color=color,
            stroke_width=stroke_width,
            max_tip_length_to_length_ratio=.14
        )

    def producer(self):
        return self.box(
            "PRODUCER",
            width=5.5,
            height=1.10,
            color=FG,
            font_size=26
        )

    def message_queue(self):
        return self.box(
            "MESSAGE QUEUE",
            width=5.8,
            height=1.25,
            color=ACCENT,
            font_size=26
        )

    def consumer(self, label="CONSUMER", color=FG):
        return self.box(
            label,
            width=5.5,
            height=1.05,
            color=color,
            font_size=25
        )


# ============================================================
# B00 - TRAFFIC BURST
# ============================================================

class B00_TrafficBurst(BrutalistScene):

    def construct(self):
        title = self.heading("WHEN TRAFFIC ARRIVES ALL AT ONCE")

        jobs = VGroup(*[
            self.message(f"JOB {i}")
            for i in range(1, 6)
        ])

        jobs.arrange_in_grid(
            rows=2,
            cols=3,
            buff=(.28, .30)
        )
        jobs.move_to(UP * 2.65)

        service = self.box(
            "SERVICE",
            width=5.5,
            height=1.25,
            color=FG
        ).move_to(DOWN * 1.75)

        self.play(FadeIn(title), FadeIn(service), run_time=.7)

        self.play(
            LaggedStart(
                *[FadeIn(job) for job in jobs],
                lag_ratio=.10
            ),
            run_time=.8
        )

        arrows = VGroup(*[
            Arrow(
                job.get_bottom(),
                service.get_top(),
                buff=.16,
                color=BAD,
                stroke_width=3,
                max_tip_length_to_length_ratio=.12
            )
            for job in jobs
        ])

        self.play(
            LaggedStart(
                *[Create(a) for a in arrows],
                lag_ratio=.07
            ),
            run_time=1.2
        )

        spike = Text(
            "TRAFFIC SPIKE",
            font_size=27,
            color=BAD,
            weight=BOLD
        ).next_to(service, DOWN, buff=.48)

        self.play(FadeIn(spike), run_time=.5)

        cap = self.caption(
            "THOUSANDS OF JOBS CAN ARRIVE IN A SHORT BURST"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B01 - OVERLOAD
# ============================================================

class B01_ServiceOverload(BrutalistScene):

    def construct(self):
        title = self.heading("WORK ARRIVES FASTER THAN IT CAN FINISH")

        backlog = VGroup(*[
            self.message(f"JOB {i}")
            for i in range(1, 6)
        ])

        backlog.arrange_in_grid(
            rows=2,
            cols=3,
            buff=(.28, .30)
        )
        backlog.move_to(UP * 2.65)

        service = self.box(
            "SERVICE",
            width=5.5,
            height=1.30,
            color=BAD
        ).move_to(DOWN * 1.55)

        self.play(FadeIn(title), run_time=.7)

        self.play(
            LaggedStart(
                *[FadeIn(job) for job in backlog],
                lag_ratio=.10
            ),
            run_time=.9
        )

        backlog_label = Text(
            "PENDING WORK",
            font_size=23,
            color=ACCENT,
            weight=BOLD
        ).move_to(LEFT * 2.7 + UP * .35)

        self.play(FadeIn(backlog_label), run_time=.4)
        self.play(FadeIn(service), run_time=.4)

        arrows = VGroup(*[
            Arrow(
                job.get_bottom(),
                service.get_top(),
                buff=.16,
                color=BAD,
                stroke_width=3,
                max_tip_length_to_length_ratio=.12
            )
            for job in backlog
        ])

        self.play(
            LaggedStart(
                *[Create(a) for a in arrows],
                lag_ratio=.07
            ),
            run_time=1.0
        )

        overload = Text(
            "OVERLOADED",
            font_size=30,
            color=BAD,
            weight=BOLD
        ).next_to(service, DOWN, buff=.48)

        self.play(FadeIn(overload), run_time=.5)

        cap = self.caption(
            "UNCONTROLLED BACKLOGS CAN INCREASE LATENCY AND FAILURES"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B02 - ADD MESSAGE QUEUE
# ============================================================

class B02_AddQueue(BrutalistScene):

    def construct(self):
        title = self.heading("ADD A MESSAGE QUEUE")

        producer = self.producer().move_to(UP * 3.0)
        queue = self.message_queue().move_to(ORIGIN)
        consumer = self.consumer().move_to(DOWN * 3.0)

        self.play(
            FadeIn(title),
            FadeIn(producer),
            FadeIn(consumer),
            run_time=.7
        )

        self.play(FadeIn(queue), run_time=.6)

        a1 = self.vertical_arrow(producer, queue)
        a2 = self.vertical_arrow(queue, consumer)

        self.play(Create(a1), Create(a2), run_time=.9)

        cap = self.caption(
            "THE QUEUE BUFFERS WORK BETWEEN PRODUCERS AND CONSUMERS"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B03 - PRODUCERS PUBLISH
# ============================================================

class B03_PublishMessages(BrutalistScene):

    def construct(self):
        title = self.heading("PRODUCERS PUBLISH. THEN MOVE ON.")

        producer = self.producer().move_to(UP * 3.25)
        queue = self.message_queue().move_to(DOWN * 2.15)

        self.play(
            FadeIn(title),
            FadeIn(producer),
            FadeIn(queue),
            run_time=.7
        )

        lane = self.vertical_arrow(producer, queue, GOOD)
        self.play(Create(lane), run_time=.7)

        messages = VGroup(*[
            self.message(f"MSG {i}")
            for i in range(1, 4)
        ]).arrange(DOWN, buff=.20)

        messages.scale(.88)
        messages.move_to(RIGHT * 2.15 + UP * .55)

        self.play(
            LaggedStart(
                *[FadeIn(msg) for msg in messages],
                lag_ratio=.15
            ),
            run_time=.8
        )

        async_label = Text(
            "ASYNCHRONOUS",
            font_size=27,
            color=GOOD,
            weight=BOLD
        ).next_to(queue, DOWN, buff=.48)

        self.play(FadeIn(async_label), run_time=.5)

        cap = self.caption(
            "THE PRODUCER DOESN'T WAIT FOR DOWNSTREAM WORK TO FINISH"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B04 - CONTROLLED CONSUMPTION
# ============================================================

class B04_ControlledConsumption(BrutalistScene):

    def construct(self):
        title = self.heading("CONSUMERS PROCESS AT A SAFE RATE")

        queue = self.message_queue().move_to(UP * 3.0)
        consumer = self.consumer().move_to(DOWN * 2.65)

        self.play(
            FadeIn(title),
            FadeIn(queue),
            FadeIn(consumer),
            run_time=.7
        )

        path = self.vertical_arrow(queue, consumer, GOOD)
        self.play(Create(path), run_time=.7)

        messages = VGroup(
            self.message("MSG 1"),
            self.message("MSG 2"),
            self.message("MSG 3")
        ).arrange(DOWN, buff=.24)

        messages.scale(.88)
        messages.move_to(RIGHT * 2.15 + UP * .20)

        msg1, msg2, msg3 = messages

        self.play(FadeIn(msg1), run_time=.35)
        self.play(FadeIn(msg2), run_time=.35)
        self.play(FadeIn(msg3), run_time=.35)

        rate = Text(
            "CONTROLLED FLOW",
            font_size=27,
            color=GOOD,
            weight=BOLD
        ).next_to(consumer, DOWN, buff=.48)

        self.play(FadeIn(rate), run_time=.5)

        cap = self.caption(
            "QUEUED WORK CAN BE PROCESSED ACCORDING TO AVAILABLE CAPACITY"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B05 - ABSORB THE SPIKE
# ============================================================

class B05_AbsorbSpike(BrutalistScene):

    def construct(self):
        title = self.heading("LET THE QUEUE ABSORB THE SPIKE")

        queue = self.box(
            "MESSAGE QUEUE",
            width=6.4,
            height=1.75,
            color=ACCENT,
            font_size=26
        ).move_to(UP * 2.15)

        consumer = self.consumer().move_to(DOWN * 2.65)

        self.play(
            FadeIn(title),
            FadeIn(queue),
            FadeIn(consumer),
            run_time=.7
        )

        backlog = VGroup(*[
            self.message(f"M{i}")
            for i in range(1, 7)
        ]).arrange_in_grid(
            rows=2,
            cols=3,
            buff=(.16, .16)
        )

        backlog.scale(.78)

        queue_label = queue[1]
        queue_label.scale(.72)
        queue_label.move_to(queue.get_center() + UP * .58)

        backlog.move_to(queue.get_center() + DOWN * .25)

        self.play(
            LaggedStart(
                *[FadeIn(msg) for msg in backlog],
                lag_ratio=.08
            ),
            run_time=.9
        )

        path = self.vertical_arrow(queue, consumer, GOOD)
        self.play(Create(path), run_time=.7)

        buffered = Text(
            "BACKLOG BUFFERED",
            font_size=25,
            color=ACCENT,
            weight=BOLD
        ).next_to(queue, DOWN, buff=.48)

        safe = Text(
            "STEADY INPUT",
            font_size=23,
            color=GOOD,
            weight=BOLD
        ).next_to(consumer, DOWN, buff=.48)

        self.play(FadeIn(buffered), FadeIn(safe), run_time=.6)

        cap = self.caption(
            "MESSAGES WAIT IN THE QUEUE INSTEAD OF ARRIVING ALL AT ONCE"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B06 - SCALE CONSUMERS
# ============================================================

class B06_ScaleConsumers(BrutalistScene):

    def construct(self):
        title = self.heading("ADD CONSUMERS AS WORKLOAD GROWS")

        queue = self.message_queue().move_to(UP * 3.35)

        consumers = VGroup(
            self.consumer("CONSUMER 1"),
            self.consumer("CONSUMER 2"),
            self.consumer("CONSUMER 3")
        ).arrange(DOWN, buff=.55)

        consumers.move_to(DOWN * 1.75)

        c1, c2, c3 = consumers

        self.play(
            FadeIn(title),
            FadeIn(queue),
            run_time=.7
        )

        self.play(
            LaggedStart(
                FadeIn(c1),
                FadeIn(c2),
                FadeIn(c3),
                lag_ratio=.15
            ),
            run_time=.8
        )

        a1 = Arrow(
            queue.get_bottom() + LEFT * 1.25,
            c1.get_top() + LEFT * 1.25,
            buff=.15,
            color=GOOD,
            stroke_width=4,
            max_tip_length_to_length_ratio=.12
        )

        a2 = Arrow(
            queue.get_bottom(),
            c2.get_top(),
            buff=.15,
            color=GOOD,
            stroke_width=4,
            max_tip_length_to_length_ratio=.12
        )

        a3 = Arrow(
            queue.get_bottom() + RIGHT * 1.25,
            c3.get_top() + RIGHT * 1.25,
            buff=.15,
            color=GOOD,
            stroke_width=4,
            max_tip_length_to_length_ratio=.12
        )

        self.play(
            LaggedStart(
                Create(a1),
                Create(a2),
                Create(a3),
                lag_ratio=.15
            ),
            run_time=1.2
        )

        scale = Text(
            "MORE PROCESSING CAPACITY",
            font_size=26,
            color=GOOD,
            weight=BOLD
        ).move_to(DOWN * 4.35)

        self.play(FadeIn(scale), run_time=.5)

        cap = self.caption(
            "PARALLEL CONSUMERS CAN INCREASE THROUGHPUT"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B07 - PAYOFF
# ============================================================

class B07_QueuePayoff(BrutalistScene):

    def construct(self):
        title = self.heading(
            "BUFFER THE SPIKE. KEEP SERVICES RESPONSIVE."
        )

        producer = self.producer().move_to(UP * 3.65)
        queue = self.message_queue().move_to(UP * .65)

        consumers = self.box(
            "CONSUMERS",
            width=5.5,
            height=1.15,
            color=FG,
            font_size=26
        ).move_to(DOWN * 2.35)

        self.play(
            FadeIn(title),
            FadeIn(producer),
            FadeIn(queue),
            FadeIn(consumers),
            run_time=.8
        )

        a1 = self.vertical_arrow(producer, queue, GOOD)
        a2 = self.vertical_arrow(queue, consumers, GOOD)

        self.play(Create(a1), Create(a2), run_time=.9)

        benefits = VGroup(
            Text(
                "BUFFER SPIKES",
                font_size=22,
                color=GOOD,
                weight=BOLD
            ),
            Text(
                "DECOUPLE SERVICES",
                font_size=22,
                color=GOOD,
                weight=BOLD
            ),
            Text(
                "STAY RESPONSIVE",
                font_size=22,
                color=GOOD,
                weight=BOLD
            )
        ).arrange(DOWN, buff=.22)

        benefits.move_to(DOWN * 4.35)

        self.play(FadeIn(benefits), run_time=.7)

        cap = self.caption(
            "QUEUES SMOOTH BURSTS AND SEPARATE PRODUCERS FROM CONSUMERS"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(1)
