# SHOTLIST — CabStream — Week 3 Progress (Kavya)

8 beats. Landscape 3840x2160 (composed 1920x1080 @ scale 2). Portrait 2160x3840 (composed 1080x1920 @ scale 2).

| Beat | Pattern (16:9) | Pattern (9:16) | What lands on screen |
|---|---|---|---|
| B00 | ClaudeComposerAsk | ClaudeComposerAsk916 | Composer greeting "Hi, Kavya"; the ask types in; three output lines cascade (Databricks cluster, two bugs fixed, Bronze+Silver ingestion). Folder chip `Kavya Mehta`. |
| B01 | BrutalistHesitantWriter | BrutalistHesitantWriter916 | Hesitate/correct: "another quiet infra week" → "the pipeline ran, at real scale". |
| B02 | ClaudeScienceLayerStack | ClaudeScienceLayerStack916 | Four-layer stack — Databricks cluster added / Two real bugs fixed (terracotta) / Bronze ingestion ran / Silver processing ran. |
| B03 | ShellSession | ShellSession916 | Dark terminal, output-only card — the real timestamped git log for the single active night (06-29). |
| B04 | ShellSession | ShellSession916 | Dark terminal, output-only card — the honest "stated in the commit message, not re-verified" caveat on the 1.57B figure. |
| B05 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | Claude artifact page, heading recap of the week. |
| B06 | ClaudeComposerAsk | ClaudeComposerAsk916 | Composer, greeting "Your turn.", viewer prompt. |
| B07 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | Closing artifact card — "CabStream — Week 3 Progress" / "Built by" / "Kavya Mehta". `ClaudeTitleOutro` deliberately NOT used — its `@NikBearBrown` handle is hardcoded with no prop override. |

## Type / visual constraints per beat

- All body beats use serif for headings, sans for UI chrome, mono for terminal output. Cream page `#FAF9F5`, ink `#3D3929`, terracotta `#D97757` as the one accent.
- B00/B06: `folderLabel: "Kavya Mehta"`.
- B03/B04: `host: "kavya"`.
- No code shown anywhere in this reel.

## Duration policy

Duration is an output of the measured Kokoro narration (`am_onyx`). B01 carries `lead_silence_s: 0.8`, B05 carries `lead_silence_s: 0.5`.

## Resolution

Compiled with explicit `--height 2160` (landscape) and `--height 3840`
(vertical) from the start — the `compile.py --height` default (720) bug
that affected every earlier reel in this series this session was already
fixed before this build began. Verified via `ffprobe`: 3840×2160 /
2160×3840.
