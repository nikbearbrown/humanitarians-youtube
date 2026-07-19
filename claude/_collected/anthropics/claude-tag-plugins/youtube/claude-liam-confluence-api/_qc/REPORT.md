# QC Report — claude-liam-confluence-api

**Date:** 2026-07-18  
**Duration:** 6:20 (380.2s compiled)  
**Verdict:** PASS

## Frame audit

| Frame | Beat | Notes |
|---|---|---|
| frame_16s_B00.png | B00 cold open | ClaudeComposerAsk: "Hola, Liam", Confluence search query, 3 output lines, @NikBearBrown |
| frame_73s_B01.png | B01 anatomy | ConfluenceApiAnatomy: v2 (green) + v1 (terracotta) version rows + 3 bundled scripts + 4 body format cards |
| frame_126s_B02.png | B02 design | ConfluenceApiDesign: security note callout + pagination trap (v2 highlighted) + 6 error code rows |
| frame_216s_B05.png | B05 teardown | ConfluenceApiTell: callout + standard 5+5 two-column teardown, spark line with asterisk |
| frame_296s_BVDT.png | BVDT verdict | ClaudeVerdictArtifact: "Confluence API" heading, 6 terracotta-numbered lines |
| frame_340s_BHTF.png | BHTF handoff | ClaudeComposerAsk: "Your Turn", label+CQL search prompt, expected/red-flag output |
| frame_378s_BOUT.png | BOUT outro | ClaudeTitleOutro: "Confluence API" title |

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
| No excessive centering | PASS — two-column B01 with format row, two-column B02, two-column B05 |

## Notes

- Greeting: "Hola, Liam" (rotation #40)
- New scenes: ConfluenceApiAnatomy (B01), ConfluenceApiDesign (B02), ConfluenceApiTell (B05)
- B01: v1 row highlighted terracotta to mark exception-only use; atlas_doc_format card highlighted as warning
- B02: v2 pagination row highlighted terracotta to mark the dangerous default trap; 404 error highlighted
- B05 callout: /wiki prefix warning placement — reads like a context note, not a hard prerequisite
