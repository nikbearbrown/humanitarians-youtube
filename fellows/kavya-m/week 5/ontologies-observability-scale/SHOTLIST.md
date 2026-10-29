# SHOTLIST — Ontologies for Observability at Scale (Kavya)

8 beats. Landscape 3840x2160 (composed 1920x1080 @ scale 2). Portrait 2160x3840 (composed 1080x1920 @ scale 2).

| Beat | Pattern (16:9) | Pattern (9:16) | What lands on screen |
|---|---|---|---|
| B00 | ClaudeComposerAsk | ClaudeComposerAsk916 | Composer greeting "Hi, Kavya"; the ask types in; three output lines cascade (naming collision, canonical entity, "modeling problem not model problem"). Folder chip `Kavya Mehta`. |
| B01 | BrutalistHesitantWriter | BrutalistHesitantWriter916 | Hesitate/correct: "a naming convention" → "a shared model of what things ARE". |
| B02 | ClaudeScienceLayerStack | ClaudeScienceLayerStack916 | Four-layer stack — Entity types / Relationships (terracotta) / Stable identifiers / A shared vocabulary. |
| B03 | ShellSession | ShellSession916 | Dark terminal, output-only card — the "without an ontology" naming-collision example. |
| B04 | ShellSession | ShellSession916 | Dark terminal, output-only card — the "with an ontology" resolved-graph example. |
| B05 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | Claude artifact page, heading "What actually changes" — four-line recap plus the honest boundary statement. |
| B06 | ClaudeComposerAsk | ClaudeComposerAsk916 | Composer, greeting "Your turn.", viewer prompt. |
| B07 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | Closing artifact card — "Made by" / "Kavya Mehta" / "Narration: AI voice (Kokoro), reading my script". `ClaudeTitleOutro` deliberately NOT used — its `@NikBearBrown` handle is hardcoded with no prop override. |

## Type / visual constraints per beat

- All body beats use serif for headings, sans for UI chrome, mono for terminal output. Cream page `#FAF9F5`, ink `#3D3929`, terracotta `#D97757` as the one accent.
- B01: `fontSize: 58`, `seed: "kavya-obs-ontology-4471"`.
- B03/B04: `host: "kavya"`, `path: "~/kavya-obs-ontology"`.
- B00/B06: `folderLabel: "Kavya Mehta"`.
- No code shown anywhere in this reel.

## Duration policy

Duration is an output of the measured Kokoro narration (`am_onyx`). B01 carries `lead_silence_s: 0.8`, B05 carries `lead_silence_s: 0.5`.
