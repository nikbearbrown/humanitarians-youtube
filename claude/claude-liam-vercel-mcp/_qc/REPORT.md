# Visual QC Report — claude-liam-vercel-mcp
**"Claude, Trusted."** · 2026-07-18

Frames extracted at 2 fps from master mp4 + per-beat 15/50/85% stills.
9-point rubric applied to each beat: (1) edge bleed/clipping, (2) title-safe margins,
(3) container overflow, (4) element collision, (5) offscreen anchors, (6) legibility,
(7) brand/bug placement, (8) aspect ratio, (9) canvas fill.

---

## Beat-by-beat results

| Beat | Scene | Duration | Result | Notes |
|------|-------|----------|--------|-------|
| B00 | ClaudeComposerAsk | 20.4 s | **PASS** | Greeting, spark, composer card, output lines all present; cream bg, terracotta accents correct |
| B01 | VercelOfficial | 27.8 s | **PASS** | Green OFFICIAL badge, mcp.vercel.com URL, BETA/OAUTH pills, Claude Code+Desktop highlighted; sparkLine present |
| B02 | ClaudeComposerAsk | 26.7 s | **PASS** | Setup command visible, detection output in terracotta mono, "@NikBearBrown" folder, "@NikBearBrown" folder correct |
| B03 | VercelDiagnose | 25.9 s | **PASS** | Three-step flow (red→white→green), tool names in code block, arrows, sparkLine correct |
| B04 | VercelAccountEquivalent | 27.7 s | **PASS** | Verbatim quote chip, key icon, four cluster cards (READ green, WRITE/DEPLOY plain, buy_domain terracotta); no tool count shown |
| B05 | VercelBuyDomain | 35.5 s | **PASS** | buy_domain badge, 6 form fields active in terracotta, price tag, expectedPrice "price-check not confirm"; **never shows completed purchase ✓** |
| B06 | VercelSafeguardGap | 31.4 s | **PASS** | Green Connection Consent (PRESENT) vs dark Per-Tool Confirm (ABSENT); "NOT THE SAME" dashed divider; **does NOT imply per-tool confirm exists ✓** |
| B07 | VercelOwnGuidance | 34.7 s | **PASS** | Rebuilt doc card (not screenshot); "REBUILT — NOT A SCREENSHOT" badge visible; pull-quote with terracotta border; Vercel attribution |
| B08 | VercelMitigations | 37.4 s | **PASS** | Two-panel layout; code block `vercel mcp --project my-app`; Narrow/Revocable/Yours bullets; sparkLine correct |
| BVDT | ClaudeVerdictArtifact | 30.6 s | **PASS** | "Claude + Vercel MCP — the honest map" artifact; 5-point verdict list; spark icon; clean layout |
| BHTF | ClaudeComposerAsk | 26.8 s | **PASS** | "Your turn." spark + full handoff prompt; "@NikBearBrown" folder; "paste this into Claude…" in terracotta |
| BOUT | ClaudeTitleOutro | 2.9 s | **PASS** | "Claude, Trusted." centered; terracotta period; "@NikBearBrown" handle; "Liam, in for Bear." subline |

---

## Constraint compliance

| Constraint | Status |
|-----------|--------|
| REBUILD LAW: no Vercel dashboard/docs screenshots | ✓ B07 is a rebuilt styled card with explicit "REBUILT" badge |
| ACCURACY: buy_domain never completes a purchase | ✓ B05 shows only fields + price-check, no confirm/submit action |
| ACCURACY: B06 never implies per-tool confirm exists | ✓ Right box is ABSENT/dark — not a future suggestion |
| ILLUSTRATE LAW: Claude UI only in B00/B02/BHTF/BVDT/BOUT | ✓ All other beats are concept illustration scenes |
| No tool COUNT on screen | ✓ B04 shows clusters, not a number |
| Free pipeline only (no ElevenLabs, no Higgsfield) | ✓ All Remotion renders, Kokoro audio |
| Clock locked — no audio regeneration | ✓ mp3/ untouched |

---

## Summary

**0 BLOCKER · 0 MAJOR · 0 MINOR**

All 12 beats pass the 9-point rubric. Build is ready for review.
