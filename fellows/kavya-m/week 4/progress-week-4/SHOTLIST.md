# SHOTLIST — CabStream — Week 1 Progress (Kavya)

8 beats. Landscape 3840x2160 (composed 1920x1080 @ scale 2). Portrait 2160x3840 (composed 1080x1920 @ scale 2).

| Beat | Pattern (16:9) | Pattern (9:16) | What lands on screen |
|---|---|---|---|
| B00 | ClaudeComposerAsk | ClaudeComposerAsk916 | Composer greeting "Konnichiwa, Kavya"; the ask types in; three output lines cascade (Kafka producer, bronze→silver→gold, 6 days). Folder chip `Kavya Mehta`. |
| B01 | BrutalistHesitantWriter | BrutalistHesitantWriter916 | Hesitate/correct beat on the week's real scope. |
| B02 | ClaudeScienceLayerStack | ClaudeScienceLayerStack916 | Four-layer stack — the week's real build milestones, Kafka producer through dbt gold layer. |
| B03 | ShellSession | ShellSession916 | Dark terminal, output-only card — day-by-day build log. |
| B04 | ShellSession | ShellSession916 | Dark terminal, output-only card — what's real vs. what comes later (the 1.57B-row metrics explicitly flagged as NOT week 1). |
| B05 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | Claude artifact page, heading recap of the week. |
| B06 | ClaudeComposerAsk | ClaudeComposerAsk916 | Composer, greeting "Your turn.", viewer prompt. |
| B07 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | Closing artifact card — "CabStream — Week 1 Progress" / "Built by" / "Kavya Mehta". `ClaudeTitleOutro` deliberately NOT used — its `@NikBearBrown` handle is hardcoded with no prop override (see BUILD-LOG.md). |

## Type / visual constraints per beat

- All body beats use serif for headings, sans for UI chrome, mono for terminal output. Cream page `#FAF9F5`, ink `#3D3929`, terracotta `#D97757` as the one accent.
- B00/B06: `folderLabel: "Kavya Mehta"`.
- No code shown anywhere in this reel.

## Duration policy

Duration is an output of the measured Kokoro narration (`am_onyx`).
