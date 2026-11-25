# BUILD-LOG — How RAG Works

## 2026-11-22 — planning (planning session for film #7; stops at the narration gate)
- **Choices made by the human:** the topic (how RAG works), the skill (`show-tell`), and the branding (default claude-liam / @NikBearBrown: Liam in for Bear, Kokoro `am_onyx`, Claude palette, locked `ClaudeTitleOutro`).
- **Title and slug:** "How RAG Works", slug `show-tell-how-rag-works`. The outro reads "How RAG Works. At Nik Bear Brown."
- **Greeting:** "Hallo" (on the SKILL's clean-greeting list).
- **Spine:** BIDEA → BDEFS → B00 hero (box of documents) → B01 opens (three pages) → B02 chunk → B03 embed → B04 store → B05 question embedded → B06 retrieve (card `search`) → B07 into the prompt → B08 grounded answer → B09 where it fails (card `tabs`, executed) → B10 confident wrong answer → B11 the fix → B12 why now (attributed: 21M passages, Lewis et al. 2020) → BHTF → BOUT.
- **Size:** 17 beats, 13 of them body beats; 2 cards (15%, under the one-third ceiling); 649 words.
- **Estimated length:** about 185 s (3:05) at 3.5 words/s, or about 250 s at pace_check's 2.6 words/s. The measured audio decides.
- **Evidence:** `demo/rag_demo.py` was executed. It is deterministic TF-IDF cosine in numpy, with no models, no APIs and no randomness. It covers three runs: the handbook; the handbook plus a stale 2019 FAQ page; and the stale page removed. Its self-checks assert every ranking claim the film makes. `make_sheet.py` reads every number from `evidence.json` and asserts the ranking IDs.
- **DOUBLE-CHECK corrections:** four, in FACTCHECK rows 9, 20, 21 and 25:
  - "different words" became "key words";
  - the stale chunk no longer announces "Old";
  - "answers fourteen days" became "can answer fourteen days";
  - "searched … this way" was dropped, because Lewis et al. used a dense retriever.
- **Pronunciation (`--phonemize`):**
  - RAG → ɹˈæɡ ("rag", the usual reading).
  - embedding → ɛmbˈɛdɪŋ; FAQ → ˌɛfˌeɪkjˈuː; Hallo → hˈæloʊ.
  - No `metadata.pronounce` override is needed (`pronounce: {}`, with the result in `pronounce_note`).
  - Whisper-check BDEFS ("RAG, retrieval-augmented") and B12 ("twenty-one million") after audio.
- **Library-first** (`scene_search.py … --no-log`), six queries: RAG pipeline, vector store, ranked search results, chunking, prompt context, before/after ranking.
  - The leads were CwcMemoryRetrieval, CwcMemorySchema, EnterpriseSearchDesign, CCHarnessMap and TtCorrection. All are fixed-content figures in other skins (props are `sparkLine` only, or reel-specific).
  - None can show this film's executed data, and SKILL forbids Remotion text cards other than `ShowTellCard` in a show-tell body. No miss was logged, because `--no-log` was used.
  - Retrieval is covered by the `ShowTellCard` kinds `search` (B06) and `tabs` (B09).
- **Props chosen:**
  - From `iso_kit`: box, open_box, tape, page, paper/scribbles, and a dark model block.
  - From the approved originals-25: `checkpoint-scanner` (B03, B05), `conveyor` (B03) and `memory-drawers` (the vector store, B04 onward).
  - Considered and not used: `context-crate` (the kraft box already is the crate) and `evidence-binder` (would compete with the pages).
- **Gates run:**
  - `runtime/scripts/bookend_check.py` PASS (exemptions `cold-open`, `bvdt` declared with a reason).
  - `runtime/qc/beat_lint.py` clean.
  - `runtime/qc/factcheck_check.py` clean (28 rows, 17 beats covered).
- **Not done (by design, this session):**
  - no audio, no `scenes.py`, no rendering;
  - no `./art run` or `final`;
  - nothing written under the toolkit;
  - nothing published.
- **Status:** waiting for narration approval (GATE P). Then GATE 0 (audio), run by the main session.

## 2026-11-22 — GATE P: narration approved
- The user approved the narration as drafted in the main session with the words "approve all six" (relayed by the main session, which asked this session to build audio, `scenes.py` and low-res previews, and to stop before any 4K render).
- Scope for this pass: Kokoro audio → `pad_silence.py` → whisper check → `align.py` → card `durationSeconds` → `scenes.py` → Gates A/W/B per scene → `-ql` previews in scratch. No 4K, no `remotion_scenes.py`, no `./art run`/`final`.

## 2026-11-22 — GATE 0 audio, scenes.py, low-res previews (stopped before 4K)
- **Audio:** `generate_audio_kokoro.py` (am_onyx), all 17 beats, then `stem-films/tools/pad_silence.py` (BIDEA +0.8 s lead, BOUT +1.0 s tail).
- **Whisper check** (faster-whisper base, word diff vs `narration_text`):
  - **Real mispronunciation found:** espeak spells "RAG" letter by letter in context (ˌɑːɹɹˌeɪdʒˈiː); whisper heard "R.A.G." in B12 and BOUT and "Ragee" in B01. My planning note ("no override needed") was wrong, because it phonemized "RAG" on its own.
  - Fixed with `metadata.pronounce = {"RAG": "ɹˈæɡ"}` in both `make_sheet.py` and `beat_sheet.json`. Regenerated `--only B01 B12 BOUT`, re-padded, and re-checked: B01, B12 and BOUT now transcribe as "Rag", ratio 1.000. BDEFS already said "rag".
  - The remaining diffs are not mispronunciations: digit normalisation (0.58, 21, 2020), Hallo→hello, four→for, Nik→Nick, and B11 "The fix is in the store" → whisper base "The fixes in the store are". The last is a whisper-base mishearing, but it should get a human listen.
- **Measured audio:** 200.30 s total (3:20). By beat (s):

  | BIDEA | BDEFS | B00 | B01 | B02 | B03 | B04 | B05 | B06 | B07 | B08 | B09 | B10 | B11 | B12 | BHTF | BOUT |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | 10.08 | 14.76 | 9.13 | 10.18 | 10.88 | 13.95 | 10.05 | 9.26 | 15.28 | 10.92 | 10.35 | 14.38 | 11.58 | 10.33 | 13.44 | 21.85 | 3.88 |

- **Align:** `align.py` aligned 17/17 beats with 0 fallbacks → `mp3/words.json`.
- **Cards:** `durationSeconds` set from `actual_duration_s` (B06 15.28, B09 14.38). B09 `cues` recomputed from words.json: "so it now scores" lands at 0.568 of the beat, so the cue is 0.56 (clear of 45–55%).
- **Cards not rendered here (by instruction).** Risk to check at render: the `search` kind drops row 3 in at 0.44–0.54 of B06, inside GATE T's midpoint window.
- **scenes.py:**
  - Built from `iso_kit.py` (pasted) plus the `memory-drawers` original (pasted subset of `iso_originals_25.py`).
  - Timing helpers follow the backprop film: `_load` with REEL fallback, `cue()` on words.json, and a frame-quantised `Clock` with a built-in midpoint guard (no motion in 45–55% ± 0.22 s).
  - 11 drawn scenes: B00–B05, B07, B08, B10–B12.
  - Embedding strips draw the real TF-IDF weights: 29 slots, with non-zero slots printed from `rag_demo.build_store` / `embed_query`, inlined as `VEC`.
  - Every number is inlined and cross-checked against `evidence.json` when present.
- **Frame clock finding (measured):** Manim's `play()` gives ceil(run_time·fps) frames, but `wait()` *floors* it. The first previews ran 1.8–2.8% short because each `wait(frames/fps − 1e-6)` dropped a frame. `Clock.at` now calls `wait(frames/fps)` exactly; `play` keeps the −1e-6.
- **Gates per scene, all exit 0:** GATE A (isolated copy, `static_scene_check.py`), GATE W (`wcag_margin_check.py --quiet`) and GATE B (`manim_layout_audit.py --curve-strict`).
  - Fixed on the way: B05 "?" crossing the scanner arch, and the "question" label outside the safe area; B07 "prompt" label touching the sheet, and the question slip parked under the label.
- **Previews** (`manim -ql --fps 24`, media in scratch, outside the film folder). Clip vs audio:

  | Beat | B00 | B01 | B02 | B03 | B04 | B05 | B07 | B08 | B10 | B11 | B12 |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | Diff | −0.06% | −0.13% | −0.05% | −0.25% | −0.09% | −0.12% | −0.04% | −0.16% | −0.33% | −0.38% | −0.17% |

  None runs longer than its audio, so nothing gets centre-cut.
- **Hand QC** at 15/50/85/99% of every scene:
  - B01's open box was drawing its inner walls over its front faces; fixed with z-index.
  - B01 pages and labels overlapped the box; fixed with a smaller box and a higher page row.
  - B08/B10 thread and "source" label re-routed.
  - B05 question strip moved clear of its slip.
  - Final frames clean.
- **Not done:** no 4K render, no `remotion_scenes.py`, no `./art run` or `final`; nothing written in the toolkit. Gate B writes `layout_audit.md/json` and a Text-cache `media/texts/` into the film folder (no videos).

## 2026-11-22 — rule update from the main session: no terracotta arrows; GATE V underfill
- Backprop's final was blocked by GATE T §8.3, which read terracotta arrow tips as accent text (2.74:1). This film had no terracotta arrows. Its one arrow (prompt sheet → model, in B07, B08, B10 and B11) was deep kraft; it is now **INK**. It is also shortened to stop 0.37 units clear of the dark model block, so an ink tip never fuses with the block.
- **Remaining terracotta**, all filled or outlined shapes, never text or arrowheads:
  - B00 tape;
  - the returns-chunk dot;
  - the drawer lamps and the model lamp;
  - the question strip's dot;
  - the B10 ring;
  - the fresh cabinet dot in B12;
  - the B02 cut lines and B03/B05 scan lines. These are thin lines, but they are created and removed outside the midpoint guard window, so neither is on screen at the 50% frame.
- **GATE V underfill:** every drawn body beat (B00–B05, B07, B08, B10–B12) carries `qc.sparse_by_design` with the show-tell reason, as SKILL allows. B06 and B09 are full-frame `ShowTellCard`s, and BHTF/BOUT are house bookends, so none of them carries the waiver.
- Re-ran Gates A, W and B on all 11 scenes: all exit 0. Re-rendered the B07, B08, B10 and B11 previews: −0.04 / −0.16 / −0.33 / −0.38% against audio. Frames at 15/50/85/99% are clean.

## 2026-11-23 — fixes after the 4K build failed GATE V and GATE T (main session will re-run 4K)
1. **GATE V, B00 midpoint, low contrast (0.23 < 0.30).**
   - The dark model block and its "model" label now arrive at "Here, it's" (about 2.0 s). Before, they came at "The model never", which the midpoint guard pushed past 50%. The 50% frame now carries the dark block.
   - The floor shadow went from GHOST to BAR2 (#B4AFA6).
   - No terracotta was added.
2. **GATE T §8.6b, B06 `search` card (bordered result rows read as text runs enclosing the labels).** B06 is now a drawn Manim scene, `B06_Ranking`:
   - The question's real embedding strip sits on top, the three best chunks' strips below it, with dashed guides from the question's two non-zero slots.
   - Open grey score bars, with no rectangle around any text: 0.58 "within 30 days", 0.25 "one year warranty", and 0.00 "receipt and charger" (no bar, just a small grey dot).
   - The vector-store cabinet stands at right, and a check lands on the top row.
   - The ranking is asserted against `evidence.json` run A at import.
   - `beat_sheet.json`: `lane: "manim"`, `shot.type: "GRAPHIC"`, `shot.manim.class: "B06_Ranking"`, `qc.sparse_by_design`; the remotion block, `why_card` and the stale `build` / `render_duration_s` stamps were removed.
   - `make_sheet.py` is mirrored. It was NOT re-run, because the live sheet carries pad hashes and build stamps; its carry-forward now also keeps `audio_pad`.
   - Cards: 1 of 13 body beats (B09 `tabs`).
   - SHOTLIST, CHECKS-REPORT and SCRIPT updated.
3. **GATE T §8.1, the small answer card in B08/B10/B11 (dark squiggle read as a 36 px text run).** Answer-card squiggles are now soft grey (BAR1), like the slips on the prompt sheet.
4. **"illustrated" tag in B08/B10:** raised from 32 to 36.
- BDEFS (ClaudeDefinitions §8.1 at 40 px) was left alone, per the main session, which is fixing the component.
- **Stale renders moved** to `_superseded/2026-11-23-gateVT/`, so `art run` re-renders them:
  - `media/B06.mp4` (the old card, which would have outranked `manim/B06.mp4`);
  - `clips/B06.mp4`;
  - `manim/` and `clips/` B00, B08, B10, B11;
  - the `media/videos` Manim cache.
- **Gates on the changed scenes:** A (isolated copy), W and B exit 0 for B00, B06, B08, B10 and B11. bookend PASS, beat-lint clean, factcheck clean.
- **Previews (`-ql`), clip vs audio:** B00 −0.06%, B06 −0.20%, B08 −0.16%, B10 −0.33%, B11 −0.38%. Frames at 15/50/85/99% are clean.
- **One fix after the first look:** B06's zero-score stub bar read as part of "0.00", so it became a dot. Numbers and the check were spaced further apart.
- **Concurrency note:** my first write of B06 into `beat_sheet.json` (01:40) was reverted by another writer within seconds, probably the tail of the 4K build. I re-applied it at 01:41 and it has held since.

## Plan for the render session (design rules to honour)
1. **GATE A pre-flights `scenes.py` as an isolated copy.** Paste `iso_kit.py` and only the needed `make_original` rigs (from `iso_originals_25.py`) into `scenes.py`; never import them.
   - With no `beat_sheet.json` beside it, `until()` is a no-op, so every scene must still add a NEW shape after its first `play` (and a membership change after the first play: SKILL, B06 trap).
   - Evidence numbers must be inlined as constants with an `evidence.json` cross-check wrapped in `try/except` (Film 1's "isolated-copy data fallback"), so the stub run never needs the file.
   - Wrap `get_center()` results in `np.array`, write rig positions as fixed numbers, and use `VGroup(*…)` for slices.
   - Never use `ease_in_quad`, `ease_out_cubic` or `.animate(path_arc=…)`.
2. **Frame clock:** Manim renders ceil(run_time·fps) frames. Count each scene's frames as `ceil(run_time*24)` per `play`/`wait` so the clip lands within its `actual_duration_s`, with about 0.05 s slack. A clip longer than its audio gets centre-cut silently.
3. **GATE V fill:** content bbox ≥ 55% of the safe area. Body beats carry `qc.sparse_by_design` (underfill and clustered only), but aim to fill anyway:
   - B03, B07, B10 and B12 span the stage (belt, prompt plus model, cabinet rows);
   - the cast should be sized up (box height ≥ 3 units) so most beats fill without the waiver;
   - drop the waiver from any beat that measures ≥ 55% on its own.
4. **Text bounds:** keep every label within ±6.0 x / ±3.2 y. That is tighter than the SKILL's ±6.2 × ±3.3 and leaves margin for the layout audit, which measures on text bottoms. Type ≥ 32.
5. **Midpoint guard (GATE T / V sample at 50%):** nothing in flight between 45 and 55% of any beat, with a margin of about 0.22 s. Every drawn beat has an ink label up by its midpoint. Cards: B09's tabs switch cue is 0.565 (its rows settle by about 0.85); B06's search settles by 0.58 with type up by 45%.
6. **Terracotta** only for the tape, the cut line (B02, drawn in ink and ending in a terracotta dot if a midpoint trap appears), the drawer lamps, the question strip's dot and the B10 ring. Never for text or numerals ("30 days", "14 days" and "21M" are ink).
7. **"illustrated" tag** on B08 and B10 answer cards (FACTCHECK rows 17 and 21). It is small ink text, size ≥ 32.
8. **After audio:** write each card's `durationSeconds` from `actual_duration_s` (make_sheet carries audio forward if re-run; never re-run after `final`). Pad BOUT with 1.0 s, whisper-check BIDEA, BDEFS and B12, and recompute B09's `cues` if the measured phrase position moves it into the 45–55% window.

## 2026-11-23 — final (main session)
- **First 4K run failed four checks:**
  - GATE V B00 low contrast
  - GATE T §8.6b on the B06 ShowTellCard `search`: bordered rows enclosing labels were read as overlapping text runs
  - GATE T §8.1 on B08/B10/B11: a dark 36 px squiggle
  - GATE T §8.1 on BDEFS: 40 px
- **Fixes:**
  - The planning session fixed B00, redrew B06 as `B06_Ranking`, made the squiggles soft gray, and raised the "illustrated" tag to 36.
  - The main session fixed the toolkit component: `ClaudeDefinitions` meanSize 48→52.
- **Master:** `exports/landscape/show-tell-how-rag-works.mp4`, 3840×2160, 24 fps, 200.7 s.
  - SHA-256 `c6d79f493ef18ff2…`, which matches `.verified.json` (`ready`).
- **Checks on the master:**
  - GATE V clean, GATE T PASS.
  - Strip check PASS (100 samples), master check PASS, loudness PASS (−24.16 LUFS).
  - Hand QC: every beat at 15/50/85%.
- **Not published.**

## Format conversion → ai-explainer (2026-11-24)
- **Why:** the user asked for this film to match the other five (ai-explainer spine), with no footer.
- **Approval (GATE P, chat, 2026-11-24):** the user approved, as previewed, a new B00 cold open, a new B01 hesitant-writer BLUF and a new BVDT recap. The greeting is "Hello" (chosen for all three converted films).
- **Change:**
  - BIDEA (hesitant writer) and BDEFS (Terms) were retired to `_superseded/format-show-tell/`. Every term is defined inline in the body: chunk (B02), embedding (B03), vector store (B04). RAG is expanded in B01.
  - Body B00–B12 is unchanged in content. It is renumbered B10–B22 so the cold open can be B00. The mp3, manim, media and clip files, the scene class names, the Clock/cue ids and the words/timings keys were renamed together.
  - BVDT `ClaudeVerdictArtifact` is added before BHTF.
- **BVDT card:** a 5-line card measured 51% fill. A sixth recap line from the B22 body ("The 2020 paper that named it searched 21 million Wikipedia passages.") was added, which matches the six-line cards of the other ai-explainer films. The fill check was not waived. The 5-line clip is in `_superseded/bvdt_underfill/`.
- **FINAL (ai-explainer), 2026-11-24:** 216.1 s, 3840×2160. GATE V 0/0 (36 frames), GATE T PASS, bookend PASS, strip check 108/108, master PASS, −24.16 LUFS. sha256 86ea9132db8987ef4abc4e74396884f4f670f6b073e0d426046403ea30e61c06 matches .verified.json. Hand QC of all 18 beats is clean; the renumbered body renders as before. Copied to the user's "Footer removed" folder. Remotion stays at 4.0.535, the version all eight films used.
- **Docs refreshed (2026-11-24):**
  - SCRIPT.md, SHOTLIST.md and CHECKS-REPORT.md were regenerated from the current beat sheet with `stem-films/tools/refresh_converted_docs.py`. Each keeps its pre-conversion content verbatim under a History heading. The originals are backed up in `_superseded/format-*/docs/`.
  - FACTCHECK.md has a dated conversion section appended that checks every new spoken and on-screen line; the earlier rows are unchanged.
