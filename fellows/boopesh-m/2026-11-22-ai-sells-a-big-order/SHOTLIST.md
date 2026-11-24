# SHOTLIST — How an AI Sells a Big Order (16:9, 3840×2160)

Typed work order. Every slot is generated (Remotion or Manim). There are no pantry or human media slots.
Measured narration (16:9): B00 9.17 s, B10 9.22, B20 16.51, B30 13.87, B40 16.56, B50 12.58, B60 16.66, B70 17.14,
B80 14.09, B90 6.91. Total 132.71 s (rendered 132.92 s).

| Beat | Act | Lane | Source / slot | What the viewer watches |
|---|---|---|---|---|
| B00 | INTRO | Remotion `ClaudeComposerAsk` → media/B00.mp4 | greeting "Hi, Boopesh", topic "Irreducibly Human", folder chip @HumanitariansAI, model "Claude" | the ask types in, then three result lines land (all at once / equal slices / learned schedule) |
| B10 | OVERVIEW | Remotion `BrutalistHesitantWriter` → media/B10.mp4 | one line + one correction: "Sell a big order all at once." → "…in slices." | the writer types and hesitates; "all at once" turns accent and is replaced; three context cards (impact · risk · the agent) |
| B20 | THE PROBLEM | Manim `B20_Impact` → manim/B20.mp4 | results.json dump | a 10,000-share bar fills step 1, the price slides $50.00 → $49.50, cost card "$5,000 = 100 bps" |
| B30 | THE OTHER RISK | Manim `B30_Drift` → manim/B30.mp4 | results.json sample_days | ten equal teal bars, impact chip 100 → 10 bps, 40 held-out price paths fan out, a bad day (79 bps) in accent |
| B40 | THE AGENT | Manim `B40_Agent` → manim/B40.mp4 | results.json rl schedule, params | state table (time left × shares left), action strip 0–100% (25% picked), score card, 40,000,000 practice runs, the learned path through the table |
| B50 | WHAT IT LEARNED | Manim `B50_Schedule` → manim/B50.mp4 | results.json rl + ac | teal learned bars; Almgren–Chriss dots drop onto them; the one formula; "within 1.7%" |
| B60 | THE TEST | Manim `B60_Costs` → manim/B60.mp4 | results.json dump/twap/rl | three cost lanes: average bar + bad-day tick (95th pct); agent's "bad day 54" in accent |
| B70 | TAKEAWAY (dark) | Manim `B70_Takeaway` → manim/B70.mp4 | — | a balance (impact vs risk) tilts and settles; "This was a synthetic market" card; read-more line |
| B80 | YOUR TURN | Remotion `ClaudeComposerAsk` → media/B80.mp4 | greeting "Your turn." | the suggested prompt types into the composer and holds while it is explained |
| B90 | OUTRO | Manim `B90_Outro` → manim/B90.mp4 | assets/hai-logo-1-ink.png | title, HAI mark + @HumanitariansAI, SUBSCRIBE pill, credits, narration and data lines |
