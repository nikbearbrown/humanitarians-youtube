# Process notes — One File, No Contradictions (both cuts)
**DriveLocation:**https://drive.google.com/drive/folders/1xOoXuHBwvOA8mb8O3YAUd3hiCSPezVJB?usp=sharing
**Status:** shipped-to-chat · committed to device folder · not yet staged to Drive · not yet published to YouTube
**Channel:** claude-hai · **Resolution:** 3840x2160 (16:9) / 2160x3840 (9:16)
**Last updated:** 2026-09-10

Build log for `hai-mycroft-router` (16:9) and `hai-mycroft-router-916` (9:16 Shorts). Chronological; append-only going forward — add dated entries, don't rewrite history.

## 2026-09-10 — Sprint 3 report → script → both cuts built at true 4K

**Starting point:** the user pasted the Mycroft Sprint 3 report directly into this session (task-type routing rules locked into `policy.json`, a pure `router.py`, 24 frozen fixtures, blind labeling against a human, structural and design-risk findings) and asked for a video script. `SCRIPT-mycroft-router.md` (15-beat ai-explainer script) was written first and delivered on its own; the user then corrected that it's specifically the Sprint 3 report (three labeling edits: header, cold-open narration, Sources), then asked for both final cuts plus supporting docs — this build.

**GATE L:** searched the existing Remotion component library (`runtime/remotion/src/scenes/`) before authoring anything new. Nothing fit three of the report's shapes — several identically-structured small cards in a grid (the six task types), a mostly-linear decision path with one side branch to a refusal state (the router), and a short bulleted list of facts with a closing line (used three times for different fact clusters) — so three genuinely new components were required. Five other beats matched shapes already built and QC'd for `hai-mycroft-gateway`, reused with new props: `DataTable` (×2), `FindingPair` (×2), `TestSuiteProof` (×1).

**3 new Remotion components authored** (in `runtime/remotion/src/scenes/`, registered in `Root.tsx`, each portrait/landscape-responsive off one motion-math source):
- `PolicyGrid` — N labeled cards in an explicit grid (not CSS grid/flex-wrap), row height computed from item count so 4 and 8 items both fill the frame. Used once, for the six task types (B02)
- `RouterFlow` — a vertical main decision path of N boxes with one dashed side branch to a muted "refused" box, plus a struck-through note for a rule deliberately left out. Used once, for the router itself (B03)
- `FactStack` — N bulleted fact lines plus a terracotta-bordered closing-line card. Used three times, for three different fact clusters (B05 synthetic-data caveat, B06 labeling methodology, B09 what the checks catch)

