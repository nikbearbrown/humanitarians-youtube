"""scenes.py — Manim scenes for accountability-mesh (claude-divij).

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757, soft #73705F, ghost #A9A491.
Type: Montserrat (DISPLAY, structural default) / EB Garamond (SERIF, editorial
voice only) / PT Mono (MONO, data+code only) — see graphics_lib.py. Boxes are
sized to their actual content via auto_box/surround_box, never hand-measured.
Pace: normal-speed creates/fades (0.3-0.8s) with deliberate HOLDS between story
beats sized to the narration's actual pacing — never a stretched/slowed
transition. Each scene's total runtime is tuned to land close to its beat's
audio duration so compile.py's crop step does not need to time-stretch it.
Negative space: ~15-35%, title at top, main diagram centered.
"""
import numpy as np
from graphics_lib import *

# ── Palette (claude-stage retint, per ai-explainer SKILL.md) ──────────────────
BG    = ManimColor("#F2F0E9")   # claude cream
INK   = ManimColor("#3D3929")   # warm ink — primary text / original
ACC   = ManimColor("#D97757")   # terracotta — accent, rejection, error
SOFT  = ManimColor("#73705F")   # secondary text
GHOST = ManimColor("#A9A491")   # dimmed, placeholder, muted


# ─────────────────────────────────────────────────────────────────────────────
#  B01_TheMesh   (target ~20.5s of 21.53s audio)
#  Agent node (left) → gate (middle) → Investor node (right).
#  Three labels light up on the gate: Sourced / Permanent / Checkable.
# ─────────────────────────────────────────────────────────────────────────────
class B01_TheMesh(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("The Accountability Mesh", color=INK)
        self.play(Write(t), run_time=0.5)
        self.wait(0.3)

        agent_node = Circle(radius=0.65, color=INK, stroke_width=3).move_to(LEFT * 4.5)
        agent_chip = label_chip("Agent", INK).next_to(agent_node, DOWN, buff=0.35)

        investor_node = Circle(radius=0.65, color=INK, stroke_width=3).move_to(RIGHT * 4.5)
        investor_chip = label_chip("Investor", INK).next_to(investor_node, DOWN, buff=0.35)

        self.play(Create(agent_node), FadeIn(agent_chip), run_time=0.5)
        self.play(Create(investor_node), FadeIn(investor_chip), run_time=0.5)
        self.wait(0.4)

        arrow_line = Line(
            agent_node.get_right() + RIGHT * 0.2,
            investor_node.get_left() + LEFT * 0.2,
            color=SOFT, stroke_width=2.5
        )
        self.play(Create(arrow_line), run_time=0.5)
        self.wait(0.3)

        properties = ["Sourced", "Permanent", "Checkable"]
        prop_texts = VGroup(*[label(p, size=28, color=SOFT) for p in properties]).arrange(
            DOWN, buff=0.32).move_to(UP * 0.05)
        gate_rect = auto_box(prop_texts, h_pad=0.55, v_pad=0.5, color=GHOST, fill_color=GHOST, fill_opacity=0.1)
        gate_label_main = label("GATE", size=24, color=GHOST, weight="BOLD").next_to(gate_rect, UP, buff=0.3)

        self.play(Create(gate_rect), FadeIn(gate_label_main), run_time=0.5)
        self.wait(0.5)

        for prop_text in prop_texts:
            self.play(FadeIn(prop_text), run_time=0.4)
            self.wait(1.0)

        self.wait(0.5)

        for prop_text in prop_texts:
            self.play(prop_text.animate.set_color(ACC), run_time=0.4)
            self.wait(1.2)

        self.play(
            gate_rect.animate.set_color(ACC).set_stroke(width=3.5),
            gate_label_main.animate.set_color(ACC),
            run_time=0.6
        )
        self.wait(0.6)

        conclusion = Circle(radius=0.32, color=ACC, fill_color=ACC, fill_opacity=1.0, stroke_width=0)
        conclusion.move_to(agent_node.get_right() + RIGHT * 0.3)
        conclusion_label = label("Conclusion", size=24, color=ACC).next_to(conclusion, UP, buff=0.2)

        self.play(FadeIn(conclusion), FadeIn(conclusion_label), run_time=0.4)
        self.play(
            conclusion.animate.move_to(investor_node.get_left() + LEFT * 0.3),
            conclusion_label.animate.next_to(
                conclusion.copy().move_to(investor_node.get_left() + LEFT * 0.3),
                UP, buff=0.2
            ),
            run_time=2.5
        )
        self.wait(2.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_NakedConclusion   (target ~38.4s of 40.79s audio)
#  Four agents, one flagged as hallucinated, funnel into an unsourced grade,
#  then a "why?" exchange visualizing the AI's confident rationalization.
# ─────────────────────────────────────────────────────────────────────────────
class B02_NakedConclusion(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("The Problem: The Naked Conclusion", color=INK)
        self.play(Write(t), run_time=0.5)
        self.wait(0.3)

        agents = ["Financials", "Patents", "Earnings", "Competition"]
        agent_positions = [
            LEFT * 4.5 + UP * 0.5,
            LEFT * 1.5 + UP * 0.5,
            RIGHT * 1.5 + UP * 0.5,
            RIGHT * 4.5 + UP * 0.5,
        ]

        agent_nodes = []
        for agent_name, pos in zip(agents, agent_positions):
            node = Circle(radius=0.5, color=INK, stroke_width=2.5).move_to(pos)
            lbl = label(agent_name, size=24, color=INK).next_to(node, DOWN, buff=0.3)
            agent_nodes.append((node, lbl))
        self.play(LaggedStart(*[Create(n) for n, _ in agent_nodes], lag_ratio=0.2), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(l) for _, l in agent_nodes], lag_ratio=0.2), run_time=0.8)
        self.wait(0.3)

        # ── One agent at a time gets a brief highlight pulse, matching the
        #    narration naming each of the four in turn ─────────────────────
        for node, _ in agent_nodes:
            self.play(Indicate(node, color=ACC, scale_factor=1.2), run_time=0.5)
            self.wait(1.0)

        self.wait(1.0)

        flag_node, flag_label_text = agent_nodes[0]
        flag_chip = label_chip("hallucinated", ACC, size=20).next_to(flag_label_text, DOWN, buff=0.3)

        self.play(FadeIn(flag_chip), run_time=0.5)
        self.wait(2.0)

        nothing_stops = label("nothing catches it", size=26, color=ACC).next_to(flag_chip, DOWN, buff=0.3)
        self.play(FadeIn(nothing_stops), run_time=0.4)
        self.wait(2.0)

        funnel_top_y = -1.0
        funnel_bottom_y = -2.4
        funnel_width_top = 3.8
        funnel_width_bottom = 0.9

        arrows = []
        for arrow_x in [pos[0] for pos in agent_positions]:
            arrow = Line(
                [arrow_x, agent_positions[0][1] - 1.15, 0],
                [arrow_x * 0.3, funnel_top_y, 0],
                color=SOFT, stroke_width=2.0
            )
            arrows.append(arrow)
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.2), run_time=1.0)
        self.wait(0.5)

        funnel = Polygon(
            np.array([LEFT[0] * funnel_width_top / 2, funnel_top_y, 0]),
            np.array([RIGHT[0] * funnel_width_top / 2, funnel_top_y, 0]),
            np.array([RIGHT[0] * funnel_width_bottom / 2, funnel_bottom_y, 0]),
            np.array([LEFT[0] * funnel_width_bottom / 2, funnel_bottom_y, 0]),
            color=GHOST, stroke_width=2.0, fill_color=GHOST, fill_opacity=0.05
        )
        self.play(Create(funnel), run_time=0.6)
        self.wait(0.8)

        output_lines = VGroup(
            mono("GRADE: SELL", size=30, color=INK, weight="BOLD"),
            label("(no source)", size=22, color=ACC),
        ).arrange(DOWN, buff=0.12)
        output_card = auto_box(output_lines, h_pad=0.45, v_pad=0.32, color=INK, fill_color=INK, fill_opacity=0.08)
        VGroup(output_card, output_lines).move_to([0, funnel_bottom_y - 1.0, 0])

        self.play(Create(output_card), FadeIn(output_lines), run_time=0.8)
        self.wait(3.5)

        # ── Clear the stage entirely before the rationalizer exchange — a
        #    fresh, uncluttered frame for the next beat of the story ─────────
        self.play(
            FadeOut(t),
            *[FadeOut(n) for n, _ in agent_nodes], *[FadeOut(l) for _, l in agent_nodes],
            FadeOut(flag_chip), FadeOut(nothing_stops),
            *[FadeOut(a) for a in arrows], FadeOut(funnel),
            FadeOut(output_card), FadeOut(output_lines),
            run_time=0.6
        )
        self.wait(0.2)

        # ── The rationalizer: ask the AI why, get a confident invented reason ─
        question_text = label("Why?", size=30, color=SOFT)
        question_bubble = auto_box(question_text, h_pad=0.4, v_pad=0.28, color=SOFT,
                                    fill_color=SOFT, fill_opacity=0.05)
        VGroup(question_bubble, question_text).move_to(UP * 1.3)
        self.play(FadeIn(question_bubble), FadeIn(question_text), run_time=0.5)
        self.wait(1.2)

        response_text = serif('"Market conditions shifted..."', size=32, color=ACC, italic=True)
        response_bubble = auto_box(response_text, h_pad=0.55, v_pad=0.35, color=ACC,
                                    fill_color=ACC, fill_opacity=0.06)
        VGroup(response_bubble, response_text).move_to(DOWN * 0.4)
        self.play(FadeIn(response_bubble), FadeIn(response_text), run_time=0.6)
        self.wait(4.5)

        invented_label = label(
            "confident, coherent — and invented", size=24, color=SOFT
        ).next_to(response_bubble, DOWN, buff=0.5)
        self.play(FadeIn(invented_label), run_time=0.5)
        self.wait(5.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B03_RejectedApproaches   (target ~27.1s of 28.54s audio)
#  Two-row table (LLM Judge / Gradient Inversion). Each row gets an X mark,
#  held long enough to cover its (longer) rejection reason.
# ─────────────────────────────────────────────────────────────────────────────
class B03_RejectedApproaches(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("What Didn't Work", color=INK)
        self.play(Write(t), run_time=0.5)
        self.wait(0.4)

        approaches = [
            ("LLM Judge", "same blind spot as the agent", 5.5),
            ("Gradient Inversion", "forces you off frontier models", 8.0),
        ]

        y_positions = [UP * 0.8, DOWN * 0.9]

        for (approach, reason, hold), y_pos in zip(approaches, y_positions):
            approach_chip = label_chip(approach, INK, size=24).move_to(y_pos + LEFT * 3.6)
            x_mark = Text("✕", font_size=44, color=ACC).move_to(y_pos + LEFT * 0.9)
            reason_text = label(reason, size=26, color=ACC).move_to(y_pos + RIGHT * 2.0)

            # Box sized to the row's actual content (chip + mark + reason),
            # never a hand-measured fixed width — the reason text length
            # varies per row and a fixed box will clip the longer one.
            row_box = auto_box(
                VGroup(approach_chip, x_mark, reason_text), h_pad=0.5, v_pad=0.3,
                color=SOFT, fill_color=SOFT, fill_opacity=0.05
            )

            self.play(Create(row_box), run_time=0.4)
            self.play(FadeIn(approach_chip), run_time=0.35)
            self.wait(0.5)
            self.play(FadeIn(x_mark, scale=1.5), run_time=0.4)
            self.wait(0.8)
            self.play(FadeIn(reason_text), run_time=0.4)
            self.wait(hold)

        self.wait(1.0)

        closing = label("Neither actually worked", size=30, color=SOFT, weight="BOLD").to_edge(DOWN, buff=0.6)
        self.play(FadeIn(closing), run_time=0.5)
        self.wait(4.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_ThreeMechanisms   (target ~56.7s of 59.71s audio)
#  Three nodes, each unpacked field by field as the narration lists them —
#  this is the densest beat, so each mechanism gets its own multi-step reveal
#  instead of one name+description flash.
# ─────────────────────────────────────────────────────────────────────────────
class B04_ThreeMechanisms(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Three Mechanisms", color=INK)
        self.play(Write(t), run_time=0.5)
        self.wait(0.3)

        node_positions = [LEFT * 4.0, ORIGIN, RIGHT * 4.0]
        names = ["Reasoning Object", "Checkpointing", "Adversarial\nArbitration"]

        nodes = [Circle(radius=0.65, color=GHOST, stroke_width=2.5).move_to(p) for p in node_positions]
        self.play(LaggedStart(*[Create(n) for n in nodes], lag_ratio=0.25), run_time=0.8)
        self.wait(0.4)

        # ── Mechanism 1: ReasoningObject — unpack the affidavit's questions ──
        node1 = nodes[0]
        self.play(node1.animate.set_color(ACC).set_stroke(width=3.0), run_time=0.5)
        chip1 = label_chip(names[0], ACC, size=22).next_to(node1, UP, buff=0.3)
        self.play(FadeIn(chip1), run_time=0.4)
        self.wait(0.6)

        fields1 = ["What did you conclude?", "How confident?", "Exact source line?", "Citations?"]
        field_group1 = VGroup()
        for i, f in enumerate(fields1):
            ftext = label(f, size=24, color=ACC).move_to(node1.get_center() + DOWN * (1.1 + i * 0.4))
            self.play(FadeIn(ftext), run_time=0.35)
            self.wait(2.0)
            field_group1.add(ftext)

        rejected1 = label("no source → rejected outright", size=22, color=SOFT).move_to(
            node1.get_center() + DOWN * 2.9)
        self.play(FadeIn(rejected1), run_time=0.4)
        self.wait(2.5)
        self.play(FadeOut(field_group1), FadeOut(rejected1), run_time=0.4)

        # ── Mechanism 2: Checkpointing — the append-only guarantee ──────────
        node2 = nodes[1]
        self.play(node2.animate.set_color(ACC).set_stroke(width=3.0), run_time=0.5)
        chip2 = label_chip(names[1], ACC, size=22).next_to(node2, UP, buff=0.3)
        self.play(FadeIn(chip2), run_time=0.4)
        self.wait(0.6)

        rule2 = mono("no UPDATE · no DELETE", size=24, color=ACC).move_to(node2.get_center() + DOWN * 1.1)
        self.play(FadeIn(rule2), run_time=0.4)
        self.wait(3.5)

        enforce2 = label("enforced by the database,\nnot the app code", size=22, color=SOFT).move_to(
            node2.get_center() + DOWN * 1.85)
        self.play(FadeIn(enforce2), run_time=0.4)
        self.wait(4.5)

        flags_text = label("flags", size=22, color=SOFT)
        flag_table = auto_box(flags_text, h_pad=0.3, v_pad=0.22, color=GHOST)
        VGroup(flag_table, flags_text).move_to(node2.get_center() + DOWN * 2.75 + RIGHT * 2.0)
        dashed_link = DashedLine(node2.get_bottom() + DOWN * 1.9, flag_table.get_left(), color=GHOST, stroke_width=1.5)
        self.play(Create(dashed_link), Create(flag_table), FadeIn(flags_text), run_time=0.5)
        self.wait(4.5)

        recon2 = label("always reconstructable", size=22, color=SOFT).move_to(node2.get_center() + DOWN * 2.75 + LEFT * 2.0)
        self.play(FadeIn(recon2), run_time=0.4)
        self.wait(3.5)
        self.play(
            FadeOut(rule2), FadeOut(enforce2), FadeOut(dashed_link), FadeOut(flag_table),
            FadeOut(flags_text), FadeOut(recon2), run_time=0.4
        )

        # ── Mechanism 3: Adversarial Arbitration — debate, then a first-class
        #    disagreement instead of a silent average ──────────────────────
        node3 = nodes[2]
        self.play(node3.animate.set_color(ACC).set_stroke(width=3.0), run_time=0.5)
        chip3 = label_chip(names[2], ACC, size=22).next_to(node3, UP, buff=0.3)
        self.play(FadeIn(chip3), run_time=0.4)
        self.wait(0.6)

        figA = Triangle(color=ACC, fill_color=ACC, fill_opacity=1.0, stroke_width=0).scale(0.2).move_to(
            node3.get_center() + DOWN * 1.1 + LEFT * 0.55)
        figB = Triangle(color=SOFT, fill_color=SOFT, fill_opacity=1.0, stroke_width=0).scale(0.2).move_to(
            node3.get_center() + DOWN * 1.1 + RIGHT * 0.55)
        self.play(FadeIn(figA), FadeIn(figB), run_time=0.5)
        self.wait(0.8)

        debate_arrow1 = Arrow(figA.get_center(), figB.get_center(), color=GHOST, stroke_width=2, buff=0.3,
                               max_tip_length_to_length_ratio=0.2)
        debate_arrow2 = Arrow(figB.get_center(), figA.get_center(), color=GHOST, stroke_width=2, buff=0.3,
                               max_tip_length_to_length_ratio=0.2).shift(DOWN * 0.2)
        debate_label = label("debate once", size=22, color=SOFT).move_to(node3.get_center() + DOWN * 1.75)
        self.play(GrowArrow(debate_arrow1), GrowArrow(debate_arrow2), FadeIn(debate_label), run_time=0.6)
        self.wait(3.5)

        affidavit_text = label("Affidavit of Disagreement", size=22, color=ACC, weight="BOLD")
        affidavit_card = auto_box(affidavit_text, h_pad=0.4, v_pad=0.28, color=ACC)
        VGroup(affidavit_card, affidavit_text).move_to(node3.get_center() + DOWN * 2.5)
        self.play(Create(affidavit_card), FadeIn(affidavit_text), run_time=0.5)
        self.wait(4.0)

        not_avg = label("not a silent average", size=22, color=SOFT).next_to(affidavit_card, DOWN, buff=0.25)
        self.play(FadeIn(not_avg), run_time=0.4)
        self.wait(4.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B05_ValidationLoop   (target ~40.0s of 42.13s audio)
#  The rule → request → response → parser → verdict → permanent ledger,
#  run twice, then the halt branch. A short intro states the structural
#  requirement before Attempt 1 begins.
# ─────────────────────────────────────────────────────────────────────────────
class B05_ValidationLoop(Scene):

    def _ledger(self):
        label_text = label("LEDGER", size=24, color=SOFT, weight="BOLD")
        box = Rectangle(width=2.9, height=3.4, color=INK, stroke_width=1.8).move_to(RIGHT * 4.6 + DOWN * 0.3)
        label_text.move_to(box.get_top() + DOWN * 0.4)
        return box, label_text

    def construct(self):
        self.camera.background_color = BG

        # ── Intro: the structural rule ───────────────────────────────────────
        intro_title = title("The Rule", color=INK)
        self.play(Write(intro_title), run_time=0.5)
        self.wait(0.3)

        rule_text = mono("<thought_log> + <conclusion> — nothing else", size=26, color=INK)
        rule_card = auto_box(rule_text, h_pad=0.5, v_pad=0.35, color=INK, fill_color=INK, fill_opacity=0.04)
        self.play(Create(rule_card), FadeIn(rule_text), run_time=0.5)
        self.wait(2.5)
        self.play(FadeOut(intro_title), FadeOut(rule_card), FadeOut(rule_text), run_time=0.4)
        self.wait(0.2)

        # ── Attempt 1: the polite request ───────────────────────────────────
        t1 = title("Attempt 1: The Polite Request", color=INK)
        self.play(Write(t1), run_time=0.5)
        self.wait(0.3)

        ledger_box, ledger_label = self._ledger()
        self.play(Create(ledger_box), FadeIn(ledger_label), run_time=0.4)
        entry_y = ledger_box.get_top()[1] - 0.75

        request_text = label('"Please format like this"', size=24, color=SOFT)
        request_card = auto_box(request_text, h_pad=0.4, v_pad=0.3, color=SOFT, fill_color=SOFT, fill_opacity=0.05)
        VGroup(request_card, request_text).move_to(LEFT * 3.0 + UP * 1.5)
        self.play(Create(request_card), FadeIn(request_text), run_time=0.4)
        self.wait(1.0)

        preamble_line = label("Here's my thought process:", size=22, color=ACC)
        tag_line = mono("<thought_log> ...", size=24, color=INK)
        response_text = VGroup(preamble_line, tag_line).arrange(DOWN, buff=0.16)
        response_card = auto_box(response_text, h_pad=0.45, v_pad=0.35, color=INK, fill_color=INK, fill_opacity=0.04)
        VGroup(response_card, response_text).move_to(LEFT * 3.0 + DOWN * 0.7)

        send_arrow = Arrow(request_card.get_bottom(), response_card.get_top(), color=SOFT,
                            stroke_width=2.5, buff=0.05, max_tip_length_to_length_ratio=0.15)
        self.play(GrowArrow(send_arrow), run_time=0.35)
        self.play(Create(response_card), FadeIn(response_text), run_time=0.5)
        self.wait(1.2)

        glass_circle = Circle(radius=0.3, color=INK, stroke_width=3).move_to(preamble_line.get_left() + LEFT * 0.65)
        glass_handle = Line(ORIGIN, DOWN * 0.35 + RIGHT * 0.25, color=INK, stroke_width=3)
        glass_handle.move_to(glass_circle.get_bottom() + DOWN * 0.15 + RIGHT * 0.12)
        glass = VGroup(glass_circle, glass_handle)

        self.play(FadeIn(glass), run_time=0.3)
        self.play(glass.animate.move_to(preamble_line.get_left() + LEFT * 0.6), run_time=0.7)
        self.wait(0.5)

        x_mark = Text("✕", font_size=30, color=ACC).move_to(glass_circle.get_center())
        self.play(FadeOut(glass_handle), Transform(glass_circle, x_mark), run_time=0.4)
        self.wait(0.3)

        fail_text = label("PARSE_FAILURE", size=24, color=ACC, weight="BOLD")
        fail_stamp = auto_box(fail_text, h_pad=0.35, v_pad=0.22, color=ACC, stroke_width=2.5)
        VGroup(fail_stamp, fail_text).move_to(response_card.get_right() + RIGHT * 2.2)
        self.play(Create(fail_stamp), FadeIn(fail_text), run_time=0.4)
        self.wait(1.5)

        entry1 = VGroup(fail_stamp.copy(), fail_text.copy())
        self.play(entry1.animate.scale(0.5).move_to(RIGHT * 4.6 + UP * entry_y), run_time=0.7)
        self.wait(0.5)

        self.play(
            FadeOut(t1), FadeOut(request_card), FadeOut(request_text), FadeOut(send_arrow),
            FadeOut(response_card), FadeOut(response_text), FadeOut(glass_circle),
            FadeOut(fail_stamp), FadeOut(fail_text),
            run_time=0.5
        )
        self.wait(0.2)

        # ── Attempt 2: the mechanical fix ───────────────────────────────────
        t2 = title("Attempt 2: The Mechanical Fix", color=INK)
        self.play(Write(t2), run_time=0.5)
        self.wait(0.3)

        request_text2 = mono('First char must be "<"', size=24, color=ACC)
        request_card2 = auto_box(request_text2, h_pad=0.4, v_pad=0.3, color=ACC, fill_color=ACC, fill_opacity=0.05)
        VGroup(request_card2, request_text2).move_to(LEFT * 3.0 + UP * 1.5)
        self.play(Create(request_card2), FadeIn(request_text2), run_time=0.4)
        self.wait(1.0)

        tag_line2 = mono("<thought_log> ...", size=24, color=INK)
        response_card2 = auto_box(tag_line2, h_pad=0.45, v_pad=0.35, color=INK, fill_color=INK, fill_opacity=0.04)
        VGroup(response_card2, tag_line2).move_to(LEFT * 3.0 + DOWN * 0.7)

        send_arrow2 = Arrow(request_card2.get_bottom(), response_card2.get_top(), color=ACC,
                             stroke_width=2.5, buff=0.05, max_tip_length_to_length_ratio=0.15)
        self.play(GrowArrow(send_arrow2), run_time=0.3)
        self.play(Create(response_card2), FadeIn(tag_line2), run_time=0.45)
        self.wait(1.2)

        glass_circle2 = Circle(radius=0.3, color=INK, stroke_width=3).move_to(tag_line2.get_left() + LEFT * 0.65)
        glass_handle2 = Line(ORIGIN, DOWN * 0.35 + RIGHT * 0.25, color=INK, stroke_width=3)
        glass_handle2.move_to(glass_circle2.get_bottom() + DOWN * 0.15 + RIGHT * 0.12)
        glass2 = VGroup(glass_circle2, glass_handle2)

        self.play(FadeIn(glass2), run_time=0.3)
        self.play(glass2.animate.move_to(tag_line2.get_center() + RIGHT * 0.9), run_time=0.7)
        self.wait(0.5)

        check_mark = Text("✓", font_size=30, color=ACC).move_to(glass_circle2.get_center())
        self.play(FadeOut(glass_handle2), Transform(glass_circle2, check_mark), run_time=0.4)
        self.wait(0.3)

        success_text = label("Retry OK", size=24, color=ACC, weight="BOLD")
        success_stamp = auto_box(success_text, h_pad=0.35, v_pad=0.22, color=ACC, stroke_width=2.5)
        VGroup(success_stamp, success_text).move_to(response_card2.get_right() + RIGHT * 2.2)
        self.play(Create(success_stamp), FadeIn(success_text), run_time=0.4)
        self.wait(1.5)

        entry2 = VGroup(success_stamp.copy(), success_text.copy())
        entry_y2 = ledger_box.get_top()[1] - 1.55
        self.play(entry2.animate.scale(0.5).move_to(RIGHT * 4.6 + UP * entry_y2), run_time=0.7)
        both_kept = label("both kept —\nnothing erased", size=22, color=SOFT).move_to(
            RIGHT * 4.6 + UP * (entry_y2 - 0.9))
        self.play(FadeIn(both_kept), run_time=0.4)
        self.wait(2.0)

        self.play(
            FadeOut(t2), FadeOut(request_card2), FadeOut(request_text2), FadeOut(send_arrow2),
            FadeOut(response_card2), FadeOut(tag_line2), FadeOut(glass_circle2),
            FadeOut(success_stamp), FadeOut(success_text),
            run_time=0.5
        )
        self.wait(0.2)

        halt_title = title("If Attempt 2 Also Fails", color=INK)
        self.play(Write(halt_title), run_time=0.5)
        self.wait(0.3)

        halt_text = label("HaltError: No Grade Ships", size=32, color=ACC, weight="BOLD")
        halt_box = auto_box(halt_text, h_pad=0.6, v_pad=0.4, color=ACC, fill_color=ACC, fill_opacity=0.1)
        VGroup(halt_box, halt_text).move_to(LEFT * 1.2 + DOWN * 0.4)
        self.play(Create(halt_box), FadeIn(halt_text), run_time=0.6)
        self.wait(9.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B06_TheHonestLimit   (target ~54.6s of 57.45s audio)
#  Structure's three guarantees tick in; a REAL and a FABRICATED log both
#  pass the same checks; a black box stands for the model's real process,
#  unseen; the ADR-06 line lands and holds; a closing card states what the
#  system is and is not.
# ─────────────────────────────────────────────────────────────────────────────
class B06_TheHonestLimit(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("The Honest Limit", color=INK)
        self.play(Write(t), run_time=0.5)
        self.wait(0.3)

        # ── Intro: what structure alone guarantees ──────────────────────────
        guarantees_label = label("Enforces structure:", size=26, color=SOFT).move_to(UP * 1.7)
        self.play(FadeIn(guarantees_label), run_time=0.4)
        self.wait(0.5)

        ticks = ["log exists", "well-formed", "permanently recorded"]
        tick_objs = VGroup(*[checked(tx, size=26, color=INK) for tx in ticks]).arrange(
            DOWN, buff=0.22, aligned_edge=LEFT).next_to(guarantees_label, DOWN, buff=0.4)
        for tk in tick_objs:
            self.play(FadeIn(tk), run_time=0.35)
            self.wait(0.8)
        self.wait(0.4)

        self.play(FadeOut(guarantees_label), FadeOut(tick_objs), run_time=0.4)
        self.wait(0.2)

        # ── Two logs, side by side: real vs. fabricated ─────────────────────
        real_text = VGroup(
            mono("thought_log:", size=22, color=INK, weight="BOLD"),
            label("Revenue is unstable...", size=20, color=SOFT),
        ).arrange(DOWN, buff=0.14)
        real_chip = label_chip("REAL", INK, size=20)
        real_stack = VGroup(real_text, real_chip).arrange(DOWN, buff=0.22)
        real_card = auto_box(real_stack, h_pad=0.4, v_pad=0.3, color=INK, fill_color=INK, fill_opacity=0.04)
        VGroup(real_card, real_stack).move_to(LEFT * 3.1 + UP * 0.3)

        fake_text = VGroup(
            mono("thought_log:", size=22, color=INK, weight="BOLD"),
            label("Revenue is unstable...", size=20, color=SOFT),
        ).arrange(DOWN, buff=0.14)
        fake_chip = label_chip("FABRICATED", ACC, size=20)
        fake_stack = VGroup(fake_text, fake_chip).arrange(DOWN, buff=0.22)
        fake_card = auto_box(fake_stack, h_pad=0.4, v_pad=0.3, color=INK, fill_color=INK, fill_opacity=0.04)
        VGroup(fake_card, fake_stack).move_to(RIGHT * 3.1 + UP * 0.3)

        self.play(FadeIn(real_card), FadeIn(real_stack), run_time=0.5)
        self.play(FadeIn(fake_card), FadeIn(fake_stack), run_time=0.5)
        self.wait(1.0)

        checks_labels = ["Sourced", "Permanent", "Checkable"]
        real_checks = VGroup(*[checked(c, size=22, color=ACC) for c in checks_labels]).arrange(
            DOWN, buff=0.14, aligned_edge=LEFT).next_to(real_card, DOWN, buff=0.3)
        fake_checks = VGroup(*[checked(c, size=22, color=ACC) for c in checks_labels]).arrange(
            DOWN, buff=0.14, aligned_edge=LEFT).next_to(fake_card, DOWN, buff=0.3)

        self.play(FadeIn(real_checks), FadeIn(fake_checks), run_time=0.7)
        self.wait(1.0)

        same_label = label("every single check — identical on both", size=24, color=SOFT).move_to(DOWN * 3.3)
        self.play(FadeIn(same_label), run_time=0.5)
        self.wait(5.5)

        self.play(
            FadeOut(real_card), FadeOut(real_stack), FadeOut(real_checks),
            FadeOut(fake_card), FadeOut(fake_stack), FadeOut(fake_checks),
            FadeOut(same_label),
            run_time=0.5
        )
        self.wait(0.2)

        box_label = label("actual process", size=22, color=BG)
        question = label("?", size=54, color=BG, weight="BOLD")
        box_content = VGroup(box_label, question).arrange(DOWN, buff=0.25)
        box = Rectangle(width=box_content.width + 1.0, height=box_content.height + 0.7,
                         color=INK, fill_color=INK, fill_opacity=1.0, stroke_width=0)
        box.move_to(UP * 0.2)
        box_content.move_to(box.get_center())

        self.play(FadeIn(box), FadeIn(box_content), run_time=0.6)
        self.wait(1.5)

        unseen = label("no check looks inside", size=24, color=SOFT).next_to(box, DOWN, buff=0.45)
        self.play(FadeIn(unseen), run_time=0.5)
        self.wait(6.25)

        self.play(FadeOut(box), FadeOut(box_content), FadeOut(unseen), run_time=0.5)
        self.wait(0.2)

        adr_eyebrow = label("ADR-06", size=22, color=ACC, weight="BOLD")
        adr_lines = VGroup(
            label("The log is evidence", size=30, color=INK, weight="BOLD"),
            label("of OUTPUT,", size=30, color=INK, weight="BOLD"),
            label("not evidence of PROCESS.", size=30, color=INK, weight="BOLD"),
        ).arrange(DOWN, buff=0.18)
        adr_text = VGroup(adr_eyebrow, adr_lines).arrange(DOWN, buff=0.3)
        adr_box = auto_box(adr_text, h_pad=0.7, v_pad=0.55, color=INK, fill_color=INK, fill_opacity=0.04)
        VGroup(adr_box, adr_text).move_to(DOWN * 0.3)

        self.play(Create(adr_box), run_time=0.6)
        self.play(FadeIn(adr_text, shift=DOWN * 0.3), run_time=0.7)
        self.wait(12.0)

        # ── Closing card: what this is, and is not ───────────────────────────
        self.play(FadeOut(adr_box), FadeOut(adr_text), run_time=0.5)
        self.wait(0.2)

        line1 = serif("Not hallucination-prevention", size=28, color=SOFT, italic=True)
        line2 = serif("Not fact-verification", size=28, color=SOFT, italic=True)
        line3 = label("Structural enforcement — honest limit", size=28, color=ACC, weight="BOLD")
        closing_lines = VGroup(line1, line2, line3).arrange(DOWN, buff=0.4)
        closing_card = auto_box(closing_lines, h_pad=0.6, v_pad=0.5, color=SOFT, fill_color=SOFT, fill_opacity=0.04)
        VGroup(closing_card, closing_lines).move_to(DOWN * 0.2)

        self.play(Create(closing_card), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(line1), run_time=0.5)
        self.wait(2.0)
        self.play(FadeIn(line2), run_time=0.5)
        self.wait(2.0)
        self.play(FadeIn(line3), run_time=0.5)
        self.wait(6.5)
