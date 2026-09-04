# Process notes — How KV Cache Works (both cuts)

**Google Drive:** https://drive.google.com/drive/folders/1-H-vE7c3x-pJmIU_Jw5rjhPBydSJfA8q?usp=sharing
**Status:** shipped-to-chat · not yet staged to Drive · not yet published to YouTube
**Channel:** claude-hai · **Resolution:** 3840x2160 (16:9) / 2160x3840 (9:16)
**Last updated:** 2026-09-04

Build log for `how-kv-cache-works` (16:9) and `how-kv-cache-works-916` (9:16 Shorts). Chronological; append-only going forward — add dated entries, don't rewrite history.

## 2026-09-04 — script → both cuts built at true 4K

**Starting point:** `SCRIPT-kv-cache.md` (12-beat ai-explainer script, written in a prior pass at the user's request for a video narration script on KV caching — no sprint report behind it, general transformer-inference mechanics instead). This session built both final videos from that script.

**GATE L:** searched the existing Remotion component library (`runtime/remotion/src/scenes/`, ~490 files) before authoring anything new. Nothing fit the KV-cache-specific content (Query/Key/Value fan-out, a decode step's append-and-attend flow, a growing-cost bar chart), so three genuinely new components were required — but three other beats matched shapes already built and QC'd for the Mycroft Gateway reel closely enough to reuse with new props rather than duplicate.

**3 new Remotion components authored** (in `runtime/remotion/src/scenes/`, registered in `Root.tsx`, each portrait/landscape-responsive off one motion-math source):
- `TokenSplit` — one token box fans out via connecting lines into N labeled projection cards (Query/Key/Value), plus a dashed causal-masking note beneath (B02)
- `GrowthMeter` — N vertical bars growing from a baseline, last bar accented; used twice, once for the naive-recompute cost (B03) and once for the cache's own memory growth (B07). Written new rather than reusing the house `BarChart`, which lives on the separate `vox` token/font system this reel family doesn't use
- `DecodeStep` — a five-box top-to-bottom pipeline (new token → compute → two branches → output) for one real decode step; used in both cuts (16:9 B05 and the Shorts cut's B02), so it's the highest-stakes new component on this reel and got both orientations built and QC'd together

**3 components reused with new props** (already built and QC'd for `hai-mycroft-gateway`, no changes needed): `DataTable` as the append-only cache table (B04), `FindingPair` for the flat-vs-growing cost comparison (B06), `TestSuiteProof` for the four mitigation levers — GQA, sliding window, quantized cache, PagedAttention (B08).

**9:16 Shorts cut designed** per THE SHORTS LAW: single cycle, no revision pass — B00 (cold open, condensed) → B01 (the idea, stated) → B02 (the one real decode step, reusing `DecodeStep916` with the same props as the long cut's B05) → B03 (verdict, condensed) → B04 (outro, points back to the long cut).

**Audio:** Kokoro `af_bella`, one pass per cut. `actual_duration_s` in each beat sheet is ground truth for everything downstream — the 16:9 cut ran long against its own word-count estimate (4:24 measured vs. ~3:51 estimated), mainly on B06 and B08, the two most clause-dense technical beats.

**Rendering:** true 4K via `ART_SCALE` default (scale=2). Chrome launched from this session's own container (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`) with `--chrome-mode=chrome-for-testing`. Rendered one beat per `remotion_scenes.py --only <BID>` call rather than the full batch, per the lesson learned on the two prior builds in this series — all 17 beats (12 + 5) rendered this way with no failures. 16:9 compiled at `--height 2160`; 9:16 at `--height 3840`, both run in the background (`nohup … & disown`, polled) so the final concat+mux step wasn't cut off by the foreground command timeout.

**QC pass — 3 real defects caught and fixed before the full render, not after** (VISUAL QC LAW: judged from rendered stills actually read, not from code review alone):

1. **`TokenSplit` internal empty space.** First QC still showed the three projection cards top-aligned inside taller-than-needed boxes, plus a wide gap between the causal-masking note and the sparkline. Fixed by reducing landscape card height (0.24→0.20 of frame height), vertically centering card content via flexbox column + `justifyContent: center` instead of top-padding, and giving the mask note a fixed height with centered text. A second-pass still showed the gap narrowed but not fully closed — judged acceptable against the same tolerance this series has already accepted elsewhere (e.g. `EvidenceTrail`'s minor dead space on the Gateway reel).

2. **`GrowthMeter` value-label text wrap.** The bar's value+unit label (e.g. "1 tokens redone") wrapped onto two lines because its containing div was only as wide as the bar itself. Fixed by widening the label div to the bar width plus half the inter-bar gap, with a compensating left offset and `whiteSpace: nowrap`. Re-rendered and confirmed clean before this component's two beats (B03, B07) were rendered into either cut.

3. **`DecodeStep` portrait layout, two rounds.** First portrait still showed the two stacked branch cards visually overlapping the output box below them — the branch stack's computed span ran past where the output box started. Fixed by recalculating all portrait vertical offsets. A second still, after that fix, showed the overlap gone but roughly 30% of the frame now empty between the output box and the sparkline — portrait wasn't using the extra vertical room a 9:16 frame has over landscape's proportions. Fixed by widening every portrait gap and box height so the five-box flow spans more of the frame. Landscape needed no changes at either round — it read clean on the first try. Confirmed clean in both orientations before this component's two beats (16:9 B05, Shorts B02) were rendered.

All three fixes shipped before the corresponding beats were rendered into either final cut.

**Final QC on compiled masters:** sampled actual frames from both *compiled* outputs — 8 timestamps across the 16:9 master, 4 across the 9:16 master — not just the isolated component stills, to confirm transitions, conforming, and text-safe crops all read clean end to end. No further defects found.

**Final specs:**

| Cut | Resolution | Duration | File size |
|---|---|---|---|
| 16:9 | 3840×2160 | 4:24 (264.3s) | 10.6 MB |
| 9:16 | 2160×3840 | 1:04 (64.2s) | 3.1 MB |

**Non-blocking lint carried from the compile logs (flagged, not treated as blocking):**
- 16:9: "illustrate" motion carries 6/12 beats (50%), over the ~40% pantry-cap guideline in `MOTION.md` — this script's middle section (STRUCTURE/PROBLEM/RESULTS/REASONING) leans heavily on illustrated diagrams, same pattern already flagged and accepted on the Gateway reel.
- 9:16: SKIN LINT on B00/B04 — `ClaudeComposerAsk916` / `ClaudeTitleOutro916` flagged against COLD OPEN LAW / OUTRO LAW, the same false-positive already noted on the other videos in this series (the linter doesn't account for the `916` responsive-variant naming convention).

**One content fix caught during authoring, not after:** B10's on-screen command prop initially carried leftover phrasing copied from the Mycroft Gateway script ("a single door every call has to pass through") — caught on review and rewritten to a KV-cache-appropriate ask before any audio or render pass touched it. Also fixed a stray accented character in B03's kicker ("NAÍVELY" → "NAIVELY") before rendering.

**Delivered:** both masters sent to Simba and committed into `youtube/hai-how-kv-cache-works/` on the connected device (`hai-how-kv-cache-works.mp4`, `hai-how-kv-cache-works-916.mp4`).

## Open item — publishing not yet possible from this repo

Same open item logged on the other videos in this series: this toolkit checkout (`brutalist.art`) stops at render, and `./art final` / `./art post` / the `youtube-publisher` script aren't present here — see `RENDER-4K-AND-UPLOAD.md` and `docs/PUBLISHING.md` at the repo root. Dropping the two finished mp4s straight into the reel's `youtube/` folder is a reasonable interim landing spot but not the sanctioned `TOPOST` staging path. Google Drive link for this video is also still TBD — add it here once the files are staged there, same as the other videos' entries.
