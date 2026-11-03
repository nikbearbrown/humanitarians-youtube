# SHOTLIST — The Review Gate (16:9 4K)

Spine: cold open → hesitant-writer BLUF → framework → ASK→RESULT → body → handoff → outro.
Transitions: cross-dissolve-through-cream at every beat boundary (add_transitions.py, 0.35s).

| Beat | Source / scene | What's on screen | Clock |
|---|---|---|---|
| T00 | Remotion `ClaudeComposerAsk` | Cold open; ask typed + answered (3 output lines) | 24.0s |
| T01 | Remotion `BrutalistHesitantWriter` | BLUF; "waving them through" → "running each through a 3-check gate" | 15.1s |
| T02 | Manim `T02_Gate` | THE framework: 3 check-stations (4K / branding / GitHub), pass vs fail, footer rule | 25.6s |
| T03 | Remotion `ClaudeComposerAsk` | ASK: hand the raw tracker to Claude, "build the scoreboard" | 14.2s |
| T04 | Manim `T04_Scoreboard` | RESULT: 88/22/8 stat tiles · 78|10 segmented approval bar · 71/88 GitHub arc | 20.7s |
| T05 | Manim `T05_Breakdown` | 8-project lollipop ranking, Brutalist 41 highlighted | 21.7s |
| T06 | Manim `T06_GreenPass` | Worked example: Jainil's batch, three greens → APPROVED | 22.7s |
| T07 | Manim `T07_FixLoop` | Falsifiability: submit→FAIL→email→fix→re-submit→PASS loop; Deepa/Harshitha/Neelabh | 22.6s |
| T08 | Remotion `ClaudeComposerAsk` | HANDOFF "Your turn."; the build-a-gate prompt read aloud | 25.0s |
| T09 | Manim `T09_Outro` | Title restate "The Review Gate." · @HumanitariansAI · Sanjana Rao | 9.0s |

Total ≈ **3:41**. Logo bug: HAI handle wordmark carried by the Claude scenes / outro.
Render: Manim 3840×2160@60, Remotion 3840×2160 (scale 2). Conform to audio via compile.py.

## 9:16 Short (dedicated sheet, not a crop) — `the-review-gate-short/`
| Beat | Source | On screen | Clock |
|---|---|---|---|
| S00 | `ClaudeComposerAsk916` | Hook, ask answered | ~9.5s |
| S01 | Manim `S01_Gate` | 3 checks + 88/78/71 numbers | ~20s |
| S02 | `ClaudeComposerAsk916` | "Your turn." gate prompt | ~13s |
| S03 | Manim `S03_Outro` | Title + @HumanitariansAI | ~5s |
Total ≈ **0:48**. Render 2160×3840.
