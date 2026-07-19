# Chapter 10 — The Look

## Overview

The lecture side of Unreal Reels has a different job from the reels side. A reel is a short film; a lecture is a narrated deck that must hold attention for twenty or forty minutes while a voice explains something hard. The failure modes are not bad frames — they are incoherence and stillness. This chapter is about the design system that fixes both: a small, opinionated constitution that makes every slide look like it belongs to the same lecture, and one motion rule that keeps the screen alive while the narration runs.

The system is deliberately austere. It is called *brutalist* because it strips away everything decorative and lets typography and motion do the work. The governing principle is a single sentence: every mark earns its place by serving the spoken point. Color does not carry meaning; the words and the movement do. If a slide element does not answer a question the viewer has at that moment, it is cut. This is the same curation discipline you met on the reels side (Chapter 3), pointed at a screen full of text instead of a generated frame.

Two things make the look cohere. The first is a tiny palette and a three-role type system, so nothing on screen is ever an arbitrary choice. The second is the rule that governs motion — the one that separates a lecture video from a screen-recording of somebody's slides. Get both right and the video looks authored even though a pipeline built it.

Everything here is free and open-source ✅: the fonts, the renderer (Remotion), the math typesetter (KaTeX). There is no paid dependency in the look at all.

## One red, warm ink, and no blue

The complete palette is six values, and you are meant to feel constrained by it. There is exactly **one red — `#C8102E`** — and it means one thing: the brand, and the single data point of interest. The filled dot on a chart, the bullet that is the punchline, the symbol currently being explained. Red is *never* "danger" or "negative," never a second series, never decorative. The moment red means two things, it means nothing.

Body text and marks are **warm ink, `#2a1a0e`** — a near-black with a little heat in it, never pure `#000`, and above all never blue. Blue is the reflex color of every default chart library, and banning it outright is the fastest way to stop a deck from looking like a template. The only other neutrals are grays: `#545454` for captions, dimmed earlier bullets, and axis labels; `#D4D4D4` for hairlines. Ochre exists as a decorative rule or underline and is forbidden at body size. The canvas is white. That is the whole world.

Two consequences follow. Contrast is checked to AAA — warm ink on white clears it comfortably — and the scheme is colorblind-safe by construction, because meaning never rests on hue. Red-versus-gray is a lightness difference before it is a color difference, so a viewer who cannot distinguish red still sees the emphasis.

## Three typefaces, three jobs

The system uses exactly three fonts, each assigned to a role, so type never becomes a decision made per slide.

The **live HTML deck** — the actual slides, titles and body — uses **Lato**, loaded by the deck's own CSS inside its iframe. Everything *drawn on top* of the deck — bullets, doodle labels, captions — uses **Inter**, loaded from a local file, never referenced by name and hoped for. That last point is a scar from a real bug: name a font and trust the machine to have it, and Inter silently renders as generic `sans-serif`. Load the file, or use a guaranteed fallback chain. There is no handwriting font anywhere; no Caveat, no Shadows Into Light.

The third font is **JetBrains Mono**, and its rule is the subtle one. Mono is for numbers — but only for *real data*. A percentage like `99%`, a decimal like `0.8`, a ratio — those go mono so the eye reads them as data. Ordinals, years, section numbers, "Part 3" — those are not data, they are labels, and they stay in the body font. The test is whether the number is a measurement or a name. Measurements are mono; names are not. Getting this wrong makes a deck look like a spreadsheet threw up on it.

## The one rule about motion

Here is the rule that matters most, and the one that is easiest to violate: **no static screen for more than about five seconds while narration runs.**

The logic is simple arithmetic. A dense slide — a full figure, six bullets, a chart — is exactly right for the three seconds it takes a viewer to read it. But the narration explaining that slide runs thirty seconds, or ninety. For the remaining twenty-seven seconds the viewer is staring at text they finished reading long ago while a voice talks over it. That is death. Attention leaks out through every second of stillness. The fix is **progressive disclosure**: the slide reveals itself in step with the narration, one element per spoken line, so there is always something arriving as the voice moves.

