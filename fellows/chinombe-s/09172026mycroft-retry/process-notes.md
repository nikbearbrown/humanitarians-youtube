# Process notes — One Retry, Never a Chain (both cuts)

**Status:** shipped-to-chat · committed to device folder · not yet staged to Drive · not yet published to YouTube
**Channel:** claude-hai · **Resolution:** 3840x2160 (16:9) / 2160x3840 (9:16)
**Last updated:** 2026-09-17
**Video Link:**https://drive.google.com/drive/folders/1OopER7YqxoKf_w_qwXM98Jh9C2Yxwm6l?usp=sharing

Build log for `hai-mycroft-retry` (16:9) and `hai-mycroft-retry-916` (9:16 Shorts). Chronological; append-only going forward — add dated entries, don't rewrite history.

## 2026-09-17 — script → both cuts built at true 4K

**Starting point:** the user pasted the Mycroft Sprint 4 report ("Handle Failures") and asked for a script, which was written and delivered as `SCRIPT-mycroft-retry.md` (14-beat ai-explainer script, labeled with the sprint from the header onward — the lesson learned on the Sprint 3 router script, applied proactively this time so no correction cycle was needed). The user then asked to run the pipeline for both videos — this build.

**GATE L:** the script's own preamble already did a script-stage GATE L assessment — every beat mapped to a shape already built and QC'd on `hai-mycroft-gateway`, `hai-mycroft-router`, `how-kv-cache-works`, or `hai-paged-attention`. Confirmed at build time by checking the actual component registrations in `Root.tsx` and each component's zod schema before writing props (`FactStack`, `RouterFlow`, `TestSuiteProof`, `DataTable`, `FindingPair`, plus the four house components). **Zero new Remotion components were authored** — the first build in this series where that's true; every prior build (router, PagedAttention) needed at least one new shape.

**9 beats reused existing components with new props:** `FactStack` twice (B02 validators.py, B10 the non-monotonic cost ladder), `RouterFlow` once (B03 gateway.py + adapter changes, merged into a single beat since both describe the same retry-once path), `TestSuiteProof` once (B04 the 96→146 test growth + the bench run), `DataTable` twice (B05 the final sweep, B09 escalation's real price), `FindingPair` three times (B06 the zero-failure headline + answer-key correction, B07 quote-check + vanished model, B08 token budget + double-counted log), plus the four always-reused house components (`ClaudeComposerAsk` ×2, `ClaudeStatement`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`).

**9:16 Shorts cut designed** per THE SHORTS LAW: single cycle, no revision pass — B00 (cold open, condensed) → B01 (the rule, stated) → B02 (the final-sweep numbers, `DataTable916`, same content as the long cut's B05 — the one real "wait, what" moment: 0% failure, 8% escalation across every deliberate trap) → B03 (verdict, condensed) → B04 (outro, points back to the long cut). The final-sweep numbers were chosen over the escalation-price table (B09) as the reused middle beat because the headline "zero failures including every trap" lands without the setup the cost-ladder finding needs — same reasoning applied on the router and PagedAttention Shorts cuts.

**Factual-accuracy self-check:** every figure placed on screen (24 fixtures, 24→26 requests/attempts, 8% escalation, 0% failure, $0.00250 total cost, p50 393ms/p95 734ms, 16/24 graded with 14 correct, sent-001/sent-004, 11%→8%, 1024→896, 27 vs 24, $0.000088/$0.000282/3.2×, 23% of spend, 20% cheaper/13× sticker/77 vs 2 tokens) was checked against the pasted Sprint 4 report before rendering — nothing invented, matching the discipline established on the Sprint 3 router build after the PolicyGrid fix.

**Audio:** Kokoro `af_bella`, one pass per cut, both run via `nohup … & disown` from the start. 16:9 (14 beats) finished in a little over 2 minutes; 9:16 (5 beats) in under a minute. `actual_duration_s` in each beat sheet is ground truth for everything downstream — no runtime target was set for this script (unlike the PagedAttention build's requested "4 minutes"), so the 5:31 length for the 16:9 cut is simply what the content took to narrate at Kokoro's pace; no padding or trimming was needed.

**Rendering:** true 4K via `ART_SCALE` default (scale=2), Chrome launched with `--chrome-mode=chrome-for-testing`. One beat per `remotion_scenes.py --only <BID>` call, all 19 beats (14 + 5) rendered with an explicit 5-minute timeout on every call (the lesson from the PagedAttention build, applied proactively from the first call rather than waiting to hit the timeout again) — no failures, no retries needed.

**Compiling:** both cuts compiled in the background (`nohup … & disown`), polled via `tail`/`ps aux` until each "wrote … .mp4" line appeared. 9:16 compiled at `--height 3840` and finished within the first couple of polls. 16:9 compiled at `--height 2160` and took close to 9 minutes end to end for the final concat+mux step (`-preset slow -crf 16`, 330.8s of true 4K footage) — the longest compile in this series so far, consistent with this being the longest cut built yet; several poll calls needed an explicit `timeout` above the Bash tool's 2-minute default to avoid the poll command itself timing out mid-wait.

**Final QC on compiled masters:** sampled actual frames from both *compiled* outputs — 14 timestamps across the 16:9 master (one per beat), 5 across the 9:16 master (one per beat) — read directly to check transitions, text-safe margins, and factual accuracy against the source report. No defects found on either cut. The `RouterFlow` omittedNote ("no second retry — the loop doesn't exist…") renders with a strikethrough, which is the component's intentional styling for an omitted-by-design note, not a bug — confirmed by comparing against the same field's use on the Sprint 3 router reel.

**Final specs:**

| Cut | Resolution | Duration | File size |
|---|---|---|---|
| 16:9 | 3840×2160 | 5:31 (330.8s) | 14.5 MB |
| 9:16 | 2160×3840 | 0:49 (49.3s) | 2.8 MB |

**Non-blocking lint carried from the compile logs (flagged, not treated as blocking):**
- 16:9: "illustrate" motion carries 8/14 beats (57%), over the ~40% pantry-cap guideline in `MOTION.md` — this report has a structure/results/problems/findings-heavy middle section that leans on illustrated diagrams and fact stacks, same pattern already flagged and accepted on every prior reel in this series.
- 9:16: SKIN LINT on B00/B04 — `ClaudeComposerAsk916` / `ClaudeTitleOutro916` flagged against COLD OPEN LAW / OUTRO LAW, the same false positive already noted on every other video in this series (the linter doesn't account for the `916` responsive-variant naming convention).

**Delivered:** both masters sent to Simba, and committed alongside this build's three docs (plus `SCRIPT-mycroft-retry.md`) into `youtube/09172026mycroft-retry/` on the connected device — `hai-mycroft-retry.mp4`, `hai-mycroft-retry-916.mp4`.

## Open item — publishing not yet possible from this repo

Same open item logged on every other video in this series: this toolkit checkout (`brutalist.art`) stops at render, and `./art final` / `./art post` / the `youtube-publisher` script aren't present here — see `RENDER-4K-AND-UPLOAD.md` and `docs/PUBLISHING.md` at the repo root. Dropping the two finished mp4s straight into the reel's `youtube/` folder is a reasonable interim landing spot but not the sanctioned `TOPOST` staging path. Google Drive link for this video is also still TBD — add it here once the files are staged there, same as the other videos' entries.
