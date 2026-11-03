# BUILD-LOG

- 2026-09-28 — Brief: 60 s, 12 beats, am_onyx, native 16:9 + 9:16 as separate outputs, fixed opening line, review cut only.
- Branding: "Ciao, Likhith"; @HumanitariansAI (claude-hai, kicker "Irreducibly Human", Plain); HAI outro via JevOutro. Outro title restated as "How KV Caching Speeds Up LLMs." (the short "KV Caching." underfilled the card, Gate V MAJOR).
- Measured 65.2 s audio / 65.4 s cut (trimmed from 73.3 s in two passes; stopped rather than cut teaching content — duration is an output). Body narration 10–17 words/beat (justified: 12 beats in ~60 s).
- Evidence: evidence/kv_cache_toy.py (numpy, seed 7) — cached ≡ uncached to 4.44e-16; counts shown in B07, bytes in B08. Math: typeset_math.py SVG rows (matplotlib added to local .venv).
- New components: runtime/remotion/src/KvCache.tsx (7 scenes × 16:9 + 916), registered in Root.tsx, scene-index rebuilt.
- Fixes during QC: sheet needed props.durationSeconds (renders were running on default length — spark lines/reveals never landed); B01 trigger must be per-word ("computing, faster" → "reusing, work"); B05 cache outline crossed SAFE; B05 label fade at 50%; B07 ratio shown exactly (500.5×, not rounded 501×); B08 tick labels wrapped; portrait B01 clipped → 4-line restack; portrait B03 counter/spark collision; portrait B04/B05 fill.
- 16:9 review: claude-hai-kv-caching-slate.mp4 — 3840×2160, 65.4 s; GATE F/L/V pass (V 0/0).
- 9:16 review: vertical/claude-hai-kv-caching-vertical-slate.mp4 — 2160×3840, compiled --height 3840; all 12 beats native <Pattern>916. GATE V on the label-free portrait scene join 0/0. The compiled 9:16 review file itself trips GATE V edge-bleed on the burned-in review label (same toolkit issue as the Jev/SDD reels).
- Likhith reviewed both review cuts and signed off (FACTCHECK.md status, first person).
- GATE T fixes before the masters (visual polish only, narration and audio unchanged):
  terracotta text → ink in B05/B08 (§8.3); pause/memory bars made thin solid accent bars (B02/B08);
  B06 labels enlarged, "mat" enlarged, equation simplified to o_t = softmax(q_t Kᵀ/√d) V with note
  "K and V: read from the cache" (§8.1 subscripts, §8.5 wordy note); B10 output line reworded
  ("your numbers, plugged into the formula", §8.9). Portrait-only: B05 labels merged into
  "✓ kept in memory, not recalculated", spark "Stored, then reused." (portrait §8.1 floor is 72px @3840).
- 16:9 master: renders/H-KVCaching_LikhithR.mp4 — 3840×2160, 65.4 s; GATE T PASS, GATE V 0/0.
- 9:16 master: renders/V-KVCaching_LikhithR.mp4 — 2160×3840, 65.4 s; GATE T PASS, GATE V (label-free scenes) 0/0.
- Runs need the local .venv on PATH (system python3 lacks Pillow): PATH="$PWD/.venv/bin:$PATH" ./art final <reel>.
- **Gate restored, outro replaced, disclosure added.** `runtime/scripts/type_check.py` restored to the unmodified toolkit version (an exemption list had been added that skipped contrast checks for several scenes, including the old JevOutro). Re-checked against the original gate and fixed: B11 now uses the default dual-aspect `HaiOutro` (darker #A44A32 Subscribe pill, full-size HAI mark); no scene fixes needed beyond the outro; B01 hesitant-writer accent passed as #A44A32. AI narration now disclosed on screen (B00 first result line, B11 note: "Narrated by an AI voice (Kokoro am_onyx), not Likhith.").
- Result: GATE T PASS (original checker) on 16:9 and 9:16; GATE V 0/0 on the 16:9 review and every 9:16 scene frame. `./art final` re-exported both masters with `ready` receipts: renders/H-KVCaching_LikhithR.mp4 (3840×2160, sha256 b58d5a7668b6…) and renders/V-KVCaching_LikhithR.mp4 (2160×3840, sha256 a80e8afd13df…).
