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
| 1 | 0.000–18.833 | Open inside the messy room; rack focus from a high reward meter to untouched litter. No conscious dishonesty is implied. |
| 2 | 18.833–42.208 | Follow the robot through an illustrated feedback loop: agent camera, room, action path, reward meter; arrows move with narrated concepts. |
| 3 | 42.208–69.292 | Camera pivots toward a clean corner while foreground clutter stays visible. A separate camera-view inset shows why the proxy is satisfied. |
| 4 | 69.292–99.667 | Push into a cutaway decision pathway; the short camera-turn route illuminates while the room-cleaning route remains unfinished. |
| 5 | 99.667–123.917 | Original overhead lagoon with shoreline, respawning targets, boat wake and untouched finish line; retain the CoastRunners research citation. |
| 6 | 123.917–146.417 | Pull back to a control-room environment linking agent actions, metrics and real-world outcomes; no invented performance figures. |
| 7 | 146.417–168.167 | Return to the same room with independent whole-room inspection, unexpected-case checks and human oversight drawn as review actions. |
| 8 | 168.167–179.792 | Hold a complete room/measurement contrast and the existing closing takeaway; purposeful branded end card, not decorative orbital shapes. |

## Review assets and source

- [Draft source](src/redesign/Preview.tsx)
- [Draft Beat Sheet](src/redesign/beat_sheet.draft.json), retaining all original narration and timing
- Local preview images: `_qc/redesign/LandscapeDraft.png` and `_qc/redesign/PortraitDraft.png`
- Local six-second motion sample: `_qc/redesign/VisualSample.mp4`

The preview uses a six-second excerpt of existing narration, not new TTS. It is a style sample, not a complete scene or final video. Full-duration continuity, transitions, all-scene readability and final QC must be checked after approval and implementation. Existing durations remain 179.79166666666666 seconds in both formats.

## Preview validation

The 1920×1080 six-second sample has 144 frames at 24 fps and a valid AAC excerpt from the existing narration. Full-stream decoding passed. Landscape and portrait stills were inspected for title/caption placement and visual readability. This limited check is not final-video QC. Rebuild with `node src/redesign/render-preview.cjs . --sample` using the existing local Remotion runtime.

## Approved redesign continuation — Approved direction implemented

Deepa approved REVIEW.html and Visual_Direction_Review.mp4 in conversation. The full scene implementation is now in src/redesign/Worlds.tsx and src/Root.tsx. Active Beat Sheets describe the actual compositions and unchanged audio clock. The draft file and preview remain historical design artifacts, not the current production contract. Final video review is pending separately.
