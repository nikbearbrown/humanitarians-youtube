# SHOTLIST — The 99.9% Accuracy Trap (16:9, 3840×2160)

| Beat | Lane | Visual |
|---|---|---|
| B00 | Remotion `ClaudeComposerAsk` | "Hi, Boopesh" composer: "Can a fraud model be 99.9% accurate and still useless?" answered in three lines; chip @HumanitariansAI |
| B10 | Remotion `BrutalistHesitantWriter` | "99.9% accurate means it works." corrected to "…means nothing when fraud is 1 in 580." |
| B20 | Manim `B20_Rare` | 580-dot grid, one dot turns red; cards 284,807 transactions · 492 fraud · 1 in 580 (0.172 %); source line |
| B30 | Manim `B30_Lazy` | dark code card `return False # always legit`; "synthetic data" card; accuracy meter 99.8 %; "0 of 148" + 148 hollow circles |
| B40 | Manim `B40_Scorecard` | confusion matrix as 4 big boxes (lazy model's numbers); typeset recall and precision with plain-words questions |
| B50 | Manim `B50_Models` | three columns (always legit / logistic / boosting): accuracy row boxed "almost identical", caught-of-148 bars 0 / 66 / 127, false alarms, recall/precision |
| B60 | Manim `B60_Threshold` | precision–recall curves (both models) with a moving dot; cutoff slider 0.9 → 0.01 with caught / false-alarm readout; dark cost card (50:1 assumption) |
| B70 | Manim `B70_Takeaway` | dark card "check these instead: recall · precision · cost"; honest limits list |
| B80 | Remotion `ClaudeComposerAsk` | "Your turn." composer with the prompt |
| B90 | Manim `B90_Outro` | title, SUBSCRIBE + HAI mark + @HumanitariansAI; credit Boopesh M. · Fellow · Brutalist team; data line; AI narration |

Every model number and curve is read from `code/results.json` / `code/curves.npz`; the real-dataset counts are
constants copied from the dataset description (FACTCHECK.md).
