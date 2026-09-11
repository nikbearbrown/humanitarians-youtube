# Process notes — How PagedAttention Works (both cuts)

**VideoLocation:**https://drive.google.com/drive/folders/1CY_suzRRK4f05C5OeNKXm-5Bw6Ynhv1H?usp=sharing
**Status:** shipped-to-chat · committed to device folder · not yet staged to Drive · not yet published to YouTube
**Channel:** claude-hai · **Resolution:** 3840x2160 (16:9) / 2160x3840 (9:16)
**Last updated:** 2026-09-10

Build log for `hai-paged-attention` (16:9) and `hai-paged-attention-916` (9:16 Shorts). Chronological; append-only going forward — add dated entries, don't rewrite history.

## 2026-09-10 — script → both cuts built at true 4K

**Starting point:** the user asked for a 4-minute script explaining PagedAttention, which was written and delivered as `SCRIPT-paged-attention.md` (12-beat ai-explainer script, no sprint report behind it — general LLM-serving mechanics, a direct follow-on to `how-kv-cache-works`, which named PagedAttention as a memory-cost mitigation without explaining it). The user then asked to run the same pipeline and produce both final videos plus supporting docs — this build.

**GATE L:** searched the existing Remotion component library (`runtime/remotion/src/scenes/`, ~500 files, including a targeted pass over memory/paging/cache/fan-out-shaped names) before authoring anything new. Nothing fit two of the script's shapes — a logical-to-physical block indirection through a lookup table, and a single shared origin fanning out to several candidates where only one diverges — so two genuinely new components were required. Everything else in the script matched shapes already built and QC'd on prior reels (`hai-mycroft-gateway`, `how-kv-cache-works`), reused with new props.

**2 new Remotion components authored** (in `runtime/remotion/src/scenes/`, registered in `Root.tsx`, each portrait/landscape-responsive off one motion-math source):
- `PageTable` — logical blocks in order on the left, a "block table" label in the middle, the same blocks scattered into a fixed-reversal order on the right, connected by crossing lines. Built for PagedAttention's core mechanic — the page-table indirection it borrows directly from OS virtual memory (B04)
- `SharedBlocks` — one shared block cluster at top, N candidate paths fanning down from it; one candidate's line switches from solid to dashed-terracotta partway down, and that candidate's box carries a "diverged → copied" note. Built for copy-on-write sharing across parallel-sampling / beam-search candidates (B06)

