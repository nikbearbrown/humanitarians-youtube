# FRICTIONAL — Cortex, In The Warehouse.

- **Folder:** `2026-09-28-snowflake-cortex-triage` · reporting week **2026-09-28 → 2026-10-04**
- **Dates inside this folder's artifacts:** fact-check 2026-09-20 · build 2026-09-21 ·
  portrait fill pass and 9:16 rebuild 2026-10-07
- Append dated entries below; never rewrite an earlier one.

---

## Entry — week of 2026-09-28 · written later, on 2026-10-28

> Reconstructed after the fact from the files in this folder, not written at the time.
> Drafted with Claude Code from those files; reviewed and confirmed by Mohammed on 2026-10-28.

**1. Date and what I was working on**
- A 1:59 reel on one starter use case for Snowflake Cortex: triaging 40,000 support tickets
  in SQL with `SENTIMENT`, `SUMMARIZE` and `CLASSIFY_TEXT`, without the text leaving the warehouse.

**2. What I tried, and what I expected**
- Five new `Cortex*` components, each reflowing natively for 9:16.
- Expected both masters to pass the house gate and be promoted through `./art final`.

**3. Where it resisted, and what I did next**
- Renders were trimmed to audio length, silently cutting late motion (B02's `COUNT(*) = 40,000`
  never appeared) → wrote `durationSeconds` onto every beat.
- Three portrait components had fixed durations; B09 would have lost 5 s → added the audio-clock contract.
- Title-safe and overflow BLOCKERs (spark line, B10 title clipped mid-word, B06 cards dropping a column) — all fixed.
- B01's on-screen correction never fired: the writer matches triggers against single
  tokens, so multi-word triggers can never match. Rewritten as single-word swaps.
- **Hit a conflict between two rules:** B01 must be a progressive typing beat, and Gate V
  wants 55% fill at the mid-beat sample. Both cannot hold. `build-state.json` records the
  gate failing on 2026-09-21. On 2026-10-07 a portrait fill pass took 9:16 from 7 → 3 MAJOR.
- The masters were assembled from the compiler's own conformed clips, **not** promoted
  through `./art final`. They have not passed the house gate; that call is still open.

**4. What Claude or another person contributed — accepted, changed, rejected**
- Claude built the components and ran the frame-by-frame QC.
- GATE P was signed "by standing authorization given in the build session".
- Deliberately excluded model names, prices, credit rates, region lists and accuracy numbers — they date.

**5. What I understand now, and what I still do not**
- Understood: Cortex functions are billed per token, so the `WHERE` clause in B05 is the cost control.
- Open: the reel was scripted from working knowledge, not a live docs fetch — the four ✅ claims
  must be re-checked against `docs.snowflake.com` before publishing.
- Open: whether to promote the masters, lower `--fill-min`, or rework beat 2.

**Evidence in this folder**
- [`QC-STATUS.md` — defects found and fixed; portrait fill pass 2026-10-07](QC-STATUS.md)
- [`FACTCHECK.md` — checked 2026-09-20](FACTCHECK.md) · [`CHECKS-REPORT.md`](CHECKS-REPORT.md) · [`build-state.json` — gate failure 2026-09-21](build-state.json)
- [`PEDAGOGY.md`](PEDAGOGY.md) · [`PROMPTS.md`](PROMPTS.md)