**5 beats reused existing components with new props** (already built and QC'd for `hai-mycroft-gateway`, no code changes needed): `TestSuiteProof` for the bench-tools/fixture-count summary (B04), `DataTable` for the labels-vs-router comparison (B07) and the two check-breaking fixtures (B10), `FindingPair` for the two-paths-to-strong finding (B08) and the two fixed problems (B11).

**9:16 Shorts cut designed** per THE SHORTS LAW: single cycle, no revision pass — B00 (cold open, condensed) → B01 (the rule, stated) → B02 (the comparison table, `DataTable916`, same props as the long cut's B07 — the one real "wait, what" moment) → B03 (verdict, condensed) → B04 (outro, points back to the long cut).

**A factual-accuracy issue caught before it shipped, not after.** The first pass at `PolicyGrid`'s props gave each of the six task-type cards a specific fabricated subtitle (e.g. "sentiment: start cheap, escalate mid") — plausible-looking, but the source report only ever gave the *aggregate* tier counts (6/11/7 human labels, 8/16/0 router labels), never each task type's individual starting or escalation tier. Caught this on review before the beat sheet or any render touched it. Fixed by changing the component's schema from `{label, startTier, escalateTier}` to `{label, note}` — a generic free-text subtitle — and using the same generic note ("format · labels · check · tier · length") across all six cards, which accurately reflects only what the report actually stated: that each task type is locked to those five shared fields, without inventing what any individual type's values are. Documented in the component's own doc comment so the reason isn't lost.

**2 real layout defects caught and fixed via VISUAL QC LAW** (rendered stills actually read, not code review alone):

1. **`RouterFlow` landscape overflow.** First QC still placed the refuse box partially off the right edge of the 1920px frame, clipping its text. The original math (`boxW = width*0.72`, then a fixed offset for the side box) didn't budget the two regions to sum within the frame. Fixed by explicitly computing `mainW` and `refuseW` so together with padding and the gap between them they fit the frame width, and rendering a second still to confirm the refuse box fully on-canvas and readable.
2. **`RouterFlow` portrait overlap, fixed proactively without a portrait render** (this reel's 9:16 cut doesn't use `RouterFlow`, so there was no beat to render it against, but the bug was visible from the math alone): the original portrait branch placement would have put the refuse box at the same vertical position as the second main-path box, overlapping it. Fixed by having portrait stack the refuse note as its own strip beneath the entire main path instead of attempting a mid-flow side branch — documented as the honest simplification for a narrow frame.

`PolicyGrid` and `FactStack` both read clean on their first rendered still — no fixes needed.

**Audio:** Kokoro `af_bella`, one pass per cut. `generate_audio_kokoro.py` (confirmed the correct script name for this checkout — `generate_audio.py` doesn't exist here) exceeded the foreground shell's default timeout on the 15-beat 16:9 cut; re-run via `nohup … & disown` and polled to completion (finished in ~2.5 minutes). The 9:16 cut's 5-beat pass was run the same way proactively and finished in under a minute. `actual_duration_s` in each beat sheet is ground truth for everything downstream — the 16:9 cut ran long against its own word-count estimate on several of the denser explanatory beats (B02, B03, B08, B11).

**Rendering:** true 4K via `ART_SCALE` default (scale=2), Chrome launched from this session's own container with `--chrome-mode=chrome-for-testing`. Rendered one beat per `remotion_scenes.py --only <BID>` call — batches of 4+ have been killed (exit 137) on prior builds in this series — all 20 beats (15 + 5) rendered this way with no failures. 16:9 compiled at `--height 2160`; 9:16 at `--height 3840`, both run in the background (`nohup … & disown`, cwd verified via `readlink /proc/<pid>/cwd`, polled via `tail`/`ps aux`) so the concat+mux step wasn't cut off by the foreground command timeout.

**Final QC on compiled masters:** sampled actual frames from both *compiled* outputs — 9 timestamps across the 16:9 master (11s, 53s, 84s, 130s, 200s, 230s, 280s, 310s, 370s), 4 across the 9:16 master (7s, 28s, 44s, 55s) — not just the isolated component stills, to confirm transitions, conforming, and text-safe crops all read clean end to end, including the B14/B04 outro cards on both masters. No further defects found.

**Final specs:**

| Cut | Resolution | Duration | File size |
|---|---|---|---|
| 16:9 | 3840×2160 | 6:12 (372.45s) | 14.2 MB |
| 9:16 | 2160×3840 | 0:58 (58.06s) | 2.9 MB |

**Non-blocking observation carried from this build, not from the compile logs:** the two prior videos in this series (`hai-mycroft-gateway`, `how-kv-cache-works`) both logged their masters as "committed to the device folder" in their own process notes, but neither mp4 was actually found there when this build checked the connected folder — only their `beatsheet.md`/`script.md`/`process-notes.md`/`SCRIPT-*.md` docs were present. Not investigated further (out of scope for this build), but this build's own commit was verified by listing the destination folder's contents after the `device_commit_files` call returned, rather than trusting the call's success response alone.

**Delivered:** both masters sent to Simba, and committed alongside this build's three docs (plus `SCRIPT-mycroft-router.md`) into `youtube/09102026mycroft-router/` on the connected device — `hai-mycroft-router.mp4`, `hai-mycroft-router-916.mp4`.

## Open item — publishing not yet possible from this repo

Same open item logged on the other videos in this series: this toolkit checkout (`brutalist.art`) stops at render, and `./art final` / `./art post` / the `youtube-publisher` script aren't present here — see `RENDER-4K-AND-UPLOAD.md` and `docs/PUBLISHING.md` at the repo root. Dropping the two finished mp4s straight into the reel's `youtube/` folder is a reasonable interim landing spot but not the sanctioned `TOPOST` staging path. Google Drive link for this video is also still TBD — add it here once the files are staged there, same as the other videos' entries.