**9 beats reused existing components with new props** (already built and QC'd on `hai-mycroft-gateway` and `how-kv-cache-works`, no code changes needed): `FactStack` three times (before-PagedAttention facts, allocation-on-demand facts, reclaimed-memory facts), `GrowthMeter` once (the reserved/used/wasted bar comparison), `DataTable` once (the before/after waste-percentage table), plus the four always-reused house components (`ClaudeComposerAsk` ×2, `ClaudeStatement`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`).

**9:16 Shorts cut designed** per THE SHORTS LAW: single cycle, no revision pass — B00 (cold open, condensed) → B01 (the idea, stated) → B02 (the comparison table, `DataTable916`, same content as the long cut's B07 — the one real "wait, what" number) → B03 (verdict, condensed) → B04 (outro, points back to the long cut). The waste-percentage stat was chosen over the block-table diagram as the reused middle beat because it's the one moment that lands on its own without the setup the diagram needs — same reasoning the router reel used to pick its comparison table over a mechanism diagram for its own Shorts cut.

**Both new components read clean on their first rendered still** — no fixes needed, a change from the last two builds in this series (both had at least one layout defect caught by VISUAL QC LAW). `PageTable`'s fixed-reversal physical order (`n-1-i`, not a real shuffle algorithm) was a deliberate simplification, documented in the component's own doc comment, to guarantee crossing lines without motion-math complexity the diagram doesn't need to earn its point.

**Audio:** Kokoro `af_bella`, one pass per cut, both run via `nohup … & disown` from the start (the timeout on the 15-beat Sprint 3 router build was already a known risk, so this build didn't wait to hit it again). 16:9 (12 beats) finished in about 2 minutes; 9:16 (5 beats) in under a minute. `actual_duration_s` in each beat sheet is ground truth for everything downstream — this script's estimated durations (word-count based, targeting the user's requested 4:00) ran noticeably *short* against Kokoro's actual pace on this build, landing the 16:9 cut at 3:33 rather than 4:00. That's the opposite of the pattern on the last two builds, where Kokoro ran long — a reminder that the word-count estimate is a rough placeholder in either direction, not a lower or upper bound. Per this series' no-revision-after-audio convention, the cut was not re-padded or re-scripted to hit 4:00 exactly.

**Rendering:** true 4K via `ART_SCALE` default (scale=2), Chrome launched from this session's own container with `--chrome-mode=chrome-for-testing`. One beat per `remotion_scenes.py --only <BID>` call, all 17 beats (12 + 5) rendered with no failures — but the first call (16:9 B00) hit the Bash tool's default 2-minute timeout with zero output, because `subprocess.run(capture_output=True)` in `remotion_scenes.py` buffers everything until the render finishes and a true-4K single-beat render plus the freeze-hold extend step can run past 2 minutes on its own. Fixed by re-running with an explicit 5-minute timeout on every subsequent render call rather than backgrounding each one individually — simpler than the audio/compile nohup pattern for a step that's already one-call-per-beat and doesn't need polling.

**Compiling:** both cuts compiled in the background (`nohup … & disown`), cwd verified via `readlink /proc/<pid>/cwd` before trusting either process, polled via `tail`/`ps aux` until each "wrote … .mp4" line appeared. 16:9 compiled at `--height 2160`, took a little over 4 minutes end to end (render-stitch, not just mux — the output file grew visibly across several polls rather than appearing all at once); 9:16 at `--height 3840` finished within the first poll.

**Final QC on compiled masters:** sampled actual frames from both *compiled* outputs — 12 timestamps across the 16:9 master (one per beat, including both new components in the real render context, not just their isolated QC stills), 5 across the 9:16 master (one per beat) — to confirm transitions, conforming, and text-safe crops all read clean end to end, including both outro cards. No defects found on either cut.

**Final specs:**

| Cut | Resolution | Duration | File size |
|---|---|---|---|
| 16:9 | 3840×2160 | 3:33 (213.6s) | 9.1 MB |
| 9:16 | 2160×3840 | 0:59 (59.3s) | 2.9 MB |

**Non-blocking lint carried from the compile logs (flagged, not treated as blocking):**
- 16:9: "illustrate" motion carries 7/12 beats (58%), over the ~40% pantry-cap guideline in `MOTION.md` — this script's structure/problem/reasoning/results middle section leans heavily on illustrated diagrams and fact stacks, same pattern already flagged and accepted on the Gateway, KV-cache, and router reels in this series.
- 9:16: SKIN LINT on B00/B04 — `ClaudeComposerAsk916` / `ClaudeTitleOutro916` flagged against COLD OPEN LAW / OUTRO LAW, the same false-positive already noted on every other video in this series (the linter doesn't account for the `916` responsive-variant naming convention).

**Delivered:** both masters sent to Simba, and committed alongside this build's three docs (plus `SCRIPT-paged-attention.md`) into `youtube/09102026paged-attention/` on the connected device — `hai-paged-attention.mp4`, `hai-paged-attention-916.mp4`.

## Open item — publishing not yet possible from this repo

Same open item logged on the other videos in this series: this toolkit checkout (`brutalist.art`) stops at render, and `./art final` / `./art post` / the `youtube-publisher` script aren't present here — see `RENDER-4K-AND-UPLOAD.md` and `docs/PUBLISHING.md` at the repo root. Dropping the two finished mp4s straight into the reel's `youtube/` folder is a reasonable interim landing spot but not the sanctioned `TOPOST` staging path. Google Drive link for this video is also still TBD — add it here once the files are staged there, same as the other videos' entries.
