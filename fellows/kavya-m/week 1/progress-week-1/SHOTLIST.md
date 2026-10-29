# SHOTLIST — Brutalist Progress — Week 1 (Kavya)

9 beats. Landscape 3840x2160 (composed 1920x1080 @ scale 2). Portrait 2160x3840 (composed 1080x1920 @ scale 2).

| Beat | Pattern (16:9) | Pattern (9:16) | What lands on screen |
|---|---|---|---|
| B00 | ClaudeComposerAsk | ClaudeComposerAsk916 | Composer greeting "Hi, Kavya"; the ask types in; terracotta send arms; three output lines cascade (deps installed, bugs fixed, videos shipped). Folder chip `Kavya Mehta` — no @NikBearBrown branding. |
| B01 | BrutalistHesitantWriter | BrutalistHesitantWriter916 | Writer types "a smooth, working pipeline", hesitates, backspaces, retypes "six breaks, fixed at the root"; holds ≥2s. |
| B02 | SkillTeardownPipeline | SkillTeardownPipeline916 | Horizontal (portrait: vertical) phase flow — IDEA → Beat sheet → Kokoro audio (terracotta) → Render + compile → QC gates → SHIPPED VIDEO. Footer: "Four stages. Six real breaks." |
| B03 | ClaudeScienceLayerStack | ClaudeScienceLayerStack916 | Four-layer stack — Toolkit setup / First reel authored (terracotta) / Six pipeline bugs fixed / Two formats shipped — stagger in; caption "one week, four milestones". |
| B04 | ShellSession | ShellSession916 | Dark terminal, output-only card: "this week — bugs found (1/2)" — three numbered findings (UnicodeDecodeError, WinError 2, missing node_modules). |
| B05 | ShellSession | ShellSession916 | Dark terminal, output-only card: "this week — bugs found (2/2)" — three more numbered findings (ffmpeg drive-letter colon, GATE V timecode exclusion, chart scale mismatch). |
| B06 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | Claude artifact page, heading "What actually happened", four lines recap the week. |
| B07 | ClaudeComposerAsk | ClaudeComposerAsk916 | Composer, greeting "Your turn.", viewer prompt types in as Kavya reads it aloud verbatim. Folder chip `Kavya Mehta`. |
| B08 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | Closing artifact card — "Brutalist Progress — Week 1" / "Built by" / "Kavya Mehta". `ClaudeTitleOutro` deliberately NOT used (its `@NikBearBrown` handle is hardcoded with no prop override — see BUILD-LOG.md). |

## Type / visual constraints per beat

- All body beats use serif for headings, sans for UI chrome, mono for terminal output. Cream page `#FAF9F5`, ink `#3D3929`, terracotta `#D97757` as the one accent.
- B01: `fontSize: 64`, `seed: "kavya-week1-progress-4102"`.
- B04/B05: `host: "kavya"` (changed from the original build's `host: "claude-liam"` — no persona branding carried over).
- B00/B07: `folderLabel: "Kavya Mehta"` (changed from `@NikBearBrown`).
- No code shown anywhere in this reel — every "evidence" beat is an output-only terminal card or a diagram, consistent with the original build this reel is adapted from.

## Duration policy

Duration is an output of the measured Kokoro narration (`am_onyx`). Each beat's `estimated_duration_s` is a planning number; `actual_duration_s` (stamped into `beat_sheet.json` after `generate_audio_kokoro.py`) is the ground truth. B01 carries `lead_silence_s: 0.8`, B06 carries `lead_silence_s: 0.5`.
