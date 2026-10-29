# SHOTLIST — CabStream — Week 2 Progress (Kavya)

8 beats. Landscape 3840x2160 (composed 1920x1080 @ scale 2). Portrait 2160x3840 (composed 1080x1920 @ scale 2).

| Beat | Pattern (16:9) | Pattern (9:16) | What lands on screen |
|---|---|---|---|
| B00 | ClaudeComposerAsk | ClaudeComposerAsk916 | Composer greeting "Hi, Kavya"; the ask types in; three output lines cascade (6 Terraform files, managed Kafka, the access-policy fix). Folder chip `Kavya Mehta`. |
| B01 | BrutalistHesitantWriter | BrutalistHesitantWriter916 | Hesitate/correct beat: "clicking through the Azure portal" → "six resources, defined entirely in Terraform". |
| B02 | ClaudeScienceLayerStack | ClaudeScienceLayerStack916 | Four-layer stack — Event Hubs defined / Databricks workspace defined (terracotta) / Storage + Key Vault added / Access gap closed, next day. |
| B03 | ShellSession | ShellSession916 | Dark terminal, output-only card — the real timestamped git log for the two active days. |
| B04 | ShellSession | ShellSession916 | Dark terminal, output-only card — the honest "defined, not deployed" caveat. |
| B05 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | Claude artifact page, heading recap of the week. |
| B06 | ClaudeComposerAsk | ClaudeComposerAsk916 | Composer, greeting "Your turn.", viewer prompt. |
| B07 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | Closing artifact card — "CabStream — Week 2 Progress" / "Built by" / "Kavya Mehta". `ClaudeTitleOutro` deliberately NOT used — its `@NikBearBrown` handle is hardcoded with no prop override. |

## Type / visual constraints per beat

- All body beats use serif for headings, sans for UI chrome, mono for terminal output. Cream page `#FAF9F5`, ink `#3D3929`, terracotta `#D97757` as the one accent.
- B00/B06: `folderLabel: "Kavya Mehta"`.
- B03/B04: `host: "kavya"`.
- No code shown anywhere in this reel.

## Duration policy

Duration is an output of the measured Kokoro narration (`am_onyx`). B01 carries `lead_silence_s: 0.8`, B05 carries `lead_silence_s: 0.5`.
