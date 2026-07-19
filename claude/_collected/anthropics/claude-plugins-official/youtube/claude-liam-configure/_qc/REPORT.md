# QC Report — claude-liam-configure

**Date:** 2026-07-18  
**Duration:** 5:18 (318.0s compiled)  
**Verdict:** PASS

## Frame audit

| Frame | Beat | Notes |
|---|---|---|
| frame_16s_B00.png | B00 cold open | ClaudeComposerAsk: "Ciao, Liam", Discord bot config query, 3 output lines, @NikBearBrown |
| frame_62s_B01.png | B01 anatomy | ConfigureAnatomy: 3-mode dispatch column (left, token save highlighted terracotta) + state files + next-step-by-state (right) |
| frame_121s_B02.png | B02 design | ConfigureDesign: 6-step lockdown flow (left, step 3 highlighted) + 4 implementation rules (right) |
| frame_199s_B05.png | B05 teardown | ConfigureTell: callout + standard 5+5 two-column teardown, spark line with asterisk |
| frame_259s_BVDT.png | BVDT verdict | ClaudeVerdictArtifact: "Configure" heading, 6 terracotta-numbered lines |
| frame_295s_BHTF.png | BHTF handoff | ClaudeComposerAsk: "Your Turn", fake-token test prompt, expected/red-flag output |
| frame_316s_BOUT.png | BOUT outro | ClaudeTitleOutro: "Configure" title |

## Rubric

| Check | Result |
|---|---|
| Canvas fill >65% | PASS |
| Text readable at all beats | PASS |
| Column alignment correct | PASS |
| Callout / spark line visible (B05) | PASS |
| No Inter font | PASS |
| No purple gradient | PASS |
| No uniform rounded corners | PASS |
| No excessive centering | PASS — dispatch+files B01, steps+rules B02, two-column B05 |

## Notes

- Greeting: "Ciao, Liam" (rotation #39)
- New scenes: ConfigureAnatomy (B01), ConfigureDesign (B02), ConfigureTell (B05)
- B01 three-mode dispatch: token-save highlighted terracotta as the key action mode
- B02 lockdown step 3 highlighted: the proactive allowlist-flip offer
- B05 callout: old-token restart asymmetry — the silent failure scenario
