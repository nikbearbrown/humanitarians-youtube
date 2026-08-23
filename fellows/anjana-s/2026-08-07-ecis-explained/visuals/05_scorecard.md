# Beat 5 — The Honest Scorecard

**Visual type:** Remotion (code block + animated chart)  
**Duration:** ~25 seconds

## What the viewer sees

**Part A — Pre-registration (first 8 sec):**

A code block slides in from the left, showing a simplified version of the Pydantic signal schema:

```python
class Signal(BaseModel):
    ticker:       str          
    direction:    Direction    # raised | lowered | maintained
    confidence:   float        # 0.87
    quote:        str          # supporting passage
    method:       SourceMethod # keyword | finbert | llm | ...
    transcript_date: date
```

Key fields highlight in sequence as the narration mentions them. Then an "append-only lock" icon stamps onto the code block — a padlock with a checkmark — conveying that signals are frozen once logged.

**Part B — Calibration curve (remaining 17 sec):**

Transition: the code block shrinks and slides to the upper-left corner (stays visible but small). A calibration scatter plot builds in the main area:

- X-axis: "Stated confidence" (0.0 to 1.0)
- Y-axis: "Observed accuracy" (0.0 to 1.0)
- A diagonal reference line draws first (perfect calibration)
- Then dots plot in one cluster at a time, each representing a confidence bin
- Bins sitting on or near the diagonal glow green
- Bins far from the diagonal glow amber or red

As the narration mentions each metric (Brier, skill score, ECE, Murphy), a small label briefly appears near the relevant part of the chart.

## Mood

Rigorous, transparent. The code block says "we write everything down." The calibration curve says "and then we check."

## Technical notes

- Code block: use a dark syntax-highlighted style, monospaced font
- Calibration chart: Plotly-style look, animated with Remotion
- The diagonal line is the visual anchor — everything is measured against it
- Use realistic-looking data points (not perfectly calibrated — show some deviation)
- Keep the code block visible in Part B as a small reference, don't discard it
