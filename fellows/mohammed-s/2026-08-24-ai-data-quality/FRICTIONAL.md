# FRICTIONAL — The Rule, Not The Report.

- **Folder:** `2026-08-24-ai-data-quality` · reporting week **2026-08-24 → 2026-08-30**
- **Dates inside this folder's artifacts:** first build 2026-08-30 · both 4K masters QC-passed 2026-08-31
- Append dated entries below; never rewrite an earlier one.

---

## Entry — week of 2026-08-24 · written later, on 2026-10-28

> Reconstructed after the fact from the files in this folder, not written at the time.
> Drafted with Claude Code from those files; reviewed and confirmed by Mohammed on 2026-10-28.

**1. Date and what I was working on**
- A 3:07 explainer on how AI manages data standards and data quality: AI's real job is
  proposing, evidencing and maintaining *rules*, with a human ratifying each one.

**2. What I tried, and what I expected**
- One fictional warehouse as a declared worked example across 12 beats, plus seven new
  illustration components. Both aspects at 4K.
- Expected the house Gate V run to tell me whether the master was clean.

**3. Where it resisted, and what I did next**
- **My own arithmetic was wrong.** The first draft said ~11 person-years to write the rules
  by hand; 3,988 × 40 min is ≈ 332 working days (≈ 1.3 person-years). Fixed, and the
  multiplication was put on screen so a viewer can check it.
- **Gate V reported 24 BLOCKERs on 24 frames.** The uniformity was the tell: the gate prefers
  the review (`-slate`) cut, whose timecode sits outside title-safe. Cropping the same corner
  from both cuts proved it. Re-run against the master → 0 BLOCKERs.
- Previewing stills before rendering caught two BLOCKERs (scenes laid out against the wrong
  box; B02's closing line clipped), each of which would have cost a full render.
- A 9:16 collision in B07 that the gate scored clean — found by reading the frame.
- Two killed compiles left truncated mp4s that looked finished; extended `verify_clips.py`
  to probe the masters.
- The compile was blocked by the branding rule because the reel declared another
  channel's brand key; changed to `claude-hussain`.

**4. What Claude or another person contributed — accepted, changed, rejected**
- Claude built the scenes, scripts and QC passes; I authorised the build (GATE P, 2026-08-30).
- Rejected: any "AI fixes your data automatically" framing, ROI figures, model-version claims,
  and a green success tick (it would have broken the single-accent rule).

**5. What I understand now, and what I still do not**
- Understood: a 98.7% quality score can measure presence and type, not meaning — six
  spellings of one country all pass. The test: *can this rule fail a row, and does that
  failure reach a person?*
- Understood: check which file a QC gate actually ran on before believing it.
- Open: the 9:16 cut is 3:07, over YouTube's Shorts cap; no true Short exists yet.

**Evidence in this folder**
- [`qc/VISUAL-QC.md` — three-pass QC record, final verdict PASS](qc/VISUAL-QC.md) · [`916/qc/REPORT.md`](916/qc/REPORT.md)
- [`FACTCHECK.md` — the 11 person-years correction](FACTCHECK.md) · [`README.md` — change notes 2026-08-30/31](README.md)
- [`verify_clips.py`](verify_clips.py) · [`916/qc/contact_sheet.png`](916/qc/contact_sheet.png)
