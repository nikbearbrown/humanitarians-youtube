# Frictional log — Embedding Model Staleness: The Index That Quietly Split in Two

*Written contemporaneously, as the build happens — not reconstructed after the fact.*

## 2026-11-19 — Start, mycroft read, and template study

Read both reference STEM reels in full as the structural template —
`2026-11-13-context-window-limits/` (most recent, mirrored most closely: `README.md`,
`BEAT-SHEET.md`, `BUILD-LOG.md`, `FRICTIONAL.md`, `FACTCHECK.md`, `SOURCES.md`, `SHOTLIST.md`,
`PROMPTS.md`, `scenes.py` + `vertical/scenes.py`, `beat_sheet.json`) and
`2026-11-04-goodharts-law-proxy-metrics/` (second reference, same format) — plus the toolkit's
`CLAUDE.md`, `art`, `runtime/scripts/run.sh`, `runtime/scripts/compile.py --help`,
`runtime/scripts/generate_audio_kokoro.py --help`, `runtime/scripts/shorts.py --help`, and
`runtime/qc/final_frame_check.py`'s header directly, to confirm exactly how `./art run` /
`./art final` / `./art vertical` work end to end before writing anything. Confirmed `./art final`
defaults to `--height 2160` (landscape 4K) and that the documented vertical final needs
`--height 3840` explicitly (matches both reference BUILD-LOGs). Confirmed the portrait
`config.frame_width` patch (toolkit bug #7 in the brief) is a per-project hand-copied snippet in
`vertical/scenes.py`'s own header, not centralized in the toolkit anywhere — will copy it verbatim
and verify it's actually present (not just commented) before any vertical render.

**Read the real `rag.py` directly, per the hard requirement not to take the brief's summary as
gospel:** `/Users/pranavijs/mycroft/scripts/mycroft-main/Core_Components/Regulatory_QA/backend/app/rag.py`.
Confirmed line-by-line: `RegulatoryRAG.__init__` builds `HuggingFaceEmbeddings(model_name=settings.embedding_model, ...)`
(not a literal string in `rag.py` itself — it reads from `app/config.py`'s `Settings`, confirmed
separately that `embedding_model: str = "all-MiniLM-L6-v2"` is that setting's actual default value,
so the brief's claim is accurate once traced to its real source). Confirmed
`build_vectorstore()` calls `Chroma.from_documents(documents=documents, embedding=self.embeddings,
collection_name="regulatory_feeds", persist_directory=None)` — a brand-new in-memory Chroma store
every single call, no persistence. Confirmed this is actually invoked on every chat request, not
just at startup or on demand some other way: `routers/chat.py`'s `POST /api/chat` handler calls
`rag.build_vectorstore(feeds)` directly inline, immediately before `rag.query(...)`, on every
request. So the brief's side-note is accurate: this design sidesteps the entire embedding-staleness
class of bug by construction (no persisted index ever exists to go stale), at the cost of
re-embedding the full feed set from scratch on every single request. This is reported in the video
strictly as an honest illustrative side-note about a design choice, never as "mycroft has this
bug" (it doesn't, and this was independently confirmed by reading the source, not assumed from the
prompt).

## 2026-11-19 — Real embedding-staleness demo (verification/)

Checked local environment for real embedding models before deciding what evidence was honestly
achievable. Confirmed internet access works (`urllib.request.urlopen('https://huggingface.co')`
succeeded) AND two real, different, already-locally-cached HuggingFace sentence-transformer
checkpoints exist: `sentence-transformers/all-MiniLM-L6-v2` (the exact model mycroft's own
`rag.py` defaults to) and `sentence-transformers/multi-qa-MiniLM-L6-cos-v1` (a different real,
published checkpoint — same MiniLM-family architecture and output dimensionality, 384, but a
different training objective: QA-pair retrieval tuned for cosine similarity, vs. all-MiniLM-L6-v2's
general-purpose sentence-similarity training). Chose these two deliberately: genuinely different
trained models (not two runs of the same model, which would only show float noise), real and
inspectable, no fabrication needed.

`sentence_transformers`, `scikit-learn`, `torch`, and `transformers` were NOT installed in this
environment — installed via `pip3 install sentence-transformers scikit-learn` (pulled in
`torch`/`transformers`/`huggingface-hub` as dependencies). Wrote `embedding_staleness_demo.py`
using plain `transformers` `AutoTokenizer`/`AutoModel` (mean-pooling + L2-normalization applied by
hand in the script, not the `sentence-transformers` wrapper) specifically so the exact pooling math
is visible and auditable in the file itself, not hidden inside a library call.

**Real bug, hit and fixed immediately:** first run failed with `401 Unauthorized` /
`RepositoryNotFoundError` from `huggingface_hub` while trying to load the (already locally cached)
tokenizer — root cause: a newer `huggingface_hub`/`transformers` version (pulled in by the fresh
pip install) tries a network call to list repo file templates even for an already-cached model, and
this account's saved HF token is expired, so that incidental network call 401'd and `transformers`
treated the whole load as a failure instead of falling back to the local cache. Fixed by setting
`HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1` in the environment for every run of this script, which
forces local-cache-only loading and skips the network call entirely — both models loaded
instantly from `~/.cache/huggingface/hub/` with no further issue. Logged here since this is exactly
the kind of silent-until-you-look dependency friction the house style wants documented honestly,
not smoothed over.

**First full run produced real, honest, but incomplete evidence:** on a 10-sentence corpus spanning
10 unrelated topics (finance, retail, hiking, biology, HR, baking, software, health, privacy,
astronomy), 3 held-out queries, same-model (clean) vs. stale/mixed (cross-model) retrieval all
correctly found the right document at rank #1 in BOTH conditions (3/3 both ways) — the topics were
distinct enough that even a measurable, real degradation in cosine similarity for stale documents
(commonly 0.08-0.14 absolute, e.g. one query's correct document scored 0.6839 clean vs. 0.5897
stale) was not enough to overtake a wrong answer sitting far below both scores. This is an honest,
real result, not a defect in the demo — but it undersells the actual video claim (degraded or WRONG
results), so rather than present only the score-drop evidence, searched for a second, closer
scenario.

**Explored for a genuine rank-inversion case** (kept this search in throwaway scripts, deleted after
finding and folding a result into the final file — the numbers below are from the kept, final
script's own run, reproducible by anyone who runs it): tried several near-duplicate document pairs
and query phrasings. Most attempts (damaged-item-refund vs. support-replacement; backup-before-
migration vs. retention-policy; exercise vs. diet) had clean-index margins (0.18-0.50) too wide for
the measured ~0.07-0.14 cross-model degradation to close. Found one pair close enough: a
"cash refund" sentence (CORRECT answer) and a "store credit only" sentence (DISTRACTOR), under the
query "Can I get cash back for a return, or only credit?" — clean margin only +0.0231 (CORRECT
0.6090 vs DISTRACTOR 0.5859). Making the CORRECT document stale (stuck in Model-A space, simulating
it being indexed before a model switch and never re-embedded) dropped its score to 0.5109 — now
BELOW the unchanged, fresh-Model-B distractor's 0.5859 — a genuine, reproducible top-1 rank
inversion: the right document wins when both are embedded by the same (current) model, and loses
to a wrong document once it's stuck in stale geometry, with no error or warning anywhere in the
process. This is real, run, and kept in `verification/embedding_staleness_demo.py` (Part 4) exactly
as found — not hand-tuned further once the flip was confirmed.

**Final demo file structure** (`verification/embedding_staleness_demo.py`, output captured verbatim
in `verification/demo_output.txt` from one real run): Part 1 (cross-model cosine similarity of the
IDENTICAL sentence embedded by both models — real mean 0.7416, far from 1.0, showing the two
models don't even agree with themselves across the model boundary), Part 2 (aggregate same-model
vs. cross-model similarity distributions over 100 doc pairs — real, independently measured), Part 3
(the realistic partial-migration retrieval scenario on the wide-topic 10-doc corpus — reported
honestly including where ranking survived despite real score degradation), Part 4 (the found
rank-inversion case — a genuine wrong top-1 result caused purely by one document's vector being
stuck in a stale embedding space). Every number in all 4 parts is from one real, reproducible
script run; none are hypothetical or hand-typed.

Next: write the beat sheet / FACTCHECK / SOURCES docs, generate Kokoro narration, measure real
durations, then author `scenes.py` against those measured durations.

## 2026-11-19 — Beat sheet (10 beats, not 9), audio, scenes.py

Designed the beat sheet with 10 beats, one more than both reference reels (9), to give the
mycroft real-world note (B06) its own dedicated beat with real narration and a verbatim code
quote, rather than compressing it into one sentence inside another beat the way CWL's companion
tie-in was handled — justified because this build's brief explicitly asked for the real project to
be named directly (unlike CWL's house rule of keeping a real-world tie-in fully generic). Act
structure: TITLE / EXEC-SUMMARY / HOOK / FRAMEWORK / WORKED-EXAMPLE / FALSIFIABILITY /
REAL-WORLD-NOTE / SCAFFOLDED-TASK / TAKEAWAY / SIGN-OFF. Rubric devised fresh, no wording reused
from any prior reel's rubric: **"Check the Checkpoint / Audit the Whole Index / Watch for
Silence."**

Wrote `BEAT-SHEET.md`, `FACTCHECK.md`, `SOURCES.md` first (durations left TBD pending measured
audio, per the audio-first rule). Built the real silent B00 track by hand
(`ffmpeg -f lavfi -i anullsrc=r=48000:cl=stereo -t 4.1`), measured via `ffprobe` at 4.128s — same
mp3 frame-boundary rounding both reference reels' B00 also measured.

Ran `generate_audio_kokoro.py --only B01...B09` (`af_bella`) as a background command (it ran ~3
minutes, longer than the 2-minute foreground timeout, so it was moved to background automatically
and polled via `ps`/directory listing rather than re-run) — completed cleanly, no retries needed:
B01=17.78 B02=24.67 B03=29.23 B04=32.47 B05=23.11 B06=32.02 B07=24.22 B08=13.1 B09=1.51. Confirmed
`generate_audio_kokoro.py` had, as documented by the CWL build, already written B00's
`actual_duration_s` to its `estimated_duration_s` fallback (4.0) even though B00 is silence-skipped
— this time caught it immediately via direct `grep -c '"actual_duration_s"'` (exactly 10 matches,
one per beat, confirmed no duplicate key existed yet) before hand-editing, then used `Edit`'s
exact-match requirement against the CURRENT post-generation file content (re-`Read` first, per the
lesson CWL's `FRICTIONAL.md` logged) to replace the `4.0` with the real measured `4.128` and add
`"audio_file": "mp3/beat-B00.mp3"` in the same edit — avoiding the exact duplicate-JSON-key bug CWL
hit, by replacing the existing key instead of inserting a second one. Verified immediately after:
still exactly 10 `actual_duration_s` occurrences, no duplicates. Total measured runtime:
4.128+17.78+24.67+29.23+32.47+23.11+32.02+24.22+13.1+1.51 = 202.238s.

Wrote `scenes.py` with the established `T()`/`PALETTE`/`fit()`/`panel()`/`box_around()`/
`stat_row()`/`metric_panel()` helpers copied verbatim from the CWL reel, hand-summed every beat's
`self.play`/`self.wait` durations to match each measured `actual_duration_s`. B06's on-screen code
quotes (`model_name=settings.embedding_model`, `embedding_model: str = "all-MiniLM-L6-v2"`,
`persist_directory=None`) were copied character-for-character from the real, already-read
`rag.py`/`config.py` source — double-checked against `FACTCHECK.md`'s own verbatim accuracy check
section before finalizing, not retyped from memory.

Next: `./art run` for the landscape pass, fix any GATE A/B findings, then build the vertical
companion.

## 2026-11-19 — Landscape previz: GATE F, GATE A, GATE B findings, all real and fixed

First `./art run --height 480` attempt failed immediately at **GATE F**: no `SHOTLIST.md`/
`PROMPTS.md` yet (paperwork-set requirement, confirmed from the brief's own documented toolkit
bug #3 — `ART_FACTS=0` only grants a previz-only exception, it does not waive GATE F's file-
existence check). Wrote both files, matching the established pattern of "no pantry assets needed —
all Manim" placeholders from the reference reels, then re-ran.

**Real GATE A static-check failure, not a false positive:** `B06_MycroftRealWorldNote` failed with
"shapes never change — 1 distinct shape-state across 13 frames." Traced the root cause directly in
`runtime/qc/static_scene_check.py`'s `_snapshot()`: it only tracks NON-text shapes per steady
state, and B06's only non-text shape was one `RoundedRectangle` panel created once and never joined
by another shape for the rest of the beat (every other on-screen element was `T()` text) — exactly
the same false-trigger CLASS the file's own B03 docstring already documents from CWL's build
(headline-text-only cards), but this is a genuinely different instance of it, caught correctly by
the checker. Fixed by adding a real top rule line (matching B04/B05's framing idiom) and a real
`box_around()` highlight rectangle around each of the 3 quoted code lines as they're revealed —
confirmed via a direct, scoped re-run of `static_scene_check.py --class B06_MycroftRealWorldNote`
before re-running the whole pipeline (6 distinct states now, clean) rather than re-running the full
10-beat pipeline just to find out.

**Second real GATE B failure, found on the full re-run:** `manim_layout_audit.py` flagged
`B06_MycroftRealWorldNote`'s closing line ("Trade-off: full re-embed cost, on every single
request.") as outside the safe area at t≈14.93s, box y from -3.5 to -3.25 against the ±3.4 safe
half-height. Root cause, found by re-reading my own just-written code rather than guessing: I had
set BOTH `closing.to_edge(DOWN, buff=0.5)` AND `bottom_rule.to_edge(DOWN, buff=0.5)` to the exact
same buff, so the two mobjects landed at the same y-position (overlapping, with the taller text
block extending past the rule's own safe placement) instead of the established pattern elsewhere
in this file (B04/B05 use two DIFFERENT buffs, text at 0.65-0.68 sitting above a rule at 0.5, so the
rule — not the text — sits closest to the hard edge). Fixed by changing `closing`'s buff to 0.68,
matching B04/B05's convention, re-ran `./art run` for the remaining pending beats (B06-B09, since
B00-B05 were already slotted from the first successful pass) — GATE A/B clean on all 4, 10/10
beats slotted on this pass.

**Review-slate GATE V, matching the documented burn-in false-positive pattern exactly:** the
review slate's embedded GATE V reported **20 BLOCKER / 0 MAJOR** for this 10-beat reel — exactly 2
per beat, the documented burn-in global-timecode-overlay signature from the brief's own toolkit-bug
list (item 4), not a real defect. Per the documented workaround, this was NOT trusted at face
value; proceeding to build the TRUE final candidate (`./art final`, no `--review`) next and
independently re-verifying with `final_frame_check.py --lenient` before accepting anything as
clean.

## 2026-11-19 — Landscape final master, verified independently and by real frame extraction

Built the TRUE final landscape master directly via `compile.py --out deliverables/landscape --height
2160` (no `--review`): succeeded on the first attempt, wrote a `.verified.json` with `"status":
"ready"`, meaning `compile.py`'s own embedded GATE V step (no `--lenient`) found nothing blocking.
Re-ran `final_frame_check.py --lenient` directly against the written candidate as an independent
confirmation (never trusting the embedded step's silent success alone): **0 BLOCKER, 0 MAJOR.**
`ffprobe`: 3840x2160, 24fps, h264/aac, 202.5s. Renamed `<slug>.mp4`/`.verified.json` to
`EmbeddingModelStaleness_SaiPranaviJ.mp4`/`.verified.json` per `FELLOWS-SUBMISSION.md`'s manual
naming convention.

**A real visual defect caught only by extracting and looking at real frames, NOT by any automated
gate:** B06's two small file-label captions ("rag.py", "config.py" above each quoted code line)
were rendered in `PALETTE["slate"]` on an ink background — a combination this very file's own
`PALETTE` dict comment already documents as broken contrast (0.04 luminance separation), but which
GATE V's whole-panel contrast sampling did not trip on (the labels are too small a fraction of the
sampled region to pull the panel's aggregate contrast reading below the MAJOR threshold). Caught by
extracting and personally inspecting a real frame at B06's steady state, per the house rule to
verify renders by looking at frames, not by the mp4 probe or automated gates alone. Fixed in both
`scenes.py` and `vertical/scenes.py` by switching the label color to `PALETTE["sage"]` — the exact
substitute the palette's own comment already names for note/tag text on an ink background. Re-
rendered only `B06_MycroftRealWorldNote` directly via `manim -qk --fps 24 -r 3840,2160` (bypassing
`run.sh` entirely, specifically to avoid the documented shared-`clips/`-cache-reverts-to-preview-
resolution side effect that a `./art run --height <preview>` call would trigger on every other
beat's already-true-4K cached clip) — confirmed clean via a scoped `manim_layout_audit.py --class
B06_MycroftRealWorldNote --png --curve-strict` run before touching the final master at all. Moved
the new render into `manim/B06.mp4`, confirmed via `ffprobe` it was true 3840x2160, then re-ran
`compile.py --out deliverables/landscape --height 2160` directly (never `./art run`) to rebuild the
final master from the corrected clip. Re-verified: still 0 BLOCKER/0 MAJOR, still 202.5s, and a
freshly re-extracted frame at B06 now shows both file labels clearly legible.

Extracted and personally inspected real frames at B02 (overlay phase), B04 (steady state), and B06
(both before and after the label-color fix) — all clean: panels fully legible, tags sit clear of
their panels with no overlap, no off-frame/off-safe-area content, no Pango small-font-size
word-gap artifacts anywhere (every on-screen string went through `T()`), and B06's verbatim code
quotes read correctly against the real `rag.py`/`config.py` source.

**Landscape final confirmed:** `deliverables/landscape/EmbeddingModelStaleness_SaiPranaviJ.mp4` —
3840x2160, 24fps, h264/aac, 202.5s. GATE V: 0 BLOCKER, 0 MAJOR (verified directly against the true
final candidate, not a review slate).

Next: hand-author `vertical/scenes.py` (done in parallel while the landscape final was building),
then render/QC the vertical companion.

## 2026-11-19 — Vertical scaffold and hand-authored portrait scenes

Ran `./art vertical <reel> --no-endcard --handle "@HumanitariansAI"` (both flags explicit, matching
the documented contract from the brief/CWL's build): confirmed it copies the parent's 10 mp3s and
beat-sheet metadata (`aspect_ratio: "9:16"`) into `vertical/`, correctly reports every beat as
`GENERATED — no cut; needs a portrait scene` (never silently center-crops), and did NOT add a
silent endcard. Confirmed `config.pixel_height > config.pixel_width` -> `config.frame_width` patch
(toolkit bug #7 in the brief) is ACTUALLY present and active in the written `vertical/scenes.py`
(not just a comment) by direct `grep`/read before relying on it, per the brief's explicit warning
that this exact bug was previously documented-but-never-coded in a prior week.

Hand-authored `vertical/scenes.py`: same `T()`/`PALETTE`/`fit()`/`panel()`/`box_around()` helpers
copied verbatim, `stat_row()`/`metric_panel()` redesigned to stack label-over-value (the narrow
~4.5-unit portrait frame can't fit a long label and a value on one line), every structure beat's
trailing tags built stacked DOWN from the start. Every `self.play`/`self.wait` duration hand-matched
to `../scenes.py` beat-for-beat.

**Real GATE A static-check false positive on B04 (not every beat, by construction):**
`static_scene_check.py --class B04_SilentSplit` reported "1 explicit coord(s) outside the frame,
e.g. (0.0,-5.7) in move_to." Grepped `vertical/scenes.py` for any literal `move_to([...])` call and
found NONE anywhere in the file — every `move_to()` call takes a dynamic `.get_center()` or
`ORIGIN` — confirming this is the exact documented stub-vs-real-Manim-portrait-geometry divergence
class of false positive from the brief's toolkit-bug list, not a real defect. Independently verified
via the real pixel-true `manim_layout_audit.py --portrait`, run against a scratch copy of the file
(`/tmp/ems_vertical_scratch/`, never the reel's own `vertical/media/` tree, per the documented
stale-cache-contamination lesson) for EVERY one of the 10 beats, not just B04: B04 came back CLEAN.

**A real GATE B warning, found and fixed BEFORE any full render — not a stub false positive this
time:** `B06_MycroftRealWorldNote` came back with 1 real warning: "label on a curve/line" near one
of the quoted code rows. Rather than assume it was another stub artifact, rendered the beat for
real at true 2160x3840 and extracted frames to look — a frame at t≈3.3s appeared to show the
two-line file-path caption overlapping the code-quote panel, but a static debug scene built from the
exact same positioning code (no animation, final layout only) showed ZERO overlap, proving the
apparent overlap was a mid-transition artifact from an arbitrarily-chosen extraction timestamp (the
same caution CWL's own BUILD-LOG logged for an unrelated beat), not a layout bug. Traced the REAL
warning to its actual root cause instead: debugged the exact rendered y-coordinates via a small
standalone Python probe script and found the true issue was between code ROWS, not between the
caption and the panel — `code_rows` used `arrange(DOWN, buff=0.18)` while each row's
`box_around()` highlight rectangle used `buff=0.16`, leaving only ~0.02 units of real clearance
between one row's highlight box and the next row's text (the landscape file avoids this because its
analogous spacing is `buff=0.35` row gap vs. `buff=0.1` box buff — a comfortable 0.25 clearance —
and this portrait file's tighter layout had silently copied the box buff without re-checking the
row gap against it). Fixed by widening `code_rows`' inter-row buff to 0.4 — confirmed via a direct,
scoped re-run of `manim_layout_audit.py --portrait --class B06_MycroftRealWorldNote` (0 errors, 0
warnings) BEFORE re-checking the other 9 beats, then re-ran the real portrait auditor against all
10 beats again: all 10 CLEAN, 0 errors, 0 warnings. Lesson logged: when copying a `buff`/`box_around`
pairing from one file into a visually denser redesign, re-derive the clearance arithmetic (gap
buff must exceed 2x the box buff) rather than copying either value in isolation.

## 2026-11-19 — A real GATE V underfill/edge-bleed cycle on the first true vertical candidate

`compile.py --out deliverables/vertical --height 3840` REFUSED on the first attempt with a genuine
(not burn-in false-positive) GATE V failure: 0 BLOCKER... actually 2 BLOCKER, 4 MAJOR — B02
`underfill` (48%, min 55%, both sampled timestamps), B08 `edge-bleed` (BLOCKER, both sampled
timestamps), B09 `underfill` (47%, both sampled timestamps). No `--review` label was present on
this candidate path, confirming these were real, not the documented burn-in artifact.

Root-caused each independently before touching any code:
- **B08 edge-bleed:** `frame = panel(width=content.width + 0.8, ...)` was uncapped. Since
  `content.width` can reach `MAX_W` (3.4) once `fit()` has scaled each line, the frame could reach
  4.2 units wide — exceeding the portrait safe full-width (~3.9, half-width 1.95) — so the card's
  own gold border sat outside the title-safe area. Fixed by capping `frame_w = min(content.width +
  0.8, 3.7)`, the same defensive pattern already used in this file's own B09.
- **B02 underfill:** the hook's closing overlay (qmark + 2 lines of text + 2 rules) was sized and
  spaced for a much shorter vertical footprint than the tall 9:16 frame actually has. Fixed with
  genuine added content mass — a larger qmark (110→150), larger overlay text, wider rules (closer
  to the safe edge), and more real spacing between the real elements (buff 0.7→1.1) — never a
  padding rectangle.
- **B09 underfill:** the sign-off card's handle/caption text and inter-group spacing were sized
  too small for the tall frame. Fixed the same way — larger real text (handle 48→60,
  captions 28/24→34/28) and more real spacing between the 4 real content groups (buff 0.5→0.75).

**The B08 fix round-tripped once, found and fixed in a single extra cycle, not discovered only
after a full re-render:** rather than re-run the whole `compile.py` pipeline to check, re-rendered
just the 3 touched beats directly via `manim` into a scratch folder, extracted one frame each, and
ran `final_frame_check.py --frames-dir <dir> --lenient` (the tool's own documented direct-PNG test
mode) against just those 3 frames. B02 and B09 came back clean, but B08 came back with a NEW
`underfill` MAJOR at 53% (just under the 55% floor) — the width cap that fixed the edge-bleed BLOCKER
had, as a side effect, reduced the card's overall footprint below the fill floor. Fixed by recovering
the lost fill with genuine added content mass within the now-capped width — larger real text
(24/27→27/30) and more real spacing between the two real text blocks (buff 0.22/0.24/0.7→
0.3/0.32/1.0) — rather than widening the frame back out, which would have re-triggered the
edge-bleed BLOCKER. Re-ran the same 3-frame direct-PNG check: **0 BLOCKER, 0 MAJOR**, confirmed by
eye on all 3 extracted frames before touching the full pipeline again.

Re-ran the real `./art final`-equivalent (`compile.py --out deliverables/vertical --height 3840`)
directly, letting it recompile `clips/` and re-render all 10 beats (since 3 scene files changed)
before its own embedded (always-strict) GATE V check runs.

## 2026-11-19 — A real duration mismatch between the two masters, and a real empty-Text bounding-
## box bug, both found only by looking past the green checkmarks

The second true vertical candidate passed `compile.py`'s own embedded GATE V (`"status": "ready"`)
and this build's own `final_frame_check.py --lenient` re-check (0 BLOCKER/0 MAJOR) — but the hard
constraint requires landscape and vertical DURATIONS to match, not just both pass GATE V
independently, so this was checked explicitly rather than assumed from two green gate results.
`ffprobe` showed landscape at 202.500000s and vertical at 202.458333s — a real, if tiny (1 frame),
mismatch. Root-caused by `ffprobe`-measuring every beat's raw `manim/B0N.mp4` clip length in both
aspect folders side by side: every beat matched except B06, where landscape's raw clip measured
32.041667s and vertical's measured only 31.291667s (0.75s short). Traced to the actual
`self.wait()` values in each file's B06 `construct()`: the vertical file used `self.wait(1.3)`
twice where the landscape file (and this beat's own design intent — every beat's timing is
supposed to match beat-for-beat across aspects) used `self.wait(1.7)` — a real, un-noticed 0.8s
authoring drift from early in this build, silently absorbed by `compile.py`'s own retime-to-exact-
duration step (a ~2.4% speed-up via `setpts`, since the shortfall was within its ±5% silent-retime
ladder) rather than erroring or padding visibly. Fixed by restoring `1.7` in both places, confirmed
via a fresh `ffprobe` that the corrected raw clip (32.041667s) now matches landscape's exactly.

While re-rendering B06 to confirm the duration fix, extracted and looked at an actual frame (not
just trusted the by-then-already-clean GATE V/layout-audit results) and found a second real,
separate visual defect: the two teal highlight boxes around the first two quoted code statements
visibly overlapped each other. This was surprising since both `manim_layout_audit.py --portrait`
and the manual `final_frame_check.py --frames-dir` checks had already passed clean on this exact
beat earlier in the build — the earlier checks were run against a DIFFERENT version of the file
(before the "widen the inter-row buff to 0.4" fix had been further revised; a fresh numeric
coordinate probe, not just eyeballing the frame, was needed to find the actual cause). The real
root cause, found by printing exact `get_top()`/`get_bottom()` coordinates for every mobject
involved: `code_row("", "settings.embedding_model", ...)` and the other continuation lines passed
an EMPTY-STRING label (`file_label=""`) to `T("", ...)`, i.e. a `Text("")` mobject. Manim's
`Text("")` has no points at all, so it never gets positioned by `arrange()` the way a normal
mobject does — it stays at its creation point near the origin — yet `VGroup.height`/`get_top()`/
`get_bottom()` still fold that degenerate, effectively origin-anchored bounding box into the
group's overall extent. This silently inflated `box_around()`'s computed box height for the first
statement far beyond its actual visible text, enough to visually crowd into the next statement's
own highlight box. This is a genuinely different root cause from the earlier "arrange buff vs.
box_around buff" clearance bug fixed previously in this same beat — that one was a real but
different geometry mistake; this one is a Manim empty-Text-mobject quirk, caught only by printing
raw coordinates, not by any gate or by eye alone (the earlier frame that looked "fine" actually
had the SAME underlying bug already, just at the specific extraction timestamp where it happened
to be less visually obvious than the later one). Fixed by rewriting the per-statement builder
(`stmt_block()`) to take one real label plus a LIST of real code lines, so no empty-string `Text()`
is ever created anywhere in this file. Re-verified via the real portrait auditor (0 errors, 0
warnings) and a fresh extracted frame (three cleanly separated, non-overlapping highlight boxes)
before re-slotting.

Re-rendered `B06_MycroftRealWorldNote` directly via `manim` a third time (bypassing `run.sh`
entirely throughout this whole cycle, consistently avoiding the documented shared-`clips/`-cache-
reversion side effect), confirmed its raw duration now matches landscape's exactly
(32.041667s via `ffprobe`), then rebuilt the vertical final master directly via `compile.py`.

**Both final masters confirmed, this time including an explicit cross-check the brief's hard
constraint actually requires (frame-exact duration parity, not just two independent GATE V
passes):**
- `deliverables/landscape/EmbeddingModelStaleness_SaiPranaviJ.mp4` — 3840x2160, 24fps, h264/aac,
  202.5s (4860 frames via `ffprobe -count_frames`). GATE V: 0 BLOCKER, 0 MAJOR.
- `deliverables/vertical/EmbeddingModelStaleness_SaiPranaviJ.mp4` — 2160x3840, 24fps, h264/aac,
  202.5s (4860 frames via `ffprobe -count_frames` — frame-exact match with the landscape master,
  not just a matching rounded-seconds duration). GATE V: 0 BLOCKER, 0 MAJOR.

Both independently re-verified against the TRUE final candidates (never the review slate), both
with real extracted frames personally inspected (not trusted from the automated gates alone) at
B02, B04, B06 (multiple times, across the full bug-fix cycle above), B07, B08, and B09. Nothing
inside `brutalist/` was modified. Nothing inside `mycroft` was modified (read-only reference).
Publishing not authorized — masters stay in this folder only, per `FELLOWS-SUBMISSION.md`.
