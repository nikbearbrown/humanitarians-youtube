# SHOTLIST.md — How the Tutor Stays Grounded in Your Textbook

- **Skill:** `medhavy-walkthrough`, textbook mode, book "Cancer textbook" (cancer.medhavy.com), **admin account**.
- **Voice:** Kokoro `am_onyx` (Liam), AI narration. 434 words in landscape, 431 in vertical (B11 wording differs).
- **Runtime:** 167.93 s for both versions (shared narration clock).

**Status: FINAL / LOCKED (2026-09-29).**
- The windows below are the frame-exact cuts used in the finals.
- Landscape windows come from `beat_sheet.json`; vertical windows come from `vertical-windows.json`.
- Footage windows are longer than their narration, and the gaps are silence so the UI can breathe.

## Beats

| Beat | Act | Dur. | Landscape source (window, s) | Vertical source (window, s) | On screen |
|---|---|---|---|---|---|
| B00 | INTRO | 11.73 | Remotion `ClaudeComposerAsk` | `ClaudeComposerAsk916` | Central question; "AI narration (Kokoro am_onyx)" running text |
| B01 | QUESTION | 10.87 | Remotion `BrutalistHesitantWriter` | `BrutalistHesitantWriter916` (card removed, 165 px line) | "The sources **prove** the answer." → "…**supply context for**…" |
| B02 | BODY | 5.50 | `run-signin` [13.5, 19.0] | `run-signin` [13.5, 19.0] · "Signed in off camera" | Sign-in card, signed out, nothing typed |
| B03 | BODY | 9.50 | `run-book` hub tab [5.5, 15.0] | `run-portrait` hub tab [3.0, 12.5] · "The textbook shelf" | Admin Dashboard (header "Admin account") → View All Textbooks → Cancer textbook → Open Textbook |
| B04 | BODY | 4.80 | `run-book-p2` [9.0, 13.8] | `run-portrait-p2` [9.9, 14.7] · "Chapter 5 · Oncogenes" | Sidebar "5. Oncogenes" → "5.1 Introduction to Oncogenes" |
| B05 | BODY | 13.70 | `run-book-p2` [13.8, 27.5] | `run-portrait-p2` [14.7, 28.4] · "Ask this textbook" | Panel opens; chips from the page title; question typed |
| B06 | BODY | 9.00 | `run-book-p2` [27.5, 36.5] | `run-portrait-p2` [28.4, 37.4] · "Retrieved passages" | "AI is thinking…"; cards + "Dive deeper (10)" arrive just before the answer text |
| B07 | BODY | 4.20 | `run-book-p2` [36.5, 40.7] | `run-portrait-p2` [37.4, 41.6] · "The answer" | Answer under the cards |
| B08 | BODY | 5.40 | `run-book-p2` [40.7, 46.1] | `run-portrait-p2` [41.6, 47.0] · "All ten sources" | "Dive deeper (10)" expands; ends before the 5.4 page loads |
| B09 | BODY | 17.90 | `run-book-p2` [46.1, 64.0] | `run-portrait-p2` [47.0, 64.9] · "Open a source" | 5.4.2 card → 5.4 → "On this page" → 5.4.2 section and figure |
| B10 | MECHANISM | 17.13 | Reel-local `GroundingFlow` | Reel-local `GroundingFlow916` (via `pantry/B10-916.mp4`) | Six plain steps: question → search → relevant passages → given to the model as context (passages · tutor instructions · recent conversation) → answer → you inspect |
| B11 | BODY | 22.00 | `run-book-p2` [75.0, 97.0] | `run-portrait-p2` [73.8, 95.8] · "A follow-up" | Follow-up typed; new cards (Angiopoietin, Two-Hit) + "Dive deeper (10)". Landscape also shows the reply building on the first answer. |
| B12 | BODY | 6.67 | `run-book-p2` [97.0, 103.65] | `run-portrait-p2` [95.8, 102.467] · "The site's own warning" | Footer "AI can make mistakes. Please verify important information." |
| B13 | VERDICT | 18.10 | Remotion `ClaudeVerdictArtifact` | `ClaudeVerdictArtifact916` | "Grounded, Not Guaranteed." |
| B14 | NEXT STEPS | 6.13 | Remotion `ClaudeComposerAsk` | `ClaudeComposerAsk916` | Your Turn |
| B15 | OUTRO | 5.30 | Remotion `ClaudeTitleOutro` | `ClaudeTitleOutro916` | Spoken title + "At Nik Bear Brown"; no jingle |

