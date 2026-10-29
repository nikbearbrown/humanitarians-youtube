# SHOTLIST — Brutalist Progress — Week 3 (Kavya)

8 beats. Landscape 3840x2160 (composed 1920x1080 @ scale 2). Portrait 2160x3840 (composed 1080x1920 @ scale 2).

| Beat | Pattern (16:9) | Pattern (9:16) | What lands on screen |
|---|---|---|---|
| B00 | ClaudeComposerAsk | ClaudeComposerAsk916 | Composer greeting "Hi, Kavya"; the ask types in; three output lines cascade (zero new bugs, three reels now, same verification method). Folder chip `Kavya Mehta`. |
| B01 | BrutalistHesitantWriter | BrutalistHesitantWriter916 | Writer types "the pipeline is finally bug-free", hesitates, backspaces, retypes "this one build hit no new edge case"; holds ≥2s. |
| B02 | ClaudeScienceLayerStack | ClaudeScienceLayerStack916 | Four-layer stack — Built reel three / Zero new bugs (terracotta) / Same verification habit / Three reels, one pipeline — stagger in; caption "the trend so far". |
| B03 | ShellSession | ShellSession916 | Dark terminal, output-only card: "this week — the trend" — the three-week bug count (6, 1, 0). |
| B04 | ShellSession | ShellSession916 | Dark terminal, output-only card: "this week — the honest caveat" — what a zero-bug build does and doesn't prove. |
| B05 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | Claude artifact page, heading "What actually happened", four lines recap the three-week trend. |
| B06 | ClaudeComposerAsk | ClaudeComposerAsk916 | Composer, greeting "Your turn.", viewer prompt types in as Kavya reads it aloud verbatim. Folder chip `Kavya Mehta`. |
| B07 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | Closing artifact card — "Brutalist Progress — Week 3" / "Built by" / "Kavya Mehta". `ClaudeTitleOutro` deliberately NOT used — see BUILD-LOG.md. |

## Type / visual constraints per beat

- All body beats use serif for headings, sans for UI chrome, mono for terminal output. Cream page `#FAF9F5`, ink `#3D3929`, terracotta `#D97757` as the one accent.
- B01: `fontSize: 58`, `seed: "kavya-week3-progress-8845"`.
- B03/B04: `host: "kavya"` (changed from the original build's `host: "claude-liam"`).
- B00/B06: `folderLabel: "Kavya Mehta"` (changed from `@NikBearBrown`).
- No code shown anywhere in this reel.

## Duration policy

Duration is an output of the measured Kokoro narration (`am_onyx`). B01 carries `lead_silence_s: 0.8`, B05 carries `lead_silence_s: 0.5`.