The visual tiers, in strict priority order, are: **progressive figure > doodle > bullets > live chart.** A **progressive figure** is the best tool and the one to reach for first — an authored SVG whose parts are wrapped in groups (`<g class="pf pf-N">`) and revealed one at a time, each `pf-N` timed to a narration line, so a diagram builds itself as it is explained. A **doodle** is line-art built the same way, one stroke or label per line. **Bullets** are the fallback for text-heavy slides, and they run as a *sliding window* — never more than about six on screen at once, the current one emphasized in red, older ones dimming to gray and scrolling off — so a list of fifteen points never becomes a static wall. A **live chart** stays live and *animates* its data on; it is last resort, not first choice. Only short dividers — a title card, a "Part N" break, the close — are allowed to hold still, because they are brief by nature.

Motion itself is quiet. One easing across the whole video (ease-out-quart), entrances that fade and translate a small distance, stroke draw-ons for line art. No bounce, no scale-on-mount, no parallax. The movement exists to keep the screen alive and to point at what the voice is naming — not to perform.

## Equations get a tangent

When an equation appears, the lecture branches into a short **tangent** of about forty seconds before moving on, built from a fixed five-zone template so the explanation quality never depends on improvising live. The zones, revealed one per narration line: the **symbolic form** (large, isolated, real math via KaTeX — never a screenshot, and never mono, because mono is reserved for data numbers); the **LHS/RHS as plain sentences plus the relation sign read as a claim** ("`=` means must be exactly equal"); a **glossary with a Role column** distinguishing a variable from its value from an index; a **worked example with real numbers that holds or breaks** (`40%` vs `22%` → violated), ending on what the violation costs a real person; and, if the equation encodes a value judgment, a **values claim** stated as something contestable, in a red-tint box while the mechanics stay in white boxes. The tangent ends by handing back to the main argument. It explains; it never derives. The five-zone template is a slide pattern that fires every time an equation shows up, so equations stop being the place a lecture goes to die.

## Worked example

A slide presents a bar chart with six bullets beneath it. The narration for this slide runs thirty-eight seconds. As authored, the whole slide appears at once and sits motionless for the full thirty-eight — a static-screen violation more than seven times over the limit.

Apply the system. First, the palette and type: the chart's default blue bars are wrong, so recolor to warm ink with the single bar of interest in `#C8102E`; the axis value `0.8` becomes JetBrains Mono, but the "Part 2" eyebrow stays in the body font because it is a label, not data. Then the motion: the chart is demoted — text carries this slide — so the six bullets convert to the **bullets tier**, a sliding window revealing one bullet per narration line, current in red, earlier ones graying and scrolling off, never more than about six visible. The bars animate on rather than appearing whole. Now something arrives on every spoken line, no frame holds longer than a few seconds, and the slide reads as authored motion instead of a screenshot with a voice-over.

## Exercises

**Exercise 10.1 — Palette and type audit.** Take one slide's overlay spec and check it against the six-value palette and the three-font roles: no blue, one red used for exactly one thing, warm ink not pure black, and every numeral correctly classified as data (mono) or label (body font). List each violation and its fix. (Artifact: a marked-up audit of one slide with corrected color and font assignments.)

**Exercise 10.2 — Fix a static-screen violation.** Find (or author) a slide whose narration runs 30+ seconds against a single static image. Choose the correct tier for it — progressive figure, doodle, or sliding-window bullets — and describe how each narration line reveals one element. (Artifact: the beat's reveal plan, one disclosure step per narration line.)

**Exercise 10.3 — Author an equation tangent.** Pick one equation from your material and fill the five-zone template: symbolic form, the LHS/RHS sentences plus the sign-as-claim, a glossary with the Role column, a worked example with real numbers that holds or breaks, and the values claim (if any). Confirm the numbers are mono and the tangent ends with a re-entry cue. (Artifact: a completed five-zone tangent for one equation.)