**Real Medhavy footage:** B02–B09, B11 and B12, 10 beats in each version. B08 and B09 were conditional in the plan; both were confirmed live and kept.

**Remotion:** B00, B01, B10, B13, B14, B15.

## Landscape strategy (16:9, 3840×2160), as executed

1. **The real product is the evidence.**
   - Footage beats are full-bleed native 4K captures (1600×900 CSS at DPR 2.4), `treatment: none`.
   - No zooms, re-timing or overlays.
   - `qc.full_bleed: true` is declared for these beats.
2. **Breathing room.**
   - Narration is shorter than each window and padded with silence, never stretched.
   - Windows end before the next navigation. B08 ends at 46.1 s, one frame before the 5.4 page switches in.
3. **Hub as front door only.** B03 is 9.5 s of click path.
4. **Remotion only where the browser can't show it:** intro, misconception, how it works (`GroundingFlow`), verdict, Your Turn, outro.
5. **GroundingFlow** is drawn in ink, not terracotta, so it passes GATE T §8.3 contrast.
6. **Result:** exported with `./art final`. GATE T PASS; Gate V 0 BLOCKER / 0 MAJOR (QC-REPORT.md).

## Vertical strategy (9:16, 2160×3840), as executed

The vertical is its **own beat sheet and its own layouts**. It is never a squeeze or crop of the landscape master.

- **Kept from landscape:** the same beats, order and claims. Only B11 differs, to match the portrait footage.
- **Source footage:** a dedicated portrait-friendly capture, `run-portrait` (1280×720 CSS at DPR 3, native 3840×2160).
  - It ran after the landscape capture was reviewed and after `run-portrait-test` passed.
  - `run-signin-916src` was not run, so B02 reuses the landscape `run-signin` capture.
- **`PanelFocus916`** (reel-local) plays a frame-exact window of the raw capture at real speed. It frames a region under a caption band; captions only label what is on screen.
  - **Framing rule:** no text line may cross a crop edge.
  - **Panel beats** (B05–B08, B11) show only the tutor-panel column, source x 2580–3840, via `clipX`.
  - **B04** shows only the sidebar column (x 0–802).
  - **B03** fits the whole hub page.
  - **B09** fits the content column, then widens to the full page with the figure.
- **`GroundingFlow916`** (reel-local): six steps stacked vertically, with every text run at or above the GATE T §8.1 floor (Inter 68 / EB Garamond 90).
  - Step numbers are removed; the connectors carry the order.
  - The pills wrap to two rows.
  - The side note is omitted because it can't fit the title-safe box at the floor size. B05's narration carries that point.
- **Bookends:** the registered portrait scenes. For B01, the small "What I Checked" card is removed and the line enlarged, in the vertical only.
- **Result:** exported with a direct `compile.py --height 3840`, not `./art final`.
  - GATE T fails only on **B15**, the locked `ClaudeTitleOutro916` handle (49 px vs 72 px floor). It was checked by eye at phone width and is readable.
  - B01 and B13 carry `qc.sparse_by_design` underfill waivers.
  - Gate V: 0 BLOCKER / 0 MAJOR.
  - Details in QC-REPORT.md.

**Known limitation (flag to PM):** the portrait panel crops upscale the 1260-px source panel about 1.7×, and B02 is upscaled more because it comes from the landscape capture. The Remotion scenes and caption bands are native 2160×3840.
