# Visual redesign — approved direction and production record

**Current status:** Deepa approved the representative direction in REVIEW.html and Visual_Direction_Review.mp4. All scenes are implemented; both replacement exports passed final technical QC and were promoted to their documented final paths. The original exports remain backed up. Final human video approval is pending.

**Historical preview record:** The proposed plan below records the preview stage. The current [Beat Sheet](BEAT-SHEET.md) describes the implemented compositions.

## References actually inspected

- Deepa’s Week 7 Claude Skills source and rendered Slack GIF Creator frame: animated editor/browser demonstrations and caption hierarchy.
- The local Brutalist toolkit `runtime/remotion/src/tokens/claude.ts`, `illustrations/kit.tsx`, `illustrations/structural.tsx`: cream ground, warm ink, terracotta focal accent, serif headings, frame-driven illustration motion. These are source-based observations; an unavailable finished Claude reel was not claimed to have been viewed.
- Supriya K.’s `2026-09-28-claude-code-explained/scenes.py`: cream/ink palette, terracotta loop emphasis, concept-specific diagram construction.
- Yeshwanth B.’s basketball campaign evidence frame and portrait-code component: layered environment artwork and width-fitted vertical typography.
- Divij’s Mycroft9 grades evidence image: evidence-first comparison and explicit uncertainty.

Reference sources informed composition and visual grammar. Contributor artwork, screenshots and claims were not copied into these videos. All new room, animal, desk and packet illustrations are original React/SVG work. The EB Garamond font is accompanied by its OFL license.

## Proposed direction

Warm editorial illustration: cream paper, dark ink, terracotta and sage accents; EB Garamond headings with Montserrat labels. The environment carries the explanation: furnished room and camera view, layered landscapes and historical vignette, editing desk or physical review pipeline. Frame-driven camera/cursor/character movement follows the topic rather than adding unrelated decorative motion.

## Scene plan

| Scene | Existing time window (s) | Proposed composition |
|---|---|---|
| 1 | 0.000–22.083 | Enter a publishing workbench with a five-contributor collection and a prepared review packet; Week 9 remains the focus. |
| 2 | 22.083–43.375 | Arrange five animated contributor collections with 4/4/4/3/2 counts; clearly identify 17 submissions. |
| 3 | 43.375–70.750 | Use a submission-record workbench to show why actual topic mappings matter. Do not attribute the suggested reference topics to Week 9. |
| 4 | 70.750–98.792 | Follow a source record into a title-editing surface; visual editing demonstrates subject accuracy without inventing submission titles. |
| 5 | 98.792–123.542 | Assemble subject, educational purpose and key concepts into the description portion of the packet. |
| 6 | 123.542–145.875 | Animate contributor cards converging into a title-and-description packet and FOR REVIEW stamp. The decision remains pending. |
| 7 | 145.875–166.042 | Compare two physically distinct collections labeled Week 8 comparison:14 and Week 9 current:17; combine to31 without counting earlier work. |
| 8 | 166.042–181.750 | Close on the prepared review packet, contributor coordination and the existing reflection; no final publication/approval asserted. |

## Review assets and source

- [Draft source](src/redesign/Preview.tsx)
- [Draft Beat Sheet](src/redesign/beat_sheet.draft.json), retaining all original narration and timing
- Local preview images: `_qc/redesign/LandscapeDraft.png` and `_qc/redesign/PortraitDraft.png`
- Local six-second motion sample: `_qc/redesign/VisualSample.mp4`

The preview uses a six-second excerpt of existing narration, not new TTS. It is a style sample, not a complete scene or final video. Full-duration continuity, transitions, all-scene readability and final QC must be checked after approval and implementation. Existing durations remain 181.75 seconds in both formats.

## Preview validation

The 1920×1080 six-second sample has 144 frames at 24 fps and a valid AAC excerpt from the existing narration. Full-stream decoding passed. Landscape and portrait stills were inspected for title/caption placement and visual readability. This limited check is not final-video QC. Rebuild with `node src/redesign/render-preview.cjs . --sample` using the existing local Remotion runtime.

## Approved redesign continuation — Approved direction implemented

Deepa approved REVIEW.html and Visual_Direction_Review.mp4 in conversation. The full scene implementation is now in src/redesign/Worlds.tsx and src/Root.tsx. Active Beat Sheets describe the actual compositions and unchanged audio clock. The draft file and preview remain historical design artifacts, not the current production contract. Final video review is pending separately.
