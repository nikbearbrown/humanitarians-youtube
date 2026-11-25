# SOURCES — Same App, New Look

## What Sai supplied (2026-11-16)

> "creata a video for date 11-13-2026. Abou tthe ui changes to the app.
> https://www.figma.com/design/NE8nKjRT9eSQE6FA1pnOY1 — please keep the video
> around 1 minute. generate it in both 9:16 and 16:9 formats in 4k"

## Sources

| Source | What it gave | Where |
|---|---|---|
| Figma file `NE8nKjRT9eSQE6FA1pnOY1` | Pages 00 As-Is, 01/02 wireframes, 03 Visual Findings (R-20261116-02: 5 decision rows, "Changes since R-20261116-01" table, 11 findings) | read via the Figma MCP, 2026-11-16 |
| Audit ledger | `intent.yaml`, `decisions/D-0001…D-0005.json`, `runs/R-20261116-01/-02/findings.json`, `ledger.jsonl` (26 events, head `be80a4cf…`), `approvals/` (empty) | `~/figma-webdesigner-work/gavia/audit/` |
| Gavia repo | `desktop/src/index.css` at `5dd8471` (Sai, 2026-11-01) and on `design/hai-brand` working tree (sha256 `3a1f5437…`, uncommitted, 7 files) | `~/Documents/gavia` |
| Re-measurement | `evidence/contrast.py` → `contrast.out`; `evidence/recapture.mjs` → `recapture.out`, `recapture.json` | this reel |
| Loon photo | loonet `web_20260818_0042.jpg` = Unsplash, Glennice Burns (`glennice-burns-0yJgv9Uf2_E-unsplash.jpg`) | `~/Documents/loonet/data/annotated/loonnet_v1/images/manifest.csv` |
| WCAG 2.2 | contrast ratio and relative luminance definitions; 4.5:1 (1.4.3), 3:1 (1.4.11) | w3.org/TR/WCAG22 |

## Week-scope changes, with authors

| Change | Author | State |
|---|---|---|
| `5dd8471` Merge PR #27 (Vegnet, 0.5.0) — the "before" | Sai Nikhil Kunapareddy | committed |
| `design/hai-brand`: index.css, main.tsx, package.json/lock (Inter), Image/AudioUploader.tsx (aria-label), browserPreview.ts (dev fix O-0001) | Claude Code (figma-webdesigner skill), at Sai's request | **uncommitted**, built before approval |

## Honesty log

- **Fake detections in every screenshot.** The audit captured the browser
  preview (`manifest.json`: "detections made up"). Its Figma crops show
  different confidences on each side (73% vs 91%; dark: 2 loons vs 1). Re-captured
  with pinned check ids so both sides show the same sample (84%, 1 loon), and the
  plate credit says "made-up sample".
- **Audit's "≥ 5.23:1 on every light background"** for the new subtle grey: my
  token pairs (bg, surface, surface-muted) give a minimum of 5.32:1. The audit
  likely included another background (e.g. a tinted banner). Not on screen; the
  reel uses the page-background pair (6.16) for the worked case.
- **axe counts differ from the Figma table** by design: the Figma table lists
  11 findings including judgment rules (brand, type, button style); axe counts
  only automated failures. The reel shows axe's 6 and says "six failures".
- **First recapture had broken fonts:** a symlinked `node_modules` outside the
  vite root got a 403 on Inter's woff2. Re-run with real copies; the recorded
  `recapture.json` is the fixed run (Inter loaded on all six "after" screens).
