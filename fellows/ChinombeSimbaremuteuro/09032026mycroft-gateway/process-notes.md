# Process notes — One Door In (both cuts)

**Google Drive:** (https://drive.google.com/drive/folders/1pHXg01GKXl1-iEPKqCr3O4BUJwsPSCBk?usp=sharing)
**Status:** shipped-to-chat · not yet staged to Drive · not yet published to YouTube
**Channel:** claude-hai · **Resolution:** 3840x2160 (16:9) / 2160x3840 (9:16)
**Last updated:** 2026-09-02

Build log for `hai-mycroft-gateway` (16:9) and `hai-mycroft-gateway-916` (9:16 Shorts). Chronological; append-only going forward — add dated entries, don't rewrite history.

## 2026-09-02 — script → both cuts built at true 4K

**Starting point:** `SCRIPT-mycroft-gateway.md` (16-beat ai-explainer script, written in a prior pass from the Mycroft Sprint 2 report) plus pre-production `beatsheet.md` / `process-notes.md` stubs were the only artifacts in `youtube/hai-mycroft-gateway/`. This session built both final videos from the script.

**GATE L:** searched the existing Remotion component library (`runtime/remotion/src/scenes/`, ~300+ files) before authoring anything new. Every candidate hit was hard-coded to another reel's specific content (other topics' cost tables, other films' diagrams) — confirmed genuine punts for B02–B12, except that three of those beats (a build-manifest table, a price table, a live-call ledger) are shaped identically enough that one generic table component covers all three rather than three near-duplicates.

**8 new Remotion components authored** (in `runtime/remotion/src/scenes/`, registered in `Root.tsx`, each portrait/landscape-responsive off one motion-math source — though only `DataTable` needed a 9:16 variant, since the Shorts cut reuses just that one beat):
- `DataTable` / `DataTable916` — generic N-column table with optional stat-chip strip and capstone footnote; reused for the build manifest (B04), the tier price table (B07), and the live-call ledger (B09, and Shorts B02)
- `GatewayDoor` — one labeled door (`GatewayClient.call()`) wrapping two inputs, both outcome cards showing a row gets written on success and on failure (B02)
- `LayerStack` — N labeled layer cards with does/does-not lines; a layer can be marked not-yet-built (dashed border) (B03)
- `TestSuiteProof` — stat-chip strip → numbered rules → capstone card (B05)
- `EvidenceTrail` — one highlighted evidenced item against a muted "others" list (B06)
- `BreakEvenThresholds` — big threshold-number cards side by side, plus a muted old-setup note (B08)
- `FindingPair` — two full-width finding cards with a stat badge each, reused across both findings beats (B10, B11)
- `ConvergenceRisk` — N labeled nodes converging into one risk box (B12)

Writing one generic `DataTable` for three beats instead of three near-identical table components is a deliberate reading of GATE L's anti-duplication spirit: it's still a genuine new component (nothing in the existing library fit this reel's content), just designed to not triplicate itself.

**9:16 Shorts cut designed** per THE SHORTS LAW: single cycle, no revision pass — B00 (cold open, condensed) → B01 (the rule, stated) → B02 (the one live-call table, reusing the exact tested `DataTable916` props from the long cut's B09) → B03 (verdict, condensed) → B04 (outro, points back to the long cut).

**Audio:** Kokoro `af_bella`, one pass per cut, generated straight into true-4K rendering. `actual_duration_s` in each beat sheet is ground truth for everything downstream — the 16:9 cut ran long against its own word-count estimate (5:58 measured vs. ~4:47 estimated), consistent with how much this script leans on multi-clause technical sentences.

**Rendering:** true 4K via `ART_SCALE` default (scale=2). Chrome launched from this session's own container (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`) with `--chrome-mode=chrome-for-testing`. Rendered one beat per `remotion_scenes.py --only <BID>` call rather than the full batch — a batch of 4+ beats reliably got killed partway through in this session (exit 137), while single-beat calls completed cleanly every time; all 21 beats (16 + 5) rendered this way with no failures. 16:9 compiled at `--height 2160`; 9:16 at `--height 3840`. The final concat+mux step for the 16:9 master also ran past the foreground command timeout on the first attempt (killed mid-write, left a truncated mp4 with no moov atom) — resolved by re-running `compile.py` in the background (`nohup … &`) and polling, which let the `slow`/`crf16` encode finish without being cut off.

**QC pass — 2 real defects caught and fixed before the full build, not after** (VISUAL QC LAW: judged from rendered stills actually read, not from code review alone):

1. **`LayerStack` overflow/overlap.** First QC still showed the sparkline text visually sitting inside the third ("Router") card — three cards at the original card height + gap + top offset summed to more vertical space than the frame had before the sparkline's fixed bottom position. Fixed by reducing `listTop` (0.18→0.16 landscape / 0.15→0.14 portrait), `cardH` (0.24→0.19), and `gap` (0.03→0.025). Re-rendered still confirmed clean clearance.

2. **`DataTable` portrait under-fill.** First portrait QC still (3 rows + footnote) showed only the top ~50% of the 1920px-tall frame filled, with a large empty gap below down to the sparkline. Root cause: portrait was using the same fixed row height as landscape, proportionally far too small for a 3840-tall canvas with only 1–3 rows. Fixed with an adaptive portrait row-height formula that scales rows to fill up to 62% of frame height, clamped to a legible range (landscape kept its fixed row height, since it already read clean). Re-rendered still confirmed the table now fills roughly two-thirds of the frame, comparable to the accepted precedent from the Logbook reel's `ResultsTable916`.

Both fixes shipped before any beat was rendered into a cut, unlike the equivalent defects on the Logbook reel, which were caught only after a full render pass.

**Final QC on compiled masters:** sampled actual frames from both *compiled* outputs — 10 timestamps across the 16:9 master, 5 across the 9:16 master — not just the isolated component stills, to confirm transitions, conforming, and text-safe crops all read clean end to end. No further defects found.

**Final specs:**

| Cut | Resolution | Duration | File size |
|---|---|---|---|
| 16:9 | 3840×2160 | 5:58 (357.8s) | 14.7 MB |
| 9:16 | 2160×3840 | 0:56 (56.1s) | 2.7 MB |

**Non-blocking lint carried from the compile logs (flagged, not treated as blocking):**
- 16:9: "illustrate" motion carries 9/16 beats (56%), over the ~40% pantry-cap guideline in `MOTION.md` — this script leans heavily on illustrated middle beats (STRUCTURE/PROOF/REASONING/FINDINGS/RISK all use it). Worth a look if this reel gets a revision pass.
- 9:16: SKIN LINT on B00/B04 — `ClaudeComposerAsk916` / `ClaudeTitleOutro916` flagged against COLD OPEN LAW / OUTRO LAW, same false-positive pattern already noted on the other two videos in this series (the linter doesn't account for the `916` responsive-variant naming convention).

**Delivered:** both masters sent to Simba and committed into `youtube/hai-mycroft-gateway/` on the connected device (`hai-mycroft-gateway.mp4`, `hai-mycroft-gateway-916.mp4`).

## Open item — publishing not yet possible from this repo

Same open item logged on the other two videos in this series: this toolkit checkout (`brutalist.art`) stops at render, and `./art final` / `./art post` / the `youtube-publisher` script aren't present here — see `RENDER-4K-AND-UPLOAD.md` and `docs/PUBLISHING.md` at the repo root. Dropping the two finished mp4s straight into the reel's `youtube/` folder is a reasonable interim landing spot but not the sanctioned `TOPOST` staging path. Google Drive link for this video is also still TBD — add it here once the files are staged there, same as the other two videos' entries.
