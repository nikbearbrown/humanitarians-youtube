# Process Notes — Prefill vs. Decode
Video Link: https://drive.google.com/drive/folders/1dNRtEobtVoOo96AsAAauUyMaR99WWjsT?usp=sharing


## Research
Primary sources: Sarathi-Serve (arXiv:2403.02310, OSDI 2024) for the compute-bound/memory-bound framing, chunked-prefill + stall-free scheduling, and the 2.6×–5.6× capacity numbers; DistServe (arXiv:2401.09670, OSDI 2024) for the TTFT/TPOT measurement framing, prefill-decode interference on shared hardware, and the 7.4×/12.6× disaggregated-serving numbers.

## The diagram back-and-forth
First draft of the script reused existing text-card components — `TwoWayCompare` for the prefill "structure" beat, `RouterFlow` for the decode "structure" beat. Both were factually fine but not actual diagrams: no fan-in/fan-out shape, no loop-back shape. Went through two rounds of misreading what "include diagrams" meant (first as "send visual previews as separate files," then as "embed those images in the script doc") before the user's explicit "i mean diagram in the video like uml diagrams etc" clarified the real ask: genuine box-and-arrow, architecture-style diagrams that appear on-screen in the finished video, not text cards mislabeled as diagrams.

Re-ran GATE L specifically scoped to that gap — confirmed nothing in the shared component library draws fan-in/fan-out around a central block, or a feedback/loop-back arrow — and authored two new components:

- **`ParallelPass`** for B02: input token boxes converge into one wide "pass" block, which fans back out into the KV-cache and first-token outputs. This is prefill's real computational shape — many tokens in, one simultaneous pass, a couple of things out.
- **`AutoregressiveLoop`** for B04: three boxes in a row (in → pass → out) with straight connecting arrows, and a curved SVG path looping from the last box back to the first — plus a KV-cache row underneath that fills in one block per cycle, newest block always highlighted terracotta. This is decode's real computational shape — a closed loop, not a forward-only list with a text "repeat" label.

Both components hit FILL-THE-CANVAS violations on first render (excess dead space in the lower half of frame) — fixed by rescaling vertical proportions for the pass/output blocks and the loop arc/cache row, re-rendered, confirmed clean on the second pass.

## Build log
- Beat sheet: 12 beats (B00–B11), built via `build_prefill_decode_sheet.py`, narration copied verbatim from the finalized script.
- Audio: Kokoro `af_bella`, all 12 beats generated in one pass, ground-truth total 242.05s (~4:02) — the beat sheet's word-count estimate had been 289.6s, so actual runtime came in noticeably shorter, as usual.
- Render: all 12 beats rendered individually via `remotion_scenes.py`, one call per beat. Both new components (`ParallelPass` at B02, `AutoregressiveLoop` at B04) rendered correctly in the full compiled context, matching their isolated QC stills.
- Compile: single 16:9 cut at `--height 2160` → 3840×2160, 242.03s final, 10,956,568 bytes.
- Motion histogram flagged `illustrate` at 7/12 beats (58%, over the ~40% pantry-cap guideline) — informational only, not blocking; the beat mix here is inherently illustration-heavy (two new diagrams plus fact stacks and finding pairs) for a mechanics-focused explainer.
- QC: sampled the midpoint of all 12 beats across the compiled master and read every frame — all clean, no defects, both new diagram components confirmed correct in situ.

## Scope note
Only a 16:9 cut was built this pass, matching the script's own stated scope ("single 16:9 cut... a 9:16 Shorts derivative can follow if a full build is wanted later"). No Shorts derivative requested this time — flagged as a possible follow-up if wanted.
