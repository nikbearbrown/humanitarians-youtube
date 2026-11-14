# BUILD-LOG — What Is RAG?

**2026-11-05**
- Script v2 (about 2½ minutes) approved by Tanishaa in chat ("Approve, build it"). Voice: Bella (`af_bella`), chosen by Tanishaa in chat.
- Toolkit: brutalist.art cloned 2026-11-05 (commit recorded in README.md), running in the micromamba env `brutalist`.
- Audio: Kokoro `af_bella` at speed 0.95, 10 beats, 156.7 s of narration, cost $0.00.
- Library-first (GATE L): searched `./art scenes` for retrieval pipelines, nearest-neighbour maps, ranked lists and two-column sorts. The hits were all reel-specific with hardcoded content (CwcMemoryRetrieval, TtTwoAnswers, MedhavyTwoColumnCard). Wrote `runtime/remotion/src/RagScenes.tsx` with six parameterized scenes (RagTwoAnswers, RagPipeline, RagEmbeddingMap, RagRetrievalDemo, RagWhenToUse, HaiTitleOutro), registered under the Root.tsx folder "Rag".
- Decisions (also in beat_sheet metadata):
  - The body uses the Claude cream palette for one consistent look.
  - The HAI mark is the corner logo on every beat: drawn in the RAG scenes, composited by `add_bug.py` on the library scenes.
  - The outro is HaiTitleOutro, because ClaudeTitleOutro is locked to @NikBearBrown.
  - B05 uses keyword search so the demo is real and runnable. B04 explains embeddings schematically and is captioned that way.
- Still preflight (`remotion_scenes.py --stills`): fixed B04 label collision, enlarged B06 type, set `largeText` on the composer beats and `lectureLayout` on the verdict.
- Not implemented by the toolkit: `lead_silence_s` (no script reads it). B01 still has 11 s of audio, above the 9 s minimum.
- Review compile (`./art run`): GATE V flagged every frame because the review cut's timecode burn-in (top-right; drawn only when ffmpeg has drawtext, which the conda ffmpeg does) sits outside the checker's excluded strip. This is a toolkit quirk, not a scene defect. Checked the clean master instead.
- `./art final`: fixed B05 accent contrast (GATE T), the B07 logo/label collision, and B01/B09 underfill. Final result: GATE T PASS, GATE V 0 BLOCKER / 0 MAJOR, 10/10 slots filled. Master: `what-is-rag.mp4` (3840×2160, 24 fps, 156.9 s), moved here from the toolkit's renders/ folder per "videos travel with their book".
- My frame review (one frame every 6 s): correction, stamp, pipeline, map links, real scores and the HAI bug all land on cue.
- Open: integrated loudness is -20.9 LUFS (quiet compared with YouTube's ~-14). The 9:16 vertical is not built yet. Remotion 4.0.535 is installed, while 4.0.541 is the latest.

**2026-11-06**
- Intro greeting changed from "Hej, HAI" to "Hi, Tanishaa" (Tanishaa's request). Only B00 was re-rendered.
- Sync fix (Tanishaa reported a lag in B06 around 1:52). Cause: reveal times were estimated from word position, which drifts at every pause, and fades lasted more than a second. Fix: `word_times.py` measures real word starts with faster-whisper → mp3/words.json, and `build_sheet.py` cues each reveal 0.2 s before its measured word. All RAG-scene fades are now 0.35 s, and the B06 headings are cued to "should you use" / "shouldn't you". B02–B07 re-rendered.
- Verified in the master: transcribed 94–122 s of its audio and grabbed frames 0.6 s before and 0.25 s after each cue word. Every item is absent before and present on its word. GATE T PASS, GATE V 0/0.
- 9:16 vertical companion (`./art vertical` → `vertical/`, all 10 beats, no drops):
  - Wrote native portrait layouts `<Name>916` for the six RAG scenes in RagScenes.tsx. The library 916s are used for the composer, writer and verdict.
  - GATE T in portrait measures glyph height against 1.9% of 3840 px, so portrait type is serif ≥ 92 / sans ≥ 72 design px.
  - SHOW LESS applied in portrait:
    - No spark lines or stage details (the narration says them).
    - First sentences only.
    - `footnoteShort` honesty captions.
    - B04 uses portrait-only map positions (`chunks916`).
  - Other fixes: B03 accent bars/chips use the darker terracotta. The B06 heading underline was spaced off the descenders (it fused into one "text run"). B08 composer uses normal text, not large (it overflowed the 9:16 bottom inset). B09 outro enlarged. B01 is three lines at 160 with 1.65 spacing, raised.
  - The derived `vertical/beat_sheet.json` was edited directly for B01, B08 and footnoteShort. `build_sheet.py` carries footnoteShort and chunks916 so a regenerated vertical keeps them.
- `./art final vertical --height 3840` (without `--height` it builds 1216×2160): GATE T PASS, GATE V 0/0, 10/10 slots. Master `vertical/what-is-rag-vertical.mp4` is 2160×3840, 156.9 s. My review: frames every 6 s, and B06 cue frames before/after each word are in sync, same as landscape.
