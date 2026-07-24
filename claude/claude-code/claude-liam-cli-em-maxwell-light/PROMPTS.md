# PROMPTS — claude-liam-cli-em-maxwell-light

Beat-prefixed generation prompts for open / slate beats.

---

## B01 — PROBLEM (slate needed)

**Prompt for graphic designer / Remotion / Canva:**

> Create a title card for a YouTube short (9:16 or 16:9).
> Background: white (#FFFFFF). Text color: dark brown (#2A1A0E).
> Accent: terracotta (#C8102E).
>
> Content (top to bottom):
> 1. Small label (terracotta, uppercase): "ELECTROMAGNETISM"
> 2. Large formula chain (dark ink, centered):
>    Ampère + displacement current → wave equation → c = 1/√(μ₀ε₀)
> 3. Subtitle (medium, dark ink):
>    "From a fix for mathematical inconsistency to the unification of light"
> 4. Thin terracotta rule at bottom
>
> Duration: hold 17 seconds. Fade in over 0.5s.
> Export as MP4 or PNG. Drop into pantry/B01-problem-slate.mp4

---

## B07 — SUMMARY (slate needed)

**Prompt for graphic designer / Remotion / Canva:**

> Create a recap card for a YouTube short (9:16 or 16:9).
> Background: white (#FFFFFF). Text color: dark brown (#2A1A0E).
> Accent: terracotta (#C8102E).
>
> Content (top to bottom):
> 1. Large centered formula: c = 1/√(μ₀ε₀)
>    (use math serif font; "c" in terracotta)
> 2. Italic block quote (medium size, dark ink):
>    "we can scarcely avoid the inference that light consists
>     in the transverse undulations of the same medium"
>    — Maxwell, 1865
> 3. Rule (thin, terracotta)
> 4. Bold footer text: "One fix. One formula. One unification."
>
> Duration: hold 15 seconds. Fade in over 0.5s.
> Export as MP4 or PNG. Drop into pantry/B07-summary-slate.mp4

---

## B04 — OUTPUT (Manim — MACHINE, no prompt needed)
Scene class: `B04_WavePacket` in `scenes.py`
Run: `manim -ql scenes.py B04_WavePacket` or via run.sh

## B06 — OUTPUT (Manim — MACHINE, no prompt needed)
Scene class: `B06_Superposition` in `scenes.py`
Run: `manim -ql scenes.py B06_Superposition` or via run.sh
