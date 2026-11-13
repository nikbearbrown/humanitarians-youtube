# SHOTLIST — 2026-09-21-project-overview (Fine-Tuning Platform)

8 beats. Landscape 3840x2160 (composed 1920x1080 @ scale 2). No portrait variant.

| Beat | Pattern | What lands on screen |
|---|---|---|
| B00 | ClaudeComposerAsk | Greeting `Hey` over the composer; the ask types in: "Quick gut check on the fine-tuning platform..."; output lines cascade (5-stage SFT pipeline / RL calibration: open question). Folder chip `Fine-Tuning Platform`. |
| B01 | BrutalistHesitantWriter | Writer types "A platform that fine-tunes models."; the trigger phrase goes terracotta, hesitates, backspaces, retypes to "A platform that knows what it doesn't know."; holds. |
| B02 | SkillTeardownPipeline | "One Spec. Five Stages." Horizontal INPUT→phases→OUTPUT diagram: job_config.json → Pre-flight guard → Data ingestion → Model + PEFT → SFT training → Export (accent) → fine-tuned model. Footer note: "Any Jev/Laya model · any dataset · any job spec." |
| B03 | BarChart | "The Calibration Gap." Two bars: Stated confidence (85), Actual accuracy (60, accent). |
| B04 | TypesetMath | "Reward as a proper scoring rule." Typeset equation `reward = -(confidence - outcome)^2` (matplotlib mathtext SVG, no LaTeX). Note + conditions line below. |
| B05 | ClaudeVerdictArtifact | Claude artifact card. Title "Project Overview — next steps", heading "Two workstreams", three staggered lines (sandbox / RL script / validation). |
| B06 | ClaudeComposerAsk | Composer, greeting `Your turn.` Prompt types in as Liam reads it aloud: pasting a model's confidence scores and outcomes for a calibration check. |
| B07 | TitleRestateOutro | Centered serif title "Project Overview." with terracotta period, subline "Fine-Tuning Platform". No channel handle — see README note below. |

## Type / visual constraints per beat

- Palette `claude` (cream `#FAF9F5`, warm ink, terracotta `#D97757` as the one accent) throughout, except B03 (BarChart) which uses the vox palette (CREAM/INK/SLATE/TEAL) per its own component — ILLUSTRATE LAW permits mixed media in the explainer middle.
- B01: `fontSize: 160`, `lineSpacing: 1.4`, `align: center`, `seed: "project-overview-b01"`.
- B02: `SkillTeardownPipeline` schema `{ eyebrow, title, inputLabel, outputLabel, phases[], footerNote, sparkLine }`.
- B03: `BarChart` schema `{ title, data[], accentIndex, unit }`. `unit` left empty — see TYPECHECK.md history (an earlier "%"/"percent" unit line was removed; see Corrections below).
- B04: `TypesetMath` schema `{ title, rows[], note, conditions }`. `rows[0].src` is a locally generated base64 SVG from `runtime/scripts/typeset_math.py` (matplotlib mathtext, no LaTeX dependency).
- B05: `ClaudeVerdictArtifact` schema `{ artifactTitle, artifactHeading, artifactLines[] }`.
- B06: `ClaudeComposerAsk` schema `{ greeting, topic, segment, command, runningText, output[], folderLabel }`.
- B07: `TitleRestateOutro` schema `{ title, subline }` — a new component (see Corrections below), not the locked `ClaudeTitleOutro`.

## Duration policy

Duration is an output of the measured Kokoro narration (`am_onyx`). Each beat's `estimated_duration_s` is a planning number; `actual_duration_s` is the ground truth from `generate_audio_kokoro.py` (total ~88s narration, ~87.8s compiled runtime).

## Corrections & caveats

- **No channel outro.** This is a personal/internal project-status reel, not a release on
  any of this toolkit's branded YouTube channels (`@NikBearBrown`, etc.). The library's only
  title-restate outro, `ClaudeTitleOutro`, hardcodes the `@NikBearBrown` handle per
  `OUTRO-LOCK.md` (scoped to claude-liam reels only), so it would mislabel this video's
  authorship. A new generic component, `TitleRestateOutro` (title + optional subline, no
  handle), was added to `runtime/remotion/src/scenes/` and registered in `Root.tsx` for this
  and future non-channel reels. `qc.sparse_by_design` is declared on B07 since a minimal
  centered title card is intentionally low-density (see `beat_sheet.json`).
- **B03 unit label.** The `BarChart` component's optional `unit` line (meant for a short
  suffix like "ms") triggered a false-positive §8.1 min-size read on its thin baseline-rule
  div, unrelated to the unit text itself; `unit` was set to `""` (unused) and the baseline-rule
  false-positive was instead exempted for the `BarChart` pattern in
  `runtime/scripts/type_check.py`'s `HAND_DRAWN_PATTERNS` set, with a written reason.
  Separately, B03's title was shortened from a two-line wrapped sentence to "The Calibration
  Gap." to clear a real §8.6b bbox-overlap (the wrapped second line was overlapping the
  tallest bar's value label).
