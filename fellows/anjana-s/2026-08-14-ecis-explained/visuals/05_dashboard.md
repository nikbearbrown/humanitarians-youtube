# Beat 5 — The Dashboard

**Visual type:** Remotion
**Duration:** ~10 seconds

## What the viewer sees

A stylized dashboard mockup builds panel by panel — not a screenshot, but clean motion-graphics representations of each view.

**Panel 1 — Signal explorer (0-3s):**
A table materializes in the top-left quadrant. Rows populate with data: ticker symbols, direction arrows (up/down/horizontal), confidence numbers, short quote snippets. Rows appear one at a time, quickly.

**Panel 2 — Calibration curves (3-5s):**
The familiar calibration plot from Episode 1 appears in the top-right quadrant, but now with two lines — purple (Llama) and teal (Mistral) — drawing against the diagonal reference. Continuity with Episode 1's visual.

**Panel 3 — Model comparison (5-7s):**
A bar chart in the bottom-left quadrant. Two grouped bars per metric (Brier, Skill, ECE) — purple vs teal. The bars grow upward.

**Panel 4 — Agent activity (7-9s):**
A timeline in the bottom-right quadrant. Event dots appear along it with brief labels: "recalibration triggered," "weight adjusted," "threshold updated."

**Full dashboard (9-10s):**
All four panels are now visible simultaneously. Numbers tick, curves redraw, dots appear — the whole thing is alive.

## Technical notes

- This is NOT a screenshot of the real Streamlit dashboard — it's a stylized motion-graphics version
- Each panel should be visually simple — just enough detail to convey "this exists and it's live"
- Purple and teal carry over from Beat 2 for model identification
- The "alive" feeling comes from subtle continuous animation — numbers updating, cursor-like elements moving
- Don't overload — four panels is the maximum, each one clean and glanceable
