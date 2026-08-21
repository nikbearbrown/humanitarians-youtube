# Beat 5 — The Dashboard

**Visual type:** Remotion
**Duration:** ~10 seconds

## What the viewer sees

The Episode 2 dashboard layout returns — same four-panel structure — but upgraded for three models.

**Calibration curves (0-4s):**
Top-left panel. The calibration plot now has three lines drawing against the diagonal reference:
- Purple (Llama)
- Teal (Mistral)
- Amber (Qwen)

The three lines weave around the diagonal — close but each with distinct patterns. Qwen's line tracks slightly tighter to the diagonal. The visual tells the story: three models, three different calibration profiles.

**Bar chart (4-6s):**
Top-right panel. Brier score comparison now shows three grouped bars per metric instead of two. Purple, teal, amber side by side. The bars grow upward — Qwen's amber bar is slightly shorter (better Brier score) on some metrics.

**Signal explorer with provenance (6-9s):**
Bottom-left panel. The signal table has a new "Model" column. A filter dropdown animates and selects "Qwen 14B" — the table filters. One row is tapped, expanding to reveal the provenance stack from Beat 4 — the accordion layers briefly visible inside the dashboard.

**Agent activity (9-10s):**
Bottom-right panel. The timeline from Episode 2 with event dots. A new dot appears: "Model weight adjusted" — the feedback loops are still running.

All four panels pulse briefly together — the system is alive and showing three models in one unified view.

## Technical notes

- Same dashboard layout as Episode 2 — four quadrants — just upgraded content
- The three-line calibration curve is the visual continuity moment: Episode 1 had one implicit line, Episode 2 had two, Episode 3 has three
- The provenance drill-down inside the dashboard connects Beat 4 to Beat 5 — the receipt is accessible from the dashboard
- Keep animations subtle — numbers ticking, lines drawing — not flashy
