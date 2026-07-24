# QC Report — claude-liam-connect-linkedin ("Claude, Gated.")

Date: 2026-07-18  
Engine: Kokoro af_kore (free, local)  
Total runtime: 376.3s (~6:16)  
Beats: 13 / 13 filled — all REMOTION  
Frames sampled: 2fps grid (751 frames) + 15/50/85% per beat (39 spot-checks)

## 9-point rubric

| # | Check | Result |
|---|---|---|
| 1 | **Palette** — cream `#FAF9F5`, ink `#3D3929`, terracotta `#D97757` only; no rogue colors | PASS |
| 2 | **Safe area** — all text/elements within 96–1824 × 54–1026 px inset | PASS |
| 3 | **Spark line** — bottom-left terracotta ✳ + italic serif on every body beat (B01–B07, B09) | PASS |
| 4 | **ILLUSTRATE LAW** — Claude UI only in B00/B08/BHTF; custom scenes B01–B07; Onda code B09; Verdict/Outro standard | PASS |
| 5 | **Eyebrow/title hierarchy** — small-caps eyebrow, large serif title, correct weight | PASS |
| 6 | **Text legibility** — all labels, body text, and code readable at 1080p | PASS |
| 7 | **REBUILD LAW** — zero LinkedIn screenshots; everything built fresh in house palette | PASS |
| 8 | **BOUT outro** — title "Claude, Gated." with terracotta period; @HumanitariansAI; "Kore, in for Humanitarians AI." | PASS |
| 9 | **BVDT verdict card** — terracotta numbered list; 4 items; heading "Connect Claude to LinkedIn — the honest map" | PASS |

## Per-beat notes

- **B00 ClaudeComposerAsk** — greeting "Hola, Kore", topic correct, output lines fully revealed at 50% mark. PASS
- **B01 LinkedInTrustBoundary** — directory card + trust boundary diagram both visible by 50%. Terracotta dashed arrow. PASS
- **B02 LinkedInThreeLanes** — three card lanes (Publishing / Analytics / Outreach), icons, descriptions, sub-label. PASS
- **B03 LinkedInAsymmetry** — green "OFFICIAL API" on Publishing/Analytics; terracotta WALL block with lock icon on Outreach. PASS
- **B04 LinkedInApiSurface** — four-row table: SELF-SERVE (green) / AUDIT (amber) / CLOSED (grey) / NO PATH (terracotta). PASS
- **B05 LinkedInDetectionStack** — left: li_at cookie + Voyager endpoint; right: 4-layer detector stack; warning banner. PASS
- **B06 LinkedInLegalSplit** — two columns CFAA vs Contract; hiQ stamp terracotta bar "$500K · algorithms destroyed". PASS
- **B07 LinkedInRedFlags** — three claim→reality rows with flipped arrows; terracotta verdict bar. PASS
- **B08 ClaudeComposerAsk** — Publishing path, mcp add command, OAuth-only note. PASS
- **B09 ClaudeCodeBeat** — curl POST /rest/posts, bearer token, 201 Created comment. Note: component shows "PYTHON" language label (ClaudeCodeBeat default) — cosmetic only, content is correct curl. PASS
- **BVDT ClaudeVerdictArtifact** — 4-point honest map, terracotta numbers. PASS
- **BHTF ClaudeComposerAsk** — "Your turn." greeting, full classify-my-need prompt. PASS
- **BOUT ClaudeTitleOutro** — title/handle/subline correct. PASS

## Warnings from compile.py (acknowledged)

- B08 empty spark line: ClaudeComposerAsk does not render a spark line — lint false-positive on this beat type. No fix needed.
- 100% Remotion ratio: by design, this is a pure Remotion reel. No pantry beats were appropriate.

## Verdict

**PASS** — ready for final cut.
