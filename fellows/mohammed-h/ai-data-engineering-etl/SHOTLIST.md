# SHOTLIST — `ai-data-engineering-etl`

Typed work order. Every slot is machine-renderable — **there are no human-media
slots in this reel and no slates are expected**. Both aspect ratios are rendered
natively (reflowed layouts), never cropped.

| Beat | Act | Composition (16:9 / 9:16) | Audio | Notes |
|---|---|---|---|---|
| B00 | INTRO | `ClaudeComposerAsk` / `ClaudeComposerAsk916` | 15.59s | Existing toolkit scene; already aspect-responsive. COLD OPEN LAW. |
| B01 | PROBLEM | `EtlGlueTax` / `EtlGlueTax916` | 14.21s | **New scene.** Landscape: endpoints left/right, stack grows upward off the pipe. Portrait: endpoints top/bottom, stack down the spine. Carries the E/T/L line folded in at GATE P. |
| B02 | ASK | `ClaudeComposerAsk` / `ClaudeComposerAsk916` | 10.41s | Ask half of the ASK→RESULT pair with B03. |
| B03 | RESULT | `EtlSchemaMapping` / `EtlSchemaMapping916` | 15.40s | **New scene.** Landscape: two panels facing across a gap, flags ride the connectors. Portrait: one full-width card per mapping, source line over target line. |
| B04 | CODE | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | 10.24s | Existing pair. ACTUAL-CODE LAW — the real `transform.py`. |
| B05 | JUDGMENT | `EtlWhereAiHelps` / `EtlWhereAiHelps916` | 12.71s | **New scene.** Landscape: two columns, vertical divider. Portrait: two stacked blocks, horizontal divider. |
| B06 | RISK | `EtlSilentFailure` / `EtlSilentFailure916` | 11.03s | **New scene.** Pipe + two tracks in both aspects; portrait gets more vertical room and larger type. |
| B07 | SUMMARY | `ClaudeVerdictArtifact` / `ClaudeVerdictArtifact916` | 11.97s | Existing pair. |
| B08 | NEXT STEPS | `ClaudeComposerAsk` / `ClaudeComposerAsk916` | 13.76s | HANDOFF LAW — `greeting: "Your turn."` |
| B09 | OUTRO | `ClaudeTitleOutro` / `ClaudeTitleOutro916` | 4.67s | Existing pair. OUTRO LAW. |

**Measured total: 119.99s (1:59.99).** Every slot is machine-renderable; no slates, no pantry drops.

## New scenes to author (5 components, 10 compositions)

All five live in `runtime/remotion/src/scenes/` in the brutalist.art toolkit and
are registered **twice** in `Root.tsx` — once at 1920×1080, once at 1080×1920 with
the `916` suffix, as the ONDA CHECK in `shorts.py` requires. Each component is a
pure function of `useP()` and branches on `height > width` to **reflow** (not
rescale) for portrait.

1. `EtlGlueTax`
2. `EtlStages` — **built, then cut from this reel at GATE P** (the shortening).
   It stays registered as a reusable illustration; this cut does not consume it.
3. `EtlSchemaMapping`
4. `EtlWhereAiHelps`
5. `EtlSilentFailure`

## Aspect-ratio contract

| | 16:9 | 9:16 |
|---|---|---|
| Composition | 1920×1080 | 1080×1920 |
| Render scale | `--scale=2` | `--scale=2` |
| Native render | 3840×2160 | 2160×3840 |
| Master height | `compile.py --height 2160` | `compile.py --height 3840` |
| Safe area | `SAFE` (x 96–1824, y 54–1026) | `SAFE916` (x 54–1026, y 96–1824) |
| Extra portrait reserve | — | keep essential content above y≈1440 (platform UI) |

## Legibility floor

Body/label type is sized so that at the **1080p delivery floor** (the resolution
most viewers actually get) nothing essential renders below ~24 px effective.
Portrait uses larger relative type than landscape because the frame is narrower —
the reflow exists precisely so text is not shrunk to fit.
