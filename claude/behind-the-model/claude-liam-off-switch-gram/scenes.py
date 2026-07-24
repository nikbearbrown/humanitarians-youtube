"""
scenes.py — claude-liam-off-switch-gram
GRAM: Gradient-Routed Auxiliary Modules (Anthropic × AE Studio, July 2026)

Palette: Claude brand
  PAGE   #FAF9F5  cream ground
  INK    #3D3929  warm near-black
  SPARK  #D97757  terracotta — ONE accent per beat
  SOFT   #73705F  secondary text

One Manim scene per GRAPHIC beat (B01-B11).
Aspect: 1920×1080 (16:9), 30fps (run.sh passes -r 1920,1080).
"""

from manim import *
import numpy as np

# ── palette ──────────────────────────────────────────────────────────────────
PAGE   = "#FAF9F5"
INK    = "#3D3929"
SPARK  = "#D97757"
SOFT   = "#73705F"
GHOST  = "#A9A491"
BORDER = "#E5E2D9"

config.background_color = PAGE


# ── helper: caption stamp (bottom-right corner) ──────────────────────────────
def gram_caption(scene):
    cap = Text(
        "After Anthropic × AE Studio, GRAM / modular pretraining (2026)",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


# ─────────────────────────────────────────────────────────────────────────────
# B01 — Three Goals Must Hold Simultaneously
# ─────────────────────────────────────────────────────────────────────────────
class B01_ThreeGoals(Scene):
    def construct(self):
        dur = 13.74

        # Title
        title = Text("Three Goals. All at Once.", font_size=40, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.6)
        self.add(title)

        # Three goal nodes arranged in a wide triangle
        labels = [
            ("Surgical lock\nof dangerous knowledge", UP * 1.8),
            ("Trusted users\ncan still reach it", DOWN * 1.2 + LEFT * 3.5),
            ("General performance\nstays intact", DOWN * 1.2 + RIGHT * 3.5),
        ]
        icons_text = ["⚕", "🔑", "◉"]  # scalpel-ish, key, gauge

        nodes = []
        node_groups = []
        for i, (label, pos) in enumerate(labels):
            circ = Circle(radius=0.7, color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=2.5)
            circ.move_to(pos)
            icon = Text(icons_text[i], font_size=30, color=SOFT).move_to(pos)
            lbl  = Text(label, font_size=22, color=INK).next_to(circ, DOWN if i == 0 else UP, buff=0.15)
            if i == 1:
                lbl.next_to(circ, LEFT, buff=0.18)
            if i == 2:
                lbl.next_to(circ, RIGHT, buff=0.18)
            nodes.append(circ)
            node_groups.append(VGroup(circ, icon, lbl))

        # Connecting lines
        line01 = Line(labels[0][1], labels[1][1], color=BORDER, stroke_width=2)
        line02 = Line(labels[0][1], labels[2][1], color=BORDER, stroke_width=2)
        line12 = Line(labels[1][1], labels[2][1], color=BORDER, stroke_width=2)

        gram_caption(self)

        # Animate in
        self.play(
            *[Create(n) for n in nodes],
            *[Write(g[1]) for g in node_groups],
            *[Write(g[2]) for g in node_groups],
            run_time=1.5,
        )
        self.play(Create(line01), Create(line02), Create(line12), run_time=1.0)

        # Terracotta moment: all three glow
        self.wait(0.5)
        self.play(
            *[nodes[i].animate.set_stroke(SPARK, width=4).set_fill(SPARK, opacity=0.15) for i in range(3)],
            *[node_groups[i][1].animate.set_color(SPARK) for i in range(3)],
            run_time=1.2,
        )

        # Subtitle when all hold
        balance_label = Text("These three must hold simultaneously.", font_size=26, color=SPARK, slant=ITALIC)
        balance_label.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(balance_label), run_time=0.8)
        self.wait(dur - 5.0)


# ─────────────────────────────────────────────────────────────────────────────
# B02 — Why Today's Locks Leak
# ─────────────────────────────────────────────────────────────────────────────
class B02_OutputGuardLeak(Scene):
    def construct(self):
        dur = 19.43

        title = Text("Guards the Door, Not the Room", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        # Model blob (left-center)
        blob = RoundedRectangle(width=3.5, height=2.8, corner_radius=0.4,
                                color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=2.5)
        blob.shift(LEFT * 2.5)
        blob_label = Text("knowledge", font_size=26, color=INK).move_to(blob.get_center())
        blob_sub   = Text("(intact)", font_size=20, color=SOFT).next_to(blob_label, DOWN, buff=0.1)

        # Two gates on the right edge of blob
        gate_x = blob.get_right()[0] + 0.4
        gate_y1 = blob.get_center()[1] + 0.5
        gate_y2 = blob.get_center()[1] - 0.5

        gate1 = Rectangle(width=1.4, height=0.55, color=INK, fill_color=BORDER, fill_opacity=1, stroke_width=2)
        gate1.move_to([gate_x, gate_y1, 0])
        g1_lbl = Text("refusal training", font_size=17, color=INK).move_to(gate1.get_center())

        gate2 = Rectangle(width=1.4, height=0.55, color=INK, fill_color=BORDER, fill_opacity=1, stroke_width=2)
        gate2.move_to([gate_x, gate_y2, 0])
        g2_lbl = Text("classifiers", font_size=17, color=INK).move_to(gate2.get_center())

        # Jailbreak arrow that curves around and reaches the blob
        jailbreak_path = ArcBetweenPoints(
            start=[gate_x + 1.2, blob.get_center()[1], 0],
            end=blob.get_center() + RIGHT * 1.75,
            angle=-1.2,
            color=SPARK, stroke_width=3,
        )
        jb_label = Text("jailbreak", font_size=20, color=SPARK).next_to(jailbreak_path, RIGHT, buff=0.1)

        annotation = Text("knowledge intact underneath", font_size=22, color=SPARK, slant=ITALIC)
        annotation.to_edge(DOWN, buff=0.6)

        gram_caption(self)

        self.play(Create(blob), Write(blob_label), Write(blob_sub), run_time=1.2)
        self.play(Create(gate1), Write(g1_lbl), Create(gate2), Write(g2_lbl), run_time=1.0)
        self.wait(1.0)

        # Jailbreak appears — terracotta accent moment
        self.play(Create(jailbreak_path), Write(jb_label), run_time=1.5)
        self.play(blob.animate.set_fill(SPARK, opacity=0.12), FadeIn(annotation), run_time=0.8)
        self.wait(dur - 6.0)


# ─────────────────────────────────────────────────────────────────────────────
# B03 — Filtering is Blunt
# ─────────────────────────────────────────────────────────────────────────────
class B03_FilteringBlunt(Scene):
    def construct(self):
        dur = 19.07

        title = Text("One Setting, One Model — Expensive", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        # Dataset with filter removing a chunk
        dataset_rect = Rectangle(width=2.4, height=3.0, color=INK, fill_color=BORDER,
                                 fill_opacity=0.5, stroke_width=2)
        dataset_rect.shift(LEFT * 4.5 + UP * 0.2)
        dataset_lbl = Text("training\ndata", font_size=22, color=INK).move_to(dataset_rect.get_center())

        filter_chunk = Rectangle(width=2.0, height=0.7, color=SOFT, fill_color=SOFT,
                                 fill_opacity=0.35, stroke_width=2)
        filter_chunk.move_to(dataset_rect.get_center() + UP * 0.5)
        filter_lbl = Text("virology", font_size=17, color=SOFT).move_to(filter_chunk.get_center())
        filter_x = Cross(scale_factor=0.3, stroke_color=INK, stroke_width=3).move_to(filter_chunk.get_center())

        # Single model box
        model_box = RoundedRectangle(width=2.4, height=1.5, corner_radius=0.25,
                                     color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=2.5)
        model_box.shift(UP * 0.2)
        model_lbl = Text("ONE model", font_size=24, color=INK, weight=BOLD).move_to(model_box.get_center())
        arrow_to_model = Arrow(dataset_rect.get_right(), model_box.get_left(), color=INK, buff=0.1)

        # Two parallel stacks below with cost labels
        m_a = RoundedRectangle(width=2.2, height=1.1, corner_radius=0.2,
                               color=SOFT, fill_color=PAGE, fill_opacity=1, stroke_width=2)
        m_a.shift(DOWN * 2.2 + LEFT * 1.8)
        m_a_lbl = Text("Model A\nvirology-OFF", font_size=19, color=INK).move_to(m_a.get_center())
        cost_a   = Text("$$$", font_size=20, color=SOFT).next_to(m_a, RIGHT, buff=0.15)

        m_b = RoundedRectangle(width=2.2, height=1.1, corner_radius=0.2,
                               color=SOFT, fill_color=PAGE, fill_opacity=1, stroke_width=2)
        m_b.shift(DOWN * 2.2 + RIGHT * 1.8)
        m_b_lbl = Text("Model B\nvirology-ON", font_size=19, color=INK).move_to(m_b.get_center())
        cost_b   = Text("$$$", font_size=20, color=SOFT).next_to(m_b, RIGHT, buff=0.15)

        # X marks prohibitive cost
        big_x = Text("✕ prohibitively expensive", font_size=24, color=INK, slant=ITALIC)
        big_x.to_edge(DOWN, buff=0.5)

        gram_caption(self)

        self.play(Create(dataset_rect), Write(dataset_lbl), run_time=0.8)
        self.play(Create(filter_chunk), Write(filter_lbl), GrowFromCenter(filter_x), run_time=0.8)
        self.play(Create(arrow_to_model), GrowFromCenter(model_box), Write(model_lbl), run_time=1.0)
        self.wait(1.0)

        self.play(
            GrowFromCenter(m_a), Write(m_a_lbl), Write(cost_a),
            GrowFromCenter(m_b), Write(m_b_lbl), Write(cost_b),
            run_time=1.2,
        )
        self.play(Write(big_x), run_time=0.8)
        self.wait(dur - 6.0)


# ─────────────────────────────────────────────────────────────────────────────
# B04 — GRAM Structure
# ─────────────────────────────────────────────────────────────────────────────
class B04_GramStructure(Scene):
    def construct(self):
        dur = 16.38

        title = Text("Four Modules, One Model", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        module_colors = [SPARK, "#8B7355", SOFT, GHOST]
        module_names  = ["virology", "cybersecurity", "nuclear", "niche-code"]

        layers = []
        module_strips = []
        layer_ys = [1.5, 0.5, -0.5, -1.5]

        for i, y in enumerate(layer_ys):
            # Main layer rectangle
            rect = Rectangle(width=5.0, height=0.75, color=INK,
                             fill_color=BORDER, fill_opacity=0.6, stroke_width=2)
            rect.shift(LEFT * 1.5 + UP * y)
            lbl = Text(f"Transformer layer {i + 1}", font_size=19, color=INK).move_to(rect.get_center())
            layers.append(VGroup(rect, lbl))

            # Module strips (right side)
            strips = []
            for j, (mc, mn) in enumerate(zip(module_colors, module_names)):
                strip = Rectangle(width=1.4, height=0.18, color=mc,
                                  fill_color=mc, fill_opacity=0.7, stroke_width=1.5)
                strip.move_to([rect.get_right()[0] + 0.9, y + 0.27 - j * 0.19, 0])
                strips.append(strip)
            module_strips.append(strips)

        # Module name labels on the right
        name_labels = []
        right_x = layers[0][0].get_right()[0] + 2.1
        for j, (mc, mn) in enumerate(zip(module_colors, module_names)):
            lbl = Text(mn, font_size=17, color=mc, slant=ITALIC)
            lbl.move_to([right_x, layer_ys[0] + 0.27 - j * 0.19, 0])
            name_labels.append(lbl)

        gram_caption(self)

        # Animate layers in
        for g in layers:
            self.play(Create(g[0]), Write(g[1]), run_time=0.35)

        # Animate module strips
        self.play(
            *[Create(s) for row in module_strips for s in row],
            run_time=1.0,
        )
        self.play(*[Write(lbl) for lbl in name_labels], run_time=0.8)

        # Terracotta accent: highlight the structure
        brace_label = Text("auxiliary modules per category", font_size=21, color=SPARK, slant=ITALIC)
        brace_label.shift(RIGHT * 3.8 + DOWN * 2.2)
        self.play(FadeIn(brace_label), run_time=0.6)
        self.wait(dur - 5.5)


# ─────────────────────────────────────────────────────────────────────────────
# B05 — Gradient Routing (Two Passes)
# ─────────────────────────────────────────────────────────────────────────────
class B05_GradientRouting(Scene):
    def construct(self):
        dur = 15.91

        title = Text("Knowledge Pools Into Its Module", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        # LEFT panel — general text
        left_title = Text("general text", font_size=24, color=INK, weight=BOLD)
        left_title.shift(LEFT * 3.5 + UP * 2.2)

        left_layers = []
        for y in [1.2, 0.4, -0.4, -1.2]:
            r = Rectangle(width=3.0, height=0.6, color=INK, fill_color=BORDER,
                          fill_opacity=0.6, stroke_width=2).shift(LEFT * 3.5 + UP * y)
            arrow = Arrow(r.get_bottom(), r.get_bottom() + DOWN * 0.25,
                          color=INK, stroke_width=2, max_tip_length_to_length_ratio=0.3, buff=0)
            left_layers.append(VGroup(r, arrow))

        left_note = Text("whole network\nupdates", font_size=20, color=INK, slant=ITALIC)
        left_note.shift(LEFT * 3.5 + DOWN * 2.2)

        # RIGHT panel — virology text
        right_title = Text("virology text", font_size=24, color=SPARK, weight=BOLD)
        right_title.shift(RIGHT * 3.5 + UP * 2.2)

        right_layers_gray = []
        for y in [1.2, 0.4, -0.4, -1.2]:
            r = Rectangle(width=2.0, height=0.6, color=GHOST, fill_color=PAGE,
                          fill_opacity=1.0, stroke_width=1.5).shift(RIGHT * 2.8 + UP * y)
            right_layers_gray.append(r)

        # Virology module strip (active)
        viro_strip = Rectangle(width=1.2, height=2.4, color=SPARK, fill_color=SPARK,
                               fill_opacity=0.25, stroke_width=3)
        viro_strip.shift(RIGHT * 4.3 + UP * 0.0)
        viro_lbl = Text("virology\nmodule", font_size=17, color=SPARK).move_to(viro_strip.get_center())
        viro_arrow = Arrow(viro_strip.get_bottom(), viro_strip.get_bottom() + DOWN * 0.5,
                           color=SPARK, stroke_width=3, max_tip_length_to_length_ratio=0.3, buff=0)
        flow_lbl = Text("gradient\nflows here", font_size=17, color=SPARK, slant=ITALIC)
        flow_lbl.next_to(viro_arrow, DOWN, buff=0.1)

        frozen_lbl = Text("general weights\nfrozen", font_size=18, color=GHOST, slant=ITALIC)
        frozen_lbl.shift(RIGHT * 2.8 + DOWN * 2.2)

        divider = Line(UP * 3, DOWN * 3, color=BORDER, stroke_width=2)

        gram_caption(self)

        self.play(Write(left_title), Write(right_title), Create(divider), run_time=0.8)
        for g in left_layers:
            self.play(Create(g[0]), Create(g[1]), run_time=0.25)
        self.play(Write(left_note), run_time=0.5)
        self.wait(0.4)

        for r in right_layers_gray:
            self.play(Create(r), run_time=0.2)
        self.play(FadeIn(frozen_lbl), run_time=0.5)

        # Terracotta accent: virology module lights up
        self.play(
            GrowFromCenter(viro_strip), Write(viro_lbl),
            Create(viro_arrow), Write(flow_lbl),
            run_time=1.2,
        )
        self.wait(dur - 7.0)


# ─────────────────────────────────────────────────────────────────────────────
# B06 — The Off Switch
# ─────────────────────────────────────────────────────────────────────────────
class B06_OffSwitch(Scene):
    def construct(self):
        dur = 14.74

        title = Text("Delete the Module, Delete the Capability", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        # Small model stack (reuse B04 style)
        layer_ys = [1.0, 0.25, -0.5, -1.25]
        rects = []
        for y in layer_ys:
            r = Rectangle(width=4.0, height=0.6, color=INK,
                          fill_color=BORDER, fill_opacity=0.6, stroke_width=2)
            r.shift(LEFT * 1.0 + UP * y)
            rects.append(r)

        # Virology module strip (solid)
        viro = Rectangle(width=1.0, height=2.3, color=SPARK, fill_color=SPARK,
                         fill_opacity=0.3, stroke_width=2.5)
        viro.shift(RIGHT * 2.3 + UP * 0.12)
        viro_label = Text("virology\nmodule", font_size=18, color=SPARK).move_to(viro.get_center())

        # Dotted outline after deletion
        viro_ghost = DashedVMobject(
            Rectangle(width=1.0, height=2.3, color=GHOST, stroke_width=2),
            num_dashes=20,
        ).shift(RIGHT * 2.3 + UP * 0.12)
        gone_label = Text("capability\ngone", font_size=18, color=GHOST, slant=ITALIC)
        gone_label.move_to(viro_ghost.get_center())

        # OR branch: trusted deployment path
        or_divider = Line(DOWN * 0.2, DOWN * 0.2 + RIGHT * 4, color=BORDER, stroke_width=1.5)
        or_divider.to_edge(DOWN, buff=1.2)
        or_text = Text("OR — trusted deployment: module retained", font_size=20, color=SOFT)
        or_text.next_to(or_divider, DOWN, buff=0.1)
        key_icon = Text("🔑", font_size=26, color=SPARK).next_to(or_text, LEFT, buff=0.15)

        gram_caption(self)

        self.play(*[Create(r) for r in rects], run_time=0.8)
        self.play(GrowFromCenter(viro), Write(viro_label), run_time=0.8)
        self.wait(0.8)

        # Module slides out to the right and fades
        self.play(
            viro.animate.shift(RIGHT * 2.5).set_opacity(0),
            viro_label.animate.shift(RIGHT * 2.5).set_opacity(0),
            run_time=1.0,
        )
        self.play(Create(viro_ghost), FadeIn(gone_label), run_time=0.7)
        self.wait(0.5)

        # OR branch
        self.play(Create(or_divider), Write(or_text), Write(key_icon), run_time=0.8)
        self.wait(dur - 6.0)


# ─────────────────────────────────────────────────────────────────────────────
# B07 — One Run, Sixteen Configurations
# ─────────────────────────────────────────────────────────────────────────────
class B07_SixteenConfigs(Scene):
    def construct(self):
        dur = 10.41

        title = Text("One Run, Sixteen Configurations", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        module_names = ["virology", "cybersecurity", "nuclear", "niche-code"]

        # Four toggle switches row
        toggle_y = 1.6
        toggles = []
        for i, name in enumerate(module_names):
            x = -4.5 + i * 3.0
            track = Rectangle(width=1.4, height=0.5, color=INK, fill_color=BORDER,
                              fill_opacity=0.8, stroke_width=2).move_to([x, toggle_y, 0])
            knob_on  = Circle(radius=0.22, color=PAGE, fill_color=SPARK, fill_opacity=1,
                              stroke_width=1.5).move_to([x + 0.45, toggle_y, 0])
            label = Text(name, font_size=17, color=SOFT).next_to(track, DOWN, buff=0.12)
            toggles.append(VGroup(track, knob_on, label))

        self.play(*[GrowFromCenter(t) for t in toggles], run_time=0.8)

        # 4×4 grid of small cells
        cells = []
        cell_objects = []
        for row in range(4):
            for col in range(4):
                cell = Square(side_length=0.6, color=INK, fill_color=PAGE,
                              fill_opacity=1, stroke_width=1.5)
                cell.move_to([-2.7 + col * 0.75, 0.3 - row * 0.75, 0])
                cells.append(cell)
                cell_objects.append(cell)

        self.play(*[GrowFromCenter(c) for c in cells], run_time=0.6)

        # Fill cells one by one (fast)
        for i, cell in enumerate(cells):
            self.play(
                cell.animate.set_fill(BORDER, opacity=0.9),
                run_time=0.08,
            )

        # Big 16 appears
        num16 = Text("16", font_size=120, color=SPARK, weight=BOLD)
        num16.shift(RIGHT * 3.5 + DOWN * 0.5)
        label16 = Text("deployable configurations\nfrom one training run", font_size=22, color=INK)
        label16.next_to(num16, DOWN, buff=0.15)
        formula  = Text("2^4 = 16", font_size=28, color=SOFT, slant=ITALIC)
        formula.next_to(title, DOWN, buff=0.2)

        gram_caption(self)

        self.play(Write(formula), run_time=0.5)
        self.play(Write(num16), run_time=0.8)
        self.play(Write(label16), run_time=0.5)
        self.wait(dur - 5.5)


# ─────────────────────────────────────────────────────────────────────────────
# B08 — Test 1: Synthetic Stories
# ─────────────────────────────────────────────────────────────────────────────
class B08_Test1Stories(Scene):
    def construct(self):
        dur = 15.62

        title = Text("Test 1: GRAM ≈ From-Scratch Filtering", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        # Story cards on the left
        topics = ["animals", "food", "space", "sports"]
        topic_colors = [SOFT, GHOST, SOFT, GHOST]
        cards = []
        for i, (topic, tc) in enumerate(zip(topics, topic_colors)):
            card = Rectangle(width=2.0, height=0.7, color=INK, fill_color=BORDER,
                             fill_opacity=0.5, stroke_width=1.5)
            card.shift(LEFT * 4.0 + UP * (1.0 - i * 0.85))
            tag = Rectangle(width=0.9, height=0.35, color=tc, fill_color=tc,
                            fill_opacity=0.6, stroke_width=1).move_to(card.get_center())
            tag_lbl = Text(topic, font_size=14, color=INK).move_to(tag.get_center())
            cards.append(VGroup(card, tag, tag_lbl))

        # Bar groups on the right
        bar_y_start = 1.0
        groups_data = [
            ("topic A", 0.85, 0.82),
            ("topic B", 0.78, 0.79),
            ("topic C", 0.88, 0.87),
        ]
        bar_groups = []
        for i, (lbl_text, gram_h, filt_h) in enumerate(groups_data):
            x_base = 0.5 + i * 2.5
            y_base = -1.5
            bar_g = Rectangle(width=0.6, height=gram_h * 2, color=INK,
                              fill_color=BORDER, fill_opacity=0.9, stroke_width=1.5)
            bar_g.next_to([x_base - 0.35, y_base, 0], UP, buff=0)
            bar_f = Rectangle(width=0.6, height=filt_h * 2, color=SOFT,
                              fill_color=SOFT, fill_opacity=0.4, stroke_width=1.5)
            bar_f.next_to([x_base + 0.35, y_base, 0], UP, buff=0)
            lbl  = Text(lbl_text, font_size=17, color=INK).next_to([x_base, y_base - 0.1, 0], DOWN, buff=0.1)
            bar_groups.append(VGroup(bar_g, bar_f, lbl))

        # Legend
        legend_g = Rectangle(width=0.4, height=0.25, color=INK, fill_color=BORDER, fill_opacity=0.9, stroke_width=1.5)
        legend_g.shift(RIGHT * 3.5 + UP * 2.4)
        legend_g_lbl = Text("GRAM config", font_size=17, color=INK).next_to(legend_g, RIGHT, buff=0.1)
        legend_f = Rectangle(width=0.4, height=0.25, color=SOFT, fill_color=SOFT, fill_opacity=0.4, stroke_width=1.5)
        legend_f.shift(RIGHT * 3.5 + UP * 2.0)
        legend_f_lbl = Text("filtered baseline", font_size=17, color=SOFT).next_to(legend_f, RIGHT, buff=0.1)

        note = Text("each config ≈ from-scratch filtered model", font_size=21, color=SOFT, slant=ITALIC)
        note.to_edge(DOWN, buff=0.5)

        self.play(*[GrowFromCenter(c) for c in cards], run_time=0.8)
        self.play(*[GrowFromCenter(g) for g in bar_groups], run_time=0.8)
        self.play(
            FadeIn(legend_g), Write(legend_g_lbl),
            FadeIn(legend_f), Write(legend_f_lbl),
            run_time=0.5,
        )
        self.play(Write(note), run_time=0.6)
        self.wait(dur - 4.5)


# ─────────────────────────────────────────────────────────────────────────────
# B09 — Test 2: Real Domains + Attack Resistance
# ─────────────────────────────────────────────────────────────────────────────
class B09_Test2Attack(Scene):
    def construct(self):
        dur = 22.70

        title = Text("Removed vs Suppressed", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        col_l_x = -3.5
        col_r_x =  3.5
        base_y   = -1.8

        # Left column — GRAM (removed)
        gram_title = Text("GRAM (removed)", font_size=24, color=INK, weight=BOLD)
        gram_title.move_to([col_l_x, 2.5, 0])

        bar_gram_low = Rectangle(width=1.0, height=0.5, color=BORDER, fill_color=BORDER,
                                 fill_opacity=0.9, stroke_width=1.5)
        bar_gram_low.next_to([col_l_x, base_y, 0], UP, buff=0)
        lbl_gram_low = Text("capability\n(module deleted)", font_size=17, color=INK)
        lbl_gram_low.next_to(bar_gram_low, DOWN, buff=0.1)

        # Arrow: attacker fine-tunes
        attack_l = Arrow([col_l_x - 0.8, 0.5, 0], [col_l_x + 0.8, 0.5, 0],
                         color=SOFT, stroke_width=2.5)
        attack_l_lbl = Text("fine-tuning\nattack", font_size=17, color=SOFT)
        attack_l_lbl.next_to(attack_l, UP, buff=0.08)

        bar_gram_still_low = Rectangle(width=1.0, height=0.5, color=BORDER, fill_color=BORDER,
                                       fill_opacity=0.9, stroke_width=1.5)
        bar_gram_still_low.next_to([col_l_x + 1.6, base_y, 0], UP, buff=0)
        lbl_gram_holds = Text("still low\n(holds)", font_size=17, color=SOFT, slant=ITALIC)
        lbl_gram_holds.next_to(bar_gram_still_low, DOWN, buff=0.1)

        # Right column — Unlearning (suppressed)
        unlearn_title = Text("Unlearning (suppressed)", font_size=24, color=SPARK, weight=BOLD)
        unlearn_title.move_to([col_r_x, 2.5, 0])

        bar_unlearn_low = Rectangle(width=1.0, height=0.5, color=BORDER, fill_color=BORDER,
                                    fill_opacity=0.9, stroke_width=1.5)
        bar_unlearn_low.next_to([col_r_x - 0.8, base_y, 0], UP, buff=0)
        lbl_unlearn_low = Text("capability\n(suppressed)", font_size=17, color=INK)
        lbl_unlearn_low.next_to(bar_unlearn_low, DOWN, buff=0.1)

        attack_r = Arrow([col_r_x - 0.7, 0.5, 0], [col_r_x + 0.7, 0.5, 0],
                         color=SOFT, stroke_width=2.5)
        attack_r_lbl = Text("fine-tuning\nattack", font_size=17, color=SOFT)
        attack_r_lbl.next_to(attack_r, UP, buff=0.08)

        bar_unlearn_high = Rectangle(width=1.0, height=2.8, color=SPARK, fill_color=SPARK,
                                     fill_opacity=0.35, stroke_width=2.5)
        bar_unlearn_high.next_to([col_r_x + 0.8, base_y, 0], UP, buff=0)
        lbl_unlearn_restores = Text("restores!", font_size=20, color=SPARK, weight=BOLD)
        lbl_unlearn_restores.next_to(bar_unlearn_high, DOWN, buff=0.1)

        divider = Line(UP * 3, DOWN * 3, color=BORDER, stroke_width=1.5)

        gram_caption(self)

        self.play(Create(divider), Write(gram_title), Write(unlearn_title), run_time=0.8)
        self.play(
            GrowFromCenter(bar_gram_low), Write(lbl_gram_low),
            GrowFromCenter(bar_unlearn_low), Write(lbl_unlearn_low),
            run_time=0.8,
        )
        self.wait(0.5)
        self.play(
            Create(attack_l), Write(attack_l_lbl),
            Create(attack_r), Write(attack_r_lbl),
            run_time=0.8,
        )
        self.play(GrowFromCenter(bar_gram_still_low), Write(lbl_gram_holds), run_time=0.6)

        # Terracotta accent: unlearning snaps back
        self.play(GrowFromCenter(bar_unlearn_high), Write(lbl_unlearn_restores), run_time=0.8)
        self.wait(dur - 7.0)


# ─────────────────────────────────────────────────────────────────────────────
# B10 — Test 3: Scale
# ─────────────────────────────────────────────────────────────────────────────
class B10_ScaleLine(Scene):
    def construct(self):
        dur = 15.74

        title = Text("Gap Grows With Scale", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 1, 0.25],
            x_length=9,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 2},
            tips=False,
        ).shift(DOWN * 0.4)

        # X-axis labels: 50M and 5B only (7 model sizes)
        x_lbl_50m = Text("50M", font_size=19, color=SOFT).next_to(axes.c2p(0, 0), DOWN, buff=0.2)
        x_lbl_5b  = Text("5B",  font_size=19, color=SOFT).next_to(axes.c2p(6, 0), DOWN, buff=0.2)
        x_axis_title = Text("model size (parameters)", font_size=20, color=INK)
        x_axis_title.next_to(axes, DOWN, buff=0.5)
        y_axis_title = Text("capability score", font_size=20, color=INK)
        y_axis_title.rotate(PI / 2).next_to(axes, LEFT, buff=0.3)

        # Module-ON line (stays high): 7 points from 0 to 6
        on_pts = [(i, 0.82 + i * 0.02) for i in range(7)]
        on_pts = [(x, min(y, 0.96)) for x, y in on_pts]
        on_path_pts = [axes.c2p(p[0], p[1]) for p in on_pts]
        on_polyline = VMobject(color=INK, stroke_width=3)
        on_polyline.set_points_as_corners(on_path_pts)
        line_on = on_polyline

        # Module-OFF line (stays low) — drawn as a DashedVMobject manually
        off_pts = [(i, 0.45 - i * 0.055) for i in range(7)]
        off_pts = [(x, max(y, 0.08)) for x, y in off_pts]
        off_path_pts = [axes.c2p(p[0], p[1]) for p in off_pts]
        off_polyline = VMobject(color=SOFT, stroke_width=3)
        off_polyline.set_points_as_corners(off_path_pts)
        line_off = DashedVMobject(off_polyline, num_dashes=24, dashed_ratio=0.6)

        # Shaded gap region (terracotta fill)
        gap_points_top    = [axes.c2p(p[0], p[1]) for p in on_pts]
        gap_points_bottom = [axes.c2p(p[0], p[1]) for p in reversed(off_pts)]
        gap_polygon = Polygon(*gap_points_top, *gap_points_bottom,
                              fill_color=SPARK, fill_opacity=0.18,
                              stroke_width=0)

        # Labels
        on_lbl  = Text("module-ON", font_size=19, color=INK).next_to(axes.c2p(5.8, 0.96), RIGHT, buff=0.1)
        off_lbl = Text("module-OFF", font_size=19, color=SOFT).next_to(axes.c2p(5.8, 0.10), RIGHT, buff=0.1)
        gap_lbl = Text("growing gap →", font_size=19, color=SPARK, slant=ITALIC)
        gap_lbl.move_to(axes.c2p(4.5, 0.6))

        gram_caption(self)

        self.play(Create(axes), Write(x_lbl_50m), Write(x_lbl_5b),
                  Write(x_axis_title), Write(y_axis_title), run_time=0.8)
        self.play(Create(line_on), Create(line_off), run_time=1.2)
        self.play(FadeIn(gap_polygon), run_time=0.6)
        self.play(Write(on_lbl), Write(off_lbl), Write(gap_lbl), run_time=0.7)
        self.wait(dur - 5.5)


# ─────────────────────────────────────────────────────────────────────────────
# B11 — Honest Limits
# ─────────────────────────────────────────────────────────────────────────────
class B11_HonestLimits(Scene):
    def construct(self):
        dur = 19.52

        title = Text("Three Caveats. Stated Plainly.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.add(title)

        # Faded GRAM background (simplified)
        bg_rects = []
        for y in [0.6, 0.0, -0.6]:
            r = Rectangle(width=7.0, height=0.45, color=BORDER, fill_color=BORDER,
                          fill_opacity=0.4, stroke_width=1)
            r.shift(UP * y)
            bg_rects.append(r)

        self.play(*[FadeIn(r) for r in bg_rects], run_time=0.5)

        caveat_texts = [
            "not in any production Claude model",
            "tested to 5B params — next-token metric only",
            "some knowledge may be inseparable",
        ]
        stamp_cards = []
        for i, txt in enumerate(caveat_texts):
            card = Rectangle(width=8.0, height=0.95, color=INK, fill_color=PAGE,
                             fill_opacity=1.0, stroke_width=2)
            card.shift(UP * (0.8 - i * 1.1) + LEFT * 0.0)
            card_lbl = Text(txt, font_size=25, color=INK).move_to(card.get_center())
            stamp_cards.append(VGroup(card, card_lbl))

        for card_group in stamp_cards:
            self.play(
                card_group.animate.move_to(card_group.get_center()),
                GrowFromCenter(card_group[0]),
                Write(card_group[1]),
                run_time=0.9,
            )
            self.wait(0.6)

        # End holding on caveat 3
        self.wait(dur - 6.0)
